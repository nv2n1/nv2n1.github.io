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
<dt><code>-d</code> &lt;directory&gt;</p>
<dd> write generated file to &lt;directory&gt;</p>
<dt><code>&#8211;skel</code> &lt;file&gt;</p>
<dd> use external skeleton &lt;file&gt;</p>
<dt><code>&#8211;switch</code>, <code>&#8211;table</code>, <code>&#8211;pack</code></p>
<dd> set default code generation method</p>
<dt><code>&#8211;jlex</code></p>
<dd> strict JLex compatibility</p>
<dt><code>&#8211;nomin</code></p>
<dd> skip minimization step</p>
<dt><code>&#8211;nobak</code></p>
<dd> don&#8217;t create backup files</p>
<dt><code>&#8211;dump</code></p>
<dd> display transition tables</p>
<dt><code>&#8211;dot</code></p>
<dd> write graphviz .dot files for the generated automata (alpha)</p>
<dt><code>&#8211;verbose</code>, <code>-v</code></p>
<dd> display generation progress messages (default)</p>
<dt><code>&#8211;quiet</code>, <code>-q</code></p>
<dd> display errors only</p>
<dt><code>&#8211;time</code></p>
<dd> display generation time statistics</p>
<dt><code>&#8211;version</code></p>
<dd> print the version number of this copy of jflex</p>
<dt><code>&#8211;info</code></p>
<dd> print system + JDK information</p>
<dt><code>&#8211;help</code>, <code>-h</code></p>
<dd> print this message</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Wolfgang Baer &lt;WBaer [at] gmx.de&gt;, for the Debian project (but may be used by others). </p>
<h2>Index</h2>
