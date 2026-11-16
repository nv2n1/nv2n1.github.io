---
title: "aterm(1)"
name: "aterm"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aterm/"
description: "aterm (Afterstep XVT) – a VT102 emulator for the X window system"
---

<h2>NAME</h2>
<p> aterm (Afterstep XVT) &#8211; a VT102 emulator for the X window system </p>
<h2>SYNOPSIS</h2>
<p> <code>aterm</code> [options] [-e command [ args ]] </p>
<h2>DESCRIPTION</h2>
<p> <code>aterm</code>, version <code>1.0.0</code>, is a colour vt102 terminal emulator, based on <i>rxvt</i> 2.4.8 with Alfredo Kojima&#8217;s additions of fast transparency, intended as an <i><a href="/docs/linux/man/1-xterm/">xterm</a></i>(1) replacement for users who do not require features such as Tektronix 4014 emulation and toolkit-style configurability. As a result, <code>aterm</code> uses much less swap space &#8212; a significant advantage on a machine serving many X sessions. </p>
<p> It was created with <code>AfterStep</code> Window Manger users in mind, but is not tied to any libraries, and can be used anywhere. </p>
<h2>OPTIONS</h2>
<p> The <code>aterm</code> options (mostly a subset of <i>xterm</i>&#8216;s) are listed below. In keeping with the smaller-is-better philosophy, options may be eliminated or default values chosen at compile-time, so options and defaults listed may not accurately reflect the version installed on your system. </p>
<p> Note that <code>aterm</code> permits the resource name to be used as a long-option (&#8211;/++ option) so the potential command-line options are far greater than those listed. For example: `aterm &#8211;loginShell &#8211;color1 Orange&#8217;. </p>
<dl>
<dt><code>-help</code>, <code>&#8211;help</code></dt>
<dd> Print out a message describing available options.</dd>
<dt><code>-version</code>, <code>&#8211;version</code></dt>
<dd> Print out a version with/without list of available options.</dd>
<dt><code>-display</code> <i>displayname</i></dt>
<dd> Attempt to open a window on the named X display (<code>-d</code> still respected). In the absence of this option, the display specified by the <code>DISPLAY</code> environment variable is used.</dd>
<dt><code>-geometry</code> <i>geom</i></dt>
<dd> Window geometry (-g still respected); resource <code>geometry</code>.</dd>
<dt><code>-rv</code>|<code>+rv</code></dt>
<dd> Turn on/off simulated reverse video; resource <code>reverseVideo</code>.</dd>
<dt><code>-bg</code> <i>colour</i></dt>
<dd> Window background colour; resource <code>background</code>.</dd>
<dt><code>-fg</code> <i>colour</i></dt>
<dd> Window foreground colour; resource <code>foreground</code>.</dd>
<dt><code>-pixmap:</code> <i>file[;geom]</i></dt>
<dd> Specify image file for the background and also optionally specify geometry of the image to be cut out of original image, to be used as background, with a geometry string. Note you may need to add quotes to avoid special shell interpretation of the `;&#8217; in the command-line; resource <code>backgroundPixmap</code>.</dd>
<dt><code>-mst:</code> <i>name</i></dt>
<dd> Specify the name of the Afterstep MyStyle to be used as the base of aterm&#8217;s look. ForeColor, BackColor, Font, BackPixmap (all texture options) will be used from MyStyle definition, unless some other command line option is specifyed for the same setting. For example -fn will override MyStyle Font. This is available only if used with AfterStep 1.9.28 or later and if compiled with AfterStep libraries support ( &#8211;enable-afterstep-lib). resource <code>MyStyle</code>.</dd>
<dt><code>-tr</code>|<code>+tr</code></dt>
<dd> Turn on/off pseudo transparency mode. In this mode <code>aterm</code> will use part of root background as it&#8217;s own background, emulating see-through effect; resource <code>transparent</code>.</dd>
<dt><code>-trsb</code>|<code>+trsb</code></dt>
<dd> Turn on/off pseudo transparent scrollbar. Works the same as -tr; resource <code>transpscrollbar</code>.</dd>
<dt><code>-tint</code> <i>color</i></dt>
<dd> Turn on pseudo transparency background tinting. Tinting can be done fast and slow way. In fast way it will be done by combining of background color with tinting color using logical function. This function defaults to AND, and it can be changed using <code>-tinttype</code> option &#8211; see below. In general solid colors like Blue, Red, Green, Cyan, Magenta, Yellow are good, but you should experiment with it for each background you have. True tinting is more memory and CPU hungry &#8211; tinted copy of background image will be created every time you move/resize window. It alows for more smooth tinting thou. You need to build it with <code>&#8211;enable-transparency=yes</code> or <code>&#8211;enable-background-imageyes</code> option, to be able to use this feature. resource <code>tinting</code>.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-sh</code> <i>amount</i></dt>
<dd> This option allows for darkening/lightening of the background image <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 &#8211; image will be darkened. if <i>amount</i> is less then 0 or more then 100 &#8211; image will be lightened. Lightening can cause some strange looking effects if applied on bright image. This option causes aterm to create shaded/lightened copy of the background &#8211; it&#8217;s more memory cosuming as the result. It does not make much difference, though, if applied on non transparent background image. resource <code>shading</code>.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-fade</code> <i>amount</i></dt>
<dd> This option allows for darkening/lightening of colors when aterm is loosing focus. <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 &#8211; colors will be darkened. if <i>amount</i> is less then 0 or more then 100 &#8211; colors will be lightened. Lightening can cause some strange looking effects if applied on bright colors. This option causes aterm to use more colors, as the result it is disabled by default. Use &#8211;enable-fading ./configure option to enable it. resource <code>fading</code>.<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-bgtype</code> <i>type</i></dt>
<dd> Specify type of the transformation to be performed on background image. Possible types are : <code>tile</code> &#8211; plain vanilla tiling of the image. <code>scale</code> &#8211; original image will be scaled to the aterm&#8217;s size, every time you resize window. <code>scalev</code> &#8211; original image will be scaled to the aterm&#8217;s height only, every time you resize window. <code>scaleh</code> &#8211; original image will be scaled to the aterm&#8217;s width only, every time you resize window. <code>center</code> &#8211; original image will be centered in aterm&#8217;s window. <code>notile</code> &#8211; background color will be padded to image&#8217;s right/bottom to make it the same size as window is. <code>notileh</code> &#8211; background color will be padded to image&#8217;s right to make it the same width as window is. <code>notilev</code> &#8211; background color will be padded to image&#8217;s bottom to make it the same height as window is. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code>cut</code> &#8211; aterm background will be cut out of the source image, as if this source image was tiled across the root window. The portion of the image that lies underneath of window will be used. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 If AfterStep Pager, asetroot or Esetroot where used to set the root image, then this option can be used in conjunction with -tr option. In this case it will do mentioned transformations to the root pixmap. and use it as aterm&#8217;s background. resource <code>backgroundType</code>.</dd>
<dt><code>-txttype</code> <i>type</i></dt>
<dd> Allows you to specify logical function to be used when displaying text. That will cause aterm to logically combine text with background pixels. That only works with transparent background and background image. Possible values are : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>; resource <code>textType</code>.</dd>
<dt><code>-tinttype</code> <i>type</i></dt>
<dd> Allows you to specify logical function to be used when tinting transparent background. That will cause aterm to logically combine text with background pixels. NOTE: If shading option is used, or background image is specifyed &#8211; <i>true</i> type will always be used. That works with bpth transparent background and background image. Possible values are :</dd>
<dt>
</dt><dd> Fast tinting options : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>,</dd>
<dt>
</dt><dd> Slow tinting: <i>true</i> &#8211; will do &quot;true&quot; tinting &#8211; that means that background pixel&#8217;s RGB components will be decreased proportionaly to the RGB components of specified tinting color; resource <code>tintingType</code>.</dd>
<dt><code>-cr</code> <i>colour</i></dt>
<dd> The cursor colour; resource <code>cursorColor</code>.</dd>
<dt><code>-pr</code> <i>colour</i></dt>
<dd> The mouse pointer colour; resource <code>pointerColor</code>.</dd>
<dt><code>-bd</code> <i>colour</i></dt>
<dd> The colour of the border between the xterm scrollbar and the text; resource <code>borderColor</code>.</dd>
<dt><code>-bl</code> <i>number</i></dt>
<dd> This option specifies that aterm should askwindow manager to not have a border around term&#8217;s window; resource <code>borderLess</code>.</dd>
<dt><code>-bw</code> <i>number</i></dt>
<dd> This option specifies the width in pixels of the border surrounding the window; resource <code>borderWidth</code>.</dd>
<dt><code>-fn</code> <i>fontname</i></dt>
<dd> Main normal text font; resource <code>font</code>.</dd>
<dt><code>-fb</code> <i>fontname</i></dt>
<dd> Main bold text font; resource <code>boldFont</code>.</dd>
<dt><code>-fm</code> <i>fontname</i></dt>
<dd> Main multicharacter font; resource <code>mfont</code>.</dd>
<dt><code>-ib</code> <i>width</i></dt>
<dd> Width of the internal border in pixels; resource <code>internalBorder</code>.</dd>
<dt><code>-km</code> <i>mode</i></dt>
<dd> Multiple-character font-set encoding mode; <code>eucj</code>: EUC Japanese encoding. <code>sjis</code>: Shift JIS encoding; resource <code>multichar_encoding</code>.</dd>
<dt><code>-grk</code> <i>mode</i></dt>
<dd> Greek keyboard translation; <code>iso</code>: ISO-8859 mapping. <code>ibm</code>: IBM-437 mapping; resource <code>greek_keyboard</code>.</dd>
<dt><code>-name</code> <i>name</i></dt>
<dd> Specify the application name under which resources are to be obtained, rather than the default executable file name. Name should not contain `.&#8217; or `*&#8217; characters. Also sets the icon and title name.</dd>
<dt><code>-ls</code>|<code>+ls</code></dt>
<dd> Start as a login-shell/sub-shell; resource <code>loginShell</code>.</dd>
<dt><code>-ut</code>|<code>+ut</code></dt>
<dd> Inhibit/enable writing a utmp entry; resource <code>utmpInhibit</code>.</dd>
<dt><code>-vb</code>|<code>+vb</code></dt>
<dd> Turn on/off visual bell on receipt of a bell character; resource <code>visualBell</code>.</dd>
<dt><code>-sb</code>|<code>+sb</code></dt>
<dd> Turn on/off scrollbar; resource <code>scrollBar</code>.</dd>
<dt><code>-si</code>|<code>+si</code></dt>
<dd> Turn on/off scroll-to-bottom on TTY output inhibit; resource <code>scrollTtyOutput</code> has opposite effect.</dd>
<dt><code>-sk</code>|<code>+sk</code></dt>
<dd> Turn on/off scroll-to-bottom on keypress; resource <code>scrollKey</code>.</dd>
<dt><code>-sr</code>|<code>+sr</code></dt>
<dd> Put scrollbar on right/left; resource <code>scrollBar_right</code>.</dd>
<dt><code>-st</code>|<code>+st</code></dt>
<dd> Display scrollbar without/with a trough; resource <code>scrollBar_floating</code>.</dd>
<dt><code>-iconic</code></dt>
<dd> Start iconified, if the window manager supports that option.</dd>
<dt><code>-sl</code> <i>number</i></dt>
<dd> Save <i>number</i> lines in the scrollback buffer; resource <code>saveLines</code>.</dd>
<dt><code>-tn</code> <i>termname</i></dt>
<dd> This option specifies the name of the terminal type to be set in the <code>TERM</code> environment variable. This terminal type must exist in the <i><a href="/docs/linux/man/5-termcap/">termcap</a>(5)</i> database and should have <i>li#</i> and <i>co#</i> entries; resource <code>termName</code>.</dd>
<dt><code>-e</code> <i>command [arguments]</i></dt>
<dd> Run the command with its command-line arguments in the <code>aterm</code> window; also sets the window title and icon name to be the basename of the program being executed if neither <i>-title</i> (<i>-T</i>) nor <i>-n</i> are given on the command line. If this option is used, it must be the last on the command-line. If there is no <code>-e</code> option then the default is to run the program specified by the <code>SHELL</code> environment variable or, failing that, <i><a href="/docs/linux/man/1-sh/">sh</a>(1)</i>.</dd>
<dt><code>-title</code> <i>text</i></dt>
<dd> Window title <code>-T</code> still respected); the default title is the basename of the program specified after the 3\-eP option, if any, otherwise the application name; resource <code>title</code>.</dd>
<dt><code>-n</code> <i>text</i></dt>
<dd> Icon name; the default name is the basename of the program specified after the 3\-eP option, if any, otherwise the application name; resource <code>iconName</code>.</dd>
<dt><code>-C</code></dt>
<dd> Capture system console messages.</dd>
</dl>
<h2>RESOURCES (available also as long-options)</h2>
<p> <code>aterm</code> accepts application defaults set in XAPPLOADDIR/aterm (compile-time defined: usually <code>/etc/X11/Xresources/aterm</code>) and resources set in <code>~/.Xdefaults</code> or <code>~/.Xresources</code>. Note that when reading X resources, <code>aterm</code> recognizes two class names: <code>XTerm</code> and <code>Aterm</code>. The class name <code>XTerm</code> allows resources common to both <code>aterm</code> and <i>xterm</i> to be easily configured, while the class name <code>Aterm</code> allows resources unique to <code>aterm</code>, notably colours and key-handling, to be shared between different <code>aterm</code> configurations. If no resources are specified, suitable defaults will be used. Command-line arguments can be used to override resource settings. The following resources are allowed: </p>
<dl>
<dt><code>geometry:</code> <i>geom</i></dt>
<dd> Create the window with the specified X window geometry [default 80&#215;24]; option <code>-geometry</code>.</dd>
<dt><code>background:</code> <i>colour</i></dt>
<dd> Use the specified colour as the window&#8217;s background colour [default White]; option <code>-bg</code>.</dd>
<dt><code>foreground:</code> <i>colour</i></dt>
<dd> Use the specified colour as the window&#8217;s foreground colour [default Black]; option <code>-fg</code>.</dd>
<dt><code>color</code><i>n</i><code>:</code> <i>colour</i></dt>
<dd> Use the specified colour for the colour value <i>n</i>, where 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity (bold = bright foreground, blink = bright background) colours. The canonical names are as follows: 0=black, 1=red, 2=green, 3=yellow, 4=blue, 5=magenta, 6=cyan, 7=white, but the actual colour names used are listed in the <code>COLORS AND GRAPHICS</code> section.</dd>
<dt><code>colorBD:</code> <i>colour</i></dt>
<dd> Use the specified colour to display bold characters when the foreground colour is the default.</dd>
<dt><code>colorUL:</code> <i>colour</i></dt>
<dd> Use the specified colour to display underlined characters when the foreground colour is the default.</dd>
<dt><code>cursorColor:</code> <i>colour</i></dt>
<dd> Use the specified colour for the cursor. The default is to use the foreground colour; option <code>-cr</code>.</dd>
<dt><code>cursorColor2:</code> <i>colour</i></dt>
<dd> Use the specified colour for the colour of the cursor text. For this to take effect, <code>cursorColor</code> must also be specified. The default is to use the background colour.</dd>
<dt><code>reverseVideo:</code> <i>boolean</i></dt>
<dd> <code>True</code>: simulate reverse video by foreground and background colours; option <code>-rv</code>, <code>False</code>: regular screen colours [default]; option <code>+rv</code>. See note in <code>COLORS AND GRAPHICS</code> section.</dd>
<dt><code>scrollColor:</code> <i>colour</i></dt>
<dd> Use the specified colour for the scrollbar [default #B2B2B2].</dd>
<dt><code>troughColor:</code> <i>colour</i></dt>
<dd> Use the specified colour for the scrollbar&#8217;s trough area [default #969696].</dd>
<dt><code>backgroundPixmap:</code> <i>file[;geom]</i></dt>
<dd> Use the specified image file, and cut the area defined by geometry string out of it.</dd>
<dt><code>MyStyle:</code> <i>name</i></dt>
<dd> Specify the name of the Afterstep MyStyle to be used as the base of aterm&#8217;s look. ForeColor, BackColor, Font, BackPixmap (all texture options) will be used from MyStyle definition, unless some other command line option is specifyed for the same setting. For example resource font will override MyStyle Font. This is available only if used with AfterStep 1.9.28 or later and if compiled with AfterStep libraries support ( &#8211;enable-afterstep-lib).</dd>
<dt><code>transparent</code></dt>
<dd> Turn on/off pseudo transparency mode. In this mode <code>aterm</code> will use part of root background as it&#8217;s own background, emulating see-through effect;</dd>
<dt><code>tinting:</code> <i>color</i></dt>
<dd> Turn on pseudo transparency background tinting. Tinting can be done fast and slow way. In fast way it will be done by combining of background color with tinting color using logical function. This function defaults to AND, and it can be changed using <code>-tinttype</code> option &#8211; see below. In general solid colors like Blue, Red, Green, Cyan, Magenta, Yellow are good, but you should experiment with it for each background you have. True tinting is more memory and CPU hungry &#8211; tinted copy of background image will be created every time you move/resize window. It alows for more smooth tinting thou. You need to build it with <code>&#8211;enable-transparency=yes</code> or <code>&#8211;enable-background-image=yes</code> option, to be able to use this feature.</dd>
<dt><code>-shading:</code> <i>amount</i></dt>
<dd> This option allows for darkening/lightening of the background image <i>amount</i> is the %value of the desired brightness, where 100 is the original. if <i>amount</i> is less then 100 &#8211; image will be darkened. if <i>amount</i> is less then 0 or more then 100 &#8211; image will be lightened. Lightening can cause some strange looking effects if applied on bright image. This option causes aterm to create shaded/lightened copy of the background &#8211; it&#8217;s more memory cosuming as the result. It does not make much difference, though, if applied on non transparent background image.</dd>
<dt><code>backgroundType:</code> <i>type</i></dt>
<dd> Specify type of the transformation to be performed on background image. Possible types are : <code>tile</code> &#8211; plain vanilla tiling of the image. <code>scale</code> &#8211; original image will be scaled to the aterm&#8217;s size, every time you resize window. <code>scalev</code> &#8211; original image will be scaled to the aterm&#8217;s height only, every time you resize window. <code>scaleh</code> &#8211; original image will be scaled to the aterm&#8217;s width only, every time you resize window. <code>center</code> &#8211; original image will be centered in aterm&#8217;s window. <code>notile</code> &#8211; background color will be padded to image&#8217;s right/bottom to make it the same size as window is. <code>notileh</code> &#8211; background color will be padded to image&#8217;s right to make it the same width as window is. <code>notilev</code> &#8211; background color will be padded to image&#8217;s bottom to make it the same height as window is. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 <code>cut</code> &#8211; aterm background will be cut out of the source image, as if this source image was tiled across the root window. The portion of the image that lies underneath of window will be used. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 If AfterStep Pager, asetroot or Esetroot where used to set the root image, then this option can be used in conjunction with -tr option. In this case it will do mentioned transformations to the root pixmap. and use it as aterm&#8217;s background.</dd>
<dt><code>textType:</code> <i>type</i></dt>
<dd> Allows you to specify logical function to be used when displaying text. That will cause aterm to logically combine text with background pixels. That only works with transparent background and background image. Possible values are : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>.</dd>
<dt><code>tintingType</code> <i>type</i></dt>
<dd> Allows you to specify logical function to be used when tinting transparent background. That will cause aterm to logically combine text with background pixels. NOTE: If shading option is used, or background image is specifyed &#8211; <i>true</i> type will always be used. That works with bpth transparent background and background image. Possible values are :</dd>
<dt>
</dt><dd> Fast tinting options : <i>and</i>, <i>andReverse</i>, <i>andInverted</i>, <i>xor</i>, <i>or</i>, <i>nor</i>, <i>invert</i>, <i>equiv</i>, <i>invert</i>, <i>orReverse</i>, <i>orInverted</i>, <i>nand</i>,</dd>
<dt>
</dt><dd> Slow tinting: <i>true</i> &#8211; will do &quot;true&quot; tinting &#8211; that means that background pixel&#8217;s RGB components will be decreased proportionaly to the RGB components of specified tinting color.</dd>
<dt><code>menu:</code> <i>file[;tag]</i></dt>
<dd> Read in the specified menu file (note the `.menu&#8217; extension is optional) and also optionally specify a starting tag to find. See the reference documentation for details on the syntax for the menuBar.</dd>
<dt><code>path:</code> <i>path</i></dt>
<dd> Specify the colon-delimited search path for finding files (XPM and menus), in addition to the paths specified by the <code>RXVTPATH</code> and <code>PATH</code> environment variables.</dd>
<dt><code>font:</code> <i>fontname</i></dt>
<dd> Select the main text font used [default 7&#215;14]; option <code>-fn</code>.</dd>
<dt><code>font</code><i>n</i><code>:</code> <i>fontname</i></dt>
<dd> Specify the alternative font <i>n</i>. The default font values: </dd>
<dl>
<dl>
<dt>
</dt><dd>
<table>
<tr VALIGN=top>
<td><code><code>font</code>: `&nbsp;<wbr>7&#215;14 </code>
</td>
</tr>
<tr VALIGN=top>
<td><code>font1</code>: `&nbsp;<wbr>6&#215;10
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font2</code>: `&nbsp;<wbr>6&#215;13
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font3</code>: `&nbsp;<wbr>8&#215;13
</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>font4</code>: `&nbsp;<wbr>9&#215;15
</td>
<td>
</td>
</tr>
</table>
</dd></dl>
</dl>
<dt><code>boldFont:</code> <i>fontname</i></dt>
<dd> Specify the name of the bold font to use if <code>colorBD</code> has not been specified and it is not possible to map the default foreground colour to colour 8-15 [default NONE]. This font must be the same height and width as the normal font; option <code>-fb</code>.</dd>
<dt><code>mfont:</code> <i>fontname</i></dt>
<dd> Select the main multiple-character text font used [default k14]; option <code>-fk</code>.</dd>
<dt><code>mfont</code><i>n</i><code>:</code> <i>fontname</i></dt>
<dd> Specify the alternative multiple-character font <i>n</i>. If compiled for multiple-character fonts, the Roman and multiple-character font sizes should match.</dd>
<dt><code>multichar_encoding:</code> <i>mode</i></dt>
<dd> Set the encoding mode to be used when multicharacter encoding is received; <code>eucj</code>: EUC Japanese encoding [default for Kanji]. <code>sjis</code>: Shift JIS encoding. <code>big5</code>: BIG5 encoding; option <code>-km</code>.</dd>
<dt><code>greek_keyboard:</code> <i>mode</i></dt>
<dd> Set the Greek keyboard translation mode to be used; <code>iso</code>: ISO-8859 mapping (elot-928) [default]. <code>ibm</code>: IBM-437 mapping (DOS codepage 737); option <code>-grk</code>. Use <code>Mode_switch</code> to toggle keyboard input. For more details, see the distributed file <code>README.greek</code>.</dd>
<dt><code>title:</code> <i>text</i></dt>
<dd> Set window title string, the default title is the command-line specified after the <code>-e</code> option, if any, otherwise the application name; option <code>-title</code>.</dd>
<dt><code>iconName:</code> <i>text</i></dt>
<dd> Set the name used to label the window&#8217;s icon or displayed in an icon manager window, it also sets the window&#8217;s title unless it is explicitly set; option <code>-n</code>.</dd>
<dt><code>mapAlert:</code> <i>boolean</i></dt>
<dd> <code>True</code>: de-iconify (map) on receipt of a bell character. <code>False</code>: no de-iconify (map) on receipt of a bell character [default].</dd>
<dt><code>visualBell:</code> <i>boolean</i></dt>
<dd> <code>True</code>: use visual bell on receipt of a bell character; option <code>-vb</code>. <code>False</code>: no visual bell [default]; option <code>+vb</code>.</dd>
<dt><code>loginShell:</code> <i>boolean</i></dt>
<dd> <code>True</code>: start as a login shell by prepending a `-&#8216; to <code>argv[0]</code> of the shell; option <code>-ls</code>. <code>False</code>: start as a normal sub-shell [default]; option <code>+ls</code>.</dd>
<dt><code>utmpInhibit:</code> <i>boolean</i></dt>
<dd> <code>True</code>: inhibit writing record into the system log file <code>utmp</code>; option <code>-ut</code>. <code>False</code>: write record into the system log file <code>utmp</code> [default]; option <code>+ut</code>.</dd>
<dt><code>print-pipe:</code> <i>string</i></dt>
<dd> Specify a command pipe for vt100 printer [default <i><a href="/docs/linux/man/1-lpr/">lpr</a>(1)</i>]. Use <code>Print</code> to initiate a screen dump to the printer and <code>Ctrl-Print</code> or <code>Shift-Print</code> to include the scrollback as well.</dd>
<dt><code>scrollBar:</code> <i>boolean</i></dt>
<dd> <code>True</code>: enable the scrollbar [default]; option <code>-sb</code>. <code>False</code>: disable the scrollbar; option <code>+sb</code>. Note that the scrollbar type (with/without arrows) is compile-time selected.</dd>
<dt><code>smallfont_key:</code> <i>keysym</i></dt>
<dd> If enabled, use <code>Alt-</code><i>keysym</i> to toggle to a smaller font [default <code>Alt-&lt;</code>]</dd>
<dt><code>bigfont_key:</code> <i>keysym</i></dt>
<dd> If enabled, use <code>Alt-</code><i>keysym</i> to toggle to a bigger font [default <code>Alt-&gt;</code>]</dd>
<dt><code>saveLines:</code> <i>number</i></dt>
<dd> Save <i>number</i> lines in the scrollback buffer [default 64]; option <code>-sl</code>.</dd>
<dt><code>termName:</code> <i>termname</i></dt>
<dd> Specifies the terminal type name to be set in the <code>TERM</code> environment variable; option <code>-tn</code>.</dd>
<dt><code>meta8:</code> <i>boolean</i></dt>
<dd> <code>True</code>: handle Meta (Alt) + keypress to set the 8th bit. <code>False</code>: handle Meta (Alt) + keypress as an escape prefix [default].</dd>
<dt><code>modifier:</code> <i>string</i></dt>
<dd> Set the Meta key to be enabled by modifier <code>Mod1</code>, <code>Mod2</code>, <code>Mod3</code>, <code>Mod4</code> or <code>Mod5</code>.</dd>
<dt><code>backspacekey:</code> <i>string</i></dt>
<dd> The string to send when the backspace key is pressed. If set to <code>DEC</code> or unset it will send <code>Delete</code> (code 127) or, if shifted, <code>Backspace</code> (code 8) &#8211; which can be reversed with the appropriate DEC private mode escape sequence.</dd>
<dt><code>deletekey:</code> <i>string</i></dt>
<dd> The string to send when the delete key (not the keypad delete key) is pressed. If unset it will send the sequence traditionally associated with the <code>Execute</code> key.</dd>
<dt><code>cutchars:</code> <i>string</i></dt>
<dd> The characters used as delimiters for double-click word selection. The built-in default:<br />
 <code>BACKSLASH `&quot;&#8217;&amp;()*,;&lt;=&gt;?@[]{|}</code></dd>
<dt><code>keysym.</code><i>sym</i>: <i>string</i></dt>
<dd> Associate <i>string</i> with keysym <i>sym</i> (<code>0xFF00 &#8211; 0xFFFF</code>). It may contain escape values (: bell, : backspace, , \E: escape, 
: newline, 
: return, 	: tab, 
</dd></dl>