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
<dl>
<dt>&#8211;</dt>
<dd> Four text families (with lining and oldstyle digits, each in both tabular and proportional variants), all with the following shapes:</dd>
<dl>
<dl>
<dl>
<dt><i>n</i></dt>
<dd> Roman (i.e., upright) text</dd>
<dt><i>it</i>, <i>sl</i></dt>
<dd> Italic and slanted (sometimes called oblique) text</dd>
<dt><i>sc</i></dt>
<dd> Small caps</dd>
<dt><i>scit</i>, <i>scsl</i></dt>
<dd> Italic and slanted small caps</dd>
<dt><i>sw</i></dt>
<dd> Swash</dd>
<dt><i>nw</i></dt>
<dd> &#8220;Upright swash&#8221;</dd></dl>
</dl>
<dl>
</dl>
</dl>
<dl>
</dl>
<dt>&#8211;</dt>
<dd> For each T1-encoded text family: a family of TS1-encoded symbol fonts, in roman, italic and slanted shapes.</dd>
<dt>&#8211;</dt>
<dd> Families with superiors, inferiors, numerators and denominators, in roman, italic and slanted shapes.</dd>
<dt>&#8211;</dt>
<dd> Families with &#8220;Titling&#8221; characters; these &#8220;&#8230; replace the default glyphs with corresponding forms designed specifically for titling. These may be all-capital and/or larger on the body, and adjusted for viewing at larger sizes&#8221; (according to the OpenType Specification).</dd>
<dt>&#8211;</dt>
<dd> An ornament family; also in roman, italic and slanted shapes.</dd></dl>
</dl>
<dl>
</dl>
<p> Of course, if your fonts don&#8217;t contain italics, oldstyle digits, small caps etc., the corresponding shapes and families are not created. In addition, the creation of most families and shapes can be controlled by the user (see &#8220;COMMAND-LINE <font SIZE="-1">OPTIONS&#8221;</font> below). </p>
<p> These families use the <i>FontPro</i> project&#8217;s naming scheme: <i>&lt;FontFamily&gt;-&lt;Suffix&gt;</i>, where <i>&lt;Suffix&gt;</i> is:</p>
<dl>
<dt><i></i><font SIZE="-1"><i>LF</i></font><i></i></dt>
<dd> proportional (i.e., figures have varying widths) lining figures</dd>
<dt><i></i><font SIZE="-1"><i>TLF</i></font><i></i></dt>
<dd> tabular (i.e., all figures have the same width) lining figures</dd>
<dt><i>OsF</i></dt>
<dd> proportional oldstyle figures</dd>
<dt><i>TOsF</i></dt>
<dd> tabular oldstyle figures</dd>
<dt><i>Sup</i></dt>
<dd> superior characters (note that most fonts have only an incomplete set of superior characters: digits, some punctuation and the letters <i>abdeilmnorst</i>; normal forms are used for other characters)</dd>
<dt><i>Inf</i></dt>
<dd> inferior characters; usually only digits and some punctuation, normal forms for other characters</dd>
<dt><i>Titl</i></dt>
<dd> Titling characters; see above</dd>
<dt><i>Orn</i></dt>
<dd> ornaments</dd>
<dt><i>Numr</i>, <i>Dnom</i></dt>
<dd> numerators and denominators</dd></dl>
<p> The individual fonts are named <i>&lt;FontName&gt;-&lt;suffix&gt;-&lt;shape&gt;-&lt;enc&gt;</i>, where <i>&lt;suffix&gt;</i> is the same as above (but in lowercase), <i>&lt;shape&gt;</i> is either empty, &#8220;sc&#8221; or &#8220;swash&#8221;, and <i>&lt;enc&gt;</i> is the encoding (also in lowercase). A typical name in this scheme would be <i>FiraSans-Light-osf-sc-ly1</i>.</p>
<h3>Using the fonts in your LaTeX documents</h3>
<p> <code>autoinst</code> generates a style file for using the fonts in LaTeX documents, named <i>&lt;FontFamily&gt;.sty</i>. This style file also loads the <i>fontenc</i> and <i>textcomp</i> packages, if necessary. To use the fonts, add the command <tt>&quot;
</p>