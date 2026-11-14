---
title: "restorefont(1)"
name: "restorefont"
section: "1"
letter: "r"
url: "/docs/linux/man/1-restorefont/"
description: "restorefont – save or restore the SVGA font for textmode."
---

<h2>NAME</h2>
<p> restorefont &#8211; save or restore the SVGA font for textmode.</p>
<h2>SYNOPSIS</h2>
<p> <code>restorefont {-r|-w} </code><i>filename</i> </p>
<h2>DESCRIPTION</h2>
<p> The font used by SVGA when in textmode is written to or restored from <i>filename</i> using the <code><a href="/docs/linux/man/3-vga_gettextfont/">vga_gettextfont</a></code>(3) and <code><a href="/docs/linux/man/3-vga_puttextfont/">vga_puttextfont</a></code>(3) functions. </p>
<h2>FILE FORMAT</h2>
<p> The VGA font file <i>filename</i> has the following format: </p>
<dl>
<dt>
<dd> <code>Offset:</code><br />
 <code> 0 &#8211; 31 </code>Character 0<br />
 <code> &#8230; </code> &#8230;<br />
 <code>8164 &#8211; 8195 </code>Character 255</dl>
<p> Each row of a character bitmap is stored as a byte (8 pixels). The space that is left from the 32-byte buffer for each character is ignored, e.g. a 16 line font uses only offsets 0 &#8211; 15 of each character. </p>
<p> Linux textmode screen resolutions: </p>
<p> <code>80&#215;25</code> 16 line font 400 scanlines<br />
 <code>80&#215;28</code> 14 line font 400 scanlines<br />
 <code>80&#215;50</code> 8 line font 400 scanlines </p>
<p> The font sizes and resolutions of extended textmodes depend on the video card type and BIOS: </p>
<p> <code>132&#215;25</code> 14 line font 350 scanlines (ugly)<br />
 <code>132&#215;25</code> 16 line font 400 scanlines<br />
 <code>132&#215;43</code> 8 line font 350 scanlines (use fix132x43 to fix/improve)<br />
 <code>132&#215;50</code> 8 line font 400 scanlines </p>
<p> Using a font that has less lines per character than the textmode works, but the characters are smaller. Using a font that is bigger than the textmode font results in the bottom part of characters being cut off. </p>
<p> The svgalib distribution contains sample fonts with 8, 14 and 16 line characters in the files <i>utils/font8</i>, <i>utils/font14</i>, and <i>utils/font16</i>. </p>
<p> The <code>convfont</code> (1) program can be used to convert fonts straightforwardly stored character-after-character (i.e. each character only uses 8/14/whatever bytes), to the 32-byte per character format that <code>restorefont</code> requires. </p>
<p> The purpose of this program is usually to recover from a crashed console due to an svgalib, Xfree or other program bug. First save the state of the SVGA card when on a text console. After the crash restore this state. The <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1) and <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1) script makes this procedure very easy. </p>
<p> The national/fontpak packages, which include kernel patches, allow different textmode fonts to be used in different virtual consoles. These have been superseded by the kbd package (in the kernel since ages). See the <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8) utility of the kbd package as a starting point. </p>
<p> Recent kernels support up to 2 fonts with 512 chars each. Recent versions of svgalib take this into account and extend the size of the datafile accordingly. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-w </code><i>filename</i></p>
<dd> write the font to the file <i>filename</i>.</p>
<dt><code>-r </code><i>filename</i></p>
<dd> restore the font from the file <i>filename</i>. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-svgalib/">svgalib</a></code>(7), <code><a href="/docs/linux/man/7-vgagl/">vgagl</a></code>(7), <code><a href="/docs/linux/man/5-libvga-config/">libvga.config</a></code>(5), <code><a href="/docs/linux/man/8-setfont/">setfont</a></code>(8), <code><a href="/docs/linux/man/3-vga_gettextfont/">vga_gettextfont</a></code>(3), <code><a href="/docs/linux/man/3-vga_puttextfont/">vga_puttextfont</a></code>(3), <code><a href="/docs/linux/man/1-dumpreg/">dumpreg</a></code>(1), <code><a href="/docs/linux/man/1-convfont/">convfont</a></code>(1), <code><a href="/docs/linux/man/1-fix132x43/">fix132x43</a></code>(1), <code><a href="/docs/linux/man/1-restoretextmode/">restoretextmode</a></code>(1), <code><a href="/docs/linux/man/1-restorepalette/">restorepalette</a></code>(1), <code><a href="/docs/linux/man/1-runx/">runx</a></code>(1), <code><a href="/docs/linux/man/1-savetextmode/">savetextmode</a></code>(1), <code><a href="/docs/linux/man/1-setmclk/">setmclk</a></code>(1), <code><a href="/docs/linux/man/1-textmode/">textmode</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was edited by Michael Weller &lt;eowmob [at] exp-math.uni-essen.de&gt;. The exact source of the referenced utility as well as of the original documentation is unknown. </p>
<p> It is very likely that both are at least to some extent are due to Harm Hanemaayer &lt;H.Hanemaayer [at] inter.nl.net&gt;. </p>
<p> Occasionally this might be wrong. I hereby asked to be excused by the original author and will happily accept any additions or corrections to this first version of the svgalib manual. </p>
<h2>Index</h2>
