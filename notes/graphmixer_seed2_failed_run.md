# GraphMixer tgbl-wiki, seed 2: run that did not train

- Seed 2 (GPU 1): train ROC AUC 0.5001, train AP 0.5001, val/test MRR 0.0020.
- Check run, seed 2 on GPU 0 (first 200 batches only, stopped, not saved as a result):
  training losses at batches 1, 50, 100, 200 identical to the original run
  (0.7142066955566406, 0.7137110829353333, 0.7132154703140259, 0.7122503519058228).
- So the failure repeats on a different GPU; it is tied to this seed, not to GPU 1.
- Cause not identified.
- Rule fixed before running further seeds: a run counts as failed if train ROC AUC < 0.55
  after the epoch. All runs are reported; headline statistics use non-failed runs.
