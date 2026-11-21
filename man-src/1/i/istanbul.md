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
<p> <code>istanbul</code> [options]</p>
<p> This manual page documents briefly the <code>istanbul</code> command. </p>
<p> <code>istanbul</code> is a program that allow you to record your desktop session. After you started it, you can control it with the icon in the notification area: a click on the icon to start recording, another click to stop. </p>
<p> <code>istanbul</code> preferences can be configured with a right click on the icon.</p>
<dl>
<dt>It can also stream to an Icecast2 server.</dt>
<dd></dd></dl>
<p> By default it records to ~/desktop-recording.ogg</p>
<h2>OPTIONS</h2>
<p> Istanbul follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, -?, &#8211;help</code></dt>
<dd> Show summary of options.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Show version of program.</dd>
<dt><code>&#8211;usage</code></dt>
<dd> Display brief usage message</dd>
<dt>Istanbul accepts also GStreamer options.</dt>
<dd> A summary of them is included below.</dd>
<dt><code>&#8211;gst-version</code></dt>
<dd> Print the GStreamer version</dd>
<dt><code>&#8211;gst-fatal-warnings</code></dt>
<dd> Make all warnings fatal</dd>
<dt><code>&#8211;gst-debug-help</code></dt>
<dd> Print available debug categories and exit</dd>
<dt><code>&#8211;gst-debug-level=LEVEL</code></dt>
<dd> Default debug level from 1 (only error) to 5 (anything) or 0 for no output</dd>
<dt><code>&#8211;gst-debug=LIST</code></dt>
<dd> Comma-separated list of category_name:level pairs to set specific levels for the individual categories</dd>
<dt><code>&#8211;gst-debug-no-color</code></dt>
<dd> Disable colored debugging output</dd>
<dt><code>&#8211;gst-debug-disable</code></dt>
<dd> Disable debugging</dd>
<dt><code>&#8211;gst-disable-cpu-opt</code></dt>
<dd> Disable accelerated CPU instructions</dd>
<dt><code>&#8211;gst-plugin-spew</code></dt>
<dd> Enable verbose plugin loading diagnostics</dd>
<dt><code>&#8211;gst-plugin-path=PATHS</code></dt>
<dd> path list for loading plugins (separated by &#8216;:&#8217;)</dd>
<dt><code>&#8211;gst-plugin-load=PLUGINS </code></dt>
<dd> Comma-separated list of plugins to preload in addition to the list stored in environment variable GST_PLUGIN_PATH</dd>
<dt><code>&#8211;gst-disable-segtrap</code></dt>
<dd> Disable trapping of segmentation faults during plugin loading</dd>
<dt><code>&#8211;gst-scheduler=SCHEDULER</code></dt>
<dd> Scheduler to use (default is &#8216;opt&#8217;)</dd>
<dt><code>&#8211;gst-registry=REGISTRY</code></dt>
<dd> Registry to use</dd></dl>
<h2>AUTHOR</h2>
<p> Istanbul was written by Zaheer Abbas Merali &lt;zaheerabbas [at] merali.org&gt;. </p>
<p> This manual page was written by Luca Bruno &lt;luca.br [at] uno.it&gt;, for the Debian project (but may be used by others). </p>
