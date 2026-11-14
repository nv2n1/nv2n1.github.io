---
title: "tfmtodit(1)"
name: "tfmtodit"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tfmtodit/"
description: "tfmtodit – create font files for use with groff -Tdvi"
---

<h2 class="name">NAME</h2>
<p> tfmtodit &#8211; create font files for use with groff -Tdvi </p>
<h2>SYNOPSIS</h2>
<p> [ <code>-s</code> ] [ <code>-g </code><i>gf_file</i> ] [ <code>-k </code><i>skewchar</i> ] <i>tfm_file</i> <i>map_file</i> <i>font</i> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <code>tfmtodit</code> creates a font file for use with <code>groff -Tdvi</code>. <i>tfm_file</i> is the name of the TeX font metric file for the font. <i>map_file</i> is a file giving the groff names for characters in the font; this file should consist of a sequence of lines of the form:</p>
<dl>
<dt>
<dd> <i>n c1 c2 </i>&#8230;</dl>
<p> where <i>n</i> is a decimal integer giving the position of the character in the font, and <i>c1</i>, <i>c2</i>,&#8230; are the groff names of the character. If a character has no groff names but exists in the tfm file, then it will be put in the groff font file as an unnamed character. <i>font</i> is the name of the groff font file. The groff font file is written to <i>font</i>. </p>
<p> The <code>-s</code> option should be given if the font is special (a font is <i>special</i> if <code>troff</code> should search it whenever a character is not found in the current font.) If the font is special, it should be listed in the <code>fonts</code> command in the DESC file; if it is not special, there is no need to list it, since <code>troff</code> can automatically mount it when it&#8217;s first used. </p>
<p> To do a good job of math typesetting, groff requires font metric information not present in the tfm file. The reason for this is that TeX has separate math italic fonts whereas groff uses normal italic fonts for math. The additional information required by groff is given by the two arguments to the <code>math_fit</code> macro in the Metafont programs for the Computer Modern fonts. In a text font (a font for which <code>math_fitting</code> is false), Metafont normally ignores these two arguments. Metafont can be made to put this information in the gf file by loading the following definition after <code>cmbase</code> when creating <i>cm.base</i>:</p>
<dl>
<dt>
<dd>
<pre><code>
def ignore_math_fit(expr left_adjustment, right_adjustment) =
    special "adjustment";
numspecial left_adjustment * 16 / designsize;
numspecial right_adjustment * 16 / designsize;
enddef;
</code></pre>
</dl>
<p> For the EC font family, load the following definition after <code>exbase</code> (it is probably easiest to patch <i>exbase.mf</i> locally):</p>
<dl>
<dt>
<dd>
<pre><code>
def ignore_math_fit(expr left_adjustment, right_adjustment) =
    ori_special "adjustment";
ori_numspecial left_adjustment * 16 / designsize;
ori_numspecial right_adjustment * 16 / designsize;
enddef;
</code></pre>
</dl>
<p> The gf file created using this modified <i>cm.base</i> or <i>exbase</i> should be specified with the <code>-g</code> option. The <code>-g</code> option should not be given for a font for which <code>math_fitting</code> is true.</p>
<h2>OPTIONS</h2>
<p> Whitespace is permitted between a command-line option and its argument.</p>
<dl>
<dt><code>-v</code></p>
<dd> Print the version number.</p>
<dt><code>-s</code></p>
<dd> The font is special. The effect of this option is to add the <code>special</code> command to the font file.</p>
<dt><code>-k</code><i>n</i></p>
<dd> The skewchar of this font is at position <i>n</i>. <i>n</i> should be an integer; it may be given in decimal, or with a leading <code>0</code> in octal, or with a leading <code>0x</code> in hexadecimal. The effect of this option is to ignore any kerns whose second component is the specified character.</p>
<dt><code>-g</code><i>gf_file</i></p>
<dd> <i>gf_file</i> is a gf file produced by Metafont containing special and numspecial commands giving additional font metric information.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devdvi/DESC</i></p>
<dd> Device description file.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:font/devdvi/</i>F</p>
<dd> Font description file for font <i>F</i>.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-grodvi/">grodvi</a></code>(1), <code><a href="/docs/linux/man/5-groff_font/">groff_font</a></code>(5) </p>
<h2>Index</h2>
