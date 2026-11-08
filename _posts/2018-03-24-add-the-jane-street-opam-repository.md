---
title: "Using the Jane Street OPAM Repository"
date: 2018-03-24 08:17:50 +0000
modified: 2026-04-12 16:10:27 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /add-the-jane-street-opam-repository/
---

The Jane Street OPAM repository contains specialized OCaml packages and libraries maintained by Jane Street, including their popular Core library and related tools. You’ll need to add this repository to your OPAM configuration to access these packages.

### Method 1: Clone and Add Locally

If you prefer to clone the repository first and add it as a local reference:

``` bash
git clone -b core-branch https://github.com/janestreet/opam-repository.git
opam repo add js opam-repository
```

Replace `core-branch` with the actual branch you need. Common branches include:

- `core-branch` — the main Jane Street packages branch
- `main` — the default branch (may not contain all Jane Street-specific packages)

After adding the repository, update your OPAM package index:

``` bash
opam update
```

### Method 2: Add Remote Repository Directly

For a cleaner approach, add the remote repository directly without cloning:

``` bash
opam repo add js https://github.com/janestreet/opam-repository.git#core-branch
```

This method fetches the repository metadata directly from GitHub without requiring a local clone. The `#core-branch` syntax specifies the branch to use. After adding it, run:

``` bash
opam update
```

### Verify the Repository Was Added

List your configured repositories:

``` bash
opam repo list
```

You should see `js` in the output with its URL and priority.

### Setting Repository Priority

OPAM repositories are searched in priority order. If you want Jane Street packages to take precedence over the default OPAM repository, you can adjust the priority when adding:

``` bash
opam repo add --priority=10 js https://github.com/janestreet/opam-repository.git#core-branch
```

Higher numbers mean higher priority. The default OPAM repository typically has priority 0.

### Installing Jane Street Packages

Once the repository is added and updated, you can install packages like Core:

``` bash
opam install core
```

Or install multiple related packages:

``` bash
opam install core core_kernel ppx_jane
```

### Removing the Repository

If you need to remove the Jane Street repository later:

``` bash
opam repo remove js
```

### Troubleshooting

If `opam update` fails after adding the repository, verify:

- Your internet connection can reach GitHub
- The branch name exists in the repository: `git ls-remote https://github.com/janestreet/opam-repository.git | grep core-branch`
- Your OPAM version is current: `opam --version`

If you’re using a very old OPAM version (pre-2.0), consider upgrading, as repository management has improved significantly.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## Additional Tips and Best Practices

When implementing the techniques described in this article, consider these best practices for production environments. Always test changes in a non-production environment first. Document your configuration changes so team members can understand what was modified and why.

Keep your system updated regularly to benefit from security patches and bug fixes. Use package managers rather than manual installations when possible, as they handle dependencies and updates automatically. For critical systems, maintain backups before making any significant changes.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
