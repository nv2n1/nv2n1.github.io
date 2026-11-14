---
title: "flipdiff(1)"
name: "flipdiff"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flipdiff/"
description: "flipdiff – exchange the order of two incremental patches"
---

<h2 class="name">NAME</h2>
<p> flipdiff &#8211; exchange the order of two incremental patches </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>flipdiff</code> [[-p&nbsp;<i>n</i>] | [&#8211;strip-match=<i>n</i>]] [[-U&nbsp;<i>n</i>] | [&#8211;unified=<i>n</i>]] [[-d&nbsp;<i>PAT</i>] | [&#8211;drop-context=<i>PAT</i>]] [[-q] | [&#8211;quiet]] [[-z] | [&#8211;decompress]] [[-b] | [&#8211;ignore-space-change]] [[-B] | [&#8211;ignore-blank-lines]] [[-i] | [&#8211;ignore-case]] [[-w] | [&#8211;ignore-all-space]] [&#8211;in-place] <i>diff1</i> <i>diff2</i></p>
<dt> <code>flipdiff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<p> <code>flipdiff</code></p>
<dd>exchanges the order of two patch files that apply one after the other. The patches must be &#8220;clean&#8221;: the context lines must match and there should be no mis-matched offsets. </p>
<p> The swapped patches are sent to standard output, with a marker line (&#8220;===&nbsp;8&lt;&nbsp;===&nbsp;cut here&nbsp;===&nbsp;8&lt;&nbsp;===&#8221;) between them, unless the <code>&#8211;in-place</code> option is passed. In that case, the output is written back to the original input files.</p>
<h2>OPTIONS</h2>
<p> <code>-p</code> <i>n</i>, <code>&#8211;strip-match=</code><i>n</i></p>
<dl>
<dt>
<dd> When comparing filenames, ignore the first <i>n</i> pathname components from both patches. (This is similar to the <code>-p</code> option to GNU <code><a href="/docs/linux/man/1-patch/">patch</a></code>(1).)</dl>
<p> <code>-q</code>, <code>&#8211;quiet</code></p>
<dl>
<dt>
<dd> Quieter output. Don&#8217;t emit rationale lines at the beginning of each patch.</dl>
<p> <code>-U</code> <i>n</i>, <code>&#8211;unified=</code><i>n</i></p>
<dl>
<dt>
<dd> Attempt to display <i>n</i> lines of context (requires at least <i>n</i> lines of context in both input files). (This is similar to the <code>-U</code> option to GNU <code><a href="/docs/linux/man/1-diff/">diff</a></code>(1).)</dl>
<p> <code>-d</code> <i>pattern</i>, <code>&#8211;drop-context=</code><i>PATTERN</i></p>
<dl>
<dt>
<dd> Don&#8217;t display any context on files that match the shell wildcard <i>pattern</i>. This option can be given multiple times. </p>
<p> Note that the interpretation of the shell wildcard pattern does not count slash characters or periods as special (in other words, no flags are given to <code>fnmatch</code>). This is so that &#8220;*/basename&#8221;-type patterns can be given without limiting the number of pathname components.</dl>
<p> <code>-i</code>, <code>&#8211;ignore-case</code></p>
<dl>
<dt>
<dd> Consider upper- and lower-case to be the same.</dl>
<p> <code>-w</code>, <code>&#8211;ignore-all-space</code></p>
<dl>
<dt>
<dd> Ignore whitespace changes in patches.</dl>
<p> <code>-b</code>, <code>&#8211;ignore-space-change</code></p>
<dl>
<dt>
<dd> Ignore changes in the amount of whitespace.</dl>
<p> <code>-B</code>, <code>&#8211;ignore-blank-lines</code></p>
<dl>
<dt>
<dd> Ignore changes whose lines are all blank.</dl>
<p> <code>-z</code>, <code>&#8211;decompress</code></p>
<dl>
<dt>
<dd> Decompress files with extensions .gz and .bz2.</dl>
<p> <code>&#8211;in-place</code></p>
<dl>
<dt>
<dd> Write output to the original input files.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of flipdiff.</dl>
<h2>LIMITATIONS</h2>
<p> This is only been very lightly tested, and may not even work. Using <code>&#8211;in-place</code> is not recommended at the moment. </p>
<p> There are some cases in which it is not possible to meaningfully flip patches without understanding the semantics of the content. This program only uses complete lines that appear at some stage during the application of the two patches, and never composes a line from parts. </p>
<p> Because of this, it is generally a good idea to read through the output to check that it makes sense.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
