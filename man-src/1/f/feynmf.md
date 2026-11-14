---
title: "feynmf(1)"
name: "feynmf"
section: "1"
letter: "f"
url: "/docs/linux/man/1-feynmf/"
description: "feynmf – Process LaTeX files using FeynMF"
---

<h2 class="name">NAME</h2>
<p> feynmf &#8211; Process LaTeX files using FeynMF </p>
<h2>SYNOPSIS</h2>
<p> <code>feynmf</code> [<code>-hvqncfT</code>] [<code>-t</code> <i>tfm</i> [<code>-t</code> <i>tfm</i> &#8230;]] [<code>-m</code> <i>mode</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<i>file</i>&nbsp;[<i>file</i>&nbsp;&#8230;] </p>
<p> <code>feynmf</code> [<code>&#8211;help</code>] [<code>&#8211;version</code>] [<code>&#8211;quiet</code>] [<code>&#8211;noexec</code>] [<code>&#8211;clean</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;force</code>]&nbsp;[<code>&#8211;notfm</code>]&nbsp;[<code>&#8211;tfm</code>&nbsp;<i>tfm</i>&nbsp;[<code>&#8211;tfm</code>&nbsp;<i>tfm</i>&nbsp;&#8230;]]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;[<code>&#8211;mode</code>&nbsp;<i>mode</i>]&nbsp;<i>file</i>&nbsp;[<i>file</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> The most complicated part of using the <code>FeynMF</code> style appears to be the proper invocation of <code>Metafont</code>. The <code>feynmf</code> script provides a convenient front end and will automagically invoke <code>Metafont</code> with the proper mode and magnification. It will also avoid cluttering system font directories and offers an option to clean them.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Print a short help text.</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Print the version of <code>feynmf</code>.</p>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Don&#8217;t echo the commands being executed.</p>
<dt><code>-n</code>, <code>&#8211;noexec</code></p>
<dd> Don&#8217;t execute <code>LaTeX</code> or <code>Metafont</code>.</p>
<dt><code>-c</code>, <code>&#8211;clean</code></p>
<dd> Offer to delete font files that have accidentally been placed in a system directory by the <code>MakeTeXTFM</code> and <code>MakeTeXPK</code> scripts (these scripts are run by <code>tex</code> (and <code>latex</code>) in the background). This option has only been tested with recent versions of <font SIZE="-1">UNIX</font> TeX.</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> Don&#8217;t ask any questions.</p>
<dt><code>-T</code>, <code>&#8211;notfm</code></p>
<dd> Don&#8217;t try to prepare fake <tt>&quot;.tfm&quot;</tt> files for the first run.</p>
<dt><code>-t</code>, <code>&#8211;tfm</code> <i>tfm</i></p>
<dd> Don&#8217;t try guess the names of the <tt>&quot;.tfm&quot;</tt> files to fake for the first run and use the given name(s) instead. This option can be useful if our incomplete parsing of the LaTeX input files fails.</p>
<dt>&#8211;<code>m</code> <i>mode</i>, <code>&#8211;mode</code> <i>mode</i></p>
<dd> Select the <font SIZE="-1">METAFONT</font> mode <i>mode</i>. The default is guessed or <tt>&quot;localfont&quot;</tt> if the guess fails.</p>
<dt><i>file</i></p>
<dd> Main <code>LaTeX</code> input files.</p>
<dt><i>file</i> &#8230;</p>
<dd> Other LaTeX input files that are included by the main file.</dl>
<h2>AUTHOR</h2>
<p> Thorsten Ohl &lt;Thorsten.Ohl [at] Physik.TH-Darmstadt.de&gt;</p>
<h2>BUGS</h2>
<p> The preparation of <tt>&quot;.tfm&quot;</tt> files is not foolproof yet, because we can parse <code>TeX</code> files only superficially. </p>
<p> This script has only been tested for recent <code>teTeX</code> distributions of <font SIZE="-1">UNIX</font> <code>TeX</code>, though it will probably work with other versions of <font SIZE="-1">UNIX</font> <code>TeX</code>. The author will be grateful for portability suggestions, even concerning <code>Borg</code> operating systems, for the benefit of those users that are forced to live with <font SIZE="-1">DOS</font> or Windows. </p>
<h2>Index</h2>
