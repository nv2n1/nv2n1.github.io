---
title: "sane-tamarack(5)"
name: "sane-tamarack"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-tamarack/"
description: "sane-tamarack – SANE backend for Tamarack flatbed scanners"
---

<p>sane-tamarack &#8211; SANE backend for Tamarack flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-tamarack</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Tamarack flatbed scanners:</p>
<dl>
<dd>Artiscan 6000C<br />
 Artiscan 8000C<br />
 Artiscan 12000C
</dl>
<h2>Device Names</h2>
<p>This backend expects device names of the form: </p>
<dl>
<dd><i>special</i></dl>
<p> Where <i>special</i> is the path-name for the special device that corresponds to a SCSI scanner. The special device name must be a generic SCSI device or a symlink to such a device. The program <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1) helps to find out the correct device. Under Linux, such a device name could be <i>/dev/sga</i> or <i>/dev/sge</i>, for example. See <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) for details.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/tamarack.conf</i></p>
<dd>The backend configuration file (see also description of <code>SANE_CONFIG_DIR</code> below).</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-tamarack.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-tamarack.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading).</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_CONFIG_DIR</code></p>
<dd>This environment variable specifies the list of directories that may contain the configuration file. On *NIX systems, the directories are separated by a colon (`:&#8217;), under OS/2, they are separated by a semi-colon (`;&#8217;). If this variable is not set, the configuration file is searched in two default directories: first, the current working directory (&quot;.&quot;) and then in <i>/etc/sane.d</i>. If the value of the environment variable ends with the directory separator character, then the default directories are searched after the explicitly specified directories. For example, setting <code>SANE_CONFIG_DIR</code> to &quot;/tmp/config:&quot; would result in directories <i>tmp/config</i>, <i>.</i>, and <i>/etc/sane.d</i> being searched (in this order).</p>
<dt><code>SANE_DEBUG_TAMARACK</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
<p> Example: export SANE_DEBUG_TAMARACK=4 </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7)<code>,</code> <code><a href="/docs/linux/man/1-sane-find-scanner/">sane-find-scanner</a></code>(1), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Author</h2>
<p>Roger Wolff</p>
