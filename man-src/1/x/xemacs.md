---
title: "xemacs(1)"
name: "xemacs"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xemacs/"
description: "xemacs – Emacs: The Next Generation"
---

<h2 class="name">NAME</h2>
<p> xemacs &#8211; Emacs: The Next Generation </p>
<h2>SYNOPSIS</h2>
<p> <code>xemacs</code> [ <i>command-line switches</i> ] [ <i>files &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <i>XEmacs</i> is a version of <i>Emacs</i>, compatible with and containing many improvements over <i>GNU</i> <i>Emacs</i>, written by Richard Stallman of the Free Software Foundation. It was originally based on an early release of <i>GNU Emacs Version</i> <i>19</i>, and has tracked subsequent releases of <i>GNU Emacs</i> as they have become available. </p>
<p> The primary documentation of <i>XEmacs</i> is in the <i>XEmacs Reference</i> <i>Manual</i>, which you can read on-line using Info, a subsystem of <i>XEmacs</i>. Please look there for complete and up-to-date documentation. Complete documentation on using Emacs Lisp is available on-line through the <i>XEmacs Lisp Programmer&#8217;s</i> <i>Manual</i>. Both manuals also can be printed out nicely using the <i>TeX</i> formatting package. </p>
<p> The user functionality of <i>XEmacs</i> encompasses everything other <i>Emacs</i> editors do, and it is easily extensible since its editing commands are written in Lisp. </p>
<p> <i>XEmacs</i> has an extensive interactive help facility, but the facility assumes that you know how to manipulate <i>XEmacs</i> windows and buffers. CTRL-h enters the Help facility. Help Tutorial (CTRL-h t) requests an interactive tutorial which can teach beginners the fundamentals of <i>XEmacs</i> in a few minutes. Help Apropos (CTRL-h a) helps you find a command given its functionality, Help Key Binding (CTRL-h k) describes a given key sequence&#8217;s effect, and Help Function (CTRL-h f) describes a given Lisp function specified by name. You can also look up key sequences in the <i>XEmacs Reference Manual</i> using Lookup Key Binding (CTRL-h CTRL-k), and look up Lisp functions in the <i>XEmacs Lisp Programmer&#8217;s Manual</i> using Lookup Function (CTRL-h CTRL-f). All of these help functions, and more, are available on the Help menu if you are using a window system. </p>
<p> <i>XEmacs</i> has extensive GUI (graphical user interface) support when running under a window system such as <i>X</i>, including multiple frames (top-level windows), a menubar, a toolbar, horizontal and vertical scrollbars, dialog boxes, and extensive mouse support. </p>
<p> <i>XEmacs</i> has full support for multiple fonts and colors, variable-width fonts, and variable-height lines, and allows for pixmaps to be inserted into a buffer. (This is used in the W3 web-browsing package and in some of the debugger and outlining interfaces, among other things.) </p>
<p> <i>XEmacs</i>&#8216;s Undo can undo several steps of modification to your buffers, so it is easy to recover from editing mistakes. </p>
<p> <i>XEmacs</i>&#8216;s many special packages handle mail reading (VM, MH-E and RMail) and sending (Mail), Usenet news reading and posting (GNUS), World Wide Web browsing (W3), specialized modes for editing source code in all common programming languages, syntax highlighting for many languages (Font-Lock), compiling (Compile), running subshells within <i>XEmacs</i> windows (Shell), outline editing (Outline), running a Lisp read-eval-print loop (Lisp-Interaction-Mode), and automated psychotherapy (Doctor). </p>
<p> There is an extensive reference manual, but users of other Emacsen should have little trouble adapting even without a copy. Users new to Emacs will be able to use basic features fairly rapidly by studying the tutorial and using the self-documentation features. </p>
<p> <font SIZE="-1">XEmacs Options</font> </p>
<p> XEmacs accepts all standard X Toolkit command line options when run in an X Windows environment. In addition, the following options are accepted (when options imply a sequence of actions to perform, they are performed in the order encountered):</p>
<dl>
<dt><code>-t</code><i> file</i></p>
<dd> Use specified <i>file</i> as the terminal instead of using stdin/stdout. This implies <code>-nw</code>.</p>
<dt><code>-batch</code></p>
<dd> Edit in batch mode. The editor will send messages to stdout. You must use the <code>-l</code>, <code>-f</code>, and <code>-eval</code> options to specify files to execute and functions to call.</p>
<dt><code>-nw</code></p>
<dd> Inhibit the use of any window-system-specific display code: use the current TTY.</p>
<dt><code>-debug-init</code></p>
<dd> Enter the debugger if an error occurs loading the init file.</p>
<dt><code>-unmapped</code></p>
<dd> Do not map the initial frame.</p>
<dt><code>-no-site-file</code></p>
<dd> Do not load the site-specific init file (site-start.el).</p>
<dt><code>-q, -no-init-file</code></p>
<dd> Do not load an init file.</p>
<dt><code>-no-early-packages</code></p>
<dd> Do not process the early packages.</p>
<dt><code>-vanilla</code></p>
<dd> Load no extra files at startup. Equivalent to the combination of <code>-q</code>, <code>-no-site-file</code>, and <code>-no-early-packages</code>.</p>
<dt><code>-u</code><i> user, </i><code>-user</code><i> user</i></p>
<dd> Load <i>user</i>&#8216;s init file.</p>
<dt><i>file</i></p>
<dd> Edit <i>file</i>.</p>
<dt><code>+</code><i>number</i></p>
<dd> Go to the line specified by <i>number</i> (do not insert a space between the &quot;+&quot; sign and the number).</p>
<dt><code>-help</code></p>
<dd> Print a help message and exit.</p>
<dt><code>-V, -version,</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-f</code><i> function, </i><code>-funcall</code><i> function</i></p>
<dd> Execute the lisp function <i>function</i>.</p>
<dt><code>-l</code><i> file, </i><code>-load</code><i> file</i></p>
<dd> Load the Lisp code in the file <i>file</i>.</p>
<dt><code>-eval</code><i> form</i></p>
<dd> Evaluate the Lisp form <i>form</i>.</p>
<dt><code>-i</code><i> file, </i><code>-insert</code><i> file</i></p>
<dd> Insert <i>file</i> into the current buffer.</p>
<dt><code>-kill</code></p>
<dd> Exit <i>XEmacs</i> (useful with <code>-batch</code>).</dl>
<p> <font SIZE="-1">Using XEmacs with X Windows</font> </p>
<p> <i>XEmacs</i> has been tailored to work well with the X window system. If you run <i>XEmacs</i> from under X windows, it will create its own X window to display in. </p>
<p> <i>XEmacs</i> can be started with the following standard X options:</p>
<dl>
<dt><code>-visual</code><i> &lt;visualname&gt;&lt;bitdepth&gt;</i></p>
<dd> Select the visual that XEmacs will attempt to use. <i>&lt;visualname&gt;</i> should be one of the strings &quot;StaticColor&quot;, &quot;TrueColor&quot;, &quot;GrayScale&quot;, &quot;PseudoColor&quot; or &quot;DirectColor&quot;, and <i>&lt;bitdepth&gt;</i> should be the number of bits per pixel (example, &quot;-visual TrueColor24&quot; for a 24bit TrueColor visual) See <i><a href="/docs/linux/man/1-x/">X</a></i>(1) for more information.</p>
<dt><code>-privateColormap</code></p>
<dd> Require XEmacs to create and use a private colormap for display. This will keep XEmacs from taking colors from the default colormap and keeping them from other clients, at the cost of causing annoying flicker when the focus changes. Use this option only if your X server does not support 24 bit visuals.</p>
<dt><code>-geometry</code><i> ##x##+##+##</i></p>
<dd> Specify the geometry of the initial window. The ##&#8217;s represent a number; the four numbers are width (characters), height (characters), X offset (pixels), and Y offset (pixels), respectively. Partial specifications of the form <i>##x##</i> or <i>+##+##</i> are also allowed. (The geometry specification is in the standard X format; see <i><a href="/docs/linux/man/1-x/">X</a></i>(1) for more information.)</p>
<dt><code>-iconic</code></p>
<dd> Specifies that the initial window should initially appear iconified.</p>
<dt><code>-name</code><i> name</i></p>
<dd> Specifies the program name which should be used when looking up defaults in the user&#8217;s X resources.</p>
<dt><code>-title</code><i> title, </i><code>-T</code><i> title, </i><code>-wn</code><i> title</i></p>
<dd> Specifies the title which should be assigned to the <i>XEmacs</i> window.</p>
<dt><code>-d</code><i> displayname, </i><code>-display</code><i> displayname</i></p>
<dd> Create the <i>XEmacs</i> window on the display specified by <i>displayname</i>. Must be the first option specified in the command line.</p>
<dt><code>-font</code><i> font, </i><code>-fn</code><i> font</i></p>
<dd> Set the <i>XEmacs</i> window&#8217;s font to that specified by <i>font</i>. You will find the various <i>X</i> fonts in the <i>/usr/lib/X11/fonts</i> directory. <i>XEmacs</i> works with either fixed- or variable-width fonts, but will probably look better with a fixed-width font.</p>
<dt><code>-scrollbar-width</code><i> pixels</i></p>
<dd> Specify the width of the vertical scrollbars.</p>
<dt><code>-scrollbar-height</code><i> pixels</i></p>
<dd> Specify the height of the horizontal scrollbars.</p>
<dt><code>-bw</code><i> pixels, </i><code>-borderwidth</code><i> pixels</i></p>
<dd> Set the <i>XEmacs</i> window&#8217;s border width to the number of pixels specified by <i>pixels</i>. Defaults to one pixel on each side of the window.</p>
<dt><code>-ib</code><i> pixels, </i><code>-internal-border-width</code><i> pixels</i></p>
<dd> Specify the width between a frame&#8217;s border and its text, in pixels. Defaults to one pixel on each side of the window.</p>
<dt><code>-fg</code><i> color, </i><code>-foreground</code><i> color</i></p>
<dd> Sets the color of the text. </p>
<p> See the file <i>/usr/share/X11/rgb.txt</i> for a list of valid color names.</p>
<dt><code>-bg</code><i> color, </i><code>-background</code><i> color</i></p>
<dd> Sets the color of the window&#8217;s background.</p>
<dt><code>-bd</code><i> color, </i><code>-bordercolor</code><i> color</i></p>
<dd> Sets the color of the window&#8217;s border.</p>
<dt><code>-mc</code><i> color</i></p>
<dd> Sets the color of the mouse pointer.</p>
<dt><code>-cr</code><i> color</i></p>
<dd> Sets the color of the text cursor.</p>
<dt><code>-rv, -reverse</code></p>
<dd> Reverses the foreground and background colors (reverse video). Consider explicitly setting the foreground and background colors instead of using this option.</p>
<dt><code>-xrm</code><i> argument</i></p>
<dd> This allows you to set an arbitrary resource on the command line. <i>argument</i> should be a resource specification, as might be found in your <i>.Xresources</i> or <i>.Xdefaults</i> file.</dl>
<p> You can also set resources, i.e. <i>X</i> default values, for your <i>XEmacs</i> windows in your <i>.Xresources</i> or <i>.Xdefaults</i> file (see <i><a href="/docs/linux/man/1-xrdb/">xrdb</a></i>(1)). Use the following format:</p>
<dl>
<dt>
<dd> Emacs.keyword:value</dl>
<p> or</p>
<dl>
<dt>
<dd> Emacs*EmacsFrame.keyword:value</dl>
<p> where <i>value</i> specifies the default value of <i>keyword</i>. (Some resources need the former format; some the latter.) </p>
<p> You can also set resources for a particular frame by using the format</p>
<dl>
<dt>
<dd> Emacs*framename.keyword:value</dl>
<p> where <i>framename</i> is the resource name assigned to that particular frame. (Certain packages, such as VM, give their frames unique resource names, in this case &quot;VM&quot;.) </p>
<p> <i>XEmacs</i> lets you set default values for the following keywords:</p>
<dl>
<dt><code>default.attributeFont (</code>class<code> Face.AttributeFont)</code></p>
<dd> Sets the window&#8217;s text font.</p>
<dt><code>default.attributeForeground (</code>class<code> Face.AttributeForeground)</code></p>
<dd> Sets the window&#8217;s text color.</p>
<dt><code>default.attributeBackground (</code>class<code> Face.AttributeBackground)</code></p>
<dd> Sets the window&#8217;s background color.</p>
<dt><i>face</i><code>.attributeFont (</code>class<code> Face.AttributeFont)</code></p>
<dd> Sets the font for <i>face</i>, which should be the name of a face. Common face names are</dl>
<p> FACE<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>PURPOSE</p>
<p> default<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Normal text.</p>
<p> bold<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Bold text.</p>
<p> italic<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Italicized text.</p>
<p> bold-italic<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Bold and italicized text.</p>
<p> modeline<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Modeline text.</p>
<p> zmacs-region<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text selected with the mouse.</p>
<p> highlight<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text highlighted when the mouse passes over.</p>
<p> left-margin<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text in the left margin.</p>
<p> right-margin<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text in the right margin.</p>
<p> isearch<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text highlighted during incremental search.</p>
<p> info-node<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text of Info menu items.</p>
<p> info-xref<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Text of Info cross references.</p>
<dl>
<dt><i>face</i><code>.attributeForeground (</code>class<code> Face.AttributeForeground)</code></p>
<dd> Sets the foreground color for <i>face</i>.</p>
<dt><i>face</i><code>.attributeBackground (</code>class<code> Face.AttributeBackground)</code></p>
<dd> Sets the background color for <i>face</i>.</p>
<dt><i>face</i><code>.attributeBackgroundPixmap (</code>class<code> Face.AttributeBackgroundPixmap)</code></p>
<dd> Sets the background pixmap (stipple) for <i>face</i>.</p>
<dt><i>face</i><code>.attributeUnderline (</code>class<code> Face.AttributeUnderline)</code></p>
<dd> Whether <i>face</i> should be underlined.</p>
<dt><code>reverseVideo (</code>class<code> ReverseVideo)</code></p>
<dd> If set to <i>on</i>, the window will be displayed in reverse video. Consider explicitly setting the foreground and background colors instead of using this resource.</p>
<dt><code>borderWidth (</code>class<code> BorderWidth)</code></p>
<dd> Sets the window&#8217;s border width in pixels.</p>
<dt><code>internalBorderWidth (</code>class<code> InternalBorderWidth)</code></p>
<dd> Sets the window&#8217;s internal border width in pixels.</p>
<dt><code>borderColor (</code>class<code> BorderColor)</code></p>
<dd> Sets the color of the window&#8217;s border.</p>
<dt><code>cursorColor (</code>class<code> Foreground)</code></p>
<dd> Sets the color of the window&#8217;s text cursor.</p>
<dt><code>pointerColor (</code>class<code> Foreground)</code></p>
<dd> Sets the color of the window&#8217;s mouse cursor.</p>
<dt><code>emacsVisual (</code>class<code> EmacsVisual)</code></p>
<dd> Sets the default visual <i>XEmacs</i> will try to use (as described above).</p>
<dt><code>privateColormap (</code>class<code> PrivateColormap)</code></p>
<dd> If set, <i>XEmacs</i> will default to using a private colormap.</p>
<dt><code>geometry (</code>class<code> Geometry)</code></p>
<dd> Sets the geometry of the <i>XEmacs</i> window (as described above).</p>
<dt><code>iconic (</code>class<code> Iconic)</code></p>
<dd> If set to on, the <i>XEmacs</i> window will initially appear as an icon.</p>
<dt><code>menubar (</code>class<code> Menubar)</code></p>
<dd> Whether the <i>XEmacs</i> window will have a menubar. Defaults to true.</p>
<dt><code>initiallyUnmapped (</code>class<code> InitiallyUnmapped)</code></p>
<dd> Whether <i>XEmacs</i> will leave the initial frame unmapped when it starts up.</p>
<dt><code>barCursor (</code>class<code> BarCursor)</code></p>
<dd> Whether the cursor should be a bar instead of the traditional box.</p>
<dt><code>title (</code>class<code> Title)</code></p>
<dd> Sets the title of the <i>XEmacs</i> window.</p>
<dt><code>iconName (</code>class<code> Title)</code></p>
<dd> Sets the icon name for the <i>XEmacs</i> window icon.</p>
<dt><code>scrollBarWidth (</code>class<code> ScrollBarWidth)</code></p>
<dd> Sets the width of the vertical scrollbars, in pixels. A width of 0 means no vertical scrollbars.</p>
<dt><code>scrollBarHeight (</code>class<code> ScrollBarHeight)</code></p>
<dd> Sets the height of the horizontal scrollbars, in pixels. A height of 0 means no horizontal scrollbars.</p>
<dt><code>scrollBarPlacement (</code>class<code> ScrollBarPlacement)</code></p>
<dd> Sets the position of vertical and horizontal scrollbars. Should be one of the strings &quot;top-left&quot;, &quot;bottom-left&quot;, &quot;top-right&quot;, or &quot;bottom-right&quot;. The default is &quot;bottom-right&quot; for the Motif and Lucid scrollbars and &quot;bottom-left&quot; for the Athena scrollbars.</p>
<dt><code>topToolBarHeight (</code>class<code> TopToolBarHeight)</code></p>
<dd> Sets the height of the top toolbar, in pixels. 0 means no top toolbar.</p>
<dt><code>bottomToolBarHeight (</code>class<code> BottomToolBarHeight)</code></p>
<dd> Sets the height of the bottom toolbar, in pixels. 0 means no bottom toolbar.</p>
<dt><code>leftToolBarWidth (</code>class<code> LeftToolBarWidth)</code></p>
<dd> Sets the width of the left toolbar, in pixels. 0 means no left toolbar.</p>
<dt><code>rightToolBarWidth (</code>class<code> RightToolBarWidth)</code></p>
<dd> Sets the width of the right toolbar, in pixels. 0 means no right toolbar.</p>
<dt><code>topToolBarShadowColor (</code>class<code> TopToolBarShadowColor)</code></p>
<dd> Sets the color of the top shadows for the toolbars. (For all toolbars, <code>not</code> just the toolbar at the top of the frame.)</p>
<dt><code>bottomToolBarShadowColor (</code>class<code> BottomToolBarShadowColor)</code></p>
<dd> Sets the color of the bottom shadows for the toolbars. (For all toolbars, <code>not</code> just the toolbar at the bottom of the frame.)</p>
<dt><code>topToolBarShadowPixmap (</code>class<code> TopToolBarShadowPixmap)</code></p>
<dd> Sets the pixmap of the top shadows for the toolbars. (For all toolbars, <code>not</code> just the toolbar at the top of the frame.) If set, this resource overrides the corresponding color resource.</p>
<dt><code>bottomToolBarShadowPixmap (</code>class<code> BottomToolBarShadowPixmap)</code></p>
<dd> Sets the pixmap of the bottom shadows for the toolbars. (For all toolbars, <code>not</code> just the toolbar at the bottom of the frame.) If set, this resource overrides the corresponding color resource.</p>
<dt><code>toolBarShadowThickness (</code>class<code> ToolBarShadowThickness)</code></p>
<dd> Thickness of the shadows around the toolbars, in pixels.</p>
<dt><code>visualBell (</code>class<code> VisualBell)</code></p>
<dd> Whether XEmacs should flash the screen rather than making an audible beep.</p>
<dt><code>bellVolume (</code>class<code> BellVolume)</code></p>
<dd> Volume of the audible beep. Range is 0 through 100.</p>
<dt><code>useBackingStore (</code>class<code> UseBackingStore)</code></p>
<dd> Whether <i>XEmacs</i> should set the backing-store attribute of the <i>X</i> windows it creates. This increases the memory usage of the <i>X</i> server but decreases the amount of <i>X</i> traffic necessary to update the screen, and is useful when the connection to the <i>X</i> server goes over a low-bandwidth line such as a modem connection.</p>
<dt><code>textPointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to use when the mouse is over text.</p>
<dt><code>selectionPointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to use when the mouse is over a mouse-highlighted text region.</p>
<dt><code>spacePointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to use when the mouse is over a blank space in a buffer (that is, after the end of a line or after the end-of-file).</p>
<dt><code>modeLinePointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to use when the mouse is over a mode line.</p>
<dt><code>gcPointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to display when a garbage-collection is in progress.</p>
<dt><code>scrollbarPointer (</code>class<code> Cursor)</code></p>
<dd> The cursor to use when the mouse is over the scrollbar.</p>
<dt><code>pointerColor (</code>class<code> Foreground)</code></p>
<dd> The foreground color of the mouse cursor.</p>
<dt><code>pointerBackground (</code>class<code> Background)</code></p>
<dd> The background color of the mouse cursor.</dl>
<p> <font SIZE="-1">Using the Mouse</font> </p>
<p> The following lists the mouse button bindings for the <i>XEmacs</i> window under X11. </p>
<p> MOUSE BUTTON<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>FUNCTION</p>
<p> left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Set point or make a text selection.</p>
<p> middle<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Paste text.</p>
<p> right<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Pop up a menu of options.</p>
<p> SHIFT-left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Extend a selection.</p>
<p> CTRL-left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Make a selection and insert it at point.</p>
<p> CTRL-middle<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Set point and move selected text there.</p>
<p> CTRL-SHIFT-left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Make a selection, delete it, and insert it at point.</p>
<p> META-left<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Make a rectangular selection.</p>
<h2>FILES</h2>
<p> Lisp code is read at startup from the user&#8217;s init file, <code>$HOME/.xemacs/init.el</code>. If this file does not exist then <code>$HOME/.emacs</code> will be read if it is present. </p>
<p> /usr/local/info &#8211; files for the Info documentation browser (a subsystem of <i>XEmacs</i>) to refer to. The complete text of the <i>XEmacs Reference Manual</i> and the <i>XEmacs Lisp Programmer&#8217;s Manual</i> is included in a convenient tree structured form. </p>
<p> /usr/local/lib/xemacs-$VERSION/info &#8211; the Info files may be here instead. </p>
<p> /usr/local/lib/xemacs-$VERSION/lisp/* &#8211; Lisp source files and compiled files that define most editing commands. The files are contained in subdirectories, categorized by function or individual package. Some are preloaded; others are autoloaded from these directories when used. </p>
<p> /usr/local/lib/xemacs-$VERSION/etc &#8211; some files of information, pixmap files, other data files used by certain packages, etc. </p>
<p> /usr/local/lib/xemacs-$VERSION/$CONFIGURATION &#8211; various programs that are used with XEmacs. </p>
<p> /usr/local/lib/xemacs-$VERSION/$CONFIGURATION/DOC &#8211; contains the documentation strings for the Lisp primitives and preloaded Lisp functions of <i>XEmacs</i>. They are stored here to reduce the size of <i>XEmacs</i> proper. </p>
<p> /usr/local/lib/xemacs/site-lisp &#8211; locally-provided Lisp files. </p>
<h2>BUGS AND HELP</h2>
<p> There is a newsgroup, comp.emacs.xemacs, for reporting <i>XEmacs</i> bugs and fixes and requesting help. But before reporting something as a bug, please try to be sure that it really is a bug, not a misunderstanding or a deliberate feature. We ask you to read the section &#8220;Reporting XEmacs Bugs&#8221; near the end of the reference manual (or Info system) for hints on how and when to report bugs. Also, include the version number of the <i>XEmacs</i> you are running and the system you are running it on in <i>every</i> bug report that you send in. Finally, the more you can isolate the cause of a bug and the conditions it happens under, the more likely it is to be fixed, so please take the time to do so. </p>
<p> The newsgroup is bidirectionally gatewayed to and from the mailing list xemacs [at] xemacs.org. You can read the list instead of the newsgroup if you do not have convenient Usenet news access. To request to be added to the mailing list, send mail to xemacs-request [at] xemacs.org. (Do not send mail to the list itself.) </p>
<p> The <i>XEmacs</i> maintainers read the newsgroup regularly and will attempt to fix bugs reported in a timely fashion. However, not every message will get a response from one of the maintainers. Note that there are many people other than the maintainers who read the newsgroup, and will usually be of assistance in helping with any problems encountered. </p>
<p> If you need more personal assistance than can be provided by the newsgroup, look in the SERVICE file (see above) for a list of people who offer it. </p>
<p> For more information about XEmacs mailing lists, see the file /usr/local/lib/xemacs-$VERSION/etc/MAILINGLISTS.</p>
<h2>UNRESTRICTIONS</h2>
<p> <i>XEmacs</i> is free; anyone may redistribute copies of <i>XEmacs</i> to anyone under the terms stated in the <i>XEmacs</i> General Public License, a copy of which accompanies each copy of <i>XEmacs</i> and which also appears in the reference manual. </p>
<p> Copies of <i>XEmacs</i> may sometimes be received packaged with distributions of Unix systems, but it is never included in the scope of any license covering those systems. Such inclusion violates the terms on which distribution is permitted. In fact, the primary purpose of the General Public License is to prohibit anyone from attaching any other restrictions to redistribution of <i>XEmacs</i>.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-x/">X</a>(1), <a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a>(1), <a href="/docs/linux/man/1-xterm/">xterm</a>(1), <a href="/docs/linux/man/1-xrdb/">xrdb</a>(1), <a href="/docs/linux/man/1-emacs/">emacs</a>(1), <a href="/docs/linux/man/1-vi/">vi</a>(1)</p>
<h2>AUTHORS</h2>
<p> <i>XEmacs</i> was written by Steve Baur &lt;steve [at] xemacs.org&gt;, Martin Buchholz &lt;martin [at] xemacs.org&gt;, Richard Mlynarik &lt;mly [at] adoc.xerox.com&gt;, Hrvoje Niksic &lt;hniksic [at] xemacs.org&gt;, Chuck Thompson &lt;cthomp [at] xemacs.org&gt;, Ben Wing &lt;ben [at] xemacs.org&gt;, Jamie Zawinski &lt;jwz [at] jwz.org&gt;, and many others. It was based on an early version of <i>GNU Emacs Version</i> <i>19</i>, written by Richard Stallman &lt;rms [at] gnu.org&gt; of the Free Software Foundation, and has tracked subsequent releases of <i>GNU Emacs</i> as they have become available. It was originally written by Lucid, Inc. (now defunct) and was called <i>Lucid</i> <i>Emacs</i>. </p>
<p> Chuck Thompson wrote the <i>XEmacs</i> redisplay engine, maintains the <i>XEmacs</i> FTP and WWW sites, and has put out all releases of <i>XEmacs</i> since 19.11 (the first release called <i>XEmacs</i>). Ben Wing wrote the Asian-language support, the on-line documentation (including this man page and much of the FAQ), the external widget code, and retooled or rewrote most of the basic, low-level <i>XEmacs</i> subsystems. Jamie Zawinski put out all releases of <i>Lucid</i> <i>Emacs</i>, from the first (19.0) through the last (19.10), and was the primary code contributor for all of these releases. Richard Mlynarik rewrote the <i>XEmacs</i> Lisp-object allocation system, improved the keymap and minibuffer code, and did the initial synching of <i>XEmacs</i> with <i>GNU Emacs Version</i> <i>19</i>. </p>
<p> Many others have also contributed significantly. For more detailed information, including a long history of <i>XEmacs</i> from multiple viewpoints and pretty pictures and bios of the major <i>XEmacs</i> contributors, see the <i>XEmacs About Page</i> (the About XEmacs option on the Help menu).</p>
<h2>MORE INFORMATION</h2>
<p> For more information about <i>XEmacs</i>, see the <i>XEmacs About Page</i> (mentioned above), look in the file /usr/local/lib/xemacs-$VERSION/etc/NEWS, or point your Web browser at </p>
<p> <a rel="nofollow" href="http://www.xemacs.org/">http://www.xemacs.org/</a> </p>
<p> for up-to-the-minute information about <i>XEmacs</i>. </p>
<p> The <i>XEmacs</i> FAQ (Frequently Asked Questions) can be found at the Web site just listed. A possibly out-of-date version is also accessible through the Info system inside of <i>XEmacs</i>. </p>
<p> The latest version of <i>XEmacs</i> can be downloaded using anonymous FTP from </p>
<p> <a href="ftp://ftp.xemacs.org/pub/xemacs/">ftp://ftp.xemacs.org/pub/xemacs/</a> </p>
<p> or from a mirror site near you. Mirror sites are listed in the file etc/FTP in the XEmacs distribution or see the Web site for an up-to-date list of mirror sites. </p>
<h2>Index</h2>
