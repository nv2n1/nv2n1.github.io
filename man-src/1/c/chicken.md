---
title: "chicken(1)"
name: "chicken"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chicken/"
description: "chicken – A Scheme-to-C translator"
---

<h2 class="name">NAME</h2>
<p> chicken &#8211; A Scheme-to-C translator</p>
<h2>SYNOPSIS</h2>
<p> <code>chicken</code> <i>PATHNAME</i> [ <i>OPTION &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>CHICKEN</i> is a compiler and interpreter for the programming language <i>Scheme</i> supporting most of the features as described in the <i>Revised^5 Report on</i> <i>the Algorithmic Language Scheme</i> . The <code>chicken</code> program is the basic Scheme-to-C translator used in this system. For a more convenient interface, see the manual page for <a href="/docs/linux/man/1-csc/">csc</a>(1). </p>
<h2>OPTIONS</h2>
<p> Enter <code>chicken -help</code> for a list of supported command-line options. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>CHICKEN_PREFIX</code></p>
<dd> Is used as a prefix directory for support files, include-files and libraries. </p>
<dt><code>CHICKEN_INCLUDE_PATH</code></p>
<dd> Contains one or more pathnames where the compiler should additionally look for include-files, separated by <code>;</code> characters. </p>
<dt><code>CHICKEN_OPTIONS</code></p>
<dd> Holds a string of default compiler options that should apply to every invocation of <code>chicken</code> . </p>
</dl>
<h2>DOCUMENTATION</h2>
<p> More information can be found in the <i>CHICKEN User&#8217;s Manual</i> </p>
<h2>AUTHORS</h2>
<p> The CHICKEN Team. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-csc/">csc</a>(1)</code> <code><a href="/docs/linux/man/1-chicken-bug/">chicken-bug</a>(1)</code> </p>
<h2>Index</h2>
