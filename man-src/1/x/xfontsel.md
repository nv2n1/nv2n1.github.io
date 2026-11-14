---
title: "xfontsel(1)"
name: "xfontsel"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfontsel/"
description: "xfontsel – point and click selection of X11 font names"
---

<h2 class="name">NAME</h2>
<p> xfontsel &#8211; point and click selection of X11 font names </p>
<h2>SYNTAX</h2>
<p> <code>xfontsel</code> [-<i>toolkitoption</i> &#8230;] [<code>-pattern </code><i>fontname</i>] [<code>-print</code>] [<code>-sample </code><i>text</i>] [<code>-sample16 </code><i>text16</i>] [<code>-sampleUCS </code><i>textUCS</i>] [<code>-scaled</code>] </p>
<h2>DESCRIPTION</h2>
<p> The <i>xfontsel</i> application provides a simple way to display the fonts known to your X server, examine samples of each, and retrieve the X Logical Font Description (&quot;XLFD&quot;) full name for a font. </p>
<p> If <code>-pattern</code> is not specified, all fonts with XLFD 14-part names will be selectable. To work with only a subset of the fonts, specify <code>-pattern</code> followed by a partially or fully qualified font name; e.g., &#8220;-pattern *medium*&#8221; will select that subset of fonts which contain the string &#8220;medium&#8221; somewhere in their font name. Be careful about escaping wildcard characters in your shell. </p>
<p> If <code>-print</code> is specified on the command line the selected font specifier will be written to standard output when the <i>quit</i> button is activated. Regardless of whether or not <code>-print</code> was specified, the font specifier may be made the PRIMARY (text) selection by activating the <i>select</i> button. </p>
<p> The <code>-sample</code> option specifies the sample text to be used to display the selected font if the font is linearly indexed, overriding the default. </p>
<p> The <code>-sample16</code> option specifies the sample text to be used to display the selected font if the font is matrix encoded, overriding the default. </p>
<p> The <code>-sampleUCS</code> option specifies the sample text encoded in the UTF-8 form to be used to display the selected font if the font has a CHARSET_REGISTRY of ISO10646, overriding the default. </p>
<p> The <code>-scaled</code> option enables the ability to select scaled fonts at arbitrary pixel or point sizes. </p>
<h2>INTERACTIONS</h2>
<p> Clicking any pointer button in one of the XLFD field names will pop up a menu of the currently-known possibilities for that field. If previous choices of other fields were made, only values for fonts which matched the previously selected fields will be selectable; to make other values selectable, you must deselect some other field(s) by choosing the &#8220;*&#8221; entry in that field. Unselectable values may be omitted from the menu entirely as a configuration option; see the <code>ShowUnselectable</code> resource, below. Whenever any change is made to a field value, <i>xfontsel</i> will assert ownership of the PRIMARY_FONT selection. Other applications (see, e.g., <i>xterm</i>) may then retrieve the selected font specification. </p>
<p> Scalable fonts come back from the server with zero for the pixel size, point size, and average width fields. Selecting a font name with a zero in these positions results in an implementation-dependent size. Any pixel or point size can be selected to scale the font to a particular size. Any average width can be selected to anamorphically scale the font (although you may find this challenging given the size of the average width menu). </p>
<p> Clicking the left pointer button in the <i>select</i> widget will cause the currently selected font name to become the PRIMARY text selection as well as the PRIMARY_FONT selection. This then allows you to paste the string into other applications. The <code>select</code> button remains highlighted to remind you of this fact, and de-highlights when some other application takes the PRIMARY selection away. The <i>select</i> widget is a toggle; pressing it when it is highlighted will cause <i>xfontsel</i> to release the selection ownership and de-highlight the widget. Activating the <i>select</i> widget twice is the only way to cause <i>xfontsel</i> to release the PRIMARY_FONT selection. </p>
<h2>RESOURCES</h2>
<p> The application class is <code>XFontSel</code>. Most of the user-interface is configured in the app-defaults file; if this file is missing a warning message will be printed to standard output and the resulting window will be nearly incomprehensible. </p>
<p> Most of the significant parts of the widget hierarchy are documented in <i>/etc/X11/app-defaults/XFontSel</i>, </p>
<p> Application specific resources: </p>
<dl>
<dt><code>cursor (</code>class<code> Cursor)</code></p>
<dd> Specifies the cursor for the application window.</p>
<dt><code>pattern (</code>class<code> Pattern)</code></p>
<dd> Specifies the font name pattern for selecting a subset of available fonts. Equivalent to the <code>-pattern</code> option. Most useful patterns will contain at least one field delimiter; e.g. &#8220;*-m-*&#8221; for monospaced fonts.</p>
<dt><code>pixelSizeList (</code>class<code> PixelSizeList)</code></p>
<dd> Specifies a list of pixel sizes to add to the pixel size menu, so that scalable fonts can be selected at those pixel sizes. The default pixelSizeList contains 7, 30, 40, 50, and 60.</p>
<dt><code>pointSizeList (</code>class<code> PointSizeList)</code></p>
<dd> Specifies a list of point sizes (in units of tenths of points) to add to the point size menu, so that scalable fonts can be selected at those point sizes. The default pointSizeList contains 250, 300, 350, and 400.</p>
<dt><code>printOnQuit (</code>class<code> PrintOnQuit)</code></p>
<dd> If <i>True</i> the currently selected font name is printed to standard output when the quit button is activated. Equivalent to the <code>-print</code> option.</p>
<dt><code>sampleText (</code>class<code> Text)</code></p>
<dd> The sample 1-byte text to use for linearly indexed fonts. Each glyph index is a single byte, with newline separating lines.</p>
<dt><code>sampleText16 (</code>class<code> Text16)</code></p>
<dd> The sample 2-byte text to use for matrix-encoded fonts. Each glyph index is two bytes, with a 1-byte newline separating lines.</p>
<dt><code>scaledFonts (</code>class<code> ScaledFonts)</code></p>
<dd> If <i>True</i> then selection of arbitrary pixel and point sizes for scalable fonts is enabled.</dl>
<p> Widget specific resources: </p>
<dl>
<dt><code>showUnselectable (</code>class<code> ShowUnselectable)</code></p>
<dd> Specifies, for each field menu, whether or not to show values that are not currently selectable, based upon previous field selections. If shown, the unselectable values are clearly identified as such and do not highlight when the pointer is moved down the menu. The full name of this resource is <code>fieldN.menu.options.showUnselectable</code>, class <code>MenuButton.SimpleMenu.Options.ShowUnselectable</code>; where N is replaced with the field number (starting with the left-most field numbered 0). The default is True for all but field 11 (average width of characters in font) and False for field 11. If you never want to see unselectable entries, &#8216;*menu.options.showUnselectable:False&#8217; is a reasonable thing to specify in a resource file.</dl>
<h2>FILES</h2>
<p>&nbsp;$XFILESEARCHPATH/XFontSel </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-xfd/">xfd</a>(1) </p>
<h2>BUGS</h2>
<p> Sufficiently ambiguous patterns can be misinterpreted and lead to an initial selection string which may not correspond to what the user intended and which may cause the initial sample text output to fail to match the proffered string. Selecting any new field value will correct the sample output, though possibly resulting in no matching font. </p>
<p> Should be able to return a FONT for the PRIMARY selection, not just a STRING. </p>
<p> Any change in a field value will cause <i>xfontsel</i> to assert ownership of the PRIMARY_FONT selection. Perhaps this should be parameterized. </p>
<p> When running on a slow machine, it is possible for the user to request a field menu before the font names have been completely parsed. An error message indicating a missing menu is printed to stderr but otherwise nothing bad (or good) happens. </p>
<p> The average-width menu is too large to be useful.</p>
<h2>COPYRIGHT</h2>
<p> Copyright 1989, 1991, X Consortium </p>
<p> See <i><a href="/docs/linux/man/7-x/">X</a>(7)</i> for a full statement of rights and permissions.</p>
<h2>AUTHOR</h2>
<p> Ralph R. Swick, Digital Equipment Corporation/MIT Project Athena </p>
<p> Mark Leisher &lt;mleisher [at] crl.nmsu.edu&gt; added the support for the UTF-8 sample text. </p>
<h2>Index</h2>
