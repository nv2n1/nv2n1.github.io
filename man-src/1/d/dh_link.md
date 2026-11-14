---
title: "dh_link(1)"
name: "dh_link"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_link/"
description: "dh_link – create symlinks in package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_link &#8211; create symlinks in package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_link</code> [<i>debhelper options</i>] [<code>-A</code>] [<code>-X</code><i>item</i>] [<i>source destination</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_link</code> is a debhelper program that creates symlinks in package build directories. </p>
<p> <code>dh_link</code> accepts a list of pairs of source and destination files. The source files are the already existing files that will be symlinked from (called <code>target</code> by <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)). The destination files are the symlinks that will be created (called <code>link name</code> by <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)). There <code>must</code> be an equal number of source and destination files specified. </p>
<p> Be sure you <code>do</code> specify the absolute path to both the source and destination files (unlike you would do if you were using something like <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)). Please note that the leading slash is optional. </p>
<p> <code>dh_link</code> will generate symlinks that comply with Debian policy &#8211; absolute when policy says they should be absolute, and relative links with as short a path as possible. It will also create any subdirectories it needs to put the symlinks in. </p>
<p> Any pre-existing destination files will be replaced with symlinks. </p>
<p> <code>dh_link</code> also scans the package build tree for existing symlinks which do not conform to Debian policy, and corrects them (v4 or later).</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.links</p>
<dd> Lists pairs of source and destination files to be symlinked. Each pair should be put on its own line, with the source and destination separated by whitespace. </p>
<p> In each pair the source file (called <code>target</code> by <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)) comes first and is followed by the destination file (called <code>link name</code> by <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1)). Thus the pairs of source and destination files in each line are give in the same order as they would be given to <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1). </p>
<p> In contrast to <i><a href="/docs/linux/man/1-ln/">ln</a></i>(1), source and destination paths must be absolute (the leading slash is optional).</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code>, <code>&#8211;all</code></p>
<dd> Create any links specified by command line parameters in <font SIZE="-1">ALL</font> packages acted on, not just the first.</p>
<dt><code>-X</code><i>item</i>, <code>&#8211;exclude=</code><i>item</i></p>
<dd> Exclude symlinks that contain <i>item</i> anywhere in their filename from being corrected to comply with Debian policy.</p>
<dt><i>source destination</i> &#8230;</p>
<dd> Create a file named <i>destination</i> as a link to a file named <i>source</i>. Do this in the package build directory of the first package acted on. (Or in all packages if <code>-A</code> is specified.)</dl>
<h2>EXAMPLES</h2>
<pre>
 dh_link usr/share/man/man1/foo.1 usr/share/man/man1/bar.1
</pre>
<p> Make <i>bar.1</i> be a symlink to <i>foo.1</i> </p>
<pre>
 dh_link var/lib/foo usr/lib/foo \
   usr/share/man/man1/foo.1 usr/share/man/man1/bar.1
</pre>
<p> Make <i>/usr/lib/foo/</i> be a link to <i>/var/lib/foo/</i>, and <i>bar.1</i> be a symlink to the <i>foo.1</i> </p>
<pre>
 var/lib/foo usr/lib/foo
 usr/share/man/man1/foo.1 usr/share/man/man1/bar.1
</pre>
<p> Same as above but as content for a debian/<i>package</i>.links file.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHOR</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<h2>Index</h2>
