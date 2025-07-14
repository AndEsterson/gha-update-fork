## Version 0.2.0

Released 2025-07-13

- Follow redirects for moved projects. {issue}`1`
- Read `GITHUB_TOKEN` to make authenticated requests, and advise setting it if
  a rate limit is reached. {issue}`7`
- Use default config if the config file does not exist. {issue}`14`
- Update action references in action definitions. Definitions are
  `action.yaml`/`.yml` file in folders in `.github/actions` or at the root.
  {issue}`6`
- Don't fail if `workflows` folder is missing.
- Add `ghes-host` config to access a GitHub Enterprise Server. {issue}`16`
- Handle pagination when fetching tags. Show an error if no version tags were
  found. {issue}`15`

## Version 0.1.0

Released 2024-08-23
