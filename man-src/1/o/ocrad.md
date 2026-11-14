---
title: "ocrad(1)"
name: "ocrad"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocrad/"
description: "Ocrad – manual page for Ocrad 0.18"
---

<h2>NAME</h2>
<p> Ocrad &#8211; manual page for Ocrad 0.18</p>
<h2>SYNOPSIS</h2>
<p> <code>ocrad</code> [<i>options</i>] [<i>files</i>]</p>
<h2>DESCRIPTION</h2>
<p> GNU Ocrad &#8211; Optical Character Recognition program. Reads pnm file(s), or standard input, and sends text to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> output version information and exit</p>
<dt><code>-a</code>, <code>&#8211;append</code></p>
<dd> append text to output file</p>
<dt><code>-c</code>, <code>&#8211;charset=</code>&lt;name&gt;</p>
<dd> try `&#8211;charset=help&#8217; for a list of names</p>
<dt><code>-e</code>, <code>&#8211;filter=</code>&lt;name&gt;</p>
<dd> try `&#8211;filter=help&#8217; for a list of names</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> force overwrite of output file</p>
<dt><code>-F</code>, <code>&#8211;format=</code>&lt;fmt&gt;</p>
<dd> output format (byte, utf8)</p>
<dt><code>-i</code>, <code>&#8211;invert</code></p>
<dd> invert image levels (white on black)</p>
<dt><code>-l</code>, <code>&#8211;layout</code></p>
<dd> perform layout analysis</p>
<dt><code>-o</code> &lt;file&gt;</p>
<dd> place the output into &lt;file&gt;</p>
<dt><code>-p</code>, <code>&#8211;crop=</code>&lt;l,t,r,b&gt;</p>
<dd> crop input image by given rectangle</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> suppress all messages</p>
<dt><code>-s</code>, <code>&#8211;scale</code>=<i>[-]</i>&lt;n&gt;</p>
<dd> scale input image by [1/]&lt;n&gt;</p>
<dt><code>-t</code>, <code>&#8211;transform=</code>&lt;name&gt;</p>
<dd> try `&#8211;transform=help&#8217; for a list of names</p>
<dt><code>-T</code>, <code>&#8211;threshold=</code>&lt;n%&gt;</p>
<dd> threshold for binarization (0-100%)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> be verbose</p>
<dt><code>-x</code> &lt;file&gt;</p>
<dd> export OCR Results File to &lt;file&gt;</dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ocrad [at] gnu.org Ocrad home page: <a rel="nofollow" href="http://www.gnu.org/software/ocrad/ocrad.html">http://www.gnu.org/software/ocrad/ocrad.html</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Antonio Diaz Diaz. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>Ocrad</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>Ocrad</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info Ocrad</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
