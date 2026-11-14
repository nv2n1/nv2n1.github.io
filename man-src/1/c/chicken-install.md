---
title: "chicken-install(1)"
name: "chicken-install"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chicken-install/"
description: "chicken-install – download and install extension libraries for CHICKEN Scheme"
---

<h2 class="name">NAME</h2>
<p> chicken-install &#8211; download and install extension libraries for CHICKEN Scheme</p>
<h2>SYNOPSIS</h2>
<p> chicken-install [OPTION | EXTENSION[:VERSION]] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <i>chicken-install</i> is a program that downloads, compiles and installs a prepackaged extension library from sources. If no extension name is given on the command-line, then any existing <code>setup</code> scripts in the current directory will be executed in some unspecified order. </p>
<h2>OPTIONS</h2>
<p> Enter <code>chicken-install -help</code> for a list of supported command-line options. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CHICKEN_PREFIX</code></p>
<dd> The installation prefix where CHICKEN Scheme and its support files and libraries are located. Defaults to the installation time prefix given when configuring the system. </p>
<dt><code>CHICKEN_INSTALL_PREFIX</code></p>
<dd> An alternative installation prefix that will be prepended to extension installation paths if specified. </p>
<dt><code>CHICKEN_REPOSITORY</code></p>
<dd> The path where extension libraries are installed. Defaults to the package-library path selected during configuration (usually <code>$prefix/lib/chicken/&lt;binary-version&gt;</code> ) </p>
<dt><code>SUDO</code></p>
<dd> The command to execute when using -s flag in command. If not provided, defaults to the <a href="/docs/linux/man/1-sudo/">sudo</a>(1). </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> More information can be found in the <i>CHICKEN User&#8217;s Manual</i> </p>
<h2>BUGS</h2>
<p> Submit bug reports by e-mail to <i>chicken-janitors [at] nongnu.org</i> , preferrably using the <code>chicken-bug</code> tool. </p>
<h2>AUTHORS</h2>
<p> The CHICKEN Team </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chicken-uninstall/">chicken-uninstall</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-status/">chicken-status</a>(1)</code> <code><a href="/docs/linux/man/1-chicken/">chicken</a>(1)</code> <code><a href="/docs/linux/man/1-csc/">csc</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-bug/">chicken-bug</a>(1)</code> </p>
<h2>Index</h2>
