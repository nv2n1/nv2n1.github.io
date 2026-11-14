---
title: "spd-conf(1)"
name: "spd-conf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spd-conf/"
description: "spd-conf – configure Speech Dispatcher and diagnose problems"
---

<h2 class="name">NAME</h2>
<p> spd-conf &#8211; configure Speech Dispatcher and diagnose problems </p>
<h2>DESCRIPTION</h2>
<p> usage: spd-conf [-h] [-u] [-c] [-C] [-d] [-s] [&#8211;test-festival]</p>
<dl>
<dt>
<dd> [&#8211;test-espeak] [&#8211;test-alsa] [&#8211;test-pulse] [-e] [-n] [-D] [&#8211;version]</dl>
<p> A simple tool for basic configuration of Speech Dispatcher and problem diagnostics</p>
<h3>options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-u</code>, <code>&#8211;create-user-conf</code></p>
<dd> Create Speech Dispatcher configuration for the given user</p>
<dt><code>-c</code>, <code>&#8211;config-basic-settings-user</code></p>
<dd> Configure basic settings in user configuration</p>
<dt><code>-C</code>, <code>&#8211;config-basic-settings-system</code></p>
<dd> Configure basic settings in system-wide configuration</p>
<dt><code>-d</code>, <code>&#8211;diagnostics</code></p>
<dd> Diagnose problems with the current setup</p>
<dt><code>-s</code>, <code>&#8211;test-spd-say</code></p>
<dd> Test connection to Speech Dispatcher using spd-say</p>
<dt><code>&#8211;test-festival</code></p>
<dd> Test whether Festival works as a server</p>
<dt><code>&#8211;test-espeak</code></p>
<dd> Test whether Espeak works as a standalone binary</p>
<dt><code>&#8211;test-alsa</code></p>
<dd> Test ALSA audio output</p>
<dt><code>&#8211;test-pulse</code></p>
<dd> Test Pulse Audio output</p>
<dt><code>-e</code>, <code>&#8211;espeak</code></p>
<dd> Use espeak to synthesize messages</p>
<dt><code>-n</code>, <code>&#8211;dont-ask</code></p>
<dd> Do not ask any questions, always use default values</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Debug a problem and generate a report</p>
<dt><code>&#8211;version</code></p>
<dd> Print version and copyright info</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 Brailcom, o.p.s.<br />
 This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. Please see COPYING for more details. </p>
<h2>Index</h2>
