---
title: "sane-st400(5)"
name: "sane-st400"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-st400/"
description: "sane-st400 – SANE backend for Siemens ST/Highscan flatbed scanners"
---

<p>sane-st400 &#8211; SANE backend for Siemens ST/Highscan flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-st400</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to Siemens ST400 flatbed scanners and compatibles. At present, the following scanners are supported by this backend:</p>
<dl>
<dd>Siemens ST400 (6 bit gray scale)<br />
 Siemens ST800 (6 bit gray scale)
</dl>
<p> The driver supports line art and gray scans up to 8bpp. The Siemens ST/Highscan series includes several more models, e.g. the ST300 and ST600. If you own one of these scanners, or a scanner other than the ones listed above that works with this backend, please let us know by sending the scanner&#8217;s model name, SCSI ID, and firmware revision to <i>sane-devel [at] alioth-lists.debian.net</i>. Have a look at <i><a rel="nofollow" href="http://www.sane-project.org/mailing-lists.html">http://www.sane-project.org/mailing-lists.html</a></i> concerning subscription to sane-devel. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. For SCSI scanners, the special device name must be a generic SCSI device or a symlink to such a device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>st400.conf</i> file is a list of device names that correspond to Siemens scanners. Empty lines and lines starting with a hash mark (#) are ignored. A sample configuration file is shown below: </p>
<dl>
<dd>/dev/scanner<br />
 # this is a comment<br />
 /dev/sge</dl>
<p> The default configuration file that is distributed with SANE looks like this: </p>
<dl>
<dd>scsi SIEMENS &quot;ST 400&quot; Scanner * * 3 0</dl>
<p> In this configuration, the driver can only access the ST400 model at SCSI ID 3 LUN 0 (see section <code>BUGS</code> below for the reason). To use the driver with other scanner models, add an appropriate line to the configuration file. For example, to use it with an ST800 at SCSI ID 3 LUN 0, add the line: </p>
<dl>
<dd>scsi SIEMENS &quot;ST 800&quot; Scanner * * 3 0</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/st400.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-st400.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-st400.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_ST400</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Missing Functionality</h2>
<p>Everything but the most basic stuff.</p>
<h2>Bugs</h2>
<p>Currently, the backend does not check if the attached device really is a ST400. It will happily accept everything that matches the configuration entries. This makes it easy to test the backend with other scanners: Just add an appropriate line to the configuration file. The configuration file as distributed (see above) only works with the ST400. Be careful: If there is no config file at all, the backend defaults to <i>/dev/scanner</i>. The ST400 answers on all eight SCSI LUNs. Normally this is not a problem, as LUN support is usually disabled in SCSI drivers, but if you are seeing multiple instances of the scanner in a device list, either disable LUNs in your SCSI setup or change the entry in the configuration file to match LUN 0 only. </p>
<h2>Debug</h2>
<p>If you encounter a bug please set the environment variable <code>SANE_DEBUG_ST400</code> to 128 and try to regenerate the problem. Then send me a report with the log attached. </p>
<p> If you encounter a SCSI bus error or trimmed and/or displaced images please also set the environment variable <code>SANE_DEBUG_SANEI_SCSI</code> to 128 before sending me the report.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5)<br />
 <i><a rel="nofollow" href="http://www.informatik.uni-oldenburg.de/~ingo/sane/">http://www.informatik.uni-oldenburg.de/~ingo/sane/</a></i> </p>
<h2>Author</h2>
<p>Ingo Wilken &lt;<i>Ingo.Wilken [at] informatik.uni-oldenburg.de</i>&gt;</p>
