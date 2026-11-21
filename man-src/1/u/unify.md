---
title: "unify(1)"
name: "unify"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unify/"
description: "unify – manual page for unify 1.2.2"
---

<h2>NAME</h2>
<p> unify &#8211; manual page for unify 1.2.2</p>
<h2>SYNOPSIS</h2>
<p> <code>unify</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]</p>
<h2>DESCRIPTION</h2>
<p> unify &#8211; Transforms context diffs into unidiffs, or vice-versa.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;context-diffs</code></dt>
<dd> force output to context diffs</dd>
<dt><code>-e</code>, <code>&#8211;echo-comments</code></dt>
<dd> echo comments to standard error</dd>
<dt><code>-o</code>, <code>&#8211;old-diffs</code></dt>
<dd> output old-style diffs, no matter what</dd>
<dt><code>-p</code>, <code>&#8211;patch-format</code></dt>
<dd> generate patch format</dd>
<dt><code>-P</code></dt>
<dd> same as <code>-p</code></dd>
<dt><code>-s</code>, <code>&#8211;strip-comments</code></dt>
<dd> strip comment lines</dd>
<dt><code>-u</code>, <code>&#8211;unidiffs</code></dt>
<dd> force output to unidiffs</dd>
<dt><code>-U</code></dt>
<dd> same as <code>-p</code> and <code>-u</code></dd>
<dt><code>-=</code>, <code>&#8211;use-equals</code></dt>
<dd> replace spaces by equal signs in unidiffs</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help then exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> display program version then exit</dd></dl>
<p> If FILE is not specified, read standard input.</p>
<h2>AUTHOR</h2>
<p> Written by Wayne Davison &lt;davison [at] borland.com&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;wdiff-bugs [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1994, 1997 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>unify</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>unify</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info unify</code></dd></dl>
<p> should give you access to the complete manual. </p>
