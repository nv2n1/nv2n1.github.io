---
title: "config-guess(1)"
name: "config-guess"
section: "1"
letter: "c"
url: "/docs/linux/man/1-config-guess/"
description: "config.guess – guess the build system triplet"
---

<p>config.guess &#8211; guess the build system triplet </p>
<h2>Synopsis</h2>
<p><code>config.guess</code> [<i>,OPTION/</i>]</p>
<h2>Description</h2>
<p>The GNU build system distinguishes three types of machines, the `build&#8217; machine on which the compilers are run, the `host&#8217; machine on which the package being built will run, and, exclusively when you build a compiler, assembler etc., the `target&#8217; machine, for which the compiler being built will produce code. </p>
<p> This script will guess the type of the `build&#8217; machine. </p>
<p> Output the configuration name of the system `config.guess&#8217; is run on.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>print this help, then exit</p>
<dt><code>-t</code>, <code>&#8211;time-stamp</code></p>
<dd>print date of last modification, then exit</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>print version number, then exit</dl>
<h2>Environment Variables</h2>
<p>config.guess might need to compile and run C code, hence it needs a compiler for the `build&#8217; machine: use the environment variable `CC_FOR_BUILD&#8217; to specify the compiler for the build machine. If `CC_FOR_BUILD&#8217; is not specified, `CC&#8217; will be used. Be sure to specify `CC_FOR_BUILD&#8217; if `CC&#8217; is a cross-compiler to the `host&#8217; machine. </p>
<p>&nbsp;<wbr>&nbsp;CC_FOR_BUILD&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a native C compiler, defaults to&nbsp;`cc&#8217;<br />
&nbsp;<wbr>&nbsp;CC&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a native C compiler, CC_FOR_BUILD is preferred</p>
<h2>Reporting Bugs</h2>
<p>Report bugs and patches to &lt;config-patches [at] gnu.org&gt;. </p>
<p> Originally written by Per Bothner.<br />
 Copyright 1992-2022 Free Software Foundation, Inc. </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
