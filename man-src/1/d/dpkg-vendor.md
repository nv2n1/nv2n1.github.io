---
title: "dpkg-vendor(1)"
name: "dpkg-vendor"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dpkg-vendor/"
description: "dpkg-vendor – queries information about distribution vendors"
---

<h2 class="name">NAME</h2>
<p> dpkg-vendor &#8211; queries information about distribution vendors </p>
<h2>SYNOPSIS</h2>
<p> <code>dpkg-vendor</code> [<i>option</i>&#8230;] <i>command</i></p>
<h2>DESCRIPTION</h2>
<p> <code>dpkg-vendor</code> is a tool to query information about vendors listed in <code>/etc/dpkg/origins</code>. <code>/etc/dpkg/origins/default</code> contains information about the current vendor.</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>&#8211;is</code> <i>vendor</i></p>
<dd> Exits with <code>0</code> if the current vendor is <i>vendor</i>. Otherwise exits with <code>1</code>.</p>
<dt><code>&#8211;derives-from</code> <i>vendor</i></p>
<dd> Exits with <code>0</code> if the current vendor distribution is a derivative of <i>vendor</i>, otherwise exits with <code>1</code>. It uses the <code>Parent</code> field to browse all ancestors of the current vendor.</p>
<dt><code>&#8211;query</code> <i>field</i></p>
<dd> Print on standard output the value of the vendor-specific <i>field</i> for the current vendor.</p>
<dt><code>&#8211;help</code></p>
<dd> Show the usage message and exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Show the version and exit.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;vendor</code> <i>vendor</i></p>
<dd> Assumes the current vendor is <i>vendor</i> instead of discovering it with the <font SIZE="-1"><code>DEB_VENDOR</code></font> environment variable or <code>/etc/dpkg/origins/default</code>.</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><font SIZE="-1"><code>DEB_VENDOR</code></font></p>
<dd> This setting defines the current vendor. If not set, it will discover the current vendor by reading <code>/etc/dpkg/origins/default</code>.</p>
<dt><font SIZE="-1"><code>DPKG_COLORS</code></font></p>
<dd> Sets the color mode (since dpkg 1.18.5). The currently accepted values are: <code>auto</code> (default), <code>always</code> and <code>never</code>.</p>
<dt><font SIZE="-1"><code>DPKG_NLS</code></font></p>
<dd> If set, it will be used to decide whether to activate Native Language Support, also known as internationalization (or i18n) support (since dpkg 1.19.0). The accepted values are: <code>0</code> and <code>1</code> (default).</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-deb-origin/">deb-origin</a></code>(5). </p>
<h2>Index</h2>
