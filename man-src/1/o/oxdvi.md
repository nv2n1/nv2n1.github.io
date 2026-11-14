---
title: "oxdvi(1)"
name: "oxdvi"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oxdvi/"
description: "xdvi – DVI Previewer for the X Window System"
---

<h2 class="name">NAME</h2>
<p> xdvi &#8211; DVI Previewer for the X Window System </p>
<h2>SYNOPSIS</h2>
<p> <code>xdvi</code> [<code>+</code>[<i>page</i>]] [<code>&#8211;help</code>] [<code>-allowshell</code>] [<code>-altfont</code> <i>font</i>] [<code>-bg</code> <i>color</i>] [<code>-browser</code> <i>WWWbrowser</i>] [<code>-copy</code>] [<code>-cr</code> <i>color</i>] [<code>-debug</code> <i>bitmask</i>|<i>string[,string &#8230;]</i>] [<code>-display</code> <i>host:display</i>] [<code>-dvipspath</code> <i>path</i>] [<code>-editor</code> <i>command</i>] [<code>-expert</code>] [<code>-expertmode</code> <i>flag</i>] [<code>-fg</code> <i>color</i>] [<code>-findstring</code> <i>string</i>] [<code>-text-encoding</code> <i>encoding</i>] [<code>-font</code> <i>font</i>] [<code>-fullscreen </code>] [<code>-gamma</code> <i>g</i>] [<code>-geometry</code> <i>geometry</i>] [<code>-gsalpha</code>] [<code>-gspalette</code> <i>palette</i>] [<code>-h</code>] [<code>-help</code>] [<code>-hl</code> <i>color</i>] [<code>-anchorposition</code> <i>anchor</i>] [<code>-hush</code>] [<code>-hushchars</code>] [<code>-hushchecksums</code>] [<code>-warnpecials</code>] [<code>-hushstdout</code>] [<code>-hushbell</code>] [<code>-icongeometry</code> <i>geometry</i>] [<code>-iconic</code>] [<code>-install</code>] [<code>-interpreter</code> <i>path</i>] [<code>-keep</code>] [<code>-l</code>] [<code>-license</code>] [<code>-linkcolor</code> <i>color</i>] [<code>-linkstyle</code> <i>0|1|2|3</i>] [<code>-margins</code> <i>dimen</i>] [<code>-mfmode</code> <i>mode-def</i>[<code>:</code><i>dpi</i>]] [<code>-mgs</code>[<i>n</i>] <i>size</i>] [<code>-mousemode</code> <i>0|1|2</i>] [<code>-nocolor</code>] [<code>-nofork</code>] [<code>-noghostscript</code>] [<code>-nogrey</code>] [<code>-nogssafer</code>] [<code>-noinstall</code>] [<code>-nomakepk</code>] [<code>-nomatchinverted</code>] [<code>-noomega</code>] [<code>-noscan</code>] [<code>-not1lib</code>] [<code>-notempfile</code>] [<code>-offsets</code> <i>dimen</i>] [<code>-p</code> <i>pixels</i>] [<code>-paper</code> <i>papertype</i>] [<code>-pause</code>] [<code>-pausespecial</code> <i>special-string</i>] [<code>-postscript</code> <i>flag</i>] [<code>-rulecolor</code> <i>color</i>] [<code>-rv</code>] [<code>-S</code> <i>density</i>] [<code>-s</code> <i>shrink</i>] [<code>-safer</code>] [<code>-sidemargin</code> <i>dimen</i>] [<code>-sourceposition</code> <i>line</i>[<code>:</code><i>col</i>][&nbsp;<wbr>]<i>filename</i>] [<code>-statusline</code>] [<code>-thorough</code>] [<code>-topmargin</code> <i>dimen</i>] [<code>-unique</code>] [<code>-version</code>] [<code>-visitedlinkcolor</code> <i>color</i>] [<code>-warnspecials</code>] [<code>-watchfile</code> <i>secs</i>] [<code>-wheelunit</code> <i>pixels</i>] [<code>-xoffset</code> <i>dimen</i>] [<code>-yoffset</code> <i>dimen</i>] [<i>dvi_file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>Xdvi</code> is a program for previewing <i>dvi</i> files, as produced e.g. by the <code><a href="/docs/linux/man/1-tex/">tex</a></code>(1) program, under the X window system. </p>
<p> <code>Xdvi</code> can show the file shrunken by various integer factors, and it has a &#8220;magnifying glass&#8221; for viewing parts of the page enlarged (see the section MAGNIFIER below). This version of <code>xdvi</code> is also referred to as <code>xdvik</code> since it uses the kpathsea library to locate and generate font files. In addition to that, it supports the following features:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&#8211;</p>
<dd> hyperlinks in DVI files (section HYPERLINKS),</p>
<dt>&#8211;</p>
<dd> direct rendering of Postscript&lt;tm&gt; Type1 fonts (section T1LIB),</p>
<dt>&#8211;</p>
<dd> source specials in the DVI file (section SOURCE SPECIALS),</p>
<dt>&#8211;</p>
<dd> string search in DVI files (section STRING SEARCH),</p>
<dt>&#8211;</p>
<dd> saving or printing (parts of) the DVI file (sections PRINT DIALOG and SAVE DIALOG).</dl>
</dl>
<p> Xdvi can be compiled with the Motif toolkit or the Xaw (Athena) toolkit (and variants of it), and the Motif version has a slightly different GUI; these differences are noted below. </p>
<p> Before displaying a page of a DVI file, <code>xdvi</code> will check to see if the file has changed since the last time it was displayed. If this is the case, it will reload the file. This feature allows you to preview many versions of the same file while running <code>xdvi</code> only once. Since it cannot read partial DVI files, <code>xdvik</code> versions starting from 22.74.3 will create a temporary copy of the DVI file being viewed, to ensure that the file can be viewed without interruptions. (The <code>-notempfile</code> can be used to turn off this feature). </p>
<p> <code>Xdvi</code> can show PostScript&lt;tm&gt; specials by any of three methods. It will try first to use Display PostScript&lt;tm&gt;, then NeWS, then it will try to use Ghostscript to render the images. All of these options depend on additional software to work properly; moreover, some of them may not be compiled into this copy of <code>xdvi</code>. </p>
<p> For performance reasons, <code>xdvi</code> does not render PostScript specials in the magnifying glass. </p>
<p> If no file name has been specified on the command line, xdvi will try to open the most recently opened file; if the file history (accessible via the <code>File &gt; Open Recent</code> menu) is empty, or if none of the files in the history are valid DVI files, it will pop up a file selector for choosing a file name. (In previous versions, which didn&#8217;t have a file history, the file selector was always used; you can set the X resource <code>noFileArgUseHistory</code> to <i>false</i> to get back the old behaviour.) </p>
<h2>OPTIONS</h2>
<p> In addition to specifying the <i>dvi</i> file (with or without the <code>.dvi</code> extension), <code>xdvi</code> supports the following command line options. If the option begins with a `<code>+</code>&#8216; instead of a `<code>&#8211;</code>&#8216;, the option is restored to its default value. By default, these options can be set via the resource names given in parentheses in the description of each option.</p>
<dl>
<dt><code>+</code><i>page</i></p>
<dd> Specifies the first page to show. If <code>+</code> is given without a number, the last page is assumed; the first page is the default.</p>
<dt><code>-allowshell</code></p>
<dd> (<code>.allowShell</code>) This option enables the shell escape in PostScript specials. (For security reasons, shell escapes are disabled by default.) This option should be rarely used; in particular it should not be used just to uncompress files: that function is done automatically if the file name ends in <code>.Z</code>, <code>.gz</code>, or <code>.bz2</code>. Shell escapes are always turned off if the <code>-safer</code> option is used.</p>
<dt><code>-altfont</code><i> font</i></p>
<dd> (<code>.altFont</code>) Declares a default font to use when the font in the <i>dvi</i> file cannot be found. This is useful, for example, with PostScript &lt;tm&gt; fonts.</p>
<dt><code>-background</code><i> color</i></p>
<dd> (<code>.background</code>) Determines the color of the background. Same as <code>-bg</code>.</p>
<dt><code>-bg</code><i> color</i></p>
<dd> (<code>.background</code>) Determines the color of the background.</p>
<dt><code>-browser</code><i> browser</i></p>
<dd> (<code>.wwwBrowser</code>) Defines the web browser used for handling external URLs. The value of this option or resource has the same syntax as the <code>BROWSER</code> environment variable; see the explanation of that variable in the section `ENVIRONMENT&#8217; below for a detailed description. If neither the option nor the X resource <i>wwwBrowser</i> is specified, the environment variables <code>BROWSER</code> and <code>WWWBROWSER</code> (in that order) are used to determine the browser command. If these are not set either, the following default value is used: <code>xdg-open %s:htmlview %s:firefox -remote -remote &quot;openURL(%s,new-window)&quot;:mozilla -remote &quot;openURL(%s,new-window)&quot;:netscape -raise -remote &quot;openURL(%s,new-window)&quot;:xterm -e w3m %s:xterm -e lynx %s:xterm -e wget %s</code></p>
<dt><code>-copy</code></p>
<dd> (<code>.copy</code>) Always use the <i>copy</i> operation when writing characters to the display. This option may be necessary for correct operation on a color display, but overstrike characters will be incorrect. If greyscale anti-aliasing is in use, the <code>-copy</code> operation will disable the use of colorplanes and make overstrikes come out incorrectly. See also <code>-thorough</code>.</p>
<dt><code>-cr</code><i> color</i></p>
<dd> (<code>.cursorColor</code>) Determines the color of the mouse cursor. The default is the same as the foreground color.</p>
<dt><code>-debug</code><i> bitmask|string[,string &#8230;]</i></p>
<dd> (<code>.debugLevel</code>) If nonzero, prints additional information on standard output. The argument can be either a bitmask specified as a decimal number, or comma-separated list of strings.<br />
 For the bitmask representation, multiple values can be specified by adding the numbers that represent the individual bits; e.g. to debug all all file searching and opening commands, use 4032 (= 2048 + 1024 + 512 + 256 + 128 + 64). Use -1 to turn on debugging of everything (this will produce huge output).<br />
 For the string representation, use the strings listed in the following table, with a comma to separate the values; e.g. to debug all file searching and opening commands, use <code>search,expand,paths,hash,stat,open</code>. (The option `kpathsea&#8217; is provided as a shorthand for these.) Note that such a list may need to be quoted to prevent the shell from interpreting commas or spaces in the list.<br />
 The individual numbers and strings have the following meanings: </p>
<pre>
 1       bitmap      Bitmap creation
 2       dvi         DVI translation
 4       pk          PK fonts
 8       batch       Batch mode: Exit after
                     reading the DVI file
 16      event       Event handling
 32      ps          PostScript interpreter calls
 64      stat        Kpathsea <a href="//www.systutorials.com/docs/linux/man/2-stat/">stat</a>(2) calls
 128     hash        Kpathsea hash table lookups
 256     open        Kpathsea file opening
 512     paths       Kpathsea path definitions
 1024    expand      Kpathsea path expansion
 2048    search      Kpathsea searching
 4032    kpathsea    All Kpathsea options 
 4096    htex        Hypertex specials
 8192    src         Source specials       
 16384   client      Client/server mode (see -unique
                     and -sourceposition options)
 32768   t1          Type1 font library messages       
 65536   t1_verbose  Verbose Type1 library messages   
 131072  gui         GUI elements
</pre>
<p> Some of the Kpathsea debugging options are actually provided by Kpathsea; see the Debugging section in the Kpathsea manual for more information on these.</p>
<dt><code>-density</code><i> density</i></p>
<dd> (<code>.densityPercent</code>) Determines the density used when shrinking bitmaps for fonts. A higher value produces a lighter font. The default value is 40. If greyscaling is in use, this argument does not apply; use <code>-gamma</code> instead. See also the `<code>S</code>&#8216; keystroke. Same as <code>-S</code>.</p>
<dt><code>-display</code><i> host</i><code>:</code><i>display</i></p>
<dd> Specifies the host and screen to be used for displaying the <i>dvi</i> file. By default this is obtained from the environment variable <font SIZE="-1"><code>DISPLAY.</code></font></p>
<dt><code>-dvipspath</code><i> path</i></p>
<dd> (<code>.dvipsPath</code>) Use <i>path</i> as the <code>dvips</code> program to use when printing. The default for this is <code>dvips</code>. The program or script should read the DVI file from standard input, and write the Postscript file to standard output.</p>
<dt><code>-editor</code><i> editor</i></p>
<dd> (<code>.editor</code>) Specifies the editor that will be invoked when the <i>source-special()</i> action is triggered to start a reverse search (by default via Ctrl-Mouse 1). The argument to this option is a format string in which occurrences of &#8220;<code>%f</code>&#8221; are replaced by the file name, occurrences of &#8220;<code>%l</code>&#8221; are replaced by the line number within the file, and optional occurrences of &#8220;<code>%c</code>&#8221; are replaced by the column number within the line. </p>
<p> If neither the option nor the X resource <i>.editor</i> is specified, the following environment variables are checked to determine the editor command: <code>XEDITOR</code>, <code>VISUAL</code>, and <code>EDITOR </code> (in this sequence). If the string is found as the value of the <font SIZE="-1"><code>VISUAL</code></font> or <font SIZE="-1"><code>EDITOR</code></font> environment variables, then &#8220;<i>xterm -e &#8221;</i> is prepended to the string; if the editor is specified by other means, then it must be in the form of a shell command to pop up an X window with an editor in it. If none of these variables is set, a warning message is displayed and the command &#8220;<i>xterm -e vi +%l %f&#8221;</i> is used. </p>
<p> If no &#8220;<code>%f</code>&#8221; or &#8220;<code>%l</code>&#8221; occurs in the string, the missing format strings are appended automatically. (This is for compatibility with other programs when using one of the environment variables). </p>
<p> A new instance of the editor is started each time this command is used; therefore it is preferable to use an editor that can be invoked in `client&#8217; mode to load new files into the same instance. Example settings are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><font SIZE="-1"><code>emacsclient &#8211;no-wait</code></font></p>
<dd> (older Emacsen)</p>
<dt><font SIZE="-1"><code>gnuclient -q</code></font></p>
<dd> (XEmacs and newer Emacsen)</p>
<dt><font SIZE="-1"><code>gvim &#8211;servername xdvi &#8211;remote</code></font></p>
<dd> (VIM v6.0+; the `&#8211;servername xdvi&#8217; option will cause gvim to run a dedicated instance for the files opened by xdvi.)</p>
<dt><font SIZE="-1"><code>nc</code></font></p>
<dd> (nedit)</dl>
<p> Note that those strings need to be enclosed into quotes when using them on the command-line to protect them from the shell; when using them as argument for the <i>.editor</i> resource in an X resource file, no quotes should be used. </p>
<p> <code>NOTE ON SECURITY:</code> The argument of this option isn&#8217;t executed as a shell command, but via <i>exec()</i> to prevent evil tricks with the contents of source specials.</dl>
<dt><code>-expert</code></p>
<dd> This option is only supported for backwards compatibility; it is equivalent to <code>-expertmode 0</code>, which should be preferred.</p>
<dt><code>-expertmode</code><i> flag</i></p>
<dd> (<code>.expertMode</code>) With an argument of <i>0</i>, this option switches off the display of the buttons, scrollbars, the toolbar (Motif only), the statusline and the page list. These GUI elements can also be (de)activated separately, by combining the appropriate values in the <i>flag</i> argument. This acts similar to the <code>-debug</code> option: The integer <i>flag</i> is treated as a bitmap where each bit represents one element. If the bit has the value <i>1</i>, the element is switched on, if it has the value <i>0</i>, the element is switched off. The meaning of the bits is as follows: </p>
<pre>
 1       statusline
 2       scrollbars
 4       Motif: pagelist, Xaw: buttons and pagelist
 8       toolbar (Motif only)
 16      menubar (Motif only)
</pre>
<p> For example, to turn on only the statusline and the scrollbars, use 3 (= 1 + 2). See also the `<code>x</code>&#8216; keystroke, where the bits are addressed by their positions, from 1 to 3 (Xaw) or 5 (Motif), respectively.</dl>
<p> If the statusline is not active, all messages that would normally be printed to the statusline will be printed to <i>stdout</i>, unless the <code>-hushstdout</code> option is used.</p>
<dl>
<dt><code>-fg</code><i> color</i></p>
<dd> (<code>.foreground</code>) Determines the color of the text (foreground).</p>
<dt><code>-text-encoding</code><i> encoding</i></p>
<dd> (<code>.textEncoding</code>) Use <i>encoding</i> as text encoding of the string in the &quot;Find&quot; window. Usually, this shouldn&#8217;t be needed since the encoding is determined from the locale settings.</p>
<dt><code>-findstring</code> <i>string</i></p>
<dd> This option triggers a search for <i>string</i> in the DVI file mentioned on the command-line, similar to forward search (see the description of the <code>sourceposition</code> option): If there is already another instance of <code>xdvi</code> running on the displaying that DVI file, it will cause that instance to perform the search instead. The search starts at the top of the current page of the DVI file.</p>
<dt><code>-font</code><i> font</i></p>
<dd> (<code>*font</code>) Sets the font used in menus, buttons etc., as described in the <i><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a>(7x)</i> man page. The font for child windows can be set separately, e.g.:</p>
<dl>
<dt>
<dd>
<pre>
<code>xdvi*statusline*font: \
   -*-helvetica-medium-r-*-*-12-*-*-*-*-*-*-*
</code></pre>
</dl>
<dt><code>-foreground</code><i> color</i></p>
<dd> Same as <code>-fg</code>.</p>
<dt><code>-fullscreen</code></p>
<dd> When this option is used, xdvi will (try to) run in fullscreen mode, with no window decorations. This option is not guaranteed to work with all windowmanagers/desktops; if you&#8217;re experiencing problems with it, please use the <code>-geometry</code> option instead, and a suitable window manager setting to remove the window decorations. When using this option for presentations, you might want to get rid of all the control widgets as well, using the <code>-expertmode</code> option. This option can also be toggled at runtime using the <code>fullscreen</code> action (by default bound to Ctrl-l).</p>
<dt><code>-gamma</code><i> gamma</i></p>
<dd> (<code>.gamma</code>) Controls the interpolation of colors in the greyscale anti-aliasing color palette. Default value is 1.0. For 0 &lt; <i>gamma</i> &lt; 1, the fonts will be lighter (more like the background), and for <i>gamma</i> &gt; 1, the fonts will be darker (more like the foreground). Negative values behave the same way, but use a slightly different algorithm. For color and grayscale displays; for monochrome, see <code>-density</code>. See also the `<code>S</code>&#8216; keystroke.</p>
<dt><code>-geometry</code><i> geometry</i></p>
<dd> (<code>.geometry</code>) Specifies the initial geometry of the main window, as described in the <i><a href="//www.systutorials.com/docs/linux/man/7x-X/">X</a>(7x)</i> man page. The geometry of child windows can be set separately, e.g.:<br />
 <i>xdvi*helpwindow.geometry: 600&#215;800</i></p>
<dt><code>-gsalpha</code></p>
<dd> (<code>.gsAlpha</code>) Causes <code>Ghostscript</code> to be called with the <code>x11alpha</code> driver instead of the <code>x11</code> driver. The <code>x11alpha</code> driver enables anti-aliasing in PostScript specials, for a nicer appearance. It is available on newer versions of <code>Ghostscript</code>. This option can also be toggled with the `<code>V</code>&#8216; keystroke.</p>
<dt><code>-gspalette</code><i> palette</i></p>
<dd> (<code>.palette</code>) Specifies the palette to be used when using Ghostscript for rendering PostScript specials. Possible values are <code>Color</code>, <code>Greyscale</code>, and <code>Monochrome</code>. The default is <code>Color</code>.</p>
<dt><code>-h</code>,<code> -help</code>,<code> &#8211;help</code></p>
<dd> Prints a short help text with an overview of the command-line options to standard output.</p>
<dt><code>-hl</code><i> color</i></p>
<dd> (<code>.highlight</code>) Determines the color of the page border, of the ruler in `ruler mode&#8217;, and of the highlighting markers in forward search and string search. The default is the foreground color.</p>
<dt><code>-anchorposition</code><i> anchor</i></p>
<dd> Jump to <i>anchor</i> after opening the DVI file. This is only useful when invoking <code>xdvi</code> from other applications.</p>
<dt><code>-hush</code></p>
<dd> (<code>.Hush</code>) Causes <code>xdvi</code> to suppress all suppressible warnings.</p>
<dt><code>-hushchars</code></p>
<dd> (<code>.hushLostChars</code>) Causes <code>xdvi</code> to suppress warnings about references to characters which are not defined in the font.</p>
<dt><code>-hushchecksums</code></p>
<dd> (<code>.hushChecksums</code>) Causes <code>xdvi</code> to suppress warnings about checksum mismatches between the <i>dvi</i> file and the font file.</p>
<dt><code>-warnspecials</code></p>
<dd> (<code>.warnSpecials</code>) Causes <code>xdvi</code> to print warnings about <code>\special</code> strings that it cannot process to stderr. These warnings are suppressed by default.</p>
<dt><code>-hushstdout</code></p>
<dd> (<code>.hushStdout</code>) Suppresses printing of status messages to <i>stdout</i>. Note that errors or warnings will still be printed to <i>stderr</i> even if this option is used.</p>
<dt><code>-hushbell</code></p>
<dd> (<code>.hushBell</code>) Don&#8217;t sound the X bell when an error occurs.</p>
<dt><code>-icongeometry</code><i> geometry</i></p>
<dd> (<code>.iconGeometry</code>) Specifies the initial position for the icon.</p>
<dt><code>-iconic</code></p>
<dd> (<code>.iconic</code>) Causes the <code>xdvi</code> window to start in the iconic state. The default is to start with the window open.</p>
<dt><code>-install</code></p>
<dd> (<code>.install</code>) If <code>xdvi</code> is running under a <code>PseudoColor</code> visual, then (by default) it will check for <code>TrueColor</code> visuals with more bits per pixel, and switch to such a visual if one exists. If no such visual exists, it will use the current visual and colormap. If <code>-install</code> is selected, however, it will still use a <code>TrueColor</code> visual with a greater depth, if one is available; otherwise, it will install its own colormap on the current visual. If the current visual is not <code>PseudoColor</code>, then <code>xdvi</code> will not switch the visual or colormap, regardless of its options. The default value of the <code>install</code> resource is the special value, <code>maybe</code>. There is no <code>+install</code> option. See also <code>-noinstall</code>, and the GREYSCALING AND COLORMAPS section.</p>
<dt><code>-interpreter</code><i> filename</i></p>
<dd> (<code>.interpreter</code>) Use <i>filename</i> as the Ghostscript interpreter. By default it uses <code>gs</code>.</p>
<dt><code>-keep</code></p>
<dd> (<code>.keepPosition</code>) Sets a flag to indicate that <code>xdvi</code> should not move to the home position when moving to a new page. See also the `<code>k</code>&#8216; keystroke. This flag is honored by all page switching actions and by <code>up-or-previous() /</code> <code>down-or-next()</code>, although the latter only honor the horizontal postion, not the vertical one. This allows for a &quot;continuous&quot; scrolling back an forth through a document with a display window narrower than a page width.</p>
<dt><code>-l</code></p>
<dd> (<code>.listFonts</code>) List the names of all fonts used.</p>
<dt><code>-license</code></p>
<dd> Prints licensing information.</p>
<dt><code>-linkcolor</code></p>
<dd> (<code>.linkColor</code>) Color used for unvisited hyperlinks (`Blue2&#8242; by default). Hyperlinks are unvisited before you click on them, or after the DVI file has been reloaded. The value should be either a valid X color name (such as <i>DarkGoldenrod4</i>) or a hexadecimal color string (such as <i>#8b6508</i>).<i>See</i>also <code>-visitedlinkcolor</code> and <code>-linkstyle</code>.</p>
<dt><code>-linkstyle</code></p>
<dd> (<code>.LinkStyle</code>) Determines the style in which hyperlinks are displayed. Possible values and their meanings are: </p>
<pre>
 0       No highlighting of links
 1       Underline links with <i>link color</i>
 2       No underlining, color text with <i>link color</i>
 3       Underline and display text colored with
         <i>link color</i>
</pre>
<p> The values for <i>link color</i> are specified by the options/resources <code>-linkcolor</code> and <code>-visitedlinkcolor</code> (which see).</p>
<dt><code>-margins</code><i> dimen</i></p>
<dd> (<code>.Margin</code>) Specifies the size of both the top margin and side margin. This determines the &#8220;home&#8221; position of the page within the window as follows. If the entire page fits in the window, then the margin settings are ignored. If, even after removing the margins from the left, right, top, and bottom, the page still cannot fit in the window, then the page is put in the window such that the top and left margins are hidden, and presumably the upper left-hand corner of the text on the page will be in the upper left-hand corner of the window. Otherwise, the text is centered in the window. The dimension should be a decimal number optionally followed by any of the two-letter abbreviations for units accepted by TeX (<code>pt</code>, <code>pc</code>, <code>in</code>, <code>bp</code>, <code>cm</code>, <code>mm</code>, <code>dd</code>, <code>cc</code>, or <code>sp</code>). By default, the unit will be <code>cm</code> (centimeters). See also <code>-sidemargin</code>, <code>-topmargin</code>, and the keystroke `<code>M</code>.&#8217;</p>
<dt><code>-mfmode</code><i> mode-def</i></p>
<dd> (<code>.mfMode</code>) Specifies a <i>mode-def</i> string, which can be used in searching for fonts (see ENVIRONMENT, below). Generally, when changing the <i>mode-def</i>, it is also necessary to change the font size to the appropriate value for that mode. This is done by adding a colon and the value in dots per inch; for example, <code>-mfmode ljfour:600</code>. This method overrides any value given by the <code>pixelsPerInch</code> resource or the <code>-p</code> command-line argument. The metafont mode is also passed to <code>metafont</code> during automatic creation of fonts. By default, it is <code>unspecified</code>.</p>
<dt><code>-mgs</code><i> size</i></p>
<dd> Same as <code>-mgs1</code>.</p>
<dt><code>-mgs[</code><i>n</i><code>]</code><i> size</i></p>
<dd> (<code>.magnifierSize</code>[<i>n</i>]) Specifies the size of the window to be used for the &#8220;magnifying glass&#8221; for Button <i>n</i>. The size may be given as an integer (indicating that the magnifying glass is to be square), or it may be given in the form <i>width</i>x<i>height</i>. See the MOUSE ACTIONS section. Defaults are 200&#215;150, 400&#215;250, 700&#215;500, 1000&#215;800, and 1200&#215;1200.</p>
<dt><code>-mousemode</code><i> </i><code>[</code><i>0</i><code>|</code><i>1</i><code>|</code><i>2</i><code>]</code></p>
<dd> (<code>.mouseMode</code>) Specifies the default mode of xdvi at startup: Magnifier (0), Text Selection Mode (1) or Ruler Mode (2). See the section <code>MODES</code>, below, for more information.</p>
<dt><code>-nocolor</code></p>
<dd> (<code>.color</code>) Turns off the use of color specials. This option can be toggled with the `<code>C</code>&#8216; keystroke. (Note: <code>-nocolor</code> corresponds to <code>color:off</code>; <code>+nocolor</code> to <code>color:on</code>.)</p>
<dt><code>-nofork</code></p>
<dd> (<code>.fork</code>) With the <code>-sourceposition</code> and <code>-unique</code> options, the default behavior is for <code>xdvi</code> to put itself into the background (like a daemon) if there is no appropriate instance of <code>xdvi</code> already running. This argument makes it run in the foreground instead. This is useful for debugging, or if your client application cannot deal well with a program self-backgrounding itself in this way &#8212; e.g., the IPC functions in <code>emacs</code> are known to have problems with this. If no <code>-sourceposition</code> or <code>-unique</code> argument is given, then this option has no effect. (Note: <code>-nofork</code> corresponds to <code>fork:off</code>; <code>+nofork</code> to <code>fork:on</code>.)</p>
<dt><code>-noghostscript</code></p>
<dd> (<code>.ghostscript</code>) Inhibits the use of Ghostscript for displaying PostScript&lt;tm&gt; specials. (Note: <code>-noghostscript</code> corresponds to <code>ghostscript:off</code>; <code>+noghostscript</code> to <code>ghostscript:on</code>.)</p>
<dt><code>-nogrey</code></p>
<dd> (<code>.grey</code>) Turns off the use of greyscale anti-aliasing when printing shrunken bitmaps. (Note: <code>-nogrey</code> corresponds to <code>grey:off</code>; <code>+nogrey</code> to <code>grey:on</code>.) See also the `<code>G</code>&#8216; keystroke.</p>
<dt><code>-nogssafer</code></p>
<dd> (<code>.gsSafer</code>) Normally, if Ghostscript is used to render PostScript specials, the Ghostscript interpreter is run with the option <code>-dSAFER</code>. The <code>-nogssafer</code> option runs Ghostscript without <code>-dSAFER</code>. The <code>-dSAFER</code> option in Ghostscript disables PostScript operators such as <code>deletefile</code>, to prevent possibly malicious PostScript programs from having any effect. If the <code>-safer</code> option is specified, then this option has no effect; in that case Ghostscript is always run with <code>-dSAFER</code>. (Note: <code>-nogssafer</code> corresponds to <code>gsSafer:off</code>; <code>+nogssafer</code> to <code>gsSafer:on</code>.)</p>
<dt><code>-noinstall</code></p>
<dd> (<code>.install</code>) Inhibit the default behavior of switching to a <code>TrueColor</code> visual if one is available with more bits per pixel than the current visual. (Note: -noinstall corresponds <code>install:off</code>; there is no <code>+noinstall</code> option.) See also <code>-install</code>, and the GREYSCALING AND COLORMAPS section.</p>
<dt><code>-nomakepk</code></p>
<dd> (<code>.makePk</code>) Turns off automatic generation of font files that cannot be found by other means. (Note: <code>-nomakepk</code> corresponds to <code>makePk:off</code>; <code>+nomakepk</code> to <code>makePK:on</code>.)</p>
<dt><code>-nomatchinverted</code></p>
<dd> (<code>.matchInverted</code>) Don&#8217;t highlight string search matches in inverted color; instead, draw a rectangle in <i>highlight</i> color (see the <code>-hl</code> option) around the match. This option is activated automatically if the display isn&#8217;t running in TrueColor. (Note: <code>-nomatchinverted</code> corresponds to <code>matchInverted:off</code>; <code>+nomatchinverted</code> to <code>matchInverted:on</code>.)</p>
<dt><code>-noomega</code></p>
<dd> (<code>.omega</code>) This will disable the use of Omega extensions when interpreting DVI files. By default, the additional opcodes <i>129</i> and <i>134</i> are recognized by xdvi as Omega extensions and interpreted as requests to set 2-byte characters. The only drawback is that the virtual font array will require 65536 positions instead of the default 256 positions, i.e. the memory requirements of xdvi will be slightly larger. If you find this unacceptable or encounter another problem with the Omega extensions, you can switch this extension off by using <code>-noomega</code> (but please do send a bug report if you find such problems &#8211; see the bug address in the <code>AUTHORS</code> section below).<br />
 (Note: <code>-noomega</code> corresponds to <code>omega: off</code>; <code>+noomega</code> to <code>omega: on</code>.)</p>
<dt><code>-noscan</code></p>
<dd> (<code>.prescan</code>) By default, <code>xdvi</code> does a preliminary scan of the <i>dvi</i> file to process any <code>papersize</code> specials; this is especially important at startup since the paper size may be needed to determine the window size. If PostScript&lt;tm&gt; is in use, then prescanning is also necessary in order to properly process header files. In addition, prescanning is needed to correctly determine the background color of a page. This option turns off such prescanning. (Prescanning will be automatically be turned back on if <code>xdvi</code> detects any of the specials mentioned above.) (Note: <code>-noscan</code> corresponds to <code>prescan:off</code>; <code>+noscan</code> to <code>prescan:on</code>.)</p>
<dt><code>-not1lib</code></p>
<dd> (<code>.t1lib</code>) This will disable the use of T1Lib to display PostScript&lt;tm&gt; fonts. Use this option as a workaround when you encounter problems with the display of T1Lib (but please don&#8217;t forget to send a bug report in this case, to the URL mentioned in the section AUTHORS below).<br />
 (Note: <code>-not1lib</code> corresponds to <code>t1lib:off</code>; <code>+not1lib</code> to <code>t1lib:on</code>.)</p>
<dt><code>-notempfile</code></p>
<dd> (<code>.tempFile</code>) As mentioned in the section <code>DESCRIPTION</code> above, xdvi will create a temporary copy of the DVI file so that it can be accessed without interruptions even while the file is being rewritten by <code>TeX</code>. Since this introduces the overhead of copying the file every time it has changed, the <code>-notempfile</code> allows you to turn off this behaviour. In this case, exposing parts of the window while the DVI file is being written by TeX will erase the current window contents until the DVI file can be completely reread.<br />
 (Note: <code>-notempfile</code> corresponds to <code>tempFile:off</code>; <code>+notempfile</code> to <code>tempFile:on</code>.)</p>
<dt><code>-offsets</code><i> dimen</i></p>
<dd> (<code>.Offset</code>) Specifies the size of both the horizontal and vertical offsets of the output on the page. By decree of the Stanford TeX Project, the default TeX page origin is always 1 inch over and down from the top-left page corner, even when non-American paper sizes are used. Therefore, the default offsets are 1.0 inch. The argument <i>dimen</i> should be a decimal number optionally followed by any of the two-letter abbreviations for units accepted by TeX (<code>pt</code>, <code>pc</code>, <code>in</code>, <code>bp</code>, <code>cm</code>, <code>mm</code>, <code>dd</code>, <code>cc</code>, or <code>sp</code>). By default, the unit will be <code>cm</code> (centimeters). See also <code>-xoffset</code> and <code>-yoffset</code>.</p>
<dt><code>-p</code><i> pixels</i></p>
<dd> (<code>.pixelsPerInch</code>) Defines the size of the fonts to use, in pixels per inch. The default value is 600. This option is provided only for backwards compatibility; the preferred way is to set both the resolution and the Metafont mode via the <code>-mfmode</code> option (which see).</p>
<dt><code>-paper</code><i> papertype</i></p>
<dd> (<code>.paper</code>) Specifies the size of the printed page. Note that in most cases it&#8217;s best to specify the paper size in the TeX input file via the line </p>
<p> <code>
