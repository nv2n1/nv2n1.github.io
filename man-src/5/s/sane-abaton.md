---
title: "sane-abaton(5)"
name: "sane-abaton"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-abaton/"
description: "sane-abaton – SANE backend for Abaton flatbed scanners"
---

<p>sane-abaton &#8211; SANE backend for Abaton flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-abaton</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Abaton flatbed scanners. At present, only the Scan 300/GS (8bit, 256 levels of gray) is fully supported, due to the absence of programming information. The Scan 300/S (black and white) is recognized, but support for it is untested. If you own a Abaton scanner other than the ones listed above that works with this backend, or if you own an Abaton scanner that does not work with this backend, please contact <i>sane-devel [at] alioth-lists.debian.net</i> with the model number, so that arrangements can be made to include support for it. Have a look at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> concerning subscription to sane-devel. Abaton is out of business, and these scanners are not supported by Everex (the parent company of Abaton), nor is there any programming information to be found. This driver is therefore based on information obtained by running Abaton&#8217;s scanning desk accessory under MacsBug and tracing the MacOS SCSI Manager calls it made during image acquisition. However, the protocol is very similar to, though not compatible with, the one used by the Apple scanners, therefore, if this backend is ever extended to support the other Abaton models (they also made a color flatbed scanner), it may be possible to fill in some &quot;missing pieces&quot; from the (quite detailed) Apple scanner documentation. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name takes a format such as <i>/dev/sga</i> or <i>/dev/sg0</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>abaton.conf</i> file is a list of device names that correspond to Abaton scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/abaton.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-abaton.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-abaton.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_ABATON</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 255 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Bugs</h2>
<p>There are a few known ones, and definitely some unknown ones.</p>
<dl>
<dt><code>Scan area miscalculations</code></p>
<dd>For the sake of programmer efficiency, this backend handles all measurements in millimetres, and floors (rather than rounds) values to avoid possible damage to the scanner mechanism. Therefore, it may not be possible to scan to the extreme right or bottom edges of the page.</p>
<dt><code>Cancelling the scan</code></p>
<dd>This might not work correctly, or it might abort the frontend. The former is more likely than the latter.</dl>
<p> If you have found something that you think is a bug, please attempt to recreate it with the SANE_DEBUG_ABATON environment variable set to 255, and send a report detailing the conditions surrounding the bug to <i>sane-devel [at] alioth-lists.debian.net</i>. </p>
<h2>Todo</h2>
<dl>
<dt><code>Implement non-blocking support</code></p>
<dd>
<dt><code>Finish reverse-engineering the MacOS driver</code></p>
<dd>This will allow me to add support for other models with reasonable confidence that it will work, as well as to fully exploit the information returned by the INQUIRY command. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) </p>
<h2>Author</h2>
<p>The <code>sane-abaton</code> backend was partially written by David Huggins-Daines, based on the <code><a href="/docs/linux/man/5-sane-apple/">sane-apple</a></code>(5) backend by Milon Firikis.</p>
