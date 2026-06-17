# Athena - No. 16

<!-- -------------------------------------------------------------- -->

> *some assembly required.*
>
> optimization depth, AI evals, product judgment,
> semiconductor maps, and one large passion project under glass.
> the door is still unmarked.

<!-- -------------------------------------------------------------- -->

```
product manager - technical
AI | supply chain | semiconductors | data science
amazon | qualcomm
MIT SDM | NTU EEE
```

```
room 16 | basement | est. 2026
no cookies, no analytics, no asks.
```

I build small evaluated products with operational discipline. every
decision lives in `decisions/`, every brief is gate-tested, every agent
run is auditable. active product repos run the same control plane:
shared schemas, shared gate scripts, shared dream-retrospective cadence.
the cross-repo charter is
[athena-site/ops/control-plane.md](https://github.com/AthenaTheOwl/athena-site/blob/main/ops/control-plane.md).

## // for each kind of reader

**project reader.** start with
[No. 17 - procurement-negotiation-lab](https://github.com/AthenaTheOwl/procurement-negotiation-lab)
(agent coordination under private information: weighted-Nash,
bounded-leakage, MPC reference path, oracle gaps, property tests), then
[No. 20 - trace-to-eval-harness](https://github.com/AthenaTheOwl/trace-to-eval-harness)
(failed traces, CDCP event ledgers, evidence packets, and run bundles).

**project reader.** if you want product cadence and field sense, read
[No. 18 - ai-field-brief](https://github.com/AthenaTheOwl/ai-field-brief)
after the two research artifacts. it is the weekly AI digest with
source gates, faithfulness audit, and run-evidence records.

**curious visitor.** four live demos: ai-field-brief on vercel,
procurement-negotiation-lab on vercel, supplier-risk-rag-agent on
streamlit, and chip-supply-chain-map on vercel. pick one and read for
five minutes.

**builder or engineer.** fork-friendly. each active repo runs the
Cognitive Delivery Control Plane — same schemas, same gates. AGENTS.md
in each repo is the agent-onboarding contract.

**future-self.** `decisions/` ledgers answer "what was I thinking."
`dreams/` surfaces weekly retrospectives. `event-log/` is the durable
history across cycles.

## // active

**[No. 18 - ai-field-brief](https://github.com/AthenaTheOwl/ai-field-brief)** - *weekly AI digest with concrete moves.*
deployed brief site with evaluator-graded sources, dream-promoted
playbook items, and a control-plane scaffold across briefs/, specs/,
decisions/. [live demo](https://ai-field-brief.vercel.app/).
*for: project readers, eval-discipline readers, brief subscribers.*

**[No. 20 - trace-to-eval-harness](https://github.com/AthenaTheOwl/trace-to-eval-harness)** - *failed traces become eval cases.* <!-- voice_lint:allow banned-harness -->
python CLI that ingests failed AI traces, creates human-reviewed eval
cases, validates CDCP run-evidence packets, and wraps runs in
runtime-agnostic bundles for replay and adapter comparison.
*for: eval-discipline readers, agent builders, reliability reviewers.*

**[No. 19 - mcp-security-lab](https://github.com/AthenaTheOwl/mcp-security-lab)** - *MCP configs before runtime.*
python CLI that scans MCP server configs for command execution,
transport, tool-scope, and prompt-injection risk, then writes JSON and
markdown policy reports.
*for: security reviewers, agent builders, tool-permission readers.*

**[No. 17 - procurement-negotiation-lab](https://github.com/AthenaTheOwl/procurement-negotiation-lab)** - *flagship research artifact. mechanism design, made interactive.*
an empirical lab for AI-mediated procurement coordination under private
information: oracle, ADMM, weighted-Nash plaintext, bounded-leakage
weighted-Nash, v1 MPC reference path, multi-party SDK, property tests,
and run-evidence records.
[live demo](https://procurement-negotiation-lab.vercel.app/).
*for: project readers, mechanism-design readers, AI economics/policy.*

**[No. 13 - supplier-risk-rag-agent](https://github.com/AthenaTheOwl/supplier-risk-rag-agent)** - *RAG with receipts.*
SEC filing excerpts in, cited answers out. retrieval, citation
faithfulness, abstention, regression evals, and a monthly EDGAR refresh
path.
[live demo](https://supplier-risk-rag-agent.streamlit.app/).
*for: project readers, eval-pipeline builders, supply-chain analysts.*

**[No. 12 - chip-supply-chain-map](https://github.com/AthenaTheOwl/chip-supply-chain-map)** - *the chip supply chain as a dependency graph.*
foundries, OSATs, equipment, substrates, EDA, hyperscalers, AI
accelerator platforms, chokepoints, disruption scenarios, and sourced
investor-sensitivity notes.
*for: semiconductor analysts, supply-chain strategists, curious visitors.*

**[No. 11 - athena-site](https://github.com/AthenaTheOwl/athena-site)** - *the front door.*
personal site, essays, portfolio doors, lens paths, and the
procurement-negotiation-lab embedded as the flagship demo. hosts the
cross-repo control-plane charter under `ops/`.
*for: curious visitors, portfolio readers, control-plane spelunkers.*

**[No. 10 - ai-supply-chain-copilot-prd](https://github.com/AthenaTheOwl/ai-supply-chain-copilot-prd)** - *a product teardown.*
PRD for an AI supply-chain exception copilot with explicit trust
boundaries and a build plan that reuses the live portfolio blocks.
*for: product readers, project readers, supply-chain operators.*

**[No. 01 - dispatch-optimizer](https://github.com/AthenaTheOwl/dispatch-optimizer)** - *greedy vs. clever, with constraints that bite.*
temperature, equipment, time windows, multi-stop. manual against
algorithmic.

**[No. 02 - LLM-evaluation-framework](https://github.com/AthenaTheOwl/LLM-evaluation-framework)** - *quality is more than one score.*
deterministic rules + persona evals + judge models, wired into CI.

## // starforge cluster - published serial + in-progress game adaptation

curated Act 1-safe public exhibits from Starforge, a published creative
serial on [Royal Road](https://www.royalroad.com/fiction/149065/starforge-canticles)
and an in-progress hobby narrative-game adaptation. these are clean
review copies, not workshop dumps: released material only, later acts
kept private, source included, runtime junk excluded, validation gates
added.

**[No. 14 - starforge-narrative-tools](https://github.com/AthenaTheOwl/starforge-narrative-tools)** - *the public slice and the operating system around it.*
released Act 1 prose/spec slice plus Python conversion and validation
tooling for moving long-form writing toward game-ready data.

**[No. 15 - starforge-renpy-demo](https://github.com/AthenaTheOwl/starforge-renpy-demo)** - *an Act 1 Ren'Py adaptation exhibit.*
released narrative scenes, dialogue files, combat vignettes, state
systems, and UI screens with lint/static validation.

**[No. 16 - starforge-rpg-prototype](https://github.com/AthenaTheOwl/starforge-rpg-prototype)** - *an Act 1 Godot RPG prototype exhibit.*
party data, combat systems, branching dialogue, quests, scenes, UI
scripts, and static project validation for the hobby adaptation.

## // how I build

spec-driven. every R-* requirement carries an `owner_role:` token and at
least one DEC-* decision before it ships. every weekly cycle runs a
dream-retrospective that produces promotion candidates for AGENTS.md,
SKILL.md, regression tests. executable gate scripts (spec_check,
voice_lint, validate_decisions, validate_roles, validate_tools,
validate_policies, validate_schemas, validate_registry) fail builds when
artifacts drift.

the cross-repo charter:
[athena-site/ops/control-plane.md](https://github.com/AthenaTheOwl/athena-site/blob/main/ops/control-plane.md).

works for a solo builder. scaling it to a team would add PR review +
policy-engine runtime + dashboard.

## // solved

**[No. 03 - MIT-SDM-Thesis-on-System-Dynamics-Modeling-of-Bitcoin](https://github.com/AthenaTheOwl/MIT-SDM-Thesis-on-System-Dynamics-Modeling-of-Bitcoin)** - *a thesis. system dynamics. bitcoin.*
all model files, replicable.

**[No. 04 - world-food-program-robust-simulator](https://github.com/AthenaTheOwl/world-food-program-robust-simulator)** - *humanitarian logistics, under uncertainty.*
77,000 people in syria. nominal LP, robust SOCP, monte carlo, two-stage adaptive contracts. streamlit + cvxpy.

**[No. 05 - semiconductor-e2e-manufacturing-optimization](https://github.com/AthenaTheOwl/semiconductor-e2e-manufacturing-optimization)** - *wafers, monte carlo, two-stage adaptive.*
the same toolkit, pointed at a fab.

**[No. 06 - Robust-Facility-Location](https://github.com/AthenaTheOwl/Robust-Facility-Location)** - *where to build, when you do not know demand.*
nominal, robust, ellipsoidal, adaptive. side-by-side, with stress tests.

## // in the drawer

**[No. 07 - News-Bias-Multi-Agent-Pipeline](https://github.com/AthenaTheOwl/News-Bias-Multi-Agent-Pipeline)** - *agents reading agents reading the news.*
pull, summarize, detect bias, critique the detector, summarize again. early experiment, kept in the drawer.

**[No. 08 - MIT-AI-Fall20](https://github.com/AthenaTheOwl/MIT-AI-Fall20)** - *coursework, kept for posterity.*

**[No. 09 - leetcode](https://github.com/AthenaTheOwl/leetcode)** - *the obligatory grind, captured for completeness.*

## // contact

github: [@AthenaTheOwl](https://github.com/AthenaTheOwl)
site: [athena-site](https://athena-site-six.vercel.app/)
email: vigneshthegreat@gmail.com

## // royal road

speculative fiction lives next door.
[Starforge Canticles](https://www.royalroad.com/fiction/149065/starforge-canticles)
is serializing chapter-by-chapter; the No. 14-16 repos are the
engineering exhibits around that work.

## // license

each repo declares its own. code mostly Apache-2.0 / MIT. content
(briefs, essays) mostly CC BY 4.0.

<!-- -------------------------------------------------------------- -->

```
built downstairs.
```
