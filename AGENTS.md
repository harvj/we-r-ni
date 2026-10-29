# Working agreements

- Prefer simple, maintainable implementations with minimal dependencies.
- Preserve original source content and metadata without destructive transformations.
- Never modify original exports.
- Preserve Unicode, including Hebrew, Greek, Sanskrit, Tarot, and I Ching symbols.
- Write automated tests for importers and content transformations.
- Make import operations repeatable and eventually idempotent.
- Do not invent missing content, metadata, or symbolic relationships.
- Keep raw exports, credentials, and potentially private conversations out of Git.
- Never modify production services, DNS, or existing websites without explicit authorization.
- Use small, verifiable milestones.
- Keep project documentation accurate as the implementation evolves.
- Update `docs/STATUS.md` whenever a milestone is completed.
- At the end of each task, report changes, tests performed, and outstanding issues.

### Media storage conventions

- Self-host application media on the Hetzner server using Rails Active Storage with the local disk service.
- Do not introduce S3, cloud object storage, a CDN, or third-party media services without an explicit architectural decision.
- Store uploaded media in persistent storage outside application release directories.
- Preserve original image files, filenames where available, source URLs, and attribution metadata.
- Support images attached to Yods, hexagrams, articles, and other content entities.
- Keep media files out of Git, except small fixtures needed for automated tests.
- Ensure deployment procedures preserve persistent storage.
- Include application media in off-server backups and document restoration procedures.
- Do not delete original media during imports or migrations.
- Prefer Rails built-in functionality over custom storage infrastructure.
