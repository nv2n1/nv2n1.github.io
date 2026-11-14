---
title: "bigloo(1)"
name: "bigloo"
section: "1"
letter: "b"
url: "/docs/linux/man/1-bigloo/"
description: "bigloo v2.3 – `a practical Scheme compiler’"
---

<h2 class="name">NAME</h2>
<p> bigloo v2.3 &#8211; `a practical Scheme compiler&#8217;</p>
<h2>SYNOPSIS</h2>
<p> <code>bigloo</code> [ options ] <i>[ input ]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>Bigloo</code> is a Scheme compiler. Scheme is defined in an IEEE standard for the Scheme Programming Language but Bigloo does not entirely conform to it. The compiler produces either C files or <code>Java</code> class files. The C files are then compiled by any <code>ISO</code> C compiler to produce <i>.o</i> or <i>executable</i> files. <code>Bigloo</code> is a module compiler which means that it is allowed to compile several files and to link them together to produce an unique executable. </p>
<h2>OPTIONS</h2>
<dl>
<dt>options</p>
<dd> Many options are available. Type `bigloo -help&#8217; to print them.</p>
<dt>-jvm</p>
<dd> Produces Java class files instead of C files. This option has to be used when compiling and when linking.</p>
<dt>-no-jvmjar</p>
<dd> Disable jar file production when linking with <i>-jvm</i>.</p>
<dt><i>input</i></p>
<dd> If an input file is provided, Bigloo compiles it. Otherwise the interpreter is entered. Input must be a <i>recognized</i> Scheme source file name (i.e. a file name with a recognized suffix (see <i>-suffix</i> option)).</dl>
<h2>CONFIGURATION FILE</h2>
<p> Each <code>Bigloo</code>&#8216;s user can use a special configuration file. This file must be named `~/.bigloorc&#8217;. This file makes it possible to modify the behaviour of the compiler. This file is a regular Scheme file which contains expressions bound in an environment where compiler parameters are bound. See the documentation for details. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>BIGLOOHEAP</code></p>
<dd> Set the environment size (in megabytes). The default value is 4.</p>
<dt><code>TMPDIR</code></p>
<dd> Set the temporary directory. The default value is `/tmp&#8217;.</p>
<dt><code>BIGLOOLIB</code></p>
<dd> The path to find the Bigloo&#8217;s library.</p>
<dt><code>BIGLOOJAVAOPT</code></p>
<dd> Java Virtual Machine options when running Bigloo a application. </p>
</dl>
<h2>FILES</h2>
<p> /&#8230;/lib/bigloo/2.3a/bigloo.heap &#8212; saved heap image for the compiler.<br />
 /&#8230;/lib/bigloo/2.3a/bigloo.jheap &#8212; saved heap image for the compiler for <i>-jvm</i> compiations.<br />
 /&#8230;/lib/bigloo/2.3a/bigloo.h &#8212; definitions which are #include&#8217;d in the C code.<br />
 /&#8230;/lib/bigloo/2.3a/libbigloo.a &#8212; library.<br />
 /&#8230;/lib/bigloo/2.3a/libbigloo_u.a &#8212; library.<br />
 ~/.bigloorc &#8212; user `runtime-command&#8217; configuration file.<br />
 /&#8230;/.bigloorc &#8212; idem. </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-bglafile/">bglafile</a>(1), <a href="/docs/linux/man/1-bgljfile/">bgljfile</a>(1), <a href="/docs/linux/man/1-bgldepend/">bgldepend</a>(1), <a href="/docs/linux/man/1-bglmake/">bglmake</a>(1), <a href="/docs/linux/man/1-bglpp/">bglpp</a>(1), <a href="/docs/linux/man/1-bglprof/">bglprof</a>(1), <a href="/docs/linux/man/1-bgltags/">bgltags</a>(1), <a href="/docs/linux/man/1-bglmco/">bglmco</a>(1), <a href="/docs/linux/man/1-gcc/">gcc</a>(1), <a href="/docs/linux/man/1-camloo/">camloo</a>(1), <a href="/docs/linux/man/1-cigloo/">cigloo</a>(1), <a href="/docs/linux/man/1-jigloo/">jigloo</a>(1). </p>
<h2>AUTHOR</h2>
<p> Manuel SERRANO, Manuel.Serrano [at] inria.fr </p>
<h2>Index</h2>
