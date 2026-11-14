---
title: "systemd-hwdb(8)"
name: "systemd-hwdb"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-hwdb/"
description: "systemd-hwdb – hardware database management tool"
---

<p>systemd-hwdb &#8211; hardware database management tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>systemd-hwdb </code><code>[options]</code><code> update</code></p>
<dt> <code>systemd-hwdb </code><code>[options]</code><code> query </code><i>modalias</i></dl>
<h2>Description</h2>
<p><code>systemd-hwdb</code></p>
<dd>expects a command and command specific arguments. It manages the binary hardware database.</p>
<h2>Options</h2>
<p><code>&#8211;usr</code></p>
<dl>
<dd>Generate in /lib/udev instead of /etc/udev.</dl>
<p> <code>-r</code>, <code>&#8211;root=</code><i>PATH</i></p>
<dl>
<dd>Alternate root path in the filesystem.</dl>
<p> <code>-s</code>, <code>&#8211;strict</code></p>
<dl>
<dd>When updating, return non-zero exit value on any parsing error.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<h3>systemd-hwdb [<i>options</i>] update</h3>
<p>Update the binary database.</p>
<h3>systemd-hwdb [<i>options</i>] query [<i>MODALIAS</i>]</h3>
<p>Query database and print result.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-hwdb/">hwdb</a></code>(7) </p>
