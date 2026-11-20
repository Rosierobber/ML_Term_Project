"""
Dump EdgeBank scores per query (1 positive + its negatives) for tgbl-wiki val and test.
Adapted from third_party/TGB/examples/linkproppred/tgbl-wiki/edgebank.py (TGB, Huang et al., 2023).
Change: scores are saved, not only the MRR. Val then test run in sequence with one EdgeBank object.
"""
import argparse, math, os, numpy as np
from tqdm import tqdm
from tgb.linkproppred.evaluate import Evaluator
from tgb.linkproppred.dataset import LinkPropPredDataset
from tgb.utils.utils import set_random_seed
from modules.edgebank_predictor import EdgeBankPredictor

p = argparse.ArgumentParser()
p.add_argument("--mem_mode", default="unlimited", choices=["unlimited", "fixed_time_window"])
p.add_argument("--time_window_ratio", type=float, default=0.15)
p.add_argument("--bs", type=int, default=200)
p.add_argument("--out", required=True)
a = p.parse_args()
set_random_seed(1)
DATA = "tgbl-wiki"
dataset = LinkPropPredDataset(name=DATA, root="datasets", preprocess=True)
data, metric = dataset.full_data, dataset.eval_metric
train_mask, val_mask, test_mask = dataset.train_mask, dataset.val_mask, dataset.test_mask
edgebank = EdgeBankPredictor(data["sources"][train_mask], data["destinations"][train_mask],
                             data["timestamps"][train_mask], memory_mode=a.mem_mode,
                             time_window_ratio=a.time_window_ratio)
evaluator, neg_sampler = Evaluator(name=DATA), dataset.negative_sampler
os.makedirs(a.out, exist_ok=True)

def run(mask, split_mode):
    S, D, T = data["sources"][mask], data["destinations"][mask], data["timestamps"][mask]
    flat, lens, mrr = [], [], []
    for b in tqdm(range(math.ceil(len(S) / a.bs))):
        s, e = b * a.bs, min((b + 1) * a.bs, len(S))
        ps, pd, pt = S[s:e], D[s:e], T[s:e]
        for i, neg in enumerate(neg_sampler.query_batch(ps, pd, pt, split_mode=split_mode)):
            qs = np.array([int(ps[i])] * (len(neg) + 1))
            qd = np.concatenate([np.array([int(pd[i])]), neg])
            y = np.asarray(edgebank.predict_link(qs, qd), dtype=np.float32)
            flat.append(y); lens.append(len(y))
            mrr.append(evaluator.eval({"y_pred_pos": y[:1], "y_pred_neg": y[1:], "eval_metric": [metric]})[metric])
        edgebank.update_memory(ps, pd, pt)
    np.savez(f"{a.out}/edgebank_{a.mem_mode}_{split_mode}.npz", flat=np.concatenate(flat), lens=np.array(lens))
    print(f"{a.mem_mode} {split_mode}: queries={len(lens)} MRR={np.mean(mrr):.4f}")

dataset.load_val_ns();  run(val_mask, "val")
dataset.load_test_ns(); run(test_mask, "test")
