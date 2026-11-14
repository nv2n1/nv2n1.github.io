---
title: "col(1)"
name: "col"
section: "1"
letter: "c"
url: "/docs/linux/man/1-col/"
description: "col – filter reverse line feeds from input"
---

<h2 class="name">NAME</h2>
<p> col &#8211; filter reverse line feeds from input </p>
<h2>SYNOPSIS</h2>
<p> <code>col</code> <i>options</i></p>
<h2>DESCRIPTION</h2>
<p> <code>col</code> filters out reverse (and half-reverse) line feeds so the output is in the correct order, with only forward and half-forward line feeds. It also replaces any whitespace characters with tabs where possible. This can be useful in processing the output of <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1) and <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1). </p>
<p> <code>col</code> reads from standard input and writes to standard output.</p>
<h2>OPTIONS</h2>
<p> <code>-b</code>, <code>&#8211;no-backspaces</code></p>
<dl>
<dt>
<dd> Do not output any backspaces, printing only the last character written to each column position.</dl>
<p> <code>-f</code>, <code>&#8211;fine</code></p>
<dl>
<dt>
<dd> Permit half-forward line feeds. Normally characters destined for a half-line boundary are printed on the following line.</dl>
<p> <code>-h</code>, <code>&#8211;tabs</code></p>
<dl>
<dt>
<dd> Output tabs instead of multiple spaces.</dl>
<p> <code>-l</code>, <code>&#8211;lines</code> <i>number</i></p>
<dl>
<dt>
<dd> Buffer at least <i>number</i> lines in memory. By default, 128 lines are buffered.</dl>
<p> <code>-p</code>, <code>&#8211;pass</code></p>
<dl>
<dt>
<dd> Force unknown control sequences to be passed through unchanged. Normally <code>col</code> will filter out any control sequences other than those recognized and interpreted by itself, which are listed below.</dl>
<p> <code>-x</code>, <code>&#8211;spaces</code></p>
<dl>
<dt>
<dd> Output multiple spaces instead of tabs.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-H</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>CONFORMING TO</h2>
<p> The <code>col</code> utility conforms to the Single UNIX Specification, Version 2. The <code>-l</code> option is an extension to the standard.</p>
<h2>NOTES</h2>
<p> The control sequences for carriage motion that <code>col</code> understands and their decimal values are listed in the following table: </p>
<p> <code>ESC-7</code></p>
<dl>
<dt>
<dd> reverse line feed (escape then 7)</dl>
<p> <code>ESC-8</code></p>
<dl>
<dt>
<dd> half reverse line feed (escape then 8)</dl>
<p> <code>ESC-9</code></p>
<dl>
<dt>
<dd> half forward line feed (escape then 9)</dl>
<p> <code>backspace</code></p>
<dl>
<dt>
<dd> moves back one column (8); ignored in the first column</dl>
<p> <code>newline</code></p>
<dl>
<dt>
<dd> forward line feed (10); also does carriage return</dl>
<p> <code>carriage return</code></p>
<dl>
<dt>
<dd> (13)</dl>
<p> <code>shift in</code></p>
<dl>
<dt>
<dd> shift to normal character set (15)</dl>
<p> <code>shift out</code></p>
<dl>
<dt>
<dd> shift to alternate character set (14)</dl>
<p> <code>space</code></p>
<dl>
<dt>
<dd> moves forward one column (32)</dl>
<p> <code>tab</code></p>
<dl>
<dt>
<dd> moves forward to next tab stop (9)</dl>
<p> <code>vertical tab</code></p>
<dl>
<dt>
<dd> reverse line feed (11)</dl>
<p> All unrecognized control characters and escape sequences are discarded. </p>
<p> <code>col</code> keeps track of the character set as characters are read and makes sure the character set is correct when they are output. </p>
<p> If the input attempts to back up to the last flushed line, <code>col</code> will display a warning message.</p>
<h2>HISTORY</h2>
<p> A <code>col</code> command appeared in Version 6 AT&amp;T UNIX.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-expand/">expand</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>col</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
