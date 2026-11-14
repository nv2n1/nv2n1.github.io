---
title: "xfig(1)"
name: "xfig"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfig/"
description: "xfig – Facility for Interactive Generation of figures under X11 Version 3.2.7b"
---

<h2 class="name">NAME</h2>
<p> xfig &#8211; Facility for Interactive Generation of figures under X11<br />
 Version 3.2.7b </p>
<h2>SYNOPSIS</h2>
<p> <code>xfig</code> [<i>options</i>] [<i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <i>Xfig</i> is a menu-driven tool that allows the user to draw and manipulate objects interactively under the X Window System. <code>It runs under X version 11</code> <code>release 4 or higher</code> and requires a two- or three-button mouse. <i>file</i> specifies the name of a file to be edited. The objects in the file will be read at the start of <i>xfig</i>. </p>
<p> The bulk of the documentation for <i>xfig</i> is in an HTML-based reference guide. See the Help menu in <i>xfig</i> or point your browser at <i>/usr/share/doc/xfig/html/index.html</i>. There are both English and Japanese versions. </p>
<p> When using a two-button mouse use the <i>&lt;Meta&gt;</i> key and the right button at the same time to effect the action of the middle button. </p>
<p> <i>Xfig</i> is available from <a rel="nofollow" href="https://sourceforge.net/projects/mcj/.">https://sourceforge.net/projects/mcj/.</a> </p>
<p> The <i>Fig2dev</i> package is used when printing or exporting the output from <i>xfig</i>. The <i>fig2dev</i> program is automatically called by <i>xfig</i> as a back-end processor to produce various types of output: </p>
<p> LaTeX, Metafont, PDF, PostScript or Encapsulated PostScript, CGM and EMF (mostyl used under Windows), tk (tcl/tk tool command language/tool kit package), SVG, GIF, JPEG, PCX, PNG, PPM, TIFF, XBM, XPM, Gerber, AutoCAD Slide, IBM-GL (HP/GL), Pic and PiCTeX. For use with TeX/LaTeX: box, epic, eepic, eepicemu, pict2e, pstricks, tikz. </p>
<p> See man fig2dev for all options. </p>
<p> The <i>Fig2dev</i> package is available from <a rel="nofollow" href="https://sourceforge.net/projects/mcj/.">https://sourceforge.net/projects/mcj/.</a></p>
<h2>OPTIONS</h2>
<p> <code>-help</code></p>
<dl>
<dt>
<dd> Print all command-line options for xfig and quit.</dl>
<p> <code>-a</code>[<code>llownegcoords</code>]</p>
<dl>
<dt>
<dd> Allow panning into the negative region of the canvas. This is the default</dl>
<p> <code>-au</code>[<code>torefresh</code>] Make xfig look at the timestamp on the .fig file and automatically load it and display it every time it changes. </p>
<p> <code>-bal</code>[<code>loon_delay</code>] <i>msec</i></p>
<dl>
<dt>
<dd> Cause popup information balloons to be delayed by <i>msec</i> milliseconds. The default is 500 milliseconds.</dl>
<p> <code>-bol</code>[<code>d</code>] <i>font</i></p>
<dl>
<dt>
<dd> Cause the font used for displaying the file name and confirmation messages to be <i>font</i> (default = 8x13bold).</dl>
<p> <code>-butt</code>[<code>on</code>] <i>font</i></p>
<dl>
<dt>
<dd> Cause the font used for most buttons to be <i>font</i> (default = 6&#215;13).</dl>
<p> <code>-but_</code>[<code>per_row</code>] <i>number</i></p>
<dl>
<dt>
<dd> Specify the number of buttons wide the mode panel should be. This is useful in conjunction with the <code>-pheight</code> parameter to reduce the canvas height for small screens.</dl>
<p> <code>-cbg</code> color</p>
<dl>
<dt>
<dd> Use <i>color</i> as the background color for the canvas. If you want to set the background of everything in xfig (e.g. menus, etc.) use the general <code>-bg</code> option.</dl>
<p> <code>-center</code></p>
<dl>
<dt>
<dd> Set the print option to print the figure centered on the page. This is the default.</dl>
<p> <code>-centim</code>[<code>ers</code>]</p>
<dl>
<dt>
<dd> Make centimeters the unit of choice. See also <code>-metric.</code></dl>
<p> <code>-cfg</code> color</p>
<dl>
<dt>
<dd> Use <i>color</i> as the default color for objects. If you want to set the foreground of everything in xfig (e.g. menus, etc.) use the general <code>-fg</code> option.</dl>
<p> <code>-correct_font_size</code></p>
<dl>
<dt>
<dd> Normally, <i>fig2dev</i> uses 1/80 inch for font size increments (for historical reasons), instead of the more proper &#8220;points&#8221; (1/72 inch) that <i>xfig</i> uses. This option makes xfig call fig2dev with the <code>-F</code> option to make it use points (1/72 inch).</dl>
<p> <code>-deb</code>[<code>ug</code>]</p>
<dl>
<dt>
<dd> Turn on debugging mode. Prints various debugging messages like font names etc.</dl>
<p> <code>-dep</code>[<code>th</code>]</p>
<dl>
<dt>
<dd> Choose depth of visual desired. Your server must support the desired visual and depth chosen. Use <i>xdpyinfo</i> to see what visuals and depths are supported. See also the <code>-visual</code> option.</dl>
<p> <code>-donta</code>[<code>llownegcoords</code>]</p>
<dl>
<dt>
<dd> Don&#8217;t allow panning into the negative region of the canvas. The default is to allow panning in the negative region.</dl>
<p> <code>-dontshowb</code>[<code>alloons</code>]</p>
<dl>
<dt>
<dd> Prevents xfig from popping up the information balloons. See also <code>-showballoons.</code></dl>
<p> <code>-dontshowl</code>[<code>engths</code>]</p>
<dl>
<dt>
<dd> Don&#8217;t show lengths of lines as they are being drawn. This is the default.</dl>
<p> <code>-dontshowz</code>[<code>erolines</code>]</p>
<dl>
<dt>
<dd> Don&#8217;t show axis zero lines on the canvas. The default is to show them.</dl>
<p> <code>-dontsw</code>[<code>itchcmap</code>]</p>
<dl>
<dt>
<dd> Prevents xfig from switching to a private colormap if there aren&#8217;t enough colors available in the default colormap. See also <code>-max_image_colors.</code></dl>
<p> <code>-enc</code>[<code>oding</code>] <i>encoding</i></p>
<dl>
<dt>
<dd> Encode character set using <i>encoding</i> when exporting LaTeX text. The default is 1. This is used for the ISO-8859 encoding of character sets. Allowed values are 0 (no encoding), 1 (ISO-8859-1) or 2 (ISO-8859-2).</dl>
<p> <code>-exportL</code>[<code>anguage</code>] <i>language</i></p>
<dl>
<dt>
<dd> Specifies the default language to be used for when exporting a fig file. Choices are: </p>
<pre>
Name              Language
<hr>Vector formats:
ps                PostScript
eps               Encapsulated PostScript
pdf               PDF (Portable Document Format)
box               LaTeX box (figure boundary)
latex             LaTeX picture
pict2e            LaTeX picture + pict2e macros
tikz              LaTeX picture + tikz macros
epic              LaTeX picture + epic macros
eepic             LaTeX picture + eepic macros
eepicemu          LaTeX picture + eepicemu macros
pstex             Combined PS/LaTeX (both PS and LaTeX parts)
pdftex            Combined PDF/LaTeX (both PDF and LaTeX parts)
pspdftex          Combined PS/PDF/LaTeX (three parts)
pictex            PiCTeX macros
cgm               Computer Graphcis Meta file
emf               Enhanced Meta file
dxf               Drawing Interchange format
gbx               Gerber (RS-247-X)
ibmgl             HPGL/2 or IBMGL
textyl            Textyl special commands
tpic              TPIC
pic               PIC
mf                MF (MetaFont)
mp                MP (MetaPost)
tk                Tk (Tcl/Tk toolkit)
ptk               Perl/Tk
shape             LaTeX shape paragraph definition
svg               SVG (Scalable Vector Graphics)
Bitmap formats:
gif               GIF
jpeg              JPEG (JFIF)
pcx               PCX
png               PNG
ppm               PPM (portable pixmap package)
sld               (AutoCad slide)
tiff              TIFF
xbm               X11 Bitmap
xpm               X11 Pixmap
<hr></pre>
</dl>
<p> <code>-export_m</code>[<code>argin</code>] <i>width</i></p>
<dl>
<dt>
<dd> Set the size of the border margin around the figure for exporting to bitmap, PostScript, Encapsulated PostScript, or HTML MAP formats. This is in units of points (1/72th inch). The default is 0.</dl>
<p> <code>-fli</code>[<code>pvisualhints</code>]</p>
<dl>
<dt>
<dd> Flip left/right mouse indicator messages for mice whose buttons have been switched. The default is to NOT flip the messages.</dl>
<p> <code>-flu</code>[<code>shleft</code>]</p>
<dl>
<dt>
<dd> Set the print option to print the figure flush left. The default is to center the figure on the page.</dl>
<p> <code>-free</code>[<code>hand_resolution</code>] <i>resolution</i></p>
<dl>
<dt>
<dd> Set the resolution of the freehand drawing mode to <i>resolution</i> pixels. This is the number of pixels the mouse must move before xfig adds another point to the object being drawn.</dl>
<p> <code>-geom</code>[<code>etry</code>] [<i>WxH</i>]<i>[+X+Y]</i></p>
<dl>
<dt>
<dd> You may use the -geometry option or resource to <i>size and/or position the xfig window,</i> or you may use <code>-pwidth</code> and/or <code>-pheight</code> to specify the canvas size in inches or centimeters. If you use the <code>-geom</code> option to make the xfig window smaller than the default, you may have to use the <code>-but_per_row</code> option to tell xfig to put 3 or 4 buttons per row on the left mode panel.</dl>
<p> <code>-gh</code>[<code>ostscript</code>] <i>postscript-interpreter</i></p>
<dl>
<dt>
<dd> Select the PostScript &#8482; interpreter of your choice. The default is ghostscript (gs). This is needed when importing Encapsulated PostScript files.</dl>
<p> <code>-grid_c</code>[<code>olor</code>] <i>color</i></p>
<dl>
<dt>
<dd> Draw the grid on the canvas in this color (default: red).</dl>
<p> <code>-grid_u</code>[<code>nit</code>] <i>unit</i></p>
<dl>
<dt>
<dd> Only used when in inches mode to choose between showing fractions or decimal inches in the rulers and grid. Any of the following may be used to force decimal inches: &quot;ten&quot;, &quot;tenth&quot;, &quot;10, &quot;1/10&quot;. If any other value is used for this option, the rulers will show 1/16 inch divisions.</dl>
<p> <code>-hidd</code>[<code>entext</code>]</p>
<dl>
<dt>
<dd> Start <i>xfig</i> with the <i>hidden text</i> mode for text objects. The <i>Hidden</i> attribute is used for figures that will be used with <i>LaTeX</i> and is applicable only to the display of the document in <i>xfig</i>. It means that the text itself is not shown onscreen, but only the string &#8220;&lt;text&gt;&#8221;. This is to keep long sequences of <i>LaTeX</i> formatting commands from making the screen messy and hard to read. The default for the <i>Hidden</i> flag is <i>off</i>.</dl>
<p> <code>-dontshowd</code>[<code>epthmanager</code>]</p>
<dl>
<dt>
<dd> Hide the depth manager panel. The default is to show the panel.</dl>
<p> <code>-icon_</code>[<code>view</code>]</p>
<dl>
<dt>
<dd> Show the library objects as icons. This is the default. The other mode is <code>-list_view.</code></dl>
<p> <code>-iconG</code>[<code>eometry</code>] +<i>X</i>+<i>Y</i></p>
<dl>
<dt>
<dd> Specifies the position for the icon.</dl>
<p> <code>-im</code>[<code>age_editor</code>] <i>editor</i></p>
<dl>
<dt>
<dd> Specify bitmap editor to use when &#8220;Edit Image&#8221; button is pressed in Picture Object panel.</dl>
<p> <code>-inc</code>[<code>hes</code>] <code>(or</code>-imperial)</p>
<dl>
<dt>
<dd> Make inches the unit of choice. This is the default.</dl>
<p> <code>-ins</code>[<code>tallowncmap</code>]</p>
<dl>
<dt>
<dd> Install own colormap. Normally, xfig uses the current colormap.</dl>
<p> <code>-internalBW</code> width</p>
<dl>
<dt>
<dd> Use lines of width <i>width</i> between all buttons and panels (default = 1).</dl>
<p> <code>-international</code></p>
<dl>
<dt>
<dd> Switch on international support (mainly Japanese and Korean), users of ISO Latin 1 (ISO-8859-1) probably should not use this, therefore the international support is switched off by default for locales using ISO-8859-1* codesets. For all other locales this option is already used by default.</dl>
<p> <code>-jpeg</code>[<code>_quality</code>] <i>quality</i></p>
<dl>
<dt>
<dd> Set the quality factor for exporting to the jpeg format. The default is 75.</dl>
<p> <code>-k</code>[<code>eyFile</code>] <i>compose-key-file</i></p>
<dl>
<dt>
<dd> Use <i>compose-key-file</i> instead of <i>CompKeyDB</i> for compose (meta) key database. If there are no &#8220;<code>/</code>&#8221;s in the name, the file must reside in the <i>xfig</i> library directory, <i>$XFIGLIBDIR</i>, usually <code>/usr/local/lib/X11/xfig</code>. If there are any &#8220;<code>/</code>&#8221;s in the name it is taken as is (not relative to <i>$XFIGLIBDIR</i>). If there is a leading &#8220;<code>~/</code>&#8221; in the string then the &#8220;<code>~</code>&#8221; is expanded to the user&#8217;s home directory.</dl>
<p> <code>-lan</code>[<code>dscape</code>]</p>
<dl>
<dt>
<dd> Make <i>xfig</i> come up in landscape mode (10.5&quot; x 8&quot;). This is the default; however as the orientation is stored with Fig files, when you load a Fig file the orientation will change as required. This is only true for files of version 3.0 or higher.<br />
 See also -portrait.</dl>
<p> <code>-lat</code>[<code>exfonts</code>]</p>
<dl>
<dt>
<dd> Start <i>xfig</i> with <i>LaTeX</i> font selection. Normally, the <i>PostScript</i> fonts are available as the default. This flag selects the <i>LaTeX</i> fonts to start.</dl>
<p> <code>-le</code>[<code>ft</code>]</p>
<dl>
<dt>
<dd> Change the position of the side panel window to the left of the canvas window. This is the default.</dl>
<p> <code>-library_d</code>[<code>ir</code>] <i>directory</i></p>
<dl>
<dt>
<dd> Specify directory where Fig object libraries are located. There may be sub-directories there and sub-sub-directories, etc.</dl>
<p> <code>-library_i</code>[<code>con_size</code>] <i>size</i></p>
<dl>
<dt>
<dd> Specify the size of the icons shown for library objects. The default is 60 pixels, with the minimum being 40 and the maximum being 120.</dl>
<p> <code>-lis</code>[<code>t_view</code>]</p>
<dl>
<dt>
<dd> Show the library objects as a list of names. The default mode is <code>-icon_view.</code></dl>
<p> <code>-mag</code>[<code>nification</code>] <i>mag</i></p>
<dl>
<dt>
<dd> Set export and print magnification in %.</dl>
<p> <code>-max</code>[<code>_image_colors</code>] <i>numcols</i></p>
<dl>
<dt>
<dd> Limit the number of colors used for imported images to <i>numcols (default 64).</i></dl>
<p> <code>-me</code>[<code>tric</code>]</p>
<dl>
<dt>
<dd> Make centimeters the unit of choice. The option <code>-centimeters</code> may also be used.</p>
<dt>
<dd> After <i>xfig</i> is started you may change the units from metric to imperial or vice versa from a popup menu available by pressing mouse button 3 in the <i>units</i> box where the two rulers meet.</dl>
<p> <code>-mo</code>[<code>nochrome</code>]</p>
<dl>
<dt>
<dd> Use black and white only.</dl>
<p> <code>-mu</code>[<code>ltiple</code>]</p>
<dl>
<dt>
<dd> Sets multiple page mode for print or export. See also <code>-single.</code></dl>
<p> <code>-noo</code>[<code>verlap</code>]</p>
<dl>
<dt>
<dd> When exporting in multiple page mode, causes no overlap from page to page. This is the default. See also <code>-overlap.</code></dl>
<p> <code>-nor</code>[<code>mal</code>] <i>font</i></p>
<dl>
<dt>
<dd> Cause the font used for the message window to be <i>font</i>. This font is also used on the canvas when the selected font is not available in an X11 font (default = 6&#215;13).</dl>
<p> <code>-nosc</code>[<code>alablefonts</code>]</p>
<dl>
<dt>
<dd> Disables use of the X11R5 or OpenWindows scalable fonts. You might want to use this for debugging.</dl>
<p> <code>-nosp</code>[<code>lash</code>]</p>
<dl>
<dt>
<dd> Don&#8217;t show the startup splash screen. The default is to show it ( <code>-splash</code> ).</dl>
<p> <code>-not</code>[<code>rack</code>]</p>
<dl>
<dt>
<dd> Turn off cursor (mouse) tracking arrows.</dl>
<p> <code>-nowrite_bak</code></p>
<dl>
<dt>
<dd> When saving a drawing into an existing .fig file xfig will first rename that file by appending &quot;.bak&quot; to the name. This option disables this feature.</dl>
<p> <code>-ov</code>[<code>erlap</code>]</p>
<dl>
<dt>
<dd> When exporting in multiple page mode, causes overlap from page to page of about 10%. See also <code>-nooverlap.</code></dl>
<p> <code>-pag</code>[<code>eborder</code>] <i>color</i></p>
<dl>
<dt>
<dd> Draw the page border on the canvas in this color (default light blue). The page border is turned on by the <code>-showpageborder</code> option (resource Fig.showpageborder), and shows the edges of the current <i>export</i> paper size.</dl>
<p> <code>-pap</code>[<code>er_size</code>] <i>size</i></p>
<dl>
<dt>
<dd> Set the initial paper size for Export and Print. Choices are </p>
<pre>
Option     Paper      Size
<hr>letter     Letter     8.5in x 11in
legal      Legal      8.5in x 14in
tabloid    Tabloid    17in x 11in
a          ANSI A     8.5in x 11in
b          ANSI B     11in x 17in
c          ANSI C     17in x 22in
d          ANSI D     22in x 34in
e          ANSI E     34in x 44in
a9         ISO A9     37mm x 52mm
a8         ISO A8     52mm x 74mm
a7         ISO A7     74mm x 105mm
a6         ISO A6     105mm x 148mm
a5         ISO A5     148mm x 210mm
a4         ISO A4     210mm x 297mm
a3         ISO A3     297mm x 420mm
a2         ISO A2     420mm x 594mm
a1         ISO A1     594mm x 840mm
a0         ISO A0     840mm x 1189mm
b10        JIS B10    32mm x 45mm
b9         JIS B9     45mm x 64mm
b8         JIS B8     64mm x 91mm
b7         JIS B7     91mm x 128mm
b6         JIS B6     128mm x 182mm
b5         JIS B5     182mm x 257mm
b4         JIS B4     257mm x 364mm
b3         JIS B3     364mm x 515mm
b2         JIS B2     515mm x 728mm
b1         JIS B1     728mm x 1030mm
b0         JIS B0     1030mm x 1456mm
<hr></pre>
<p> Note that this doesn&#8217;t affect the size of the drawing canvas. Use the <code>-pheight</code> and <code>-pwidth</code> options for that.</dl>
<p> <code>-ph</code>[<code>eight</code>] <i>height</i></p>
<dl>
<dt>
<dd> Make the <i>xfig</i> canvas <i>height</i> high (where <i>height</i> is either cm or in, depending on the <code>-metric</code> setting).</dl>
<p> <code>-po</code>[<code>rtrait</code>]</p>
<dl>
<dt>
<dd> Make <i>xfig</i> come up in portrait mode (8.5&quot; x 9&quot;). See note about landscape mode.</dl>
<p> <code>-pw</code>[<code>idth</code>] <i>width</i></p>
<dl>
<dt>
<dd> Make the <i>xfig</i> canvas <i>width</i> wide (where <i>width</i> is either cm or in, depending on the <code>-metric</code> setting).</dl>
<p> <code>-righ</code>[<code>t</code>]</p>
<dl>
<dt>
<dd> Change the position of the side panel window to the right of the canvas window (default: left).</dl>
<p> <code>-rigi</code>[<code>d</code>]</p>
<dl>
<dt>
<dd> Start <i>xfig</i> with the <i>rigid text</i> mode for text objects. The <i>Rigid</i> attribute forces text to remain the same size even if inside a compound object that is scaled up or down. The default is <i>off</i>.</dl>
<p> <code>-ru</code>[<code>lerthick</code>]</p>
<dl>
<dt>
<dd> Set the height(width) of the top(side) rulers in pixels. The default (and minimum) is 24.</dl>
<p> <code>-scala</code>[<code>blefonts</code>]</p>
<dl>
<dt>
<dd> Allows use of the X11R5 or OpenWindows scalable fonts (this is the default). If the scalable fonts aren&#8217;t available <i>xfig</i> will automatically switch to non-scaling fonts.</dl>
<p> <code>-scale_factor</code> <i>scale</i></p>
<dl>
<dt>
<dd> Scale every figure read in by this value. This is useful in conjunction with the <code>-update</code> option to do batch scaling of figures.</dl>
<p> <code>-showa</code>[<code>llbuttons</code>]</p>
<dl>
<dt>
<dd> Show all the <i>xfig</i> indicator buttons instead of only those relevant to the current drawing mode. Normally, the buttons <i>line width</i>, <i>area-fill</i>, <i>grid mode</i>, <i>text size</i>, etc. are only visible when they are relevant to the current drawing mode. The <code>-showallbuttons</code> option makes all of the indicator buttons visible at all times. This takes up more screen real estate, but allows the user to see all settable parameters.</dl>
<p> <code>-showb</code>[<code>alloons</code>]</p>
<dl>
<dt>
<dd> Forces <i>xfig</i> to pop up the information balloons when the mouse passws over a button. This is the default. See also <code>-dontshowballoons .</code></dl>
<p> <code>-showd</code>[<code>epthmanager</code>]</p>
<dl>
<dt>
<dd> Show the depth manager panel. This panel lets one show or hide objects at various depths. This is the default.</dl>
<p> <code>-showl</code>[<code>engths</code>]</p>
<dl>
<dt>
<dd> Makes <i>xfig</i> show the lengths of lines being drawn, in red text near the line itself. Also, when points are moved or added. In addition, imagine a triangle formed with the line segment as the hypotenuse, and a vertical and horizontal line forming the other two sides. These lines and their lengths are also drawn in red as the point is moved or added. This mode is ignored when drawing in freehand mode.<br />
 This flag may be toggled by pressing &lt;Meta&gt;i (default).</dl>
<p> <code>-shown</code>[<code>ums</code>]</p>
<dl>
<dt>
<dd> With this option, xfig will draw all objects with a red number next to each vertex. This is generally only useful for debugging.</dl>
<p> <code>-showp</code>[<code>ageborder</code>]</p>
<dl>
<dt>
<dd> Makes <i>xfig</i> show the border of the current paper size in the color specified by the <code>-pageborder</code> option (default: light blue).</dl>
<p> <code>-showz</code>[<code>erolines</code>]</p>
<dl>
<dt>
<dd> Show axis zero lines on the canvas. This is the default</dl>
<p> <code>-si</code>[<code>ngle</code>]</p>
<dl>
<dt>
<dd> Sets single page mode for print or export. This is the default. See also <code>-multiple.</code></dl>
<p> <code>-sm</code>[<code>ooth_factor</code>] <i>factor</i></p>
<dl>
<dt>
<dd> Enable smoothing when exporting to the bitmap formats (e.g. GIF, PNG, etc.). The allowed values are 0 (no smoothing), 2 or 4 (most smoothing). This parameter is passed to ghostscript in the -dTextAlphaBits -dGraphicsAlphaBits options to smooth the figure.</dl>
<p> <code>-spec</code>[<code>ialtext</code>]</p>
<dl>
<dt>
<dd> Start <i>xfig</i> with the <i>TeX text</i> mode for text objects. This means that characters that have a special meaning to TeX/LaTeX, e.g., &#8216;$&#8217; or &#8216;\&#8217;, are not quoted but left untouched in the text string. This is most useful for writing LaTeX equations. If this flag is not set, then the backslash character &#8216;\&#8217; is changed to the ackslash command, a brace &#8216;{&#8216; is turned into a brace command \{, etc.</dl>
<p> <code>-spel</code>[<code>lcheckcommand</code>] <i>command</i></p>
<dl>
<dt>
<dd> Use <i>command</i> for the external spell checking program when using the spell check/search/replace popup. The string <i>command</i> should include the string &#8220;%s&#8221; which is replaced by a temporary filename. Default is &#8220;spell %s&#8221;.</dl>
<p> <code>-spinner_d</code>[<code>elay</code>] <i>msec</i></p>
<dl>
<dt>
<dd> The delay (in milliseconds) before the spinner will automatically count up or down when the button is pressed. Spinners are the (numeric) text widgets with an up- and down-arrow, which when clicked, cause the value to be incremented/decremented. The default is 500 milliseconds.</dl>
<p> <code>-spinner_r</code>[<code>rate</code>] <i>msec</i></p>
<dl>
<dt>
<dd> The rate (in milliseconds) at which the spinner will count when the up- or down-arrow is pressed.</dl>
<p> <code>-startfi</code>[<code>llstyle</code>] <i>stylenumber</i></p>
<dl>
<dt>
<dd> Set the starting fill style for area fill (-1 to 21).</dl>
<p> <code>-startfo</code>[<code>ntsize</code>] <i>pointsize</i></p>
<dl>
<dt>
<dd> Set the default font size for text objects (default = 12pt).</dl>
<p> <code>-startg</code>[<code>ridmode</code>] <i>modenumber</i></p>
<dl>
<dt>
<dd> Set the starting grid mode (0 to 3). Mode 0 is no grid. In imperial (inches) mode, grid mode 1 is 1/4 inch, mode 2 is 1/2 inch and mode 3 is 1 inch. In metric mode, grid mode 1 is 2mm, mode 2 is 5mm and mode 3 is 1cm.</dl>
<p> <code>-startla</code>[<code>texFont</code>] <i>font</i></p>
<dl>
<dt>
<dd> Set the starting font name for <i>LaTeX</i> fonts.</dl>
<p> <code>-startli</code>[<code>newidth</code>] <i>width</i></p>
<dl>
<dt>
<dd> Set the starting line width.</dl>
<p> <code>-startpo</code>[<code>snmode</code>] <i>modenumber</i></p>
<dl>
<dt>
<dd> Set the starting point positioning mode (0 to 4) In imperial (inches) mode, positioning mode 0 is &#8220;any&#8221;, mode 1 is 1/16 inch, mode 2 is 1/4 inch, mode 3 is 1/2 inch and mode 4 is 1 inch. In metric mode, mode 0 is &#8220;any&#8221;, mode 1 is 1mm, mode 2 is 5mm, mode 3 is 10mm and mode 4 is 20mm.</dl>
<p> <code>-startp</code>[<code>sFont</code>] <i>font</i></p>
<dl>
<dt>
<dd> Set the starting font name for <i>PostScript</i> fonts.</dl>
<p> <code>-startt</code>[<code>extstep</code>] <i>stepsize</i></p>
<dl>
<dt>
<dd> Set the starting text step.</dl>
<p> <code>-ta</code>[<code>blet</code>]</p>
<dl>
<dt>
<dd> Specifies that xfig should use the input tablet instead of the mouse for drawing. You must have the XInputExtension in your X server and an input tablet for this to work. Also, you must modify the Imakefile to include the <code>USETAB</code> and <code>TABLIB</code> variables.</dl>
<p> <code>-track</code></p>
<dl>
<dt>
<dd> Turn on cursor (mouse) tracking arrows (default).</dl>
<p> <code>-tran</code>[<code>sparent_color</code>] <i>color_number</i></p>
<dl>
<dt>
<dd> Make the transparent color for GIF export <i>color_number.</i> This number is the color number according to the <code>xfig</code> color panel, starting at 0 (black) and ending at 31 (gold), or may be a user-defined color number, which is 32 or higher.</dl>
<p> <code>-update</code> <i>file [ file &#8230; ]</i></p>
<dl>
<dt>
<dd> Run xfig in an &quot;update&quot; mode, where it will read each Fig file specified on the command line and write it out to the original file, in the current file format for the version of xfig being run. The original Fig file will be preserved with the suffix <i>.bak</i> attached to the name.<br />
 In this mode, xfig doesn&#8217;t connect the X server, so no window is opened, and it exits when finished.</dl>
<p> <code>-users</code>[<code>cale</code>] <i>scale</i></p>
<dl>
<dt>
<dd> Set the multiplier for displayed line lengths etc. This factor is multiplied by the actual length, radius or diameter of the object currently being drawn on the canvas. It is useful for making scale drawings, where e.g. 1 inch = 1 foot (userscale = 12.0) or 1cm = 1m (userscale = 100.0).</dl>
<p> <code>-useru</code>[<code>nit</code>] <i>units</i></p>
<dl>
<dt>
<dd> The <i>units</i> string is printed with the length information when drawing objects. For example if the <i>userscale</i> = 1.0 and the <i>userunit</i> = <i>ft</i> then a line which is 3 inches long on the canvas would be displayed as &#8220;length = 3 ft&#8221; when it is being drawn.</p>
<dt>
<dd> After <i>xfig</i> is started you may change the <i>userscale</i> and the <i>userunit</i> from a popup menu available by pressing mouse button 3 in the <i>units</i> box where the two rulers meet.</dl>
<p> <code>-visual</code> <i>visualname</i></p>
<dl>
<dt>
<dd> Use <i>visualname</i> as the visual for xfig. The names are TrueColor (case is not important), StaticColor, DirectColor, StaticGray, GrayScale and PseudoColor. <i>xfig</i> uses the default visual unless this is specified. Your server must support the desired visual. Use <i>xdpyinfo</i> to see what visuals and depths are supported. See also the <code>-depth</code> option.</dl>
<p> <code>-write_bak</code></p>
<dl>
<dt>
<dd> When saving a drawing into an existing .fig file xfig will first rename that file by appending</dl>
<p> <code>-zoom</code> <i>zoomscale</i></p>
<dl>
<dt>
<dd> Set the starting zoom scale. </p>
</dl>
<h2>X RESOURCES and DEFAULTS</h2>
<p> The overall widget name(Class) is xfig(Fig). These resources correspond to the command line arguments: </p>
<pre><code>
Name Type Default Command - line equivalent allownegcoords boolean true - allownegcoords(true),
    -dontallownegcoords(false)
            autorefresh boolean false -
        autorefresh
        axislines string pink
        - axislines balloon_delay integer 500(ms)-balloon_delay boldFont string 8x13bold - bold but_per_row integer 2 - but_per_row buttonFont string 6x13 - button canvasbackground string white - cbg canvasforeground string black - cfg correctfontsize boolean false - correctfontsize debug boolean false - debug depth integer * -depth dontswitchcmap boolean false - dontswitchcmap euc_encoding boolean false(n / a) locale_encoding boolean false(n / a) encoding integer 1 - encoding save8bit boolean false(n / a) exportLanguage string eps - exportLanguage export_margin integer 0 - export_margin flipvisualhints boolean false - flipvisualhints flushleft boolean false - flushleft(true),
    -center(false)
            freehand_resolution integer 25 -
        freehand_resolution
        grid_color string black
        - grid_color grid_unit string 1 / 16(inch)-grid_unit 0.1(metric)hiddentext boolean false - hiddentext icon_view boolean true - icon_view(true),
    -list_view(false)
            image_editor string xv
        - image_editor inches boolean true - inches(true),
    -imperial(true),
    -centimeters(false),
    -metric(false)
            installowncmap boolean false -
        installowncmap
        internalborderwidth integer 1 -
        internalBW
        international International booleanfalse
        - international jpeg_quality integer 75 - jpeg_quality justify boolean false - left(false),
    -right(true)
            keyFile string CompKeyDB
        - keyFile landscape boolean true - Landscape(true),
    -landscape(true),
    -Portrait(false),
    -portrait(false)
            latexfonts boolean false -
        latexfonts
            library_dir string ~ /
            xfiglib
        - library_dir magnification float 100 - magnification max_image_colors integer 64 - max_image_colors monochrome boolean false - monochrome multiple boolean false - multiple normalFont string 6x13 - normal overlap boolean true - overlap(true),
    -nooverlap(false)
            pageborder string lightblue
        - pageborder paper_size string Letter(inch) - paper_size A4(metric)
pheight float 8.5(landscape)-pheight
    9.5(portrait)
        pwidth float 11(landscape)-pwidth
    8.5(portrait)
        rigidtext boolean false -
    rigid(true)
        rulerthick integer 24 -
    rulerthick
    scalablefonts boolean true -
    scalablefonts(true),
    -noscalablefonts(false)
            scale_factor float 1.0 -
        scale_factor
        showallbuttons boolean false -
        showallbuttons
        showaxislines boolean true -
        showaxislines(true),
    -dontshowaxislines(false)
            showballoons boolean true -
        showballoons(true),
    -dontshowballoons(false)
            showdepthmanager boolean true -
        showdepthmanager(true),
    -dontshowdepthmanager(false)
            showlengths boolean false -
        showlengths(true),
    -dontshowlengths(false)
            shownums boolean false -
        shownums(true),
    -dontshownums(false)
            showpageborder boolean true -
        showpageborder(true),
    -dontshowpageborder(false)
            single boolean true -
        single
        smooth_factor integer 0 -
        smooth_factor
        specialtext boolean false -
        specialtext
        splash boolean true -
        splash(true),
    -nosplash(false)
                spellcheckcommand string spell
            % s
        - spellcheckcommand spinner_delay integer 500(ms)-spinner_delay spinner_rate integer 100(ms)-spinner_rate startfillstyle integer 0 - startfillstyle startfontsize float 12 - startfontsize startgridmode integer 0 - startgridmode startlatexFont string Default - startlatexFont startlinewidth integer 1 - startlinewidth startposnmode integer 1 - startposnmode startpsFont string Times - Roman - startpsFont starttextstep float 1.2 - starttextstep tablet boolean false - track,
    trackCursor boolean true - track(true),
    -notrack(false)
            transparent_color integer
        - 2(none)-transparent_color userscale float 1.0 - userscale userunit string in(inches)-userunit cm(metric)
visual string * -visual
                    write_bak boolean true -
    write_bak
        zoom float 1.0 -
    zoom
        *Default visual and depth depend on the X server.Use xdpyinfo
            to see what visuals and depths are supported.
</code></pre>
<h2>BUGS and RESTRICTIONS</h2>
<p> Please send bug reports, fixes, new features etc. to:<br />
 thomas.loimer [at] tuwien.ac.at </p>
<p> Because of the difference of some fonts in some X servers and the PostScript fonts on printers, text alignment can be problematic. </p>
<p> Not all operations employ smart redrawing of objects which are altered as a by product of the operation. You may need to use <i>Redraw</i> in these cases. </p>
<p> If the image is panned or the <i>xfig</i> window iconified and de-iconified during the middle of an operation (e.g. while drawing a line), the picture will be distorted. This can be corrected using <i>Redraw</i> after the operation is complete. </p>
<p> When zoomed very large, the length of dashes in dashed lines will top out at 255 pixels long. This is due to a restriction in X that the dash list is defined by char (255 pixels maximum for a dash). The figure will print correctly, however. </p>
<p> When you do a copy/rotate with multiple copies, only the creation of the last object can be undone with the Undo button. </p>
<p> Modifications to text using the popup search/update/replace/spell check panel cannot be undone.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-fig2dev/">fig2dev</a>(1) (<i>Fig2dev</i> package) </p>
<p> <a href="/docs/linux/man/1-gs/">gs</a>(1) (<i>Ghostscript</i> PostScript previewer)</p>
<h2>ACKNOWLEDGEMENT</h2>
<p> (From the original author, Supoj Sutanthavibul): Many thanks goes to Professor Donald E. Fussell who inspired the creation of this tool. </p>
<p> (From Brian Smith): Thanks to all the users who have contributed to xfig, especially Paul King who, besides adding many features, revamped the look and feel which became version 2.1.</p>
<h2>COPYRIGHT</h2>
<pre>
Original Copyright (c) 1985 by Supoj Sutanthavibul
Parts Copyright (c) 1989-2015 by Brian V. Smith
Parts Copyright (c) 1991 by Paul King
Parts Copyright (c) 2016-2018 by Thomas Loimer
Other Copyrights may be found in various files
</pre>
<p> Any party obtaining a copy of these files is granted, free of charge, a full and unrestricted irrevocable, world-wide, paid up, royalty-free, nonexclusive right and license to deal in this software and documentation files (the &quot;Software&quot;), including without limitation the rights to use, copy, modify, merge, publish and/or distribute copies of the Software, and to permit persons who receive copies from any such party to do so, with the only requirement being that this copyright notice remain intact. </p>
<p> THE AUTHORS DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS, IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE. </p>
<p> <i>PostScript</i> is a trademark of Adobe Systems Incorporated. </p>
<pre>
Parts Copyright (C) 1989 by Jef Poskanzer.
Copyright notice for pbmplus code:
Permission to use, copy, modify, and distribute this
software and its documentation for any purpose and without
fee is hereby granted, provided that the above copyright
notice appear in all copies and that both that copyright
notice and this permission notice appear in supporting
documentation.  This software is provided ``as is'' without
express or implied warranty.
</pre>
<h2>FILES</h2>
<dl>
<dt><i>/usr/share/xfig/CompKeyDB</i></p>
<dd> Data base of compose (meta) key sequences for 8-bit characters. A different file may be specified with the command line option <code>-keyFile</code> or X toolkit resource keyFile.</p>
<dt><i>/usr/share/doc/xfig/html</i></p>
<dd> This directory contains the html documentation.</p>
<dt><i>/usr/share/doc/xfig/FORMAT3.2</i></p>
<dd> Description of Fig file format.</p>
<dt><i>/usr/share/xfig/Libraries</i></p>
<dd> This directory contains libraries of Fig objects such as electrical symbols, logic symbols, etc.</p>
<dt><i>/usr/share/X11/app-defaults/Fig</i></p>
<dd> Application defaults file.</p>
<dt><i>/usr/share/applications/xfig.desktop</i></p>
<dd> Desktop entry file.</p>
<dt><i>/usr/share/pixmaps/xfig.png</i></p>
<dd> Desktop icon. </p>
</dl>
<h2>AUTHORS</h2>
<p> Many people have contributed to <i>xfig</i>. Here is a list of the people who have contributed the most (in chronological order): </p>
<p> <code>Version 1:</code> </p>
<p> Original author:<br />
 Supoj Sutanthavibul, University of Texas at Austin </p>
<p> The <i>LaTeX</i> line drawing modes were contributed by:<br />
 Frank Schmuck, Cornell University </p>
<p> Original X11 port by:<br />
 Ken Yap, Rochester </p>
<p> Variable window sizes, cleanup of X11 port, right hand side panel:<br />
 Dana Chee, Bellcore </p>
<p> Cleanup of color port to X11 by:<br />
 John T. Kohl, MIT </p>
<p> <code>Version 2.0:</code> </p>
<p> Area fill, multiple line thicknesses, multiple fonts and font sizes, bottom panel, line style/thickness, (and anything else that wasn&#8217;t written by the others) by:<br />
 Brian Smith<br />
 (standard disclaimer applies)<br />
 (bvsmith [at] lbl.gov) </p>
<p> Popup change-object menu by:<br />
 Jon Tombs<br />
 Frank Schmuck </p>
<p> Zooming and panning functions, shift key select mechanism by:<br />
 Dieter Pellkofer<br />
 Henning Spruth </p>
<p> Depth feature by:<br />
 Mike Lutz </p>
<p> Cut/Paste by:<br />
 Tom Tkacik </p>
<p> <code>Version 2.1:</code> </p>
<p> Indicator panel, file menu popup, print menu popup, panning with rulers, mouse function window, regular polygon, rubberbanding of circles/ellipses, filled splines on canvas, dashed/dotted splines on canvas, update button, arbitrary angle rotation of objects, alignment in compound, object scaling, constrained copy/move, corner markers for compound, context sensitive corner markers, smarter redraw, undo for compound and point move for boxes, cancel object creation, point positioning to three resolutions, <i>TransFig</i> scalable text, hidden text, special text, save of figure on crash by: </p>
<p> Paul King (king [at] cs.uq.oz.au)<br />
 with help from:<br />
 Brian Smith and Micah Beck (beck [at] cs.utk.edu) </p>
<p> Encapsulated <i>PostScript</i> importing by:<br />
 Brian Boyter </p>
<p> Pan/zoom with ctrl key/mouse by:<br />
 Henning Spruth </p>
<p> International characters by:<br />
 Herve Soulard </p>
<p> Directory Browser based on XDir by:<br />
 Win Treese, Digital Equipment Corporation </p>
<p> Rotated ellipses by:<br />
 James Tough, Dept. of Computer Science, Heriot-Watt University, Scotland </p>
<p> Rotated text from the <i>xvertext</i> package by:<br />
 Alan Richardson, Space Science Centre, School of MAPS, University of Sussex </p>
<p> Popup scale menu and dynamic switching between inches and cm by:<br />
 Paul King (king [at] cs.uq.oz.au) </p>
<p> Extensive man page formatting revisions by:<br />
 David W. Sanderson </p>
<p> Display Postscript code for IBM RS/6000 by:<br />
 Dave Hale (dhale [at] green.mines.colorado.edu) </p>
<p> <code>Version 3.0:</code> </p>
<p> New arrowhead types, separate pen/fill colors, new file protocol, more colors with extended color popup panel, new arc style, new fill patterns (bricks, etc), new line join and cap styles, export offset and file load offset, XPM import, XBM import and export (and anything else that wasn&#8217;t written by the others) by:<br />
 Brian Smith<br />
 (Note: the color popup panel was based on <i>xcoloredit</i> by Richard Hesketh) </p>
<p> GIF header reading code by:<br />
 David Koblas from the giftoppm part of the pbmplus package </p>
<p> XPM export code (using XPM3 libraries) by:<br />
 Karel van Houten (K.H.C.vanHouten [at] research.ptt.nl) </p>
<p> Higher figure resolution (1200dpi) by:<br />
 Ross Martin (martin [at] trcsun3.eas.asu.edu) </p>
<p> Color quantization using neural network by:<br />
 Anthony Dekker (dekker [at] ACM.org)<br />
 [NEUQUANT Neural-Net quantization algorithm by Anthony Dekker, 1994. See &#8220;Kohonen neural networks for optimal colour quantization&#8221; in &#8220;Network: Computation in Neural Systems&#8221; Vol. 5 (1994) pp 351-367. for a discussion of the algorithm.] </p>
<p> Floyd-Steinberg algorithm for dithering color images on monochrome displays lifted from the Pbmplus package by Jef Poskanser. </p>
<p> rotate/flip objects around/about selected anchor point and multiple copies of objects by:<br />
 Uwe Bonnes (bon [at] lte.e-technik.uni-erlangen.de) </p>
<p> Input tablet extension by:<br />
 Greg LaCoste (greg [at] seismo.do.usbr.gov) </p>
<p> <code>Version 3.1:</code> </p>
<p> The only difference between protocol version 3.0 and version 3.1 is that the position of the &#8220;magnet&#8221; has been shifted by 14 fig units. In the 2.1 and older versions of xfig the grid was in multiples of 5 fig units, but they were on intervals 4, 9, 14, 19, etc. When version 3.0 was created, coordinates were simply multiplied by the ratio of the resolutions (1200/80 = 15) so values like 4 became 60 instead of 74 ((4+1)*15 &#8211; 1). </p>
<p> The JPEG import/export code uses the Independent JPEG Group software (see jpeg/README for details) </p>
<p> Image browser, editor and screen capture features by:<br />
 Jim Daley (jdaley [at] cix.compulink.co.uk) </p>
<p> <code>Version 3.2:</code> </p>
<p> The changes to the version 3.2 file protocol are the addition of the paper size, print/export magnification, single/multiple page indicator and a transparent color name used for GIF export to the header of the file.<br />
 The other difference in the version 3.2 protocol is the mathematical model used for splines. The new version uses X-splines which allows the user to mix interpolation and approximation points in a same curve. More precisely, it means that an X-spline curve is neither an interpolated spline nor an approximated one, it is BOTH (the behaviour of each point is controlled by one single parameter called &#8220;shape factor&#8221;). For additional information about X-splines, see: </p>
<p>&nbsp;<wbr>&nbsp;&quot;X-Splines: A Spline Model Designed for the End User&quot;<br />
&nbsp;<wbr>&nbsp;by C. Blanc and C. Schlick, Proceedings of SIGGRAPH&#8217;95<br />
&nbsp;<wbr>&nbsp;<a rel="nofollow" href="http://dept-info.labri.u-bordeaux.fr/~schlick/DOC/sig1.html">http://dept-info.labri.u-bordeaux.fr/~schlick/DOC/sig1.html</a> </p>
<p> Caveat: Because previous spline models (quadratic B-splines and Bezier with hidden points) are no longer supported, curves that are present in version 3.1 and older files are automatically converted to X-splines. This translation is only an approximation process. It means that the converted curves are not exactly the same as the original ones. Though they are usually very close, some hand-fitting may be needed in some pathological cases. </p>
<p> Inclusion of X-splines by:<br />
 Carole Blanc (blanc [at] labri.u-bordeaux.fr)<br />
 Christophe Schlick (schlick [at] labri.u-bordeaux.fr)<br />
 Note: the initial implementation was done by C. Feuille, S. Grosbois, L. Maziere and L. Minihot as a student practice (Universite Bordeaux, France). </p>
<p> Open/close compound feature written by<br />
 Bill Taylor (bill [at] mainstream.com) </p>
<p> Library feature written by<br />
 Stephane Mancini (mancini [at] elecsrv.enst.fr) (object preview by Brian V. Smith) </p>
<p> The library objects in the Electrical and Logic libraries were done by<br />
 Peter Hiscocks (phiscock [at] ee.ryerson.ca) </p>
<p> The library objects in the Computer, Networks, and Hospital-Equipment libraries were extracted from the clipart example files by<br />
 Bill Chimiak (chim [at] bgsm.edu) </p>
<p> <code>Version 3.2.3 and newer:</code> </p>
<p> Please see the CHANGES file for credits for newer releases.</p>
<h2>NOTES</h2>
<p> Many bug fixes/cleanups etc. by a host of faithful users. </p>
<p> See the <code>CHANGES</code> file for all the credits. </p>
<p> The <i>Fig2dev</i> package was written by Micah Beck and is maintained by Thomas Loimer. </p>
<h2>Index</h2>
