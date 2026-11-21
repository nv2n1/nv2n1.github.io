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
<p> <code>jpilot-sync [-v] [-h] [-d] [-P] [-b] [-l] [-p port] </code></p>
<p> J-Pilot preferences are read to get port, rate, number of backups, etc. They are read from the directory <i>$JPILOT_HOME/.jpilot/jpilot.rc</i></p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></dt>
<dd> Print out the version and exit.</dd>
<dt><code>-h</code></dt>
<dd> Print out help and exit.</dd>
<dt><code>-d</code></dt>
<dd> run in debug mode.</dd>
<dt><code>-P</code></dt>
<dd> do not load plugins.</dd>
<dt><code>-b</code></dt>
<dd> Do a sync and then a backup, otherwise just do a sync.</dd>
<dt><code>-l</code></dt>
<dd> Stay in a loop, otherwise sync once and exit.</dd>
<dt><code>-p </code><i>port</i></dt>
<dd> Use this port to sync with instead of using preferences or the default of /dev/jpilot.</dd></dl>
<h2>BUGS</h2>
<p> See /usr/share/doc/jpilot/BUGS</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-jpilot/">jpilot</a>(1)</p>
<h2>AUTHOR</h2>
<p> Judd Montgomery &lt;judd [at] jpilot.org&gt; </p>
