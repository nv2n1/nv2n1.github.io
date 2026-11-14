---
title: "merge(1)"
name: "merge"
section: "1"
letter: "m"
url: "/docs/linux/man/1-merge/"
description: "merge – three-way file merge"
---

<h2>NAME</h2>
<p> merge &#8211; three-way file merge</p>
<h2>SYNOPSIS</h2>
<p> <code>merge</code> [ <i>options</i> ] <i>file1 file2 file3</i></p>
<h2>DESCRIPTION</h2>
<p> <code>merge</code> incorporates all changes that lead from <i>file2</i> to <i>file3</i> into <i>file1</i>. The result ordinarily goes into <i>file1</i>. <code>merge</code> is useful for combining separate changes to an original. Suppose <i>file2</i> is the original, and both <i>file1</i> and <i>file3</i> are modifications of <i>file2</i>. Then <code>merge</code> combines both changes. </p>
<p> A conflict occurs if both <i>file1</i> and <i>file3</i> have changes in a common segment of lines. If a conflict is found, <code>merge</code> normally outputs a warning and brackets the conflict with <code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code> and <code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code> lines. A typical conflict will look like this: </p>
<dl>
<dt>
<dd>
<pre>
<code>&lt;&lt;&lt;&lt;&lt;&lt;&lt;</code><i> file A</i>
<i>lines in file A</i>
<code>=======</code>
<i>lines in file B</i>
<code>&gt;&gt;&gt;&gt;&gt;&gt;&gt;</code><i> file B</i>
</dl>
</pre>
<p> If there are conflicts, the user should edit the result and delete one of the alternatives.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-A</code></p>
<dd> Output conflicts using the <code>-A</code> style of <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1), if supported by <code>diff3</code>. This merges all changes leading from <i>file2</i> to <i>file3</i> into <i>file1</i>, and generates the most verbose output.</p>
<dt><code>-E</code>, <code>-e</code></p>
<dd> These options specify conflict styles that generate less information than <code>-A</code>. See <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1) for details. The default is <code>-E</code>. With <code>-e</code>, <code>merge</code> does not warn about conflicts.</p>
<dt><code>-L</code><i> label</i></p>
<dd> This option may be given up to three times, and specifies labels to be used in place of the corresponding file names in conflict reports. That is, <code>merge -L x -L y -L z a b c</code> generates output that looks like it came from files <code>x</code>, <code>y</code> and <code>z</code> instead of from files <code>a</code>, <code>b</code> and <code>c</code>.</p>
<dt><code>-p</code></p>
<dd> Send results to standard output instead of overwriting <i>file1</i>.</p>
<dt><code>-q</code></p>
<dd> Quiet; do not warn about conflicts.</p>
<dt><code>-V</code></p>
<dd> Print <font SIZE="-1">RCS</font>&#8216;s version number.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 for no conflicts, 1 for some conflicts, 2 for trouble.</p>
<h2>IDENTIFICATION</h2>
<p> Author: Walter F. Tichy.<br />
 Manual Page Revision: 5.9.0; Release Date: 2014-06-10.<br />
 Copyright &#169; 2010-2013 Thien-Thi Nguyen.<br />
 Copyright &#169; 1990, 1991, 1992, 1993, 1994, 1995 Paul Eggert.<br />
 Copyright &#169; 1982, 1988, 1989 Walter F. Tichy. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-diff3/">diff3</a></code>(1), <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1), <code><a href="/docs/linux/man/1-rcsmerge/">rcsmerge</a></code>(1), <code><a href="/docs/linux/man/1-co/">co</a></code>(1). </p>
<p> The full documentation for <font SIZE="-1">RCS</font> is maintained as a Texinfo manual. If the <code><a href="/docs/linux/man/1-info/">info</a></code>(1) and <font SIZE="-1">RCS</font> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info rcs</code></dl>
<p> should give you access to the complete manual. Additionally, the <font SIZE="-1">RCS</font> homepage:</p>
<dl>
<dt>
<dd> <code><a rel="nofollow" href="http://www.gnu.org/software/rcs/">http://www.gnu.org/software/rcs/</a></code></dl>
<p> has news and links to the latest release, development site, etc.</p>
<h2>BUGS</h2>
<p> It normally does not make sense to merge binary files as if they were text, but <code>merge</code> tries to do it anyway. </p>
<h2>Index</h2>
