---
title: "boincmgr(1)"
name: "boincmgr"
section: "1"
letter: "b"
url: "/docs/linux/man/1-boincmgr/"
description: "boincmgr – The graphical BOINC manager for the client."
---

<h2>NAME</h2>
<p> boincmgr &#8211; The graphical BOINC manager for the client.</p>
<h2>SYNOPSIS</h2>
<p> <code>boincmgr</code> [<code>&#8211;verbose</code>] [<code>-a</code>] [<code>-e</code> <i>client_dir</i>] [<code>-d</code> <i>data_dir</i>] [<code>-n</code> <i>hostname</i>] [<code>-g</code> <i>port</i>] [<code>-p</code> <i>passwd</i>] [<code>-b</code> <i>BOINC_ARGS</i>] [<code>-i</code>] [<code>-c</code>] [<code>-m</code>] <code>boincmgr</code> [<code>-h</code> | <code>&#8211;help</code>]</p>
<h2>DESCRIPTION</h2>
<p> The BOINC manager (<code>boincmgr</code>) is a graphical controlling and monitoring utility for the BOINC client (<code><a href="/docs/linux/man/1-boinc/">boinc</a></code>(1)). It communicates with a running client using port 31416 over TCP/IP. It can only connect to one client at a time.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show all options.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Generate verbose log messages.</p>
<dt><code>-a</code>, <code>&#8211;autostart</code></p>
<dd> Tells the BOINC Manager that it was started by the operating system automatically. Use this if the Manager is started at login time.</p>
<dt><code>-e</code> <i>client_dir</i>, <code>&#8211;clientdir=</code><i>client_dir</i></p>
<dd> Directory containing the <i>locale</i> directory containing the Manager localisation files.</p>
<dt><code>-d</code> <i>data_dir</i>, <code>&#8211;datadir=</code><i>data_dir</i></p>
<dd> Directory containing the configuration files .</p>
<dt><code>-n</code> <i>hostname</i>, <code>&#8211;namehost=</code><i>hostname</i></p>
<dd> Hostname or IP address of client to which the manager should connect to.</p>
<dt><code>-g</code> <i>port</i>, <code>&#8211;gui_rpc_port=</code><i>port</i></p>
<dd> RPC port number used to communicate with the client. Has to be the same value as on the client (see <code><a href="/docs/linux/man/1-boinc/">boinc</a></code>(1)).</p>
<dt><code>-p</code> <i>passwd</i>, <code>&#8211;password=</code><i>passwd</i></p>
<dd> Use <i>passwd</i> as password for RPC authentication. If the current working directory contains a file <i>gui_rpc_auth.cfg</i>, <code>boincmgr</code> will read the password from this file.</p>
<dt><code>-b</code> <i>BOINC_ARGS</i>, <code>&#8211;boincargs=</code><i>BOINC_ARGS</i></p>
<dd> Startup the BOINC client with these optional arguments if necessary.</p>
<dt><code>-i</code>, <code>&#8211;insecure</code></p>
<dd> Disable BOINC security users and permissions.</p>
<dt><code>-c</code>, <code>&#8211;checkskins</code></p>
<dd> Set skin debugging mode to enable skin manager error messages.</p>
<dt><code>-m</code>, <code>&#8211;multiple</code></p>
<dd> Allow multiple instances of BOINC manager on this host.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-boinc/">boinc</a></code>(1), <code><a href="/docs/linux/man/1-boinccmd/">boinccmd</a></code>(1) </p>
<p> &lt;<a rel="nofollow" href="http://boinc.berkeley.edu/wiki/The_BOINC_Manager">http://boinc.berkeley.edu/wiki/The_BOINC_Manager</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2007-2013 University of California. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, no Front-Cover Texts, and no Back-Cover Texts. </p>
<h2>Index</h2>
