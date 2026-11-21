---
title: "session-migration(1)"
name: "session-migration"
section: "1"
letter: "s"
url: "/docs/linux/man/1-session-migration/"
description: "session-migration – Migrate in user session settings."
---

<h2>SYNOPSIS</h2>
<p> <code>session-migration</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> The <code>session-migration</code> program can be used to migrate in-session user data when a program is evolving its configuration, or needing to have files moved and so on. This program is generally autostarted at the very beginning of the session and integrates caching capabilities. </p>
<p> The general usage is to ship an executable file in XDG_DATA_DIR/session-migration/scripts. This one will be executed the next time the user log into the session. It will executes all executable files there in ascii order, one after another. </p>
<p> Even if the program tries to cache some timestamp and scripts to not be launched twiced (they are skipped on subsequent runs), the executables file should be idempotent. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;dry-run</code></dt>
<dd> This parameter enables to run the session-migration tool without really launching the scripts and marking them are migrated. It&#8217;s generally used with &#8211;verbose for debugging purposes. </dd>
<dt><code>&#8211;file</code>&nbsp;<i>filename</i></dt>
<dd> This parameter, followed by a path or filename, tells sesions-migration to only consider that script file and ignoring XDG_DATA_DIR. It won&#8217;t log as well this special file as being migrated. </dd>
<dt><code>&#8211;help</code></dt>
<dd> Display a quick command help. </dd>
<dt><code>&#8211;verbose</code></dt>
<dd> Show a lot of verbose information. It can be used by the user to debug configuration issues; </dd>
</dl>
