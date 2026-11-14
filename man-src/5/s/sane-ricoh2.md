---
title: "sane-ricoh2(5)"
name: "sane-ricoh2"
section: "5"
letter: "s"
url: "/docs/linux/man/5-sane-ricoh2/"
description: "sane-ricoh2 – SANE backend for Ricoh flatbed scanners"
---

<p>sane-ricoh2 &#8211; SANE backend for Ricoh flatbed scanners</p>
<h2>Description</h2>
<p>The <code>sane-ricoh2</code> library implements a SANE (Scanner Access Now Easy) backend that provides access to the following Ricoh flatbed scanners:</p>
<dl>
<dd>SG-3110SFNw<br />
 SG-3100SNw<br />
 SP-100SU<br />
 SP-111SU (SP-112SU)</dl>
<h2>Files</h2>
<dl>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ricoh2.a</i></p>
<dd>The static library implementing this backend.</p>
<dt><i>/usr/lib/x86_64-linux-gnu/sane/libsane-ricoh2.so</i></p>
<dd>The shared library implementing this backend (present on systems that support dynamic loading). </p>
</dl>
<h2>Options</h2>
<p>The options the backend supports can either be selected through command line options to programs like <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1) or through GUI elements in programs like <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1) or <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1). </p>
<p> The following options are supported by ricoh2: </p>
<p> <code>&#8211;mode color|gray</code> </p>
<dl>
<dd>Color or grayscale mode.</dl>
<p> <code>&#8211;resolution 300|600</code> </p>
<dl>
<dd>DPI resolution. </p>
</dl>
<h2>Environment</h2>
<dl>
<dt><code>SANE_DEBUG_RICOH2</code></p>
<dd>If the library was compiled with debug support enabled, this environment variable controls the debug level for this backend. Higher debug levels increase the verbosity of the output. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-sane/">sane</a></code>(7), <code><a href="/docs/linux/man/5-sane-usb/">sane-usb</a></code>(5), <code><a href="/docs/linux/man/1-scanimage/">scanimage</a></code>(1), <code><a href="/docs/linux/man/1-xscanimage/">xscanimage</a></code>(1), <code><a href="/docs/linux/man/1-xsane/">xsane</a></code>(1) </p>
<h2>Author</h2>
<p>Stanislav Yuzvinsky</p>
