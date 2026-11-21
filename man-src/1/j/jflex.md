---
title: "jflex(1)"
name: "jflex"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jflex/"
description: "jflex – a lexical analyzer generator (also known as scanner generator) for Java"
---

<h2>NAME</h2>
<p> jflex &#8211; a lexical analyzer generator (also known as scanner generator) for Java</p>
<h2>SYNOPSIS</h2>
<p> <code>jflex</code> <i>&lt;options&gt; &lt;input-files&gt;</i></p>
<h2>DESCRIPTION</h2>
<p> JFlex is a lexical analyzer generator (also known as scanner generator) for Java(tm), written in Java(tm). It is also a rewrite of the very useful tool JLex. JFlex is designed to work together with the LALR parser generator CUP, and the Java modification of Berkeley Yacc BYacc/J. It can also be used together with other parser generators like ANTLR or as a standalone tool. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> &lt;directory&gt;</dt>
<dd> write generated file to &lt;directory&gt;</dd>
<dt><code>&#8211;skel</code> &lt;file&gt;</dt>
<dd> use external skeleton &lt;file&gt;</dd>
<dt><code>&#8211;switch</code>, <code>&#8211;table</code>, <code>&#8211;pack</code></dt>
<dd> set default code generation method</dd>
<dt><code>&#8211;jlex</code></dt>
<dd> strict JLex compatibility</dd>
<dt><code>&#8211;nomin</code></dt>
<dd> skip minimization step</dd>
<dt><code>&#8211;nobak</code></dt>
<dd> don&#8217;t create backup files</dd>
<dt><code>&#8211;dump</code></dt>
<dd> display transition tables</dd>
<dt><code>&#8211;dot</code></dt>
<dd> write graphviz .dot files for the generated automata (alpha)</dd>
<dt><code>&#8211;verbose</code>, <code>-v</code></dt>
<dd> display generation progress messages (default)</dd>
<dt><code>&#8211;quiet</code>, <code>-q</code></dt>
<dd> display errors only</dd>
<dt><code>&#8211;time</code></dt>
<dd> display generation time statistics</dd>
<dt><code>&#8211;version</code></dt>
<dd> print the version number of this copy of jflex</dd>
<dt><code>&#8211;info</code></dt>
<dd> print system + JDK information</dd>
<dt><code>&#8211;help</code>, <code>-h</code></dt>
<dd> print this message</dd></dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Wolfgang Baer &lt;WBaer [at] gmx.de&gt;, for the Debian project (but may be used by others). </p>
