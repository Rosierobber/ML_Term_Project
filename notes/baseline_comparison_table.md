| Model | Published val | Published test | My val | My test | n | Test gap / published std |
|---|---|---|---|---|---|---|
| EdgeBank_inf | 0.527 | 0.495 | 0.5267 ± 0.0000 | 0.4947 ± 0.0000 | 3 | n/a (deterministic) |
| EdgeBank_tw | 0.600 | 0.571 | 0.5997 ± 0.0000 | 0.5710 ± 0.0000 | 3 | n/a (deterministic) |
| TGN | 0.435 ± 0.069 | 0.396 ± 0.060 | 0.3852 ± 0.0086 | 0.3328 ± 0.0124 | 3 | -1.05 |
| DyRep | 0.072 ± 0.009 | 0.050 ± 0.017 | 0.0508 ± 0.0199 | 0.0399 ± 0.0143 | 3 | -0.60 |
| GraphMixer * | 0.113 ± 0.003 | 0.118 ± 0.002 | 0.1278 ± 0.0513 | 0.1255 ± 0.0516 | 4 | +3.75 |

Published values: Huang et al., NeurIPS 2023 D&B, Table 2a (tgbl-wiki, 5 runs).
Mine: TGB default settings and official evaluator/negatives. EdgeBank is deterministic (3 seeds, identical results).
TGN and DyRep: seeds 1-3. "My val" for TGN/DyRep is the best validation epoch; for GraphMixer it is the single epoch's validation MRR.
* GraphMixer: fpour/TGB_Baselines (DyGLib-based), 1 epoch per seed (limited budget), seeds 1-5. Seed 2 did not train
  (train ROC AUC 0.50, test MRR 0.002) and is excluded from this row; it is reported in results/graphmixer_wiki.csv.
  All 5 runs: test MRR 0.1008 ± 0.0710. The published std for GraphMixer (0.002) is much smaller than the spread
  across my runs, so the gap column is not meaningful for this row.
