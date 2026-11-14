---
title: "ptx(1)"
name: "ptx"
section: "1"
letter: "p"
url: "/docs/linux/man/1-ptx/"
description: "ptx – produce a permuted index of file contents"
---

<h2 class="name">NAME</h2>
<p> ptx &#8211; produce a permuted index of file contents </p>
<h2>SYNOPSIS</h2>
<p> <code>ptx</code> [<i>,OPTION/</i>]&#8230; [<i>,INPUT/</i>]&#8230; <i>,(without -G)/</i><br />
 <code>ptx</code> <i>,-G /</i>[<i>,OPTION/</i>]&#8230; [<i>,INPUT /</i>[<i>,OUTPUT/</i>]]</p>
<h2>DESCRIPTION</h2>
<p> Output a permuted index, including context, of the words in the input files. </p>
<p> With no FILE, or when FILE is -, read standard input. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-A</code>, <code>&#8211;auto-reference</code></p>
<dd> output automatically generated references</p>
<dt><code>-G</code>, <code>&#8211;traditional</code></p>
<dd> behave more like System V &#8216;ptx&#8217;</p>
<dt><code>-F</code>, <code>&#8211;flag-truncation</code>=<i>,STRING/</i></p>
<dd> use STRING for flagging line truncations. The default is &#8216;/&#8217;</p>
<dt><code>-M</code>, <code>&#8211;macro-name</code>=<i>,STRING/</i></p>
<dd> macro name to use instead of &#8216;xx&#8217;</p>
<dt><code>-O</code>, <code>&#8211;format</code>=<i>,roff/</i></p>
<dd> generate output as roff directives</p>
<dt><code>-R</code>, <code>&#8211;right-side-refs</code></p>
<dd> put references at right, not counted in <code>-w</code></p>
<dt><code>-S</code>, <code>&#8211;sentence-regexp</code>=<i>,REGEXP/</i></p>
<dd> for end of lines or end of sentences</p>
<dt><code>-T</code>, <code>&#8211;format</code>=<i>,tex/</i></p>
<dd> generate output as TeX directives</p>
<dt><code>-W</code>, <code>&#8211;word-regexp</code>=<i>,REGEXP/</i></p>
<dd> use REGEXP to match each keyword</p>
<dt><code>-b</code>, <code>&#8211;break-file</code>=<i>,FILE/</i></p>
<dd> word break characters in this FILE</p>
<dt><code>-f</code>, <code>&#8211;ignore-case</code></p>
<dd> fold lower case to upper case for sorting</p>
<dt><code>-g</code>, <code>&#8211;gap-size</code>=<i>,NUMBER/</i></p>
<dd> gap size in columns between output fields</p>
<dt><code>-i</code>, <code>&#8211;ignore-file</code>=<i>,FILE/</i></p>
<dd> read ignore word list from FILE</p>
<dt><code>-o</code>, <code>&#8211;only-file</code>=<i>,FILE/</i></p>
<dd> read only word list from this FILE</p>
<dt><code>-r</code>, <code>&#8211;references</code></p>
<dd> first field of each line is a reference</p>
<dt> <code>-t</code>, <code>&#8211;typeset-mode</code> &#8211; not implemented &#8211;</p>
<dt><code>-w</code>, <code>&#8211;width</code>=<i>,NUMBER/</i></p>
<dd>
<dd>output width in columns, reference excluded</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by F. Pinard.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/ptx">https://www.gnu.org/software/coreutils/ptx</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) ptx invocation&#8217; </p>
<h2>Index</h2>
