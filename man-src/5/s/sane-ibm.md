---
title: "sane-ibm(5)"
name: "sane-ibm"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-ibm/"
description: "sane-ibm – SANE backend for IBM and Ricoh SCSI flatbed scanners"
---

<p>sane-ibm &#8211; SANE backend for IBM and Ricoh SCSI flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-ibm</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the IBM 2456 and the Ricoh IS-410, IS-420, and IS-430 flatbed scanners. Support for the IS-410 and IS-430 is untested. Please contact the maintainer or the sane-devel mailing list if you own such a scanner. This backend is alpha-quality. It may have bugs and some scanners haven&#8217;t been tested at all. Be careful and pull the plug if the scanner causes unusual noise. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct device. Under Linux, such a device name could be <i>/dev/sg0</i> or <i>/dev/sga</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>ibm.conf</i> file is a list of device names that correspond to SCSI scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/ibm.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ibm.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ibm.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_IBM</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), </p>
<h2>Author</h2>
<p>mf &lt;<i>massifr [at] tiscalinet.it</i>&gt;<br />
 Maintained by Henning Meier-Geinitz &lt;<i>henning [at] meier-geinitz.de</i>&gt;</p>
