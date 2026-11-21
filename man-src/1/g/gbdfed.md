---
title: "gbdfed(1)"
name: "gbdfed"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gbdfed/"
description: "gbdfed – GTK-based BDF font editor"
---
<h2>NAME</h2>
<p> gbdfed - GTK-based BDF font editor </p>
<h2>SYNOPSIS</h2>
<p> <code>gbdfed</code> [<i>options</i>] [<i>fonts ...</i>] </p>
<h2>DESCRIPTION</h2>
<p> <i>gbdfed</i> lets you interactively create new bitmap font files or modify existing ones. It allows editing multiple fonts and multiple glyphs, it allows cut and paste operations between fonts and glyphs and editing font properties. <i>gbdfed</i> can import Metafont PK/GF fonts, Han Bitmap Font Format (HBF) fonts, Linux console fonts (PSF, CP, and EGA/VGA) fonts, Sun VF fonts, OpenType/TrueType (OTF/TTF) fonts, or grab a font from the X server (when running under X11). <i>gbdfed</i> can export PSF2 Linux console fonts and HEX fonts (see online help). </p>
<p> <i>gbdfed</i> works on X Window System Version 11 (X11), Release 5 or 6, with GTK+ 2.6 or greater. It may work on Windows, but hasn&#8217;t been tested yet. </p>
<h2>OPTIONS</h2>
<p> <i>gbdfed</i> accepts the following command line arguments: </p>
<dl>
<dt><i>-nc</i></dt>
<dd> <p> do not preserve comments (by default, <i>gbdfed</i> automatically collects comments that are saved with the font). </p>
 </dd></dl>
<dl>
<dt><i>-nu</i></dt>
<dd> <p> do not preserve unencoded glyphs (by default, <i>gbdfed</i> preserves the unencoded glyphs). </p>
 </dd></dl>
<dl>
<dt><i>-nm</i></dt>
<dd> <p> do not make metrics corrections (by default, <i>gbdfed</i> attempts to make metrics corrections automatically). </p>
 </dd></dl>
<dl>
<dt><i>-np</i></dt>
<dd> <p> do not pad character-cell bitmaps (by default, <i>gbdfed</i> pads character-cell bitmaps with 0&#8217;s to the cell dimensions when the font is saved). </p>
 </dd></dl>
<dl>
<dt><i>-bp</i></dt>
<dd> <p> allow blank pages (by default, <i>gbdfed</i> skips blank pages). </p>
 </dd></dl>
<dl>
<dt><i>-ed</i></dt>
<dd> <p> do not present the &quot;Really Exit?&quot; dialog (by default, this dialog always presented). </p>
 </dd></dl>
<dl>
<dt><i>-ps n</i></dt>
<dd> <p> set default point size (if unspecified, <i>gbdfed</i> sets it to 12). </p>
 </dd></dl>
<dl>
<dt><i>-hres n</i></dt>
<dd> <p> set default horizontal resolution. </p>
 </dd></dl>
<dl>
<dt><i>-vres n</i></dt>
<dd> <p> set default vertical resolution. </p>
 </dd></dl>
<dl>
<dt><i>-res n</i></dt>
<dd> <p> set both default resolutions (if unspecified, <i>gbdfed</i> sets both horizontal and vertical resolution to that of display, (e.g. 90x90 dpi for Sun workstations). </p>
 </dd></dl>
<dl>
<dt><i>-sp s</i></dt>
<dd> <p> set the default font spacing (&quot;p&quot; for Proportional, &quot;m&quot; for Monowidth, or &quot;c&quot; for Character Cell). </p>
 </dd></dl>
<dl>
<dt><i>-eol e</i></dt>
<dd> <p> set the default end-of-line type (&quot;u&quot; for Unix LF, &quot;d&quot; for DOS/Windows CRLF, or &quot;m&quot; for Macintosh CR). CR) </p>
 </dd></dl>
<dl>
<dt><i>-g glyph-code</i></dt>
<dd> <p> specify the initial glyph code at startup. The glyph code can be specified in decimal, octal, or hex. Octal numbers must be prefixed with the digit 0, and hex numbers must be prefixed with one of: <i>0x, 0X, U+, U-, \u</i>. </p>
 </dd></dl>
<dl>
<dt><i>-cb code-base</i></dt>
<dd> <p> specify the code base used to display the glyphs encodings (can be &quot;octal&quot;, &quot;decimal&quot;, or &quot;hexadecimal&quot;). </p>
 </dd></dl>
<h2>FONT GRID</h2>
<p> At the top of each editor window there are some fields and buttons. These are: </p>
<dl>
<dd> <p> The &quot;Font&quot; text field is where the font name is set so it can be edited. </p>
<p> The &quot;Glyph&quot; field is a label that provides some information about glyph name, encoding, and metrics when a glyph is selected. When a range of glyphs are selected, this field displays the start and end codes of the range. </p>
<p> The push buttons are used to navigate through the glyph pages. The &quot;Previous Page&quot; and &quot;Next Page&quot; buttons normally skip glyph pages that are empty, but that can be changed using the &quot;Preferences&quot; dialog. </p>
<p> The &quot;Page&quot; field indicates the current glyph page and also allows a specific page number to be entered. Once a page number is entered, pressing the Return key will cause the Font Grid to shift to that page. The page number entered is assumed to be a decimal number. </p>
<p> The &quot;Code&quot; field is provided for situations where the page number is not known, but the encoding is known. The encoding entered in this field must be in the base (8, 10, or 16) that is currently being used to display glyph encodings (see the &quot;View&quot; menu below). Once the encoding is entered, pressing the Return key will cause the Font Grid to shift to the page containing the encoding. </p>
 </dd></dl>
<p> The main window of each font editor is called the <i>Font Grid.</i> Each Font Grid has a clipboard used for passing glyphs around. This clipboard is called <i>FONTGRID_CLIPBOARD.</i> The format of the data stored to this clipboard is not documented yet. </p>
<p> When a glyph has been modified either by the user or by automatic metrics corrections when the font is loaded, the glyph code above the glyph cell will be highlighted. </p>
<h2>Font Grid Menus</h2>
<p> The <i>File</i> menu has the following entries: </p>
<dl>
<dt><i>New &lt;Ctrl+N&gt;</i></dt>
<dd> <p> This creates a new font using the current defaults for point size, horizontal and vertical resolution, and font spacing. </p>
 </dd></dl>
<dl>
<dt><i>Open &lt;Ctrl+O&gt;</i></dt>
<dd> <p> This opens a new font in the current Font Grid. If the font in the grid has been modified, the option to save the font before loading a new one will be given. </p>
 </dd></dl>
<dl>
<dt><i>Save &lt;Ctrl+S&gt;</i></dt>
<dd> <p> Save the current font. If the current font does not have a file name, a file selection dialog will pop up so a file name can be entered. <br />
 When the font is saved, it will automatically generate a list of _XFREE86_GLYPH_RANGE properties containing a list of glyph codes available in the font. </p>
 </dd></dl>
<dl>
<dt><i>Save As &lt;Ctrl+W&gt;</i></dt>
<dd> <p> Save the current font with some other name. <br />
 When the font is saved, it will automatically generate a list of _XFREE86_GLYPH_RANGE properties containing a list of glyph codes available in the font. </p>
 </dd></dl>
<p> The <i>Import</i> submenu of the <i>File</i> menu has the following entries: </p>
<dl>
<dd> <p> <i>PK/GF Font &lt;Ctrl+K&gt;</i> Import a Metafont PK or GF font. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Console Font &lt;Ctrl+L&gt;</i> Import a binary console font used by Linux and Sun (PSF1, PSF2, CP, vfont, and other font formats). </p>
 </dd></dl>
<dl>
<dd> <p> <i>HBF Font &lt;Ctrl+H&gt;</i> Import an HBF font. Only available if HBF support is compiled into gbdfed. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Windows Font &lt;Ctrl+B&gt;</i> Import a Windows FON/FNT font. This will also import fonts from .EXE and .DLL files as well. </p>
 </dd></dl>
<dl>
<dd> <p> <i>OpenType/TrueType Font &lt;Ctrl+Y&gt;</i> Import an OpenType/TrueType font (.otf or .ttf extension) or a TrueType collection (.ttc extension). </p>
 </dd></dl>
<dl>
<dd> <p> <i>Server Font &lt;Ctrl+G&gt;</i> Import a font from the X server if running under the X Windowing System. </p>
 </dd></dl>
<p> The <i>Export</i> submenu of the <i>File</i> menu has the following entries: </p>
<dl>
<dd> <p> <i>PSF &lt;Ctrl+F&gt;</i> This will export the current BDF font or the currently selected glyphs to a PSF2 font. Glyphs in PSF fonts are usually arranged in a specific way to make them work properly with the basic display driver. Many of these fonts come with mapping tables attached that indicate which Unicode characters a glyph can be used for. The mapping table allows the console to attempt to display Unicode text. </p>
<p> During the export, an option menu will let you select whether to: </p>
 </dd>
<dd> <p> Export Font with Mapping Table <br />
 Export Font Only <br />
 Export Mapping Table Only </p>
 </dd>
<dd> <p> Only the first 512 glyphs will be exported to the font. </p>
 </dd></dl>
<dl>
<dd> <p> <i>HEX</i> <br />
 This will export the current BDF font into the HEX format (see <a rel="nofollow" href="http://czyborra.com/unifont/">http://czyborra.com/unifont/</a>). </p>
 </dd></dl>
<dl>
<dt><i>Exit/Close &lt;Ctrl+F4&gt;</i></dt>
<dd> <p> Exit the program if this is the primary Font Grid or simply hide (unmap) the current Font Grid window. </p>
 </dd></dl>
<p> The <i>Edit</i> menu has the following entries: </p>
<dl>
<dt><i>Copy &lt;Ctrl+C&gt; or &lt;Button3Down&gt;</i></dt>
<dd> <p> This copies the current selection to the Font Grid clipboard. </p>
 </dd></dl>
<dl>
<dt><i>Cut &lt;Ctrl+X&gt; or &lt;Key&gt;Delete or &lt;Key&gt;BackSpace</i></dt>
<dd> <p> This copies the current selection to the Font Grid clipboard and then deletes the selection. </p>
 </dd></dl>
<dl>
<dt><i>Paste &lt;Ctrl+V&gt; or &lt;Button2Down&gt;</i></dt>
<dd> <p> This replaces the glyphs starting at the currently selected position with the Font Grid clipboard. </p>
 </dd></dl>
<dl>
<dt><i>Overlay &lt;Ctrl+Shift+V&gt; or Ctrl&lt;Button2Down&gt;</i></dt>
<dd> <p> This merges the glyphs on the Font Grid cliboard with the glyphs starting at the currently selected position. This means that the bitmaps are actually combined together. The names of the modified glyphs are not changed. </p>
 </dd></dl>
<dl>
<dt><i>Insert &lt;Ctrl+Meta+V&gt; or Shift&lt;Button2Down&gt;</i></dt>
<dd> <p> This inserts the glyphs on the Font Grid clipboard in front of the currently selected position. </p>
 </dd></dl>
<dl>
<dt><i>Properties &lt;Ctrl+P&gt;</i></dt>
<dd> <p> This invokes the font property editor. </p>
 </dd></dl>
<dl>
<dt><i>Comments &lt;Ctrl+M&gt;</i></dt>
<dd> <p> This invokes the font comments editor. </p>
 </dd></dl>
<dl>
<dt><i>Font Info &lt;Ctrl+I&gt;</i></dt>
<dd> <p> This invokes a dialog that allows changes to some of the font information so these values do not have to be changed using the property editor. These values include the default character, font device width (for monowidth and character cell fonts), font ascent and descent, font vertical and horizontal resolution, and the font spacing. </p>
 </dd></dl>
<p> The <i>Font Name</i> submenu of the <i>Edit</i> menu has the following four entries: </p>
<dl>
<dd> <p> <i>Make XLFD Name</i> If the font does not have an XLFD name, this will save the current font name in the <i>_ORIGINAL_FONT_NAME</i> font property and then generate an XLFD name for the font. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Update Name From Properties</i> This will update the XLFD font name fields from the font property list. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Update Properties From Name</i> This will update the font properties from the XLFD font name. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Update Average Width</i> This will update the average width field of the XLFD font name and will update the <i>AVERAGE_WIDTH</i> font property as a side effect. </p>
 </dd></dl>
<dl>
<dt><i>Name Glyphs</i></dt>
<dd>  </dd></dl>
<dl>
<dd> <p> <i>Unicode Names</i> This will rename all the glyphs using names taken from a file in the Unicode Character Database format. This file can be set in the configuration file or set using the <i>Setup</i> dialog. </p>
 </dd></dl>
<dl>
<dd> <p> <i>Unicode Values</i> This will rename all the glyphs with a hexadecimal value prefixed by 0x, U+, or \u (example: 0x010D, U+010D, \u010D). </p>
 </dd></dl>
<dl>
<dt><i>Test Glyphs &lt;Ctrl+Z&gt;</i></dt>
<dd> <p> This will toggle the glyph test dialog on or off for the editor. When this is active, selecting a glyph from any Font Grid will also add it to the glyph test dialog. When changes are made to a glyph or the font bounding box, the glyph test dialog will be updated accordingly. </p>
<p> The glyph test dialog provides a toggle to turn the baseline on or off and another toggle to draw from right to left instead of left to right. </p>
 </dd></dl>
<dl>
<dt><i>Setup &lt;Ctrl+T&gt;</i></dt>
<dd> <p> This will invoke the dialog to edit various settings used by the editor such as the default point size, resolution and font spacing. </p>
 </dd></dl>
<p> The <i>View</i> menu has the following entries: </p>
<dl>
<dt><i>Unencoded &lt;Ctrl+E&gt;</i></dt>
<dd> <p> This will toggle between displaying the unencoded (glyphs with an <i>ENCODING</i> field of -1) and encoded glyphs. </p>
 </dd></dl>
<dl>
<dt><i>Code Base</i></dt>
<dd> <p> Selects displaying of glyph encoding. Options are Octal (base 8), Decimal (base 10) or Hexadecimal (base 16). </p>
 </dd></dl>
<dl>
<dt><i>Other Page &lt;Ctrl+Shift+S&gt;</i></dt>
<dd> <p> This will toggle between the current page and the last page that was viewed. </p>
 </dd></dl>
<dl>
<dt><i>Vertical View &lt;Ctrl+Q&gt;</i></dt>
<dd> <p> This will toggle the FontGrid between showing the glyphs horizontally (default) and vertically. </p>
 </dd></dl>
<dl>
<dt><i>Messages &lt;Ctrl+A&gt;</i></dt>
<dd> <p> This will show messages generated when corrections to the font metrics are done or errors are encountered. </p>
 </dd></dl>
<p> The <i>Operations</i> menu has the following entries: </p>
<dl>
<dt><i>Translate &lt;Ctrl+D&gt;</i></dt>
<dd> <p> This will bring up the dialog for entering the X offset and Y offset used to translate the glyph to a new location. </p>
<p> The option of translating the selected glyphs or all of the glyphs is provided. </p>
 </dd></dl>
<dl>
<dt><i>Rotate &lt;Ctrl+R&gt;</i></dt>
<dd> <p> This will bring up the dialog for entering the rotation angle. The rotation is limited to between plus or minus 1 and 359 degrees. </p>
<p> The option of rotating the selected glyphs or all of the glyphs is provided. </p>
 </dd></dl>
<dl>
<dt><i>Shear &lt;Ctrl+J&gt;</i></dt>
<dd> <p> This will bring up the dialog for entering theangle of the shear. The shear is limited to plus or minus 45 degrees. </p>
<p> The option of rotating the selected glyphs or all of the glyphs is provided. </p>
 </dd></dl>
<dl>
<dt><i>Embolden &lt;Ctrl+Shift+B&gt;</i></dt>
<dd> <p> This will bring up the dialog for emboldening either the selected or all glyphs. </p>
<p> To <i>embolden</i> means to make bold. </p>
 </dd></dl>
<p> The <i>Editors</i> menu has the following entries: </p>
<dl>
<dt><i>New &lt;Ctrl+N&gt;</i></dt>
<dd> <p> This will cause a new editor to be created using the point size, resolution, and bits per pixel set in the config file, from the command line or from the Setup dialog. </p>
 </dd></dl>
<dl>
<dt><i>[editor list]</i></dt>
<dd> <p> The remaining menu items are all the Font Grid&#8217;s that have been created. Choosing one will force that window to be made visible (mapped) and also put that window on top. </p>
 </dd></dl>
<h2>Font Grid Other Features</h2>
<p> Double clicking the mouse on one of the glyphs will start a Glyph Editor for that glyph. </p>
<p> The font name can be edited in the Font Grid and page switching can be done with the buttons on the Font Grid. </p>
<h2>GLYPH EDITOR</h2>
<p> The <i>Glyph Editor</i> provides a simple bitmap editor designed to edit glyph bitmaps and other glyph information. The Glyph Editors all use a special clipboard used to pass bitmaps between the Glyph Editors. This clipboard is called <i>GLYPHEDIT_CLIPBOARD.</i> </p>
<p> The only limit on the number of Glyph Editors that can be open at one time is the amount of memory. </p>
<h2>Glyph Editor Menus</h2>
<p> The <i>File</i> menu has the following entries: </p>
<dl>
<dt><i>Update &lt;Ctrl+S&gt;</i></dt>
<dd> <p> This will update the Font Grid with the modified glyph. <br />
 To the right of the Glyph Name field is a button that performs the same function. </p>
 </dd></dl>
<dl>
<dt><i>Update and Next &lt;Ctrl+U&gt;</i></dt>
<dd> <p> This will update the FontGrid with the modified glyph and move to the next glyph. </p>
 </dd></dl>
<dl>
<dt><i>Update and Previous &lt;Ctrl+B&gt;</i></dt>
<dd> <p> This will update the FontGrid with the modified glyph and move to the previous glyph. </p>
 </dd></dl>
<dl>
<dt><i>Close &lt;Ctrl+F4&gt;</i></dt>
<dd> <p> This will close the Glyph Editor. </p>
 </dd></dl>
<p> The <i>Edit</i> menu has the following entries: </p>
<dl>
<dt><i>Reload &lt;Ctrl+L&gt;</i></dt>
<dd> <p> This will reload the glyph and discard any changes made in the GlyphEditor. </p>
 </dd></dl>
<dl>
<dt><i>Copy &lt;Ctrl+C&gt;</i></dt>
<dd> <p> This will copy the currently selected portion of the bitmap to the Glyph Editor clipboard. </p>
 </dd></dl>
<dl>
<dt><i>Cut &lt;Ctrl+X&gt;</i></dt>
<dd> <p> This will copy the currently selected portion of the bitmap to the Glyph Editor clipboard and then delete the selection. </p>
 </dd></dl>
<dl>
<dt><i>Paste &lt;Ctrl+V&gt;</i></dt>
<dd> <p> This will paste the contents of the Glyph Editor clipboard into the current Glyph Editor with the top-left coordinate of the bitmap on the clipboard pasted at the location of the mouse. If the bitmap is too big to fit if it is pasted at the mouse location, the bitmap will be shifted until it fits completely in the Glyph Editor. </p>
 </dd></dl>
<dl>
<dt><i>Select All &lt;Ctrl+A&gt;</i></dt>
<dd> <p> This will select the whole glyph bitmap. </p>
 </dd></dl>
<dl>
<dt><i>Next Glyph &lt;Ctrl+N&gt;</i></dt>
<dd> <p> This will move the Glyph Editor to the next glyph position in the Font Grid. If the current glyph has been modified, a save prompt will appear before moving to the next glyph. <br />
 To the right of the Glyph Name field is a button that performs the same function. </p>
 </dd></dl>
<dl>
<dt><i>Previous Glyph &lt;Ctrl+P&gt;</i></dt>
<dd> <p> This will move the Glyph Editor to the previous glyph position in the Font Grid. If the current glyph has been modified, a save prompt will appear before moving to the previous glyph. <br />
 To the right of the Glyph Name field is a button that performs the same function. </p>
 </dd></dl>
<p> The <i>Operation</i> menu has the following entries: </p>
<dl>
<dt><i>Draw &lt;Ctrl+D&gt;</i></dt>
<dd> <p> Change the Glyph Editor into Draw mode. </p>
 </dd></dl>
<dl>
<dt><i>Move &lt;Ctrl+M&gt;</i></dt>
<dd> <p> Change the Glyph Editor into Move mode. Move mode allows selecting a portion of the glyph bitmap and moving it to another location. </p>
 </dd></dl>
<dl>
<dt><i>Copy &lt;Ctrl+Y&gt;</i></dt>
<dd> <p> Change the Glyph Editor into Copy mode. Copy mode allows copying a portion of the glyph bitmap and moving it to another location. </p>
 </dd></dl>
<dl>
<dt><i>Rotate &lt;Ctrl+T&gt;</i></dt>
<dd> <p> This will invoke the rotation dialog that allows the degrees of rotation to be specified. Rotation can be between 1 and 359 degrees. </p>
 </dd></dl>
<dl>
<dt><i>Shear &lt;Ctrl+E&gt;</i></dt>
<dd> <p> This will invoke the shear dialog that allows the degrees of horizontal shear to be specified. Other names for shearing are obliquing or slanting. Shearing is allowed between 1 and 45 degrees. </p>
 </dd></dl>
<dl>
<dt><i>Embolden &lt;Ctrl+H&gt;</i></dt>
<dd> <p> This will embolden the glyph in a simple manner. </p>
 </dd></dl>
<dl>
<dt><i>Resize BBX &lt;Ctrl+R&gt;</i></dt>
<dd> <p> This will allow changing the sizes of the glyph bounding box including the left/right bearings and the glyph ascent/descent. If this change causes the glyph bounding box to be larger than the font bounding box, the font bounding box will be resized when the glyph is saved next. </p>
 </dd></dl>
<dl>
<dt><i>Edit PSF Unicode Mappings &lt;Ctrl+F&gt;</i></dt>
<dd> <p> This allows adding, deleting and editing of Unicode mappings for fonts that will be exported as PSF fonts. The code valued entered are expected to be in hexadecimal. </p>
 </dd></dl>
<h2>Glyph Editor Other Features</h2>
<p> When the mouse is used to shift the bitmap using one of the buttons, holding the mouse down will cause the activity to repeat. </p>
<h2>PROPERTIES</h2>
<h2>SEE ALSO</h2>
<p> xmbdfed(1), xfed(1), <a href="/docs/linux/man/1-bdftopcf/">bdftopcf</a>(1), bdftosnf(1), <a href="/docs/linux/man/1-psfaddtable/">psfaddtable</a>(1), <a href="/docs/linux/man/1-psfgettable/">psfgettable</a>(1), <a href="/docs/linux/man/1-fontforge/">fontforge</a>(1) <br />
 <i>Glyph Bitmap Distribution Format (BDF) Specification</i>, Application Note 5005, Adobe System Inc, 1993 <br />
 <i>X Logical Font Description</i>, X Consortium </p>
<h2>ACKNOWLEDGMENTS</h2>
<p> Ross Patterson for his HBF code. <br />
 der Mouse for his &quot;getbdf&quot; code. <br />
 K. Carothers and A. Korobka for their &quot;fnt2bdf&quot; code in Wine. </p>
<p> Mike Stroyan &lt;mike_stroyan [at] fc.hp.com&gt; for patches. <br />
 Primoz Peterlin &lt;primoz.peterlin [at] biofiz.mf.uni-lj.si&gt; for this manual page. <br />
 Danny Backx &lt;u27113 [at] kb.be&gt; for the LessTif Imakefile. <br />
 Donald Page &lt;donaldp [at] sco.com&gt; for patches. <br />
 Michal Szymanski &lt;msz [at] sirius.astrouw.edu.pl&gt; for problem reports. <br />
 Werner Lemberg &lt;a7971428 [at] unet.univie.ac.at&gt; for problem reports. <br />
 William F. Maton &lt;wmaton [at] enterprise.ic.gc.ca&gt; for problem reports. <br />
 Ivan Nejgebauer &lt;ian [at] uns.ns.ac.yu&gt; for problem reports. <br />
 Solofo &lt;solofo [at] mpi-sb.mpg.de&gt; for problem reports. <br />
 Dave Bodenstab &lt;imdave [at] mcs.net&gt; for patches. <br />
 W. Chao &lt;wchao [at] HRZ.Uni-Bielefeld.DE&gt; for Makefile changes and problem report. <br />
 Andreas Reuter &lt;ar205 [at] bonzo.geowiss.nat.tu-bs.de&gt; for problem reports. <br />
 Leonard Dickens &lt;leonard [at] saul.hipgraphics.com&gt; for IRIX 6.3 Makefile changes. <br />
 Markus Kuhn &lt;Markus.Kuhn [at] cl.cam.ac.uk&gt; for suggestions. <br />
 Jim Knoble &lt;jmknoble [at] pobox.com&gt; for dialog geometry fixes. <br />
 Darren Stuart Embry &lt;dsembr01 [at] ox.slug.louisville.edu&gt; for HP/UX 10.20 X11R6 Makefile additions. <br />
 Vladimir Volovich &lt;vvv [at] vvv.vsu.ru&gt; for pointing out something I forgot to test. <br />
 Ben Fry &lt;fry [at] media.mit.edu&gt; for IRIX 6.5.2 variables for the Makefile. <br />
 J.H.M. Dassen (Ray) &lt;jdassen [at] debian.org&gt; for bug fixes. <br />
 Robert Brady &lt;rwb197 [at] ecs.soton.ac.uk&gt; for pointing out a problem. <br />
 Stefan Monnier &lt;monnier [at] cs.yale.edu&gt; for a bug report. <br />
 Humphrey Clerx &lt;humphrey.clerx [at] eurocontrol.be&gt; for a bug report. <br />
 Rudolf Cejka &lt;cejkar [at] dcse.fee.vutbr.cz&gt; for bug fixes and a suggestion. <br />
 Baruch Even &lt;baruch [at] ev-en.org&gt; for a bug fix. <br />
 Sergey Vlasov &lt;vsu [at] mivlgu.murom.ru&gt; for bug fixes. <br />
 Daniel Neuburger &lt;daniel.neuburger [at] lmco.com&gt; for bug fixes. <br />
 Pierre HANSER &lt;Pierre.Hanser [at] sxb.bsf.alcatel.fr&gt; for a bug fix. <br />
 Patrick Hagglund &lt;patrik.hagglund [at] bredband.net&gt; for FreeType 2 support. <br />
 James Cloos &lt;cloos [at] jhcloos.com&gt; for pointing out problems. <br />
 Ming Hua &lt;minghua [at] rice.edu&gt; for pointing out problems. <br />
 Viktor Urban &lt;viktor [at] icc-atcsolutions.com&gt; for pointing out problems. <br />
 Jiri &quot;BlueBear&quot; Dluhos &lt;modry.medved [at] seznam.cz&gt; for providing 64-bit fixes. <br />
 Jan Engelhardt &lt;jengelh [at] linux01.gwdg.de&gt; help text improvements and missing prototype. <br />
 Daniel Richard G. &lt;skunk [at] iSKUNK.ORG&gt; for help on 64-bit architectures. <br />
 Baruch Even &lt;baruch [at] ev-en.org&gt; for help on 64-bit architectures. <br />
 Ming Hua &lt;minghua.debian [at] gmail.com&gt; for an unsuspected warning. <br />
 Ryan Hill &lt;dirtyepic [at] gentoo.org&gt; for import dialog crash report. <br />
 Don Knuth (<a rel="nofollow" href="https://bugs.launchpad.net/ubuntu/+source/gbdfed/+bug/172836)">https://bugs.launchpad.net/ubuntu/+source/gbdfed/+bug/172836)</a> for reporting spelling, gramatical and behavior problems. <br />
 Tim Allen &lt;screwtape [at] froup.com&gt; for discovering glyph and font spacing bugs. <br />
 Daniel Quarras &lt;dqarras [at] yahoo.com&gt; for discovering a PSF unicode map editing problem. <br />
 Bertrand Janin &lt;tamentis [at] neopulsar.org&gt; for improving the GlyphEditor user interface. </p>
<h2>AUTHOR</h2>
<p> Mark Leisher &lt;mleisher [at] gmail.com&gt; </p>
