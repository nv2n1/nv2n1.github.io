---
title: "sane-nec(5)"
name: "sane-nec"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-nec/"
description: "sane-nec – SANE backend for NEC scanners"
---

<p>sane-nec &#8211; SANE backend for NEC scanners</p>
<h2>Description</h2>
<p>The <code>sane-nec</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to NEC SCSI scanners. This backend should be considered <code>alpha-quality</code> software! In the current state it is known to work with PC-IN500/4C scanners. Other MultiReader scanner series are not supported. PC-IN 500/4C and MultiReader scanner are only sold in Japan (except Multi Reader PetiScan). For other scanners, it may or may not work. The backend has the following known problems:</p>
<dl>
<dd>
<dl>
<dt>&#8211; ColorLineart mode is not supported.</p>
<dd>
<dt>&#8211; Device name is fixed to <i>/dev/scanner</i></p>
<dd></dl>
</dl>
<p> At present, the following scanners are known to work with this backend.</p>
<dl>
<dd>
<pre>Vendor Product id
------ -----------
NEC PC-IN500/4C</pre>
</dl>
<h2>Files</h2>
<dl>
<dt><i>/etc/sane.d/nec.conf</i></p>
<dd>The backend configuration file.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-nec.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-nec.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_NEC</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-scsi/">sane-scsi</a></code>(5) </p>
<h2>Authors</h2>
<p>Kazuya Fukuda</p>
