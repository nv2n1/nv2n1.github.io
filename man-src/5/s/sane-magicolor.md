---
title: "sane-magicolor(5)"
name: "sane-magicolor"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-magicolor/"
description: "sane-magicolor – SANE backend for KONICA MINOLTA magicolor scanners"
---

<p>sane-magicolor &#8211; SANE backend for KONICA MINOLTA magicolor scanners</p>
<h2>Description</h2>
<p>The <code>sane-magicolor</code> backend supports KONICA MINOLTA magicolor scanners connected via USB or LAN. Currently, only the magicolor 1690MF device is supported, no other devices with the same scanning protocol are known.</p>
<h2>Supported Devices</h2>
<p>The following scanner should work with this backend: </p>
<p> Device Details<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
 Vendor: KONICA MINOLTA<br />
 Model: magicolor 1690MF</p>
<h2>Configuration</h2>
<p>This section describes the backend&#8217;s configuration file entries. The file is located at:</p>
<dl>
<dd><i>/etc/sane.d/magicolor.conf</i></dl>
<p> For a proper setup, at least one of the following entries are needed:</p>
<dl>
<dd><i>net autodiscovery</i><br />
 <i>net [IP ADDRESS] [DEVICE-ID]</i><br />
 <i>usb</i><br />
 <i>usb [VENDOR-ID] [DEVICE-ID]</i> </p>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/magicolor.conf</i></p>
<dd>The backend configuration file</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-magicolor.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-magicolor.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>/tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_MAGICOLOR</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_MAGICOLOR=127 </p>
<p> To obtain debug messages from the backend, set this environment variable before calling your favorite frontend (e.g. <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1)). </p>
<p> Example: SANE_DEBUG_MAGICOLOR=65 xscanimage</dl>
<h2>Known Bugs And Restrictions</h2>
<p>Large color scans may sometimes timeout due to unknown reasons (the scanner simply stops returning data). </p>
<p> Cancelling large scans may lock up the scanner.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7),<br />
 <i><a rel="nofollow" href="http://wiki.kainhofer.com/hardware/magicolor_scan">http://wiki.kainhofer.com/hardware/magicolor_scan</a></i> </p>
<h2>Author</h2>
<p>Reinhold Kainhofer &lt;<i>reinhold [at] kainhofer.com</i>&gt;</p>
