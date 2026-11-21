---

title: "infobrowser(1)"
name: "infobrowser"
section: "1"
letter: "i"
url: "/docs/linux/man/1-infobrowser/"
description: "info – read Info documents"
---

<p> info &#8211; read Info documents </p>
<h2>SYNOPSIS</h2>
<p> <code>info</code> [<i>,OPTION/</i>]&#8230; [<i>,MENU-ITEM/</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> Read documentation in Info format.</p>
<h3>Frequently-used options:</h3>
<dl>
<dt><code>-a</code>, <code>&#8211;all</code></dt>
<dd> use all matching manuals</dd>
<dt><code>-k</code>, <code>&#8211;apropos</code>=<i>,STRING/</i></dt>
<dd> look up STRING in all indices of all manuals</dd>
<dt><code>-d</code>, <code>&#8211;directory</code>=<i>,DIR/</i></dt>
<dd> add DIR to INFOPATH</dd>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>,MANUAL/</i></dt>
<dd> specify Info manual to visit</dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;index-search</code>=<i>,STRING/</i></dt>
<dd> go to node pointed by index entry STRING</dd>
<dt><code>-n</code>, <code>&#8211;node</code>=<i>,NODENAME/</i></dt>
<dd> specify nodes in first visited Info file</dd>
<dt><code>-o</code>, <code>&#8211;output</code>=<i>,FILE/</i></dt>
<dd> output selected nodes to FILE</dd>
<dt><code>-O</code>, <code>&#8211;show-options</code>, <code>&#8211;usage</code></dt>
<dd> go to command-line options node</dd>
<dt><code>&#8211;subnodes</code></dt>
<dd> recursively output menu items</dd>
<dt><code>-v</code>, <code>&#8211;variable</code> VAR=VALUE</dt>
<dd> assign VALUE to Info variable VAR</dd>
<dt><code>&#8211;version</code></dt>
<dd> display version information and exit</dd>
<dt><code>-w</code>, <code>&#8211;where</code>, <code>&#8211;location</code></dt>
<dd> print physical location of Info file</dd></dl>
<p> The first non-option argument, if present, is the menu entry to start from; it is searched for in all &#8216;dir&#8217; files along INFOPATH. If it is not present, info merges all &#8216;dir&#8217; files and shows the result. Any remaining arguments are treated as the names of menu items relative to the initial node visited. </p>
<p> For a summary of key bindings, type H within Info.</p>
<h2>EXAMPLES</h2>
<dl>
<dt>info</dt>
<dd> show top-level dir menu</dd>
<dt>info info-stnd</dt>
<dd> show the manual for this Info program</dd>
<dt>info emacs</dt>
<dd> start at emacs node from top-level dir</dd>
<dt>info emacs buffers</dt>
<dd> select buffers menu entry in emacs manual</dd>
<dt>info emacs -n Files</dt>
<dd> start at Files node within emacs manual</dd>
<dt>info &#8216;(emacs)Files&#8217;</dt>
<dd> alternative way to start at Files node</dd>
<dt>info &#8211;show-options emacs</dt>
<dd> start at node with emacs&#8217; command line options</dd>
<dt>info &#8211;subnodes -o out.txt emacs</dt>
<dd> dump entire emacs manual to out.txt</dd>
<dt>info -f ./foo.info</dt>
<dd> show file ./foo.info, not searching dir</dd></dl>
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
</dt><dd> <code>info info</code></dd></dl>
<p> should give you access to the complete manual. (Or, if you have Emacs, M-x info will lead to the manual.) </p>
