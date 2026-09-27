# SANDBOX ONLY - THROWAWAY

This repository is a throwaway proof harness for Saiyan-ECAD Gate-12
(CI + repository-ruleset end-to-end evidence).

- It contains NO real ECAD data - only a synthetic acceptance matrix,
  a toy pytest, and reference copies of the proposed CI workflow and
  ruleset that mirror the real lane's semantics at reduced scale.
- GitHub-hosted enforcement was ATTEMPTED here and BLOCKED:
  `POST /repos/.../rulesets` -> HTTP 403 "Upgrade to GitHub Pro or make
  this repository public to enable this feature." (private-repo plan gate)
  `PUT .../branches/main/protection` -> same HTTP 403.
  The credential in use also cannot write `.github/workflows/*` (404),
  so no GitHub-hosted Actions run could be created.
- The end-to-end proof therefore runs as a LOCAL dry-run of the same
  ruleset semantics (bare repo + emulating update hook + local execution
  of the exact CI steps); see the gate-12 lane artifacts.
- Nothing here applies to `dakuwonmoody-lab/Saiyan-ECAD`.
- Safe to delete at any time. Created 2026-09-27 by Glint (Worker B,
  Gate-12 sandbox proof lane).
