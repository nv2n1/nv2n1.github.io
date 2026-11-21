---

title: "ocrad(1)"
name: "ocrad"
section: "1"
letter: "o"
url: "/docs/linux/man/1-ocrad/"
description: "Ocrad – manual page for Ocrad 0.18"
---

<p> Ocrad &#8211; manual page for Ocrad 0.18</p>
<h2>SYNOPSIS</h2>
<p> <code>ocrad</code> [<i>options</i>] [<i>files</i>]</p>
<h2>DESCRIPTION</h2>
<p> GNU Ocrad &#8211; Optical Character Recognition program. Reads pnm file(s), or standard input, and sends text to standard output.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>-V</code>, <code>&#8211;version</code></dt>
<dd> output version information and exit</dd>
<dt><code>-a</code>, <code>&#8211;append</code></dt>
<dd> append text to output file</dd>
<dt><code>-c</code>, <code>&#8211;charset=</code>&lt;name&gt;</dt>
<dd> try `&#8211;charset=help&#8217; for a list of names</dd>
<dt><code>-e</code>, <code>&#8211;filter=</code>&lt;name&gt;</dt>
<dd> try `&#8211;filter=help&#8217; for a list of names</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> force overwrite of output file</dd>
<dt><code>-F</code>, <code>&#8211;format=</code>&lt;fmt&gt;</dt>
<dd> output format (byte, utf8)</dd>
<dt><code>-i</code>, <code>&#8211;invert</code></dt>
<dd> invert image levels (white on black)</dd>
<dt><code>-l</code>, <code>&#8211;layout</code></dt>
<dd> perform layout analysis</dd>
<dt><code>-o</code> &lt;file&gt;</dt>
<dd> place the output into &lt;file&gt;</dd>
<dt><code>-p</code>, <code>&#8211;crop=</code>&lt;l,t,r,b&gt;</dt>
<dd> crop input image by given rectangle</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> suppress all messages</dd>
<dt><code>-s</code>, <code>&#8211;scale</code>=<i>[-]</i>&lt;n&gt;</dt>
<dd> scale input image by [1/]&lt;n&gt;</dd>
<dt><code>-t</code>, <code>&#8211;transform=</code>&lt;name&gt;</dt>
<dd> try `&#8211;transform=help&#8217; for a list of names</dd>
<dt><code>-T</code>, <code>&#8211;threshold=</code>&lt;n%&gt;</dt>
<dd> threshold for binarization (0-100%)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> be verbose</dd>
<dt><code>-x</code> &lt;file&gt;</dt>
<dd> export OCR Results File to &lt;file&gt;</dd></dl>
<h2>REPORTING BUGS</h2>
<p> Report bugs to bug-ocrad [at] gnu.org Ocrad home page: <a rel="nofollow" href="http://www.gnu.org/software/ocrad/ocrad.html">http://www.gnu.org/software/ocrad/ocrad.html</a> General help using GNU software: <a rel="nofollow" href="http://www.gnu.org/gethelp">http://www.gnu.org/gethelp</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2009 Antonio Diaz Diaz. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>Ocrad</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>Ocrad</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info Ocrad</code></dd></dl>
<p> should give you access to the complete manual. </p>
