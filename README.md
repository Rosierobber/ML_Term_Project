# ML_Term_Project
# Learning on temporal graphs: do complex models beat simple memory?
Background: 
Transactions, messages, reviews and flights form graphs that change every second. Temporal graph
networks such as TGN are built for this, but the Temporal Graph Benchmark (Huang et al., NeurIPS
2023) showed that a simple memorisation heuristic, EdgeBank, is surprisingly hard to beat on some
datasets, and that random negative sampling had made earlier results look better than they were.
Research Questions
1. RQ1: How do TGN, DyRep and GraphMixer compare with EdgeBank under TGB's realistic
negative sampling?
2. RQ2: On which kinds of graphs (recurring vs novel edges) do learned models help most?
3. RQ3: How do training cost and memory scale from a small to a medium TGB dataset?
Benchmark and Data

Temporal Graph Benchmark (Huang et al., NeurIPS 2023 Datasets and Benchmarks), Python package py-
tgb. Use tgbl-wiki (small) and tgbl-review or tgbl-coin (medium) for dynamic link prediction, with the
official splits, negatives and MRR evaluator.
Baselines to Reproduce: 
Baselines: EdgeBank (both variants), TGN, DyRep and GraphMixer, using the TGB or DyGLib
implementations. At least 3 seeds per model.

Page 9 of 11
Direction for Your Contribution
Propose and test one change, for example combining EdgeBank's memory with a learned model, a
recency-aware negative sampler for training, or a lighter memory module that keeps MRR at lower cost.
Sections Your Paper Must Contain
1. Introduction: dynamic graphs in finance, social media and e-commerce
2. Related work: continuous-time temporal GNNs and evaluation pitfalls
3. Problem formulation: dynamic link prediction and the MRR metric
4. Datasets: statistics and novelty/recurrence of edges
5. Proposed method: your modification, with a diagram
6. Experimental setup: official splits, negatives, seeds, hardware
7. Results: MRR per dataset, mean ± std over seeds
8. Cost analysis: training time and memory
9. Discussion: when memorisation is enough, threats to validity
Watch Out For
Use only TGB's official negative samples and evaluator. Self-made random negatives are exactly the flaw
TGB was built to remove.
Anchor Reference
• S. Huang et al., "Temporal graph benchmark for machine learning on temporal graphs," in
Advances in NeurIPS, Datasets and Benchmarks Track, vol. 36, 2023.

Term project, Advanced Machine Learning (MSCS, Fall 2026), Kinnaird College for Women.
Author: <Rabia Habib, F26MPCS005> | Instructor: Dr. Sidra Zafar

## 1. Overview
Do complex temporal graph models beat simple memory under TGB's realistic
evaluation? This repository contains code to (a) reproduce published baselines
on the Temporal Graph Benchmark (TGB) and (b) evaluate my proposed
contribution: TODO (one sentence describing your method).

## 2. Repository structure
```
configs/      # hyperparameters per model/dataset
scripts/      # training and evaluation scripts
results/      # per-seed CSV files (one row per run)
logs/         # raw logs, hardware and version info
reproduce_main_table.sh   # TODO: regenerates the main results table
requirements.txt
```
## 3. Setup
```bash
conda create -n tgb python=3.9 -y && conda activate tgb
pip install -r requirements.txt
```
Software versions: Python TODO, PyTorch TODO, PyG TODO, py-tgb TODO.
Hardware: TODO (GPU model, memory, CPU, RAM).

## 4. Data
Datasets: tgbl-wiki (small) and TODO (medium) from TGB. They download
automatically on first run with TGB's official splits and official negative
samples. I use only TGB's official negatives and MRR evaluator.
Datasets are used under their own licences (see the TGB paper, Appendix B).
Data is not redistributed in this repository.

## 5. Baselines
EdgeBank (tw and infinite), TGN, DyRep, GraphMixer, using TODO (TGB examples /
DyGLib). Reused code is in `third_party/` or marked in commit history; my
changes are in `src/` (TODO).

## 6. Proposed method
TODO: short description and where it lives in the code.

## 7. Running experiments
```bash
# example: TODO replace with your actual commands
python scripts/run.py --model tgn --dataset tgbl-wiki --seed 1
```
Seeds used: TODO (for example 1, 2, 3). EdgeBank is deterministic.
Hyperparameters were tuned on validation data only; the test set was used
once for the final numbers.

## 8. Reproducing the main results table
```bash
bash reproduce_main_table.sh
```
Expected output: TODO (table of test MRR, mean ± std over seeds).

## 9. Results
TODO: paste your table (mean ± std over 3+ seeds) and compare with published
TGB numbers.

## 10. Compute report
TODO: training time, GPU hours, parameter count, peak memory per model.

## 11. Citation and acknowledgements
This work uses the Temporal Graph Benchmark:
S. Huang et al., "Temporal graph benchmark for machine learning on temporal
graphs," NeurIPS Datasets and Benchmarks Track, vol. 36, 2023.
Official code: https://github.com/shenyangHuang/TGB
TODO: add DyGLib / other reused repositories.

## 12. AI use
TODO: state which tool, what for, and what you changed (same as the paper).
