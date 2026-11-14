---
title: "mrxvt(1)"
name: "mrxvt"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrxvt/"
description: "mrxvt – A tabbed VT102 terminal emulator for X Window System"
---

<h2>NAME</h2>
<p> <code>mrxvt</code> &#8211; A tabbed VT102 terminal emulator for X Window System</p>
<h2>SYNOPSIS</h2>
<p> [options] [-<code>e </code><i>cmd</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The program is a terminal emulator for X Window System. It provides <code>DEC VT102</code> compatible terminals for programs that cannot use the window system directly. </p>
<p> is based on <a href="/docs/linux/man/1-rxvt/">rxvt</a>(1) version 2.7.11 CVS, and features most of functionality of rxvt, with a few major enhancements (namely multiple tabs, and transparency). Like rxvt, aims to be light, fast, flexible and desktop independent, thus KDE or GNOME are not required. </p>
<p> The primary features of include (but are not limited to) multiple tabs, dynamically changeable tab titles, customisable command for each tab, input broadcasting, true translucent window, fast pseudo transparency with tinting, user supplied background images (XPM, JPEG, PNG), off-focus fading, text shadow, multiple style (NeXT, Rxvt, Xterm, SGI, Plain) scrollbars, XIM, multi-language support (Chinese, Korean, Japanese), freetype font and logging. </p>
<p> The default behaviour can be set using the resource configuration file ~/.mrxvtrc For backward compatibility, if ~/.mrxvtrc is not found, tries to load configuration settings from the files ~/.Xdefaults or ~/.Xresources Alternately, you can specify which config file to load using the &#8211;<code>cf</code> command line option.</p>
<h2>OPTIONS</h2>
<p> This section describes the commandline options accepts. To disable an option, prefix it with an `<i>+</i> &#8216; instead of a `<i>&#8211;</i> &#8216; Most options can be set from your ~/.mrxvtrc file using the option name listed in brackets as [<code>option_name</code> ] The option name can also be used as a &quot;long option&quot; from the command line (i.e. by prefixing it with `<i>&#8212;</i> &#8216; or `<i>++</i> &#8216; as appropriate. For example </p>
<pre>
mrxvt -tr -shade 85 +trt
</pre>
<p> is the same as </p>
<pre>
mrxvt --transparent --shading 85 ++transparentTabbar
</pre>
<p> which is the same as putting the lines </p>
<pre>
Mrxvt.transparent:              True
Mrxvt.shading:                  85
Mrxvt.transparentTabbar:        False
</pre>
<p> in your ~/.mrxvtrc </p>
<p> All options are case sensitive. Some options are similar to those of other terminals, so if you find the explanation given here insufficient, we strongly recommend you look in the <a href="/docs/linux/man/1-rxvt/">rxvt</a>(1) and <a href="/docs/linux/man/1-xterm/">xterm</a>(1) manpages.</p>
<h3>Terminal name and display options</h3>
<dl>
<dt><code>-display | -d </code><i>displayname</i></p>
<dd> X display name, the X server to contact</p>
<dt><code>-geometry | -g </code><i>geometry</i></p>
<dd> geometry at startup [<code>geometry</code> ]</p>
<dt><code>-ic </code><i>file </i>[<code>; </code><i>geometry</i> ]</p>
<dd> application icon file. [appIcon]</p>
<dt><code>-iconic | +iconic</code></p>
<dd> start iconic [<code>iconic</code> ]</p>
<dt><code>-in </code><i>name</i></p>
<dd> Icon name for window [<code>iconName</code> ]</p>
<dt><code>-into </code><i>WinID</i></p>
<dd> If given an X window identifier, will reparent its top-level shell widget to that window. This is used to embed within other applications.</p>
<dt><code>-name </code><i>name</i></p>
<dd> Client instance, icon, and title strings [<code>clientName</code> ]</p>
<dt><code>-title </code><i>string</i></p>
<dd> title name of the window [<code>title</code> ]</p>
<dt><code>-tn </code><i>termname</i></p>
<dd> The type of terminal should emulate. The value of the TERM environment variable is set to this value for all child processes launched by <code>.</code> Note that rxvt and most rxvt clones including <code>,</code> have slightly different terminal capabilities than those of <a href="/docs/linux/man/1-xterm/">xterm</a>(1). Thus will not always work properly with the terminal set to <i>xterm</i> and we recommend setting this value to <i>rxvt</i> instead. However some systems have incorrect (or even missing) <a href="/docs/linux/man/1-terminfo/">terminfo</a>(1) or <a href="/docs/linux/man/1-termcap/">termcap</a>(1) entries for the terminal <i>rxvt</i> If you experience problems with this, the ideal solution would be to correct your systems termcap and terminfo entries. If you are unable to do that, then you can try setting your terminal to <i>xterm</i> and hope everything works properly. [<code>termName</code> ]</dl>
<h3>Transparency related options</h3>
<dl>
<dt><code>-o </code><i>%d</i></p>
<dd> Translucent window (true transparent) background opacity degree. <i>%d</i> is an integer between 0 and 100. This option needs translucent support by the X server, e.g., Xorg 6.8, and overrides the pseudo-transparency. [<code>opacity</code> ]</p>
<dt><code>-od %d</code></p>
<dd> Translucent window opacity degree increase/decrease interval. <i>%d</i> is an integer between 0 and 100 [<code>opacityDegree</code> ]</p>
<dt><code>-tr | +tr</code></p>
<dd> Enable / disable background pseudo-transparency. To use this feature you must set your desktop wallpaper using an Esetroot compatible program ( i.e. a program that publishes the wallpaper using the <code>_XROOTPMAP_ID</code> atom). Some programs that will do this are <a href="/docs/linux/man/1-esetroot/">Esetroot</a>(1), <a href="/docs/linux/man/1-feh/">feh</a>(1), fvwm-root1 with the `<code>&#8211;retain-pixmap</code> &#8216; option, or KDE. Note: To use your precious <code>backgroundFade , tinting</code> or <code>shading</code> options, you MUST set the desktop wallpaper in an Esetroot way. [<code>transparent</code> ]</p>
<dt><code>-trf | +trf</code></p>
<dd> If you choose NOT to set the background in an Esetroot compatible way, then you can still have transparency using this option. (You must also enable the <code>transparent</code> option). Background changes made by FvwmBacker, xsetbg (xli) or Esetroot compatible programs, will be automatically detected. However changes made by <a href="/docs/linux/man/1-xv/">xv</a>(1), <a href="/docs/linux/man/1-xsetroot/">xsetroot</a>(1) or other non-Esetroot compatible programs will not be detected. If you&#8217;re hell bent on non-Esetroot compatible programs to set your background, then do something like </p>
<pre>
xsetroot -solid &quot;#202040&quot; &amp;&amp; fvwm-root -d
</pre>
<p> Note: To use your precious <code>backgroundFade , tinting</code> or <code>shading</code> options, you MUST set the desktop wallpaper in an Esetroot way. [<code>transparentForce</code> ]</p>
<dt><code>-trm | +trm</code></p>
<dd> Enable / disable pseudo-transparent menubar. Pseudo-transparency must be turned on. [<code>transparentMenubar</code> ]</p>
<dt><code>-trs | +trs</code></p>
<dd> Enable / disable pseudo-transparent scrollbar. Pseudo-transparency must be turned on. [<code>transparentScrollbar</code> ]</p>
<dt><code>-trt | +trt</code></p>
<dd> Enable / disable pseudo-transparent tabbar. Pseudo-transparency must be turned on. [<code>transparentTabbar</code> ]</dl>
<h3>Background image related options</h3>
<dl>
<dt><code>-mbpixmap </code><i>file </i>[<code>; </code><i>geometry</i> ]</p>
<dd> Menubar background image. Pseudo-transparency must be turned off. [<code>menubarPixmap</code> ]</p>
<dt><code>-pixmap </code><i>file </i>[<code>; </code><i>geometry</i> ]</p>
<dd> Background image for all terminals if not set individually. Pseudo-transparency must be turned off. [<code>Pixmap</code> ]</p>
<dt><code>-sbpixmap </code><i>file </i>[<code>; </code><i>geometry</i> ]</p>
<dd> Scrollbar background image. Pseudo transparency must be turned off. [<code>scrollbarPixmap</code> ]</p>
<dt><code>-tbpixmap </code><i>file </i>[<code>; </code><i>geometry</i> ]</p>
<dd> Tabbar background image. Pseudo transparency must be turned off. [<code>tabbarPixmap</code> ]</p>
<dt><code>-tupixmap | +tupixmap</code></p>
<dd> Apply tabbar background image to tabs. [<code>tabUsePixmap</code> ]</dl>
<h3>Scrolling related options</h3>
<dl>
<dt><code>-mp | +mp</code></p>
<dd> scroll one page when press mouse wheel button [<code>mouseWheelScrollPage</code> ]</p>
<dt><code>-sa </code><i>mode</i></p>
<dd> Scrollbar alignment ( <i>top | bottom</i> [<code>scrollbarAlign</code> ]</p>
<dt><code>-sb | +sb</code></p>
<dd> Hide / show scrollbar [<code>scrollBar</code> ]</p>
<dt><code>-sbt </code><i>width</i></p>
<dd> Scrollbar thickness/width [<code>scrollbarThickness</code> ]</p>
<dt><code>-si | +si</code></p>
<dd> Inhibit scrolling on tty output. [<code>scrollTtyOutputInhibit</code> ]</p>
<dt><code>-sk | +sk</code></p>
<dd> scroll-on-keypress [<code>scrollTtyKeypress</code> ]</p>
<dt><code>-sl </code><i>n</i></p>
<dd> The number of scrolled lines to save (for all tabs) if not set individually. The maximal number of saved lines is 65535. [<code>saveLines</code> ]</p>
<dt><code>-sr | +sr</code></p>
<dd> Scrollbar on right [<code>scrollbarRight</code> ]</p>
<dt><code>-ss </code><i>mode</i></p>
<dd> Scrollbar style. <i>mode</i> should be one of <i>plain , xterm , rxvt , next</i> or <i>sgi</i> [<code>scrollbarStyle</code> ]</p>
<dt><code>-st | +st</code></p>
<dd> Draw floating scrollbar (i.e. without a trough). [<code>scrollbarFloating</code> ]</dl>
<h3>Color related options</h3>
<dl>
<dt><code>-bg </code><i>color</i></p>
<dd> Background color [<code>background</code> ]</p>
<dt><code>-bd </code><i>color</i></p>
<dd> Border color [<code>borderColor</code> ]</p>
<dt><code>-bgfade </code><i>%d</i></p>
<dd> (Obsolete) Make colors <i>%d</i> darker for background image or pseudo-transparent background. <i>%d</i> is an integer between 0 and 100. This is like tinting the background with black. This option is obsolete, and you should use the <code>tint</code> and <code>shade</code> options instead. [<code>backgroundFade</code> ]</p>
<dt><code>-bgtype </code><i>type</i></p>
<dd> Transformation type for background pixmap (not implemented yet)</p>
<dt><code>-cr </code><i>color</i></p>
<dd> color of cursor [<code>cursorColor</code> ]</p>
<dt><code>-fade </code><i>%d</i></p>
<dd> Make colors <i>%d</i> darker when mrxvt looses focus. <i>%d</i> is an integer between 0 and 100 [<code>fading</code> ]</p>
<dt><code>-fg </code><i>color</i></p>
<dd> Foreground color. [<code>foreground</code> ]</p>
<dt><code>-itabbg </code><i>color</i></p>
<dd> Background color of inactive tabs and tabbar. [<code>itabBackground</code> ]</p>
<dt><code>-itabfg </code><i>color</i></p>
<dd> Foreground color of inactive tabs. [<code>itabForeground</code> ]</p>
<dt><code>-pr </code><i>color</i></p>
<dd> color of pointer [<code>pointerColor</code> ]</p>
<dt><code>-shade </code><i>%d</i></p>
<dd> Shade background to <i>%d</i> degree when tinting the background. <i>%d</i> is an integer between 0 and 100. You must also define a color using the <code>tint</code> option. When compiled with XRender support, the tabbar, menubar and scroll bar are tinted with their respective background colors for pseudo-transparent terminals. [<code>shading</code> ]</p>
<dt><code>-tabbg </code><i>color</i></p>
<dd> background color of active tab. [<code>tabBackground</code> ]</p>
<dt><code>-tabfg </code><i>color</i></p>
<dd> Foreground color of tabbar [<code>tabForeground</code> ]</p>
<dt><code>-tint </code><i>color</i></p>
<dd> Color tinted on background image or pseudo-transparent background. This works differently depending on the tint type: With XRender (when compiled with &#8211;enable-xrender), <i>color</i> is the color you want to tint your background to. The brighter the color, the less transparent it will be (regardless of the shade degree specified by &#8211;<code>shade )</code> For example, if you want your background tinted black, set <i>color</i> to `#000000&#8242; however if you want a white tinted transparent background, set <i>color</i> to some level of grey (e.g. `#808080&#8242; but NOT to `#ffffff&#8217; </p>
<p> When compiled without XRender support, <i>color</i> works like a color mask. Thus if you want a black tinted background, set <i>color</i> to `#ffffff&#8217; </p>
<p> The shade degree (using &#8211;<code>shade</code> must be defined as well. [<code>tintColor</code> ]</p>
<dt><code>-tinttype </code><i>type</i></p>
<dd> Function applied for background tinting (not implemented yet).</p>
<dt><code>-ts </code><i>color</i></p>
<dd> color of text shadow [<code>textShadow</code> ]</p>
<dt><code>-tsm </code><i>mode</i></p>
<dd> Text shadow mode, specify shadow position of text: <i>left | right | top | bottom | topleft | topright | botleft | botright | none</i> [<code>textShadowMode</code> ]</p>
<dt><code>-txttype type</code></p>
<dd> Function applied for text drawing (not implemented yet)</p>
<dt><code>-ufbg </code><i>color</i></p>
<dd> Default background color when the terminal window looses focus. [<code>ufBackground</code> ]</dl>
<h3>Font related options</h3>
<dl>
<dt><code>-fb </code><i>fontname</i></p>
<dd> bold text X11 font name [<code>boldFont</code> ]</p>
<dt><code>-fm </code><i>fontname</i></p>
<dd> multichar text X11 font name [<code>mfont</code> ]</p>
<dt><code>-fn </code><i>fontname</i></p>
<dd> normal text X11 font name [<code>font</code> ]</p>
<dt><code>-xft | +xft</code></p>
<dd> Use freetype font instead of X11 font. This option controls all other freetype font related options. [<code>xft</code> ]</p>
<dt><code>-xftaa | +xftaa</code></p>
<dd> Enable / disable antialiasing of freetype font. This makes font look much nicer, but significantly slows down the rendering speed. The &#8211;<code>xft</code> option must be enabled. [<code>xftAntialias</code> ]</p>
<dt><code>-xftah | +xftah</code></p>
<dd> Enable / disable autohint of freetype font. The &#8211;<code>xft</code> option must be enabled [<code>xftAutoHint</code> ]</p>
<dt><code>-xftfm </code><i>fontname</i></p>
<dd> Multichar text freetype font family. The &#8211;<code>xft</code> option must be enabled [<code>xftmFont</code> ]</p>
<dt><code>-xftfn </code><i>fontname</i></p>
<dd> Normal text freetype font family. The &#8211;<code>xft</code> option must be enabled [<code>xftFont</code> ]</p>
<dt><code>-xftga | +xftga</code></p>
<dd> Enable / disable global advance of freetype font. The &#8211;<code>xft</code> option must be enabled [<code>xftGlobalAdvance</code> ]</p>
<dt><code>-xftht | +xftht</code></p>
<dd> Enable / disable hinting of freetype font. The &#8211;<code>xft</code> option must be enabled [<code>xftHinting</code> ]</p>
<dt><code>-xftmsz </code><i>size</i></p>
<dd> Freetype multichar font size in pixels. The &#8211;<code>xft</code> option must be enabled. [<code>xftmSize</code> ]</p>
<dt><code>-xftnfm | +xftnfm</code></p>
<dd> Do not load freetype mfont, but use freetype font instead. This can avoid a large line space if the size of font and mfont are very different. The &#8211;<code>xft</code> option must be enabled [<code>xftNomFont</code> ]</p>
<dt><code>-xftpfn </code><i>font</i></p>
<dd> Specify a proportionally spaced font to use for drawing tab-titles. If set, the tab bar behaves like Firefox&#8217;s tab-bar: All tabs have the same width, and the widths are shrunk / expanded to keep the number of tabs specified by <code>minVisibleTabs</code> visible. The active tab title is drawn in a bold font. (Your colors are still used). [<code>xftPFont</code> ]</p>
<dt><code>-xftrgb </code><i>style</i></p>
<dd> Freetype font sub-pixel order: <i>rgb | bgr | vrgb | vbgr | none</i> The &#8211;<code>xft</code> option must be enabled. [<code>xftRGBA</code> ]</p>
<dt><code>-xftslow | +xftslow</code></p>
<dd> Display freetype multichar string in slow mode for better display effect. The xft option must be enabled. [<code>xftSlowOutput</code> ]</p>
<dt><code>-xftst </code><i>style</i></p>
<dd> Freetype font slant: <i>roman | italic | oblique</i> The &#8211;<code>xft</code> option must be enabled. [<code>xftSlant</code> ]</p>
<dt><code>-xftsz </code><i>number</i></p>
<dd> Freetype font size in pixel. The &#8211;<code>xft</code> option must be enabled [<code>xftSize</code> ]</p>
<dt><code>-xftbwt </code><i>style</i></p>
<dd> Freetype bold font weight: <i>light | medium | demibold | bold | black</i> The &#8211;<code>xft</code> option must be enabled. [<code>xftBoldWeight</code> ]</p>
<dt><code>-xftwd </code><i>style</i></p>
<dd> Freetype font width: <i>ultracondensed | condensed | normal | expanded | ultraexpanded</i> The &#8211;<code>xft</code> option must be enabled. [<code>xftWidth</code> ]</p>
<dt><code>-xftwt </code><i>style</i></p>
<dd> Freetype font weight: <i>light | medium | demibold | bold | black</i> The &#8211;<code>xft</code> option must be enabled. [<code>xftWeight</code> ]</dl>
<h3>Tabs and command related options</h3>
<dl>
<dt><code>-aht</code></p>
<dd> Automatically hide or show the tab bar depending on the number of tabs. On startup, the tabbar is shown only if there are more than one tabs present. If there is only one tab, and a new one is created, then the tabbar is shown. If there are two tabs and one is closed, then the tabbar is hidden. A keyboard shortcut used at any time to hide / show the tabbar. [<code>autohideTabbar</code> ]</p>
<dt><code>-at | +at</code></p>
<dd> Run command specified with &#8211;<code>e</code> on all tabs (by default the command specified by &#8211;<code>e</code> is only used for the first tab opened). This causes the profile option <code>command</code> to be ignored. However a command specified via the <code>NewTab</code> macro is honored. [<code>cmdAllTabs</code> ]</p>
<dt><code>-bt | +bt</code></p>
<dd> Show tabbar at bottom. [<code>bottomTabbar</code> ]</p>
<dt><code>-e </code>[<i>arguments &#8230;</i> ]</p>
<dd> Specifies the program (and its command line arguments) to be run in the window. By default this command is only run initially, and all tabs created after startup will run the default shell (or program supplied by &#8211;<code>profile </code><i>%d </i><code>). This behaviour can be overridden with the</code> &#8211;<code>at</code> option. [<code>command</code> ]</p>
<dt><code>-hb | +hb</code></p>
<dd> Hide buttons in the tabbar. [<code>hideButtons</code> ]</p>
<dt><code>-het </code><i>string</i></p>
<dd> Message to display in tabs after the child process exits. (This string is escape and percent interpolated). [<code>holdExitText</code> ]</p>
<dt><code>-heT </code><i>string</i></p>
<dd> Set the title of tabs to <i>string</i> after the process in the tab exits. (This string is escape and percent interpolated). [<code>holdExitTitle</code> ]</p>
<dt><code>-hold </code><i>mask</i></p>
<dd> Hold the tab open after the child process in it exits. <i>mask</i> is the mask of flags which control weather the tab will be held open based on the exit status of the child process. If the lowest bit (0x01) of <i>mask</i> is set, then the tab will always be held open after the child exits. If the next bit (0x02) is set, then the tab will only be held open if the child exits abnormally (e.g. via <a href="/docs/linux/man/1-abort/">abort</a>(1)). If the third bit (0x04) is set, then the tab will be held open if the child exits with non-zero status. </p>
<p> NOTE: In previous versions of this was a boolean option. For backward compatibility, the value of <i>True , On, Yes</i> will be treated as <i>1</i> and anything illegal will be treated as <i>0</i> The default is 0x06. [<code>holdExit</code> ]</p>
<dt><code>-ht | +ht</code></p>
<dd> Hide tabbar on initialization [<code>hideTabbar</code> ]</p>
<dt><code>-htb | +htb</code></p>
<dd> Highlight inactive tabs only when bell sounds. Default is to highlight inactive tabs whenever they produce output. [<code>highlightTabOnBell</code> ]</p>
<dt><code>-ip </code><i>profiles</i></p>
<dd> <i>profiles</i> is a comma separated list of profiles numbers. On startup opens each of these profiles in a tab. [<code>initProfileList</code> ]</p>
<dt><code>-ls | +ls</code></p>
<dd> Indicates that the shell that is started in the window will be a login shell (i.e., the first character of argv[0] will be a dash, indicating to the shell that it should read the user&#8217;s .login or .profile). [<code>loginShell</code> ]</p>
<dt><code>-mtw </code><i>width</i></p>
<dd> The maximum width (in characters) of the displayed tabs. This can not be larger than 40. If you use Xft, then you might want to use the <code>minVisibleTabs</code> option instead. [<code>maxTabWidth</code> ]</p>
<dt><code>-mvt </code><i>n</i></p>
<dd> When using <code>xftPFont</code> to display tabs, keep at least <i>n</i> tabs visible. [<code>minVisibleTabs</code> ]</p>
<dt><code>-profile </code><i>N </i><code>. </code><i>option value</i></p>
<dd> Set <i>option</i> to <i>value</i> in profile <i>N</i> When a new tab is created with profile <i>N</i> it uses all options that are set for this profile. Currently the only options that can be set per profile are <code>Pixmap , background , command , foreground , saveLines , holdExit , holdExitText , holdExitTitle , tabTitle , titleFormat , winTitleFormat</code> and <code>workingDirectory</code> Then all the settings from that profile number are used. </p>
<p> <i>N</i> can be any integer between 0 and the compiled in maximum (default 5). The profile number 0 is special, and contains default settings which are used for all profiles where this option is not set (e.g. &#8211;<code>profile0.tt </code><i>mrxvt</i> sets the tab title to <i>mrxvt</i> for all profiles where the tab title has not been set). In this case the &#8211;<code>profile0.</code> can be omitted entirely (i.e. &#8211;<code>profile0.tt</code> is equivalent to &#8211;<code>tt )</code> </p>
<p> This option is intended to replace the &#8211;<code>vt </code><i>%d </i><code>.xx</code> options from version 0.5.0. The old &#8211;<code>vt </code><i>%d </i><code>.xx</code> would set options for the <i>%d </i><code>th</code> tab. This causes inconsistent behaviour when the user moves / closes tabs. The behaviour of the &#8211;<code>profile</code> option is to set options for a particular profile, and then these settings can be associated (on demand) to newly created tabs. [<code>profile </code><i>N </i><code>. </code><i>option</i> ]</p>
<dt><code>-ps | +ps</code></p>
<dd> Protect tab from being closed if it is using the secondary screen, for example, when the user is running <a href="/docs/linux/man/1-vim/">vim</a>(1) or <a href="/docs/linux/man/1-mutt/">mutt</a>(1), this can prevent the terminal from being accidentally closed. [<code>protectSecondary</code> ]</p>
<dt><code>-sti | +sti</code></p>
<dd> Synchronize icon name with tab title when switch to a new tab or the title of the active tab changes. [<code>syncTabIcon</code> ]</p>
<dt><code>-stt | +stt</code></p>
<dd> Synchronize terminal title with tab title when switch to a new tab or the title of the active tab changes. (See also the &#8211;<code>wtf</code> option). [<code>syncTabTitle</code> ]</p>
<dt><code>-tnum </code><i>N</i></p>
<dd> OBSOLETE. Opens <i>N</i> tabs on startup. For backward compatibility, the tabs are opened with profile 0, 1, &#8230; <i>N </i><code>-1</code> [<code>initTermNumber</code> ]</p>
<dt><code>-tt </code><i>string</i></p>
<dd> Title of the tab [<code>tabTitle</code> ]</p>
<dt><code>-tf </code><i>format</i></p>
<dd> If set, this controls the displayed title of each tab. <i>format</i> is % interpolated, and the result is displayed as the tab title. </p>
<p> <code>NOTE:</code> Currently this option requires the tab titles to be drawn with a proportionally spaced font (which is currently only possible with Xft). Also, this option only affects the displayed tab title, and thus <i>%t</i> will still expand to the actual tab title, as set via an escape sequence, or macro. For example, setting this option to `<i>%n. %t</i> &#8216; will cause all the tabs to be numbered. [<code>titleFormat</code> ]</p>
<dt><code>-ut | +ut</code></p>
<dd> Utmp inhibit. [<code>utmpInhibit</code> ]</p>
<dt><code>-vbf | +vbf</code></p>
<dd> If unset, colored bold text will not be rendered using overstrike / bold font. See also <code>boldColors</code> and <code>veryBright</code> [<code>veryBoldFont</code> ]</p>
<dt><code>-wd</code></p>
<dd> Working directory of the child process. If non-empty, then the child process is started in this directory. If set to `.&#8217; then the child process is run in the working directory of the current tab if possible. On Linux, this is the default. (NOTE: It is not always possible to find the working directory of the current tab. This works fine on Linux, but causes problems on other systems [e.g. OpenBSD], which is why it is only enabled by default on Linux). [<code>workingDirectory</code> ]</p>
<dt><code>-wtf </code><i>format</i></p>
<dd> Controls the format of the window title. If set, and the option &#8211;<code>stt</code> is used, then the window title is set to <i>format</i> (after % interpolation), instead of the tab title. [<code>winTitleFormat</code> ]</dl>
<h3>Multichar and multi-language support</h3>
<dl>
<dt><code>-mcc | +mcc</code></p>
<dd> Multichar cursor movement [<code>multibyte_cursor</code> ]</p>
<dt><code>-km </code><i>mode</i></p>
<dd> multichar encoding mode [<code>multichar_encoding</code> ]</p>
<dt><code>-im </code><i>name</i></p>
<dd> name of X Input Method (XIM) [<code>inputMethod</code> ]</p>
<dt><code>-pt </code><i>mode</i></p>
<dd> XIM input style: <i>OverTheSpot </i><code>| </code><i>OffTheSpot </i><code>| </code><i>Root</i> [<code>preeditType</code> ]</p>
<dt><code>-thai | +thai</code></p>
<dd> Thai support [<code>thai</code> ]</p>
<dt><code>-grk </code><i>mode</i></p>
<dd> Greek keyboard mapping: <i>iso </i><code>| </code><i>ibm</i> [<code>greek_keyboard</code> ]</dl>
<h3>Menu related options</h3>
<dl>
<dt><code>-menu </code><i>filename </i>[; <i>tag</i> ]</p>
<dd> Menubar definition file. [<code>menu</code> ]</p>
<dt><code>-showmenu | +showmenu</code></p>
<dd> show menubar [<code>showMenu</code> ]</dl>
<h3>Keyboard and window related options</h3>
<dl>
<dt><code>-b </code><i>number</i></p>
<dd> internal border width [<code>internalBorder</code> ]</p>
<dt><code>-bc | +bc</code></p>
<dd> Display a blinking cursor. [<code>cursorBlink</code> ]</p>
<dt><code>-bcst | +bcst</code></p>
<dd> Enable / disable broadcasting input to all terminals [<code>broadcast</code> ]</p>
<dt><code>-bci </code><i>number</i></p>
<dd> Cursor blink interval (ms) [<code>cursorBlinkInterval</code> ]</p>
<dt><code>-bl | +bl</code></p>
<dd> Use a borderless window. [<code>borderLess</code> ]</p>
<dt><code>-blc </code><i>cmd</i></p>
<dd> Bell command instead of beeping. If <i>cmd</i> begins with `!&#8217; then it is passed to <code>/bin/sh -c</code> for execution. Otherwise it is split into words at spaces or tabs only, and executed via <a href="/docs/linux/man/3-execvp/">execvp</a>(3). If you don&#8217;t want a space or tab to cause word splitting, then precede it with a `<code>\</code> &#8216; If you want to pass `\&nbsp;<wbr>&#8216; as an argument, double the `\&#8217; </p>
<p> Note: Only backslashes (or chains of backslashes) that precede a space or tab character are treated specially. That is `\a&#8217; will be left untouched, however `\&nbsp;<wbr>&#8216; will expand to a `\&#8217; and the `&nbsp;<wbr>&#8216; will cause a word break, and `\&nbsp;<wbr>&#8216; will expand to a `&nbsp;<wbr>&#8216; which does not cause a word break. [<code>bellCommand</code> ]</p>
<dt><code>-bw | -w </code><i>number</i></p>
<dd> external border width [<code>externalBorder</code> ]</p>
<dt><code>-desktop </code><i>number</i></p>
<dd> Desktop to place the window (for gnome compatible window manager). The number starts from 0, NOT 1! [<code>desktop</code> ]</p>
<dt><code>-dm | +dm</code></p>
<dd> Enable / disable all keyboard macros. This functionality can be toggled at runtime via a pop-up menu, or the <code>ToggleMacros</code> keyboard shortcut. NOTE: When keyboard macros are disabled, the <code>ToggleMacros</code> keyboard macro will still work. Thus you can re-enable your keyboard macros via the keyboard using this function. [<code>disableMacros</code> ]</p>
<dt><code>-fs | +fs</code></p>
<dd> Startup fullscreen. Use in conjunction with [smoothResize] to really make it full screen. Requires an EWMH compatible window manager. [<code>fullscreen</code> ]</p>
<dt><code>-lk | +lk</code></p>
<dd> Enable Linux console style Home/End keys [<code>linuxHomeEndKey</code> ]</p>
<dt><code>-mod </code><i>mode</i></p>
<dd> Meta modifier: <i>alt </i><code>| </code><i>meta </i><code>| </code><i>hyper </i><code>| </code><i>super </i><code>| </code><i>mod1 </i><code>| </code><i>&#8230; </i><code>| </code><i>mod5</i> [<code>modifier</code> ]</p>
<dt><code>-lsp </code><i>number</i></p>
<dd> Line space between rows [<code>lineSpace</code> ]</p>
<dt><code>-m | +m</code></p>
<dd> Start maximized (requires an EWMH compatible window manager). [<code>maximized</code> ]</p>
<dt><code>-m8 | +m8</code></p>
<dd> Enable / disable meta8 [<code>meta8</code> ]</p>
<dt><code>-nsc | +nsc</code></p>
<dd> Enable / disable reading the system wide configuration file. Only the default keyboard macros are defined in this file, so this option can effectively disable all default keyboard shortcuts. [<code>noSysConfig</code> ]</p>
<dt><code>-or | +or</code></p>
<dd> Override redirect [<code>overrideRedirect</code> ]</p>
<dt><code>-pb | +pb</code></p>
<dd> <code>Pointer blank (see also pointerBlankDelay</code> [<code>pointerBlank</code> ]</p>
<dt><code>-rv | +rv</code></p>
<dd> reverse video [<code>reverseVideo</code> ]</p>
<dt><code>-tcw | +tcw</code></p>
<dd> Triple click word selection [<code>tripleclickwords</code> ]</p>
<dt><code>-vb | +vb</code></p>
<dd> Visual bell [<code>visualBell</code> ]</dl>
<h3>Miscellaneous options</h3>
<dl>
<dt><code>-C</code></p>
<dd> Intercept console messages</p>
<dt><code>-dmask </code><i>namelist</i></p>
<dd> Print out debug message defined by a coma separated name list. Available names include: command, screen, ptytty, init, main, logging, macros, menubar, tabbar, scrollbar, images, pixmap, transparent, encoding, gkrelot, memory, session, string, resource, xftacs, misc, and all.</p>
<dt><code>-dlevel </code><i>verboselevel</i></p>
<dd> Print out debug message defined by verboselevel. Available verboselevel are: fatal, error, warn, info, verbose, and debug. The latter, the more information is printed</p>
<dt><code>-cf </code><i>filename</i></p>
<dd> X resource configuration file</p>
<dt><code>-cfs </code><i>filename</i></p>
<dd> X resource configuration file to save the current configuration [<code>confFileSave</code> ]</p>
<dt><code>-path </code><i>path</i></p>
<dd> Colon delimited list of directories to search for background images and menu files. first searches for the file in the current directory, then in the directories specified by <i>path</i> then in the directories specified by the environment variable <code>PATH_ENV</code> and finally tries in the user configuration directory ~/.mrxvt and the (compiled in) system wide configuration directory /etc/mrxvt [<code>path</code> ]</p>
<dt><code>-sid </code><i>string</i></p>
<dd> Client identity of mrxvt for X session management [<code>smClientID</code> ]</p>
<dt><code>-sm | +sm</code></p>
<dd> enable X session management [<code>sessionMgt</code> ]</dl>
<h3>Long options</h3>
<p> The following options do not have a &#8220;short&#8221; form. If these options are to be used on the command line, they must be prefixed with a `<i>&#8212;</i> &#8216; (or `<i>++</i> &#8216; for boolean options). They can of course be used in the configuration file.</p>
<dl>
<dt><code>answerBackString </code><i>string</i></p>
<dd> Specify the reply sends to the shell when an ENQ (control-E) character is passed through. It may contain escape values as described in the entry on <code>keysym</code> following.</p>
<dt><code>backspaceKey </code><i>string</i></p>
<dd> The string to send when the backspace key is pressed. If set to DEC or unset it will send Delete (code 127) or, if shifted, Backspace (code 8) &#8211; which can be reversed with the appropriate DEC private mode escape sequence.</p>
<dt><code>bgRefreshInterval </code><i>delay</i></p>
<dd> Specify the delay (ms) to wait before refreshing the background in pseudo-transparency. Generally tinting and refreshing the background is slow (especially with XRender), and causes lags while dragging the window. This delay causes enables the window to be dragged smoothly. If you have a fast system, you can reduce or disable this (by setting it to 0). The default value is 100ms.</p>
<dt><code>boldFont </code><i>N font</i></p>
<dd> Specifies bold font to use along with fontset <i>N</i></p>
<dt><code>boldColors </code><i>True </i><code>| </code><i>False</i></p>
<dd> If false, the bold primary colors (0 &#8212; 7) will be rendered using the brighter analogues (8&#8211;15) in a regular font. If true a bold font will be used. See also <code>veryBright</code></p>
<dt><code>color </code><i>N color</i></p>
<dd> Use the specified colour for the colour value <i>N</i> where 0-7 corresponds to low-intensity (normal) colours and 8-15 corresponds to high-intensity colours.</p>
<dt><code>colorBD </code><i>color</i></p>
<dd> Color to use to display bold text. If unspecified, the text will be displayed using a bold font / overstrike.</p>
<dt><code>colorRV </code><i>color</i></p>
<dd> Color to use to display reverse video text. If unspecified, the text will be displayed as reverse video.</p>
<dt><code>colorUL </code><i>color</i></p>
<dd> Color to use to display underlined text. If unspecified, the text will be displayed as underlined.</p>
<dt><code>cursorColor2 </code><i>color</i></p>
<dd> Second color of cursor.</p>
<dt><code>cutChars </code><i>string</i></p>
<dd> String containing all characters to be treated as one word for double click selection. If you want double clicks to select URL&#8217;s, then set this to a string containing all letters (both upper and lower case), digits and punctuation you find in urls.</p>
<dt><code>deleteKey </code><i>string</i></p>
<dd> The string to send when the delete key (not the keypad delete key) is pressed. If unset it will send the sequence traditionally associated with the <code>Execute</code> key.</p>
<dt><code>focusDelay </code><i>msec</i></p>
<dd> The time interval (in mili-seconds) to wait after getting / losing focus, before fading the colors and changing the background color as specified by the &#8211;<code>fade</code> and &#8211;<code>ufbg</code> options. Set it to 0 if you want your colors faded immediately on focus change events. </p>
<p> This option is there mainly to work around a bug in some window managers which send focus in immediately followed by focus out events when moving windows, or pressing Alt+Tab (e.g. fvwm-2.5.16).</p>
<dt><code>font </code><i>N font</i></p>
<dd> Specify the alternative font <i>n . n </i><code>can be 1, 2, 3, 4 or 5.</code></p>
<dt><code>greektoggle_key </code><i>keysym</i></p>
<dd> Key to toggle into greek keyboard mapping. See README.greek for details.</p>
<dt><code>highlightColor </code><i>color</i></p>
<dd> Color to use for selection. If not specified, reverse video is used. (Note blinking text is also displayed with this color).</p>
<dt><code>mapAlert </code><i>True </i><code>| </code><i>False</i></p>
<dd> If true, de-iconifies the window when a bell is received.</p>
<dt><code>mfont </code><i>n font</i></p>
<dd> Specify alternative multiple character font <i>n</i></p>
<dt><code>pointerBlankDelay </code><i>delay</i></p>
<dd> Delay (ms) to blank pointer after.</p>
<dt><code>printPipe </code><i>cmd</i></p>
<dd> Specify a command pipe for vt100 printer.</p>
<dt><code>refreshLimit </code><i>N</i></p>
<dd> This option and <code>skipPages</code> are to be used to replace the `jump scroll&#8217; behaviour of other terminal emulators (and previous version of <code>)</code> Generally when data is available from a tab, reads as much of it as is available (up to our buffer size), and process it. After we are done processing it (generally takes a fraction of a mili-second), we look for more data from the tab. If we obtain not more than <i>N</i> characters, then we request a screen refresh (which takes a while, especially if you use Xft with anti aliasing). If we obtain more than <i>N</i> characters from the tab, then we delay the screen refresh until the tab eventually has either <i>N</i> or fewer characters of output, or the tab has (cumulatively) produced at least <code>skipPages</code> of data. </p>
<p> The default value is 0. On new fast machines, this is probably the best. If you find screen refreshes laggy on on slow older machines, then increase this value a little (say to 10). Setting it to something enormous (say BUFSIZ) will cause to request screen refreshes every time the active tab has data, and effectively disable the so called `jump scrolling&#8217;</p>
<dt><code>scrollColor </code><i>color</i></p>
<dd> Color of scrollbar (see also <code>troughColor )</code></p>
<dt><code>selectStyle </code><i>mode</i></p>
<dd> Set mouse selection style to <code>old</code> which is 2.20, <code>oldword</code> which is xterm style with 2.20 old word selection, or anything else which gives xterm style selection.</p>
<dt><code>skipPages </code><i>N</i></p>
<dd> This option and <code>refreshLimit</code> are to be used to replace the `jump scroll&#8217; behaviour of other terminal emulators (and previous version of <code>)</code> If the screen refresh is delayed because of the <code>refreshLimit</code> option, then will refresh the screen every <i>N</i> pages of output. The default is 25. If you set it to a very large value (say INT_MAX), then will refresh the screen only after the tab has stopped `flat out&#8217; scrolling.</p>
<dt><code>smartResize </code><i>True </i><code>| </code><i>False</i></p>
<dd> Enable / disable smart resize. When the tabbar is shown, or font size is increased, the resize terminal window could be partially off screen. If <code>smartResize is enabled, then tries to move the terminal window to stay on screen.</code></p>
<dt><code>smoothResize </code><i>True </i><code>| </code><i>False</i></p>
<dd> <code>Enable / disable smooth resize. If </code>enabled, then the <code>window is resized in pixel increments (instead of character increments). This is useful if you want a full screen / maximized window that covers the entire screen (without leaving an annoying few pixel wide strip uncovered).</code></p>
<dt><code>troughColor</code></p>
<dd> Color of scrollbar trough (see also <code>scrollColor )</code></p>
<dt><code>useFifo </code><i>True </i><code>| </code><i>False</i></p>
<dd> If enabled, then mrxvt will create a <a href="/docs/linux/man/7-fifo/">fifo</a>(7)Pa/tmp/.mrxvt-%pid and listen for macros on it. To execute macros, just write them to this fifo. For example </p>
<pre>
/bin/echo -e &quot;NewTab
Raise&quot; &gt;&gt; /tmp/.mrxvt-%pid
</pre>
<p> creates a new tab and raises the window with process ID <i>%pid</i> <code>NOTE:</code> The meaning and syntax of this option might change in future versions.</p>
<dt><code>veryBright </code><i>True </i><code>| </code><i>False</i></p>
<dd> If true, and if <code>boldColors</code> is false, then bold primary colors are rendered as bright colors with a bold font (this was the default behaviour in 0.5.2 and earlier versions).</dl>
<h2>CONFIGURATION FILE SYNTAX</h2>
<p> A line in the config file generally looks like this </p>
<pre>
ClassName.OptionName:   Value
</pre>
<p> Blank lines, and lines beginning with `<i>#</i> &#8216; are ignored (comments). </p>
<p> The ClassName is the name specified via the &#8211;<code>name</code> option (by default `<i>mrxvt</i> &#8216; When starts up, it ONLY reads options with ClassName `<i>Mrxvt</i> &#8216; `<i>XTerm</i> &#8216; or the class specified via the &#8211;<code>name</code> option. See /etc/mrxvt/mrxvtrc.sample for how this feature can be used. </p>
<p> The OptionName is the long name of the option you want to set. It can be any long option (listed under the Sx Long Options sub section), or is specified in brackets as [<code>option_name</code> ] alongside regular options in this man page. Finally Value is the value of this option. </p>
<h3>Example</h3>
<p> The following is an example ~/.mrxvtrc file, or in a configuration file you will load with &#8211;<code>cf</code> option at startup. You can consult the doc/mrxvtrc.sample in the directory for more details. </p>
<pre>
Mrxvt.profile0.tabTitle:        term1
Mrxvt.profile1.tabTitle:        term2
Mrxvt.profile2.tabTitle:        term3
Mrxvt.profile0.saveLines:       600
Mrxvt.profile1.saveLines:       600
Mrxvt.profile2.saveLines:       600
# Mrxvt.profile0.Pixmap:        /home/images/vt0bg.xpm
# Mrxvt.profile1.Pixmap:        /home/images/vt1bg.xpm
# Mrxvt.profile2.Pixmap:        /home/images/vt2bg.xpm
Mrxvt.scrollbarStyle:           next
Mrxvt.initTermNumber:           3
Mrxvt.transparent:              True
Mrxvt.transparentScrollbar:     True
Mrxvt.transparentTabbar:        False
Mrxvt.transparentMenubar:       False
Mrxvt.tintColor:                #ffffff
Mrxvt.shading:                  85
Mrxvt.foreground:               white
Mrxvt.background:               black
</pre>
<h2>MENUS</h2>
<p> The menu system is similar to rxvt&#8217;s menus (see the included file rxvtRef.txt with a few enhancements, and a few notable exceptions:</p>
<dl>
<dt><code>The menus can use a proportionally spaced font under Xft (</code></p>
<dd> &#8211;<code>xftpfn</code> which is significantly less ugly than a mono-spaced font.</p>
<dt>
<dd> supports pop-up menus. If you create a menu named <code>PopupButton </code><i>N </i><code>(where </code><i>N </i><code>is 1, 2, or 3) then that menu is popped up when you control click (with the appropriate mouse button) on the terminal window. Additionally if you right click on the Tab bar, then the menu PopupButton1 is popped up.</code></p>
<dt><code>To create a menu containing a list of all open tabs, create an empty menu called</code></p>
<dd> <code>PopupButton </code><i>N</i> (which will be popped on control click&#8217;s as described above). To include a list of all open tabs as a sub menu, create a sub-menu called `Switch to tab&#8217;</p>
<dt><code>Menu actions are completely different in</code></p>
<dd> than the original implementation in <a href="/docs/linux/man/1-rxvt/">rxvt</a>(1). The menu actions are exactly the same as macro actions, and are described in the section Sx Defining custom shortcuts .</p>
<dt><code>On startup</code></p>
<dd> reads the file default.menu which contains the default menu definitions. The file is searched for in your search path (specified by option &#8211;<code>path )</code></dl>
<h2>KEYBOARD AND MOUSE SHORTCUTS</h2>
<p> You have several default keyboard shortcuts to ease the use of mrxvt. The default gnome-terminal, Konsole, rxvt shortcuts are predefined for you. You can also define your own shortcuts as described in Sx Defining custom shortcuts .</p>
<h3>Default keyboard shortcuts</h3>
<p> The following key combinations are defined by default. These are defined in the system configuration file /etc/mrxvt/mrxvtrc and can be disabled using the option &#8211;<code>nsc</code> See the next section for instructions on defining your own custom keyboard shortcuts. </p>
<p> <i>Gnome-terminal style shortcuts:</i></p>
<dl>
<dt><code>Ctrl+Shift+t</code></p>
<dd> create a new tab</p>
<dt><code>Ctrl+Shift+q</code></p>
<dd> Close all tabs and exit</p>
<dt><code>Ctrl+Shift+w</code></p>
<dd> Close active tab, and do not hold it open if it exits abnormally.</p>
<dt><code>Ctrl+PgUp </code>activate left tab</p>
<dd>
<dt><code>Ctrl+PgDn </code>activate right tab</p>
<dd>
<dt><code>Meta+1</code></p>
<dd> activate 1st tab</p>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>Meta+0</code></p>
<dd> activate 10th tab</p>
<dt><code>Ctrl+equal</code></p>
<dd> increase font size (next font)</p>
<dt><code>Ctrl+Shift+plus</code></p>
<dd> increase font size by 2</p>
<dt><code>Ctrl+minus</code></p>
<dd> decrease font size (previous font)</p>
<dt><code>Ctrl+Shift+underscore</code></p>
<dd> decrease font size by 2</dl>
<p> <i>Konsole style default shortcuts:</i></p>
<dl>
<dt><code>Ctrl+Shift+Left</code></p>
<dd> move active tab to left</p>
<dt><code>Ctrl+Shift+Right:</code></p>
<dd> active tab to right</p>
<dt><code>Shift+Left</code></p>
<dd> Activate left tab (Primary only)</p>
<dt><code>Shift+Right</code></p>
<dd> Activate right tab (Primary only)</p>
<dt><code>Ctrl+Shift+n</code></p>
<dd> Create a new tab with the same profile as the current tab.</dl>
<p> <i>Vi </i>style default shortcuts:</p>
<dl>
<dt><code>Ctrl+Shift+h</code></p>
<dd> activate left tab</p>
<dt><code>Ctrl+Shift+l</code></p>
<dd> activate right tab</dl>
<p> <i>Screen style default shortcuts:</i></p>
<dl>
<dt><code>Ctrl+Shift+p</code></p>
<dd> activate previous active tab</dl>
<p> <i>Mrxvt default shortcuts:</i></p>
<dl>
<dt><code>Ctrl+Shift+1</code></p>
<dd> Move tab to 1st position</p>
<dt><code>&#8230;</code></p>
<dd>
<dt><code>Ctrl+Shift+0</code></p>
<dd> Move tab to 10th position</p>
<dt><code>Ctrl+Tab</code></p>
<dd> activate previous active tab</p>
<dt><code>Ctrl+Shift+less_than</code></p>
<dd> Move active tab left</p>
<dt><code>Ctrl+Shift+greater_than</code></p>
<dd> Move active tab right</p>
<dt><code>Ctrl+Shift+o</code></p>
<dd> Change opacity of terminal to make it more transparent.</p>
<dt><code>Ctrl+Shift+u</code></p>
<dd> Change opacity of terminal to make it less transparent.</p>
<dt><code>Ctrl+Shift+j</code></p>
<dd> Change shading of terminal to make it more transparent.</p>
<dt><code>Ctrl+Shift+k</code></p>
<dd> Change shading of terminal to make it less transparent.</p>
<dt><code>Ctrl+Shift+r</code></p>
<dd> Toggle psdudo-transparency</p>
<dt><code>Ctrl+Shift+i</code></p>
<dd> Hide/show tabbar</p>
<dt><code>Ctrl+Shift+s</code></p>
<dd> Hide/show scrollbar</p>
<dt><code>Ctrl+Shift+m</code></p>
<dd> Hide/show menubar</p>
<dt><code>Ctrl+Shift+a</code></p>
<dd> Hide/show tabbar buttons</p>
<dt><code>Ctrl+Shift+b</code></p>
<dd> Toggle very bold font</p>
<dt><code>Ctrl+Shift+c</code></p>
<dd> Open a console in a new tab, and enable the <code>useFifo</code> option if necessary. Anything typed in this console will be executed as a macro. On clean exit the <code>useFifo</code> option will be disabled.</p>
<dt><code>Ctrl+Shift+d</code></p>
<dd> Toggle input broadcasting (unbound by default)</p>
<dt><code>Ctrl+Shift+e</code></p>
<dd> Toggle holding exited tab</p>
<dt><code>Ctrl+Shift+f</code></p>
<dd> Toggle full screen mode</p>
<dt><code>Ctrl+Shift+x</code></p>
<dd> Save current configuration</p>
<dt><code>Shift+Del</code></p>
<dd> Set title of active tab to selection.</p>
<dt><code>Shift+Insert</code></p>
<dd> Paste X selection into active tab.</p>
<dt><code>Ctrl+Shift+v</code></p>
<dd> Paste X selection into active tab.</p>
<dt><code>Shift+Up </code>Scroll up one line (Primary screen only)</p>
<dd>
<dt><code>Shift+Dn </code>scroll down one line (Primary screen only)</p>
<dd>
<dt><code>Shift+PgUp </code>scroll up one page (Primary screen only)</p>
<dd>
<dt><code>Shift+PgDn </code>scroll down one page (Primary screen only)</p>
<dd>
<dt><code>Shift+Home</code></p>
<dd> Scroll to beginning of scroll-back buffer (Primary screen only)</p>
<dt><code>Shift+End</code></p>
<dd> Scroll to end of scroll-back buffer (Primary screen only)</p>
<dt><code>Shift+KeypadPlus</code></p>
<dd> Increase font size</p>
<dt><code>Shift+KeypadMinus</code></p>
<dd> Decrease font size</p>
<dt><code>Ctrl+Shift+F1</code></p>
<dd> Open man page in a new tab.</p>
<dt><code>Ctrl+Shift+F12</code></p>
<dd> Enable / disable all keyboard macros (except this one of course).</dl>
<h3>Defining custom shortcuts</h3>
<p> NOTE: The `hotkey&#8217; mechanism used in versions 0.4.2 and earlier is now obsolete. It has been replaced by the `macro&#8217; functionality (described below) as of version 0.5.0. </p>
<p> You can define your own keyboard shortcuts in your configuration file by using the following syntax: </p>
<pre>
Mrxvt.macro.[modifiers+]keyname:         action
</pre>
<p> Here `modifiers&#8217; is a `+&#8217; separated list of modifiers `<i>Ctrl</i> &#8216; `<i>Alt</i> &#8216; `<i>Meta</i> &#8216; `<i>Shift</i> &#8216; `<i>Primary</i> &#8216; and `<i>Add</i> &#8216; The first four refer to the respective modifier keys. `<i>Primary</i> &#8216; tells to make the macro available ONLY when the primary screen is displayed (e.g. `<i>Primary</i> &#8216; macros will not be effective when you are running <a href="/docs/linux/man/1-vim/">vim</a>(1), but will be effective when you are at the shell prompt). Finally `<i>Add</i> &#8216; tells to add the macro action to any previous action associated to that particular key. For instance </p>
<pre>
Mrxvt.macro.Primary+Shift+Return:       Esc c
Mrxvt.macro.Primary+Add+Shift+Return:   Str ^M
</pre>
<p> will define the macro `Shift+Return&#8217; to first send the escape sequence `c&#8217; to (which has the effect of clearing the scroll back buffer) and then send `Ctrl-M&#8217; to the child process, but ONLY in the primary screen. If you&#8217;re running a shell, then this effectively clears the scroll back buffer and executes the command. </p>
<p> If the `<i>Add</i> &#8216; modifier is not specified, then the macro action replaces any previous action (if any) associated to the specified key. It is an error to add a macro to a non-existing macro. Currently one key can have at most 16 actions associated to it (this might be reduced to 8 in future). </p>
<p> `keyname&#8217; is the name of the key you want to bind to the specified macro. Non alpha numeric keys (e.g. punctuation, or cursor/keypad keys) are specified by using their keyname, which you can find by <a href="/docs/linux/man/1-xev/">xev</a>(1), or looking directly in the system header file /usr/include/X11/keysymdef.h </p>
<p> In case you want to unbind a default keyboard macro, just bind the appropriate key to the function `<code>Dummy</code> &#8216; For example </p>
<pre>
Mrxvt.macro.Ctrl+Shift+t:       Dummy
</pre>
<p> will disable the default keyboard shortcut `Ctrl+Shift+t&#8217; If you want to disable all keyboard macros, use the option `-<code>dm</code> &#8216; (which can also be accessed via a pop-up menu). The default keyboard macros are defined in the system configuration file /etc/mrxvt/mrxvtrc so if you only want to disable all default shortcuts keys, don&#8217;t read the system configuration file by using the &#8211;<code>nsc</code> option. </p>
<p> Notice that keyboard shortcuts definitions are incompatible with X Windows own resource parsing API, i.e., XGetDefaults. So, to enable the keyboard shortcuts, you will need to enable resources but disable xgetdefault when you configure </p>
<p> Finally `action&#8217; is the action you want bound to the specified macro key. The available actions you can bind to macros are:</p>
<dl>
<dt><code>Dummy</code></p>
<dd> Clear an existing keyboard shortcut</p>
<dt><code>Esc </code><i>str</i></p>
<dd> Send the escape sequence <i>str</i> to <code>.</code></p>
<dt><code>Str </code><i>str</i></p>
<dd> Send the string <i>str</i> to the child process.</p>
<dt><code>Exec </code><i>command</i></p>
<dd> Executes <i>command</i> asynchronously. The command run without any controlling shell or TTY. This is generally used to launch X11 programs (e.g. open the selected text in firefox). If you want a command run in a new tab, see the <code>NewTab</code> macro). </p>
<p> The argument <i>command</i> is word split exactly as described in the &#8211;<code>blc</code> option (thus for instance beginning it with `!&#8217; will pass it to <code>/bin/sh -c</code> for word splitting and execution). However keep in mind that like all macro arguments, <i>command</i> is first `<code>\</code> &#8216; interpolated. Thus if on the rare occasion you want `\&nbsp;<wbr>&#8216; to be part of <i>command</i> then you will have to do something like `\\\&nbsp;<wbr>&#8216; and not `\\&nbsp;<wbr>&#8216; as you would with the argument of &#8211;<code>blc</code></p>
<dt><code>NewTab </code>[<i>-N </i>[<i>title </i>[[! <i>command</i> ] ] ] ]</p>
<dd> Open a new tab. <i>N</i> specifies the profile number. If omitted, profile 0 is used. If only `-&#8216; (with no number) is specified, then the profile of the current active tab is used (i.e. this can be used to duplicate the current tab). <i>title</i> is specified (needs to be double quoted), use that for the tab title. If <i>command</i> is specified, execute that command in the new tab (instead of the one specified by the resource file, or the shell). </p>
<p> <i>command</i> is word split as described in the <code>Exec</code> macro. However if command begins with an So ! Sc then run a shell first, and execute the command in the shell as if the user had typed <i>command</i> at the shell prompt. If instead you want <i>command</i> to be passed to <code>/bin/sh -c</code> for word splitting and execution, then begin <i>command</i> with `\!&#8217;</p>
<dt><code>Close </code>[<i>N</i> ]</p>
<dd> Close a tab. If no argument is specified, close all tabs and exit. If <i>N</i> is 0, close the active tab. Otherwise close the <i>N </i><code>th tab</code></p>
<dt><code>GotoTab </code>[<i>N</i> ]</p>
<dd> Goto tab. If <i>N</i> is ommited or 0, then goto the previous active tab. Otherwise goto the <i>N </i><code>th</code> tab. If <i>N</i> begins with a `+&#8217; or `-&#8216; then <i>N</i> is relative to the current tab.</p>
<dt><code>MoveTab </code><i>N</i></p>
<dd> Move active tab to position <i>N</i> If <i>N</i> begins with a `+&#8217; or `-&#8216; then <i>N</i> is relative to the current tab.</p>
<dt><code>Scroll </code><i>amount</i></p>
<dd> Scroll the active tab by <i>amount</i> lines (negative values mean scroll backward). If <i>amount</i> ends with `p&#8217; then scroll <i>amount</i> pages instead of lines.</p>
<dt><code>Copy</code></p>
<dd> Copy selection into clipboard (not implemented).</p>
<dt><code>Paste</code></p>
<dd> Pasete selection into active tab.</p>
<dt><code>ToggleSubwin </code>[[<i>+ </i><code>| </code><i>&#8211; </i>[<i>b </i><code>| </code><i>m </i><code>| </code><i>s </i><code>| </code><i>t</i> ] ] ]</p>
<dd> Toggle visibility of sub-windows. If the argument begins with a `+&#8217; the subwindow is shown. If it begins with a `-&#8216; the subwindow is hidden. Otherwise it is toggled. The letters `<i>b</i> &#8216; `<i>m</i> &#8216; `<i>s</i> &#8216; and `<i>t</i> &#8216; represent the tabbar buttons, menubar, scrollbar and tabbar respectively. NOTE: Currently you can only toggle one subwindow at a time.</p>
<dt><code>ResizeFont </code>[<i>+ </i><code>| </code><i>&#8211; </i><i>N</i> ]</p>
<dd> Resize the font. With Xft, <i>N</i> represents the size increment of the xft font. Without Xft, <i>N</i> represents the index of the X11 fonts specified by the <code>font </code><i>N</i> resources.</p>
<dt><code>ToggleVeryBold</code></p>
<dd> Toggle use of bold font for colored text.</p>
<dt><code>ToggleTransparency</code></p>
<dd> Toggle pseudo transparency.</p>
<dt><code>ToggleBroadcast</code></p>
<dd> Toggle broadcasting of input to all tabs.</p>
<dt><code>ToggleHold </code>[<i>mask</i> ]</p>
<dd> If <i>mask</i> is not specified, then just close all tabs who&#8217;s child processes have exited. (This is almost compatible with the behaviour of 0.5.1 and earlier). If <i>mask</i> is specified, then change the hold status of the current tab. <i>mask</i> must begin with `<code>+</code> &#8216; `<code>&#8211;</code> &#8216; or `<code>!</code> &#8216; and be followed by a bit mask (as in the <code>holdExit</code> option). `<code>+</code> &#8216; will add bits to the <code>holdExit</code> option for this tab, `<code>&#8211;</code> &#8216; will subtract, and `<code>!</code> &#8216; will toggle. Remember that if the lowest bit of the current tabs <code>holdExit</code> option is set, then the tab will always be held open and everything else will be ignored.</p>
<dt><code>ToggleFullscreen</code></p>
<dd> Toggle between full screen and regular mode. Also enable &#8211;<code>-smoothResize</code> to get true full screen. This will only work if you are running an EWMH compatible window manager (e.g. Fvwm / OpenBox / KDE / Gnome).</p>
<dt><code>Raise</code></p>
<dd> Raise the window.</p>
<dt><code>SetTitle</code></p>
<dd> Set title of active tab to selection. (The selection must be owned by <code>)</code></p>
<dt><code>UseFifo </code><i>status</i></p>
<dd> Enable or disable using a <a href="/docs/linux/man/1-fifo/">fifo</a>(1) to listen for macros on (see the <code>useFifo</code> option). The argument <i>status</i> should be <code>0 , 1 , -1</code> to disable, enable or toggle respectively.</p>
<dt><code>PrintScreen </code>[-<code>psn </code>[<i>command</i> ] ]</p>
<dd> Dump screen to printer (or <i>command )</i> If &#8211;<code>p</code> is specified, then the output is pretty printed (i.e. escape sequences are used to get the same color in the output as on your screen). If &#8211;<code>s</code> is specified, then the entire scroll back is printed (instead of just the current screen). If &#8211;<code>n</code> is specified, then every screen line is terminated with a newline char (by default screen lines that wrap to the next line are not terminated with a newline). Finally, if command is specified it is used as the printer pipe (if not the value of <code>printPipe</code> or the compiled in default is used).</p>
<dt><code>SaveConfig </code>[<i>filename</i> ]</p>
<dd> Save config to file. If no filename is specified, save to ~/.mrxvtrc.save</p>
<dt><code>ToggleMacros</code></p>
<dd> Toggle the use of keyboard shortcuts. When macros are disabled (either by using this macro, or by the &#8211;<code>dm</code> option), then this is the only keyboard shortcut that will work. Thus you can re-enable your keyboard shortcuts via the keyboard using this function.</dl>
<p> Additionally, the argument to any of the above macros are `<code>\</code> &#8216; and `<code>%</code> &#8216; interpolated as follows: </p>
<dl>
<dt><code></code></p>
<dd> Bell</p>
<dt><code></code></p>
<dd> Backspace</p>
<dt><code>\E , </code></p>
<dd> Escape</p>
<dt><code>
</code></p>
<dd> Newline</p>
<dt><code></code></p>
<dd> Carriage return</p>
<dt><code>	</code></p>
<dd> Tab</p>
<dt><code>\ </code><i>ddd</i></p>
<dd> Char with octal ASCII code <i>ddd</i></p>
<dt><code>^@ , ^A .. ^Z .. ^_ , ^?</code></p>
<dd> Control-@, Control-A &#8230; </p>
<dt><code>%G</code></p>
<dd> Global (static) tab number.</p>
<dt><code>%p</code></p>
<dd> PID of child process in current tab.</p>
<dt><code>%P</code></p>
<dd> PID of</p>
<dt><code>%n</code></p>
<dd> Tab number.</p>
<dt><code>% N</code></p>
<dd> Expands to `normally&#8217; if the process exited normally (e.g. by calling <a href="/docs/linux/man/1-exit/">exit</a>(1)) or `abnormally&#8217; otherwise. (Note this is independent of the exit status).</p>
<dt><code>%s</code></p>
<dd> Text selected in the window.</p>
<dt><code>%S</code></p>
<dd> If the process in this tab is dead, then it expands to the exit status of the child process. Otherwise left unchanged.</p>
<dt><code>%t</code></p>
<dd> Tab title.</p>
<dt><code>%T</code></p>
<dd> Total number of tabs created in lifetime.</dl>
<h3>Mouse shortcuts</h3>
<dl>
<dt><code>Changing tab titles</code></p>
<dd> This mouse shortcut can be used to dynamically change the tab title as follows: Select text in the terminal window. Then middle click on a tab to change the tab&#8217;s title. If you middle click on the tabbar background, then the title of the active tab is changed.</p>
<dt><code>Tab list menu</code></p>
<dd> By default, if you right click on the tab bar, or control-left-click on the terminal window, a popup menu with a list of currently open tabs pops up. The actual menu popped up can be customized as described under the section Sx MENUS .</p>
<dt><code>Popup menus</code></p>
<dd> If you Control-click on the terminal window (with any mouse button), it pops up a menu. The actual menu popped up can be customized as described under the section Sx MENUS .</p>
<dt><code>Moving tabs</code></p>
<dd> Click and drag a tab to some other location on the tab-bar to move it.</dl>
<h2>ESCAPE SEQUENCES</h2>
<p> You have several escape sequences to control <code>.</code> All default <a href="/docs/linux/man/1-rxvt/">rxvt</a>(1) escape sequences are supported by <code>.</code> A few extra escape sequences have been added to improve DEC compatibility, and allow interaction with extra features (e.g. tabs). The supported escape sequences are listed in the file mrxvt_seq.txt included in the distribution. </p>
<p> For omissions in the documentation, and a more complete reference to escape sequences you should look at the file ctlseqs.txt that comes with the xterm package, console_codes4 and the original rxvt documentation in the file rxvtRef.txt </p>
<p> For basic interaction with (e.g. changing the tab title etc.) you should also look at the programs share/scripts/settitle.c and share/scripts/mrxvtset.pl that are supplied with the distribution.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>COLORFGBG</code></p>
<dd> Set to the terminal foreground and background colors.</p>
<dt><code>COLORTERM</code></p>
<dd> Sets to the terminal sub-name that indicates its color.</p>
<dt><code>DISPLAY</code></p>
<dd> Used (and set) to the X display bieng used.</p>
<dt><code>PATH_ENV</code></p>
<dd> Path to look for menu / background files (see &#8211;<code>path</code> option).</p>
<dt><code>TERM</code></p>
<dd> Set to the terminal name in the window you have created.</p>
<dt><code>MRXVT_TABTITLE</code></p>
<dd> Set to the initial tab title of each terminal. Notice that its value will not be altered if the user uses a shortcut or escape sequence to change the tab title. The user must modify it manually after doing that.</p>
<dt><code>WINDOWID</code></p>
<dd> Set to the X window id number of the mrxvt window.</dl>
<h2>FILES</h2>
<p> The actual pathnames given may differ on your system.</p>
<dl>
<dt><code>default.menu </code></p>
<dd> The default menu file loaded at startup (searched for in your &#8211;<code>path )</code></p>
<dt><code>~/mrxvt </code></p>
<dd> Directory in which to look for user menu and image files.</p>
<dt><code>~/.mrxvtrc </code></p>
<dd> This is the default configuration file (since 0.3.9). If present, resources read from this file override existing resources.</p>
<dt><code>~/.Xdefaults </code></p>
<dd> (OBSOLETE) This was the default configuration file (before 0.3.9). If present, resources read from this file override existing resources.</p>
<dt><code>~/.Xresources </code></p>
<dd> (OBSOLETE) If both .mrxvtrc and .Xdefaults are not found, try this one.</p>
<dt><code>/etc/mrxvt </code></p>
<dd> System wide directory in which to look for user menu and image files.</p>
<dt><code>/etc/mrxvt/default.menu </code></p>
<dd> Default menu file read on startup.</p>
<dt><code>/etc/mrxvt/mrxvtrc </code></p>
<dd> System wide configuration file. (By default this file only defines the default keyboard macros)</p>
<dt><code>/etc/utmp </code></p>
<dd> System file for login records.</p>
<dt><code>/usr/lib/X11/rgb.txt </code></p>
<dd> Color names.</p>
<dt><code>/usr/X11R6/lib/X11/app-defaults/XTerm </code></p>
<dd> (OBSOLETE) If enable xgetdefaults at compiled time, this is the first configuration file read.</dl>
<h2>BUGS</h2>
<h3>Reporting bugs</h3>
<p> Please report bugs using the sourceforge bug tracker system at </p>
<p> <i><a rel="nofollow" href="http://sourceforge.net/projects/materm">http://sourceforge.net/projects/materm</a></i> </p>
<p> Alternately you can send your bug report to the mrxvt developer mailing list at </p>
<p> Mt materm-devel [at] lists.sourceforge.net </p>
<p> Be sure you give us enough details to reproduce the bug ourselves, and check to see if your bug still exists in the current CVS version.</p>
<h3>Known bugs</h3>
<dl>
<dt><code>Tabs don&#8217;t work properly when running under Xnest.</code></p>
<dd>
<dt><code>Transparency and tinting are global, not specific to a terminal.</code></p>
<dd>
<dt><code>The transparentForce option does not work well with all window managers (e.g. OpenBox).</code></p>
<dd></dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-rxvt/">rxvt</a>(1), <a href="/docs/linux/man/1-xterm/">xterm</a>(1), <a href="/docs/linux/man/1-resize/">resize</a>(1), mrxvt_seq.txt <i>Xterm control sequences</i> (this is the file ctlseqs.ms or ctlseqs.txt ) console_codes4 </p>
<p> <i><a rel="nofollow" href="http://materm.sourceforge.net">http://materm.sourceforge.net</a></i></p>
<h2>AUTHORS</h2>
<p> An Terminator &lt; Ns Mt jimmyzhou [at] users.sourceforge.net Ns &gt; An Gautam Iyer &lt; Ns Mt gi1242 [at] users.sourceforge.net Ns &gt; </p>
<h2>Index</h2>
