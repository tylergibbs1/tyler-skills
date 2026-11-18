# Rented compute guardrails

Quote these rules in full in every brief for an agent that may create cloud GPU pods.
Fill in the numbers the user gave you; never invent a budget.

## Before creating a pod

1. Check the price of the exact GPU type and cloud tier first. Never create one at or
   above the user's per-GPU cap. If you created one by mistake, delete it immediately
   and report it.
2. Check the account balance. Do not create pods below the floor the user set (leave
   room for other running agents).
3. Count pods already running for this bet against its pod cap.
4. Name pods with a per-bet prefix so agents never touch each other's pods.

## While running

- **Training runs on GPU.** Check the device flag in every training command. CPU is
  fine for data prep, scoring, physics and analysis, not for training.
- **CPU-bound work on GPU pods:** simulators are often single-threaded. Shard episodes
  across all CPU cores in one pod (one process per core) before renting more pods, and
  check results match a serial run on a small sample.
- Keep code, weights and data on a network volume or image so a pod is ready in about a
  minute instead of re-uploading each time.
- Write results to disk continuously and copy them off the pod as they land.

## Tearing down

- Delete each pod the moment its work ends or stalls, then confirm with a pod listing.
- Report pod-hours and cost in the final reply.
- If an agent dies mid-run, the next agent first inspects running pods and jobs,
  fetches finished results, deletes idle pods, and only then reruns missing work.

## Long local jobs

Wait on a PID or a done-file with a timeout. `until ! pgrep -f NAME` matches its own
shell and never exits.
