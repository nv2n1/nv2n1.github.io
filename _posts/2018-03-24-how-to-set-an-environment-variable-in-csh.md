---
title: "Setting Environment Variables in C Shell"
date: 2018-03-24 08:18:35 +0000
modified: 2026-04-12 06:45:12 +0000
author: "Q A"
layout: post
categories: [linux-systems-administration]
canonical: /how-to-set-an-environment-variable-in-csh/
---

\[md\]
Use `setenv` to set an environment variable in csh:

```wp-block-code
setenv VARIABLE value
```

Replace `VARIABLE` with the name of the variable and `value` with its value. The variable is immediately available in the current shell and inherited by child processes.

\## Examples

Set a simple variable:

```wp-block-code
setenv PATH /usr/local/bin:/usr/bin:/bin
setenv EDITOR vim
setenv JAVA_HOME /usr/lib/jvm/java-17-openjdk
```

Use quotes if the value contains spaces:

```wp-block-code
setenv MY_MESSAGE "Hello World"
```

Reference existing variables when building new ones:

```wp-block-code
setenv LD_LIBRARY_PATH /opt/lib
```

\## Setting Shell Variables vs Environment Variables

csh distinguishes between shell variables and environment variables:

– `setenv` — creates an environment variable (inherited by child processes)
– `set` — creates a shell variable (local to current shell only)

```wp-block-code
# Environment variable - child processes see this
setenv DATABASE_HOST db.example.com

# Shell variable - only current shell sees this
set prompt = "%n@%m:%~% "
```

Common shell variables you set with `set`:

```wp-block-code
set history = 1000
set savehist = 1000
set notify
set filec
```

\## Displaying Variables

View a specific variable:

```wp-block-code
echo $VARIABLE
printenv VARIABLE
```

List all environment variables:

```wp-block-code
printenv
env
```

List shell variables (shows both shell and env vars):

```wp-block-code
set
```

\## Making Changes Persistent

Environment variables set with `setenv` only persist for the current shell session. To make them permanent, add the commands to your shell configuration file.

For csh, edit `~/.cshrc`:

```wp-block-code
setenv PATH /usr/local/bin:/usr/bin:/bin
setenv EDITOR vim
setenv JAVA_HOME /usr/lib/jvm/java-17-openjdk
```

For tcsh (a modern csh variant), use `~/.tcshrc`. Changes take effect on the next shell login or after running:

```wp-block-code
source ~/.cshrc
```

For system-wide environment variables, add them to `/etc/csh.cshrc` (affects all csh users).

\## Login vs Non-Login Shells

The file loading order differs between login and non-login shells:

\*\*Login shell\*\* reads: `/etc/csh.cshrc` → `/etc/csh.login` → `~/.cshrc` → `~/.login`

\*\*Non-login shell\*\* (e.g. script execution) reads: `/etc/csh.cshrc` → `~/.cshrc`

Put environment variables in `~/.cshrc` to ensure they’re available in all shell types. Put login-specific setup (like terminal configuration) in `~/.login`.

\## Unsetting Variables

Remove an environment variable with `unsetenv`:

```wp-block-code
unsetenv VARIABLE
```

Remove a shell variable with `unset`:

```wp-block-code
unset prompt
```

\## Important Differences from Bash

If you’re coming from bash, these differences catch people out:

– csh uses `setenv` instead of `export`
– csh uses `unsetenv` instead of `unset` (for env vars)
– csh syntax doesn’t support `VARIABLE=value` at the shell prompt (that’s a POSIX shell feature)
– Variable references require `$` prefix
– No `export` command — use `setenv` directly
– No inline variable assignment like bash’s `VAR=val command`

Quick reference for common bash-to-csh translations:

\| Bash \| csh/tcsh \|
\|——\|———-\|
\| `export VAR=val` \| `setenv VAR val` \|
\| `VAR=val` \| `set VAR = val` \|
\| `unset VAR` \| `unsetenv VAR` \|
\| `echo $VAR` \| `echo $VAR` \|
\| `export -n VAR` \| `unsetenv VAR` \|

\## Common Setup Patterns

A typical `~/.cshrc` for a developer:

```wp-block-code
# Path
setenv PATH /usr/local/bin:/usr/bin:/bin

# Development
setenv EDITOR vim
setenv LANG en_US.UTF-8

# History
set history = 2000
set savehist = 2000

# Aliases
alias ll 'ls -la'
alias gs 'git status'
```

\## Why Still Use csh?

While csh and tcsh are less common than bash in modern deployments, they’re still present on BSD systems (FreeBSD and OpenBSD default to csh/tcsh) and some legacy Unix environments. tcsh offers improved features like history expansion and command-line editing compared to original csh, making it a reasonable choice for interactive use despite its scripting limitations. For scripting, bash or sh is generally preferred due to better POSIX compliance.
