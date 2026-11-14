---
title: "sane-snapscan(5)"
name: "sane-snapscan"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-snapscan/"
description: "sane-snapscan – SANE backend for AGFA SnapScan flatbed scanners"
---

<p>sane-snapscan &#8211; SANE backend for AGFA SnapScan flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-snapscan</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to AGFA SnapScan flatbed scanners. At present, the following scanners are supported from this backend: AGFA SnapScan 300, 310, 600, and 1236s, 1236u, 1212u, e20, e25, e40, e50, e60, Vuego 310s, Acer 300f, 310s, 610s, 610plus, Prisa 620s, Prisa 620u, Prisa 620ut, Prisa 640u, Prisa 640bu, Prisa 1240, Prisa 3300, Prisa 4300, Prisa 5300 and Guillemot Maxi Scan A4 Deluxe (SCSI) (with varying success). </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details. </p>
<p> For USB scanners the devicename must contain the keyword &quot;usb&quot;, as in <i>/dev/usbscanner</i> or <i>/dev/usb/scanner0</i>. For scanners that need a firmware upload before scanning add a line starting with &quot;firmware&quot; followed by the fully qualified path to your firmware file, e.g. </p>
<dl>
<dd>firmware /usr/share/sane/snapscan/firmware.bin</dl>
<p> For further details read <i><a rel="nofollow" href="http://snapscan.sourceforge.net">http://snapscan.sourceforge.net</a></i>.</p>
<h2>Configuration</h2>
<p>The contents of the <i>snapscan.conf</i> file is a list of device names that correspond to SnapScan scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/snapscan.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-snapscan.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-snapscan.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_SNAPSCAN</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Bugs</h2>
<p>Man page doesn&#8217;t provide much information yet. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5),<br />
 <i><a rel="nofollow" href="http://sourceforge.net/projects/snapscan/">http://sourceforge.net/projects/snapscan/</a></i> (new development website) </p>
<h2>Author</h2>
<p>Kevin Charter, Franck Schneider, Michel Roelofs, Emmanuel Blot, Mikko Tyolajarvi, David Mosberger-Tang, Wolfgang Goeller, Petter Reinholdtsen, Gary Plewa, Sebastien Sable, Oliver Schwartz and Mikael Magnusson.<br />
 Man page by Henning Meier-Geinitz (mostly based on the web pages and source code).</p>
