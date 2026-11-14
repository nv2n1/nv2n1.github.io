---
title: "setfont(8)"
name: "setfont"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setfont/"
description: "setfont – load EGA/VGA console screen font"
---

<p>setfont &#8211; load EGA/VGA console screen font</p>
<h2>Synopsis</h2>
<p><code>setfont</code> [<code>-O</code> <i>font+umap.orig</i>] [<code>-o</code> <i>font.orig</i>] [<code>-om</code> <i>cmap.orig</i>] [<code>-ou</code> <i>umap.orig</i>] [<code>&#8211;</code><i>N</i>] [<i>font.new &#8230;</i>] [<code>-m</code> <i>cmap</i>] [<code>-u</code> <i>umap</i>] [<code>-C</code> <i>console</i>] [<code>-h</code><i>H</i>] [<code>-v</code>] [<code>-V</code>]</p>
<h2>Description</h2>
<p>The <code>setfont</code> command reads a font from the file <i>font.new</i> and loads it into the EGA/VGA character generator, and optionally outputs the previous font. It can also load various mapping tables and output the previous versions. If no args are given (or only the option &#8211;<i>N</i> for some number <i>N</i>), then a default (8x<i>N</i>) font is loaded (see below). One may give several small fonts, all containing a Unicode table, and <code>setfont</code> will combine them and load the union. Typical use:</p>
<dl>
<dt><code>setfont</code></p>
<dd>Load a default font.</p>
<dt><code>setfont drdos8x16</code></p>
<dd>Load a given font (here the 448-glyph drdos font).</p>
<dt><code>setfont cybercafe -u cybercafe</code></p>
<dd>Load a given font that does not have a Unicode map and provide one explicitly.</p>
<dt><code>setfont LatArCyrHeb-19 -m 8859-2</code></p>
<dd>Load a given font (here a 512-glyph font combining several character sets) and indicate that one&#8217;s local character set is ISO 8859-2.</dl>
<p> Note: if a font has more than 256 glyphs, only 8 out of 16 colors can be used simultaneously. It can make console perception worse (loss of intensity and even some colors). </p>
<h2>Font Formats</h2>
<p>The standard Linux font format is the PSF font. It has a header describing font properties like character size, followed by the glyph bitmaps, optionally followed by a Unicode mapping table giving the Unicode value for each glyph. Several other (obsolete) font formats are recognized. If the input file has code page format (probably with suffix .cp), containing three fonts with sizes e.g. 8&#215;8, 8&#215;14 and 8&#215;16, then one of the options -8 or -14 or -16 must be used to select one. Raw font files are binary files of size 256*<i>N</i> bytes, containing bit images for each of 256 characters, one byte per scan line, and <i>N</i> bytes per character (0 &lt; <i>N</i> &lt;= 32). Most fonts have a width of 8 bits, but with the framebuffer device (fb) other widths can be used.</p>
<h2>Font Height</h2>
<p>The program <code>setfont</code> has no built-in knowledge of VGA video modes, but just asks the kernel to load the character ROM of the video card with certain bitmaps. However, since Linux 1.3.1 the kernel knows enough about EGA/VGA video modes to select a different line distance. The default character height will be the number <i>N</i> inferred from the font or specified by option. However, the user can specify a different character height <i>H</i> using the <i>-h</i> option.</p>
<h2>Console Maps</h2>
<p>Several mappings are involved in the path from user program output to console display. If the console is in utf8 mode (see <code><a href="/docs/linux/man/1-unicode_start/">unicode_start</a></code>(1)) then the kernel expects that user program output is coded as UTF-8 (see <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7)), and converts that to Unicode (ucs2). Otherwise, a translation table is used from the 8-bit program output to 16-bit Unicode values. Such a translation table is called a <i>Unicode console map</i>. There are four of them: three built into the kernel, the fourth settable using the <i>-m</i> option of <code>setfont</code>. An escape sequence chooses between these four tables; after loading a <i>cmap</i>, <code>setfont</code> will output the escape sequence Esc ( K that makes it the active translation. </p>
<p> Suitable arguments for the <i>-m</i> option are for example <i>8859-1</i>, <i>8859-2</i>, &#8230;, <i>8859-15</i>, <i>cp437</i>, &#8230;, <i>cp1250</i>. </p>
<p> Given the Unicode value of the symbol to be displayed, the kernel finds the right glyph in the font using the Unicode mapping info of the font and displays it. </p>
<p> Old fonts do not have Unicode mapping info, and in order to handle them there are direct-to-font maps (also loaded using <i>-m</i>) that give a correspondence between user bytes and font positions. The most common correspondence is the one given in the file <i>trivial</i> (where user byte values are used directly as font positions). Other correspondences are sometimes preferable since the PC video hardware expects line drawing characters in certain font positions. </p>
<p> Giving a <i>-m none</i> argument inhibits the loading and activation of a mapping table. The previous console map can be saved to a file using the <i>-om file</i> option. These options of setfont render <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8) obsolete. (However, it may be useful to read that man page.)</p>
<h2>Unicode Font Maps</h2>
<p>The correspondence between the glyphs in the font and Unicode values is described by a Unicode mapping table. Many fonts have a Unicode mapping table included in the font file, and an explicit table can be indicated using the <i>-u</i> option. The program <code>setfont</code> will load such a Unicode mapping table, unless a <i>-u none</i> argument is given. The previous Unicode mapping table will be saved as part of the saved font file when the -O option is used. It can be saved to a separate file using the <i>-ou file</i> option. These options of setfont render <code><a href="/docs/linux/man/8-loadunimap/">loadunimap</a></code>(8) obsolete. </p>
<p> The Unicode mapping table should assign some glyph to the `missing character&#8217; value U+fffd, otherwise missing characters are not translated, giving a usually very confusing result. </p>
<p> Usually no mapping table is needed, and a Unicode mapping table is already contained in the font (sometimes this is indicated by the .psfu extension), so that most users need not worry about the precise meaning and functioning of these mapping tables. </p>
<p> One may add a Unicode mapping table to a psf font using <code><a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a></code>(1).</p>
<h2>Options</h2>
<dl>
<dt><code>-h </code><i>H</i></p>
<dd>Override font height.</p>
<dt><code>-d</code></p>
<dd>Doubles the size of the font, by replicating all of its pixels vertically and horizontally. This is suitable for high pixel density (e.g. &quot;4k&quot;) displays on which the standard fonts are too small to be easily legible. Due to kernel limitations, this is suitable only for 16&#215;16 or smaller fonts.</p>
<dt><code>-m </code><i>file</i></p>
<dd>Load console map or Unicode console map from <i>file</i>.</p>
<dt><code>-o </code><i>file</i></p>
<dd>Save previous font in <i>file</i>.</p>
<dt><code>-O </code><i>file</i></p>
<dd>Save previous font and Unicode map in <i>file</i>.</p>
<dt><code>-om </code><i>file</i></p>
<dd>Store console map in <i>file</i>.</p>
<dt><code>-ou </code><i>file</i></p>
<dd>Save previous Unicode map in <i>file</i>.</p>
<dt><code>-u </code><i>file</i></p>
<dd>Load Unicode table describing the font from <i>file</i>.</p>
<dt><code>-C </code><i>console</i></p>
<dd>Set the font for the indicated console. (May require root permissions.)</p>
<dt><code>-v</code></p>
<dd>Be verbose.</p>
<dt><code>-V</code></p>
<dd>Print version and exit. </p>
</dl>
<h2>Note</h2>
<p>PC video hardware allows one to use the &quot;intensity&quot; bit either to indicate brightness, or to address 512 (instead of 256) glyphs in the font. So, if the font has more than 256 glyphs, the console will be reduced to 8 (instead of 16) colors.</p>
<h2>Files</h2>
<dl>
<dt><i>/usr/share/consolefonts</i></p>
<dd>The default font directory.</dl>
<dl>
<dt><i>/usr/share/unimaps</i></p>
<dd>The default directory for Unicode maps.</dl>
<dl>
<dt><i>/usr/share/consoletrans</i></p>
<dd>The default directory for screen mappings.</dl>
<p> The default font is a file <i>default</i> (or <i>default8x</i>N if the -N option was given for some number N) perhaps with suitable extension (like .psf).</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a></code>(1), <code><a href="/docs/linux/man/1-unicode_start/">unicode_start</a></code>(1), <code><a href="/docs/linux/man/8-loadunimap/">loadunimap</a></code>(8), <code><a href="/docs/linux/man/7-utf-8/">utf-8</a></code>(7), <code><a href="/docs/linux/man/8-mapscrn/">mapscrn</a></code>(8) </p>
