---

title: "spd-conf(1)"
name: "spd-conf"
section: "1"
letter: "s"
url: "/docs/linux/man/1-spd-conf/"
description: "spd-conf – configure Speech Dispatcher and diagnose problems"
---

<p> spd-conf &#8211; configure Speech Dispatcher and diagnose problems </p>
<h2>DESCRIPTION</h2>
<p> usage: spd-conf [-h] [-u] [-c] [-C] [-d] [-s] [&#8211;test-festival]</p>
<dl>
<dt>
</dt><dd> [&#8211;test-espeak] [&#8211;test-alsa] [&#8211;test-pulse] [-e] [-n] [-D] [&#8211;version]</dd></dl>
<p> A simple tool for basic configuration of Speech Dispatcher and problem diagnostics</p>
<h3>options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-u</code>, <code>&#8211;create-user-conf</code></dt>
<dd> Create Speech Dispatcher configuration for the given user</dd>
<dt><code>-c</code>, <code>&#8211;config-basic-settings-user</code></dt>
<dd> Configure basic settings in user configuration</dd>
<dt><code>-C</code>, <code>&#8211;config-basic-settings-system</code></dt>
<dd> Configure basic settings in system-wide configuration</dd>
<dt><code>-d</code>, <code>&#8211;diagnostics</code></dt>
<dd> Diagnose problems with the current setup</dd>
<dt><code>-s</code>, <code>&#8211;test-spd-say</code></dt>
<dd> Test connection to Speech Dispatcher using spd-say</dd>
<dt><code>&#8211;test-festival</code></dt>
<dd> Test whether Festival works as a server</dd>
<dt><code>&#8211;test-espeak</code></dt>
<dd> Test whether Espeak works as a standalone binary</dd>
<dt><code>&#8211;test-alsa</code></dt>
<dd> Test ALSA audio output</dd>
<dt><code>&#8211;test-pulse</code></dt>
<dd> Test Pulse Audio output</dd>
<dt><code>-e</code>, <code>&#8211;espeak</code></dt>
<dd> Use espeak to synthesize messages</dd>
<dt><code>-n</code>, <code>&#8211;dont-ask</code></dt>
<dd> Do not ask any questions, always use default values</dd>
<dt><code>-D</code>, <code>&#8211;debug</code></dt>
<dd> Debug a problem and generate a report</dd>
<dt><code>&#8211;version</code></dt>
<dd> Print version and copyright info</dd></dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 Brailcom, o.p.s.<br />
 This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. Please see COPYING for more details. </p>
