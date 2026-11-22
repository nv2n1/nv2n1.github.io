---

title: "djview(1)"
name: "djview"
section: "1"
letter: "d"
url: "/docs/linux/man/1-djview/"
description: "djview3 – Standalone DjVu viewer"
---

<p> djview3 &#8211; Standalone DjVu viewer </p>
<h2>SYNOPSIS</h2>
<p> <code>djview3 [</code><i>options</i><code>] [</code><i>djvufile</i><code>]</code> </p>
<h2>DESCRIPTION</h2>
<p> Standalone viewer for DjVu files. Features include navigating documents, zooming and panning page images, producing and displaying thumbnails, searching documents for particular words in the hidden text layer, copying hidden text to the clipboard, exporting page images as PNM files, saving pages and documents as bundled or indirect multi-page files, and printing page and documents to Postscript printers. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></dt>
<dd> Display a brief help message.</dd>
<dt><code>-page=</code><i>pagenum</i></dt>
<dd> Open page <i>pagenum</i> of the document.</dd>
<dt><code>-style=</code><i>stylename</i></dt>
<dd> Specify the graphical user interface style. Recognized values for <i>stylename</i> depend on the installed version of the Qt toolkit. Common style names include <code>windows</code>, <code>motif</code>, <code>motifplus</code>, <code>sgi</code>, <code>cde</code>, and <code>platinum</code>.</dd>
<dt><code>-fullscreen, -fs </code></dt>
<dd> Start <code>djview3 </code> in full screen mode. This only works if you also provide a DjVu file name on the command line.</dd>
<dt><code>-geometry=</code><i>geom</i></dt>
<dd> Specify the initial window size. The X11 geometry specification <i>geom</i> often has the form <i>w</i><code>x</code><i>h</i><code>+</code><i>x</i><code>+</code><i>y</i> where <i>w</i> and <i>h</i> are the window width and height, and <i>x</i> and <i>y</i> indicate the window position.</dd>
<dt><code>-display=</code><i>disp</i></dt>
<dd> Specify that the <code>djview3</code> windows should appear on the X11 display <i>disp</i>.</dd>
<dt><code>-fn </code><i>fontname</i></dt>
<dd> Specify the name of the default font used for buttons and menus.</dd>
<dt><code>-bg </code><i>color</i></dt>
<dd> Specify the default background color.</dd>
<dt><code>-fg </code><i>color</i></dt>
<dd> Specify the default foreground color.</dd>
<dt><code>-btn </code><i>color</i></dt>
<dd> Specify the default button color.</dd>
<dt><code>-visual TrueColor</code></dt>
<dd> Force the use of a TrueColor visual on a 8 bit display.</dd>
<dt><code>-ncols count</code></dt>
<dd> Limit the number of colors allocated in the color cube on a 8 bit display. The default is 216.</dd>
<dt><code>-cmap</code></dt>
<dd> Cause <code>djview3</code> to install a private color map on an 8-bit display.</dd>
<dt><code>-fix</code></dt>
<dd> Checks the files <code>$HOME/.mailcap </code> and <code>$HOME/.mime.types</code> and attempt to reconstruct sensible DjVu entries. This is sometimes useful to make the DjVu plugin work. </dd>
</dl>
<h2>USING DJVIEW3 AS A BROWSER PLUGIN</h2>
<p> The djvulibre browser plugin works by invoking a standalone DjVu viewer with the special option <code>-netscape</code>. See the man page <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1) for more details. </p>
<p> When <code>djview3</code> is invoked by the djvulibre browser plugin, a number of options can be specified as CGI style arguments in document URL according to the following template:</p>
<dl>
<dt>
</dt><dd> <code><a rel="nofollow" href="http://server/dir/file.djvu?djvuopts">http://server/dir/file.djvu?djvuopts</a>&amp;</code><i>keyword=value</i><code>&amp;</code><i>keyword=value</i><code>&amp;</code><i>&#8230;</i></dd></dl>
<p> The DjVu browser plugin only recognizes keywords that appear after the word <code>djvuopts</code>. Unrecognized keywords are silently ignored. The following keywords are recognized:</p>
<dl>
<dt><code>passive=(yes|no)</code></dt>
<dd> Cause the image to be displayed in a manner similar to an ordinary web image. The default zoom factor is changed to &quot;Fit Page&quot;. The toolbar, the pop-up menu, the scroll bar, and the keyboard shortcuts are disabled. The default is no.</dd>
<dt><code>scrollbars=(yes|no)</code></dt>
<dd> Enable or disable the presence of scroll bars when the full image size exceeds the plugin window size. The default is yes.</dd>
<dt><code>menu=(yes|no)</code></dt>
<dd> Enable or disable the pop-up menu. The pop-up menu is enabled by default.</dd>
<dt><code>keyboard=(yes|no)</code></dt>
<dd> Enable or disable the DjVu plugin keyboard shortcuts. The default is yes (enabled).</dd>
<dt><code>frame=(yes|no)</code></dt>
<dd> Enable or disable the display of a thin gray frame around the DjVu image. Keyboard shortcuts are enabled by default.</dd>
<dt><code>links=(yes|no)</code></dt>
<dd> Enable or disable hyper-links in the DjVu image. Hyper-links are enabled by default.</dd>
<dt><code>logo=(yes|no)</code></dt>
<dd> Enable or disable the display of the DjVu log while the plug-in is downloading data. This is enabled by default.</dd>
<dt><code>page=</code><i>pagenum</i></dt>
<dd> Specify the initial page to be displayed. Page numbers are numbered from 1.</dd>
<dt><code>zoom=</code><i>zoomfactor</i></dt>
<dd> Specify the initial zoom factor. Unless the toolbar, pop-up menu and keyboard are disabled, the user will be able to change the zoom factor. Legal values for <i>zoomfactor</i> are shown in the below:<br/>
 <center></dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><i>number</i></td>
<td>Magnification factor in range 10% to 999%.
</td>
</tr>
<tr VALIGN=top>
<td><code>one2one</code></td>
<td>Select the &quot;one-to-one&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>width</code></td>
<td>Select the &quot;fit width&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>page</code></td>
<td>Select the &quot;fit page&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>stretch</code></td>
<td>Stretch the image to the plugin window size.
</td>
</tr>
</table>
</table>
<p></center></dl>
<dl>
<dt><code>mode=</code><i>modespec</i></dt>
<dd> Specify the initial display mode. Unless the toolbar and pop-up menu are disabled, the user will be able to change it. Legal values for <i>modespec</i> are shown in the below:<br/>
 <center></dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>color</code></td>
<td>Display the color image.
</td>
</tr>
<tr VALIGN=top>
<td><code>bw</code></td>
<td>Display the foreground mask only.
</td>
</tr>
<tr VALIGN=top>
<td><code>fore</code></td>
<td>Display the foreground only.
</td>
</tr>
<tr VALIGN=top>
<td><code>back</code></td>
<td>Display the background only.
</td>
</tr>
</table>
</table>
<p></center></dl>
<dl>
<dt><code>hor_align=</code><i>keyword</i></dt>
<dd> Specify the horizontal position of the page in the viewer window. (This does not specify what part of the page will be shown, but rather how margins will be laid out around the page in the plugin window.) Argument <i>keyword</i> must be <code>left</code>, <code>center</code>, or <code>right</code>.</dd>
<dt><code>ver_align=</code><i>keyword</i></dt>
<dd> Specify the vertical position of the page in the viewer window. (This does not specify what part of the page will be shown, but rather how margins will be laid out around the page in the plugin window.) Argument <i>keyword</i> must be <code>top</code>, <code>center</code>, or <code>bottom</code>.</dd>
<dt><code>toolbar=</code><i>keyword</i><code>{(,|+|-)</code><i>keyword</i><code>}</code></dt>
<dd> Controls the appearance and the contents of the toolbar. The argument of option <code>toolbar</code> is composed of a number of keywords separated by characters comma, plus or minus. The appearance of the toolbar is controlled by keywords placed before the first occurrence of a character plus or minus. The following keywords are recognized in this context:<br/>
 <center></dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>no</code></td>
<td>Disable toolbar.
</td>
</tr>
<tr VALIGN=top>
<td><code>always</code></td>
<td>Disable toolbar &quot;autohide&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>auto</code></td>
<td>Enable toolbar &quot;autohide&quot; mode.
</td>
</tr>
<tr VALIGN=top>
<td><code>top</code></td>
<td>Place toolbar along top edge (not implemented).
</td>
</tr>
<tr VALIGN=top>
<td><code>bottom</code></td>
<td>Place toolbar along bottom edge.
</td>
</tr>
</table>
</table>
<p></center></p>
<dt>
</dt><dd> The contents of the toolbar is controlled by keywords placed after the first occurrence of a character plus or minus. Each keyword adds (after a plus) or remove (after a minus) a particular toolbar button or group of buttons. The initial content of the toolbar is determined by the first occurrence of a character plus or minus. When this is a plus the toolbar is initially empty. When this is a minus the toolbar is initially full. The following keywords are recognized:<br/>
 <center></dd>
<table BORDER>
<tr>
<td>
<table>
<tr VALIGN=top>
<td><code>fore,back,color,bw</code></td>
<td>for the display mode selection tool.
</td>
</tr>
<tr VALIGN=top>
<td><code>rescombo</code></td>
<td>for the zoom selection tool.
</td>
</tr>
<tr VALIGN=top>
<td><code>zoom</code></td>
<td>for the zoom buttons.
</td>
</tr>
<tr VALIGN=top>
<td><code>pan</code></td>
<td>for the panning mode button.
</td>
</tr>
<tr VALIGN=top>
<td><code>zoomsel</code></td>
<td>for the zooming mode button.
</td>
</tr>
<tr VALIGN=top>
<td><code>textsel</code></td>
<td>for the text selection mode button.
</td>
</tr>
<tr VALIGN=top>
<td><code>rotate</code></td>
<td>for the image rotation buttons.
</td>
</tr>
<tr VALIGN=top>
<td><code>search</code></td>
<td>for the text search button.
</td>
</tr>
<tr VALIGN=top>
<td><code>save</code></td>
<td>for the save button.
</td>
</tr>
<tr VALIGN=top>
<td><code>print</code></td>
<td>for the print button.
</td>
</tr>
<tr VALIGN=top>
<td><code>pagecombo</code></td>
<td>for the page selection tool.
</td>
</tr>
<tr VALIGN=top>
<td><code>firstlast</code></td>
<td>for the first-page and last-page buttons.
</td>
</tr>
<tr VALIGN=top>
<td><code>prevnext</code></td>
<td>for the previous- and next-page buttons.
</td>
</tr>
<tr VALIGN=top>
<td>backforw</td>
</tr>
</table>
</table>
<p></center></dl>
<dl>
<dt><code>highlight=</code><i>x</i><code>,</code><i>y</i><code>,</code><i>w</i><code>,</code><i>h</i><code>[,</code><i>color</i><code>]</code></dt>
<dd> Display a highlighted rectangle at the specified coordinates and with the specified color. Coordinates <i>x</i>, <i>y</i>, <i>w</i>, and <i>h</i> are measured in document image coordinates (not screen coordinates). The origin is set at the bottom left corner of the image. The color <i>color</i> must be given in hexadecimal RRGGBB format. Omitting the color argument means to use XOR highlighting. Multiple highlighted zone can be specified.</dd>
<dt><code>rotate=(0|90|180|270)</code></dt>
<dd> Rotate the djvu image by the specified angle expressed in degrees counter-clockwise.</dd>
<dt><code>print=(yes|no)</code></dt>
<dd> Enable or disable printing the djvu image. Printing is enabled by default.</dd>
<dt><code>cache=(yes|no)</code></dt>
<dd> Enable or disable the caching of fully decoded pages of the document. Caching is on by default. Caching of documents whose URL does not contain extension <code>.djvu</code> or <code>.djv</code> is off by default.</dd></dl>
<p> The same options can be specified as parameters of EMBED or OBJECT tags in a HTML file. See <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1) for more details. </p>
<h2>CREDITS</h2>
<p> This program was written by Andrei Erofeev &lt;andrew_erofeev [at] yahoo.com&gt; and was then improved by Bill Riemers &lt;docbill [at] sourceforge.net&gt; and L&#8217;eon Bottou &lt;leonb [at] users.sourceforge.net&gt;. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-djvu/">djvu</a></code>(1), <code><a href="/docs/linux/man/1-ddjvu/">ddjvu</a></code>(1), <code><a href="/docs/linux/man/1-nsdejavu/">nsdejavu</a></code>(1) </p>
