---
title: "pkfix-helper(1)"
name: "pkfix-helper"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pkfix-helper/"
description: "pkfix-helper – preprocess dvips-produced PostScript documents before passing them to pkfix"
---

<h2 class="name">NAME</h2>
<p> pkfix-helper &#8211; preprocess dvips-produced PostScript documents before passing them to pkfix </p>
<h2>SYNOPSIS</h2>
<p> pkfix-helper [<code>&#8211;help</code>] [<code>&#8211;verbose</code>] [<code>&#8211;force</code>=<i>name</i>=<i>fontspec</i>] [<code>&#8211;ps</code>=<i>filename.ps</i>] [<code>&#8211;tex</code>=<i>filename.tex</i>] [<code>&#8211;cache</code>=<i>filename</i>] [<code>&#8211;include</code>=<i>fontspec</i>] [<code>&#8211;exclude</code>=<i>regexp</i>] [<code>&#8211;keep</code>=<i>fontspec</i>] [<code>&#8211;quiet</code>] [<code>&#8211;no-repeats</code>] [<code>&#8211;spp</code>=<i>number</i>] [<i>input.ps</i> [<i>output.ps</i>]]</p>
<h2>DESCRIPTION</h2>
<h3>Motivation</h3>
<p> PostScript documents created with old versions of <code>dvips</code> almost invariably utilize bitmapped (PostScript Type 3) fonts. The problem with bitmapped fonts is that they target a specific device resolution; a PostScript file produced using 300&nbsp;<font SIZE="-1">DPI</font> fonts will look grainy on a 600&nbsp;<font SIZE="-1">DPI</font> printer. Even worse, <i>all</i> bitmapped fonts look grainy when zoomed in on screen. The solution is to use vector (PostScript Type 1) fonts, which are resolution-independent and appear crisp at any size or scale. </p>
<p> While it is no longer difficult to configure <code>dvips</code> to use vector fonts, it is not always possible to rerun <code>dvips</code> on an old <i>.dvi</i> file. The <i>.dvi</i> file and document source may have been lost; or, the source may no longer compile because packages it depends upon may no longer be available. </p>
<p> Heiko Oberdiek&#8217;s <code>pkfix</code> script replaces bitmapped fonts in <code>dvips</code>-produced PostScript files with the corresponding vector fonts. It works by parsing the PostScript comments with which <code>dvips</code> surrounds bitmapped-font definitions. For example, a font definition beginning with the comment <tt>&quot;%DVIPSBitmapFont: Fi cmss10 11 28&quot;</tt> and ending with a matching <tt>%EndDVIPSBitmapFont</tt> is known to define font <tt>&quot;Fi&quot;</tt> as <tt>&quot;cmss10&quot;</tt> (Computer Modern Sans Serif at a design size of 10 points) scaled to <tt>11</tt>&nbsp;points. Only the <tt>28</tt> characters actually used by the document are defined. <code>pkfix</code> then replaces the font definition with one that defines <tt>&quot;Fi&quot;</tt> using the same set of characters but taken from the <i>cmss10.pfb</i> vector font file. </p>
<p> Unfortunately, <code>pkfix</code> works only with versions of <code>dvips</code> newer than v5.58 (ca. 1996). Naturally, the older a PostScript document, the less likely its sources still exist and can still be recompiled. Older versions of <code>dvips</code> lack <tt>%DVIPSBitmapFont</tt> comments and various other PostScript comments on which <code>pkfix</code> relies. Without PostScript comments to guide it, <code>pkfix</code> is unable to determine which vector fonts correspond with which bitmapped fonts.</p>
<h3>Overview</h3>
<p> The <code>pkfix-helper</code> script is a preprocessor for <code>pkfix</code> that attempts to determine the association between each document-font name (e.g.,&nbsp;<tt>&quot;Fi&quot;</tt>) in a PostScript file and the original font (e.g.,&nbsp;<tt>&quot;cmss10&quot;</tt>) and fonts size (e.g., <tt>11</tt>&nbsp;points). It then fabricates the PostScript comments that <code>pkfix</code> expects to see so that <code>pkfix</code> can do its job. </p>
<p> <code>pkfix-helper</code> works by comparing every document font against every <i>.tfm</i> font file it knows about (assuming that each such font has a corresponding <i>.pfb</i> vector version) and selecting the best matching <i>.tfm</i> file for every document font. <code>pkfix-helper</code> has access only to the widths of characters and only to those characters actually used in the document. Also, the program recognizes only a limited set of the most popular <i>.tfm</i> files and scaling factors. Consequently, the comparison is imperfect and <code>pkfix-helper</code> may attribute an incorrect font to a given name. Fonts comprising only one or two characters actually used in a document are particularly problematic for <code>pkfix-helper</code> because many fonts may be near-enough matches to fool the problem. </p>
<p> <code>pkfix-helper</code> is designed so that a user can guide the font-selection process by manually designating matching fonts. With a modicum of diligence and patience a user can correct any mismatched fonts and help the program provide proper input to <code>pkfix</code>.</p>
<h2>OPTIONS</h2>
<p> <code>pkfix-helper</code> accepts on the command line the filename of a PostScript document to process (with the default being the standard input device) and the filename of a modified PostScript document to create (with the default being the standard output device). The program also accepts the following command-line options:</p>
<h3>Frequently Used Options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display usage information and exit. The <code>&#8211;verbose</code> and <code>&#8211;quiet</code> options can be used to increase and decrease the amount of information presented.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> Increase the amount of status information that <code>pkfix-helper</code> displays as it runs. Additional instances of <code>&#8211;verbose</code> on the command line further increase the program&#8217;s verbosity. By default, only major operations are displayed. A single <code>&#8211;verbose</code> additionally displays information about individual font comparisons. A second <code>&#8211;verbose</code> additionally displays details about some of the program&#8217;s internal operations.</p>
<dt><code>-f</code> <i>name</i>=<i>fontspec</i>, <code>&#8211;force</code>=<i>name</i>=<i>fontspec</i></p>
<dd> Force <code>pkfix-helper</code> to associate a specific font with a given font name appearing the document. <i>name</i> is a (usually) two-character <code>dvips</code> font name such as <tt>&quot;Fa&quot;</tt>. <i>fontspec</i> is a font specification that comprises a font name and an optional scale: &quot;<i>font</i> [<tt>&quot;@&quot;</tt>&nbsp;<i>scale</i>]&quot;. Some examples of <i>fontspec</i>s are <tt>&quot;cmmi8&quot;</tt> and <tt>&quot;cmsy10&nbsp;@&nbsp;1.1X&quot;</tt>. </p>
<p> An asterisk used in the name of the font (e.g.,&nbsp;<tt>&quot;cmti*&quot;</tt>) will be replaced by all integers from 5 to 17 (<tt>&quot;cmti5&quot;</tt>, <tt>&quot;cmti6&quot;</tt>, &#8230;, <tt>&quot;cmti17&quot;</tt>). The scale can be written as a multiple of the design size (<tt>&quot;X&quot;</tt>) or as an absolute size in either TeX points (<tt>&quot;pt&quot;</tt>) or PostScript &#8220;big&#8221; points (<tt>&quot;bp&quot;</tt>). Hence, <tt>&quot;cmsy8&nbsp;@&nbsp;1.5X&quot;</tt>, <tt>&quot;cmsy8&nbsp;@&nbsp;12pt&quot;</tt>, and <tt>&quot;cmsy8&nbsp;@&nbsp;11.96bp&quot;</tt> all represent the <i>Computer Modern Math Symbols 8 Point</i> font scaled to 12 TeX points/11.96 PostScript points. Instead of specifying an explicit scale, an asterisk can be used (as in <tt>&quot;cmsy8&nbsp;@&nbsp;*&quot;</tt>) to request that <code>pkfix-helper</code> find the scale that best matches the original font&#8217;s metrics. </p>
<p> The <code>&#8211;force</code> option can be specified repeatedly on the command line.</p>
<dt><code>-p</code> <i>filename.ps</i>, <code>&#8211;ps</code>=<i>filename.ps</i></p>
<dd> Create a PostScript file called <i>filename.ps</i> that shows the <code>dvips</code> name and a font sample of every font used by the input document.</p>
<dt><code>-t</code> <i>filename.tex</i>, <code>&#8211;tex</code>=<i>filename.tex</i></p>
<dd> Create a Plain TeX file called <i>filename.tex</i> that shows the <code>dvips</code> name and a font sample of every font that <code>pkfix-helper</code> used in the output document.</p>
<dt><code>-k</code> <i>fontspec</i>, <code>&#8211;keep</code>=<i>fontspec</i></p>
<dd> Do not substitute a vector font for bitmapped font <i>fontspec</i> (<tt>&quot;Fa&quot;</tt>, <tt>&quot;Fb&quot;</tt>, etc.). This is useful when converting documents that use obscure bitmapped fonts for which there is no vector equivalent. For example, it was somewhat common in the past to include graphics such as university or corporate logos into a document by converting the bitmapped image into a single-character font and using that font in LaTeX. <code>&#8211;keep</code> prevents such fonts from being replaced. The <code>&#8211;keep</code> option can be specified repeatedly on the command line.</p>
<dt><code>-1</code>, <code>&#8211;no-repeats</code></p>
<dd> Prevent <code>pkfix-helper</code> from associating the same <i>fontspec</i> with more than one <code>dvips</code> font name.</dl>
<h3>Less-frequently Used Options</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;quiet</code></p>
<dd> Instruct <code>pkfix-helper</code> to produce no output during its run except for error and warning messages.</p>
<dt><code>-C</code> <i>filename</i>, <code>&#8211;cache</code>=<i>filename</i></p>
<dd> Speed up <font SIZE="-1">TFM</font> file processing by caching character metrics into file <i>filename</i>. On some systems it takes a long time to read a <font SIZE="-1">TFM</font> file, spawn <i>tftopl</i> to convert it to <font SIZE="-1">PL</font> format, and extract from the <font SIZE="-1">PL</font> data the metrics for each character. The first time <code>&#8211;cache</code> is specified, <code>pkfix-helper</code> proceeds as normal then writes all of the extracted character metrics to <i>filename</i>. On subsequent runs in which <code>&#8211;cache</code>=<i>filename</i> is specified, <code>pkfix-helper</code> reads the previously extracted metrics from <i>filename</i>, going through the <i>tftopl</i>-based process only for <font SIZE="-1">TFM</font> files that were not previously encountered.</p>
<dt><code>-i</code> <i>fontspec</i>, <code>&#8211;include</code>=<i>fontspec</i></p>
<dd> Add <i>fontspec</i> to the list of font specifications against which <code>pkfix-helper</code> compares <i>every</i> document font. (In contrast, <code>&#8211;force</code> designates a font specification to use only for a <i>specific</i> document font.) The <code>&#8211;include</code> option can be specified repeatedly on the command line.</p>
<dt><code>-x</code> <i>regexp</i>, <code>&#8211;exclude</code>=<i>regexp</i></p>
<dd> Remove all font specifications matching regular expression <i>regexp</i> from <code>pkfix-helper</code>&#8216;s list of known fonts. The <code>&#8211;exclude</code> option can be specified repeatedly on the command line.</p>
<dt><code>-s</code>, <code>&#8211;spp</code></p>
<dd> Specify the number of font samples per page to print to the files indicated using the <code>&#8211;ps</code> and <code>&#8211;tex</code> options. The default value, 25, should work well in most circumstances.</dl>
<h2>DIAGNOSTICS</h2>
<dl>
<dt>&quot;Best match for <i>name</i> is rather poor&quot;</p>
<dd> The best font <code>pkfix-helper</code> found for <code>dvips</code> font name <i>name</i> has a mismatch value greater than or equal to 1.0. (The mismatch value is the sum of the squares of the difference between the character widths of a document font and a potential replacement font.) Use the <code>&#8211;force</code> option to designate an alternative replacement font or scaling amount.</p>
<dt>&quot;<i>name</i> uses characters that don&#8217;t appear in any candidate font&quot;</p>
<dd> None of the fonts considered for a match include all of the characters in font <i>name</i>. The user should use the <code>&#8211;force</code> option to inform <code>pkfix-helper</code> which font to use or the <code>&#8211;keep</code> option to retain the original, bitmapped font.</p>
<dt>&quot;Processing <i>name</i> &#8230; done (<i>font</i> with mismatch=<i>number</i>, tied with <i>font</i>&#8230;)&quot;</p>
<dd> The best match for <i>name</i> is font <i>font</i>. A perfect match has a <i>number</i> of 0.00000. Worse matches observe larger values. If a tie is reported, this means one or more fonts matched <i>name</i> equally well (i.e., they see the same <i>number</i>). In this case, <code>pkfix-helper</code> selects the qualitatively most likely font as the winner.</dl>
<h2>EXAMPLES</h2>
<p> For the purpose of the following examples, assume that <i>oldfile.ps</i> is the name of a PostScript file produced by an old version of <code>dvips</code> and utilizing at least one bitmapped font. It&#8217;s always worth verifying that <code>pkfix</code> can&#8217;t convert the file on its own: </p>
<pre>
    $ pkfix oldfile.ps newfile.ps
    PKFIX 1.3, 2005/02/25 - Copyright (c) 2001, 2005 by Heiko Oberdiek.
    ==&gt; no fonts converted
</pre>
<p> (Alternatively <code>pkfix</code> may issue an error message such as <tt>&quot;!!! Error: Parse error (@start parameters)!&quot;</tt>.) Only when <code>pkfix</code> can&#8217;t replace bitmapped fonts with vector fonts is <code>pkfix-helper</code> needed. In its simplest form, <code>pkfix-helper</code> takes the name of an input file (<i>oldfile.ps</i> in this example) and the name of an output file (<i>pkfix-oldfile.ps</i>), which will have the same contents as the input file but serve as suitable input for <code>pkfix</code>: </p>
<pre><code>
$ pkfix - helper oldfile.ps pkfix - oldfile.ps Reading oldfile.ps... done.Number of Type 3 fonts encountered : 10 Bitmapped fonts are typeset at 600 DPI.Finding character widths... done.Reading TFM files... done(103 TFMs in 193 scaling variations).Matching fonts : Processing Fi... done(cmr10 @1X, mismatch = 0.11683).Processing Fa... done(cmti10 @1X, mismatch = 0.08892).Processing Fb... done(cmr8 @1X, mismatch = 0.07133).Processing Ff... done(cmbx12 @1.2X, mismatch = 0.02948).Processing Fh... done(cmtt10 @1X, mismatch = 0.06895).Processing Fd... done(cmmi10 @1X, mismatch = 0.03966).Processing Fj... done(cmbx12 @1X, mismatch = 0.03972).Processing Fe... done(cmbx10 @1X, mismatch = 0.00762).Processing Fg... done(cmsy10 @1X, mismatch = 0.00875).Processing Fc... done(cmr6 @1X, mismatch = 0.00284).$ pkfix pkfix - oldfile.ps newfile.ps PKFIX 1.3, 2005 / 02 / 25 - Copyright(c) 2001, 2005 by Heiko Oberdiek.***Font conversion : `cmti10 ' -&gt; `CMTI10'.***Font conversion : `cmr8 ' -&gt; `CMR8'.***Font conversion : `cmr6 ' -&gt; `CMR6'.***Font conversion : `cmmi10 ' -&gt; `CMMI10'.***Font conversion : `cmbx10 ' -&gt; `CMBX10'.***Font conversion : `cmbx12 ' -&gt; `CMBX12'.***Font conversion : `cmsy10 ' -&gt; `CMSY10'.***Font conversion : `cmtt10 ' -&gt; `CMTT10'.***Font conversion : `cmr10 ' -&gt; `CMR10'.***Font conversion : `cmbx12 ' -&gt; `CMBX12'.***Merging font `CMBX12' (2). == &gt; 10 converted fonts.== &gt; 1 merged font.
</code></pre>
<p> Although <code>pkfix-helper</code> tries to automate as much as possible the font-detection process, some fonts will invariably be incorrectly identified. The program outputs a warning message if it <i>knows</i> a match is bad but the lack of a warning message does not necessarily indicate that <code>pkfix-helper</code> did a good job. It is therefore strongly recommended that the user produce &#8220;before&#8221; and &#8220;after&#8221; font sheets: </p>
<pre><code>
$ pkfix - helper - q oldfile.ps pkfix - oldfile.ps-- ps = oldfonts.ps-- tex = newfonts.tex
                                                                                  $ tex newfonts.tex
                                                                                      This is TeX,
                                                     Version 3.14159(Web2C 7.4.5)(./ newfonts.tex[1])
                                                             Output written on newfonts.dvi(1 page, 1292 bytes)
                                                                 .Transcript written on newfonts.log.$ dvips newfonts.dvi
                                                         - o newfonts.ps
                                                           This is dvips(k) 5.92b Copyright 2002 Radical Eye Software(www.radicaleye.com) ' TeX output 2006.06.11:1636'-&gt;newfonts.ps&lt;texc.pro&gt;&lt;8r.enc&gt;&lt;texps.pro&gt;
                                                               .&lt;cmr6.pfb&gt;&lt;cmsy10.pfb&gt;&lt;cmbx10.pfb&gt;&lt;cmbx12.pfb&gt;
                                                           &lt;cmmi10.pfb&gt;&lt;cmtt10.pfb&gt;&lt;cmr8.pfb&gt;&lt;cmti10.pfb&gt;&lt;cmr10.pfb&gt;[1]
</code></pre>
<p> After running the preceding commands, <i>oldfonts.ps</i> shows samples of the fonts in <i>oldfile.ps</i> and <i>newfonts.ps</i> shows samples of the replacement fonts that <code>pkfix-helper</code> used to produce <i>pkfix-oldfile.ps</i>. Print <i>oldfonts.ps</i> and <i>newfonts.ps</i> and compare them carefully for incorrect fonts and sizes. </p>
<p> Suppose that the choice of <tt>&quot;cmbx12 @ 1.2X&quot;</tt> for font <tt>&quot;Ff&quot;</tt> looks wrong; say the characters look taller in <i>oldfonts.ps</i> than in <i>newfonts.ps</i>. This is where the trial-and-error stage begins. Let&#8217;s hypothesize that <tt>&quot;cmb12&quot;</tt> is a better match than <tt>&quot;cmbx12&quot;</tt> but we don&#8217;t know how much to scale the font. Fortunately, <code>pkfix-helper</code> allows <tt>&quot;*&quot;</tt> to be used as a scaling factor to tell the program to automatically detect an optimal scaling factor, even if doing so means choosing a nonstandard font size: </p>
<pre>
    $ pkfix-helper oldfile.ps pkfix-oldfile.ps --force=&quot;Ff=cmb12 @ *&quot;
    Reading oldfile.ps ... done.
    Number of Type 3 fonts encountered: 10
    Bitmapped fonts are typeset at 600 DPI.
    Finding character widths ... done.
    Reading TFM files ... failed.
    pkfix-helper: Unable to process user-specified TFM file &quot;cmb12&quot;
</pre>
<p> Oops, it looks like we don&#8217;t have a <i>cmb12.tfm</i> file on our system. Let&#8217;s try scaling up <i>cmb10.tfm</i> instead: </p>
<pre>
    $ pkfix-helper oldfile.ps pkfix-oldfile.ps --force=&quot;Ff=cmb10 @ *&quot;
    Reading oldfile.ps ... done.
    Number of Type 3 fonts encountered: 10
    Bitmapped fonts are typeset at 600 DPI.
    Finding character widths ... done.
    Reading TFM files ... done (103 TFMs in 193 scaling variations).
    Matching fonts:
        Processing Fi ... done (cmr10 @ 1X, mismatch=0.11683).
        Processing Fa ... done (cmti10 @ 1X, mismatch=0.08892).
        Processing Fb ... done (cmr8 @ 1X, mismatch=0.07133).
        Processing Ff ... done (cmb10 @ 1.5X, mismatch=0.00035).
        Processing Fh ... done (cmtt10 @ 1X, mismatch=0.06895).
        Processing Fd ... done (cmmi10 @ 1X, mismatch=0.03966).
        Processing Fj ... done (cmbx12 @ 1X, mismatch=0.03972).
        Processing Fe ... done (cmbx10 @ 1X, mismatch=0.00762).
        Processing Fg ... done (cmsy10 @ 1X, mismatch=0.00875).
        Processing Fc ... done (cmr6 @ 1X, mismatch=0.00284).
</pre>
<p> The match has definitely improved, although 15 pt. is certainly an odd size for a font. Then again, many documents <i>do</i> use nonstandard sizes so this may in fact be correct. The best way to verify is once again to produce, print, and compare a pair of font samples and iterate until all of the fonts look correct. Use one instance of <code>&#8211;force</code> for each font you want to alter.</p>
<h2>ENVIRONMENT</h2>
<p> <code>pkfix-helper</code> honors the following environment variables:</p>
<dl>
<dt><font SIZE="-1">GS</font></p>
<dd> The name of the Ghostscript interpreter (default: <i>gs</i>)</p>
<dt><font SIZE="-1">TFTOPL</font></p>
<dd> The name of a utility for converting <i>.tfm</i> files to <i>.pl</i> files (default: <i>tftopl</i>)</dl>
<h2>RESTRICTIONS</h2>
<p> <code>pkfix-helper</code> works only with PostScript files produced by <code>dvips</code>, not with arbitrary PostScript files. Only bitmapped fonts loaded by <code>dvips</code> can be analyzed, not bitmapped fonts loaded by embedded graphics. </p>
<p> <code>pkfix-helper</code> works by comparing character widths, not the actual glyphs. Consequently, it is misled by sets of fonts with similar character widths (at least for those characters used by a given document). As an extreme example, all Computer Modern Teletype fonts of a given design size (e.g., <tt>&quot;cmtt10&quot;</tt>, <tt>&quot;cmsltt10&quot;</tt>, and <tt>&quot;cmitt10&quot;</tt>) use exactly the same widths for all characters. Human assistance is generally needed to guide <code>pkfix-helper</code>&#8216;s font-matching procedures, especially for fonts for which relatively few characters appear in the document. </p>
<p> There is an astonishing variety of <code>dvips</code> output. Different versions of the program and different command-line options can result in PostScript files with a completely different structure. <code>pkfix-helper</code> works hard to find font information buried in numerous output-file variants, but it is not uncommon for a PostScript file produced by a sufficiently old version of <code>dvips</code> or with sufficiently obscure command-line options to utterly confuse <code>pkfix-helper</code>. In this case, please send your problematic PostScript files to the author of <code>pkfix-helper</code> (see &#8220;<font SIZE="-1">AUTHOR&#8221;</font> below), who may be able to enhance <code>pkfix-helper</code> to handle them.</p>
<h2>NOTES</h2>
<p> Files produced using the <code>&#8211;tex</code> option are Plain TeX files and therefore must be compiled with <code>tex</code> (or a variant such as <code>pdftex</code>, <code>luatex</code>, <code>xetex</code>, etc.), <i>not</i> with <code>latex</code>. </p>
<p> <code>dvips</code>-produced PostScript files can be structured in sections, demarcated by <tt>%DVIPSBeginSection</tt> and <tt>%DVIPSEndSection</tt>. Font names are local to a section. Hence, a font named <tt>&quot;Fa&quot;</tt> may map to <tt>&quot;cmex10&quot;</tt> in one section and to <tt>&quot;cmmi7&quot;</tt> in another. <code>pkfix-helper</code> assigns every font in a multi-section document a unique name by appending a section-number suffix: <tt>&quot;Fa_S01&quot;</tt>, <tt>&quot;Fa_S02&quot;</tt>, etc. </p>
<p> Font names are processed in decreasing order of the number of characters they have represented in the document. That is, if the document includes 10 characters from <tt>&quot;Fa&quot;</tt> and 23 characters from <tt>&quot;Fb&quot;</tt>, <code>pkfix-helper</code> will process <tt>&quot;Fb&quot;</tt> before <tt>&quot;Fa&quot;</tt>.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pkfix/">pkfix</a></code>(1), <code><a href="/docs/linux/man/1-dvips/">dvips</a></code>(1), <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1), <code><a href="/docs/linux/man/1-gs/">gs</a></code>(1) </p>
<p> PostScript Language Reference, Third Edition. Published by Addison-Wesley, <font SIZE="-1">ISBN 0-201-37922-8,</font> &lt;<a rel="nofollow" href="http://www.adobe.com/products/postscript/pdfs/PLRM.pdf">http://www.adobe.com/products/postscript/pdfs/PLRM.pdf</a>&gt;.</p>
<h2>AUTHOR</h2>
<p> Scott Pakin, <i>scott+pkfh [at] pakin.org</i></p>
<h2>COPYRIGHT AND LICENSE</h2>
<p> Copyright (C) 2009-2020, Scott Pakin </p>
<p> This file may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1.3c of this license or (at your option) any later version. The latest version of this license is in &lt;<a rel="nofollow" href="http://www.latex-project.org/lppl.txt">http://www.latex-project.org/lppl.txt</a>&gt; and version 1.3c or later is part of all distributions of LaTeX version 2006/05/20 or later. </p>
<h2>Index</h2>
