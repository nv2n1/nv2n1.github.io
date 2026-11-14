---
title: "speech-dispatcher(1)"
name: "speech-dispatcher"
section: "1"
letter: "s"
url: "/docs/linux/man/1-speech-dispatcher/"
description: "speech-dispatcher – speech synthesis daemon"
---

<h2 class="name">NAME</h2>
<p> speech-dispatcher &#8211; speech synthesis daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>speech-dispatcher</code> [<i>,-{d|s}/</i>] [<i>,-l {1|2|3|4|5}/</i>] [<i>,-c com_method/</i>] [<i>,-S socket_path/</i>] [<i>,-p port/</i>] [<i>,-t timeout/</i>] <i>,| /</i>[<i>,-v/</i>] <i>,| /</i>[<i>,-h/</i>]</p>
<h2>DESCRIPTION</h2>
<p> Speech Dispatcher <code>&#8212;</code> Common interface for Speech Synthesis (GNU GPL)</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;run-daemon</code></p>
<dd> Run as a daemon</p>
<dt><code>-s</code>, <code>&#8211;run-single</code></p>
<dd> Run as single application</p>
<dt><code>-a</code>, <code>&#8211;spawn</code></p>
<dd> Start only if autospawn is not disabled</p>
<dt><code>-l</code>, <code>&#8211;log-level</code></p>
<dd> Set log level (between 1 and 5)</p>
<dt><code>-L</code>, <code>&#8211;log-dir</code></p>
<dd> Set path to logging</p>
<dt><code>-c</code>, <code>&#8211;communication-method</code></p>
<dd> Communication method to use (&#8216;unix_socket&#8217; or &#8216;inet_socket&#8217;)</p>
<dt><code>-S</code>, <code>&#8211;socket-path</code></p>
<dd> Socket path to use for &#8216;unix_socket&#8217; method (filesystem path or &#8216;default&#8217;)</p>
<dt><code>-p</code>, <code>&#8211;port</code></p>
<dd> Specify a port number for &#8216;inet_socket&#8217; method</p>
<dt><code>-t</code>, <code>&#8211;timeout</code></p>
<dd> Set time in seconds for the server to wait before it shuts down, if it has no clients connected. Setting to 0 disables such shutdown</p>
<dt><code>-P</code>, <code>&#8211;pid-file</code></p>
<dd> Set path to pid file</p>
<dt><code>-C</code>, <code>&#8211;config-dir</code></p>
<dd> Set path to configuration</p>
<dt><code>-m</code>, <code>&#8211;module-dir</code></p>
<dd> Set path to modules</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Report version of this program</p>
<dt><code>-D</code>, <code>&#8211;debug</code></p>
<dd> Output debugging information into <i>,$TMPDIR/speechd-debug/</i> if TMPDIR is exported, otherwise to <i>,/tmp/speechd-debug/</i></p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print this info</dl>
<p> Please report bugs to speechd-discuss [at] nongnu.org</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2002-2012 Brailcom, o.p.s.<br />
 This is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. Please see COPYING for more details.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>speech-dispatcher</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>speech-dispatcher</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info speech-dispatcher</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
