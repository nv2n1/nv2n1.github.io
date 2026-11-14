---
title: "xpdfrc(5)"
name: "xpdfrc"
section: "5"
letter: "x"
url: "/docs/linux/man/5-xpdfrc/"
description: "xpdfrc – configuration file for Xpdf tools (version 3.04)"
---

<p>xpdfrc &#8211; configuration file for Xpdf tools (version 3.04)</p>
<h2>Description</h2>
<p>All of the Xpdf tools read a single configuration file. If you have a <i>.xpdfrc</i> file in your home directory, it will be read. Otherwise, a system-wide configuration file will be read from <i>/etc/xpdfrc</i>, if it exists. (This is its default location; depending on build options, it may be placed elsewhere.) On Win32 systems, the <i>xpdfrc</i> file should be placed in the same directory as the executables. </p>
<p> The xpdfrc file consists of a series of configuration options, one per line. Blank lines and lines starting with a &#8216;#&#8217; (comments) are ignored. </p>
<p> Arguments may be quoted, using &quot;double-quote&quot; characters, e.g., for file names that contain spaces. </p>
<p> The following sections list all of the configuration options, sorted into functional groups. There is an examples section at the end.</p>
<h2>Include Files</h2>
<dl>
<dt><code>include</code><i> config-file</i></p>
<dd>Includes the specified config file. The effect of this is equivalent to inserting the contents of <i>config-file</i> directly into the parent config file in place of the <i>include</i> command. Config files can be nested arbitrarily deeply.</dl>
<h2>Character Mapping</h2>
<dl>
<dt><code>nameToUnicode</code><i> map-file</i></p>
<dd>Specifies a file with the mapping from character names to Unicode. This is used to handle PDF fonts that have valid encodings but no ToUnicode entry. Each line of a nameToUnicode file looks like this: </p>
<p> <i> hex-string name</i> </p>
<p> The <i>hex-string</i> is the Unicode (UCS-2) character index, and <i>name</i> is the corresponding character name. Multiple nameToUnicode files can be used; if a character name is given more than once, the code in the last specified file is used. There is a built-in default nameToUnicode table with all of Adobe&#8217;s standard character names.</p>
<dt><code>cidToUnicode</code><i> registry-ordering map-file</i></p>
<dd>Specifies the file with the mapping from character collection to Unicode. Each line of a cidToUnicode file represents one character: </p>
<p> <i> hex-string</i> </p>
<p> The <i>hex-string</i> is the Unicode (UCS-2) index for that character. The first line maps CID 0, the second line CID 1, etc. File size is determined by size of the character collection. Only one file is allowed per character collection; the last specified file is used. There are no built-in cidToUnicode mappings.</p>
<dt><code>unicodeToUnicode</code><i> font-name-substring map-file</i></p>
<dd>This is used to work around PDF fonts which have incorrect Unicode information. It specifies a file which maps from the given (incorrect) Unicode indexes to the correct ones. The mapping will be used for any font whose name contains <i>font-name-substring</i>. Each line of a unicodeToUnicode file represents one Unicode character: </p>
<p> <i>in-hex</i> <i>out-hex1</i> <i>out-hex2</i> &#8230; </p>
<p> The <i>in-hex</i> field is an input (incorrect) Unicode index, and the rest of the fields are one or more output (correct) Unicode indexes. Each occurrence of <i>in-hex</i> will be converted to the specified output sequence.</p>
<dt><code>unicodeMap</code><i> encoding-name map-file</i></p>
<dd>Specifies the file with mapping from Unicode to <i>encoding-name</i>. These encodings are used for text output (see below). Each line of a unicodeMap file represents a range of one or more Unicode characters which maps linearly to a range in the output encoding: </p>
<pre><i> in-start-hex in-end-hex out-start-hex</i></pre>
<p>Entries for single characters can be abbreviated to: </p>
<pre><i> in-hex out-hex</i></pre>
<p>The <i>in-start-hex</i> and <i>in-end-hex</i> fields (or the single <i>in-hex</i> field) specify the Unicode range. The <i>out-start-hex</i> field (or the <i>out-hex</i> field) specifies the start of the output encoding range. The length of the <i>out-start-hex</i> (or <i>out-hex</i>) string determines the length of the output characters (e.g., UTF-8 uses different numbers of bytes to represent characters in different ranges). Entries must be given in increasing Unicode order. Only one file is allowed per encoding; the last specified file is used. The <i>Latin1</i>, <i>ASCII7</i>, <i>Symbol</i>, <i>ZapfDingbats</i>, <i>UTF-8</i>, and <i>UCS-2</i> encodings are predefined.</p>
<dt><code>cMapDir</code><i> registry-ordering dir</i></p>
<dd>Specifies a search directory, <i>dir</i>, for CMaps for the <i>registry-ordering</i> character collection. There can be multiple directories for a particular collection. There are no default CMap directories.</p>
<dt><code>toUnicodeDir</code><i> dir</i></p>
<dd>Specifies a search directory, <i>dir</i>, for ToUnicode CMaps. There can be multiple ToUnicode directories. There are no default ToUnicode directories.</dl>
<h2>General Font Configuration</h2>
<dl>
<dt><code>fontFile</code><i> PDF-font-name font-file</i></p>
<dd>Maps a PDF font, <i>PDF-font-name</i>, to a font for display or PostScript output. The font file, <i>font-file</i>, can be any type allowed in a PDF file. This command can be used for 8-bit or 16-bit (CID) fonts.</p>
<dt><code>fontDir</code><i> dir</i></p>
<dd>Specifies a search directory for font files. There can be multiple fontDir commands; all of the specified directories will be searched in order. The font files can be Type 1 (.pfa or .pfb) or TrueType (.ttf or .ttc); other files in the directory will be ignored. The font file name (not including the extension) must exactly match the PDF font name. This search is performed if the font name doesn&#8217;t match any of the fonts declared with the fontFile command. There are no default fontDir directories.</p>
<dt><code>fontFileCC</code><i> registry-ordering font-file</i></p>
<dd>Maps the <i>registry-ordering</i> character collection to a font for display or PostScript output. This mapping is used if the font name doesn&#8217;t match any of the fonts declared with the fontFile, fontDir, psResidentFont16, or psResidentFontCC commands.</dl>
<h2>Postscript Font Configuration</h2>
<dl>
<dt><code>psFontPassthrough</code> yes | no</p>
<dd>If set to &quot;yes&quot;, pass 8-bit font names through to the PostScript output without substitution. Fonts which are not embedded in the PDF file are expected to be available on the printer. This defaults to &quot;no&quot;.</p>
<dt><code>psResidentFont</code><i> PDF-font-name PS-font-name</i></p>
<dd>When the 8-bit font <i>PDF-font-name</i> is used (without embedding) in a PDF file, it will be translated to the PostScript font <i>PS-font-name</i>, which is assumed to be resident in the printer. Typically, <i>PDF-font-name</i> and <i>PS-font-name</i> are the same. By default, only the Base-14 fonts are assumed to be resident.</p>
<dt><code>psResidentFont16</code><i> PDF-font-name wMode PS-font-name encoding</i></p>
<dd>When the 16-bit (CID) font <i>PDF-font-name</i> with writing mode <i>wMode</i> is used (without embedding) in a PDF file, it will be translated to the PostScript font <i>PS-font-name</i>, which is assumbed to be resident in the printer. The writing mode must be either &#8216;H&#8217; for horizontal or &#8216;V&#8217; for vertical. The resident font is assumed to use the specified encoding (which must have been defined with the unicodeMap command).</p>
<dt><code>psResidentFontCC</code><i> registry-ordering wMode PS-font-name encoding</i></p>
<dd>When a 16-bit (CID) font using the <i>registry-ordering</i> character collection and <i>wMode</i> writing mode is used (without embedding) in a PDF file, the PostScript font, <i>PS-font-name</i>, is substituted for it. The substituted font is assumbed to be resident in the printer. The writing mode must be either &#8216;H&#8217; for horizontal or &#8216;V&#8217; for vertical. The resident font is assumed to use the specified encoding (which must have been defined with the unicodeMap command).</p>
<dt><code>psEmbedType1Fonts</code> yes | no</p>
<dd>If set to &quot;no&quot;, prevents embedding of Type 1 fonts in generated PostScript. This defaults to &quot;yes&quot;.</p>
<dt><code>psEmbedTrueTypeFonts</code> yes | no</p>
<dd>If set to &quot;no&quot;, prevents embedding of TrueType fonts in generated PostScript. This defaults to &quot;yes&quot;.</p>
<dt><code>psEmbedCIDTrueTypeFonts</code> yes | no</p>
<dd>If set to &quot;no&quot;, prevents embedding of CID TrueType fonts in generated PostScript. For Level 3 PostScript, this generates a CID font, for lower levels it generates a non-CID composite font. This defaults to &quot;yes&quot;.</p>
<dt><code>psEmbedCIDPostScriptFonts</code> yes | no</p>
<dd>If set to &quot;no&quot;, prevents embedding of CID PostScript fonts in generated PostScript. For Level 3 PostScript, this generates a CID font, for lower levels it generates a non-CID composite font. This defaults to &quot;yes&quot;.</dl>
<h2>Postscript Control</h2>
<dl>
<dt><code>psPaperSize</code><i> width(pts) height(pts)</i></p>
<dd>Sets the paper size for PostScript output. The <i>width</i> and <i>height</i> parameters give the paper size in PostScript points (1 point = 1/72 inch).</p>
<dt><code>psPaperSize</code> letter | legal | A4 | A3 | match</p>
<dd>Sets the paper size for PostScript output to a standard size. The default paper size is set when xpdf and pdftops are built, typically to &quot;letter&quot; or &quot;A4&quot;. This can also be set to &quot;match&quot;, which will set the paper size to match the size specified in the PDF file.</p>
<dt><code>psImageableArea</code> llx lly urx ury</p>
<dd>Sets the imageable area for PostScript output. The four integers are the coordinates of the lower-left and upper-right corners of the imageable region, specified in points (with the origin being the lower-left corner of the paper). This defaults to the full paper size; the psPaperSize option will reset the imageable area coordinates.</p>
<dt><code>psCrop</code> yes | no</p>
<dd>If set to &quot;yes&quot;, PostScript output is cropped to the CropBox specified in the PDF file; otherwise no cropping is done. This defaults to &quot;yes&quot;.</p>
<dt><code>psUseCropBoxAsPage</code> yes | no</p>
<dd>If set to &quot;yes&quot;, PostScript output treats the CropBox as the page size. By default, this is &quot;no&quot;, and the MediaBox is used as the page size.</p>
<dt><code>psExpandSmaller</code> yes | no</p>
<dd>If set to &quot;yes&quot;, PDF pages smaller than the PostScript imageable area are expanded to fill the imageable area. Otherwise, no scalling is done on smaller pages. This defaults to &quot;no&quot;.</p>
<dt><code>psShrinkLarger</code> yes | no</p>
<dd>If set to yes, PDF pages larger than the PostScript imageable area are shrunk to fit the imageable area. Otherwise, no scaling is done on larger pages. This defaults to &quot;yes&quot;.</p>
<dt><code>psCenter</code> yes | no</p>
<dd>If set to yes, PDF pages smaller than the PostScript imageable area (after any scaling) are centered in the imageable area. Otherwise, they are aligned at the lower-left corner of the imageable area. This defaults to &quot;yes&quot;.</p>
<dt><code>psDuplex</code> yes | no</p>
<dd>If set to &quot;yes&quot;, the generated PostScript will set the &quot;Duplex&quot; pagedevice entry. This tells duplex-capable printers to enable duplexing. This defaults to &quot;no&quot;.</p>
<dt><code>psLevel</code> level1 | level1sep | level2 | level2sep | level3 | level3Sep</p>
<dd>Sets the PostScript level to generate. This defaults to &quot;level2&quot;.</p>
<dt><code>psPreload</code> yes | no</p>
<dd>If set to &quot;yes&quot;, PDF forms are converted to PS procedures, and image data is preloaded. This uses more memory in the PostScript interpreter, but generates significantly smaller PS files in situations where, e.g., the same image is drawn on every page of a long document. This defaults to &quot;no&quot;.</p>
<dt><code>psOPI</code> yes | no</p>
<dd>If set to &quot;yes&quot;, generates PostScript OPI comments for all images and forms which have OPI information. This option is only available if the Xpdf tools were compiled with OPI support. This defaults to &quot;no&quot;.</p>
<dt><code>psASCIIHex</code> yes | no</p>
<dd>If set to &quot;yes&quot;, the ASCIIHexEncode filter will be used instead of ASCII85Encode for binary data. This defaults to &quot;no&quot;.</p>
<dt><code>psLZW</code> yes | no</p>
<dd>If set to &quot;yes&quot;, the LZWEncode filter will be used for lossless compression in PostScript output; if set to &quot;no&quot;, the RunLengthEncode filter will be used instead. LZW generates better compression (smaller PS files), but may not be supported by some printers. This defaults to &quot;yes&quot;.</p>
<dt><code>psUncompressPreloadedImages</code> yes | no</p>
<dd>If set to &quot;yes&quot;, all preloaded images in PS files will uncompressed. If set to &quot;no&quot;, the original compressed images will be used when possible. The &quot;yes&quot; setting is useful to work around certain buggy PostScript interpreters. This defaults to &quot;no&quot;.</p>
<dt><code>psMinLineWidth</code> float</p>
<dd>Set the minimum line width, in points, for PostScript output. The default value is 0 (no minimum).</p>
<dt><code>psRasterResolution</code> float</p>
<dd>Set the resolution (in dpi) for rasterized pages in PostScript output. (Pdftops will rasterize pages which use transparency.) This defaults to 300.</p>
<dt><code>psRasterMono</code> yes | no</p>
<dd>If set to &quot;yes&quot;, rasterized pages in PS files will be monochrome (8-bit gray) instead of color. This defaults to &quot;no&quot;.</p>
<dt><code>psRasterSliceSize</code> pixels</p>
<dd>When rasterizing pages, pdftops splits the page into horizontal &quot;slices&quot;, to limit memory usage. This option sets the maximum slice size, in pixels. This defaults to 20000000 (20 million).</p>
<dt><code>psAlwaysRasterize</code> yes | no</p>
<dd>If set to &quot;yes&quot;, all PostScript output will be rasterized. This defaults to &quot;no&quot;.</p>
<dt><code>psFile</code><i> file-or-command</i></p>
<dd>Sets the default PostScript file or print command for xpdf. Commands start with a &#8216;|&#8217; character; anything else is a file. If the file name or command contains spaces it must be quoted. This defaults to unset, which tells xpdf to generate a name of the form &lt;file&gt;.ps for a PDF file &lt;file&gt;.pdf.</p>
<dt><code>fontDir</code><i> dir</i></p>
<dd>See the description above, in the DISPLAY FONTS section.</dl>
<h2>Text Control</h2>
<dl>
<dt><code>textEncoding</code><i> encoding-name</i></p>
<dd>Sets the encoding to use for text output. (This can be overridden with the &quot;-enc&quot; switch on the command line.) The <i>encoding-name</i> must be defined with the unicodeMap command (see above). This defaults to &quot;Latin1&quot;.</p>
<dt><code>textEOL</code> unix | dos | mac</p>
<dd>Sets the end-of-line convention to use for text output. The options are: </p>
<pre> unix = LF
 dos = CR+LF
 mac = CR</pre>
<p>(This can be overridden with the &quot;-eol&quot; switch on the command line.) The default value is based on the OS where xpdf and pdftotext were built.</p>
<dt><code>textPageBreaks</code> yes | no</p>
<dd>If set to &quot;yes&quot;, text extraction will insert page breaks (form feed characters) between pages. This defaults to &quot;yes&quot;.</p>
<dt><code>textKeepTinyChars</code> yes | no</p>
<dd>If set to &quot;yes&quot;, text extraction will keep all characters. If set to &quot;no&quot;, text extraction will discard tiny (smaller than 3 point) characters after the first 50000 per page, avoiding extremely slow run times for PDF files that use special fonts to do shading or cross-hatching. This defaults to &quot;yes&quot;.</dl>
<h2>Miscellaneous Settings</h2>
<dl>
<dt><code>initialZoom</code> <i>percentage</i> | page | width</p>
<dd>Sets the initial zoom factor. A number specifies a zoom percentage, where 100 means 72 dpi. You may also specify &#8216;page&#8217;, to fit the page to the window size, or &#8216;width&#8217;, to fit the page width to the window width.</p>
<dt><code>continuousView</code> yes | no</p>
<dd>If set to &quot;yes&quot;, xpdf will start in continuous view mode, i.e., with one vertical screoll bar for the whole document. This defaults to &quot;no&quot;.</p>
<dt><code>enableFreeType</code> yes | no</p>
<dd>Enables or disables use of FreeType (a TrueType / Type 1 font rasterizer). This is only relevant if the Xpdf tools were built with FreeType support. (&quot;enableFreeType&quot; replaces the old &quot;freetypeControl&quot; option.) This option defaults to &quot;yes&quot;.</p>
<dt><code>enableFreeType</code> yes | no</p>
<dd>Enables or disables use of FreeType (a TrueType / Type 1 font rasterizer). This is only relevant if the Xpdf tools were built with FreeType support. (&quot;enableFreeType&quot; replaces the old &quot;freetypeControl&quot; option.) This option defaults to &quot;yes&quot;.</p>
<dt><code>disableFreeTypeHinting</code> yes | no</p>
<dd>If this is set to &quot;yes&quot;, FreeType hinting will be forced off. This option defaults to &quot;no&quot;.</p>
<dt><code>antialias</code> yes | no</p>
<dd>Enables or disables font anti-aliasing in the PDF rasterizer. This option affects all font rasterizers. (&quot;antialias&quot; replaces the anti-aliasing control provided by the old &quot;t1libControl&quot; and &quot;freetypeControl&quot; options.) This default to &quot;yes&quot;.</p>
<dt><code>vectorAntialias</code> yes | no</p>
<dd>Enables or disables anti-aliasing of vector graphics in the PDF rasterizer. This defaults to &quot;yes&quot;.</p>
<dt><code>antialiasPrinting</code> yes | no</p>
<dd>If this is &quot;yes&quot;, bitmaps sent to the printer will be antialiased (according to the &quot;antialias&quot; and &quot;vectorAntialias&quot; settings). If this is &quot;no&quot;, printed bitmaps will not be antialiased. This defaults to &quot;no&quot;.</p>
<dt><code>strokeAdjust</code> yes | no</p>
<dd>Enables or disables stroke adjustment. Stroke adjustment moves horizontal and vertical lines by up to half a pixel to make them look &quot;cleaner&quot; when vector anti-aliasing is enabled. This defaults to &quot;yes&quot;.</p>
<dt><code>screenType</code> dispersed | clustered | stochasticClustered</p>
<dd>Sets the halftone screen type, which will be used when generating a monochrome (1-bit) bitmap. The three options are dispersed-dot dithering, clustered-dot dithering (with a round dot and 45-degree screen angle), and stochastic clustered-dot dithering. By default, &quot;stochasticClustered&quot; is used for resolutions of 300 dpi and higher, and &quot;dispersed&quot; is used for resolutions lower then 300 dpi.</p>
<dt><code>screenSize</code><i> integer</i></p>
<dd>Sets the size of the (square) halftone screen threshold matrix. By default, this is 4 for dispersed-dot dithering, 10 for clustered-dot dithering, and 100 for stochastic clustered-dot dithering.</p>
<dt><code>screenDotRadius</code><i> integer</i></p>
<dd>Sets the halftone screen dot radius. This is only used when screenType is set to stochasticClustered, and it defaults to 2. In clustered-dot mode, the dot radius is half of the screen size. Dispersed-dot dithering doesn&#8217;t have a dot radius.</p>
<dt><code>screenGamma</code><i> float</i></p>
<dd>Sets the halftone screen gamma correction parameter. Gamma values greater than 1 make the output brighter; gamma values less than 1 make it darker. The default value is 1.</p>
<dt><code>screenBlackThreshold</code><i> float</i></p>
<dd>When halftoning, all values below this threshold are forced to solid black. This parameter is a floating point value between 0 (black) and 1 (white). The default value is 0.</p>
<dt><code>screenWhiteThreshold</code><i> float</i></p>
<dd>When halftoning, all values above this threshold are forced to solid white. This parameter is a floating point value between 0 (black) and 1 (white). The default value is 1.</p>
<dt><code>minLineWidth</code><i> float</i></p>
<dd>Set the minimum line width, in device pixels. This affects the rasterizer only, not the PostScript converter (except when it uses rasterization to handle transparency). The default value is 0 (no minimum).</p>
<dt><code>drawAnnotations</code><i> yes | no</i></p>
<dd>If set to &quot;no&quot;, annotations will not be drawn or printed. The default value is &quot;yes&quot;.</p>
<dt><code>overprintPreview</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, generate overprint preview output, honoring the OP/op/OPM settings in the PDF file. Ignored for non-CMYK output. The default value is &quot;no&quot;.</p>
<dt><code>launchCommand</code><i> command</i></p>
<dd>Sets the command executed when you click on a &quot;launch&quot;-type link. The intent is for the command to be a program/script which determines the file type and runs the appropriate viewer. The command line will consist of the file to be launched, followed by any parameters specified with the link. Do not use &quot;%s&quot; in &quot;command&quot;. By default, this is unset, and Xpdf will simply try to execute the file (after prompting the user).</p>
<dt><code>urlCommand</code><i> command</i></p>
<dd>Sets the command executed when you click on a URL link. The string &quot;%s&quot; will be replaced with the URL. (See the example below.) This has no default value.</p>
<dt><code>movieCommand</code><i> command</i></p>
<dd>Sets the command executed when you click on a movie annotation. The string &quot;%s&quot; will be replaced with the movie file name. This has no default value.</p>
<dt><code>mapNumericCharNames</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, the Xpdf tools will attempt to map various numeric character names sometimes used in font subsets. In some cases this leads to usable text, and in other cases it leads to gibberish &#8212; there is no way for Xpdf to tell. This defaults to &quot;yes&quot;.</p>
<dt><code>mapUnknownCharNames</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, and mapNumericCharNames is set to &quot;no&quot;, the Xpdf tools will apply a simple pass-through mapping (Unicode index = character code) for all unrecognized glyph names. (For CID fonts, setting mapNumericCharNames to &quot;no&quot; is unnecessary.) In some cases, this leads to usable text, and in other cases it leads to gibberish &#8212; there is no way for Xpdf to tell. This defaults to &quot;no&quot;.</p>
<dt><code>mapExtTrueTypeFontsViaUnicode</code><i> yes | no</i></p>
<dd>When rasterizing text using an external TrueType font, there are two options for handling character codes. If mapExtTrueTypeFontsViaUnicode is set to &quot;yes&quot;, Xpdf will use the font encoding/ToUnicode info to map character codes to Unicode, and then use the font&#8217;s Unicode cmap to map Unicode to GIDs. If mapExtTrueTypeFontsViaUnicode is set to &quot;no&quot;, Xpdf will assume the character codes are GIDs (i.e., use an identity mapping). This defaults to &quot;yes&quot;.</p>
<dt><code>enableXFA</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, an XFA form (if present) will be rendered in place of an AcroForm. If &quot;no&quot;, an XFA form will never be rendered. This defaults to &quot;yes&quot;.</p>
<dt><code>bind</code><i> modifiers-key context command &#8230;</i></p>
<dd>Add a key or mouse button binding. <i>Modifiers</i> can be zero or more of: </p>
<pre> shift-
 ctrl-
 alt-</pre>
<p><i>Key</i> can be a regular ASCII character, or any one of: </p>
<pre> space
 tab
 return
 enter
 backspace
 insert
 delete
 home
 end
 pgup
 pgdn
 left / right / up / down (arrow keys)
 f1 .. f35 (function keys)
 mousePress1 .. mousePress7 (mouse buttons)
 mouseRelease1 .. mouseRelease7 (mouse buttons)</pre>
<p><i>Context</i> is either &quot;any&quot; or a comma-separated combination of: </p>
<pre> fullScreen / window (full screen mode on/off)
 continuous / singlePage (continuous mode on/off)
 overLink / offLink (mouse over link or not)
 scrLockOn / scrLockOff (scroll lock on/off)</pre>
<p>The context string can include only one of each pair in the above list. </p>
<p> <i>Command</i> is an Xpdf command (see the COMMANDS section of the <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) man page for details). Multiple commands are separated by whitespace. </p>
<p> The bind command replaces any existing binding, but only if it was defined for the exact same modifiers, key, and context. All tokens (modifiers, key, context, commands) are case-sensitive. </p>
<p> Example key bindings: </p>
<pre> # bind ctrl-a in any context to the nextPage
 # command
 bind ctrl-a any nextPage
 # bind uppercase B, when in continuous mode
 # with scroll lock on, to the reload command
 # followed by the prevPage command
 bind B continuous,scrLockOn reload prevPage</pre>
<p>See the <code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1) man page for more examples.</p>
<dt><code>unbind</code><i> modifiers-key context</i></p>
<dd>Removes a key binding established with the bind command. This is most useful to remove default key bindings before establishing new ones (e.g., if the default key binding is given for &quot;any&quot; context, and you want to create new key bindings for multiple contexts).</p>
<dt><code>printCommands</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, drawing commands are printed as they&#8217;re executed (useful for debugging). This defaults to &quot;no&quot;.</p>
<dt><code>errQuiet</code><i> yes | no</i></p>
<dd>If set to &quot;yes&quot;, this suppresses all error and warning messages from all of the Xpdf tools. This defaults to &quot;no&quot;.</dl>
<h2>Examples</h2>
<p>The following is a sample xpdfrc file. </p>
<pre># from the Thai support package
nameToUnicode /usr/local/share/xpdf/Thai.nameToUnicode
# from the Japanese support package
cidToUnicode Adobe-Japan1 /usr/local/share/xpdf/Adobe-Japan1.cidToUnicode
unicodeMap JISX0208 /usr/local/share/xpdf/JISX0208.unicodeMap
cMapDir Adobe-Japan1 /usr/local/share/xpdf/cmap/Adobe-Japan1
# use the Base-14 Type 1 fonts from ghostscript
fontFile Times-Roman /usr/local/share/ghostscript/fonts/n021003l.pfb
fontFile Times-Italic /usr/local/share/ghostscript/fonts/n021023l.pfb
fontFile Times-Bold /usr/local/share/ghostscript/fonts/n021004l.pfb
fontFile Times-BoldItalic /usr/local/share/ghostscript/fonts/n021024l.pfb
fontFile Helvetica /usr/local/share/ghostscript/fonts/n019003l.pfb
fontFile Helvetica-Oblique /usr/local/share/ghostscript/fonts/n019023l.pfb
fontFile Helvetica-Bold /usr/local/share/ghostscript/fonts/n019004l.pfb
fontFile Helvetica-BoldOblique /usr/local/share/ghostscript/fonts/n019024l.pfb
fontFile Courier /usr/local/share/ghostscript/fonts/n022003l.pfb
fontFile Courier-Oblique /usr/local/share/ghostscript/fonts/n022023l.pfb
fontFile Courier-Bold /usr/local/share/ghostscript/fonts/n022004l.pfb
fontFile Courier-BoldOblique /usr/local/share/ghostscript/fonts/n022024l.pfb
fontFile Symbol /usr/local/share/ghostscript/fonts/s050000l.pfb
fontFile ZapfDingbats /usr/local/share/ghostscript/fonts/d050000l.pfb
# use the Bakoma Type 1 fonts
# (this assumes they happen to be installed in /usr/local/fonts/bakoma)
fontDir /usr/local/fonts/bakoma
# set some PostScript options
psPaperSize letter
psDuplex no
psLevel level2
psEmbedType1Fonts yes
psEmbedTrueTypeFonts yes
psFile &quot;| lpr -Pprinter5&quot;
# assume that the PostScript printer has the Univers and
# Univers-Bold fonts
psResidentFont Univers Univers
psResidentFont Univers-Bold Univers-Bold
# set the text output options
textEncoding UTF-8
textEOL unix
# misc options
enableFreeType yes
launchCommand viewer-script
urlCommand &quot;netscape -remote 'openURL(%s)'&quot;</pre>
<h2>Files</h2>
<dl>
<dt><code>/etc/xpdfrc</code></p>
<dd>This is the default location for the system-wide configuration file. Depending on build options, it may be placed elsewhere.</p>
<dt><code>$HOME/.xpdfrc</code></p>
<dd>This is the user&#8217;s configuration file. If it exists, it will be read in place of the system-wide file.</dl>
<h2>Author</h2>
<p>The Xpdf software and documentation are copyright 1996-2014 Glyph &amp; Cog, LLC.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-xpdf/">xpdf</a></code>(1), <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftopng/">pdftopng</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1)<br />
 <code><a rel="nofollow" href="http://www.foolabs.com/xpdf/">http://www.foolabs.com/xpdf/</a></code> </p>
