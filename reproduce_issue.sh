# this will reproduce the issue with resuming temporary checkpoints
dvc exp run --temp
rm dvc.lock # remove the changes from the workspace to simulate a clean environment

# re-run from the earlier experiment. 
# Expection: This should resume counting from 3 and immediately exit
# Behaviour: This experiment starts counting from 0 again
dvc exp run --temp --rev $(dvc exp list --names-only)