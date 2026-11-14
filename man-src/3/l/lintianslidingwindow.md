---
title: "lintianslidingwindow(3)"
name: "lintianslidingwindow"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lintianslidingwindow/"
description: "Lintian::SlidingWindow – Lintian interface to sliding window match"
---

<p>Lintian::SlidingWindow &#8211; Lintian interface to sliding window match </p>
<h2>Synopsis</h2>
<pre> use Lintian::SlidingWindow;
 my $sfd = Lintian::SlidingWindow-&gt;new('&lt;','someevilfile.c', sub { $_ = lc($_); });
 my $window;
 while ($window = $sfd-&gt;readwindow) {
 if (index($window, 'evil') &gt; -1) {
 if($window =~
 m/software \s++ shall \s++
 be \s++ used \s++ for \s++ good \s*+ ,?+ \s*+
 not \s++ evil/xsim) {
 # do something like : tag 'license-problem-json-evil';
 }
 }
 }</pre>
<h2>Description</h2>
<p>Lintian::SlidingWindow provides a way of matching some pattern, including multi line pattern, without needing to fully load the file in memory.</p>
<h2>Class Methods</h2>
<dl COMPACT>
<dt>new(HANDLE[, BLOCKSUB[, <font SIZE="-1">BLOCKSIZE</font>]])</p>
<dd>Create a new sliding window by reading from a given <font SIZE="-1">HANDLE,</font> which must be open for reading. Optionally run <font SIZE="-1">BLOCKSUB</font> against each block. Note that <font SIZE="-1">BLOCKSUB</font> should apply transform byte by byte and does not depend of context. </p>
<p> Each window consists of up to two blocks of <font SIZE="-1">BLOCKSIZE</font> characters.</dl>
<h2>Instance Methods</h2>
<dl COMPACT>
<dt>readwindow</p>
<dd>Return a new block of sliding window. Return undef at end of file.</p>
<dt>blocknumber</p>
<dd>return the number of block read by the instance. Return undef if no block has been read.</dl>
<h2>Diagnostics</h2>
<dl COMPACT>
<dt>no data type specified</p>
<dd></dl>
<h2>Author</h2>
<p>Originally written by Bastien <font SIZE="-1">ROUCARIES</font> for Lintian.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-lintian/">lintian</a></code>(1)</p>
