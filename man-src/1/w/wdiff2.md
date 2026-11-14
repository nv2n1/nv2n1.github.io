---
title: "wdiff2(1)"
name: "wdiff2"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wdiff2/"
description: "wdiff – manual page for wdiff 1.2.2"
---

<h2>NAME</h2>
<p> wdiff &#8211; manual page for wdiff 1.2.2</p>
<h2>SYNOPSIS</h2>
<p> <code>wdiff2</code> [<i>,OPTION/</i>]&#8230; <i>,FILE1 FILE2/</i></p>
<h2>DESCRIPTION</h2>
<p> wdiff &#8211; Compute word differences by internally launching `mdiff <code>-W</code>&#8216;. This program exists mainly to support the now oldish `wdiff&#8217; syntax. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;copyright</code></p>
<dd> display copyright then exit</p>
<dt><code>-1</code>, <code>&#8211;no-deleted</code></p>
<dd> inhibit output of deleted words</p>
<dt><code>-2</code>, <code>&#8211;no-inserted</code></p>
<dd> inhibit output of inserted words</p>
<dt><code>-3</code>, <code>&#8211;no-common</code></p>
<dd> inhibit output of common words</p>
<dt><code>-a</code>, <code>&#8211;auto-pager</code></p>
<dd> automatically calls a pager</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help then exit</p>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></p>
<dd> fold character case while comparing</p>
<dt><code>-l</code>, <code>&#8211;less-mode</code></p>
<dd> variation of printer mode for &quot;less&quot;</p>
<dt><code>-n</code>, <code>&#8211;avoid-wraps</code></p>
<dd> do not extend fields through newlines</p>
<dt><code>-p</code>, <code>&#8211;printer</code></p>
<dd> overstrike as for printers</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> inhibit the `mdiff&#8217; call message</p>
<dt><code>-s</code>, <code>&#8211;statistics</code></p>
<dd> say how many words deleted, inserted etc.</p>
<dt><code>-t</code>, <code>&#8211;terminal</code></p>
<dd> use termcap as for terminal displays</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> display program version then exit</p>
<dt><code>-w</code>, <code>&#8211;start-delete</code>=<i>,STRING/</i></p>
<dd> string to mark beginning of delete region</p>
<dt><code>-x</code>, <code>&#8211;end-delete</code>=<i>,STRING/</i></p>
<dd> string to mark end of delete region</p>
<dt><code>-y</code>, <code>&#8211;start-insert</code>=<i>,STRING/</i></p>
<dd> string to mark beginning of insert region</p>
<dt><code>-z</code>, <code>&#8211;end-insert</code>=<i>,STRING/</i></p>
<dd> string to mark end of insert region</dl>
<p> This program also tells how `mdiff&#8217; could have been called directly.</p>
<h2>AUTHOR</h2>
<p> Written by Franc,ois Pinard &lt;pinard [at] iro.umontreal.ca&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;wdiff-bugs [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1997, 1998, 1999 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>wdiff</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>wdiff</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info wdiff</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
