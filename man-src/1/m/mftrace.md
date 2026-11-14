---
title: "mftrace(1)"
name: "mftrace"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mftrace/"
description: "mftrace – convert METAFONT format fonts into Type1 outline fonts"
---

<h2 class="name">NAME</h2>
<p> mftrace &#8211; convert METAFONT format fonts into Type1 outline fonts </p>
<h2>SYNOPSIS</h2>
<p> <code>mftrace</code> [<i>options</i>]<i> fontname</i></p>
<h2>DESCRIPTION</h2>
<p> <code>mftrace</code> is a program that can convert a METAFONT font into a Type1 font. It is simply called with the name of the font (without a `.mf&#8217; suffix) and produces a Type1 font file called either <i>fontname</i>.pfa or <i>fontname</i>.pfb depending on the command line options. With the help of <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1) it can produce other font formats too. </p>
<p> For tracing the bitmap, <code>mftrace</code> either uses <code><a href="/docs/linux/man/1-potrace/">potrace</a></code>(1) or <code><a href="/docs/linux/man/1-autotrace/">autotrace</a></code>(1) (the former preferred) if available; this can be overridden with the <code>&#8211;autotrace</code> and <code>&#8211;potrace</code> command line options.</p>
<h2>OPTIONS</h2>
<p> This program follows the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;).</p>
<dl>
<dt><code>-k</code>, <code>&#8211;keep</code></p>
<dd> Keep all output in directory `mftrace.dir&#8217;.</p>
<dt><code>&#8211;magnification=</code><i>MAG</i></p>
<dd> The magnification to use for the PFA file. The default is 1000. The larger the magnification, the more precise the PFA file will be. However, if the magnification is too large METAFONT can crash with overflow errors.</p>
<dt>
<dd> Sadly, many MF fonts contain resolution checks</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> if dots_per_inch * design_size &gt; 1500:</dl>
</dl>
<dt>
<dd> This check is susceptible to overflow errors. Such code should be reported as a bug, and changed to</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> if dots_per_inch &gt; (1500 / design_size):</dl>
</dl>
<dt><code>&#8211;formats=</code><i>FMT1</i><code>,</code><i>FMT2</i><code>,</code><i>&#8230;</i></p>
<dd> Specify which formats to generate (default is pfa). Choices are: `afm&#8217;, `pfa&#8217;, `pfb&#8217;, `ttf&#8217;, `svg&#8217;. Note that <code>fontforge</code> (formerly called <code>pfaedit</code>) must be installed to generate any format except `pfa&#8217; or `pfb&#8217;. For generating `afm&#8217; you need either <code>fontforge</code> or <code>ghostscript</code>.</p>
<dt><code>&#8211;simplify</code></p>
<dd> This passes the created Type1 font to <code>fontforge</code> (formerly called <code>pfaedit</code>) to simplify and autohint it.</p>
<dt><code>&#8211;gffile=</code><i>FILE</i></p>
<dd> Use generic font file <i>FILE</i> instead of running Metafont. (GF is the default output format of Metafont.)</p>
<dt><code>-I</code> <i>DIR</i>, <code>&#8211;include=</code><i>DIR</i></p>
<dd> Add <i>DIR</i> to the current path for searching files.</p>
<dt><code>&#8211;glyphs=</code><i>LIST</i></p>
<dd> Process only these glyphs. <i>LIST</i> is a comma separated list of decimal numbers or ranges, for example `1-10,50,55,90-100&#8242;.</p>
<dt><code>&#8211;tfmfile=</code><i>FILE</i></p>
<dd> Use <i>FILE</i> for the TFM file. (The default is to use <i>fontname</i>.tfm).</p>
<dt><code>-e</code> <i>ENC</i>, <code>&#8211;encoding=</code><i>ENC</i></p>
<dd> Use encoding file <i>ENC</i>. Encoding files used by <code>mftrace</code> are basically in the GhostScript/dvips format, but you may use a special <code>.notavail</code> glyph name in order to tell mftrace not to process a specific glyph. If this option is not specified, <code>mftrace</code> tries to determine the encoding file automatically, from the encoding specified in the TFM file, the default being `tex256.enc&#8217;.</p>
<dt><code>&#8211;keep-trying</code></p>
<dd> Try to continue if external programs called by mftrace fail. If METAFONT crashes with overflow errors, but nevertheless outputs a GF file, try to process its output as is (useful for some buggy fonts, see above). If <code>potrace</code> or <code>autotrace</code> fail to trace a specific character, first try it with a less smoothed curve, and if that fails, skip the character. By default, <code>mftrace</code> leaves a file `trace-bug-<i>font</i>&#8211;<i>char</i>.pbm&#8217; and stops the process with a request to file a bugreport.</p>
<dt><code>&#8211;dos-kpath</code></p>
<dd> Try to use MikTeX&#8217;s version of <code>kpsewhich</code>.</p>
<dt><code>&#8211;potrace</code></p>
<dd> Use <code>potrace</code> for tracing bitmaps. The default is to use <code>potrace</code> if it is found, otherwise to use <code>autotrace</code>.</p>
<dt><code>&#8211;autotrace</code></p>
<dd> Use <code>autotrace</code> for tracing bitmaps.</p>
<dt><code>&#8211;no-afm</code></p>
<dd> Don&#8217;t read the AFM file to find font information.</p>
<dt><code>&#8211;noround</code></p>
<dd> Do not round coordinates of control points to integer values (use with <code>&#8211;grid</code>). Disabled by default.</p>
<dt><code>&#8211;grid=</code><i>GRID</i></p>
<dd> Set reciprocal grid size in em units multiplied by ratio magnification/1000. For example, `<code>&#8211;grid 10 &#8211;magnification 1000</code>&#8216; rounds coordinates of control points to 1/10th of the em unit. Useful simultaneously with the <code>&#8211;noround</code> option. Default <i>GRID</i> value is~1, i.e., round to integer. This option is only used with <code>potrace</code>.</p>
<dt><code>-D,&#8211;define=</code><i>SYMBOL=VALUE</i></p>
<dd> Set the font info <i>SYMBOL</i> to the given <i>VALUE</i>. For example, <code>-DFamilyName=Foo</code> sets the font family name to <i>Foo</i>. <code>mftrace</code> tries to fill in sensible default values for the `FontName&#8217;, `FamilyName&#8217;, `FullName&#8217; and `Weight&#8217; fields.</p>
<dt><code>-V, &#8211;verbose</code></p>
<dd> Be verbose.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show version of program.</p>
<dt><code>-w, &#8211;warranty</code></p>
<dd> Show warranty and copyright.</dl>
<h2>COPYRIGHT</h2>
<p> You may redistribute copies of mftrace under the terms of the GNU General Public License &lt;<a rel="nofollow" href="http://www.gnu.org/licenses/gpl.html">http://www.gnu.org/licenses/gpl.html</a>&gt;. There is NO WARRANTY, to the extent permitted by law.<br />
 This manual page is copyright &#169; 2005,2006,2007 Julian Gilbey and is distributed under the GNU General Public License too.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mf/">mf</a></code>(1), <code><a href="/docs/linux/man/1-autotrace/">autotrace</a></code>(1), <code><a href="/docs/linux/man/1-potrace/">potrace</a></code>(1), <code><a href="/docs/linux/man/1-fontforge/">fontforge</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> <code>mftrace</code> was written by Han-Wen Nienhuys &lt;hanwen [at] xs4all.nl&gt;. This manual page was originally written by Julian Gilbey &lt;jdg [at] debian.org&gt; and has been revised by Werner Lemberg &lt;wl [at] gnu.org&gt;. </p>
<h2>Index</h2>
