---
title: "gsmartcontrol(1)"
name: "gsmartcontrol"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gsmartcontrol/"
description: "GSmartControl – Hard disk drive health inspection tool"
---

<h2>NAME</h2>
<p> GSmartControl &#8211; Hard disk drive health inspection tool</p>
<h2>SYNOPSIS</h2>
<p> <code>gsmartcontrol</code> [OPTIONS]</p>
<h2>DESCRIPTION</h2>
<p> <code>GSmartControl</code> is a graphical user interface for smartctl (from smartmontools), which is a tool for querying and controlling SMART (Self-Monitoring, Analysis, and Reporting Technology) data on modern hard disk drives. It allows you to inspect the drive&#8217;s SMART data to determine its health, as well as run various tests on it. </p>
<p> This manual page documents briefly the <code>gsmartcontrol</code> command. </p>
<h2>OPTIONS</h2>
<h3>Help Options:</h3>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ options</p>
<dt><code>&#8211;help-debug</code></p>
<dd> Show logging options</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>-l</code>, <code>&#8211;no-locale</code></p>
<dd> Don&#8217;t use system locale</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information</p>
<dt><code>&#8211;no-scan</code></p>
<dd> Don&#8217;t scan devices on startup</p>
<dt><code>&#8211;no-hide-tabs</code></p>
<dd> Don&#8217;t hide non-identity tabs when SMART is disabled. Useful for debugging.</p>
<dt><code>&#8211;add-virtual</code></p>
<dd> Load smartctl data from file, creating a virtual drive. You can specify this option multiple times.</p>
<dt><code>&#8211;add-device</code></p>
<dd> Add this device to device list. The format of the device is <i>&lt;device&gt;::&lt;type&gt;::&lt;extra_args&gt;</i>, where type and extra_args are optional. This option is useful with <code>&#8211;no-scan</code> to list certain drives only. You can specify this option multiple times. Example: </p>
<pre>
--add-device /dev/sda --add-device /dev/twa0::3ware,2 --add-device '/dev/sdb::::-T permissive'
</pre>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Enable verbose logging; same as <code>&#8211;verbosity-level</code> 5</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Disable logging; same as <code>&#8211;verbosity-level</code> 0</p>
<dt><code>-b</code>, <code>&#8211;verbosity-level</code></p>
<dd> Set verbosity level [0-5]</dl>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2008 &#8211; 2012 Alexander Shaduri &lt;ashaduri &#8216;at&#8217; gmail.com&gt; </p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Giuseppe Iuculano &lt;giuseppe [at] iuculano.it&gt; for the Debian project. </p>
<h2>Index</h2>
