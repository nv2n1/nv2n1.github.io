---
title: "sane-pnm(5)"
name: "sane-pnm"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-pnm/"
description: "sane-pnm – SANE PNM image reader pseudo-backend"
---

<p>sane-pnm &#8211; SANE PNM image reader pseudo-backend</p>
<h2>Description</h2>
<p>The <code>sane-pnm</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to PNM (Portable aNyMap files, which covers PBM bitmap files, PGM grayscale files, and PPM pixmap files). The purpose of this backend is primarily to aid in debugging of SANE frontends. It also serves as an illustrative example of a minimal SANE backend.</p>
<h2>Device Names</h2>
<p>This backend provides two devices called <code>0</code> and <code>1.</code></p>
<h2>Configuration</h2>
<p>No configuration required.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pnm.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-pnm.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_PNM</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. E.g., a value of 128 requests all debug output to be printed. Smaller levels reduce verbosity. </p>
</dl>
<h2>Bugs</h2>
<p>If the <code>sane-pnm</code> backend is installed and <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) is used to allow users on remote computers to scan on the local machine, PNM files can be read by the remote user. This is limited to the files <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) can access (usually it&#8217;s running as user &quot;sane&quot;). All PNM files can be read if <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) runs as root which isn&#8217;t recommended anyway. The <code>sane-pnm</code> backend is disabled by default. If you want to use it, enable it with configure (see <i>configure &#8211;help</i> for details). Be sure that only trusted users can access the <code>sane-pnm</code> backend over <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8). </p>
<h2>Author</h2>
<p>Andreas Beck, Gordon Matzigkeit, and David Mosberger</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/8-saned/">saned</a></code>(8) </p>
