---
title: "kawa(1)"
name: "kawa"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kawa/"
description: "kawa – Scheme language implemented using on a Java VM"
---

<h2 class="name">NAME</h2>
<p> kawa &#8211; Scheme language implemented using on a Java VM </p>
<h2>SYNOPSIS</h2>
<p> <code>kawa</code> <i>[options]</i><br />
 <code>java kawa.repl</code> <i>[options]</i></p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>kawa</code> package, a Scheme dialect written completely in the Java language. Scheme forms are compiled into Java bytecodes for efficiency. </p>
<p> Scheme is a high-level non-pure functional language in the Lisp family, with lexical scoping dynamically-types. The Kawa dialect of Scheme contains hooks to access and control Java objects. </p>
<p> Using the <code>kawa</code> script is equivalent to invoking an interpreter of the Java language on the <code>kawa.repl</code> class. </p>
<p> This manual page is just a quick synopsis. For more information, read the <code>kawa</code> manual &#8211; see below. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-e </code><i>expression</i></p>
<dd> Evaluate the <i>expression</i>.</p>
<dt><code>-c </code><i>expression</i></p>
<dd> Evaluate the <i>expression</i>, but does not cause the start-up file <i>~/.kawarc.scm</i> to be read.</p>
<dt><code>-f </code><i>filename</i></p>
<dd> Read and evaluate Scheme commands from the <i>filename</i>.</p>
<dt><code>-s</code></p>
<dd> Enter an interactive read-evaluate-print command loop.</p>
<dt><code>-w</code></p>
<dd> Enter an interactive read-evaluate-print in a new top-level window.</p>
<dt><code>-C </code><i>filename</i></p>
<dd> Compile <i>filename</i> to one or more Java class files. See the Kawa manual for details. If no options are specified, it is equivalent to <code>-s</code>.<br />
 GNU <code><a href="/docs/linux/man/3-readline/">readline</a>(3)</code> can normally be used to edit commands. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>/usr/bin/kawa</code></p>
<dd> The <code>kawa</code> executable, which starts a <code>java</code> interpreter.</p>
<dt><code>~/.kawarc.scm</code></p>
<dd> Commands that are executed when <code>kawa</code> is started.</dl>
<h2>AUTHOR</h2>
<p> Per Bothner &lt;per [at] bothner.com&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code>info kawa</code> &#8211; the complete Kawa manual. <i><a rel="nofollow" href="http://www.gnu.org/software/kawa/">http://www.gnu.org/software/kawa/</a></i> &#8211; the <code>kawa</code> home page, based on the same Kawa manual. <code><a href="/docs/linux/man/1-qexo/">qexo</a>(1)</code> &#8211; an implementation of XQuery using the same engine. </p>
<h2>Index</h2>
