---
title: "sane-agfafocus(5)"
name: "sane-agfafocus"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-agfafocus/"
description: "sane-agfafocus – SANE backend for AGFA Focus flatbed scanners"
---

<p>sane-agfafocus &#8211; SANE backend for AGFA Focus flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-agfafocus</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to AGFA Focus flatbed scanners. At present, the following scanners are supported from this backend:</p>
<dl>
<dd>AGFA Focus GS Scanner (6 bit gray scale) (untested)<br />
 AGFA Focus Lineart Scanner (lineart) (untested)<br />
 AGFA Focus II (8 bit gray scale) (untested)<br />
 AGFA Focus Color (24 bit color 3-pass)<br />
 AGFA Focus Color Plus (24 bit color 3-pass)<br />
 Siemens S9036 (8 bit gray scale) (untested)
</dl>
<p> The driver supports line art, 6bpp and 8bpp gray, 18bpp and 24bpp color scans. If you own a scanner other than the ones listed above that works with this backend, please let us know by sending the scanner&#8217;s model name, SCSI id, and firmware revision to <i>sane-devel [at] alioth-lists.debian.net</i>. Have a look at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> concerning subscription to sane-devel. All of these scanners are pre-SCSI-2, and do not even report properly to SCSI Inquiry. This is typically evident in SCSI bus scans, where the scanner will come up with only garbage as vendor and models strings. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>agfafocus.conf</i> file is a list of device names that correspond to AGFA Focus scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/scanner<br />
 # this is a comment<br />
 /dev/sge</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/agfafocus.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/libsane-agfafocus.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/libsane-agfafocus.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_AGFAFOCUS</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. <code>SANE_DEBUG_AGFAFOCUS</code> values: </p>
<pre>Number Remark
 0 print important errors (printed each time)
 1 print errors
 2 print sense
 3 print warnings
 4 print scanner-inquiry
 5 print information
 6 print less important information
 7 print called procedures
 8 print reader_process messages
 10 print called sane-init-routines
 11 print called sane-procedures
 12 print sane infos
 13 print sane option-control messages</pre>
</dl>
<h2>Missing Functionality</h2>
<p>Uploading of dither matrices and tonecurves has been implemented, but so far has not proven to be useful for anything. For this reason these options have been disabled.</p>
<h2>Bugs</h2>
<p>The scanners that do not support disconnect have problems with SCSI timeouts if the SCSI bus gets loaded, eg. if you do a kernel build at the same time as scanning. To see if your scanner supports disconnect, run <i>SANE_DEBUG_AGFAFOCUS=128 scanimage -L</i> in a terminal and look for the &quot;disconnect:&quot; line. </p>
<h2>Debug</h2>
<p>If you have problems with SANE not detecting your scanner, make sure the Artec backend is disabled. Somehow, this backend causes at least my scanner not to respond correctly to SCSI inquiry commands. </p>
<p> If you encounter a bug please set the environment variable <code>SANE_DEBUG_AGFAFOCUS</code> to 128 and try to regenerate the problem. Then send me a report with the log attached. </p>
<p> If you encounter a SCSI bus error or trimmed and/or displaced images please also set the environment variable <code>SANE_DEBUG_SANEI_SCSI</code> to 128 before sending me the report.</p>
<h2>Todo</h2>
<dl>
<dt><code>More scanners?</code></p>
<dd>The AGFA ACS and ARCUS scanners are similar to the FOCUS scanners. The driver could probably be extended to support these scanners without too many changes. I do not have access to such scanners, and cannot add support for it. However, if you are in possession of such a scanner, I could be helpful in adding support for these scanners. </p>
<p> The AGFA HORIZON scanners are SCSI-2 scanners, and it would probably be easier to support these scanners in a SCSI-2 compliant backend. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>Ingo Schneider and Karl Anders &Oslash;ygard.</p>
