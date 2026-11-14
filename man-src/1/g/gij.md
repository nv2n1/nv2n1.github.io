---
title: "gij(1)"
name: "gij"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gij/"
description: "gij – GNU interpreter for Java bytecode"
---

<h2 class="name">NAME</h2>
<p> gij &#8211; GNU interpreter for Java bytecode </p>
<h2>SYNOPSIS</h2>
<p> gij [<font SIZE="-1"><code>OPTION</code></font>] &#8230; <i></i><font SIZE="-1"><i>JARFILE</i></font><i></i> [<i></i><font SIZE="-1"><i>ARGS</i></font><i></i>&#8230;] </p>
<p> gij [<code>-jar</code>] [<font SIZE="-1"><code>OPTION</code></font>] &#8230; <i></i><font SIZE="-1"><i>CLASS</i></font><i></i> [<i></i><font SIZE="-1"><i>ARGS</i></font><i></i>&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-cp</code>&nbsp;<wbr><i>path</i>]&nbsp;<wbr>[<code>-classpath</code>&nbsp;<wbr><i>path</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-D</code><i>name</i>[=<i>value</i>]&#8230;]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-ms=</code><i>number</i>]&nbsp;<wbr>[<code>-mx=</code><i>number</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-X</code><i>argument</i>]&nbsp;<wbr>[<code>-verbose</code>]&nbsp;<wbr>[<code>-verbose:class</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;showversion</code>]&nbsp;<wbr>[<code>&#8211;version</code>]&nbsp;<wbr>[<code>&#8211;help</code>][<code>-?</code>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;gij&quot;</tt> is a Java bytecode interpreter included with <tt>&quot;libgcj&quot;</tt>. <tt>&quot;gij&quot;</tt> is not available on every platform; porting it requires a small amount of assembly programming which has not been done for all the targets supported by <code>gcj</code>. </p>
<p> The primary argument to <tt>&quot;gij&quot;</tt> is the name of a class or, with <tt>&quot;-jar&quot;</tt>, a jar file. Options before this argument are interpreted by <tt>&quot;gij&quot;</tt>; remaining options are passed to the interpreted program. </p>
<p> If a class name is specified and this class does not have a <tt>&quot;main&quot;</tt> method with the appropriate signature (a <tt>&quot;static void&quot;</tt> method with a <tt>&quot;String[]&quot;</tt> as its sole argument), then <tt>&quot;gij&quot;</tt> will print an error and exit. </p>
<p> If a jar file is specified then <tt>&quot;gij&quot;</tt> will use information in it to determine which class&#8217; <tt>&quot;main&quot;</tt> method will be invoked. </p>
<p> <tt>&quot;gij&quot;</tt> will invoke the <tt>&quot;main&quot;</tt> method with all the remaining command-line options. </p>
<p> Note that <tt>&quot;gij&quot;</tt> is not limited to interpreting code. Because <tt>&quot;libgcj&quot;</tt> includes a class loader which can dynamically load shared objects, it is possible to give <tt>&quot;gij&quot;</tt> the name of a class which has been compiled and put into a shared library on the class path.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-cp</code> <i>path</i></p>
<dd>
<dt><code>-classpath</code> <i>path</i></p>
<dd> Set the initial class path. The class path is used for finding class and resource files. If specified, this option overrides the <tt>&quot;CLASSPATH&quot;</tt> environment variable. Note that this option is ignored if <tt>&quot;-jar&quot;</tt> is used.</p>
<dt><code>-D</code><i>name</i><code>[=</code><i>value</i><code>]</code></p>
<dd> This defines a system property named <i>name</i> with value <i>value</i>. If <i>value</i> is not specified then it defaults to the empty string. These system properties are initialized at the program&#8217;s startup and can be retrieved at runtime using the <tt>&quot;java.lang.System.getProperty&quot;</tt> method.</p>
<dt><code>-ms=</code><i>number</i></p>
<dd> Equivalent to <tt>&quot;-Xms&quot;</tt>.</p>
<dt><code>-mx=</code><i>number</i></p>
<dd> Equivalent to <tt>&quot;-Xmx&quot;</tt>.</p>
<dt><code>-noverify</code></p>
<dd> Do not verify compliance of bytecode with the <font SIZE="-1">VM</font> specification. In addition, this option disables type verification which is otherwise performed on BC-ABI compiled code.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>-X</code><i>argument</i></p>
<dd> Supplying <tt>&quot;-X&quot;</tt> by itself will cause <tt>&quot;gij&quot;</tt> to list all the supported <tt>&quot;-X&quot;</tt> options. Currently these options are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-Xms</code><i>size</i></p>
<dd> Set the initial heap size.</p>
<dt><code>-Xmx</code><i>size</i></p>
<dd> Set the maximum heap size.</p>
<dt><code>-Xss</code><i>size</i></p>
<dd> Set the thread stack size.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Unrecognized <tt>&quot;-X&quot;</tt> options are ignored, for compatibility with other runtimes.</dl>
<dt><code>-jar</code></p>
<dd> This indicates that the name passed to <tt>&quot;gij&quot;</tt> should be interpreted as the name of a jar file, not a class.</p>
<dt><code>&#8211;help</code></p>
<dd>
<dt><code>-?</code></p>
<dd> Print help, then exit.</p>
<dt><code>&#8211;showversion</code></p>
<dd> Print version number and continue.</p>
<dt><code>&#8211;fullversion</code></p>
<dd> Print detailed version information, then exit.</p>
<dt><code>&#8211;version</code></p>
<dd> Print version number, then exit.</p>
<dt><code>-verbose</code></p>
<dd>
<dt><code>-verbose:class</code></p>
<dd> Each time a class is initialized, print a short message on standard error.</dl>
<p> <tt>&quot;gij&quot;</tt> also recognizes and ignores the following options, for compatibility with existing application launch scripts: <tt>&quot;-client&quot;</tt>, <tt>&quot;-server&quot;</tt>, <tt>&quot;-hotspot&quot;</tt>, <tt>&quot;-jrockit&quot;</tt>, <tt>&quot;-agentlib&quot;</tt>, <tt>&quot;-agentpath&quot;</tt>, <tt>&quot;-debug&quot;</tt>, <tt>&quot;-d32&quot;</tt>, <tt>&quot;-d64&quot;</tt>, <tt>&quot;-javaagent&quot;</tt>, <tt>&quot;-noclassgc&quot;</tt>, <tt>&quot;-verify&quot;</tt>, and <tt>&quot;-verifyremote&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1), <i><a href="/docs/linux/man/1-gcj/">gcj</a></i>(1), <i><a href="/docs/linux/man/1-gcjh/">gcjh</a></i>(1), <i><a href="/docs/linux/man/1-jcf-dump/">jcf-dump</a></i>(1), <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7), and the Info entries for <i>gcj</i> and <i>gcc</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, the Front-Cover Texts being (a) (see below), and with the Back-Cover Texts being (b) (see below). A copy of the license is included in the man page <i><a href="/docs/linux/man/7-gfdl/">gfdl</a></i>(7). </p>
<p> (a) The <font SIZE="-1">FSF</font>&#8216;s Front-Cover Text is: </p>
<pre>
     A GNU Manual
</pre>
<p> (b) The <font SIZE="-1">FSF</font>&#8216;s Back-Cover Text is: </p>
<pre>
     You have freedom to copy and modify this GNU Manual, like GNU
     software.  Copies published by the Free Software Foundation raise
     funds for GNU development.
</pre>
<h2>Index</h2>
