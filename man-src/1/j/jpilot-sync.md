---
title: "jpilot-sync(1)"
name: "jpilot-sync"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpilot-sync/"
description: "jpilot-sync – A command line tool for syncing jpilot databases to a Palm OS device."
---

<h2>NAME</h2>
<p> jpilot-sync &#8211; A command line tool for syncing jpilot databases to a Palm OS device.</p>
<h2>SYNOPSIS</h2>
<p> <code>jpilot-sync [-v] [-h] [-d] [-P] [-b] [-l] [-p port] </code></p>
<h2>DESCRIPTION</h2>
<p> J-Pilot preferences are read to get port, rate, number of backups, etc. They are read from the directory <i>$JPILOT_HOME/.jpilot/jpilot.rc</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> Print out the version and exit.</p>
<dt><code>-h</code></p>
<dd> Print out help and exit.</p>
<dt><code>-d</code></p>
<dd> run in debug mode.</p>
<dt><code>-P</code></p>
<dd> do not load plugins.</p>
<dt><code>-b</code></p>
<dd> Do a sync and then a backup, otherwise just do a sync.</p>
<dt><code>-l</code></p>
<dd> Stay in a loop, otherwise sync once and exit.</p>
<dt><code>-p </code><i>port</i></p>
<dd> Use this port to sync with instead of using preferences or the default of /dev/jpilot.</dl>
<h2>BUGS</h2>
<p> See /usr/share/doc/jpilot/BUGS</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-jpilot/">jpilot</a>(1)</p>
<h2>AUTHOR</h2>
<p> Judd Montgomery &lt;judd [at] jpilot.org&gt; </p>
<h2>Index</h2>
