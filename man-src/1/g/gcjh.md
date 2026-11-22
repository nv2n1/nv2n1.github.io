---

title: "gcjh(1)"
name: "gcjh"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gcjh/"
description: "gcjh – – generate header files from Java class files"
---

<p> gcjh &#8211; &#8211; generate header files from Java class files </p>
<h2>SYNOPSIS</h2>
<p> gcjh [<i></i><i>OPTIONS</i><i></i>]&#8230; <i></i><i>CLASS</i><i></i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> The <tt>&quot;gcjh&quot;</tt> program is used to generate header files from class files. It can generate both CNI and JNI header files, as well as stub implementation files which can be used as a basis for implementing the required native methods. It is similar to <tt>&quot;javah&quot;</tt> but has slightly different command line options, and defaults to CNI.</p>
<h2>OPTIONS</h2>
<p> See <tt>&quot;javah&quot;</tt> for a full description; this page only lists the additional options provided by <tt>&quot;gcjh&quot;</tt>. </p>
<p> CNI text options</p>
<dl>
<dt><code>-add</code> <i>text</i></dt>
<dd> Insert <i>text</i> into class body.</dd>
<dt><code>-append</code> <i>text</i></dt>
<dd> Append <i>text</i> after class declaration.</dd>
<dt><code>-friend</code> <i>text</i></dt>
<dd> Insert <i>text</i> as a <tt>&quot;friend&quot;</tt> declaration.</dd>
<dt><code>-prepend</code> <i>text</i></dt>
<dd> Insert <i>text</i> before start of class.</dd></dl>
<p> Compatibility options (unused)</p>
<dl>
<dt><code>-td</code> <i></i><i>DIR</i><i></i></dt>
<dd>
</dd><dt><code>-M</code></dt>
<dd>
</dd><dt><code>-MM</code></dt>
<dd>
</dd><dt><code>-MD</code></dt>
<dd>
</dd><dt><code>-MMD</code></dt>
<dd> Unused compatibility option.</dd></dl>
<p> Standard options:</p>
<dl>
<dt><code>-help</code></dt>
<dd> Print help text, then exit.</dd>
<dt><code>-version</code></dt>
<dd> Print version number, then exit.</dd>
<dt><code>-J</code><i></i><i>OPTION</i><i></i></dt>
<dd> Pass argument to the Java runtime.</dd></dl>
<h2>BUGS</h2>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-javac/">javac</a></i>(1), <i>javah</i>(1), &#8230;</p>
<h2>AUTHOR</h2>
