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
<dt><code>-h</code></p>
<dd> (ignored)</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> report a few statistics on stderr</p>
<dt><code>&#8211;help</code></p>
<dd> display this help then exit</p>
<dt><code>&#8211;version</code></p>
<dd> display program version then exit</dl>
<h3>Formatting output:</h3>
<dl>
<dt><code>-T</code>, <code>&#8211;initial-tab</code></p>
<dd> produce TAB instead of initial space</p>
<dt><code>-l</code>, <code>&#8211;paginate</code></p>
<dd> paginate output through `pr&#8217;</p>
<dt><code>-S</code>, <code>&#8211;string</code>[=<i>,STRING/</i>]</p>
<dd> take note of another user STRING</p>
<dt><code>-V</code>, <code>&#8211;show-links</code></p>
<dd> give file and line references in annotations</p>
<dt><code>-t</code>, <code>&#8211;expand-tabs</code></p>
<dd> expand tabs to spaces in the output</dl>
<h3>Debugging:</h3>
<dl>
<dt><code>-0</code>, <code>&#8211;debugging</code></p>
<dd> output many details about what is going on</dl>
<h3>Word mode options:</h3>
<dl>
<dt><code>-1</code>, <code>&#8211;no-deleted</code></p>
<dd> inhibit output of deleted words</p>
<dt><code>-2</code>, <code>&#8211;no-inserted</code></p>
<dd> inhibit output of inserted words</p>
<dt><code>-3</code>, <code>&#8211;no-common</code></p>
<dd> inhibit output of common words</p>
<dt><code>-A</code>, <code>&#8211;auto-pager</code></p>
<dd> automatically calls a pager</p>
<dt><code>-k</code>, <code>&#8211;less-mode</code></p>
<dd> variation of printer mode for &quot;less&quot;</p>
<dt><code>-m</code>, <code>&#8211;avoid-wraps</code></p>
<dd> do not extend fields through newlines</p>
<dt><code>-o</code>, <code>&#8211;printer</code></p>
<dd> overstrike as for printers</p>
<dt><code>-z</code>, <code>&#8211;terminal</code></p>
<dd> use termcap as for terminal displays</p>
<dt><code>-O</code>, <code>&#8211;item-regexp</code>=<i>,REGEXP/</i></p>
<dd> compare items as defined by REGEXP</p>
<dt><code>-W</code>, <code>&#8211;word-mode</code></p>
<dd> compare words instead of lines</dl>
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
<dd> <code>info mdiff</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
