# Gate-12 hosted sandbox proof — TEST LOG

Date: 2026-09-27. Sandbox: `dakuwonmoody-lab/ecad-gates-ci-sandbox` (public; disposable).
Production repo `dakuwonmoody-lab/Saiyan-ECAD` and `master` untouched.
Policy under test mirrors `proposals/ecad-acceptance-gates/gate-12/ruleset.json` from
`glint/ecad-gates-0712-evidence-20260927` (ffcbd080), with enforcement ACTIVE (proposal: disabled).

Active ruleset `gate12-two-reviewer-ci` (id 24078839) on `refs/heads/main`, no bypass actors:
- deletion, non_fast_forward
- pull_request: merge-only, 2 approving reviews, dismiss-stale-reviews-on-push,
  require-code-owner-review, require-thread-resolution
- required_status_checks: [`gates`], strict

CODEOWNERS (pre-existing): `sandbox-matrix.json` and `protected/` owned by @dakuwonmoody-lab.
PR #1 `gate12-pr1` -> `main` touches code-owned `protected/sensitive.txt`.

## Results

### S0-baseline — VERIFIED
- before/after: `568281a2` -> `568281a2`
- note: Sandbox disposable repo, public (required for rulesets on this plan). Disabled probe ruleset removed; zero rulesets before test.

### S1-policy-files — VERIFIED
- before/after: `568281a2` -> `ce80a33f`
- note: Workflow + test committed to main via Contents API with workflow-scoped PAT (pre-ruleset).

### S2-ruleset-v2 — VERIFIED
- before/after: `-` -> `-`
- note: Mirrors proposal ruleset.json values (2 approvals, dismiss-stale, code-owner review, thread resolution, strict checks); enforcement ACTIVE (proposal had disabled).

### T1-direct-push — VERIFIED
- before/after: `ce80a33f` -> `ce80a33f`
- note: Well-formed Contents-API file update on protected main denied by ruleset; main SHA unchanged.
- GitHub response (409): Repository rule violations found

Changes must be made through a pull request.

### T2-force-push — VERIFIED
- before/after: `ce80a33f` -> `ce80a33f`
- note: Force ref-update of main to older commit denied; main SHA unchanged.
- GitHub response (422): Repository rule violations found

Cannot force-push to this branch

Changes must be made through a pull request.

### T3-delete-branch — VERIFIED
- before/after: `probe-exists` -> `probe-exists`
- note: DELETE of probe branch while covered by deletion rule denied; branch survived. (DELETE of default branch main is refused by GitHub regardless of rulesets, so the rule was tested on a protected non-default branch; ruleset then restored to main-only and probe cleaned up.)
- GitHub response (422): Repository rule violations found

Cannot delete this branch

### T4-approval-count — VERIFIED
- before/after: `ce80a33f` -> `ce80a33f`
- note: PR #1 (head bed4a02c) merge attempt with 0 countable approvals rejected citing the 2-approval rule. Exact-1-approval boundary BLOCKED: only one GitHub identity exists (both supplied tokens are dakuwonmoody-lab); author self-approval is API-rejected 422 'Can not approve your own pull request'.
- GitHub response (405): Repository rule violations found

At least 2 approving reviews are required by reviewers with write access.

Required status check "gates" is failing.

### T5-stale-approval — BLOCKED
- before/after: `-` -> `-`
- note: Needs a 2nd distinct reviewer identity. With one identity no approval can exist to go stale (author approval rejected 422). dismiss_stale_reviews_on_push=true is configured but unexercised.

### T6-unresolved-thread — VERIFIED
- before/after: `ce80a33f` -> `ce80a33f`
- note: Open review thread on code-owned path blocked merge; thread resolved after via resolveReviewThread.
- GitHub response (405): Repository rule violations found

A conversation must be resolved before this pull request can be merged.

Required status check "gates" is failing.

### T7-failing-ci — VERIFIED
- before/after: `ce80a33f` -> `ce80a33f`
- note: required_status_checks[gates, strict] fires on the genuinely failing 'gates' check-run (Actions run failed: 'account is locked due to a billing issue' on dakuwonmoody-lab). Merge rejected citing the failing check. (A synthetic failing status was also posted via Statuses API, but the block is attributable to the real failed check-run.)
- GitHub response (405): Repository rule violations found

At least 2 approving reviews are required by reviewers with write access.

Required status check "gates" is failing.

### T7b-check-clears-on-success — NOT TESTED
- before/after: `-` -> `-`
- note: Cannot produce a passing 'gates' check-run while Actions is billing-locked. Empirically: a Statuses-API success does NOT override a failed check-run in ruleset evaluation (combined status showed success, merge still cited failing check).

### T8-two-approval-merge — BLOCKED
- before/after: `ce80a33f` -> `ce80a33f`
- note: Needs 3 distinct identities (PR author + 2 approvers; author cannot self-count). Only 1 identity available. Rule NOT weakened; no merge performed. PR #1 left open in blocked state as evidence.

## Preconditions discovered (blockers, not workarounds)
- Both supplied tokens resolve to the same GitHub user `dakuwonmoody-lab` (id 261674734): exactly ONE reviewer identity exists.
- GitHub Actions on this account is billing-locked: `The job was not started because your account is locked due to a billing issue.`
  CI check-runs fail without executing; the `gates` check-run on the PR head is genuinely `failure`.
- Unblock path: a 2nd (for T4-exact/T5) and 3rd (for T8) distinct GitHub user with write access; a billing-unlocked account for a green `gates` run (T7b).
- Nothing was weakened: no local simulation substituted, no rule lowered, no merge performed.
