---
title: "jpilot(1)"
name: "jpilot"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jpilot/"
description: "jpilot – A palm pilot desktop for Linux/Unix"
---

<h2>NAME</h2>
<p> jpilot &#8211; A palm pilot desktop for Linux/Unix</p>
<h2>SYNOPSIS</h2>
<p> <code>jpilot [-v] [-h] [-d] [-a] [-A] [-i] [-s]</code></p>
<h2>DESCRIPTION</h2>
<p> J-Pilot is a desktop organizer application for the palm pilot and other Palm OS devices. It is similar in functionality to the one that 3Com/Palm distributes.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-v</code></p>
<dd> displays version and exits.</p>
<dt><code>-h</code></p>
<dd> displays help and exits.</p>
<dt><code>-d</code></p>
<dd> displays debug info to stdout.</p>
<dt><code>-a</code></p>
<dd> ignores missed alarms since the last time program was run.</p>
<dt><code>-A</code></p>
<dd> ignores all alarms, past and future.</p>
<dt><code>-i </code></p>
<dd> makes <code>jpilot</code> iconify itself upon launch.</p>
<dt><code>-s </code></p>
<dd> initiates a sync on the running <code>jpilot</code> instance. </p>
<p> If you have more than one <code>jpilot </code> running at the same time the sync may not work as expected since nothing is done to support a multi-instance configuration.</dl>
<h2>ENVIRONMENT</h2>
<p> The PILOTPORT and PILOTRATE environment variables are used to specify which port to sync on and at what speed. </p>
<p> If PILOTPORT is not set then it defaults to /dev/pilot.</p>
<h2>BUGS</h2>
<p> See /usr/share/doc/jpilot/BUGS</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-jpilot-sync/">jpilot-sync</a>(1)</p>
<h2>AUTHOR</h2>
<p> Judd Montgomery &lt;judd [at] jpilot.org&gt; </p>
<h2>Index</h2>
