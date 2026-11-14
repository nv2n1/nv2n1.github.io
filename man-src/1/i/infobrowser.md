---
title: "infobrowser(1)"
name: "infobrowser"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infobrowser/"
description: "info – read Info documents"
---

<h2 class="name">NAME</h2>
<p> info &#8211; read Info documents </p>
<h2>SYNOPSIS</h2>
<p> <code>info</code> [<i>,OPTION/</i>]&#8230; [<i>,MENU-ITEM/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Read documentation in Info format.</p>
<h3>Frequently-used options:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> use all matching manuals</p>
<dt><code>-k</code>, <code>&#8211;apropos</code>=<i>,STRING/</i></p>
<dd> look up STRING in all indices of all manuals</p>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></p>
<dd> add DIR to INFOPATH</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>,MANUAL/</i></p>
<dd> specify Info manual to visit</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;index-search</code>=<i>,STRING/</i></p>
<dd> go to node pointed by index entry STRING</p>
<dt><code>-n</code>, <code>&#8211;node</code>=<i>,NODENAME/</i></p>
<dd> specify nodes in first visited Info file</p>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></p>
<dd> output selected nodes to FILE</p>
<dt><code>-O</code>, <code>&#8211;show-options</code>, <code>&#8211;usage</code></p>
<dd> go to command-line options node</p>
<dt><code>&#8211;subnodes</code></p>
<dd> recursively output menu items</p>
<dt><code>-v</code>, <code>&#8211;variable</code> VAR=VALUE</p>
<dd> assign VALUE to Info variable VAR</p>
<dt><code>&#8211;version</code></p>
<dd> display version information and exit</p>
<dt><code>-w</code>, <code>&#8211;where</code>, <code>&#8211;location</code></p>
<dd> print physical location of Info file</dl>
<p> The first non-option argument, if present, is the menu entry to start from; it is searched for in all &#8216;dir&#8217; files along INFOPATH. If it is not present, info merges all &#8216;dir&#8217; files and shows the result. Any remaining arguments are treated as the names of menu items relative to the initial node visited. </p>
<p> For a summary of key bindings, type H within Info.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>info</p>
<dd> show top-level dir menu</p>
<dt>info info-stnd</p>
<dd> show the manual for this Info program</p>
<dt>info emacs</p>
<dd> start at emacs node from top-level dir</p>
<dt>info emacs buffers</p>
<dd> select buffers menu entry in emacs manual</p>
<dt>info emacs -n Files</p>
<dd> start at Files node within emacs manual</p>
<dt>info &#8216;(emacs)Files&#8217;</p>
<dd> alternative way to start at Files node</p>
<dt>info &#8211;show-options emacs</p>
<dd> start at node with emacs&#8217; command line options</p>
<dt>info &#8211;subnodes -o out.txt emacs</p>
<dd> dump entire emacs manual to out.txt</p>
<dt>info -f ./foo.info</p>
<dd> show file ./foo.info, not searching dir</dl>
<h2>REPORTING BUGS</h2>
<p> Email bug reports to bug-texinfo [at] gnu.org, general questions and discussion to help-texinfo [at] gnu.org.<br />
 Texinfo home page: <a rel="nofollow" href="http://www.gnu.org/software/texinfo/">http://www.gnu.org/software/texinfo/</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2021 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>info</code> is maintained as a Texinfo manual. If the <code>info</code> program is properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info info</code></dl>
<p> should give you access to the complete manual. (Or, if you have Emacs, M-x info will lead to the manual.) </p>
<h2>Index</h2>
