---
title: "gjavah(1)"
name: "gjavah"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gjavah/"
description: "gjavah – – generate header files from Java class files"
---

<h2 class="name">NAME</h2>
<p> gjavah &#8211; &#8211; generate header files from Java class files </p>
<h2>SYNOPSIS</h2>
<p> gjavah &#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <code>gjavah</code> program is used to generate header files from class files. It can generate both <font SIZE="-1">CNI</font> and <font SIZE="-1">JNI</font> header files, as well as stub implementation files which can be used as a basis for implementing the required native methods.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></dt>
<dd> Set output directory.</dd>
<dt><code>-o</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Set output file (only one of <code>-d</code> or <code>-o</code> may be used).</dd>
<dt><code>-cmdfile</code> <i></i><font SIZE="-1"><i>FILE</i></font><i></i></dt>
<dd> Read command file.</dd>
<dt><code>-all</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></dt>
<dd> Operate on all class files under directory <i></i><font SIZE="-1"><i>DIR</i></font><i></i>.</dd>
<dt><code>-stubs</code></dt>
<dd> Emit stub implementation.</dd>
<dt><code>-jni</code></dt>
<dd> Emit <font SIZE="-1">JNI</font> stubs or header (default).</dd>
<dt><code>-cni</code></dt>
<dd> Emit <font SIZE="-1">CNI</font> stubs or header (default <font SIZE="-1">JNI</font>).</dd>
<dt><code>-verbose</code></dt>
<dd> Set verbose mode.</dd>
<dt><code>-force</code></dt>
<dd> Output files should always be written.</dd></dl>
<p> Class path options:</p>
<dl>
<dt><code>-classpath</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> Set the class path.</dd>
<dt><code>-I</code><i></i><font SIZE="-1"><i>DIR</i></font><i></i></dt>
<dd> Add directory to class path.</dd>
<dt><code>-bootclasspath</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> Set the boot class path.</dd>
<dt><code>-extdirs</code> <i></i><font SIZE="-1"><i>PATH</i></font><i></i></dt>
<dd> Set the extension directory path.</dd></dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></dt>
<dd> Print help text, then exit.</dd>
<dt><code>-version</code></dt>
<dd> Print version number, then exit.</dd>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></dt>
<dd> Pass argument to the Java runtime.</dd></dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-javac/">javac</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
<h2>Index</h2>
