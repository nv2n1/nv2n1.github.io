---
title: "mdiff(1)"
name: "mdiff"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mdiff/"
description: "mdiff – manual page for mdiff 1.2.2"
---

<h2>NAME</h2>
<p> mdiff &#8211; manual page for mdiff 1.2.2</p>
<h2>SYNOPSIS</h2>
<p> <code>mdiff</code> [<i>,OPTION/</i>]&#8230; [<i>,FILE/</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> mdiff &#8211; Studies multiple files and searches for similar sequences, it then produces possibly detailed lists of differences and similarities.</p>
<h3>Operation modes:</h3>
<dl>
<dt><code>-h</code></dt>
<dd> (ignored)</dd>
<dt><code>-v</code>, <code>&#8211;verbose</code></dt>
<dd> report a few statistics on stderr</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help then exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> display program version then exit</dd></dl>
<h3>Formatting output:</h3>
<dl>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></dt>
<dd> produce TAB instead of initial space</dd>
<dt><code>-l</code>, <code>&#8211;paginate</code></dt>
<dd> paginate output through `pr&#8217;</dd>
<dt><code>-S</code>, <code>&#8211;string</code>[=<i>,STRING/</i>]</dt>
<dd> take note of another user STRING</dd>
<dt><code>-V</code>, <code>&#8211;show-links</code></dt>
<dd> give file and line references in annotations</dd>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></dt>
<dd> expand tabs to spaces in the output</dd></dl>
<h3>Debugging:</h3>
<dl>
<dt><code>-0</code>, <code>&#8211;debugging</code></dt>
<dd> output many details about what is going on</dd></dl>
<h3>Word mode options:</h3>
<dl>
<dt><code>-1</code>, <code>&#8211;no-deleted</code></dt>
<dd> inhibit output of deleted words</dd>
<dt><code>-2</code>, <code>&#8211;no-inserted</code></dt>
<dd> inhibit output of inserted words</dd>
<dt><code>-3</code>, <code>&#8211;no-common</code></dt>
<dd> inhibit output of common words</dd>
<dt><code>-A</code>, <code>&#8211;auto-pager</code></dt>
<dd> automatically calls a pager</dd>
<dt><code>-k</code>, <code>&#8211;less-mode</code></dt>
<dd> variation of printer mode for &quot;less&quot;</dd>
<dt><code>-m</code>, <code>&#8211;avoid-wraps</code></dt>
<dd> do not extend fields through newlines</dd>
<dt><code>-o</code>, <code>&#8211;printer</code></dt>
<dd> overstrike as for printers</dd>
<dt><code>-z</code>, <code>&#8211;terminal</code></dt>
<dd> use termcap as for terminal displays</dd>
<dt><code>-O</code>, <code>&#8211;item-regexp</code>=<i>,REGEXP/</i></dt>
<dd> compare items as defined by REGEXP</dd>
<dt><code>-W</code>, <code>&#8211;word-mode</code></dt>
<dd> compare words instead of lines</dd></dl>
<p> With no FILE, or when FILE is -, read standard input.</p>
<h2>AUTHOR</h2>
<p> Written by Franc,ois Pinard &lt;pinard [at] iro.umontreal.ca&gt;.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;wdiff-bugs [at] gnu.org&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1992, 1997, 1998, 1999, 2010 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>mdiff</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>mdiff</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info mdiff</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
