# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **personal knowledge management repository** (not a software project) created to document software architecture learning. It contains notes in Spanish from IT books, concepts, and personal reflections. There is no build system, test suite, CI/CD pipeline, or code to execute.

## Structure and Conventions

All documents are Markdown files at the **root level** — no subdirectories. File names use Spanish descriptive nouns with hyphens (e.g., `Diseño-APIs.md`, `The-Software-Architect-Elevator.md`).

### Document Format
- Primary language: **Spanish**
- Headers: `#` for document title, `##` for major sections, `###` for subsections
- Key terms are **bolded** on first use within a section
- Lists use `-`, `*`, or `+` bullets (mixed styles are acceptable per existing convention)
- Tables are used for comparative or state-transition data (see `ACID.md` coherencia example)
- Real-world examples follow each concept, often using banking/financial scenarios

### Content Areas

| File | Topic |
|------|-------|
| `ACID.md` | Database transaction properties (Atomicity, Consistency, Isolation, Durability) |
| `Diseño-APIs.md` | REST API design: query functions, layered architecture (canal/negocio/sistema), best practices, corporate standards |
| `The-Software-Architect-Elevator.md` | Book notes from Gregor Hohpe — Shift-Left Testing, organizational scaling, velocity over efficiency, autonomy vs. anarchy |
| `Code-Review.md` | Reference links on code review |
| `Documentacion.md` | Reference links on technical documentation principles |
| `JAX-RS.md` | Java REST API specification stub (incomplete) |
| `Reflexiones-Aleatorias` | Personal reflections (no `.md` extension, plain text) |
| `README.md` | Reading list of IT books by year |

## Adding New Content

- New topics get their own root-level `.md` file with a descriptive Spanish name
- Book notes follow the pattern in `The-Software-Architect-Elevator.md`: a `### Notas ###` section for raw highlights, `### Comentarios personales ###` for personal reactions, then `## Capitulo N ##` sections for structured summaries
- Concept documents (like `ACID.md`, `Diseño-APIs.md`) use `#` sections per concept with `**Ejemplo**:` blocks demonstrating real-world application
- `README.md` tracks the reading list — add new books under the appropriate year heading

## Key Architectural Concepts Documented

The **layered API architecture** in `Diseño-APIs.md` is the most detailed technical model:
1. **Canal/Experiencia** — device-specific facade layer, changes frequently with UX
2. **Negocio/Proceso** — orchestration layer, applies business rules, source-agnostic
3. **Producto/Sistema** — stable core exposing raw data from ERP/CRM/databases

The **Fast & Good** framework from `The-Software-Architect-Elevator.md` (Ch. 31) defines six attributes for fast software delivery: Velocidad, Confianza, Repetible, Elástico, Feedback, Seguridad.
