---
title: "synctex(1)"
name: "synctex"
section: "1"
letter: "s"
url: "/docs/linux/man/1-synctex/"
description: "synctex – command line client tool to support the Synchronize TeXnology available in most TeX engines."
---

<h2 class="name">NAME</h2>
<p> <code>synctex</code> &#8211; command line client tool to support the Synchronize TeXnology available in most TeX engines. </p>
<h2>SYNOPSIS</h2>
<p> <code>synctex</code> <i>command</i> [<i>options</i>] [<i>args</i>]</p>
<h2>OVERVIEW</h2>
<p> The Synchronization TeXnology is a feature of recent TeX engines. It allows to synchronize between input and output, which means to navigate from the source document to the typeset material and vice versa. </p>
<p> Run `synctex help&#8217; to access the built-in tool documentation.</p>
<h2>TEX ENGINE OPTION -synctex=NUMBER</h2>
<ul>
<li> If NUMBER=0 or no option is given, no synctex file is created.
<li> If NUMBER&lt;0, synctex files are text files.
<li> If NUMBER&gt;0, synctex files are compressed with gz.
<li> If NUMBER&amp;2, no .gz extension is used.
<li> If NUMBER&amp;4, activate form support, useful for pdftex.
<li> If NUMBER&amp;8, better file compression. </ul>
<p> Use for example `pdftex -synctex=15 foo.tex&#8217; to activate all the options. </p>
<p> Notice that LuaTeX option is `&#8211;synctex=NUMBER&#8217; with two dashes.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-synctex/">synctex</a>(5) <a href="/docs/linux/man/1-tex/">tex</a>(1)</p>
<h2>AUTHOR</h2>
<p> The Synchronize TeXnology is essentially due to Jerome Laurens, with useful suggestions by some well known actors of the TeX world.</p>
<h2>HISTORY Revised on Sun Apr 23 09:54:20 UTC 2017.</h2>
<h2>Index</h2>
