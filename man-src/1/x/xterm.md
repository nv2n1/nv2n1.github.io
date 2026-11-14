---
title: "xterm(1)"
name: "xterm"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xterm/"
description: "xterm – terminal emulator for X"
---

<h2 class="name">NAME</h2>
<p> xterm &#8211; terminal emulator for X </p>
<h2>SYNOPSIS</h2>
<p> <code>xterm</code> [-<i>toolkitoption</i> &#8230;] [-<i>option</i> &#8230;] [<i>shell</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xterm</i> program is a terminal emulator for the X Window System. It provides DEC VT102/VT220 and selected features from higher-level terminals such as VT320/VT420/VT520 (VT<i>xxx</i>). It also provides Tektronix 4014 emulation for programs that cannot use the window system directly. If the underlying operating system supports terminal resizing capabilities (for example, the SIGWINCH signal in systems derived from 4.3BSD), <i>xterm</i> will use the facilities to notify programs running in the window whenever it is resized. </p>
<p> The VT<i>xxx</i> and Tektronix 4014 terminals each have their own window so that you can edit text in one and look at graphics in the other at the same time. To maintain the correct aspect ratio (height/width), Tektronix graphics will be restricted to the largest box with a 4014&#8217;s aspect ratio that will fit in the window. This box is located in the upper left area of the window. </p>
<p> Although both windows may be displayed at the same time, one of them is considered the &#8220;active&#8221; window for receiving keyboard input and terminal output. This is the window that contains the text cursor. The active window can be chosen through escape sequences, the <code>VT Options</code> menu in the VT<i>xxx</i> window, and the <code>Tek Options</code> menu in the 4014 window.</p>
<h2>EMULATIONS</h2>
<p> <i>Xterm</i> provides usable emulations of related DEC terminals:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 VT52 emulation is complete.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 VT102 emulation is fairly complete, but does not support autorepeat (because that would affect the keyboard used by other X clients).</p>
<dl>
<dt>
<dd> Double-size characters are displayed properly if your font server supports scalable bitmap fonts.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 VT220 emulation does not support soft fonts, it is otherwise complete.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 VT420 emulation (the default) supports controls for manipulating rectangles of characters as well as left/right margins.</p>
<dt>
<dd> <i>Xterm</i> does not support some other features which are not suitable for emulation, e.g., two-sessions.</dl>
<p> Terminal database (<i>terminfo</i> (5) or <i>termcap</i> (5)) entries that work with <i>xterm</i> include</p>
<dl>
<dt>
<dd> an optional platform-specific entry (&#8220;xterm&#8221;),<br />
 &#8220;xterm&#8221;,<br />
 &#8220;vt102&#8221;,<br />
 &#8220;vt100&#8221;,<br />
 &#8220;ansi&#8221; and<br />
 &#8220;dumb&#8221;</dl>
<p> <i>Xterm</i> automatically searches the terminal database in this order for these entries and then sets the &#8220;TERM&#8221; variable (and the &#8220;TERMCAP&#8221; environment variable on a few older systems). The alternatives after &#8220;xterm&#8221; are very old, from the late 1980s. </p>
<p> VT100 and VT102 emulations are commonly equated, though they actually differ. The VT102 provided controls for inserting and deleting lines. </p>
<p> Similarly, &#8220;ansi&#8221; and &#8220;vt100&#8221; are often equated. These are not really the same. For instance, they use different controls for scrolling (but <i>xterm</i> supports both). These features differ in an &#8220;ansi&#8221; terminal description from <i>xterm</i>:</p>
<dl>
<dt><code>acsc</code></p>
<dd>
 Pseudo-graphics (line-drawing) uses a different mapping.</p>
<dt><code>xenl</code></p>
<dd>
 <i>Xterm</i> wraps text at the right margin using the VT100 &#8220;newline glitch&#8221; behavior.</dl>
<p> Because of the wrapping behavior, you would occasionally have to repaint the screen when using a text editor with the &#8220;ansi&#8221; description. </p>
<p> You may also use descriptions corresponding to the various supported emulations such as &#8220;vt220&#8221; or &#8220;vt420&#8221;, but should set the terminal emulation level with the <code>decTerminalID</code> resource. </p>
<p> On most systems, <i>xterm</i> will use the terminfo database. Some older systems use termcap. (The &#8220;TERMCAP&#8221; environment variable is not set if <i>xterm</i> is linked against a terminfo library, since the requisite information is not provided by the termcap emulation of terminfo libraries). </p>
<p> Many of the special <i>xterm</i> features may be modified under program control through a set of escape sequences different from the standard VT<i>xxx</i> escape sequences (see <i>Xterm Control Sequences</i>). </p>
<p> The Tektronix 4014 emulation is also fairly good. It supports 12-bit graphics addressing, scaled to the window size. Four different font sizes and five different lines types are supported. There is no write-through or defocused mode support. The Tektronix text and graphics commands are recorded internally by <i>xterm</i> and may be written to a file by sending the COPY escape sequence (or through the <code>Tektronix</code> menu; see below). The name of the file will be<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
``COPY<i>yyyy</i>-<i>MM</i>-<i>dd</i>.<i>hh</i>:<i>mm</i>:<i>ss</i>''
</pre>
<p>&nbsp;.in -4 </p>
<p> where <i>yyyy</i>, <i>MM</i>, <i>dd</i>, <i>hh</i>, <i>mm</i> and <i>ss</i> are the year, month, day, hour, minute and second when the COPY was performed (the file is created in the directory <i>xterm</i> is started in, or the home directory for a login <i>xterm</i>). </p>
<p> Not all of the features described in this manual are necessarily available in this version of <i>xterm</i>. Some (e.g., the non-VT220 extensions) are available only if they were compiled in, though the most commonly-used are in the default configuration.</p>
<h2>OTHER FEATURES</h2>
<p> <i>Xterm</i> automatically highlights the text cursor when the pointer enters the window (selected) and unhighlights it when the pointer leaves the window (unselected). If the window is the focus window, then the text cursor is highlighted no matter where the pointer is. </p>
<p> In VT<i>xxx</i> mode, there are escape sequences to activate and deactivate an alternate screen buffer, which is the same size as the display area of the window. When activated, the current screen is saved and replaced with the alternate screen. Saving of lines scrolled off the top of the window is disabled until the normal screen is restored. The usual terminal description for <i>xterm</i> allows the visual editor <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) to switch to the alternate screen for editing and to restore the screen on exit. A popup menu entry makes it simple to switch between the normal and alternate screens for cut and paste. </p>
<p> In either VT<i>xxx</i> or Tektronix mode, there are escape sequences to change the name of the windows. Additionally, in VT<i>xxx</i> mode, <i>xterm</i> implements the window-manipulation control sequences from <i>dtterm</i>, such as resizing the window, setting its location on the screen. </p>
<p> <i>Xterm</i> allows character-based applications to receive mouse events (currently button-press and release events, and button-motion events) as keyboard control sequences. See <i>Xterm Control Sequences</i> for details.</p>
<h2>OPTIONS</h2>
<p> Because <i>xterm</i> uses the X Toolkit library, it accepts the standard X Toolkit command line options. <i>Xterm</i> also accepts many application-specific options. </p>
<p> By convention, if an option begins with a &#8220;<code>+</code>&#8221; instead of a &#8220;<code>&#8211;</code>&#8221;, the option is restored to its default value. </p>
<p> Most of the <i>xterm</i> options are actually parsed by the X Toolkit, which sets resource values, and overrides corresponding resource-settings in your X resource files. <i>Xterm</i> provides the X Toolkit with a table of options. A few of these are marked, telling the X Toolkit to ignore them (<code>-help</code>, <code>-version</code>, <code>-class</code>, <code>-e</code>, and <code>-into</code>). After the X Toolkit has parsed the command-line parameters, it removes those which it handles, leaving the specially-marked parameters for <i>xterm</i> to handle. </p>
<p> These options do not set a resource value, and are handled specially:</p>
<dl>
<dt><code>-version</code></p>
<dd> This causes <i>xterm</i> to print a version number to the standard output, and then exit.</p>
<dt><code>-help</code></p>
<dd> This causes <i>xterm</i> to print out a verbose message describing its options, one per line. The message is written to the standard output. After printing the message, <i>xterm</i> exits. <i>Xterm</i> generates this message, sorting it and noting whether a &#8220;<code>&#8211;</code><i>option</i>&#8221; or a &#8220;<code>+</code><i>option</i>&#8221; turns the feature on or off, since some features historically have been one or the other. <i>Xterm</i> generates a concise help message (multiple options per line) when an unknown option is used, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
xterm -z
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> If the logic for a particular option such as logging is not compiled into <i>xterm</i>, the help text for that option also is not displayed by the <code>-help</code> option.</dl>
<p> The <code>-version</code> and <code>-help</code> options are interpreted even if <i>xterm</i> cannot open the display, and are useful for testing and configuration scripts. Along with <code>-class</code>, they are checked before other options. To do this, <i>xterm</i> has its own (much simpler) argument parser, along with a table of the X Toolkit&#8217;s built-in list of options. </p>
<p> Relying upon the X Toolkit to parse the options and associated values has the advantages of simplicity and good integration with the X resource mechanism. There are a few drawbacks<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> cannot tell easily whether a resource value was set by one of the external resource- or application-defaults files, whether it was set using <code><a href="/docs/linux/man/1-xrdb/">xrdb</a></code>(1), or if it was set through the <code>-xrm</code> option or via some directly relevant command-line option. <i>Xterm</i> sees only the end-result: a value supplied when creating its widgets.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> does not know the order in which particular options and items in resource files are evaluated. Rather, it sees all of the values for a given widget at the same time. In the design of these options, some are deemed more important, and can override other options.</p>
<dl>
<dt>
<dd> The X Toolkit uses patterns (constants and wildcards) to match resources. Once a particular pattern has been used, it will not modify it. To override a given setting, a more-specific pattern must be used, e.g., replacing &#8220;*&#8221; with &#8220;.&#8221;. Some poorly-designed resource files are too specific to allow the command-line options to affect the relevant widget values.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 In a few cases, the X Toolkit combines its standard options in ways which do not work well with <i>xterm</i>. This happens with the color (<code>-fg</code>, <code>-bg</code>) and reverse (<code>-rv</code>) options. <i>Xterm</i> makes a special case of these and adjusts its sense of &#8220;reverse&#8221; to lessen user surprise.</dl>
<p> One parameter (after all options) may be given. That overrides <i>xterm</i>&#8216;s built-in choice of shell program:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the parameter is not a relative path, i.e., beginning with &#8220;./&#8221; or &#8220;../&#8221;, <i>xterm</i> looks for the file in the user&#8217;s PATH. In either case, this check fails if <i>xterm</i> cannot construct an absolute path.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If that check fails (or if no such parameter is given), <i>xterm</i> next checks the &#8220;SHELL&#8221; variable. If that specifies an executable file, <i>xterm</i> will attempt to start that. However, <i>xterm</i> additionally checks if it is a valid shell, and will unset &#8220;SHELL&#8221; if it is not.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;SHELL&#8221; is not set to an executable file, <i>xterm</i> tries to use the shell program specified in the user&#8217;s password file entry. As before, <i>xterm</i> verifies if this is a valid shell.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Finally, if the password file entry does not specify a valid shell, <i>xterm</i> uses <i>/bin/sh</i>. </p>
<p> The <code>-e</code> option cannot be used with this parameter since it uses all parameters following the option. </p>
<p> <i>Xterm</i> validates shell programs by finding their pathname in the text file <code>/etc/shells</code>. It treats the environment variable &#8220;SHELL&#8221; specially because (like &#8220;TERM&#8221;), <i>xterm</i> both reads and updates the variable, and because the program started by <i>xterm</i> is not necessarily a shell. </p>
<p> The other options are used to control the appearance and behavior. Not all options are necessarily configured into your copy of <i>xterm</i>:</p>
<dl>
<dt><code>-132</code></p>
<dd> Normally, the VT102 DECCOLM escape sequence that switches between 80 and 132 column mode is ignored. This option causes the DECCOLM escape sequence to be recognized, and the <i>xterm</i> window will resize appropriately.</p>
<dt><code>-ah</code></p>
<dd> This option indicates that <i>xterm</i> should always highlight the text cursor. By default, <i>xterm</i> will display a hollow text cursor whenever the focus is lost or the pointer leaves the window.</p>
<dt><code>+ah</code></p>
<dd> This option indicates that <i>xterm</i> should do text cursor highlighting based on focus.</p>
<dt><code>-ai</code></p>
<dd> This option disables active icon support if that feature was compiled into <i>xterm</i>. This is equivalent to setting the <i>vt100</i> resource <code>activeIcon</code> to &#8220;false&#8221;.</p>
<dt><code>+ai</code></p>
<dd> This option enables active icon support if that feature was compiled into <i>xterm</i>. This is equivalent to setting the <i>vt100</i> resource <code>activeIcon</code> to &#8220;true&#8221;.</p>
<dt><code>-aw</code></p>
<dd> This option indicates that auto-wraparound should be allowed, and is equivalent to setting the <i>vt100</i> resource <code>autoWrap</code> to &#8220;true&#8221;.</p>
<dt>
<dd> Auto-wraparound allows the cursor to automatically wrap to the beginning of the next line when it is at the rightmost position of a line and text is output.</p>
<dt><code>+aw</code></p>
<dd> This option indicates that auto-wraparound should not be allowed, and is equivalent to setting the <i>vt100</i> resource <code>autoWrap</code> to &#8220;false&#8221;.</p>
<dt><code>-b</code><i> number</i></p>
<dd> This option specifies the size of the inner border (the distance between the outer edge of the characters and the window border) in pixels. That is the <i>vt100</i> <code>internalBorder</code> resource. The default is &#8220;2&#8221;.</p>
<dt><code>-baudrate</code><i> number</i></p>
<dd> Set the line-speed, used to test the behavior of applications that use the line-speed when optimizing their output to the screen. The default is &#8220;38400&#8221;.</p>
<dt><code>-bc</code></p>
<dd> turn on text cursor blinking. This overrides the <code>cursorBlink</code> resource.</p>
<dt><code>+bc</code></p>
<dd> turn off text cursor blinking. This overrides the <code>cursorBlink</code> resource.</p>
<dt><code>-bcf</code><i> milliseconds</i></p>
<dd> set the amount of time text cursor is off when blinking via the <code>cursorOffTime</code> resource.</p>
<dt><code>-bcn</code><i> milliseconds</i></p>
<dd> set the amount of time text cursor is on when blinking via the <code>cursorOnTime</code> resource.</p>
<dt><code>-bdc</code></p>
<dd> Set the <i>vt100</i> resource <code>colorBDMode</code> to &#8220;false&#8221;, disabling the display of characters with bold attribute as color.</p>
<dt><code>+bdc</code></p>
<dd> Set the <i>vt100</i> resource <code>colorBDMode</code> to &#8220;true&#8221;, enabling the display of characters with bold attribute as color rather than bold.</p>
<dt><code>-cb</code></p>
<dd> Set the <i>vt100</i> resource <code>cutToBeginningOfLine</code> to &#8220;false&#8221;.</p>
<dt><code>+cb</code></p>
<dd> Set the <i>vt100</i> resource <code>cutToBeginningOfLine</code> to &#8220;true&#8221;.</p>
<dt><code>-cc </code><i>characterclassrange</i>:<i>value</i>[, &#8230;]</p>
<dd> This sets classes indicated by the given ranges for using in selecting by words (see <code>CHARACTER CLASSES</code> and the <code>charClass</code> resource).</p>
<dt><code>-cjk_width</code></p>
<dd> Set the <code>cjkWidth</code> resource to &#8220;true&#8221;. When turned on, characters with East Asian Ambiguous (A) category in UTR 11 have a column width of 2. Otherwise, they have a column width of 1. This may be useful for some legacy CJK text terminal-based programs assuming box drawings and others to have a column width of 2. It also should be turned on when you specify a TrueType CJK double-width (bi-width/monospace) font either with <code>-fa</code> at the command line or <code>faceName</code> resource. The default is &#8220;false&#8221;</p>
<dt><code>+cjk_width</code></p>
<dd> Reset the <code>cjkWidth</code> resource.</p>
<dt><code>-class</code><i> string</i></p>
<dd> This option allows you to override <i>xterm</i>&#8216;s resource class. Normally it is &#8220;XTerm&#8221;, but can be set to another class such as &#8220;UXTerm&#8221; to override selected resources.</p>
<dt>
<dd> X Toolkit sets the <code>WM_CLASS</code> property using the instance name and this class value.</p>
<dt><code>-cm</code></p>
<dd> This option disables recognition of ANSI color-change escape sequences. It sets the <code>colorMode</code> resource to &#8220;false&#8221;.</p>
<dt><code>+cm</code></p>
<dd> This option enables recognition of ANSI color-change escape sequences. This is the same as the <i>vt100</i> resource <code>colorMode</code>.</p>
<dt><code>-cn</code></p>
<dd> This option indicates that newlines should not be cut in line-mode selections. It sets the <code>cutNewline</code> resource to &#8220;false&#8221;.</p>
<dt><code>+cn</code></p>
<dd> This option indicates that newlines should be cut in line-mode selections. It sets the <code>cutNewline</code> resource to &#8220;true&#8221;.</p>
<dt><code>-cr</code><i> color</i></p>
<dd> This option specifies the color to use for text cursor. The default is to use the same foreground color that is used for text. It sets the <code>cursorColor</code> resource according to the parameter.</p>
<dt><code>-cu</code></p>
<dd> This option indicates that <i>xterm</i> should work around a bug in the <i><a href="/docs/linux/man/1-more/">more</a></i>(1) program that causes it to incorrectly display lines that are exactly the width of the window and are followed by a line beginning with a tab (the leading tabs are not displayed). This option is so named because it was originally thought to be a bug in the <i><a href="//www.systutorials.com/docs/linux/man/3x-curses/">curses</a></i>(3x) cursor motion package.</p>
<dt><code>+cu</code></p>
<dd> This option indicates that <i>xterm</i> should not work around the <i><a href="/docs/linux/man/1-more/">more</a></i>(1) bug mentioned above.</p>
<dt><code>-dc</code></p>
<dd> This option disables the escape sequence to change dynamic colors: the vt100 foreground and background colors, its text cursor color, the pointer cursor foreground and background colors, the Tektronix emulator foreground and background colors, its text cursor color and highlight color. The option sets the <code>dynamicColors</code> option to &#8220;false&#8221;.</p>
<dt><code>+dc</code></p>
<dd> This option enables the escape sequence to change dynamic colors. The option sets the <code>dynamicColors</code> option to &#8220;true&#8221;.</p>
<dt><code>-e</code><i> program </i>[ <i>arguments </i>&#8230; ]<i></i></p>
<dd> This option specifies the program (and its command line arguments) to be run in the <i>xterm</i> window. It also sets the window title and icon name to be the basename of the program being executed if neither <i>-T</i> nor <i>-n</i> are given on the command line.</p>
<dt>
<dd> <code>NOTE:</code> This must be the <code>last option</code> on the command line.</p>
<dt><code>-en</code><i> encoding</i></p>
<dd> This option determines the encoding on which <i>xterm</i> runs. It sets the <code>locale</code> resource. Encodings other than UTF-8 are supported by using <i>luit</i>. The <code>-lc</code> option should be used instead of <code>-en</code> for systems with locale support.</p>
<dt><code>-fa</code><i> pattern</i></p>
<dd> This option sets the pattern for fonts selected from the FreeType library if support for that library was compiled into <i>xterm</i>. This corresponds to the <code>faceName</code> resource. When a CJK double-width font is specified, you also need to turn on the <code>cjkWidth</code> resource.</p>
<dt>
<dd> If you specify both <code>-fa</code> and the X Toolkit option <code>-fn</code>, the <code>-fa</code> setting overrides the latter.</p>
<dt>
<dd> See also the <code>renderFont</code> resource, which combines with this to determine whether FreeType fonts are initially active.</p>
<dt><code>-fb</code><i> font</i></p>
<dd> This option specifies a font to be used when displaying bold text. It sets the <code>boldFont</code> resource.</p>
<dt>
<dd> This font must be the same height and width as the normal font, otherwise it is ignored. If only one of the normal or bold fonts is specified, it will be used as the normal font and the bold font will be produced by overstriking this font.</p>
<dt>
<dd> See also the discussion of <code>boldMode</code> and <code>alwaysBoldMode</code> resources.</p>
<dt><code>-fbb</code></p>
<dd> This option indicates that <i>xterm</i> should compare normal and bold fonts bounding boxes to ensure they are compatible. It sets the <code>freeBoldBox</code> resource to &#8220;false&#8221;.</p>
<dt><code>+fbb</code></p>
<dd> This option indicates that <i>xterm</i> should not compare normal and bold fonts bounding boxes to ensure they are compatible. It sets the <code>freeBoldBox</code> resource to &#8220;true&#8221;.</p>
<dt><code>-fbx</code></p>
<dd> This option indicates that <i>xterm</i> should not assume that the normal and bold fonts have VT100 line-drawing characters. If any are missing, <i>xterm</i> will draw the characters directly. It sets the <code>forceBoxChars</code> resource to &#8220;false&#8221;.</p>
<dt><code>+fbx</code></p>
<dd> This option indicates that <i>xterm</i> should assume that the normal and bold fonts have VT100 line-drawing characters. It sets the <code>forceBoxChars</code> resource to &#8220;true&#8221;.</p>
<dt><code>-fc</code><i> fontchoice</i></p>
<dd> Specify the initial font chosen from the font menu. The option value corresponds to the <code>initialFont</code> resource.</p>
<dt><code>-fd</code><i> pattern</i></p>
<dd> This option sets the pattern for double-width fonts selected from the FreeType library if support for that library was compiled into <i>xterm</i>. This corresponds to the <code>faceNameDoublesize</code> resource.</p>
<dt><code>-fi</code><i> font</i></p>
<dd> This option sets the font for active icons if that feature was compiled into <i>xterm</i>.</p>
<dt>
<dd> See also the discussion of the <code>iconFont</code> resource.</p>
<dt><code>-fs</code><i> size</i></p>
<dd> This option sets the pointsize for fonts selected from the FreeType library if support for that library was compiled into <i>xterm</i>. This corresponds to the <code>faceSize</code> resource.</p>
<dt><code>-fullscreen</code></p>
<dd> This option indicates that <i>xterm</i> should ask the window manager to let it use the full-screen for display, e.g., without window decorations. It sets the <code>fullscreen</code> resource to &#8220;true&#8221;.</p>
<dt><code>+fullscreen</code></p>
<dd> This option indicates that <i>xterm</i> should not ask the window manager to let it use the full-screen for display. It sets the <code>fullscreen</code> resource to &#8220;false&#8221;.</p>
<dt><code>-fw </code><i>font</i></p>
<dd> This option specifies the font to be used for displaying wide text. By default, it will attempt to use a font twice as wide as the font that will be used to draw normal text. If no double-width font is found, it will improvise, by stretching the normal font. This corresponds to the <code>wideFont</code> resource.</p>
<dt><code>-fwb </code><i>font</i></p>
<dd> This option specifies the font to be used for displaying bold wide text. By default, it will attempt to use a font twice as wide as the font that will be used to draw bold text. If no double-width font is found, it will improvise, by stretching the bold font. This corresponds to the <code>wideBoldFont</code> resource.</p>
<dt><code>-fx </code><i>font</i></p>
<dd> This option specifies the font to be used for displaying the preedit string in the &#8220;OverTheSpot&#8221; input method.</p>
<dt>
<dd> See also the discussion of the <code>ximFont</code> resource.</p>
<dt><code>-hc</code><i> color</i></p>
<dd> (see <code>-selbg</code>).</p>
<dt><code>-hf</code></p>
<dd> This option indicates that HP function key escape codes should be generated for function keys. It sets the <code>hpFunctionKeys</code> resource to &#8220;true&#8221;.</p>
<dt><code>+hf</code></p>
<dd> This option indicates that HP function key escape codes should not be generated for function keys. It sets the <code>hpFunctionKeys</code> resource to &#8220;false&#8221;.</p>
<dt><code>-hm</code></p>
<dd> Tells <i>xterm</i> to use <code>highlightTextColor</code> and <code>highlightColor</code> to override the reversed foreground/background colors in a selection. It sets the <code>highlightColorMode</code> resource to &#8220;true&#8221;.</p>
<dt><code>+hm</code></p>
<dd> Tells <i>xterm</i> not to use <code>highlightTextColor</code> and <code>highlightColor</code> to override the reversed foreground/background colors in a selection. It sets the <code>highlightColorMode</code> resource to &#8220;false&#8221;.</p>
<dt><code>-hold</code></p>
<dd> Turn on the <code>hold</code> resource, i.e., <i>xterm</i> will not immediately destroy its window when the shell command completes. It will wait until you use the window manager to destroy/kill the window, or if you use the menu entries that send a signal, e.g., HUP or KILL.</p>
<dt><code>+hold</code></p>
<dd> Turn off the <code>hold</code> resource, i.e., <i>xterm</i> will immediately destroy its window when the shell command completes.</p>
<dt><code>-ie</code></p>
<dd> Turn on the <code>ptyInitialErase</code> resource, i.e., use the pseudo-terminal&#8217;s sense of the <i>stty</i> erase value.</p>
<dt><code>+ie</code></p>
<dd> Turn off the <code>ptyInitialErase</code> resource, i.e., set the <i>stty</i> erase value using the <code>kb</code> string from the termcap entry as a reference, if available.</p>
<dt><code>-im</code></p>
<dd> Turn on the <code>useInsertMode</code> resource, which forces use of insert mode by adding appropriate entries to the TERMCAP environment variable. (This option is ignored on most systems, because TERMCAP is not used).</p>
<dt><code>+im</code></p>
<dd> Turn off the <code>useInsertMode</code> resource.</p>
<dt><code>-into</code><i> windowId</i></p>
<dd> Given an X window identifier (an integer, which can be hexadecimal, octal or decimal according to whether it begins with &quot;0x&quot;, &quot;0&quot; or neither), <i>xterm</i> will reparent its top-level shell widget to that window. This is used to embed <i>xterm</i> within other applications.</p>
<dt>
<dd> For instance, there are scripts for Tcl/Tk and Gtk which can be used to demonstrate the feature. When using Gtk, there is a limitation of that toolkit which requires that <i>xterm</i>&#8216;s <code>allowSendEvents</code> resource is enabled.</p>
<dt><code>-itc</code></p>
<dd> Set the <i>vt100</i> resource <code>colorITMode</code> to &#8220;false&#8221;, disabling the display of characters with italic attribute as color.</p>
<dt><code>+itc</code></p>
<dd> Set the <i>vt100</i> resource <code>colorITMode</code> to &#8220;true&#8221;, enabling the display of characters with italic attribute as color rather than italic.</p>
<dt><code>-j</code></p>
<dd> This option indicates that <i>xterm</i> should do jump scrolling. It corresponds to the <code>jumpScroll</code> resource. Normally, text is scrolled one line at a time; this option allows <i>xterm</i> to move multiple lines at a time so that it does not fall as far behind. Its use is strongly recommended since it makes <i>xterm</i> much faster when scanning through large amounts of text. The VT100 escape sequences for enabling and disabling smooth scroll as well as the <code>VT Options</code> menu can be used to turn this feature on or off.</p>
<dt><code>+j</code></p>
<dd> This option indicates that <i>xterm</i> should not do jump scrolling.</p>
<dt><code>-k8</code></p>
<dd> This option sets the <code>allowC1Printable</code> resource. When <code>allowC1Printable</code> is set, <i>xterm</i> overrides the mapping of C1 control characters (code 128-159) to treat them as printable.</p>
<dt><code>+k8</code></p>
<dd> This option resets the <code>allowC1Printable</code> resource.</p>
<dt><code>-kt</code><i> keyboardtype</i></p>
<dd> This option sets the <code>keyboardType</code> resource. Possible values include: &#8220;unknown&#8221;, &#8220;default&#8221;, &#8220;legacy&#8221;, &#8220;hp&#8221;, &#8220;sco&#8221;, &#8220;sun&#8221;, &#8220;tcap&#8221; and &#8220;vt220&#8221;.</p>
<dt>
<dd> The value &#8220;unknown&#8221;, causes the corresponding resource to be ignored.</p>
<dt>
<dd> The value &#8220;default&#8221;, suppresses the associated resources</p>
<dt>
<dd> <code>hpFunctionKeys</code>,<br />
 <code>scoFunctionKeys</code>,<br />
 <code>sunFunctionKeys</code>,<br />
 <code>tcapFunctionKeys</code>,<br />
 <code>oldXtermFKeys</code> and<br />
 <code>sunKeyboard</code>,</p>
<dt>
<dd> using the Sun/PC keyboard layout.</p>
<dt><code>-l</code></p>
<dd> Turn logging on, unless disabled by the <code>logInhibit</code> resource.</p>
<dt>
<dd> Some versions of <i>xterm</i> may have logging enabled. However, normally logging is not supported, due to security concerns in the early 1990s. That was a problem in X11R4 <code>xterm</code> (1989) which was addressed by a patch to X11R5 late in 1993. X11R6 included these fixes. The older version (when running with <i>root</i> privilege) would create the log file using <i>root</i> privilege. The reason why <i>xterm</i> ran with <i>root</i> privileges was to open pseudo-terminals. Those privileges are now needed only on very old systems: Unix98 pseudo-terminals made the BSD scheme unnecessary.</p>
<dt>
<dd> Unless overridden by the <code>-lf</code> option or the <code>logFile</code> resource:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the filename is &#8220;-&#8221;, then logging is sent to the standard output.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Otherwise a filename is generated, and the log file is written to the directory from which <i>xterm</i> is invoked.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The generated filename is of the form<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
XtermLog.<i>XXXXXX</i>
</pre>
<p>&nbsp;.in -4</p>
<dl>
<dt>
<dd> or<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
Xterm.log.<i>hostname.yyyy.mm.dd.hh.mm.ss.XXXXXX</i>
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> depending on how <i>xterm</i> was built.</dl>
</dl>
<dt><code>+l</code></p>
<dd> Turn logging off.</p>
<dt><code>-lc</code></p>
<dd> Turn on support of various encodings according to the users&#8217; locale setting, i.e., LC_ALL, LC_CTYPE, or LANG environment variables. This is achieved by turning on UTF-8 mode and by invoking <i>luit</i> for conversion between locale encodings and UTF-8. (<i>luit</i> is not invoked in UTF-8 locales.) This corresponds to the <code>locale</code> resource.</p>
<dt>
<dd> The actual list of encodings which are supported is determined by <i>luit</i>. Consult the <i>luit</i> manual page for further details.</p>
<dt>
<dd> See also the discussion of the <code>-u8</code> option which supports UTF-8 locales.</p>
<dt><code>+lc</code></p>
<dd> Turn off support of automatic selection of locale encodings. Conventional 8bit mode or, in UTF-8 locales or with <code>-u8</code> option, UTF-8 mode will be used.</p>
<dt><code>-lcc</code><i> path</i></p>
<dd> File name for the encoding converter from/to locale encodings and UTF-8 which is used with <code>-lc</code> option or <code>locale</code> resource. This corresponds to the <code>localeFilter</code> resource.</p>
<dt><code>-leftbar</code></p>
<dd> Force scrollbar to the left side of VT100 screen. This is the default, unless you have set the <code>rightScrollBar</code> resource.</p>
<dt><code>-lf</code><i> filename</i></p>
<dd> Specify the log filename. This sets the <code>logFile</code> resource. If set to &#8220;-&#8221;, <i>xterm</i> writes its log to the standard output. See the <code>-l</code> option.</p>
<dt><code>-ls</code></p>
<dd> This option indicates that the shell that is started in the <i>xterm</i> window will be a login shell (i.e., the first character of argv[0] will be a dash, indicating to the shell that it should read the user&#8217;s .login or .profile).</p>
<dt>
<dd> The <code>-ls</code> flag and the <code>loginShell</code> resource are ignored if <code>-e</code> is also given, because <i>xterm</i> does not know how to make the shell start the given command after whatever it does when it is a login shell &#8211; the user&#8217;s shell of choice need not be a Bourne shell after all. Also, <i>xterm -e</i> is supposed to provide a consistent functionality for other applications that need to start text-mode programs in a window, and if <code>loginShell</code> were not ignored, the result of ~/.profile might interfere with that.</p>
<dt>
<dd> If you do want the effect of <code>-ls</code> and <code>-e</code> simultaneously, you may get away with something like<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
xterm -e /bin/bash -l -c &quot;my command here&quot;
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Finally, <code>-ls</code> is not completely ignored, because <i>xterm -ls -e</i> does write a <i>/var/log/wtmp</i> entry (if configured to do so), whereas <i>xterm -e</i> does not.</p>
<dt><code>+ls</code></p>
<dd> This option indicates that the shell that is started should not be a login shell (i.e., it will be a normal &#8220;subshell&#8221;).</p>
<dt><code>-maximized</code></p>
<dd> This option indicates that <i>xterm</i> should ask the window manager to maximize its layout on startup. This corresponds to the <code>maximized</code> resource.</p>
<dt>
<dd> Maximizing is not the reverse of iconifying; it is possible to do both with certain window managers.</p>
<dt><code>+maximized</code></p>
<dd> This option indicates that <i>xterm</i> should ask the window manager to not maximize its layout on startup.</p>
<dt><code>-mb</code></p>
<dd> This option indicates that <i>xterm</i> should ring a margin bell when the user types near the right end of a line.</p>
<dt><code>+mb</code></p>
<dd> This option indicates that margin bell should not be rung.</p>
<dt><code>-mc</code><i> milliseconds</i></p>
<dd> This option specifies the maximum time between multi-click selections.</p>
<dt><code>-mesg</code></p>
<dd> Turn off the <code>messages</code> resource, i.e., disallow write access to the terminal.</p>
<dt><code>+mesg</code></p>
<dd> Turn on the <code>messages</code> resource, i.e., allow write access to the terminal.</p>
<dt><code>-mk_width</code></p>
<dd> Set the <code>mkWidth</code> resource to &#8220;true&#8221;. This makes <i>xterm</i> use a built-in version of the wide-character width calculation. The default is &#8220;false&#8221;</p>
<dt><code>+mk_width</code></p>
<dd> Reset the <code>mkWidth</code> resource.</p>
<dt><code>-ms</code><i> color</i></p>
<dd> This option specifies the color to be used for the pointer cursor. The default is to use the foreground color. This sets the <code>pointerColor</code> resource.</p>
<dt><code>-nb</code><i> number</i></p>
<dd> This option specifies the number of characters from the right end of a line at which the margin bell, if enabled, will ring. The default is &#8220;10&#8221;.</p>
<dt><code>-nul</code></p>
<dd> This option disables the display of underlining.</p>
<dt><code>+nul</code></p>
<dd> This option enables the display of underlining.</p>
<dt><code>-pc</code></p>
<dd> This option enables the PC-style use of bold colors (see <code>boldColors</code> resource).</p>
<dt><code>+pc</code></p>
<dd> This option disables the PC-style use of bold colors.</p>
<dt><code>-pf </code><i>font</i></p>
<dd> This option specifies the font to be used for the pointer. The corresponding resource name is <i>pointerFont</i>. The resource value default is <i>cursor</i>.</p>
<dt><code>-pob</code></p>
<dd> This option indicates that the window should be raised whenever a Control-G is received.</p>
<dt><code>+pob</code></p>
<dd> This option indicates that the window should not be raised whenever a Control-G is received.</p>
<dt><code>-report-charclass</code></p>
<dd> Print a report to the standard output showing information about the character-classes which can be altered using the <code>charClass</code> resource.</p>
<dt><code>-report-colors</code></p>
<dd> Print a report to the standard output showing information about colors as <i>xterm</i> allocates them. This corresponds to the <code>reportColors</code> resource.</p>
<dt><code>-report-fonts</code></p>
<dd> Print a report to the standard output showing information about fonts which are loaded. This corresponds to the <code>reportFonts</code> resource.</p>
<dt><code>-report-icons</code></p>
<dd> Print a report to the standard output showing information about pixmap-icons which are loaded. This corresponds to the <code>reportIcons</code> resource.</p>
<dt><code>-report-xres</code></p>
<dd> Print a report to the standard output showing the values of boolean, numeric or string X resources for the VT100 widget when initialization is complete. This corresponds to the <code>reportXRes</code> resource.</p>
<dt><code>-rightbar</code></p>
<dd> Force scrollbar to the right side of VT100 screen.</p>
<dt><code>-rvc</code></p>
<dd> This option disables the display of characters with reverse attribute as color.</p>
<dt><code>+rvc</code></p>
<dd> This option enables the display of characters with reverse attribute as color.</p>
<dt><code>-rw</code></p>
<dd> This option indicates that reverse-wraparound should be allowed. This allows the cursor to back up from the leftmost column of one line to the rightmost column of the previous line. This is very useful for editing long shell command lines and is encouraged. This option can be turned on and off from the <code>VT Options</code> menu.</p>
<dt><code>+rw</code></p>
<dd> This option indicates that reverse-wraparound should not be allowed.</p>
<dt><code>-s</code></p>
<dd> This option indicates that <i>xterm</i> may scroll asynchronously, meaning that the screen does not have to be kept completely up to date while scrolling. This allows <i>xterm</i> to run faster when network latencies are very high and is typically useful when running across a very large internet or many gateways.</p>
<dt><code>+s</code></p>
<dd> This option indicates that <i>xterm</i> should scroll synchronously.</p>
<dt><code>-samename</code></p>
<dd> Does not send title and icon name change requests when the request would have no effect: the name is not changed. This has the advantage of preventing flicker and the disadvantage of requiring an extra round trip to the server to find out the previous value. In practice this should never be a problem.</p>
<dt><code>+samename</code></p>
<dd> Always send title and icon name change requests.</p>
<dt><code>-sb</code></p>
<dd> This option indicates that some number of lines that are scrolled off the top of the window should be saved and that a scrollbar should be displayed so that those lines can be viewed. This option may be turned on and off from the <code>VT Options</code> menu.</p>
<dt><code>+sb</code></p>
<dd> This option indicates that a scrollbar should not be displayed.</p>
<dt><code>-selbg</code><i> color</i></p>
<dd> This option specifies the color to use for the background of selected text. If not specified, reverse video is used. See the discussion of the <code>highlightColor</code> resource.</p>
<dt><code>-selfg</code><i> color</i></p>
<dd> This option specifies the color to use for selected text. If not specified, reverse video is used. See the discussion of the <code>highlightTextColor</code> resource.</p>
<dt><code>-sf</code></p>
<dd> This option indicates that Sun function key escape codes should be generated for function keys.</p>
<dt><code>+sf</code></p>
<dd> This option indicates that the standard escape codes should be generated for function keys.</p>
<dt><code>-sh</code><i> number</i></p>
<dd> scale line-height values by the given number. See the discussion of the <code>scaleHeight</code> resource.</p>
<dt><code>-si</code></p>
<dd> This option indicates that output to a window should not automatically reposition the screen to the bottom of the scrolling region. This option can be turned on and off from the <code>VT Options</code> menu.</p>
<dt><code>+si</code></p>
<dd> This option indicates that output to a window should cause it to scroll to the bottom.</p>
<dt><code>-sk</code></p>
<dd> This option indicates that pressing a key while using the scrollbar to review previous lines of text should cause the window to be repositioned automatically in the normal position at the bottom of the scroll region.</p>
<dt><code>+sk</code></p>
<dd> This option indicates that pressing a key while using the scrollbar should not cause the window to be repositioned.</p>
<dt><code>-sl</code><i> number</i></p>
<dd> This option specifies the number of lines to save that have been scrolled off the top of the screen. This corresponds to the <code>saveLines</code> resource. The default is &#8220;1024&#8221;.</p>
<dt><code>-sm</code></p>
<dd> This option, corresponding to the <code>sessionMgt</code> resource, indicates that <i>xterm</i> should set up session manager callbacks.</p>
<dt><code>+sm</code></p>
<dd> This option indicates that <i>xterm</i> should not set up session manager callbacks.</p>
<dt><code>-sp</code></p>
<dd> This option indicates that Sun/PC keyboard should be assumed, providing mapping for keypad &#8220;+&#8221; to &#8220;,&#8221;, and CTRL-F1 to F13, CTRL-F2 to F14, etc.</p>
<dt><code>+sp</code></p>
<dd> This option indicates that the standard escape codes should be generated for keypad and function keys.</p>
<dt><code>-t</code></p>
<dd> This option indicates that <i>xterm</i> should start in Tektronix mode, rather than in VT<i>xxx</i> mode. Switching between the two windows is done using the &#8220;Options&#8221; menus.</p>
<dt>
<dd> Terminal database (<i>terminfo</i> (5) or <i>termcap</i> (5)) entries that work with <i>xterm</i> are:</p>
<dt>
<dd> &#8220;tek4014&#8221;,<br />
 &#8220;tek4015&#8221;,<br />
 &#8220;tek4012&#8221;,<br />
 &#8220;tek4013&#8221;,<br />
 &#8220;tek4010&#8221;, and<br />
 &#8220;dumb&#8221;.</p>
<dt>
<dd> <i>Xterm</i> automatically searches the terminal database in this order for these entries and then sets the &#8220;TERM&#8221; variable (and the &#8220;TERMCAP&#8221; environment variable, if relevant).</p>
<dt><code>+t</code></p>
<dd> This option indicates that <i>xterm</i> should start in VT<i>xxx</i> mode.</p>
<dt><code>-tb</code></p>
<dd> This option, corresponding to the <code>toolBar</code> resource, indicates that <i>xterm</i> should display a toolbar (or menubar) at the top of its window. The buttons in the toolbar correspond to the popup menus, e.g., control/left/mouse for <code>Main Options</code>.</p>
<dt><code>+tb</code></p>
<dd> This option indicates that <i>xterm</i> should not set up a toolbar.</p>
<dt><code>-ti</code><i> term_id</i></p>
<dd> Specify the name used by <i>xterm</i> to select the correct response to terminal ID queries. It also specifies the emulation level, used to determine the type of response to a DA control sequence. Valid values include vt52, vt100, vt101, vt102, vt220, and vt240 (the &#8220;vt&#8221; is optional). The default is &#8220;vt420&#8221;. The <i>term_id</i> argument specifies the terminal ID to use. (This is the same as the <code>decTerminalID</code> resource).</p>
<dt><code>-tm</code><i> string</i></p>
<dd> This option specifies a series of terminal setting keywords followed by the characters that should be bound to those functions, similar to the <i>stty</i> program. The keywords and their values are described in detail in the <code>ttyModes</code> resource.</p>
<dt><code>-tn</code><i> name</i></p>
<dd> This option specifies the name of the terminal type to be set in the TERM environment variable. It corresponds to the <code>termName</code> resource. This terminal type must exist in the terminal database (termcap or terminfo, depending on how <i>xterm</i> is built) and should have <i>li#</i> and <i>co#</i> entries. If the terminal type is not found, <i>xterm</i> uses the built-in list &#8220;xterm&#8221;, &#8220;vt102&#8221;, etc.</p>
<dt><code>-u8</code></p>
<dd> This option sets the <code>utf8</code> resource. When <code>utf8</code> is set, <i>xterm</i> interprets incoming data as UTF-8. This sets the <code>wideChars</code> resource as a side-effect, but the UTF-8 mode set by this option prevents it from being turned off. If you must turn UTF-8 encoding on and off, use the <code>-wc</code> option or the corresponding <code>wideChars</code> resource, rather than the <code>-u8</code> option.</p>
<dt>
<dd> This option and the <code>utf8</code> resource are overridden by the <code>-lc</code> and <code>-en</code> options and <code>locale</code> resource. That is, if <i>xterm</i> has been compiled to support <i>luit</i>, and the <code>locale</code> resource is not &#8220;false&#8221; this option is ignored. We recommend using the <code>-lc</code> option or the &#8220;<code>locale: true</code>&#8221; resource in UTF-8 locales when your operating system supports locale, or <code>-en UTF-8</code> option or the &#8220;<code>locale: UTF-8</code>&#8221; resource when your operating system does not support locale.</p>
<dt><code>+u8</code></p>
<dd> This option resets the <code>utf8</code> resource.</p>
<dt><code>-uc</code></p>
<dd> This option makes the cursor underlined instead of a box.</p>
<dt><code>+uc</code></p>
<dd> This option makes the cursor a box instead of underlined.</p>
<dt><code>-ulc</code></p>
<dd> This option disables the display of characters with underline attribute as color rather than with underlining.</p>
<dt><code>+ulc</code></p>
<dd> This option enables the display of characters with underline attribute as color rather than with underlining.</p>
<dt><code>-ulit</code></p>
<dd> This option, corresponding to the <code>italicULMode</code> resource, disables the display of characters with underline attribute as italics rather than with underlining.</p>
<dt><code>+ulit</code></p>
<dd> This option, corresponding to the <code>italicULMode</code> resource, enables the display of characters with underline attribute as italics rather than with underlining.</p>
<dt><code>-ut</code></p>
<dd> This option indicates that <i>xterm</i> should not write a record into the system <i>utmp</i> log file.</p>
<dt><code>+ut</code></p>
<dd> This option indicates that <i>xterm</i> should write a record into the system <i>utmp</i> log file.</p>
<dt><code>-vb</code></p>
<dd> This option indicates that a visual bell is preferred over an audible one. Instead of ringing the terminal bell whenever a Control-G is received, the window will be flashed.</p>
<dt><code>+vb</code></p>
<dd> This option indicates that a visual bell should not be used.</p>
<dt><code>-wc</code></p>
<dd> This option sets the <code>wideChars</code> resource.</p>
<dt>
<dd> When <code>wideChars</code> is set, <i>xterm</i> maintains internal structures for 16-bit characters. If <i>xterm</i> is not started in UTF-8 mode (or if this resource is not set), initially it maintains those structures to support 8-bit characters. <i>Xterm</i> can later be switched, using a menu entry or control sequence, causing it to reallocate those structures to support 16-bit characters.</p>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>+wc</code></p>
<dd> This option resets the <code>wideChars</code> resource.</p>
<dt><code>-wf</code></p>
<dd> This option indicates that <i>xterm</i> should wait for the window to be mapped the first time before starting the subprocess so that the initial terminal size settings and environment variables are correct. It is the application&#8217;s responsibility to catch subsequent terminal size changes.</p>
<dt><code>+wf</code></p>
<dd> This option indicates that <i>xterm</i> should not wait before starting the subprocess.</p>
<dt><code>-ziconbeep </code><i>percent</i></p>
<dd> Same as <code>zIconBeep</code> resource. If percent is non-zero, xterms that produce output while iconified will cause an XBell sound at the given volume and have &#8220;***&#8221; prepended to their icon titles. Most window managers will detect this change immediately, showing you which window has the output. (A similar feature was in x10 <i>xterm</i>.)</p>
<dt><code>-C</code></p>
<dd> This option indicates that this window should receive console output. This is not supported on all systems. To obtain console output, you must be the owner of the console device, and you must have read and write permission for it. If you are running X under <i>xdm</i> on the console screen you may need to have the session startup and reset programs explicitly change the ownership of the console device in order to get this option to work.</p>
<dt><code>-S</code><i>ccn</i></p>
<dd> This option allows <i>xterm</i> to be used as an input and output channel for an existing program and is sometimes used in specialized applications. The option value specifies the last few letters of the name of a pseudo-terminal to use in slave mode, plus the number of the inherited file descriptor. If the option contains a &#8220;/&#8221; character, that delimits the characters used for the pseudo-terminal name from the file descriptor. Otherwise, exactly two characters are used from the option for the pseudo-terminal name, the remainder is the file descriptor. Examples (the first two are equivalent since the descriptor follows the last &#8220;/&#8221;):<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
-S/dev/pts/123/45
-S123/45
-Sab34
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Note that <i>xterm</i> does not close any file descriptor which it did not open for its own use. It is possible (though probably not portable) to have an application which passes an open file descriptor down to <i>xterm</i> past the initialization or the <code>-S</code> option to a process running in the <i>xterm</i>.</dl>
<h3>Old Options</h3>
<p> The following command line arguments are provided for compatibility with older versions. They may not be supported in the next release as the X Toolkit provides standard options that accomplish the same task.</p>
<dl>
<dt><code>%</code><i>geom</i></p>
<dd> This option specifies the preferred size and position of the Tektronix window. It is shorthand for specifying the &#8220;<code>tekGeometry</code>&#8221; resource.</p>
<dt><code>#</code><i>geom</i></p>
<dd> This option specifies the preferred position of the icon window. It is shorthand for specifying the &#8220;<code>iconGeometry</code>&#8221; resource.</p>
<dt><code>-T</code><i> string</i></p>
<dd> This option specifies the title for <i>xterm</i>&#8216;s windows. It is equivalent to <code>-title</code>.</p>
<dt><code>-n</code><i> string</i></p>
<dd> This option specifies the icon name for <i>xterm</i>&#8216;s windows. It is shorthand for specifying the &#8220;<code>iconName</code>&#8221; resource. Note that this is not the same as the toolkit option <code>-name</code>. The default icon name is the application name.</p>
<dt>
<dd> If no suitable icon is found, <i>xterm</i> provides a compiled-in pixmap.</p>
<dt>
<dd> X Toolkit sets the <code>WM_ICON_NAME</code> property using this value.</p>
<dt><code>-r</code></p>
<dd> This option indicates that reverse video should be simulated by swapping the foreground and background colors. It is equivalent to <code>-rv</code>.</p>
<dt><code>-w</code><i> number</i></p>
<dd> This option specifies the width in pixels of the border surrounding the window. It is equivalent to <code>-borderwidth</code> or <code>-bw</code>.</dl>
<h3>X Toolkit Options</h3>
<p> The following standard X Toolkit command line arguments are commonly used with <i>xterm</i>:</p>
<dl>
<dt><code>-bd </code><i>color</i></p>
<dd> This option specifies the color to use for the border of the window. The corresponding resource name is <code>borderColor</code>. <i>Xterm</i> uses the X Toolkit default, which is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> <i>Xterm</i>&#8216;s VT100 window has two borders: the <i>inner</i> border <code>internalBorder</code> and the <i>outer</i> border <code>borderWidth</code>, managed by the X Toolkit.</p>
<dt>
<dd> Normally <i>xterm</i> fills the inner border using the VT100 window&#8217;s background color. If the <code>colorInnerBorder</code> resource is enabled, then <i>xterm</i> may fill the inner border using the <code>borderColor</code> resource.</p>
<dt><code>-bg </code><i>color</i></p>
<dd> This option specifies the color to use for the background of the window. The corresponding resource name is <i>background</i>. The default is &#8220;XtDefaultBackground&#8221;.</p>
<dt><code>-bw </code><i>number</i></p>
<dd> This option specifies the width in pixels of the border surrounding the window.</p>
<dt>
<dd> This appears to be a legacy of older X releases. It sets the <code>borderWidth</code> resource of the shell widget, and may provide advice to your window manager to set the thickness of the window frame. Most window managers do not use this information. See the <code>-b</code> option, which controls the inner border of the <i>xterm</i> window.</p>
<dt><code>-display </code><i>display</i></p>
<dd> This option specifies the X server to contact; see <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<dt><code>-fg </code><i>color</i></p>
<dd> This option specifies the color to use for displaying text. The corresponding resource name is <i>foreground</i>. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt><code>-fn </code><i>font</i></p>
<dd> This option specifies the font to be used for displaying normal text. The corresponding resource name is <i>font</i>. The resource value default is <i>fixed</i>.</p>
<dt><code>-font </code><i>font</i></p>
<dd> This is the same as <code>-fn</code>.</p>
<dt><code>-geometry </code><i>geometry</i></p>
<dd> This option specifies the preferred size and position of the VT<i>xxx</i> window; see <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<dt>
<dd> The normal geometry specification can be suffixed with <code>@</code> followed by a Xinerama screen specification; it can be either <code>g</code> for the global screen (default), <code>c</code> for the current screen or a screen number.</p>
<dt><code>-iconic</code></p>
<dd>
 This option indicates that <i>xterm</i> should ask the window manager to start it as an icon rather than as the normal window. The corresponding resource name is <i>iconic</i>.</p>
<dt><code>-name </code><i>name</i></p>
<dd> This option specifies the application name under which resources are to be obtained, rather than the default executable file name. <i>Name</i> should not contain &#8220;.&#8221; or &#8220;*&#8221; characters.</p>
<dt><code>-rv</code></p>
<dd> This option indicates that reverse video should be simulated by swapping the foreground and background colors. The corresponding resource name is <code>reverseVideo</code>.</p>
<dt><code>+rv</code></p>
<dd> Disable the simulation of reverse video by swapping foreground and background colors.</p>
<dt><code>-title </code><i>string</i></p>
<dd> This option specifies the window title string, which may be displayed by window managers if the user so chooses. It is shorthand for specifying the &#8220;<code>title</code>&#8221; resource. The default title is the command line specified after the <code>-e</code> option, if any, otherwise the application name.</p>
<dt>
<dd> X Toolkit sets the <code>WM_NAME</code> property using this value.</p>
<dt><code>-xrm </code><i>resourcestring</i></p>
<dd> This option specifies a resource string to be used. This is especially useful for setting resources that do not have separate command line options.</dl>
<p> X Toolkit accepts alternate names for a few of these options, e.g.,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;<code>-background</code>&#8221; for &#8220;<code>-bg</code>&#8221;<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;<code>-font</code>&#8221; for &#8220;<code>-fn</code>&#8221;<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;<code>-foreground</code>&#8221; for &#8220;<code>-fg</code>&#8221; </p>
<p> Abbreviated options also are supported, e.g., &#8220;<code>-v</code>&#8221; for &#8220;<code>-version</code>.&#8221;</p>
<h2>RESOURCES</h2>
<p> <i>Xterm</i> understands all of the core X Toolkit resource names and classes. It also uses the X Toolkit resource types (such as booleans, colors, fonts, integers, and strings) along with their respective converters. Those resource types are not always sufficient:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i>&#8216;s resource values may be lists of names. X Toolkit resource types do not include lists. <i>Xterm</i> uses a string for the resource, and parses it.</p>
<dl>
<dt>
<dd> Comma-separated lists of names ignore case.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> may defer processing a resource until it is needed. For example, <code>font2</code> through <code>font7</code> are loaded as needed, to start faster. Again, the actual resource type is a string, parsed and used when needed.</dl>
<p> Application specific resources (e.g., &#8220;<code>XTerm.</code><i>NAME</i>&#8221;) follow:</p>
<h3>Application Resources</h3>
<dl>
<dt><code>backarrowKeyIsErase</code> (class<code> BackarrowKeyIsErase</code>)</p>
<dd> Tie the VT<i>xxx</i> <code>backarrowKey</code> and <code>ptyInitialErase</code> resources together by setting the DECBKM state according to whether the <i>initial erase</i> character is a backspace (8) or delete (127) character. A &#8220;false&#8221; value disables this feature. The default is &#8220;True&#8221;.</p>
<dt>
<dd> Here are tables showing how the initial settings for</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>backarrowKeyIsErase</code> (BKIE),<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>backarrowKey</code> (BK), and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <code>ptyInitialErase</code> (PIE), along with the<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>stty</i> erase character (^H for backspace, ^? for delete)</dl>
<dt>
<dd> will affect DECBKM. First, <i>xterm</i> obtains the initial <i>erase</i> character:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>xterm</i>&#8216;s internal value is ^H<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>xterm</i> asks the operating system for the value which <code>stty</code> shows<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the <code>ttyModes</code> resource may override <i>erase</i><br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if <code>ptyInitialErase</code> is false, <i>xterm</i> will look in the terminal database</dl>
<dt>
<dd> Summarizing that as a table: </p>
<table>
<tr VALIGN=top>
<td><code>PIE</code></td>
<td><code>stty</code></td>
<td><code>termcap</code></td>
<td><i>erase</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^H
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^H
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^H
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^H</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^?</td>
<td ALIGN=center>^?
</td>
</tr>
</table>
<dt>
<dd> Using that <i>erase</i> character, <i>xterm</i> allows further choices:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 if <code>backarrowKeyIsErase</code> is true, <i>xterm</i> uses the <i>erase</i> character for the initial state of <code>DECBKM</code><br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 if <code>backarrowKeyIsErase</code> is false, <i>xterm</i> sets <code>DECBKM</code> to 2 (internal). This ties together <code>backarrowKey</code> and the control sequence for <code>DECBKM</code>.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 applications can send a control sequence to set/reset <code>DECBKM</code> control set<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 the &#8220;Backarrow Key (BS/DEL)&#8221; menu entry toggles <code>DECBKM</code></dl>
<dt>
<dd> Summarizing the initialization details: </p>
<table>
<tr VALIGN=top>
<td><i>erase</i></td>
<td><code>BKIE</code></td>
<td><code>BK</code></td>
<td><code>DECBKM</code></td>
<td><i>result</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^?</td>
<td>false</td>
<td>true</td>
<td ALIGN=center>2</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^?</td>
<td>true</td>
<td>false</td>
<td ALIGN=center>0</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^?</td>
<td>true</td>
<td>true</td>
<td ALIGN=center>1</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^H</td>
<td>false</td>
<td>false</td>
<td ALIGN=center>2</td>
<td ALIGN=center>^H
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^H</td>
<td>false</td>
<td>true</td>
<td ALIGN=center>2</td>
<td ALIGN=center>^?
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^H</td>
<td>true</td>
<td>false</td>
<td ALIGN=center>0</td>
<td ALIGN=center>^H
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>^H</td>
<td>true</td>
<td>true</td>
<td ALIGN=center>1</td>
<td ALIGN=center>^H
</td>
</tr>
</table>
<dt><code>buffered</code> (class<code> Buffered</code>)</p>
<dd> Normally <i>xterm</i> is built with double-buffer support. This resource can be used to turn it on or off. Setting the resource to &#8220;true&#8221; turns double-buffering on. The default value is &#8220;False&#8221;.</p>
<dt><code>bufferedFPS</code> (class<code> BufferedFPS</code>)</p>
<dd> When <i>xterm</i> is built with double-buffer support, this gives the maximum number of frames/second. The default is &#8220;40&#8221; and is limited to the range 1 through 100.</p>
<dt><code>cursorTheme</code> (class<code> CursorTheme</code>)</p>
<dd> The <a href="/docs/linux/man/7-xcursor/">Xcursor</a>(7) library provides a way to change the pointer shape and size. The X11 library uses this library to extend the font- and glyph-cursor calls used by applications such as <i>xterm</i> to substitute external files for the built-in &#8220;core&#8221; cursors provided by X.</p>
<dt>
<dd> <i>Xterm</i> uses the <code>pointerShape</code> resource to select the X cursor shape. Most of the available sets of cursor themes provide an incomplete set of &#8220;core&#8221; cursors (while possibly adding other cursors). Because of this limitation, <i>xterm</i> disables the feature by default.</p>
<dt>
<dd> The cursor theme feature can be useful because X cursors are not scalable and on a high-resolution display, the cursors are hard to find. Some of the cursor themes include larger cursors to work around this limitation:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The default core cursors are 8&#215;8 pixels;<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Some cursor themes include cursors up to the X server limit of 64&#215;64 pixels.</dl>
<dt>
<dd> At startup, <i>xterm</i> sets the <code>XCURSOR_THEME</code> environment variable to enable or disable the cursor theme feature. The default value is &#8220;none&#8221;. Other values (including &#8220;default&#8221;) are passed to the Xcursor library to select a cursor theme.</p>
<dt><code>fullscreen</code> (class<code> Fullscreen</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should ask the window manager to use a fullscreen layout on startup. <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> Fullscreen layout is not used initially, but may be later via menu-selection or control sequence.</p>
<dt>true (1)</p>
<dd> Fullscreen layout is used initially, but may be disabled later via menu-selection or control sequence.</p>
<dt>always (2)</p>
<dd> Fullscreen layout is used initially, and cannot be disabled later via menu-selection or control sequence.</p>
<dt>never (3)</p>
<dd> Fullscreen layout is not used, and cannot be enabled later via menu-selection or control sequence.</dl>
</dl>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>hold</code> (class<code> Hold</code>)</p>
<dd> If true, <i>xterm</i> will not immediately destroy its window when the shell command completes. It will wait until you use the window manager to destroy/kill the window, or if you use the menu entries that send a signal, e.g., HUP or KILL. You may scroll back, select text, etc., to perform most graphical operations. Resizing the display will lose data, however, since this involves interaction with the shell which is no longer running.</p>
<dt><code>hpFunctionKeys</code> (class<code> HpFunctionKeys</code>)</p>
<dd> Specifies whether or not HP function key escape codes should be generated for function keys. The default is &#8220;false&#8221;, i.e., this feature is disabled.</p>
<dt>
<dd> The <code>keyboardType</code> resource is the preferred mechanism for selecting this mode.</p>
<dt><code>iconGeometry</code> (class<code> IconGeometry</code>)</p>
<dd> Specifies the preferred size and position of the application when iconified. It is not necessarily obeyed by all window managers.</p>
<dt><code>iconHint</code> (class<code> IconHint</code>)</p>
<dd> Specifies an icon which will be added to the window manager hints. <i>Xterm</i> provides no default value.</p>
<dt>
<dd> Set this resource to &#8220;none&#8221; to omit the hint entirely, using whatever the window manager may decide.</p>
<dt>
<dd> If the <code>iconHint</code> resource is given (or is set via the <code>-n</code> option) <i>xterm</i> searches for a pixmap file with that name, in the current directory as well as in /usr/share/pixmaps. if the resource does not specify an absolute pathname. In each case, <i>xterm</i> adds &#8220;_48x48&#8221; and/or &#8220;.xpm&#8221; to the filename after trying without those suffixes. If it is able to load the file, <i>xterm</i> sets the window manager hint for the icon-pixmap. These pixmaps are distributed with <i>xterm</i>, and can optionally be compiled-in:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 mini.xterm_16x16, mini.xterm_32x32, mini.xterm_48x48<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 filled-xterm_16x16, filled-xterm_32x32, filled-xterm_48x48<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 xterm_16x16, xterm_32x32, xterm_48x48<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 xterm-color_16x16, xterm-color_32x32, xterm-color_48x48</dl>
<dt>
<dd> In either case, <i>xterm</i> allows for adding a &#8220;_48x48&#8221; to specify the largest of the pixmaps as a default. That is, &#8220;mini.xterm&#8221; is the same as &#8220;mini.xterm_48x48&#8221;.</p>
<dt>
<dd> If no explicit <code>iconHint</code> resource is given (or if none of the compiled-in names matches), <i>xterm</i> uses &#8220;mini.xterm&#8221; (which is always compiled-in).</p>
<dt>
<dd> The <code>iconHint</code> resource has no effect on &#8220;desktop&#8221; files, including &#8220;panel&#8221; and &#8220;menu&#8221;. Those are typically set via a &#8220;.desktop&#8221; file; <i>xterm</i> provides samples for itself (and the <i>uxterm</i> script). The more capable desktop systems allow changing the icon on a per-user basis.</p>
<dt><code>iconName</code> (class<code> IconName</code>)</p>
<dd> Specifies a label for <i>xterm</i> when iconified. <i>Xterm</i> provides no default value; some window managers may assume the application name, e.g., &#8220;xterm&#8221;.</p>
<dt>
<dd> Setting the <code>iconName</code> resource sets the icon label unless overridden by <code>zIconBeep</code> or the control sequences which change the window and icon labels.</p>
<dt><code>keyboardType</code> (class<code> KeyboardType</code>)</p>
<dd> Enables one (or none) of the various keyboard-type resources: <code>hpFunctionKeys</code>, <code>scoFunctionKeys</code>, <code>sunFunctionKeys</code>, <code>tcapFunctionKeys</code>, <code>oldXtermFKeys</code> and <code>sunKeyboard</code>.</p>
<dt>
<dd> The resource&#8217;s value should be one of the corresponding strings &#8220;hp&#8221;, &#8220;sco&#8221;, &#8220;sun&#8221;, &#8220;tcap&#8221;, &#8220;legacy&#8221; or &#8220;vt220&#8221;, respectively.</p>
<dt>
<dd> The individual resources are provided for legacy support; this resource is simpler to use. <i>Xterm</i> will use only one keyboard-type, but if multiple resources are set, it warns and uses the last one it checks.</p>
<dt>
<dd> The default is &#8220;unknown&#8221;, i.e., none of the associated resources are set via this resource.</p>
<dt><code>maxBufSize</code> (class<code> MaxBufSize</code>)</p>
<dd> Specify the maximum size of the input buffer. The default is &#8220;32768&#8221;. You cannot set this to a value less than the <code>minBufSize</code> resource. It will be increased as needed to make that value evenly divide this one.</p>
<dt>
<dd> On some systems you may want to increase one or both of the <code>maxBufSize</code> and <code>minBufSize</code> resource values to achieve better performance if the operating system prefers larger buffer sizes.</p>
<dt><code>maximized</code> (class<code> Maximized</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should ask the window manager to maximize its layout on startup. The default is &#8220;false&#8221;.</p>
<dt><code>menuHeight</code> (class<code> MenuHeight</code>)</p>
<dd> Specifies the height of the toolbar, which may be increased by the X toolkit layout widget depending upon the fontsize used. The default is &#8220;25&#8221;.</p>
<dt><code>menuLocale</code> (class<code> MenuLocale</code>)</p>
<dd> Specify the locale used for character-set computations when loading the popup menus. Use this to improve initialization performance of the Athena popup menus, which may load unnecessary (and very large) fonts, e.g., in a locale having UTF-8 encoding. The default is &#8220;C&#8221; (POSIX).</p>
<dt>
<dd> To use the current locale (only useful if you have localized the resource settings for the menu entries), set the resource to an empty string.</p>
<dt><code>messages</code> (class<code> Messages</code>)</p>
<dd> Specifies whether write access to the terminal is allowed initially. See <code><a href="/docs/linux/man/1-mesg/">mesg</a></code>(1). The default is &#8220;true&#8221;.</p>
<dt><code>minBufSize</code> (class<code> MinBufSize</code>)</p>
<dd> Specify the minimum size of the input buffer, i.e., the amount of data that <i>xterm</i> requests on each read. The default is &#8220;4096&#8221;. You cannot set this to a value less than 64.</p>
<dt><code>omitTranslation</code> (class<code> OmitTranslation</code>)</p>
<dd> Selectively omit one or more parts of <i>xterm</i>&#8216;s default translations at startup. The resource value is a comma-separated list of keywords, which may be abbreviated:</p>
<dl>
<dt>
<dd>
<dl>
<dt>default</p>
<dd> ignore (mouse) button-down events which were not handled by other translations</p>
<dt>fullscreen</p>
<dd> assigns a key-binding to the <code>fullscreen()</code> action.</p>
<dt>keypress</p>
<dd> assigns keypresses by default to the <code>insert-seven-bit()</code> and <code>insert-eight-bit()</code> actions.</p>
<dt>paging</p>
<dd> assigns key bindings to the <code>scroll-back()</code> and <code>scroll-forw()</code> actions.</p>
<dt>pointer</p>
<dd> assigns pointer <i>motion</i> and <i>button</i> events to the <code>pointer-motion()</code> and <code>pointer-button()</code> actions respectively.</p>
<dt>popup-menu</p>
<dd> assigns mouse-buttons with the <i>control</i> modifier to the popup-menus.</p>
<dt>reset</p>
<dd> assigns mouse-button 2 with the <i>meta</i> modifier to the <code>clear-saved-lines</code> action.</p>
<dt>scroll-lock</p>
<dd> assigns a key-binding to the <code>scroll-lock()</code> action.</p>
<dt>select</p>
<dd> assigns mouse- and keypress-combinations to actions which manipulate the selection.</p>
<dt>
<dd> <i>Xterm</i> also uses these actions to capture mouse button and motion events which can be manipulated with the mouse protocol control sequences. If the <i>select</i> translations are omitted, then the <code>pointer-motion</code> and <code>pointer-button</code> handle these mouse protocol control sequences instead.</p>
<dt>shift-fonts</p>
<dd> assigns key-bindings to <code>larger-vt-font()</code> and <code>smaller-vt-font()</code> actions.</p>
<dt>wheel-mouse</p>
<dd> assigns buttons 4 and 5 with different modifiers to the <code>scroll-back()</code> and <code>scroll-forw()</code> actions.</dl>
</dl>
<dt><code>ptyHandshake</code> (class<code> PtyHandshake</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will perform handshaking during initialization to ensure that the parent and child processes update the <i>utmp</i> and <i>stty</i> state.</p>
<dt>
<dd> See also <code>waitForMap</code> which waits for the pseudo-terminal&#8217;s notion of the screen size, and <code>ptySttySize</code> which resets the screen size after other terminal initialization is complete. The default is &#8220;true&#8221;.</p>
<dt><code>ptyInitialErase</code> (class<code> PtyInitialErase</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will use the pseudo-terminal&#8217;s sense of the <i>stty</i> erase value. If &#8220;false&#8221;, <i>xterm</i> will set the <i>stty</i> erase value to match its own configuration, using the <code>kb</code> string from the termcap entry as a reference, if available.</p>
<dt>
<dd> In either case, the result is applied to the TERMCAP variable which <i>xterm</i> sets, if the system uses TERMCAP.</p>
<dt>
<dd> See also the <code>ttyModes</code> resource, which may override this. The default is &#8220;False&#8221;.</p>
<dt><code>ptySttySize</code> (class<code> PtySttySize</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will reset the screen size after terminal initialization is complete. This is needed for some systems whose pseudo-terminals cannot propagate terminal characteristics. Where it is not needed, it can interfere with other methods for setting the initial screen size, e.g., via window manager interaction.</p>
<dt>
<dd> See also <code>waitForMap</code> which waits for a handshake-message giving the pseudo-terminal&#8217;s notion of the screen size. The default is &#8220;false&#8221; on Linux and macOS systems, &#8220;true&#8221; otherwise.</p>
<dt><code>reportColors</code> (class<code> ReportColors</code>)</p>
<dd> If true, <i>xterm</i> will print to the standard output a summary of colors as it allocates them. The default is &#8220;false&#8221;.</p>
<dt><code>reportFonts</code> (class<code> ReportFonts</code>)</p>
<dd> If true, <i>xterm</i> will print to the standard output a summary of each font&#8217;s metrics (size, number of glyphs, etc.), as it loads them. The default is &#8220;false&#8221;.</p>
<dt><code>reportIcons</code> (class<code> ReportIcons</code>)</p>
<dd> If true, <i>xterm</i> will print to the standard output a summary of each pixmap icon as it loads them. The default is &#8220;false&#8221;.</p>
<dt><code>reportXRes</code> (class<code> ReportXRes</code>)</p>
<dd> If true, <i>xterm</i> will print to the standard output a list of the boolean, numeric and string X resources for the VT100 widget after initialization. The default is &#8220;false&#8221;.</p>
<dt><code>sameName</code> (class<code> SameName</code>)</p>
<dd> If the value of this resource is &#8220;true&#8221;, <i>xterm</i> does not send title and icon name change requests when the request would have no effect: the name is not changed. This has the advantage of preventing flicker and the disadvantage of requiring an extra round trip to the server to find out the previous value. In practice this should never be a problem. The default is &#8220;true&#8221;.</p>
<dt><code>scaleHeight</code> (class<code> ScaleHeight</code>)</p>
<dd> Scale line-height values by the resource value, which is limited to &#8220;0.9&#8221; to &#8220;1.5&#8221;. The default value is &#8220;1.0&#8221;,</p>
<dt>
<dd> While this resource applies to either bitmap or TrueType fonts, its main purpose is to help work around incompatible changes in the Xft library&#8217;s font metrics. <i>Xterm</i> checks the font metrics to find what the library claims are the bounding boxes for each glyph (character). However, some of Xft&#8217;s features (such as the autohinter) can cause the glyphs to be scaled larger than the bounding boxes, and be partly overwritten by the next row.</p>
<dt>
<dd> See <code>useClipping</code> for a related resource.</p>
<dt><code>scoFunctionKeys</code> (class<code> ScoFunctionKeys</code>)</p>
<dd> Specifies whether or not SCO function key escape codes should be generated for function keys. The default is &#8220;false&#8221;, i.e., this feature is disabled.</p>
<dt>
<dd> The <code>keyboardType</code> resource is the preferred mechanism for selecting this mode.</p>
<dt><code>sessionMgt</code> (class<code> SessionMgt</code>)</p>
<dd> If the value of this resource is &#8220;true&#8221;, <i>xterm</i> sets up session manager callbacks for <code>XtNdieCallback</code> and <code>XtNsaveCallback</code>. The default is &#8220;true&#8221;.</p>
<dt><code>sunFunctionKeys</code> (class<code> SunFunctionKeys</code>)</p>
<dd> Specifies whether or not Sun function key escape codes should be generated for function keys. The default is &#8220;false&#8221;, i.e., this feature is disabled.</p>
<dt>
<dd> The <code>keyboardType</code> resource is the preferred mechanism for selecting this mode.</p>
<dt><code>sunKeyboard</code> (class<code> SunKeyboard</code>)</p>
<dd> <i>Xterm</i> translates certain key symbols based on its assumptions about your keyboard. This resource specifies whether or not Sun/PC keyboard layout (i.e., the PC keyboard&#8217;s numeric keypad together with 12 function keys) should be assumed rather than DEC VT220. This causes the keypad &#8220;+&#8221; to be mapped to &#8220;,&#8221;. and CTRL F1-F10 to F11-F20, depending on the setting of the <code>ctrlFKeys</code> resource, so <i>xterm</i> emulates a DEC VT220 more accurately. Otherwise (the default, with <code>sunKeyboard</code> set to &#8220;false&#8221;), <i>xterm</i> uses PC-style bindings for the function keys and keypad.</p>
<dt>
<dd> PC-style bindings use the Shift, Alt, Control and Meta keys as modifiers for function-keys and keypad (see <i>Xterm Control Sequences</i> for details). The PC-style bindings are analogous to PCTerm, but not the same thing. Normally these bindings do not conflict with the use of the Meta key as described for the <code>eightBitInput</code> resource. If they do, note that the PC-style bindings are evaluated first.</p>
<dt>
<dd> See also the <code>keyboardType</code> resource.</p>
<dt><code>tcapFunctionKeys</code> (class<code> TcapFunctionKeys</code>)</p>
<dd> Specifies whether or not function key escape codes read from the termcap/terminfo entry corresponding to the <code>TERM</code> environment variable should be generated for function keys instead of those configured using <code>sunKeyboard</code> and <code>keyboardType</code>. The default is &#8220;false&#8221;, i.e., this feature is disabled.</p>
<dt>
<dd> The <code>keyboardType</code> resource is the preferred mechanism for selecting this mode.</p>
<dt><code>termName</code> (class<code> TermName</code>)</p>
<dd> Specifies the terminal type name to be set in the TERM environment variable.</p>
<dt><code>title</code> (class<code> Title</code>)</p>
<dd> Specifies a string that may be used by the window manager when displaying this application.</p>
<dt><code>toolBar</code> (class<code> ToolBar</code>)</p>
<dd> Specifies whether or not the toolbar should be displayed. The default is &#8220;true&#8221;.</p>
<dt><code>ttyModes</code> (class<code> TtyModes</code>)</p>
<dd> Specifies a string containing terminal setting keywords. Except where noted, they may be bound to <i>characters</i>. Other keywords set <i>modes</i>. Not all keywords are supported on a given system. Allowable keywords include: </p>
<table>
<tr VALIGN=top>
<td><code>Keyword</code></td>
<td><code>POSIX?</code></td>
<td><code>Notes</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>dsusp</td>
<td>no</td>
<td> <i>CHAR</i> will send a terminal &#8220;stop&#8221; signal after input is flushed.
</td>
</tr>
<tr VALIGN=top>
<td>eof</td>
<td>yes</td>
<td> <i>CHAR</i> will terminate input (i.e., an end of file).
</td>
</tr>
<tr VALIGN=top>
<td>eol</td>
<td>yes</td>
<td><i>CHAR</i> will end the line.
</td>
</tr>
<tr VALIGN=top>
<td>eol2</td>
<td>no</td>
<td>alternate <i>CHAR</i> for ending the line.
</td>
</tr>
<tr VALIGN=top>
<td>erase</td>
<td>yes</td>
<td><i>CHAR</i> will erase the last character typed.
</td>
</tr>
<tr VALIGN=top>
<td>erase2</td>
<td>no</td>
<td> alternate <i>CHAR</i> for erasing the last input-character.
</td>
</tr>
<tr VALIGN=top>
<td>flush</td>
<td>no</td>
<td> <i>CHAR</i> will cause output to be discarded until another <code>flush</code> character is typed.
</td>
</tr>
<tr VALIGN=top>
<td>intr</td>
<td>yes</td>
<td><i>CHAR</i> will send an &#8220;interrupt&#8221; signal.
</td>
</tr>
<tr VALIGN=top>
<td>kill</td>
<td>yes</td>
<td><i>CHAR</i> will erase the current line.
</td>
</tr>
<tr VALIGN=top>
<td>lnext</td>
<td>no</td>
<td><i>CHAR</i> will enter the next character quoted.
</td>
</tr>
<tr VALIGN=top>
<td>quit</td>
<td>yes</td>
<td>CHAR will send a &#8220;quit&#8221; signal.
</td>
</tr>
<tr VALIGN=top>
<td>rprnt</td>
<td>no</td>
<td><i>CHAR</i> will redraw the current line.
</td>
</tr>
<tr VALIGN=top>
<td>start</td>
<td>yes</td>
<td> <i>CHAR</i> will <i>restart</i> the output after stopping it.
</td>
</tr>
<tr VALIGN=top>
<td>status</td>
<td>no</td>
<td> <i>CHAR</i> will cause a system-generated status line to be printed.
</td>
</tr>
<tr VALIGN=top>
<td>stop</td>
<td>yes</td>
<td><i>CHAR</i> will stop the output.
</td>
</tr>
<tr VALIGN=top>
<td>susp</td>
<td>yes</td>
<td><i>CHAR</i> will send a terminal &#8220;stop&#8221; signal
</td>
</tr>
<tr VALIGN=top>
<td>swtch</td>
<td>no</td>
<td><i>CHAR</i> will switch to a different shell layer.
</td>
</tr>
<tr VALIGN=top>
<td>tabs</td>
<td>yes</td>
<td><i>Mode</i> disables tab-expansion.
</td>
</tr>
<tr VALIGN=top>
<td>-tabs</td>
<td>yes</td>
<td><i>Mode</i> enables tab-expansion.
</td>
</tr>
<tr VALIGN=top>
<td>weras</td>
<td>no</td>
<td><i>CHAR</i> will erase the last word typed.
</td>
</tr>
</table>
<dt>
<dd> Control characters may be specified as ^char (e.g., ^c or ^u) and <code>^?</code> may be used to indicate delete (127). Use <code>^-</code> to denote <i>undef</i>. Use <code></code> to represent <code>^\</code>, since a literal backslash in an X resource escapes the next character.</p>
<dt>
<dd> This is very useful for overriding the default terminal settings without having to run <i>stty</i> every time an <i>xterm</i> is started. Note, however, that the <i>stty</i> program on a given host may use different keywords; <i>xterm</i>&#8216;s table is built in. The <i>POSIX</i> column in the table indicates which keywords are supported by a standard <i>stty</i> program.</p>
<dt>
<dd> If the <code>ttyModes</code> resource specifies a value for <code>erase</code>, that overrides the <code>ptyInitialErase</code> resource setting, i.e., <i>xterm</i> initializes the terminal to match that value.</p>
<dt><code>useInsertMode</code> (class<code> UseInsertMode</code>)</p>
<dd> Force use of insert mode by adding appropriate entries to the TERMCAP environment variable. This is useful if the system termcap is broken. (This resource is ignored on most systems, because TERMCAP is not used). The default is &#8220;false&#8221;.</p>
<dt><code>utmpDisplayId</code> (class<code> UtmpDisplayId</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should try to record the display identifier (display number and screen number) as well as the hostname in the system <i>utmp</i> log file. The default is &#8220;true&#8221;.</p>
<dt><code>utmpInhibit</code> (class<code> UtmpInhibit</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should try to record the user&#8217;s terminal in the system <i>utmp</i> log file. If true, <i>xterm</i> will not try. The default is &#8220;false&#8221;.</p>
<dt><code>validShells</code> (class<code> ValidShells</code>)</p>
<dd> Augment (add to) the system&#8217;s <i>/etc/shells</i>, when determining whether to set the &#8220;SHELL&#8221; environment variable when running a given program.</p>
<dt>
<dd> The resource value is a list of lines (separated by newlines). Each line holds one pathname. <i>Xterm</i> ignores any line beginning with &#8220;#&#8221; after trimming leading/trailing whitespace from each line.</p>
<dt>
<dd> The default is an empty string.</p>
<dt><code>waitForMap</code> (class<code> WaitForMap</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should wait for the initial window map before starting the subprocess. This is part of the <code>ptyHandshake</code> logic. When <i>xterm</i> is directed to wait in this fashion, it passes the terminal size from the display end of the pseudo-terminal to the terminal I/O connection, e.g., using the size according to the window manager. Otherwise, it uses the size as given in resource values or command-line option <code>-geometry</code>. The default is &#8220;false&#8221;.</p>
<dt><code>zIconBeep</code> (class<code> ZIconBeep</code>)</p>
<dd> Same as -ziconbeep command line argument. If the value of this resource is non-zero, xterms that produce output while iconified will cause an XBell sound at the given volume and have &#8220;***&nbsp;&#8221; prepended to their icon titles. Most window managers will detect this change immediately, showing you which window has the output. (A similar feature was in x10 <i>xterm</i>.) The default is &#8220;false&#8221;.</p>
<dt><code>zIconTitleFormat</code> (class<code> ZIconTitleFormat</code>)</p>
<dd> Allow customization of the string used in the <code>zIconBeep</code> feature. The default value is &#8220;***&nbsp;%s&#8221;.</p>
<dt>
<dd> If the resource value contains a &#8220;%s&#8221;, then <i>xterm</i> inserts the icon title at that point rather than prepending the string to the icon title. (Only the first &#8220;%s&#8221; is used).</dl>
<h3>VT100 Widget Resources</h3>
<p> The following resources are specified as part of the <i>vt100</i> widget (class <i>VT100</i>). They are specified by patterns such as &#8220;<code>XTerm.vt100.</code><i>NAME</i>&#8221;. </p>
<p> If your <i>xterm</i> is configured to support the &#8220;toolbar&#8221;, then those patterns need an extra level for the form-widget which holds the toolbar and vt100 widget. A wildcard between the top-level &#8220;XTerm&#8221; and the &#8220;vt100&#8221; widget makes the resource settings work for either, e.g., &#8220;<code>XTerm*vt100.</code><i>NAME</i>&#8221;.</p>
<dl>
<dt><code>activeIcon</code> (class<code> ActiveIcon</code>)</p>
<dd> Specifies whether or not active icon windows are to be used when the <i>xterm</i> window is iconified, if this feature is compiled into <i>xterm</i>. The active icon is a miniature representation of the content of the window and will update as the content changes. Not all window managers necessarily support application icon windows. Some window managers will allow you to enter keystrokes into the active icon window. The default is &#8220;default&#8221;.</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> No active icon is shown.</p>
<dt>true (1)</p>
<dd> The active icon is shown. If you are using <i>twm</i>, use this setting to enable active-icons.</p>
<dt>default (2)</p>
<dd> <i>Xterm</i> checks at startup, and shows an active icon only for window managers which it can identify and which are known to support the feature. These are <i>fvwm</i> (full support), and <i>window maker</i> (limited). A few other windows managers (such as <i>twm</i> and <i>ctwm</i>) support active icons, but do not support the extensions which allow <i>xterm</i> to identify the window manager.</dl>
</dl>
<dt><code>allowBoldFonts</code> (class<code> AllowBoldFonts</code>)</p>
<dd> When set to &#8220;false&#8221;, <i>xterm</i> will not use bold fonts. This overrides both the <code>alwaysBoldMode</code> and the <code>boldMode</code> resources.</p>
<dt><code>allowC1Printable</code> (class<code> AllowC1Printable</code>)</p>
<dd> If true, overrides the mapping of C1 controls (codes 128-159) to make them be treated as if they were printable characters. Although this corresponds to no particular standard, some users insist it is a VT100. The default is &#8220;false&#8221;.</p>
<dt><code>allowColorOps</code> (class<code> AllowColorOps</code>)</p>
<dd> Specifies whether control sequences that set/query the dynamic colors should be allowed. ANSI colors are unaffected by this resource setting. The default is &#8220;true&#8221;.</p>
<dt><code>allowFontOps</code> (class<code> AllowFontOps</code>)</p>
<dd> Specifies whether control sequences that set/query the font should be allowed. The default is &#8220;false&#8221;.</p>
<dt><code>allowMouseOps</code> (class<code> AllowMouseOps</code>)</p>
<dd> Specifies whether control sequences that enable <i>xterm</i> to send escape sequences to the host on mouse-clicks and movement. The default is &#8220;true&#8221;.</p>
<dt><code>allowPasteControls</code> (class<code> AllowPasteControls</code>)</p>
<dd> If true, allow control characters such as BEL and CAN to be pasted. Formatting characters (tab, newline) are always allowed. Other C0 control characters are suppressed unless this resource is enabled. The exact set of control characters (C0 and C1) depends upon whether UTF-8 encoding is used, as well as the <code>allowC1Printable</code> resource. The default is &#8220;false&#8221;.</p>
<dt><code>allowScrollLock</code> (class<code> AllowScrollLock</code>)</p>
<dd> Specifies whether control sequences that set/query the Scroll Lock key should be allowed, as well as whether the Scroll Lock key responds to user&#8217;s keypress. The default is &#8220;false&#8221;.</p>
<dt>
<dd> When this feature is enabled, <i>xterm</i> will sense the state of the Scroll Lock key each time it acquires focus. Pressing the Scroll Lock key toggles <i>xterm</i>&#8216;s internal state, as well as toggling the associated LED. While the Scroll Lock is active, <i>xterm</i> attempts to keep a viewport on the same set of lines. If the current viewport is scrolled past the limit set by the <code>saveLines</code> resource, then Scroll Lock has no further effect.</p>
<dt>
<dd> The reason for setting the default to &#8220;false&#8221; is to avoid user surprise. This key is generally unused in keyboard configurations, and has not acquired a standard meaning even when it is used in that manner. Consequently, users have assigned it for ad hoc purposes.</p>
<dt>
<dd> See also the <code>autoScrollLock</code> resource.</p>
<dt><code>allowSendEvents</code> (class<code> AllowSendEvents</code>)</p>
<dd> Specifies whether or not synthetic key and button events (generated using the X protocol SendEvent request) should be interpreted or discarded. The default is &#8220;false&#8221; meaning they are discarded. Note that allowing such events would create a very large security hole, therefore enabling this resource forcefully disables the <code>allow</code><i>XXX</i><code>Ops</code> resources. The default is &#8220;false&#8221;.</p>
<dt><code>allowTcapOps</code> (class<code> AllowTcapOps</code>)</p>
<dd> Specifies whether control sequences that query the terminal&#8217;s notion of its function-key strings, as termcap or terminfo capabilities should be allowed. The default is &#8220;true&#8221;.</p>
<dt>
<dd> A few programs, e.g., <i>vim</i>, use this feature to get an accurate description of the terminal&#8217;s capabilities, independent of the termcap/terminfo setting:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> can tell the querying program how many colors it supports. This is a constant, depending on how it is compiled, typically 16. It does not change if you alter resource settings, e.g., the <code>boldColors</code> resource.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> can tell the querying program what strings are sent by modified (shift-, control-, alt-) function- and keypad-keys. Reporting control- and alt-modifiers is a feature that relies on the <i>ncurses</i> extended naming.</dl>
<dt><code>allowTitleOps</code> (class<code> AllowTitleOps</code>)</p>
<dd> Specifies whether control sequences that modify the window title or icon name should be allowed. The default is &#8220;true&#8221;.</p>
<dt><code>allowWindowOps</code> (class<code> AllowWindowOps</code>)</p>
<dd> Specifies whether extended window control sequences (as used in <i>dtterm</i>) should be allowed. These include several control sequences which manipulate the window size or position, as well as reporting these values and the title or icon name. Each of these can be abused in a script; curiously enough most terminal emulators that implement these restrict only a small part of the repertoire. For fine-tuning, see <code>disallowedWindowOps</code>. The default is &#8220;false&#8221;.</p>
<dt><code>altIsNotMeta</code> (class<code> AltIsNotMeta</code>)</p>
<dd> If &#8220;true&#8221;, treat the Alt-key as if it were the Meta-key. Your keyboard may happen to be configured so they are the same. But if they are not, this allows you to use the same prefix- and shifting operations with the Alt-key as with the Meta-key. See <code>altSendsEscape</code> and <code>metaSendsEscape</code>. The default is &#8220;false&#8221;.</p>
<dt><code>altSendsEscape</code> (class<code> AltSendsEscape</code>)</p>
<dd> This is an additional keyboard operation that may be processed after the logic for <code>metaSendsEscape</code>. It is only available if the <code>altIsNotMeta</code> resource is set.</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;true&#8221;, Alt characters (a character combined with the modifier associated with left/right Alt-keys) are converted into a two-character sequence with the character itself preceded by ESC. This applies as well to function key control sequences, unless <i>xterm</i> sees that <code>Alt</code> is used in your key translations.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;false&#8221;, Alt characters input from the keyboard cause a shift to 8-bit characters (just like <code>metaSendsEscape</code>). By combining the Alt- and Meta-modifiers, you can create corresponding combinations of ESC-prefix and 8-bit characters.</dl>
<dt>
<dd> The default is &#8220;False&#8221;. <i>Xterm</i> provides a menu option for toggling this resource.</p>
<dt><code>alternateScroll</code> (class<code> ScrollCond</code>)</p>
<dd> If &#8220;true&#8221;, the <code>scroll-back</code> and <code>scroll-forw</code> actions send cursor-up and -down keys when <i>xterm</i> is displaying the alternate screen. The default is &#8220;false&#8221;.</p>
<dt>
<dd> The <code>alternateScroll</code> state can also be set using a control sequence.</p>
<dt><code>alwaysBoldMode</code> (class<code> AlwaysBoldMode</code>)</p>
<dd> Specifies whether <i>xterm</i> should check if the normal and bold fonts are distinct before deciding whether to use overstriking to simulate bold fonts. If this resource is true, <i>xterm</i> does not make the check for distinct fonts when deciding how to handle the <code>boldMode</code> resource. The default is &#8220;false&#8221;. </p>
<table>
<tr VALIGN=top>
<td><i>boldMode</i></td>
<td><i>alwaysBoldMode</i></td>
<td><i>Comparison</i></td>
<td><i>Action</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>ignored</td>
<td>use font
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>same</td>
<td>overstrike
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>different</td>
<td>use font
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>ignored</td>
<td>overstrike
</td>
</tr>
</table>
<dl>
<dt>
<dd>
<p> This resource is used only for bitmap fonts:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 When using bitmap fonts, it is possible that the font server will approximate the bold font by rescaling it from a different font size than expected. The <code>alwaysBoldMode</code> resource allows the user to override the (sometimes poor) resulting bold font with overstriking (which is at least consistent).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The problem does not occur with TrueType fonts (though there can be other unnecessary issues such as different coverage of the normal and bold fonts).</dl>
<dt>
<dd> As an alternative, setting the <code>allowBoldFonts</code> resource to false overrides both the <code>alwaysBoldMode</code> and the <code>boldMode</code> resources.</p>
<dt><code>alwaysHighlight</code> (class<code> AlwaysHighlight</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should always display a highlighted text cursor. By default (if this resource is false), a hollow text cursor is displayed whenever the pointer moves out of the window or the window loses the input focus. The default is &#8220;false&#8221;.</p>
<dt><code>alwaysUseMods</code> (class<code> AlwaysUseMods</code>)</p>
<dd> Override the <code>numLock</code> resource, telling <i>xterm</i> to use the Alt and Meta modifiers to construct parameters for function key sequences even if those modifiers appear in the translations resource. Normally <i>xterm</i> checks if Alt or Meta is used in a translation that would conflict with function key modifiers, and will ignore these modifiers in that special case. The default is &#8220;false&#8221;.</p>
<dt><code>answerbackString</code> (class<code> AnswerbackString</code>)</p>
<dd> Specifies the string that <i>xterm</i> sends in response to an ENQ (control/E) character from the host. The default is a blank string, i.e., &#8220;&#8221;. A hardware VT100 implements this feature as a setup option.</p>
<dt><code>appcursorDefault</code> (class<code> AppcursorDefault</code>)</p>
<dd> If &#8220;true&#8221;, the cursor keys are initially in application mode. This is the same as the VT102 private DECCKM mode, The default is &#8220;false&#8221;.</p>
<dt><code>appkeypadDefault</code> (class<code> AppkeypadDefault</code>)</p>
<dd> If &#8220;true&#8221;, the keypad keys are initially in application mode. The default is &#8220;false&#8221;.</p>
<dt><code>assumeAllChars</code> (class<code> AssumeAllChars</code>)</p>
<dd> If &#8220;true&#8221;, this enables a special case in bitmap fonts to allow the font server to choose how to display missing glyphs. The default is &#8220;true&#8221;.</p>
<dt>
<dd> The reason for this resource is to help with certain quasi-automatically generated fonts (such as the ISO-10646-1 encoding of Terminus) which have incorrect font-metrics.</p>
<dt><code>autoScrollLock</code> (class<code> AutoScrollLock</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will maintain its viewport of displayed lines whenever displaying scrollback, as if <code>allowScrollLock</code> were enabled and the Scroll Lock key had been pressed. The default is &#8220;false&#8221;. This feature is only useful if the <code>scrollTtyOutput</code> resource is set to &#8220;false&#8221;.</p>
<dt><code>autoWrap</code> (class<code> AutoWrap</code>)</p>
<dd> Specifies whether or not auto-wraparound should be enabled. This is the same as the VT102 DECAWM. The default is &#8220;true&#8221;.</p>
<dt><code>awaitInput</code> (class<code> AwaitInput</code>)</p>
<dd> Specifies whether or not <i>xterm</i> uses a 50 millisecond timeout to await input (i.e., to support the Xaw3d arrow scrollbar). The default is &#8220;false&#8221;.</p>
<dt><code>backarrowKey</code> (class<code> BackarrowKey</code>)</p>
<dd> Specifies whether the backarrow key transmits a backspace (8) or delete (127) character. This corresponds to the DECBKM control sequence. A &#8220;true&#8221; value specifies backspace. The default is &#8220;True&#8221;. Pressing the control key toggles this behavior.</p>
<dt><code>background</code> (class<code> Background</code>)</p>
<dd> Specifies the color to use for the background of the window. The default is &#8220;XtDefaultBackground&#8221;.</p>
<dt><code>bellIsUrgent</code> (class<code> BellIsUrgent</code>)</p>
<dd> Specifies whether to set the Urgency hint for the window manager when making a bell sound. The default is &#8220;false&#8221;.</p>
<dt><code>bellOnReset</code> (class<code> BellOnReset</code>)</p>
<dd> Specifies whether to sound a bell when doing a hard reset. The default is &#8220;true&#8221;.</p>
<dt><code>bellSuppressTime</code> (class<code> BellSuppressTime</code>)</p>
<dd> Number of milliseconds after a bell command is sent during which additional bells will be suppressed. Default is 200. If set non-zero, additional bells will also be suppressed until the server reports that processing of the first bell has been completed; this feature is most useful with the visible bell.</p>
<dt><code>boldColors</code> (class<code> ColorMode</code>)</p>
<dd> Specifies whether to combine bold attribute with colors like the IBM PC, i.e., map colors 0 through 7 to colors 8 through 15. These normally are the brighter versions of the first 8 colors, hence bold. The default is &#8220;true&#8221;.</p>
<dt><code>boldFont</code> (class<code> BoldFont</code>)</p>
<dd> Specifies the name of the bold font to use instead of overstriking. There is no default for this resource.</p>
<dt>
<dd> This font must be the same height and width as the normal font, otherwise it is ignored. If only one of the normal or bold fonts is specified, it will be used as the normal font and the bold font will be produced by overstriking this font.</p>
<dt>
<dd> See also the discussion of <code>boldMode</code> and <code>alwaysBoldMode</code> resources.</p>
<dt><code>boldMode</code> (class<code> BoldMode</code>)</p>
<dd> This specifies whether or not text with the bold attribute should be overstruck to simulate bold fonts if the resolved bold font is the same as the normal font. It may be desirable to disable bold fonts when color is being used for the bold attribute.</p>
<dt>
<dd> Note that <i>xterm</i> has one bold font which you may set explicitly. <i>Xterm</i> attempts to derive a bold font for the other font selections (<code>font1</code> through <code>font7</code>). If it cannot find a bold font, it will use the normal font. In each case (whether the explicit resource or the derived font), if the normal and bold fonts are distinct, this resource has no effect. The default is &#8220;true&#8221;.</p>
<dt>
<dd> See the <code>alwaysBoldMode</code> resource which can modify the behavior of this resource.</p>
<dt>
<dd> Although <i>xterm</i> attempts to derive a bold font for other font selections, the font server may not cooperate. Since X11R6, bitmap fonts have been scaled. The font server claims to provide the bold font that <i>xterm</i> requests, but the result is not always readable. XFree86 introduced a feature which can be used to suppress the scaling. In the X server&#8217;s configuration file (e.g., &#8220;/etc/X11/XFree86&#8221; or &#8220;/etc/X11/xorg.conf&#8221;), you can add &#8220;:unscaled&#8221; to the end of the directory specification for the &#8220;misc&#8221; fonts, which comprise the fixed-pitch fonts that are used by <i>xterm</i>. For example<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
FontPath        &quot;/usr/lib/X11/fonts/misc/&quot;
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> would become<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
FontPath        &quot;/usr/lib/X11/fonts/misc/:unscaled&quot;
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Depending on your configuration, the font server may have its own configuration file. The same &#8220;:unscaled&#8221; can be added to its configuration file at the end of the directory specification for &#8220;misc&#8221;.</p>
<dt>
<dd> The bitmap scaling feature is also used by <i>xterm</i> to implement VT102 double-width and double-height characters.</p>
<dt><code>brokenLinuxOSC</code> (class<code> BrokenLinuxOSC</code>)</p>
<dd> If true, <i>xterm</i> applies a workaround to ignore malformed control sequences that a Linux script might send. Compare the palette control sequences documented in <i>console_codes</i> with ECMA-48. The default is &#8220;true&#8221;.</p>
<dt><code>brokenSelections</code> (class<code> BrokenSelections</code>)</p>
<dd> If true, <i>xterm</i> in 8-bit mode will interpret <code>STRING</code> selections as carrying text in the current locale&#8217;s encoding. Normally <code>STRING</code> selections carry ISO-8859-1 encoded text. Setting this resource to &#8220;true&#8221; violates the ICCCM; it may, however, be useful for interacting with some broken X clients. The default is &#8220;false&#8221;.</p>
<dt><code>brokenStringTerm</code> (class<code> BrokenStringTerm</code>)</p>
<dd> provides a work-around for some ISDN routers which start an application control string without completing it. Set this to &#8220;true&#8221; if <i>xterm</i> appears to freeze when connecting. The default is &#8220;false&#8221;.</p>
<dt>
<dd> <i>Xterm</i>&#8216;s state parser recognizes several types of control strings which can contain text, e.g., </p>
<dl>
<dt>
<dd> <code>APC</code> (Application Program Command),<br />
 <code>DCS</code> (Device Control String),<br />
 <code>OSC</code> (Operating System Command),<br />
 <code>PM</code> (Privacy Message), and<br />
 <code>SOS</code> (Start of String),</dl>
<dt>
<dd> Each should end with a string-terminator (a special character which cannot appear in these strings). Ordinary control characters found within the string are not ignored; they are processed without interfering with the process of accumulating the control string&#8217;s content. <i>Xterm</i> recognizes these controls in all modes, although some of the functions may be suppressed after parsing the control.</p>
<dt>
<dd> When enabled, this feature allows the user to exit from an unterminated control string when any of these ordinary control characters are found: </p>
<dl>
<dt>
<dd> control/D (used as an end of file in many shells),<br />
 control/H (backspace),<br />
 control/I (tab-feed),<br />
 control/J (line feed aka newline),<br />
 control/K (vertical tab),<br />
 control/L (form feed),<br />
 control/M (carriage return),<br />
 control/N (shift-out),<br />
 control/O (shift-in),<br />
 control/Q (XOFF),<br />
 control/X (cancel)</dl>
<dt><code>c132</code> (class<code> C132</code>)</p>
<dd> Specifies whether or not the VT102 DECCOLM escape sequence, used to switch between 80 and 132 columns, should be honored. The default is &#8220;false&#8221;.</p>
<dt><code>cacheDoublesize</code> (class<code> CacheDoublesize</code>)</p>
<dd> Tells whether to cache double-sized fonts by <i>xterm</i>. Set this to zero to disable double-sized fonts altogether.</p>
<dt><code>cdXtraScroll</code> (class<code> CdXtraScroll</code>)</p>
<dd> Specifies whether <i>xterm</i> should scroll to a new page when clearing the whole screen. Like <code>tiXtraScroll</code>, the intent of this option is to provide a picture of the full-screen application&#8217;s display on the scrollback before wiping out the text.</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> nothing is added to the scrollback.</p>
<dt>true (1)</p>
<dd> the current screen is added to the scrollback.</p>
<dt>trim (2)</p>
<dd> the current screen is added to the scrollback, but repeated blank lines are trimmed (reduced to a single blank line).</dl>
</dl>
<dt>
<dd> The default for this resource is &#8220;false&#8221;.</p>
<dt><code>charClass</code> (class<code> CharClass</code>)</p>
<dd> Specifies comma-separated lists of character class bindings of the form<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre><code>
low[-high][:value].
</code></pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> These are used in determining which sets of characters should be treated the same when doing cut and paste. See the <code>CHARACTER CLASSES</code> section.</p>
<dt><code>checksumExtension</code> (class<code> ChecksumExtension</code>)</p>
<dd> DEC VT420 and up support a control sequence <code>DECRQCRA</code> which reports the checksum of the characters in a rectangle. <i>Xterm</i> supports this, with extensions that can be configured with bits of the <code>checksumExtension</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> do not negate the result.</p>
<dt>1</p>
<dd> do not report the VT100 video attributes.</p>
<dt>2</p>
<dd> do not omit checksum for blanks.</p>
<dt>3</p>
<dd> omit checksum for cells not explicitly initialized.</p>
<dt>4</p>
<dd> do not mask cell value to 8 bits or ignore combining characters.</p>
<dt>5</p>
<dd> do not mask cell value to 7 bits.</dl>
</dl>
<dt>
<dd> With the default value (0), <i>xterm</i> matches the behavior of DEC&#8217;s terminals. To use all extensions, set all bits, &#8220;-1&#8221; for example.</p>
<dt><code>cjkWidth</code> (class<code> CjkWidth</code>)</p>
<dd> Specifies whether <i>xterm</i> should follow the traditional East Asian width convention. When turned on, characters with East Asian Ambiguous (A) category in UTR 11 have a column width of 2. You may have to set this option to &#8220;true&#8221; if you have some old East Asian terminal based programs that assume that line-drawing characters have a column width of 2. If this resource is false, the <code>mkWidth</code> resource controls the choice between the system&#8217;s <code>wcwidth</code> and <i>xterm</i>&#8216;s built-in tables. The default is &#8220;false&#8221;.</p>
<dt><code>color0</code> (class<code> Color0</code>)</p>
<dd>
<dt><code>color1</code> (class<code> Color1</code>)</p>
<dd>
<dt><code>color2</code> (class<code> Color2</code>)</p>
<dd>
<dt><code>color3</code> (class<code> Color3</code>)</p>
<dd>
<dt><code>color4</code> (class<code> Color4</code>)</p>
<dd>
<dt><code>color5</code> (class<code> Color5</code>)</p>
<dd>
<dt><code>color6</code> (class<code> Color6</code>)</p>
<dd>
<dt><code>color7</code> (class<code> Color7</code>)</p>
<dd> These specify the colors for the ISO-6429 extension. The defaults are, respectively, black, red3, green3, yellow3, a customizable dark blue, magenta3, cyan3, and gray90. The default shades of color are chosen to allow the colors 8-15 to be used as brighter versions.</p>
<dt><code>color8</code> (class<code> Color8</code>)</p>
<dd>
<dt><code>color9</code> (class<code> Color9</code>)</p>
<dd>
<dt><code>color10</code> (class<code> Color10</code>)</p>
<dd>
<dt><code>color11</code> (class<code> Color11</code>)</p>
<dd>
<dt><code>color12</code> (class<code> Color12</code>)</p>
<dd>
<dt><code>color13</code> (class<code> Color13</code>)</p>
<dd>
<dt><code>color14</code> (class<code> Color14</code>)</p>
<dd>
<dt><code>color15</code> (class<code> Color15</code>)</p>
<dd> These specify the colors for the ISO-6429 extension if the bold attribute is also enabled. The default resource values are respectively, gray50, red, green, yellow, a customized light blue, magenta, cyan, and white.</p>
<dt><code>color16</code> (class<code> Color16</code>)</p>
<dd>
<dt>through</p>
<dd>
<dt><code>color255</code> (class<code> Color255</code>)</p>
<dd> These specify the colors for the 256-color extension. The default resource values are for</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 colors 16 through 231 to make a 6x6x6 color cube, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 colors 232 through 255 to make a grayscale ramp.</dl>
<dt>
<dd> Resources past <code>color15</code> are available as a compile-time option. Due to a hardcoded limit in the X libraries on the total number of resources (to 400), the resources for 256-colors are omitted when wide-character support and <i>luit</i> are enabled. Besides inconsistent behavior if only part of the resources were allowed, determining the exact cutoff is difficult, and the X libraries tend to crash if the number of resources exceeds the limit. The color palette is still initialized to the same default values, and can be modified via control sequences.</p>
<dt>
<dd> On the other hand, the resource limit does permit including the entire range for 88-colors.</p>
<dt><code>colorAttrMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether <code>colorBD</code>, <code>colorBL</code>, <code>colorRV</code>, and <code>colorUL</code> should override ANSI colors. If not, these are displayed only when no ANSI colors have been set for the corresponding position. The default is &#8220;false&#8221;.</p>
<dt><code>colorBD</code> (class<code> ColorBD</code>)</p>
<dd> This specifies the color to use to display bold characters if the &#8220;colorBDMode&#8221; resource is enabled. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> See also the <code>veryBoldColors</code> resource which allows combining bold and color.</p>
<dt><code>colorBDMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the bold attribute should be displayed in color or as bold characters. Note that setting <code>colorMode</code> off disables all colors, including bold. The default is &#8220;false&#8221;.</p>
<dt><code>colorBL</code> (class<code> ColorBL</code>)</p>
<dd> This specifies the color to use to display blink characters if the &#8220;colorBLMode&#8221; resource is enabled. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> See also the <code>veryBoldColors</code> resource which allows combining underline and color.</p>
<dt><code>colorBLMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the blink attribute should be displayed in color. Note that setting <code>colorMode</code> off disables all colors, including this. The default is &#8220;false&#8221;.</p>
<dt><code>colorIT</code> (class<code> ColorIT</code>)</p>
<dd> This specifies the color to use to display italic characters if the &#8220;colorITMode&#8221; resource is enabled. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> See also the <code>veryBoldColors</code> resource which allows combining attributes and color.</p>
<dt><code>colorITMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the italic attribute should be displayed in color or as italic characters. The default is &#8220;false&#8221;.</p>
<dt>
<dd> Note that:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Setting <code>colorMode</code> off disables all colors, including italic.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>italicULMode</code> resource overrides <code>colorITMode</code>.</dl>
<dt><code>colorInnerBorder</code> (class<code> ColorInnerBorder</code>)</p>
<dd> Normally, <i>xterm</i> fills the VT100 window&#8217;s inner border using the background color.</p>
<dt>
<dd> If the <code>colorInnerBorder</code> resource is enabled, at startup <i>xterm</i> will compare the <code>borderColor</code> and the window&#8217;s background color. If those are different, <i>xterm</i> will use the <code>borderColor</code> resource to fill the inner border. Otherwise, it will use the window&#8217;s background color.</p>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>colorMode</code> (class<code> ColorMode</code>)</p>
<dd> Specifies whether or not recognition of ANSI (ISO-6429) color change escape sequences should be enabled. The default is &#8220;true&#8221;.</p>
<dt><code>colorRV</code> (class<code> ColorRV</code>)</p>
<dd> This specifies the color to use to display reverse characters if the &#8220;colorRVMode&#8221; resource is enabled. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> See also the <code>veryBoldColors</code> resource which allows combining reverse and color.</p>
<dt><code>colorRVMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the reverse attribute should be displayed in color. Note that setting <code>colorMode</code> off disables all colors, including this. The default is &#8220;false&#8221;.</p>
<dt><code>colorUL</code> (class<code> ColorUL</code>)</p>
<dd> This specifies the color to use to display underlined characters if the &#8220;colorULMode&#8221; resource is enabled. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt>
<dd> See also the <code>veryBoldColors</code> resource which allows combining underline and color.</p>
<dt><code>colorULMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the underline attribute should be displayed in color or as underlined characters. Note that setting <code>colorMode</code> off disables all colors, including underlining. The default is &#8220;false&#8221;.</p>
<dt><code>combiningChars</code> (class<code> CombiningChars</code>)</p>
<dd> Specifies the number of wide-characters which can be stored in a cell to overstrike (combine) with the base character of the cell. This can be set to values in the range 0 to 5. The default is &#8220;2&#8221;.</p>
<dt><code>ctrlFKeys</code> (class<code> CtrlFKeys</code>)</p>
<dd> In VT220 keyboard mode (see <code>sunKeyboard</code> resource), specifies the amount by which to shift F1-F12 given a control modifier (CTRL). This allows you to generate key symbols for F10-F20 on a Sun/PC keyboard. The default is &#8220;10&#8221;, which means that CTRL F1 generates the key symbol for F11.</p>
<dt><code>curses</code> (class<code> Curses</code>)</p>
<dd> Specifies whether or not the last column bug in <i><a href="/docs/linux/man/1-more/">more</a></i>(1) should be worked around. See the <code>-cu</code> option for details. The default is &#8220;false&#8221;.</p>
<dt><code>cursorBlink</code> (class<code> CursorBlink</code>)</p>
<dd> Specifies whether to make the cursor blink. <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> The cursor will not blink, but may be combined with escape sequences according to the <code>cursorBlinkXOR</code> resource.</p>
<dt>true (1)</p>
<dd> The cursor will blink, but may be combined with escape sequences according to the <code>cursorBlinkXOR</code> resource.</p>
<dt>always (2)</p>
<dd> The cursor will always blink, ignoring escape sequences. The menu entry will be disabled.</p>
<dt>never (3)</p>
<dd> The cursor will never blink, ignoring escape sequences. The menu entry will be disabled.</dl>
</dl>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>cursorBlinkXOR</code> (class<code> CursorBlinkXOR</code>)</p>
<dd> <i>Xterm</i> uses two inputs to determine whether the cursor blinks:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <code>cursorBlink</code> resource (which can be altered with a menu entry).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Control sequences (private mode 12 and DECSCUSR).</dl>
<dt>
<dd> The <code>cursorBlinkXOR</code> resource determines how those inputs are combined:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false</p>
<dd>
 <i>Xterm</i> uses the logical-OR of the two variables. If either is set, <i>xterm</i> makes the cursor blink.</p>
<dt>true</p>
<dd>
 <i>Xterm</i> uses the logical-XOR of the two variables. If only one is set, <i>xterm</i> makes the cursor blink.</dl>
</dl>
<dt>
<dd> The default is &#8220;true&#8221;.</p>
<dt><code>cursorColor</code> (class<code> CursorColor</code>)</p>
<dd> Specifies the color to use for the text cursor. The default is &#8220;XtDefaultForeground&#8221;. By default, <i>xterm</i> attempts to keep this color from being the same as the background color, since it draws the cursor by filling the background of a text cell. The same restriction applies to control sequences which may change this color.</p>
<dt>
<dd> Setting this resource overrides most of <i>xterm</i>&#8216;s adjustments to cursor color. It will still use reverse-video to disallow some cases, such as a black cursor on a black background.</p>
<dt><code>cursorOffTime</code> (class<code> CursorOffTime</code>)</p>
<dd> Specifies the duration of the &#8220;off&#8221; part of the cursor blink cycle-time in milliseconds. The same timer is used for text blinking. The default is &#8220;300&#8221;.</p>
<dt><code>cursorOnTime</code> (class<code> CursorOnTime</code>)</p>
<dd> Specifies the duration of the &#8220;on&#8221; part of the cursor blink cycle-time, in milliseconds. The same timer is used for text blinking. The default is &#8220;600&#8221;.</p>
<dt><code>cursorUnderLine</code> (class<code> CursorUnderLine</code>)</p>
<dd> Specifies whether to make the cursor underlined or a box. The default is &#8220;false&#8221;.</p>
<dt><code>cutNewline</code> (class<code> CutNewline</code>)</p>
<dd> If &#8220;false&#8221;, triple clicking to select a line does not include the <i>newline</i> at the end of the line. If &#8220;true&#8221;, the Newline is selected. The default is &#8220;true&#8221;.</p>
<dt><code>cutToBeginningOfLine</code> (class<code> CutToBeginningOfLine</code>)</p>
<dd> If &#8220;false&#8221;, triple clicking to select a line selects only from the current word forward. If &#8220;true&#8221;, the entire line is selected. The default is &#8220;true&#8221;.</p>
<dt><code>decGraphicsID</code> (class<code> DecGraphicsID</code>)</p>
<dd> Allows a way to combine the graphics feature from certain DEC terminals (125, 240, 241, 330, 340 or 382) with other emulation levels which did not provide the graphics feature. As in <code>decTerminalID</code>, leading non-digit characters are ignored, e.g., &#8220;vt340&#8221; and &#8220;340&#8221; are the same.</p>
<dt>
<dd> If the resource value is nonzero, <i>xterm</i> uses that emulation level when initializing the drawing region and decoding control sequences to draw graphics.</p>
<dt>
<dd> The default is &#8220;0&#8221;.</p>
<dt><code>decTerminalID</code> (class<code> DecTerminalID</code>)</p>
<dd> Specifies the emulation level (100=VT100, 220=VT220, etc.), used to determine the type of response to a DA control sequence. Leading non-digit characters are ignored, e.g., &#8220;vt100&#8221; and &#8220;100&#8221; are the same. The default is &#8220;420&#8221;.</p>
<dt><code>defaultString</code> (class<code> DefaultString</code>)</p>
<dd> Specify the character (or string) which <i>xterm</i> will substitute when pasted text includes a character which cannot be represented in the current encoding. For instance, pasting UTF-8 text into a display of ISO-8859-1 characters will only be able to display codes 0-255, while UTF-8 text can include Unicode values above 255. The default is &#8220;#&#8221; (a single pound sign).</p>
<dt>
<dd> If the undisplayable text would be double-width, <i>xterm</i> will add a space after the &#8220;#&#8221; character, to give roughly the same layout on the screen as the original text.</p>
<dt><code>deleteIsDEL</code> (class<code> DeleteIsDEL</code>)</p>
<dd> Specifies what the <i>Delete</i> key on the editing keypad should send when pressed. The resource value is a string, evaluated as a boolean after startup. <i>Xterm</i> uses it in conjunction with the <code>keyboardType</code> resource:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the keyboard type is &#8220;default&#8221;, or &#8220;vt220&#8221; and the resource is either &#8220;true&#8221; or &#8220;maybe&#8221; send the VT220-style <i>Remove</i> escape sequence. Otherwise, send DEL (127).<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the keyboard type is &#8220;legacy&#8221;, and the resource is &#8220;true&#8221; send DEL. Otherwise, send the <i>Remove</i> sequence.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Otherwise, if the keyboard type is none of these special cases, send DEL (127).</dl>
<dt>
<dd> The default is &#8220;Maybe&#8221;. The resource is allowed to be a non-boolean &#8220;maybe&#8221; so that the popup menu <code>Delete is DEL</code> entry does not override the keyboard type.</p>
<dt><code>directColor</code> (class<code> DirectColor</code>)</p>
<dd> Specifies whether to handle direct-color control sequences using the X server&#8217;s available colors, or to approximate those using a color map with 256 entries. A &#8220;true&#8221; value enables the former. The default is &#8220;true&#8221;.</p>
<dt><code>disallowedColorOps</code> (class<code> DisallowedColorOps</code>)</p>
<dd> Specify which features will be disabled if <code>allowColorOps</code> is false. This is a comma-separated list of names. The default value is</p>
<dl>
<dt>
<dd> SetColor,GetColor,GetAnsiColor</dl>
<dt>
<dd> The names are listed below. <i>Xterm</i> ignores capitalization, but they are shown in mixed-case for clarity.</p>
<dl>
<dt>
<dd>
<dl>
<dt>SetColor</p>
<dd> Set a specific dynamic color.</p>
<dt>GetColor</p>
<dd> Report the current setting of a given dynamic color.</p>
<dt>GetAnsiColor</p>
<dd> Report the current setting of a given ANSI color (actually any of the colors set via ANSI-style controls).</dl>
</dl>
<dt><code>disallowedFontOps</code> (class<code> DisallowedFontOps</code>)</p>
<dd> Specify which features will be disabled if <code>allowFontOps</code> is false. This is a comma-separated list of names. The default value is<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
SetFont,GetFont
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> The names are listed below. <i>Xterm</i> ignores capitalization, but they are shown in mixed-case for clarity.</p>
<dl>
<dt>
<dd>
<dl>
<dt>SetFont</p>
<dd> Set the specified font.</p>
<dt>GetFont</p>
<dd> Report the specified font.</dl>
</dl>
<dt><code>disallowedMouseOps</code> (class<code> DisallowedMouseOps</code>)</p>
<dd> Specify which features will be disabled if <code>allowMouseOps</code> is false. This is a comma-separated list of names. The default value is &#8220;*&#8221; which matches all names. The names are listed below. <i>Xterm</i> ignores capitalization, but they are shown in mixed-case for clarity.</p>
<dl>
<dt>
<dd>
<dl>
<dt>X10</p>
<dd> The original X10 mouse protocol.</p>
<dt>Locator</p>
<dd> DEC locator mode</p>
<dt>VT200Click</p>
<dd> X11 mouse-clicks only.</p>
<dt>VT200Hilite</p>
<dd> X11 mouse-clicks and highlighting.</p>
<dt>AnyButton</p>
<dd> XFree86 <i>xterm</i> any-button mode sends button-clicks as well as motion events while the button is pressed.</p>
<dt>AnyEvent</p>
<dd> XFree86 <i>xterm</i> any-event mode sends button-clicks as well as motion events whether or not a button is pressed.</p>
<dt>FocusEvent</p>
<dd> Send FocusIn/FocusOut events.</p>
<dt>Extended</p>
<dd> The first extension beyond X11 mouse protocol, this encodes the coordinates in UTF-8. It is deprecated in favor of <i>SGR</i>, but provided for compatibility.</p>
<dt>SGR</p>
<dd> This is the recommended extension for mouse-coordinates</p>
<dt>URXVT</p>
<dd> Like <i>Extended</i>, this is provided for compatibility.</p>
<dt>AlternateScroll</p>
<dd> This overrides the <code>alternateScroll</code> resource.</dl>
</dl>
<dt><code>disallowedPasteControls</code> (class<code> DisallowedPasteControls</code>)</p>
<dd> The <code>allowPasteControls</code> resource is normally used to prevent pasting C1 controls, as well as non-formatting C0 controls such as the ASCII escape character. Those characters are simply ignored. This resource further extends the set of control characters which cannot be pasted, converting each into a space.</p>
<dt>
<dd> The resource value is a comma-separated list of names. <i>Xterm</i> ignores capitalization. The default value is<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
BS,DEL,ENQ,EOT,ESC,NUL
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> The names are listed below:</p>
<dl>
<dt>
<dd>
<dl>
<dt>C0</p>
<dd> all ASCII control characters.</p>
<dt><i>Individual C0 characters</i></p>
<dd> NUL, SOH, STX, ETX, EOT, ENQ, ACK, BEL, BS, HT, LF, VT, FF, CR, SO, SI, DLE, DC1, DC2, DC3, DC4, NAK, SYN, ETB, CAN, EM, SUB, ESC, FS, GS, RS, US</p>
<dt>DEL</p>
<dd> ASCII delete</p>
<dt>NL</p>
<dd> ASCII line-feed, i.e., &#8220;newline&#8221; is the same as LF.</dl>
</dl>
<dt><code>disallowedTcapOps</code> (class<code> DisallowedTcapOps</code>)</p>
<dd> Specify which features will be disabled if <code>allowTcapOps</code> is false. This is a comma-separated list of names. The default value is<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
SetTcap,GetTcap
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> The names are listed below. <i>Xterm</i> ignores capitalization, but they are shown in mixed-case for clarity.</p>
<dl>
<dt>
<dd>
<dl>
<dt>SetTcap</p>
<dd> (not implemented)</p>
<dt>GetTcap</p>
<dd> Report specified function- and other special keys.</dl>
</dl>
<dt><code>disallowedWindowOps</code> (class<code> DisallowedWindowOps</code>)</p>
<dd> Specify which features will be disabled if <code>allowWindowOps</code> is false. This is a comma-separated list of names, or (for the controls adapted from <i>dtterm</i> the operation number). The default value is<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
1,2,3,4,5,6,7,8,9,11,13,14,18,19,20,21,GetSelection,SetSelection,SetWinLines,SetXprop
(i.e., no operations are allowed).
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> The names are listed below. <i>Xterm</i> ignores capitalization, but they are shown in mixed-case for clarity. Where a number can be used as an alternative, it is given in parentheses after the name.</p>
<dl>
<dt>
<dd>
<dl>
<dt>GetChecksum</p>
<dd> Report checksum of characters in a rectangular region.</p>
<dt>GetIconTitle (20)</p>
<dd> Report <i>xterm</i> window&#8217;s icon label as a string.</p>
<dt>GetScreenSizeChars (19)</p>
<dd> Report the size of the screen in characters as numbers.</p>
<dt>GetSelection</p>
<dd> Report selection data as a base64 string.</p>
<dt>GetWinPosition (13)</p>
<dd> Report <i>xterm</i> window position as numbers.</p>
<dt>GetWinSizeChars (18)</p>
<dd> Report the size of the text area in characters as numbers.</p>
<dt>GetWinSizePixels (14)</p>
<dd> Report <i>xterm</i> window in pixels as numbers.</p>
<dt>GetWinState (11)</p>
<dd> Report <i>xterm</i> window state as a number.</p>
<dt>GetWinTitle (21)</p>
<dd> Report <i>xterm</i> window&#8217;s title as a string.</p>
<dt>LowerWin (6)</p>
<dd> Lower the <i>xterm</i> window to the bottom of the stacking order.</p>
<dt>MaximizeWin (9)</p>
<dd> Maximize window (i.e., resize to screen size).</p>
<dt>FullscreenWin (10)</p>
<dd> Use full screen (i.e., resize to screen size, without window decorations).</p>
<dt>MinimizeWin (2)</p>
<dd> Iconify window.</p>
<dt>PopTitle (23)</p>
<dd> Pop title from internal stack.</p>
<dt>PushTitle (22)</p>
<dd> Push title to internal stack.</p>
<dt>RaiseWin (5)</p>
<dd> Raise the <i>xterm</i> window to the front of the stacking order.</p>
<dt>RefreshWin (7)</p>
<dd> Refresh the <i>xterm</i> window.</p>
<dt>RestoreWin (1)</p>
<dd> De-iconify window.</p>
<dt>SetChecksum</p>
<dd> Modify algorithm for reporting checksum of characters in a rectangular region.</p>
<dt>SetSelection</p>
<dd> Set selection data.</p>
<dt>SetWinLines</p>
<dd> Resize to a given number of lines, at least 24.</p>
<dt>SetWinPosition (3)</p>
<dd> Move window to given coordinates.</p>
<dt>SetWinSizeChars (8)</p>
<dd> Resize the text area to given size in characters.</p>
<dt>SetWinSizePixels (4)</p>
<dd> Resize the <i>xterm</i> window to given size in pixels.</p>
<dt>SetXprop</p>
<dd> Set X property on top-level window.</dl>
</dl>
<dt><code>dynamicColors</code> (class<code> DynamicColors</code>)</p>
<dd> Specifies whether or not escape sequences to change colors assigned to different attributes are recognized.</p>
<dt><code>eightBitControl</code> (class<code> EightBitControl</code>)</p>
<dd> Specifies whether or not control sequences sent by the terminal should be eight-bit characters or escape sequences. The default is &#8220;false&#8221;.</p>
<dt><code>eightBitInput</code> (class<code> EightBitInput</code>)</p>
<dd> If &#8220;true&#8221;, Meta characters (a single-byte character combined with the <i>Meta</i> modifier key) input from the keyboard are presented as a single character, modified according to the <code>eightBitMeta</code> resource. If &#8220;false&#8221;, Meta characters are converted into a two-character sequence with the character itself preceded by ESC. The default is &#8220;true&#8221;.</p>
<dt>
<dd> The <code>metaSendsEscape</code> and <code>altSendsEscape</code> resources may override this feature. Generally keyboards do not have a key labeled &#8220;Meta&#8221;, but &#8220;Alt&#8221; keys are common, and they are conventionally used for &#8220;Meta&#8221;. If they were synonymous, it would have been reasonable to name this resource &#8220;<code>altSendsEscape</code>&#8221;, reversing its sense. For more background on this, see the <code><a href="//www.systutorials.com/docs/linux/man/3x-meta/">meta</a></code>(3x) function in curses.</p>
<dt>
<dd> Note that the <i>Alt</i> key is not necessarily the same as the <i>Meta</i> modifier. The <i>xmodmap</i> utility lists your key modifiers. X defines modifiers for shift, (caps) lock and control, as well as 5 additional modifiers which are generally used to configure key modifiers. <i>Xterm</i> inspects the same information to find the modifier associated with either <i>Meta</i> key (left or right), and uses that key as the <i>Meta</i> modifier. It also looks for the NumLock key, to recognize the modifier which is associated with that.</p>
<dt>
<dd> If your <i>xmodmap</i> configuration uses the same keycodes for Alt- and Meta-keys, <i>xterm</i> will only see the Alt-key definitions, since those are tested before Meta-keys. NumLock is tested first. It is important to keep these keys distinct; otherwise some of <i>xterm</i>&#8216;s functionality is not available.</p>
<dt>
<dd> The <code>eightBitInput</code> resource is tested at startup time. If &#8220;true&#8221;, the <i>xterm</i> tries to put the terminal into 8-bit mode. If &#8220;false&#8221;, on startup, <i>xterm</i> tries to put the terminal into 7-bit mode. For some configurations this is unsuccessful; failure is ignored. After startup, <i>xterm</i> does not change the terminal between 8-bit and 7-bit mode.</p>
<dt>
<dd> As originally implemented in X11, the resource value did not change after startup. However (since patch #216 in 2006) <i>xterm</i> can modify <code>eightBitInput</code> after startup via a control sequence. The corresponding terminfo capabilities <code>smm</code> (set meta mode) and <code>rmm</code> (reset meta mode) have been recognized by <i>bash</i> for some time. Interestingly enough, <i>bash</i>&#8216;s notion of &#8220;meta mode&#8221; differs from the standard definition (in the <i>terminfo</i> manual), which describes the change to the eighth bit of a character. It happens that <i>bash</i> views &#8220;meta mode&#8221; as the ESC character that <i>xterm</i> puts before a character when a special meta key is pressed. <i>bash</i>&#8216;s early documentation talks about the ESC character and ignores the eighth bit.</p>
<dt><code>eightBitMeta</code> (class<code> EightBitMeta</code>)</p>
<dd> This controls the way <i>xterm</i> modifies the eighth bit of a single-byte key when the <code>eightBitInput</code> resource is set. The default is &#8220;locale&#8221;.</p>
<dt>
<dd> The resource value is a string, evaluated as a boolean after startup.</p>
<dl>
<dt>
<dd>
<dl>
<dt>false</p>
<dd> The key is sent unmodified.</p>
<dt>locale</p>
<dd> The key is modified only if the locale uses eight-bit encoding.</p>
<dt>true</p>
<dd> The key is sent modified.</p>
<dt>never</p>
<dd> The key is always sent unmodified.</dl>
</dl>
<dt>
<dd> Except for the <code>never</code> choice, <i>xterm</i> honors the terminfo capabilities <code>smm</code> (set meta mode) and <code>rmm</code> (reset meta mode), allowing the feature to be turned on or off dynamically.</p>
<dt>
<dd> If <code>eightBitMeta</code> is enabled when the locale uses UTF-8, <i>xterm</i> encodes the value as UTF-8 (since patch #183 in 2003).</p>
<dt><code>eightBitOutput</code> (class<code> EightBitOutput</code>)</p>
<dd> Specifies whether or not eight-bit characters sent from the host should be accepted as is or stripped when printed. The default is &#8220;true&#8221;, which means that they are accepted as is.</p>
<dt><code>eightBitSelectTypes</code> (class<code> EightBitSelectTypes</code>)</p>
<dd> Override <i>xterm</i>&#8216;s default selection target list (see <code>SELECT/PASTE</code>) for selections in normal (ISO-8859-1) mode. The default is an empty string, i.e., &#8220;&#8221;, which does not override anything.</p>
<dt><code>eraseSavedLines</code> (class<code> EraseSavedLines</code>)</p>
<dd> Specifies whether or not to allow <i>xterm</i> extended ED/DECSED control sequences to erase the saved-line buffer. The default is &#8220;true&#8221;.</p>
<dt><code>faceName</code> (class<code> FaceName</code>)</p>
<dd> Specify the pattern for scalable fonts selected from the FreeType library if support for that library was compiled into <i>xterm</i>. There is no default value.</p>
<dt>
<dd> One or more fonts can be specified, separated by commas. If prefixed with &#8220;x:&#8221; or &#8220;x11:&#8221; the specification applies to the XLFD <code>font</code> resource. A &#8220;xft:&#8221; prefix is accepted but unnecessary since a missing prefix for <code>faceName</code> means that it will be used for TrueType. For example,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
XTerm*faceName: x:fixed,xft:Bitstream Vera Sans Mono
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> If no <code>faceName</code> resource is specified, or if there is no match for both TrueType normal and bold fonts, <i>xterm</i> uses the XLFD (bitmap) <code>font</code> and related resources.</p>
<dt>
<dd> It is possible to select suitable bitmap fonts using a script such as this:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
#!/bin/sh
FONT=`xfontsel -print`
test -n &quot;$FONT&quot; &amp;&amp; xfd -fn &quot;$FONT&quot;
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> However (even though <i>xfd</i> accepts a &#8220;<code>-fa</code>&#8221; option to denote FreeType fonts), <i>xfontsel</i> has not been similarly extended. As a workaround, you may try<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
fc-list :scalable=true:spacing=mono: family
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> to find a list of scalable fixed-pitch fonts which may be used for the <code>faceName</code> resource value.</p>
<dt><code>faceNameDoublesize</code> (class<code> FaceNameDoublesize</code>)</p>
<dd> Specify a double-width scalable font for cases where an application requires this, e.g., in CJK applications. There is no default value.</p>
<dt>
<dd> Like the <code>faceName</code> resource, this allows one or more comma-separated font specifications to be applied to the <i>wide</i> TrueType or XLFD fonts.</p>
<dt>
<dd> If the application uses double-wide characters and this resource is not given, <i>xterm</i> will use a scaled version of the font given by <code>faceName</code>.</p>
<dt><code>faceSize</code> (class<code> FaceSize</code>)</p>
<dd> Specify the pointsize for fonts selected from the FreeType library if support for that library was compiled into <i>xterm</i>. The default is &#8220;8.0&#8221; On the <code>VT Fonts</code> menu, this corresponds to the <i>Default</i> entry.</p>
<dt>
<dd> Although the default is &#8220;8.0&#8221;, this may not be the same as the pointsize for the default bitmap font, i.e., that assigned with the <code>-fn</code> option, or the <code>font</code> resource. The default value of <code>faceSize</code> is chosen to match the size of the &#8220;fixed&#8221; font, making switching between bitmap and TrueType fonts via the font menu give comparable sizes for the window. If your <code>-fn</code> option uses a different pointsize, you might want to adjust the <code>faceSize</code> resource to match.</p>
<dt>
<dd> You can specify the pointsize for TrueType fonts selected with the other size-related menu entries such as Medium, Huge, etc., by using one of the following resource values. If you do not specify a value, they default to &#8220;0.0&#8221;, which causes <i>xterm</i> to use the ratio of font sizes from the corresponding bitmap font resources to obtain a TrueType pointsize.</p>
<dt>
<dd> If all of the <code>faceSize</code> resources are set, then <i>xterm</i> will use this information to determine the next smaller/larger TrueType font for the <code>larger-vt-font()</code> and <code>smaller-vt-font()</code> actions. If any are not set, <i>xterm</i> will use only the areas of the bitmap fonts.</p>
<dt><code>faceSize1</code> (class<code> FaceSize1</code>)</p>
<dd> Specifies the pointsize of the first alternative font.</p>
<dt><code>faceSize2</code> (class<code> FaceSize2</code>)</p>
<dd> Specifies the pointsize of the second alternative font.</p>
<dt><code>faceSize3</code> (class<code> FaceSize3</code>)</p>
<dd> Specifies the pointsize of the third alternative font.</p>
<dt><code>faceSize4</code> (class<code> FaceSize4</code>)</p>
<dd> Specifies the pointsize of the fourth alternative font.</p>
<dt><code>faceSize5</code> (class<code> FaceSize5</code>)</p>
<dd> Specifies the pointsize of the fifth alternative font.</p>
<dt><code>faceSize6</code> (class<code> FaceSize6</code>)</p>
<dd> Specifies the pointsize of the sixth alternative font.</p>
<dt><code>faceSize7</code> (class<code> FaceSize7</code>)</p>
<dd> Specifies the pointsize of the seventh alternative font.</p>
<dt><code>fastScroll</code> (class<code> FastScroll</code>)</p>
<dd> Modifies the effect of jump scroll (<code>jumpScroll</code>) by suppressing screen refreshes for the special case when output to the screen has completely shifted the contents off-screen. For instance, <i>cat</i>&#8216;ing a large file to the screen does this.</p>
<dt><code>font</code> (class<code> Font</code>)</p>
<dd> Specifies the name of the normal font. The default is &#8220;fixed&#8221;.</p>
<dt>
<dd> See the discussion of the <code>locale</code> resource, which describes how this font may be overridden.</p>
<dt>
<dd> NOTE: some resource files use patterns such as<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
*font: fixed
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> which are overly broad, affecting both<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
xterm.vt100.font
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> and<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
xterm.vt100.utf8Fonts.font
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> which is probably not what you intended.</p>
<dt><code>font1</code> (class<code> Font1</code>)</p>
<dd> Specifies the name of the first alternative font, corresponding to &#8220;Unreadable&#8221; in the standard menu.</p>
<dt><code>font2</code> (class<code> Font2</code>)</p>
<dd> Specifies the name of the second alternative font, corresponding to &#8220;Tiny&#8221; in the standard menu.</p>
<dt><code>font3</code> (class<code> Font3</code>)</p>
<dd> Specifies the name of the third alternative font, corresponding to &#8220;Small&#8221; in the standard menu.</p>
<dt><code>font4</code> (class<code> Font4</code>)</p>
<dd> Specifies the name of the fourth alternative font, corresponding to &#8220;Medium&#8221; in the standard menu.</p>
<dt><code>font5</code> (class<code> Font5</code>)</p>
<dd> Specifies the name of the fifth alternative font, corresponding to &#8220;Large&#8221; in the standard menu.</p>
<dt><code>font6</code> (class<code> Font6</code>)</p>
<dd> Specifies the name of the sixth alternative font, corresponding to &#8220;Huge&#8221; in the standard menu.</p>
<dt><code>font7</code> (class<code> Font7</code>)</p>
<dd> Specifies the name of the seventh alternative font, corresponding to &#8220;Enormous&#8221; in the standard menu.</p>
<dt><code>fontDoublesize</code> (class<code> FontDoublesize</code>)</p>
<dd> Specifies whether <i>xterm</i> should attempt to use font scaling to draw double-sized characters. Some older font servers cannot do this properly, will return misleading font metrics. The default is &#8220;true&#8221;. If disabled, <i>xterm</i> will simulate double-sized characters by drawing normal characters with spaces between them.</p>
<dt><code>fontWarnings</code> (class<code> FontWarnings</code>)</p>
<dd> Specify whether <i>xterm</i> should report an error if it fails to load a font:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Never report an error (though the X libraries may).</p>
<dt>1</p>
<dd> Report an error if the font name was given as a resource setting.</p>
<dt>2</p>
<dd> Always report an error on failure to load a font.</dl>
</dl>
<dt>
<dd> The default is &#8220;1&#8221;.</p>
<dt><code>forceBoxChars</code> (class<code> ForceBoxChars</code>)</p>
<dd> Specifies whether <i>xterm</i> should assume the normal and bold fonts have VT100 line-drawing characters:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The fixed-pitch ISO-8859-*-encoded fonts used by <i>xterm</i> normally have the VT100 line-drawing glyphs in cells 1-31. Other fixed-pitch fonts may be more attractive, but lack these glyphs.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 When using an ISO-10646-1 font and the <code>wideChars</code> resource is true, <i>xterm</i> uses the Unicode glyphs which match the VT100 line-drawing glyphs.</dl>
<dt>
<dd> If &#8220;false&#8221;, <i>xterm</i> checks for missing glyphs in the font and makes line-drawing characters directly as needed. If &#8220;true&#8221;, <i>xterm</i> assumes the font does not contain the line-drawing characters, and draws them directly. The default is &#8220;false&#8221;.</p>
<dt>
<dd> The VT100 line-drawing character set (also known as the <i>DEC Special Character and Line Drawing Set</i>) is shown in this table. It includes a few <i>special</i> characters which are not used for drawing lines: </p>
<table>
<tr VALIGN=top>
<td><i>Cell</i></td>
<td><i>Unicode</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>1</td>
<td>U+25C6</td>
<td>black diamond
</td>
</tr>
<tr VALIGN=top>
<td>2</td>
<td>U+2592</td>
<td>medium shade
</td>
</tr>
<tr VALIGN=top>
<td>3</td>
<td>U+2409</td>
<td>symbol for horizontal tabulation
</td>
</tr>
<tr VALIGN=top>
<td>4</td>
<td>U+240C</td>
<td>symbol for form feed
</td>
</tr>
<tr VALIGN=top>
<td>5</td>
<td>U+240D</td>
<td>symbol for carriage return
</td>
</tr>
<tr VALIGN=top>
<td>6</td>
<td>U+240A</td>
<td>symbol for line feed
</td>
</tr>
<tr VALIGN=top>
<td>7</td>
<td>U+00B0</td>
<td>degree sign
</td>
</tr>
<tr VALIGN=top>
<td>8</td>
<td>U+00B1</td>
<td>plus-minus sign
</td>
</tr>
<tr VALIGN=top>
<td>9</td>
<td>U+2424</td>
<td>symbol for newline
</td>
</tr>
<tr VALIGN=top>
<td>10</td>
<td>U+240B</td>
<td>symbol for vertical tabulation
</td>
</tr>
<tr VALIGN=top>
<td>11</td>
<td>U+2518</td>
<td>box drawings light up and left
</td>
</tr>
<tr VALIGN=top>
<td>12</td>
<td>U+2510</td>
<td>box drawings light down and left
</td>
</tr>
<tr VALIGN=top>
<td>13</td>
<td>U+250C</td>
<td>box drawings light down and right
</td>
</tr>
<tr VALIGN=top>
<td>14</td>
<td>U+2514</td>
<td>box drawings light up and right
</td>
</tr>
<tr VALIGN=top>
<td>15</td>
<td>U+253C</td>
<td>box drawings light vertical and horizontal
</td>
</tr>
<tr VALIGN=top>
<td>16</td>
<td>U+23BA</td>
<td>box drawings scan 1
</td>
</tr>
<tr VALIGN=top>
<td>17</td>
<td>U+23BB</td>
<td>box drawings scan 3
</td>
</tr>
<tr VALIGN=top>
<td>18</td>
<td>U+2500</td>
<td>box drawings light horizontal
</td>
</tr>
<tr VALIGN=top>
<td>19</td>
<td>U+23BC</td>
<td>box drawings scan 7
</td>
</tr>
<tr VALIGN=top>
<td>20</td>
<td>U+23BD</td>
<td>box drawings scan 9
</td>
</tr>
<tr VALIGN=top>
<td>21</td>
<td>U+251C</td>
<td>box drawings light vertical and right
</td>
</tr>
<tr VALIGN=top>
<td>22</td>
<td>U+2524</td>
<td>box drawings light vertical and left
</td>
</tr>
<tr VALIGN=top>
<td>23</td>
<td>U+2534</td>
<td>box drawings light up and horizontal
</td>
</tr>
<tr VALIGN=top>
<td>24</td>
<td>U+252C</td>
<td>box drawings light down and horizontal
</td>
</tr>
<tr VALIGN=top>
<td>25</td>
<td>U+2502</td>
<td>box drawings light vertical
</td>
</tr>
<tr VALIGN=top>
<td>26</td>
<td>U+2264</td>
<td>less-than or equal to
</td>
</tr>
<tr VALIGN=top>
<td>27</td>
<td>U+2265</td>
<td>greater-than or equal to
</td>
</tr>
<tr VALIGN=top>
<td>28</td>
<td>U+03C0</td>
<td>greek small letter pi
</td>
</tr>
<tr VALIGN=top>
<td>29</td>
<td>U+2260</td>
<td>not equal to
</td>
</tr>
<tr VALIGN=top>
<td>30</td>
<td>U+00A3</td>
<td>pound sign
</td>
</tr>
<tr VALIGN=top>
<td>31</td>
<td>U+00B7</td>
<td>middle dot
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=3>
<hr>
</td>
</tr>
</table>
<dt><code>forcePackedFont</code> (class<code> ForcePackedFont</code>)</p>
<dd> Specifies whether <i>xterm</i> should use the maximum or minimum glyph width when displaying using a bitmap font. Use the maximum width to help with proportional fonts. The default is &#8220;true&#8221;, denoting the minimum width.</p>
<dt><code>forceXftHeight</code> (class<code> ForceXftHeight</code>)</p>
<dd> Specifies whether <i>xterm</i> should use the given font metrics for TrueType fonts, or amend the ascent/descent to total no more than the given font-height. This optional feature is used to work around inconsistencies in FreeType&#8217;s rounding computation. The default is &#8220;false&#8221;, denoting the given metrics.</p>
<dt><code>foreground</code> (class<code> Foreground</code>)</p>
<dd> Specifies the color to use for displaying text in the window. Setting the class name instead of the instance name is an easy way to have everything that would normally appear in the text color change color. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt><code>formatOtherKeys</code> (class<code> FormatOtherKeys</code>)</p>
<dd> Overrides the format of the escape sequence used to report modified keys with the <code>modifyOtherKeys</code> resource.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> send modified keys as parameters for function-key 27 (default).</p>
<dt>1</p>
<dd> send modified keys as parameters for CSI u.</dl>
</dl>
<dt><code>freeBoldBox</code> (class<code> FreeBoldBox</code>)</p>
<dd> Specifies whether <i>xterm</i> should assume the bounding boxes for normal and bold fonts are compatible. If &#8220;false&#8221;, <i>xterm</i> compares them and will reject choices of bold fonts that do not match the size of the normal font. The default is &#8220;false&#8221;, which means that the comparison is performed.</p>
<dt><code>geometry</code> (class<code> Geometry</code>)</p>
<dd> Specifies the preferred size and position of the VT<i>xxx</i> window. There is no default for this resource.</p>
<dt><code>highlightColor</code> (class<code> HighlightColor</code>)</p>
<dd> Specifies the color to use for the background of selected (highlighted) text. If not specified (i.e., matching the default foreground), reverse video is used. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt><code>highlightColorMode</code> (class<code> HighlightColorMode</code>)</p>
<dd> Specifies whether <i>xterm</i> should use <code>highlightTextColor</code> and <code>highlightColor</code> to override the reversed foreground/background colors in a selection. The default is unspecified: at startup, <i>xterm</i> checks if those resources are set to something other than the default foreground and background colors. Setting this resource disables the check.</p>
<dt>
<dd> The following table shows the interaction of the highlighting resources, abbreviated as shown to fit in this page:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>HCM</i></p>
<dd> highlightColorMode</p>
<dt><i>HR</i></p>
<dd> highlightReverse</p>
<dt><i>HBG</i></p>
<dd> highlightColor</p>
<dt><i>HFG</i></p>
<dd> highlightTextColor</dl>
</dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><i>HCM</i></td>
<td><i>HR</i></td>
<td><i>HBG</i></td>
<td><i>HFG</i></td>
<td><i>Highlight</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>false</td>
<td>default</td>
<td>set</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>false</td>
<td>set</td>
<td>default</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>false</td>
<td>set</td>
<td>set</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>default</td>
<td>default</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>default</td>
<td>set</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>set</td>
<td>default</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>set</td>
<td>set</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>default</td>
<td>default</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>default</td>
<td>set</td>
<td>HFG/fg
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>set</td>
<td>default</td>
<td>bg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>set</td>
<td>set</td>
<td>HFG/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>default</td>
<td>default</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>default</td>
<td>set</td>
<td>HFG/fg
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>set</td>
<td>default</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>set</td>
<td>set</td>
<td>HFG/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>false</td>
<td>default</td>
<td>default</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>false</td>
<td>default</td>
<td>set</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>false</td>
<td>set</td>
<td>default</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>false</td>
<td>set</td>
<td>set</td>
<td>HFG/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>true</td>
<td>default</td>
<td>default</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>true</td>
<td>default</td>
<td>set</td>
<td>bg/fg
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>true</td>
<td>set</td>
<td>default</td>
<td>fg/HBG
</td>
</tr>
<tr VALIGN=top>
<td>default</td>
<td>true</td>
<td>set</td>
<td>set</td>
<td>HFG/HBG
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=5>
<hr>
<hr>
</td>
</tr>
</table>
<dt><code>highlightReverse</code> (class<code> HighlightReverse</code>)</p>
<dd> Specifies whether <i>xterm</i> should reverse the selection foreground and background colors when selecting text with reverse-video attribute. This applies only to the <code>highlightColor</code> and <code>highlightTextColor</code> resources, e.g., to match the color scheme of <i>xwsh</i>. If &#8220;true&#8221;, <i>xterm</i> reverses the colors, If &#8220;false&#8221;, <i>xterm</i> does not reverse colors, The default is &#8220;true&#8221;.</p>
<dt><code>highlightSelection</code> (class<code> HighlightSelection</code>)</p>
<dd> Tells <i>xterm</i> whether to highlight all of the selected positions, or only the selected text:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;false&#8221;, selecting with the mouse highlights all positions on the screen between the beginning of the selection and the current position.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;true&#8221;, <i>xterm</i> highlights only the positions that contain text that can be selected.</dl>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt>
<dd> Depending on the way your applications write to the screen, there may be trailing blanks on a line. <i>Xterm</i> stores data as it is shown on the screen. Erasing the display changes the internal state of each cell so it is not considered a blank for the purpose of selection. Blanks written since the last erase are selectable. If you do not wish to have trailing blanks in a selection, use the <code>trimSelection</code> resource.</p>
<dt><code>highlightTextColor</code> (class<code> HighlightTextColor</code>)</p>
<dd> Specifies the color to use for the foreground of selected (highlighted) text. If not specified (i.e., matching the default background), reverse video is used. The default is &#8220;XtDefaultBackground&#8221;.</p>
<dt><code>hpLowerleftBugCompat</code> (class<code> HpLowerleftBugCompat</code>)</p>
<dd> Specifies whether to work around a bug in HP&#8217;s <i>xdb</i>, which ignores termcap and always sends ESC F to move to the lower left corner. &#8220;true&#8221; causes <i>xterm</i> to interpret ESC F as a request to move to the lower left corner of the screen. The default is &#8220;false&#8221;.</p>
<dt><code>i18nSelections</code> (class<code> I18nSelections</code>)</p>
<dd> If false, <i>xterm</i> will not request the targets <code>COMPOUND_TEXT</code> or <code>TEXT</code>. The default is &#8220;true&#8221;. It may be set to false in order to work around ICCCM violations by other X clients.</p>
<dt><code>iconBorderColor</code> (class<code> BorderColor</code>)</p>
<dd> Specifies the border color for the active icon window if this feature is compiled into <i>xterm</i>. Not all window managers will make the icon border visible.</p>
<dt><code>iconBorderWidth</code> (class<code> BorderWidth</code>)</p>
<dd> Specifies the border width for the active icon window if this feature is compiled into <i>xterm</i>. The default is &#8220;2&#8221;. Not all window managers will make the border visible.</p>
<dt><code>iconFont</code> (class<code> IconFont</code>)</p>
<dd> Specifies the font for the miniature active icon window, if this feature is compiled into <i>xterm</i>. The default is &#8220;nil2&#8221;.</p>
<dt><code>indicatorFormat</code> (class<code> IndicatorFormat</code>)</p>
<dd> When displaying the status line using the <i>indicator</i> mode (i.e., selecting DECSSDT line type 1), format the status using this resource.</p>
<dt>
<dd> The default value of the resource displays the version of <i>xterm</i>, the cursor position and the time/date:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4<br />
&#8220;% {version % } &amp; nbsp;<br />
&amp;nbsp;<br />
% {position % } &amp; nbsp;<br />
&amp;nbsp;<br />
%<br />
{<br />
    unixtime %<br />
}<br />
&#8221;</p>
<p>&nbsp;.in -4</p>
<dt>
<dd> If a &#8220;%&#8221; marker does not match any of the three special tokens used in the default resource setting, <i>xterm</i> uses <code>strftime</code> to interpret it.</p>
<dt><code>initialFont</code> (class<code> InitialFont</code>)</p>
<dd> Specifies which of the VT100 fonts to use initially. Values are the same as for the <code>set-vt-font</code> action. The default is &#8220;d&#8221;, i.e., &#8220;default&#8221;.</p>
<dt><code>inputMethod</code> (class<code> InputMethod</code>)</p>
<dd> Tells <i>xterm</i> which type of input method to use. There is no default method.</p>
<dt><code>internalBorder</code> (class<code> BorderWidth</code>)</p>
<dd> Specifies the number of pixels between the characters and the window border. The default is &#8220;2&#8221;.</p>
<dt><code>italicULMode</code> (class<code> ColorAttrMode</code>)</p>
<dd> Specifies whether characters with the underline attribute should be displayed in an italic font or as underlined characters. It is implemented only for TrueType fonts.</p>
<dt><code>jumpScroll</code> (class<code> JumpScroll</code>)</p>
<dd> Specifies whether or not jump scroll should be used. This corresponds to the VT102 DECSCLM private mode. The default is &#8220;true&#8221;. See <code>fastScroll</code> for a variation.</p>
<dt><code>keepClipboard</code> (class<code> KeepClipboard</code>)</p>
<dd> Specifies whether <i>xterm</i> will reuse the selection data which it copied to the clipboard rather than asking the clipboard for its current contents when told to provide the selection. The default is &#8220;false&#8221;.</p>
<dt>
<dd> If compiled into <i>xterm</i>, the menu entry <code>Keep Clipboard</code> allows you to change this at runtime.</p>
<dt><code>keepSelection</code> (class<code> KeepSelection</code>)</p>
<dd> Specifies whether <i>xterm</i> will keep the selection even after the selected area was touched by some output to the terminal. The default is &#8220;true&#8221;.</p>
<dt>
<dd> The menu entry <code>Keep Selection</code> allows you to change this at runtime.</p>
<dt><code>keyboardDialect</code> (class<code> KeyboardDialect</code>)</p>
<dd> Specifies the initial keyboard dialect, as well as the default value when the terminal is reset. The value given is the same as the final character in the control sequences which change character sets. The default is &#8220;B&#8221;, which corresponds to US ASCII.</p>
<dt><code>limitFontsets</code> (class<code> LimitFontsets</code>)</p>
<dd> Limits the number of TrueType fallback fonts (i.e., fontset) which can be used. The default is &#8220;50&#8221;.</p>
<dt>
<dd> This limits the number of fallback fonts which <i>xterm</i> uses to display characters. Because TrueType fonts typically are small, <i>xterm</i> may open several fonts for good coverage, and may open additional fonts to obtain information. You can see which font-files <i>xterm</i> opens by setting the environment variable <code>XFT_DEBUG</code> to 3. The Xft library and <i>xterm</i> write this debugging trace to the standard output.</p>
<dt>
<dd> Set this to &#8220;0&#8221; to disable fallbacks entirely.</p>
<dt><code>limitResize</code> (class<code> LimitResize</code>)</p>
<dd> Limits resizing of the screen via control sequence to a given multiple of the display dimensions. The default is &#8220;1&#8221;.</p>
<dt><code>limitResponse</code> (class<code> LimitResponse</code>)</p>
<dd> Limits the buffer-size used when <i>xterm</i> replies to various control sequences. The default is &#8220;1024&#8221;. The minimum value is &#8220;256&#8221;.</p>
<dt><code>locale</code> (class<code> Locale</code>)</p>
<dd> Specifies how to use <i>luit</i>, an encoding converter between UTF-8 and locale encodings. The resource value (ignoring case) may be:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>true</i></p>
<dd> <i>Xterm</i> will use the encoding specified by the users&#8217; LC_CTYPE locale (i.e., LC_ALL, LC_CTYPE, or LANG variables) as far as possible. This is realized by always enabling UTF-8 mode and invoking <i>luit</i> in non-UTF-8 locales.</p>
<dt><i>medium</i></p>
<dd> <i>Xterm</i> will follow users&#8217; LC_CTYPE locale only for UTF-8, east Asian, and Thai locales, where the encodings were not supported by conventional 8bit mode with changing fonts. For other locales, <i>xterm</i> will use conventional 8bit mode.</p>
<dt><i>checkfont</i></p>
<dd> If mini-luit is compiled-in, <i>xterm</i> will check if a Unicode font has been specified. If so, it checks if the character encoding for the current locale is POSIX, Latin-1 or Latin-9, uses the appropriate mapping to support those with the Unicode font. For other encodings, <i>xterm</i> assumes that UTF-8 encoding is required.</p>
<dt><i>false</i></p>
<dd> <i>Xterm</i> will use conventional 8bit mode or UTF-8 mode according to <code>utf8</code> resource or <code>-u8</code> option.</dl>
</dl>
<dt>
<dd> Any other value, e.g., &#8220;UTF-8&#8221; or &#8220;ISO8859-2&#8221;, is assumed to be an encoding name; <i>luit</i> will be invoked to support the encoding. The actual list of supported encodings depends on <i>luit</i>. The default is &#8220;medium&#8221;.</p>
<dt>
<dd> Regardless of your locale and encoding, you need an ISO-10646-1 font to display the result. Your configuration may not include this font, or locale-support by <i>xterm</i> may not be needed.</p>
<dt>
<dd> At startup, <i>xterm</i> uses a mechanism equivalent to the <code>load-vt-fonts(utf8Fonts, Utf8Fonts)</code> action to load font name subresources of the VT100 widget. That is, resource patterns such as &#8220;<code>*vt100.utf8Fonts.font</code>&#8221; will be loaded, and (if this resource is enabled), override the normal fonts. If no subresources are found, the normal fonts such as &#8220;<code>*vt100.font</code>&#8221;, etc., are used.</p>
<dt>
<dd> For instance, you could have this in your resource file:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
*VT100.font: 12x24
*VT100.utf8Fonts.font:9x15
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> When started with a UTF-8 locale, <i>xterm</i> would use 9&#215;15, but allow you to switch to the 12&#215;24 font using the menu entry &#8220;<code>UTF-8 Fonts</code>&#8221;.</p>
<dt>
<dd> The resource files distributed with <i>xterm</i> use ISO-10646-1 fonts, but do not rely on them unless you are using the locale mechanism.</p>
<dt><code>localeFilter</code> (class<code> LocaleFilter</code>)</p>
<dd> Specifies the file name for the encoding converter from/to locale encodings and UTF-8 which is used with the <code>-lc</code> option or <code>locale</code> resource. The help message shown by &#8220;xterm -help&#8221; lists the default value, which depends on your system configuration.</p>
<dt>
<dd> If the encoding converter requires command-line parameters, you can add those after the command, e.g.,<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
*localeFilter: xterm-filter -p
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Alternatively, you may put those parameter within a shell script to execute the converter, and set this resource to point to the shell script.</p>
<dt>
<dd> When using a locale-filter, e.g., with the <i>-e</i> option, or the shell, <i>xterm</i> first tries passing control via that filter. If it fails, <i>xterm</i> will retry without the locale-filter. <i>Xterm</i> warns about the failure before retrying.</p>
<dt><code>logFile</code> (class<code> Logfile</code>)</p>
<dd> Specify the name for <i>xterm</i>&#8216;s log file. If no name is specified, <i>xterm</i> will generate a name when logging is enabled, as described in the <code>-l</code> option.</p>
<dt><code>logInhibit</code> (class<code> LogInhibit</code>)</p>
<dd> If &#8220;true&#8221;, prevent the logging feature from being enabled, whether by the command-line option <code>-l</code>, or the menu entry <code>Log to File</code>. The default is &#8220;false&#8221;.</p>
<dt><code>logging</code> (class<code> Logging</code>)</p>
<dd> If &#8220;true&#8221;, (and if <code>logInhibit</code> is not set) enable the logging feature. This resource is set/updated by the <code>-l</code> option and the menu entry <code>Log to File</code>. The default is &#8220;false&#8221;.</p>
<dt><code>loginShell</code> (class<code> LoginShell</code>)</p>
<dd> Specifies whether or not the shell to be run in the window should be started as a login shell. The default is &#8220;false&#8221;.</p>
<dt><code>marginBell</code> (class<code> MarginBell</code>)</p>
<dd> Specifies whether or not the bell should be rung when the user types near the right margin. The default is &#8220;false&#8221;.</p>
<dt><code>maxGraphicSize</code> (class<code> MaxGraphicSize</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS or SIXEL graphics, this resource controls the maximum size of a graph which can be displayed.</p>
<dt>
<dd> The default is &#8220;1000&#215;1000&#8221; (given as <i>width</i> by <i>height</i>).</p>
<dt>
<dd> If the resource is &#8220;auto&#8221; then <i>xterm</i> will use the <code>decGraphicsID</code> resource (or <code>decTerminalID</code> if that is not set): </p>
<table>
<tr VALIGN=top>
<td><code>Result</code></td>
<td><code>decGraphicsID</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>800&#215;460</td>
<td ALIGN=right>240
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>800&#215;460</td>
<td ALIGN=right>241
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>800&#215;480</td>
<td ALIGN=right>330
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>800&#215;480</td>
<td ALIGN=right>340
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>860&#215;750</td>
<td ALIGN=right>382
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>800&#215;480</td>
<td ALIGN=right><i>other</i>
</td>
</tr>
</table>
<dt><code>metaSendsEscape</code> (class<code> MetaSendsEscape</code>)</p>
<dd> Tells <i>xterm</i> what to do with input-characters modified by <i>Meta</i>:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;true&#8221;, Meta characters (a character combined with the <i>Meta</i> modifier key) are converted into a two-character sequence with the character itself preceded by ESC. This applies as well to function key control sequences, unless <i>xterm</i> sees that <code>Meta</code> is used in your key translations.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If &#8220;false&#8221;, Meta characters input from the keyboard are handled according to the <code>eightBitInput</code> resource.</dl>
<dt>
<dd> The default is &#8220;False&#8221;.</p>
<dt><code>mkSamplePass</code> (class<code> MkSamplePass</code>)</p>
<dd> If <code>mkSampleSize</code> is nonzero, and <code>mkWidth</code> (and <code>cjkWidth</code>) are false, on startup <i>xterm</i> compares its built-in tables to the system&#8217;s wide character width data to decide if it will use the system&#8217;s data. It tests the first <code>mkSampleSize</code> character values, and allows up to <code>mkSamplePass</code> mismatches before the test fails. The default (for the allowed number of mismatches) is 655 (one percent of the default value for <code>mkSampleSize</code>).</p>
<dt><code>mkSampleSize</code> (class<code> MkSampleSize</code>)</p>
<dd> With <code>mkSamplePass</code>, this specifies a startup test used for initializing wide character width calculations. The default (number of characters to check) is 65536.</p>
<dt><code>mkWidth</code> (class<code> MkWidth</code>)</p>
<dd> Specifies whether <i>xterm</i> should use a built-in version of the wide character width calculation. See also the <code>cjkWidth</code> resource which can override this. The default is &#8220;false&#8221;.</p>
<dt>
<dd> Here is a summary of the resources which control the choice of wide character width calculation: </p>
<table>
<tr VALIGN=top>
<td><i>cjkWidth</i></td>
<td><i>mkWidth</i></td>
<td><i>Action</i>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td>false</td>
<td>true</td>
<td>use built-in tables
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>false</td>
<td>use built-in CJK tables
</td>
</tr>
<tr VALIGN=top>
<td>true</td>
<td>true</td>
<td>use built-in CJK tables
</td>
</tr>
</table>
<dt>
<dd> To disable <code>mkWidth</code>, and use the system&#8217;s tables, set both <code>mkSampleSize</code> and <code>mkSamplePass</code> to &#8220;0&#8221;. Doing that may make <i>xterm</i> more consistent with applications running in <i>xterm</i>, but may omit some font glyphs whose width correctly differs from the system&#8217;s character tables.</p>
<dt><code>modifyCursorKeys</code> (class<code> ModifyCursorKeys</code>)</p>
<dd> Tells how to handle the special case where Control-, Shift-, Alt- or Meta-modifiers are used to add a parameter to the escape sequence returned by a cursor-key. The default is &#8220;2&#8221;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> disables the feature.</p>
<dt>0</p>
<dd> uses the old/obsolete behavior, i.e., the modifier is the first parameter.</p>
<dt>1</p>
<dd> prefixes modified sequences with CSI.</p>
<dt>2</p>
<dd> forces the modifier to be the second parameter if it would otherwise be the first.</p>
<dt>3</p>
<dd> marks the sequence with a &#8220;&gt;&#8221; to hint that it is private.</dl>
</dl>
<dt><code>modifyFunctionKeys</code> (class<code> ModifyFunctionKeys</code>)</p>
<dd> Tells how to handle the special case where Control-, Shift-, Alt- or Meta-modifiers are used to add a parameter to the escape sequence returned by a (numbered) function-key. The default is &#8220;2&#8221;. The resource values are similar to <code>modifyCursorKeys</code>:</p>
<dl>
<dt>
<dd>
<dl>
<dt>-1</p>
<dd> permits the user to use shift- and control-modifiers to construct function-key strings using the normal encoding scheme.</p>
<dt>0</p>
<dd> uses the old/obsolete behavior, i.e., the modifier is the first parameter.</p>
<dt>1</p>
<dd> prefixes modified sequences with CSI.</p>
<dt>2</p>
<dd> forces the modifier to be the second parameter if it would otherwise be the first.</p>
<dt>3</p>
<dd> marks the sequence with a &#8220;&gt;&#8221; to hint that it is private.</dl>
</dl>
<dt>
<dd> If <code>modifyFunctionKeys</code> is zero, <i>xterm</i> uses Control- and Shift-modifiers to allow the user to construct numbered function-keys beyond the set provided by the keyboard:</p>
<dl>
<dt>
<dd>
<dl>
<dt>Control</p>
<dd> adds the value given by the <code>ctrlFKeys</code> resource.</p>
<dt>Shift</p>
<dd> adds twice the value given by the <code>ctrlFKeys</code> resource.</p>
<dt>Control/Shift</p>
<dd> adds three times the value given by the <code>ctrlFKeys</code> resource.</dl>
</dl>
<dt>
<dd>
<dt><code>modifyKeyboard</code> (class<code> ModifyKeyboard</code>)</p>
<dd> Normally <i>xterm</i> makes a special case regarding modifiers (shift, control, etc.) to handle special keyboard layouts (<code>legacy</code> and <code>vt220</code>). This is done to provide compatible keyboards for DEC VT220 and related terminals that implement user-defined keys (UDK).</p>
<dt>
<dd> The bits of the resource value selectively enable modification of the given category when these keyboards are selected. The default is &#8220;0&#8221;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> The legacy/vt220 keyboards interpret only the Control-modifier when constructing numbered function-keys. Other special keys are not modified.</p>
<dt>1</p>
<dd> allows modification of the numeric keypad</p>
<dt>2</p>
<dd> allows modification of the editing keypad</p>
<dt>4</p>
<dd> allows modification of function-keys, overrides use of Shift-modifier for UDK.</p>
<dt>8</p>
<dd> allows modification of other special keys</dl>
</dl>
<dt><code>modifyOtherKeys</code> (class<code> ModifyOtherKeys</code>)</p>
<dd> Like <code>modifyCursorKeys</code>, tells <i>xterm</i> to construct an escape sequence for <i>ordinary</i> (i.e., &#8220;other&#8221;) keys (such as &#8220;2&#8221;) when modified by Shift-, Control-, Alt- or Meta-modifiers. This feature does not apply to <i>special keys</i>, i.e., cursor-, keypad-, function- or control-keys which are labeled on your keyboard. Those have key symbols which XKB identifies uniquely.</p>
<dt>
<dd> For example, this feature does not apply to <i>special</i> control-keys (e.g., Escape, Tab, Enter, Backspace) Other control keys (e.g., Control-I, Control-M, Control-H) may send escape sequences when this feature is enabled.</p>
<dt>
<dd> The default is &#8220;0&#8221;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> disables this feature.</p>
<dt>1</p>
<dd> enables this feature for keys except for those with well-known behavior, e.g., Tab, Backarrow and some special control character cases which are built into the X11 library, e.g., Control-Space to make a NUL, or Control-3 to make an Escape character.</p>
<dt>
<dd> Except for those special cases built into the X11 library, the Shift- and Control- modifiers are treated normally. The Alt- and Meta- modifiers do not cause <i>xterm</i> to send escape sequences. Those modifier keys are interpreted according to other resources, e.g., the <code>metaSendsEscape</code> resource.</p>
<dt>2</p>
<dd> enables this feature for keys including the exceptions listed. <i>Xterm</i> ignores the special cases built into the X11 library. Any shifted (modified) ordinary key sends an escape sequence. The Alt- and Meta- modifiers cause <i>xterm</i> to send escape sequences.</dl>
</dl>
<dt>
<dd> The <i>Xterm</i> FAQ has an extended discussion of this feature, with examples: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://invisible-island.net/xterm/modified-keys.html">https://invisible-island.net/xterm/modified-keys.html</a></dl>
<dt><code>multiClickTime</code> (class<code> MultiClickTime</code>)</p>
<dd> Specifies the maximum time in milliseconds between multi-click select events. The default is &#8220;250&#8221; milliseconds.</p>
<dt><code>multiScroll</code> (class<code> MultiScroll</code>)</p>
<dd> Specifies whether or not scrolling should be done asynchronously. The default is &#8220;false&#8221;.</p>
<dt><code>nMarginBell</code> (class<code> Column</code>)</p>
<dd> Specifies the number of characters from the right margin at which the margin bell should be rung, when enabled by the <code>marginBell</code> resource. The default is &#8220;10&#8221;.</p>
<dt><i>name</i><code>Keymap</code> (class<i>Name</i><code>Keymap</code>)</p>
<dd> See the discussion of the <code>keymap()</code> action.</p>
<dt><code>nextEventDelay</code> (class<code> NextEventDelay</code>)</p>
<dd> Specifies a delay time in milliseconds before checking for new X events. The default is &#8220;1&#8221;.</p>
<dt><code>numColorRegisters</code> (class<code> NumColorRegisters</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS or SIXEL graphics, this specifies the number of color-registers which are available.</p>
<dt>
<dd> If this resource is not specified, <i>xterm</i> uses a value determined by the <code>decTerminalID</code> resource: </p>
<table>
<tr VALIGN=top>
<td><code>Result</code></td>
<td><code>decTerminalID</code>
</td>
</tr>
<tr VALIGN=top>
<td>
<hr>
</td>
<td>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=right>240
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=right>241
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>4</td>
<td ALIGN=right>330
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>16</td>
<td ALIGN=right>340
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>2</td>
<td ALIGN=right>382
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=right>1024</td>
<td ALIGN=right><i>other</i>
</td>
</tr>
</table>
<dt><code>numLock</code> (class<code> NumLock</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> checks if NumLock is used as a modifier (see <code><a href="/docs/linux/man/1-xmodmap/">xmodmap</a></code>(1)). If so, this modifier is used to simplify the logic when implementing special NumLock for the <code>sunKeyboard</code> resource. Also (when <code>sunKeyboard</code> is false), similar logic is used to find the modifier associated with the left and right Alt keys. The default is &#8220;true&#8221;.</p>
<dt><code>oldXtermFKeys</code> (class<code> OldXtermFKeys</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will use old-style (X11R5) escape sequences for function keys F1 to F4, for compatibility with X Consortium <i>xterm</i>. Otherwise, it uses the VT100 codes for PF1 to PF4. The default is &#8220;false&#8221;.</p>
<dt>
<dd> Setting this resource has the same effect as setting the <code>keyboardType</code> to <code>legacy</code>. The <code>keyboardType</code> resource is the preferred mechanism for selecting this mode.</p>
<dt>
<dd> The old-style escape sequences resemble VT220 keys, but appear to have been invented for <i>xterm</i> in X11R4.</p>
<dt><code>on2Clicks</code> (class<code> On2Clicks</code>)</p>
<dd>
<dt><code>on3Clicks</code> (class<code> On3Clicks</code>)</p>
<dd>
<dt><code>on4Clicks</code> (class<code> On4Clicks</code>)</p>
<dd>
<dt><code>on5Clicks</code> (class<code> On5Clicks</code>)</p>
<dd> Specify selection behavior in response to multiple mouse clicks. A single mouse click is always interpreted as described in the <code>Selection Functions</code> section (see <code>POINTER USAGE</code>). Multiple mouse clicks (using the button which activates the <code>select-start</code> action) are interpreted according to the resource values of <code>on2Clicks</code>, etc. The resource value can be one of these:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>word</code></p>
<dd> Select a &#8220;word&#8221; as determined by the <code>charClass</code> resource. See the <code>CHARACTER CLASSES</code> section.</p>
<dt>
<dd> If the pointer is on a &#8220;word&#8221; then <i>xterm</i> searches back to the beginning of the word, and then to the end.</p>
<dt>
<dd> If the pointer is not on a &#8220;word&#8221; then the result depends on whether it is on whitespace (including a newline), or past the end of the line. In the latter case <i>xterm</i> may select a &#8220;word&#8221; beginning after the newline, if there is no additional whitespace.</p>
<dt><code>line</code></p>
<dd> Select a line (counting wrapping).</p>
<dt><code>group</code></p>
<dd> Select a group of adjacent lines (counting wrapping). The selection stops on a blank line, and does not extend outside the current page.</p>
<dt><code>page</code></p>
<dd> Select all visible lines, i.e., the page.</p>
<dt><code>all</code></p>
<dd>
 Select all lines, i.e., including the saved lines.</p>
<dt><code>regex</code></p>
<dd> Select the best match for the POSIX extended regular expression (ERE) which follows in the resource value:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> matches the regular expression against a byte array for the entire (possibly wrapped) line. That byte array may be UTF-8 or ISO-8859-1, depending on the mode in which <i>xterm</i> is running.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> steps through each byte-offset in this array, keeping track of the best (longest) match. If more than one match ties for the longest length, the first is used.</p>
<dl>
<dt>
<dd> <i>Xterm</i> does this to make it convenient to click anywhere in the area of interest and cause the regular expression to match the entire word, etc.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The &#8220;^&#8221; and &#8220;$&#8221; anchors in a regular expression denote the ends of the entire line.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the regular expression contains backslashes &#8220;\&#8221; those should be escaped &#8220;\&#8221; because the X libraries interpret backslashes in resource strings.</dl>
</dl>
<dt><code>none</code></p>
<dd> No selection action is associated with this resource. <i>Xterm</i> interprets it as the end of the list. For example, you may use it to disable triple (and higher) clicking by setting <code>on3Clicks</code> to &#8220;none&#8221;.</dl>
</dl>
<dt>
<dd> The default values for <code>on2Clicks</code> and <code>on3Clicks</code> are &#8220;word&#8221; and &#8220;line&#8221;, respectively. There is no default value for <code>on4Clicks</code> or <code>on5Clicks</code>, making those inactive. On startup, <i>xterm</i> determines the maximum number of clicks by the <code>on</code><i>X</i><code>Clicks</code> resource values which are set.</p>
<dt><code>openIm</code> (class<code> OpenIm</code>)</p>
<dd> Tells <i>xterm</i> whether to open the input method at startup. The default is &#8220;true&#8221;.</p>
<dt><code>pointerColor</code> (class<code> PointerColor</code>)</p>
<dd> Specifies the foreground color of the pointer. The default is &#8220;XtDefaultForeground&#8221;.</p>
<dt><code>pointerColorBackground</code> (class<code> PointerColorBackground</code>)</p>
<dd> Specifies the background color of the pointer. The default is &#8220;XtDefaultBackground&#8221;.</p>
<dt><code>pointerFont</code> (class<code> PointerFont</code>)</p>
<dd> Specifies the font to be used for the pointer. The shapes specified by <code>pointerShape</code> are glyphs in this font. The resource value default is <i>cursor</i>.</p>
<dt><code>pointerMode</code> (class<code> PointerMode</code>)</p>
<dd> Specifies when the pointer may be hidden as the user types. It will be redisplayed if the user moves the mouse, or clicks one of its buttons.</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> never</p>
<dt>1</p>
<dd> the application running in <i>xterm</i> has not activated mouse mode. This is the default.</p>
<dt>2</p>
<dd> always.</dl>
</dl>
<dt><code>pointerShape</code> (class<code> Cursor</code>)</p>
<dd> Specifies the name of the shape of the pointer. The default is &#8220;xterm&#8221;.</p>
<dt>
<dd> Other shapes can be selected. Here is a list of the &#8220;core&#8221; (i.e., <i>standard</i>) names extracted from &lt;X11/cursorfont.h&gt;:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> X_cursor, arrow, based_arrow_down, based_arrow_up, boat, bogosity, bottom_left_corner, bottom_right_corner, bottom_side, bottom_tee, box_spiral, center_ptr, circle, clock, coffee_mug, cross, cross_reverse, crosshair, diamond_cross, dot, dotbox, double_arrow, draft_large, draft_small, draped_box, exchange, fleur, gobbler, gumby, hand1, hand2, heart, icon, iron_cross, left_ptr, left_side, left_tee, leftbutton, ll_angle, lr_angle, man, middlebutton, mouse, pencil, pirate, plus, question_arrow, right_ptr, right_side, right_tee, rightbutton, rtl_logo, sailboat, sb_down_arrow, sb_h_double_arrow, sb_left_arrow, sb_right_arrow, sb_up_arrow, sb_v_double_arrow, shuttle, sizing, spider, spraycan, star, target, tcross, top_left_arrow, top_left_corner, top_right_corner, top_side, top_tee, trek, ul_angle, umbrella, ur_angle, watch, xterm</dl>
</dl>
<dt>
<dd> If you are using a <i>cursor theme</i>, expect it to provide about a third of those names, while adding others.</p>
<dt><code>popOnBell</code> (class<code> PopOnBell</code>)</p>
<dd> Specifies whether the window would be raised when Control-G is received. The default is &#8220;false&#8221;.</p>
<dt>
<dd> If the window is iconified, this has no effect. However, the <code>zIconBeep</code> resource provides you with the ability to see which iconified windows have sounded a bell.</p>
<dt><code>precompose</code> (class<code> Precompose</code>)</p>
<dd> Tells <i>xterm</i> whether to precompose UTF-8 data into Normalization Form C, which combines commonly-used accents onto base characters. If it does not do this, accents are left as separate characters. The default is &#8220;true&#8221;.</p>
<dt><code>preeditType</code> (class<code> PreeditType</code>)</p>
<dd> Tells <i>xterm</i> which types of preedit (preconversion) string to display. The default is &#8220;OverTheSpot,Root&#8221;.</p>
<dt><code>printAttributes</code> (class<code> PrintAttributes</code>)</p>
<dd> Specifies whether to print graphic attributes along with the text. A real DEC VT<i>xxx</i> terminal will print the underline, highlighting codes but your printer may not handle these.</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;0&#8221; disables the attributes.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;1&#8221; prints the normal set of attributes (bold, underline, inverse and blink) as VT100-style control sequences.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 &#8220;2&#8221; prints ANSI color attributes as well.</dl>
<dt>
<dd> The default is &#8220;1&#8221;.</p>
<dt><code>printFileImmediate</code> (class <code>PrintFileImmediate</code>)</p>
<dd> When the <code>print-immediate</code> action is invoked, <i>xterm</i> prints the screen contents directly to a file. Set this resource to the prefix of the filename (a timestamp will be appended to the actual name).</p>
<dt>
<dd> The default is an empty string, i.e., &#8220;&#8221;, However, when the <code>print-immediate</code> action is invoked, if the string is empty, then &#8220;XTerm&#8221; is used.</p>
<dt><code>printFileOnXError</code> (class <code>PrintFileOnXError</code>)</p>
<dd> If <i>xterm</i> exits with an X error, e.g., your connection is broken when the server crashes, it can be told to write the contents of the screen to a file. To enable the feature, set this resource to the prefix of the filename (a timestamp will be appended to the actual name).</p>
<dt>
<dd> The default is an empty string, i.e., &#8220;&#8221;, which disables this feature. However, when the <code>print-on-error</code> action is invoked, if the string is empty, then &#8220;XTermError&#8221; is used.</p>
<dt>
<dd> These error codes are handled: ERROR_XERROR, ERROR_XIOERROR and ERROR_ICEERROR.</p>
<dt><code>printModeImmediate</code> (class <code>PrintModeImmediate</code>)</p>
<dd> When the <code>print-immediate</code> action is invoked, <i>xterm</i> prints the screen contents directly to a file. You can use the <code>printModeImmediate</code> resource to tell it to use escape sequences to reconstruct the video attributes and colors. This uses the same values as the <code>printAttributes</code> resource. The default is &#8220;0&#8221;.</p>
<dt><code>printModeOnXError</code> (class <code>PrintModeOnXError</code>)</p>
<dd> <i>Xterm</i> implements the <code>printFileOnXError</code> feature using the printer feature, although the output is written directly to a file. You can use the <code>printModeOnXError</code> resource to tell it to use escape sequences to reconstruct the video attributes and colors. This uses the same values as the <code>printAttributes</code> resource. The default is &#8220;0&#8221;.</p>
<dt><code>printOptsImmediate</code> (class <code>PrintOptsImmediate</code>)</p>
<dd> Specify the range of text which is printed to a file when the <code>print-immediate</code> action is invoked.</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If zero (0), then this selects the current (visible screen) plus the saved lines, except if the alternate screen is being used. In that case, only the alternate screen is selected.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If nonzero, the bits of this resource value (checked in descending order) select the range:</p>
<dl>
<dt>
<dd>
<dl>
<dt>8</p>
<dd> selects the saved lines.</p>
<dt>4</p>
<dd> selects the alternate screen.</p>
<dt>2</p>
<dd> selects the normal screen.</p>
<dt>1</p>
<dd> selects the current screen, which can be either the normal or alternate screen.</dl>
</dl>
</dl>
<dt>
<dd> The default is &#8220;9&#8221;, which selects the current visible screen plus saved lines, with no special case for the alternated screen.</p>
<dt><code>printOptsOnXError</code> (class <code>PrintOptsOnXError</code>)</p>
<dd> Specify the range of text which is printed to a file when the <code>print-on-error</code> action is invoked. The resource value is interpreted the same as in <code>printOptsImmediate</code>.</p>
<dt>
<dd> The default is &#8220;9&#8221;, which selects the current visible screen plus saved lines, with no special case for the alternated screen.</p>
<dt><code>printerAutoClose</code> (class<code> PrinterAutoClose</code>)</p>
<dd> If &#8220;true&#8221;, <i>xterm</i> will close the printer (a pipe) when the application switches the printer offline with a Media Copy command. The default is &#8220;false&#8221;.</p>
<dt><code>printerCommand</code> (class<code> PrinterCommand</code>)</p>
<dd> Specifies a shell command to which <i>xterm</i> will open a pipe when the first MC (Media Copy) command is initiated. The default is an empty string, i.e., &#8220;&#8221;. If the resource value is given as an empty string, the printer is disabled.</p>
<dt><code>printerControlMode</code> (class<code> PrinterControlMode</code>)</p>
<dd> Specifies the printer control mode. A &#8220;1&#8221; selects autoprint mode, which causes <i>xterm</i> to print a line from the screen when</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 you move the cursor off that line with a line feed, form feed or vertical tab character, or<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 an autowrap occurs.</dl>
<dt>
<dd> Autoprint mode is overridden by printer controller mode (a &#8220;2&#8221;), which causes all of the output to be directed to the printer. The default is &#8220;0&#8221;.</p>
<dt><code>printerExtent</code> (class<code> PrinterExtent</code>)</p>
<dd> Controls whether a print page function will print the entire page (true), or only the portion within the scrolling margins (false). The default is &#8220;false&#8221;.</p>
<dt><code>printerFormFeed</code> (class<code> PrinterFormFeed</code>)</p>
<dd> Controls whether a form feed is sent to the printer at the end of a print page function. The default is &#8220;false&#8221;.</p>
<dt><code>printerNewLine</code> (class<code> PrinterNewLine</code>)</p>
<dd> Controls whether a newline is sent to the printer at the end of a print page function. The default is &#8220;true&#8221;.</p>
<dt><code>privateColorRegisters</code> (class<code> PrivateColorRegisters</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS or SIXEL graphics, this controls whether <i>xterm</i> allocates separate color registers for each sixel device control string, e.g., for DECGCI. If not true, color registers are allocated only once, when the terminal is reset, and color changes in any graphic affect all graphics. The default is &#8220;true&#8221;.</p>
<dt><code>quietGrab</code> (class<code> QuietGrab</code>)</p>
<dd> Controls whether the cursor is repainted when <i>NotifyGrab</i> and <i>NotifyUngrab</i> event types are received during change of focus. The default is &#8220;false&#8221;.</p>
<dt><code>regisDefaultFont</code> (class<code> RegisDefaultFont</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS graphics, this resource tells <i>xterm</i> which font to use if the ReGIS data does not specify one. No default value is specified; <i>xterm</i> accepts a TrueType font specification as in the <code>faceName</code> resource.</p>
<dt>
<dd> If no value is specified, <i>xterm</i> draws a bitmap indicating a missing character.</p>
<dt><code>regisScreenSize</code> (class<code> RegisScreenSize</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS graphics, this resource tells <i>xterm</i> the default size (in pixels) for these graphics, which also sets the default coordinate space to [0,0] (upper-left) and [<i>width</i>,<i>height</i>] (lower-right).</p>
<dt>
<dd> The application using ReGIS may use the &#8220;A&#8221; option of the &#8220;S&#8221; command to adjust the coordinate space or change the addressable portion of the screen.</p>
<dt>
<dd> <i>Xterm</i> accepts a special resource value &#8220;auto&#8221;, which tells <i>xterm</i> to use the <code>decGraphicsID</code> and <code>decTerminalID</code> resources to set the default size based on the hardware terminal&#8217;s limits. Those limits are the same as for the <code>maxGraphicSize</code> resource.</p>
<dt>
<dd> The default is &#8220;auto&#8221;.</p>
<dt><code>renderFont</code> (class<code> RenderFont</code>)</p>
<dd> If <i>xterm</i> is built with the Xft library, this controls whether the <code>faceName</code> resource is used. The default is &#8220;default&#8221;.</p>
<dt>
<dd> The resource values are strings, evaluated as booleans after startup.</p>
<dl>
<dt>
<dd>
<dl>
<dt>false</p>
<dd>
 disable the feature and use the normal (bitmap) font.</p>
<dt>true</p>
<dd>
 startup using the TrueType font specified by the <code>faceName</code> and <code>faceSize</code> resource settings. If there is no value for <code>faceName</code>, disable the feature and use the normal (bitmap) font.</p>
<dt>
<dd> After startup, you can still switch to/from the bitmap font using the &#8220;TrueType Fonts&#8221; menu entry.</p>
<dt>default</p>
<dd>
 Enable the &#8220;TrueType Fonts&#8221; menu entry to allow runtime switching to/from TrueType fonts. The initial font used depends upon whether the <code>faceName</code> resource is set:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <code>faceName</code> resource is not set, start by using the normal (bitmap) font. <i>Xterm</i> has a separate compiled-in value for <code>faceName</code> for this special case. That is normally &#8220;mono&#8221;.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <code>faceName</code> resource is set, then start by using the TrueType font rather than the bitmap font.</dl>
<dt>defaultOff</p>
<dd>
 Enable the &#8220;TrueType Fonts&#8221; menu entry to allow runtime switching to/from TrueType fonts, but allow it to be initially unselected if no <code>faceName</code> resource was given.</dl>
</dl>
<dt><code>resizeByPixel</code> (class<code> ResizeByPixel</code>)</p>
<dd> Set this &#8220;true&#8221; to disable hints to the window manager that request resizing by character rather than pixels.</p>
<dt>
<dd> Most window managers provide visual feedback showing the size of a window as you resize it, using these hints. When you maximize <i>xterm</i>, it disables those hints to allow the window manager to make better use of fractional rows or columns. Setting this resource disables the hints all the time.</p>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>resizeGravity</code> (class<code> ResizeGravity</code>)</p>
<dd> Affects the behavior when the window is resized to be taller or shorter. <code>NorthWest</code> specifies that the top line of text on the screen stay fixed. If the window is made shorter, lines are dropped from the bottom; if the window is made taller, blank lines are added at the bottom. This is compatible with the behavior in X11R4. <code>SouthWest</code> (the default) specifies that the bottom line of text on the screen stay fixed. If the window is made taller, additional saved lines will be scrolled down onto the screen; if the window is made shorter, lines will be scrolled off the top of the screen, and the top saved lines will be dropped.</p>
<dt><code>retryInputMethod</code> (class<code> RetryInputMethod</code>)</p>
<dd> Tells <i>xterm</i> how many times to retry, in case the input-method server is not responding. This is a different issue than unsupported preedit type, etc. You may encounter retries if your X configuration (and its libraries) are missing pieces. Setting this resource to zero &#8220;0&#8221; will cancel the retrying. The default is &#8220;3&#8221;.</p>
<dt><code>reverseVideo</code> (class<code> ReverseVideo</code>)</p>
<dd> Specifies whether or not reverse video should be simulated. The default is &#8220;false&#8221;.</p>
<dt>
<dd> There are several aspects to reverse video in <i>xterm</i>:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 The command-line <code>-rv</code> option tells the X libraries to reverse the foreground and background colors. <i>Xterm</i>&#8216;s command-line options set resource values. In particular, the X Toolkit sets the <code>reverseVideo</code> resource when the <code>-rv</code> option is used.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the user has also used command-line options <code>-fg</code> or <code>-bg</code> to set the foreground and background colors, <i>xterm</i> does not see these options directly. Instead, it examines the resource values to reconstruct the command-line options, and determine which of the colors is the user&#8217;s intended foreground, etc. Their actual values are irrelevant to the reverse video function; some users prefer the X defaults (black text on a white background), others prefer white text on a black background.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 After startup, the user can toggle the &#8220;Enable Reverse Video&#8221; menu entry. This exchanges the current foreground and background colors of the VT100 widget, and repaints the screen. Because of the X resource hierarchy, the <code>reverseVideo</code> resource applies to more than the VT100 widget.</dl>
<dt>
<dd> Programs running in an <i>xterm</i> can also use control sequences to enable the VT100 reverse video mode. These are independent of the <code>reverseVideo</code> resource and the menu entry. <i>Xterm</i> exchanges the current foreground and background colors when drawing text affected by these control sequences.</p>
<dt>
<dd> Other control sequences can alter the foreground and background colors which are used:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Programs can also use the ANSI color control sequences to set the foreground and background colors.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Extensions to the ANSI color controls (such as 16-, 88- or 256-colors) are treated similarly to the ANSI control.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Using other control sequences (the &#8220;<i>dynamic colors</i>&#8221; feature), a program can change the foreground and background colors.</dl>
<dt><code>reverseWrap</code> (class<code> ReverseWrap</code>)</p>
<dd> Specifies whether or not reverse-wraparound should be enabled. This corresponds to <i>xterm</i>&#8216;s private mode 45. The default is &#8220;false&#8221;.</p>
<dt><code>rightScrollBar</code> (class<code> RightScrollBar</code>)</p>
<dd> Specifies whether or not the scrollbar should be displayed on the right rather than the left. The default is &#8220;false&#8221;.</p>
<dt><code>saveLines</code> (class<code> SaveLines</code>)</p>
<dd> Specifies the number of lines to save beyond the top of the screen when a scrollbar is turned on. The default is &#8220;1024&#8221;.</p>
<dt><code>scrollBar</code> (class<code> ScrollBar</code>)</p>
<dd> Specifies whether or not the scrollbar should be displayed. The default is &#8220;false&#8221;.</p>
<dt><code>scrollBarBorder</code> (class<code> ScrollBarBorder</code>)</p>
<dd> Specifies the width of the scrollbar border. Note that this is drawn to overlap the border of the <i>xterm</i> window. Modifying the scrollbar&#8217;s border affects only the line between the VT100 widget and the scrollbar. The default value is 1.</p>
<dt><code>scrollKey</code> (class<code> ScrollCond</code>)</p>
<dd> Specifies whether or not pressing a key should automatically cause the scrollbar to go to the bottom of the scrolling region. This corresponds to <i>xterm</i>&#8216;s private mode 1011. The default is &#8220;false&#8221;.</p>
<dt><code>scrollLines</code> (class<code> ScrollLines</code>)</p>
<dd> Specifies the number of lines that the <code>scroll-back</code> and <code>scroll-forw</code> actions should use as a default. The default value is 1.</p>
<dt><code>scrollTtyOutput</code> (class<code> ScrollCond</code>)</p>
<dd> Specifies whether or not output to the terminal should automatically cause the scrollbar to go to the bottom of the scrolling region. The default is &#8220;true&#8221;.</p>
<dt><code>selectToClipboard</code> (class<code> SelectToClipboard</code>)</p>
<dd> Tells <i>xterm</i> whether to use the <code>PRIMARY</code> or <code>CLIPBOARD</code> for <code>SELECT</code> tokens in the selection mechanism. The <code>set-select</code> action can change this at runtime, allowing the user to work with programs that handle only one of these mechanisms. The default is &#8220;false&#8221;, which tells it to use <code>PRIMARY</code>.</p>
<dt><code>shiftEscape</code> (class<code> ShiftEscape</code>)</p>
<dd> <i>Xterm</i> uses the <code>translations</code> resource to determine how to invoke actions for selecting and copying text using the pointer (e.g., a mouse). It also provides a mouse protocol which can be used by applications running in an xterm to detect mouse button clicks.</p>
<dt>
<dd> The mouse protocol causes <i>xterm</i> to send special escape sequences which allow an application to determine if <i>modifiers</i> (i.e., one or more of <i>shift</i>, <i>control</i>, <i>alt</i>, and <i>meta</i>) were used.</p>
<dt>
<dd> <i>Xterm</i> provides this mouse protocol by interpreting button- and motion-events in the functions which the <code>translations</code> resource calls for selecting and copying text:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
<code>insert-selection</code>
<code>select-end</code>
<code>select-extend</code>
<code>select-start</code>
<code>start-extend</code>
</pre>
</dl>
</dl>
<dt>
<dd> While the mouse protocol is active, <i>xterm</i> reserves most of the mouse button events for sending special escape sequences to the application. <i>Xterm</i> normally allows you to use the <i>shift</i>-key to temporarily override this mouse protocol, permitting the selection and copying actions to be used.</p>
<dt>
<dd> The <code>shiftEscape</code> resource setting allows you to tell <i>xterm</i> whether to use the <i>shift</i>-key in this way (i.e., overriding the mouse protocol). <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> Mouse protocol does not send special escapes when <i>shift</i>-key is used.</p>
<dt>true (1)</p>
<dd> Mouse protocol may send special escapes when <i>shift</i>-key is used.</p>
<dt>
<dd> At startup, <i>xterm</i> analyzes the <code>translations</code> to see which buttons are used in the (mouse) button-related bindings for selection and copying text. If the <i>shift</i>-key is not mentioned explicitly in a button&#8217;s binding, <i>xterm</i> allows that button with <i>shift</i>-key for overriding the mouse protocol.</p>
<dt>always (2)</p>
<dd> Mouse protocol can always send special escapes when <i>shift</i>-key is used.</p>
<dt>never (3)</p>
<dd> Mouse protocol will never send special escapes when <i>shift</i>-key is used.</dl>
</dl>
<dt>
<dd> <i>Xterm</i> interprets a control sequence which can change this setting between &#8220;true&#8221; and &#8220;false&#8221;. The default is &#8220;false&#8221;.</p>
<dt><code>shiftFonts</code> (class<code> ShiftFonts</code>)</p>
<dd> Specifies whether to enable the actions <code>larger-vt-font()</code> and <code>smaller-vt-font()</code>, which are normally bound to the shifted KP_Add and KP_Subtract. The default is &#8220;true&#8221;.</p>
<dt><code>showBlinkAsBold</code> (class<code> ShowBlinkAsBold</code>)</p>
<dd> Tells <i>xterm</i> whether to display text with blink-attribute the same as bold. If <i>xterm</i> has not been configured to support blinking text, the default is &#8220;true&#8221;, which corresponds to older versions of <i>xterm</i>, otherwise the default is &#8220;false&#8221;.</p>
<dt><code>showMissingGlyphs</code> (class<code> ShowMissingGlyphs</code>)</p>
<dd> Tells <i>xterm</i> whether to display a box outlining places where a character has been used that the font does not represent. The default is &#8220;false&#8221;.</p>
<dt><code>showWrapMarks</code> (class<code> ShowWrapMarks</code>)</p>
<dd> For debugging <i>xterm</i> and applications that may manipulate the wrapped-line flag by writing text at the right margin, show a mark on the right inner-border of the window. The mark shows which lines have the flag set.</p>
<dt><code>signalInhibit</code> (class<code> SignalInhibit</code>)</p>
<dd> Specifies whether or not the entries in the <code>Main Options</code> menu for sending signals to <i>xterm</i> should be disallowed. The default is &#8220;false&#8221;.</p>
<dt><code>sixelScrolling</code> (class<code> SixelScrolling</code>)</p>
<dd> If <i>xterm</i> is configured to support SIXEL graphics, this resource tells it whether to scroll up one line at a time when sixels would be written past the bottom line on the window. The default is &#8220;false&#8221; which enables scrolling.</p>
<dt><code>sixelScrollsRight</code> (class<code> SixelScrollsRight</code>)</p>
<dd> If <i>xterm</i> is configured to support SIXEL graphics, this resource tells it whether to scroll to the right as needed to keep the current position visible rather than truncate the plot on the on the right. The default is &#8220;false&#8221; which disables scrolling.</p>
<dt><code>tekGeometry</code> (class<code> Geometry</code>)</p>
<dd> Specifies the preferred size and position of the Tektronix window. There is no default for this resource.</p>
<dt><code>tekInhibit</code> (class<code> TekInhibit</code>)</p>
<dd> Specifies whether or not the escape sequence to enter Tektronix mode should be ignored. The default is &#8220;false&#8221;.</p>
<dt><code>tekSmall</code> (class<code> TekSmall</code>)</p>
<dd> Specifies whether or not the Tektronix mode window should start in its smallest size if no explicit geometry is given. This is useful when running <i>xterm</i> on displays with small screens. The default is &#8220;false&#8221;.</p>
<dt><code>tekStartup</code> (class<code> TekStartup</code>)</p>
<dd> Specifies whether or not <i>xterm</i> should start up in Tektronix mode. The default is &#8220;false&#8221;.</p>
<dt><code>tiXtraScroll</code> (class<code> TiXtraScroll</code>)</p>
<dd> Specifies whether <i>xterm</i> should scroll to a new page when processing the <i>ti</i> or <i>te</i> termcap strings, i.e., the private modes 47, 1047 or 1049. This is only in effect if <code>titeInhibit</code> is &#8220;true&#8221;, because the intent of this option is to provide a picture of the full-screen application&#8217;s display on the scrollback without wiping out the text that would be shown before the application was initialized.</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> nothing is added to the scrollback.</p>
<dt>true (1)</p>
<dd> the current screen is added to the scrollback.</p>
<dt>trim (2)</p>
<dd> the current screen is added to the scrollback, but repeated blank lines are trimmed (reduced to a single blank line).</dl>
</dl>
<dt>
<dd> The default for this resource is &#8220;false&#8221;.</p>
<dt><code>titeInhibit</code> (class<code> TiteInhibit</code>)</p>
<dd> Originally specified whether or not <i>xterm</i> should remove <i>ti</i> and <i>te</i> termcap entries (used to switch between alternate screens on startup of many screen-oriented programs) from the TERMCAP string.</p>
<dt>
<dd> TERMCAP is used rarely now, but <i>xterm</i> supports the feature on modern systems:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If set, <i>xterm</i> also ignores the escape sequence to switch to the alternate screen.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 <i>Xterm</i> supports terminfo in a different way, supporting composite control sequences (also known as private modes) 1047, 1048 and 1049 which have the same effect as the original 47 control sequence.</dl>
<dt>
<dd> The default for this resource is &#8220;false&#8221;.</p>
<dt><code>titleModes</code> (class<code> TitleModes</code>)</p>
<dd> Tells <i>xterm</i> whether to accept or return window- and icon-labels in ISO-8859-1 (the default) or UTF-8. Either can be encoded in hexadecimal:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 UTF-8 titles require special treatment, because they may contain bytes which can be mistaken for control characters. Hexadecimal-encoding is supported to eliminate that possibility.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 As an alternative, you could use the <code>allowC1Printable</code> resource, which suppresses <i>xterm</i>&#8216;s parsing of the relevant control characters (and as a result, treats those bytes as data).</dl>
<dt>
<dd> The default for this resource is &#8220;0&#8221;.</p>
<dt>
<dd> Each bit (bit &#8220;0&#8221; is 1, bit &#8220;1&#8221; is 2, etc.) corresponds to one of the parameters set by the title modes control sequence:</p>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> Set window/icon labels using hexadecimal</p>
<dt>1</p>
<dd> Query window/icon labels using hexadecimal</p>
<dt>2</p>
<dd> Set window/icon labels using UTF-8 (gives the same effect as the <code>utf8Title</code> resource).</p>
<dt>3</p>
<dd> Query window/icon labels using UTF-8</dl>
</dl>
<dt><code>translations</code> (class<code> Translations</code>)</p>
<dd> Specifies the key and button bindings for menus, selections, &#8220;programmed strings&#8221;, etc. The <code>translations</code> resource, which provides much of <i>xterm</i>&#8216;s configurability, is a feature of the X Toolkit Intrinsics library (Xt). See the <code>Actions</code> section.</p>
<dt><code>trimSelection</code> (class<code> TrimSelection</code>)</p>
<dd> If you set <code>highlightSelection</code>, you can see the text which is selected, including any trailing spaces. Clearing the screen (or a line) resets it to a state containing no spaces. Some lines may contain trailing spaces when an application writes them to the screen. However, you may not wish to paste lines with trailing spaces. If this resource is true, <i>xterm</i> will trim trailing spaces from text which is selected. It does not affect spaces which result in a wrapped line, nor will it trim the trailing newline from your selection. The default is &#8220;false&#8221;.</p>
<dt><code>underLine</code> (class<code> UnderLine</code>)</p>
<dd> This specifies whether or not text with the underline attribute should be underlined. It may be desirable to disable underlining when color is being used for the underline attribute. The default is &#8220;true&#8221;.</p>
<dt><code>useBorderClipping</code> (class<code> UseBorderClipping</code>)</p>
<dd> Tell <i>xterm</i> whether to apply clipping when <code>useClipping</code> is false. Unlike <code>useClipping</code>, this simply limits text to keep it within the window borders, e.g., as a refinement to the <code>scaleHeight</code> workaround. The default is &#8220;false&#8221;.</p>
<dt><code>useClipping</code> (class<code> UseClipping</code>)</p>
<dd> Tell <i>xterm</i> whether to use clipping to keep from producing dots outside the text drawing area. Originally used to work around for overstriking effects, this is also needed to work with some incorrectly-sized fonts. The default is &#8220;true&#8221;.</p>
<dt><code>utf8</code> (class<code> Utf8</code>)</p>
<dd> This specifies whether <i>xterm</i> will run in UTF-8 mode. If you set this resource, <i>xterm</i> also sets the <code>wideChars</code> resource as a side-effect. The resource can be set via the menu entry &#8220;UTF-8 Encoding&#8221;. The default is &#8220;default&#8221;.</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> UTF-8 mode is initially off. The command-line option <code>+u8</code> sets the resource to this value. Escape sequences for turning UTF-8 mode on/off are allowed.</p>
<dt>true (1)</p>
<dd> UTF-8 mode is initially on. Escape sequences for turning UTF-8 mode on/off are allowed.</p>
<dt>always (2)</p>
<dd> The command-line option <code>-u8</code> sets the resource to this value. Escape sequences for turning UTF-8 mode on/off are ignored.</p>
<dt>default (3)</p>
<dd> This is the default value of the resource. It is changed during initialization depending on whether the <code>locale</code> resource was set, to false (0) or always (2). See the <code>locale</code> resource for additional discussion of non-UTF-8 locales.</dl>
</dl>
<dt>
<dd> If you want to set the value of <code>utf8</code>, it should be in this range. Other nonzero values are treated the same as &#8220;1&#8221;, i.e., UTF-8 mode is initially on, and escape sequences for turning UTF-8 mode on/off are allowed.</p>
<dt><code>utf8Fonts</code> (class<code> Utf8Fonts</code>)</p>
<dd> See the discussion of the <code>locale</code> resource. This specifies whether <i>xterm</i> will use UTF-8 fonts specified via resource patterns such as &#8220;<code>*vt100.utf8Fonts.font</code>&#8221; or normal (ISO-8859-1) fonts via patterns such as &#8220;<code>*vt100.font</code>&#8221;. The resource can be set via the menu entry &#8220;<code>UTF-8 Fonts</code>&#8221;. The default is &#8220;default&#8221;.</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> Use the ISO-8859-1 fonts. The menu entry is enabled, allowing the choice of fonts to be changed at runtime.</p>
<dt>true (1)</p>
<dd> Use the UTF-8 fonts. The menu entry is enabled, allowing the choice of fonts to be changed at runtime.</p>
<dt>always (2)</p>
<dd> Always use the UTF-8 fonts. This also disables the menu entry.</p>
<dt>default (3)</p>
<dd> At startup, the resource is set to true or false, according to the effective value of the <code>utf8</code> resource.</dl>
</dl>
<dt><code>utf8Latin1</code> (class<code> Utf8Latin1</code>)</p>
<dd> If true, allow an ISO-8859-1 <i>normal</i> font to be combined with an ISO-10646-1 font if the latter is given via the <code>-fw</code> option or its corresponding resource value. The default is &#8220;false&#8221;.</p>
<dt><code>utf8SelectTypes</code> (class<code> Utf8SelectTypes</code>)</p>
<dd> Override <i>xterm</i>&#8216;s default selection target list (see <code>SELECT/PASTE</code>) for selections in wide-character (UTF-8) mode. The default is an empty string, i.e., &#8220;&#8221;, which does not override anything.</p>
<dt><code>utf8Title</code> (class<code> Utf8Title</code>)</p>
<dd> Applications can set <i>xterm</i>&#8216;s title by writing a control sequence. Normally this control sequence follows the VT220 convention, which encodes the string in ISO-8859-1 and allows for an 8-bit string terminator. If <i>xterm</i> is started in a UTF-8 locale, it translates the ISO-8859-1 string to UTF-8 to work with the X libraries which assume the string is UTF-8.</p>
<dt>
<dd> However, some users may wish to write a title string encoded in UTF-8. The window manager is responsible for drawing window titles. Some window managers (not all) support UTF-8 encoding of window titles. Set this resource to &#8220;true&#8221; to also set UTF-8 encoded title strings using the EWMH properties.</p>
<dt>
<dd> This feature is available as a menu entry, since it is related to the particular applications you are running within <i>xterm</i>. You can also use a control sequence (see the discussion of &#8220;Title Modes&#8221; in <i>Xterm Control Sequences</i>), to set an equivalent flag (which can also be set using the <code>titleModes</code> resource).</p>
<dt>
<dd> <i>Xterm</i> accepts either a keyword (ignoring case) or the number shown in parentheses:</p>
<dl>
<dt>
<dd>
<dl>
<dt>false (0)</p>
<dd> Set only ISO-8859-1 title strings, e.g., using the ICCCM <code>WM_NAME</code> STRING property. The menu entry is enabled, allowing the choice of title-strings to be changed at runtime.</p>
<dt>true (1)</p>
<dd> Set both the EWMH (UTF-8 strings) and the ICCCM <code>WM_NAME</code>, etc. The menu entry is enabled, allowing the choice to be changed at runtime.</p>
<dt>always (2)</p>
<dd> Always set both the EWMH (UTF-8 strings) and the ICCCM <code>WM_NAME</code>, etc. This also disables the menu entry.</p>
<dt>default (3)</p>
<dd> At startup, the resource is set to true or false, according to the effective value of the <code>utf8</code> resource.</dl>
</dl>
<dt>
<dd> The default is &#8220;default&#8221;.</p>
<dt><code>utf8Weblike</code> (class<code> Utf8Weblike</code>)</p>
<dd> Provide an alternate error-handling scheme for ill-formed UTF-8 as recommended in a W3C document. The Unicode standard does not require this for conformance. Some additional information can be found here: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="https://invisible-island.net/xterm/bad-utf8/">https://invisible-island.net/xterm/bad-utf8/</a></dl>
<dt>
<dd> The default is &#8220;false&#8221;.</p>
<dt><code>veryBoldColors</code> (class<code> VeryBoldColors</code>)</p>
<dd> Specifies whether to combine video attributes with colors specified by <code>colorBD</code>, <code>colorBL</code>, <code>colorIT</code>, <code>colorRV</code>, and <code>colorUL</code>. The resource value is the sum of values for each attribute:</p>
<dl>
<dt>
<dd>
1 for reverse,<br />
2 for underline,<br />
4 for bold,<br />
8 for blink, and<br />
512 for italic
</dl>
<dt>
<dd> The default is &#8220;0&#8221;.</p>
<dt><code>visualBell</code> (class<code> VisualBell</code>)</p>
<dd> Specifies whether or not a visible bell (i.e., flashing) should be used instead of an audible bell when Control-G is received. The default is &#8220;false&#8221;, which tells <i>xterm</i> to use an audible bell.</p>
<dt><code>visualBellDelay</code> (class<code> VisualBellDelay</code>)</p>
<dd> Number of milliseconds to delay when displaying a visual bell. Default is 100. If set to zero, no visual bell is displayed. This is useful for very slow displays, e.g., an LCD display on a laptop.</p>
<dt><code>visualBellLine</code> (class<code> VisualBellLine</code>)</p>
<dd> Specifies whether to flash only the current line when displaying a visual bell rather than flashing the entire screen: The default is &#8220;false&#8221;, which tells <i>xterm</i> to flash the entire screen.</p>
<dt><code>vt100Graphics</code> (class<code> VT100Graphics</code>)</p>
<dd> This specifies whether <i>xterm</i> will interpret VT100 graphic character escape sequences while in UTF-8 mode. This feature also applies to code-pages (e.g., for VT320 and VT520) and National Replacement Character Sets (VT220 and up), but not US-ASCII (the initially selected character set), to avoid conflict with UTF-8. The default is &#8220;true&#8221;, to provide support for various legacy applications.</p>
<dt><code>wideBoldFont</code> (class<code> WideBoldFont</code>)</p>
<dd> This option specifies the font to be used for displaying bold wide text. By default, it will attempt to use a font twice as wide as the font that will be used to draw bold text. If no double-width font is found, it will improvise, by stretching the bold font.</p>
<dt><code>wideChars</code> (class<code> WideChars</code>)</p>
<dd> Specifies if <i>xterm</i> should respond to control sequences that process 16-bit characters. The default is &#8220;false&#8221;.</p>
<dt><code>wideFont</code> (class<code> WideFont</code>)</p>
<dd> This option specifies the font to be used for displaying wide text. By default, it will attempt to use a font twice as wide as the font that will be used to draw normal text. If no double-width font is found, it will improvise, by stretching the normal font.</p>
<dt><code>ximFont</code> (class<code> XimFont</code>)</p>
<dd> This option specifies the font to be used for displaying the preedit string in the &#8220;OverTheSpot&#8221; input method.</p>
<dt>
<dd> In &#8220;OverTheSpot&#8221; preedit type, the preedit (preconversion) string is displayed at the position of the cursor. It is the XIM server&#8217;s responsibility to display the preedit string. The XIM client must inform the XIM server of the cursor position. For best results, the preedit string must be displayed with a proper font. Therefore, <i>xterm</i> informs the XIM server of the proper font. The font is be supplied by a &quot;fontset&quot;, whose default value is &#8220;*&#8221;. This matches every font, the X library automatically chooses fonts with proper charsets. The <code>ximFont</code> resource is provided to override this default font setting.</dl>
<h3>Tek4014 Widget Resources</h3>
<p> The following resources are specified as part of the <i>tek4014</i> widget (class <i>Tek4014</i>). These are specified by patterns such as &#8220;<code>XTerm.tek4014.</code><i>NAME</i>&#8221;:</p>
<dl>
<dt><code>font2</code> (class<code> Font</code>)</p>
<dd> Specifies font number 2 to use in the Tektronix window.</p>
<dt><code>font3</code> (class<code> Font</code>)</p>
<dd> Specifies font number 3 to use in the Tektronix window.</p>
<dt><code>fontLarge</code> (class<code> Font</code>)</p>
<dd> Specifies the large font to use in the Tektronix window.</p>
<dt><code>fontSmall</code> (class<code> Font</code>)</p>
<dd> Specifies the small font to use in the Tektronix window.</p>
<dt><code>ginTerminator</code> (class<code> GinTerminator</code>)</p>
<dd> Specifies what character(s) should follow a GIN report or status report. The possibilities are &#8220;none&#8221;, which sends no terminating characters, &#8220;CRonly&#8221;, which sends CR, and &#8220;CR&amp;EOT&#8221;, which sends both CR and EOT. The default is &#8220;none&#8221;.</p>
<dt><code>height</code> (class<code> Height</code>)</p>
<dd> Specifies the height of the Tektronix window in pixels.</p>
<dt><code>initialFont</code> (class<code> InitialFont</code>)</p>
<dd> Specifies which of the four Tektronix fonts to use initially. Values are the same as for the <code>set-tek-text</code> action. The default is &#8220;large&#8221;.</p>
<dt><code>width</code> (class<code> Width</code>)</p>
<dd> Specifies the width of the Tektronix window in pixels.</dl>
<h3>Menu Resources</h3>
<p> The resources that may be specified for the various menus are described in the documentation for the Athena <code>SimpleMenu</code> widget. The name and classes of the entries in each of the menus are listed below. Resources named &#8220;<code>line</code><i>N</i>&#8221; where <i>N</i> is a number are separators with class <code>SmeLine</code>. </p>
<p> As with all X resource-based widgets, the labels mentioned are customary defaults for the application. </p>
<p> The <code>Main Options</code> menu (widget name <i>mainMenu</i>) has the following entries:</p>
<dl>
<dt><code>toolbar</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-toolbar(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>securekbd</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>secure()</code> action.</p>
<dt><code>allowsends</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-send-events(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>redraw</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>redraw()</code> action.</p>
<dt><code>logging</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>logging(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>print-immediate</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>print-immediate()</code> action.</p>
<dt><code>print-on-error</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>print-on-error()</code> action.</p>
<dt><code>print</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>print()</code> action.</p>
<dt><code>print-redir</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>print-redir()</code> action.</p>
<dt><code>dump-html</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>dump-html()</code> action.</p>
<dt><code>dump-svg</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>dump-svg()</code> action.</p>
<dt><code>8-bit-control</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-8-bit-control(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>backarrow key</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-backarrow(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>num-lock</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-num-lock(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>alt-esc</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>alt-sends-escape(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>meta-esc</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>meta-sends-escape(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>delete-is-del</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>delete-is-del(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>oldFunctionKeys</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-old-function-keys(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>hpFunctionKeys</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-hp-function-keys(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>scoFunctionKeys</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-sco-function-keys(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>sunFunctionKeys</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-sun-function-keys(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>sunKeyboard</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>sunKeyboard(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>suspend</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>tstp</i><code>)</code> action on systems that support job control.</p>
<dt><code>continue</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>cont</i><code>)</code> action on systems that support job control.</p>
<dt><code>interrupt</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>int</i><code>)</code> action.</p>
<dt><code>hangup</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>hup</i><code>)</code> action.</p>
<dt><code>terminate</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>term</i><code>)</code> action.</p>
<dt><code>kill</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>send-signal(</code><i>kill</i><code>)</code> action.</p>
<dt><code>quit</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>quit()</code> action.</dl>
<p> The <code>VT Options</code> menu (widget name <i>vtMenu</i>) has the following entries:</p>
<dl>
<dt><code>scrollbar</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-scrollbar(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>jumpscroll</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-jumpscroll(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>reversevideo</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-reverse-video(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>autowrap</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-autowrap(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>reversewrap</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-reversewrap(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>autolinefeed</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-autolinefeed(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>appcursor</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-appcursor(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>appkeypad</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-appkeypad(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>scrollkey</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-scroll-on-key(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>scrollttyoutput</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-scroll-on-tty-output(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>allow132</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-allow132(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>cursesemul</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-cursesemul(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>keepSelection</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-keep-selection(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>selectToClipboard</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-keep-clipboard(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>visualbell</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-visual-bell(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>bellIsUrgent</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-bellIsUrgent(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>poponbell</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-pop-on-bell(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>cursorblink</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-cursorblink(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>titeInhibit</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-titeInhibit(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>activeicon</code> (class<code> SmeBSB</code>)</p>
<dd> This entry toggles active icons on and off if this feature was compiled into <i>xterm</i>. It is enabled only if <i>xterm</i> was started with the command line option +ai or the <code>activeIcon</code> resource is set to &#8220;true&#8221;.</p>
<dt><code>softreset</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>soft-reset()</code> action.</p>
<dt><code>hardreset</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>hard-reset()</code> action.</p>
<dt><code>clearsavedlines</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>clear-saved-lines()</code> action.</p>
<dt><code>tekshow</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-visibility(</code><i>tek,toggle</i><code>)</code> action.</p>
<dt><code>tekmode</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-terminal-type(</code><i>tek</i><code>)</code> action.</p>
<dt><code>vthide</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-visibility(</code><i>vt,off</i><code>)</code> action.</p>
<dt><code>altscreen</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-altscreen(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>sixelScrolling</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-sixel-scrolling(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>privateColorRegisters</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-private-colors(</code><i>toggle</i><code>)</code> action.</dl>
<p> The <code>VT Fonts</code> menu (widget name <i>fontMenu</i>) has the following entries:</p>
<dl>
<dt><code>fontdefault</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>d</i><code>)</code> action, setting the font using the <code>font</code> (default) resource, e.g., &#8220;Default&#8221; in the menu.</p>
<dt><code>font1</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>1</i><code>)</code> action, setting the font using the <code>font1</code> resource, e.g., &#8220;Unreadable&#8221; in the menu.</p>
<dt><code>font2</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>2</i><code>)</code> action, setting the font using the <code>font2</code> resource, e.g., &#8220;Tiny&#8221; in the menu.</p>
<dt><code>font3</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>3</i><code>)</code> action, setting the font using the <code>font3</code> resource, e.g., &#8220;Small&#8221; in the menu.</p>
<dt><code>font4</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>4</i><code>)</code> action, letting the font using the <code>font4</code> resource, e.g., &#8220;Medium&#8221; in the menu.</p>
<dt><code>font5</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>5</i><code>)</code> action, letting the font using the <code>font5</code> resource, e.g., &#8220;Large&#8221; in the menu.</p>
<dt><code>font6</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>6</i><code>)</code> action, letting the font using the <code>font6</code> resource, e.g., &#8220;Huge&#8221; in the menu.</p>
<dt><code>font7</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>7</i><code>)</code> action, letting the font using the <code>font7</code> resource, e.g., &#8220;Enormous&#8221; in the menu.</p>
<dt><code>fontescape</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>e</i><code>)</code> action.</p>
<dt><code>fontsel</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-vt-font(</code><i>s</i><code>)</code> action.</p>
<dt><code>allow-bold-fonts</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-bold-fonts(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>font-linedrawing</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-font-linedrawing(</code><i>s</i><code>)</code> action.</p>
<dt><code>font-packed</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-font-packed(</code><i>s</i><code>)</code> action.</p>
<dt><code>font-doublesize</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-font-doublesize(</code><i>s</i><code>)</code> action.</p>
<dt><code>render-font</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-render-font(</code><i>s</i><code>)</code> action.</p>
<dt><code>utf8-fonts</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-utf8-fonts(</code><i>s</i><code>)</code> action.</p>
<dt><code>utf8-mode</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-utf8-mode(</code><i>s</i><code>)</code> action.</p>
<dt><code>utf8-title</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-utf8-title(</code><i>s</i><code>)</code> action.</p>
<dt><code>allow-color-ops</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-color-ops(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>allow-font-ops</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-fonts-ops(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>allow-tcap-ops</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-tcap-ops(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>allow-title-ops</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-title-ops(</code><i>toggle</i><code>)</code> action.</p>
<dt><code>allow-window-ops</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>allow-window-ops(</code><i>toggle</i><code>)</code> action.</dl>
<p> The <code>Tek Options</code> menu (widget name <i>tekMenu</i>) has the following entries:</p>
<dl>
<dt><code>tektextlarge</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-tek-text(</code><i>large</i><code>)</code> action.</p>
<dt><code>tektext2</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-tek-text(</code><i>2</i><code>)</code> action.</p>
<dt><code>tektext3</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-tek-text(</code><i>3</i><code>)</code> action.</p>
<dt><code>tektextsmall</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-tek-text(</code><i>small</i><code>)</code> action.</p>
<dt><code>tekpage</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>tek-page()</code> action.</p>
<dt><code>tekreset</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>tek-reset()</code> action.</p>
<dt><code>tekcopy</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>tek-copy()</code> action.</p>
<dt><code>vtshow</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-visibility(</code><i>vt,toggle</i><code>)</code> action.</p>
<dt><code>vtmode</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-terminal-type(</code><i>vt</i><code>)</code> action.</p>
<dt><code>tekhide</code> (class<code> SmeBSB</code>)</p>
<dd> This entry invokes the <code>set-visibility(</code><i>tek,toggle</i><code>)</code> action.</dl>
<h3>Scrollbar Resources</h3>
<p> The following resources are useful when specified for the Athena Scrollbar widget:</p>
<dl>
<dt><code>background</code> (class<code> Background</code>)</p>
<dd> Specifies the color to use for the background of the scrollbar.</p>
<dt><code>foreground</code> (class<code> Foreground</code>)</p>
<dd> Specifies the color to use for the foreground of the scrollbar.</p>
<dt><code>thickness</code> (class<code> Thickness</code>)</p>
<dd> Specifies the width in pixels of the scrollbar (default: 14).</p>
<dt>
<dd> This may be overridden by the <code>width</code> resource.</p>
<dt><code>thumb</code> (class<code> Thumb</code>)</p>
<dd> The default &#8220;thumb&#8221; pixmap used for the scrollbar is a simple checkerboard pattern alternating pixels for foreground and background color.</p>
<dt><code>width</code> (class<code> Width</code>)</p>
<dd> Specifies the width in pixels of the scrollbar (default: 0).</p>
<dt>
<dd> The widget checks the <i>width</i> resource first, using the <i>thickness</i> value if the <i>width</i> is zero.</dl>
<h2>POINTER USAGE</h2>
<p> Once the VT<i>xxx</i> window is created, <i>xterm</i> allows you to select text and copy it within the same or other windows using the <i>pointer</i> or the keyboard. </p>
<p> A &#8220;pointer&#8221; could be a mouse, touchpad or similar device. X applications generally do not care, since they see only <i>button events</i> which have<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 position and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 button up/down state </p>
<p> <i>Xterm</i> can see these events as long as it has <i>focus</i>. </p>
<p> The keyboard also supplies events, but it is less flexible than the pointer for selecting/copying text. </p>
<p> <i>Events</i> are applied to <i>actions</i> using the <code>translations</code> resource. See <code>Actions</code> for a complete list, and <code>Default Key Bindings</code> for the built-in set of <code>translations</code> resources.</p>
<h3>Selection Functions</h3>
<p> By default, the selection functions are invoked when the pointer buttons are used with no modifiers, and when they are used with the &#8220;shift&#8221; key. The &#8220;shift&#8221; key is special, because <i>xterm</i> uses that to ensure that selection functions are still available when it is programmed to send escape sequences in one of the mouse modes (see <i>Xterm Control Sequences</i>, as well as the resource <code>disallowedMouseOps</code>). </p>
<p> At startup, <i>xterm</i> inspects the <code>translations</code> resource to see which pointer buttons may be used in this way, and remembers these buttons when deciding whether to send escape sequences or perform selection when those buttons are used with the &#8220;shift&#8221; modifier. Other pointer buttons, e.g., typically those sent for wheel mouse events, are not affected. </p>
<p> The assignment of the functions described below to keys and buttons may be changed through the resource database; see <code>Actions</code> below.</p>
<dl>
<dt>Pointer button one (usually left)</p>
<dd> is used to save text into the cut buffer:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
~Meta &lt;Btn1Down&gt;:<code>select-start</code>()
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Move the cursor to beginning of the text, and then hold the button down while moving the cursor to the end of the region and releasing the button. The selected text is highlighted and is saved in the global <i>cut buffer</i> and made the selection when the button is released:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
&lt;BtnUp&gt;:<code>select-end</code>(<code>SELECT</code>, <code>CUT_BUFFER0</code>) 

</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> Normally (but see the discussion of <code>on2Clicks</code>, etc):</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 Double-clicking selects by words.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Triple-clicking selects by lines.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Quadruple-clicking goes back to characters, etc.</dl>
<dt>
<dd> Multiple-click is determined by the time from button up to button down, so you can change the selection unit in the middle of a selection. Logical words and lines selected by double- or triple-clicking may wrap across more than one screen line if lines were wrapped by <i>xterm</i> itself rather than by the application running in the window. If the key/button bindings specify that an X selection is to be made, <i>xterm</i> will leave the selected text highlighted for as long as it is the selection owner.</p>
<dt>Pointer button two (usually middle)</p>
<dd> &#8220;types&#8221; (<i>pastes</i>) the text from the given selection, if any, otherwise from the cut buffer, inserting it as keyboard input:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
~Ctrl ~Meta &lt;Btn2Up&gt;:<code>insert-selection</code>(<code>SELECT</code>, <code>CUT_BUFFER0</code>)
</pre>
<p>&nbsp;.in -4</p>
<dt>Pointer button three (usually right)</p>
<dd> <i>extends</i> the current selection.<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
~Ctrl ~Meta &lt;Btn3Down&gt;:<code>start-extend</code>()
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> (Without loss of generality, you can swap &#8220;right&#8221; and &#8220;left&#8221; everywhere in the rest of this paragraph.) If pressed while closer to the right edge of the selection than the left, it extends/contracts the right edge of the selection. If you contract the selection past the left edge of the selection, <i>xterm</i> assumes you really meant the left edge, restores the original selection, then extends/contracts the left edge of the selection. Extension starts in the selection unit mode that the last selection or extension was performed in; you can multiple-click to cycle through them.</dl>
<p> By cutting and pasting pieces of text without trailing new lines, you can take text from several places in different windows and form a command to the shell, for example, or take output from a program and insert it into your favorite editor. Since cut buffers are globally shared among different applications, you may regard each as a &#8220;file&#8221; whose contents you know. The terminal emulator and other text programs should be treating it as if it were a text file, i.e., the text is delimited by new lines.</p>
<h3>Scrolling</h3>
<p> The scroll region displays the position and amount of text currently showing in the window (highlighted) relative to the amount of text actually saved. As more text is saved (up to the maximum), the size of the highlighted area decreases. </p>
<p> Clicking button one with the pointer in the scroll region moves the adjacent line to the top of the display window. </p>
<p> Clicking button three moves the top line of the display window down to the pointer position. </p>
<p> Clicking button two moves the display to a position in the saved text that corresponds to the pointer&#8217;s position in the scrollbar.</p>
<h3>Tektronix Pointer</h3>
<p> Unlike the VT<i>xxx</i> window, the Tektronix window does not allow the copying of text. It does allow Tektronix GIN mode, and in this mode the cursor will change from an arrow to a cross. Pressing any key will send that key and the current coordinate of the cross cursor. Pressing button one, two, or three will return the letters &#8220;l&#8221;, &#8220;m&#8221;, and &#8220;r&#8221;, respectively. If the &#8220;shift&#8221; key is pressed when a pointer button is pressed, the corresponding upper case letter is sent. To distinguish a pointer button from a key, the high bit of the character is set (but this is bit is normally stripped unless the terminal mode is RAW; see <i><a href="/docs/linux/man/4-tty/">tty</a></i>(4) for details).</p>
<h2>SELECT/PASTE</h2>
<p> X clients provide select and paste support by responding to requests conveyed by the X server. The X server holds data in &#8220;atoms&#8221; which correspond to the different types of selection (<code>PRIMARY</code>, <code>SECONDARY</code>, <code>CLIPBOARD</code>) as well as the similar cut buffer mechanism (<code>CUT_BUFFER0</code> to <code>CUT_BUFFER7</code>). Those are documented in the ICCCM. </p>
<p> The ICCCM deals with the underlying mechanism for select/paste. It does not mention <i>highlighting</i>. The <i>selection</i> is not the same as <i>highlighting</i>. <i>Xterm</i> (like many applications) uses highlighting to show you the currently selected text. An X application may <i>own</i> a selection, which allows it to be the source of data copied using a given selection atom <i>Xterm</i> may continue owning a selection after it stops highlighting (see <code>keepSelection</code>).</p>
<h3>PRIMARY</h3>
<p> When configured to use the primary selection (the default), <i>xterm</i> can provide the selection data in ways which help to retain character encoding information as it is pasted. </p>
<p> The <code>PRIMARY</code> token is a standard X feature, documented in the ICCCM (<i>Inter-Client Communication Conventions Manual</i>), which states</p>
<dl>
<dt>
<dd>
<p> The selection named by the atom <code>PRIMARY</code> is used for all commands that take only a single argument and is the principal means of communication between clients that use the selection mechanism.</dl>
<p> A user &#8220;selects&#8221; text on <i>xterm</i>, which highlights the selected text. A subsequent &#8220;paste&#8221; to another client forwards a request to the client owning the selection. If <i>xterm</i> owns the primary selection, it makes the data available in the form of one or more &#8220;selection targets&#8221;. If it does not own the primary selection, e.g., if it has released it or another client has asserted ownership, it relies on cut-buffers to pass the data. But cut-buffers handle only ISO-8859-1 data (officially &#8211; some clients ignore the rules).</p>
<h3>CLIPBOARD</h3>
<p> When configured to use the clipboard (using the <code>selectToClipboard</code> resource), the problem with persistence of ownership is bypassed. Otherwise, there is no difference regarding the data which can be passed via selection. </p>
<p> The <code>selectToClipboard</code> resource is a compromise, allowing <code>CLIPBOARD</code> to be treated almost like <code>PRIMARY</code>, unlike the ICCCM, which describes <code>CLIPBOARD</code> in different terms than <code>PRIMARY</code> or <code>SECONDARY</code>. Its lengthy explanation begins with the essential points:</p>
<dl>
<dt>
<dd>
<p> The selection named by the atom CLIPBOARD is used to hold data that is being transferred between clients, that is, data that usually is being cut and then pasted or copied and then pasted. Whenever a client wants to transfer data to the clipboard:<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 It should assert ownership of the CLIPBOARD.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If it succeeds in acquiring ownership, it should be prepared to respond to a request for the contents of the CLIPBOARD in the usual way (retaining the data to be able to return it). The request may be generated by the clipboard client described below.</dl>
<h3>SELECT</h3>
<p> However, many applications use <code>CLIPBOARD</code> in imitation of other windowing systems. The <code>selectToClipboard</code> resource (and corresponding menu entry <code>Select to Clipboard</code>) introduce the <code>SELECT</code> token (known only to <i>xterm</i>) which chooses between the <code>PRIMARY</code> and <code>CLIPBOARD</code> tokens. </p>
<p> Without using this feature, one can use workarounds such as the <i>xclip</i> program to show the contents of the X clipboard within an <i>xterm</i> window.</p>
<h3>SECONDARY</h3>
<p> This is used less often than <code>PRIMARY</code> or <code>CLIPBOARD</code>. According to the ICCCM, it is used<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 As the second argument to commands taking two arguments (for example, &#8220;exchange primary and secondary selections&#8221;)<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 As a means of obtaining data when there is a primary selection and the user does not want to disturb it</p>
<h3>Selection Targets</h3>
<p> The different types of data which are passed depend on what the receiving client asks for. These are termed <i>selection targets</i>. </p>
<p> When asking for the selection data, <i>xterm</i> tries the following types in this order:</p>
<dl>
<dt>
<dd>
<dl>
<dt>UTF8_STRING</p>
<dd> This is an XFree86 extension, which denotes that the data is encoded in UTF-8. When <i>xterm</i> is built with wide-character support, it both accepts and provides this type.</p>
<dt>TEXT</p>
<dd> the text is in the encoding which corresponds to your current locale.</p>
<dt>
<dd> COMPOUND_TEXT this is a format for multiple character set data, such as multi-lingual text. It can store UTF-8 data as a special case.</p>
<dt>STRING</p>
<dd> This is Latin 1 (ISO-8859-1) data.</dl>
</dl>
<p> The middle two (TEXT and COMPOUND_TEXT) are added if <i>xterm</i> is configured with the <code>i18nSelections</code> resource set to &#8220;true&#8221;. </p>
<p> UTF8_STRING is preferred (therefore first in the list) since <i>xterm</i> stores text as Unicode data when running in wide-character mode, and no translation is needed. On the other hand, TEXT and COMPOUND_TEXT may require translation. If the translation is incomplete, they will insert X&#8217;s &#8220;defaultString&#8221; whose value cannot be set, and may simply be empty. <i>Xterm</i>&#8216;s <code>defaultString</code> resource specifies the string to use for incomplete translations of the UTF8_STRING. </p>
<p> You can alter the types which <i>xterm</i> tries using the <code>eightBitSelectTypes</code> or <code>utf8SelectTypes</code> resources. For instance, you might have some specific locale setting which does not use UTF-8 encoding. The resource value is a comma-separated list of the selection targets, which consist of the names shown. You can use the special name I18N to denote the optional inclusion of TEXT and COMPOUND_TEXT. The names are matched ignoring case, and can be abbreviated. The default list can be expressed in several ways, e.g., </p>
<dl>
<dt>
<dd>
<pre>
UTF8_STRING,I18N,STRING
utf8,i18n,string
u,i,s
</pre>
</dl>
<h3>Mouse Protocol</h3>
<p> Applications can send escape sequences to <i>xterm</i> to cause it to send escape sequences back to the computer when you press a pointer button, or even (depending on which escape sequence) send escape sequences back to the computer as you move the pointer. </p>
<p> These escape sequences and the responses, called the <i>mouse protocol</i>, are documented in <i>XTerm Control Sequences</i>. They do not appear in the <i>actions</i> invoked by the <code>translations</code> resource because the resource does not change while you run <i>xterm</i>, whereas applications can change the mouse prototol (i.e., enable, disable, use different modes). </p>
<p> However, the mouse protocol is interpreted within the <i>actions</i> that are usually associated with the pointer buttons. <i>Xterm</i> ignores the mouse protocol in the <code>insert-selection</code> action if the shift-key is pressed at the same time. It also modifies a few other actions if the shift-key is pressed, e.g., suppressing the response with the pointer position, though not eliminating changes to the selected text.</p>
<h2>MENUS</h2>
<p> <i>Xterm</i> has four menus, named <i>mainMenu</i>, <i>vtMenu</i>, <i>fontMenu</i>, and <i>tekMenu</i>. Each menu pops up under the correct combinations of key and button presses. Each menu is divided into sections, separated by a horizontal line. Some menu entries correspond to modes that can be altered. A check mark appears next to a mode that is currently active. Selecting one of these modes toggles its state. Other menu entries are commands; selecting one of these performs the indicated function. </p>
<p> All of the menu entries correspond to X actions. In the list below, the menu label is shown followed by the action&#8217;s name in parenthesis.</p>
<h3>Main Options</h3>
<p> The <i>xterm</i> <i>mainMenu</i> pops up when the &#8220;control&#8221; key and pointer button one are pressed in a window. This menu contains items that apply to both the VT<i>xxx</i> and Tektronix windows. There are several sections:</p>
<dl>
<dt>Commands for managing X events:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Toolbar</code> (resource <code>toolbar</code>)</p>
<dd> Clicking on the &#8220;Toolbar&#8221; menu entry hides the toolbar if it is visible, and shows it if it is not.</p>
<dt><code>Secure Keyboard</code> (resource <code>securekbd</code>)</p>
<dd> The <code>Secure Keyboard</code> mode is helpful when typing in passwords or other sensitive data in an unsecure environment (see <code>SECURITY</code> below, but read the limitations carefully).</p>
<dt><code>Allow SendEvents</code> (resource <code>allowsends</code>)</p>
<dd> Specifies whether or not synthetic key and button events generated using the X protocol SendEvent request should be interpreted or discarded. This corresponds to the <code>allowSendEvents</code> resource.</p>
<dt><code>Redraw Window</code> (resource <code>redraw</code>)</p>
<dd> Forces the X display to repaint; useful in some environments.</dl>
</dl>
<dt>Commands for capturing output:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Log to File</code> (resource <code>logging</code>)</p>
<dd> Captures text sent to the screen in a log file, as in the <code>-l</code> logging option.</p>
<dt><code>Print-All Immediately</code> (resource <code>print-immediate</code>)</p>
<dd> Invokes the <code>print-immediate</code> action, sending the text of the current window directly to a file, as specified by the <code>printFileImmediate</code>, <code>printModeImmediate</code> and <code>printOptsImmediate</code> resources.</p>
<dt><code>Print-All on Error</code> (resource <code>print-on-error</code>)</p>
<dd> Invokes the <code>print-on-error</code> action, which toggles a flag telling <i>xterm</i> that if it exits with an X error, to send the text of the current window directly to a file, as specified by the <code>printFileOnXError</code>, <code>printModeOnXError</code> and <code>printOptsOnXError</code> resources.</p>
<dt><code>Print Window</code> (resource <code>print</code>)</p>
<dd> Sends the text of the current window to the program given in the <code>printerCommand</code> resource.</p>
<dt><code>Redirect to Printer</code> (resource <code>print-redir</code>)</p>
<dd> This sets the <code>printerControlMode</code> to 0 or 2. You can use this to turn the printer on as if an application had sent the appropriate control sequence. It is also useful for switching the printer off if an application turns it on without resetting the print control mode.</p>
<dt><code>XHTML Screen Dump</code> (resource <code>dump-html</code>)</p>
<dd> Available only when compiled with screen dump support. Invokes the <code>dump-html</code> action. This creates an XHTML file matching the contents of the current screen, including the border, internal border, colors and most attributes: bold, italic, underline, faint, strikeout, reverse; blink is rendered as white-on-red; double underline is rendered the same as underline since there is no portable equivalent in CSS 2.2.</p>
<dt>
<dd> The font is whatever your browser uses for preformatted (&lt;pre&gt;) elements. The XHTML file references a cascading style sheet (CSS) named &#8220;<code>xterm.css</code>&#8221; that you can create to select a font or override properties.</p>
<dl>
<dt>
<dd>
<p> The following CSS selectors are used with the expected default behavior in the XHTML file: </p>
<p> <i>.ul</i> for underline,<br />
 <i>.bd</i> for bold,<br />
 <i>.it</i> for italic,<br />
 <i>.st</i> for strikeout,<br />
 <i>.lu</i> for strikeout combined with underline. </p>
<p> In addition you may use </p>
<p> <i>.ev</i> to affect even numbered lines and<br />
 <i>.od</i> to affect odd numbered lines.</dl>
<dt>
<dd> Attributes faint, reverse and blink are implemented as <i>style</i> attributes setting color properties. All colors are specified as RGB percentages in order to support displays with 10 bits per RGB.</p>
<dt>
<dd> The name of the file will be<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
<code>xterm.</code><i>yyyy</i><code>.</code><i>MM</i><code>.</code><i>dd</i><code>.</code><i>hh</i><code>.</code><i>mm</i><code>.</code><i>ss</i>.xhtml
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> where <i>yyyy</i>, <i>MM</i>, <i>dd</i>, <i>hh</i>, <i>mm</i> and <i>ss</i> are the year, month, day, hour, minute and second when the screen dump was performed (the file is created in the directory <i>xterm</i> is started in, or the home directory for a login <i>xterm</i>).</p>
<dt>
<dd> The <code>dump-html</code> action can also be triggered using the Media Copy control sequence CSI 1 0 i, for example from a shell script with<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
printf '[10i'
</pre>
<p>&nbsp;.in -4 </p>
<p> Only the UTF-8 encoding is supported.</p>
<dt><code>SVG Screen Dump</code> (resource <code>dump-svg</code>)</p>
<dd> Available only when compiled with screen dump support. Invokes the <code>dump-svg</code> action. This creates a Scalable Vector Graphics (SVG) file matching the contents of the current screen, including the border, internal border, colors and most attributes: bold, italic, underline, double underline, faint, strikeout, reverse; blink is rendered as white-on-red. The font is whatever your renderer uses for the <i>monospace</i> font-family. All colors are specified as RGB percentages in order to support displays with 10 bits per RGB.</p>
<dt>
<dd> The name of the file will be<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
<code>xterm.</code><i>yyyy</i><code>.</code><i>MM</i><code>.</code><i>dd</i><code>.</code><i>hh</i><code>.</code><i>mm</i><code>.</code><i>ss</i>.svg
</pre>
<p>&nbsp;.in -4</p>
<dt>
<dd> where <i>yyyy</i>, <i>MM</i>, <i>dd</i>, <i>hh</i>, <i>mm</i> and <i>ss</i> are the year, month, day, hour, minute and second when the screen dump was performed (the file is created in the directory <i>xterm</i> is started in, or the home directory for a login <i>xterm</i>).</p>
<dt>
<dd> The <code>dump-svg</code> action can also be triggered using the Media Copy control sequence CSI 1 1 i, for example from a shell script with<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
printf '[11i'
</pre>
<p>&nbsp;.in -4 </p>
<p> Only the UTF-8 encoding is supported.</dl>
</dl>
<dt>Modes for setting keyboard style:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>8-Bit Controls</code> (resource <code>8-bit-control</code>)</p>
<dd> Enabled for VT220 emulation, this controls whether <i>xterm</i> will send 8-bit control sequences rather than using 7-bit (ASCII) controls, e.g., sending a byte in the range 128-159 rather than the escape character followed by a second byte. <i>Xterm</i> always interprets both 8-bit and 7-bit control sequences (see <i>Xterm Control Sequences</i>). This corresponds to the <code>eightBitControl</code> resource.</p>
<dt><code>Backarrow Key (BS/DEL)</code> (resource <code>backarrow key</code>)</p>
<dd> Modifies the behavior of the backarrow key, making it transmit either a backspace (8) or delete (127) character. This corresponds to the <code>backarrowKey</code> resource.</p>
<dt><code>Alt/NumLock Modifiers</code> (resource <code>num-lock</code>)</p>
<dd> Controls the treatment of Alt- and NumLock-key modifiers. This corresponds to the <code>numLock</code> resource.</p>
<dt><code>Meta Sends Escape</code> (resource <code>meta-esc</code>)</p>
<dd> Controls whether <i>Meta</i> keys are converted into a two-character sequence with the character itself preceded by ESC. This corresponds to the <code>metaSendsEscape</code> resource.</p>
<dt><code>Delete is DEL</code> (resource <code>delete-is-del</code>)</p>
<dd> Controls whether the Delete key on the editing keypad should send DEL (127) or the VT220-style Remove escape sequence. This corresponds to the <code>deleteIsDEL</code> resource.</p>
<dt><code>Old Function-Keys</code> (resource <code>oldFunctionKeys</code>)</p>
<dd>
<dt><code>HP Function-Keys</code> (resource <code>hpFunctionKeys</code>)</p>
<dd>
<dt><code>SCO Function-Keys</code> (resource <code>scoFunctionKeys</code>)</p>
<dd>
<dt><code>Sun Function-Keys</code> (resource <code>sunFunctionKeys</code>)</p>
<dd>
<dt><code>VT220 Keyboard</code> (resource <code>sunKeyboard</code>)</p>
<dd> These act as a radio-button, selecting one style for the keyboard layout. The layout corresponds to more than one resource setting: <code>sunKeyboard</code>, <code>sunFunctionKeys</code>, <code>scoFunctionKeys</code> and <code>hpFunctionKeys</code>.</dl>
</dl>
<dt>Commands for process signalling:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Send STOP Signal</code> (resource <code>suspend</code>)</p>
<dd>
<dt><code>Send CONT Signal</code> (resource <code>continue</code>)</p>
<dd>
<dt><code>Send INT Signal</code> (resource <code>interrupt</code>)</p>
<dd>
<dt><code>Send HUP Signal</code> (resource <code>hangup</code>)</p>
<dd>
<dt><code>Send TERM Signal</code> (resource <code>terminate</code>)</p>
<dd>
<dt><code>Send KILL Signal</code> (resource <code>kill</code>)</p>
<dd> These send the SIGTSTP, SIGCONT, SIGINT, SIGHUP, SIGTERM and SIGKILL signals respectively, to the process group of the process running under <i>xterm</i> (usually the shell). The <code>SIGCONT</code> function is especially useful if the user has accidentally typed CTRL-Z, suspending the process.</p>
<dt><code>Quit</code> (resource <code>quit</code>)</p>
<dd> Stop processing X events except to support the <code>-hold</code> option, and then send a SIGHUP signal to the process group of the process running under <i>xterm</i> (usually the shell).</dl>
</dl>
</dl>
<h3>VT Options</h3>
<p> The <i>xterm</i> <i>vtMenu</i> sets various modes in the VT<i>xxx</i> emulation, and is popped up when the &#8220;control&#8221; key and pointer button two are pressed in the VT<i>xxx</i> window.</p>
<dl>
<dt>VT<i>xxx</i> Modes:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Enable Scrollbar</code> (resource <code>scrollbar</code>)</p>
<dd> Enable (or disable) the scrollbar. This corresponds to the <code>-sb</code> option and the <code>scrollBar</code> resource.</p>
<dt><code>Enable Jump Scroll</code> (resource <code>jumpscroll</code>)</p>
<dd> Enable (or disable) jump scrolling. This corresponds to the <code>-j</code> option and the <code>jumpScroll</code> resource.</p>
<dt><code>Enable Reverse Video</code> (resource <code>reversevideo</code>)</p>
<dd> Enable (or disable) reverse-video. This corresponds to the <code>-rv</code> option and the <code>reverseVideo</code> resource.</p>
<dt><code>Enable Auto Wraparound</code> (resource <code>autowrap</code>)</p>
<dd> Enable (or disable) auto-wraparound. This corresponds to the <code>-aw</code> option and the <code>autoWrap</code> resource.</p>
<dt><code>Enable Reverse Wraparound</code> (resource <code>reversewrap</code>)</p>
<dd> Enable (or disable) reverse wraparound. This corresponds to the <code>-rw</code> option and the <code>reverseWrap</code> resource.</p>
<dt><code>Enable Auto Linefeed</code> (resource <code>autolinefeed</code>)</p>
<dd> Enable (or disable) auto-linefeed. This is the VT102 NEL function, which causes the emulator to emit a line feed after each carriage return. There is no corresponding command-line option or resource setting.</p>
<dt><code>Enable Application Cursor Keys</code> (resource <code>appcursor</code>)</p>
<dd> Enable (or disable) application cursor keys. This corresponds to the <code>appcursorDefault</code> resource. There is no corresponding command-line option.</p>
<dt><code>Enable Application Keypad</code> (resource <code>appkeypad</code>)</p>
<dd> Enable (or disable) application keypad keys. This corresponds to the <code>appkeypadDefault</code> resource. There is no corresponding command-line option.</p>
<dt><code>Scroll to Bottom on Key Press</code> (resource <code>scrollkey</code>)</p>
<dd> Enable (or disable) scrolling to the bottom of the scrolling region on a keypress. This corresponds to the <code>-sk</code> option and the <code>scrollKey</code> resource.</p>
<dt>
<dd> As a special case, the XON / XOFF keys (control/S and control/Q) are ignored.</p>
<dt><code>Scroll to Bottom on Tty Output</code> (resource <code>scrollttyoutput</code>)</p>
<dd> Enable (or disable) scrolling to the bottom of the scrolling region on output to the terminal. This corresponds to the <code>-si</code> option and the <code>scrollTtyOutput</code> resource.</p>
<dt><code>Allow 80/132 Column Switching</code> (resource <code>allow132</code>)</p>
<dd> Enable (or disable) switching between 80 and 132 columns. This corresponds to the <code>-132</code> option and the <code>c132</code> resource.</p>
<dt><code>Keep Selection</code> (resource <code>keepSelection</code>)</p>
<dd> Tell <i>xterm</i> whether to disown the selection when it stops highlighting it, e.g., when an application modifies the display so that it no longer matches the text which has been highlighted. As long as <i>xterm</i> continues to own the selection for a given atom, it can provide the corresponding text to other clients which request the selection using that atom.</p>
<dt>
<dd> This corresponds to the <code>keepSelection</code> resource. There is no corresponding command-line option.</p>
<dt>
<dd> Telling <i>xterm</i> to not disown the selection does not prevent other applications from taking ownership of the selection. When that happens, <i>xterm</i> receives notification that this has happened, and removes its highlighting.</p>
<dt>
<dd> See <code>SELECT/PASTE</code> for more information.</p>
<dt><code>Select to Clipboard</code> (resource <code>selectToClipboard</code>)</p>
<dd> Tell <i>xterm</i> whether to use the <code>PRIMARY</code> or <code>CLIPBOARD</code> for <code>SELECT</code> tokens in the <code>translations</code> resource which maps keyboard and mouse actions to select/paste actions.</p>
<dt>
<dd> This corresponds to the <code>selectToClipboard</code> resource. There is no corresponding command-line option.</p>
<dt>
<dd> The <code>keepSelection</code> resource setting applies to <code>CLIPBOARD</code> selections just as it does for <code>PRIMARY</code> selections. However some window managers treat the clipboard specially. For instance, XQuartz&#8217;s synchronization between the OSX <i>pasteboard</i> and the X11 <i>clipboard</i> causes applications to lose the selection ownership for that atom when a selection is copied to the clipboard.</p>
<dt>
<dd> See <code>SELECT/PASTE</code> for more information.</p>
<dt><code>Enable Visual Bell</code> (resource <code>visualbell</code>)</p>
<dd> Enable (or disable) visible bell (i.e., flashing) instead of an audible bell. This corresponds to the <code>-vb</code> option and the <code>visualBell</code> resource.</p>
<dt><code>Enable Bell Urgency</code> (resource <code>bellIsUrgent</code>)</p>
<dd> Enable (or disable) Urgency window manager hint when Control-G is received. This corresponds to the <code>bellIsUrgent</code> resource.</p>
<dt><code>Enable Pop on Bell</code> (resource <code>poponbell</code>)</p>
<dd> Enable (or disable) raising of the window when Control-G is received. This corresponds to the <code>-pop</code> option and the <code>popOnBell</code> resource.</p>
<dt><code>Enable Blinking Cursor</code> (resource <code>cursorblink</code>)</p>
<dd> Enable (or disable) the blinking-cursor feature. This corresponds to the <code>-bc</code> option and the <code>cursorBlink</code> resource. There are also escape sequences (see <i>Xterm Control Sequences</i>):</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <code>cursorBlinkXOR</code> resource is set, the menu entry and the escape sequence states will be XOR&#8217;d: if both are enabled, the cursor will not blink, if only one is enabled, the cursor will blink.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 If the <code>cursorBlinkXOR</code> is not set; if either the menu entry or the escape sequence states are set, the cursor will blink.</dl>
<dt>
<dd> In either case, the checkbox for the menu shows the state of the <code>cursorBlink</code> resource, which may not correspond to what the cursor is actually doing.</p>
<dt><code>Enable Alternate Screen Switching</code> (resource <code>titeInhibit</code>)</p>
<dd> Enable (or disable) switching between the normal and alternate screens. This corresponds to the <code>titeInhibit</code> resource. There is no corresponding command-line option.</p>
<dt><code>Enable Active Icon</code> (resource <code>activeicon</code>)</p>
<dd> Enable (or disable) the active-icon feature. This corresponds to the <code>-ai</code> option and the <code>activeIcon</code> resource.</p>
<dt><code>Sixel Scrolling</code> (resource <code>sixelScrolling</code>)</p>
<dd> When enabled, sixel graphics are positioned at the current text cursor location, scroll the image vertically if larger than the screen, and leave the text cursor at the start of the next complete line after the image when returning to text mode (this is the default). When disabled, sixel graphics are positioned at the upper left of the screen, are cropped to fit the screen, and do not affect the text cursor location. This corresponds to the <code>sixelScrolling</code> resource. There is no corresponding command-line option.</p>
<dt><code>Private Color Registers</code> (resource <code>privateColorRegisters</code>)</p>
<dd> If <i>xterm</i> is configured to support ReGIS graphics, this controls whether a private color palette can be used.</p>
<dt>
<dd> When enabled, each graphic image uses a separate set of color registers, so that it essentially has a private palette (this is the default). If it is not set, all graphics images share a common set of registers which is how sixel and ReGIS graphics worked on actual hardware. The default is likely a more useful mode on modern TrueColor hardware.</p>
<dt>
<dd> This corresponds to the <code>privateColorRegisters</code> resource. There is no corresponding command-line option.</dl>
</dl>
<dt>VT<i>xxx</i> Commands:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Do Soft Reset</code> (resource <code>softreset</code>)</p>
<dd> Reset scroll regions. This can be convenient when some program has left the scroll regions set incorrectly (often a problem when using VMS or TOPS-20). This corresponds to the VT220 DECSTR control sequence.</p>
<dt><code>Do Full Reset</code> (resource <code>hardreset</code>)</p>
<dd> The full reset entry will clear the screen, reset tabs to every eight columns, and reset the terminal modes (such as wrap and smooth scroll) to their initial states just after <i>xterm</i> has finished processing the command line options. This corresponds to the VT102 RIS control sequence, with a few obvious differences. For example, your session is not disconnected as a real VT102 would do.</p>
<dt><code>Reset and Clear Saved Lines</code> (resource <code>clearsavedlines</code>)</p>
<dd> Perform a full reset, and also clear the saved lines.</dl>
</dl>
<dt>Commands for setting the current screen:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>Show Tek Window</code> (resource <code>tekshow</code>)</p>
<dd> When enabled, pops the Tektronix 4014 window up (makes it visible). When disabled, hides the Tektronix 4014 window.</p>
<dt><code>Switch to Tek Mode</code> (resource <code>tekmode</code>)</p>
<dd> When enabled, pops the Tektronix 4014 window up if it is not already visible, and switches the input stream to that window. When disabled, hides the Tektronix 4014 window and switches input back to the VT<i>xxx</i> window.</p>
<dt><code>Hide VT Window</code> (resource <code>vthide</code>)</p>
<dd> When enabled, hides the VT<i>xxx</i> window, shows the Tektronix 4014 window if it was not already visible and switches the input stream to that window. When disabled, shows the VT<i>xxx</i> window, and switches the input stream to that window.</p>
<dt><code>Show Alternate Screen</code> (resource <code>altscreen</code>)</p>
<dd> When enabled, shows the alternate screen. When disabled, shows the normal screen. Note that the normal screen may have saved lines; the alternate screen does not.</dl>
</dl>
</dl>
<h3>VT Fonts</h3>
<p> The <i>xterm</i> <i>fontMenu</i> pops up when the &#8220;control&#8221; key and pointer button three are pressed in a window. It sets the font used in the VT<i>xxx</i> window, or modifies the way the font is specified or displayed. There are several sections. </p>
<p> The first section allows you to select the font from a set of alternatives:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Default</code> (resource <code>fontdefault</code>)</p>
<dd> Set the font to the default, i.e., that given by the <code>*VT100.font</code> resource.</p>
<dt><code>Unreadable</code> (resource <code>font1</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font1</code> resource.</p>
<dt><code>Tiny</code> (resource <code>font2</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font2</code> resource.</p>
<dt><code>Small</code> (resource <code>font3</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font3</code> resource.</p>
<dt><code>Medium</code> (resource <code>font4</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font4</code> resource.</p>
<dt><code>Large</code> (resource <code>font5</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font5</code> resource.</p>
<dt><code>Huge</code> (resource <code>font6</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font6</code> resource.</p>
<dt><code>Enormous</code> (resource <code>font7</code>)</p>
<dd> Set the font to that given by the <code>*VT100.font7</code> resource.</p>
<dt><code>Escape Sequence</code> (resource <code>fontescape</code>)</p>
<dd> This allows you to set the font last specified by the Set Font escape sequence (see <i>Xterm Control Sequences</i>).</p>
<dt><code>Selection</code> (resource <code>fontsel</code>)</p>
<dd> This allows you to set the font specified the current selection as a font name (if the <code>PRIMARY</code> selection is owned).</dl>
</dl>
<p> The second section allows you to modify the way it is displayed:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Bold Fonts</code> (resource <code>allow-bold-fonts</code>)</p>
<dd> This is normally checked (enabled). When unchecked, <i>xterm</i> will not use bold fonts. The setting corresponds to the <code>allowBoldFonts</code> resource.</p>
<dt><code>Line-Drawing Characters</code> (resource <code>font-linedrawing</code>)</p>
<dd> When set, tells <i>xterm</i> to draw its own line-drawing characters. Otherwise it relies on the font containing these. Compare to the <code>forceBoxChars</code> resource.</p>
<dt><code>Packed Font</code> (resource <code>font-packed</code>)</p>
<dd> When set, tells <i>xterm</i> to use the minimum glyph-width from a font when displaying characters. Use the maximum width (unchecked) to help display proportional fonts. Compare to the <code>forcePackedFont</code> resource.</p>
<dt><code>Doublesized Characters</code> (resource <code>font-doublesize</code>)</p>
<dd> When set, <i>xterm</i> may ask the font server to produce scaled versions of the normal font, for VT102 double-size characters.</dl>
</dl>
<p> The third section allows you to modify the way it is specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>TrueType Fonts</code> (resource <code>render-font</code>)</p>
<dd> If the <code>renderFont</code> and corresponding resources were set, this is a further control whether <i>xterm</i> will actually use the Xft library calls to obtain a font.</p>
<dt><code>UTF-8 Encoding</code> (resource <code>utf8-mode</code>)</p>
<dd> This controls whether <i>xterm</i> uses UTF-8 encoding of input/output. It is useful for temporarily switching <i>xterm</i> to display text from an application which does not follow the locale settings. It corresponds to the <code>utf8</code> resource.</p>
<dt><code>UTF-8 Fonts</code> (resource <code>utf8-fonts</code>)</p>
<dd> This controls whether <i>xterm</i> uses UTF-8 fonts for display. It is useful for temporarily switching <i>xterm</i> to display text from an application which does not follow the locale settings. It combines the <code>utf8</code> and <code>utf8Fonts</code> resources, subject to the <code>locale</code> resource.</p>
<dt><code>UTF-8 Titles</code> (resource <code>utf8-title</code>)</p>
<dd> This controls whether <i>xterm</i> accepts UTF-8 encoding for title control sequences. It corresponds to the <code>utf8Fonts</code> resource.</p>
<dt>
<dd> Initially the checkmark is set according to both the <code>utf8</code> and <code>utf8Fonts</code> resource values. If the latter is set to &#8220;always&#8221;, the checkmark is disabled. Likewise, if there are no fonts given in the <code>utf8Fonts</code> subresources, then the checkmark also is disabled.</p>
<dt>
<dd> The standard <code>XTerm</code> app-defaults file defines both sets of fonts, while the <code>UXTerm</code> app-defaults file defines only one set. Assuming the standard app-defaults files, this command will launch <i>xterm</i> able to switch between UTF-8 and ISO-8859-1 encoded fonts:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
uxterm -class XTerm
</pre>
<p>&nbsp;.in -4</dl>
</dl>
<p> The fourth section allows you to enable or disable special operations which can be controlled by writing escape sequences to the terminal. These are disabled if the SendEvents feature is enabled:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Allow Color Ops</code> (resource <code>allow-font-ops</code>)</p>
<dd> This corresponds to the <code>allowColorOps</code> resource. Enable or disable control sequences that set/query the colors.</p>
<dt><code>Allow Font Ops</code> (resource <code>allow-font-ops</code>)</p>
<dd> This corresponds to the <code>allowFontOps</code> resource. Enable or disable control sequences that set/query the font.</p>
<dt><code>Allow Mouse Ops</code> (resource <code>allow-mouse-ops</code>)</p>
<dd> Enable or disable control sequences that cause the terminal to send escape sequences on pointer-clicks and movement. This corresponds to the <code>allowMouseOps</code> resource.</p>
<dt><code>Allow Tcap Ops</code> (resource <code>allow-tcap-ops</code>)</p>
<dd> Enable or disable control sequences that query the terminal&#8217;s notion of its function-key strings, as termcap or terminfo capabilities. This corresponds to the <code>allowTcapOps</code> resource.</p>
<dt><code>Allow Title Ops</code> (resource <code>allow-title-ops</code>)</p>
<dd> Enable or disable control sequences that modify the window title or icon name. This corresponds to the <code>allowTitleOps</code> resource.</p>
<dt><code>Allow Window Ops</code> (resource <code>allow-window-ops</code>)</p>
<dd> Enable or disable extended window control sequences (as used in dtterm). This corresponds to the <code>allowWindowOps</code> resource.</dl>
</dl>
<h3>Tek Options</h3>
<p> The <i>xterm</i> <i>tekMenu</i> sets various modes in the Tektronix emulation, and is popped up when the &#8220;control&#8221; key and pointer button two are pressed in the Tektronix window. The current font size is checked in the modes section of the menu.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Large Characters</code> (resource <code>tektextlarge</code>)</p>
<dd>
<dt><code>#2 Size Characters</code> (resource <code>tektext2</code>)</p>
<dd>
<dt><code>#3 Size Characters</code> (resource <code>tektext3</code>)</p>
<dd>
<dt><code>Small Characters</code> (resource <code>tektextsmall</code>)</p>
<dd></dl>
</dl>
<p> Commands:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>PAGE</code> (resource <code>tekpage</code>)</p>
<dd> Simulates the Tektronix &#8220;PAGE&#8221; button by</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 clearing the window,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 cancelling the graphics input-mode, and<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 moving the cursor to the <i>home</i> position.</dl>
<dt><code>RESET</code> (resource <code>tekreset</code>)</p>
<dd> Unlike the similarly-named Tektronix &#8220;RESET&#8221; button, this does everything that <code>PAGE</code> does as well as resetting the line-type and font-size to their default values.</p>
<dt><code>COPY</code> (resource <code>tekcopy</code>)</p>
<dd> Simulates the Tektronix &#8220;COPY&#8221; button (which makes a hard-copy of the screen) by writing the information to a text file.</dl>
</dl>
<p> Windows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Show VT Window</code> (resource <code>vtshow</code>)</p>
<dd>
<dt><code>Switch to VT Mode</code> (resource <code>vtmode</code>)</p>
<dd>
<dt><code>Hide Tek Window</code> (resource <code>tekhide</code>)</p>
<dd></dl>
</dl>
<h2>SECURITY</h2>
<p> X environments differ in their security consciousness.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Most servers, run under <i>xdm</i>, are capable of using a &#8220;magic cookie&#8221; authorization scheme that can provide a reasonable level of security for many people. If your server is only using a host-based mechanism to control access to the server (see <code><a href="/docs/linux/man/1-xhost/">xhost</a>(1)</code>), then if you enable access for a host and other users are also permitted to run clients on that same host, it is possible that someone can run an application which uses the basic services of the X protocol to snoop on your activities, potentially capturing a transcript of everything you type at the keyboard.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 Any process which has access to your X display can manipulate it in ways that you might not anticipate, even redirecting your keyboard to itself and sending events to your application&#8217;s windows. This is true even with the &#8220;magic cookie&#8221; authorization scheme. While the <code>allowSendEvents</code> provides some protection against rogue applications tampering with your programs, guarding against a snooper is harder.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The X input extension for instance allows an application to bypass all of the other (limited) authorization and security features, including the GrabKeyboard protocol.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The possibility of an application spying on your keystrokes is of particular concern when you want to type in a password or other sensitive data. The best solution to this problem is to use a better authorization mechanism than is provided by X. </p>
<p> Subject to all of these caveats, a simple mechanism exists for protecting keyboard input in <i>xterm</i>. </p>
<p> The <i>xterm</i> menu (see <code>MENUS</code> above) contains a <code>Secure Keyboard</code> entry which, when enabled, attempts to ensure that all keyboard input is directed <i>only</i> to <i>xterm</i> (using the GrabKeyboard protocol request). When an application prompts you for a password (or other sensitive data), you can enable <code>Secure Keyboard</code> using the menu, type in the data, and then disable <code>Secure Keyboard</code> using the menu again.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 This ensures that you know which window is accepting your keystrokes.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 It cannot ensure that there are no processes which have access to your X display that might be observing the keystrokes as well. </p>
<p> Only one X client at a time can grab the keyboard, so when you attempt to enable <code>Secure Keyboard</code> it may fail. In this case, the bell will sound. If the <code>Secure Keyboard</code> succeeds, the foreground and background colors will be exchanged (as if you selected the <code>Enable Reverse Video</code> entry in the <code>Modes</code> menu); they will be exchanged again when you exit secure mode. If the colors do <i>not</i> switch, then you should be <i>very</i> suspicious that you are being spoofed. If the application you are running displays a prompt before asking for the password, it is safest to enter secure mode <i>before</i> the prompt gets displayed, and to make sure that the prompt gets displayed correctly (in the new colors), to minimize the probability of spoofing. You can also bring up the menu again and make sure that a check mark appears next to the entry. </p>
<p> <code>Secure Keyboard</code> mode will be disabled automatically if your <i>xterm</i> window becomes iconified (or otherwise unmapped), or if you start up a reparenting window manager (that places a title bar or other decoration around the window) while in <code>Secure Keyboard</code> mode. (This is a feature of the X protocol not easily overcome.) When this happens, the foreground and background colors will be switched back and the bell will sound in warning.</p>
<h2>CHARACTER CLASSES</h2>
<p> Clicking the left pointer button twice in rapid succession (double-clicking) causes all characters of the same class (e.g., letters, white space, punctuation) to be selected as a &#8220;word&#8221;. Since different people have different preferences for what should be selected (for example, should filenames be selected as a whole or only the separate subnames), the default mapping can be overridden through the use of the <code>charClass</code> (class <i>CharClass</i>) resource. </p>
<p> This resource is a series of comma-separated <i>range</i>:<i>value</i> pairs.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <i>range</i> is either a single number or <i>low</i>&#8211;<i>high</i> in the range of 0 to 65535, corresponding to the code for the character or characters to be set.<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 The <i>value</i> is arbitrary. For example, the default table uses the character number of the first character occurring in the set. When not in UTF-8 mode, only the first 256 entries of this table will be used. </p>
<p> The default table starts as follows &#8211;<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4<br />
static int charClass[256] = {<br />
    /* NUL  SOH  STX  ETX  EOT  ENQ  ACK  BEL */<br />
    32, 1, 1, 1, 1, 1, 1, 1,<br />
    /*  BS   HT   NL   VT   NP   CR   SO   SI */<br />
    1, 32, 1, 1, 1, 1, 1, 1,<br />
    /* DLE  DC1  DC2  DC3  DC4  NAK  SYN  ETB */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /* CAN   EM  SUB  ESC   FS   GS   RS   US */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /*  SP    !    &#8221;    #    $    %    &amp;    &#8216; */<br />
    32, 33, 34, 35, 36, 37, 38, 39,<br />
    /*   (    )    *    +    ,    &#8211;    .    / */<br />
    40, 41, 42, 43, 44, 45, 46, 47,<br />
    /*   0    1    2    3    4    5    6    7 */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   8    9    :    ;    &lt;    =    &gt;    ? */<br />
    48, 48, 58, 59, 60, 61, 62, 63,<br />
    /*   @    A    B    C    D    E    F    G */<br />
    64, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   H    I    J    K    L    M    N    O */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   P    Q    R    S    T    U    V    W */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   X    Y    Z    [    \    ]    ^    _ */<br />
    48, 48, 48, 91, 92, 93, 94, 48,<br />
    /*   `    a    b    c    d    e    f    g */<br />
    96, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   h    i    j    k    l    m    n    o */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   p    q    r    s    t    u    v    w */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   x    y    z    {    |    }    ~  DEL */<br />
    48, 48, 48, 123, 124, 125, 126, 1,<br />
    /* x80  x81  x82  x83  IND  NEL  SSA  ESA */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /* HTS  HTJ  VTS  PLD  PLU   RI  SS2  SS3 */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /* DCS  PU1  PU2  STS  CCH   MW  SPA  EPA */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /* x98  x99  x9A  CSI   ST  OSC   PM  APC */<br />
    1, 1, 1, 1, 1, 1, 1, 1,<br />
    /*   &#8211;    i   c/    L   ox   Y-    |   So */<br />
    160, 161, 162, 163, 164, 165, 166, 167,<br />
    /*  ..   c0   ip   &lt;&lt;    _        R0    &#8211; */<br />
    168, 169, 170, 171, 172, 173, 174, 175,<br />
    /*   o   +-    2    3    &#8216;    u   q|    . */<br />
    176, 177, 178, 179, 180, 181, 182, 183,<br />
    /*   ,    1    2   &gt;&gt;  1/4  1/2  3/4    ? */<br />
    184, 185, 186, 187, 188, 189, 190, 191,<br />
    /*  A`   A&#8217;   A^   A~   A:   Ao   AE   C, */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*  E`   E&#8217;   E^   E:   I`   I&#8217;   I^   I: */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*  D-   N~   O`   O&#8217;   O^   O~   O:    X */<br />
    48, 48, 48, 48, 48, 48, 48, 215,<br />
    /*  O/   U`   U&#8217;   U^   U:   Y&#8217;    P    B */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*  a`   a&#8217;   a^   a~   a:   ao   ae   c, */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*  e`   e&#8217;   e^   e:   i`   i&#8217;   i^   i: */<br />
    48, 48, 48, 48, 48, 48, 48, 48,<br />
    /*   d   n~   o`   o&#8217;   o^   o~   o:   -: */<br />
    48, 48, 48, 48, 48, 48, 48, 247,<br />
    /*  o/   u`   u&#8217;   u^   u:   y&#8217;    P   y: */<br />
    48, 48, 48, 48, 48, 48, 48, 48};</p>
<p>&nbsp;.in -4</p>
<dl>
<dt>
<dd> For example, the string &#8220;33:48,37:48,45-47:48,38:48&#8221; indicates that the exclamation mark, percent sign, dash, period, slash, and ampersand characters should be treated the same way as characters and numbers. This is useful for cutting and pasting electronic mailing addresses and filenames.</dl>
<h2>KEY BINDINGS</h2>
<p> It is possible to rebind keys (or sequences of keys) to arbitrary strings for input, by changing the <code>translations</code> resources for the vt100 or tek4014 widgets. Changing the <code>translations</code> resource for events other than key and button events is not expected, and will cause unpredictable behavior.</p>
<h3>Actions</h3>
<p> The following actions are provided for use within the <i>vt100</i> or <i>tek4014</i> <code>translations</code> resources:</p>
<dl>
<dt><code>allow-bold-fonts(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowBoldFonts</code> resource and is also invoked by the <code>allow-bold-fonts</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-color-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowColorOps</code> resource and is also invoked by the <code>allow-color-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-font-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowFontOps</code> resource and is also invoked by the <code>allow-font-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-mouse-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowMousepOps</code> resource and is also invoked by the <code>allow-mouse-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-send-events(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowSendEvents</code> resource and is also invoked by the <code>allowsends</code> entry in <i>mainMenu</i>.</p>
<dt><code>allow-tcap-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowTcapOps</code> resource and is also invoked by the <code>allow-tcap-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-title-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowTitleOps</code> resource and is also invoked by the <code>allow-title-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>allow-window-ops(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>allowWindowOps</code> resource and is also invoked by the <code>allow-window-ops</code> entry in <i>fontMenu</i>.</p>
<dt><code>alt-sends-escape()</code></p>
<dd> This action toggles the state of the <code>altSendsEscape</code> resource.</p>
<dt><code>bell([</code><i>percent</i>])</p>
<dd> This action rings the keyboard bell at the specified percentage above or below the base volume.</p>
<dt><code>clear-saved-lines()</code></p>
<dd> This action does <code>hard-reset()</code> and also clears the history of lines saved off the top of the screen. It is also invoked from the <code>clearsavedlines</code> entry in <i>vtMenu</i>. The effect is identical to a hardware reset (RIS) control sequence.</p>
<dt><code>copy-selection(</code><i>destname</i> [, &#8230;])</p>
<dd> This action puts the currently selected text into all of the selections or cutbuffers specified by <i>destname</i>. Unlike <code>select-end</code>, it does not send a mouse position or otherwise modify the internal selection state.</p>
<dt><code>create-menu(</code><i>m/v/f/t</i>)</p>
<dd> This action creates one of the menus used by <i>xterm</i>, if it has not been previously created. The parameter values are the menu names: <i>mainMenu</i>, <i>vtMenu</i>, <i>fontMenu</i>, <i>tekMenu</i>, respectively.</p>
<dt><code>dabbrev-expand()</code></p>
<dd> Expands the word before cursor by searching in the preceding text on the screen and in the scrollback buffer for words starting with that abbreviation. Repeating <code>dabbrev-expand()</code> several times in sequence searches for an alternative expansion by looking farther back. Lack of more matches is signaled by a bell. Attempts to expand an empty word (i.e., when cursor is preceded by a space) yield successively all previous words. Consecutive identical expansions are ignored. The word here is defined as a sequence of non-whitespace characters. This feature partially emulates the behavior of &#8220;dynamic abbreviation&#8221; expansion in Emacs (bound there to M-/). Here is a resource setting for <i>xterm</i> which will do the same thing:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
*VT100*translations:    #override 
\
        Meta &lt;KeyPress&gt; /:<code>dabbrev-expand</code>()
</pre>
<p>&nbsp;.in -4</p>
<dt><code>deiconify()</code></p>
<dd> Changes the window state back to normal, if it was iconified.</p>
<dt><code>delete-is-del()</code></p>
<dd> This action toggles the state of the <code>deleteIsDEL</code> resource.</p>
<dt><code>dired-button()</code></p>
<dd> Handles a button event (other than press and release) by echoing the event&#8217;s position (i.e., character line and column) in the following format:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
^X ESC G &lt;line+`` ''&gt; &lt;col+`` ''&gt;
</pre>
<p>&nbsp;.in -4</p>
<dt><code>dump-html()</code></p>
<dd> Invokes the <code>XHTML Screen Dump</code> feature.</p>
<dt><code>dump-svg()</code></p>
<dd> Invokes the <code>SVG Screen Dump</code> feature.</p>
<dt><code>exec-formatted(</code><i>format</i>, <i>sourcename</i> [, &#8230;])</p>
<dd> Execute an external command, using the current selection for part of the command&#8217;s parameters. The first parameter, <i>format</i> gives the basic command. Succeeding parameters specify the selection source as in <code>insert-selection</code>.</p>
<dt>
<dd> The <i>format</i> parameter allows these substitutions:</p>
<dl>
<dt>
<dd>
<dl>
<dt>%%</p>
<dd> inserts a &quot;%&quot;.</p>
<dt>%P</p>
<dd> the screen-position at the beginning of the highlighted region, as a semicolon-separated pair of integers using the values that the CUP control sequence would use.</p>
<dt>%p</p>
<dd> the screen-position after the beginning of the highlighted region, using the same convention as &#8220;%P&#8221;.</p>
<dt>%S</p>
<dd> the length of the string that &#8220;%s&#8221; would insert.</p>
<dt>%s</p>
<dd> the content of the selection, unmodified.</p>
<dt>%T</p>
<dd> the length of the string that &#8220;%t&#8221; would insert.</p>
<dt>%t</p>
<dd> the selection, trimmed of leading/trailing whitespace. Embedded spaces (and newlines) are copied as is.</p>
<dt>%R</p>
<dd> the length of the string that &#8220;%r&#8221; would insert.</p>
<dt>%r</p>
<dd> the selection, trimmed of trailing whitespace.</p>
<dt>%V</p>
<dd> the video attributes at the beginning of the highlighted region, as a semicolon-separated list of integers using the values that the SGR control sequence would use.</p>
<dt>%v</p>
<dd> the video attributes after the end of the highlighted region, using the same convention as &#8220;%V&#8221;.</dl>
</dl>
<dt>
<dd> After constructing the command-string, <i>xterm</i> forks a subprocess and executes the command, which completes independently of <i>xterm</i>.</p>
<dt>
<dd> For example, this translation would invoke a new <i>xterm</i> process to view a file whose name is selected while holding the shift key down. The new process is started when the mouse button is released:<br />
&nbsp;.sp<br />
&nbsp;.in&nbsp;+4 </p>
<pre>
*VT100*translations: #override Shift \
    &lt;Btn1Up&gt;:<code>exec-formatted</code>(&quot;xterm -e view '%t'&quot;, <code>SELECT</code>)
</pre>
<p>&nbsp;.in -4</p>
<dt><code>exec-selectable(</code><i>format</i>, <i>onClicks</i>)</p>
<dd> Execute an external command, using data copied from the screen for part of the command&#8217;s parameters. The first parameter, <i>format</i> gives the basic command as in <code>exec-formatted</code>. The second parameter specifies the method for copying the data as in the <code>on2Clicks</code> resource.</p>
<dt><code>fullscreen(</code><i>on/off/toggle</i>)</p>
<dd> This action sets, unsets or toggles the <code>fullscreen</code> resource.</p>
<dt><code>hard-reset()</code></p>
<dd> This action resets the scrolling region, tabs, window size, and cursor keys and clears the screen. It is also invoked from the <code>hardreset</code> entry in <i>vtMenu</i>.</p>
<dt><code>iconify()</code></p>
<dd> Iconifies the window.</p>
<dt><code>ignore()</code></p>
<dd> This action ignores the event but checks for special pointer position escape sequences.</p>
<dt><code>insert()</code></p>
<dd> This action inserts the character or string associated with the key that was pressed.</p>
<dt><code>insert-eight-bit()</code></p>
<dd> This action inserts an eight-bit (Meta) version of the character or string associated with the key that was pressed. Only single-byte values are treated specially. The exact action depends on the value of the <code>altSendsEscape</code> and the <code>metaSendsEscape</code> and the <code>eightBitInput</code> resources. The <code>metaSendsEscape</code> resource is tested first. See the <code>eightBitInput</code> resource for a full discussion.</p>
<dt>
<dd> The term &#8220;eight-bit&#8221; is misleading: <i>xterm</i> checks if the key is in the range 128 to 255 (the eighth bit is set). If the value is in that range, depending on the resource values, <i>xterm</i> may then do one of the following:</p>
<dl>
<dt>
<dd>
&nbsp;.IP&nbsp;&bull;&nbsp;4 add 128 to the value, setting its eighth bit,<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 send an ESC byte before the key, or<br />
&nbsp;.IP&nbsp;&bull;&nbsp;4 send the key unaltered.</dl>
<dt><code>insert-formatted(</code><i>format</i>, <i>sourcename</i> [, &#8230;])</p>
<dd> Insert the current selection or data related to it, formatted. The first parameter, <i>format</i> gives the template for the data as in <code>exec-formatted</code>. Succeeding parameters specify the selection source as in <code>insert-selection</code>.</p>
<dt><code>insert-selectable(</code><i>format</i>, <i>onClicks</i>)</p>
<dd> Insert data copied from the screen, formatted. The first parameter, <i>format</i> gives the template for the data as in <code>exec-formatted</code>. The second parameter specifies the method for copying the data as in the <code>on2Clicks</code> resource.</p>
<dt><code>insert-selection(</code><i>sourcename</i> [, &#8230;])</p>
<dd> This action inserts the string found in the selection or cutbuffer indicated by <i>sourcename</i>. Sources are checked in the order given (case is significant) until one is found. Commonly-used selections include: <code>PRIMARY</code>, <code>SECONDARY</code>, and <code>CLIPBOARD</code>. Cut buffers are typically named <code>CUT_BUFFER0</code> through <code>CUT_BUFFER7</code>.</p>
<dt><code>insert-seven-bit()</code></p>
<dd> This action is a synonym for <code>insert()</code>. The term &#8220;seven-bit&#8221; is misleading: it only implies that <i>xterm</i> does not try to add 128 to the key&#8217;s value as in <code>insert-eight-bit()</code>.</p>
<dt><code>interpret(</code><i>control-sequence</i>)</p>
<dd> Interpret the given control sequence locally, i.e., without passing it to the host. This works by inserting the control sequence at the front of the input buffer. Use &#8220;\&#8221; to escape octal digits in the string. Xt does not allow you to put a null character (i.e., &#8220;
