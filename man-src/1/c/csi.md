---
title: "csi(1)"
name: "csi"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csi/"
description: "The CHICKEN Scheme interpreter"
---

<h2 class="name">NAME</h2>
<p> The <i>CHICKEN</i> Scheme interpreter</p>
<h2>SYNOPSIS</h2>
<p> <code>csi</code> [ <i>pathname</i> | <i>option &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>csi</i> is an interpreter for the programming language <i>Scheme</i> supporting most of the features as described in the <i>Revised^5 Report on</i> <i>the Algorithmic Language Scheme</i> . <i>csi</i> is implemented as a program compiled with the <code>chicken</code> compiler. </p>
<h2>OPTIONS</h2>
<p> Enter <code>csi -help</code> for a list of supported command-line options. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CHICKEN_INCLUDE_PATH</code></p>
<dd> Contains one or more pathnames where the interpreter should also look for include-files, separated by <code>;</code> characters. </p>
<dt><code>CHICKEN_PREFIX</code></p>
<dd> Is used as a prefix directory for support files, include-files and libraries. </p>
<dt><code>CSI_OPTIONS</code></p>
<dd> When set to a string of command-line options, then the options are passed implicitly to every direct or indirect invocation of <i>csi</i><br />
 Note that runtime options of the form <code>-:&#8230;</code> can not be passed using this method. </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> More information can be found in the <i>CHICKEN User&#8217;s Manual</i> </p>
<h2>BUGS</h2>
<p> Submit bug reports by e-mail to <i>chicken-janitors [at] nongnu.org</i> , preferrably using the <code>chicken-bug</code> tool. </p>
<h2>AUTHOR</h2>
<p> The CHICKEN Team </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chicken/">chicken</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-bug/">chicken-bug</a>(1)</code> </p>
<h2>Index</h2>
