---
title: "aterm(1)"
name: "aterm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aterm/"
description: "aterm (Afterstep XVT) – a VT102 emulator for the X window system"
---
<h2>NAME</h2>
<p> aterm (Afterstep XVT) - a VT102 emulator for the X window system </p>
<h2>SYNOPSIS</h2>
<p> <code>aterm</code> [options] [-e command [ args ]] </p>
<h2>DESCRIPTION</h2>
<p> <code>aterm</code>, version <code>1.0.0</code>, is a colour vt102 terminal emulator, based on <i>rxvt</i> 2.4.8 with Alfredo Kojima&#8217;s additions of fast transparency, intended as an <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) replacement for users who do not require features such as Tektronix 4014 emulation and toolkit-style configurability. As a result, <code>aterm</code> uses much less swap space -- a significant advantage on a machine serving many X sessions. </p>
<p> It was created with <code>AfterStep</code> Window Manger users in mind, but is not tied to any libraries, and can be used anywhere. </p>
<h2>OPTIONS</h2>
<p> The <code>aterm</code> options (mostly a subset of <i>xterm</i>&#8216;s) are listed below. In keeping with the smaller-is-better philosophy, options may be eliminated or default values chosen at compile-time, so options and defaults listed may not accurately reflect the version installed on your system. </p>
<p> Note that <code>aterm</code> permits the resource name to be used as a long-option (--/++ option) so the potential command-line options are far greater than those listed. For example: `aterm --loginShell --color1 Orange&#8217;. </p>
<dl>
<dt><code>-help</code>, <code>--help</code></dt>
<dd> <p> Print out a message describing available options. </p>
 </dd>
<dt><code>-version</code>, <code>--version</code></dt>
<dd> <p> Print out a version with/without list of available options. </p>
 </dd>
<dt><code>-display</code><i>displayname</i></dt>
<dd> <p> Attempt to open a window on the named X display (<code>-d</code> still respected). In the absence of this option, the display specified by the <code>DISPLAY</code> environment variable is used. </p>
 </dd>
<dt><code>-geometry</code><i>geom</i></dt>
<dd> <p> Window geometry (-g still respected); resource <code>geometry</code>. </p>
 </dd>
<dt><code>-rv</code>|<code>+rv</code></dt>
<dd> <p> Turn on/off simulated reverse video; resource <code>reverseVideo</code>. </p>
 </dd>
<dt><code>-bg</code><i>colour</i></dt>
<dd> <p> Window background colour; resource <code>background</code>. </p>
 </dd>
<dt><code>-fg</code><i>colour</i></dt>
<dd> <p> Window foreground colour; resource <code>foreground</code>. </p>
 </dd>
<dt><code>-pixmap:</code><i>file[;geom]</i></dt>
<dd> <p> Specify image file for the background and also optionally specify geometry of the image to be cut out of original image, to be used as background, with a geometry string. Note you may need to add quotes to avoid special shell interpretation of the `;&#8216; in the command-line; resource <code>backgroundPixmap</code>. </p>
 </dd>
<dt><code>-mst:</code><i>name</i></dt>
<dd> <p> Specify the name of the Afterstep MyStyle to be used as the base of aterm&#8217;s look. ForeColor, BackColor, Font, BackPixmap (all texture options) will be used from MyStyle definition, unless some other command line option is specifyed for the same setting. For example -fn will override MyStyle Font. This is available only if used with AfterStep 1.9.28 or later and if compiled with AfterStep libraries support ( --enable-afterstep-lib). resource <code>MyStyle</code>. </p>
 </dd>
<dt><code>-tr</code>|<code>+tr</code></dt>
<dd> <p> Turn on/off pseudo transparency mode. In this mode <code>aterm</code> will use part of root background as it&#8217;s own background, emulating see-through effect; resource <code>transparent</code>. </p>
 </dd>
<dt><code>-trsb</code>|<code>+trsb</code></dt>
<dd> <p> Turn on/off pseudo transparent scrollbar. Works the same as -tr; resource <code>transpscrollbar</code>. </p>
 </dd>
<dt><code>-tint</code><i>color</i></dt>
<dd> <p> Turn on pseudo transparency background tinting. Tinting can be done fast and slow way. In fast way it will be done by combining of background color with tinting color using logical function. This function defaults to AND, and it can be changed using <code>-tinttype</code> option - see below. In general solid colors like Blue, Red, Green, Cyan, Magenta, Yellow are good, but you should experiment with it for each background you have. True tinting is more memory and CPU hungry - tinted copy of background image will be created every time you move/resize window. It alows for more smooth tinting thou. You need to build it with <code>--enable-transparency=yes</code> or <code>--enable-background-imageyes</code> option, to be able to use this feature. resource <code>tinting</code>.<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 </p>
 </dd>
<dt><code>-sh</code><i>amount</i></dt>
<dd> <p> This option allows for darkening/lightening of the background image <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 - image will be darkened. if <i>amount</i> is less then 0 or more then 100 - image will be lightened. Lightening can cause some strange looking effects if applied on bright image. This option causes aterm to create shaded/lightened copy of the background - it&#8217;s more memory cosuming as the result. It does not make much difference, though, if applied on non transparent background image. resource <code>shading</code>.<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 </p>
 </dd>
<dt><code>-fade</code><i>amount</i></dt>
<dd> <p> This option allows for darkening/lightening of colors when aterm is loosing focus. <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 - colors will be darkened. if <i>amount</i> is less then 0 or more then 100 - colors will be lightened. Lightening can cause some strange looking effects if applied on bright colors. This option causes aterm to use more colors, as the result it is disabled by default. Use --enable-fading ./configure option to enable it. resource <code>fading</code>.<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 </p>
 </dd>
<dt><code>-bgtype</code><i>type</i></dt>
<dd> <p> Specify type of the transformation to be performed on background image. Possible types are : <code>tile</code> - plain vanilla tiling of the image. <code>scale</code> - original image will be scaled to the aterm&#8217;s size, every time you resize window. <code>scalev</code> - original image will be scaled to the aterm&#8217;s height only, every time you resize window. <code>scaleh</code> - original image will be scaled to the aterm&#8217;s width only, every time you resize window. <code>center</code> - original image will be centered in aterm&#8217;s window. <code>notile</code> - background color will be padded to image&#8217;s right/bottom to make it the same size as window is. <code>notileh</code> - background color will be padded to image&#8217;s right to make it the same width as window is. <code>notilev</code> - background color will be padded to image&#8217;s bottom to make it the same height as window is. <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 <code>cut</code> - aterm background will be cut out of the source image, as if this source image was tiled across the root window. The portion of the image that lies underneath of window will be used. <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 If AfterStep Pager, asetroot or Esetroot where used to set the root image, then this option can be used in conjunction with -tr option. In this case it will do mentioned transformations to the root pixmap. and use it as aterm&#8217;s background. resource <code>backgroundType</code>. </p>
 </dd>
<dt><code>-txttype</code><i>type</i></dt>
<dd> <p> Allows you to specify logical function to be used when displaying text. That will cause aterm to logically combine text with background pixels. That only works with transparent background and background image. Possible values are : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>; resource <code>textType</code>. </p>
 </dd>
<dt><code>-tinttype</code><i>type</i></dt>
<dd> <p> Allows you to specify logical function to be used when tinting transparent background. That will cause aterm to logically combine text with background pixels. NOTE: If shading option is used, or background image is specifyed - <i>true</i> type will always be used. That works with bpth transparent background and background image. Possible values are : </p>
 </dd>
<dd> <p> Fast tinting options : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>, </p>
 </dd>
<dd> <p> Slow tinting: <i>true</i> - will do &quot;true&quot; tinting - that means that background pixel&#8217;s RGB components will be decreased proportionaly to the RGB components of specified tinting color; resource <code>tintingType</code>. </p>
 </dd>
<dt><code>-cr</code><i>colour</i></dt>
<dd> <p> The cursor colour; resource <code>cursorColor</code>. </p>
 </dd>
<dt><code>-pr</code><i>colour</i></dt>
<dd> <p> The mouse pointer colour; resource <code>pointerColor</code>. </p>
 </dd>
<dt><code>-bd</code><i>colour</i></dt>
<dd> <p> The colour of the border between the xterm scrollbar and the text; resource <code>borderColor</code>. </p>
 </dd>
<dt><code>-bl</code><i>number</i></dt>
<dd> <p> This option specifies that aterm should askwindow manager to not have a border around term&#8217;s window; resource <code>borderLess</code>. </p>
 </dd>
<dt><code>-bw</code><i>number</i></dt>
<dd> <p> This option specifies the width in pixels of the border surrounding the window; resource <code>borderWidth</code>. </p>
 </dd>
<dt><code>-fn</code><i>fontname</i></dt>
<dd> <p> Main normal text font; resource <code>font</code>. </p>
 </dd>
<dt><code>-fb</code><i>fontname</i></dt>
<dd> <p> Main bold text font; resource <code>boldFont</code>. </p>
 </dd>
<dt><code>-fm</code><i>fontname</i></dt>
<dd> <p> Main multicharacter font; resource <code>mfont</code>. </p>
 </dd>
<dt><code>-ib</code><i>width</i></dt>
<dd> <p> Width of the internal border in pixels; resource <code>internalBorder</code>. </p>
 </dd>
<dt><code>-km</code><i>mode</i></dt>
<dd> <p> Multiple-character font-set encoding mode; <code>eucj</code>: EUC Japanese encoding. <code>sjis</code>: Shift JIS encoding; resource <code>multichar_encoding</code>. </p>
 </dd>
<dt><code>-grk</code><i>mode</i></dt>
<dd> <p> Greek keyboard translation; <code>iso</code>: ISO-8859 mapping. <code>ibm</code>: IBM-437 mapping; resource <code>greek_keyboard</code>. </p>
 </dd>
<dt><code>-name</code><i>name</i></dt>
<dd> <p> Specify the application name under which resources are to be obtained, rather than the default executable file name. Name should not contain `.&#8216; or `*&#8216; characters. Also sets the icon and title name. </p>
 </dd>
<dt><code>-ls</code>|<code>+ls</code></dt>
<dd> <p> Start as a login-shell/sub-shell; resource <code>loginShell</code>. </p>
 </dd>
<dt><code>-ut</code>|<code>+ut</code></dt>
<dd> <p> Inhibit/enable writing a utmp entry; resource <code>utmpInhibit</code>. </p>
 </dd>
<dt><code>-vb</code>|<code>+vb</code></dt>
<dd> <p> Turn on/off visual bell on receipt of a bell character; resource <code>visualBell</code>. </p>
 </dd>
<dt><code>-sb</code>|<code>+sb</code></dt>
<dd> <p> Turn on/off scrollbar; resource <code>scrollBar</code>. </p>
 </dd>
<dt><code>-si</code>|<code>+si</code></dt>
<dd> <p> Turn on/off scroll-to-bottom on TTY output inhibit; resource <code>scrollTtyOutput</code> has opposite effect. </p>
 </dd>
<dt><code>-sk</code>|<code>+sk</code></dt>
<dd> <p> Turn on/off scroll-to-bottom on keypress; resource <code>scrollKey</code>. </p>
 </dd>
<dt><code>-sr</code>|<code>+sr</code></dt>
<dd> <p> Put scrollbar on right/left; resource <code>scrollBar_right</code>. </p>
 </dd>
<dt><code>-st</code>|<code>+st</code></dt>
<dd> <p> Display scrollbar without/with a trough; resource <code>scrollBar_floating</code>. </p>
 </dd>
<dt><code>-iconic</code></dt>
<dd> <p> Start iconified, if the window manager supports that option. </p>
 </dd>
<dt><code>-sl</code><i>number</i></dt>
<dd> <p> Save <i>number</i> lines in the scrollback buffer; resource <code>saveLines</code>. </p>
 </dd>
<dt><code>-tn</code><i>termname</i></dt>
<dd> <p> This option specifies the name of the terminal type to be set in the <code>TERM</code> environment variable. This terminal type must exist in the <i><a href="/docs/linux/man/5-termcap/">termcap</a>(5)</i> database and should have <i>li#</i> and <i>co#</i> entries; resource <code>termName</code>. </p>
 </dd>
<dt><code>-e</code><i>command [arguments]</i></dt>
<dd> <p> Run the command with its command-line arguments in the <code>aterm</code> window; also sets the window title and icon name to be the basename of the program being executed if neither <i>-title</i> (<i>-T</i>) nor <i>-n</i> are given on the command line. If this option is used, it must be the last on the command-line. If there is no <code>-e</code> option then the default is to run the program specified by the <code>SHELL</code> environment variable or, failing that, <i><a href="/docs/linux/man/1-sh/">sh</a>(1)</i>. </p>
 </dd>
<dt><code>-title</code><i>text</i></dt>
<dd> <p> Window title <code>-T</code> still respected); the default title is the basename of the program specified after the \f3\-e\fP option, if any, otherwise the application name; resource <code>title</code>. </p>
 </dd>
<dt><code>-n</code><i>text</i></dt>
<dd> <p> Icon name; the default name is the basename of the program specified after the \f3\-e\fP option, if any, otherwise the application name; resource <code>iconName</code>. </p>
 </dd>
<dt><code>-C</code></dt>
<dd> <p> Capture system console messages. </p>
 </dd>
<dd>  </dd></dl>
<h2>RESOURCES (available also as long-options)</h2>
<p> <code>aterm</code> accepts application defaults set in XAPPLOADDIR/aterm (compile-time defined: usually <code>/etc/X11/Xresources/aterm</code>) and resources set in <code>~/.Xdefaults</code> or <code>~/.Xresources</code>. Note that when reading X resources, <code>aterm</code> recognizes two class names: <code>XTerm</code> and <code>Aterm</code>. The class name <code>XTerm</code> allows resources common to both <code>aterm</code> and <i>xterm</i> to be easily configured, while the class name <code>Aterm</code> allows resources unique to <code>aterm</code>, notably colours and key-handling, to be shared between different <code>aterm</code> configurations. If no resources are specified, suitable defaults will be used. Command-line arguments can be used to override resource settings. The following resources are allowed: </p>
<dl>
<dt><code>geometry:</code><i>geom</i></dt>
<dd> <p> Create the window with the specified X window geometry [default 80x24]; option <code>-geometry</code>. </p>
 </dd>
<dt><code>background:</code><i>colour</i></dt>
<dd> <p> Use the specified colour as the window&#8217;s background colour [default White]; option <code>-bg</code>. </p>
 </dd>
<dt><code>foreground:</code><i>colour</i></dt>
<dd> <p> Use the specified colour as the window&#8217;s foreground colour [default Black]; option <code>-fg</code>. </p>
 </dd>
<dt><code>color</code><i>n</i><code>:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the colour value <i>n</i>, where 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity (bold = bright foreground, blink = bright background) colours. The canonical names are as follows: 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white, but the actual colour names used are listed in the <code>COLORS AND GRAPHICS</code> section. </p>
 </dd>
<dt><code>colorBD:</code><i>colour</i></dt>
<dd> <p> Use the specified colour to display bold characters when the foreground colour is the default. </p>
 </dd>
<dt><code>colorUL:</code><i>colour</i></dt>
<dd> <p> Use the specified colour to display underlined characters when the foreground colour is the default. </p>
 </dd>
<dt><code>cursorColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the cursor. The default is to use the foreground colour; option <code>-cr</code>. </p>
 </dd>
<dt><code>cursorColor2:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the colour of the cursor text. For this to take effect, <code>cursorColor</code> must also be specified. The default is to use the background colour. </p>
 </dd>
<dt><code>reverseVideo:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: simulate reverse video by foreground and background colours; option <code>-rv</code>, <code>False</code>: regular screen colours [default]; option <code>+rv</code>. See note in <code>COLORS AND GRAPHICS</code> section. </p>
 </dd>
<dt><code>scrollColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the scrollbar [default #B2B2B2]. </p>
 </dd>
<dt><code>troughColor:</code><i>colour</i></dt>
<dd> <p> Use the specified colour for the scrollbar&#8217;s trough area [default #969696]. </p>
 </dd>
<dt><code>backgroundPixmap:</code><i>file[;geom]</i></dt>
<dd> <p> Use the specified image file, and cut the area defined by geometry string out of it. </p>
 </dd>
<dt><code>MyStyle:</code><i>name</i></dt>
<dd> <p> Specify the name of the Afterstep MyStyle to be used as the base of aterm&#8217;s look. ForeColor, BackColor, Font, BackPixmap (all texture options) will be used from MyStyle definition, unless some other command line option is specifyed for the same setting. For example resource font will override MyStyle Font. This is available only if used with AfterStep 1.9.28 or later and if compiled with AfterStep libraries support ( --enable-afterstep-lib). </p>
 </dd>
<dt><code>transparent</code></dt>
<dd> <p> Turn on/off pseudo transparency mode. In this mode <code>aterm</code> will use part of root background as it&#8217;s own background, emulating see-through effect; </p>
 </dd>
<dt><code>tinting:</code><i>color</i></dt>
<dd> <p> Turn on pseudo transparency background tinting. Tinting can be done fast and slow way. In fast way it will be done by combining of background color with tinting color using logical function. This function defaults to AND, and it can be changed using <code>-tinttype</code> option - see below. In general solid colors like Blue, Red, Green, Cyan, Magenta, Yellow are good, but you should experiment with it for each background you have. True tinting is more memory and CPU hungry - tinted copy of background image will be created every time you move/resize window. It alows for more smooth tinting thou. You need to build it with <code>--enable-transparency=yes</code> or <code>--enable-background-image=yes</code> option, to be able to use this feature. </p>
 </dd>
<dd>  </dd>
<dt><code>-shading:</code><i>amount</i></dt>
<dd> <p> This option allows for darkening/lightening of the background image <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 - image will be darkened. if <i>amount</i> is less then 0 or more then 100 - image will be lightened. Lightening can cause some strange looking effects if applied on bright image. This option causes aterm to create shaded/lightened copy of the background - it&#8217;s more memory cosuming as the result. It does not make much difference, though, if applied on non transparent background image. </p>
 </dd>
<dt><code>backgroundType:</code><i>type</i></dt>
<dd> <p> Specify type of the transformation to be performed on background image. Possible types are : <code>tile</code> - plain vanilla tiling of the image. <code>scale</code> - original image will be scaled to the aterm&#8217;s size, every time you resize window. <code>scalev</code> - original image will be scaled to the aterm&#8217;s height only, every time you resize window. <code>scaleh</code> - original image will be scaled to the aterm&#8217;s width only, every time you resize window. <code>center</code> - original image will be centered in aterm&#8217;s window. <code>notile</code> - background color will be padded to image&#8217;s right/bottom to make it the same size as window is. <code>notileh</code> - background color will be padded to image&#8217;s right to make it the same width as window is. <code>notilev</code> - background color will be padded to image&#8217;s bottom to make it the same height as window is. <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 <code>cut</code> - aterm background will be cut out of the source image, as if this source image was tiled across the root window. The portion of the image that lies underneath of window will be used. <code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></code><br />
 If AfterStep Pager, asetroot or Esetroot where used to set the root image, then this option can be used in conjunction with -tr option. In this case it will do mentioned transformations to the root pixmap. and use it as aterm&#8217;s background. </p>
 </dd>
<dt><code>textType:</code><i>type</i></dt>
<dd> <p> Allows you to specify logical function to be used when displaying text. That will cause aterm to logically combine text with background pixels. That only works with transparent background and background image. Possible values are : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>. </p>
 </dd>
<dt><code>tintingType</code><i>type</i></dt>
<dd> <p> Allows you to specify logical function to be used when tinting transparent background. That will cause aterm to logically combine text with background pixels. NOTE: If shading option is used, or background image is specifyed - <i>true</i> type will always be used. That works with bpth transparent background and background image. Possible values are : </p>
 </dd>
<dd> <p> Fast tinting options : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>, </p>
 </dd>
<dd> <p> Slow tinting: <i>true</i> - will do &quot;true&quot; tinting - that means that background pixel&#8217;s RGB components will be decreased proportionaly to the RGB components of specified tinting color. </p>
 </dd>
<dd>  </dd>
<dt><code>menu:</code><i>file[;tag]</i></dt>
<dd> <p> Read in the specified menu file (note the `.menu&#8217; extension is optional) and also optionally specify a starting tag to find. See the reference documentation for details on the syntax for the menuBar. </p>
 </dd>
<dt><code>path:</code><i>path</i></dt>
<dd> <p> Specify the colon-delimited search path for finding files (XPM and menus), in addition to the paths specified by the <code>RXVTPATH</code> and <code>PATH</code> environment variables. </p>
 </dd>
<dt><code>font:</code><i>fontname</i></dt>
<dd> <p> Select the main text font used [default 7x14]; option <code>-fn</code>. </p>
 </dd>
<dt><code>font</code><i>n</i><code>:</code><i>fontname</i></dt>
<dd> <p> Specify the alternative font <i>n</i>. The default font values: <br />
 </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <table>
<tr VALIGN=top>
<td><code><code>font</code>: `&nbsp;<wbr>7x14 </code>
</td>
</tr>
<tr VALIGN=top>
<td><code>font1</code>: `&nbsp;<wbr>6x10 
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font2</code>: `&nbsp;<wbr>6x13 
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font3</code>: `&nbsp;<wbr>8x13 
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font4</code>: `&nbsp;<wbr>9x15 
</td>
<td>
</td>
</tr>
</table>
 </dd></dl>
</dl>
<dd>  </dd>
<dt><code>boldFont:</code><i>fontname</i></dt>
<dd> <p> Specify the name of the bold font to use if <code>colorBD</code> has not been specified and it is not possible to map the default foreground colour to colour 8-15 [default NONE]. This font must be the same height and width as the normal font; option <code>-fb</code>. </p>
 </dd>
<dt><code>mfont:</code><i>fontname</i></dt>
<dd> <p> Select the main multiple-character text font used [default k14]; option <code>-fk</code>. </p>
 </dd>
<dt><code>mfont</code><i>n</i><code>:</code><i>fontname</i></dt>
<dd> <p> Specify the alternative multiple-character font <i>n</i>. If compiled for multiple-character fonts, the Roman and multiple-character font sizes should match. </p>
 </dd>
<dt><code>multichar_encoding:</code><i>mode</i></dt>
<dd> <p> Set the encoding mode to be used when multicharacter encoding is received; <code>eucj</code>: EUC Japanese encoding [default for Kanji]. <code>sjis</code>: Shift JIS encoding. <code>big5</code>: BIG5 encoding; option <code>-km</code>. </p>
 </dd>
<dt><code>greek_keyboard:</code><i>mode</i></dt>
<dd> <p> Set the Greek keyboard translation mode to be used; <code>iso</code>: ISO-8859 mapping (elot-928) [default]. <code>ibm</code>: IBM-437 mapping (DOS codepage 737); option <code>-grk</code>. Use <code>Mode_switch</code> to toggle keyboard input. For more details, see the distributed file <code>README.greek</code>. </p>
 </dd>
<dt><code>title:</code><i>text</i></dt>
<dd> <p> Set window title string, the default title is the command-line specified after the <code>-e</code> option, if any, otherwise the application name; option <code>-title</code>. </p>
 </dd>
<dt><code>iconName:</code><i>text</i></dt>
<dd> <p> Set the name used to label the window&#8217;s icon or displayed in an icon manager window, it also sets the window&#8217;s title unless it is explicitly set; option <code>-n</code>. </p>
 </dd>
<dt><code>mapAlert:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: de-iconify (map) on receipt of a bell character. <code>False</code>: no de-iconify (map) on receipt of a bell character [default]. </p>
 </dd>
<dt><code>visualBell:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: use visual bell on receipt of a bell character; option <code>-vb</code>. <code>False</code>: no visual bell [default]; option <code>+vb</code>. </p>
 </dd>
<dt><code>loginShell:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: start as a login shell by prepending a `-&#8216; to <code>argv[0]</code> of the shell; option <code>-ls</code>. <code>False</code>: start as a normal sub-shell [default]; option <code>+ls</code>. </p>
 </dd>
<dt><code>utmpInhibit:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: inhibit writing record into the system log file <code>utmp</code>; option <code>-ut</code>. <code>False</code>: write record into the system log file <code>utmp</code> [default]; option <code>+ut</code>. </p>
 </dd>
<dt><code>print-pipe:</code><i>string</i></dt>
<dd> <p> Specify a command pipe for vt100 printer [default <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>]. Use <code>Print</code> to initiate a screen dump to the printer and <code>Ctrl-Print</code> or <code>Shift-Print</code> to include the scrollback as well. </p>
 </dd>
<dt><code>scrollBar:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: enable the scrollbar [default]; option <code>-sb</code>. <code>False</code>: disable the scrollbar; option <code>+sb</code>. Note that the scrollbar type (with/without arrows) is compile-time selected. </p>
 </dd>
<dt><code>smallfont_key:</code><i>keysym</i></dt>
<dd> <p> If enabled, use <code>Alt-</code><i>keysym</i> to toggle to a smaller font [default <code>Alt-&lt;</code>] </p>
 </dd>
<dt><code>bigfont_key:</code><i>keysym</i></dt>
<dd> <p> If enabled, use <code>Alt-</code><i>keysym</i> to toggle to a bigger font [default <code>Alt-&gt;</code>] </p>
 </dd>
<dt><code>saveLines:</code><i>number</i></dt>
<dd> <p> Save <i>number</i> lines in the scrollback buffer [default 64]; option <code>-sl</code>. </p>
 </dd>
<dt><code>termName:</code><i>termname</i></dt>
<dd> <p> Specifies the terminal type name to be set in the <code>TERM</code> environment variable; option <code>-tn</code>. </p>
 </dd>
<dt><code>meta8:</code><i>boolean</i></dt>
<dd> <p> <code>True</code>: handle Meta (Alt) + keypress to set the 8th bit. <code>False</code>: handle Meta (Alt) + keypress as an escape prefix [default]. </p>
 </dd>
<dt><code>modifier:</code><i>string</i></dt>
<dd> <p> Set the Meta key to be enabled by modifier <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code> or <code>Mod5</code>. </p>
 </dd>
<dt><code>backspacekey:</code><i>string</i></dt>
<dd> <p> The string to send when the backspace key is pressed. If set to <code>DEC</code> or unset it will send <code>Delete</code> (code 127) or, if shifted, <code>Backspace</code> (code 8) - which can be reversed with the appropriate DEC private mode escape sequence. </p>
 </dd>
<dt><code>deletekey:</code><i>string</i></dt>
<dd> <p> The string to send when the delete key (not the keypad delete key) is pressed. If unset it will send the sequence traditionally associated with the <code>Execute</code> key. </p>
 </dd>
<dt><code>cutchars:</code><i>string</i></dt>
<dd> <p> The characters used as delimiters for double-click word selection. The built-in default: <br />
 <code>BACKSLASH `&quot;&#8216;&amp;()*,;&lt;=&gt;?@[]{|}</code> </p>
 </dd>
<dt><code>keysym.</code><i>sym</i>: <i>string</i></dt>
<dd> <p> Associate <i>string</i> with keysym <i>sym</i> (<code>0xFF00 - 0xFFFF</code>). It may contain escape values (\a: bell, \b: backspace, \e, \E: escape, \n: newline, \r: return, \t: tab, \000: octal number) or control characters (^?: delete, ^@: null, ^A ...) and may enclosed with double quotes so that it can start or end with whitespace. The intervening resource name <code>keysym.</code> cannot be omitted. This resource is only available when compiled with KEYSYM_RESOURCE. </p>
 </dd></dl>
<h2>THE SCROLLBAR</h2>
<p> Lines of text that scroll off the top of the <code>aterm</code> window (resource: <code>saveLines</code>) and can be scrolled back using the scrollbar or by keystrokes. The normal <code>aterm</code> scrollbar has arrows and its behaviour is fairly intuitive. The <code>xterm-scrollbar</code> is without arrows and its behaviour mimics that of <i>xterm</i>. When build with --enable-next-scroll <code>aterm</code> will have NeXT-ish scrollbars. They look nicer and easier in use, but have slightly larger size. Their look and size can be tweaked at compile time by modifying parameters in rxvt.h. </p>
<p> Scroll down with <code>Button1</code> (<code>xterm-scrollbar</code>) or <code>Shift-Next</code>. Scroll up with <code>Button3</code> (<code>xterm-scrollbar</code>) or <code>Shift-Prior</code>. Continuous scroll with <code>Button2</code>.  </p>
<h2>MOUSE REPORTING</h2>
<p> To temporarily override mouse reporting, for either the scrollbar or the normal text selection/insertion, hold either the Shift or the Meta (Alt) key while performing the desired mouse action. </p>
<p> If mouse reporting mode is active, the normal scrollbar actions are disabled -- on the assumption that we are using a fullscreen application. Instead, pressing Button1 and Button3 sends <code>ESC[6~</code> (Next) and <code>ESC[5~</code> (Prior), respectively. Similarly, clicking on the up and down arrows sends <code>ESC[A</code> (Up) and <code>ESC[B</code> (Down), respectively.  </p>
<h2>TEXT SELECTION AND INSERTION</h2>
<p> The behaviour of text selection and insertion mechanism is similar to <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1). </p>
<dl>
<dt><code>Selection</code>:</dt>
<dd> <p> Left click at the beginning of the region, drag to the end of the region and release; Right click to extend the marked region; Left double-click to select a word; Left triple-click to select the entire line. </p>
 </dd>
<dd>  </dd>
<dt><code>Insertion</code>:</dt>
<dd> <p> Pressing and releasing the Middle mouse button (or <code>Shift-Insert</code>) in an <code>aterm</code> window causes the current text selection to be inserted as if it had been typed on the keyboard. </p>
 </dd></dl>
<h2>CHANGING FONTS</h2>
<p> You can change fonts on-the-fly, which is to say cycle through the default font and others of various sizes, by using <code>Shift-KP_Add</code> and <code>Shift-KP_Subtract</code>. Or, alternatively (if enabled) with <code>Alt-&gt;</code> and <code>Alt-&lt;</code>, where the actual key can be selected using resources <code>smallfont_key</code>/<code>bigfont_key</code>.  </p>
<h2>LOGIN STAMP</h2>
<p> <code>aterm</code> tries to write an entry into the <i><a href="/docs/linux/man/5-utmp/">utmp</a></i>(5) file so that it can be seen via the <i><a href="/docs/linux/man/1-who/">who</a>(1)</i> command, and can accept messages. To allow this feature, <code>aterm</code> must be installed setuid root on some systems.  </p>
<h2>COLORS AND GRAPHICS</h2>
<p> If graphics support was enabled at compile-time, <code>aterm</code> can be queried with ANSI escape sequences and can address individual pixels instead of text characters. Note the graphics support is still considered beta code. </p>
<p> In addition to the default foreground and background colours, <code>aterm</code> can display up to 16 colours (8 ANSI colours plus high-intensity bold/blink versions of the same). Here is a list of the colours with their <code>rgb.txt</code> names. </p>
<table>
<tr VALIGN=top>
<td><code><code>color0</code> `&nbsp;<wbr>(black) `&nbsp;<wbr>= Black </code>
</td>
</tr>
<tr VALIGN=top>
<td><code>color1</code> `&nbsp;<wbr>(red) `&nbsp;<wbr>= Red3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color2</code> `&nbsp;<wbr>(green) `&nbsp;<wbr>= Green3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color3</code> `&nbsp;<wbr>(yellow) `&nbsp;<wbr>= Yellow3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color4</code> `&nbsp;<wbr>(blue) `&nbsp;<wbr>= Blue3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color5</code> `&nbsp;<wbr>(magenta) `&nbsp;<wbr>= Magenta3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color6</code> `&nbsp;<wbr>(cyan) `&nbsp;<wbr>= Cyan3 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color7</code> `&nbsp;<wbr>(white) `&nbsp;<wbr>= AntiqueWhite 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color8</code> `&nbsp;<wbr>(bright black) `&nbsp;<wbr>= Grey25 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color9</code> `&nbsp;<wbr>(bright red) `&nbsp;<wbr>= Red 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color10</code> `&nbsp;<wbr>(bright green) `&nbsp;<wbr>= Green 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color11</code> `&nbsp;<wbr>(bright yellow) `&nbsp;<wbr>= Yellow 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color12</code> `&nbsp;<wbr>(bright blue) `&nbsp;<wbr>= Blue 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color13</code> `&nbsp;<wbr>(bright magenta) `&nbsp;<wbr>= Magenta 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color14</code> `&nbsp;<wbr>(bright cyan) `&nbsp;<wbr>= Cyan 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>color15</code> `&nbsp;<wbr>(bright white) `&nbsp;<wbr>= White 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>foreground</code> `&nbsp;<wbr> `&nbsp;<wbr>= Black 
</td>
<td>
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>background</code> `&nbsp;<wbr> `&nbsp;<wbr>= White 
</td>
<td>
</td>
<td>
</td>
</tr>
</table>
<p> It is also possible to specify the colour values of <code>foreground</code>, <code>background</code>, <code>cursorColor</code>, <code>cursorColor2</code>, <code>colorBD</code>, <code>colorUL</code> as a number 0-15, as a convenient shorthand to reference the colour name of color0-color15. </p>
<p> Note that <code>-rv</code> (<code>&quot;reverseVideo: True&quot;</code>) simulates reverse video by always swapping the foreground/background colours. This is in contrast to <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) where the colours are only swapped if they have not otherwise been specified. For example, </p>
<dl>
<dt><code>aterm -fg Black -bg White -rv</code></dt>
<dd> <p> would yield White on Black, while on <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) it would yield Black on White. </p>
 </dd></dl>
<h2>ENVIRONMENT</h2>
<p> <code>aterm</code> sets the environment variables <code>TERM</code>, <code>COLORTERM</code> and <code>COLORFGBG</code>. The environment variable <code>WINDOWID</code> is set to the X window id number of the <code>aterm</code> window and it also uses and sets the environment variable <code>DISPLAY</code> to specify which display terminal to use. <code>aterm</code> uses the environment variables <code>ATERMPATH</code>, then <code>RXVTPATH</code> and finally <code>PATH</code> to find XPM files.  </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/utmp</code></dt>
<dd> <p> System file for login records. </p>
 </dd>
<dt><code>/usr/lib/X11/rgb.txt</code></dt>
<dd> <p> Color names. </p>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1), <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1), <i><a href="/docs/linux/man/1-resize/">resize</a></i>(1), <i>X</i>(1), <i>pty</i>(4), <i><a href="/docs/linux/man/4-tty/">tty</a></i>(4), <i><a href="/docs/linux/man/5-utmp/">utmp</a></i>(5) </p>
<p> Cursor change support is not yet implemented. </p>
<p> Click-and-drag doesn&#8217;t work with X11 mouse report overriding. </p>
<p> Graphics support is fairly crude. </p>
<h2>FTP LOCATION</h2>
<p> aterm-0.4.2.tar.gz can be found at the following ftp sites <a href="ftp://ftp.afterstep.org/apps/aterm">ftp://ftp.afterstep.org/apps/aterm</a> </p>
<h2>CURRENT PROJECT COORDINATOR</h2>
<dl>
<dt>Project Coordinator</dt>
<dd> <p> Sasha Vasko <i>&lt;sasha [at] aftercode.net&gt;</i> <br />
 </p>
 </dd>
<dt>Web page maintainter</dt>
<dd> <p> Sasha Vasko <i>&lt;sasha [at] aftercode.net&gt;</i> <br />
 &lt;<a rel="nofollow" href="http://www.afterstep.org/aterm">http://www.afterstep.org/aterm</a>&gt; <br />
 </p>
 </dd>
<dt>Online support</dt>
<dd> <p> You can meet maintainers online, get support, report bugs and make sugestions on <code>AfterStep</code> IRC channel: <i>#afterstep on freenode.net</i>. </p>
 </dd>
<dt>Mailing list</dt>
<dd> <p> Support for <code>aterm</code> can be obtained from <code>AfterStep</code> mailing list <i><a rel="nofollow" href="http://mail.afterstep.org/mailman/listinfo/as-users/">http://mail.afterstep.org/mailman/listinfo/as-users/</a></i>. </p>
 </dd></dl>
<h2>AUTHORS</h2>
<dl>
<dt>John Bovey</dt>
<dd> <p> University of Kent, 1992, wrote the original Xvt. </p>
 </dd>
<dt>Rob Nation <i>&lt;nation [at] rocket.sanders.lockheed.com&gt;</i></dt>
<dd> <p> very heavily modified Xvt and came up with Rxvt </p>
 </dd>
<dt>Angelo Haritsis <i>&lt;ah [at] doc.ic.ac.uk&gt;</i></dt>
<dd> <p> wrote the Greek Keyboard Input </p>
 </dd>
<dt>mj olesen <i>&lt;olesen [at] me.QueensU.CA&gt;</i></dt>
<dd> <p> Wrote the menu system. <br />
 Project Coordinator (changes.txt 2.11 to 2.21) </p>
 </dd>
<dt>Oezguer Kesim <i>&lt;kesim [at] math.fu-berlin.de&gt;</i></dt>
<dd> <p> Project Coordinator (changes.txt 2.21a to 2.4.5) </p>
 </dd>
<dt>Geoff Wing <i>&lt;gcw [at] pobox.com&gt;</i></dt>
<dd> <p> Rewrote screen display and text selection routines. <br />
 Project Coordinator (changes.txt 2.4.6 - ) </p>
 </dd>
<dt>Sasha Vasko <i>&lt;sasha [at] aftercode.net&gt;</i></dt>
<dd> <p> branched rxvt with Alfredo Kojima additions to aterm. <br />
 </p>
 </dd></dl>
