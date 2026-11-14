---
title: "istanbul(1)"
name: "istanbul"
section: "1"
letter: "i"
url: "/docs/linux/man/1-istanbul/"
description: "istanbul – a desktop session recorder"
---

<h2>NAME</h2>
<p> istanbul &#8211; a desktop session recorder</p>
<h2>SYNOPSIS</h2>
<p> <code>istanbul</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>istanbul</code> command. </p>
<p> <code>istanbul</code> is a program that allow you to record your desktop session. After you started it, you can control it with the icon in the notification area: a click on the icon to start recording, another click to stop. </p>
<p> <code>istanbul</code> preferences can be configured with a right click on the icon.</p>
<dl>
<dt>It can also stream to an Icecast2 server.</p>
<dd></dl>
<p> By default it records to ~/desktop-recording.ogg</p>
<h2>OPTIONS</h2>
<p> Istanbul follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, -?, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>&#8211;usage</code></p>
<dd> Display brief usage message</p>
<dt>Istanbul accepts also GStreamer options.</p>
<dd> A summary of them is included below.</p>
<dt><code>&#8211;gst-version</code></p>
<dd> Print the GStreamer version</p>
<dt><code>&#8211;gst-fatal-warnings</code></p>
<dd> Make all warnings fatal</p>
<dt><code>&#8211;gst-debug-help</code></p>
<dd> Print available debug categories and exit</p>
<dt><code>&#8211;gst-debug-level=LEVEL</code></p>
<dd> Default debug level from 1 (only error) to 5 (anything) or 0 for no output</p>
<dt><code>&#8211;gst-debug=LIST</code></p>
<dd> Comma-separated list of category_name:level pairs to set specific levels for the individual categories</p>
<dt><code>&#8211;gst-debug-no-color</code></p>
<dd> Disable colored debugging output</p>
<dt><code>&#8211;gst-debug-disable</code></p>
<dd> Disable debugging</p>
<dt><code>&#8211;gst-disable-cpu-opt</code></p>
<dd> Disable accelerated CPU instructions</p>
<dt><code>&#8211;gst-plugin-spew</code></p>
<dd> Enable verbose plugin loading diagnostics</p>
<dt><code>&#8211;gst-plugin-path=PATHS</code></p>
<dd> path list for loading plugins (separated by &#8216;:&#8217;)</p>
<dt><code>&#8211;gst-plugin-load=PLUGINS </code></p>
<dd> Comma-separated list of plugins to preload in addition to the list stored in environment variable GST_PLUGIN_PATH</p>
<dt><code>&#8211;gst-disable-segtrap</code></p>
<dd> Disable trapping of segmentation faults during plugin loading</p>
<dt><code>&#8211;gst-scheduler=SCHEDULER</code></p>
<dd> Scheduler to use (default is &#8216;opt&#8217;)</p>
<dt><code>&#8211;gst-registry=REGISTRY</code></p>
<dd> Registry to use</dl>
<h2>AUTHOR</h2>
<p> Istanbul was written by Zaheer Abbas Merali &lt;zaheerabbas [at] merali.org&gt;. </p>
<p> This manual page was written by Luca Bruno &lt;luca.br [at] uno.it&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
