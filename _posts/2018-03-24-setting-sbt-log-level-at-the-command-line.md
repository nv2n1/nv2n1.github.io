---
title: "Controlling SBT Log Levels from the CLI and Configuration"
date: 2018-03-24 11:41:06 +0000
author: "Eric Ma"
layout: post
categories: [linux-systems-administration]
canonical: /setting-sbt-log-level-at-the-command-line/
---

The simplest approach is passing log level flags directly to sbt:

``` bash
sbt --error "compile"
sbt --warn "clean compile"
sbt --info "test"
sbt --debug "publishLocal"
```

Common log level flags:

- `--error` — errors only
- `--warn` — warnings and errors (default)
- `--info` — info, warnings, and errors
- `--debug` — verbose debugging output
- `--trace` — most verbose, rarely needed

You can combine log level flags with other sbt options:

``` bash
sbt --error --offline "compile"
sbt --warn -Dsbt.log.noformat=true "test"
sbt --info -mem 2048 "publishLocal"
```

The `-Dsbt.log.noformat=true` flag strips ANSI color codes—useful in CI/CD where colored output breaks log parsing or causes formatting issues.

## Interactive shell

If you’re already in the sbt shell, adjust log level without restarting:

``` bash
sbt
> set logLevel := Level.Error
> compile
> set logLevel := Level.Info
> test
```

Available levels are `Level.Error`, `Level.Warn`, `Level.Info`, `Level.Debug`, and `Level.Trace`.

## Persistent configuration

For consistent settings across all projects, add to `~/.sbt/1.0/global.sbt`:

``` scala
logLevel := Level.Warn
```

For project-specific settings, add to `build.sbt`:

``` scala
logLevel := Level.Info
```

You can set different log levels for specific tasks using scoped settings:

``` scala
logLevel := Level.Warn
logLevel in compile := Level.Debug
logLevel in test := Level.Info
```

In newer sbt versions (1.4+), use the `Compile / compile / logLevel` syntax:

``` scala
logLevel := Level.Warn
Compile / compile / logLevel := Level.Debug
Test / logLevel := Level.Info
```

## Fine-grained logger control

For finer control over which loggers are active, configure them in `build.sbt`. This is useful when dependencies emit excessive debug output:

``` scala
logLevel := Level.Info

loggers := {
  val console = new sbt.BasicLogger {
    def log(level: sbt.Level.Value, message: => String): Unit = {
      if (level >= sbt.Level.Warn) println(message)
    }
  }
  Seq(console)
}
```

You can add filtering logic to silence specific modules while preserving warnings from others:

``` scala
loggers := {
  val console = new sbt.BasicLogger {
    def log(level: sbt.Level.Value, message: => String): Unit = {
      val msg = message
      // Suppress debug logs from netty and akka
      if (!msg.contains("[netty]") && !msg.contains("[akka]")) {
        if (level >= sbt.Level.Debug) println(message)
      } else if (level >= sbt.Level.Warn) {
        println(message)
      }
    }
  }
  Seq(console)
}
```

This approach is more maintainable than grepping logs after builds complete.

## CI/CD environments

GitHub Actions:

``` yaml
- name: Build with sbt
  run: sbt --error "clean compile test"
```

Jenkins:

``` bash
#!/bin/bash
set -e
sbt --warn "clean compile publishLocal"
```

GitLab CI:

``` yaml
build:
  script:
    - sbt --warn "clean compile"
  artifacts:
    logs: build.log
```

In CI, prefer `--error` or `--warn` to keep logs readable and catch only real issues. Pipeline systems often have log size limits; reducing noise helps you stay within quotas and makes troubleshooting faster.

## Practical debugging workflow

Start with `--warn` for local development to catch issues without drowning in details. Use `--error` in CI pipelines to reduce noise. Switch to `--debug` only when investigating build failures or dependency resolution problems.

For long-running builds, `--info` serves as a middle ground—it shows compilation progress and test counts without excessive verbosity.

If a build hangs or behaves unexpectedly, combine flags to diagnose the issue:

``` bash
sbt --debug -Dsbt.log.noformat=true "compile"
```

This often reveals the root cause, especially with classpath issues or Ivy resolution deadlocks. Add `--trace` if `--debug` doesn’t provide enough detail.

## Environment variables

You can also set log level via environment variables for CI environments where modifying commands is inconvenient:

``` bash
export SBT_OPTS="-Dsbt.log.level=warn"
sbt "clean compile"
```

Valid values: `error`, `warn`, `info`, `debug`, `trace`.
