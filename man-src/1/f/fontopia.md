---
title: "fontopia(1)"
name: "fontopia"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fontopia/"
---


 </p>
<h2>NAME</h2>
<p> fontopia &#8211; the console bitmap font editor  </p>
<h2>SYNOPSIS</h2>
<p> <code>fontopia [OPTIONS] [file-name]</code>  </p>
<h2>DESCRIPTION</h2>
<p> About: <br />
 ====== <br />
 Fontopia is an easy-to-use, text-based, console font editor. What this means in simple English is that you can edit the fonts that your GNU/Linux kernel is using to display your text on text-based (vs graphical) terminals. </p>
<p> Unlike other console text editors which usually work on one PSF version, or work on unicode tables only, or allow very minimal glyph editing, fontopia provides all these functions together: <br />
 &#8211; It works on both PSF 1 &amp; 2, you can even change file type and save <br />
&nbsp;<wbr>&nbsp;<wbr>it to disk in the other version. <br />
 &#8211; It allows exporting and importing of unicode tables from external <br />
&nbsp;<wbr>&nbsp;<wbr>files. <br />
 &#8211; It provides a user-friendly, easy-to-use glyph editor. <br />
 &#8211; It can easily change font metrics, e.g. length, width, height... <br />
 Console font files are commonly of PSF type (of which there are two versions), or of CP type (legacy fonts). Fontopia works with PSF files of both versions, as well as CP fonts, BDF files and raw font files. <br />
 </p>
<p> Supported formats: <br />
 ================== <br />
 &#8211; PSF 1 and 2 <br />
 &#8211; Linux Code pages (CP) <br />
 &#8211; Raw fonts <br />
 &#8211; BDF fonts (beta) <br />
 &#8211; PCF font and Windows FON files support are under development <br />
 </p>
<p> WARNING: <br />
 ======== <br />
 (1) There is a major downside currently: fontopia doesn&#8217;t work with unicode sequences properly (at least not in all cases). If you export a unicode table, edit it, and then import it to a font file, you should be safe. <br />
 (2) Note that if you changed the font version from CP to any other version, only the ACTIVE font will be changed, as the other font formats (PSF, Raw, BDF) don&#8217;t support multiple fonts inside the same font file. In this case, you will need to open the original CP file multiple times, every time select a different font size (by using &#8216;1&#8217;-&#8216;4&#8217; number keys) and convert to the new font version, then reopen the original CP file, select another font size, convert it, and so on. <br />
 </p>
<p> Navigation: <br />
 =========== <br />
 Using the editor is very easy: <br />
 (1) Navigate the glyphs on the right side window using the arrow keys. <br />
&nbsp;<wbr>Edit a single glyph using ENTER&nbsp;<wbr>(or TAB). <br />
 (2) Navigate the bits that form a single bit (on the left side window) <br />
&nbsp;<wbr>using arrow keys. Press ENTER or SPACE to set/unset the desired bit. <br />
&nbsp;<wbr>Go back to right window&nbsp;<wbr>(glyph list)&nbsp;<wbr>using TAB. <br />
 (3) To zoom in (make the glyph on the left look bigger), press Z. <br />
 (4) To zoom out, press X. <br />
 (5) To open a new file, press CTRL+O. <br />
 (6) To create a new font from scratch, press CTRL+N. <br />
 (7) To save your work, press CTRL+S. <br />
 (8) To save with a new filename, press CTRL+D (aka Save As..). <br />
 (9) To quit the editor, press CTRL+Q. <br />
 (10) To show help, press CTRL+H. <br />
 (11) To copy a glyph, press CTRL+C. <br />
 (12) To cut a glyph, press CTRL+X. <br />
 (13) To paste a glyph, press CTRL+V. <br />
 (14) To show about dialog box, press A. <br />
 (15) To switch buffer mode (on/off), press CTRL+B. <br />
 (16) To clear a glyph (i.e. remove all bits), press C. <br />
 (17) To invert a glyph, press D. <br />
 (18) To export font unicode table (by default to a file with same original <br />
&nbsp;<wbr>file name plus .tab extension), press E. <br />
 (19) To flip a glyph horizontally, press H. <br />
 (20) To import unicode table from another file, press I. <br />
 (21) To show these keys without the extra jargon, press K. <br />
 (22) To show font metrics window, press M. <br />
 (23) To change codepage of a CP font, press P. <br />
&nbsp;<wbr>&nbsp;<wbr>If font is in BDF format, P shows properties&nbsp;<wbr>(or metadata). <br />
 (24) To remove unicode table from font, press CTRL+R. <br />
 (25) To set a glyph (i.e. set all bits), press S. <br />
 (26) To show font unicode table, press U. <br />
 (27) To flip a glyph vertically, press V. <br />
 (28) To export font glyphs in textual format (by default to a file with <br />
&nbsp;<wbr>&nbsp;<wbr>same original file name plus .glyph extension), press W. <br />
 (29) If editing a CP font and you want to change the active font (e.g. <br />
&nbsp;<wbr>&nbsp;<wbr>edit the 8x8 font instead of the 16x8 font you are currently editing) <br />
&nbsp;<wbr>&nbsp;<wbr>press any key from&nbsp;<wbr>&#8216;1&#8217;&nbsp;<wbr>to&nbsp;<wbr>&#8216;4&#8217;&nbsp;<wbr>and the respective font will be the <br />
&nbsp;<wbr>&nbsp;<wbr>active font to be edited. You can go back and forth by using the <br />
&nbsp;<wbr>&nbsp;<wbr>number keys. <br />
 </p>
<p> The unicode values that are mapped to a specific glyph are shown on the status bar (the bottom strip) to the right side. <br />
 </p>
<p> That should make you ready to move around and edit your fonts. Have fun!. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, --help</dt>
<dd> <p> Print command line help and exit </p>
 </dd>
<dt>-v, --version</dt>
<dd> <p> Display program version and exit </p>
 </dd></dl>
<h2>FILES</h2>
<p> <i>file-name</i> The name of a font file to load into fontopia. </p>
<h2>TODO</h2>
<p> &#8211; Testing and debugging &#8211; Help with handling unicode sequences </p>
<h2>SEE ALSO</h2>
<p> info fontopia </p>
<h2>AUTHOR</h2>
<p> Mohammed Isam &lt;mohammed_isam1984 [at] yahoo.com&gt; </p>
