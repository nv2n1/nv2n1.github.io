---
title: "deb-shlibs(5)"
name: "deb-shlibs"
section: "5"
letter: "d"
url: "/docs/linux/man/5-deb-shlibs/"
description: "deb-shlibs – Debian shared library information file"
---

<p>deb-shlibs &#8211; Debian shared library information file</p>
<h2>Synopsis</h2>
<p><code>debian/shlibs</code>, <code>debian/</code><i>binary-name</i><code>.shlibs</code>, <code>DEBIAN/shlibs</code></p>
<h2>Description</h2>
<p><code>shlibs</code> files map shared library names and versions (<i>SONAMEs</i>) to dependencies suitable for a package control file. There is one entry per line. Blank lines are <code>not</code> allowed. Lines beginning with a <code>#</code> character are considered commentary, and are ignored. All other lines must have the format: </p>
<dl>
<dd>[<i>type</i><code>:</code>] <i>library</i> <i>version</i> <i>dependencies</i></dl>
<p> The <i>library</i> and <i>version</i> fields are whitespace-delimited, but the <i>dependencies</i> field extends to the end of the line. The <i>type</i> field is optional and normally not needed. </p>
<p> The <i>dependencies</i> field has the same syntax as the <code>Depends</code> field in a binary control file, see <code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5).</p>
<h2>Soname Formats</h2>
<p>The <font SIZE="-1">SONAME</font> formats supported are: </p>
<dl>
<dd><i>name</i>.so.<i>version</i></dl>
<p> and </p>
<dl>
<dd><i>name</i>&#8211;<i>version</i>.so</dl>
<p> where <i>name</i> is usually prefixed by <code>lib</code>.</p>
<h2>Examples</h2>
<p>The <code>shlibs</code> file for a typical library package, named <i>libcrunch1</i>, that provides one library whose <font SIZE="-1">SONAME</font> is <i>libcrunch.so.1</i>, might read </p>
<pre> libcrunch 1 libcrunch1 (&gt;= 1.2-1)</pre>
<p>The <i>dependencies</i> must mention the most recent version of the package that added new symbols to the library: in the above example, new symbols were added to version 1.2 of <i>libcrunch</i>. This is not the only reason the dependencies might need to be tightened.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-deb-control/">deb-control</a></code>(5), <code><a href="/docs/linux/man/1-dpkg-shlibdeps/">dpkg-shlibdeps</a></code>(1), <code><a href="/docs/linux/man/5-deb-symbols/">deb-symbols</a></code>(5). </p>
