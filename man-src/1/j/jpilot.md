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
<dt><code>-v</code></dt>
<dd> displays version and exits.</dd>
<dt><code>-h</code></dt>
<dd> displays help and exits.</dd>
<dt><code>-d</code></dt>
<dd> displays debug info to stdout.</dd>
<dt><code>-a</code></dt>
<dd> ignores missed alarms since the last time program was run.</dd>
<dt><code>-A</code></dt>
<dd> ignores all alarms, past and future.</dd>
<dt><code>-i </code></dt>
<dd> makes <code>jpilot</code> iconify itself upon launch.</dd>
<dt><code>-s </code></dt>
<dd> initiates a sync on the running <code>jpilot</code> instance. </dd>
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
