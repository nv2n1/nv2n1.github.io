---
title: "xpdf(1)"
name: "xpdf"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xpdf/"
description: "xpdf – Portable Document Format (PDF) file viewer for X (version 3.04)"
---

<h2>NAME</h2>
<p> xpdf &#8211; Portable Document Format (PDF) file viewer for X (version 3.04)</p>
<h2>SYNOPSIS</h2>
<p> <code>xpdf</code> [options] [<i>PDF-file</i> [<i>page</i> | +<i>dest</i>]]</p>
<h2>DESCRIPTION</h2>
<p> <code>Xpdf</code> is a viewer for Portable Document Format (PDF) files. (These are also sometimes also called &#8216;Acrobat&#8217; files, from the name of Adobe&#8217;s PDF software.) Xpdf runs under the X Window System on UNIX, VMS, and OS/2. </p>
<p> To run xpdf, simply type: </p>
<dl>
<dt>
<dd> xpdf file.pdf</dl>
<p> where <i>file.pdf</i> is your PDF file. The file name can be followed by a number specifying the page which should be displayed first, e.g.: </p>
<dl>
<dt>
<dd> xpdf file.pdf 18</dl>
<p> You can also give a named destination, prefixed with &#8216;+&#8217; in place of the page number. (This is only useful with PDF files that provide named destination targets.) </p>
<p> You can also start xpdf without opening any files: </p>
<dl>
<dt>
<dd> xpdf</dl>
<h2>CONFIGURATION FILE</h2>
<p> Xpdf reads a configuration file at startup. It first tries to find the user&#8217;s private config file, ~/.xpdfrc. If that doesn&#8217;t exist, it looks for a system-wide config file, typically /usr/local/etc/xpdfrc (but this location can be changed when xpdf is built). See the <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5) man page for details.</p>
<h2>OPTIONS</h2>
<p> Many of the following options can be set with configuration file commands or X resources. These are listed in square brackets with the description of the corresponding command line option.</p>
<dl>
<dt><code>-g</code><i> geometry</i></p>
<dd> Set the initial window geometry. (<code>-geometry</code> is equivalent.) [X resource: <code>xpdf.geometry</code>]</p>
<dt><code>-title</code><i> title</i></p>
<dd> Set the window title. By default, the title will be &quot;xpdf: foo.pdf&quot;. [X resource: <code>xpdf.title</code>]</p>
<dt><code>-cmap</code></p>
<dd> Install a private colormap. This is ignored on TrueColor visuals. [X resource: <code>xpdf.installCmap</code>]</p>
<dt><code>-rgb</code><i> number</i></p>
<dd> Set the size of largest RGB cube xpdf will try to allocate. The default is 5 (for a 5x5x5 cube); set to a smaller number to conserve color table entries. This is ignored with private colormaps and on TrueColor visuals. [X resource: <code>xpdf.rgbCubeSize</code>]</p>
<dt><code>-rv</code></p>
<dd> Set reverse video mode. This reverses the colors of everything except images. It may not always produce great results for PDF files which do weird things with color. This also causes the paper color to default to black. [X resource: <code>xpdf.reverseVideo</code>]</p>
<dt><code>-papercolor</code><i> color</i></p>
<dd> Set the &quot;paper color&quot;, i.e., the background of the page display. This will not work too well with PDF files that do things like filling in white behind the text. [X resource: <code>xpdf.paperColor</code>]</p>
<dt><code>-mattecolor</code><i> color</i></p>
<dd> Set the matte color, i.e., the color used for background outside the actual page area. (There is a separate setting, xpdf.fullScreenMatteColor, for full-screen mode.) [X resource: <code>xpdf.matteColor</code>]</p>
<dt><code>-z</code><i> zoom</i></p>
<dd> Set the initial zoom factor. A number specifies a zoom percentage, where 100 means 72 dpi. You may also specify &#8216;page&#8217;, to fit the page to the window size, or &#8216;width&#8217;, to fit the page width to the window width. [config file: <code>initialZoom</code>; or X resource: <code>xpdf.initialZoom</code>]</p>
<dt><code>-cont</code></p>
<dd> Start in continuous view mode, i.e., with one vertical scroll bar for the whole document. [config file: <code>continuousView</code>]</p>
<dt><code>-freetype</code><i> yes | no</i></p>
<dd> Enable or disable FreeType (a TrueType / Type 1 font rasterizer). This defaults to &quot;yes&quot;. [config file: <code>enableFreeType</code>]</p>
<dt><code>-aa</code><i> yes | no</i></p>
<dd> Enable or disable font anti-aliasing. This defaults to &quot;yes&quot;. [config file: <code>antialias</code>]</p>
<dt><code>-aaVector</code><i> yes | no</i></p>
<dd> Enable or disable vector anti-aliasing. This defaults to &quot;yes&quot;. [config file: <code>vectorAntialias</code>]</p>
<dt><code>-ps</code><i> PS-file</i></p>
<dd> Set the default file name for PostScript output (i.e., the name which will appear in the print dialog). This can also be of the form &#8216;|command&#8217; to pipe the PostScript through a command. [config file: <code>psFile</code>]</p>
<dt><code>-paper</code><i> size</i></p>
<dd> Set the paper size to one of &quot;letter&quot;, &quot;legal&quot;, &quot;A4&quot;, or &quot;A3&quot;. This can also be set to &quot;match&quot;, which will set the paper size to match the size specified in the PDF file. [config file: <code>psPaperSize</code>]</p>
<dt><code>-paperw</code><i> size</i></p>
<dd> Set the paper width, in points. [config file: <code>psPaperSize</code>]</p>
<dt><code>-paperh</code><i> size</i></p>
<dd> Set the paper height, in points. [config file: <code>psPaperSize</code>]</p>
<dt><code>-level1</code></p>
<dd> Generate Level 1 PostScript. The resulting PostScript files will be significantly larger (if they contain images), but will print on Level 1 printers. This also converts all images to black and white. [config file: <code>psLevel</code>]</p>
<dt><code>-enc</code><i> encoding-name</i></p>
<dd> Sets the encoding to use for text output. The <i>encoding-name</i> must be defined with the unicodeMap command (see <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5)). This defaults to &quot;Latin1&quot; (which is a built-in encoding). [config file: <code>textEncoding</code>]</p>
<dt><code>-eol</code><i> unix | dos | mac</i></p>
<dd> Sets the end-of-line convention to use for text output. [config file: <code>textEOL</code>]</p>
<dt><code>-opw</code><i> password</i></p>
<dd> Specify the owner password for the PDF file. Providing this will bypass all security restrictions.</p>
<dt><code>-upw</code><i> password</i></p>
<dd> Specify the user password for the PDF file.</p>
<dt><code>-fullscreen</code></p>
<dd> Open xpdf in full-screen mode, useful for presentations.</p>
<dt><code>-remote</code><i> name</i></p>
<dd> Start/contact xpdf remote server with specified name (see the <code>REMOTE SERVER MODE</code> section below).</p>
<dt><code>-exec</code><i> command</i></p>
<dd> Execute a command (see the <code>COMMANDS</code> section below) in an xpdf remote server window (with -remote only).</p>
<dt><code>-reload</code></p>
<dd> Reload xpdf remote server window (with -remote only).</p>
<dt><code>-raise</code></p>
<dd> Raise xpdf remote server window (with -remote only).</p>
<dt><code>-quit</code></p>
<dd> Kill xpdf remote server (with -remote only).</p>
<dt><code>-cmd</code></p>
<dd> Print commands as they&#8217;re executed (useful for debugging). [config file: <code>printCommands</code>]</p>
<dt><code>-q</code></p>
<dd> Don&#8217;t print any messages or errors. [config file: <code>errQuiet</code>]</p>
<dt><code>-cfg</code><i> config-file</i></p>
<dd> Read <i>config-file</i> in place of ~/.xpdfrc or the system-wide config file.</p>
<dt><code>-v</code></p>
<dd> Print copyright and version information.</p>
<dt><code>-h</code></p>
<dd> Print usage information. (<code>-help</code> and <code>&#8211;help</code> are equivalent.)</dl>
<p> Several other standard X options and resources will work as expected:</p>
<dl>
<dt><code>-display</code><i> display</i></p>
<dd> [X resource: <code>xpdf.display</code>]</p>
<dt><code>-fg</code><i> color</i></p>
<dd> (<code>-foreground</code> is equivalent.) [X resource: <code>xpdf*Foreground</code>]</p>
<dt><code>-bg</code><i> color</i></p>
<dd> (<code>-background</code> is equivalent.) [X resource: <code>xpdf*Background</code>]</p>
<dt><code>-font</code><i> font</i></p>
<dd> (<code>-fn</code> is equivalent.) [X resource: <code>xpdf*fontList</code>]</dl>
<p> The color and font options only affect the user interface elements, not the PDF display (the &#8216;paper&#8217;). </p>
<p> The following X resources do not have command line option equivalents:</p>
<dl>
<dt><code>xpdf.toolTipEnable</code></p>
<dd> Enables (if set to true) or disables (if set to false) the tool-tips on the toolbar buttons.</p>
<dt><code>xpdf.fullScreenMatteColor</code></p>
<dd> Sets the matte color to be used in full-screen mode. The default setting is &quot;black&quot;.</dl>
<h2>CONTROLS</h2>
<h3>On-screen controls, at the bottom of the xpdf window</h3>
<dl>
<dt><code>left/right arrow buttons</code></p>
<dd> Move to the previous/next page.</p>
<dt><code>double left/right arrow buttons</code></p>
<dd> Move backward or forward by ten pages.</p>
<dt><code>dashed left/right arrow buttons</code></p>
<dd> Move backward or forward along the history path.</p>
<dt><code>&#8216;Page&#8217; entry box</code></p>
<dd> Move to a specific page number. Click in the box to activate it, type the page number, then hit return.</p>
<dt><code>zoom popup menu</code></p>
<dd> Change the zoom factor (see the description of the -z option above).</p>
<dt><code>binoculars button</code></p>
<dd> Find a text string.</p>
<dt><code>print button</code></p>
<dd> Bring up a dialog for generating a PostScript file. The dialog has options to set the pages to be printed and the PostScript file name. The file name can be &#8216;-&#8216; for stdout or &#8216;|command&#8217; to pipe the PostScript through a command, e.g., &#8216;|lpr&#8217;.</p>
<dt><code>&#8216;?&#8217; button</code></p>
<dd> Bring up the &#8216;about xpdf&#8217; window.</p>
<dt><code>link info</code></p>
<dd> The space between the &#8216;?&#8217; and &#8216;Quit&#8217; buttons is used to show the URL or external file name when the mouse is over a link.</p>
<dt><code>&#8216;Quit&#8217; button</code></p>
<dd> Quit xpdf.</dl>
<h3>Menu</h3>
<p> Pressing the right mouse button will post a popup menu with the following commands:</p>
<dl>
<dt><code>Open&#8230;</code></p>
<dd> Open a new PDF file via a file requester.</p>
<dt><code>Open in new window&#8230;</code></p>
<dd> Create a new window and open a new PDF file via a file requester.</p>
<dt><code>Reload</code></p>
<dd> Reload the current PDF file. Note that Xpdf will reload the file automatically (on a page change or redraw) if it has changed since it was last loaded.</p>
<dt><code>Save as&#8230;</code></p>
<dd> Save the current file via a file requester.</p>
<dt><code>Continuous view</code></p>
<dd> Toggles between single page and continuous view modes.</p>
<dt><code>Rotate counterclockwise</code></p>
<dd> Rotate the page 90 degrees counterclockwise.</p>
<dt><code>Rotate clockwise</code></p>
<dd> Rotate the page 90 degrees clockwise. The two rotate commands are intended primarily for PDF files where the rotation isn&#8217;t correctly specified in the file.</p>
<dt><code>Zoom to selection</code></p>
<dd> Zoom in to the currently selected rectangle.</p>
<dt><code>Close</code></p>
<dd> Close the current window. If this is the only open window, the document is closed, but the window is left open (i.e., this menu command won&#8217;t quit xpdf).</p>
<dt><code>Quit</code></p>
<dd> Quit xpdf.</dl>
<h3>Outline</h3>
<p> If the PDF contains an outline (a.k.a., bookmarks), there will be an outline pane on the left side of the window. The width of the outline pane is adjustable with a vertical split bar via the knob near its bottom end. </p>
<h3>Text selection</h3>
<p> Dragging the mouse with the left button held down will highlight an arbitrary rectangle. Any text inside this rectangle will be copied to the X selection buffer. </p>
<h3>Links</h3>
<p> Clicking on a hyperlink will jump to the link&#8217;s destination. A link to another PDF document will make xpdf load that document. A &#8216;launch&#8217; link to an executable program will display a dialog, and if you click &#8216;ok&#8217;, execute the program. URL links call an external command (see the <code>WEB BROWSERS</code> section below). </p>
<h3>Panning</h3>
<p> Dragging the mouse with the middle button held down pans the window. </p>
<h3>Key bindings</h3>
<dl>
<dt><code>o</code></p>
<dd> Open a new PDF file via a file requester.</p>
<dt><code>r</code></p>
<dd> Reload the current PDF file. Note that Xpdf will reload the file automatically (on a page change or redraw) if it has changed since it was last loaded.</p>
<dt><code>control-L</code></p>
<dd> Redraw the current page.</p>
<dt><code>control-W</code></p>
<dd> Close the current window.</p>
<dt><code>f or control-F</code></p>
<dd> Find a text string.</p>
<dt><code>control-G</code></p>
<dd> Find next occurrence.</p>
<dt><code>control-P</code></p>
<dd> Print.</p>
<dt><code>n</code></p>
<dd> Move to the next page. Scrolls to the top of the page, unless scroll lock is turned on.</p>
<dt><code>p</code></p>
<dd> Move to the previous page. Scrolls to the top of the page, unless scroll lock is turned on.</p>
<dt><code>&lt;Space&gt;</code> or <code>&lt;PageDown&gt;</code> or <code>&lt;Next&gt;</code></p>
<dd> Scroll down on the current page; if already at bottom, move to next page.</p>
<dt><code>&lt;Backspace&gt;</code> or <code>&lt;Delete&gt;</code> or <code>&lt;PageUp&gt;</code> or <code>&lt;Previous&gt;</code></p>
<dd> Scroll up on the current page; if already at top, move to previous page.</p>
<dt><code>v</code></p>
<dd> Move forward along the history path.</p>
<dt><code>b</code></p>
<dd> Move backward along the history path.</p>
<dt><code>&lt;Home&gt;</code></p>
<dd> Scroll to top of current page.</p>
<dt><code>&lt;End&gt;</code></p>
<dd> Scroll to bottom of current page.</p>
<dt><code>control-&lt;Home&gt;</code></p>
<dd> Scroll to first page of document.</p>
<dt><code>control-&lt;End&gt;</code></p>
<dd> Scroll to last page of document.</p>
<dt><code>arrows</code></p>
<dd> Scroll the current page.</p>
<dt><code>g</code></p>
<dd> Activate the page number text field (&quot;goto page&quot;).</p>
<dt><code>0</code></p>
<dd> Set the zoom factor to 125%.</p>
<dt><code>+</code></p>
<dd> Zoom in (increment the zoom factor by 1).</p>
<dt><code>&#8211;</code></p>
<dd> Zoom out (decrement the zoom factor by 1).</p>
<dt><code>z</code></p>
<dd> Set the zoom factor to &#8216;page&#8217; (fit page to window).</p>
<dt><code>w</code></p>
<dd> Set the zoom factor to &#8216;width&#8217; (fit page width to window).</p>
<dt><code>alt-F</code></p>
<dd> Toggle full-screen mode.</p>
<dt><code>q</code></p>
<dd> Quit xpdf.</dl>
<h2>WEB BROWSERS</h2>
<p> If you want to run xpdf automatically from netscape or mosaic (and probably other browsers) when you click on a link to a PDF file, you need to edit (or create) the files <i>.mime.types</i> and <i>.mailcap</i> in your home directory. In <i>.mime.types</i> add the line: </p>
<dl>
<dt>
<dd> application/pdf pdf</dl>
<p> In <i>.mailcap</i> add the lines: </p>
<dl>
<dt>
<dd> # Use xpdf to view PDF files.</dl>
<dl>
<dt>
<dd> application/pdf; xpdf -q %s</dl>
<p> Make sure that xpdf is on your executable search path. </p>
<p> When you click on a URL link in a PDF file, xpdf will execute the command specified by the urlCommand config file option, replacing an occurrence of &#8216;%s&#8217; with the URL. For example, to call netscape with the URL, add this line to your config file: </p>
<dl>
<dt>
<dd> urlCommand &quot;netscape -remote &#8216;openURL(%s)&#8217;&quot;</dl>
<h2>COMMANDS</h2>
<p> Xpdf&#8217;s key and mouse bindings are user-configurable, using the bind and unbind options in the config file (see <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5)). The bind command allows you to bind a key or mouse button to a sequence of one or more commands.</p>
<h3>Available Commands</h3>
<p> The following commands are supported:</p>
<dl>
<dt><code>gotoPage(</code><i>page</i><code>)</code></p>
<dd> Go to the specified page.</p>
<dt><code>gotoPageNoScroll(</code><i>page</i><code>)</code></p>
<dd> Go to the specified page, with the current relative scroll position.</p>
<dt><code>gotoDest(</code><i>dest</i><code>)</code></p>
<dd> Go to a named destination.</p>
<dt><code>gotoLastPage</code></p>
<dd> Go to the last page in the PDF file.</p>
<dt><code>gotoLastPageNoScroll</code></p>
<dd> Go to the last page in the PDF file, with the current relative scroll position.</p>
<dt><code>nextPage</code></p>
<dd> Go to the next page.</p>
<dt><code>nextPageNoScroll</code></p>
<dd> Go to the next page, with the current relative scroll position.</p>
<dt><code>prevPage</code></p>
<dd> Go to the previous page.</p>
<dt><code>prevPageNoScroll</code></p>
<dd> Go to the previous page, with the current relative scroll position.</p>
<dt><code>pageUp</code></p>
<dd> Scroll up by one screenful.</p>
<dt><code>pageDown</code></p>
<dd> Scroll down by one screenful.</p>
<dt><code>scrollLeft(</code><i>n</i><code>)</code></p>
<dd> Scroll left by <i>n</i> pixels.</p>
<dt><code>scrollRight(</code><i>n</i><code>)</code></p>
<dd> Scroll right by <i>n</i> pixels.</p>
<dt><code>scrollUp(</code><i>n</i><code>)</code></p>
<dd> Scroll up by <i>n</i> pixels.</p>
<dt><code>scrollDown(</code><i>n</i><code>)</code></p>
<dd> Scroll down by <i>n</i> pixels.</p>
<dt><code>scrollUpPrevPage(</code><i>n</i><code>)</code></p>
<dd> Scroll up by <i>n</i> pixels, moving to the previous page if appropriate.</p>
<dt><code>scrollDownPrevPage(</code><i>n</i><code>)</code></p>
<dd> Scroll down by <i>n</i> pixels, moving to the next page if appropriate.</p>
<dt><code>scrollToTopEdge</code></p>
<dd> Scroll to the top edge of the current page, with no horizontal movement.</p>
<dt><code>scrollToBottomEdge</code></p>
<dd> Scroll to the bottom edge of the current page, with no horizontal movement.</p>
<dt><code>scrollToLeftEdge</code></p>
<dd> Scroll to the left edge of the current page, with no vertical movement.</p>
<dt><code>scrollToRightEdge</code></p>
<dd> Scroll to the right edge of the current page, with no vertical movement.</p>
<dt><code>scrollToTopLeft</code></p>
<dd> Scroll to the top-left corner of the current page.</p>
<dt><code>scrollToBottomRight</code></p>
<dd> Scroll to the bottom-right corner of the current page.</p>
<dt><code>goForward</code></p>
<dd> Move forward along the history path.</p>
<dt><code>goBackward</code></p>
<dd> Move backward along the history path.</p>
<dt><code>zoomPercent(</code><i>z</i><code>)</code></p>
<dd> Set the zoom factor to <i>z</i>%.</p>
<dt><code>zoomFitPage</code></p>
<dd> Set the zoom factor to fit-page.</p>
<dt><code>zoomFitWidth</code></p>
<dd> Set the zoom factor to fit-width.</p>
<dt><code>zoomIn</code></p>
<dd> Zoom in &#8211; go to the next higher zoom factor.</p>
<dt><code>zoomOut</code></p>
<dd> Zoom out &#8211; go the next lower zoom factor.</p>
<dt><code>rotateCW</code></p>
<dd> Rotate the page 90 degrees clockwise.</p>
<dt><code>rotateCCW</code></p>
<dd> Rotate the page 90 degrees counterclockwise.</p>
<dt><code>setSelection(</code><i>pg</i><code>,</code><i>ulx</i><code>,</code><i>uly</i><code>,</code><i>lrx</i><code>,</code><i>lry</i><code>)</code></p>
<dd> Set the selection to the specified coordinates on the specified page.</p>
<dt><code>continuousMode</code></p>
<dd> Go to continuous view mode.</p>
<dt><code>singlePageMode</code></p>
<dd> Go to single-page view mode.</p>
<dt><code>toggleContinuousMode</code></p>
<dd> Toggle between continuous and single page view modes.</p>
<dt><code>fullScreenMode</code></p>
<dd> Go to full-screen mode.</p>
<dt><code>windowMode</code></p>
<dd> Go to window (non-full-screen) mode.</p>
<dt><code>toggleFullScreenMode</code></p>
<dd> Toggle between full-screen and window modes.</p>
<dt><code>open</code></p>
<dd> Open a PDF file in this window, using the open dialog.</p>
<dt><code>openInNewWin</code></p>
<dd> Open a PDF file in a new window, using the open dialog.</p>
<dt><code>openFile(</code><i>file</i><code>)</code></p>
<dd> Open a specified PDF file in this window.</p>
<dt><code>openFileInNewWin(</code><i>file</i><code>)</code></p>
<dd> Open a specified PDF file in a new window.</p>
<dt><code>openFileAtDest(</code><i>file</i><code>,</code><i>dest</i><code>)</code></p>
<dd> Open a specified PDF file in this window and go to a named destination.</p>
<dt><code>openFileAtDestInNewWin(</code><i>file</i><code>,</code><i>dest</i><code>)</code></p>
<dd> Open a specified PDF file in a new window and go to a named destination.</p>
<dt><code>reload</code></p>
<dd> Reload the current PDF file.</p>
<dt><code>redraw</code></p>
<dd> Redraw the window.</p>
<dt><code>raise</code></p>
<dd> Raise the window to the front.</p>
<dt><code>closeWindow</code></p>
<dd> Close the window. If this was the last open window, clear the window, but don&#8217;t quit from Xpdf.</p>
<dt><code>closeWindowOrQuit</code></p>
<dd> Close the window. If this was the last open window, quit from Xpdf.</p>
<dt><code>run(</code><i>external-command-string</i><code>)</code></p>
<dd> Run an external command. The following escapes are allowed in the command string: </p>
<pre><code>
% f = &gt; PDF file name(or an empty string if no
                             file is open) %
            b = &gt; PDF file base name,
  i.e., file name minus the extension(or an empty string if no file is open) % u = &gt; link URL(or an empty string if not over a URL link) % p = &gt; current page number(or an empty string if no file is open) % x = &gt; selection upper - left x coordinate(or 0 if there is no selection) % y = &gt; selection upper - left y coordinate(or 0 if there is no selection) % X = &gt; selection lower - right x coordinate(or 0 if there is no selection) % Y = &gt; selection lower - right y coordinate(or 0 if there is no selection) % i = &gt; page containing the mouse pointer % j = &gt; x coordinate of the mouse pointer % k = &gt; y coordinate of the mouse pointer % % = &gt; %
</code></pre>
<p> The external command string will often contain spaces, so the whole command must be quoted in the xpdfrc file: </p>
<pre>
    bind x &quot;run(ls -l)&quot;
</pre>
<dt><code>openOutline</code></p>
<dd> Open the outline pane.</p>
<dt><code>closeOutline</code></p>
<dd> Close the outline pane.</p>
<dt><code>toggleOutline</code></p>
<dd> Toggle the outline pane between open and closed.</p>
<dt><code>scrollOutlineDown(</code><i>n</i><code>)</code></p>
<dd> Scroll the outline down by <i>n</i> increments.</p>
<dt><code>scrollOutlineUp(</code><i>n</i><code>)</code></p>
<dd> Scroll the outline up by <i>n</i> increments.</p>
<dt><code>focusToDocWin</code></p>
<dd> Set the keyboard focus to the main document window.</p>
<dt><code>focusToPageNum</code></p>
<dd> Set the keyboard focus to the page number text box.</p>
<dt><code>find</code></p>
<dd> Open the &#8216;find&#8217; dialog.</p>
<dt><code>findNext</code></p>
<dd> Finds the next occurrence of the search string (no dialog).</p>
<dt><code>print</code></p>
<dd> Open the &#8216;print&#8217; dialog.</p>
<dt><code>about</code></p>
<dd> Open the &#8216;about&#8217; dialog.</p>
<dt><code>quit</code></p>
<dd> Quit from xpdf.</dl>
<p> The following commands depend on the current mouse position:</p>
<dl>
<dt><code>startSelection</code></p>
<dd> Start a selection, which will be extended as the mouse moves.</p>
<dt><code>endSelection</code></p>
<dd> End a selection.</p>
<dt><code>startPan</code></p>
<dd> Start a pan, which will scroll the document as the mouse moves</p>
<dt><code>endPan</code></p>
<dd> End a pan.</p>
<dt><code>postPopupMenu</code></p>
<dd> Display the popup menu.</p>
<dt><code>followLink</code></p>
<dd> Follow a hyperlink (does nothing if the mouse is not over a link).</p>
<dt><code>followLinkInNewWin</code></p>
<dd> Follow a hyperlink, opening PDF files in a new window (does nothing if the mouse is not over a link). For links to non-PDF files, this command is identical to followLink.</p>
<dt><code>followLinkNoSel</code></p>
<dd> Same as followLink, but does nothing if there is a non-empty selection. (This is useful as a mouse button binding.)</p>
<dt><code>followLinkInNewWinNoSel</code></p>
<dd> Same as followLinkInNewWin, but does nothing if there is a non-empty selection. (This is useful as a mouse button binding.)</dl>
<h3>Default Bindings</h3>
<p> The default mouse bindings are as follows: </p>
<pre>
    bind mousePress1    any         startSelection
    bind mouseRelease1  any         endSelection followLinkNoSel
    bind mousePress2    any         startPan
    bind mouseRelease2  any         endPan
    bind mousePress3    any         postPopupMenu
    bind mousePress4    any         scrollUpPrevPage(16)
    bind mousePress5    any         scrollDownNextPage(16)
    bind mousePress6    any         scrollLeft(16)
    bind mousePress7    any         scrollRight(16)
</pre>
<p> The default key bindings are as follows: </p>
<pre>
    bind ctrl-home      any         <a href="//www.systutorials.com/docs/linux/man/1-gotoPage/">gotoPage</a>(1)
    bind home           any         scrollToTopLeft
    bind ctrl-end       any         gotoLastPage
    bind end            any         scrollToBottomRight
    bind pgup           any         pageUp
    bind backspace      any         pageUp
    bind delete         any         pageUp
    bind pgdn           any         pageDown
    bind space          any         pageDown
    bind left           any         scrollLeft(16)
    bind right          any         scrollRight(16)
    bind up             any         scrollUp(16)
    bind down           any         scrollDown(16)
    bind o              any         open
    bind O              any         open
    bind r              any         reload
    bind R              any         reload
    bind f              any         find
    bind F              any         find
    bind ctrl-f         any         find
    bind ctrl-g         any         findNext
    bind ctrl-p         any         print
    bind n              scrLockOff  nextPage
    bind N              scrLockOff  nextPage
    bind n              scrLockOn   nextPageNoScroll
    bind N              scrLockOn   nextPageNoScroll
    bind p              scrLockOff  prevPage
    bind P              scrLockOff  prevPage
    bind p              scrLockOn   prevPageNoScroll
    bind P              scrLockOn   prevPageNoScroll
    bind v              any         goForward
    bind b              any         goBackward
    bind g              any         focusToPageNum
    bind 0              any         zoomPercent(125)
    bind +              any         zoomIn
    bind -              any         zoomOut
    bind z              any         zoomFitPage
    bind w              any         zoomFitWidth
    bind alt-f          any         toggleFullScreenMode
    bind ctrl-l         any         redraw
    bind ctrl-w         any         closeWindowOrQuit
    bind ?              any         about
    bind q              any         quit
    bind Q              any         quit
</pre>
<p> Previous versions of xpdf included a &quot;viKeys&quot; X resource. It is no longer available, but the following bindings are equivalent: </p>
<pre>
    bind h any scrollLeft(16)
    bind l any scrollRight(16)
    bind k any scrollUp(16)
    bind j any scrollDown(16)
</pre>
<h2>REMOTE SERVER MODE</h2>
<p> Xpdf can be started in remote server mode by specifying a server name (in addition to the file name and page number). For example: </p>
<dl>
<dt>
<dd> xpdf -remote myServer file.pdf</dl>
<p> If there is currently no xpdf running in server mode with the name &#8216;myServer&#8217;, a new xpdf window will be opened. If another command: </p>
<dl>
<dt>
<dd> xpdf -remote myServer another.pdf 9</dl>
<p> is issued, a new copy of xpdf will not be started. Instead, the first xpdf (the server) will load <i>another.pdf</i> and display page nine. If the file name is the same: </p>
<dl>
<dt>
<dd> xpdf -remote myServer another.pdf 4</dl>
<p> the xpdf server will simply display the specified page. </p>
<p> The -raise option tells the server to raise its window; it can be specified with or without a file name and page number. </p>
<p> The -quit option tells the server to close its window and exit.</p>
<h2>EXIT CODES</h2>
<p> The Xpdf tools use the following exit codes:</p>
<dl>
<dt>0</p>
<dd> No error.</p>
<dt>1</p>
<dd> Error opening a PDF file.</p>
<dt>2</p>
<dd> Error opening an output file.</p>
<dt>3</p>
<dd> Error related to PDF permissions.</p>
<dt>99</p>
<dd> Other error.</dl>
<h2>AUTHOR</h2>
<p> The xpdf software and documentation are copyright 1996-2014 Glyph &amp; Cog, LLC.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pdftops/">pdftops</a></code>(1), <code><a href="/docs/linux/man/1-pdftotext/">pdftotext</a></code>(1), <code><a href="/docs/linux/man/1-pdftohtml/">pdftohtml</a></code>(1), <code><a href="/docs/linux/man/1-pdfinfo/">pdfinfo</a></code>(1), <code><a href="/docs/linux/man/1-pdffonts/">pdffonts</a></code>(1), <code><a href="/docs/linux/man/1-pdfdetach/">pdfdetach</a></code>(1), <code><a href="/docs/linux/man/1-pdftoppm/">pdftoppm</a></code>(1), <code><a href="/docs/linux/man/1-pdftopng/">pdftopng</a></code>(1), <code><a href="/docs/linux/man/1-pdfimages/">pdfimages</a></code>(1), <code><a href="/docs/linux/man/5-xpdfrc/">xpdfrc</a></code>(5)<br />
 <code><a rel="nofollow" href="http://www.foolabs.com/xpdf/">http://www.foolabs.com/xpdf/</a></code> </p>
<h2>Index</h2>
