---
title: "chicken-status(1)"
name: "chicken-status"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chicken-status/"
description: "chicken-status – list installed extension libraries"
---

<h2 class="name">NAME</h2>
<p> chicken-status &#8211; list installed extension libraries</p>
<h2>SYNOPSIS</h2>
<p> chicken-status [OPTION | PATTERN] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>chicken-status</i> lists installed extensions for the CHICKEN Scheme system matching the regular expression(s) <code>PATTERN</code> or all, if no pattern has been given. </p>
<h2>OPTIONS</h2>
<p> Enter <code>chicken-status -help</code> for a list of supported command-line options. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CHICKEN_PREFIX</code></p>
<dd> The installation prefix where CHICKEN Scheme and its support files and libraries are located. Defaults to the installation time prefix given when configuring the system. </p>
<dt><code>CHICKEN_REPOSITORY</code></p>
<dd> The path where extension libraries are installed. Defaults to the package-library path selected during configuration (usually <code>$prefix/lib/chicken/&lt;binary-version&gt;</code> ) </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> More information can be found in the <i>CHICKEN User&#8217;s Manual</i> </p>
<h2>BUGS</h2>
<p> Submit bug reports by e-mail to <i>chicken-janitors [at] nongnu.org</i> , preferrably using the <code>chicken-bug</code> tool. </p>
<h2>AUTHORS</h2>
<p> The CHICKEN Team </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chicken-install/">chicken-install</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-uninstall/">chicken-uninstall</a>(1)</code> <code><a href="/docs/linux/man/1-chicken/">chicken</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-bug/">chicken-bug</a>(1)</code> </p>
<h2>Index</h2>
