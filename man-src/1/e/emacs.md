---
title: "emacs(1)"
name: "emacs"
section: "1"
letter: "e"
url: "/docs/linux/man/1-emacs/"
description: "emacs – GNU project Emacs editor"
---

<h2 class="name">NAME</h2>
<p> emacs &#8211; GNU project Emacs editor </p>
<h2>SYNOPSIS</h2>
<p> <code>emacs</code> [ <i>command-line switches</i> ] [ <i>files &#8230;</i> ]</p>
<h2>DESCRIPTION</h2>
<p> <i>GNU Emacs</i> is a version of <i>Emacs</i>, written by the author of the original (PDP-10) <i>Emacs</i>, Richard Stallman. The user functionality of GNU Emacs encompasses everything other editors do, and it is easily extensible since its editing commands are written in Lisp. </p>
<p> The primary documentation of GNU Emacs is in the GNU Emacs Manual, which you can read using Info, either from Emacs or as a standalone program. Please look there for complete and up-to-date documentation. This man page is updated only when someone volunteers to do so. </p>
<p> <i>Emacs</i> has an extensive interactive help facility, but the facility assumes that you know how to manipulate <i>Emacs</i> windows and buffers. CTRL-h or F1 enters the Help facility. Help Tutorial (CTRL-h t) starts an interactive tutorial to quickly teach beginners the fundamentals of <i>Emacs.</i> Help Apropos (CTRL-h a) helps you find a command with a name matching a given pattern, Help Key (CTRL-h k) describes a given key sequence, and Help Function (CTRL-h f) describes a given Lisp function. </p>
<p> <i>GNU Emacs</i>&#8216;s many special packages handle mail reading (RMail) and sending (Mail), outline editing (Outline), compiling (Compile), running subshells within <i>Emacs</i> windows (Shell), running a Lisp read-eval-print loop (Lisp-Interaction-Mode), automated psychotherapy (Doctor), and much more.</p>
<h3>Emacs Options</h3>
<p> The following options are of general interest:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>file</i></p>
<dd> Edit <i>file</i>.</p>
<dt><code>&#8211;file=</code><i>file</i>, <code>&#8211;find-file=</code><i>file</i>, <code>&#8211;visit=</code><i>file</i></p>
<dd> The same as specifying <i>file</i> directly as an argument.</p>
<dt><code>+</code><i>number</i></p>
<dd> Go to the line specified by <i>number</i> (do not insert a space between the &quot;+&quot; sign and the number). This applies only to the next file specified.</p>
<dt><code>+</code><i>line:column</i></p>
<dd> Go to the specified <i>line</i> and <i>column</i>.</p>
<dt><code>&#8211;chdir=</code><i>directory</i></p>
<dd> Change to <i>directory</i>.</p>
<dt><code>-q</code>, <code>&#8211;no-init-file</code></p>
<dd> Do not load an init file.</p>
<dt><code>-nl</code>, <code>&#8211;no-shared-memory</code></p>
<dd> Do not use shared memory.</p>
<dt><code>&#8211;no-site-file</code></p>
<dd> Do not load the site-wide startup file.</p>
<dt><code>-nsl</code>, <code>&#8211;no-site-lisp</code></p>
<dd> Do not add site-lisp directories to load-path.</p>
<dt><code>&#8211;no-desktop</code></p>
<dd> Do not load a saved desktop.</p>
<dt><code>-Q</code>, <code>&#8211;quick</code></p>
<dd> Similar to &quot;-q &#8211;no-site-file &#8211;no-splash&quot;. Also, avoid processing X resources.</p>
<dt><code>&#8211;no-splash</code></p>
<dd> Do not display a splash screen during start-up.</p>
<dt><code>&#8211;debug-init</code></p>
<dd> Enable <i>Emacs</i> Lisp debugger during the processing of the user init file <code>~/.emacs</code>. This is useful for debugging problems in the init file.</p>
<dt><code>-u</code><i> user</i>, <code>&#8211;user=</code><i>user</i></p>
<dd> Load <i>user</i>&#8216;s init file.</p>
<dt><code>-t</code><i> file</i>, <code>&#8211;terminal=</code><i>file</i></p>
<dd> Use specified <i>file</i> as the terminal instead of using stdin/stdout. This must be the first argument specified in the command line.</p>
<dt><code>&#8211;daemon</code><i></i>[=name], <code>&#8211;bg-daemon</code><i></i>[=name]</p>
<dd> Start Emacs as a daemon, enabling the Emacs server and disconnecting from the terminal. You can then use the emacsclient (see <code><a href="/docs/linux/man/1-emacsclient/">emacsclient</a></code>(1)) command to connect to the server (with optional <i>name</i>).</p>
<dt><code>&#8211;fg-daemon</code><i></i>[=name]</p>
<dd> Like &quot;&#8211;bg-daemon&quot;, but don&#8217;t disconnect from the terminal.</p>
<dt><code>&#8211;version</code></p>
<dd> Display <i>Emacs</i> version information and exit.</p>
<dt><code>&#8211;help</code></p>
<dd> Display this help and exit.</dl>
</dl>
<p> The following options are Lisp-oriented (these options are processed in the order encountered):</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-f</code><i> function</i>, <code>&#8211;funcall=</code><i>function</i></p>
<dd> Execute the lisp function <i>function</i>.</p>
<dt><code>-l</code><i> file</i>, <code>&#8211;load=</code><i>file</i></p>
<dd> Load the lisp code in the file <i>file</i>.</p>
<dt><code>&#8211;eval=</code><i>expr</i>, <code>&#8211;execute=</code><i>expr</i></p>
<dd> Evaluate the Lisp expression <i>expr</i>.</dl>
</dl>
<p> The following options are useful when running <i>Emacs</i> as a batch editor:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;batch</code></p>
<dd> Edit in batch mode. The editor will send messages to stderr. You must use -l and -f options to specify files to execute and functions to call.</p>
<dt><code>&#8211;script=</code><i>file</i></p>
<dd> Run <i>file</i> as an Emacs Lisp script.</p>
<dt><code>&#8211;insert=</code><i>file</i></p>
<dd> Insert contents of <i>file</i> into the current buffer.</p>
<dt><code>&#8211;kill</code></p>
<dd> Exit <i>Emacs</i> while in batch mode.</p>
<dt><code>-L</code><i> dir</i>, <code>&#8211;directory=</code><i>dir</i></p>
<dd> Add <i>dir</i> to the list of directories <i>Emacs</i> searches for Lisp files.</dl>
</dl>
<h3>Using Emacs with X</h3>
<p> <i>Emacs</i> has been tailored to work well with the X window system. If you run <i>Emacs</i> from under X windows, it will create its own X window to display in. You will probably want to start the editor as a background process so that you can continue using your original window. </p>
<p> <i>Emacs</i> can be started with the following X switches:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Specify the name which should be assigned to the initial <i>Emacs</i> window. This controls looking up X resources as well as the window title.</p>
<dt><code>-T</code><i> name</i>, <code>&#8211;title=</code><i>name</i></p>
<dd> Specify the title for the initial X window.</p>
<dt><code>-r</code>, <code>-rv</code>, <code>&#8211;reverse-video</code></p>
<dd> Display the <i>Emacs</i> window in reverse video.</p>
<dt><code>-fn</code><i> font</i>, <code>&#8211;font=</code><i>font</i></p>
<dd> Set the <i>Emacs</i> window&#8217;s font to that specified by <i>font</i>. You will find the various <i>X</i> fonts in the <i>/usr/lib/X11/fonts</i> directory. Note that <i>Emacs</i> will only accept fixed width fonts. Under the X11 Release 4 font-naming conventions, any font with the value &quot;m&quot; or &quot;c&quot; in the eleventh field of the font name is a fixed width font. Furthermore, fonts whose name are of the form <i>width</i>x<i>height</i> are generally fixed width, as is the font <i>fixed</i>. See <code><a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a></code>(1) for more information. </p>
<p> When you specify a font, be sure to put a space between the switch and the font name.</p>
<dt><code>&#8211;xrm=</code><i>resources</i></p>
<dd> Set additional X resources.</p>
<dt><code>&#8211;color</code>, &#8211;color=<i>mode</i></p>
<dd> Override color mode for character terminals; <i>mode</i> defaults to &quot;auto&quot;, and can also be &quot;never&quot;, &quot;auto&quot;, &quot;always&quot;, or a mode name like &quot;ansi8&quot;.</p>
<dt><code>-bw</code><i> pixels</i>, <code>&#8211;border-width=</code><i>pixels</i></p>
<dd> Set the <i>Emacs</i> window&#8217;s border width to the number of pixels specified by <i>pixels</i>. Defaults to one pixel on each side of the window.</p>
<dt><code>-ib</code><i> pixels</i>, <code>&#8211;internal-border=</code><i>pixels</i></p>
<dd> Set the window&#8217;s internal border width to the number of pixels specified by <i>pixels</i>. Defaults to one pixel of padding on each side of the window.</p>
<dt><code>-g</code><i> geometry</i>, <code>&#8211;geometry=</code><i>geometry</i></p>
<dd> Set the <i>Emacs</i> window&#8217;s width, height, and position as specified. The geometry specification is in the standard X format; see <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for more information. The width and height are specified in characters; the default for GUI frames is 80 by 36. See the Emacs manual, section &quot;Options for Window Size and Position&quot;, for information on how window sizes interact with selecting or deselecting the tool bar and menu bar.</p>
<dt><code>-lsp</code><i> pixels</i>, <code>&#8211;line-spacing=</code><i>pixels</i></p>
<dd> Additional space to put between lines.</p>
<dt><code>-vb</code>, <code>&#8211;vertical-scroll-bars</code></p>
<dd> Enable vertical scrollbars.</p>
<dt><code>-fh</code>, <code>&#8211;fullheight</code></p>
<dd> Make the first frame as high as the screen.</p>
<dt><code>-fs</code>, <code>&#8211;fullscreen</code></p>
<dd> Make the first frame fullscreen.</p>
<dt><code>-fw</code>, <code>&#8211;fullwidth</code></p>
<dd> Make the first frame as wide as the screen.</p>
<dt><code>-mm</code>, <code>&#8211;maximized</code></p>
<dd> Maximize the first frame, like &quot;-fw -fh&quot;.</p>
<dt><code>-fg</code><i> color</i>, <code>&#8211;foreground-color=</code><i>color</i></p>
<dd> On color displays, set the color of the text. </p>
<p> Use the command <i>M-x list-colors-display</i> for a list of valid color names.</p>
<dt><code>-bg</code><i> color</i>, <code>&#8211;background-color=</code><i>color</i></p>
<dd> On color displays, set the color of the window&#8217;s background.</p>
<dt><code>-bd</code><i> color</i>, <code>&#8211;border-color=</code><i>color</i></p>
<dd> On color displays, set the color of the window&#8217;s border.</p>
<dt><code>-cr</code><i> color</i>, <code>&#8211;cursor-color=</code><i>color</i></p>
<dd> On color displays, set the color of the window&#8217;s text cursor.</p>
<dt><code>-ms</code><i> color</i>, <code>&#8211;mouse-color=</code><i>color</i></p>
<dd> On color displays, set the color of the window&#8217;s mouse cursor.</p>
<dt><code>-d</code><i> displayname</i>, <code>&#8211;display=</code><i>displayname</i></p>
<dd> Create the <i>Emacs</i> window on the display specified by <i>displayname</i>. Must be the first option specified in the command line.</p>
<dt><code>-nbi</code>, <code>&#8211;no-bitmap-icon</code></p>
<dd> Do not use picture of gnu for Emacs icon.</p>
<dt><code>&#8211;iconic</code></p>
<dd> Start <i>Emacs</i> in iconified state.</p>
<dt><code>-nbc</code>, <code>&#8211;no-blinking-cursor</code></p>
<dd> Disable blinking cursor.</p>
<dt><code>&#8211;parent-id=</code><i>xid</i></p>
<dd> Set parent window.</p>
<dt><code>-nw</code>, <code>&#8211;no-window-system</code></p>
<dd> Tell <i>Emacs</i> not to create a graphical frame. If you use this switch when invoking <i>Emacs</i> from an <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1) window, display is done in that window.</p>
<dt><code>-D</code>, <code>&#8211;basic-display</code></p>
<dd> This option disables many display features; use it for debugging Emacs.</dl>
</dl>
<p> You can set <i>X</i> default values for your <i>Emacs</i> windows in your <i>.Xresources</i> file (see <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1)). Use the following format:</p>
<dl>
<dt>
<dd> emacs.<i>keyword</i>:<i>value</i></dl>
<p> where <i>value</i> specifies the default value of <i>keyword</i>. <i>Emacs</i> lets you set default values for the following keywords:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>background</code> (class <code>Background</code>)</p>
<dd> For color displays, sets the window&#8217;s background color.</p>
<dt><code>bitmapIcon</code> (class <code>BitmapIcon</code>)</p>
<dd> If <code>bitmapIcon</code>&#8216;s value is set to <i>on</i>, the window will iconify into the &quot;kitchen sink.&quot;</p>
<dt><code>borderColor</code> (class <code>BorderColor</code>)</p>
<dd> For color displays, sets the color of the window&#8217;s border.</p>
<dt><code>borderWidth</code> (class <code>BorderWidth</code>)</p>
<dd> Sets the window&#8217;s border width in pixels.</p>
<dt><code>cursorColor</code> (class <code>Foreground</code>)</p>
<dd> For color displays, sets the color of the window&#8217;s text cursor.</p>
<dt><code>cursorBlink</code> (class <code>CursorBlink</code>)</p>
<dd> Specifies whether to make the cursor blink. The default is <i>on</i>. Use <i>off</i> or <i>false</i> to turn cursor blinking off.</p>
<dt><code>font</code> (class <code>Font</code>)</p>
<dd> Sets the window&#8217;s text font.</p>
<dt><code>foreground</code> (class <code>Foreground</code>)</p>
<dd> For color displays, sets the window&#8217;s text color.</p>
<dt><code>fullscreen</code> (class <code>Fullscreen</code>)</p>
<dd> The desired fullscreen size. The value can be one of <i>fullboth</i>, <i>maximized</i>, <i>fullwidth</i>, or <i>fullheight</i>, which correspond to the command-line options &quot;-fs&quot;, &quot;-mm&quot;, &quot;-fw&quot;, and &quot;-fh&quot;, respectively. Note that this applies to the initial frame only.</p>
<dt><code>geometry</code> (class <code>Geometry</code>)</p>
<dd> Sets the geometry of the <i>Emacs</i> window (as described above).</p>
<dt><code>iconName</code> (class <code>Title</code>)</p>
<dd> Sets the icon name for the <i>Emacs</i> window icon.</p>
<dt><code>internalBorder</code> (class <code>BorderWidth</code>)</p>
<dd> Sets the window&#8217;s internal border width in pixels.</p>
<dt><code>lineSpacing</code> (class <code>LineSpacing</code>)</p>
<dd> Additional space (&quot;leading&quot;) between lines, in pixels.</p>
<dt><code>menuBar</code> (class <code>MenuBar</code>)</p>
<dd> Gives frames menu bars if <i>on</i>; don&#8217;t have menu bars if <i>off</i>. See the Emacs manual, sections &quot;Lucid Resources&quot; and &quot;Motif Resources&quot;, for how to control the appearance of the menu bar if you have one.</p>
<dt><code>minibuffer</code> (class <code>Minibuffer</code>)</p>
<dd> If <i>none</i>, don&#8217;t make a minibuffer in this frame. It will use a separate minibuffer frame instead.</p>
<dt><code>paneFont</code> (class <code>Font</code>)</p>
<dd> Font name for menu pane titles, in non-toolkit versions of <i>Emacs</i>.</p>
<dt><code>pointerColor</code> (class <code>Foreground</code>)</p>
<dd> For color displays, sets the color of the window&#8217;s mouse cursor.</p>
<dt><code>privateColormap</code> (class <code>PrivateColormap</code>)</p>
<dd> If <i>on</i>, use a private color map, in the case where the &quot;default visual&quot; of class <code>PseudoColor</code> and <code>Emacs</code> is using it.</p>
<dt><code>reverseVideo</code> (class <code>ReverseVideo</code>)</p>
<dd> If <code>reverseVideo</code>&#8216;s value is set to <i>on</i>, the window will be displayed in reverse video.</p>
<dt><code>screenGamma</code> (class ScreenGamma<code>)</code></p>
<dd> Gamma correction for colors, equivalent to the frame parameter &quot;screen-gamma&quot;.</p>
<dt><code>scrollBarWidth</code> (class ScrollBarWidth<code>)</code></p>
<dd> The scroll bar width in pixels, equivalent to the frame parameter &quot;scroll-bar-width&quot;.</p>
<dt><code>selectionFont</code> (class <code>SelectionFont</code>)</p>
<dd> Font name for pop-up menu items, in non-toolkit versions of <i>Emacs</i>. (For toolkit versions, see the Emacs manual, sections &quot;Lucid Resources&quot; and &quot;Motif Resources&quot;.)</p>
<dt><code>selectionTimeout</code> (class <code>SelectionTimeout</code>)</p>
<dd> Number of milliseconds to wait for a selection reply. A value of 0 means wait as long as necessary.</p>
<dt><code>synchronous</code> (class <code>Synchronous</code>)</p>
<dd> Run Emacs in synchronous mode if <i>on</i>. Synchronous mode is useful for debugging X problems.</p>
<dt><code>title</code> (class <code>Title</code>)</p>
<dd> Sets the title of the <i>Emacs</i> window.</p>
<dt><code>toolBar</code> (class <code>ToolBar</code>)</p>
<dd> Number of lines to reserve for the tool bar.</p>
<dt><code>useXIM</code> (class <code>UseXIM</code>)</p>
<dd> Turns off use of X input methods (XIM) if <i>false</i> or <i>off</i>.</p>
<dt><code>verticalScrollBars</code> (class <code>ScrollBars</code>)</p>
<dd> Gives frames scroll bars if <i>on</i>; suppresses scroll bars if <i>off</i>.</p>
<dt><code>visualClass</code> (class <code>VisualClass</code>)</p>
<dd> Specify the &quot;visual&quot; that X should use. This tells X how to handle colors. The value should start with one of <i>TrueColor</i>, <i>PseudoColor</i>, <i>DirectColor</i>, <i>StaticColor</i>, <i>GrayScale</i>, and <i>StaticGray</i>, followed by <code>&#8211;</code><i>depth</i>, where <i>depth</i> is the number of color planes.</dl>
</dl>
<h2>MANUALS</h2>
<p> You can order printed copies of the GNU Emacs Manual from the Free Software Foundation, which develops GNU software. See the online store at &lt;<a rel="nofollow" href="https://shop.fsf.org/">https://shop.fsf.org/</a>&gt;.<br />
 Your local administrator might also have copies available. As with all software and publications from FSF, everyone is permitted to make and distribute copies of the Emacs manual. The Texinfo source to the manual is also included in the Emacs source distribution.</p>
<h2>FILES</h2>
<p> /usr/local/share/info &#8212; files for the Info documentation browser. The complete text of the Emacs reference manual is included in a convenient tree structured form. Also includes the Emacs Lisp Reference Manual, useful to anyone wishing to write programs in the Emacs Lisp extension language, and the Introduction to Programming in Emacs Lisp. </p>
<p> /usr/local/share/emacs/$VERSION/lisp &#8212; Lisp source files and compiled files that define most editing commands. Some are preloaded; others are autoloaded from this directory when used. </p>
<p> /usr/local/libexec/emacs/$VERSION/$ARCH &#8212; various programs that are used with GNU Emacs. </p>
<p> /usr/local/share/emacs/$VERSION/etc &#8212; various files of information. </p>
<p> /usr/local/share/emacs/$VERSION/etc/DOC.* &#8212; contains the documentation strings for the Lisp primitives and preloaded Lisp functions of GNU Emacs. They are stored here to reduce the size of Emacs proper. </p>
<h2>BUGS</h2>
<p> There is a mailing list, bug-gnu-emacs [at] gnu.org, for reporting Emacs bugs and fixes. But before reporting something as a bug, please try to be sure that it really is a bug, not a misunderstanding or a deliberate feature. We ask you to read the section &quot;Reporting Bugs&quot; in the Emacs manual for hints on how and when to report bugs. Also, include the version number of the Emacs you are running in <i>every</i> bug report that you send in. Bugs tend actually to be fixed if they can be isolated, so it is in your interest to report them in such a way that they can be easily reproduced. </p>
<p> Do not expect a personal answer to a bug report. The purpose of reporting bugs is to get them fixed for everyone in the next release, if possible. For personal assistance, consult the service directory at &lt;<a rel="nofollow" href="https://www.fsf.org/resources/service/">https://www.fsf.org/resources/service/</a>&gt; for a list of people who offer it. </p>
<p> Please do not send anything but bug reports to this mailing list. For other Emacs lists, see &lt;<a rel="nofollow" href="https://savannah.gnu.org/mail/?group=emacs">https://savannah.gnu.org/mail/?group=emacs</a>&gt;.</p>
<h2>UNRESTRICTIONS</h2>
<p> <i>Emacs</i> is free; anyone may redistribute copies of <i>Emacs</i> to anyone under the terms stated in the GNU General Public License, a copy of which accompanies each copy of <i>Emacs</i> and which also appears in the reference manual. </p>
<p> Copies of <i>Emacs</i> may sometimes be received packaged with distributions of Unix systems, but it is never included in the scope of any license covering those systems. Such inclusion violates the terms on which distribution is permitted. In fact, the primary purpose of the GNU General Public License is to prohibit anyone from attaching any other restrictions to redistribution of <i>Emacs</i>. </p>
<p> Richard Stallman encourages you to improve and extend <i>Emacs</i>, and urges that you contribute your extensions to the GNU library. Eventually GNU (Gnu&#8217;s Not Unix) will be a complete replacement for Unix. Everyone will be free to use, copy, study and change the GNU system.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-emacsclient/">emacsclient</a></code>(1), <code><a href="/docs/linux/man/1-etags/">etags</a></code>(1), <code><a href="/docs/linux/man/7-x/">X</a></code>(7), <code><a href="/docs/linux/man/1-xlsfonts/">xlsfonts</a></code>(1), <code><a href="/docs/linux/man/1-xterm/">xterm</a></code>(1), <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> <i>Emacs</i> was written by Richard Stallman and the Free Software Foundation. For detailed credits and acknowledgments, see the GNU Emacs manual.</p>
<h2>COPYING</h2>
<p> Copyright 1995, 1999-2019 Free Software Foundation, Inc. </p>
<p> Permission is granted to make and distribute verbatim copies of this document provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this document under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this document into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by the Free Software Foundation. </p>
<h2>Index</h2>
