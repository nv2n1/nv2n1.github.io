---

title: "wdiff2(1)"
name: "wdiff2"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wdiff2/"
description: "wdiff – manual page for wdiff 1.2.2"
---

<p> wdiff &#8211; manual page for wdiff 1.2.2</p>
<h2>SYNOPSIS</h2>
<p> <code>wdiff2</code> [<i>,OPTION/</i>]&#8230; <i>,FILE1 FILE2/</i></p>
<h2>DESCRIPTION</h2>
<p> wdiff &#8211; Compute word differences by internally launching `mdiff <code>-W</code>&#8216;. This program exists mainly to support the now oldish `wdiff&#8217; syntax. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-C</code>, <code>&#8211;copyright</code></dt>
<dd> display copyright then exit</dd>
<dt><code>-1</code>, <code>&#8211;no-deleted</code></dt>
<dd> inhibit output of deleted words</dd>
<dt><code>-2</code>, <code>&#8211;no-inserted</code></dt>
<dd> inhibit output of inserted words</dd>
<dt><code>-3</code>, <code>&#8211;no-common</code></dt>
<dd> inhibit output of common words</dd>
<dt><code>-a</code>, <code>&#8211;auto-pager</code></dt>
<dd> automatically calls a pager</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help then exit</dd>
<dt><code>-i</code>, <code>&#8211;ignore-case</code></dt>
<dd> fold character case while comparing</dd>
<dt><code>-l</code>, <code>&#8211;less-mode</code></dt>
<dd> variation of printer mode for &quot;less&quot;</dd>
<dt><code>-n</code>, <code>&#8211;avoid-wraps</code></dt>
<dd> do not extend fields through newlines</dd>
<dt><code>-p</code>, <code>&#8211;printer</code></dt>
<dd> overstrike as for printers</dd>
<dt><code>-q</code>, <code>&#8211;quiet</code></dt>
<dd> inhibit the `mdiff&#8217; call message</dd>
<dt><code>-s</code>, <code>&#8211;statistics</code></dt>
<dd> say how many words deleted, inserted etc.</dd>
<dt><code>-t</code>, <code>&#8211;terminal</code></dt>
<dd> use termcap as for terminal displays</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd> display program version then exit</dd>
<dt><code>-w</code>, <code>&#8211;start-delete</code>=<i>,STRING/</i></dt>
<dd> string to mark beginning of delete region</dd>
<dt><code>-x</code>, <code>&#8211;end-delete</code>=<i>,STRING/</i></dt>
<dd> string to mark end of delete region</dd>
<dt><code>-y</code>, <code>&#8211;start-insert</code>=<i>,STRING/</i></dt>
<dd> string to mark beginning of insert region</dd>
<dt><code>-z</code>, <code>&#8211;end-insert</code>=<i>,STRING/</i></dt>
<dd> string to mark end of insert region</dd></dl>
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
</dt><dd> <code>info wdiff</code></dd></dl>
<p> should give you access to the complete manual. </p>
