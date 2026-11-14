---
title: "lirc-lsplugins(1)"
name: "lirc-lsplugins"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lirc-lsplugins/"
description: "lirc-lsplugins – print dynamic modules info"
---

<h2>NAME</h2>
<p> lirc-lsplugins &#8211; print dynamic modules info</p>
<h2>SYNOPSIS</h2>
<p> <code>lirc-lsplugins</code> <i>[-l] [-q] [-U plugindir]</i> <i>[drivers]</i><br />
 <code>lirc-lsplugins</code> <i>-e [-q] [-U plugindir]</i><br />
 <code>lirc-lsplugins</code> <i>-e [-q|-p|-h|-v]</i></p>
<h2>DESCRIPTION</h2>
<p> Tool which writes a simple list with info for each driver found. In particular, it writes info if a plugin can&#8217;t be loaded e. g., due to unresolved references. </p>
<p> The <i>[drivers]</i> argument is an optional selector which limits the output to matching drivers. The match is a glob-type match as done by fnmatch()</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-U</code> <code>&#8211;plugindir &lt;path&gt;</code></p>
<dd> Use &lt;path&gt; to search for plugins. The path is a&#8217;:&#8217;-separated search path similar to e. g., $PATH.</p>
<dt><code>-q</code> <code>&#8211;quiet</code></p>
<dd> Don&#8217;t write headers and trailing legend.</p>
<dt><code>-s</code> <code>&#8211;summary</code></p>
<dd> Just write a summary over number of plugins, drivers and errors.</p>
<dt><code>-e</code> <code>&#8211;errors</code></p>
<dd> Only list plugins which can&#8217;t be loaded, or does not contain any drivers.</p>
<dt><code>-l</code> <code>&#8211;long</code></p>
<dd> Add info on driver features.</p>
<dt><code>-p</code> <code>&#8211;default-path</code></p>
<dd> Print default search path and exit.</p>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> Display usage summary.</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> Display version info.</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd> $ lirc-lsplugins -U ../lib/.libs:/usr/local/lib/lirc/plugins tira*</dl>
<p> Lists all drivers with name matching &#8216;tira*&#8217; found in plugins living in ../lib/.libs or /usr/local/lib/lirc/plugins.</p>
<h2>RETURN VALUE</h2>
<p> lirc-lsplugins returns a non-zero error code if there is at least one plugin from which no driver can be loaded or options and parameters can&#8217;t be parsed. Otherwise it returns zero.</p>
<h2>BUGS</h2>
<p> Some drivers change their capabilities in runtime after inspecting the underlying hardware. These runtime capabilities can not be listed by lirc-lsplugins.</p>
<h2>STATUS</h2>
<p> This tool is in an early alpha stage. Both the output format and the command line syntax are subject to change.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3)<br />
 <a href="/docs/linux/man/8-lircd/">lircd</a>(8) </p>
<h2>Index</h2>
