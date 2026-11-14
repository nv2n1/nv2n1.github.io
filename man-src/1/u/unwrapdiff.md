---
title: "unwrapdiff(1)"
name: "unwrapdiff"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unwrapdiff/"
description: "unwrapdiff – demangle word-wrapped patches"
---

<h2 class="name">NAME</h2>
<p> unwrapdiff &#8211; demangle word-wrapped patches </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>unwrapdiff</code> [-v] [<i>file</i>&#8230;]</p>
<dt> <code>unwrapdiff</code> {[&#8211;help] | [&#8211;version]}</dl>
<h2>DESCRIPTION</h2>
<p> <code>unwrapdiff</code></p>
<dd>demangles patches that have been word-wrapped, in an attempt to make them useful. </p>
<p> The corrected diff is sent to standard output. Note that you will probably need to use the <code>-l</code> option when applying the patch, in order to ignore any whitespace differences there may be.</p>
<h2>OPTIONS</h2>
<p> <code>-v</code></p>
<dl>
<dt>
<dd> Verbose operation. A list of lines that are modified in a way that might be wrong is sent to stderr.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display a short usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display the version number of unwrapdiff.</dl>
<h2>LIMITATIONS</h2>
<p> Some heuristics are used to decide whether use a space to recombine a wrapped line, or just join them together. Currently this is done by comparing with last three characters of a line with the first two characters of its continuation, and using a space if any of them are different. </p>
<p> The patch needs to have been valid before being word-wrapped. </p>
<p> The last line of a hunk is nearly always ambiguous. If the next line begins &#8220;@@&#8221;, &#8220;Index:&nbsp;&#8220;, &#8220;diff&nbsp;&#8221; or &#8220;&#8212;&nbsp;&#8221; then it is taken to be complete; otherwise it is unwrapped using the next line.</p>
<h2>AUTHOR</h2>
<p> <code>Tim Waugh</code> &lt;twaugh [at] redhat.com&gt;</p>
<dl>
<dt>
<dd> Package maintainer</dl>
<h2>Index</h2>
