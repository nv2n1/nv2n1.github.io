---
title: "autoinst(1)"
name: "autoinst"
section: "1"
letter: "a"
url: "/docs/linux/man/1-autoinst/"
description: "autoinst – wrapper around the LCDF TypeTools, for installing and using OpenType fonts in LaTeX."
---

<h2 class="name">NAME</h2>
<p> autoinst &#8211; wrapper around the LCDF TypeTools, for installing and using OpenType fonts in LaTeX. </p>
<h2>SYNOPSIS</h2>
<p> <code>autoinst</code> <i>-help</i> </p>
<p> <code>autoinst</code> [<i>options</i>] <code>font(s)</code></p>
<h2>DESCRIPTION</h2>
<p> Eddie Kohler&#8217;s <i></i><font SIZE="-1"><i>LCDF</i></font><i> TypeTools</i> are superb tools for installing OpenType fonts in LaTeX, but they can be hard to use: they need many, often long, command lines and don&#8217;t generate the <i>fd</i> and <i>sty</i> files LaTeX needs. <code>autoinst</code> simplifies the use of the <i>TypeTools</i> for font installation by generating and executing all commands for <i>otftotfm</i>, and by creating and installing all necessary <i>fd</i> and <i>sty</i> files. </p>
<p> Given a family of font files (in <i>otf</i> or <i>ttf</i> format), <code>autoinst</code> will create several LaTeX font families:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> Four text families (with lining and oldstyle digits, each in both tabular and proportional variants), all with the following shapes:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><i>n</i></p>
<dd> Roman (i.e., upright) text</p>
<dt><i>it</i>, <i>sl</i></p>
<dd> Italic and slanted (sometimes called oblique) text</p>
<dt><i>sc</i></p>
<dd> Small caps</p>
<dt><i>scit</i>, <i>scsl</i></p>
<dd> Italic and slanted small caps</p>
<dt><i>sw</i></p>
<dd> Swash</p>
<dt><i>nw</i></p>
<dd> &#8220;Upright swash&#8221;</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<dl>
<dt>
<dd></dl>
<dt>&#8211;</p>
<dd> For each T1-encoded text family: a family of TS1-encoded symbol fonts, in roman, italic and slanted shapes.</p>
<dt>&#8211;</p>
<dd> Families with superiors, inferiors, numerators and denominators, in roman, italic and slanted shapes.</p>
<dt>&#8211;</p>
<dd> Families with &#8220;Titling&#8221; characters; these &#8220;&#8230; replace the default glyphs with corresponding forms designed specifically for titling. These may be all-capital and/or larger on the body, and adjusted for viewing at larger sizes&#8221; (according to the OpenType Specification).</p>
<dt>&#8211;</p>
<dd> An ornament family; also in roman, italic and slanted shapes.</dl>
</dl>
<dl>
<dt>
<dd></dl>
<p> Of course, if your fonts don&#8217;t contain italics, oldstyle digits, small caps etc., the corresponding shapes and families are not created. In addition, the creation of most families and shapes can be controlled by the user (see &#8220;COMMAND-LINE <font SIZE="-1">OPTIONS&#8221;</font> below). </p>
<p> These families use the <i>FontPro</i> project&#8217;s naming scheme: <i>&lt;FontFamily&gt;-&lt;Suffix&gt;</i>, where <i>&lt;Suffix&gt;</i> is:</p>
<dl>
<dt><i></i><font SIZE="-1"><i>LF</i></font><i></i></p>
<dd> proportional (i.e., figures have varying widths) lining figures</p>
<dt><i></i><font SIZE="-1"><i>TLF</i></font><i></i></p>
<dd> tabular (i.e., all figures have the same width) lining figures</p>
<dt><i>OsF</i></p>
<dd> proportional oldstyle figures</p>
<dt><i>TOsF</i></p>
<dd> tabular oldstyle figures</p>
<dt><i>Sup</i></p>
<dd> superior characters (note that most fonts have only an incomplete set of superior characters: digits, some punctuation and the letters <i>abdeilmnorst</i>; normal forms are used for other characters)</p>
<dt><i>Inf</i></p>
<dd> inferior characters; usually only digits and some punctuation, normal forms for other characters</p>
<dt><i>Titl</i></p>
<dd> Titling characters; see above</p>
<dt><i>Orn</i></p>
<dd> ornaments</p>
<dt><i>Numr</i>, <i>Dnom</i></p>
<dd> numerators and denominators</dl>
<p> The individual fonts are named <i>&lt;FontName&gt;-&lt;suffix&gt;-&lt;shape&gt;-&lt;enc&gt;</i>, where <i>&lt;suffix&gt;</i> is the same as above (but in lowercase), <i>&lt;shape&gt;</i> is either empty, &#8220;sc&#8221; or &#8220;swash&#8221;, and <i>&lt;enc&gt;</i> is the encoding (also in lowercase). A typical name in this scheme would be <i>FiraSans-Light-osf-sc-ly1</i>.</p>
<h3>Using the fonts in your LaTeX documents</h3>
<p> <code>autoinst</code> generates a style file for using the fonts in LaTeX documents, named <i>&lt;FontFamily&gt;.sty</i>. This style file also loads the <i>fontenc</i> and <i>textcomp</i> packages, if necessary. To use the fonts, add the command <tt>&quot;
