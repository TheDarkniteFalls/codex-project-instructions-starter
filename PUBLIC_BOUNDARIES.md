# Public And Private Boundaries

Use this checklist before publishing examples, fixtures, docs, or agent output.

## Public-Safe

- Synthetic data.
- Minimal examples created for the repo.
- Commands, checks, and templates that do not reveal private context.
- Public issue or pull request links.

## Keep Private

- Credentials, tokens, private keys, and real `.env` files.
- Personal notes, private memory, email/calendar/drive exports, and raw logs.
- Internal project state that was not written for public release.
- Local machine paths that expose people, clients, or private projects.

## Review Rule

If a file only makes sense because of private context, rewrite it as a synthetic
example before publishing.
