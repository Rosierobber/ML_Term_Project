# TGN, tgbl-wiki, seed 1: first attempt (not pushed)

Same command and settings as the pushed run (seed 1, num_run 1, defaults).
The push was rejected (remote ahead), the session was later restarted, and the
raw log file was not saved to the repo. Numbers below were copied from the
notebook output printed at the time.

- stopped at epoch 18 (early stopping), best validation epoch 13
- best validation MRR: 0.3723
- test MRR: 0.3063
- train+validation time: 1673.1 s, test time: 79.1 s

The run stored in results/seed1_TGN_tgbl-wiki_results.json (test MRR 0.3469)
was produced afterwards with the same seed and settings.
