# Project status

Updated: 2026-10-29

## Current milestone

Completed: repository documentation and first local Squarespace content inventory.

## Completed work

- Documented WE R NI, the two planned interfaces, shared content, migration sources,
  working agreements, and the intended Rails/PostgreSQL stack (not implemented).
- Added a dependency-free Python inventory utility, synthetic XML fixtures, and tests.
- Inventoried the local Squarespace export: **37 items, all pages, 0 reported problems**.
- Generated `docs/SQUARESPACE_INVENTORY.md` and ignored
  `tmp/inventory/squarespace.json` with text, metadata, HTML, links, and image references.
- Verified all 4 automated tests pass, including Unicode, missing fields, malformed
  XML, repeatability, CLI outputs/count validation, and source-directory write protection.
- Verified another real-export run left the source unchanged and produced byte-identical
  JSON and Markdown outputs. Confirmed Git ignores raw exports, generated JSON,
  credentials, and local environments. No commits or pushes performed.

## Known issues and limits

- Image URLs embedded only in CSS or JavaScript are not extracted; HTML is retained.
- Readable text normalizes whitespace; the export remains the authoritative original.
- Multiple exports are inventoried independently; overlapping records are not merged.
- No application importer, search, database, or symbolic relationship model exists yet.
- Medium and Substack exports have not been inventoried.

## Next possible tasks

1. Review inventory text and image/link coverage against the original pages locally.
2. Inventory Medium and Substack exports with similarly small tested utilities.
3. Define shared content identities, provenance, and explicit relationship rules before
   building an idempotent importer and the Rails/PostgreSQL application.

Resume with `python3 -m unittest discover -s tests -v` and
`python3 scripts/squarespace_inventory.py --expect-count 37`.
