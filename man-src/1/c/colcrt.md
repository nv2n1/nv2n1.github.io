---
title: "colcrt(1)"
name: "colcrt"
section: "1"
letter: "c"
url: "/docs/linux/man/1-colcrt/"
description: "colcrt – filter nroff output for CRT previewing"
---

<h2 class="name">NAME</h2>
<p> colcrt &#8211; filter nroff output for CRT previewing </p>
<h2>SYNOPSIS</h2>
<p> <code>colcrt</code> [options] [<i>file</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>colcrt</code> provides virtual half-line and reverse line feed sequences for terminals without such capability, and on which overstriking is destructive. Half-line characters and underlining (changed to dashing `-&#8216;) are placed on new lines in between the normal output lines.</p>
<h2>OPTIONS</h2>
<p> <code>&#8211;</code>, <code>&#8211;no-underlining</code></p>
<dl>
<dt>
<dd> Suppress all underlining. This option is especially useful for previewing <i>allboxed</i> tables from <code><a href="/docs/linux/man/1-tbl/">tbl</a></code>(1).</dl>
<p> <code>-2</code>, <code>&#8211;half-lines</code></p>
<dl>
<dt>
<dd> Causes all half-lines to be printed, effectively double spacing the output. Normally, a minimal space output format is used which will suppress empty lines. The program never suppresses two consecutive empty lines, however. The <code>-2</code> option is useful for sending output to the line printer when the output contains superscripts and subscripts which would otherwise be invisible.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>HISTORY</h2>
<p> The <code>colcrt</code> command appeared in 3.0BSD.</p>
<h2>BUGS</h2>
<p> Should fold underlines onto blanks even with the <code>&#8216;-&#8216;</code> option so that a true underline character would show. </p>
<p> Can&#8217;t back up more than 102 lines. </p>
<p> General overstriking is lost; as a special case &#8216;|&#8217; overstruck with &#8216;-&#8216; or underline becomes &#8216;+&#8217;. </p>
<p> Lines are trimmed to 132 characters. </p>
<p> Some provision should be made for processing superscripts and subscripts in documents which are already double-spaced.</p>
<h2>EXAMPLES</h2>
<p> A typical use of <code>colcrt</code> would be:</p>
<dl>
<dt>
<dd>
<p> <code>tbl exum2.n | nroff -ms | colcrt &#8211; | more</code>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-col/">col</a></code>(1), <code><a href="/docs/linux/man/1-more/">more</a></code>(1), <code><a href="/docs/linux/man/1-nroff/">nroff</a></code>(1), <code><a href="/docs/linux/man/1-troff/">troff</a></code>(1), <code><a href="/docs/linux/man/1-ul/">ul</a></code>(1)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>colcrt</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
