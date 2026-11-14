---
title: "gcjh(1)"
name: "gcjh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcjh/"
description: "gcjh – – generate header files from Java class files"
---

<h2 class="name">NAME</h2>
<p> gcjh &#8211; &#8211; generate header files from Java class files </p>
<h2>SYNOPSIS</h2>
<p> gcjh [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>]&#8230; <i></i><font SIZE="-1"><i>CLASS</i></font><i></i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <tt>&quot;gcjh&quot;</tt> program is used to generate header files from class files. It can generate both <font SIZE="-1">CNI</font> and <font SIZE="-1">JNI</font> header files, as well as stub implementation files which can be used as a basis for implementing the required native methods. It is similar to <tt>&quot;javah&quot;</tt> but has slightly different command line options, and defaults to <font SIZE="-1">CNI</font>.</p>
<h2>OPTIONS</h2>
<p> See <tt>&quot;javah&quot;</tt> for a full description; this page only lists the additional options provided by <tt>&quot;gcjh&quot;</tt>. </p>
<p> <font SIZE="-1">CNI</font> text options</p>
<dl>
<dt><code>-add</code> <i>text</i></p>
<dd> Insert <i>text</i> into class body.</p>
<dt><code>-append</code> <i>text</i></p>
<dd> Append <i>text</i> after class declaration.</p>
<dt><code>-friend</code> <i>text</i></p>
<dd> Insert <i>text</i> as a <tt>&quot;friend&quot;</tt> declaration.</p>
<dt><code>-prepend</code> <i>text</i></p>
<dd> Insert <i>text</i> before start of class.</dl>
<p> Compatibility options (unused)</p>
<dl>
<dt><code>-td</code> <i></i><font SIZE="-1"><i>DIR</i></font><i></i></p>
<dd>
<dt><code>-M</code></p>
<dd>
<dt><code>-MM</code></p>
<dd>
<dt><code>-MD</code></p>
<dd>
<dt><code>-MMD</code></p>
<dd> Unused compatibility option.</dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></p>
<dd> Print help text, then exit.</p>
<dt><code>-version</code></p>
<dd> Print version number, then exit.</p>
<dt><code>-J</code><i></i><font SIZE="-1"><i>OPTION</i></font><i></i></p>
<dd> Pass argument to the Java runtime.</dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-javac/">javac</a></i>(1), <i><a href="/docs/linux/man/1-javah/">javah</a></i>(1), &#8230;</p>
<h2>AUTHOR</h2>
<h2>Index</h2>
