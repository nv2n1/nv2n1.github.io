---
title: "sane-hs2p(5)"
name: "sane-hs2p"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-hs2p/"
description: "sane-hs2p – SANE backend for Ricoh SCSI flatbed/ADF scanners"
---

<p>sane-hs2p &#8211; SANE backend for Ricoh SCSI flatbed/ADF scanners</p>
<h2>Description</h2>
<p>The <code>sane-hs2p</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the Ricoh IS450 family of scanners. Should also work with the IS420, IS410, and IS430 scanners, but these are untested. Please contact the maintainer or the sane-devel mailing list if you own such a scanner. This backend is alpha-quality. It may have bugs and some scanners haven&#8217;t been tested at all. Be careful and pull the plug if the scanner causes unusual noise. </p>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct device. Under Linux, such a device name could be <i>/dev/sg0</i> or <i>/dev/sga</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Configuration</h2>
<p>The contents of the <i>hs2p.conf</i> file is a list of device names that correspond to SCSI scanners. Empty lines and lines starting with a hash mark (#) are ignored. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) on details of what constitutes a valid device name.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/hs2p.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hs2p.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-hs2p.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_HS2P</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. A value of 255 prints all debug output. Smaller values reduce verbosity. </p>
</dl>
<h2>Current Status</h2>
<p>The <code>sane-hs2p</code> backend is now in version 1.00. All major scanning-related features are supported, except for those features requiring the optional IPU. Scanning from the flatbed or ADF (either simplex or duplex) is supported. Lineart, halftone, 4-bit gray, and 8-bit gray are supported. Pre-set gamma tables and halftone patterns are supported, as well as brightness, threshold, contrast. Also supported is scan wait mode, binary and gray filtering, negative scanning, and absolute or relative white setting. Printing with the optional endorser also is supported.</p>
<h2>Planned Functionality</h2>
<p>This scanner can scan from the ADF in continuous simplex mode. Surprisingly, many scanners scan an entire document from the ADF into memory before ejecting the sheet. Thus if the document is too long, the scanner cannot hold the entire image data in memory. But if the scanner would send its image data when its memory got full, and then read the next buffer&#8217;s worth of data, continuous scanning could be achieved.</p>
<h2>Missing Functionality</h2>
<p>The SCSI commands for uploading (2AH) or downloading (28H) custom halftone patterns (02H) and gamma vectors (03H) should work, but require implementing the SANE Option-Value code to allow the user to create the tables to be uploaded to the scanner. No support for Maintenance Data (80H) is planned as this functionality is more suited to a stand-alone utility to be used by a technician when replacing the lamp or ADF unit. Nor is support for reading or changing IPU (93H) parameters and adjustments planned, since my IS450 lacks such a unit. The 31-byte Auto Photo/Letter struct and 21-byte Dynamic threshold struct are documented in the <i>hs2p-scsi.h</i> file should someone wish to use their IPU for image data processing.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5), </p>
<h2>Author</h2>
<p>jeremy &lt;<i>jeremy [at] acjlaw.net</i>&gt;<br />
 Maintained by Jeremy Johnson &lt;<i>jeremy [at] acjlaw.net</i>&gt;</p>
