---
title: "How to Read Environment Variables in Bash"
date: 2018-03-24 11:52:10 +0000
author: "Q A"
layout: post
canonical: https://www.systutorials.com/how-to-get-an-environment-variable-in-bash/
---

Environment variables store configuration settings for your shell and applications. They’re essential for configuring containers, serverless functions, application runtime behavior, and system services.

## Retrieving an environment variable

Use the dollar sign prefix to access a variable:

``` bash
echo $VARIABLE_NAME
```

This prints the variable’s value to stdout. If the variable doesn’t exist, it prints an empty line.

## Checking if a variable is set

To distinguish between an unset variable and an empty one, use parameter expansion:

``` bash
echo ${VARIABLE_NAME}
```

This syntax is more robust in scripts. To test whether a variable exists before using it:

``` bash
if [[ -z ${VARIABLE_NAME} ]]; then
  echo "Variable is not set or empty"
fi
```

For stricter checking that requires the variable to be set (regardless of whether it’s empty):

``` bash
if [[ -v VARIABLE_NAME ]]; then
  echo "Variable is set"
fi
```

## Common environment variables

Several standard variables are available in any shell:

``` bash
echo $HOME        # User's home directory
echo $USER        # Current username
echo $PWD         # Current working directory
echo $PATH        # Executable search paths
echo $SHELL       # Current shell
echo $LANG        # System language/locale
```

## Setting environment variables

Create a variable for the current session:

``` bash
export MY_VAR="value"
```

The `export` keyword makes it available to child processes. Without `export`, the variable only exists in the current shell.

Set a variable for a single command:

``` bash
MY_VAR="value" some_command
```

The variable is only available during that command’s execution.

## Managing variables across sessions

For persistent environment variables, add them to your shell profile:

``` bash
# ~/.bashrc (for Bash)
export DB_HOST="localhost"
export DB_USER="admin"
```

Source the file to load changes immediately:

``` bash
source ~/.bashrc
```

## Using .env files

For application configuration, especially in containerized environments, use a `.env` file:

``` bash
# .env
DATABASE_URL="postgresql://user:pass@localhost/dbname"
API_KEY="secret-key-here"
LOG_LEVEL="debug"
```

Load variables from the file in your script:

``` bash
set -a
source .env
set +e
```

The `set -a` flag exports all variables defined in the file; `set +e` turns off the flag afterward. Never commit `.env` files with secrets to version control.

## In systemd services

Define environment variables in service unit files:

``` ini
[Service]
Environment="APP_ENV=production"
Environment="LOG_LEVEL=info"
EnvironmentFile=/etc/myapp/config.env
ExecStart=/usr/local/bin/myapp
```

Use `EnvironmentFile=` to load variables from an external file. This approach is standard for system daemons and containerized services.

## Debugging variables

List all environment variables:

``` bash
env
```

Display only exported variables:

``` bash
declare -p
```

Check a specific variable’s value with quotes to see whitespace:

``` bash
printf '%s\n' "$MY_VAR"
```

This is safer than `echo` when the variable might contain special characters or flags.

## Practical Tips and Common Gotchas

When working with programming languages on Linux, environment management is crucial. Use version managers like asdf, pyenv, or sdkman to handle multiple language versions without system-wide conflicts. Always pin dependency versions in production to prevent unexpected breakage from upstream changes.

For build automation, modern alternatives often outperform traditional tools. Consider using just or task instead of Make for simpler task definitions. Use containerized build environments to ensure reproducibility across different development machines.

## Debugging Strategies

Start with the simplest debugging approach and escalate as needed. Print statements and logging often reveal the issue faster than attaching a debugger. For complex issues, use language-specific debuggers like gdb for C and C++, jdb for Java, or dlv for Go. Always check error messages carefully before diving into code.

## Quick Verification

After applying the changes described above, verify that everything works as expected. Run the relevant commands to confirm the new configuration is active. Check system logs for any errors or warnings that might indicate problems. If something does not work as expected, review the steps carefully and consult the official documentation for your specific version.
