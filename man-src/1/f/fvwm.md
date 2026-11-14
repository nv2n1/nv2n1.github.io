---
title: "fvwm(1)"
name: "fvwm"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fvwm/"
description: "Fvwm – F? Virtual Window Manager for X11"
---

<h2 class="name">NAME</h2>
<p> Fvwm &#8211; F? Virtual Window Manager for X11 </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>fvwm</code> [<code>-c</code>&nbsp;<wbr><i>config-command</i>] [<code>-d</code>&nbsp;<wbr><i>displayname</i>] [<code>-f</code>&nbsp;<wbr><i>config-file</i>] [<code>-r</code>] [<code>-s</code>&nbsp;<wbr>[<i>screen_num</i>]] [<code>-V</code>] [<code>-C</code>&nbsp;<wbr><i>visual-class</i> | <code>-I</code>&nbsp;<wbr><i>visual-id</i>] [<code>-l</code>&nbsp;<wbr><i>colors</i>&nbsp;<wbr>[<code>-L</code>]&nbsp;<wbr>[<code>-A</code>]&nbsp;<wbr>[<code>-S</code>]&nbsp;<wbr>[<code>-P</code>]] [<code>-D</code>] [<code>-h</code>] [<code>-i</code>&nbsp;<wbr><i>client-id</i>] [<code>-F</code>&nbsp;<wbr><i>state-file</i>] [<code>&#8211;debug-stack-ring</code>] [<code>-blackout</code>]</dl>
<h2>DESCRIPTION</h2>
<dd>Fvwm is a window manager for X11. It is designed to minimize memory consumption, provide a 3D look to window frames, and a virtual desktop. </p>
<p> Note that there are several window managers around that have &quot;fvwm&quot; in their name. In the past, version 2.x of fvwm was commonly called fvwm2 to distinguish it from the former version 1.x (fvwm or even fvwm1). Since version 1.x has been replaced by version 2.x a long time ago we simply call version 2.x and all versions to come, fvwm, throughout this document, and the executable program is named fvwm. There is an fvwm offspring called fvwm95, it is mostly a patched version of fvwm-2.0.43. The main goal of fvwm95 was to supply a Windows 95 like look and feel. Since then, fvwm has been greatly enhanced and practically all fvwm95 features can be achieved by fvwm. </p>
<p> Fvwm provides both a large <i>virtual desktop</i> and <i>multiple disjoint desktops</i> which can be used separately or together. The virtual desktop allows you to pretend that your video screen is really quite large, and you can scroll around within the desktop. The multiple disjoint desktops allow you to pretend that you really have several screens to work at, but each screen is completely unrelated to the others. </p>
<p> Fvwm provides <i>keyboard accelerators</i> that allow you to perform most window manager functions, including moving and resizing windows and operating the menus, using keyboard shortcuts. </p>
<p> Fvwm has also overcome the distinction between configuration commands and action commands that most window managers make. Configuration commands typically set fonts, colors, menu contents, and key and mouse function bindings, while action commands do things like raise and lower windows. Fvwm makes no such distinction and allows anything to be changed at any time. </p>
<p> Other noteworthy differences between fvwm and other X11 window managers are the introduction of the <i>SloppyFocus</i> and <i>NeverFocus</i> focus methods. Focus policy can be separately specified for different window groups. Windows using <i>SloppyFocus</i> acquire focus when the pointer moves into them and retain focus until some other window acquires it. Such windows do not lose focus when the pointer moves into the root window. The <i>NeverFocus</i> policy is provided for use with windows into which one never types (e.g. xclock, oclock, xbiff, xeyes, tuxeyes) &#8211; for example, if a SloppyFocus terminal window has focus, moving the pointer over a NeverFocus decoration window does not deprive the terminal of focus.</p>
<h2>OPTIONS</h2>
<p> These are the command line options that are recognized by fvwm: </p>
<p> <code>-i</code> | <code>&#8211;clientid</code> <i>id</i></p>
<dl>
<dt>
<dd> This option is used when fvwm is started by a session manager. Should not be used by a user.</dl>
<p> <code>-c</code> | <code>&#8211;cmd</code> <i>config-command</i></p>
<dl>
<dt>
<dd> Causes fvwm to use <i>config-command</i> instead of &#8216;<code>Read</code> <i>config</i>&#8216; (or &#8216;<code>Read</code> <i>.fvwm2rc</i>&#8216;) as its initialization command. (Note that up to 10 <code>-f</code> and <code>-c</code> parameters can be given, and they are executed in the order specified.) </p>
<p> Any module started by command line arguments is assumed to be a module that sends back config commands. All command line modules have to quit before fvwm proceeds on to the StartFunction and setting border decorations and styles. There is a potential deadlock if you start a module other than <code>FvwmCpp</code>/<code>FvwmM4</code>/<code>FvwmPerl</code> but there is a timeout so fvwm eventually gets going. </p>
<p> As an example, starting the pager this way hangs fvwm until the timeout, but the following should work well: </p>
<dl>
<dt>
<dd>
<pre>
fvwm -c &quot;<code>AddToFunc</code> StartFunction I <code>Module</code> <code>FvwmPager</code>&quot;
</pre>
</dl>
</dl>
<p> <code>-d</code> | <code>&#8211;display</code> <i>displayname</i></p>
<dl>
<dt>
<dd> Manage the display called <i>displayname</i> instead of the name obtained from the environment variable <i>$DISPLAY</i>.</dl>
<p> <code>-D</code> | <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Puts X transactions in synchronous mode, which dramatically slows things down, but guarantees that fvwm&#8217;s internal error messages are correct. Also causes fvwm to output debug messages while running.</dl>
<p> <code>-f</code> <i>config-file</i></p>
<dl>
<dt>
<dd> Causes fvwm to read <i>config-file</i> instead of <i>~/.fvwm/config</i> as its initialization file. This is equivalent to -c &#8216;<code>Read</code> <i>config-file</i>&#8216;.</dl>
<p> <code>-h</code> | <code>&#8211;help</code></p>
<dl>
<dt>
<dd> A short usage description is printed.</dl>
<p> <code>-r</code> | <code>&#8211;replace</code></p>
<dl>
<dt>
<dd> Try to take over from a previously running wm. This does not work unless the other wm is ICCCM2 2.0 compliant.</dl>
<p> <code>-F</code> | <code>&#8211;restore</code> <i>state-file</i></p>
<dl>
<dt>
<dd> This option is used when fvwm is started by a session manager. Should not be used by a user.</dl>
<p> <code>-s</code> | <code>&#8211;single-screen</code> [<i>screen_num</i>]</p>
<dl>
<dt>
<dd> On a multi-screen display, run fvwm only on the screen named in the <i>$DISPLAY</i> environment variable or provided through the <code>-d</code> option. The optional argument <i>screen_num</i> should be positive or null and override the screen number. Normally, fvwm attempts to start up on all screens of a multi-screen display.</dl>
<p> <code>-V</code> | <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Prints the version of fvwm to <i>stderr</i>. Also prints an information about the compiled in support for readline, rplay, stroke, xpm, png, svg, GNOME hints, EWMH hints, session management, bidirectional text, multibyte characters, xinerama and Xft aa font rendering.</dl>
<p> <code>-C</code> | <code>&#8211;visual</code> <i>visual-class</i></p>
<dl>
<dt>
<dd> Causes fvwm to use <i>visual-class</i> for the window borders and menus. <i>visual-class</i> can be &quot;StaticGray&quot;, &quot;GrayScale&quot;, &quot;StaticColor&quot;, &quot;PseudoColor&quot;, &quot;TrueColor&quot; or &quot;DirectColor&quot;.</dl>
<p> <code>-I</code> | <code>&#8211;visualid</code> <i>id</i></p>
<dl>
<dt>
<dd> Causes fvwm to use <i>id</i> as the visual id for the window borders and menus. <i>id</i> can be specified as N for decimal or 0xN for hexadecimal. See man page of xdpyinfo for a list of supported visuals.</dl>
<p> <code>-l</code> | <code>&#8211;color-limit</code> <i>limit</i></p>
<dl>
<dt>
<dd> Specifies a <i>limit</i> on the colors used in image, gradient and possibly simple colors used by fvwm. In fact, fvwm (and all the modules) uses a palette with at most <i>limit</i> colors. This option is only useful with screens that display 256 colors (or less) with a dynamic visual (PseudoColor, GrayScale or DirectColor). The default depends on your X server and how you run fvwm. In most case this default is reasonable. The <code>-l</code> option should be used only if you encounter problems with colors. By default, fvwm tries to detect large pre-allocated palettes. If such a palette is detected fvwm uses it and a priori the <code>-l</code> must not be used. Moreover, in this case the <code>-A</code> and <code>-S</code> options are forced. Note that XFree-4.2 pre-allocates 244 colors (if you use a driver with Render support) leaving only a few free colors. This may lead to some color problems (and nothing can be done). XFree-4.3 or better pre-allocate only 85 colors. If no pre-allocated palette is auto detected the defaults are as follow: </p>
<p> Display depth 8 (256 colors)</p>
<dl>
<dt>
<dd>
<pre>
<dl>
<dt><dd>PseudoColor: 68 (4x4x4 color cube + 4 grey)
GrayScale: 64 regular grey
DirectColor: 32 (3x3x3 color cube + 5 grey)
</pre>
</dl>
</dl>
<p> Display depth 4 (16 colors)</p>
<dl>
<dt>
<dd>
<pre>
<dl>
<dt><dd>PseudoColor: 10 (2x2x2 color cube + 2 grey)
GrayScale: 8 regular grey
DirectColor: 10 (2x2x2 color cube + 2 grey)
</pre>
</dl>
</dl>
<p> These defaults may change before version 2.6. Note that if you use a private color map (i.e., fvwm is started with the <code>-C</code> or the <code>-I</code> options), then other defaults are used. </p>
<p> Now what to do if you encounter problems with colors? The first thing to do is to check if you really cannot run your X server with depth 15, 16 or better. Check your X server documentation. Note that some hardware can support two different depths on the same screen (typically depth 8 and depth 24). If depth 8 is the default, you can force fvwm to use the best depth by using the <code>-C</code> option with <i>TrueColor</i> as argument. So now we assume that you are forced to run in depth 8 with a dynamic visual because your hardware/driver cannot do better or because you need to use an application which needs to run under this mode (e.g., because this application needs read-write colors). What it should be understand is that you have only 256 colors and that all the applications which use the default color map must share these colors. The main problem is that there are applications which use a lot or even all the colors. If you use such application you may have no more free colors and some applications (which used only a few colors) may fail to start or are unusable. There are three things that can be done (and fvwm does not really play a particular role, all applications are concerned). The first is to run the applications which waste your (default) color map with a private color map. For example, run netscape with the -install option, run KDE or QT applications with the &#8211;cmap option, use the <code>-C</code> option for fvwm. The disadvantage of this method is that it is visually disturbing (see the <code>ColormapFocus</code> command for a better control of the color maps switching). The second method is to limit the number of colors that the applications use. Again, some applications have options to specify a given color limit. With fvwm you may try various values, 61 (a special &quot;visual&quot; palette), 56 (a 4x4x3 color cube plus 6 grey), 29 (a 3x3x3 color cube plus 2 grey), 10 or 9. Also, you may use the <code>-L</code> option. However, limiting the number of colors is not the definitive solution. The definitive solution is to try cause applications which use a lot of colors use the same colors. This is a difficult task as there are no formal standards for this goal. However, some toolkits as QT and GTK use color cubes as palettes. So, the idea is to configure your applications/toolkits to all use the same color cube. Moreover, you can use the colors in this color cube in your X resources configuration files and/or as arguments to colors options. Fvwm can use any color cube of the form RxGxB with 2 &lt;= R &lt;= 6, R = G, R-1 =&lt; B &lt;= R and B &gt;= 2. To get an RxGxB color cube give an argument to <code>-l</code> an integer c &gt;= R*G*B and &lt; (R+1)*(G+1)*B if B=R and &lt; R*G*(B+1) if B &lt; R (and different from 61). If c &gt; R*G*B, then some grey may be added to the color cube. You can use the <code>PrintInfo</code> <i>Colors</i> [<i>1</i>] command to get information on your fvwm colors setting. In particular, this command prints the palette used by fvwm in rgb format (the last integer gives the number of times fvwm has allocated the colors).</dl>
<p> <code>-L</code> | <code>&#8211;strict-color-limit</code></p>
<dl>
<dt>
<dd> If the screen displays 256 colors (or less) and has a dynamic visual, causes fvwm to use its palette for all the colors. By default, the palette is used only for images and gradients.</dl>
<p> <code>-P</code> | <code>&#8211;visual-palette</code></p>
<dl>
<dt>
<dd> If the screen displays 256 colors (or less) and has a dynamic visual, this option causes fvwm to use a palette designed for limiting the &quot;visual&quot; color distance between the points of the palette. Moreover, for better color sharing, if possible colors with a name in the X rgb data base are used for defining the colors (with the hope that applications and images prefer to use named colors). If the <code>-l</code> option is not used this palette has 61 colors. This palette is also automatically selected if 61 or 9 is used as argument to the <code>-l</code> option.</dl>
<p> <code>-A</code> | <code>&#8211;allocate-palette</code></p>
<dl>
<dt>
<dd> If the screen displays 256 colors (or less) and has a dynamic visual this option causes fvwm to allocate all the colors of its palette at start up for reserving these colors for future use. This option forces the <code>-static-palette</code> option. By default, fvwm allocates (reserves) a color in its palette only if it needs this color.</dl>
<p> <code>-S</code> | <code>&#8211;static-palette</code></p>
<dl>
<dt>
<dd> If the screen displays 256 colors (or less) and has a dynamic visual this option causes fvwm to never free the colors in its palette. By default, when fvwm does not need a color any more it frees this color so that a new color can be used. This option may speed up image loading and save a few bits of memory.</dl>
<p> <code>-blackout</code></p>
<dl>
<dt>
<dd> This option is provided for backward compatibility only. Blacking out the screen during startup is not necessary (and doesn&#8217;t work) anymore. This option will be removed in the future.</dl>
<p> <code>&#8211;debug-stack-ring</code></p>
<dl>
<dt>
<dd> Enables stack ring debugging. This option is only intended for internal debugging and should only be used by developers.</dl>
<h2>ANATOMY OF A WINDOW</h2>
<p> Fvwm puts a decorative border around most windows. This border consists of a bar on each side and a small L-shaped section on each corner. There is an additional top bar called the title-bar which is used to display the name of the window. In addition, there are up to 10 title-bar buttons. The top, side, and bottom bars are collectively known as the side-bars. The corner pieces are called the frame. </p>
<p> With the built-in minimal configuration, dragging mouse button 1 in the frame or side-bars begins a resize operation on the window. Dragging mouse button 2 in the frame or side-bars begins a move operation. There are raise/lower operations bound to a single clicking on borders. Similarly for the window title. </p>
<p> Up to ten title-bar buttons may exist. Their use is completely user definable. One popular configuration uses one button on the left that is used to bring up a list of window options and two buttons on the right used to iconify and maximize the window. Another popular configuration adds a close button to the right. The number of title-bar buttons used depends on which ones have mouse actions bound to them. See the <code>Mouse</code> command.</p>
<h2>THE VIRTUAL DESKTOP</h2>
<p> Fvwm provides multiple virtual desktops for users who wish to use them. The screen is a viewport onto a <i>desktop</i> which may be larger than the screen. Several distinct desktops can be accessed (concept: one desktop for each project, or one desktop for each application, when view applications are distinct). Since each desktop can be larger than the physical screen, divided into m by n <i>pages</i> which are each the size of the physical screen, windows which are larger than the screen or large groups of related windows can easily be viewed. </p>
<p> The (m by n) size (i.e. number of pages) of the virtual desktops can be changed any time, by using the <code>DesktopSize</code> command. All virtual desktops must be (are) the same size. The total number of distinct desktops does not need to be specified, but is limited to approximately 4 billion total. All windows on a range of desktops can be viewed in the <code>FvwmPager</code>, a miniature view of the desktops. The pager is an accessory program, called a module, which is not essential for the window manager to operate. Windows may also be listed, along with their geometries, in a window list, accessible as a pop-up menu, or as a separate window, called the <code>FvwmWinList</code> (another module). </p>
<p> Fvwm keeps the windows on the desktop in a layered stacking order; a window in a lower layer never obscures a window in a higher layer. The layer of a window can be changed by using the <code>Layer</code> command. The concept of layers is a generalization of the <i>StaysOnTop</i> flag of older fvwm versions. The <i>StaysOnTop</i> and <i>StaysPut</i> <code>Style</code> options are now implemented by putting the windows in suitable layers and the previously missing <i>StaysOnBottom</i> <code>Style</code> option has been added. </p>
<p> <i>Sticky</i> windows are windows which transcend the virtual desktop by &quot;Sticking to the screen&#8217;s glass&quot;. They always stay put on the screen. This is convenient for things like clocks and xbiffs, so you only need to run one such gadget and it always stays with you. Icons can also be made to stick to the glass, if desired. </p>
<p> Window geometries are specified relative to the current viewport. That is: </p>
<dl>
<dt>
<dd>
<pre>
xterm -geometry +0+0
</pre>
</dl>
<p> creates a window in the upper left hand corner of the visible portion of the screen. It is permissible to specify geometries which place windows on the virtual desktop, but off the screen. For example, if the visible screen is 1000 by 1000 pixels, and the desktop size is 3&#215;3, and the current viewport is at the upper left hand corner of the desktop, invoking: </p>
<dl>
<dt>
<dd>
<pre>
xterm -geometry +1000+1000
</pre>
</dl>
<p> places a window just off of the lower right hand corner of the screen. It can be found by moving the mouse to the lower right hand corner of the screen and waiting for it to scroll into view. A geometry specified as something like: </p>
<dl>
<dt>
<dd>
<pre>
xterm -geometry -5-5
</pre>
</dl>
<p> places the window&#8217;s lower right hand corner 5 pixels from the lower right corner of the visible portion of the screen. Not all applications support window geometries with negative offsets. Some applications place the window&#8217;s upper right hand corner 5 pixels above and to the left of the upper left hand corner of the screen; others may do just plain bizarre things. </p>
<p> There are several ways to cause a window to map onto a desktop or page other than the currently active one. The geometry technique mentioned above (specifying x,y coordinates larger than the physical screen size), however, suffers from the limitation of being interpreted relative to the current viewport: the window may not consistently appear on a specific page, unless you always invoke the application from the same page. </p>
<p> A better way to place windows on a different page, screen or desk from the currently mapped viewport is to use the <i>StartsOnPage</i> or <i>StartsOnScreen</i> style specification (the successors to the older <i>StartsOnDesk</i> style) in your <i>config</i> file. The placement is consistent: it does not depend on your current location on the virtual desktop. </p>
<p> Some applications that understand standard Xt command line arguments and X resources, like xterm and xfontsel, allow the user to specify the start-up desk or page on the command line: </p>
<dl>
<dt>
<dd>
<pre>
xterm -xrm &quot;*Desk:1&quot;
</pre>
</dl>
<p> starts an xterm on desk number 1; </p>
<dl>
<dt>
<dd>
<pre>
xterm -xrm &quot;*Page:3 2 1&quot;
</pre>
</dl>
<p> starts an xterm two pages to the right and one down from the upper left hand page of desk number 3. Not all applications understand the use of these options, however. You could achieve the same results with the following lines in your <i>.Xdefaults</i> file: </p>
<dl>
<dt>
<dd>
<pre>
XTerm*Desk: 1
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
XTerm*Page: 3 2 1
</pre>
</dl>
<h2>USE ON MULTI-SCREEN DISPLAYS</h2>
<p> If the <code>-s</code> command line argument is not given, fvwm automatically starts up on every screen on the specified display. After fvwm starts each screen is treated independently. Restarts of fvwm need to be performed separately on each screen. The use of </p>
<dl>
<dt>
<dd>
<pre>
<code>EdgeScroll</code> 0 0
</pre>
</dl>
<p> is strongly recommended for multi-screen displays. You may need to quit on each screen to quit from the X session completely. This is not to be confused with Xinerama support.</p>
<h2>XINERAMA SUPPORT</h2>
<p> Fvwm supports the Xinerama extension of newer X servers which is similar to multi head support (multiple screens) but allows one to move windows between screens. If Xinerama support has been compiled into fvwm, it is used whenever fvwm runs on an X server that supports and uses multiple screens via Xinerama. Without this option, the whole desktop is treated as one big screen. For example, menus might pop up right between two screens. The <i>EdgeResistance</i> option of the <code>Style</code> command command allows for specifying an explicit resistance value for moving windows over the screen edge between two Xinerama screens. Xinerama support can be enabled or disabled on the fly or from the configuration file with the <code>Xinerama</code> command. Many modules and commands work nicely with Xinerama displays. </p>
<p> Whenever a geometry in the usual X format can be supplied, fvwm&#8217;s Xinerama extension allows for specifying a screen in addition to the geometry (or even the screen alone). To do this, a &#8216;@&#8217; is added to the end of the geometry string followed by either the screen number or a letter. A number is taken as the number of the Xinerama screen to be used (as configured in the X server). The letter can be one of &#8216;g&#8217; for the global screen (the rectangle that encloses all Xinerama screens), &#8216;p&#8217; for the primary screen (see below), &#8216;c&#8217; for the current screen (the one that currently contains the pointer). If the X server does not support Xinerama or only one screen is used, the screen bit is ignored. </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>IconBox</i> 64x300-0-0@p
</pre>
</dl>
<p> Xinerama support can be configured to use a primary screen. Fvwm can be configured to place new windows and icons on this screen. The primary screen is screen 0 by default but can be changed with the <code>XineramaPrimaryScreen</code> command. </p>
<p> Xinerama support was designed to work out of the box with the same configuration file that would work on a single screen. It may not perform very well if the involved screens use different screen resolutions. In this situation, windows may get stuck in the portion of the whole desktop that belongs to neither screen. When this happens, the windows or icons can be retrieved with the command </p>
<dl>
<dt>
<dd>
<pre>
<code>All</code> <code>MoveToScreen</code>
</pre>
</dl>
<p> that can be entered in an <code>FvwmConsole</code> window or with <code>FvwmCommand</code>. </p>
<p> For multi-screen implementations other than Xinerama, such as Single Logical Screen, it is possible to simulate a Xinerama configuration if the total screen seen by fvwm is made up of equal sized monitors in a rectangular grid. The commands <code>XineramaSls</code>, <code>XineramaSlsSize</code> and <code>XineramaSlsScreens</code> are used to configure this feature.</p>
<h2>INITIALIZATION</h2>
<p> During initialization, fvwm searches for a configuration file which describes key and button bindings, and many other things. The format of these files is described later. Fvwm first searches for configuration files using the command </p>
<dl>
<dt>
<dd>
<pre>
<code>Read</code> <i>config</i>
</pre>
</dl>
<p> This looks for file <i>config</i> in <i>$FVWM_USERDIR</i> and <i>$FVWM_DATADIR</i> directories, as described in <code>Read</code>. If this fails more files are queried for backward compatibility. Here is the complete list of all file locations queried in the default installation (only the first found file is used): </p>
<pre>
<dl>
<dt><dd><i>$HOME</i>/.fvwm/config
/usr/local/share/fvwm/config
</pre>
<pre>
<dt><dd><i>$HOME</i>/.fvwm/.fvwm2rc
<i>$HOME</i>/.fvwm2rc
/usr/local/share/fvwm/.fvwm2rc
/usr/local/share/fvwm/system.fvwm2rc
/etc/system.fvwm2rc
</pre>
</dl>
<p> Please note, the last 5 locations are not guaranteed to be supported in the future. </p>
<p> If a configuration file is not found, the left mouse button, or <font SIZE="-1">Help</font> or <font SIZE="-1">F1</font> keys on the root window bring up menus and forms that can create a starting configuration file. </p>
<p> Fvwm sets two environment variables which are inherited by its children. These are <i>$DISPLAY</i> which describes the display on which fvwm is running. <i>$DISPLAY</i> may be <i>unix:0.0</i> or <i>:0.0</i>, which doesn&#8217;t work too well when passed through ssh to another machine, so <i>$HOSTDISPLAY</i> is set to a network-ready description of the display. <i>$HOSTDISPLAY</i> always uses the TCP/IP transport protocol (even for a local connection) so <i>$DISPLAY</i> should be used for local connections, as it may use Unix-domain sockets, which are faster. </p>
<p> If you want to start some applications or modules with fvwm, you can simply put </p>
<dl>
<dt>
<dd>
<pre>
<code>Exec</code> app
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
<code>Module</code> FvwmXxx
</pre>
</dl>
<p> into your <i>config</i>, but it is not recommended; do this only if you know what you are doing. It is usually important to start applications or modules after the entire config is read, because it contains styles or module configurations which can affect window appearance and functionality. </p>
<p> The standard way to start applications or modules on fvwm&#8217;s start up is to add them to an initialization function (usually <code>StartFunction</code> or <code>InitFunction</code>). This way they are only started after fvwm finishes to read and execute <i>config</i> file. </p>
<p> Fvwm has three special functions for initialization: <code>StartFunction</code>, which is executed on startups and restarts; <code>InitFunction</code> and <code>RestartFunction</code>, which are executed during initialization and restarts (respectively) just after StartFunction. These functions may be customized in a user&#8217;s <i>config</i> file using the <code>AddToFunc</code> command (described later) to start up modules, xterms, or whatever you&#8217;d like to have started by fvwm. </p>
<p> Fvwm has also a special exit function: <code>ExitFunction</code>, executed when exiting or restarting before actually quitting. It could be used to explicitly kill modules, etc. </p>
<p> If fvwm is run under a session manager, functions <code>SessionInitFunction</code> and <code>SessionRestartFunction</code> are executed instead of InitFunction and RestartFunction. This helps to define the user&#8217;s <i>config</i> file to be good for both running under a session manager and without it. Generally it is a bad idea to start xterms or other applications in &quot;Session*&quot; functions. Also someone can decide to start different modules while running under a session manager or not. For the similar purposes <code>SessionExitFunction</code> is used instead of ExitFunction. </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyFunc</code> StartFunction
<code>AddToFunc</code> StartFunction
 + I <code>Module</code> <code>FvwmPager</code> * *
 + I <code>Module</code> <code>FvwmButtons</code>
<code>DestroyFunc</code> InitFunction
<code>AddToFunc</code> InitFunction
 + I <code>Module</code> <code>FvwmBanner</code>
 + I <code>Module</code> <code>FvwmTaskBar</code>
 + I <code>Exec</code> xsetroot -solid cyan
 + I <code>Exec</code> xterm
 + I <code>Exec</code> netscape
<code>DestroyFunc</code> RestartFunction
<code>AddToFunc</code> RestartFunction
 + I <code>Module</code> <code>FvwmTaskBar</code>
<code>DestroyFunc</code> SessionInitFunction
<code>AddToFunc</code> SessionInitFunction
 + I <code>Module</code> <code>FvwmBanner</code>
<code>DestroyFunc</code> SessionRestartFunction
<code>AddToFunc</code> SessionRestartFunction
 + I <code>Nop</code>
</pre>
</dl>
<p> You do not need to define all special functions if some are empty. Also note, all these special functions may be emulated now using <code>StartFunction</code> and <code>ExitFunction,</code> like this: </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyFunc</code> StartFunction
<code>AddToFunc</code> StartFunction
+ I <code>Test</code> (Init) <code>Module</code> <code>FvwmBanner</code>
+ I <code>Module</code> <code>FvwmPager</code> * *
+ I <code>Test</code> (Restart) <code>Beep</code>
<code>DestroyFunc</code> ExitFunction
<code>AddToFunc</code> ExitFunction
+ I <code>Test</code> (Quit) <code>Echo</code> Bye-bye
+ I <code>KillModule</code> MyBuggyModule
+ I <code>Test</code> (ToRestart) <code>Beep</code>
</pre>
</dl>
<h2>COMPILATION OPTIONS</h2>
<p> Fvwm has a number of compile-time options. If you have trouble using a certain command or feature, check to see if support for it was included at compile time. Optional features are described in the <i>config.h</i> file that is generated during compilation.</p>
<h2>ICONS AND IMAGES</h2>
<p> Fvwm can load <code>.xbm,</code> <code>.xpm,</code> <code>.png</code> and <code>.svg</code> images. <code>XBM</code> images are monochrome. Fvwm can always display <code>XBM</code> files. <code>XPM</code> and <code>PNG</code> formats are color images. SVG is a vector graphics image format. Compile-time options determine whether fvwm can display <code>XPM</code>, <code>PNG</code> or <code>SVG</code> icons and images. See the <i>INSTALL.fvwm</i> file for more information. </p>
<p> The related <code>SHAPE</code> compile-time option can make fvwm display spiffy shaped icons.</p>
<h3>SVG rendering options</h3>
<p> SVG images are generated from (XML) text files. A really simple SVG file might look something like this: </p>
<dl>
<dt>
<dd>
<pre>
&lt;svg width=&quot;120&quot; height=&quot;80&quot;&gt;
        &lt;rect fill=&quot;red&quot;     width=&quot;40&quot; height=&quot;40&quot;  x=&quot;0&quot;   y=&quot;0&quot;  /&gt;
        &lt;rect fill=&quot;lime&quot;    width=&quot;40&quot; height=&quot;40&quot;  x=&quot;40&quot;  y=&quot;0&quot;  /&gt;
        &lt;rect fill=&quot;blue&quot;    width=&quot;40&quot; height=&quot;40&quot;  x=&quot;80&quot;  y=&quot;0&quot;  /&gt;
        &lt;rect fill=&quot;cyan&quot;    width=&quot;40&quot; height=&quot;40&quot;  x=&quot;0&quot;   y=&quot;40&quot; /&gt;
        &lt;rect fill=&quot;magenta&quot; width=&quot;40&quot; height=&quot;40&quot;  x=&quot;40&quot;  y=&quot;40&quot; /&gt;
        &lt;rect fill=&quot;yellow&quot;  width=&quot;40&quot; height=&quot;40&quot;  x=&quot;80&quot;  y=&quot;40&quot; /&gt;
&lt;/svg&gt;
</pre>
</dl>
<p> By default, SVG images are rendered as the image creator intended them to. But since SVG is a vector graphics format, the images can be rendered at any chosen size and rotation, e.g. making it possible to use the same icon file rendered at diffrent sizes for the <i>Icon</i> and <i>MiniIcon</i> styles. </p>
<p> The rendering options are specified as a string appended to the SVG filename as follows:</p>
<dl>
<dt> <i>image.svg</i>:[!] [(1)&nbsp;<wbr><i>size</i>] [(2)&nbsp;<wbr><i>position</i>]&nbsp;<wbr>[(3)&nbsp;<wbr><i>rotation</i>]&nbsp;<wbr>[(4)&nbsp;<wbr><i>scale</i>] &#8230;</p>
<dt> (1) [-]<i>width</i>{x}[-]<i>height</i> </p>
<dt> (2) {- | +}<i>xpos</i>{- | +}<i>ypos</i> </p>
<dt> (3) @[-]<i>angle</i> </p>
<dt> (4) {* | /}[-]<i>factor</i>[x | y]</dl>
<dd>The option string always starts with a colon (&#8216;:&#8217;) to separate it from the filename. An empty option string can skip this colon, but it might still be a good idea to include it to prevent ambiguity if the filename contains any colon. </p>
<dl>
<dt>
<dd>
<pre>
filename_without_colon.svg
filename:with:colon.svg:
</pre>
</dl>
<p> An exclamation point (&#8216;!&#8217;) transposes the entire final image (including the rendering area), i.e. all the horizontal and all the vertical coordinates are swapped with each other. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:!
</pre>
</dl>
<p> <i>width</i> and <i>height</i> specifies the dimensions of the rendering area in pixels, i.e. the dimensions of the resulting image. The actual image is fitted to fill the entire rendering area. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:60x60
</pre>
</dl>
<p> Use a <i>width</i> or <i>height</i> value of 0 to keep the aspect ratio. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:0x60
image.svg:60x0
</pre>
</dl>
<p> A &#8216;-&#8216; before <i>width</i> mirrors the rendering area horizontally. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:-0x0
</pre>
</dl>
<p> A &#8216;-&#8216; before <i>height</i> mirrors the rendering area vertically. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:0x-0
</pre>
</dl>
<p> <i>xpos</i> and <i>ypos</i> specifies a translation of the image in pixels. A positive <i>xpos</i> value moves the image to the right. A positive <i>ypos</i> value moves it down. Moving it partially outside of the rendering area results in a cropped image. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:-30-0
image.svg:-0+10
image.svg:-30+10
</pre>
</dl>
<p> <i>angle</i> specifies a rotation around the actual image center in degrees. This might result in a cropped image. A positive value rotates the image clockwise. Floating point values are recognized. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:@180
image.svg:@-90
image.svg:@30
image.svg:@57.3
</pre>
</dl>
<p> <i>factor</i> specifes a scaling of the actual image (not the rendering area). Scaling it up results in a cropped image. Floting point values are recognized. Division by zero is ignored. If <i>factor</i> is directly followed by a &#8216;x&#8217; or a &#8216;y&#8217;, the scaling is horizontal or vertical respectively. Otherwise the scaling is uniform. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:*2
image.svg:/2
image.svg:/3x
image.svg:/2y
</pre>
</dl>
<p> Scaling down a translated or rotated image can prevent cropping. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:@30*0.6
</pre>
</dl>
<p> Repeated usage of translation, rotation, and scaling is allowed. Translation and rotation are additive. Scaling is multiplicative. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:*2/3
image.svg:/3x/2y
</pre>
</dl>
<p> When combining affine transformations, the scaling is always done first, then the rotation, and finally the translation. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:-30+10@30/3x/2y
</pre>
</dl>
<p> Use a negative scale <i>factor</i> to mirror the actual image. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:-30+10@30/-3x/2y
</pre>
</dl>
<p> Mirroring of the rendering area is done after any scaling, rotation or translation of the image. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:-0x0-30+10@30/3x/2y
</pre>
</dl>
<p> Transposing is done last of all, after everything else. </p>
<dl>
<dt>
<dd>
<pre>
image.svg:!-0x0-30+10@30/3x/2y
</pre>
</dl>
<h2>MODULES</h2>
<p> A module is a separate program which runs as a separate Unix process but transmits commands to fvwm to execute. Users can write their own modules to do any weird or bizarre manipulations without bloating or affecting the integrity of fvwm itself. </p>
<p> Modules must be spawned by fvwm so that it can set up two pipes for fvwm and the module to communicate with. The pipes are already open for the module when it starts and the file descriptors for the pipes are provided as command line arguments. </p>
<p> Modules can be spawned by fvwm at any time during the X session by use of the <code>Module</code> command. Modules can exist for the duration of the X session, or can perform a single task and exit. If the module is still active when fvwm is told to quit, then fvwm closes the communication pipes and waits to receive a SIGCHLD from the module, indicating that it has detected the pipe closure and has exited. If modules fail to detect the pipe closure fvwm exits after approximately 30 seconds anyway. The number of simultaneously executing modules is limited by the operating system&#8217;s maximum number of simultaneously open files, usually between 60 and 256. </p>
<p> Modules simply transmit commands to the fvwm command engine. Commands are formatted just as in the case of a mouse binding in the <i>config</i> setup file. Certain auxiliary information is also transmitted, as in the sample module <code>FvwmButtons</code>. </p>
<p> Please refer to the <code>Module Commands</code> section for details.</p>
<h2>ICCCM COMPLIANCE</h2>
<p> Fvwm attempts to be ICCCM 2.0 compliant. Check <i><a rel="nofollow" href="http://tronche.com/gui/x/icccm/">http://tronche.com/gui/x/icccm/</a></i> for more info. In addition, ICCCM states that it should be possible for applications to receive any keystroke, which is not consistent with the keyboard shortcut approach used in fvwm and most other window managers. In particular you cannot have the same keyboard shortcuts working with your fvwm and another fvwm running within Xnest (a nested X server running in a window). The same problem exists with mouse bindings. </p>
<p> The ICCCM states that windows possessing the property </p>
<dl>
<dt>
<dd>
<pre>
WM_HINTS(WM_HINTS):
    Client accepts input or input focus: False
</pre>
</dl>
<p> should not be given the keyboard input focus by the window manager. These windows can take the input focus by themselves, however. A number of applications set this property, and yet expect the window manager to give them the keyboard focus anyway, so fvwm provides a window style, <i>Lenience</i>, which allows fvwm to overlook this ICCCM rule. Even with this window style it is not guaranteed that the application accepts focus. </p>
<p> The differences between ICCCM 1.1 and 2.0 include the ability to take over from a running ICCCM 2.0 compliant window manager; thus </p>
<dl>
<dt>
<dd>
<pre>
fvwm; vi ~/.fvwm/config; fvwm -replace
</pre>
</dl>
<p> resembles the <code>Restart</code> command. It is not exactly the same, since killing the previously running wm may terminate your X session, if the wm was started as the last client in your <i>.Xclients</i> or <i>.Xsession</i> file. </p>
<p> Further additions are support for client-side colormap installation (see the ICCCM for details) and the urgency hint. Clients can set this hint in the WM_HINTS property of their window and expect the window manager to attract the user&#8217;s attention to the window. Fvwm has two re-definable functions for this purpose, &quot;UrgencyFunc&quot; and &quot;UrgencyDoneFunc&quot;, which are executed when the flag is set/cleared. Their default definitions are: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> UrgencyFunc
 + I <code>Iconify</code> off
 + I <code>FlipFocus</code>
 + I <code>Raise</code>
 + I <code>WarpToWindow !raise</code> 5p 5p
<code>AddToFunc</code> UrgencyDoneFunc
 + I <code>Nop</code>
</pre>
</dl>
<h2>GNOME COMPLIANCE</h2>
<p> Fvwm attempts to be GNOME (version 1) compliant. Check <i><a rel="nofollow" href="http://www.gnome.org">http://www.gnome.org</a></i> for what that may mean. To disable GNOME hints for some or all windows, the <i>GNOMEIgnoreHints</i> style can be used.</p>
<h2>EXTENDED WINDOW MANAGER HINTS</h2>
<p> Fvwm attempts to respect the extended window manager hints (ewmh or EWMH for short) specification: <i><a rel="nofollow" href="http://www.freedesktop.org/wiki/Standards_2fwm_2dspec">http://www.freedesktop.org/wiki/Standards_2fwm_2dspec</a></i> and some extensions of this specification. This allows fvwm to work with KDE version &gt;= 2, GNOME version 2 and other applications which respect this specification (any application based on <i>GTK+</i> version 2). Applications which respect this specification are called ewmh compliant applications. </p>
<p> This support is configurable with styles and commands. These styles and commands have EWMH as the prefix (so you can find them easily in this man page). </p>
<p> There is a new Context &#8216;D&#8217; for the <code>Key</code>, <code>PointerKey</code>, <code>Mouse</code> and <code>Stroke</code> commands. This context is for desktop applications (such as kdesktop and Nautilus desktop). </p>
<p> When a compliant taskbar asks fvwm to activate a window (typically when you click on a button which represents a window in such a taskbar), then fvwm calls the complex function <code>EWMHActivateWindowFunc</code> which by default is Iconify Off, Focus and Raise. You can redefine this function. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyFunc</code> EWMHActivateWindowFunc
<code>AddToFunc</code> EWMHActivateWindowFunc I <code>Iconify</code> Off
+ I <code>Focus</code>
+ I <code>Raise</code>
+ I <code>WarpToWindow</code> 50 50
</pre>
</dl>
<p> additionally warps the pointer to the center of the window. </p>
<p> The EWMH specification introduces the notion of Working Area. Without ewmh support the Working Area is the full visible screen (or all your screens if you have a multi head setup and you use Xinerama). However, compliant applications (such as a panel) can ask to reserve space at the edge of the screen. If this is the case, the Working Area is your full visible screen minus these reserved spaces. If a panel can be hidden by clicking on a button the Working Area does not change (as you can unhide the panel at any time), but the Dynamic Working Area is updated: the space reserved by the panel is removed (and added again if you pop up the panel). The Dynamic Working Area may be used when fvwm places or maximizes a window. To know if an application reserves space you can type &quot;xprop | grep _NET_WM_STRUT&quot; in a terminal and select the application. If four numbers appear then these numbers define the reserved space as explained in the <code>EwmhBaseStruts</code> command.</p>
<h2>MWM COMPATIBILITY</h2>
<p> Fvwm provides options to emulate Motif Window Manager (Mwm) as well as possible. Please refer to the <code>Emulate</code> command as well as to the Mwm specific options of the <code>Style</code> and <code>MenuStyle</code> commands for details.</p>
<h2>OPEN LOOK AND XVIEW COMPATIBILITY</h2>
<p> Fvwm supports all the Open Look decoration hints (except pushpins). Should you use any such application, please add the following line to your config: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>OLDecor</i>
</pre>
</dl>
<p> Most (perhaps all) Open Look applications have a strange notion of keyboard focus handling. Although a lot of work went into fvwm to work well with these, you may still encounter problems. It is recommended to use the <i>NeverFocus</i> focus policy and the <i>Lenience</i> style for all such applications (the windows still get the focus): </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> &lt;application name&gt; <i>NeverFocus</i>, <i>Lenience</i>
</pre>
</dl>
<p> But in case you can not live with that focus policy, you can try using one of the other focus policies in combination with the <i>Lenience</i> style: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> &lt;application name&gt; <i>MouseFocus</i>, <i>Lenience</i>
<code>Style</code> &lt;application name&gt; <i>SloppyFocus</i>, <i>Lenience</i>
<code>Style</code> &lt;application name&gt; <i>ClickToFocus</i>, <i>Lenience</i>
</pre>
</dl>
<h2>M4 PREPROCESSING</h2>
<p> M4 pre-processing is handled by a module in fvwm. To get more details, try man <code>FvwmM4</code>. In short, if you want fvwm to parse your files with m4, then replace the command <code>Read</code> with <code>FvwmM4</code> in your <i>~/.fvwm/config</i> file (if it appears at all), and start fvwm with the command </p>
<dl>
<dt>
<dd>
<pre>
fvwm -cmd &quot;<code>FvwmM4</code> config&quot;
</pre>
</dl>
<h2>CPP PREPROCESSING</h2>
<p> Cpp is the C-language pre-processor. fvwm offers cpp processing which mirrors the m4 pre-processing. To find out about it, re-read the <code>M4</code> section, but replace &quot;m4&quot; with &quot;cpp&quot;.</p>
<h2>CONFIGURATION</h2>
<h3>Configuration Files</h3>
<p> The configuration file is used to describe mouse and button bindings, colors, the virtual display size, and related items. The initialization configuration file is typically called <i>config</i> (or <i>.fvwm2rc</i>). By using the <code>Read</code> command, it is easy to read in new configuration files as you go. </p>
<p> Lines beginning with &#8216;#&#8217; are ignored by fvwm. Lines starting with &#8216;*&#8217; are expected to contain module configuration commands (rather than configuration commands for fvwm itself). Like in shell scripts embedded newlines in a configuration file line can be quoted by preceding them with a backslash. All lines linked in this fashion are treated as a single line. The newline itself is ignored. </p>
<p> Fvwm makes no distinction between configuration commands and action commands, so anything mentioned in the fvwm commands section can be placed on a line by itself for fvwm to execute as it reads the configuration file, or it can be placed as an executable command in a menu or bound to a mouse button or a keyboard key. It is left as an exercise for the user to decide which function make sense for initialization and which ones make sense for run-time.</p>
<h3>Supplied Configuration</h3>
<p> A sample configuration file, <i>system.fvwm2rc</i>, is supplied with the fvwm distribution. It is well commented and can be used as a source of examples for fvwm configuration. It may be copied to <i>/usr/local/share/fvwm/config</i> file. </p>
<p> Alternatively, the built-in menu (accessible when no configuration file is found) has options to create an initial config file for the user. </p>
<p> If you are new to fvwm, try <i>fvwm-themes</i>[] package demonstrating the powerful fvwm functionality.</p>
<h2>FONTS</h2>
<h3>Font names and font loading</h3>
<p> The fonts used for the text of a window title, icon titles, menus and geometry window can be specified by using the Font and IconFont <code>Style</code>, the Font <code>MenuStyle</code> and the <code>DefaultFont</code> commands. Also, all the Modules which use text have configuration command(s) to specify font(s). All these styles and commands take a font name as an argument. This section explains what is a font name for fvwm and which fonts fvwm loads. </p>
<p> First, you can use what we can call a usual font name, for example, </p>
<dl>
<dt>
<dd>
<pre>
-adobe-courier-bold-r-normal--10-100-75-75-m-60-ISO8859-1
-adobe-courier-bold-r-normal--10-*
-*-fixed-medium-o-normal--14-*-ISO8859-15
</pre>
</dl>
<p> That is, you can use an X Logical Font Description (XLFD for short). Then the &quot;first&quot; font which matches the description is loaded and used. This &quot;first&quot; font depends of your font path and also of your locale. Fonts which match the locale charset are loaded in priority order. For example with </p>
<dl>
<dt>
<dd>
<pre>
-adobe-courier-bold-r-normal--10-*
</pre>
</dl>
<p> if the locale charset is ISO8859-1, then fvwm tries to load a font which matches </p>
<dl>
<dt>
<dd>
<pre>
-adobe-courier-bold-r-normal--10-*-ISO8859-1
</pre>
</dl>
<p> with the locale charset ISO8859-15 fvwm tries to load </p>
<dl>
<dt>
<dd>
<pre>
-adobe-courier-bold-r-normal--10-*-ISO8859-15.
</pre>
</dl>
<p> A font name can be given as an extended XLFD. This is a comma separated list of (simple) XLFD font names, for example: </p>
<dl>
<dt>
<dd>
<pre>
-adobe-courier-bold-r-normal--14-*,-*-courier-medium-r-normal--14-*
</pre>
</dl>
<p> Each simple font name is tried until a matching font with the locale charset is found and if this fails each simple font name is tried without constraint on the charset. </p>
<p> More details on the XLFD can be found in the X manual page, the X Logical Font Description Conventions document (called xlfd) and the XLoadFont and XCreateFontSet manual pages. Some useful font utilities are: xlsfonts, xfontsel, xfd and xset. </p>
<p> If you have Xft support you can specify an Xft font name (description) of a true type (or Type1) font prefixed by &quot;xft:&quot;, for example: </p>
<dl>
<dt>
<dd>
<pre>
&quot;xft:Luxi Mono&quot;
&quot;xft:Luxi Mono:Medium:Roman:size=14:encoding=iso8859-1&quot;
</pre>
</dl>
<p> The &quot;first&quot; font which matches the description is loaded. This first font depends on the XftConfig configuration file with Xft1 and on the /etc/fonts/fonts.conf file with Xft2. One may read the Xft manual page and the fontconfig man page with Xft2. The first string which follows &quot;xft:&quot; is always considered as the family. With the second example Luxi Mono is the Family (Other XFree TTF families: &quot;Luxi Serif&quot;, &quot;Luxi Sans&quot;), Medium is the Weight (other possible weights: Light, DemiBold, Bold, Black), Roman is the slant or the style (other possibilities: Regular, Oblique, Italic) size specifies the point size (for a pixel size use pixelsize=), encoding allows for enforce a charset (iso8859-1 or iso10646-1 only; if no encoding is given the locale charset is assumed). An important parameter is &quot;minspace=bool&quot; where bool is True or False. If bool is False (the default?) Xft gives a greater font height to fvwm than if bool is True. This may modify text placement, icon and window title height, line spacing in menus and <code>FvwmIdent</code>, button height in some fvwm modules &#8230;etc. With a LCD monitor you may try to add &quot;rgba=mode&quot; where mode is either rgb, bgr, vrgb or vbgr to enable subpixel rendering. The best mode depends on the way your LCD cells are arranged. You can pass other specifications in between &quot;:&quot;, as &quot;foundry=foundry_name&quot;, &quot;spacing=type&quot; where type can be monospace, proportional or charcell, &quot;charwidth=integer&quot;, &quot;charheight=integer&quot; or &quot;antialias=bool&quot; where bool is True or False. It seems that these parameters are not always taken in account. </p>
<p> To determine which Xft fonts are really loaded you can export XFT_DEBUG=1 before starting fvwm and take a look to the error log. With Xft2 you may use fc-list to list the available fonts. Anyway, Xft support is experimental (from the X and the fvwm point of view) and the quality of the rendering depends on number of parameters (the XFree and the freetype versions and your video card(s)). </p>
<p> After an Xft font name you can add after a &quot;;&quot; an XLFD font name (simple or extended) as: </p>
<dl>
<dt>
<dd>
<pre>
xft:Verdana:pixelsize=14;-adobe-courier-bold-r-normal--14-*
</pre>
</dl>
<p> then, if either loading the Xft font fails or fvwm has no Xft support, fvwm loads the font &quot;-adobe-courier-bold-r-normal&#8211;14-*&quot;. This allows for writing portable configuration files.</p>
<h3>Font and string encoding</h3>
<p> Once a font is loaded, fvwm finds its encoding (or charset) using its name (the last two fields of the name). fvwm assumes that the strings which are displayed with this font use this encoding (an exception is that if an iso10646-1 font is loaded, then UTF-8 is assumed for string encoding). In a normal situation, (i) a font is loaded by giving a font name without specifying the encoding, (ii) the encoding of the loaded font is the locale encoding, and then (iii) the strings in the fvwm configuration files should use the locale encoding as well as the window and icon name. With Xft the situation is bit different as Xft supports only iso10646-1 and iso8859-1. If you do not specify one of these encodings in the Xft font name, then fvwm does strings conversion using (iii). Note that with multibyte fonts (and in particular with &quot;CJK&quot; fonts) for good text rendering, the locale encoding should be the charset of the font. </p>
<p> To override the previous rules, it is possible to specify the string encoding in the beginning of a font description as follow: </p>
<dl>
<dt>
<dd>
<pre>
StringEncoding=<i>enc</i>:_full_font_name_
</pre>
</dl>
<p> where <i>enc</i> is an encoding supported by fvwm (usually font name charset plus some unicode encodings: UTF-8, USC-2, USC-4 and UTF-16). </p>
<p> For example, you may use an iso8859-1 locale charset and have an <code>FvwmForm</code> in Russian using koi8-r encoding. In this case, you just have to ask <code>FvwmForm</code> to load a koi8-r font by specifying the encoding in the font name. With a multibyte language, (as multibyte font works well only if the locale encoding is the charset of the font), you should use an iso10646-1 font: </p>
<dl>
<dt>
<dd>
<pre>
StringEncoding=jisx0208.1983-0:-*-fixed-medium-r-*-ja-*-iso10646-1
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
&quot;StringEncoding=jisx0208.1983-0:xft:Bitstream Cyberbit&quot;
</pre>
</dl>
<p> if your <code>FvwmForm</code> configuration uses jisx0208.1983-0 encoding. Another possibility is to use UTF-8 encoding for your <code>FvwmForm</code> configuration and use an iso10646-1 font: </p>
<dl>
<dt>
<dd>
<pre>
-*-fixed-medium-r-*-ja-*-iso10646-1
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
&quot;StringEncoding=UTF-8:xft:Bitstream Cyberbit&quot;
</pre>
</dl>
<p> or equivalently </p>
<dl>
<dt>
<dd>
<pre>
&quot;xft:Bitstream Cyberbit:encoding=iso10646-1&quot;
</pre>
</dl>
<p> In general iso10646-1 fonts together with UTF-8 string encoding allows the display of any characters in a given menu, <code>FvwmForm</code> etc. </p>
<p> More and more, unicode is used and text files use UTF-8 encoding. However, in practice the characters used range over your locale charset (this is the case when you generate a menu with fvwm-menu-desktop with recent versions of KDE and GNOME). For saving memory (an iso10646-1 font may have a very large number of characters) or because you have a pretty font without an iso10646-1 charset, you can specify the string encoding to be UTF-8 and use a font in the locale charset: </p>
<dl>
<dt>
<dd>
<pre>
StringEncoding=UTF-8:-*-pretty_font-*-12-*
</pre>
</dl>
<p> In most cases, fvwm correctly determines the encoding of the font. However, some fonts do not end with valid encoding names. When the font name isn&#8217;t normal, for example: </p>
<dl>
<dt>
<dd>
<pre>
-misc-fixed-*--20-*-my_utf8-36
</pre>
</dl>
<p> you need to add the encoding after the font name using a slash as a delimiter. For example: </p>
<dl>
<dt>
<dd>
<pre>
<code>MenuStyle</code> * <i>Font</i> -misc-fixed-*--20-*-my_utf8-36/iso10646-1
</pre>
</dl>
<p> If fvwm finds an encoding, fvwm uses the iconv system functions to do conversion between encodings. Unfortunately, there are no standards. For conversion between iso8859-1 and UTF-8: a GNU system uses &quot;ISO-8859-1&quot; and other systems use &quot;iso881&quot; to define the converters (these two names are supported by fvwm). Moreover, in some cases it may be necessary to use machine specific converters. So, if you experience problems you can try to get information on your iconv implementation (&quot;man iconv&quot; may help) and put the name which defines the converter between the font encoding and UTF-8 at the end of the font name after the encoding hint and a / (another possible solution is to use GNU libiconv). For example use: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>Font</i> -misc-fixed-*--14-*-iso8859-1/*/latin1
</pre>
</dl>
<p> to use latin1 for defining the converter for the iso8859-1 encoding. The &quot;*&quot; in between the &quot;/&quot; says to fvwm to determine the encoding from the end of the font name. Use: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>Font</i> \
        -misc-fixed-*--14-*-local8859-6/iso8859-6/local_iso8859_6_iconv
</pre>
</dl>
<p> to force fvwm to use the font with iso8859-6 as the encoding (this is useful for bi-directionality) and to use local_iso8859_6_iconv for defining the converters.</p>
<h3>Font Shadow Effects</h3>
<p> Fonts can be given 3d effects. At the beginning of the font name (or just after a possible StringEncoding specification) add </p>
<dl>
<dt>
<dd>
<pre><code>
Shadow=size [offset] [directions]]:
</code></pre>
</dl>
<p> <i>size</i> is a positive integer which specifies the number of pixels of shadow. <i>offset</i> is an optional positive integer which defines the number of pixels to offset the shadow from the edge of the character. The default offset is zero. <i>directions</i> is an optional set of directions the shadow emanates from the character. The <i>directions</i> are a space separated list of fvwm directions: </p>
<p> <i>N</i>, <i>North</i>, <i>Top</i>, <i>t</i>, <i>Up</i>, <i>u</i>, <i>&#8211;</i> </p>
<p> <i>E</i>, <i>East</i>, <i>Right</i>, <i>r</i>, <i>Right</i>, <i>r</i>, <i>]</i> </p>
<p> <i>S</i>, <i>South</i>, <i>Bottom</i>, <i>b</i>, <i>Down</i>, <i>d</i>, <i>_</i> </p>
<p> <i>W</i>, <i>West</i>, <i>Left</i>, <i>l</i>, <i>Left</i>, <i>l</i>, <i>[</i> </p>
<p> <i>NE</i>, <i>NorthEast</i>, <i>TopRight</i>, <i>tr</i>, <i>UpRight</i>, <i>ur</i>, <i>^</i> </p>
<p> <i>SE</i>, <i>SouthEast</i>, <i>BottomRight</i>, <i>br</i>, <i>DownRight</i>, <i>dr</i>, <i>&gt;</i> </p>
<p> <i>SW</i>, <i>SouthWest</i>, <i>BottomLeft</i>, <i>bl</i>, <i>DownLeft</i>, <i>dl</i>, <i>v</i> </p>
<p> <i>NW</i>, <i>NorthWest</i>, <i>TopLeft</i>, <i>tl</i>, <i>UpLeft</i>, <i>ul</i>, <i>&lt;</i> </p>
<p> <i>C</i>, <i>Center</i>, <i>Centre</i>, <i>.</i> </p>
<p> A shadow is displayed in each given direction. <i>All</i> is equivalent to all the directions. The default <i>direction</i> is <i>BottomRight</i>. With the <i>Center</i> direction, the shadow surrounds the whole string. Since this is a super set of all other directions, it is a waste of time to specify this along with any other directions. </p>
<p> The shadow effect only works with colorsets. The color of the shadow is defined by using the <i>fgsh</i> option of the <code>Colorset</code> command. Please refer to the <code>Colorsets</code> section for details about colorsets. </p>
<p> Note: It can be difficult to find the font, <i>fg</i>, <i>fgsh</i> and <i>bg</i> colors to make this effect look good, but it can look quite good.</p>
<h2>BI-DIRECTIONAL TEXT</h2>
<p> Arabic and Hebrew text require bi-directional text support to be displayed correctly, this means that logical strings should be converted before their visual presentation, so left-to-right and right-to-left sub-strings are determined and reshuffled. In fvwm this is done automatically in window titles, menus, module labels and other places if the fonts used for displaying the text are of one of the charsets that require <i>bidi</i> (bi-directional) support. For example, this includes iso8859-6, iso8859-8 and iso10646-1 (unicode), but not other iso8859-* fonts. </p>
<p> This bi-directional text support is done using the <i>fribidi</i> library compile time option, see <i>INSTALL.fvwm</i>.</p>
<h2>KEYBOARD SHORTCUTS</h2>
<p> Almost all window manager operations can be performed from the keyboard so mouse-less operation should be possible. In addition to scrolling around the virtual desktop by binding the <code>Scroll</code> command to appropriate keys, <code>Popup</code>, <code>Move</code>, <code>Resize</code>, and any other command can be bound to keys. Once a command is started the pointer is moved by using the up, down, left, and right arrows, and the action is terminated by pressing return. Holding down the <font SIZE="-1">Shift</font> key causes the pointer movement to go in larger steps and holding down the <font SIZE="-1">control</font> key causes the pointer movement to go in smaller steps. Standard emacs and vi cursor movement controls ( <font SIZE="-1">n</font> , <font SIZE="-1">p</font> , <font SIZE="-1">f</font> , <font SIZE="-1">b</font> , and <font SIZE="-1">j</font> , <font SIZE="-1">k</font> , <font SIZE="-1">h</font> , <font SIZE="-1">l</font> ) can be used instead of the arrow keys.</p>
<h2>SESSION MANAGEMENT</h2>
<p> Fvwm supports session management according to the X Session Management Protocol. It saves and restores window position, size, stacking order, desk, stickiness, shadiness, maximizedness, iconifiedness for all windows. Furthermore, some global state is saved. </p>
<p> Fvwm doesn&#8217;t save any information regarding styles, decors, functions or menus. If you change any of these resources during a session (e.g. by issuing <code>Style</code> commands or by using various modules), these changes are lost after saving and restarting the session. To become permanent, such changes have to be added to the configuration file. </p>
<p> Note further that the current implementation has the following anomaly when used on a multi-screen display: Starting fvwm for the first time, fvwm manages all screens by forking a copy of itself for each screen. Every copy knows its parent and issuing a <code>Quit</code> command to any instance of fvwm kills the master and thus all copies of fvwm. When you save and restart the session, the session manager brings up a copy of fvwm on each screen, but this time they are started as individual instances managing one screen only. Thus a <code>Quit</code> kills only the copy it was sent to. This is probably not a very serious problem, since with session management, you are supposed to quit a session through the session manager anyway. If it is really needed, </p>
<dl>
<dt>
<dd>
<pre>
<code>Exec</code> exec killall fvwm
</pre>
</dl>
<p> still kills all copies of fvwm. Your system must have the <code>killall</code> command though.</p>
<h2>BOOLEAN ARGUMENTS</h2>
<p> A number of commands take one or several boolean arguments. These take a few equivalent inputs: &quot;yes&quot;, &quot;on&quot;, &quot;true&quot;, &quot;t&quot; and &quot;y&quot; all evaluate to true while &quot;no&quot;, &quot;off&quot;, &quot;false&quot;, &quot;f&quot; and &quot;n&quot; evaluate to false. Some commands allow &quot;toggle&quot; too which means that the feature is disabled if it is currently enabled and vice versa.</p>
<h2>BUILTIN KEY AND MOUSE BINDINGS</h2>
<p> The following commands are built-in to fvwm: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> Help R A <code>Popup</code> MenuFvwmRoot
<code>Key</code> F1 R A <code>Popup</code> MenuFvwmRoot
<code>Key</code> Tab A M <code>WindowList</code> Root c c NoDeskSort
<code>Key</code> Escape A MC <code>EscapeFunc</code>
<code>Mouse</code> 1 R A <code>Menu</code> MenuFvwmRoot
<code>Mouse</code> 1 T   A FuncFvwmRaiseLowerX <code>Move</code>
<code>Mouse</code> 1 FS  A FuncFvwmRaiseLowerX <code>Resize</code>
<code>Mouse</code> 2 FST A FuncFvwmRaiseLowerX <code>Move</code>
<code>AddToFunc</code> FuncFvwmRaiseLowerX
+ I <code>Raise</code>
+ M $0
+ D <code>Lower</code>
</pre>
</dl>
<p> The <font SIZE="-1">Help</font> and <font SIZE="-1">F1</font> keys invoke a built-in menu that fvwm creates. This is primarily for new users that have not created their own configuration file. Either key on the root (background) window pops up an menu to help you get started. </p>
<p> The <font SIZE="-1">Tab</font> key pressed anywhere with the <font SIZE="-1">Meta</font> key (same as the <font SIZE="-1">Alt</font> key on PC keyboards) held down pop-ups a window list. </p>
<p> Mouse button 1 on the title-bar or side frame can move, raise or lower a window. </p>
<p> Mouse button 1 on the window corners can resize, raise or lower a window. </p>
<p> You can override or remove these bindings. To remove the window list binding, use this: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> Tab A M -
</pre>
</dl>
<h2>COMMAND EXECUTION</h2>
<h3>Module and Function Commands</h3>
<p> If fvwm encounters a command that it doesn&#8217;t recognize, it checks to see if the specified command should have been </p>
<dl>
<dt>
<dd>
<pre>
<code>Function</code> (rest of command)
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
<code>Module</code> (rest of command)
</pre>
</dl>
<p> This allows complex functions or modules to be invoked in a manner which is fairly transparent to the configuration file. </p>
<p> Example: the <i>config</i> file contains the line </p>
<dl>
<dt>
<dd>
<pre>
HelpMe
</pre>
</dl>
<p> Fvwm looks for an fvwm command called &quot;HelpMe&quot;, and fails. Next it looks for a user-defined complex function called &quot;HelpMe&quot;. If no such function exists, fvwm tries to execute a module called &quot;HelpMe&quot;.</p>
<h3>Delayed Execution of Commands</h3>
<p> Note: There are many commands that affect look and feel of specific, some or all windows, like <code>Style</code>, <code>Mouse</code>, <code>Colorset</code>, <code>TitleStyle</code> and many others. For performance reasons such changes are not applied immediately but only when fvwm is idle, i.e. no user interaction or module input is pending. Specifically, new <code>Style</code> options that are set in a function are not applied until after the function has completed. This can sometimes lead to unwanted effects. </p>
<p> To force that all pending changes are applied immediately, use the <code>UpdateStyles</code>, <code>Refresh</code> or <code>RefreshWindow</code> commands.</p>
<h2>QUOTING</h2>
<p> Quotes are required only when needed to make fvwm consider two or more words to be a single argument. Unnecessary quoting is allowed. If you want a quote character in your text, you must escape it by using the backslash character. For example, if you have a pop-up menu called &quot;Window-Ops&quot;, then you do not need quotes: </p>
<dl>
<dt>
<dd>
<pre>
<code>Popup</code> Window-Ops
</pre>
</dl>
<p> but if you replace the dash with a space, then you need quotes: </p>
<dl>
<dt>
<dd>
<pre>
<code>Popup</code> &quot;Window Ops&quot;
</pre>
</dl>
<p> The supported quoting characters are double quotes, single quotes and reverse single quotes. All three kinds of quotes are treated in the same way. Single characters can be quoted with a preceding backslash. Quoting single characters works even inside other kinds of quotes.</p>
<h2>COMMAND EXPANSION</h2>
<p> Whenever an fvwm command line is executed, fvwm performs parameter expansion. A parameter is a &#8216;$&#8217; followed by a word enclosed in brackets ($[&#8230;]) or a single special character. If fvwm encounters an unquoted parameter on the command line it expands it to a string indicated by the parameter name. Unknown parameters are left untouched. Parameter expansion is performed before quoting. To get a literal &#8216;$&#8217; use &quot;$$&quot;. </p>
<p> If a command is prefixed with a &#8216;-&#8216; parameter expansion isn&#8217;t performed. This applies to the command immediately following the &#8216;-&#8216;, in which the expansion normally would have taken place. When uesed together with other prefix commands it must be added before the other prefix. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Pick</code> -<code>Exec</code> exec xmessage '$[w.name]'
</pre>
</dl>
<p> opens an xmessage dialog with &quot;$[w.name]&quot; unexpanded. </p>
<p> The longer variables may contain additional variables inside the name, which are expanded before the outer variable. </p>
<p> In earlier versions of fvwm, some single letter variables were supported. It is deprecated now, since they cause a number of problems. You should use the longer substitutes instead. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
#Print the current desk number, horizontal page number<br />
#and the window&#8217;s class (unexpanded here, no window).<br />
Echo $[desk.n] $[page.nx] $[w.class]
</dl>
<p> Note: If the command is called outside a window context, it prints &quot;$[w.class]&quot; instead of the class name. It is usually not enough to have the pointer over a window to have a context window. To force using the window with the focus, the <code>Current</code> command can be used: </p>
<dl>
<dt>
<dd>
Current Echo $[desk.n] $[page.nx] $[w.class]
</dl>
<p> The parameters known by fvwm are: </p>
<p> $$</p>
<dl>
<dt>
<dd> A literal &#8216;$&#8217;.</dl>
<p> $.</p>
<dl>
<dt>
<dd> The absolute directory of the currently Read file. Intended for creating relative and relocatable configuration trees. If used outside of any read file, the returned value is &#8216;.&#8217;.</dl>
<p> $0 to $9</p>
<dl>
<dt>
<dd> The positional parameters given to a complex function (a function that has been defined with the <code>AddToFunc</code> command). &quot;$0&quot; is replaced with the first parameter, &quot;$1&quot; with the second parameter and so on. If the corresponding parameter is undefined, the &quot;$&#8230;&quot; is deleted from the command line.</dl>
<p> $*</p>
<dl>
<dt>
<dd> All positional parameters given to a complex function. This includes parameters that follow after &quot;$9&quot;.</dl>
<p> $[<i>n</i>]</p>
<dl>
<dt>
<dd> The <i>n</i>:th positional parameter given to a complex function, counting from 0. If the corresponding parameter is undefined, the &quot;$[<i>n</i>]&quot; is deleted from the command line. The parameter is expanded unquoted.</dl>
<p> $[<i>n</i>&#8211;<i>m</i>]</p>
<dl>
<dt>
<dd> The positional parameters given to a complex function, starting with parameter <i>n</i> and ending with parameter <i>m</i>. If all the corresponding parameters are undefined, the &quot;$[&#8230;]&quot; is deleted from the command line. If only some of the parameters are defined, all defined parameters are expanded, and the remaining silently ignored. All parameters are expanded unquoted.</dl>
<p> $[<i>n</i>-]</p>
<dl>
<dt>
<dd> All the positional parameters given to a complex function, starting with parameter <i>n</i>. If all the corresponding parameters are undefined, the &quot;$[&#8230;]&quot; is deleted from the command line. All parameters are expanded unquoted.</dl>
<p> $[*]</p>
<dl>
<dt>
<dd> All the positional parameters given to a complex function. This is equivalent of $[0-].</dl>
<p> $[version.num]</p>
<dl>
<dt>
<dd> The version number, like &quot;2.6.0&quot;.</dl>
<p> $[version.info]</p>
<dl>
<dt>
<dd> The version info, like &quot; (from cvs)&quot;, empty for the official releases.</dl>
<p> $[version.line]</p>
<dl>
<dt>
<dd> The first line printed by the &#8211;version command line option.</dl>
<p> $[vp.x] $[vp.y] $[vp.width] $[vp.height]</p>
<dl>
<dt>
<dd> Either coordinate or the width or height of the current viewport.</dl>
<p> $[wa.x] $[wa.y] $[wa.width] $[wa.height]</p>
<dl>
<dt>
<dd> Either coordinate or the width or height of the EWMH working area.</dl>
<p> $[dwa.x] $[dwa.y] $[dwa.width] $[dwa.height]</p>
<dl>
<dt>
<dd> Either coordinate or the width or height of the dynamic EWMH working area.</dl>
<p> $[desk.n]</p>
<dl>
<dt>
<dd> The current desk number.</dl>
<p> $[desk.name&lt;n&gt;]</p>
<dl>
<dt>
<dd> These parameters are replaced with the name of the desktop number &lt;n&gt; that is defined with the <code>DesktopName</code> command. If no name is defined, then the default name is returned.</dl>
<p> $[desk.width] $[desk.height]</p>
<dl>
<dt>
<dd> The width or height of the whole desktop, i.e. the width or height multiplied by the number of pages in x or y direction.</dl>
<p> $[desk.pagesx] $[desk.pagesy]</p>
<dl>
<dt>
<dd> The number of total pages in a desk in x or y direction. This is the same as the values set by <code>DesktopSize</code>.</dl>
<p> $[page.nx] $[page.ny]</p>
<dl>
<dt>
<dd> The current page numbers, by X and Y axes, starting from 0. <i>page</i> is equivalent to <i>area</i> in the GNOME terminology.</dl>
<p> $[w.id]</p>
<dl>
<dt>
<dd> The window-id (expressed in hex, e.g. 0x10023c) of the window the command was called for or &quot;$[w.id]&quot; if no window is associated with the command.</dl>
<p> $[w.name] $[w.iconname] $[w.class] $[w.resource] $[w.visiblename] $[w.iconfile] $[w.miniiconfile] $[w.iconfile.svgopts] $[w.miniiconfile.svgopts]</p>
<dl>
<dt>
<dd> The window&#8217;s name, icon name, resource class and resource name, visible name, file name of its icon or mini icon defined with the <i>Icon</i> or <i>MiniIcon</i> style (including the full path if the file was found on disk), and (if fvwm is compiled with SVG support) the icon or mini icon svg rendering options (including the leading colon), or unexpanded &quot;$[w.&lt;attribute&gt;]&quot; string if no window is associated with the command. </p>
<p> Note, the first 5 variables may include any kind of characters, so these variables are quoted. It means that the value is surrounded by single quote characters and any contained single quote is prefixed with a backslash. This guarantees that commands like: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> $[w.resource] <i>Icon</i> norm/network.png
</pre>
</dl>
<p> work correctly, regardless of any special symbols the value may contain, like spaces and different kinds of quotes. </p>
<p> In the case of the window&#8217;s visible name, this is the value returned from the literal title of the window shown in the titlebar. Typically this will be the same as $[w.name] once expanded, although in the case of using <i>IndexedWindowName</i> then this is more useful a distinction, and allows for referencing the specific window by its visible name for inclusion in things like <code>Style</code> commands.</dl>
<p> $[w.x] $[w.y] $[w.width] $[w.height]</p>
<dl>
<dt>
<dd> Either coordinate or the width or height of the current window if it is not iconified. If no window is associated with the command or the window is iconified, the string is left as is.</dl>
<p> $[w.desk]</p>
<dl>
<dt>
<dd> The number of the desk on which the window is shown. If the window is sticky the current desk number is used.</dl>
<p> $[w.layer]</p>
<dl>
<dt>
<dd> The layer of the window.</dl>
<p> $[cw.x] $[cw.y] $[cw.width] $[cw.height]</p>
<dl>
<dt>
<dd> These work like $[w&#8230;.] but return the geometry of the client part of the window. In other words: the border and title of the window is not taken into account.</dl>
<p> $[i.x], $[it.x], $[ip.x] $[i.y], $[it.y], $[ip.y] $[i.width], $[it.width], $[ip.width] $[i.height], $[it.height], $[ip.height]</p>
<dl>
<dt>
<dd> These work like $[w&#8230;.] but return the geometry of the icon ($[i&#8230;.]), the icon title ($[it&#8230;.]) or the icon picture ($[ip&#8230;.]).</dl>
<p> $[pointer.x] $[pointer.y]</p>
<dl>
<dt>
<dd> These return the position of the pointer on the screen. If the pointer is not on the screen, these variables are not expanded.</dl>
<p> $[pointer.wx] $[pointer.wy]</p>
<dl>
<dt>
<dd> These return the position of the pointer in the selected window. If the pointer is not on the screen, the window is iconified or no window is selected, these variables are not expanded.</dl>
<p> $[pointer.cx] $[pointer.cy]</p>
<dl>
<dt>
<dd> These return the position of the pointer in the client portion of the selected window. If the pointer is not on the screen, the window is shaded or iconified or no window is selected, these variables are not expanded.</dl>
<p> $[pointer.screen]</p>
<dl>
<dt>
<dd> The screen number the pointer is currently on. Returns 0 if Xinerama is not enabled.</dl>
<p> $[screen]</p>
<dl>
<dt>
<dd> The screen number fvwm is running on. Useful for setups with multiple screens.</dl>
<p> $[fg.cs&lt;n&gt;] $[bg.cs&lt;n&gt;] $[hilight.cs&lt;n&gt;] $[shadow.cs&lt;n&gt;]</p>
<dl>
<dt>
<dd> These parameters are replaced with the name of the foreground (fg), background (bg), hilight (hilight) or shadow (shadow) color that is defined in colorset &lt;n&gt; (replace &lt;n&gt; with zero or a positive integer). For example &quot;$[fg.cs3]&quot; is expanded to the name of the foreground color of colorset 3 (in rgb:rrrr/gggg/bbbb form). Please refer to the <code>Colorsets</code> section for details about colorsets.</dl>
<p> $[schedule.last]</p>
<dl>
<dt>
<dd> This is replaced by the id of the last command that was scheduled with the <code>Schedule</code> command, even if this command was already executed.</dl>
<p> $[schedule.next]</p>
<dl>
<dt>
<dd> This is replaced by the id the next command used with <code>Schedule</code> will get (unless a different id is specified explicitly).</dl>
<p> $[cond.rc]</p>
<dl>
<dt>
<dd> The return code of the last conditional command. This variable is only valid inside a function and can not be used in a conditional command. Please refer to the section <code>Conditional Commands</code> in the command list.</dl>
<p> $[func.context]</p>
<dl>
<dt>
<dd> The context character of the running command as used in the <code>Mouse</code>, <code>Key</code> or <code>PointerKey</code> command. This is useful for example with: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 3 FS N <code>WindowShade</code> $$[func.context]
</pre>
</dl>
</dl>
<p> $[gt.<i>str</i>]</p>
<dl>
<dt>
<dd> return the translation of <i>str</i> by looking in the current locale catalogs. If no translation is found <i>str</i> is returned as is. See the <code>LocalePath</code> command.</dl>
<p> $[infostore.<i>key</i>]</p>
<dl>
<dt>
<dd> Return the value of the item stored in the InfoStore at the given <i>key</i>. If no key is present, the unexpanded string is returned.</dl>
<p> $[&#8230;]</p>
<dl>
<dt>
<dd> If the string within the braces is neither of the above, fvwm tries to find an environment variable with this name and replaces its value if one is found (e.g. &quot;$[PAGER]&quot; could be replaced by &quot;more&quot;). Otherwise the string is left as is.</dl>
<p> Some examples can be found in the description of the <code>AddToFunc</code> command.</p>
<h2>SCRIPTING &amp; COMPLEX FUNCTIONS</h2>
<p> To achieve the more complex effects, fvwm has a number of commands that improve its scripting abilities. Scripts can be read from a file with <code>Read</code>, from the output of a command with <code>PipeRead</code> or written as a complex function with the <code>AddToFunc</code> command. For the curious, section 7 of the fvwm FAQ shows some real life applications of scripting. Please refer to the sections <code>User Functions and Shell Commands</code> and <code>Conditional Commands</code> for details. A word of warning: during execution of complex functions, fvwm needs to take all input from the mouse pointer (the pointer is &quot;grabbed&quot; in the slang of X). No other programs can receive any input from the pointer while a function is run. This can confuse some programs. For example, the xwd program refuses to make screen shots when run from a complex function. To achieve the same functionality you can use the <code>Read</code> or <code>PipeRead</code> command instead.</p>
<h2>LIST OF FVWM COMMANDS</h2>
<p> The command descriptions below are grouped together in the following sections. The sections are hopefully sorted in order of usefulness to the newcomer. </p>
<dl>
<dt>
<dd> &bull;<code>Menu commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Miscellaneous commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands affecting window movement and placement</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands for focus and mouse movement</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands controlling window state</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands for mouse, key and stroke bindings</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>The Style command (controlling window styles)</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Other commands controlling window styles</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands controlling the virtual desktop</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Commands for user functions and shell commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Conditional commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Module commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Quit, restart and session management commands</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Colorsets</code> </p>
</dl>
<dl>
<dt>
<dd> &bull;<code>Color gradients</code> </p>
</dl>
<h3>Menus</h3>
<p> Before a menu can be opened, it has to be populated with menu items using the <code>AddToMenu</code> command and bound to a key or mouse button with the <code>Key</code>, <code>PointerKey</code> or <code>Mouse</code> command (there are many other ways to invoke a menu too). This is usually done in the configuration file. </p>
<p> Fvwm menus are extremely configurable in look and feel. Even the slightest nuances can be changed to the user&#8217;s liking, including the menu item fonts, the background, delays before popping up sub menus, generating menus dynamically and many other features. Please refer to the <code>MenuStyle</code> command to learn more.</p>
<dl>
<dt><code>Types of Menus</code></p>
<dd>
<dl>
<dt>
<dd> In fvwm there are four slightly different types of menus: </p>
<p> <code>Popup</code> menus can appear everywhere on the screen on their own or attached to a part of a window. The <code>Popup</code> command opens popup menus. If the popup menu was invoked with a mouse button held down, it is closed when the button is released. The item under the pointer is then activated and the associated action is executed. </p>
<p> <code>Menu</code> is a very similar command, but the menus it opens are slightly less transient. When invoked by clicking a mouse button, it stays open and can be navigated with no button held. But if it is invoked by a button press followed by mouse motion, it behaves exactly like a popup menu. </p>
<p> <i>Tear off menus</i> or <i>Pin up menus</i> are menus from either of the above two commands that have been &quot;torn off&quot; their original context and pinned on the desktop like a normal window. They are created from other menus by certain key presses or mouse sequences or with the <code>TearMenuOff</code> command from inside a menu. </p>
<p> <i>Sub menus</i> are menus inside menus. When a menu item that has the <code>Popup</code> command as its action is selected, the named menu is opened as an inferior menu to the parent. Any type of menu can have sub menus.</dl>
<dt><code>Menu Anatomy</code></p>
<dd>
<dl>
<dt>
<dd> Menus consist of any number of titles which are inactive menu items that usually appear at the top of the menu, normal items triggering various actions when selected, separator lines between the items, tear off bars (a horizontal broken line) that tear off the menu when selected, and sub menu items indicated with a triangle pointing left or right, depending on the direction in which the sub menu appears. All the above menu items are optional. </p>
<p> Additionally, if the menu is too long to fit on the screen, the excess menu items are put in a continuation menu and a sub menu with the string &quot;More&#8230;&quot; is placed at the bottom of the menu. The &quot;More&#8230;&quot; string honors the locale settings. </p>
<p> Finally, there may be a picture running up either side of the menu (a &quot;side bar&quot;).</dl>
<dt><code>Menu Navigation</code></p>
<dd>
<dl>
<dt>
<dd> Menus can be navigated either with the keyboard or with the mouse. Many people prefer to use the mouse, but it can be rather tedious. Once you get the hang of it, keyboard navigation can be much faster. While fvwm displays a menu, it can do nothing else. For example, new windows do not appear before the menu is closed. However, this is not exactly true for tear off menus. See the <code>Tear Off Menus</code> section for details.</dl>
<dt><code>Mouse Navigation</code></p>
<dd>
<dl>
<dt>
<dd> Moving the pointer over a menu selects the item below it. Normally this is indicated by a 3d border around the item, but not all parts of a menu can be selected. Pressing any mouse button while a menu is open by default activates the item below it. Items of a popup menu are also activated by releasing a held mouse button. In case of an item that hides a sub menu, the sub menu is displayed if the pointer hovers over the item long enough or moves close to the triangle indicating the sub menu. This behaviour can be tuned with menu styles. </p>
<p> Scrolling a mouse wheel over a menu either wraps the pointer along the menu (default), scrolls the menu under the pointer or act as if the menu was clicked depending on the <i>MouseWheel</i> menu style. </p>
<p> Clicking on a selected item activates it &#8211; what happens exactly depends on the type of the item. </p>
<p> Clicking on a title, a separator, the side bar, or outside the menu closes the menu (exception: tear off menus can not be closed this way). Pressing mouse button 2 over a menu title or activating a tear off bar creates a tear off menu from the current menu. Clicking on a normal menu item invokes the command that is bound to it, and clicking on a sub menu item either closes all open menus and replaces them with the sub menu or posts the menu (default). </p>
<p> Posting menus is meant to ease mouse navigation. Once a sub menu is posted, only items from that sub menu can be selected. This can be very useful to navigate the menu if the pointer tends to stray off the menu. To unpost the menu and revert back to normal operation, either click on the same sub menu item or press any key.</dl>
<dt><code>Keyboard Navigation</code></p>
<dd>
<dl>
<dt>
<dd> Just like with mouse navigation, the item below the pointer is selected. This is achieved by warping the pointer to the menu items when necessary. While a menu is open, all key presses are intercepted by the menu. No other application can get keyboard input (although this is not the case for tear off menus). </p>
<p> Items can be selected directly by pressing a hotkey that can be configured individually for each menu item. The hotkey is indicated by underlining it in the menu item label. With the <i>AutomaticHotkeys</i> menu style fvwm automatically assigns hotkeys to all menu items. </p>
<p> The most basic keys to navigate through menus are the cursor keys (move up or down one item, enter or leave a sub menu), <font SIZE="-1">Space</font> (activate item) and <font SIZE="-1">Escape</font> (close menu). Numerous other keys can be used to navigate through menus by default: </p>
<p> <i>Enter</i>, <i>Return</i>, <i>Space</i> activate the current item. </p>
<p> <i>Escape</i>, <i>Delete</i>, <i>Ctrl-G</i> exit the current sequence of menus or destroy a tear off menu. </p>
<p> <i>J</i>, <i>N</i>, <i>Cursor-Down</i>, <i>Tab</i>, <i>Meta-Tab</i>, <i>Ctrl-F</i>, move to the next item. </p>
<p> <i>K</i>, <i>P</i>, <i>Cursor-Up</i>, <i>Shift-Tab</i>, <i>Shift-Meta-Tab</i>, <i>Ctrl-B</i>, move to the prior item. </p>
<p> <i>L</i>, <i>Cursor-Right</i>, <i>F</i> enter a sub menu. </p>
<p> <i>H</i>, <i>Cursor-Left</i>, <i>B</i> return to the prior menu. </p>
<p> <i>Ctrl-Cursor-Up</i>, <i>Ctrl-K</i> <i>Ctrl-P</i>, <i>Shift-Ctrl-Meta-Tab</i>, <i>Page-Up</i> move up five items. </p>
<p> <i>Ctrl-Cursor-Down</i>, <i>Ctrl-J</i> <i>Ctrl-N</i>, <i>Ctrl-Meta-Tab</i> <i>Page-Down</i> move down five items. </p>
<p> <i>Shift-P</i>, <i>Home</i>, <i>Shift-Cursor-Up</i>, <i>Ctrl-A</i> move to the first item. </p>
<p> <i>Shift-N</i>, <i>End</i>, <i>Shift-Cursor-Down</i>, <i>Ctrl-E</i> move to the last item. </p>
<p> <i>Meta-P</i>, <i>Meta-Cursor-Up</i>, <i>Ctrl-Cursor-Left</i>, <i>Shift-Ctrl-Tab</i>, move up just below the next separator. </p>
<p> <i>Meta-N</i>, <i>Meta-Cursor-Down</i>, <i>Ctrl-Cursor-Right</i>, <i>Ctrl-Tab</i>, move down just below the next separator. </p>
<p> <i>Insert</i> opens the &quot;More&#8230;&quot; sub menu if any. </p>
<p> <i>Backspace</i> tears off the menu.</dl>
<dt><code>Menu Bindings</code></p>
<dd>
<dl>
<dt>
<dd> The keys and mouse buttons used to navigate the menu can be configured using the <code>Key</code> and <code>Mouse</code> commands with the special context &#8216;M&#8217;, possible combined with &#8216;T&#8217; for the menu title, &#8216;I&#8217; for other menu items, &#8216;S&#8217; for any border or sidepic, &#8216;[&#8216; for left border including a left sidepic, &#8216;]&#8217; for right border including a right sidepic, &#8216;-&#8216; for top border, &#8216;_&#8217; for bottom border. The menu context uses its own set of actions that can be bound to keys and mouse buttons. These are <i>MenuClose</i>, <i>MenuCloseAndExec</i>, <i>MenuEnterContinuation</i>, <i>MenuEnterSubmenu</i>, <i>MenuLeaveSubmenu</i>, <i>MenuMoveCursor</i>, <i>MenuCursorLeft</i>, <i>MenuCursorRight</i>, <i>MenuSelectItem</i>, <i>MenuScroll</i> and <i>MenuTearOff</i>. </p>
<p> It is not possible to override the key Escape with no modifiers for closing the menu. Neither is it possible to undefine mouse button 1, the arrow keys or the enter key for minimal navigation. </p>
<p> <code>MenuClose</code> exits from the current sequence of menus or destroys a tear off menu. </p>
<p> <code>MenuCloseAndExec</code> exits from the current sequence of menus or destroys a tear off menu and executes the rest of the line as a command. </p>
<p> <code>MenuEnterContinuation</code> opens the &quot;More&#8230;&quot; sub menu if any. </p>
<p> <code>MenuEnterSubmenu</code> enters a sub menu. </p>
<p> <code>MenuLeaveSubmenu</code> returns to the prior menu. </p>
<p> <code>MenuMoveCursor</code> <i>n</i> [<i>m</i>] moves the selection to another item. If the first argument is zero the second argument specifies an absolute item in the menu to move the pointer to. Negative items are counted from the end of the menu. If the first argument is non-zero, the second argument must be omitted, and the first argument specifies a relative change in the selected item. The positions may be suffixed with a &#8216;s&#8217; to indicate that the items should refer only to the first items after separators. </p>
<p> <code>MenuCursorLeft</code> enters a sub menu with the <i>SubmenusLeft</i> menu style, and returns to the prior menu with the <i>SubmenusRight</i> menu style. </p>
<p> <code>MenuCursorRight</code> enters a sub menu with the <i>SubmenusRight</i> menu style, and returns to the prior menu with the <i>SubmenusLeft</i> menu style. </p>
<p> <code>MenuSelectItem</code> triggers the action for the menu item. </p>
<p> <code>MenuScroll </code><i>n</i> performs menu scrolling according to the <i>MouseWheel</i> menu style with <i>n</i> items. The distance can be suffixed with an &#8216;s&#8217; to indicate the items should refer only to the first items after separators. </p>
<p> <code>MenuTearOff</code> turns a normal menu into a &quot;torn off&quot; menu. See <code>Tear Off Menus</code> for details.</dl>
<dt><code>Tear Off Menus</code></p>
<dd>
<dl>
<dt>
<dd> A tear off menu is any menu that has been &quot;torn off&quot; the window it was attached to and pinned to the root window. There are three ways to tear off a menu: click on the menu title with mouse button 2, press <font SIZE="-1">Backspace</font> in the menu or activate its tear off bar (a horizontal bar with a broken line). Tear off bars must be added to the menu as any other item by assigning them the command <code>TearMenuOff</code>. </p>
<p> The builtin tear off actions can be overridden by undefining the builtin menu actions bound to tear off. To remove the builtin mouse button 2 binding, use: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 2 MT A -
</pre>
</dl>
<p> and to remove the builtin backspace binding, use: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> Backspace M A -
</pre>
</dl>
<p> See the section <code>Menu Bindings</code> for details on how to assign other bindings for tear off. </p>
<p> Note that prior to fvwm 2.5.20 the tear off mouse bindings were redefined in different way, which no longer work. </p>
<p> The window containing the menu is placed as any other window would be. If you find it confusing to have your tear off menus appear at random positions on the screen, put this line in your configuration file: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> fvwm_menu <i>UsePPosition</i>
</pre>
</dl>
<p> To remove borders and buttons from a tear-off menu but keep the menu title, you can use </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> fvwm_menu !<i>Button</i> 0, !<i>Button</i> 1
<code>Style</code> fvwm_menu !<i>Button</i> 2, !<i>Button</i> 3
<code>Style</code> fvwm_menu !<i>Button</i> 4, !<i>Button</i> 5
<code>Style</code> fvwm_menu !<i>Button</i> 6, !<i>Button</i> 7
<code>Style</code> fvwm_menu !<i>Button</i> 8, !<i>Button</i> 9
<code>Style</code> fvwm_menu <i>Title</i>, <i>HandleWidth</i> 0
</pre>
</dl>
<p> A tear off menu is a cross breeding between a window and a menu. The menu is swallowed by a window and its title is stripped off and displayed in the window title. The main advantage is that the menu becomes permanent &#8211; activating an item does not close the menu. Therefore, it can be used multiple times without reopening it. To destroy such a menu, close its window or press the <font SIZE="-1">Escape</font> key. </p>
<p> Tear off menus behave somewhat differently than normal menus and windows. They do not take the keyboard focus, but while the pointer is over one of them, all key presses are sent to the menu. Other fvwm key bindings are disabled as long as the pointer is inside the tear off menu or one of its sub menus. When the pointer leaves this area, all sub menus are closed immediately. Note that the window containing a tear off menu is never hilighted as if it had the focus. </p>
<p> A tear off menu is an independent copy of the menu it originated from. As such, it is not affected by adding items to that menu or changing its menu style. </p>
<p> To create a tear off menu without opening the normal menu first, the option <i>TearOffImmediately</i> can be added to the <code>Menu</code> or <code>Popup</code> command.</dl>
<dt><code>AddToMenu</code> <i>menu-name</i> [<i>menu-label</i>&nbsp;<wbr><i>action</i>]</p>
<dd>
<dl>
<dt>
<dd> Begins or adds to a menu definition. Typically a menu definition looks like this: </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu Utilities Utilities <code>Title</code>
 + Xterm           <code>Exec</code>  exec xterm -e tcsh
 + Rxvt            <code>Exec</code>  exec rxvt
 + &quot;Remote Logins&quot; <code>Popup</code> Remote-Logins
 + Top             <code>Exec</code>  exec rxvt -T Top -n Top -e top
 + Calculator      <code>Exec</code>  exec xcalc
 + Xman            <code>Exec</code>  exec xman
 + Xmag            <code>Exec</code>  exec xmag
 + emacs           <code>Exec</code>  exec xemacs
 + Mail            MailFunction xmh &quot;-font fixed&quot;
 + &quot;&quot;              <code>Nop</code>
 + Modules         <code>Popup</code> Module-Popup
 + &quot;&quot;              <code>Nop</code>
 + Exit Fvwm       <code>Popup</code> Quit-Verify
</pre>
</dl>
<p> The menu could be invoked via </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 R A <code>Menu</code> Utilities Nop
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 R A <code>Popup</code> Utilities
</pre>
</dl>
<p> There is no end-of-menu symbol. Menus do not have to be defined in a contiguous region of the <i>config</i> file. The quoted (or first word) portion in the above examples is the menu label, which appears in the menu when the user pops it up. The remaining portion is an fvwm command which is executed if the user selects that menu item. An empty menu-label (&quot;&quot;) and the <code>Nop</code> function are used to insert a separator into the menu. </p>
<p> The keywords <i>DynamicPopUpAction</i> and <i>DynamicPopDownAction</i> have a special meaning when used as the name of a menu item. The action following the keyword is executed whenever the menu is popped up or down. This way you can implement dynamic menus. It is even possible to destroy itself with <code>DestroyMenu</code> and the rebuild from scratch. When the menu has been destroyed (unless you used the <i>recreate</i> option when destroying the menu), do not forget to add the dynamic action again. </p>
<p> Note: Do not trigger actions that require user interaction. They may fail and may screw up your menus. See the <code>Silent</code> command. </p>
<p> <code>Warning</code> Do not issue <code>MenuStyle</code> commands as dynamic menu actions. Chances are good that this crashes fvwm. </p>
<p> There are several configurable scripts installed together with fvwm for automatic menu generation. They have their own man pages. Some of them, specifically <code>fvwm-menu-directory</code> and <code>fvwm-menu-desktop</code>, may be used with <i>DynamicPopupAction</i> to create a directory listing or GNOME/KDE application listing. </p>
<p> Example (File browser): </p>
<dl>
<dt>
<dd>
<pre>
# You can find the shell script fvwm_make_browse_menu.sh
# in the utils/ directory of the distribution.
AddToMenu BrowseMenu
+ DynamicPopupAction <code>PipeRead</code> \
  'fvwm_make_browse_menu.sh BrowseMenu'
</pre>
</dl>
<p> Example (Picture menu): </p>
<dl>
<dt>
<dd>
<pre>
# Build a menu of all .jpg files in
# $HOME/Pictures
AddToMenu JpgMenu foo title
+ DynamicPopupAction <code>Function</code> MakeJpgMenu
<code>AddToFunc</code> MakeJpgMenu
+ I <code>DestroyMenu</code> recreate JpgMenu
+ I AddToMenu JpgMenu Pictures <code>Title</code>
+ I <code>PipeRead</code> 'for i in <i>$HOME</i>/Pictures/*.jpg; \
  do echo AddToMenu JpgMenu &quot;`basename $i`&quot; <code>Exec</code> xv $i; done'
</pre>
</dl>
<p> The keyword <i>MissingSubmenuFunction</i> has a similar meaning. It is executed whenever you try to pop up a sub menu that does not exist. With this function you can define and destroy menus on the fly. You can use any command after the keyword, but if the name of an item (that is a submenu) defined with <code>AddToFunc</code> follows it, fvwm executes this command: </p>
<dl>
<dt>
<dd>
<pre>
<code>Function</code> &lt;function-name&gt; &lt;submenu-name&gt;
</pre>
</dl>
<p> i.e. the name is passed to the function as its first argument and can be referred to with &quot;$0&quot;. </p>
<p> The <code>fvwm-menu-directory</code> script mentioned above may be used with <i>MissingSubmenuFunction</i> to create an up to date recursive directory listing. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
#There is another shell script fvwm_make_directory_menu.sh<br />
#in the utils / directory of the distribution.To use it,<br />
#define this function in your configuration file:<br />
DestroyFunc MakeMissingDirectoryMenu<br />
        AddToFunc MakeMissingDirectoryMenu +<br />
    I PipeRead fvwm_make_directory_menu.sh $0<br />
        DestroyMenu SomeMenu<br />
            AddToMenu SomeMenu +<br />
    MissingSubmenuFunction MakeMissingDirectoryMenu + &#8220;Root directory&#8221; Popup /
</dl>
<p> This is another implementation of the file browser that uses sub menus for subdirectories. </p>
<p> Titles can be used within the menu. If you add the option <i>top</i> behind the keyword <code>Title</code>, the title is added to the top of the menu. If there was a title already, it is overwritten. </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu Utilities Tools Title top
</pre>
</dl>
<p> All text up to the first <font SIZE="-1">Tab</font> in the menu label is aligned to the left side of the menu, all text right of the first <font SIZE="-1">Tab</font> is aligned to the left in a second column and all text thereafter is placed right aligned in the third column. All other <font SIZE="-1">Tab</font> s are replaced by spaces. Note that you can change this format with the <i>ItemFormat</i> option of the <code>MenuStyle</code> command. </p>
<p> If the menu-label contains an ampersand (&#8216;&amp;&#8217;), the next character is taken as a hot-key for the menu item. Hot-keys are underlined in the label. To get a literal &#8216;&amp;&#8217;, insert &quot;&amp;&amp;&quot;. Pressing the hot-key moves through the list of menu items with this hot-key or selects an item that is the only one with this hot-key. </p>
<p> If the menu-label contains a sub-string which is set off by stars, then the text between the stars is expected to be the name of an image file to insert in the menu. To get a literal &#8216;*&#8217;, insert &quot;**&quot;. For example </p>
<dl>
<dt>
<dd>
<pre>
+ Calculator*xcalc.xpm* <code>Exec</code> exec xcalc
</pre>
</dl>
<p> inserts a menu item labeled &quot;Calculator&quot; with a picture of a calculator above it. The following: </p>
<dl>
<dt>
<dd>
<pre>
+ *xcalc.xpm*           <code>Exec</code> exec xcalc
</pre>
</dl>
<p> Omits the &quot;Calculator&quot; label, but leaves the picture. </p>
<p> If the menu-label contains a sub-string which is set off by percent signs, then the text between the percent signs is expected to be the name of image file (a so called mini icon to insert to the left of the menu label. A second mini icon that is drawn at the right side of the menu can be given in the same way. To get a literal &#8216;%&#8217;, insert &quot;%%&quot;. For example </p>
<dl>
<dt>
<dd>
<pre>
+ Calculator%xcalc.xpm% <code>Exec</code> exec xcalc
</pre>
</dl>
<p> inserts a menu item labeled &quot;Calculator&quot; with a picture of a calculator to the left. The following: </p>
<dl>
<dt>
<dd>
<pre>
+ %xcalc.xpm%           <code>Exec</code> exec xcalc
</pre>
</dl>
<p> Omits the &quot;Calculator&quot; label, but leaves the picture. The pictures used with this feature should be small (perhaps 16&#215;16). </p>
<p> If the menu-name (not the label) contains a sub-string which is set off by at signs (&#8216;@&#8217;), then the text between them is expected to be the name of an image file to draw along the left side of the menu (a side pixmap). You may want to use the <i>SidePic</i> option of the <code>MenuStyle</code> command instead. To get a literal &#8216;@&#8217;, insert &quot;@@&quot;. For example </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu StartMenu [at] linux-menu.xpm@
</pre>
</dl>
<p> creates a menu with a picture in its bottom left corner. </p>
<p> If the menu-name also contains a sub-string surrounded by &#8216;^&#8217;s, then the text between &#8216;^&#8217;s is expected to be the name of an X11 color and the column containing the side picture is colored with that color. You can set this color for a menu style using the <i>SideColor</i> option of the <code>MenuStyle</code> command. To get a literal &#8216;^&#8217;, insert &quot;^^&quot;. Example: </p>
<dl>
<dt>
<dd>
<pre>
AddToMenu StartMenu [at] linux-menu.xpm@^blue^
</pre>
</dl>
<p> creates a menu with a picture in its bottom left corner and colors with blue the region of the menu containing the picture. </p>
<p> In all the above cases, the name of the resulting menu is name specified, stripped of the substrings between the various delimiters.</dl>
<dt><code>ChangeMenuStyle</code> <i>menustyle</i> <i>menu</i> &#8230;</p>
<dd>
<dl>
<dt>
<dd> Changes the menu style of <i>menu</i> to <i>menustyle</i>. You may specify more than one menu in each call of <code>ChangeMenuStyle</code>.</dl>
<dt><code>CopyMenuStyle</code> <i>orig-menustyle</i> <i>dest-menustyle</i></p>
<dd>
<dl>
<dt>
<dd> Copy <i>orig-menustyle</i> to <i>dest-menustyle</i>, where <i>orig-menustyle</i> is an existing menu style. If the menu style <i>dest_menustyle</i> does not exist, then it is created.</dl>
<dt><code>DestroyMenu</code> [recreate] <i>menu</i></p>
<dd>
<dl>
<dt>
<dd> Deletes a menu, so that subsequent references to it are no longer valid. You can use this to change the contents of a menu during an fvwm session. The menu can be rebuilt using <code>AddToMenu</code>. The optional parameter <i>recreate</i> tells fvwm not to throw away the menu completely but to throw away all the menu items (including the title). </p>
<dl>
<dt>
<dd>
<pre>
DestroyMenu Utilities
</pre>
</dl>
</dl>
<dt><code>DestroyMenuStyle</code> <i>menustyle</i></p>
<dd>
<dl>
<dt>
<dd> Deletes the menu style named <i>menustyle</i> and changes all menus using this style to the default style, you cannot destroy the default menu style. </p>
<dl>
<dt>
<dd>
<pre>
DestroyMenuStyle pixmap1
</pre>
</dl>
</dl>
<dt><code>Menu</code> <i>menu-name</i> [<i>position</i>] [<i>double-click-action</i>]</p>
<dd>
<dl>
<dt>
<dd> Causes a previously defined menu to be popped up in a sticky manner. That is, if the user invokes the menu with a click action instead of a drag action, the menu stays up. The command <i>double-click-action</i> is invoked if the user double-clicks a button (or hits the key rapidly twice if the menu is bound to a key) when bringing up the menu. If the double click action is not specified, double clicking on the menu does nothing. However, if the menu begins with a menu item (i.e. not with a title or a separator) and the double click action is not given, double clicking invokes the first item of the menu (but only if the pointer really was over the item). </p>
<p> The pointer is warped to where it was when the menu was invoked if it was both invoked and closed with a keystroke. </p>
<p> The <i>position</i> arguments allow placement of the menu somewhere on the screen, for example centered on the visible screen or above a title bar. Basically it works like this: you specify a <i>context-rectangle</i> and an offset to this rectangle by which the upper left corner of the menu is moved from the upper left corner of the rectangle. The <i>position</i> arguments consist of several parts:</p>
<dl>
<dt> [<i>context-rectangle</i>] <i>x</i> <i>y</i> [<i>special-options</i>]</dl>
<dd>The <i>context-rectangle</i> can be one of: </p>
<p> <i>Root</i></p>
<dl>
<dt>
<dd> the root window of the current screen.</dl>
<p> <i>XineramaRoot</i></p>
<dl>
<dt>
<dd> the root window of the whole Xinerama screen. Equivalent to &quot;root&quot; when Xinerama is not used.</dl>
<p> <i>Mouse</i></p>
<dl>
<dt>
<dd> a 1&#215;1 rectangle at the mouse position.</dl>
<p> <i>Window</i></p>
<dl>
<dt>
<dd> the frame of the context window.</dl>
<p> <i>Interior</i></p>
<dl>
<dt>
<dd> the inside of the context window.</dl>
<p> <i>Title</i></p>
<dl>
<dt>
<dd> the title of the context window or icon.</dl>
<p> <i>Button</i>&lt;n&gt;</p>
<dl>
<dt>
<dd> button #n of the context window.</dl>
<p> <i>Icon</i></p>
<dl>
<dt>
<dd> the icon of the context window.</dl>
<p> <i>Menu</i></p>
<dl>
<dt>
<dd> the current menu.</dl>
<p> <i>Item</i></p>
<dl>
<dt>
<dd> the current menu item.</dl>
<p> <i>Context</i></p>
<dl>
<dt>
<dd> the current window, menu or icon.</dl>
<p> <i>This</i></p>
<dl>
<dt>
<dd> whatever widget the pointer is on (e.g. a corner of a window or the root window).</dl>
<p> <i>Rectangle</i> &lt;<i>geometry</i>&gt;</p>
<dl>
<dt>
<dd> the rectangle defined by &lt;<i>geometry</i>&gt; in X geometry format. Width and height default to 1 if omitted.</dl>
<p> If the context-rectangle is omitted or illegal (e.g. &quot;item&quot; on a window), &quot;Mouse&quot; is the default. Note that not all of these make sense under all circumstances (e.g. &quot;Icon&quot; if the pointer is on a menu). </p>
<p> The offset values <i>x</i> and <i>y</i> specify how far the menu is moved from its default position. By default, the numeric value given is interpreted as a percentage of the context rectangle&#8217;s width (height), but with a trailing &#8216;<i>m</i>&#8216; the menu&#8217;s width (height) is used instead. Furthermore a trailing &#8216;<i>p</i>&#8216; changes the interpretation to mean pixels. </p>
<p> Instead of a single value you can use a list of values. All additional numbers after the first one are separated from their predecessor by their sign. Do not use any other separators. </p>
<p> If <i>x</i> or <i>y</i> are prefixed with &quot;&#8217;<i>o</i>&lt;number&gt;&quot; where &lt;number&gt; is an integer, the menu and the rectangle are moved to overlap at the specified position before any other offsets are applied. The menu and the rectangle are placed so that the pixel at &lt;number&gt; percent of the rectangle&#8217;s width/height is right over the pixel at &lt;number&gt; percent of the menu&#8217;s width/height. So &quot;o0&quot; means that the top/left borders of the menu and the rectangle overlap, with &quot;o100&quot; it&#8217;s the bottom/right borders and if you use &quot;o50&quot; they are centered upon each other (try it and you will see it is much simpler than this description). The default is &quot;o0&quot;. The prefix &quot;o&lt;number&gt;&quot; is an abbreviation for &quot;+&lt;number&gt;-&lt;number&gt;m&quot;. </p>
<p> A prefix of &#8216;<i>c</i>&#8216; is equivalent to &quot;o50&quot;. Examples: </p>
<dl>
<dt>
<dd>
<pre>
# window list in the middle of the screen
<code>WindowList</code> Root c c
# menu to the left of a window
Menu name window -100m c+0
# popup menu 8 pixels above the mouse pointer
<code>Popup</code> name mouse c -100m-8p
# somewhere on the screen
Menu name rectangle 512x384+1+1 +0 +0
# centered vertically around a menu item
<code>AddToMenu</code> foobar-menu
 + &quot;first item&quot; <code>Nop</code>
 + &quot;special item&quot; <code>Popup</code> &quot;another menu&quot; item +100 c
 + &quot;last item&quot; <code>Nop</code>
# above the first menu item
<code>AddToMenu</code> foobar-menu
 + &quot;first item&quot; <code>Popup</code> &quot;another menu&quot; item +0 -100m
</pre>
</dl>
<p> Note that you can put a sub menu far off the current menu so you could not reach it with the mouse without leaving the menu. If the pointer leaves the current menu in the general direction of the sub menu the menu stays up. </p>
<p> The <i>special-options</i>: </p>
<p> To create a tear off menu without opening the normal menu, add the option <i>TearOffImmediately</i>. Normally the menu opens in normal state for a split second before being torn off. As tearing off places the menu like any other window, a position should be specified explicitly: </p>
<dl>
<dt>
<dd>
<pre>
# Forbid fvwm to place the menu window
<code>Style</code> &lt;name of menu&gt; UsePPosition
# Menu at top left corner of screen
Menu Root 0p 0p TearOffImmediately
</pre>
</dl>
<p> The <i>Animated</i> and <i>Mwm</i> or <i>Win</i> menu styles may move a menu somewhere else on the screen. If you do not want this you can add <i>Fixed</i> as an option. This might happen for example if you want the menu always in the top right corner of the screen. </p>
<p> Where do you want a menu to appear when you click on its menu item? The default is to place the title under the cursor, but if you want it where the position arguments say, use the <i>SelectInPlace</i> option. If you want the pointer on the title of the menu, use <i>SelectWarp</i> too. Note that these options apply only if the <i>PopupAsRootMenu</i> <code>MenuStyle</code> option is used. </p>
<p> The pointer is warped to the title of a sub menu whenever the pointer would be on an item when the sub menu is popped up (<i>fvwm</i> menu style) or never warped to the title at all (<i>Mwm</i> or <i>Win</i> menu styles). You can force (forbid) warping whenever the sub menu is opened with the <i>WarpTitle</i> (<i>NoWarp</i>) option. </p>
<p> Note that the <i>special-options</i> do work with a normal menu that has no other position arguments.</dl>
<dt><code>MenuStyle</code> <i>stylename</i> [<i>options</i>]</p>
<dd>
<dl>
<dt>
<dd> Sets a new menu style or changes a previously defined style. The <i>stylename</i> is the style name; if it contains spaces or tabs it has to be quoted. The name &quot;*&quot; is reserved for the default menu style. The default menu style is used for every menu-like object (e.g. the window created by the <code>WindowList</code> command) that had not be assigned a style using the <code>ChangeMenuStyle</code>. See also <code>DestroyMenuStyle</code>. When using monochrome color options are ignored. </p>
<p> <i>options</i> is a comma separated list containing some of the keywords Fvwm / Mwm / Win, BorderWidth, Foreground, Background, Greyed, HilightBack / !HilightBack, HilightTitleBack, ActiveFore / !ActiveFore, MenuColorset, ActiveColorset, GreyedColorset, TitleColorset, Hilight3DThick / Hilight3DThin / Hilight3DOff, Hilight3DThickness, Animation / !Animation, Font, TitleFont, MenuFace, PopupDelay, PopupOffset, TitleWarp / !TitleWarp, TitleUnderlines0 / TitleUnderlines1 / TitleUnderlines2, SeparatorsLong / SeparatorsShort, TrianglesSolid / TrianglesRelief, PopupImmediately / PopupDelayed, PopdownImmediately / PopdownDelayed, PopupActiveArea, DoubleClickTime, SidePic, SideColor, PopupAsRootMenu / PopupAsSubmenu / PopupIgnore / PopupClose, RemoveSubmenus / HoldSubmenus, SubmenusRight / SubmenusLeft, SelectOnRelease, ItemFormat, VerticalItemSpacing, VerticalMargins, VerticalTitleSpacing, AutomaticHotkeys / !AutomaticHotkeys, UniqueHotkeyActivatesImmediate / !UniqueHotkeyActivatesImmediate, MouseWheel, ScrollOffPage / !ScrollOffPage, TrianglesUseFore / !TrianglesUseFore. </p>
<p> In the above list some options are listed as option pairs or triples with a &#8216;/&#8217; in between. These options exclude each other. All paired options can be negated to have the effect of the counterpart option by prefixing ! to the option. </p>
<p> Some options are now negated by prefixing ! to the option. This is the preferred form for all such options. The other negative forms are now deprecated and will be removed in the future. </p>
<p> This is a list of MenuStyle deprecated negative options: ActiveForeOff, AnimationOff, AutomaticHotkeysOff, HilightBackOff, TitleWarpOff </p>
<p> <i>Fvwm</i>, <i>Mwm</i>, <i>Win</i> reset all options to the style with the same name in former versions of fvwm. The default for new menu styles is <i>Fvwm</i> style. These options override all others except <i>Foreground</i>, <i>Background</i>, <i>Greyed</i>, <i>HilightBack</i>, <i>ActiveFore</i> and <i>PopupDelay</i>, so they should be used only as the first option specified for a menu style or to reset the style to defined behavior. The same effect can be created by setting all the other options one by one. </p>
<p> <i>Mwm</i> and <i>Win</i> style menus popup sub menus automatically. <i>Win</i> menus indicate the current menu item by changing the background to dark. <i>Fvwm</i> sub menus overlap the parent menu, <i>Mwm</i> and <i>Win</i> style menus never overlap the parent menu. </p>
<p> <i>Fvwm</i> style is equivalent to !HilightBack, Hilight3DThin, !ActiveFore, !Animation, Font, MenuFace, PopupOffset 0 67, TitleWarp, TitleUnderlines1, SeparatorsShort, TrianglesRelief, PopupDelayed, PopdownDelayed, PopupDelay 150, PopdownDelay 150, PopupAsSubmenu, HoldSubmenus, SubmenusRight, BorderWidth 2, !AutomaticHotkeys, UniqueHotkeyActivatesImmediate, PopupActiveArea 75. </p>
<p> <i>Mwm</i> style is equivalent to !HilightBack, Hilight3DThick, !ActiveFore, !Animation, Font, MenuFace, PopupOffset -3 100, !TitleWarp, TitleUnderlines2, SeparatorsLong, TrianglesRelief, PopupImmediately, PopdownDelayed, PopdownDelay 150, PopupAsSubmenu, HoldSubmenus, SubmenusRight, BorderWidth 2, UniqueHotkeyActivatesImmediate, !AutomaticHotkeys, PopupActiveArea 75. </p>
<p> <i>Win</i> style is equivalent to HilightBack, Hilight3DOff, ActiveFore, !Animation, Font, MenuFace, PopupOffset -5 100, !TitleWarp, TitleUnderlines1, SeparatorsShort, TrianglesSolid, PopupImmediately, PopdownDelayed, PopdownDelay 150, PopupAsSubmenu, RemoveSubmenus, SubmenusRight, BorderWidth 2, UniqueHotkeyActivatesImmediate, !AutomaticHotkeys, PopupActiveArea 75. </p>
<p> <i>BorderWidth</i> takes the thickness of the border around the menus in pixels. It may be zero to 50 pixels. The default is 2. Using an illegal value reverts the border width to the default. </p>
<p> <i>Foreground</i> and <i>Background</i> may have a color name as an argument. This color is used for menu text or the menu&#8217;s background. You can omit the color name to reset these colors to the built-in default. </p>
<p> <i>Greyed</i> may have a color name as an argument. This color is the one used to draw a menu-selection which is prohibited (or not recommended) by the Mwm hints which an application has specified. If the color is omitted the color of greyed menu entries is based on the background color of the menu. </p>
<p> <i>HilightBack</i> and <i>!HilightBack</i> switch hilighting the background of the selected menu item on and off. A specific background color may be used by providing the color name as an argument to <i>HilightBack</i>. If you use this option without an argument the color is based on the menu&#8217;s background color. The <i>ActiveColorset</i> option overrides the specified color. If the colorset has a non solid background it is used for the hilighting. </p>
<p> <i>HilightTitleBack</i> switches hilighting the background of menu titles on. If a <i>TitleColorset</i> was used, the background colour is taken from there. Otherwise the color is based on the menu&#8217;s background color. If the colorset has a non solid background it is used for the hilighting. </p>
<p> <i>ActiveFore</i> and <i>!ActiveFore</i> switch hilighting the foreground of the selected menu item on and off. A specific foreground color may be used by providing the color name as an argument to <i>ActiveFore</i>. Omitting the color turns hilighting on when an <i>ActiveColorset</i> is used. <i>ActiveFore</i> turns off hilighting the foreground completely. The <i>ActiveColorset</i> option overrides the specified color. </p>
<p> <i>MenuColorset</i> controls if a colorset is used instead of the <i>Foreground</i>, <i>Background</i> and <i>MenuFace</i> menu styles. If the <i>MenuColorset</i> keyword is followed by a number equal to zero or greater, this number is taken as the number of the colorset to use. If the number is omitted, the colorset is switched off and the regular menu styles are used again. The foreground and background colors of the menu items are replaced by the colors from the colorset. If the colorset has a pixmap defined, this pixmap is used as the background of the menu. Note that the <i>MenuFace</i> menu style has been optimized for memory consumption and may use less memory than the background from a colorset. The shape mask from the colorset is used to shape the menu. Please refer to the <code>Colorsets</code> section for details about colorsets. </p>
<p> <i>ActiveColorset</i> works exactly like <i>MenuColorset</i>, but the foreground from the colorset replaces the color given with the <i>ActiveFore</i> menu style and the colorset&#8217;s background color replaces the color given with the <i>HilightBack</i> command (to turn on background hilighting you have to use the <i>HilightBack</i> menu style too). If specified, the hilight and shadow colors from the colorset are used too. The pixmap and shape mask from the colorset are not used. Hilighting the background or foreground can be turned off individually with the <i>!ActiveFore</i> or <i>!HilightBack</i> menu styles. </p>
<p> <i>GreyedColorset</i> works exactly like <i>MenuColorset</i>, but the foreground from the colorset replaces the color given with the <i>Greyed</i> menu style. No other parts of the colorset are used. </p>
<p> <i>TitleColorset</i> works exactly like <i>MenuColorset</i>, but is used only for menu titles. </p>
<p> <i>Hilight3DThick</i>, <i>Hilight3DThin</i> and <i>Hilight3DOff</i> determine if the selected menu item is hilighted with a 3D relief. Thick reliefs are two pixels wide, thin reliefs are one pixel wide. </p>
<p> <i>Hilight3DThickness</i> takes one numeric argument that may be between -50 and +50 pixels. With negative values the menu item gets a pressed in look. The above three commands are equivalent to a thickness of 2, 1 and 0. </p>
<p> <i>Animation</i> and <i>!Animation</i> turn menu animation on or off. When animation is on, sub menus that do not fit on the screen cause the parent menu to be shifted to the left so the sub menu can be seen. </p>
<p> <i>Font</i> and <i>TitleFont</i> take a font name as an argument. If a font by this name exists it is used for the text of all menu items. If it does not exist or if the name is left blank the built-in default is used. If a <i>TitleFont</i> is given, it is used for all menu titles instead of the normal font. </p>
<p> <i>MenuFace</i> enforces a fancy background upon the menus. You can use the same options for <i>MenuFace</i> as for the <code>ButtonStyle</code>. See description of <code>ButtonStyle</code> command and the <code>Color Gradients</code> sections for more information. If you use <i>MenuFace</i> without arguments the style is reverted back to normal. </p>
<p> Some examples of MenuFaces are: </p>
<dl>
<dt>
<dd>
<pre>
MenuFace DGradient 128 2 lightgrey 50 blue 50 white
MenuFace TiledPixmap texture10.xpm
MenuFace HGradient 128 2 Red 40 Maroon 60 White
MenuFace Solid Maroon
</pre>
</dl>
<p> Note: The gradient styles H, V, B and D are optimized for high speed and low memory consumption in menus. This is not the case for all the other gradient styles. They may be slow and consume huge amounts of memory, so if you encounter performance problems with them you may be better off by not using them. To improve performance you can try one or all of the following: </p>
<p> Turn hilighting of the active menu item other than foreground color off: </p>
<dl>
<dt>
<dd>
<pre>
MenuStyle &lt;style&gt; Hilight3DOff, !HilightBack
MenuStyle &lt;style&gt; ActiveFore &lt;preferred color&gt;
</pre>
</dl>
<p> Make sure sub menus do not overlap the parent menu. This can prevent menus being redrawn every time a sub menu pops up or down. </p>
<dl>
<dt>
<dd>
<pre>
MenuStyle &lt;style&gt; PopupOffset 1 100
</pre>
</dl>
<p> Run your X server with backing storage. If your X Server is started with the -bs option, turn it off. If not try the -wm and +bs options: </p>
<dl>
<dt>
<dd>
<pre>
startx -- -wm +bs
</pre>
</dl>
<p> You may have to adapt this example to your system (e.g. if you use xinit to start X). </p>
<p> <i>PopupDelay</i> requires one numeric argument. This value is the delay in milliseconds before a sub menu is popped up when the pointer moves over a menu item that has a sub menu. If the value is zero no automatic pop up is done. If the argument is omitted the built-in default is used. Note that the popup delay has no effect if the <i>PopupImmediately</i> option is used since sub menus pop up immediately then. </p>
<p> <i>PopupImmediately</i> makes menu items with sub menus pop up it up as soon as the pointer enters the item. The <i>PopupDelay option</i> is ignored then. If <i>PopupDelayed</i> is used fvwm looks at the <i>PopupDelay</i> option if or when this automatic popup happens. </p>
<p> <i>PopdownDelay</i> works exactly like <i>PopupDelay</i> but determines the timeout of the <i>PopupDelayed</i> style. </p>
<p> <i>PopdownImmediately</i> makes sub menus vanish as soon as the pointer leaves the sub menu and the correspondent item in the parent menu. With the opposite option <i>PopdownDelayed</i> the sub menu only pops down after the time specified with the <i>PopdownDelay</i> option. This comes handy when the pointer often strays off the menu item when trying to move into the sub menu. Whenever there is a conflict between the <i>PopupImmediately</i>, <i>PopupDelayed</i>, <i>PopupDelay</i> styles and the <i>PopdownImmediately</i>, <i>PopdownDelayed</i>, <i>PopdownDelay</i> styles, the <i>Popup&#8230;</i> styles win when using mouse navigation and the <i>Popdown&#8230;</i> styles win when navigating with the keyboard. </p>
<p> <i>PopupOffset</i> requires two integer arguments. Both values affect where sub menus are placed relative to the parent menu. If both values are zero, the left edge of the sub menu overlaps the left edge of the parent menu. If the first value is non-zero the sub menu is shifted that many pixels to the right (or left if negative). If the second value is non-zero the menu is moved by that many percent of the parent menu&#8217;s width to the right or left. </p>
<p> <i>PopupActiveArea</i> requires an integer value between 51 and 100. Normally, when the pointer is over a menu item with a sub menu and the pointer enters the area that starts at 75% of the menu width, the sub menu is shown immediately. This percentage can be changed with <i>PopupActiveArea</i>. Setting this value to 100 disables this kind of automatic popups altogether. The default value is restored if no or an illegal value is given. </p>
<p> <i>TitleWarp</i> and <i>!TitleWarp</i> affect if the pointer warps to the menu title when a sub menu is opened or not. Note that regardless of this setting the pointer is not warped if the menu does not pop up under the pointer. </p>
<p> <i>TitleUnderlines0</i>, <i>TitleUnderlines1</i> and <i>TitleUnderlines2</i> specify how many lines are drawn below a menu title. </p>
<p> <i>SeparatorsLong</i> and <i>SeparatorsShort</i> set the length of menu separators. Long separators run from the left edge all the way to the right edge. Short separators leave a few pixels to the edges of the menu. </p>
<p> <i>TrianglesSolid</i> and <i>TrianglesRelief</i> affect how the small triangles for sub menus is drawn. Solid triangles are filled with a color while relief triangles are hollow. </p>
<p> <i>DoubleClickTime</i> requires one numeric argument. This value is the time in milliseconds between two mouse clicks in a menu to be considered as a double click. The default is 450 milliseconds. If the argument is omitted the double click time is reset to this default. </p>
<p> <i>SidePic</i> takes the name of an image file as an argument. The picture is drawn along the left side of the menu. The <i>SidePic</i> option can be overridden by a menu specific side pixmap (see <code>AddToMenu</code>). If the file name is omitted an existing side pixmap is removed from the menu style. </p>
<p> <i>SideColor</i> takes the name of an X11 color as an argument. This color is used to color the column containing the side picture (see above). The SideColor option can be overridden by a menu specific side color (see <code>AddToMenu</code>). If the color name is omitted the side color option is switched off. </p>
<p> <i>PopupAsRootMenu</i>, <i>PopupAsSubmenu</i>, <i>PopupIgnore</i> and <i>PopupClose</i> change the behavior when you click on a menu item that opens a sub menu. With <i>PopupAsRootMenu</i> the original menu is closed before the sub menu appears, with <i>PopupAsSubmenu</i> it is not, so you can navigate back into the parent menu. Furthermore, with <i>PopupAsSubmenu</i> the sub menu is held open (posted) regardless of where you move the mouse. Depending on your menu style this may simplify navigating through the menu. <code>Any</code> keystroke while a menu is posted reverts the menu back to the normal behavior. With <i>PopupClose</i> the menu is closed when a sub menu item is activated, and the menu stays open if <i>PopupIgnore</i> is used (even if the menu was invoked with the <code>Popup</code> command). <i>PopupAsSubmenu</i> is the default. </p>
<p> <i>RemoveSubmenus</i> instructs fvwm to remove sub menu when you move back into the parent menu. With <i>HoldSubmenus</i> the sub menu remains visible. You probably want to use <i>HoldSubmenus</i> if you are using the <i>PopupDelayed</i> style. <i>RemoveSubmenus</i> affects menu navigation with the keyboard. </p>
<p> <i>SelectOnRelease</i> takes an optional key name as an argument. If the given key is released in a menu using this style, the current menu item is selected. This is intended for <font SIZE="-1">Alt-Tab</font> <code>WindowList</code> navigation. The key name is a standard X11 key name as defined in <i>/usr/include/X11/keysymdef.h</i>, (without the <i>XK_</i> prefix), or the keysym database <i>/usr/X11R6/lib/X11/XKeysymDB</i>. To disable this behavior, omit the key name. </p>
<p> Note: Some X servers do not support KeyRelease events. <i>SelectOnRelease</i> does not work on such a machine. </p>
<p> <i>ItemFormat</i> takes a special string as its argument that determines the layout of the menu items. Think of the format string as if it were a menu item. All you have to do is tell fvwm where to place the different parts of the menu item (i.e. the labels, the triangle denoting a sub menu, the mini icons and the side pic) in the blank area. The string consists of spaces, <font SIZE="-1">Tab</font> characters and formatting directives beginning with &#8216;%&#8217;. Any illegal characters and formatting directives are silently ignored: </p>
<p> <code>%l</code>, <code>%c</code> and <code>%r</code></p>
<dl>
<dt>
<dd> Insert the next item label. Up to three labels can be used. The item column is left-aligned (<code>%l</code>), centered (<code>%c</code>) or right-aligned (<code>%r</code>).</dl>
<p> <code>%i</code></p>
<dl>
<dt>
<dd> Inserts the mini icon.</dl>
<p> <code>%&gt;</code> and <code>%&lt;</code></p>
<dl>
<dt>
<dd> Insert the sub menu triangle pointing either to the right (<code>%&gt;</code>) or to the left (<code>%&lt;</code>).</dl>
<p> <code>%|</code></p>
<dl>
<dt>
<dd> The first <code>%|</code> denotes the beginning of the area that is highlighted either with a background color or a relief (or both). The second <code>%|</code> marks the end of this area. <code>%|</code> can be used up to twice in the string. If you do not add one or both of them, fvwm sets the margins to the margins of the whole item (not counting the side picture).</dl>
<p> <code>%s</code></p>
<dl>
<dt>
<dd> Places the side picture either at the beginning or the end of the menu. This directive may be used only once and only as the first or last in the format string. If the <code>%s</code> is not at the beginning of the string, menus are not drawn properly.</dl>
<p> <code>Space</code>, <code>Tab</code>, <code>%Space</code> and <code>%Tab</code></p>
<dl>
<dt>
<dd> Add gap of one space, or a tab, using the width of the menu font. When using a tab, the size of the gap can be one to 8 spaces since the tab position is a multiple of 8 from the edge of the menu. The whole string must be quoted if spaces or tabs are used.</dl>
<p> <code>%p</code></p>
<dl>
<dt>
<dd> Like Space and Tab <code>%p</code> inserts an empty area into the item, but with better control of its size (see below).</dl>
<p> You can define an additional space before and after each of the objects like this: </p>
<dl>
<dt>
<dd>
<pre>
<code>%</code><i>left</i><code>.</code><i>right</i><code>p</code>
</pre>
</dl>
<p> This means: if the object is defined in the menu (e.g. if it is <code>%s</code> and you use a side picture, or it is <code>%l</code> for the third column and there are items defined that actually have a third column), then add <i>left</i> pixels before the object and <i>right</i> pixels after it. You may leave out the <i>left</i> or the <i>.right</i> parts if you do not need them. All values up to the screen width are allowed. Even negative values can be used with care. The <code>p</code> may be replaced with any other formatting directives described above. </p>
<p> Note: Only items defined in the format string are visible in the menus. So if you do not put a <code>%s</code> in there you do not see a side picture, even if one is specified. </p>
<p> Note: The <i>SubmenusLeft</i> style changes the default <i>ItemFormat</i> string, but if it was set manually it is not modified. </p>
<p> Note: If any unformatted title of the menu is wider than the widest menu item, the spaces between the different parts of the menu items are enlarged to match the width of the title. Leading left aligned objects in the format string (<code>%l</code>, <code>%i</code>, <code>%&lt;</code>, first <code>%|</code>) stick to the left edge of the menu and trailing right aligned objects (<code>%r</code>, <code>%i</code>, <code>%&gt;</code>, second <code>%|</code>) stick to the right edge. The gaps between the remaining items are enlarged equally. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
MenuStyle * ItemFormat &quot;%.4s%.1|%.5i%.5l%.5l%.5r%.5i%2.3&gt;%1|&quot;
</pre>
</dl>
<p> Is the default string used by fvwm: (side picture + 4 pixels gap) (beginning of the hilighted area + 1 pixel gap) (mini icon + 5p) (first column left aligned + 5p) (second column left aligned + 5p) (third column right aligned + 5p) (second mini icon + 5p) (2p + sub menu triangle + 3p) (1p + end of hilighted area). </p>
<dl>
<dt>
<dd>
<pre>
MenuStyle * ItemFormat &quot;%.1|%3.2&lt;%5i%5l%5l%5r%5i%1|%4s&quot;
</pre>
</dl>
<p> Is used by fvwm with the <i>SubmenusLeft</i> option below. </p>
<p> <i>VerticalItemSpacing</i> and <i>VerticalTitleSpacing</i> control the vertical spacing of menu items and titles like <i>ItemFormat</i> controls the horizontal spacing. Both take two numeric arguments that may range from -100 to +100. The first is the gap in pixels above a normal menu item (or a menu title), the second is the gap in pixels below it. Negative numbers do not make much sense and may screw up the menu completely. If no arguments are given or the given arguments are invalid, the built-in defaults are used: one pixel above the item or title and two below. </p>
<p> <i>VerticalMargins</i> can be used to add some padding at the top and bottom of menus. It takes two numeric arguments that must be positive integers (or zero). If the number of arguments or its values are incorrect, fvwm defaults both to 0, which means no padding at all. If the values are correct, the first one is used for the top margin, and the second one is used for the bottom margin. </p>
<p> <i>SubmenusLeft</i> mirrors the menu layout and behavior. Sub menus pop up to the left, the sub menu triangle is drawn left and the mini icon and side picture are drawn at the right side of the menu. The default is <i>SubmenusRight</i>. The position hints of a menu are also affected by this setting, i.e. position hints using <i>item</i> or <i>menu</i> as context rectangle and position hints using <i>m</i> offsets. </p>
<p> <i>AutomaticHotkeys</i> and <i>!AutomaticHotkeys</i> control the menu&#8217;s ability to automatically provide hot-keys on the first character of each menu item&#8217;s label. This behavior is always overridden if an explicit hot-key is assigned in the <code>AddToMenu</code> command. </p>
<p> <i>UniqueHotkeyActivatesImmediate</i> and <i>!UniqueHotkeyActivatesImmediate</i> controls how menu items are invoked when used with hotkeys. By default, if a given menu entry only has one completeable match for a given hotkey, the action for that menu entry is invoked and the menu is closed. This is due to the <i>UniqueHotkeyActivatesImmediate</i> option. However, the menu can be told to remain open, waiting for the user to invoke the selected item instead when there is only one matched item for a given hotkey, by using the <i>!UniqueHotkeyActivatesImmediate</i> option. </p>
<p> <i>MouseWheel</i> controls the ability to scroll the menu using a mouse wheel. It takes one argument, that can be one of ScrollsPointer, ScrollsMenu, ScrollsMenuBackwards or ActivatesItem. ScrollsPointer makes the mouse wheel scroll the pointer over a menu. This is the default. ScrollsMenu and ScrollsMenuBackwards scroll the menu beneath the pointer. ActivatesItem disables scrolling by mouse wheel and makes the use of a mouse wheel act as if the menu was clicked. If no argument is supplied the default setting is restored. </p>
<p> <i>ScrollOffPage</i> allows a menu to be scrolled out of the visible area if <i>MouseWheel</i> is set to ScrollsMenu or ScrollsMenuBackwards. This is the default. The opposite, <i>!ScrollOffPage</i> disables this behaviour. </p>
<p> <i>TrianglesUseFore</i> draws sub menu triangles with the foreground color of the menu colorset (normally drawn with the hilight color). <i>!TrianglesUseFore</i> disables this behaviour. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
MenuStyle * Mwm
MenuStyle * Foreground Black, Background gray40
MenuStyle * Greyed gray70, ActiveFore White
MenuStyle * !HilightBack, Hilight3DOff
MenuStyle * Font lucidasanstypewriter-14
MenuStyle * MenuFace DGradient 64 darkgray MidnightBlue
MenuStyle red Mwm
MenuStyle red Foreground Yellow
MenuStyle red Background Maroon
MenuStyle red Greyed Red, ActiveFore Red
MenuStyle red !HilightBack, Hilight3DOff
MenuStyle red Font lucidasanstypewriter-12
MenuStyle red MenuFace DGradient 64 Red Black
</pre>
</dl>
<p> Note that all style options could be placed on a single line for each style name.</dl>
<dt><code>MenuStyle</code> <i>forecolor</i> <i>backcolor</i> <i>shadecolor</i> <i>font</i> <i>style</i> [<i>anim</i>]</p>
<dd>
<dl>
<dt>
<dd> This is the old syntax of the <code>MenuStyle</code> command. It is obsolete and may be removed in the future. Please use the new syntax as described above. </p>
<p> Sets the menu style. When using monochrome the colors are ignored. The <i>shadecolor</i> is the one used to draw a menu-selection which is prohibited (or not recommended) by the Mwm hints which an application has specified. The style option is either <i>Fvwm</i>, <i>Mwm</i> or <i>Win</i>, which changes the appearance and operation of the menus. </p>
<p> <i>Mwm</i> and <i>Win</i> style menus popup sub menus automatically. <i>Win</i> menus indicate the current menu item by changing the background to black. <i>Fvwm</i> sub menus overlap the parent menu, <i>Mwm</i> and <i>Win</i> style menus never overlap the parent menu. </p>
<p> When the <i>anim</i> option is given, sub menus that do not fit on the screen cause the parent menu to be shifted to the left so the sub menu can be seen. See also <code>SetAnimation</code> command.</dl>
<dt><code>Popup</code> <i>PopupName</i> [<i>position</i>] [<i>default-action</i>]</p>
<dd>
<dl>
<dt>
<dd> This command has two purposes: to bind a menu to a key or mouse button, and to bind a sub menu into a menu. The formats for the two purposes differ slightly. The <i>position</i> arguments are the same as for <code>Menu</code>. The command <i>default-action</i> is invoked if the user clicks a button to invoke the menu and releases it immediately again (or hits the key rapidly twice if the menu is bound to a key). If the default action is not specified, double clicking on the menu does nothing. However, if the menu begins with a menu item (i.e. not with a title or a separator) and the default action is not given, double clicking invokes the first item of the menu (but only if the pointer really was over the item). </p>
<p> To bind a previously defined pop-up menu to a key or mouse button: </p>
<p> The following example binds mouse buttons 2 and 3 to a pop-up called &quot;Window Ops&quot;. The menu pops up if the buttons 2 or 3 are pressed in the window frame, side-bar, or title-bar, with no modifiers (none of shift, control, or meta). </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 2 FST N Popup &quot;Window Ops&quot;
<code>Mouse</code> 3 FST N Popup &quot;Window Ops&quot;
</pre>
</dl>
<p> Pop-ups can be bound to keys through the use of the <code>Key</code> command. Pop-ups can be operated without using the mouse by binding to keys and operating via the up arrow, down arrow, and enter keys. </p>
<p> To bind a previously defined pop-up menu to another menu, for use as a sub menu: </p>
<p> The following example defines a sub menu &quot;Quit-Verify&quot; and binds it into a main menu, called &quot;RootMenu&quot;: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToMenu</code> Quit-Verify
 + &quot;Really Quit Fvwm?&quot; <code>Title</code>
 + &quot;Yes, Really Quit&quot;  <code>Quit</code>
 + &quot;Restart Fvwm&quot;      <code>Restart</code>
 + &quot;Restart Fvwm 1.xx&quot; <code>Restart</code> fvwm1 -s
 + &quot;&quot;                  <code>Nop</code>
 + &quot;No, Don't Quit&quot;    <code>Nop</code>
<code>AddToMenu</code> RootMenu &quot;Root Menu&quot; <code>Title</code>
 + &quot;Open XTerm Window&quot; Popup NewWindowMenu
 + &quot;Login as Root&quot;     <code>Exec</code> exec xterm -T Root -n Root -e su -
 + &quot;Login as Anyone&quot;   <code>Popup</code> AnyoneMenu
 + &quot;Remote Hosts&quot;      <code>Popup</code> HostMenu
 + &quot;&quot;                  <code>Nop</code>
 + &quot;X utilities&quot;       Popup Xutils
 + &quot;&quot;                  <code>Nop</code>
 + &quot;Fvwm Modules&quot;      Popup Module-Popup
 + &quot;Fvwm Window Ops&quot;   Popup Window-Ops
 + &quot;&quot;                  <code>Nop</code>
 + &quot;Previous Focus&quot;    <code>Prev</code> (AcceptsFocus) <code>Focus</code>
 + &quot;Next Focus&quot;        <code>Next</code> (AcceptsFocus) <code>Focus</code>
 + &quot;&quot;                  <code>Nop</code>
 + &quot;Refresh screen&quot;    <code>Refresh</code>
 + &quot;&quot;                  <code>Nop</code>
 + &quot;Reset X defaults&quot;  <code>Exec</code> xrdb -load \
                       $HOME/.Xdefaults
 + &quot;&quot;                  <code>Nop</code>
 + &quot;&quot;                  <code>Nop</code>
 + <code>Quit</code>                Popup Quit-Verify
</pre>
</dl>
<p> Popup differs from <code>Menu</code> in that pop-ups do not stay up if the user simply clicks. These are popup-menus, which are a little hard on the wrist. <code>Menu</code> menus stay up on a click action. See the <code>Menu</code> command for an explanation of the interactive behavior of menus. A menu can be open up to ten times at once, so a menu may even use itself or any of its predecessors as a sub menu.</dl>
<dt><code>TearMenuOff</code></p>
<dd>
<dl>
<dt>
<dd> When assigned to a menu item, it inserts a tear off bar into the menu (a horizontal broken line). Activating that item tears off the menu. If the menu item has a label, it is shown instead of the broken line. If used outside menus, this command does nothing. Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToMenu</code> WindowMenu
+ I &quot;&quot; TearMenuOff
<code>AddToMenu</code> RootMenu
+ I &quot;click here to tear me off&quot; TearMenuOff
</pre>
</dl>
</dl>
<dt><code>Title</code></p>
<dd>
<dl>
<dt>
<dd> Does nothing This is used to insert a title line in a popup or menu.</dl>
</dl>
<h3>Miscellaneous Commands</h3>
<dl>
<dt><code>BugOpts</code> [<i>option</i>&nbsp;<wbr>[<i>bool</i>]], &#8230;</p>
<dd>
<dl>
<dt>
<dd> This command controls several workarounds for bugs in third party programs. The individual options are separated by commas. The optional argument <i>bool</i> is a boolean argument and controls if the bug workaround is enabled or not. It can either be &quot;True&quot; or &quot;False&quot; to turn the option on or off, or &quot;toggle&quot; to switch is back and forth. If <i>bool</i> is omitted, the default setting is restored. </p>
<p> <i>FlickeringMoveWorkaround</i> disables ConfigureNotify events that are usually sent to an application while it is moved. If some windows flicker annoyingly while being moved, this option may help you. Note that if this problem occurs it is not an fvwm bug, it is a problem of the application. </p>
<p> <i>MixedVisualWorkaround</i> makes fvwm install the root colormap before it does some operations using the root window visuals. This is only useful when the <code>-visual</code> option is used to start fvwm and then only with some configurations of some servers (e.g. Exceed 6.0 with an 8 bit PseudoColor root and fvwm using a 24 bit TrueColor visual). </p>
<p> The <i>ModalityIsEvil</i> option controls whether Motif applications have the ability to have modal dialogs (dialogs that force you to close them first before you can do anything else). The default is to not allow applications to have modal dialogs. Use this option with care. Once this option is turned on, you have to restart fvwm to turn it off. </p>
<p> <i>RaiseOverNativeWindows</i> makes fvwm try to raise the windows it manages over native windows of the X server&#8217;s host system. This is needed for some X servers running under Windows, Windows NT or Mac OS X. Fvwm tries to detect if it is running under such an X server and initializes the flag accordingly. </p>
<p> <i>RaiseOverUnmanaged</i> makes fvwm try to raise the windows it manages over override_redirect windows. This is used to cope with ill-mannered applications that use long-lived windows of this sort, contrary to ICCCM conventions. It is useful with the <i>Unmanaged</i> style option too. </p>
<p> <i>FlickeringQtDialogsWorkaround</i> suppresses flickering of the focused window in some modules when using KDE or QT applications with application modal dialog windows. By default this option is turned on. This option may be visually disturbing for other applications using windows not managed by fvwm. Since these applications are rare it is most likely safe to leave this option at its default. </p>
<p> <i>QtDragnDropWorkaround</i> suppresses the forwarding of unknown ClientEvent messages to windows &#8212; usually this is harmless, but Qt has problems handling unrecognised ClientEvent messages. Enabling this option might therefore help for Qt applications using DragnDrop. This option is off by default. </p>
<p> <i>EWMHIconicStateWorkaround</i> is needed by EWMH compliant pagers or taskbars which represent windows which are on a different desktops as iconified. These pagers and taskbars use a version of the EWMH specification before version 1.2 (the current KDE 2 &amp; 3 versions). These pagers and taskbars use the IconicState WM_STATE state to determine if an application is iconified. This state, according to the ICCCM, does not imply that a window is iconified (in the usual sense). Turning on this option forces fvwm to establish an equivalence between the IconicState WM_STATE state and the iconified window. This violates ICCCM compliance but should not cause big problems. By default this option is off. </p>
<p> With the <i>DisplayNewWindowNames</i> enabled, fvwm prints the name, icon name (if available), resource and class of new windows to the console. This can help in finding the correct strings to use in the <code>Style</code> command. </p>
<p> When the <i>ExplainWindowPlacement</i> option is enabled, fvwm prints a message to the console whenever a new window is placed or one of the commands <code>PlaceAgain</code>, <code>Recapture</code> or <code>RecaptureWindow</code> is used. The message explains on which desk, page, Xinerama screen and position it was placed and why. This option can be used to figure out why a specific window does not appear where you think it should. </p>
<p> The <i>DebugCRMotionMethod</i> option enables some debugging code in the ConfigureRequest handling routines of fvwm. It is not helpful for the user, but if you report a bug to the fvwm team we may ask you to enable this option. </p>
<p> The <i>TransliterateUtf8</i> option enables transliteration during conversions from utf-8 strings. By default fvwm will not transliterate during conversion, but will fall back to alternate strings provided by the clients if conversion from utf-8 fails due to characters which have no direct correspondance in the target charecter set. Some clients however neglect to set non utf-8 properties correctly in which case this option may help.</dl>
<dt><code>BusyCursor</code> [<i>Option</i>&nbsp;<wbr><i>bool</i>], &#8230;</p>
<dd>
<dl>
<dt>
<dd> This command controls the cursor during the execution of certain commands. <i>Option</i> can be <i>DynamicMenu</i>, <i>ModuleSynchronous</i>, <i>Read</i>, <i>Wait</i> or <i>*</i>. An option must be followed by a boolean argument <i>bool</i>. You can use commas to separate individual options. If you set an option to &quot;True&quot;, then when the corresponding command is run, fvwm displays the cursor of the <i>WAIT</i> context of the <code>CursorStyle</code> command. &quot;False&quot; forces to not display the cursor. The default is: </p>
<dl>
<dt>
<dd>
<pre>
BusyCursor DynamicMenu False, ModuleSynchronous False, \
  Read False, Wait False
</pre>
</dl>
<p> The <i>*</i> option refers to all available options. </p>
<p> The <i>Read</i> option controls the <code>PipeRead</code> command. </p>
<p> The <i>DynamicMenu</i> option affects the <i>DynamicPopupAction</i> and <i>MissingSubmenuFunction</i> options of the <code>AddToMenu</code> command. If this option is set to &quot;False&quot;, then the busy cursor is not displayed during a dynamic menu command even if this command is a <code>Read</code> or <code>PipeRead</code> command and the <i>Read</i> option is set to &quot;True&quot;. </p>
<p> The <i>ModuleSynchronous</i> option affects the <code>ModuleSynchronous</code> command. If this option is set to &quot;False&quot;, then the busy cursor is not displayed while fvwm waits for a module started by <code>ModuleSynchronous</code> to complete its startup. </p>
<p> The <i>Wait</i> option affects only the root cursor. During a wait pause the root cursor is replaced by the busy cursor and fvwm is still fully functional (you can escape from the pause, see the <code>EscapeFunc</code> command). If you want to use this option and if you do not use the default root cursor, you must set your root cursor with the <code>CursorStyle</code> command.</dl>
<dt><code>ClickTime</code> [<i>delay</i>]</p>
<dd>
<dl>
<dt>
<dd> Specifies the maximum delay in milliseconds between a button press and a button release for the <code>Function</code> command to consider the action a mouse click. The default delay is 150 milliseconds. Omitting the delay value resets the <code>ClickTime</code> to the default.</dl>
<dt><code>ColorLimit</code> <i>limit</i></p>
<dd>
<dl>
<dt>
<dd> This command is obsolete. See the <code>&#8211;color-limit</code> option to fvwm.</dl>
<dt><code>ColormapFocus</code> FollowsMouse | FollowsFocus</p>
<dd>
<dl>
<dt>
<dd> By default, fvwm installs the colormap of the window that the cursor is in. If you use </p>
<dl>
<dt>
<dd>
<pre>
ColormapFocus <i>FollowsFocus</i>
</pre>
</dl>
<p> then the installed colormap is the one for the window that currently has the keyboard focus.</dl>
<dt><code>CursorStyle</code> <i>context</i> [<i>num</i>&nbsp;<wbr>|&nbsp;<wbr><i>name</i>&nbsp;<wbr>| None | Tiny |&nbsp;<wbr><i>file</i>&nbsp;<wbr>[<i>x</i>&nbsp;<wbr><i>y</i>]&nbsp;<wbr>[<i>fg</i>&nbsp;<wbr><i>bg</i>]]</p>
<dd>
<dl>
<dt>
<dd> Defines a new cursor for the specified context. Note that this command can not control the shapes an applications uses, for example, to indicate that it is busy. The various contexts are: </p>
<p> <i>POSITION</i> (top_left_corner)</p>
<dl>
<dt>
<dd> used when initially placing windows</dl>
<p> <i>TITLE</i> (top_left_arrow)</p>
<dl>
<dt>
<dd> used in a window title-bar</dl>
<p> <i>DEFAULT</i> (top_left_arrow)</p>
<dl>
<dt>
<dd> used in windows that do not set their cursor</dl>
<p> <i>SYS</i> (hand2)</p>
<dl>
<dt>
<dd> used in one of the title-bar buttons</dl>
<p> <i>MOVE</i> (fleur)</p>
<dl>
<dt>
<dd> used when moving or resizing windows</dl>
<p> <i>RESIZE</i> (sizing)</p>
<dl>
<dt>
<dd> used when moving or resizing windows</dl>
<p> <i>WAIT</i> (watch)</p>
<dl>
<dt>
<dd> used during certain fvwm commands (see <code>BusyCursor</code> for details)</dl>
<p> <i>MENU</i> (top_left_arrow)</p>
<dl>
<dt>
<dd> used in menus</dl>
<p> <i>SELECT</i> (crosshair)</p>
<dl>
<dt>
<dd> used when the user is required to select a window</dl>
<p> <i>DESTROY</i> (pirate)</p>
<dl>
<dt>
<dd> used for <code>Destroy</code>, <code>Close</code>, and <code>Delete</code> commands</dl>
<p> <i>TOP</i> (top_side)</p>
<dl>
<dt>
<dd> used in the top side-bar of a window</dl>
<p> <i>RIGHT</i> (right_side)</p>
<dl>
<dt>
<dd> used in the right side-bar of a window</dl>
<p> <i>BOTTOM</i> (bottom_side)</p>
<dl>
<dt>
<dd> used in the bottom side-bar of a window</dl>
<p> <i>LEFT</i> (left_side)</p>
<dl>
<dt>
<dd> used in the left side-bar of a window</dl>
<p> <i>TOP_LEFT</i> (top_left_corner)</p>
<dl>
<dt>
<dd> used in the top left corner of a window</dl>
<p> <i>TOP_RIGHT</i> (top_right_corner)</p>
<dl>
<dt>
<dd> used in the top right corner of a window</dl>
<p> <i>BOTTOM_LEFT</i> (bottom_left_corner)</p>
<dl>
<dt>
<dd> used in the bottom left corner of a window</dl>
<p> <i>BOTTOM_RIGHT</i> (bottom_right_corner)</p>
<dl>
<dt>
<dd> used in the bottom right corner of a window</dl>
<p> <i>TOP_EDGE</i> (top_side)</p>
<dl>
<dt>
<dd> used at the top edge of the screen</dl>
<p> <i>RIGHT_EDGE</i> (right_side)</p>
<dl>
<dt>
<dd> used at the right edge of the screen</dl>
<p> <i>BOTTOM_EDGE</i> (bottom_side)</p>
<dl>
<dt>
<dd> used at the bottom edge of the screen</dl>
<p> <i>LEFT_EDGE</i> (left_side)</p>
<dl>
<dt>
<dd> used at the left edge of the screen</dl>
<p> <i>ROOT</i> (left_ptr)</p>
<dl>
<dt>
<dd> used as the root cursor</dl>
<p> <i>STROKE</i> (plus)</p>
<dl>
<dt>
<dd> used during a <code>StrokeFunc</code> command.</dl>
<p> The defaults are shown in parentheses above. If you ever want to restore the default cursor for a specific context you can omit the second argument. </p>
<p> The second argument is either the numeric value of the cursor as defined in the include file <i>X11/cursorfont.h</i> or its name (without the XC_ prefix). Alternatively, the xpm file name may be specified. The name can also be <i>None</i> (no cursor) or <i>Tiny</i> (a single pixel as the cursor). </p>
<dl>
<dt>
<dd>
<pre>
# make the kill cursor be XC_gumby (both forms work):
CursorStyle DESTROY 56
CursorStyle DESTROY gumby
</pre>
</dl>
<p> Alternatively, the cursor can be loaded from an (XPM, PNG or SVG) image <i>file</i>. If fvwm is compiled with Xcursor support, full ARGB is used, and (possibly animated) cursor files made with the <code>xcursorgen</code> program can be loaded. Otherwise the cursor is converted to monochrome. </p>
<p> The optional <i>x</i> and <i>y</i> arguments (following a <i>file</i> argument) specifies the hot-spot coordinate with 0 0 as the top left corner of the image. Coordinates within the image boundary are valid and overrides any hot-spot defined in the (XPM/Xcursor) image file. An invalid or undefined hot-spot is placed in the center of the image. </p>
<dl>
<dt>
<dd>
<pre>
CursorStyle ROOT cursor_image.png 0 0
</pre>
</dl>
<p> The optional <i>fg</i> and <i>bg</i> arguments specify the foreground and background colors for the cursor, defaulting to black and white (reverse video compared to the actual bitmap). These colors are only used with monochrome cursors. Otherwise they are silently ignored. </p>
<dl>
<dt>
<dd>
<pre>
CursorStyle ROOT nice_arrow.xpm yellow black
</pre>
</dl>
</dl>
<dt><code>DefaultColors</code> [<i>foreground</i>] [<i>background</i>]</p>
<dd>
<dl>
<dt>
<dd> <code>DefaultColors</code> sets the default foreground and background colors used in miscellaneous windows created by fvwm, for example in the geometry feedback windows during a move or resize operation. If you do not want to change one color or the other, use &#8211; as its color name. To revert to the built-in default colors omit both color names. Note that the default colors are not used in menus, window titles or icon titles.</dl>
<dt><code>DefaultColorset</code> [<i>num</i>]</p>
<dd>
<dl>
<dt>
<dd> <code>DefaultColorset</code> sets the colorset used by the windows controlled by the <code>DefaultColors</code> command. To revert back to the <code>DefaultColors</code> colors use </p>
<dl>
<dt>
<dd>
<pre>
DefaultColorset -1
</pre>
</dl>
<p> or any variant of the <code>DefaultColors</code> command.</dl>
<dt><code>DefaultFont</code> [<i>fontname</i>]</p>
<dd>
<dl>
<dt>
<dd> <code>DefaultFont</code> sets the default font to font <i>fontname</i>. The default font is used by fvwm whenever no other font has been specified. To reset the default font to the built-in default, omit the argument. The default font is used for menus, window titles, icon titles as well as the geometry feedback windows during a move or resize operation. To override the default font in a specific context, use the <code>Style</code> * <i>Font</i>, <code>Style</code> * <i>IconFont</i>, or <code>MenuStyle</code> commands.</dl>
<dt><code>DefaultIcon</code> <i>filename</i></p>
<dd>
<dl>
<dt>
<dd> Sets the default icon which is used if a window has neither an client-supplied icon nor an icon supplied via the <i>Icon</i> option of the <code>Style</code> command.</dl>
<dt><code>DefaultLayers</code> <i>bottom</i> <i>put</i> <i>top</i></p>
<dd>
<dl>
<dt>
<dd> Changes the layers that are used for the <i>StaysOnBottom</i>, <i>StaysPut</i>, <i>StaysOnTop</i> <code>Style</code> options. Initially, the layers 2, 4 and 6 are used.</dl>
<dt><code>Deschedule</code> [<i>command_id</i>]</p>
<dd>
<dl>
<dt>
<dd> Removes all commands that were scheduled with the id <i>command_id</i> with the <code>Schedule</code> command from the list of commands to be executed unless they were already executed. If the <i>command_id</i> is omitted, the value of the variable $[schedule.last] is used as the id.</dl>
<dt><code>Emulate</code> Fvwm | Mwm | Win</p>
<dd>
<dl>
<dt>
<dd> This command is a catch all for how miscellaneous things are done by fvwm. Right now this command affects where the move/resize feedback window appears and how window placement is aborted. To have more Mwm- or Win-like behavior you can call <code>Emulate</code> with <i>Mwm</i> or <i>Win</i> as its argument. With Mwm resize and move feedback windows are in the center of the screen, instead of the upper left corner. This also affects how manual placement is aborted. See the <i>ManualPlacement</i> description.</dl>
<dt><code>EscapeFunc</code></p>
<dd>
<dl>
<dt>
<dd> By default the key sequence <font SIZE="-1">Ctrl-Alt-Escape</font> allows for escaping from a <code>Wait</code> pause and from a locked <code>ModuleSynchronous</code> command. The <code>EscapeFunc</code> command used with the <code>Key</code> command allows for configuring this key sequence. An example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> Escape A MC -
<code>Key</code> Escape A  S EscapeFunc
</pre>
</dl>
<p> replaces the <font SIZE="-1">Ctrl-Alt-Escape</font> key sequence with <font SIZE="-1">Shift-Escape</font> for aborting a <code>Wait</code> pause and <code>ModuleSynchronous</code> command. <code>EscapeFunc</code> used outside the <code>Key</code> command does nothing.</dl>
<dt><code>FakeClick</code> [<i>command</i>&nbsp;<wbr><i>value</i>] &#8230;</p>
<dd>
<dl>
<dt>
<dd> This command is mainly intended for debugging fvwm and no guarantees are made that it works for you. <i>FakeClick</i> can simulate mouse button press and release events and pass them to fvwm or the applications. The parameters are a list of commands which consist of pairs of <i>command</i> tokens and integer <i>values</i>, The <i>press</i> and <i>release</i> commands are followed by the appropriate mouse button number and generate a button press or release event on the window below the pointer. The <i>wait</i> commands pauses fvwm for the given number of milliseconds. The <i>modifiers</i> command simulates pressing or releasing modifier keys. The values 1 to 5 are mapped to <font SIZE="-1">Mod1</font> to <font SIZE="-1">Mod5</font> while 6, 7 and 8 are mapped to <font SIZE="-1">Shift</font> , <font SIZE="-1">Lock</font> and <font SIZE="-1">Control</font> . The modifier is set for any further button events. To release a modifier key, use the corresponding negative number. The <i>depth</i> command determines to which window the button events are sent. With a depth of 1, all events go to the root window, regardless of the pointer&#8217;s position. With 2, the event is passed to the top level window under the pointer which is usually the frame window. With 3, events go to the client window. Higher numbers go to successive sub windows. Zero (0) goes to the smallest window that contains the pointer. Note that events propagate upward. </p>
<dl>
<dt>
<dd>
<pre>
FakeClick depth 2 press 1 wait 250 release 1
</pre>
</dl>
<p> This simulates a click with button 1 in the parent window (depth 2) with a delay of 250 milliseconds between the press and the release. Note: all command names can be abbreviated with their first letter.</dl>
<dt><code>FakeKeypress</code> [<i>command</i>&nbsp;<wbr><i>value</i>] &#8230;</p>
<dd>
<dl>
<dt>
<dd> This command is mainly intended for debugging fvwm and no guarantees are made that it works for you. <code>FakeKeypress</code> can simulate key press and release events and pass them to fvwm or applications. The parameters are a list of commands which consist of pairs of command tokens and values. The <i>press</i> and <i>release</i> commands are followed by a key name. The key name is a standard X11 key name as defined in <i>/usr/include/X11/keysymdef.h</i>, (without the <i>XK_</i> prefix), or the keysym database <i>/usr/X11R6/lib/X11/XKeysymDB</i>. The <i>wait</i>, <i>modifiers</i> and <i>depth</i> commands are the same as those used by <code>FakeClick</code>. </p>
<p> Save all GVim sessions with: &quot;Esc:w
&quot; </p>
<dl>
<dt>
<dd>
<pre>
<code>All</code> (gvim) FakeKeypress press Escape \
                        press colon \
                        press w \
                        press Return
</pre>
</dl>
<p> Save &amp; exit all GVim sessions with: &quot;Esc:wq
&quot; </p>
<dl>
<dt>
<dd>
<pre>
<code>All</code> (gvim) FakeKeypress press Escape \
                        press colon \
                        press w \
                        press q \
                        press Return
</pre>
</dl>
<p> Send A to a specific window: </p>
<dl>
<dt>
<dd>
<pre>
<code>WindowId</code> 0x3800002 FakeKeypress press A
</pre>
</dl>
<p> Note: all command names can be abbreviated with their first letter.</dl>
<dt><code>GlobalOpts</code> [<i>options</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is obsolete. Please replace the global options in your configuration file according to the following table: </p>
<dl>
<dt>
<dd>
GlobalOpts WindowShadeShrinks&#8211; &gt;<br />
    Style *WindowShadeShrinks<br />
        GlobalOpts WindowShadeScrolls&#8211; &gt;<br />
    Style *WindowShadeScrolls<br />
        GlobalOpts SmartPlacementIsReallySmart&#8211; &gt;<br />
    Style *MinOverlapPlacement<br />
        GlobalOpts SmartPlacementIsNormal&#8211; &gt;<br />
    Style *TileCascadePlacement<br />
        GlobalOpts ClickToFocusDoesntPassClick&#8211; &gt;<br />
    Style *ClickToFocusPassesClickOff<br />
        GlobalOpts ClickToFocusPassesClick&#8211; &gt;<br />
    Style *ClickToFocusPassesClick<br />
        GlobalOpts ClickToFocusDoesntRaise&#8211; &gt;<br />
    Style *ClickToFocusRaisesOff<br />
        GlobalOpts ClickToFocusRaises&#8211; &gt;<br />
    Style *ClickToFocusRaises<br />
        GlobalOpts MouseFocusClickDoesntRaise&#8211; &gt;<br />
    Style *MouseFocusClickRaisesOff<br />
        GlobalOpts MouseFocusClickRaises&#8211; &gt;<br />
    Style *MouseFocusClickRaises<br />
        GlobalOpts NoStipledTitles&#8211; &gt;<br />
    Style * !StippledTitle<br />
                GlobalOpts StipledTitles&#8211; &gt;<br />
    Style *StippledTitle<br />
        GlobalOpts CaptureHonorsStartsOnPage&#8211; &gt;<br />
    Style *CaptureHonorsStartsOnPage<br />
        GlobalOpts CaptureIgnoresStartsOnPage&#8211; &gt;<br />
    Style *CaptureIgnoresStartsOnPage<br />
        GlobalOpts RecaptureHonorsStartsOnPage&#8211; &gt;<br />
    Style *RecaptureHonorsStartsOnPage<br />
        GlobalOpts RecaptureIgnoresStartsOnPage&#8211; &gt;<br />
    Style *RecaptureIgnoresStartsOnPage<br />
        GlobalOpts ActivePlacementHonorsStartsOnPage&#8211; &gt;<br />
    Style *ManualPlacementHonorsStartsOnPage<br />
        GlobalOpts ActivePlacementIgnoresStartsOnPage&#8211; &gt;<br />
    Style *ManualPlacementIgnoresStartsOnPage<br />
        GlobalOpts RaiseOverNativeWindows&#8211; &gt;<br />
    BugOpts RaiseOverNativeWindows on<br />
        GlobalOpts IgnoreNativeWindows&#8211; &gt;<br />
    BugOpts RaiseOverNativeWindows off
</dl>
</dl>
<dt><code>HilightColor</code> <i>textcolor</i> <i>backgroundcolor</i></p>
<dd>
<dl>
<dt>
<dd> This command is obsoleted by the <code>Style</code> options <i>HilightFore</i> and <i>HilightBack</i>. Please use </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>HilightFore</i> textcolor, <i>HilightBack</i> backgroundcolor
</pre>
</dl>
<p> instead.</dl>
<dt><code>HilightColorset</code> [<i>num</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is obsoleted by the <code>Style</code> option <i>HilightColorset</i>. Please use </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>HilightColorset</i> num
</pre>
</dl>
<p> instead.</dl>
<dt><code>IconFont</code> [<i>fontname</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is obsoleted by the <code>Style</code> option <i>IconFont</i>. Please use </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * IconFont fontname
</pre>
</dl>
<p> instead.</dl>
<dt><code>IconPath</code> <i>path</i></p>
<dd>
<dl>
<dt>
<dd> This command is obsolete. Please use <code>ImagePath</code> instead.</dl>
<dt><code>ImagePath</code> <i>path</i></p>
<dd>
<dl>
<dt>
<dd> Specifies a colon separated list of directories in which to search for images (both monochrome and pixmap). To find an image given by a relative pathname, fvwm looks into each directory listed in turn, and uses the first file found. </p>
<p> If a directory is given in the form &quot;/some/dir;.ext&quot;, this means all images in this directory have the extension &quot;.ext&quot; that should be forced. The original image name (that may contain another extension or no extension at all) is not probed, instead &quot;.ext&quot; is added or replaces the original extension. This is useful, for example, if a user has some image directories with &quot;.xpm&quot; images and other image directories with the same names, but &quot;.png&quot; images. </p>
<p> The <i>path</i> may contain environment variables such as <i>$HOME</i> (or <i>${HOME}</i>). Further, a &#8216;+&#8217; in the <i>path</i> is expanded to the previous value of the path, allowing appending or prepending to the path easily. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
ImagePath $HOME/icons:+:/usr/include/X11/bitmaps
</pre>
</dl>
<p> Note: if the <code>FvwmM4</code> module is used to parse your <i>config</i> files, then m4 may want to mangle the word &quot;include&quot; which frequently shows up in the <code>ImagePath</code> command. To fix this one may add </p>
<dl>
<dt>
<dd>
<pre>
undefine(`include')
</pre>
</dl>
<p> prior to the <code>ImagePath</code> command, or better: use the <code>-m4-prefix</code> option to force all <code>m4</code> directives to have a prefix of &quot;m4_&quot; (see the <code>FvwmM4</code> man page).</dl>
<dt><code>LocalePath</code> <i>path</i></p>
<dd>
<dl>
<dt>
<dd> Specifies a colon separated list of &quot;locale path&quot; in which to search for string translations. A locale path is constituted by a directory path and a text domain separated by a semicolon (&#8216;;&#8217;). As an example the default locale path is: </p>
<dl>
<dt>
<dd>
<pre>
/install_prefix/share/locale;fvwm
</pre>
</dl>
<p> where install_prefix is the fvwm installation directory. With such a locale path translations are searched for in </p>
<dl>
<dt>
<dd>
<pre>
/install_prefix/share/locale/lang/LC_MESSAGES/fvwm.mo
</pre>
</dl>
<p> where <i>lang</i> depends on the locale. If no directory is given the default directory path is assumed. If no text domain is given, <code>fvwm</code> is assumed. Without argument the default locale path is restored. </p>
<p> As for the <code>ImagePath</code> command, <i>path</i> may contain environment variables and a &#8216;+&#8217; to append or prepend the locale path easily. </p>
<p> For example, the fvwm-themes package uses </p>
<dl>
<dt>
<dd>
<pre>
LocalePath &quot;;fvwm-themes:+&quot;
</pre>
</dl>
<p> to add locale catalogs. </p>
<p> The default fvwm catalog contains a few strings used by the fvwm executable itself (Desk and Geometry) and strings used in some default configuration files and <code>FvwmForm</code> configuration. You can take a look at the po/ subdirectory of the fvwm source to get the list of the strings with a possible translation in various languages. At present, very few languages are supported. </p>
<p> The main use of locale catalogs is via the &quot;$[gt.string]&quot; parameter: </p>
<dl>
<dt>
<dd>
DestroyMenu MenuFvwmWindowOps<br />
        AddToMenu MenuFvwmWindowOps &#8220;$[gt.Window Ops]&#8221; Title +<br />
    &#8220;$[gt.&amp;Move]&#8221; Move + &#8220;$[gt.&amp;Resize]&#8221; Resize + &#8220;$[gt.R&amp;aise]&#8221; Raise + &#8220;$[gt.&amp;Lower]&#8221; Lower + &#8220;$[gt.(De)&amp;Iconify]&#8221; Iconify + &#8220;$[gt.(Un)&amp;Stick]&#8221; Stick + &#8220;$[gt.(Un)Ma&amp;ximize]&#8221; Maximize + &#8220;&#8221; Nop + &#8220;$[gt.&amp;Close]&#8221; Close + &#8220;$[gt.&amp;Destroy]&#8221; Destroy
</dl>
<p> gives a menu in the locale languages if translations are available. </p>
<p> Note that the <code>FvwmTaskBar</code> module has its own catalog and that the <code>FvwmScript</code> module has a set of special instructions for string translation. It is out of the scope of this discussion to explain how to build locale catalogs. Please refer to the GNU gettext documentation.</dl>
<dt><code>PixmapPath</code> <i>path</i></p>
<dd>
<dl>
<dt>
<dd> This command is obsolete. Please use <code>ImagePath</code> instead.</dl>
<dt><code>PrintInfo</code> <i>subject</i> [<i>verbose</i>]</p>
<dd>
<dl>
<dt>
<dd> Print information on <i>subject</i> on stderr. An optional integer argument <i>verbose</i> defines the level of information which is given. The current valid subjects are: </p>
<p> <i>Colors</i> which prints information about the colors used by fvwm. This useful on screens which can only display 256 (or less) colors at once. If <i>verbose</i> is one or greater the palette used by fvwm is printed. If you have a limited color palette, and you run out of colors, this command might be helpful. </p>
<p> <i>ImageCache</i> which prints information about the images loaded by fvwm. If <i>verbose</i> is one or greater all images in the cache will be listed together with their respective reuse. </p>
<p> <i>Locale</i> which prints information on your locale and the fonts that fvwm used. <i>verbose</i> can be 1 or 2. </p>
<p> <i>nls</i> which prints information on the locale catalogs that fvwm used </p>
<p> <i>style</i> which prints information on fvwm styles. <i>verbose</i> can be 1. </p>
<p> <i>bindings</i> which prints information on all the bindings fvwm has: key, mouse and stroke bindings. <i>verbose</i> has no effect with this option. </p>
<p> <i>infostore</i> which prints information on all entries in the infostore, listing the key and its value. <i>verbose</i> has no effect with this option.</dl>
<dt><code>Repeat</code></p>
<dd>
<dl>
<dt>
<dd> When the <code>Repeat</code> command is invoked, the last command that was executed by fvwm is executed again. This happens regardless of whether it was triggered by user interaction, a module or by an X event. Commands that are executed from a function defined with the <code>Function</code> command, from the <code>Read</code> or <code>PipeRead</code> commands or by a menu are not repeated. Instead, the function, menu or the <code>Read</code> or <code>PipeRead</code> command is executed again.</dl>
<dt><code>Schedule</code> [Periodic] <i>delay_ms</i> [<i>command_id</i>] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> The <i>command</i> is executed after about <i>delay_ms</i> milliseconds. This may be useful in some tricky setups. The <i>command</i> is executed in the same context window as the <code>Schedule</code> command. An optional integer argument <i>command_id</i> may be given in decimal, hexadecimal or octal format. This id can be used with the <code>Deschedule</code> command to remove the scheduled command before it is executed. If no id is given, fvwm uses negative id numbers, starting with -1 and decreasing by one with each use of the <code>Schedule</code> command. Note that the <code>Schedule</code> command and its arguments undergo the usual command line expansion, and, when <i>command</i> is finally executed, it is expanded again. It may therefore be necessary to quote the parts of the command that must not be expanded twice. </p>
<p> Note: A window&#8217;s id as it is returned with $[w.id] can be used as the <i>command_id</i>. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Current</code> Schedule 1000 $[w.id] <code>WindowShade</code>
</pre>
</dl>
<p> The <code>Schedule</code> command also supports the optional keyword <i>Periodic</i> which indicates that the <i>command</i> should be executed every <i>delay_ms</i>. Example: </p>
<dl>
<dt>
<dd>
<pre>
Schedule Periodic 10000 <code>PipeRead</code> '[ -N &quot;$MAIL&quot; ] &amp;&amp; echo \
     Echo You have mail'
</pre>
</dl>
<p> Use the <code>Deschedule</code> command to stop periodic commands.</dl>
<dt><code>State</code> <i>state</i> [<i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> Sets, clears or toggles one of the 32 user defined states which are associated with each window. The <i>state</i> is a number ranging from 0 to 31. The states have no meaning in fvwm, but they can be checked in conditional commands like <code>Next</code> with the <i>State</i> condition. The optional argument <i>bool</i> is a boolean argument. &quot;True&quot; sets the given state, while &quot;False&quot; clears it. Using &quot;toggle&quot; switches to the opposite state. If the <i>bool</i> argument is not given, the state is toggled.</dl>
<dt><code>WindowFont</code> [<i>fontname</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is obsoleted by the <code>Style</code> option <i>Font</i>. Please use </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>Font</i> fontname
</pre>
</dl>
<p> instead.</dl>
<dt><code>WindowList</code> [(<i>conditions</i>)] [<i>position</i>] [<i>options</i>] [<i>double-click-action</i>]</p>
<dd>
<dl>
<dt>
<dd> Generates a pop-up menu (and pops it up) in which the title and geometry of each of the windows currently on the desktop are shown. </p>
<p> The format of the geometry part is: <i>desk</i>(<i>layer</i>): <i>x-geometry</i> <i>sticky</i>, where <i>desk</i> and <i>layer</i> are the corresponding numbers and <i>sticky</i> is empty or a capital S. The geometry of iconified windows is shown in parentheses. Selecting an item from the window list pop-up menu causes the interpreted function &quot;WindowListFunc&quot; to be run with the window id of that window passed in as $0. The default &quot;WindowListFunc&quot; looks like this: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> WindowListFunc
+ I <code>Iconify</code> off
+ I <code>FlipFocus</code>
+ I <code>Raise</code>
+ I <code>WarpToWindow</code> 5p 5p
</pre>
</dl>
<p> You can destroy the built-in &quot;WindowListFunc&quot; and create your own if these defaults do not suit you. </p>
<p> The window list menu uses the &quot;WindowList&quot; menu style if it is defined (see <code>MenuStyle</code> command). Otherwise the default menu style is used. To switch back to the default menu style, issue the command </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyMenuStyle</code> WindowList
</pre>
</dl>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>MenuStyle</code> WindowList <i>SelectOnRelease</i> Meta_L
</pre>
</dl>
<p> The <i>conditions</i> can be used to exclude certain windows from the window list. Please refer to the <code>Current</code> command for details. Only windows that match the given conditions are displayed in the window list. The <i>options</i> below work vice versa: windows that would otherwise not be included in the window list can be selected with them. The <i>conditions</i> always override the <i>options</i>. </p>
<p> The <i>position</i> arguments are the same as for <code>Menu</code>. The command <i>double-click-action</i> is invoked if the user double-clicks (or hits the key rapidly twice if the menu is bound to a key) when bringing the window list. The <i>double-click-action</i> must be quoted if it consists of more than one word. </p>
<p> The <i>double-click-action</i> is useful to define a default window if you have bound the window list to a key (or button) like this: </p>
<dl>
<dt>
<dd>
<pre>
# Here we call an existing function, but
# it may be different.  See the default
# WindowListFunc definition earlier in this
# man page.
<code>AddToFunc</code> SwitchToWindow
+ I WindowListFunc
<code>Key</code> Tab A M WindowList &quot;Prev SwitchToWindow&quot;
</pre>
</dl>
<p> Hitting <font SIZE="-1">Alt-Tab</font> once it brings up the window list, if you hit it twice the focus is flipped between the current and the last focused window. With the proper <i>SelectOnRelease</i> menu style (see example above) a window is selected as soon as you release the <font SIZE="-1">Alt</font> key. </p>
<p> The <i>options</i> passed to WindowList are separated by commas and can be <i>Geometry</i> / <i>NoGeometry</i> / <i>NoGeometryWithInfo</i>, <i>NoDeskNum,</i> <i>NoLayer,</i> <i>NoNumInDeskTitle</i>, <i>NoCurrentDeskTitle</i>, <i>MaxLabelWidth width</i>, <i>TitleForAllDesks</i>, <i>Function funcname</i>, <i>Desk desknum</i>, <i>CurrentDesk</i>, <i>NoIcons</i> / <i>Icons</i> / <i>OnlyIcons</i>, <i>NoNormal</i> / <i>Normal</i> / <i>OnlyNormal</i>, <i>NoSticky</i> / <i>Sticky</i> / <i>OnlySticky</i>, <i>NoStickyAcrossPages</i> / <i>StickyAcrossPages</i> / <i>OnlyStickyAcrossPages</i>, <i>NoStickyAcrossDesks</i> / <i>StickyAcrossDesks</i> / <i>OnlyStickyAcrossDesks</i>, <i>NoOnTop</i> / <i>OnTop</i> / <i>OnlyOnTop</i>, <i>NoOnBottom</i> / <i>OnBottom</i> / <i>OnlyOnBottom</i>, <i>Layer m [n]</i>, <i>UseSkipList</i> / <i>OnlySkipList</i>, <i>NoDeskSort</i>, <i>ReverseOrder</i>, <i>CurrentAtEnd</i>, <i>IconifiedAtEnd</i>, <i>UseIconName</i>, <i>Alphabetic</i> / <i>NotAlphabetic</i>, <i>SortByResource</i>, <i>SortByClass</i>, <i>NoHotkeys</i>, <i>SelectOnRelease</i>. </p>
<p> (Note &#8211; normal means not iconic, sticky, or on top) </p>
<p> With the <i>SortByResource</i> option windows are alphabetically sorted first by resource class, then by resource name and then by window name (or icon name if <i>UseIconName</i> is specified). <i>ReverseOrder</i> also works in the expected manner. </p>
<p> With the <i>SortByClass</i> option windows are sorted just like with <i>SortByResource</i>, but the resource name is not taken into account, only the resource class. </p>
<p> The <i>SelectOnRelease</i> option works exactly like the <code>MenuStyle</code> option with the same name, but overrides the option given in a menu style. By default, this option is set to the left <font SIZE="-1">Alt</font> key. To switch it off, use <i>SelectOnRelease</i> without a key name. </p>
<p> If you pass in a function via <code>Function</code> funcname, it is called within a window context of the selected window: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> IFunc I <code>Iconify</code> toggle
WindowList <code>Function</code> IFunc, NoSticky, CurrentDesk, NoIcons
</pre>
</dl>
<p> If you use the <i>Layer</i> <i>m</i> [<i>n</i>] option, only windows in layers between m and n are displayed. n defaults to m. With the <i>ReverseOrder</i> option the order of the windows in the list is reversed. </p>
<p> With the <i>CurrentAtEnd</i> option the currently focused window (if any) is shown at the bottom of the list. This is mostly intended for simulating the Alt-Tab behavior in another GUI. </p>
<p> <i>IconifiedAtEnd</i> makes iconified windows be moved to the end of the list. This is also from another GUI. </p>
<p> The <i>NoGeometry</i> option causes fvwm to not display the geometries as well as the separators which indicate the different desktops. <i>NoGeometryWithInfo</i> removes the geometries, but keep the desktop information and indicates iconic windows. <i>NoDeskNum</i> causes fvwm to not display the desktop number in the geometry or before the window title with the <i>NoGeometryWithInfo</i> option. <i>NoNumInDeskTitle</i> is only useful if a desktop name is defined with the <code>DesktopName</code> command. It causes fvwm to not display the desktop number before the desktop name. By default, the WindowList menu have a title which indicates the current desk or the selected desktop if the <i>Desk</i> condition is used. The <i>NoCurrentDeskTitle</i> option removes this title. <i>TitleForAllDesks</i> causes fvwm to add a menu title with the desk name and/or number before each group of windows on the same desk. With <i>NoLayer</i>, the layer of the window is not diplayed. The options <i>ShowPage</i>, <i>ShowPageX</i> and <i>ShowPageY</i> enable displaying the page of the window rounded multiples of the display size. With <i>ShowScreen</i>, the window&#8217;s Xinerama screen number is displayed. </p>
<p> The <i>MaxLabelWidth</i> option takes the number of characters to print as its argument. No more than that many characters of the window name are visible. </p>
<p> If you wanted to use the <code>WindowList</code> as an icon manager, you could invoke the following: </p>
<dl>
<dt>
<dd>
<pre>
WindowList OnlyIcons, Sticky, OnTop, Geometry
</pre>
</dl>
<p> (Note &#8211; the <i>Only</i> options essentially wipe out all other ones&#8230; but the <i>OnlyListSkip</i> option which just causes <code>WindowList</code> to only consider the windows with <i>WindowListSkip</i> style.)</dl>
<dt><code>XSync</code></p>
<dd>
<dl>
<dt>
<dd> When <code>XSync</code> is called, the X function with the same name is used to send all pending X requests to the server. This command is intended for debugging only.</dl>
<dt><code>XSynchronize</code> [bool]</p>
<dd>
<dl>
<dt>
<dd> The <code>XSynchronize</code> command controls whether X requests are sent to the X server immediately or not. Normally, requests are sent in larger batches to save unnecessary communication. To send requests immediately, use &quot;True&quot; as the argument, to disable this use &quot;False&quot; or to toggle between both methods use &quot;Toggle&quot; or omit the <code>bool</code> argument. Fvwm defaults to synchronized requests when started with the <code>&#8211;debug</code> option. This command is intended for debugging only.</dl>
<dt><code>+</code></p>
<dd>
<dl>
<dt>
<dd> Used to continue adding to the last specified decor, function or menu. See the discussion for <code>AddToDecor</code>, <code>AddToFunc</code>, and <code>AddToMenu</code>.</dl>
</dl>
<h3>Window Movement and Placement</h3>
<dl>
<dt><code>AnimatedMove</code> <i>x</i> <i>y</i> [Warp]</p>
<dd>
<dl>
<dt>
<dd> Move a window in an animated fashion. Similar to <code>Move</code> command. The options are the same, except they are required, since it doesn&#8217;t make sense to have a user move the window interactively and animatedly. If the optional argument <i>Warp</i> is specified the pointer is warped with the window.</dl>
<dt><code>HideGeometryWindow</code> [Never | Move | Resize]</p>
<dd>
<dl>
<dt>
<dd> Hides the position or size window that is usually shown when a window is moved or resized interactively. To switch it off only for move or resize operations the optional parameters <i>Move</i> and <i>Resize</i> can be used respectively. To switch both on again use the <i>Never</i> option.</dl>
<dt><code>Layer</code> [<i>arg1</i>&nbsp;<wbr><i>arg2</i>] | [default]</p>
<dd>
<dl>
<dt>
<dd> Puts the current window in a new layer. If <i>arg1</i> is non zero then the next layer is the current layer number plus <i>arg1</i>. If <i>arg1</i> is zero then the new layer is <i>arg2</i>. </p>
<p> As a special case, <i>default</i> puts the window in its default layer, i.e. the layer it was initially in. The same happens if no or invalid arguments are specified.</dl>
<dt><code>Lower</code></p>
<dd>
<dl>
<dt>
<dd> Allows the user to lower a window. Note that this lowers a window only in its layer. To bring a window to the absolute bottom, use </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> lower-to-bottom
 + I <code>Layer</code> 0 0
 + I Lower
</pre>
</dl>
</dl>
<dt><code>Move</code> [[screen&nbsp;<wbr><i>screen</i>]&nbsp;<wbr>[w | m]<i>x</i>[p | w]&nbsp;<wbr>&#8230;&nbsp;<wbr>[w | m]<i>y</i>[p | w]&nbsp;<wbr>&#8230;&nbsp;<wbr>[Warp]] | [pointer] | [ewmhiwa]</p>
<dd>
<dl>
<dt>
<dd> Allows the user to move a window. If called from somewhere in a window or its border, then that window is moved. If called from the root window then the user is allowed to select the target window. By default, the EWMH working area is honoured. </p>
<p> If the literal option <i>screen</i> followed by a <i>screen</i> argument is specified, the coordinates are interpreted as relative to the given screen. The width and height of the screen are used for the calculations instead of the display dimensions. The <i>screen</i> as interpreted as in the <code>MoveToScreen</code> command. If the optional argument <i>Warp</i> is specified the pointer is warped with the window. If the single argument <i>pointer</i> is given, the top left corner of the window is moved to the pointer position before starting the operation; this is mainly intended for internal use by modules like <code>FvwmPager</code>. If the optional argument <i>ewmhiwa</i> is given, then the window position will ignore the working area (such as ignoring any values set via <code>EwmhBaseStruts</code>). </p>
<p> The operation can be aborted with <font SIZE="-1">Escape</font> or any mouse button not set to place the window. By default mouse button 2 is set to cancel the move operation. To change this you may use the <code>Mouse</code> command with special context &#8216;P&#8217; for Placement. </p>
<p> The window condition <i>PlacedByButton</i> can be used to check if a specific button was pressed to place the window (see <code>Current</code> command). </p>
<p> If the optional arguments <i>x</i> and <i>y</i> are provided, then the window is moved immediately without user interaction. Each argument can specify an absolute or relative position from either the left/top or right/bottom of the screen. By default, the numeric value given is interpreted as a percentage of the screen width/height, but a trailing &#8216;<i>p</i>&#8216; changes the interpretation to mean pixels, while a trailing &#8216;<i>w</i>&#8216; means precent of the window width/height. To move the window relative to its current position, add the &#8216;<i>w</i>&#8216; (for &quot;window&quot;) prefix before the <i>x</i> and/or <i>y</i> value. To move the window to a position relative to the current location of the pointer, add the &#8216;<i>m</i>&#8216; (for &quot;mouse&quot;) prefix. To leave either coordinate unchanged, &quot;<i>keep</i>&quot; can be specified in place of <i>x</i> or <i>y</i>. </p>
<p> For advanced uses, the arguments <i>x</i> and <i>y</i> can be used multiple times, but without the prefix &#8216;<i>m</i>&#8216; or &#8216;<i>w</i>&#8216;. (See complex examples below). </p>
<p> Simple Examples: </p>
<dl>
<dt>
<dd>
<pre>
# Interactive move
<code>Mouse</code> 1 T A Move
# Move window to top left is at (10%,10%)
<code>Mouse</code> 2 T A Move 10 10
# Move top left to (10pixels,10pixels)
<code>Mouse</code> 3 T A Move 10p 10p
</pre>
</dl>
<p> More complex examples (these can be bound as actions to keystrokes, etc.; only the command is shown, though): </p>
<dl>
<dt>
<dd>
<pre>
# Move window so bottom right is at bottom
# right of screen
Move -0 -0
# Move window so top left corner is 10 pixels
# off the top left screen edge
Move +-10 +-10
# Move window 5% to the right, and to the
# middle vertically
Move w+5 50
# Move window up 10 pixels, and so left edge
# is at x=40 pixels
Move 40p w-10p
# Move window to the mouse pointer location
Move m+0 m+0
# Move window to center of screen (50% of screen
# poition minus 50% of widow size).
Move 50-50w 50-50w
</pre>
</dl>
<p> Note: In order to obtain moving windows which do not snap to screen, with interactive move, hold down <i>Alt</i> whilst moving the window to disable snap attraction if it&#8217;s defined. </p>
<p> See also the <code>AnimatedMove</code> command.</dl>
<dt><code>MoveToDesk</code> [prev | <i>arg1</i>&nbsp;<wbr>[<i>arg2</i>]&nbsp;<wbr>[<i>min</i>&nbsp;<wbr><i>max</i>]]</p>
<dd>
<dl>
<dt>
<dd> Moves the selected window to another desktop. The arguments are the same as for the <code>GotoDesk</code> command. Without any arguments, the window is moved to the current desk. <code>MoveToDesk</code> is a replacement for the obsolete <code>WindowsDesk</code> command, which can no longer be used.</dl>
<dt><code>MoveThreshold</code> [<i>pixels</i>]</p>
<dd>
<dl>
<dt>
<dd> When the user presses a mouse button upon an object fvwm waits to see if the action is a click or a drag. If the mouse moves by more than <i>pixels</i> pixels it is assumed to be a drag. </p>
<p> Previous versions of fvwm hardwired <i>pixels</i> to 3, which is now the default value. If <i>pixels</i> is negative or omitted the default value (which might be increased when 16000&#215;9000 pixel displays become affordable) is restored.</dl>
<dt><code>MoveToPage</code> [<i>options</i>]&nbsp;<wbr>[<i>x</i>[p | w]&nbsp;<wbr><i>y</i>[p | w]] | [prev]</p>
<dd>
<dl>
<dt>
<dd> Moves the selected window to another page (<i>x</i>,<i>y</i>). The upper left page is (0,0), the upper right is (M,0), where M is one less than the current number of horizontal pages specified in the <code>DesktopSize</code> command. Similarly the lower left page is (0,N), and the lower right page is (M,N). Negative page numbers refer to pages from the rightmost/lowest page. If <i>x</i> and <i>y</i> are not given, the window is moved to the current page (a window that has the focus but is off-screen can be retrieved with this). Moving windows to a page relative to the current page can be achieved by adding a trailing &#8216;<i>p</i>&#8216; after any or both numerical arguments. To move the window relative to its current location, add a trailing &#8216;<i>w</i>&#8216;. To move a window to the previous page use <i>prev</i> as the single argument. </p>
<p> Windows are usually not moved beyond desk boundaries. </p>
<p> Possible <i>options</i> are <i>wrapx</i> and <i>wrapy</i> to wrap around the x or y coordinate when the window is moved beyond the border of the desktop. For example, with <i>wrapx</i>, when the window moves past the right edge of the desktop, it reappears on the left edge. The options <i>nodesklimitx</i> and <i>nodesklimity</i> allow moving windows beyond the desk boundaries in x and y direction (disabling the <i>wrapx</i> and <i>wrapy</i> options). </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
# <code>Move</code> window to page (2,3)
MoveToPage 2 3
# <code>Move</code> window to lowest and rightmost page
MoveToPage -1 -1
# <code>Move</code> window to last page visited
MoveToPage prev
# <code>Move</code> window two pages to the right and one
# page up, wrap at desk boundaries
MoveToPage wrapx wrapy +2p -1p
</pre>
</dl>
</dl>
<dt><code>MoveToScreen</code> [<i>screen</i>]</p>
<dd>
<dl>
<dt>
<dd> Moves the selected window to another Xinerama screen. The <i>screen</i> argument can be &#8216;<i>p</i>&#8216; for the primary screen, &#8216;<i>c</i>&#8216; for the current screen (containing the mouse pointer), &#8216;<i>w</i>&#8216; for the screen containing the center of +the the context window, &#8216;<i>g</i>&#8216; for the global screen or the screen number itself (counting from zero).</dl>
<dt><code>OpaqueMoveSize</code> [<i>percentage</i>]</p>
<dd>
<dl>
<dt>
<dd> Tells fvwm the maximum size window with which opaque window movement should be used. The percentage is percent of the total screen area (may be greater than 100). With </p>
<dl>
<dt>
<dd>
<pre>
OpaqueMoveSize 0
</pre>
</dl>
<p> all windows are moved using the traditional rubber-band outline. With </p>
<dl>
<dt>
<dd>
<pre>
OpaqueMoveSize <i>unlimited</i>
</pre>
</dl>
<p> or if a negative percentage is given all windows are moved as solid windows. The default is </p>
<dl>
<dt>
<dd>
<pre>
OpaqueMoveSize 5
</pre>
</dl>
<p> which allows small windows to be moved in an opaque manner but large windows are moved as rubber-bands. If <i>percentage</i> is omitted or invalid the default value is set. To resize windows in an opaque manner you can use the <i>ResizeOpaque</i> style. See the <code>Style</code> command.</dl>
<dt><code>PlaceAgain</code> [Anim] [Icon]</p>
<dd>
<dl>
<dt>
<dd> Causes the current window&#8217;s position to be re-computed using the initial window placement logic. The window is moved to where it would have been if it were a new window that had just appeared. Most useful with <i>Smart</i> or <i>Clever</i> (<i>ReallySmart</i>) placement. With the optional argument <i>Anim</i> an animated move is used to place the window in its new position. With the additional option <i>Icon</i>, the icon is placed again instead.</dl>
<dt><code>Raise</code></p>
<dd>
<dl>
<dt>
<dd> Allows the user to raise a window. Note that this raises a window only in its layer. To bring a window to the absolute top, use </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> raise-to-top
 + I <code>Layer</code> 0 ontop
 + I Raise
</pre>
</dl>
<p> where ontop is the highest layer used in your setup.</dl>
<dt><code>RaiseLower</code></p>
<dd>
<dl>
<dt>
<dd> Alternately raises and lowers a window. The window is raised if it is obscured by any window (except for its own transients when <i>RaiseTransient</i> style is used; see the <code>Style</code> command) otherwise it is lowered.</dl>
<dt><code>Resize</code> [[frame] [direction&nbsp;<wbr><i>dir</i>] [warptoborder&nbsp;<wbr><i>automatic</i>] [fixeddirection] [w]<i>width</i>[p | c | wa | da] [w]<i>height</i>[p | c]]</p>
<dd>
<dl>
<dt>
<dd> Allows for resizing a window. If called from somewhere in a window or its border, then that window is resized. If called from the root window then the user is allowed to select the target window. </p>
<p> The operation can be aborted with <font SIZE="-1">Escape</font> or by pressing any mouse button (except button 1 which confirms it). </p>
<p> If the optional arguments <i>width</i> and <i>height</i> are provided, then the window is resized so that its dimensions are <i>width</i> by <i>height</i>. The units of <i>width</i> and <i>height</i> are percent-of-screen, unless a letter &#8216;<i>p</i>&#8216; is appended to one or both coordinates, in which case the location is specified in pixels. With a &#8216;<i>c</i>&#8216; suffix the unit defined by the client application (hence the c) is used. With the suffix &#8216;<i>wa</i>&#8216; the value is a percentage of the width or height size of the EWMH working area, and with the suffix &#8216;<i>da</i>&#8216; it is a percentage of the width or height of the EWMH dynamic working area. So you can say </p>
<dl>
<dt>
<dd>
<pre>
Resize 80c 24c
</pre>
</dl>
<p> to make a terminal window just big enough for 80&#215;24 characters. </p>
<p> If the <i>width</i> or <i>height</i> is prefixed with the letter &#8216;<i>w</i>&#8216; the size is not taken as an absolute value but added to the current size of the window. Example: </p>
<dl>
<dt>
<dd>
<pre>
# Enlarge window by one line
Resize keep w+1c
</pre>
</dl>
<p> Both, <i>width</i> and <i>height</i> can be negative. In this case the new size is the screen size minus the given value. If either value is &quot;<i>keep</i>&quot;, the corresponding dimension of the window is left untouched. The new size is the size of the client window, thus </p>
<dl>
<dt>
<dd>
<pre>
Resize 100 100
</pre>
</dl>
<p> may make the window bigger than the screen. To base the new size on the size of the whole fvwm window, add the <i>frame</i> option after the command. The options <i>fixeddirection</i>, <i>direction</i> and <i>warptoborder</i> are only used in interactive move operations. With <i>fixeddirection</i> the same border is moved even if the pointer moves past the opposite border. The <i>direction</i> option must be followed by a direction name such as &quot;NorthWest&quot;, &quot;South&quot; or &quot;East&quot; (you get the idea). Resizing is started immediately, even if the pointer is not on a border. If the special option <i>automatic</i> is given as a direction argument, then the direction to resize is calculated based on the position of the pointer in the window. If the pointer is in the middle of the window, then no direction is calculated. The <i>warptoborder</i> option can be used to warp the pointer to the direction indicated. As with the <i>automatic</i> option for <i>direction</i>, the border to warp to is calculated based on the pointer&#8217;s proximity to a given border. Also, if resizing is started by clicking on the window border, the pointer is warped to the outer edge of the border. </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> ResizeSE I Resize <code>Direction</code> SE
<code>Mouse</code> 3 A M ResizeSE
</pre>
</dl>
</dl>
<dt><code>Resize</code> [bottomright | br&nbsp;<wbr><i>x</i>&nbsp;<wbr><i>y</i>]</p>
<dd>
<dl>
<dt>
<dd> An alternate syntax is used if the keyword <i>bottomright</i> or in short <i>br</i> follows the command name. In this case, the arguments <i>x</i> and <i>y</i> specify the desired position of the bottom right corner of the window. They are interpreted exactly like the <i>x</i> and <i>y</i> arguments of the <code>Move</code> command. Actually, any of the options accepted by the <code>Move</code> command can be used.</dl>
<dt><code>ResizeMaximize</code> [<i>resize-arguments</i>]</p>
<dd>
<dl>
<dt>
<dd> Combines the effects of <code>Resize</code> and <code>Maximize</code> in a single command. When used on a maximized window, the window is resized and is still in the maximized state afterwards. When used on an unmaximized window, the window is resized and put into the maximized state afterwards. This is useful if the user wants to resize the window temporarily and then return to the original geometry. The <i>resize-arguments</i> are the same as for the <code>Resize</code> command.</dl>
<dt><code>ResizeMove</code> <i>resize-arguments</i> <i>move-arguments</i></p>
<dd>
<dl>
<dt>
<dd> This command does the same as the <code>Resize</code> and <code>Move</code> commands, but in a single call which is less visually disturbing. The <i>resize-arguments</i> are exactly the same arguments as for the <code>Resize</code> command and the <i>move-arguments</i> are exactly the same arguments as for the <code>Move</code> command except the <i>pointer</i> option which is not supported by the <code>ResizeMove</code> command. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
# Move window to top left corner and cover
# most of the screen
ResizeMove -10p -20p 0 0
# Grow the focused window towards the top of screen
<code>Current</code> <code>Resize</code> keep w+$[w.y]p keep 0
</pre>
</dl>
<p> Note: Fvwm may not be able to parse the command properly if the option <i>bottomright</i> of the <code>Resize</code> command is used.</dl>
<dt><code>ResizeMoveMaximize</code> <i>resize-arguments</i> <i>move-arguments</i></p>
<dd>
<dl>
<dt>
<dd> Combines the effects of <code>ResizeMove</code> and <code>Maximize</code> in a single command. When used on a maximized window, the window is resized and moved and is still in the maximized state afterwards. When used on an unmaximized window, the window is resized and put into the maximized state afterwards. This is useful if the user wants to resize the window temporarily and then return to the original geometry. The <i>resize-arguments</i> and <i>move-arguments</i> are the same as for the <code>ResizeMove</code> command.</dl>
<dt><code>RestackTransients</code></p>
<dd>
<dl>
<dt>
<dd> This command regroups the transients of a window close to it in the stacking order as if the window had just been lowered and then raised. The position of the window itself is not altered. Only windows that use either the <i>RaiseTransient</i> or <i>LowerTransient</i> style are affected at all. When <code>RestackTransients</code> is used on a transient window with the <i>StackTransientParent</i> style set, it is redirected to the parent window.</dl>
<dt><code>SetAnimation</code> <i>milliseconds-delay</i> [<i>fractions-to-move-list</i>]</p>
<dd>
<dl>
<dt>
<dd> Sets the time between frames and the list of fractional offsets to customize the animated moves of the <code>AnimatedMove</code> command and the animation of menus (if the menu style is set to animated; see <code>MenuStyle</code> command). If the <i>fractions-to-move-list</i> is omitted, only the time between frames is altered. The <i>fractions-to-move-list</i> specifies how far the window should be offset at each successive frame as a fraction of the difference between the starting location and the ending location. e.g.: </p>
<dl>
<dt>
<dd>
<pre>
SetAnimation 10 -.01 0 .01 .03 .08 .18 .3 \
  .45 .6 .75 .85 .90 .94 .97 .99 1.0
</pre>
</dl>
<p> Sets the delay between frames to 10 milliseconds, and sets the positions of the 16 frames of the animation motion. Negative values are allowed, and in particular can be used to make the motion appear more cartoonish, by briefly moving slightly in the opposite direction of the main motion. The above settings are the default.</dl>
<dt><code>SnapAttraction</code> [<i>proximity</i>&nbsp;<wbr>[<i>behaviour</i>]&nbsp;<wbr>[Screen]]</p>
<dd>
<dl>
<dt>
<dd> The <code>SnapAttraction</code> command is obsolete. It has been replaced by the <code>Style</code> command option <i>SnapAttraction</i>.</dl>
<dt><code>SnapGrid</code> [<i>x-grid-size</i>&nbsp;<wbr><i>y-grid-size</i>]</p>
<dd>
<dl>
<dt>
<dd> The <code>SnapGrid</code> command is obsolete. It has been replaced by the <code>Style</code> command option <i>SnapGrid</i>.</dl>
<dt><code>WindowsDesk</code> <i>arg1</i> [<i>arg2</i>]</p>
<dd>
<dl>
<dt>
<dd> Moves the selected window to another desktop. </p>
<p> This command has been removed and must be replaced by <code>MoveToDesk</code>, the arguments for which are the same as for the <code>GotoDesk</code> command. </p>
<p> <code>Important</code> </p>
<p> You cannot simply change the name of the command: the syntax has changed. If you used: </p>
<dl>
<dt>
<dd>
<pre>
WindowsDesk n
</pre>
</dl>
<p> to move a window to desk n, you have to change it to: </p>
<dl>
<dt>
<dd>
<pre>
<code>MoveToDesk</code> 0 n
</pre>
</dl>
</dl>
<dt><code>XorPixmap</code> [<i>pixmap</i>]</p>
<dd>
<dl>
<dt>
<dd> Selects the pixmap with which bits are xor&#8217;ed when doing rubber-band window moving or resizing. This has a better chance of making the rubber-band visible if <code>XorValue</code> does not give good results. An example pixmap <i>resize.rainbow.xpm</i> is provided with the icon distribution. To turn the <i>XorPixmap</i> off again use the <code>XorValue</code> command or omit the <i>pixmap</i> argument.</dl>
<dt><code>XorValue</code> [<i>number</i>]</p>
<dd>
<dl>
<dt>
<dd> Changes the value with which bits are xor&#8217;ed when doing rubber-band window moving or resizing. Valid values range from zero to the maximum value of an unsigned long integer on your system. Setting this value is a trial-and-error process. The default value 0 tries to find a value that gives a good contrast to black and white. The default value is used if the given <i>number</i> is omitted or invalid.</dl>
</dl>
<h3>Focus &amp; Mouse Movement</h3>
<dl>
<dt><code>CursorMove</code> <i>horizontal</i>[p] <i>vertical</i>[p]</p>
<dd>
<dl>
<dt>
<dd> Moves the mouse pointer by <i>horizontal</i> pages in the X direction and <i>vertical</i> pages in the Y direction. Either or both entries may be negative. Both horizontal and vertical values are expressed in percent of pages, so </p>
<dl>
<dt>
<dd>
<pre>
CursorMove 100 100
</pre>
</dl>
<p> means to move down and right by one full page. </p>
<dl>
<dt>
<dd>
<pre>
CursorMove 50 25
</pre>
</dl>
<p> means to move right half a page and down a quarter of a page. Alternatively, the distance can be specified in pixels by appending a &#8216;<i>p</i>&#8216; to the horizontal and/or vertical specification. For example </p>
<dl>
<dt>
<dd>
<pre>
CursorMove -10p -10p
</pre>
</dl>
<p> means move ten pixels up and ten pixels left. The CursorMove function should not be called from pop-up menus.</dl>
<dt><code>FlipFocus</code> [NoWarp]</p>
<dd>
<dl>
<dt>
<dd> Executes a <code>Focus</code> command as if the user had used the pointer to select the window. This command alters the order of the WindowList in the same way as clicking in a window to focus, i.e. the target window is removed from the <code>WindowList</code> and placed at the start. This command is recommended for use with the <code>Direction</code> command and in the function invoked from <code>WindowList</code>.</dl>
<dt><code>Focus</code> [NoWarp]</p>
<dd>
<dl>
<dt>
<dd> Sets the keyboard focus to the selected window. If the <i>NoWarp</i> argument is given, this is all it does. Otherwise it also moves the viewport or window as needed to make the selected window visible. This command does not automatically raise the window. Does not warp the pointer into the selected window (see <code>WarpToWindow</code> function). Does not de-iconify. This command does not alter the order of the <code>WindowList</code>, it rotates the <code>WindowList</code> around so that the target window is at the start. </p>
<p> When the <i>NoWarp</i> argument is given, Focus cannot transfer the keyboard focus to windows on other desks. </p>
<p> To raise and/or warp a pointer to a window together with <code>Focus</code> or <code>FlipFocus</code>, use a function, like: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> SelectWindow
+ I Focus
+ I <code>Iconify</code> false
+ I <code>Raise</code>
+ I <code>WarpToWindow</code> 50 8p
</pre>
</dl>
</dl>
<dt><code>WarpToWindow</code> [!raise | raise] <i>x</i>[p] <i>y</i>[p]</p>
<dd>
<dl>
<dt>
<dd> Warps the cursor to the associated window and raises it (unless the option <i>!raise</i> is present). The parameters <i>x</i> and <i>y</i> default to percentage of window down and in from the upper left hand corner (or number of pixels down and in if &#8216;<i>p</i>&#8216; is appended to the numbers). If a number is negative the opposite edge is used and the direction reversed. This command works also with windows that are not managed by fvwm. In this case fvwm does not bring the window onto the screen if it is not visible. For example it is possible to warp the pointer to the center of the root window on screen 1: </p>
<dl>
<dt>
<dd>
<pre>
<code>WindowId</code> root 1 WarpToWindow 50 50
</pre>
</dl>
</dl>
</dl>
<h3>Window State</h3>
<dl>
<dt><code>Close</code></p>
<dd>
<dl>
<dt>
<dd> If the window accepts the delete window protocol a message is sent to the window asking it to gracefully remove itself. If the window does not understand the delete window protocol then the window is destroyed as with the <code>Destroy</code> command. Note: if the window accepts the delete window protocol but does not close itself in response, the window is not deleted.</dl>
<dt><code>Delete</code></p>
<dd>
<dl>
<dt>
<dd> Sends a message to a window asking that it remove itself, frequently causing the application to exit.</dl>
<dt><code>Destroy</code></p>
<dd>
<dl>
<dt>
<dd> Destroys an application window, which usually causes the application to crash and burn.</dl>
<dt><code>Iconify</code> [<i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> Iconifies a window if it is not already iconified or de-iconifies it if it is already iconified. The optional argument <i>bool</i> is a boolean argument. &quot;<i>True</i>&quot; means only iconification is allowed, while &quot;<i>False</i>&quot; forces de-iconification. Using &quot;<i>toggle</i>&quot; switches between iconified and de-iconified states. </p>
<p> There are a number of <code>Style</code> options which influence the appearance and behavior of icons (e.g. <i>StickyIcon</i>, <i>NoIcon</i>). </p>
<p> For backward compatibility, the optional argument may also be a positive number instead of &quot;True&quot;, or a negative number instead of &quot;False&quot;. Note that this syntax is obsolete, and will be removed in the future.</dl>
<dt><code>Maximize</code> [<i>flags</i>] [<i>bool | forget</i>] [<i>horizontal</i>[p]] [<i>vertical</i>[p]]</p>
<dd>
<dl>
<dt>
<dd> Without its optional arguments (or if the <i>bool</i> bit has the value &quot;<i>toggle</i>&quot;) <code>Maximize</code> causes the window to alternately switch from a full-screen size to its normal size. To force a window into maximized (normal) state you can use a &quot;<i>True</i>&quot; or &quot;<i>False</i>&quot; value for the <i>bool</i> argument. </p>
<p> With just the parameter &quot;forget&quot; a maximized window reverts back into normal state but keeps its current maximized size. This can be useful in conjunction with the commands <code>ResizeMaximize</code> and <code>ResizeMoveMaximize</code>. If the window is not maximized, nothing happens. </p>
<p> With the optional arguments <i>horizontal</i> and <i>vertical</i>, which are expressed as percentage of a full screen, the user can control the new size of the window. An optional suffix &#8216;<i>p</i>&#8216; can be used to indicate pixels instead of percents of the screen size. If horizontal is greater than 0 then the horizontal dimension of the window is set to <i>horizontal</i>*screen_width/100. If the value is smaller than 0 the size is subtracted from the screen width, i.e. -25 is the same as 75. If <i>horizontal</i> is &quot;<i>grow</i>&quot;, it is maximized to curren available space until finding any obstacle. The vertical resizing is similar. If both horizontal and vertical values are &quot;grow&quot;, it expands vertically first, then horizontally to find space. Instead of the horizontal &quot;grow&quot; argument, &quot;<i>growleft</i>&quot; or &quot;<i>growright</i>&quot; can be used respectively &quot;<i>growup</i>&quot; and &quot;<i>growdown</i>&quot;. The optional <i>flags</i> argument is a space separated list containing the following key words: <i>ewmhiwa</i>, <i>growonwindowlayer</i>, <i>growonlayers</i> and <i>screen</i>. <i>ewmhiwa</i> causes fvwm to ignore the EWMH working area. <i>growonwindowlayer</i> causes the various grow methods to ignore windows with a layer other than the current layer of the window which is maximized. The <i>growonlayers</i> option must have two integer arguments. The first one is the minimum layer and the second one the maximum layer to use. Windows that are outside of this range of layers are ignored by the grow methods. A negative value as the first or second argument means to assume no minimum or maximum layer. <i>screen</i> must have an argument which specifies the Xinerama screen on which to operate. It can be &#8216;p&#8217; for the primary screen, &#8216;c&#8217; for the current screen (containing the mouse pointer), &#8216;g&#8217; for the global screen or the screen number itself (counting from zero). This option is only useful with multiple Xinerama screens. </p>
<p> Here are some examples. The following adds a title-bar button to switch a window to the full vertical size of the screen: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize 0 100
</pre>
</dl>
<p> The following causes windows to be stretched to the full width: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize 100 0
</pre>
</dl>
<p> This makes a window that is half the screen size in each direction: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize 50 50
</pre>
</dl>
<p> To expand a window horizontally until any other window is found: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize 0 grow
</pre>
</dl>
<p> To expand a window until any other window on the same or a higher layer is hit. </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize growonlayers $[w.layer] -1 grow grow
</pre>
</dl>
<p> To expand a window but leave the lower 60 pixels of the screen unoccupied: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 0 4 A Maximize 100 -60p
</pre>
</dl>
<p> Values larger than 100 can be used with caution.</dl>
<dt><code>Recapture</code></p>
<dd>
<dl>
<dt>
<dd> This command is obsolete and should not be used anymore. Should you want to do something specific that you cannot do without it, please report this to the fvwm-workers mailing list &lt;fvwm-workers [at] fvwm.org&gt;. This command may be removed at some point in the future. Please read the note at the end of the section <code>Delayed Execution of Commands</code> to learn about how to avoid the <code>Recapture</code> command. </p>
<p> Causes fvwm to recapture all of its windows. This ensures that the latest style parameters are used. The recapture operation is visually disturbing. </p>
<p> Since fvwm version 2.4 only a very few <code>Style</code> options need a <code>Recapture</code> to take effect (e.g. <i>UseStyle</i>).</dl>
<dt><code>RecaptureWindow</code></p>
<dd>
<dl>
<dt>
<dd> This command is obsolete and should not be used anymore. See <code>Recapture</code> For details. </p>
<p> Causes fvwm to recapture the chosen window.</dl>
<dt><code>Refresh</code></p>
<dd>
<dl>
<dt>
<dd> Causes all windows on the screen to redraw themselves. All pending updates of all windows&#8217; styles and looks are applied immediately. E.g. if <code>Style</code> or <code>TitleStyle</code> commands were issued inside a fvwm function.</dl>
<dt><code>RefreshWindow</code></p>
<dd>
<dl>
<dt>
<dd> Causes the chosen window to redraw itself. All pending updates of the window&#8217;s style and look are applied immediately. E.g. if <code>Style</code> or <code>TitleStyle</code> commands were issued inside a fvwm function.</dl>
<dt><code>Stick</code> [<i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> If the <i>bool</i> argument is empty or &quot;<i>toggle</i>&quot;, the <code>Stick</code> command makes a window sticky if it is not already sticky, or non-sticky if it is already sticky. To make a window sticky regardless of its current state the <i>bool</i> argument must be &quot;True&quot;. To make it non-sticky use &quot;False&quot;.</dl>
<dt><code>StickAcrossPages</code> [<i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> Works like <code>Stick</code> but only sticks a window across pages, not across desks.</dl>
<dt><code>StickAcrossDesks</code> [<i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> Works like <code>Stick</code> but only sticks a window across desks, not across pages.</dl>
<dt><code>WindowShade</code> [bool] | [[ShadeAgain]&nbsp;<wbr><i>direction</i>]</p>
<dd>
<dl>
<dt>
<dd> Toggles the window shade feature for titled windows. Windows in the shaded state only display a title-bar. If <i>bool</i> is not given or &quot;<i>toggle</i>&quot;, the window shade state is toggled. If <i>bool</i> is &quot;True&quot;, the window is forced to the shaded state. If <i>bool</i> is &quot;False&quot;, then the window is forced to the non-shaded state. To force shading in a certain direction, the <i>direction</i> argument can be used. Any of the strings &quot;<i>North</i>&quot;, &quot;<i>South</i>&quot;, &quot;<i>West</i>&quot;, &quot;<i>East</i>&quot;, &quot;<i>NorthWest</i>&quot;, &quot;<i>NorthEast</i>&quot;, &quot;<i>SouthWest</i>&quot;, &quot;<i>SouthEast</i>&quot; or &quot;<i>Last</i>&quot; can be given. The direction can be abbreviated with the usual one or two letters &quot;<i>N</i>&quot;, &quot;<i>NW</i>&quot;, etc. Using a direction on a window that was already shaded unshades the window. To shade it in a different direction, use the <i>ShadeAgain</i> option. The direction <i>Last</i> shades the window in the direction it last was shaded. If the window has never been shaded before it is shaded as if no direction had been given. Windows without titles can be shaded too. Please refer also to the options <i>WindowShadeSteps</i>, <i>WindowShadeShrinks</i>, <i>WindowShadeScrolls</i>, <i>WindowShadeLazy</i>, <i>WindowShadeAlwaysLazy</i> and <i>WindowShadeBusy</i> options of the <code>Style</code> command. Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>WindowShadeShrinks</i>, <i>WindowShadeSteps</i> 20, \
        <i>WindowShadeLazy</i>
<code>Mouse</code> 1 - S WindowShade North
<code>Mouse</code> 1 [ S WindowShade West
<code>Mouse</code> 1 ] S WindowShade E
<code>Mouse</code> 1 _ S WindowShade S
</pre>
</dl>
<p> Note: When a window that has been shaded with a <i>direction</i> argument changes the direction of the window title (see <i>TitleAtTop</i> <code>Style</code> option), the shading direction does not change. This may look very strange. Windows that were shaded without a <i>direction</i> argument stay shaded in the direction of the title bar. </p>
<p> For backward compatibility, the optional argument may also be 1 to signify &quot;on&quot;, and 2 to signify &quot;off&quot;. Note that this syntax is obsolete, and will be removed in the future.</dl>
<dt><code>WindowShadeAnimate</code> [<i>steps</i>&nbsp;<wbr>[p]]</p>
<dd>
<dl>
<dt>
<dd> This command is obsolete. Please use the <i>WindowShadeSteps</i> option of the <code>Style</code> command instead.</dl>
</dl>
<h3>Mouse, Key &amp; Stroke Bindings</h3>
<dl>
<dt><code>IgnoreModifiers</code> [<i>Modifiers</i>]</p>
<dd>
<dl>
<dt>
<dd> Tells fvwm which modifiers to ignore when matching Mouse or Key bindings. <code>IgnoreModifiers</code> affects the <i>ClickToFocus</i> style too. This command belongs into your <i>config</i>. If you issue it when your fvwm session is already up and running the results are unpredictable. The should appear before any applications or modules are started in your <i>config</i> file (e.g. with the <code>Exec</code> command). </p>
<p> <i>Modifiers</i> has the same syntax as in the <code>Mouse</code> or <code>Key</code> bindings, with the addition of &#8216;L&#8217; meaning the <font SIZE="-1">caps lock</font> key. The default is &quot;L&quot;. <i>Modifiers</i> can be omitted, meaning no modifiers are ignored. This command comes in handy if the <font SIZE="-1">num-lock</font> and <font SIZE="-1">scroll-lock</font> keys interfere with your shortcuts. With XFree86 &#8216;2&#8217; usually is the <font SIZE="-1">num-lock</font> modifier and &#8216;5&#8217; refers to the <font SIZE="-1">scroll-lock</font> key. To turn all these pesky modifiers off you can use this command: </p>
<dl>
<dt>
<dd>
<pre>
IgnoreModifiers L25
</pre>
</dl>
<p> If the <i>Modifiers</i> argument is the string &quot;<i>default</i>&quot;, fvwm reverts back to the default value &quot;L&quot;. </p>
<p> <code>Important</code> This command creates a lot of extra network traffic, depending on your CPU, network connection, the number of <code>Key</code> or <code>Mouse</code> commands in your configuration file and the number of modifiers you want to ignore. If you do not have a lightning fast machine or very few bindings you should not ignore more than two modifiers. I.e. do not ignore <font SIZE="-1">scroll-lock</font> if you have no problem with it. In the <i>FAQ</i> you can find a better solution of this problem.</dl>
<dt><code>EdgeCommand</code> [<i>direction</i>&nbsp;<wbr>[<i>Function</i>]]</p>
<dd>
<dl>
<dt>
<dd> Binds a specified fvwm command <i>Function</i> to an edge of the screen. Direction may be one of &quot;<i>North</i>&quot;, &quot;<i>Top</i>&quot;, &quot;<i>West</i>&quot;, &quot;<i>Left</i>&quot;, &quot;<i>South</i>&quot;, &quot;<i>Bottom</i>&quot;, &quot;<i>Right</i>&quot; and &quot;<i>East</i>&quot;. If <i>Function</i> is omitted the binding for this edge is removed. If EdgeCommand is called without any arguments all edge bindings are removed. </p>
<p> <i>Function</i> is executed when the mouse pointer enters the invisible pan frames that surround the visible screen. The binding works only if <code>EdgeThickness</code> is set to a value greater than 0. If a function is bound to an edge, scrolling specified by <code>EdgeScroll</code> is disabled for this edge. It is possible to bind a function only to some edges and use the other edges for scrolling. This command is intended to raise or lower certain windows when the mouse pointer enters an edge. <code>FvwmAuto</code> can be used get a delay when raising or lowering windows. The following example raises <code>FvwmButtons</code> if the mouse pointer enters the top edge of the screen. </p>
<dl>
<dt>
<dd>
<pre>
# Disable EdgeScrolling but make it possible
# to move windows over the screen edge
<code>EdgeResistance</code> -1
<code>Style</code> * EdgeMoveDelay 250
<code>Style</code> * EdgeMoveResistance 20
# Set thickness of the edge of the screen to 1
<code>EdgeThickness</code> 1
# Give focus to FvwmButtons if the mouse
# hits top edge
EdgeCommand Top <code>Next</code> (FvwmButtons) <code>Focus</code>
# Make sure the <code>Next</code> command matches the window
<code>Style</code> FvwmButtons CirculateHit
<code>Module</code> <code>FvwmButtons</code>
<code>Module</code> <code>FvwmAuto</code> 100 &quot;Silent AutoRaiseFunction&quot; \
     &quot;Silent AutoLowerFunction&quot;
# If any window except FvwmButtons has
# focus when calling this function
# FvwmButtons are lowered
<code>DestroyFunc</code> AutoLowerFunction
<code>AddToFunc</code> AutoLowerFunction
+ I <code>Current</code> (!FvwmButtons) <code>All</code> (FvwmButtons) <code>Lower</code>
# If FvwmButtons has focus when calling this function raise it
<code>DestroyFunc</code> AutoRaiseFunction
<code>AddToFunc</code> AutoRaiseFunction
+ I <code>Current</code> (FvwmButtons) <code>Raise</code>
</pre>
</dl>
<p> Normally, the invisible pan frames are only on the screen edges that border virtual pages. If a screen edge has a command bound to it, the pan frame is always created on that edge.</dl>
<dt><code>EdgeLeaveCommand</code> [<i>direction</i>&nbsp;<wbr>[<i>Function</i>]]</p>
<dd>
<dl>
<dt>
<dd> Binds a specified fvwm command <i>Function</i> to an edge of the screen. Direction may be one of &quot;<i>North</i>&quot;, &quot;<i>Top</i>&quot;, &quot;<i>West</i>&quot;, &quot;<i>Left</i>&quot;, &quot;<i>South</i>&quot;, &quot;<i>Bottom</i>&quot;, &quot;<i>Right</i>&quot; and &quot;<i>East</i>&quot;. If <i>Function</i> is omitted the binding for this edge is removed. If EdgeLeaveCommand is called without any arguments all edge bindings are removed. </p>
<p> <i>Function</i> is executed when the mouse pointer leaves the invisible pan frames that surround the visible screen. The binding works only if <code>EdgeThickness</code> is set to a value greater than 0. If a function is bound to an edge, scrolling specified by <code>EdgeScroll</code> is disabled for this edge. It is possible to bind a function only to some edges and use the other edges for scrolling. This command is intended to raise or lower certain windows when the mouse pointer leaves an edge. <code>FvwmAuto</code> can be used get a delay when raising or lowering windows. See example for <code>EdgeCommand</code> </p>
<p> Normally, the invisible pan frames are only on the screen edges that border virtual pages. If a screen edge has a command bound to it, the pan frame is always created on that edge.</dl>
<dt><code>GnomeButton</code></p>
<dd>
<dl>
<dt>
<dd> Used in conjunction with <code>Mouse</code> to pass mouse button presses on the root window to a GNOME program (such as GMC). The following example passes presses of mouse buttons 1 and 3 to such a program. </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 R A GnomeButton
<code>Mouse</code> 3 R A GnomeButton
</pre>
</dl>
</dl>
<dt><code>Key</code> [(<i>window</i>)] <i>Keyname</i> <i>Context</i> <i>Modifiers</i> <i>Function</i></p>
<dd>
<dl>
<dt>
<dd> Binds a keyboard key to a specified fvwm command, or removes the binding if <i>Function</i> is &#8216;-&#8216;. The syntax is the same as for a <code>Mouse</code> binding except that the mouse button number is replaced with a <i>Keyname</i>. Normally, the key binding is activated when the key is pressed. <i>Keyname</i> is a standard X11 key name as defined in <i>/usr/include/X11/keysymdef.h</i>, (without the <i>XK_</i> prefix), or the keysym database <i>/usr/X11R6/lib/X11/XKeysymDB</i>. Only key names that are generated with no modifier keys or with just the <font SIZE="-1">Shift</font> key held are guaranteed to work. The <i>Context</i> and <i>Modifiers</i> fields are defined as in the <code>Mouse</code> binding. However, when you press a key the context window is the window that has the keyboard focus. That is not necessarily the same as the window the pointer is over (with <i>SloppyFocus</i> or <i>ClickToFocus</i>). Note that key bindings with the &#8216;<i>R</i>&#8216; (root window) context do not work properly with <i>SloppyFocus</i> and <i>ClickToFocus</i>. If you encounter problems, use the <code>PointerKey</code> command instead. If you want to bind keys to a window with <i>SloppyFocus</i> or <i>ClickToFocus</i> that are supposed to work when the pointer is not over the window, fvwm assumes the pointer is over the client window (i.e. you have to use the &#8216;W&#8217; context). </p>
<p> The special context &#8216;<i>M</i>&#8216; for menus can be used to (re)define the menu controls. It be used alone or together with &#8216;T&#8217;, &#8216;S&#8217;, &#8216;I&#8217;, &#8216;[&#8216;, &#8216;]&#8217;, &#8216;-&#8216; and &#8216;_&#8217;. See the <code>Menu Bindings</code> section for details. </p>
<p> The following example binds the built-in window list to pop up when <font SIZE="-1">Alt-Ctrl-Shift-F11</font> is hit, no matter where the mouse pointer is: </p>
<dl>
<dt>
<dd>
<pre>
Key F11 A SCM <code>WindowList</code>
</pre>
</dl>
<p> Binding a key to a title-bar button causes that button to appear. Please refer to the <code>Mouse</code> command for details.</dl>
<dt><code>Mouse</code> [(<i>window</i>)] <i>Button</i> <i>Context</i> <i>Modifiers</i> <i>Function</i></p>
<dd>
<dl>
<dt>
<dd> Defines a mouse binding, or removes the binding if <i>Function</i> is &#8216;-&#8216;. <i>Button</i> is the mouse button number. If <i>Button</i> is zero then any button performs the specified function. Note that only mouse buttons 1 to 5 are fully supported by X11. Any number above this works only partially. Complex functions can not be used with these buttons and neither any operation that requires dragging the pointer with the button held. This is due to limitations of X11. By default, the highest allowed button number is 9. </p>
<p> <i>Context</i> describes where the binding applies. Valid contexts are &#8216;<i>R</i>&#8216; for the root window, &#8216;<i>W</i>&#8216; for an application window, &#8216;<i>D</i>&#8216; for a desktop application (as kdesktop or Nautilus desktop), &#8216;<i>T</i>&#8216; for a window title-bar, &#8216;<i>S</i>&#8216; for a window side, top, or bottom bar, &#8216;<i>[</i>&#8216;, &#8216;<i>]</i>&#8216;, &#8216;<i>&#8211;</i>&#8216; and &#8216;<i>_</i>&#8216; for the left, right, top or bottom side only, &#8216;<i>F</i>&#8216; for a window frame (the corners), &#8216;&lt;&#8216;, &#8216;^&#8217;, &#8216;&gt;&#8217; and &#8216;<i>v</i>&#8216; for the top left, top right, bottom right or bottom left corner, &#8216;<i>I</i>&#8216; for an icon window, or &#8216;<i>0</i>&#8216; through &#8216;<i>9</i>&#8216; for title-bar buttons, or any combination of these letters. &#8216;<i>A</i>&#8216; is for any context. For instance, a context of &quot;FST&quot; applies when the mouse is anywhere in a window&#8217;s border except the title-bar buttons. Only &#8216;S&#8217; and &#8216;W&#8217; are valid for an undecorated window. </p>
<p> The special context &#8216;<i>M</i>&#8216; for menus can be used to (re)define the menu controls. It can be used alone or together with &#8216;T&#8217;, &#8216;S&#8217;, &#8216;I&#8217;, &#8216;[&#8216;, &#8216;]&#8217;, &#8216;-&#8216; and &#8216;_&#8217;. See the <code>Menu Bindings</code> section for details. </p>
<p> The special context &#8216;<i>P</i>&#8216; controls what buttons that can be used to place a window. When using this context no modifiers are allowed (<i>Modifiers</i> must be N), no <i>window</i> is allowed, and the <i>Function</i> must be one of <i>PlaceWindow</i>, <i>PlaceWindowDrag</i>, <i>PlaceWindowInteractive</i>, <i>CancelPlacement</i>, <i>CancelPlacementDrag</i>, <i>CancelPlacementInteractive</i> or <i>&#8211;</i>. </p>
<p> <i>PlaceWindow</i> makes <i>Button</i> usable for window placement, both for interactive and drag move. <i>CancelPlacement</i> does the inverse. That is makes <i>Button</i> to cancel move for both interactive and drag move. It may however not override how new windows are resized after being placed. This is controlled by the <code>Emulate</code> command. Also a window being dragged can always be placed by releasing the button hold while dragging, regardless of if it is set to <i>PlaceWindow</i> or not. </p>
<p> <i>PlaceWindowDrag</i> and <i>PlaceWindowInteractive</i>/<i>CancelPlacementDrag</i> and <i>CancelPlacementInteractive</i> work as <i>PlaceWindow</i>/<i>CancelPlacement</i> with the exception that they only affect either windows dragged / placed interactively. </p>
<p> <i>&#8211;</i> is equivalent to <i>CancelPlacement</i>. </p>
<p> The following example makes all buttons but button 3 usable for interactive placement and makes drag moves started by other buttons than one cancel if button 1 is pressed before finishing the move: </p>
<dl>
<dt>
<dd>
<pre>
Mouse 0 P N PlaceWindow
Mouse 3 P N CancelPlacement
Mouse 1 P N CancelPlacementDrag
</pre>
</dl>
<p> By default, the binding applies to all windows. You can specify that a binding only applies to specific windows by specifying the window name in brackets. The window name is a wildcard pattern specifying the class, resource or name of the window you want the binding to apply to. </p>
<p> The following example shows how the same key-binding can be used to perform different functions depending on the window that is focused: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> (rxvt)  V A C <code>Echo</code> ctrl-V-in-RXVT
<code>Key</code> (*term) V A C <code>Echo</code> ctrl-V-in-Term
<code>Key</code> (*vim)  V A C --
<code>Key</code>         V A C <code>Echo</code> ctrl-V-elsewhere
</pre>
</dl>
<p> A &#8216;<i>&#8212;</i>&#8216; action indicates that the event should be propagated to the specified window to handle. This is only a valid action for window-specific bindings. </p>
<p> This example shows how to display the WindowList when Button 3 is pressed on an rxvt window: </p>
<dl>
<dt>
<dd>
<pre>
Mouse (rxvt) 3 A A <code>WindowList</code>
</pre>
</dl>
<p> Note that Fvwm actually intercepts all events for a window-specific binding and (if the focused window doesn&#8217;t match any of the bindings) sends a synthetic copy of the event to the window. This should be transparent to most applications, however (for security reasons) some programs ignore these synthetic events by default &#8211; xterm is one of them. To enable handling of these events, add the following line to your <i>~/.Xdefaults</i> file: </p>
<dl>
<dt>
<dd>
<pre>
XTerm*allowSendEvents:  true
</pre>
</dl>
<p> <i>Modifiers</i> is any combination of &#8216;<i>N</i>&#8216; for no modifiers, &#8216;<i>C</i>&#8216; for control, &#8216;<i>S</i>&#8216; for shift, &#8216;<i>M</i>&#8216; for Meta, &#8216;<i>L</i>&#8216; for Caps-Lock or &#8216;<i>A</i>&#8216; for any modifier. For example, a modifier of &quot;SM&quot; applies when both the <font SIZE="-1">Meta</font> and <font SIZE="-1">Shift</font> keys are down. X11 modifiers mod1 through mod5 are represented as the digits &#8216;1&#8217; through &#8216;5&#8217;. The modifier &#8216;L&#8217; is ignored by default. To turn it on, use the <code>IgnoreModifiers</code> command. </p>
<p> <i>Function</i> is one of fvwm&#8217;s commands. </p>
<p> The title-bar buttons are numbered with odd numbered buttons on the left side of the title-bar and even numbers on the right. Smaller-numbered buttons are displayed toward the outside of the window while larger-numbered buttons appear toward the middle of the window (0 is short for 10). In summary, the buttons are numbered: </p>
<dl>
<dt>
<dd>
<pre>
1 3 5 7 9    0 8 6 4 2
</pre>
</dl>
<p> The highest odd numbered button which has an action bound to it determines the number of buttons drawn on the left side of the title bar. The highest even number determines the number of right side buttons which are drawn. Actions can be bound to either mouse buttons or keyboard keys.</dl>
<dt><code>PointerKey</code> [(<i>window</i>)] <i>Keyname</i> <i>Context</i> <i>Modifiers</i> <i>Function</i></p>
<dd>
<dl>
<dt>
<dd> This command works exactly like the <code>Key</code> command. The only difference is that the binding operates on the window under the pointer. Normal key bindings operate on the focused window instead. The <code>PointerKey</code> command can for example be used to bind keys to the root window if you are using <i>SloppyFocus</i> or <i>ClickToFocus</i>. However, some applications (xterm is one example) are unable to handle this key anymore, even if the pointer is over the xterm window. It is recommended to use the <code>PointerKey</code> command only for key combinations that are not needed in any application window. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * <i>SloppyFocus</i>
PointerKey f1 a m <code>Menu</code> MainMenu
</pre>
</dl>
</dl>
<dt><code>Stroke</code> [(<i>window</i>)] <i>Sequence</i> <i>Button</i> <i>Context</i> <i>Modifiers</i> <i>Function</i></p>
<dd>
<dl>
<dt>
<dd> Binds a mouse stroke sequence to a specified fvwm command, or removes the binding if <i>Function</i> is &#8216;-&#8216;. The syntax is the same as for a <code>Mouse</code> binding except that <i>Sequence</i> is inserted in front of the button number and a value of 0 for <i>Button</i> concerns the <code>StrokeFunc</code> command. The <i>Context</i> and <i>Modifiers</i> fields are defined as in the <code>Mouse</code> binding. However, only the &#8216;<i>R</i>&#8216; Context really works (if you want to use other contexts you need to use the <code>StrokeFunc</code> below). </p>
<p> Strokes sequences are defined in a telephone grid like this: </p>
<dl>
<dt>
<dd>
<pre>
 1  2  3
 4  5  6
 7  8  9
</pre>
</dl>
<p> or in a numeric pad grid like this: </p>
<dl>
<dt>
<dd>
<pre>
 7  8  9
 4  5  6
 1  2  3
</pre>
</dl>
<p> The telephone grid is used by default, to use the numeric pad grid you should begin the sequence with a &#8216;<i>N</i>&#8216;. Note that a complex motion may produce several different sequences (see the &quot;netscape&quot; example below to handle such motion). Moreover, sequences are limited to 20 elements (with the present version of <code>libstroke</code>), however, in practice it is preferable to use sequence with less than 12 elements. </p>
<p> Because of the default button menu in fvwm, you may need to remove a mouse button binding (using an empty action) before using the stroke </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 3 R N
</pre>
</dl>
<p> Also, you can still use the stroke &quot;sequence 0&quot; to simulate a click: </p>
<dl>
<dt>
<dd>
<pre>
Stroke 0 3 R N <code>Menu</code> <code>WindowList</code> <code>Nop</code>
</pre>
</dl>
<p> The following example starts xterm when the mouse drags an &#8216;I&#8217; on the root window with button 3 pressed down: </p>
<dl>
<dt>
<dd>
<pre>
Stroke 258  3  R  N  <code>Exec</code> exec xterm
</pre>
</dl>
<p> An example for Netscape: </p>
<dl>
<dt>
<dd>
<pre>
Stroke 7415963    3  R  N  <code>Exec</code> exec netscape
Stroke 74148963   3  R  N  <code>Exec</code> exec netscape
Stroke 74158963   3  R  N  <code>Exec</code> exec netscape
Stroke 7418963    3  R  N  <code>Exec</code> exec netscape
Stroke 415963     3  R  N  <code>Exec</code> exec netscape
</pre>
</dl>
<p> You may prefer to use the numeric pad grid since you have such a grid on your machine. Here an example: </p>
<dl>
<dt>
<dd>
<pre>
Stroke N78963214   3  R  N <code>FvwmForm</code> FvwmForm-QuitVerify
Stroke N789632147  3  R  N <code>FvwmForm</code> FvwmForm-QuitVerify
</pre>
</dl>
<p> This example starts the &quot;QuitVerify&quot; form if you draw a box that begins in the top left corner. </p>
<p> Note: You need <code>libstroke</code> installed and fvwm compiled with stroke support. <code>libstroke</code> can be obtained at <i><a rel="nofollow" href="http://www.etla.net/~willey/projects/libstroke/">http://www.etla.net/~willey/projects/libstroke/</a></i></dl>
<dt><code>StrokeFunc</code> [<i>Options</i>]</p>
<dd>
<dl>
<dt>
<dd> Causes fvwm to record a mouse stroke sequence and to execute the corresponding action as defined in a <code>Stroke</code> command. The cursor is modified to the <i>STROKE</i> context of the <code>CursorStyle</code> command during recording. When the stroke is finished <code>StrokeFunc</code> looks for a stroke binding of the form </p>
<dl>
<dt>
<dd>
<pre>
<code>Stroke</code> sequence 0 Context Modifiers action
</pre>
</dl>
<p> and executes the corresponding action (Note the 0). Normal use of this function is via a <code>Mouse</code> or <code>Key</code> command. Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 3 A M StrokeFunc
<code>Key</code> x R N StrokeFunc
</pre>
</dl>
<p> If you press mouse button 3 and <font SIZE="-1">Alt</font> anywhere (respectively, press the key x when the cursor is on the root window), then fvwm records the mouse motions until the mouse button 3 (respectively, the x key) is released and then check if the recorded <i>sequence</i> corresponds to a stroke binding of the form </p>
<dl>
<dt>
<dd>
<pre>
&quot;Stroke <i>sequence</i> 0 A M <i>action</i>&quot;
&quot;Stroke <i>sequence</i> 0 R N <i>action</i>&quot;
</pre>
</dl>
<p> Note that the <i>Context</i> and <i>Modifiers</i> are taken at the beginning of the execution of the <code>StrokeFunc</code> command (so you can release the modifiers before the end of the stroke recording in the case of a mouse binding and if you used, say, a title-bar context the mouse motion can go through an application window). The keys <font SIZE="-1">Escape</font> and <font SIZE="-1">Delete</font> allow you to abort the command. </p>
<p> The <code>StrokeFunc</code> command has five options: <i>NotStayPressed</i>, <i>EchoSequence</i>, <i>DrawMotion</i>, <i>FeedBack</i> and <i>StrokeWidth</i>. These options are disabled by default. <i>EchoSequence</i> causes fvwm to Echo the recorded stroke sequence. <i>DrawMotion</i> causes fvwm to draw the mouse motion on the screen. <i>FeedBack</i> causes fvwm to display during a fraction of second the cursor of the <i>WAIT</i> context of the <code>CursorStyle</code> command if the recorded stroke sequence corresponds to a stroke binding. <i>StrokeWidth</i> takes an integer argument, which must be &gt;= 0 and &lt;= 100 and which defines the width of the line for the <i>DrawMotion</i> option. </p>
<p> <i>NotStayPressed</i> works only if <code>StrokeFunc</code> is used via a <code>Mouse</code> or a <code>Key</code> command. This option removes the need to have a button or the key pressed during the stroke, but you have to do a mouse click or press the <font SIZE="-1">Return</font> or <font SIZE="-1">Space</font> key to finish the mouse motion recording (these keys also work without the <i>NotStayPressed</i> option). </p>
<p> You can use the <code>StrokeFunc</code> &quot;alone&quot;. In this case it works as above with the <i>NotStayPressed</i> option enabled. However, <i>Modifiers</i>, in general, may not work as expected (i.e., in this case use &#8216;A&#8217; or &#8216;N&#8217; as <i>Modifiers</i> in the stroke bindings). </p>
<p> Note that some computers do not support key release events. If that is the case the <code>StrokeFunc</code> used via a <code>Key</code> command works as if the <i>NotStayPressed</i> option is enabled.</dl>
</dl>
<h3>Controlling Window Styles</h3>
<p> For readability, the commands in this section are not sorted alphabetically. The description of the <code>Style</code> command can be found at the end of this section.</p>
<dl>
<dt><code>FocusStyle</code> <i>stylename</i> <i>options</i></p>
<dd>
<dl>
<dt>
<dd> works exactly like the <code>Style</code> command, but accepts only the focus policy related styles beginning with &quot;FP&quot;. The prefix can be removed, but at the cost of a little bit of time. <code>FocusStyle</code> is meant to make the configuration file more readable. Example: </p>
<dl>
<dt>
<dd>
<pre>
FocusStyle * EnterToFocus, !LeaveToUnfocus
</pre>
</dl>
<p> is equivalent to </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * FPEnterToFocus, !FPLeaveToUnfocus
</pre>
</dl>
</dl>
<dt><code>DestroyStyle</code> <i>style</i></p>
<dd>
<dl>
<dt>
<dd> deletes the style named <i>style</i>. The changes take effect immediately. Note that <i>style</i> is not a wild-carded search string, but rather a case-sensitive string that should exactly match the original <code>Style</code> command. </p>
<p> Destroying style &quot;*&quot; can be done, but isn&#8217;t really to be recommended. For example: </p>
<dl>
<dt>
<dd>
<pre>
DestroyStyle Application*
</pre>
</dl>
<p> This removes all settings for the style named &quot;Application*&quot;, NOT all styles starting with &quot;Application&quot;.</dl>
<dt><code>DestroyWindowStyle</code></p>
<dd>
<dl>
<dt>
<dd> deletes the styles set by the <code>WindowStyle</code> command on the selected window. The changes take effect immediately.</dl>
<dt><code>UpdateStyles</code></p>
<dd>
<dl>
<dt>
<dd> All pending updates of all windows&#8217; styles and looks are applied immediately. E.g. if <code>Style</code>, <i>WindowStyle</i> or <i>TitleStyle</i> commands were issued inside a fvwm function.</dl>
<dt><code>Style</code> <i>stylename</i> <i>options</i> &#8230;</p>
<dd>
<dl>
<dt>
<dd> The <code>Style</code> command is used to set attributes of a window to values other than the default or to set the window manager default styles. </p>
<p> <i>stylename</i> can be a window&#8217;s name, class, visible name, or resource string. It may contain the wildcards &#8216;*&#8217; and &#8216;?&#8217;, which are matched in the usual Unix filename manner. Multiple style options in a single <code>Style</code> command are read from left to right as if they were issued one after each other in separate commands. A given style always overrides all conflicting styles that have been issued earlier (or further left on the same style line). </p>
<p> Note: windows that have no name (WM_NAME) are given a name of &quot;Untitled&quot;, and windows that do not have a class (WM_CLASS, res_class) are given class &quot;NoClass&quot; and those that do not have a resource (WM_CLASS, res_name) are given resource &quot;NoResource&quot;. </p>
<p> If a window has the resource &quot;fvwmstyle&quot; set, the value of that resource is used in addition to any window names when selecting the style. </p>
<p> <i>options</i> is a comma separated list containing one or more of the following keywords. Each group of style names is separated by slashes (&#8216;/&#8217;). The last style in these groups is the default. <i>BorderWidth</i>, <i>HandleWidth</i>, <i>!Icon</i> / <i>Icon</i>, <i>MiniIcon</i>, <i>IconBox</i>, <i>IconGrid</i>, <i>IconFill</i>, <i>IconSize</i>, <i>!Title</i> / <i>Title</i>, <i>TitleAtBottom</i> / <i>TitleAtLeft</i> / <i>TitleAtRight</i> / <i>TitleAtTop</i>, <i>LeftTitleRotatedCW</i> / <i>LeftTitleRotatedCCW</i>, <i>RightTitleRotatedCCW</i> / <i>RightTitleRotatedCW</i>, <i>TopTitleRotated</i> / <i>TopTitleNotRotated</i>, <i>BottomTitleRotated</i> / <i>BottomTitleNotRotated</i>, <i>!UseTitleDecorRotation</i> / <i>UseTitleDecorRotation</i>, <i>StippledTitle</i> / <i>!StippledTitle</i>, <i>StippledIconTitle</i> / <i>!StippledIconTitle</i>, <i>IndexedWindowName</i> / <i>ExactWindowName</i>, <i>IndexedIconName</i> / <i>ExactIconName</i>, <i>TitleFormat</i> / <i>IconTitleFormat</i> / <i>!Borders</i> / <i>Borders</i>, <i>!Handles</i> / <i>Handles</i>, <i>WindowListSkip</i> / <i>WindowListHit</i>, <i>CirculateSkip</i> / <i>CirculateHit</i>, <i>CirculateSkipShaded</i> / <i>CirculateHitShaded</i>, <i>CirculateSkipIcon</i> / <i>CirculateHitIcon</i>, <i>Layer</i>, <i>StaysOnTop</i> / <i>StaysOnBottom</i> / <i>StaysPut</i>, <i>Sticky</i> / <i>Slippery</i>, <i>StickyAcrossPages</i> / <i>!StickyAcrossPages</i>, <i>StickyAcrossDesks</i> / <i>!StickyAcrossDesks</i>, <i>!StickyStippledTitle</i> / <i>StickyStippledTitle</i>, <i>!StickyStippledIconTitle</i> / <i>StickyStippledIconTitle</i>, <i>StartIconic</i> / <i>StartNormal</i>, <i>Color</i>, <i>ForeColor</i>, <i>BackColor</i>, <i>Colorset</i>, <i>HilightFore</i>, <i>HilightBack</i>, <i>HilightColorset</i>, <i>BorderColorset</i>, <i>HilightBorderColorset</i>, <i>IconTitleColorset</i>, <i>HilightIconTitleColorset</i>, <i>IconBackgroundColorset</i>, <i>IconTitleRelief</i>, <i>IconBackgroundRelief</i>, <i>IconBackgroundPadding</i>, <i>Font</i>, <i>IconFont</i>, <i>StartsOnDesk</i> / <i>StartsOnPage</i> / <i>StartsAnyWhere</i>, <i>StartsOnScreen</i>, <i>StartShaded</i> / <i>!StartShaded</i>, <i>ManualPlacementHonorsStartsOnPage</i> / <i>ManualPlacementIgnoresStartsOnPage</i>, <i>CaptureHonorsStartsOnPage</i> / <i>CaptureIgnoresStartsOnPage</i>, <i>RecaptureHonorsStartsOnPage</i> / <i>RecaptureIgnoresStartsOnPage</i>, <i>StartsOnPageIncludesTransients</i> / <i>StartsOnPageIgnoresTransients</i>, <i>IconTitle</i> / <i>!IconTitle</i>, <i>MwmButtons</i> / <i>FvwmButtons</i>, <i>MwmBorder</i> / <i>FvwmBorder</i>, <i>MwmDecor</i> / <i>!MwmDecor</i>, <i>MwmFunctions</i> / <i>!MwmFunctions</i>, <i>HintOverride</i> / <i>!HintOverride</i>, <i>!Button</i> / <i>Button</i>, <i>ResizeHintOverride</i> / <i>!ResizeHintOverride</i>, <i>OLDecor</i> / <i>!OLDecor</i>, <i>GNOMEUseHints</i> / <i>GNOMEIgnoreHints</i>, <i>StickyIcon</i> / <i>SlipperyIcon</i>, <i>StickyAcrossPagesIcon</i> / <i>!StickyAcrossPagesIcon</i>, <i>StickyAcrossDesksIcon</i> / <i>!StickyAcrossDesksIcon</i>, <i>ManualPlacement</i> / <i>CascadePlacement</i> / <i>MinOverlapPlacement</i> / <i>MinOverlapPercentPlacement</i> / <i>TileManualPlacement</i> / <i>TileCascadePlacement</i> / <i>PositionPlacement</i>, <i>MinOverlapPlacementPenalties</i>, <i>MinOverlapPercentPlacementPenalties</i>, <i>DecorateTransient</i> / <i>NakedTransient</i>, <i>DontRaiseTransient</i> / <i>RaiseTransient</i>, <i>DontLowerTransient</i> / <i>LowerTransient</i>, <i>DontStackTransientParent</i> / <i>StackTransientParent</i>, <i>SkipMapping</i> / <i>ShowMapping</i>, <i>ScatterWindowGroups</i> / <i>KeepWindowGroupsOnDesk</i>, <i>UseDecor</i>, <i>UseStyle</i>, <i>!UsePPosition</i> / <i>NoPPosition</i> / <i>UsePPosition</i>, <i>!UseUSPosition</i>, <i>NoUSPosition</i> / <i>UseUSPosition</i>, <i>!UseTransientPPosition</i>, <i>NoTransientPPosition</i> / <i>UseTransientPPosition</i>, <i>!UseTransientUSPosition</i> / <i>NoTransientUSPosition</i> / <i>UseTransientUSPosition</i>, <i>!UseIconPosition</i> / <i>NoIconPosition</i> / <i>UseIconPosition</i>, <i>Lenience</i> / <i>!Lenience</i>, <i>ClickToFocus</i> / <i>SloppyFocus</i> / <i>MouseFocus</i>|<i>FocusFollowsMouse</i> / <i>NeverFocus</i>, <i>ClickToFocusPassesClickOff</i> / <i>ClickToFocusPassesClick</i>, <i>ClickToFocusRaisesOff</i> / <i>ClickToFocusRaises</i>, <i>MouseFocusClickRaises</i> / <i>MouseFocusClickRaisesOff</i>, <i>GrabFocus</i> / <i>GrabFocusOff</i>, <i>GrabFocusTransientOff</i> / <i>GrabFocusTransient</i>, <i>FPFocusClickButtons</i>, <i>FPFocusClickModifiers</i>, <i>!FPSortWindowlistByFocus</i> / <i>FPSortWindowlistByFocus</i>, <i>FPClickRaisesFocused</i> / <i>!FPClickRaisesFocused</i>, <i>FPClickDecorRaisesFocused</i> / <i>!FPClickDecorRaisesFocused</i>, <i>FPClickIconRaisesFocused</i> / <i>!FPClickIconRaisesFocused</i>, <i>!FPClickRaisesUnfocused</i> / <i>FPClickRaisesUnfocused</i>, <i>FPClickDecorRaisesUnfocused</i> / <i>!FPClickDecorRaisesUnfocused</i>, <i>FPClickIconRaisesUnfocused</i> / <i>!FPClickIconRaisesUnfocused</i>, <i>FPClickToFocus</i> / <i>!FPClickToFocus</i>, <i>FPClickDecorToFocus</i> / <i>!FPClickDecorToFocus</i>, <i>FPClickIconToFocus</i> / <i>!FPClickIconToFocus</i>, <i>!FPEnterToFocus</i> / <i>FPEnterToFocus</i>, <i>!FPLeaveToUnfocus</i> / <i>FPLeaveToUnfocus</i>, <i>!FPFocusByProgram</i> / <i>FPFocusByProgram</i>, <i>!FPFocusByFunction</i> / <i>FPFocusByFunction</i>, <i>FPFocusByFunctionWarpPointer</i> / <i>!FPFocusByFunctionWarpPointer</i>, <i>FPLenient</i> / <i>!FPLenient</i>, <i>!FPPassFocusClick</i> / <i>FPPassFocusClick</i>, <i>!FPPassRaiseClick</i> / <i>FPPassRaiseClick</i>, <i>FPIgnoreFocusClickMotion</i> / <i>!FPIgnoreFocusClickMotion</i>, <i>FPIgnoreRaiseClickMotion</i> / <i>!FPIgnoreRaiseClickMotion</i>, <i>!FPAllowFocusClickFunction</i> / <i>FPAllowFocusClickFunction</i>, <i>!FPAllowRaiseClickFunction</i> / <i>FPAllowRaiseClickFunction</i>, <i>FPGrabFocus</i> / <i>!FPGrabFocus</i>, <i>!FPGrabFocusTransient</i> / <i>FPGrabFocusTransient</i>, <i>FPOverrideGrabFocus</i> / <i>!FPOverrideGrabFocus</i>, <i>FPReleaseFocus</i> / <i>!FPReleaseFocus</i>, <i>!FPReleaseFocusTransient</i> / <i>FPReleaseFocusTransient</i>, <i>FPOverrideReleaseFocus</i> / <i>!FPOverrideReleaseFocus</i>, <i>StartsLowered</i> / <i>StartsRaised</i>, <i>IgnoreRestack</i> / <i>AllowRestack</i>, <i>FixedPosition</i> / <i>VariablePosition</i>, <i>FixedUSPosition</i> / <i>VariableUSPosition</i>, <i>FixedPPosition</i> / <i>VariablePPosition</i>, <i>FixedSize</i> / <i>VariableSize</i>, <i>FixedUSSize</i> / <i>VariableUSSize</i>, <i>FixedPSize</i> / <i>VariablePSize</i>, <i>!Closable</i> / <i>Closable</i>, <i>!Iconifiable</i> / <i>Iconifiable</i>, <i>!Maximizable</i> / <i>Maximizable</i>, <i>!AllowMaximizeFixedSize</i> / <i>AllowMaximizeFixedSize</i>, <i>IconOverride</i> / <i>NoIconOverride</i> / <i>NoActiveIconOverride</i>, <i>DepressableBorder</i> / <i>FirmBorder</i>, <i>MinWindowSize</i>, <i>MaxWindowSize</i>, <i>IconifyWindowGroups</i> / <i>IconifyWindowGroupsOff</i>, <i>ResizeOpaque</i> / <i>ResizeOutline</i>, <i>BackingStore</i> / <i>BackingStoreOff</i> / <i>BackingStoreWindowDefault</i>, <i>Opacity</i> / <i>ParentalRelativity</i>, <i>SaveUnder</i> / <i>SaveUnderOff</i>, <i>WindowShadeShrinks</i> / <i>WindowShadeScrolls</i>, <i>WindowShadeSteps</i>, <i>WindowShadeAlwaysLazy</i> / <i>WindowShadeBusy</i> / <i>WindowShadeLazy,</i> <i>EWMHDonateIcon</i> / <i>EWMHDontDonateIcon</i>, <i>EWMHDonateMiniIcon</i> / <i>EWMHDontDonateMiniIcon</i>, <i>EWMHMiniIconOverride</i> / <i>EWMHNoMiniIconOverride</i>, <i>EWMHUseStackingOrderHints</i> / <i>EWMHIgnoreStackingOrderHints</i>, <i>EWMHIgnoreStateHints</i> / <i>EWMHUseStateHints</i>, <i>EWMHIgnoreStrutHints</i> / <i>EWMHUseStrutHints</i>, <i>EWMHIgnoreWindowType</i> / <i>!EWMHIgnoreWindowType</i>, <i>EWMHMaximizeIgnoreWorkingArea</i> / <i>EWMHMaximizeUseWorkingArea</i> / <i>EWMHMaximizeUseDynamicWorkingArea</i>, <i>EWMHPlacementIgnoreWorkingArea</i> / <i>EWMHPlacementUseWorkingArea</i> / <i>EWMHPlacementUseDynamicWorkingArea</i>, <i>MoveByProgramMethod</i>, <i>Unmanaged</i>, <i>State</i>, <i>SnapGrid</i>, <i>SnapAttraction</i>, <i>EdgeMoveDelay</i>, <i>EdgeResizeDelay</i>. <i>EdgeMoveResistance</i>, <i>InitialMapCommand</i> </p>
<p> In the above list some options are listed as style-option/opposite-style-option. The opposite-style-option for entries that have them describes the fvwm default behavior and can be used if you want to change the fvwm default behavior.</p>
<dl>
<dt><code>Focus policy</code></p>
<dd>
<dl>
<dt>
<dd> <i>ClickToFocus</i> instructs fvwm to give the focus to a window when it is clicked in. The default <i>MouseFocus</i> (or its alias <i>FocusFollowsMouse</i>) tells fvwm to give a window the focus as soon as the pointer enters the window, and take it away when the pointer leaves the window. <i>SloppyFocus</i> is similar, but doesn&#8217;t give up the focus if the pointer leaves the window to pass over the root window or a ClickToFocus window (unless you click on it, that is), which makes it possible to move the mouse out of the way without losing focus. A window with the style <i>NeverFocus</i> never receives the focus. This is useful for modules like <code>FvwmButtons</code>. for example. Note: Once any of the &quot;FP&#8230;&quot; styles has been used, the defaults that come with the basic focus policies are not restored when the latter are used again. For example, once !FPGrabFocus has been used, using ClickToFocus does not restore FPGrabFocus. </p>
<p> The focus model can be augmented with several additional options. In fvwm-2.5.3 and later, there are a large number of advanced options beginning with &quot;FP&quot; or &quot;!FP&quot;. These options shall replace the older options one day and are described first. Using any of these new options may limit compatibility with older releases. In general, options beginning with &quot;FP&quot; turn a feature on, while those beginning with &quot;!FP&quot; turn it off.</dl>
<dt><code>Focusing the window</code></p>
<dd>
<dl>
<dt>
<dd> With <i>FPEnterToFocus</i>, when the pointer enters a window it receives focus. </p>
<p> With <i>FPLeaveToUnfocus</i> a window loses focus when the pointer leaves it. </p>
<p> With <i>FPClickToFocus</i>, <i>FPClickDecorToFocus</i> or <i>FPClickIconToFocus</i>, a window receives focus when the inside of the window or the decorations or its icon is clicked. </p>
<p> The <i>FPFocusByProgram</i> style allows windows to take the focus themselves. </p>
<p> The !<i>FPFocusByFunction</i> style forbids that a window receives the focus via the <code>Focus</code> and <code>FlipFocus</code> commands. </p>
<p> The <i>FPFocusByFunctionWarpPointer</i> style controls if the pointer is warped to a selected window when the <code>Focus</code> command is used. </p>
<p> <i>FPLenient</i> allows focus on windows that do not want it, like <code>FvwmPager</code> or xclock. </p>
<p> The <i>FPFocusClickButtons</i> style takes a list of mouse buttons that can be clicked to focus or raise a window when the appropriate style is used. The default is to use the first three buttons (&quot;123&quot;). </p>
<p> The <i>FPFocusClickModifiers</i> style takes a list of modifier keys just like the <code>Key</code> command. The exact combination of modifier keys must be pressed for the click to focus or raise a window to work. The default is to use no modifiers (&quot;N&quot;). </p>
<p> With the <i>FPPassFocusClick</i> style, the click that was used to focus a window is passed to the application. </p>
<p> With the <i>FPAllowFocusClickFunction</i> style, the click that was used to focus a window can also trigger a normal action that was bound to the window with the <code>Mouse</code> command). </p>
<p> If the <i>FPIgnoreFocusClickMotion</i> style is used, clicking in a window and then dragging the pointer with the button held down does not count as the click to focus the window. Instead, the application processes these events normally. This is useful to select text in a terminal window with the mouse without raising the window. However, mouse bindings on the client window are not guaranteed to work anymore (see <code>Mouse</code> command). This style forces the initial click to be passed to the application. The distance that the pointer must be moved to trigger this is controlled by the <code>MoveThreshold</code> command. </p>
<p> The <i>FPSortWindowlistByFocus</i> and !<i>FPSortWindowlistByFocus</i> styles control whether the internal window list is sorted in the order the windows were focused or in the order they were created. The latter is the default for <i>ClickToFocus</i> and <i>SloppyFocus</i>. </p>
<p> <code>Clicking the window to raise</code> </p>
<p> The styles <i>FPClickRaisesFocused</i>, <i>FPClickDecorRaisesFocused</i> and <i>FPClickIconRaisesFocused</i> allow to raise the window when the interior or the decorations or the icon of the window is clicked while the window is already focused. </p>
<p> The styles <i>FPClickRaisesUnfocused</i>, <i>FPClickDecorRaisesUnfocused</i> and <i>FPClickIconRaisesUnfocused</i> allow to raise the window when the interior or the decorations or the icon of the window is clicked while the window is not yet focused. </p>
<p> With the <i>FPPassRaiseClick</i> style, the click that was used to raise the window is passed to the application. </p>
<p> With the <i>FPAllowRaiseClickFunction</i> style, the click that was used to raise the window can also trigger a normal action that was bound to the window with the <code>Mouse</code> command. </p>
<p> If the <i>FPIgnoreRaiseClickMotion</i> style is used, clicking in a window and then dragging the pointer with the button held down does not count as the click to raise the window. Instead, the application processes these events normally. This is useful to select text in a terminal window with the mouse without raising the window. However, mouse bindings on the client window are not guaranteed to work anymore (see <code>Mouse</code> command. Note that this style forces that the initial click is passed to the application. The distance that the pointer must be moved to trigger this is controlled by the <code>MoveThreshold</code> command. </p>
<p> <code>Grabbing the focus when a new window is created</code> </p>
<p> New normal or transient windows with the <i>FPGrabFocus</i> or <i>FPGrabFocusTransient</i> style automatically receive the focus when they are created. <i>FPGrabFocus</i> is the default for windows with the <i>ClickToFocus</i> style. Note that even if these styles are disabled, the application may take the focus itself. Fvwm can not prevent this. </p>
<p> The <i>OverrideGrabFocus</i> style instructs fvwm to never take away the focus from such a window via the <i>GrabFocus</i> or <i>GrabFocusTransient</i> styles. This can be useful if you like to have transient windows receive the focus immediately, for example in a web browser, but not while you are working in a terminal window or a text processor. </p>
<p> The above three styles are accompanied by <i>FPReleaseFocus</i>, <i>FPReleaseFocusTransient</i> and <i>FPOverrideReleaseFocus</i>. These control if the focus is returned to another window when the window is closed. Otherwise no window or the window under the pointer receives the focus. </p>
<p> <i>ClickToFocusPassesClickOff</i> and <i>ClickToFocusPassesClick</i> controls whether a mouse click to focus a window is sent to the application or not. Similarly, <i>ClickToFocusRaisesOff</i>/<i>MouseFocusClickRaisesOff</i> and <i>ClickToFocusRaises</i>/<i>MouseFocusClickRaises</i> control if the window is raised (but depending on the focus model). </p>
<p> Note: in fvwm versions prior to 2.5.3, the &quot;Click&#8230;&quot; options applied only to windows with <i>ClickToFocus</i> while the &quot;Mouse&#8230;&quot; options applied to windows with a different focus policy. This is no longer the case. </p>
<p> The old <i>GrabFocus</i> style is equivalent to using <i>FPGrabFocus</i> + <i>FPReleaseFocus</i>. </p>
<p> The old <i>GrabFocusTransient</i> style is equivalent to using <i>FPGrabFocusTransient</i> + <i>FPReleaseFocusTransient</i>. </p>
<p> <i>Lenience</i> is equivalent to the new style <i>FPLenient</i>.</dl>
<dt><code>Window title</code></p>
<dd>
<dl>
<dt>
<dd> The <i>Title</i> and !Title options determine if the window has a title-bar or not. By default all windows have a title-bar. <i>NoTitle</i> is equivalent to <i>!Title</i> but is deprecated. </p>
<p> Windows with the <i>TitleAtBottom</i>, <i>TitleAtLeft</i> or <i>TitleAtRight</i> style have a title-bar below, to the left or to the right of the window instead of above as usual. The <i>TitleAtTop</i> style restores the default placement. Even if the window has the <i>!Title</i> style set, this affects the <code>WindowShade</code> command. Please check the <code>WindowShade</code> command for interactions between that command and these styles. Titles on the left or right side of the windows are augmented by the following styles: </p>
<p> Normally, the text in titles on the left side of a window is rotated counterclockwise by 90 degrees from the normal upright position and 90 degrees clockwise for titles on the right side. It can also be rotated in the opposite directions with <i>LeftTitleRotatedCW</i> if <i>TitleAtLeft</i> is used, and with <i>RightTitleRotatedCCW</i> if <i>TitleAtRight</i> is used. The defaults can be restored with <i>LeftTitleRotatedCCW</i> and <i>RightTitleRotatedCW</i>. A normal horizontal text may be rotated as well with <i>TopTitleRotated</i> if <i>TitleAtTop</i> is used, and with <i>BottomTitleRotated</i> if <i>TitleAtBottom</i> is used. The defaults can be restored with <i>TopTitleNotRotated</i> and <i>BottomTitleNotRotated</i>. </p>
<p> By default the title bar decoration defined using the <code>TitleStyle</code> command is rotated following the title text rotation (see the previous paragraph). This can be disabled by using the !<i>UseTitleDecorRotation</i> style. <i>UseTitleDecorRotation</i> reverts back to the default. </p>
<p> With the <i>StippledTitle</i> style, titles are drawn with the same effect that is usually reserved for windows with the <i>Sticky</i>, <i>StickyAcrossPages</i> or <i>StickyAcrossDesks</i> style. <i>!StippledTitle</i> reverts back to normal titles. <i>StippledTitleOff</i> is equivalent to <i>!StippledTitle</i> but is deprecated. </p>
<p> <i>Color</i> takes two arguments. The first is the window-label text color and the second is the window decorations normal background color. The two colors are separated with a slash. If the use of a slash causes problems then the separate <i>ForeColor</i> and <i>BackColor</i> options can be used. </p>
<p> <code>Colorset</code> takes the colorset number as its sole argument and overrides the colors set by <i>Color</i>. Instead, the corresponding colors from the given colorset are used. Note that all other features of a colorset are not used. Use the <code>Colorset</code> decoration style in the <code>TitleStyle</code> and <i>ButtonStyle</i> command for that. To stop using the colorset, the colorset number is omitted. </p>
<p> The <i>HilightFore</i>, <i>HilightBack</i> and <i>HilightColorset</i> style options work exactly like <i>ForeColor</i>, <i>BackColor</i> and <i>Colorset</i> but are used only if the window has the focus. These styles replace the old commands <code>HilightColor</code> and <i>HilightColorset</i>. </p>
<p> <i>BorderColorset</i> takes the colorset number as its sole argument and overrides the colors set by <i>Color</i> or <i>Colorset</i>. for the window border. To stop using a colorset, the argument is omitted. </p>
<p> The <i>HilightBorderColorset</i> style option works similarly to <i>BorderColorset</i> but is used when the window has the focus. </p>
<p> !<i>IconTitle</i> disables displaying icon labels while the opposite style <i>IconTitle</i> enables icon labels (default behaviour). <i>NoIconTitle</i> is equivalent to <i>!IconTitle</i> but is deprecated. </p>
<p> <i>IconTitleColorset</i> takes the colorset number as its sole argument and overrides the colors set by <i>Color</i> or <i>Colorset</i>. To stop using this colorset, the argument is omitted. </p>
<p> <i>HilightIconTitleColorset</i> takes the colorset number as its sole argument and overrides the colors set by <code>HilightColor</code> or <i>HilightColorset</i>. To stop using this colorset, the argument is omitted. </p>
<p> <i>IconBackgroundColorset</i> takes the colorset number as its sole argument and uses it to set a background for the icon picture. By default the icon picture is not drawn onto a background image. To restore the default, the argument is omitted. </p>
<p> <i>IconTitleRelief</i> takes one numeric argument that may be between -50 and +50 pixels and defines the thickness of the 3D relief drawn around the icon title. With negative values the icon title gets a pressed in look. The default is 2 and it is restored if the argument is omitted. </p>
<p> <i>IconBackgroundRelief</i> takes one numeric argument that may be between -50 and +50 pixels and defines the thickness of the 3D relief drawn around the icon picture background (if any). With negative values the icon background gets a pressed in look. The default is 2 and it is restored if the argument is omitted. </p>
<p> <i>IconBackgroundPadding</i> takes one numeric argument that may be between 0 and 50 pixels and defines the amount of free space between the relief of the icon background picture (if any) and the icon picture. The default is 2 and it is restored if the argument is omitted. </p>
<p> The <i>Font</i> and <i>IconFont</i> options take the name of a font as their sole argument. This font is used in the window or icon title. By default the font given in the <code>DefaultFont</code> command is used. To revert back to the default, use the style without the name argument. These styles replace the older <code>WindowFont</code> and <i>IconFont</i> commands. </p>
<p> The deprecated <i>IndexedWindowName</i> style causes fvwm to use window titles in the form </p>
<dl>
<dt>
<dd>
<pre>
name (i)
</pre>
</dl>
<p> where <i>name</i> is the exact window name and <i>i</i> is an integer which represents the <i>i th</i> window with <i>name</i> as window name. This has been replaced with: </p>
<dl>
<dt>
<dd>
<pre>
TitleFormat %n (%t)
</pre>
</dl>
<p> <i>ExactWindowName</i> restores the default which is to use the exact window name. Deprecated in favour of: </p>
<dl>
<dt>
<dd>
<pre>
    TitleFormat %n
</pre>
</dl>
<p> <i>IndexedIconName</i> and <i>ExactIconName</i> work the same as <i>IndexedWindowName</i> and <i>ExactWindowName</i> styles but for the icon titles. Both are deprecated in favour of: </p>
<dl>
<dt>
<dd>
<pre>
IconTitleFormat %n (%t)
IconTitleFormat %n
</pre>
</dl>
<p> <i>TitleFormat</i> describes what the visible name of a window should look like, with the following placeholders being valid: </p>
<p> <code>%n</code></p>
<dl>
<dt>
<dd> Insert the window&#8217;s name.</dl>
<p> <code>%i</code></p>
<dl>
<dt>
<dd> Insert the window&#8217;s icon name.</dl>
<p> <code>%c</code></p>
<dl>
<dt>
<dd> Insert the window&#8217;s class name.</dl>
<p> <code>%r</code></p>
<dl>
<dt>
<dd> Insert the window&#8217;s resource name.</dl>
<p> <code>%t</code></p>
<dl>
<dt>
<dd> Insert the window count.</dl>
<p> <code>%I</code></p>
<dl>
<dt>
<dd> Insert the window ID.</dl>
<p> <code>%%</code></p>
<dl>
<dt>
<dd> Insert a literal &#8216;%&#8217; character.</dl>
<p> Any amount of whitespace may be used, along with other characters to make up the string &#8212; but a valid <i>TitleFormat</i> string must contain at least one of the placeholders mentioned. No quote stripping is performed on the string, so for example the following is printed verbatim: </p>
<dl>
<dt>
<dd>
TitleFormat &#8221; %n &#8220;-&gt;[% t] -&gt; [% c]
</dl>
<p> Note: It&#8217;s perfectly possible to use a <i>TitleFormat</i> which can result in wiping out the visible title altogether. For example: </p>
<dl>
<dt>
<dd>
<pre>
    TitleFormat %z
</pre>
</dl>
<p> Simply because the placeholder &#8216;%z&#8217; isn&#8217;t supported. This is not a bug but rather a facet of how the formatting parser works. </p>
<p> <i>IconTitleFormat</i> describes what the visible icon name of a window should look like, with the options being the same as <i>TitleFormat</i>.</dl>
<dt><code>Title buttons</code></p>
<dd>
<dl>
<dt>
<dd> <i>Button</i> and !<i>Button</i> take a numeric argument which is the number of the title-bar button which is to be shown or omitted. <i>NoButton</i> is equivalent to <i>!Button</i> but is deprecated. </p>
<p> <i>MwmButtons</i> makes the <code>Maximize</code> button look pressed-in when the window is maximized. See the <i>MwmDecorMax</i> flag in <code>ButtonStyle</code> for more information. To switch this style off again, use the <code>FvwmButtons</code> style.</dl>
<dt><code>Borders</code></p>
<dd>
<dl>
<dt>
<dd> !<i>Borders</i> suppresses the window border (but not the title) completely. The <i>Borders</i> style enables them again. Without borders, all other styles affecting window borders are meaningless. </p>
<p> <i>MwmBorder</i> makes the 3D bevel more closely match Mwm&#8217;s. <i>FvwmBorder</i> turns off the previous option. </p>
<p> With the !<i>Handles</i> style, the window does not get the handles in the window corners that are commonly used to resize it. With <i>!Handles</i>, the width from the <i>BorderWidth</i> style is used. By default, or if <i>Handles</i> is specified, the width from the <i>HandleWidth</i> style is used. <i>NoHandles</i> is equivalent to <i>!Handles</i> but is deprecated. </p>
<p> <i>HandleWidth</i> takes a numeric argument which is the width of the border to place the window if it does have resize-handles. Using HandleWidth without an argument restores the default. </p>
<p> <i>BorderWidth</i> takes a numeric argument which is the width of the border to place the window if it does not have resize-handles. It is used only if the <i>!Handles</i> style is specified too. Using BorderWidth without an argument restores the default. </p>
<p> <i>DepressableBorder</i> makes the border parts of the window decoration look sunken in when a button is pressed over them. This can be disabled again with the <i>FirmBorder</i> style.</dl>
<dt><code>Icons, shading, maximizing, movement, resizing</code></p>
<dd>
<dl>
<dt>
<dd> <i>Icon</i> takes an (optional) unquoted string argument which is the icon bitmap or pixmap to use. Icons specified this way override pixmap icons, but not icon windows or the ewmh icon, provided by the client in the application (with the WM_HINTS property or with the ewmh _NET_WM_ICON property). The <i>IconOverride</i> style changes the behavior to override any client-provided icons; the <i>NoIconOverride</i> style changes the behavior to not override any client-provided icons; the default overriding behavior can be activated with the <i>NoActiveIconOverride</i> style. With this style, fvwm uses application provided icons if the icon is changed but uses the icon provided in the configuration file until then. </p>
<p> There is one exception to these rules, namely </p>
<dl>
<dt>
<dd>
<pre>
Style * Icon unknown.xpm
</pre>
</dl>
<p> doesn&#8217;t force the unknown.xpm icon on every window, it just sets the default icon like the DefaultIcon command. If you really want all windows to have the same icon, you can use </p>
<dl>
<dt>
<dd>
<pre>
Style ** Icon unknown.xpm
</pre>
</dl>
<p> If the <i>NoIcon</i> attribute is set then the specified window simply disappears when it is iconified. The window can be recovered through the window-list. If <i>Icon</i> is set without an argument then the <i>NoIcon</i> attribute is cleared but no icon is specified. An example which allows only the <code>FvwmPager</code> module icon to exist: </p>
<dl>
<dt>
<dd>
<pre>
Style * NoIcon
Style FvwmPager Icon
</pre>
</dl>
<p> <i>IconBox</i> takes no argument, four numeric arguments (plus optionally a screen specification), an X11 geometry string or the string &quot;none&quot;: </p>
<dl>
<dt>
<dd>
<pre>
IconBox<i> [</i>screen scr-spec<i>] </i>l t r b
</pre>
</dl>
<p> or </p>
<dl>
<dt>
<dd>
<pre>
IconBox geometry
</pre>
</dl>
<p> Where <i>l</i> is the left coordinate, <i>t</i> is the top, <i>r</i> is right and <i>b</i> is bottom. Negative coordinates indicate distance from the right or bottom of the screen. If the first argument is the word <i>screen</i>, the <i>scr-spec</i> argument specifies the Xinerama screen on which the IconBox is defined. It can be the usual screen Xinerama specification, &#8216;p&#8217;, &acute;c&#8217;, &#8216;g&#8217;, a screen number or the additional &#8216;w&#8217; for the screen where the window center is located. This is only useful with multiple Xinerama screens. The &quot;l t r b&quot; specification is more flexible than an X11 geometry. For example: </p>
<dl>
<dt>
<dd>
<pre>
IconBox -80 240 -1 -1
</pre>
</dl>
<p> defines a box that is 80 pixels wide from the right edge, 240 pixels down from the top, and continues to the bottom of the screen. </p>
<p> Perhaps it is easier to use is an X11 geometry string though: </p>
<dl>
<dt>
<dd>
<pre>
IconBox 1000x70-1-1
</pre>
</dl>
<p> places an 1000 by 70 pixel icon box on the bottom of the screen starting in the lower right hand corner of the screen. One way to figure out a geometry like this is to use a window that resizes in pixel increments, for example, xv. Then resize and place the xv window where you want the iconbox. Then use FvwmIdent to read the windows geometry. The icon box is a region of the screen where fvwm attempts to put icons for any matching window, as long as they do not overlap other icons. Multiple icon boxes can be defined as overflow areas. When the first icon box is full, the second one is filled. All the icon boxes for one style must be defined in one <code>Style</code> command. For example: </p>
<dl>
<dt>
<dd>
<pre>
Style * IconBox -80 240 -1 -1, \
        IconBox 1000x70-1-1
</pre>
</dl>
<p> A Style command with the IconBox option replaces any icon box defined previously by another Style command for the same style. Thats why the backslash in the previous example is required. </p>
<p> Note: The geometry for the icon box command takes the additional screen specifier &quot;@w&quot; in case a Xinerama setup is used. This designates the screen where the window center is located. The additional screen specifier is not allowed anywhere else. </p>
<p> If you never define an icon box, or you fill all the icon boxes, fvwm has a default icon box that covers the screen, it fills top to bottom, then left to right, and has an 80&#215;80 pixel grid. To disable all but the default icon box you can use IconBox without arguments in a separate <code>Style</code> command. To disable all icon boxes including the default icon box, the argument &quot;none&quot; can be specified. </p>
<p> Hint: You can auto arrange your icons in the icon box with a simple fvwm function. Put the &quot;DeiconifyAndRearrange&quot; function below in your configuration file: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> DeiconifyAndRearrange
 + C <code>Iconify</code> off
 + C <code>All</code> (CurrentPage, Iconic) <code>PlaceAgain</code> Icon
</pre>
</dl>
<p> And then replace all places where you call the <code>Iconify</code> command to de-iconify an icon with a call to the new function. For example replace </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> IconFunc
 + C <code>Iconify</code> off
 + M <code>Raise</code>
 + M <code>Move</code>
 + D <code>Iconify</code> off
<code>Mouse</code> 1 I A <code>Iconify</code> off
</pre>
</dl>
<p> with </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> IconFunc
 + C DeiconifyAndRearrange
 + M <code>Raise</code>
 + M <code>Move</code>
 + D DeiconifyAndRearrange
<code>Mouse</code> 1 I A DeiconifyAndRearrange
</pre>
</dl>
<p> <i>IconGrid</i> takes 2 numeric arguments greater than zero. </p>
<dl>
<dt>
<dd>
<pre>
<i>IconGrid x y</i>
</pre>
</dl>
<p> Icons are placed in an icon box by stepping through the icon box using the <i>x</i> and <i>y</i> values for the icon grid, looking for a free space. The default grid is 3 by 3 pixels which gives a tightly packed appearance. To get a more regular appearance use a grid larger than your largest icon. Use the <i>IconSize</i> argument to clip or stretch an icon to a maximum size. An <i>IconGrid</i> definition must follow the <code>IconBox</code> definition that it applies to: </p>
<dl>
<dt>
<dd>
<pre>
Style * IconBox -80x240-1-1, IconGrid 90 90
</pre>
</dl>
<p> <i>IconFill</i> takes 2 arguments. </p>
<dl>
<dt>
<dd>
<pre>
IconFill <i>Bottom Right</i>
</pre>
</dl>
<p> Icons are placed in an icon box by stepping through the icon box using these arguments to control the direction the box is filled in. By default the direction is left to right, then top to bottom. This would be expressed as: </p>
<dl>
<dt>
<dd>
<pre>
IconFill left top
</pre>
</dl>
<p> To fill an icon box in columns instead of rows, specify the vertical direction (top or bottom) first. The directions can be abbreviated or spelled out as follows: &quot;t&quot;, &quot;top&quot;, &quot;b&quot;, &quot;bot&quot;, &quot;bottom&quot;, &quot;l&quot;, &quot;lft&quot;, &quot;left&quot;, &quot;r&quot;, &quot;rgt&quot;, &quot;right&quot;. An <code>IconFill</code> definition must follow the <code>IconBox</code> definition that it applies to: </p>
<dl>
<dt>
<dd>
<pre>
Style * IconBox -80x240-1-1, IconFill b r
</pre>
</dl>
<p> <i>IconSize</i> sets limits on the size of an icon image. Both user-provided and application-provided icon images are affected. </p>
<dl>
<dt>
<dd>
IconSize[width height[maxwidth maxheight]]
</dl>
<p> All arguments are measured in pixels. When all four arguments are passed to <i>IconSize,</i> <i>width</i> and <i>height</i> represent the minimum size of an icon, and <i>maxwidth</i> and <i>maxheight</i> represent the maximum size of an icon. Icon images that are smaller than the minimum size are padded. Icon images that are bigger than the maximum size are clipped. </p>
<p> If only two arguments are passed to <i>IconSize,</i> <i>width</i> and <i>height</i> represent the absolute size of an icon. Icons covered by this style are padded or clipped to achieve the given size. </p>
<p> If no arguments are specified, the default values are used for each dimension. This effectively places no limits on the size of an icon. </p>
<p> The value of &quot;-1&quot; can be used in place of any of the arguments to specify the default value for that dimension. </p>
<p> In addition to the numeric arguments, 1 additional argument can be &quot;Stretched&quot;, &quot;Adjusted&quot;, or &quot;Shrunk&quot;. </p>
<p> Note that module provided icon managers are not affected by this style.</dl>
</dl>
<p> <i>MiniIcon</i> specifies a pixmap to use as the miniature icon for the window. This miniature icon can be drawn in a title-bar button (see <code>ButtonStyle</code>), and can be used by various fvwm modules (<code>FvwmWinList</code>, <code>FvwmIconMan</code> and <code>FvwmTaskBar</code>). It takes the name of a pixmap as an argument. </p>
<p> <i>WindowShadeShrinks</i> and <i>WindowShadeScrolls</i> control if the contents of a window that is being shaded with the <code>WindowShade</code> command are scrolled (default) or if they stay in place. The shrinking mode is a bit faster </p>
<p> The <i>WindowShadeSteps</i> option selects the number of steps for animation when shading a window with <code>WindowShade</code>. It takes one number as its argument. If the number has a trailing &#8216;<i>p</i>&#8216; it sets the number of pixels to use as the step size instead of a fixed number of steps. 0 disables the animation. This happens too if the argument is omitted or invalid. </p>
<p> The <code>WindowShade</code> command has two modes of operation: busy and lazy shading. Busy shading can be 50% slower than lazy shading, but the latter can look strange under some conditions, for example, if the window borders, buttons or the title are filled with a tiled pixmap. Also, the window handles are not drawn in lazy mode and the border relief may only be drawn partially right before the window reaches the shaded state or tight after leaves the unshaded state. By default, fvwm uses lazy mode if there are no bad visual effects (not counting the window handles) and busy mode otherwise. Use the <i>WindowShadeAlwaysLazy or WindowShadeBusy</i> to force using the lazy or busy mode. The default setting is restored with <i>WindowShadeLazy</i>. </p>
<p> <i>ResizeOpaque</i> instructs fvwm to resize the corresponding windows with their contents visible instead of using an outline. Since this causes the application to redraw frequently it can be quite slow and make the window flicker excessively, depending on the amount of graphics the application redraws. The <i>ResizeOutline</i> style (default) negates the <i>ResizeOpaque</i> style. Many applications do not like their windows being resized opaque, e.g. XEmacs, Netscape or terminals with a pixmap background. If you do not like the result, do not use the <i>ResizeOpaque</i> style for these windows. To exempt certain windows from opaque resizing you could use these lines in your configuration file: </p>
<dl>
<dt>
<dd>
<pre>
Style * ResizeOpaque
Style rxvt ResizeOutline
Style emacs ResizeOutline
</pre>
</dl>
<p> <i>Sticky</i> makes the window sticky, i.e. it is always visible on each page and each desk. The opposite style, <i>Slippery</i> reverts back to the default. </p>
<p> <i>StickyIcon</i> makes the window sticky when it&#8217;s iconified. It de-iconifies on top the active desktop. <i>SlipperyIcon</i> reverts back to the default. </p>
<p> <i>StickyAcrossPages</i> and <i>StickyAcrossPagesIcon</i> work like <i>Sticky</i> and <i>StickyIcon</i>, but stick the window only across pages, not desks while <i>StickyAcrossDesks and StickyAcrossDesksIcon</i> works the other way round. </p>
<p> Windows that have been marked as <i>Sticky</i> or <i>StickyAcrossDesks</i> or <i>StickyAcrossPages</i> will have stipples drawn on the titlebar. This can be negated with the !<i>StickyStippledTitle</i> style. The style <i>StickyStippledTitle</i> puts back the stipples where that window has also been marked as <i>Sticky</i>. Note that this is the default style for <i>Sticky</i> windows. Sticky icons will have stipples drawn on the icon title. This can be disabled in the same way with the !<i>StickyStippledIconTitle</i> style. </p>
<p> Windows with the <i>StartIconic</i> style are shown as icons initially. Note that some applications counteract that by deiconifying themselves. The default is to not iconify windows and can be set with the <i>StartNormal</i> style. </p>
<p> <i>StickyIcon</i> makes the window sticky when it&#8217;s iconified. It de-iconifies on top the active desktop. <i>SlipperyIcon</i> reverts back to the default. </p>
<p> <i>StickyIconPage</i> works like <i>StickyIcon</i>, but sticks the icon only across pages, not desks while <i>StickyIconDesk</i> works the other way round. </p>
<p> <i>StippledIconTitle</i> works like <i>StippledTitle</i> in that it draws stipples on the titles of icons but doesn&#8217;t make the icon sticky. </p>
<p> <i>IgnoreRestack</i> makes fvwm ignore attempts of clients to raise or lower their own windows. By default, the opposite style, <i>AllowRestack</i> is active. </p>
<p> <i>FixedPosition</i> and <i>FixedUSPosition</i> make fvwm ignore attempts of the user to move the window. It is still possible to move the window by resizing it. To allow the user to move windows, use the <i>VariablePosition</i> or <i>VariableUSPosition</i> style. </p>
<p> <i>FixedSize</i> and <i>FixedUSSize</i> make fvwm ignore attempts of the user to resize the window. To allow the user to resize windows, use the <i>VariableSize</i> or <i>VariableUSSize</i> style. </p>
<p> <i>FixedPPosition</i> and <i>FixedPSize</i> make fvwm ignore attempts of the program to move or resize its windows. To allow this kind of actions, use the <i>VariablePPosition</i> or <i>VariablePSize</i> style. These styles may sometimes affect the initial placement and dimensions of new windows (depending on the application). If windows are created at strange places, try either the <i>VariablePPosition</i> or <i>!UsePPosition</i> styles. The <i>FixedPSize</i> style may screw up window dimensions for some applications. Do Not use this style in this case. </p>
<p> <i>MoveByProgramMethod</i> affects how fvwm reacts to requests by the application to move its windows. By default, fvwm tries to detect which method to use, but it sometimes detects the wrong method. You may come across a window that travels across the screen by a few pixels when the application resizes it, moves to a screen border with the frame decorations off screen, that remembers its position for the next time it starts but appears in a slighly shifted position, or that attepmts to become full screen but has the. Try out both options, <i>UseGravity</i> and <i>IgnoreGravity</i> on the window (and that window only) and see if that helps. By default, fvwm uses the <i>AutoDetect</i> method. Once the method was detected, it is never changed again. As long as fvwm can not detect the proper method, it uses <i>IgnoreGravity</i>. To force fvwm to retry the detection, use one of the other two options first and then use <i>AutoDetect</i> again. </p>
<p> Note: This option was introduced to alleviate a problem with the ICCCM specification. The ICCCM clearly states that the <i>UseGravity</i> option should be used, but traditionally applications ignored this rule. </p>
<p> <i>Closable</i> enables the functions <code>Close</code>, <code>Delete</code> and <code>Destroy</code> to be performed on the windows. This is on by default. The opposite, <i>!Closable</i>, inhibits the window to be closed. </p>
<p> <i>Iconifiable</i> enables the function <code>Iconify</code> to be performed on the windows. This is on by default. The opposite, <i>!Iconifiable</i>, inhibits the window from being iconified. </p>
<p> <i>Maximizable</i> enables the function <code>Maximize</code> to be performed on the windows. This is on by default. The opposite, <i>!Maximizable</i>, inhibits the window from being maximized. </p>
<p> <i>AllowMaximizeFixedSize</i> enables the function <code>Maximize</code> to be performed on windows that are not resizable, unless maximization has been disabled either using the style <i>!Maximizable</i> or through WM hints. This is on by default. The opposite, <i>!AllowMaximizeFixedSize</i>, inhibits all windows that are not resizable from being maximized. </p>
<p> <i>ResizeHintOverride</i> instructs fvwm to ignore the program supplied minimum and maximum size as well as the resize step size (the character size in many applications). This can be handy for broken applications that refuse to be resized. Do not use it if you do not need it. The default (opposite) style is <i>NoResizeOverride</i>. </p>
<p> <i>MinWindowSize [ width [ p ] height [ p ] ]</i> Tells fvwm the minimum width and height of a window. The values are the percentage of the total screen area. If the letter &#8216;<i>p</i>&#8216; is appended to either of the values, the numbers are interpreted as pixels. This command is useful for certain versions of xemacs which freak out if their windows become too small. If you omit he parameters or their values are invalid, both limits are set to 0 pixels (which is the default value). </p>
<p> <i>MaxWindowSize [ width [ p ] height [ p ] ]</i> Tells fvwm the maximum width and height of a window. The values are the percentage of the total screen area. If the letter &#8216;<i>p</i>&#8216; is appended to either of the values, the numbers are interpreted as pixels. This command is useful to force large application windows to be fully visible. Neither <i>height</i> nor <i>width</i> may be less than 100 pixels. If you omit the parameters or their values are invalid, both limits are set to 32767 pixels (which is the default). </p>
<p> With <i>IconifyWindowGroups</i> all windows in the same window group are iconified and deiconified at once when any window in the group is (de)iconified. The default is <i>IconifyWindowGroupsOff</i>, which disables this behavior. Although a number of applications use the window group hint, it is rarely used in a proper way, so it is probably best to use <i>IconifyWindowGroups</i> only for selected applications. </p>
<p> The option <i>SnapAttraction</i> affects interactive window movement: If during an interactive move the window or icon comes within <i>proximity</i> pixels of another the window or icon, it is moved to make the borders adjoin. The default of 0 means that no snapping happens. Calling this command without arguments turns off snap attraction and restores the default behavior. Please refer also to the <code>SnapGrid</code> command. </p>
<p> The second argument determined is optional and may be set to one of the five following values: With <i>All</i> both icons and windows snap to other windows and other icons. <i>SameType</i> lets windows snap only to windows, and icons snap only to icons. With <i>Windows</i> windows snap only to other windows. Similarly with <i>Icons</i> icons snap only to other icons. With <i>None</i> no snapping takes place. This option can be useful in conjunction with the following argument if you only want to snap against the screen edges. The default behavior is <i>All</i>. </p>
<p> The third and last optional argument may be set to one of the four following values: </p>
<dl>
<dt>
<dd> &bull;With <i>Screen</i> the already snapping icons or windows, which is controlled by the second argument, will snap now also to the screen edges.</dl>
<dl>
<dt>
<dd> &bull;<i>ScreenWindows</i> snaps only windows to the screen edges.</dl>
<dl>
<dt>
<dd> &bull;<i>ScreenIcons</i> snaps only icons to the screen edges.</dl>
<dl>
<dt>
<dd> &bull;<i>ScreenAll</i> snaps windows and icons to the screen edges.</dl>
<p> The option <i>SnapGrid</i> defines an invisible grid on the screen. During an interactive move a window or icon is positioned such that its location (top left corner) is coincident with the nearest grid point. The default <i>x-grid-size</i> and <i>y-grid-size</i> setting are both 1, which is effectively no grid all. </p>
<p> An interactive move with both <code>SnapGrid</code> and <i>SnapAttraction</i> results in the window being moved to be adjacent to the nearest window border (if within snap proximity) or grid position. The window moves the shortest distance possible to satisfy both <code>SnapGrid</code> and <i>SnapAttraction</i>. Note that the x and y coordinates are not coupled. For example, a window may snap to another window on the x axis while snapping to a grid point on the y axis. Using this style without arguments reinstates the default settings. </p>
<p> The styles <i>EdgeMoveDelay</i> and <i>EdgeResizeDelay</i> tells how hard it should be to change the desktop viewport by moving or resizing a window over the edge of the screen. The parameter tells how many milliseconds the pointer must spend on the screen edge before fvwm moves the viewport. The command <code>EdgeScroll</code> determines how far the viewport is scrolled. If -1 is given as the delay, page flipping is disabled completely. The defaults are no delay for moving (0) and no flipping for resizing (-1). Using these styles without any argument restores the default settings. Note that, with </p>
<dl>
<dt>
<dd>
<pre>
<code>EdgeScroll</code> 0 0
</pre>
</dl>
<p> it is still possible to move or resize windows across the edge of the current screen. See also <code>EdgeThickness</code>. </p>
<p> The option <i>EdgeMoveResistance</i> makes it easier to place a window directly adjacent to the screen&#8217;s or xinerama screen&#8217;s border. It takes one or two parameters. The first parameter tells how many pixels over the edge of the screen a window&#8217;s edge must move before it actually moves partially off the screen. The optional second parameter does the same as the first, but for individual Xinerama screens. If omitted, the value of the first parameter is assumed for this type of movement. Set the second parameter to 0 to zero to ignore individual xinerama screen edges. Note that the center of the window being moved determines the xinerama screen on which the window should be kept. Both values are 0 by default. To restore the defaults, the option <i>EdgeMoveResistance</i> can be used without any parameters. </p>
<p> The option <i>InitialMapCommand</i> allows for any valid fvwm command or function to run when the window is initially mapped by fvwm. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> MyWindow StartsOnPage 0 0, InitialMapCommand Iconify
</pre>
</dl>
<p> This would hence place the window called <i>MyWindow</i> on page 0 0 for the current desk, and immediately run the <code>Iconify</code> command on that window. </p>
<p> Note that should <i>InitialMapCommand</i> be used as a global option for all windows, but there is a need that some windows should not have this command applied, then an action of <code>Nop</code> can be used on those windows, as in the following example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> * InitialMapCommand Iconify
<code>Style</code> XTeddy InitialMapCommand Nop
</pre>
</dl>
</dl>
<dt><code>Window Manager placement</code></p>
<dd>
<dl>
<dt>
<dd> Applications can place windows at a particular spot on the screen either by window manager hints or a geometry specification. When they do neither, then the window manager steps in to find a place for the window. Fvwm knows several ways to deal with this situation. The default is <i>TileCascadePlacement</i>. </p>
<p> <i>PositionPlacement</i> [<i>Center</i>|<i>UnderMouse</i>|<i>move-arguments</i>] When used without an argument, new windows are placed in the top left corner of the display. With the argument <i>Center</i>, all new window appear at the center of the screen, and with <i>UnderMouse</i>, windows are centered under the mouse pointer where possible. If the window is unable to fit on the screen because the pointer is at the edge of the screen, then the window is forced on-screen using this option. If any other <i>move-arguments</i> are given, they are interpreted exactly as the <code>Move</code> command does (with the exception that references to the current window position do not work as the window has not been placed yet). </p>
<p> <i>CascadePlacement</i> automatically place new windows in a cascading fashion. </p>
<p> <i>TileCascadePlacement</i> automatically places new windows in a smart location &#8211; a location in which they do not overlap any other windows on the screen. If no such position can be found <i>CascadePlacement</i> is used as a fall-back method. </p>
<p> <i>TileManualPlacement</i> This is the same as <i>TileCascadePlacement</i>, but uses <i>ManualPlacement</i> as the fall-back method. </p>
<p> <i>MinOverlapPlacement</i> automatically places new windows in a location in which the overlapping area in pixels of other windows is minimized. By default this placement policy tries to avoid overlapping icons and windows on higher layers. This can be configured with the <i>MinOverlapPlacementPenalties</i> style. </p>
<p> <i>MinOverlapPercentPlacement</i> is similar to <i>MinOverlapPlacement</i> but tries to minimize the overlapped percentages of other windows instead of the overlapped area in pixels. This placement policy tries to avoid covering other windows completely and tries even harder not to cover small windows. This can be configured with the <i>MinOverlapPlacementPenalties</i> and <i>MinOverlapPercentPlacementPenalties</i> styles. </p>
<p> <i>MinOverlapPlacementPenalties</i> takes at most 6 positive or null decimal arguments: </p>
<dl>
<dt>
<dd>
<pre>
<i>normal ontop icon sticky below strut</i>
</pre>
</dl>
<p> if trailing arguments are missing the default is used which is: </p>
<dl>
<dt>
<dd>
<pre>
1 5 10 1 0.05 50
</pre>
</dl>
<p> To reset this style to the default values, prefix it with a &#8216;!&#8217;. This style configures the <i>MinOverlapPlacement</i> and <i>MinOverlapPercentPlacement</i> placement policy. The <i>normal</i> factor affects normal windows, the <i>ontop</i> factor affects windows with a greater layer than the window being placed, the <i>icon</i> factor affects icons, the <i>sticky</i> factor affects sticky windows, the <i>below</i> factor affects windows with a smaller layer than the window being placed, the <i>strut</i> factor affects the complement of the EWMH working area if the window being placed has the <i>EWMHPlacementUseWorkingArea</i> style and windows with an EWMH strut hint (i.e., a &quot;please do not cover me&quot; hint) if the window being placed has the <i>EWMHPlacementUseDynamicWorkingArea</i> style. These factors represent the amount of area that these types of windows (or area) are counted as, when a new window is placed. For example, by default the area of ontop windows is counted 5 times as much as normal windows. So <i>MinOverlapPlacement</i> and <i>MinOverlapPercentPlacement</i> covers 5 times as much area of another window before it will cover an ontop window. To treat ontop windows the same as other windows, set this to 1. To really, really avoid putting windows under ontop windows, set this to a high value, say 1000. This style affects the window already mapped and not the window which is currently placed. There is one exception to this rule: in the case of the window being placed has the <i>EWMHPlacementUseWorkingArea</i> style the <i>strut</i> factor affects the placed window. </p>
<p> <i>MinOverlapPercentPlacementPenalties</i> takes at most 4 positive or null integer arguments: </p>
<dl>
<dt>
<dd>
<pre>
<i>cover_100 cover_95 cover_85 cover_75</i>
</pre>
</dl>
<p> if trailing arguments are missing the defaults are used which are: </p>
<dl>
<dt>
<dd>
<pre>
12 6 4 1
</pre>
</dl>
<p> To reset this style to the default values, prefix it with a &#8216;!&#8217;. This style affects the <i>MinOverlapPercentPlacement</i> placement policy and is similar to the <i>MinOverlapPlacementPenalties</i> style. The <i>cover_xx</i> factor is used when the window being placed covers at least <i>xx</i> percent of the window. This factor is added to the factor determined by the <i>MinOverlapPlacementPenalties</i> style. </p>
<p> <i>ManualPlacement</i> (aka active placement). The user is required to place every new window manually. The window only shows as a rubber band until a place is selected manually. The window is placed when a mouse button or any key except <i>Escape</i> is pressed. Escape aborts manual placement which places the window in the top left corner of the screen. If mouse button 2 is pressed during the initial placement of a window (respectively <i>Shift</i> and mouse button 1 in case Mwm emulation has been enabled with the <code>Emulate</code> command), the user is asked to resize the window too. </p>
<p> It is possible to define buttons usable to place windows with the <code>Move</code> command and the special context &#8216;P&#8217; for placement (see <code>Move</code> command). However, you can&#8217;t redefine the way to also resize the window other than the way it is affected by the <code>Emulate</code> command. The button used for placing the window can be checked with the <i>PlacedByButton</i> condition (see <code>Current</code> command). </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
Style * ManualPlacement
*FvwmEvent: PassID
*FvwmEvent: add_window GrowDownFunc
<code>AddToFunc</code> StartFunction
+ I FvwmEvent
<code>AddToFunc</code> GrowDownFunc
+ I windowid $0 (PlacedByButton 3) \
  <code>Resize</code> bottomright keep -0p
</pre>
</dl>
<p> Now, whenever a window is created and the user presses button 3 to finish initial placement, the window is automatically enlarged until it hits the bottom screen border. </p>
<p> <i>Old placement styles</i> DumbPlacement / SmartPlacement / SmartPlacementOff, CleverPlacement / CleverPlacementOff, ActivePlacement / RandomPlacement, ActivePlacementsHonorsStartsOnPage / ActivePlacementsHonorsStartsOnPageOff, GlobalOpts SmartPlacementIsReallySmart / GlobalOpts SmartPlacementIsNormal are still supported but will be removed in the future. The old and new styles can be translated according to the following table: </p>
<dl>
<dt>
<dd>
GlobalOpts SmartPlacementIsReallySmart<br />
        Style *SmartPlacement&#8211; &gt;<br />
    Style *SmartPlacement,<br />
    CleverPlacement<br />
            GlobalOpts SmartPlacementIsNormal<br />
                Style *SmartPlacement&#8211; &gt;<br />
        Style *SmartPlacement,<br />
    CleverPlacementOff<br />
        Style *DumbPlacement,<br />
    RandomPlacement&#8211; &gt;<br />
        Style *CascadePlacement<br />
            Style *DumbPlacement,<br />
    ActivePlacement&#8211; &gt;<br />
        Style *ManualPlacement<br />
            Style *SmartPlacement,<br />
    RandomPlacement, CleverPlacementOff&#8211; &gt; Style *TileCascadePlacement Style *SmartPlacement,<br />
    ActivePlacement, CleverPlacementOff&#8211; &gt; Style *TileManualPlacement Style *SmartPlacement, CleverPlacement&#8211; &gt; Style *MinOverlapPlacement Style *SmartPlacement,<br />
    ActivePlacement, CleverPlacement&#8211; &gt; Style *MinOverlapPercentPlacement Style *ActivePlacementsHonorsStartsOnPage&#8211; &gt; Style *ManualPlacementsHonorsStartsOnPage Style *ActivePlacementsHonorsStartsOnPageOff&#8211; &gt; Style *ManualPlacementsHonorsStartsOnPageOff
</dl>
</dl>
<dt><code>Placement policy options and window stacking</code></p>
<dd>
<dl>
<dt>
<dd> <i>!UsePPosition</i> instructs fvwm to ignore the program specified position (PPosition hint) when adding new windows. Using PPosition is required for some applications, but if you do not have one of those it&#8217;s a real headache. Many programs set PPosition to something obnoxious like 0,0 (upper left corner). Note: <i>!UsePPosition</i> is equivalent to the deprecated option <i>!UsePPosition</i> </p>
<p> <i>!UseUSPosition</i> works like <i>!UsePPosition</i> but applies suppresses using the user specified position indicated by the program (USPosition hint). It is generally a bad thing to override the user&#8217;s choice, but some applications misuse the USPosition hint to force their windows to a certain spot on the screen without the user&#8217;s consent. Note: <i>!UseUSPosition</i> is equivalent to the deprecated option <i>!USPosition</i> </p>
<p> <i>NoUseTransientPPosition</i> and <i>UseTransientPPosition</i> work like <i>!UsePPosition</i> and <i>UsePPosition</i> but apply only to transient windows. Note: <i>!UseTransientPPosition</i> is equivalent to the deprecated option <i>!TransientPPosition</i> </p>
<p> <i>NoUseIconPosition</i> instructs fvwm to ignore the program specified icon position (IconPosition hint) when iconifying the window. Note: <i>!UseIconPosition</i> is equivalent to the deprecated option <i>!IconPosition</i> </p>
<p> <i>StartsOnDesk</i> takes a numeric argument which is the desktop number on which the window should be initially placed. Note that standard Xt programs can also specify this via a resource (e.g. &quot;-xrm &#8216;*Desk: 1&#8217;&quot;). </p>
<p> <i>StartsOnPage</i> takes 1, 2, or 3 numeric arguments. If one or three arguments are given, the first (or only) argument is the desktop number. If three arguments are given, the 2nd and 3rd arguments identify the x,y page position on the virtual window. If two arguments are given, they specify the page position, and indicate no desk preference. If only one argument is given, <i>StartsOnPage</i> functions exactly like <i>StartsOnDesk</i>. For those standard Xt programs which understand this usage, the starting desk/page can also be specified via a resource (e.g., &quot;-xrm &#8216;*page: 1 0 2&#8217;&quot;). <i>StartsOnPage</i> in conjunction with <i>SkipMapping</i> is a useful technique when you want to start an app on some other page and continue with what you were doing, rather than waiting for it to appear. </p>
<p> <i>StartsOnScreen</i> takes one argument. It can be &#8216;p&#8217; for the primary screen, &#8216;c&#8217; for the current screen (containing the mouse pointer), &#8216;g&#8217; for the global screen or the screen number itself (counting from zero). A new window is placed on the specified Xinerama screen. The default is to place windows on the screen that contains the mouse pointer at the time the window is created. However, those windows which are not placed by fvwm (i.e., those with a USPosition hint from a user specified geometry) are normally placed in a position relative to the global screen. The <i>StartsOnScreen</i> style is also useful to cause these windows to be placed relative to a specific Xinerama screen. For example: </p>
<dl>
<dt>
<dd>
<pre>
Style * StartsOnScreen c
</pre>
</dl>
<p> Would cause all windows, including those with their own geometry to be placed relative to the current Xinerama screen rather than the global screen. For those standard Xt programs which understand this usage, the starting desk/page can also be specified via a resource (e.g., &quot;-xrm &#8216;*fvwmscreen: c&#8217;&quot;). (&#8216;fvwmscreen&#8217; was chosen because some applications already use &acute;.screen&#8217; for other purposes.) </p>
<p> <i>StartsOnPageIncludesTransients</i> causes the <i>StartsOnPage</i> style to be applied even for transient windows. This is not usually useful, since transients are usually pop ups that you want to appear in your visible viewport; but occasionally an application uses a transient for something like a startup window that needs to be coerced into place. </p>
<p> <i>ManualPlacementIgnoresStartsOnPage</i> suppresses <i>StartsOnPage</i> or <i>StartsOnDesk</i> placement in the event that both <i>ManualPlacement</i> and <i>SkipMapping</i> are in effect when a window is created. This prevents you from interactively placing a window and then wondering where it disappeared to, because it got placed on a different desk or page. <i>ManualPlacementHonorsStartsOnPage</i> allows this to happen anyway. The option has no effect if <i>SkipMapping</i> is not in effect, because fvwm switches to the proper desk/page to perform interactive placement. The default is <i>ManualPlacementIgnoresStartsOnPage</i>; <i>ManualPlacementHonorsStartsOnPage</i> matches the way the old <i>StartsOnDesk</i> style used to handle the situation. </p>
<p> <i>CaptureHonorsStartsOnPage</i> causes the initial capture (of an already existing window) at startup to place the window according to the <i>StartsOnPage</i> and <i>StartsOnScreen</i> desk, page and Xinerama screen specification. <i>CaptureIgnoresStartsOnPage</i> causes fvwm to ignore these settings (including <i>StartsOnDesk</i>) on initial capture. The default is <i>CaptureIgnoresStartsOnPage</i>. </p>
<p> <i>RecaptureHonorsStartsOnPage</i> causes a window to be placed according to, or revert to, the <i>StartsOnPage</i> and <i>StartsOnScreen</i> desk, page and Xinerama screen specification on <code>Restart</code> or <i>Recapture</i>. <i>RecaptureIgnoresStartsOnPage</i> causes fvwm to respect the current window position on <code>Restart</code> or <code>Recapture</code>. The default is <i>RecaptureIgnoresStartsOnPage</i>. </p>
<p> <i>Layer</i> accepts one optional argument: a non-negative integer. This is the layer the window is put in. If no argument is given, any previously set value is deleted and the default layer is implied. </p>
<p> <i>StaysOnTop</i> puts the window in the top layer. This layer can be changed by the command <code>DefaultLayers</code>; the default is 6. </p>
<p> <i>StaysPut</i> puts the window in the put layer. This layer can be changed by the command <code>DefaultLayers</code>; the default is 4. </p>
<p> <i>StaysOnBottom</i> puts the window in the bottom layer. This layer can be changed by the command <code>DefaultLayers</code>; the default is 2. </p>
<p> <i>StartsLowered</i> instructs fvwm to put the window initially at the bottom of its layer rather than the default <i>StartsRaised</i>. </p>
<p> <i>StartShaded</i> tells fvwm to shade the window. An optional direction argument may be given, which can be one of &quot;<i>North</i>&quot;, &quot;<i>South</i>&quot;, &quot;<i>West</i>&quot;, &quot;<i>East</i>&quot;, &quot;<i>NorthWest</i>&quot;, &quot;<i>NorthEast</i>&quot;, &quot;<i>SouthWest</i>&quot;, &quot;<i>SouthEast</i>&quot; or if no direction is given, the default is to shade north. </p>
<p> <i>SkipMapping</i> tells fvwm not to switch to the desk the window is on when it gets mapped initially (useful with <i>StartsOnDesk</i> or <i>StartsOnPage</i>). </p>
<p> <i>KeepWindowGroupsOnDesk</i> makes new windows that have the window group hint set appear on the same desk as the other windows of the same group. Since this behavior may be confusing, the default setting is <i>ScatterWindowGroups</i>. The window group hint is ignored when placing windows in this case.</dl>
<dt><code>Transient windows</code></p>
<dd>
<dl>
<dt>
<dd> <i>DecorateTransient</i> causes transient windows, which are normally left undecorated, to be given the usual fvwm decorations (title bar, buttons, etc.). Note that some pop-up windows, such as the xterm menus, are not managed by the window manager and still do not receive decorations. <i>NakedTransient</i> (the default) causes transient windows not to be given the standard decorations. You can only bind keys or mouse buttons to the sides and the client part of an undecorated window (&#8216;S&#8217; and &acute;W&#8217; contexts in bindings, see <code>Mouse</code> and <i>Key</i> commands). </p>
<p> A window with the <i>RaiseTransient</i> style that has transient windows raises all its transients when it is raised. The <i>DontRaiseTransient</i> style disables this behavior. All windows are then treated as if they had no transients. </p>
<p> A window with the <i>LowerTransient</i> style that has transient windows lowers all its transients when it is lowered. The <i>DontLowerTransient</i> style disables this behavior. All windows are then treated as if they had no transients. </p>
<p> The <i>StackTransientParent</i> style augments <i>RaiseTransient</i> and <i>LowerTransient</i> styles. Raising a window with <i>StackTransientParent</i> style transfers the raise action to the main window if the window being raised is a transient and its main window has <i>RaiseTransient</i> style; this effect makes raise on a transient act just like raise on its main &#8211; the whole group is raised. Similar behavior holds for lowering a whole group of transients when the main has <i>LowerTransient</i> style. <i>DontStackTransientParent</i> turns this behavior off. <i>(Dont)StackTransientParent</i> has no effect if <i>RaiseTransient</i> and <i>LowerTransient</i> are not used. </p>
<p> A reasonable emulation of Motif raise/lower on transients is possible like this </p>
<dl>
<dt>
<dd>
<pre>
Style * RaiseTransient
Style * LowerTransient
Style * StackTransientParent
</pre>
</dl>
</dl>
<dt><code>Extended Window Manager Hints styles</code></p>
<dd>
<dl>
<dt>
<dd> To understand the used terminology in this sub section, please read the <code>Extended Window Manager Hints</code> section. </p>
<p> <i>EWMHDonateIcon</i> instructs fvwm to set the application ewmh icon hint with the icon that is used by fvwm if the application does not provide such hint (and if the icon used by fvwm is not an icon window). <i>EWMHDonateMiniIcon</i> does the same thing for mini icons. This allows compliant pager, taskbar, iconbox &#8230;etc to display the same (mini) icons as fvwm. Note that on some hardware (e.g., 8-bit displays) these styles can slow down window mapping and that in general only one of these styles is needed by a compliant application. <i>EWMHDontDonateIcon</i> and <i>EWMHDontDonateMiniIcon</i> restore the defaults which are to not set any ewmh (mini) icons hints. </p>
<p> By default, if an application provides an ewmh icon hint of small size (i.e., height and width less than or equal to 22), then fvwm uses this icon as its mini icon. <i>EWMHMiniIconOverride</i> instructs fvwm to ignore ewmh icons and to use the mini icon provided by the <i>MiniIcon</i> style. <i>EWMHNoMiniIconOverride</i> restores the default. </p>
<p> <i>EWMHUseStackingOrderHints</i> causes fvwm to use EWMH hints and respect EWMH hints which change the window layer. <i>EWMHIgnoreStackingOrderHints</i> causes fvwm to ignore EWMH layer hints. </p>
<p> An application can ask for some reserved space on the desktop by a hint. In the EWMH terminology such a hint is called a strut and it is used to compute the working area and may be used for window placement and in the maximize command. <i>EWMHIgnoreStrutHints</i> causes fvwm to ignore such hints, as <i>EWMHUseStrutHints</i>, causes fvwm to use it which is the default. </p>
<p> <i>EWMHIgnoreStateHints</i> causes fvwm to ignore initial EWMH state hints when a new window is mapped. The default <i>EWMHUseStateHints</i> causes fvwm to accept such hints. </p>
<p> <i>EWMHIgnoreWindowType</i> causes fvwm to ignore EWMH window type specification. The default <i>!EWMHIgnoreWindowType</i> causes fvwm to style windows of specified types as such. </p>
<p> <i>EWMHMaximizeIgnoreWorkingArea</i> causes fvwm to ignore the EWMH working area when it executes a <code>Maximize</code> command. With <i>EWMHMaximizeUseWorkingArea</i> the EWMH working area is used as with <i>EWMHMaximizeUseDynamicWorkingArea</i> the EWMH dynamic working area is used (the default). </p>
<p> <i>EWMHPlacementIgnoreWorkingArea</i> causes fvwm to ignore the EWMH working area when it places (or places again) a window. With <i>EWMHPlacementUseWorkingArea</i> the EWMH working area is taken in account as with <i>EWMHPlacementUseDynamicWorkingArea</i> the EWMH dynamic working area is taken in account (the default). Note that with the <i>MinOverlapPlacement</i> and <i>MinOverlapPercentPlacement</i> placement policy, the way the EWMH (dynamic) working area is taken in account is configurable with the <i>MinOverlapPlacementPenalties</i> style.</dl>
<dt><code>Miscellaneous</code></p>
<dd>
<dl>
<dt>
<dd> The <i>BackingStore</i>, <i>BackingStoreOff</i> and <i>BackingStoreWindowDefault</i> determine if the X server uses backing store for the window or not. <i>BackingStore</i> means that the X server tries to keep the obscured parts of a window in memory. This is usually slower if the client runs on the same machine as the X server, but can be much faster if the connection is slow (see also <i>SaveUnder</i> below). <i>BackingStoreOff</i> disables backing store for the window. By default, fvwm does not enable or disable backing store itself but leaves is as the window requested it. To revert back to the application&#8217;s choice, use the <i>BackingStoreWindowDefault</i> style. </p>
<p> Note: This style is useless if the X server does not allow backing store. </p>
<p> <i>SaveUnder</i> enables the corresponding window attribute in the X server. For a window using this style, the X server tries to store the graphics below it in memory which is usually slower if the client runs on the same machine as the X server. <i>SaveUnder</i> may speed up fvwm if the connection to the X server is slow (e.g. over a modem link). To disable save under, use the <i>SaveUnderOff</i> style. This is the default. See also <i>BackingStore</i> above. </p>
<p> Note: This style is useless if the X server does not allow save under. </p>
<p> <i>ParentalRelativity</i> enables clients that use a background pixmap of type <i>ParentRelative</i> to achieve transparency. Fvwm modules that support transparent colorsets require this setting. <i>Opacity</i> is the default and should be used for all non-transparent clients for better performance. </p>
<p> <i>MwmDecor</i> makes fvwm attempt to recognize and respect the mwm decoration hints that applications occasionally use. To switch this style off, use the <i>NoDecorHint</i> style. </p>
<p> <i>MwmFunctions</i> makes fvwm attempt to recognize and respect the mwm prohibited operations hints that applications occasionally use. <i>HintOverride</i> makes fvwm shade out operations that mwm would prohibit, but it lets you perform the operation anyway. <i>NoFuncHint</i> allows turns off the mwm hints completely. </p>
<p> <i>OLDecor</i> makes fvwm attempt to recognize and respect the olwm and olvwm hints that many older XView and OLIT applications use. Switch this option off with <i>NoOLDecor</i>. </p>
<p> With <i>GNOMEIgnoreHints</i> fvwm ignores all GNOME hints for the window, even if GNOME compliance is compiled in. This is useful for those pesky applications that try to be more clever than the user and use GNOME hints to force the window manager to ignore the user&#8217;s preferences. The <i>GNOMEUseHints</i> style switches back to the default behavior. </p>
<p> <i>UseDecor</i> This style is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> <i>UseDecor</i> accepts one argument: the name of a decor created with <code>AddToDecor</code>. If no decor name is specified, the &quot;Default&quot; decor is used. Windows do not actually contain decors, but are always assigned to one. If the decor is later modified with <code>AddToDecor</code>, the changes are visible for all windows which are assigned to it. The decor for a window can be reassigned with <code>ChangeDecor</code>. </p>
<p> <i>UseStyle</i> This style is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> <i>UseStyle</i> takes one arg, which is the name of another style. That way you can have unrelated window names easily inherit similar traits without retyping. For example: </p>
<dl>
<dt>
<dd>
<pre>
  Style rxvt UseStyle XTerm
</pre>
</dl>
<p> Warning: If a style is built from one or more parent styles and the parent styles are changed, the derived style is not modified. To achieve this you have to issue the <i>UseStyle</i> line again. </p>
<p> <i>Unmanaged</i> Windows with the <i>Unmanaged</i> style option are ignored by fvwm. They are not decorated, can not be moved or resized, etc. You probably want to use <code>Bugopts RaiseOverUnmanaged</code> too. This option can be turned off with the <i>!Unmanaged</i> style. However, windows that are already ignored at the time when the option is set must be recaptured with the <code>Recapture</code> command in order to become managed. </p>
<p> <i>State</i> sets the initial value of one of the 32 user defined states which are associated with each window. The state number ranges from 0 to 31 and must be given as an argument. The states have no meaning in fvwm, but they can be checked in conditional commands like <code>Next</code> with the <i>State</i> condition and manipulated with the <code>State</code> command. </p>
<dl>
<dt>
<dd>
<pre>
# turn on state 11 for xterms ...
Style xterm <code>State</code> 11
# ... but not for rxvts.
Style rxvt !State 11
</pre>
</dl>
<p> Windows with the <i>WindowListSkip</i> styles do not appear in the menu that is created with the <code>WindowList</code> command or the lists shown in several modules like <code>FvwmIconMan</code> or <code>FvwmWinList</code>. In the modules, the style can usually be ignored with an option. Please refer to the man page of the module in question for further information. To disable this feature, use the default style <i>WindowListHit</i>. </p>
<p> The styles <i>CirculateSkip</i> and <i>CirculateHit</i> control whether the window is considered by conditional commands, for example <code>Next</code>, <i>Prev</i> or <i>All</i>. Windows with <i>CirculateSkip</i>, are never selected by conditional commands. However, the styles can be overridden explicitly in the condition with the <i>CirculateHit</i>, <i>CirculateHitIcon</i> or <i>CirculateHitShaded</i> conditions, and some conditional commands, e.g. <code>Current</code> and <i>All</i>, do this by default. The styles <i>CirculateSkipIcon</i>, <i>CirculateHitIcon</i>, <i>CirculateSkipShaded</i> and <i>CirculateHitShaded</i> work like <i>CirculateSkip</i> and <i>CirculateHit</i> but apply only to iconic or shaded windows. Note: if multiple &#8230;Skip&#8230; options are combined, windows are only selected if they match none of the given conditions. So, with </p>
<dl>
<dt>
<dd>
<pre>
Style * CirculateSkipIcon, CirculateSkipShaded
</pre>
</dl>
<p> only windows that are neither iconic nor shaded are selected. Note: For historical reasons, the conditional commands understand the names of these styles as condition names. Take care not to confuse them.</dl>
<dt><code>Examples</code></p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# Change default fvwm behavior to no title-
# bars on windows! Also define a default icon.
Style *             !Title,                \
                    Icon unknown1.xpm,     \
                    BorderWidth 4,         \
                    HandleWidth 5
# now, window specific changes:
Style Fvwm*       !Handles, Sticky,        \
                  WindowListSkip,          \
                  BorderWidth 0
Style FvwmPager   StaysOnTop, BorderWidth 0
Style *lock       !Handles, Sticky,        \
                  StaysOnTop, WindowListSkip
Style xbiff       Sticky, WindowListSkip
Style FvwmButtons !Handles, Sticky,        \
                  WindowListSkip
Style sxpm        !Handles
# Put title-bars back on xterms only!
Style xterm     Title, Color black/grey
Style rxvt        Icon term.xpm
Style xterm       Icon rterm.xpm
Style xcalc       Icon xcalc.xpm
Style xbiff       Icon mail1.xpm
Style xmh         Icon mail1.xpm,         \
                    StartsOnDesk 2
Style xman        Icon xman.xpm
Style matlab      Icon math4.xpm,         \
                    StartsOnDesk 3
Style xmag        Icon magnifying_glass2.xpm
Style xgraph      Icon graphs.xpm
Style FvwmButtons Icon toolbox.xpm
Style Maker       StartsOnDesk 1
Style signal      StartsOnDesk 3
# Fire up Netscape on the second desk, in the
# middle of my 3x3 virtual desktop, and do not
# bother me with it...
Style Netscape* SkipMapping,              \
                StartsOnPage 1 1 1
</pre>
</dl>
<p> Note that all properties for a window are or&#8217;ed together. In the above example &quot;FvwmPager&quot; gets the property <i>StaysOnTop</i> via an exact window name match but also gets <i>!Handles</i>, <i>Sticky</i> and <i>WindowListSkip</i> by a match to &quot;Fvwm*&quot;. It gets <i>!Title</i> by virtue of a match to &quot;*&quot;. If conflicting styles are specified for a window, then the last style specified is used.</dl>
<dt><code>WindowStyle</code> <i>options</i></p>
<dd>
<dl>
<dt>
<dd> sets attributes (styles) on the selected window. The <i>options</i> are exactly the same as for the <code>Style</code> command.</dl>
</dl>
<h3>Window Styles</h3>
<dl>
<dt><code>AddButtonStyle</code> button [<i>state</i>] [<i>style</i>] [&#8211;&nbsp;<wbr>[!]<i>flag</i>&nbsp;<wbr>&#8230;]</p>
<dd>
<dl>
<dt>
<dd> Adds a button style to <i>button</i>. <i>button</i> can be a button number, or one of &quot;<i>All</i>&quot;, &quot;<i>Left</i>&quot; or &quot;<i>Right</i>&quot;. <i>state</i> can be &quot;<i>ActiveUp</i>&quot;, &quot;<i>ActiveDown</i>&quot;, &quot;<i>InactiveUp</i>&quot; or &quot;<i>InactiveDown</i>&quot;, or &quot;<i>Active</i>&quot; (the same as both &quot;ActiveUp&quot; and &quot;ActiveDown&quot;) or &quot;<i>Inactive</i>&quot; (the same as both &quot;InactiveUp&quot; and &quot;InactiveDown&quot;) or any of these 6 with &quot;<i>Toggled</i>&quot; prepended. The &quot;Active&quot; states apply to the focused window, the &quot;Inactive&quot; ones apply to all other windows. The &quot;Up&quot; states apply to the non pressed buttons, the &quot;Down&quot; ones apply to pressed buttons. The &quot;Toggled&quot; prefix refers to maximized, shaded or sticky windows that have the corresponding <i>MwmDecor&#8230;</i> button style set. Additionally, the following shortcuts may be used: &quot;<i>AllNormal</i>&quot;, &quot;<i>AllToggled</i>&quot;, &quot;<i>AllActive</i>&quot;, &quot;<i>AllInactive</i>&quot;, &quot;<i>AllUp</i>&quot;, &quot;<i>AllDown</i>&quot;. They are actually different masks for 4 individual states from 8 total. These are supported too: &quot;<i>AllActiveUp</i>&quot;, &quot;<i>AllActiveDown</i>&quot;, &quot;<i>AllInactiveUp</i>&quot;, &quot;<i>AllInactiveDown</i>&quot;. </p>
<p> If <i>state</i> is omitted, then the style is added to every state. If the <i>style</i> and <i>flags</i> are enclosed in parentheses, then multiple <i>state</i> definitions can be placed on a single line. <i>Flags</i> for additional button styles cannot be changed after definition. </p>
<p> Buttons are drawn in the order of definition, beginning with the most recent button style, followed by those added with <code>AddButtonStyle</code>. To clear the button style stack, change style flags, or for descriptions of available styles and flags, see the <code>ButtonStyle</code> command. Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>ButtonStyle</code> 1 Pixmap led.xpm -- Top Left
<code>ButtonStyle</code> 1 ActiveDown HGradient 8 grey black
<code>ButtonStyle</code> <code>All</code> --  UseTitleStyle
AddButtonStyle 1 \
        ActiveUp (Pixmap a.xpm) \
        ActiveDown (Pixmap b.xpm -- Top)
AddButtonStyle 1 Vector 4 50x30@1 70x70@0 30x70@0 50x30@1
</pre>
</dl>
<p> Initially for this example all button states are set to a pixmap. The second line replaces the &quot;ActiveDown&quot; state with a gradient (it overrides the pixmap assigned to it in the line before, which assigned the same style to every state). Then, the <i>UseTitleStyle</i> flag is set for all buttons, which causes fvwm to draw any styles set with <code>TitleStyle</code> before drawing the buttons. Finally, <code>AddButtonStyle</code> is used to place additional pixmaps for both &quot;ActiveUp&quot; and &quot;ActiveDown&quot; states and a vector button style is drawn on top of all states.</dl>
<dt><code>AddTitleStyle</code> [<i>state</i>] [<i>style</i>] [&#8211;&nbsp;<wbr>[!]<i>flag</i>&nbsp;<wbr>&#8230;]</p>
<dd>
<dl>
<dt>
<dd> Adds a title style to the title-bar. <i>state</i> can be &quot;<i>ActiveUp</i>&quot;, &quot;<i>ActiveDown</i>&quot;, &quot;<i>InactiveUp</i>&quot; or &quot;<i>InactiveDown</i>&quot;, or &quot;<i>Active</i>&quot; (the same as both &quot;ActiveUp&quot; and &quot;ActiveDown&quot;) or &quot;<i>Inactive</i>&quot; (the same as both &quot;InactiveUp&quot; and &quot;InactiveDown&quot;) or any of these 6 with &quot;Toggled&quot; prepended. If <i>state</i> is omitted, then the style is added to every state. If the <i>style</i> and <i>flags</i> are enclosed in parentheses, then multiple <i>state</i> definitions can be placed on a single line. This command is quite similar to the <code>AddButtonStyle</code> command. </p>
<p> Title-bars are drawn in the order of definition, beginning with the most recent <code>TitleStyle</code>, followed by those added with <code>AddTitleStyle</code>. To clear the title style stack, change style flags, or for the descriptions of available styles and flags, see the <code>TitleStyle</code> and <code>ButtonStyle</code> commands.</dl>
<dt><code>AddToDecor</code> <i>decor</i></p>
<dd>
<dl>
<dt>
<dd> This command is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> Add or divert commands to the decor named <i>decor</i>. A decor is a name given to the set of commands which affect button styles, title-bar styles and border styles. If <i>decor</i> does not exist it is created; otherwise the existing <i>decor</i> is modified. Note: Earlier versions allowed to use the <code>HilightColor</code>, <code>HilightColorset</code> and <code>WindowFont</code> commands in decors. This is no longer possible. Please use the <code>Style</code> command with the <i>Hilight&#8230;</i> and <i>Font</i> options. </p>
<p> New decors start out exactly like the &quot;default&quot; decor without any style definitions. A given decor may be applied to a set of windows with the <i>UseDecor</i> option of the <code>Style</code> command. Modifying an existing decor affects all windows which are currently assigned to it. </p>
<p> <code>AddToDecor</code> is similar in usage to the <code>AddToMenu</code> and <code>AddToFunc</code> commands, except that menus and functions are replaced by <code>ButtonStyle</code>, <code>AddButtonStyle</code>, <code>TitleStyle</code>, <code>AddTitleStyle</code> and <code>BorderStyle</code> commands. Decors created with <code>AddToDecor</code> can be manipulated with <code>ChangeDecor</code>, <code>DestroyDecor</code>, <code>UpdateDecor</code> and the <code>Style</code> option. </p>
<p> The following example creates a decor &quot;FlatDecor&quot; and style &quot;FlatStyle&quot;. They are distinct entities: </p>
<dl>
<dt>
<dd>
AddToDecor FlatDecor + ButtonStyle All Active(&#8211;flat) Inactive(&#8211;flat) + TitleStyle&#8211; flat<br />
    + BorderStyle&#8211; HiddenHandles NoInset Style FlatStyle UseDecor FlatDecor,<br />
    HandleWidth 4, ForeColor white,<br />
    BackColor grey40, HilightFore black, HilightBack grey70 Style xterm UseStyle FlatStyle
</dl>
<p> An existing window&#8217;s decor may be reassigned with <code>ChangeDecor</code>. A decor can be destroyed with <code>DestroyDecor</code>. </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyDecor</code> FlatDecor
AddToDecor FlatDecor ...
<code>Style</code> FlatStyle UseDecor FlatDecor
</pre>
</dl>
<p> and now apply the style again: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> xterm UseStyle FlatStyle
</pre>
</dl>
</dl>
<dt><code>BorderStyle</code> <i>state</i> [<i>style</i>] [&#8211;&nbsp;<wbr>[!]<i>flag</i>&nbsp;<wbr>&#8230;]</p>
<dd>
<dl>
<dt>
<dd> Defines a border style for windows. <i>state</i> can be either &quot;<i>Active</i>&quot; or &quot;<i>Inactive</i>&quot;. If <i>state</i> is omitted, then the style is set for both states. If the <i>style</i> and <i>flags</i> are enclosed in parentheses, then multiple <i>state</i> definitions can be specified per line. </p>
<p> <i>style</i> is a subset of the available button styles, and can only be <i>TiledPixmap</i> (uniform pixmaps which match the bevel colors work best this way) or <i>Colorset</i>. If a &#8216;!&#8217; is prefixed to any <i>flag</i>, the behavior is negated. If <i>style</i> is not specified, then one can change flags without resetting the style. </p>
<p> The <i>HiddenHandles</i> flag hides the corner handle dividing lines on windows with handles (this option has no effect for !<i>Handles</i> windows). By default, <i>HiddenHandles</i> is disabled. </p>
<p> The <i>NoInset</i> flag supplements <i>HiddenHandles</i>. If given, the inner bevel around the window frame is not drawn. If <i>HiddenHandles</i> is not specified, the frame looks a little strange. </p>
<p> <i>Raised</i> causes a raised relief pattern to be drawn (default). <i>Sunk</i> causes a sunken relief pattern to be drawn. <i>Flat</i> inhibits the relief pattern from being drawn. </p>
<p> To decorate the active and inactive window borders with a textured pixmap, one might specify: </p>
<dl>
<dt>
<dd>
<pre>
BorderStyle Active TiledPixmap marble.xpm
BorderStyle Inactive TiledPixmap granite.xpm
BorderStyle Active -- HiddenHandles NoInset
</pre>
</dl>
<p> To clear the style for both states: </p>
<dl>
<dt>
<dd>
<pre>
BorderStyle <i>Simple</i>
</pre>
</dl>
<p> To clear for a single state: </p>
<dl>
<dt>
<dd>
<pre>
BorderStyle Active Simple
</pre>
</dl>
<p> To unset a flag for a given state: </p>
<dl>
<dt>
<dd>
<pre>
BorderStyle Inactive -- !NoInset
</pre>
</dl>
<p> title-bar buttons can inherit the border style with the <i>UseBorderStyle</i> flag (see <code>ButtonStyle</code>).</dl>
<dt><code>ButtonState</code> [ActiveDown&nbsp;<wbr><i>bool</i>] [Inactive&nbsp;<wbr><i>bool</i>] [InactiveDown&nbsp;<wbr><i>bool</i>]</p>
<dd>
<dl>
<dt>
<dd> The <code>ButtonState</code> command controls which states of the window titles and title buttons are used. The default is to use all four states: &quot;ActiveUp&quot;, &quot;ActiveDown&quot;, &quot;InactiveUp&quot; and &quot;InactiveDown&quot; (see <code>ButtonStyle</code> and <code>TitleStyle</code> commands). The <i>bool</i> argument after the key word controls if the designated state is used (&quot;True&quot;) or not (&quot;False&quot;). The <i>bool</i> flag is the same as other commands, and not limited to just &quot;True&quot; or &quot;False&quot;; &quot;Yes&quot; and &quot;No&quot; may also be used. The &quot;ActiveUp&quot; state cannot be deactivated. If no arguments are provided or the given arguments are illegal, the default is restored. </p>
<p> If <i>ActiveDown</i> argument is &quot;False&quot;, no different button style for the pressed down buttons used, instead &quot;ActiveUp&quot; state is used even when button is pressed. </p>
<p> If <i>Inactive</i> argument is &quot;False&quot;, focused and unfocused windows look similarly, the corresponding &quot;Active&quot; states are always used. </p>
<p> If <i>InactiveDown</i> argument is &quot;False&quot; (only applied when <i>Inactive</i> is &quot;True&quot;), the pressed titles and title buttons in non-focused windows are drawn using &quot;InactiveUp&quot; or &quot;ActiveUp&quot; states depending on the values of the other key words.</dl>
<dt><code>ButtonStyle</code> button [<i>state</i>] [<i>style</i>] [&#8211;&nbsp;<wbr>[!]<i>flag</i>&nbsp;<wbr>&#8230;]</p>
<dd>
<dl>
<dt>
<dd> Sets the button style for a title-bar button. <i>button</i> is the title-bar button number between 0 and 9, or one of &quot;<i>All</i>&quot;, &quot;<i>Left</i>&quot;, &quot;<i>Right</i>&quot;, or &quot;<i>Reset</i>&quot;. Button numbering is described in the <code>Mouse</code> command section. If the <i>style</i> and <i>flags</i> are enclosed in parentheses, then multiple <i>state</i> definitions can be specified per line. </p>
<p> <i>state</i> refers to which button state should be set. Button states are defined as follows: &quot;<i>ActiveUp</i>&quot; and &quot;<i>ActiveDown</i>&quot; refer to the un-pressed and pressed states for buttons on active windows; while the &quot;<i>InactiveUp</i>&quot; and &quot;<i>InactiveDown</i>&quot; states denote buttons on inactive windows. The shortcut &quot;<i>Active</i>&quot; denotes both &quot;ActiveUp&quot; and &quot;ActiveDown&quot; states. Shortcut &quot;<i>Inactive</i>&quot; denotes both &quot;InactiveUp&quot; and &quot;InactiveDown&quot; states. The similar state names like just described, but with the &quot;Toggled&quot; prefix are used instead for title buttons which have one of the <i>MwmDecorMax</i>, <i>MwmDecorShade</i>, <i>MwmDecorStick</i> or <i>MwmDecorLayer</i> hints, if the window is maximized, shaded, sticky or placed on specific layer, respectively. </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToDecor</code> Default
 + ButtonStyle 6                   \
   Vector 4 50x25@1 85x75@0 15x75@0 50x25@1
 + ButtonStyle 6 ToggledActiveUp   \
   Vector 4 50x75@0 85x25@1 15x25@0 50x75@0
 + ButtonStyle 6 ToggledActiveDown \
   Vector 4 50x75@0 85x25@1 15x25@0 50x75@0
 + ButtonStyle 6 ToggledInactive   \
   Vector 4 50x75@0 85x25@1 15x25@0 50x75@0
 + ButtonStyle 6 - MwmDecorShade
<code>Mouse</code> 0 6 N <code>WindowShade</code>
</pre>
</dl>
<p> Additionally, the following shortcuts may be used: &quot;<i>AllNormal</i>&quot;, &quot;<i>AllToggled</i>&quot;, &quot;<i>AllActive</i>&quot;, &quot;<i>AllInactive</i>&quot;, &quot;<i>AllUp</i>&quot;, &quot;<i>AllDown</i>&quot;. They are actually different masks for 4 individual states from 8 total. These are supported too: &quot;<i>AllActiveUp</i>&quot;, &quot;<i>AllActiveDown</i>&quot;, &quot;<i>AllInactiveUp</i>&quot;, &quot;<i>AllInactiveDown</i>&quot;. </p>
<p> If <i>state</i> is specified, that particular button state is set. If <i>state</i> is omitted, every state is set. Specifying a style destroys the current style (use <code>AddButtonStyle</code> to avoid this). </p>
<p> If <i>style</i> is omitted, then state-dependent flags can be set for the primary button style without destroying the current style. Examples (each line should be considered independent): </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle Left -- flat
ButtonStyle All ActiveUp (-- flat) Inactive (-- flat)
</pre>
</dl>
<p> The first line sets every state of the left buttons to flat, while the second sets only the &quot;ActiveUp&quot; and &quot;Inactive&quot; states of every button to flat (only flags are changed; the buttons&#8217; individual styles are not changed). </p>
<p> If you want to reset all buttons to their defaults: </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle <i>Reset</i>
</pre>
</dl>
<p> To reset the &quot;ActiveUp&quot; button state of button 1 to the default: </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle 1 ActiveUp Default
</pre>
</dl>
<p> To reset all button states of button 1 to the default of button number 2: </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle 1 Default 2
</pre>
</dl>
<p> For any button, multiple <i>state</i> definitions can be given on one line by enclosing the <i>style</i> and <i>flags</i> in parentheses. If only one definition per line is given the parentheses can be omitted. </p>
<p> <i>flags</i> affect the specified <i>state</i>. If a &#8216;!&#8217; is prefixed to any <i>flag</i>, its behavior is negated. The available state-dependent flags for all styles are described here (the <code>ButtonStyle</code> entry deals with state-independent flags). </p>
<p> <i>Raised</i> causes a raised relief pattern to be drawn. </p>
<p> <i>Sunk</i> causes a sunken relief pattern to be drawn. </p>
<p> <i>Flat</i> inhibits the relief pattern from being drawn. </p>
<p> <i>UseTitleStyle</i> causes the given button state to render the current title style before rendering the buttons&#8217; own styles. The <i>Raised</i>, <i>Flat</i> and <i>Sunk</i> <code>TitleStyle</code> flags are ignored since they are redundant in this context. </p>
<p> <i>UseBorderStyle</i> causes the button to inherit the decorated <code>BorderStyle</code> options. </p>
<p> <i>Raised</i>, <i>Sunk</i> and <i>Flat</i> are mutually exclusive, and can be specified for the initial <code>ButtonStyle</code> only. <i>UseTitleStyle</i> and <i>UseBorderStyle</i> are also mutually exclusive (both can be off however). The default is <i>Raised</i> with both <i>UseBorderStyle and UseTitleStyle</i> left unset. </p>
<p> <code>Important</code> </p>
<p> for the &quot;ActiveDown&quot; and &quot;InactiveDown&quot; states: When a button is pressed, the relief is inverted. Because of this, to obtain the raised look in &quot;ActiveDown&quot; or &quot;InactiveDown&quot; states you must specify the opposite of the desired relief (i.e. <i>Sunk</i> for &quot;ActiveDown&quot; or &quot;InactiveDown&quot;). This behavior is consistent, but may seem confusing at first. The same applies to the &quot;Toggled&quot; states. </p>
<p> Button styles are classified as non-destructive, partially destructive, or fully destructive. Non-destructive styles do not affect the image. Partially destructive styles can obscure some or all parts of the underlying image (i.e. <i>Pixmap</i>). Fully destructive styles obscure the entire underlying image (i.e. <i>Solid</i> or one of the <i>gradient</i> styles). Thus, if stacking styles with <code>AddButtonStyle</code> (or <code>AddTitleStyle</code> for title-bars), use care in sequencing styles to minimize redraw. </p>
<p> The available styles are: </p>
<p> <i>Simple</i>, <i>Default</i>, <i>Solid</i>, <i>Colorset</i>, <i>Vector</i>, <i>?Gradient</i>, <i>Pixmap</i>, <i>AdjustedPixmap</i>, <i>ShrunkPixmap</i>, <i>StretchedPixmap</i>, <i>TiledPixmap</i>, <i>MiniIcon</i> </p>
<p> The description of these styles and their arguments follow: </p>
<p> The <i>Simple</i> style does nothing. There are no arguments, and this style is an example of a non-destructive button style. </p>
<p> The <i>Default</i> style conditionally accepts one argument: a number which specifies the default button number to load. If the style command given is <code>ButtonStyle</code> or <code>AddButtonStyle</code>, the argument is optional (if given, it overrides the current button). If a command other than <code>ButtonStyle</code> or <code>AddButtonStyle</code> is used, the number must be specified. </p>
<p> The <i>Solid</i> style fills the button with a solid color. The relief border color is not affected. The color is specified as a single argument. This style is fully destructive. </p>
<p> The <i>Colorset</i> <i>cs</i> [<i>alpha</i>] style fills the button with the Colorset <i>cs</i>. The optional <i>alpha</i> argument is a percentage between 0 and 100. It causes fvwm to merge the colorset background onto the button using this percentage. If the percentage is 0 the colorset background is hidden and if it is 100 the colorset background is fully applied. The default is 100. So, the destructiveness depends on the <i>alpha</i> argument. </p>
<p> The <i>Vector</i> <i>num</i> <i>X</i><code>[</code><i>offset</i><code>p]x</code><i>Y</i><code>[</code><i>offset</i><code>p]@</code><i>C</i><code> &#8230;</code> style draws a line pattern. Since this is a standard button style, the keyword <i>Vector</i> is optional, <i>num</i> is a number of point specifications of the form <i>X</i><code>[</code><i>offset</i><code>p]x</code><i>Y</i><code>[</code><i>offset</i><code>p]@</code><i>C</i><code> &#8230;</code> <i>X</i> and <i>Y</i> are point coordinates inside the button, given in percents (from 0 to 100). An optional absolute <i>offset</i> in pixels, can be given as &quot;+&lt;offset&gt;p&quot; for a positive or &quot;-&lt;offset&gt;p&quot; for a negative offset. </p>
<p> <i>C</i> specifies a line color (0 &#8211; the shadow color, 1 &#8211; the highlight color, 2 &#8211; the background color, 3 &#8211; the foreground color, 4 &#8211; only move the point, do not draw). The first point color is not used. You can use up to 10000 points in a line pattern. This style is partially destructive. </p>
<p> The specification is a little cumbersome: </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle 2 Vector 4 50x30@1 70x70@0 30x70@0 50x30@1
</pre>
</dl>
<p> then the button 2 decoration uses a 4-point pattern consisting of a line from (x=50,y=30) to (70,70) in the shadow color (@0), and then to (30,70) in the shadow color, and finally to (50,30) in the highlight color (@1). Is that too confusing? See the fvwm web pages for some examples with screenshots. </p>
<p> A more complex example of <i>Vector</i>: </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle 8 Vector 10 45x65@2 45x75@3 \
  20x75@3 20x50@3 35x50@3 35x65@1 35x25@1 \
  75x25@1 75x65@0 35x65@0
ButtonStyle 0 Vector 10 45x65@2 45x75@0 \
  20x75@0 20x50@1 45x50@1 45x65@0 75x65@3 \
  75x25@3 35x25@3 35x47@3
</pre>
</dl>
<p> The <i>?Gradient</i> styles denote color gradients. Fill in the question mark with any one of the defined gradient types. Please refer to the <code>Color Gradients</code> section for a description of the gradient syntax. The gradient styles are fully destructive. </p>
<p> The <i>Pixmap</i> style displays a pixmap. A pixmap should be specified as an argument. For example, the following would give button number 2 the same pixmap for all 4 states (2 active and 2 inactive), and button number 4 all different pixmaps. </p>
<dl>
<dt>
<dd>
<pre>
ButtonStyle 2 Pixmap my_pixmap.xpm
ButtonStyle 4 \
        ActiveUp (Pixmap activeup.xpm) \
        ActiveDown (Pixmap activedown.xpm) \
        Inactive (Pixmap inactiveup.xpm)
ButtonStyle 4 \
        InactiveDown Pixmap inactivedown.xpm
</pre>
</dl>
<p> The pixmap specification can be given as an absolute or relative pathname (see <code>ImagePath</code>). If the pixmap cannot be found, the button style reverts to <i>Simple</i>. Flags specific to the <i>Pixmap</i> style are <i>Left</i>, <i>Right</i>, <i>Top</i>, and <i>Bottom</i>. These can be used to justify the pixmap (default is centered for both directions). Pixmap transparency is used for the color &quot;None.&quot; This style is partially destructive. </p>
<p> The <i>AdjustedPixmap</i> style is similar to the <i>Pixmap</i> style. But the image is resized to exactly fit the button. </p>
<p> The <i>ShrunkPixmap</i> style is similar to the <i>Pixmap</i> style. But if the image is bigger than the button the image is resized to fit into the button. </p>
<p> The <i>StretchedPixmap</i> style is similar to the <i>Pixmap</i> style. But if the image is smaller than the button the image is resized to cover the button. </p>
<p> The <i>TiledPixmap</i> style accepts a pixmap to be tiled as the button background. One pixmap is specified as an argument. Pixmap transparency is not used. This style is fully destructive. </p>
<p> The <i>MiniIcon</i> style draws the window&#8217;s miniature icon in the button, which is specified with the <i>MiniIcon</i> option of the <code>Style</code> command. This button style accepts no arguments. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> *     MiniIcon mini-bx2.xpm
<code>Style</code> xterm MiniIcon mini-term.xpm
<code>Style</code> Emacs MiniIcon mini-doc.xpm
ButtonStyle 1 MiniIcon
</pre>
</dl>
</dl>
<dt><code>ButtonStyle</code> <i>button</i> &#8211; [!]<i>flag</i> &#8230;</p>
<dd>
<dl>
<dt>
<dd> Sets state-independent flags for the specified <i>button</i>. State-independent flags affect button behavior. Each <i>flag</i> is separated by a space. If a &#8216;!&#8217; is prefixed to the flag then the behavior is negated. The special flag <i>Clear</i> clears any existing flags. </p>
<p> The following flags are usually used to tell fvwm which buttons should be affected by mwm function hints (see <i>MwmFunctions</i> option of the <code>Style</code> command. This is not done automatically since you might have buttons bound to complex functions, for instance. </p>
<p> <i>MwmDecorMenu</i> should be assigned to title-bar buttons which display a menu. The default assignment is the leftmost button. When a window with the <i>MwmFunctions</i> <code>Style</code> option requests not to show this button, it is hidden. </p>
<p> <i>MwmDecorMin</i> should be assigned to title-bar buttons which minimize or iconify the window. The default assignment is the second button over from the rightmost button. When a window with the <i>MwmFunctions</i> <code>Style</code> option requests not to show this button, it is hidden. </p>
<p> <i>MwmDecorMax</i> should be assigned to title-bar buttons which maximize the window. The default assignment is the rightmost button. When a window with the <i>MwmFunctions</i> <code>Style</code> option requests not to show this button, it is hidden. When the window is maximized, the vector pattern on the button looks pressed in. </p>
<p> <i>MwmDecorShade</i> should be assigned to title-bar buttons which shade the window (see <code>WindowShade</code> command). When the window is shaded, the vector pattern on the button looks pressed in. </p>
<p> <i>MwmDecorStick</i> should be assigned to title-bar buttons which make the window sticky. When the window is sticky, the vector pattern on the button looks pressed in. </p>
<p> The flag <i>MwmDecorLayer</i> <i>layer</i> should be assigned to title-bar buttons which place the window in the layer numbered <i>layer</i>. When the window is on that specific layer, the vector pattern on the button looks pressed in.</dl>
<dt><code>ChangeDecor</code> <i>decor</i></p>
<dd>
<dl>
<dt>
<dd> This command is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> Changes the decor of a window to <i>decor</i>. <i>decor</i> is &quot;Default&quot; or the name of a decor defined with <code>AddToDecor</code>. If <i>decor</i> is invalid, nothing occurs. If called from somewhere in a window or its border, then that window is affected. If called from the root window the user is allowed to select the target window. <code>ChangeDecor</code> only affects attributes which can be set using the <code>AddToDecor</code> command. </p>
<dl>
<dt>
<dd>
<pre>
ChangeDecor CustomDecor1
</pre>
</dl>
</dl>
<dt><code>DestroyDecor</code> [recreate] <i>decor</i></p>
<dd>
<dl>
<dt>
<dd> This command is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> Deletes the <i>decor</i> defined with <code>AddToDecor</code>, so that subsequent references to it are no longer valid. Windows using this <i>decor</i> revert to the &quot;Default&quot; decor. The optional parameter <i>recreate</i> tells fvwm not to throw away the decor completely but to throw away only its contents. If the decor is created again later, windows do not use it before the <i>UseDecor</i> style is applied again unless the decor was destroyed with the <i>recreate</i> option. The decor named &quot;Default&quot; cannot be destroyed. </p>
<dl>
<dt>
<dd>
<pre>
DestroyDecor CustomDecor1
</pre>
</dl>
</dl>
<dt><code>TitleStyle</code> [<i>justification</i>] [Height&nbsp;<wbr>[<i>num</i>]] [MinHeight&nbsp;<wbr>[<i>num</i>]]</p>
<dd>
<dl>
<dt>
<dd> Sets attributes for the title-bar. Justifications can be <i>Centered</i>, <i>RightJustified</i> or <i>LeftJustified</i>. <i>Height</i> sets the title bar&#8217;s height to an amount in pixels. <i>MinHeight</i> sets the minimal height in pixels of the title bar. Defaults are <i>Centered</i>, the window&#8217;s font height and no minimal height. To reset the font height to the default value, omit the <i>num</i> argument after the <i>Height</i> keyword. The <i>MinHeight</i> height is reseted by <i>Height</i> or if given with no argument. Example: </p>
<dl>
<dt>
<dd>
<pre>
TitleStyle LeftJustified Height 24
</pre>
</dl>
</dl>
<dt><code>TitleStyle</code> [<i>state</i>] [<i>style</i>] [&#8211;&nbsp;<wbr>[!]<i>flag</i>&nbsp;<wbr>&#8230;]</p>
<dd>
<dl>
<dt>
<dd> Sets the style for the title-bar. See also <code>AddTitleStyle</code> and <code>ButtonStyle</code> <i>state</i> can be one of &quot;<i>ActiveUp</i>&quot;, &quot;<i>ActiveDown</i>&quot;, &quot;<i>InactiveUp</i>&quot;, or &quot;<i>InactiveDown</i>&quot;. Shortcuts like &quot;<i>Active</i>&quot; and &quot;<i>Inactive</i>&quot; are allowed. The states with the &quot;Toggled&quot; prefix are allowed too, the title itself does not use &quot;Toggled&quot; states, but these states are used for the buttons with <code>ButtonStyle</code> <i>UseTitleStyle</i>. If <i>state</i> is omitted, then the <i>style</i> is added to every state. If parentheses are placed around the <i>style</i> and <i>flags</i>, then multiple state definitions can be given per line. <i>style</i> can be omitted so that flags can be set while not destroying the current style. </p>
<p> If a &#8216;!&#8217; is prefixed to any <i>flag</i>, its behavior is negated. Valid flags for each state include <i>Raised</i>, <i>Flat</i> and <i>Sunk</i> (these are mutually exclusive). The default is <i>Raised</i>. See the note in <code>ButtonStyle</code> regarding the &quot;<i>ActiveDown</i>&quot; state. Examples: </p>
<dl>
<dt>
<dd>
TitleStyle ActiveUp HGradient 16 navy black<br />
    TitleStyle<br />
    ActiveDown(Solid red&#8211; flat)<br />
        Inactive(TiledPixmap wood.xpm)<br />
            TitleStyle<br />
    ActiveUp(&#8211;Flat)<br />
        ActiveDown(&#8211;Raised)<br />
            InactiveUp(&#8211;Flat)<br />
                InactiveDown(&#8211;Sunk)
</dl>
<p> This sets the &quot;ActiveUp&quot; state to a horizontal gradient, the &quot;ActiveDown&quot; state to solid red, and the &quot;Inactive&quot; states to a tiled wood pixmap. Finally, &quot;ActiveUp&quot; and &quot;InactiveUp&quot; are set to look flat, while &quot;ActiveDown&quot; set to be sunk (the <i>Raised</i> flag for the &quot;ActiveDown&quot; state causes it to appear sunk due to relief inversion), and &quot;InactiveDown&quot; is set to look raised. An example which sets flags for all states: </p>
<dl>
<dt>
<dd>
<pre>
TitleStyle -- flat
</pre>
</dl>
<p> For a flattened look: </p>
<dl>
<dt>
<dd>
<pre>
TitleStyle -- flat
<code>ButtonStyle</code> <code>All</code> Active (-- flat) Inactive (-- flat)
</pre>
</dl>
<p> <code>TitleStyle</code> accepts all the <code>ButtonStyle</code> styles and arguments: </p>
<p> <i>Simple</i>, <i>Default</i>, <i>Solid</i>, <i>Colorset</i>, <i>Vector</i>, <i>?Gradient</i>, <i>Pixmap</i>, <i>AdjustedPixmap</i>, <i>ShrunkPixmap</i>, <i>StretchedPixmap</i>, <i>TiledPixmap</i>, <i>MiniIcon</i>. </p>
<p> See the <code>ButtonStyle</code> command for a description of all these styles and their arguments. </p>
<p> In addition to these styles <code>TitleStyle</code> accepts a powerful <i>MultiPixmap</i> option. This allows you to specify different pixmaps, colorsets or colors for different parts of the titlebar. Some of them are tiled or stretched to fit a particular space; others are discrete &quot;transition&quot; images. The definable <i>sections</i> are: </p>
<p> <i>Main</i></p>
<dl>
<dt>
<dd> The full titlebar</dl>
<p> <i>LeftMain</i></p>
<dl>
<dt>
<dd> Left of title text</dl>
<p> <i>RightMain</i></p>
<dl>
<dt>
<dd> Right of title text</dl>
<p> <i>UnderText</i></p>
<dl>
<dt>
<dd> Underneath title text</dl>
<p> <i>LeftOfText</i></p>
<dl>
<dt>
<dd> just to the left of the title text</dl>
<p> <i>RightOfText</i></p>
<dl>
<dt>
<dd> just to the right of the title text</dl>
<p> <i>LeftEnd</i></p>
<dl>
<dt>
<dd> at the far left end of the titlebar (just after left buttons if any)</dl>
<p> <i>RightEnd</i></p>
<dl>
<dt>
<dd> at the far right end of the titlebar (just before right buttons if any)</dl>
<p> <i>Buttons</i></p>
<dl>
<dt>
<dd> under buttons in case of <i>UseTitleStyle</i></dl>
<p> <i>LeftButtons</i></p>
<dl>
<dt>
<dd> under left buttons in case of <i>UseTitleStyle</i></dl>
<p> <i>RightButtons</i></p>
<dl>
<dt>
<dd> under right buttons in case of <i>UseTitleStyle</i></dl>
<p> None of these are mandatory except for <i>Main</i> (or, if you do not define <i>Main</i> you must define both <i>LeftMain</i> and <i>RightMain</i>). If no <i>Buttons</i> pixmaps are defined and <i>UseTitleStyle</i> is specified for one or more buttons, <i>Main</i>, <i>LeftMain</i> or <i>RightMain</i> are used as appropriate. </p>
<p> The syntax for this style type is: </p>
<dl>
<dt>
<dd>
<pre>
MultiPixmap section style arg, ...
</pre>
</dl>
<p> continuing for whatever you want to define. The <i>style</i> can be either <i>TiledPixmap</i>, <i>AdjustedPixmap</i>, <i>Colorset</i> or <i>Solid</i>. See the <code>ButtonStyle</code> command for the description of these styles. In the case of a transition section, <i>LeftEnd</i>, <i>LeftOfText</i>, <i>RightOfText</i> or <i>RightEnd</i>, <i>AdjustedPixmap</i> only resize the pixmap in the &quot;y&quot; direction. For the <i>Colorset</i> and <i>Solid</i> styles a width of the half of the title bar height is assumed for the transition sections. </p>
<p> An example: </p>
<dl>
<dt>
<dd>
<pre>
MultiPixmap Main AdjustedPixmap foo.xpm, \
            UnderText TiledPixmap bar.xpm, \
            Buttons <i>Colorset</i> 2
</pre>
</dl>
<p> Note that the old syntax is still supported: if the style is omitted, <i>TiledPixmap</i> is assumed and adding &quot;(stretched)&quot; between the section and the file name implies <i>AdjustedPixmap</i>.</dl>
<dt><code>UpdateDecor</code> [<i>decor</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is deprecated and will be removed in the future. There are plans to replace it with a more flexible solution in fvwm-3.0. </p>
<p> This command is kept mainly for backward compatibility. Since all elements of a decor are updated immediately when they are changed, this command is mostly useless. </p>
<p> Updates window decorations. <i>decor</i> is an optional argument which specifies the <i>decor</i> to update. If given, only windows which are assigned to that particular <i>decor</i> are updated. This command is useful, for instance, after a <code>ButtonStyle</code>, <code>TitleStyle</code> or <code>BorderStyle</code> (possibly used in conjunction with <code>AddToDecor</code>). Specifying an invalid decor results in all windows being updated. This command is less disturbing than <code>Recapture</code>, but does not affect window style options as <code>Recapture</code> does.</dl>
</dl>
<h3>Controlling the Virtual Desktop</h3>
<dl>
<dt><code>Desk</code> <i>arg1</i> [<i>arg2</i>] [<i>min</i>&nbsp;<wbr><i>max</i>]</p>
<dd>
<dl>
<dt>
<dd> This command has been renamed. Please see <code>GotoDesk</code> command.</dl>
<dt><code>DesktopName</code> <i>desk</i> <i>name</i></p>
<dd>
<dl>
<dt>
<dd> Defines the name of the desktop number <i>desk</i> to <i>name</i>. This name is used in the <code>WindowList</code> command and in the <code>FvwmPager</code> where it override the <i>Label</i> configuration option. Moreover, if consecutive names starting from desktop 0 are defined, then these names can be used by any EWMH compliant application (as a pager).</dl>
<dt><code>DesktopSize</code> <i>Horizontal</i>x<i>Vertical</i></p>
<dd>
<dl>
<dt>
<dd> Defines the virtual desktop size in units of the physical screen size.</dl>
<dt><code>EdgeResistance</code> <i>delay</i><code>EdgeResistance</code> <i>scrolling</i> <i>moving</i> [<i>xinerama-scrolling</i>]</p>
<dd>
<dl>
<dt>
<dd> Tells how hard it should be to change the desktop viewport by moving the mouse over the edge of the screen. The parameter tells how many milliseconds the pointer must spend on the screen edge before fvwm moves the viewport. This is intended for people who use </p>
<dl>
<dt>
<dd>
<pre>
<code>EdgeScroll</code> 100 100
</pre>
</dl>
<p> but find themselves accidentally flipping pages when they do not want to. If -1 is given as the delay, scrolling is disabled completely. </p>
<p> The second form of invocation with two or three arguments is obsolete and should be replaced with the following three commands as needed: </p>
<dl>
<dt>
<dd>
<pre>
<code>EdgeResistance</code> <i>scrolling</i>
<code>Style</code> * EdgeMoveDelay <i>scrolling</i>
<code>Style</code> * EdgeMoveResistance <i>moving</i>
or
<code>Style</code> * EdgeMoveResistance <i>moving</i> <i>xinerama-scrolling</i>
</pre>
</dl>
<p> Fvwm does this substitution automatically and prints a warning.</dl>
<dt><code>EdgeScroll</code> <i>horizontal</i>[p] <i>vertical</i>[p] [wrap | wrapx | wrapy]</p>
<dd>
<dl>
<dt>
<dd> Specifies the percentage of a page to scroll when the cursor hits the edge of a page. A trailing &#8216;<i>p</i>&#8216; changes the interpretation to mean pixels. If you do not want any paging or scrolling when you hit the edge of a page include </p>
<dl>
<dt>
<dd>
<pre>
EdgeScroll 0 0
</pre>
</dl>
<p> in your <i>config</i> file, or possibly better, set the <code>EdgeThickness</code> to zero. See the <code>EdgeThickness</code> command. If you want whole pages, use </p>
<dl>
<dt>
<dd>
<pre>
EdgeScroll 100 100
</pre>
</dl>
<p> Both <i>horizontal</i> and <i>vertical</i> should be positive numbers. </p>
<p> If the <i>horizontal</i> and <i>vertical</i> percentages are multiplied by 1000 or one of the keywords <i>wrap</i>, <i>wrapx</i> and <i>wrapy</i> is given then scrolling wraps around at the edge of the desktop. If </p>
<dl>
<dt>
<dd>
<pre>
EdgeScroll 100000 100000
</pre>
</dl>
<p> is used fvwm scrolls by whole pages, wrapping around at the edge of the desktop.</dl>
<dt><code>EdgeThickness</code> 0 | 1 | 2</p>
<dd>
<dl>
<dt>
<dd> This is the width or height of the invisible window that fvwm creates on the edges of the screen that are used for the edge scrolling feature. </p>
<p> In order to enable page scrolling via the mouse, four windows called the &quot;pan frames&quot; are placed at the very edge of the screen. This is how fvwm detects the mouse&#8217;s presence at the window edge. Because of the way this works, they need to be at the top of the stack and eat mouse events, so if you have any kind of error along the lines of: &quot;mouse clicks at the edge of the screen do the wrong thing&quot; you&#8217;re having trouble with the pan frames and (assuming you do not use the mouse to flip between pages) should set the EdgeThickness to 0. </p>
<p> A value of 0 completely disables mouse edge scrolling, even while dragging a window. 1 gives the smallest pan frames, which seem to work best except on some servers. </p>
<p> 2 is the default. </p>
<p> Pan frames of 1 or 2 pixels can sometimes be confusing, for example, if you drag a window over the edge of the screen, so that it straddles a pan frame, clicks on the window, near the edge of the screen are treated as clicks on the root window.</dl>
<dt><code>EwmhBaseStruts</code> <i>left</i> <i>right</i> <i>top</i> <i>bottom</i></p>
<dd>
<dl>
<dt>
<dd> Where left, right, top and bottom are positive or null integers which define bands at the edge of the screen. <i>left</i> defines a band on the left of your screen of width <i>left</i>, <i>right</i> defines a band on the right of your screen of width <i>right</i>, <i>top</i> defines a band on the top of your screen of height <i>top</i> and <i>bottom</i> defines a band on the bottom of your screen of height <i>bottom</i>. The unit is the pixel and the default is 0 0 0 0. These areas define additional reserved space to the reserved space defined by some ewmh compliant applications. This is used to compute the Working Area. See the <code>Extended Window Manager Hints</code> section for a definition of the Working Area.</dl>
<dt><code>EwmhNumberOfDesktops</code> <i>num</i> [<i>max</i>]</p>
<dd>
<dl>
<dt>
<dd> This command is useful only for an ewmh compliant pager or taskbar (as kpager or kicker taskbar) and not for fvwm modules ( <code>FvwmPager</code> or <code>FvwmIconMan</code>). It causes a compliant application to consider at least <i>num</i> desktops (desktop 0 to desktop <i>num</i>-1). The optional argument <i>max</i> causes a compliant application to never consider more than <i>max</i> desktops. If <i>max</i> is 0 (the default) there is no limitation. The actual number of desktops is determined dynamically. It is at least <i>num</i>, but it can be d if there is a window on desktop d-1 (or if the current desktop is desktop d-1) and d is less or equal to <i>max</i> or <i>max</i> is null. Moreover, a compliant pager can ask to change <i>num</i> itself. This is accepted by fvwm only if this number is less than or equal to <i>max</i> or if <i>max</i> is null. Note that negative desktops are not supported by the ewmh specification. The default is 4 0.</dl>
<dt><code>GotoDesk</code> [prev | <i>arg1</i>&nbsp;<wbr>[<i>arg2</i>]&nbsp;<wbr>[<i>min</i>&nbsp;<wbr><i>max</i>]]</p>
<dd>
<dl>
<dt>
<dd> Switches the current viewport to another desktop (workspace, room). </p>
<p> The command takes 1, 2, 3, or 4 arguments. A single argument is interpreted as a relative desk number. Two arguments are understood as a relative and an absolute desk number. Three arguments specify a relative desk and the minimum and maximum of the allowable range. Four arguments specify the relative, absolute, minimum and maximum values. (Desktop numbers can be negative). If a literal <i>prev</i> is given as the single argument, the last visited desk number is used. </p>
<p> If <i>arg1</i> is non zero then the next desktop number is the current desktop number plus <i>arg1</i>. </p>
<p> If <i>arg1</i> is zero then the new desktop number is <i>arg2</i>. (If <i>arg2</i> is not present, then the command has no effect.) </p>
<p> If <i>min</i> and <i>max</i> are given, the new desktop number is no smaller than <i>min</i> and no bigger than <i>max</i>. Values out of this range are truncated (if you gave an absolute desk number) or wrapped around (if you gave a relative desk number). </p>
<p> The syntax is the same as for <code>MoveToDesk</code>, which moves a window to a different desktop. </p>
<p> The number of active desktops is determined dynamically. Only desktops which contain windows or are currently being displayed are active. Desktop numbers must be between 2147483647 and -2147483648 (is that enough?).</dl>
<dt><code>GotoDeskAndPage</code> prev | <i>desk</i>&nbsp;<wbr><i>xpage</i>&nbsp;<wbr><i>ypage</i></p>
<dd>
<dl>
<dt>
<dd> Switches the current viewport to another desktop and page, similar to the <code>GotoDesk</code> and <code>GotoPage</code> commands. The new desk is <i>desk</i> and the new page is (<i>xpage</i>,<i>ypage</i>).</dl>
<dt><code>GotoPage</code> prev | [<i>options</i>]&nbsp;<wbr><i>x</i>[p]&nbsp;<wbr><i>y</i>[p]</p>
<dd>
<dl>
<dt>
<dd> Moves the desktop viewport to page (x,y). The upper left page is (0,0), the upper right is (M,0), where M is one less than the current number of horizontal pages specified in the <code>DesktopSize</code> command. The lower left page is (0,N), and the lower right page is (M,N), where N is the desktop&#8217;s vertical size as specified in the <code>DesktopSize</code> command. To switch to a page relative to the current one add a trailing &#8216;<i>p</i>&#8216; after any or both numerical arguments. </p>
<p> Possible <i>options</i> are <i>wrapx</i> and <i>wrapy</i> to wrap around the x or y coordinate when the viewport is moved beyond the border of the desktop. </p>
<p> To go to the last visited page use <i>prev</i> as the first argument. The <code>GotoPage</code> function should not be used in a pop-up menu. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
# Go to page (2,3)
GotoPage 2 3
# Go to lowest and rightmost page
GotoPage -1 -1
# Go to last page visited
GotoPage prev
# Go two pages to the right and one page up
GotoPage +2p -1p
</pre>
</dl>
</dl>
<dt><code>Scroll</code> [<i>horizonal</i>[p]&nbsp;<wbr><i>vertical</i>[p] | reverse]</p>
<dd>
<dl>
<dt>
<dd> Scrolls the virtual desktop&#8217;s viewport by <i>horizontal</i> pages in the x-direction and <i>vertical</i> pages in the y-direction or starts interactive scrolling of the viewport. Either or both entries may be negative. Both <i>horizontal</i> and <i>vertical</i> values are expressed in percent of pages, so </p>
<dl>
<dt>
<dd>
<pre>
Scroll 100 100
</pre>
</dl>
<p> means to scroll down and right by one full page. </p>
<dl>
<dt>
<dd>
<pre>
Scroll 50 25
</pre>
</dl>
<p> means to scroll right half a page and down a quarter of a page. The <code>Scroll</code> function should not be called from pop-up menus. Normally, scrolling stops at the edge of the desktop. </p>
<p> If the <i>horizontal</i> and <i>vertical</i> percentages are 100 or more and are multiplied by 1000 then scrolling wraps around at the edge of the desktop. If </p>
<dl>
<dt>
<dd>
<pre>
Scroll 100000 0
</pre>
</dl>
<p> is executed over and over fvwm moves to the next desktop page on each execution and wraps around at the edge of the desktop, so that every page is hit in turn. </p>
<p> If the letter &#8216;<i>p</i>&#8216; is appended to each coordinate (<i>horizontal</i> and/or <i>vertical</i>), then the scroll amount is measured in pixels. </p>
<p> Without arguments or if the option <i>reverse</i> is given interactive scrolling takes place. The viewport scrolls as the mouse is moved. With the <i>reverse</i> option scrolling is done in opposite direction of the mouse movement, and without it scrolling in the same direction as the mouse. </p>
<p> The binding </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 A CM Scroll reverse
</pre>
</dl>
<p> gives an effect of grabbing and dragging the viewport with button 1 if <font SIZE="-1">Control</font> and <font SIZE="-1">Meta</font> is pressed.</dl>
<dt><code>Xinerama</code> [bool]</p>
<dd>
<dl>
<dt>
<dd> Enables Xinerama support if the boolean argument is true and disables it if the argument is false. Calling this command without arguments turns on Xinerama support if it was disabled before and turns it off if it was enabled. For example: </p>
<dl>
<dt>
<dd>
<pre>
# Turn Xinerama support on, use primary screen 2
<code>XineramaPrimaryScreen</code> 2
Xinerama on
# Turn it off again
Xinerama off
</pre>
</dl>
</dl>
<dt><code>XineramaPrimaryScreen</code> [primary-screen]</p>
<dd>
<dl>
<dt>
<dd> Takes an integer number or &#8216;g&#8217; or &#8216;c&#8217; as its argument. A number is taken as the number of the Xinerama screen that is to be used as the primary screen. The primary screen can be used as the preferred screen to place windows with </p>
<dl>
<dt>
<dd>
<pre>
XineramaPrimaryScreen &lt;screen number&gt;
<code>Style</code> * StartsOnScreen p
</pre>
</dl>
<p> The primary screen is used in some of the modules and for the default icon box too. Any number that is zero or more is taken as the primary screen&#8217;s number. Instead, the letter &#8216;c&#8217; indicates to use the current screen (containing the pointer) whenever the primary screen is used. This may be very confusing under some circumstances. With &#8216;g&#8217;, the global screen is used as the primary screen, effectively disabling the primary screen. Calling this function with any other argument (including none) resets the primary screen to 0.</dl>
<dt><code>XineramaSls</code> [bool]</p>
<dd>
<dl>
<dt>
<dd> For multi-screen implementations other than Xinerama, such as Single Logical Screen, it is possible to simulate a Xinerama configuration if the total screen seen by fvwm is made up of equal sized monitors in a rectangular grid. The <code>XineramaSls</code> command turns SLS support on or off or toggles it to the opposite state, depending on if the boolean argument is &quot;True&quot;, &quot;False&quot; or &quot;toggle&quot;. If no argument is given, this is treated like &quot;toggle&quot;. The default layout uses one by one screens. To configure the layout, use the <code>XineramaSlsSize</code> or <code>XineramaSlsScreens</code> command.</dl>
<dt><code>XineramaSlsSize</code> <i>Horizontal</i> <i>Vertical</i></p>
<dd>
<dl>
<dt>
<dd> This command configures the layout of the Single Logical screen feature. It takes two arguments, <i>Horizontal</i> and <i>Vertical</i> which must be an integer value dividing evenly into the total desktop width, and height. For an example with two monitors side by side which appear as one screen through the X-Server with the right screen as the primary screen, use: </p>
<dl>
<dt>
<dd>
<pre>
XineramaSlsSize 2x1
<code>XineramaSls</code> On
<code>XineramaPrimaryScreen</code> 1
<code>Xinerama</code> On
</pre>
</dl>
</dl>
<dt><code>XineramaSlsScreens</code> number-of-screens [<i>screen-spec</i> &#8230;]</p>
<dd>
<dl>
<dt>
<dd> This command configures the layout of the Single Logical screen feature. Its first argument is the number of screens to use. It must be followed by exactly this number of <i>screen-spec</i> arguments. Each of these can be written either in standard X geometry format: &quot;&lt;width&gt;x&lt;height&gt;+&lt;x&gt;+&lt;y&gt;&quot; or as a space separated list of numbers: &quot;x y width height&quot;. Both ways of describing screens can be mixed in a single command. All four numbers must be supplied. The <i>x</i> and <i>y</i> values specify the origin of the screen in relation to the global screen&#8217;s origin while <i>width</i> and <i>height</i> specify the size of the screen in pixels. No checks are done if the geometries make sense, so it is possible to define overlapping screens (with random results) or screens that are not visible at all. </p>
<dl>
<dt>
<dd>
<pre>
XineramaSlsScreens 3 \
  512x768+0+0 512x300+512+0 512 300 512 468
<code>XineramaSls</code> On
<code>XineramaPrimaryScreen</code> 1
<code>Xinerama</code> On
</pre>
</dl>
</dl>
</dl>
<h3>User Functions and Shell Commands</h3>
<dl>
<dt><code>AddToFunc</code> [<i>name</i>&nbsp;<wbr>[I | M | C | H | D&nbsp;<wbr><i>action</i>]]</p>
<dd>
<dl>
<dt>
<dd> Begins or adds to a function definition. Here is an example: </p>
<dl>
<dt>
<dd>
<pre>
AddToFunc Move-or-Raise I <code>Raise</code>
 + M <code>Move</code>
 + D <code>Lower</code>
</pre>
</dl>
<p> The function name is &quot;Move-or-Raise&quot;, and it could be invoked from a menu or a mouse binding or key binding: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 TS A Move-or-Raise
</pre>
</dl>
<p> The <i>name</i> must not contain embedded whitespace. No guarantees are made whether function names with embedded whitespace work or not. This behavior may also change in the future without further notice. The letter before the <i>action</i> tells what kind of action triggers the command which follows it. &#8216;<i>I</i>&#8216; stands for &quot;Immediate&quot;, and is executed as soon as the function is invoked. &#8216;<i>M</i>&#8216; stands for &quot;Motion&quot;, i.e. if the user starts moving the mouse. &#8216;<i>C</i>&#8216; stands for &quot;Click&quot;, i.e., if the user presses and releases the mouse button. &#8216;<i>H</i>&#8216; stands for &quot;Hold&quot;, i.e. if the user presses a mouse button and holds it down for more than <code>ClickTime</code> milliseconds. &#8216;<i>D</i>&#8216; stands for &quot;Double-click&quot;. The action &#8216;<i>I</i>&#8216; causes an action to be performed on the button-press, if the function is invoked with prior knowledge of which window to act on. </p>
<p> There is a number of predefined symbols that are replaced by certain values if they appear on the command line. Please refer to the <code>Command Expansion</code> section for details. </p>
<p> <code>Warning</code> Please read the comments on executing complex functions in the section <code>Scripting and Complex Functions</code>. </p>
<p> Examples: </p>
<p> If you call </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> F10 R A <code>Function</code> MailFunction xmh &quot;-font fixed&quot;
</pre>
</dl>
<p> and &quot;MailFunction&quot; is </p>
<dl>
<dt>
<dd>
<pre>
AddToFunc MailFunction
 + I <code>Next</code> ($0) <code>Iconify</code> off
 + I <code>Next</code> (AcceptsFocus, $0) <code>Focus</code>
 + I <code>None</code> ($0) <code>Exec</code> exec $0 $1
</pre>
</dl>
<p> Then the last line of the function becomes </p>
<dl>
<dt>
<dd>
<pre>
 + I <code>None</code> (xmh) <code>Exec</code> exec xmh -font fixed
</pre>
</dl>
<p> The expansion is performed as the function is executed, so you can use the same function with all sorts of different arguments. You could use </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> F11 R A <code>Function</code> MailFunction zmail &quot;-bg pink&quot;
</pre>
</dl>
<p> in the same <i>config</i>, if you wanted. An example of using &quot;$[w.id]&quot; is: </p>
<dl>
<dt>
<dd>
<pre>
AddToFunc PrintFunction
 + I <code>Raise</code>
 + I <code>Exec</code> xdpr -id $[w.id]
</pre>
</dl>
<p> Note that &quot;$$&quot; is expanded to &#8216;$&#8217;. </p>
<p> Another example: bind right mouse button within the window button number 6 (this is a minimize button for the win95 theme) to iconify all windows of the same resource: </p>
<dl>
<dt>
<dd>
<pre>
AddToFunc FuncIconifySameResource &quot;I&quot; <code>All</code> ($0) <code>Iconify</code> on
<code>Mouse</code> 3 6 A FuncIconifySameResource $[w.resource]
</pre>
</dl>
</dl>
<dt><code>Beep</code></p>
<dd>
<dl>
<dt>
<dd> As might be expected, this makes the terminal beep.</dl>
<dt><code>DestroyFunc</code> <i>function</i></p>
<dd>
<dl>
<dt>
<dd> Deletes a function, so that subsequent references to it are no longer valid. You can use this to change the contents of a function during a fvwm session. The function can be rebuilt using <code>AddToFunc</code>. </p>
<dl>
<dt>
<dd>
<pre>
DestroyFunc PrintFunction
</pre>
</dl>
</dl>
<dt><code>Echo</code> <i>string</i></p>
<dd>
<dl>
<dt>
<dd> Prints a message to <i>stderr</i>. Potentially useful for debugging things in your <i>config</i>. </p>
<dl>
<dt>
<dd>
<pre>
Echo Beginning style definitions...
</pre>
</dl>
</dl>
<dt><code>EchoFuncDefinition</code> <i>function</i></p>
<dd>
<dl>
<dt>
<dd> The <code>EchoFuncDefinition</code> is similar to the <code>Echo</code> command but prints the definition for the given <i>function</i> to <i>stderr</i>. It is useful to find out how fvwm handles quoting and for debugging functions .</dl>
<dt><code>Exec</code> <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Executes <i>command</i>. You should not use an ampersand &#8216;&amp;&#8217; at the end of the command. You probably want to use an additional &quot;exec&quot; at the beginning of <i>command</i>. Without that, the shell that fvwm invokes to run your command stays until the command exits. In effect, you&#8217;ll have twice as many processes running as you need. Note that some shells are smart enough to avoid this, but it never hurts to include the &quot;exec&quot; anyway. </p>
<p> The following example binds function key <font SIZE="-1">F1</font> in the root window, with no modifiers, to the exec function. The program rxvt is started with an assortment of options. </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> F1 R N Exec exec rxvt -fg yellow -bg blue \
  -e /bin/tcsh
</pre>
</dl>
<p> Note that this function doesn&#8217;t wait for <i>command</i> to complete, so things like: </p>
<dl>
<dt>
<dd>
<pre>
Exec &quot;echo <code>AddToMenu</code> ... &gt; /tmp/file&quot;
<code>Read</code> /tmp/file
</pre>
</dl>
<p> do not work reliably (see the <code>PipeRead</code> command).</dl>
<dt><code>ExecUseShell</code> [<i>shell</i>]</p>
<dd>
<dl>
<dt>
<dd> Makes the <code>Exec</code> command use the specified shell, or the value of the <i>$SHELL</i> environment variable if no shell is specified, instead of the default Bourne shell (<i>/bin/sh</i>). </p>
<dl>
<dt>
<dd>
<pre>
ExecUseShell
ExecUseShell /usr/local/bin/tcsh
</pre>
</dl>
</dl>
<dt><code>Function</code> <i>FunctionName</i></p>
<dd>
<dl>
<dt>
<dd> Used to bind a previously defined function to a key or mouse button. The following example binds mouse button 1 to a function called &quot;Move-or-Raise&quot;, whose definition was provided as an example earlier in this man page. After performing this binding fvwm executes the &quot;move-or-raise&quot; function whenever button 1 is pressed in a window&#8217;s title-bar. </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code> 1 T A Function Move-or-Raise
</pre>
</dl>
<p> The keyword <code>Function</code> may be omitted if <i>FunctionName</i> does not coincide with an fvwm command. </p>
<p> Warning: Please read the comments on executing complex functions in the section <code>Scripting and Complex Functions</code>.</dl>
<dt><code>InfoStoreAdd</code> <i>key</i> <i>value</i></p>
<dd>
<dl>
<dt>
<dd> Stores the <i>value</i> at the given <i>key</i>. This is useful to store generic information used in the lifetime of an fvwm config file. For example storing program preferences for opening video files. </p>
<p> The purpose of this command is to store internal information to fvwm which can be used bu fvwm functions, or when opening programs of a certain type. Previous to this command the only way to do this was via <code>SetEnv</code> but this is discouraged because it places such information in the environment, which pollutes it and makes the information global to other processes started by fvwm which may then modify them which might not be what&#8217;s wanted. Hence the point of <code>InfoStoreAdd</code> is to still allow for such information to be stored, but kept internal to fvwm. </p>
<p> In this way, one can build up as many key/value pairs as needed. Recalling the value of a given key happens through fvwm&#8217;s usual expansion mechanism. See the <code>Command Expansion</code> section for more details. For example: </p>
<dl>
<dt>
<dd>
<pre>
    InfoStoreAdd teddybearprog xteddy
    # Echo the value of teddybearprog
    Echo $[infostore.teddybearprog]
</pre>
</dl>
<p> Removing an entry from the InfoStore is done with the <code>InfoStoreRemove</code> command.</dl>
<dt><code>InfoStoreRemove</code> <i>key</i></p>
<dd>
<dl>
<dt>
<dd> Removes an entry at the given <i>key</i> from the InfoStore. Example: </p>
<dl>
<dt>
<dd>
<pre>
InfoStoreRemove teddybearprog
</pre>
</dl>
</dl>
<dt><code>Nop</code></p>
<dd>
<dl>
<dt>
<dd> Does nothing. This is used to insert a blank line or separator in a menu. If the menu item specification is </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToMenu</code> MyMenu &quot; &quot; Nop
</pre>
</dl>
<p> then a blank line is inserted. If it looks like </p>
<dl>
<dt>
<dd>
<pre>
+ &quot;&quot; Nop
</pre>
</dl>
<p> then a separator line is inserted. Can also be used as the double-click action for <code>Menu</code> or <code>Popup</code>.</dl>
<dt><code>PipeRead</code> <i>command</i> [quiet]</p>
<dd>
<dl>
<dt>
<dd> Causes fvwm to read commands from the output of the <i>command</i>. This <i>command</i> is executed by <i>/bin/sh</i> as if you typed it on the command line. If the command consists of more than one word it must be quoted. Useful for building up dynamic menu entries based on a directories contents, for example. If the keyword <i>Quiet</i> follows the command no message is produced if the <i>command</i> is not found. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToMenu</code> HomeDirMenu
PipeRead 'for i in $HOME/*; \
  do echo &quot;+ $i <code>Exec</code> xterm -e vi $i&quot;; done'
</pre>
</dl>
<p> Note: The <code>PipeRead</code> changes the pointer to a watch cursor by default during execution. However, some commands, for example xwd, need to take control of the pointer themselves and do not work. To disable the watch cursor, use the command prior to <code>PipeRead</code> </p>
<dl>
<dt>
<dd>
<pre>
<code>BusyCursor</code> <i>Read</i> off
</pre>
</dl>
<p> The <code>PipeRead</code> command executes synchronously. If you want to <code>Exec</code> something, but need the command to run synchronously, you might do something like: </p>
<dl>
<dt>
<dd>
<pre>
PipeRead 'command 1&gt;&amp;2'
</pre>
</dl>
<p> The redirection causes any output from the program to go to stderr instead of being read as a sequence of commands by fvwm. <code>PipeRead</code> returns 1 if the given command could be executed or -1 if not (see the section <code>Conditional Commands</code> for the meaning of return codes).</dl>
<dt><code>Read</code> <i>filename</i> [quiet]</p>
<dd>
<dl>
<dt>
<dd> Causes fvwm to read commands from the file named <i>filename</i>. If the keyword <i>Quiet</i> follows the command no message is produced if the file is not found. If the file name does not begin with a slash (&#8216;/&#8217;), fvwm looks in the user&#8217;s data directory, then the system data directory. The user&#8217;s data directory is by default <i>$HOME</i><i>/.fvwm</i>. It can be overridden by exporting <i>FVWM_USERDIR</i> set to any other directory. The <code>Read</code> command returns 1 if the given file could be read or -1 if not (see the section <code>Conditional Commands</code> for the meaning of return codes).</dl>
<dt><code>SetEnv</code> <i>variable</i> <i>value</i></p>
<dd>
<dl>
<dt>
<dd> Set an environment variable to a new value, similar to the shell&#8217;s export or setenv command. The <i>variable</i> and its <i>value</i> are inherited by processes started directly by fvwm. This can be especially useful in conjunction with the <code>FvwmM4</code> module. For example: </p>
<dl>
<dt>
<dd>
<pre>
SetEnv height HEIGHT
</pre>
</dl>
<p> makes the <code>FvwmM4</code> set variable <i>HEIGHT</i> usable by processes started by fvwm as the environment variable <i>$height</i>. If <i>value</i> includes whitespace, you should enclose it in quotes. If no <i>value</i> is given, the variable is deleted.</dl>
<dt><code>Silent</code> <i>command</i></p>
<dd>
<dl>
<dt>
<dd> A number of commands require a window to operate on. If no window was selected when such a function is invoked the user is asked to select a window. Sometimes this behavior is unwanted, for example if the function was called by a module and the window that was selected at first does not exist anymore. You can prevent this by putting <code>Silent</code> in front of the fvwm <i>command</i>. If a function that needs a window is called with <code>Silent</code> without a window selected, it simply returns without doing anything. If <code>Silent</code> is used on a user defined function it affects all function and sub function calls until the original function exits. </p>
<p> Another usage of <code>Silent</code> is with binding commands <code>Key</code>, <code>PointerKey</code> and <code>Mouse</code>, this disables error messages. </p>
<p> <code>Silent</code> also disables the error message for non-existent commands. Note: This command is treated as a prefix to its <i>command</i>. Expansion of the command line is done as if <code>Silent</code> was not there. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
Silent <code>Move</code> 0 0
Silent User_defined_function
# do not complain on keyboards without &quot;Help&quot; key
Silent <code>Key</code> Help R A <code>Popup</code> HelpMenu
</pre>
</dl>
</dl>
<dt><code>UnsetEnv</code> [<i>variable</i>]</p>
<dd>
<dl>
<dt>
<dd> Unset an environment variable, similar to shell&#8217;s export or unsetenv command. The <i>variable</i> then is removed from the environment array inherited by processes started directly by fvwm.</dl>
<dt><code>Wait</code> <i>window</i></p>
<dd>
<dl>
<dt>
<dd> This command is intended to be used in fvwm functions only. It causes execution of a function to pause until a new window matching <i>window</i> appears. This can be a window&#8217;s name, class, or resource string. It may contain the wildcards &#8216;*&#8217; and &#8216;?&#8217;, which are matched in the usual Unix filename manner. This is particularly useful in the &quot;InitFunction&quot; if you are trying to start windows on specific desktops: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> InitFunction
 + I <code>Exec</code> exec xterm -geometry 80x64+0+0
 + I Wait xterm
 + I <code>GotoDesk</code> 0 2
 + I <code>Exec</code> exec xmh -font fixed -geometry \
       507x750+0+0
 + I Wait xmh
 + I <code>GotoDesk</code> 0 0
</pre>
</dl>
<p> The above function starts an xterm on the current desk, waits for it to map itself, then switches to desk 2 and starts an xmh. After the xmh window appears control moves to desk 0. </p>
<p> Fvwm remains partially functional during a wait, but any input from the modules is queued up and processed only after the window appears or the command is aborted. For example, windows can not be focused with <code>FvwmTaskBar</code> or <code>FvwmWinList</code> during a wait. </p>
<p> You can escape from a <code>Wait</code> pause by pressing <font SIZE="-1">Ctrl-Alt-Escape</font> (where <font SIZE="-1">Alt</font> is the first modifier). To redefine this key sequence see the <code>EscapeFunc</code> command.</dl>
</dl>
<h3>Conditional Commands</h3>
<p> Conditional commands are commands that are only executed if certain conditions are met. Most conditional commands work on windows, like <code>Next</code>, <code>ThisWindow</code> or <code>All</code>. There is one conditional command, <code>Test</code>, that works on global conditions unrelated to windows. The syntax of the conditions is described below. For readability, the list of conditions is located at the end of this section.</p>
<dl>
<dt><code>Return Codes</code></p>
<dd>
<dl>
<dt>
<dd> All commands in this section (unless specifically stated for the command) also have a return code that can be 1 (if the condition was met) or 0 (if the condition was not met). Some commands may return -1 which means that an error occurred and the return code is useless. The <code>Break</code> command returns -2. Additionally, the return codes of commands run in a complex functions are passed to the invoking complex function. The return code is used by the <code>TestRc</code> command. Please refer to the commands&#8217; description for examples. The return code can also be accessed through the variable <i>$[cond.rc]</i>. Non conditional commands do not modify the return code of the last conditional command. Important note: return codes are only defined inside functions created with the <code>AddToFunc</code> command and are not inherited by sub functions. To run a command without altering the return code, the <code>KeepRc</code> command can be used.</dl>
<dt><code>The Ring of Windows</code></p>
<dd>
<dl>
<dt>
<dd> Fvwm stores windows in a ring internally. Think of the focused window as a cursor on the current position in the ring. The <code>Next</code> command and many other commands search forwards through the ring for a matching window, and <code>Prev</code> searches backwards. The windows in the ring are either ordered by creation time (if the <i>!FPSortWindowlistByFocus</i>, <i>NeverFocus</i> or <i>MouseFocus</i> styles are used) or by the last time they had the focus.</dl>
<dt><code>List of Conditional Commands</code></p>
<dd>
<dl>
<dt>
<dd> <code>All</code> [<i>options</i>] [(<i>conditions</i>)] <i>command</i></p>
<dl>
<dt>
<dd> Execute <i>command</i> on all windows meeting the conditions. It returns 1 if any window matches the condition and 0 otherwise. The execution starts at the top of the window ring and continues towards the bottom. The <i>options</i> can be any combination of <i>Reverse</i> and <i>UseStack</i>. If the option <i>Reverse</i> is given the execution order is reversed. The option <i>UseStack</i> makes All use the stacking order instead of the window ring when walking through windows. See the <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly.</dl>
<dl>
<dt><code>Any</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> if any window which satisfies all <i>conditions</i> exists. The command is run in the context of the root window. See the <code>Conditions</code> section for a list of conditions.</dl>
<dt><code>Break</code> [<i>levels</i>]</p>
<dd>
<dl>
<dt>
<dd> If the break command is used in a function, function execution is terminated immediately. Further commands of the function are not processed. Normally, all nested invocations of complex functions are left. An optional integer number <i>levels</i> may be given to break out of the given number of nested functions and continue execution of a higher level function. The <code>Break</code> command always has the return code -2. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> PickWindowRaiseAndDeiconify
+ I <code>Pick</code>
+ I <code>TestRc</code> (Error) Break
+ I <code>Raise</code>
+ I <code>Iconify</code> off
</pre>
</dl>
</dl>
<dt><code>Current</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> on the currently focused window if it satisfies all <i>conditions</i>. See the <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly.</dl>
<dt><code>Direction</code> [FromPointer] <i>direction</i> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> (typically <code>Focus</code>) on a window in the given direction which satisfies all <i>conditions</i>. Normally, the center of the currently focused window or the context window in which the command was invoked is taken as the starting point. Lacking such a window, or when the <i>FromPointer</i> option is given, the current position of the pointer is taken as the starting point. The <i>direction</i> may be one of &quot;North&quot;, &quot;Northeast&quot;, &quot;East&quot;, &quot;Southeast&quot;, &quot;South&quot;, &quot;Southwest&quot;, &quot;West&quot;, &quot;Northwest&quot; and &quot;Center&quot;. Which window <code>Direction</code> selects depends on angle and distance between the center points of the windows. Closer windows are considered a better match than those farther away. The <i>Center</i> direction simply selects the window closest to the starting point. Returns -1 if an invalid direction was given. See the <code>Conditions</code> section for a list of conditions.</dl>
<dt><code>KeepRc</code> <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Runs the <i>command</i> but does not alter the return code of the previous command. Note: <code>KeepRc</code> is treated as a prefix to its <i>command</i>. Expansion of the command line is done as if <code>KeepRc</code> was not there.</dl>
<dt><code>Next</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> (typically <code>Focus</code>) on the next window which satisfies all <i>conditions</i>. If the command is running in a window context, it starts looking for a matching window from there. Otherwise it starts at the focused window. See <code>Conditions</code> section for a list of conditions.</dl>
<dt><code>None</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> if no window which satisfies all <i>conditions</i> exists. The command is run in the context of the root window. Returns 1 if no window matches the conditions and 0 otherwise. See <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly.</dl>
<dt><code>NoWindow</code> <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i>, but removes the window context if any. This is not really a conditional command, but a prefix that may be useful in menu items that should operate without a window even if such menu is bound to window decorations.</dl>
<dt><code>Pick</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> <code>Pick</code> works like <code>Function</code> if invoked in the context of a window. If invoked in the root window, it first asks the user to pick a window and then executes the <i>command</i> in the context of that window. This avoids annoying multiple selections with complex functions. The command is executed only if the given <i>conditions</i> are met. Returns -1 if no window was selected. See <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly.</dl>
<dt><code>PointerWindow</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> if the window under the pointer satisfies all <i>conditions</i>. Returns -1 if there is no window under the pointer. See <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly.</dl>
<dt><code>Prev</code> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> (typically <code>Focus</code>) on the previous window which satisfies all <i>conditions</i>. If the command is running in a window context, it starts looking for a matching window from there. Otherwise it starts at the focused window. See <code>Conditions</code> section for a list of conditions.</dl>
<dt><code>ScanForWindow</code> [FromPointer] <i>dir1</i> <i>dir2</i> [(<i>conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> (typically <code>Focus</code>) on a window in the given direction which satisfies all <i>conditions</i>. Normally, the center of the currently focused window or the context window in which the command was invoked is taken as the starting point. Lacking such a window, or when the <i>FromPointer</i> option is given, the current position of the pointer is taken as the starting point. The direction <i>dir1</i> may be one of &quot;North&quot;, &quot;NorthEast&quot;, &quot;East&quot;, &quot;SouthEast&quot;, &quot;South&quot;, &quot;SouthWest&quot;, &quot;West&quot;, and &quot;NorthWest&quot;. Which window <code>ScanForWindow</code> selects depends first on the position along the primary axis given by <i>dir1</i>. If any windows have the exact same coordinate along the primary axis, the secondary direction is used to order the windows. The direction <i>dir2</i> may be one of the same set of values as <i>dir1</i>. If <i>dir2</i> is not perfectly perpendicular to <i>dir1</i>, ScanForWindow returns a failure. When using ScanForWindow repeatedly with the same arguments, it is guaranteed that all windows matching the conditions will eventually be found. If the focus reaches a limit along the primary axis, it will wrap around to the opposite side. Returns -1 if an invalid direction was given. See <code>Conditions</code> section for a list of conditions.</dl>
<dt><code>Test</code> [(<i>test-conditions</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> if all <i>test-conditions</i> are satisfied. The <i>test-conditions</i> are keywords with possible arguments from the list below and are separated by commas or whitespace. They include: <i>Version operator x.y.z</i>, <i>EnvIsSet varname</i>, <i>EnvMatch varname pattern</i>, <i>EdgeHasPointer direction</i>, <i>EdgeIsActive direction</i>, <i>Start</i>, <i>Init</i>, <i>Restart</i>, <i>Exit</i>, <i>Quit</i>, <i>ToRestart</i>, <i>True</i>, <i>False</i>, <i>F</i>, <i>R</i>, <i>W</i>, <i>X</i> and <i>I</i>. A test-condition prefixed with &quot;!&quot; is negated. </p>
<p> The <i>Version</i> <i>operator x.y.z</i> test-condition is fulfilled if the logical condition of the expression is true. Valid <i>operator</i> values are: <i>&gt;=</i>, <i>&gt;</i>, <i>&lt;=</i>, <i>&lt;</i>, <i>==</i> and <i>!=</i>. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
Test (Version &gt;= 2.5.11) <code>Echo</code> 2.5.11 or later.
</pre>
</dl>
<p> The <i>EnvIsSet</i> <i>varname</i> test-condition is true if the given environment variable is set. The <i>EnvMatch</i> <i>varname pattern</i> test-condition is true if <i>pattern</i> matches the given environment or infostore variable value. (See <code>InfoStoreAdd</code>). The pattern may contain special &quot;*&quot; and &quot;?&quot; chars. The &quot;varname&quot; is coded without the leading dollar sign ($). </p>
<p> The <i>EdgeHasPointer</i> [<i>direction</i>] test-condition is true if the edge in the given direction currently contains the pointer. The <i>EdgeIsActive</i> [<i>direction</i>] test-condition is true if the edge in the given direction currently is active. An edge is active, and can contain a pointer if either a command is bound to it or edge scroll is available in that direction. The direction may be one of <i> Any</i>,<i> North</i>,<i> Top</i>,<i> Up</i>,<i> West</i>,<i> Left</i>,<i> South</i>,<i> Bottom</i>, <i> Down</i>,<i> Right</i> and <i> East</i>. If no direction is specified <i>Any</i> is assumed. </p>
<p> The <i>Start</i> test-condition is the same as either <i>Init</i> or <i>Restart</i>. It is only true on startup or restart prior and during <code>StartFunction</code> execution. The <i>Exit</i> test-condition is the same as either <i>Quit</i> or <i>ToRestart</i>. It is only valid on shutdown during <code>ExitFunction</code> function execution. </p>
<p> The <i>True</i> and <i>False</i> test-conditions are unconditionally true and false. </p>
<p> Additionally, if a test-condition name is not recognized, the Error return code is set and the command is not executed. </p>
<p> The <i>F</i> <i>file</i>, <i>R</i> <i>file</i>, <i>W</i> <i>file</i>, <i>X</i> <i>file</i> and <i>I</i> <i>file</i> test-conditions test for existence of the given [F]ile (possibly with [R]ead/[W]rite permissions), e[X]ecutable (in <i>$PATH</i>), or the [I]mage (in ImagePath). </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> StartFunction I Test (Init) <code>Exec</code> exec xterm
<code>AddToFunc</code> VerifyVersion
+ I Test (Version 2.5.*) <code>Echo</code> 2.5.x detected
+ I <code>TestRc</code> (NoMatch) \
        Test (!Version 2.6.*) <code>Echo</code> Future version
+ I <code>TestRc</code> (NoMatch) \
        <code>Echo</code> 2.6.x is detected
Test (F $[FVWM_USERDIR]/local-config) <code>Read</code> local-config
Test (X xterm-utf16) <code>Exec</code> exec xterm-utf16
</pre>
</dl>
</dl>
<dt><code>TestRc</code> [([!]<i>returncode</i>)] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> Performs <i>command</i> if the last conditional command returned the value <i>returncode</i>. Instead of the numeric values 0 (no match), 1 (match), -1 (error), and -2 (break) the symbolic names &quot;<i>NoMatch</i>&quot;, &quot;<i>Match</i>&quot;, &quot;<i>Error</i>&quot; and &quot;<i>Break</i>&quot; can be used. If no <i>returncode</i> is given, the default 0 is assumed. If the return code is prefixed with &#8216;!&#8217;, the command is executed if <i>returncode</i> does not match the value returned by the conditional command. The <code>TestRc</code> command can only be used inside functions. If the <i>command</i> is another conditional command, the previous return code is replaced by the new one. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>AddToFunc</code> ToggleXterm
+ I <code>All</code> (my_xtermwindow) <code>Close</code>
+ I TestRc (NoMatch) <code>Exec</code> xterm -T my_xtermwindow
</pre>
</dl>
</dl>
<dt><code>ThisWindow</code> [(<i>conditions</i>)] command</p>
<dd>
<dl>
<dt>
<dd> <code>ThisWindow</code> executes the specified <i>command</i> in the context of the current operand window. If there is no operand window (it is invoked in the root window), the command is ignored. <code>ThisWindow</code> is never interactive. The command is executed only if the given <i>conditions</i> are met. It returns -1 if used outside a window context. See <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying &quot;!CirculateHit&quot; etc. explicitly.</dl>
<dt><code>WindowId</code> [<i>id</i>]&nbsp;<wbr>[(<i>conditions</i>)] | [root&nbsp;<wbr>[<i>screen</i>]] <i>command</i></p>
<dd>
<dl>
<dt>
<dd> The <code>WindowId</code> command looks for a specific window <i>id</i> and runs the specified <i>command</i> on it. The second form of syntax retrieves the window id of the root window of the given <i>screen</i>. If no <i>screen</i> is given, the current screen is assumed. The window indicated by <i>id</i> may belong to a window not managed by fvwm or even a window on a different screen. Although most commands can not operate on such windows, there are some exceptions, for example the <code>WarpToWindow</code> command. Returns -1 if no window with the given id exists. See <code>Conditions</code> section for a list of conditions. </p>
<p> This command implies the conditions <i>CirculateHit</i>, <i>CirculateHitIcon</i> and <i>CirculateHitShaded</i>. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
WindowId 0x34567890 <code>Raise</code>
WindowId root 1 <code>WarpToWindow</code> 50 50
WindowId $0 (Silly_Popup) <code>Delete</code>
</pre>
</dl>
<p> In the past this command was mostly useful for functions used with the <code>WindowList</code> command, or for selective processing of <code>FvwmEvent</code> calls (as in the last example), but currently these handler functions are called within a window context, so this command is not really needed in these cases. Still it may be useful if, for example, the window id should be stored in the environment variable for a further proceeding. </p>
<dl>
<dt>
<dd>
Pick SetEnv BOOKMARKED_WINDOW $[w.id] WindowId $[BOOKMARKED_WINDOW] WarpToWindow
</dl>
</dl>
</dl>
</dl>
<dt><code>Conditions</code></p>
<dd>
<dl>
<dt>
<dd> The <i>conditions</i> that may be given as an argument to any conditional command are a list of keywords separated by commas, enclosed in parentheses. Unless stated otherwise, conditional commands accept all the conditions listed below. Note that earlier versions of fvwm required the conditions to be separated by whitespace instead of commas and enclosed in brackets instead of parentheses (this is still supported for backward compatibility). </p>
<p> In addition, the <i>conditions</i> may include one or more window names to match to. If more than one window name is given, all of them must match. The window name, icon name, class, and resource are considered when attempting to find a match. Each name may include the wildcards &#8216;*&#8217; and &#8216;?&#8217;, and may consist of two or more alternatives, separated by the character &#8216;|&#8217;, which acts as an OR operator. (If OR operators are used, they must not be separated by spaces from the names.) Each window name can begin with &#8216;!&#8217;, which prevents <i>command</i> if any of the window name, icon name, class or resource match. However, &#8216;!&#8217; must not be applied to individual names in a group separated by OR operators; it may only be applied to the beginning of the group, and then it operates on the whole group. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>Next</code> (&quot;Netscape|konqueror|Mozilla*&quot;) <code>WarpToWindow</code> 99 90
</pre>
</dl>
<p> This goes to the next web browser window, no matter which of the three named web browsers is being used. </p>
<dl>
<dt>
<dd>
<pre>
<code>Next</code> (&quot;Mozilla*&quot;, &quot;Bookmark*&quot;) <code>WarpToWindow</code> 99 90
</pre>
</dl>
<p> This goes to Mozilla&#8217;s bookmark manager window, ignoring other Mozilla windows and other browsers&#8217; bookmark windows. </p>
<dl>
<dt>
<dd>
<pre>
<code>All</code> (&quot;XTerm|rxvt&quot;, !console) <code>Iconify</code>
</pre>
</dl>
<p> This iconifies all the xterm and rxvt windows on the current page, except that the one named &quot;console&quot; (with the -name option to xterm) is excluded. </p>
<dl>
<dt>
<dd>
<pre>
<code>Next</code> (!&quot;<code>FvwmPager</code>|<code>FvwmForm</code>*|<code>FvwmButtons</code>&quot;) <code>Raise</code>
<code>Next</code> (!<code>FvwmPager</code>, !<code>FvwmForm</code>*, !<code>FvwmButtons</code>) <code>Raise</code>
</pre>
</dl>
<p> These two commands are equivalent; either one raises the next window which is not one of the named fvwm modules. </p>
<p> Any condition can be negated by using a an exclamation mark (&#8216;!&#8217;) directly in front of its name. </p>
<p> <i>AcceptsFocus</i>, <i>AnyScreen</i>, <i>CirculateHit</i>, <i>CirculateHitIcon</i>, <i>CirculateHitShaded</i>, <i>Closable</i>, <i>CurrentDesk</i>, <i>CurrentGlobalPage</i>, <i>CurrentGlobalPageAnyDesk</i>, <i>CurrentPage</i>, <i>CurrentPageAnyDesk</i>, <i>CurrentScreen</i>, <i>FixedPosition</i>, <i>FixedSize</i>, <i>Focused</i>, <i>HasHandles</i>, <i>HasPointer</i>, <i>Iconic</i>, <i>Iconifiable</i>, <i>Layer [n]</i>, <i>Maximizable</i>, <i>Maximized</i>, <i>Overlapped</i>, <i>PlacedByButton n</i>, <i>PlacedByButton3</i>, <i>PlacedByFvwm</i>, <i>Raised</i>, <i>Shaded</i>, <i>State n</i>, <i>Sticky</i>, <i>StickyAcrossDesks</i>, <i>StickyAcrossPages</i>, <i>StickyIcon</i>, <i>StickyAcrossDesksIcon</i>, <i>StickyAcrossPagesIcon</i>, <i>Transient</i>, <i>Visible</i>. </p>
<p> The <i>AcceptsFocus</i> condition excludes all windows that do not want the input focus (the application has set the &quot;Input hints&quot; for the window to False) and do not use the <i>Lenience</i> option of the <code>Style</code> command. Also, all windows using the <i>NeverFocus</i> style are ignored. Note: <i>!Lenience</i> is equivalent to the deprecated option <i>NoLenience</i>. </p>
<p> With the <i>AnyScreen</i> condition used together with any of the <i>Current&#8230;</i> conditions, windows that do not intersect the Xinerama screen containing the mouse pointer are considered for a match too. For example: </p>
<dl>
<dt>
<dd>
<pre>
# Focus next window on current page,
# regardless of Xinerama screen
<code>Next</code> (CurrentPage, AnyScreen) <code>Focus</code>
</pre>
</dl>
<p> The <i>CirculateHit</i> and <i>CirculateHitIcon</i> options override the <i>CirculateSkip</i> and <i>CirculateSkipIcon</i> <code>Style</code> attributes for normal or iconic windows. The <i>CirculateHitShaded</i> option overrides the <i>CirculateSkipShaded</i> <code>Style.</code> All three options are turned on by default for the <code>Current</code> command. They can be turned off by specifying <i>!CirculateHit</i> etc. explicitly. Note: Do not confuse these conditions with the style options of the same name. Specifically, </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> foo CirculateSkip
<code>Next</code> (foo, CirculateHit) ...
</pre>
</dl>
<p> is not the same as </p>
<dl>
<dt>
<dd>
<pre>
<code>Style</code> foo CirculateHit ...
<code>Next</code> (foo)
</pre>
</dl>
<p> The prior selects windows with the name foo only in the Next command. In the second example, these windows are always matched in all conditional commands. </p>
<p> The <i>Closable</i> condition matches only windows that are allowed to be closed. </p>
<p> The <i>CurrentDesk</i> condition matches only windows that are on the current desk. </p>
<p> The <i>CurrentGlobalPage</i> condition matches only windows that are on the current page of the current desk, regardless of whether Xinerama support is enabled or not. This condition implicitly activates the <i>CurrentDesk</i> condition. </p>
<p> The <i>CurrentGlobalPageAnyDesk</i> condition matches only windows that are on the current page of any desk, regardless of whether Xinerama support is enabled or not. </p>
<p> The <i>CurrentPage</i> condition matches only windows that are on the current page of the current desk. If Xinerama support is enabled, it only matches windows that are at least partially on the Xinerama screen containing the mouse pointer. This condition implicitly activates the <i>CurrentDesk</i> condition. </p>
<p> The <i>CurrentPageAnyDesk</i> and <i>CurrentScreen</i> conditions matches only windows that are on the current page of any desk. If Xinerama support is enabled, they only match windows that are at least partially on the Xinerama screen containing the mouse pointer. </p>
<p> The <i>FixedPosition</i> condition excludes all windows that do not have a fixed position, either set through WM hints or the <code>Style</code> option <i>FixedPosition</i>. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyFunc</code> ToggleFixedGeometry
<code>AddToFunc</code>   ToggleFixedGeometry
+ I <code>Pick</code> (FixedPosition) \
        <code>WindowStyle</code> VariablePosition, VariableSize
+ I <code>TestRc</code> (NoMatch) <code>WindowStyle</code> FixedPosition, FixedSize
</pre>
</dl>
<p> The <i>FixedSize</i> condition excludes all windows that do not have a fixed size, either set through WM hints or the <code>Style</code> option <i>FixedSize</i>. </p>
<p> The <i>Focused</i> matches on the window that currently has the keyboard focus. This is not useful for the <code>Current</code> command but can be used with the other conditional commands. </p>
<p> The <i>HasHandles</i> condition excludes all windows that do not have resize handles. </p>
<p> The <i>HasPointer</i> condition excludes all windows that do not contain the pointer. </p>
<p> The <i>Iconic</i> condition matches only iconic windows. </p>
<p> The <i>Iconifiable</i> condition matches only windows that are allowed to be iconified. </p>
<p> The <i>Layer [n]</i> condition matches only windows on the specified layer. The optional argument of the <i>Layer</i> condition defaults to the layer of the focused window. The negation <i>!Layer</i> switches off the <i>Layer</i> condition. </p>
<p> The <i>Maximizable</i> condition matches only windows that are allowed to be maximized. </p>
<p> The <i>Maximized</i> condition matches only maximized windows. </p>
<p> The <i>Overlapped</i> condition matches only windows that are overlapped by other windows on the same layer (or unmanaged windows if the option <i>RaiseOverUnmanaged</i> of the <code>BugOpts</code> command is used). Note that this condition can be slow if you have many windows or if RaiseOverUnmanaged is used and the connection to the X server is slow. </p>
<p> The <i>PlacedByButton n</i> condition is fulfilled if the last interactive motion of the window (with the <code>Move</code> command or as <i>ManualPlacement</i>) was ended by pressing mouse button <i>n</i>. Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>Mouse</code>   1 T     A       <code>Function</code> MoveWindow
<code>DestroyFunc</code> MoveWindow
<code>AddToFunc</code> MoveWindow
+ C <code>Move</code>
+ C <code>ThisWindow</code> (PlacedByButton 5) <code>WindowShade</code> off
+ C <code>TestRc</code> (Match) <code>Maximize</code> on 0 100
+ C <code>ThisWindow</code> (PlacedByButton 4) <code>WindowShade</code> on
</pre>
</dl>
<p> The <i>PlacedByButton3</i> condition has the same meaning as <i>PlacedByButton</i> 3. It remains only for backward compatibility. </p>
<p> The <i>PlacedByFvwm</i> condition excludes all windows that have been placed manually or by using the user or program position hint. </p>
<p> The <i>Raised</i> conditions matches only windows that are fully visible on the current viewport and not overlapped by any other window. </p>
<p> The <i>Shaded</i> conditions matches only shaded windows (see <code>WindowShade</code> command). </p>
<p> The <i>State n</i> or <i>!State n</i> conditions match only windows with the specified integer state set (or unset). See the <code>State</code> command for details. The argument may range from 0 to 31. </p>
<p> The <i>Sticky</i>, <i>StickyAcrossDesks</i> and <i>StickyAcrossPages</i> match only windows that are currently sticky, sticky across all desks or sticky across all pages. Please refer to the <code>Style</code> options with the same name and the commands <code>Stick</code>, <code>StickAcrossDesks</code> and <code>StickAcrossPages</code> for details. </p>
<p> The <i>StickyIcon</i>, <i>StickyAcrossDesksIcon</i> and <i>StickyAcrossPagesIcon</i> match only windows that become sticky, sticky across all desks or sticky across all pages when they are in iconified state. </p>
<p> The <i>Transient</i> condition matches only windows that have the &quot;transient&quot; property set by the application. This it usually the case for application popup menus and dialogs. The <code>FvwmIdent</code> module can be used to find out whether a specific window is transient. </p>
<p> The <i>Visible</i> condition matches only windows that are at least partially visible on the current viewport and not completely overlapped by other windows.</dl>
</dl>
<h3>Module Commands</h3>
<p> Fvwm maintains a database of module configuration lines in a form </p>
<dl>
<dt>
<dd>
<pre>
<code>*</code><i>&lt;ModuleName&gt;</i><code>: </code><i>&lt;Config-Resource&gt;</i>
</pre>
</dl>
<p> where <i>&lt;ModuleName&gt;</i> is either a real module name or an alias. </p>
<p> This database is initially filled from config file (or from output of <code>-cmd</code> config command), and can be later modified either by user (via <code>FvwmCommand</code>) or by modules. </p>
<p> When modules are run, they read appropriate portion of database. (The concept of this database is similar to one used in X resource database). </p>
<p> Commands for manipulating module configuration database are described below.</p>
<dl>
<dt><code>*</code> <i>module_config_line</i></p>
<dd>
<dl>
<dt>
<dd> Defines a module configuration. <i>module_config_line</i> consists of a module name (or a module alias) and a module resource line. The new syntax allows a delimiter, a colon and optional spaces, between the module name and the rest of the line, this is recommended to avoid conflicts. </p>
<dl>
<dt>
<dd>
<pre>
*FvwmIconBox: MaxIconSize 48x48
*FvwmPager: WindowBorderWidth 1
*FvwmButtons-TopRight: Geometry 100x100-0+0
*FvwmButtons-Bottom: Geometry +0-0
</pre>
</dl>
</dl>
<dt><code>DestroyModuleConfig</code> <i>module_config</i></p>
<dd>
<dl>
<dt>
<dd> Deletes module configuration entries, so that new configuration lines may be entered instead. This also sometimes the only way to turn back some module settings, previously defined. This changes the way a module runs during a fvwm session without restarting. Wildcards can be used for portions of the name as well. </p>
<p> The new non-conflicting syntax allows a delimiter, a colon and optional spaces between the module name and the rest of the line. In this case a module name (or alias) can&#8217;t have wildcards. </p>
<dl>
<dt>
<dd>
<pre>
DestroyModuleConfig FvwmButtons*
DestroyModuleConfig FvwmForm: Fore
DestroyModuleConfig FvwmIconBox: Max*
</pre>
</dl>
</dl>
<dt><code>KillModule</code> <i>modulename</i> [<i>modulealias</i>]</p>
<dd>
<dl>
<dt>
<dd> Causes the module which was invoked with name <i>modulename</i> to be killed. The name may include wildcards. If <i>modulealias</i> is given, only modules started with the given alias are killed. </p>
<dl>
<dt>
<dd>
<pre>
# kill all pagers
KillModule FvwmPager
<code>Module</code> FvwmEvent SoundEvent
KillModule FvwmEvent SoundEvent
</pre>
</dl>
</dl>
<dt><code>Module</code> <i>modulename</i> [<i>moduleparams</i>]</p>
<dd>
<dl>
<dt>
<dd> Specifies a module with its optional parameters which should be spawned. Currently several modules, including <code>FvwmButtons</code>, <code>FvwmEvent</code>, <code>FvwmForm</code>, <code>FvwmGtk</code>, <code>FvwmPager</code>, <code>FvwmScript</code> support aliases. Aliases are useful if more than one instance of the module should be spawned. Aliases may be configured separately using <code>*</code> syntax. To start a module <code>FvwmForm</code> using an alias <i>MyForm</i>, the following syntax may be used: </p>
<dl>
<dt>
<dd>
<pre>
Module FvwmForm MyForm
</pre>
</dl>
<p> At the current time the available modules (included with fvwm) are <code>FvwmAnimate</code> (produces animation effects when a window is iconified or de-iconified), <code>FvwmAuto</code> (an auto raise module), <code>FvwmBacker</code> (to change the background when you change desktops), <code>FvwmBanner</code> (to display a spiffy XBM, XPM, PNG or SVG), <code>FvwmButtons</code> (brings up a customizable tool bar), <code>FvwmCommandS</code> (a command server to use with shell&#8217;s FvwmCommand client), <code>FvwmConsole</code> (to execute fvwm commands directly), <code>FvwmCpp</code> (to preprocess your <i>config</i> with cpp), <code>FvwmDebug</code> (to help debug fvwm), <code>FvwmDragWell</code> (the place to drag&amp;drop to), <code>FvwmEvent</code> (trigger various actions by events), <code>FvwmForm</code> (to bring up dialogs), <code>FvwmGtk</code> (to bring up GTK menus and dialogs), <code>FvwmIconBox</code> (like the mwm IconBox), <code>FvwmIconMan</code> (a flexible icon manager), <code>FvwmIdent</code> (to get window info), <code>FvwmM4</code> (to preprocess your <i>config</i> with m4), <code>FvwmPager</code> (a mini version of the desktop), <code>FvwmPerl</code> (a Perl manipulator and preprocessor), <code>FvwmProxy</code> (to locate and control obscured windows by using small proxy windows), <code>FvwmRearrange</code> (to rearrange windows), <code>FvwmSave</code> (saves the desktop state in .xinitrc style), <code>FvwmSaveDesk</code> (saves the desktop state in fvwm commands), <code>FvwmScript</code> (another powerful dialog toolkit), <code>FvwmScroll</code> (puts scrollbars on any window), <code>FvwmTabs</code> (a generic tabbing module), <code>FvwmTaskBar</code> (a Windows like task bar), <code>FvwmTheme</code> (managed colorsets, obsolete), <code>FvwmWharf</code> (an AfterStep like button bar), <code>FvwmWindowMenu</code> (a configurable fvwm menu listing current windows), <code>FvwmWinList</code> (a window list). These modules have their own man pages. There may be other modules out on there as well. </p>
<p> Modules can be short lived transient programs or, like <code>FvwmButtons</code> , can remain for the duration of the X session. Modules are terminated by the window manager prior to restarts and quits, if possible. See the introductory section on modules. The keyword <code>Module</code> may be omitted if <i>modulename</i> is distinct from all fvwm commands.</dl>
<dt><code>ModuleListenOnly</code> <i>modulename</i> [<i>moduleparams</i>]</p>
<dd>
<dl>
<dt>
<dd> This command works like the <code>Module</code> command, but fvwm never sends any messages to the module. This may be handy to write a module as a shell script that is triggered by external events without the burden to answer packets sent by fvwm. For example, a module written as a shell script may change labels of the <code>FvwmButtons</code> module to implement a simple clock.</dl>
<dt><code>ModulePath</code> <i>path</i></p>
<dd>
<dl>
<dt>
<dd> Specifies a colon separated list of directories in which to search for modules. To find a module, fvwm searches each directory in turn and uses the first file found. Directory names on the list do not need trailing slashes. </p>
<p> The <code>ModulePath</code> may contain environment variables such as <i>$HOME</i> (or <i>${HOME}</i>). Further, a &#8216;+&#8217; in the <i>path</i> is expanded to the previous value of the <i>path</i>, allowing easy appending or prepending to the <i>path</i>. </p>
<p> For example: </p>
<dl>
<dt>
<dd>
<pre>
ModulePath ${HOME}/lib/fvwm/modules:+
</pre>
</dl>
<p> The directory containing the standard modules is available via the environment variable <i>$FVWM_MODULEDIR</i>.</dl>
<dt><code>ModuleSynchronous</code> [Expect&nbsp;<wbr><i>string</i>] [Timeout&nbsp;<wbr><i>secs</i>] <i>modulename</i></p>
<dd>
<dl>
<dt>
<dd> The <code>ModuleSynchronous</code> command is very similar to <code>Module</code>. Fvwm stops processing any commands and user input until the module sends a string beginning with &quot;NOP FINISHED STARTUP&quot; back to fvwm. If the optional <i>Timeout</i> is given fvwm gives up if the module sent no input back to fvwm for <i>secs</i> seconds. If the <i>Expect</i> option is given, fvwm waits for the given <i>string</i> instead. <code>ModuleSynchronous</code> should only be used during fvwm startup to enforce the order in which modules are started. This command is intended for use with the (currently hypothetical) module that should be in place before other modules are started. </p>
<p> Warning: It is quite easy to hang fvwm with this command, even if a timeout is given. Be extra careful choosing the string to wait for. Although all modules in the fvwm distribution send back the &quot;NOP FINISHED STARTUP&quot; string once they have properly started up, this may not be the case for third party modules. Moreover, you can try to escape from a locked <code>ModuleSynchronous</code> command by using the key sequence <font SIZE="-1">Ctrl-Alt-Escape</font> (see the <code>EscapeFunc</code>).</dl>
<dt><code>ModuleTimeout</code> <i>timeout</i></p>
<dd>
<dl>
<dt>
<dd> Specifies how many seconds fvwm waits for a module to respond. If the module does not respond within the time limit then fvwm kills it. <i>timeout</i> must be greater than zero, or it is reset to the default value of 30 seconds.</dl>
<dt><code>SendToModule</code> <i>modulename</i> <i>string</i></p>
<dd>
<dl>
<dt>
<dd> Sends an arbitrary string (no quotes required) to all modules, whose alias or name matching <i>modulename</i>, which may contain wildcards. This only makes sense if the module is set up to understand and deal with these strings though. Can be used for module to module communication, or implementation of more complex commands in modules.</dl>
</dl>
<h3>Session Management Commands</h3>
<dl>
<dt><code>Quit</code></p>
<dd>
<dl>
<dt>
<dd> Exits fvwm, generally causing X to exit too.</dl>
<dt><code>QuitScreen</code></p>
<dd>
<dl>
<dt>
<dd> Causes fvwm to stop managing the screen on which the command was issued.</dl>
<dt><code>Restart</code> [<i>window_manager</i>&nbsp;<wbr>[<i>params</i>]]</p>
<dd>
<dl>
<dt>
<dd> Causes fvwm to restart itself if <i>window_manager</i> is left blank, or to switch to an alternate window manager (or other fvwm version) if <i>window_manager</i> is specified. If the window manager is not in your default search path, then you should use the full path name for <i>window_manager</i>. </p>
<p> This command should not have a trailing ampersand. The command can have optional parameters with simple shell-like syntax. You can use <i>~</i> (is expanded to the user&#8217;s home directory) and environmental variables <i>$VAR</i> or <i>${VAR}</i>. Here are several examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>Key</code> F1 R N Restart
<code>Key</code> F1 R N Restart fvwm -s
<code>Key</code> F1 R N Restart ~/bin/fvwm -f $HOME/.fvwm/main
<code>Key</code> F1 R N Restart fvwm1 -s -f .fvwmrc
<code>Key</code> F1 R N Restart xterm -n '&quot;X console&quot;' \
  -T \&quot;X\&nbsp;<wbr>console\&quot; -e fvwm1 -s
</pre>
</dl>
<p> If you need a native restart, we suggest only to use <code>Restart</code> command without parameters unless there is a reason not to. If you still use an old command &#8216;Restart fvwm2&#8217; that was correct in 2.2.x, all current command line arguments are lost. On a restart without parameters or with &#8211;pass-args, they are preserved. Here are some cases when &#8216;Restart fvwm2&#8217; or &#8216;Restart fvwm&#8217; cause troubles: </p>
<dl>
<dt>
<dd>
<pre>
* running fvwm under a session manager
* running fvwm with multi headed displays
* having command line arguments, like
  -f themes-rc or -cmd
* if the first fvwm2 in the $PATH is a
  different one
</pre>
</dl>
<p> This is why we are issuing a warning on an old usage. If you really want to restart to fvwm with no additional arguments, you may get rid of this warning by using &quot;Restart fvwm -s&quot; or &quot;Restart /full/path/fvwm&quot;. </p>
<p> Note, currently with multi headed displays, restart of fvwms on different screens works independently.</dl>
<dt><code>Restart</code> <code>&#8211;pass-args</code> <i>window_manager</i></p>
<dd>
<dl>
<dt>
<dd> The same as <code>Restart</code> without parameters but the name for the current window manager is replaced with the specified <i>window_manager</i> and original arguments are preserved. </p>
<p> This command is useful if you use initial arguments like </p>
<dl>
<dt>
<dd>
<pre>
-cmd FvwmCpp
</pre>
</dl>
<p> and want to switch to another fvwm version without losing the initial arguments.</dl>
<dt><code>Restart</code> <code>&#8211;dont-preserve-state</code> [<i>other-params</i>]</p>
<dd>
<dl>
<dt>
<dd> The same as </p>
<dl>
<dt>
<dd>
<pre>
<code>Restart</code> [<i>other-params</i>]
</pre>
</dl>
<p> but it does not save any window states over the restart. </p>
<p> Without this option, <code>Restart</code> preserves most per-window state by writing it to a file named <i>.fs-restart-</i><i>$HOSTDISPLAY</i> in the user&#8217;s home directory.</dl>
<dt><code>SaveSession</code></p>
<dd>
<dl>
<dt>
<dd> Causes a session manager (if any) to save the session. This command does not work for xsm, it seems that xsm does not implement this functionality. Use Unix signals to manage xsm remotely.</dl>
<dt><code>SaveQuitSession</code></p>
<dd>
<dl>
<dt>
<dd> Causes a session manager (if any) to save and then shutdown the session. This command does not work for xsm, it seems that xsm does not implement this functionality. Use Unix signals to manage xsm remotely.</dl>
</dl>
<h3>Colorsets</h3>
<p> Colorsets are a powerful method to control colors. Colorsets create appearance resources that are shared by fvwm and its modules. When a colorset is modified all parts of fvwm react to that change. A colorset includes a foreground color, background color, shadow and highlight color (often based on the background color), background face (this includes images and all kinds of gradients). There is a way to render background face and specify other color operations. </p>
<p> In the 2.4.x versions a special module <code>FvwmTheme</code> was introduced to manage colorsets. Starting with the 2.5.x beta version, the <code>FvwmTheme</code> functionality was moved to the core fvwm, so this module became obsolete. </p>
<p> The old syntax: </p>
<dl>
<dt>
<dd>
<pre>
<code>DestroyModuleConfig</code> <code>FvwmTheme</code>: *
*<code>FvwmTheme</code>: <code>Colorset</code> 0 fg black, bg rgb:b4/aa/94
*<code>FvwmTheme</code>: <code>Colorset</code> 1 fg black, bg rgb:a1/b2/c8
</pre>
</dl>
<p> corresponds to the new syntax: </p>
<dl>
<dt>
<dd>
<pre>
<code>CleanupColorsets</code>
<code>Colorset</code> 0 fg black, bg rgb:b4/aa/94
<code>Colorset</code> 1 fg black, bg rgb:a1/b2/c8
</pre>
</dl>
<dl>
<dt><code>Colorset</code> <i>num</i> [<i>options</i>]</p>
<dd>
<dl>
<dt>
<dd> Creates or modifies colorset <i>num</i>. Colorsets are identified by this number. The number can start at zero and can be a very large number. </p>
<p> Warning: The highest colorset number used determines memory consumption. Thus, if you define &#8216;Colorset 100000&#8217;, the memory for 100001 colorsets is used. Keep your colorset numbers as small as possible. </p>
<p> By convention, colorsets are numbered like this: </p>
<dl>
<dt>
<dd>
<pre>
# 0 = Default colors
# 1 = Inactive windows
# 2 = Active windows
# 3 = Inactive menu entry and menu background
# 4 = Active menu entry
# 5 = greyed out menu entry (only bg used)
# 6 = module foreground and background
# 7 = hilight colors
</pre>
</dl>
<p> If you need to have more colors and do not want to reinvent the wheel, you may use the convention used in fvwm-themes, it defines the meaning of the first 40 colorsets for nearly all purposes: </p>
<p> <i><a rel="nofollow" href="http://fvwm-themes.sourceforge.net/doc/colorsets">http://fvwm-themes.sourceforge.net/doc/colorsets</a></i> </p>
<p> Each colorset has four colors, an optional pixmap and an optional shape mask. The four colors are used by modules as the foreground, background, highlight and shadow colors. When a colorset is created it defaults to a foreground of black and background of gray. The background and foreground are marked as &quot;average&quot; and &quot;contrast&quot; (see later) so that just specifying a pixmap or gradient gives sensible results. </p>
<p> <i>options</i> is a comma separated list containing some of the keywords: fg, Fore, Foreground, bg, Back, Background, hi, Hilite, Hilight, sh, Shade, Shadow, fgsh, Pixmap, TiledPixmap, AspectPixmap, Transparent, RootTransparent, Shape, TiledShape, AspectShape, NoShape, ?Gradient, Tint, fgTint, bgTint, Alpha, fgAlpha, Dither, NoDither, IconTint, IconAlpha, Plain. </p>
<p> <i>fg</i>, <i>Fore</i> and <i>Foreground</i> take a color name as an argument and set the foreground color. The special name <i>Contrast</i> may be used to select a color that contrasts well with the background color. To reset the foreground color to the default value you can simply omit the color name. </p>
<p> <i>bg</i>, <i>Back</i> and <i>Background</i> take a color name as an argument and set the background color. It also sets the highlight and shadow colors to values that give a 3d effect unless these have been explicitly set with the options below. The special name <i>Average</i> may be used to select a color that is the average color of the pixmap. If the pixmap is tinted with the <i>Tint</i> option, the tint is not taken in account in the computation of the average color. You should use the <i>bgTint</i> option to get the &quot;real&quot; average color. The background color is reset to the default value if the color name is omitted. </p>
<p> <i>hi</i>, <i>Hilite</i> and <i>Hilight</i> take a color name as an argument and set the highlight color. If the highlight color is not explicitly set, the default is to calculate it from the background color. To switch back to the default behavior the color name can be omitted. </p>
<p> <i>sh</i>, <i>Shade</i> and <i>Shadow</i> take a color name as an argument and set the shadow color. If the shadow color is not explicitly set, the default is to calculate it from the background color. To switch back to the default behavior the color name can be omitted. </p>
<p> <i>fgsh</i> takes a color name as an argument and sets the color used by the shadowing font effect. See the <code>Font Shadow Effects</code> section of the fvwm man page. By default this color is computed from the foreground and background colors. To switch back to the default the color name can be omitted. </p>
<p> <i>Pixmap</i>, <i>TiledPixmap</i> and <i>AspectPixmap</i> take a file name as an argument, search the <code>ImagePath</code> and use it as the background pixmap. Any transparent parts are filled with the background color. Not specifying a file name removes any existing image from the colorset. <i>TiledPixmap</i> produces repeated copies of the image with no scaling, <i>Pixmap</i> causes the image to be stretched to fit whatever object the colorset is applied to and <i>AspectPixmap</i> stretches to fit but retains the image aspect ratio. </p>
<p> <i>Transparent</i> creates a transparent background pixmap. The pixmap is used as a window background to achieve root transparency. For this you should use the <i>ParentalRelativity</i> option to the <code>Style</code> command. A subsequent root background change may be detected or not, this depends on the program used to set the background. If you use <code>fvwm-root</code>, <code>xsetbg</code> (xli), <code>FvwmBacker</code> with solid or colorset colors or a recent version of <code>Esetroot</code> (&gt;= 9.2) a background change is detected. If background changes are not detected (e.g., if you use <code>xv</code> or <code>xsetroot</code>) you can force detection by using the <code>-d</code> option of fvwm-root: </p>
<dl>
<dt>
<dd>
<pre>
xv -root -quit mybg.png; fvwm-root -d
</pre>
</dl>
<p> Due to the way X implements transparency no guarantees can be made that the desired effect can be achieved. The application may even crash. If you experience any problems with this option, do not use it. </p>
<p> Using outline move and resize (see the <code>OpaqueMoveSize</code> command and the <i>ResizeOpaque</i> <code>Style</code> option) as well as setting the <i>WindowShadeShrinks</i> style may help. The transparency achieved with <i>Transparent</i> depends on whether the colorset is applied to the foreground or the background of a window. In the second case the transparency is relative to the parent window of the window on which the colorset is defined. For example: </p>
<dl>
<dt>
<dd>
<pre>
Colorset 12 VGradient 200 grey30 grey60
Colorset 17 Transparent
*<code>FvwmIconMan</code>: Colorset 12
*<code>FvwmIconMan</code>: PlainColorset 17
</pre>
</dl>
<p> gives an IconMan with a vertical grey gradient background and the buttons use the background (by transparency). To obtain a (root) transparent IconMan: </p>
<dl>
<dt>
<dd>
<pre>
Colorset 12 Transparent
Colorset 17 Transparent
Colorset 18 Transparent
Colorset 19 Transparent
*<code>FvwmIconMan</code>: Colorset 12
*<code>FvwmIconMan</code>: PlainColorset 17
*<code>FvwmIconMan</code>: FocusColorset 18
*<code>FvwmIconMan</code>: IconColorset  19
</pre>
</dl>
<p> The Colorset IconMan option defines the IconMan window background, but the PlainColorset and the FocusColorset are drawn on the foreground. So, the transparency of the IconMan buttons is achieved by drawing nothing. Now if this IconMan is swallowed in an FvwmButtons as: </p>
<dl>
<dt>
<dd>
<pre>
<code>FvwmButtons</code>:(Colorset 10, Swallow &quot;FvwmIconMan&quot; 'FvwmIconMan')
</pre>
</dl>
<p> then, <code>FvwmIconMan</code> becomes a child of <code>FvwmButtons</code> and it is transparent relative to <code>FvwmButtons</code>. So, in this case <code>FvwmIconMan</code> uses Colorset 10 as background. If you want root transparency use the <i>RootTransparent</i> option. <code>FvwmButtons</code>, <code>FvwmIconMan</code>, <code>FvwmIdent</code>, <code>FvwmScroll</code> and <code>FvwmTaskBar</code> are relatively simple. There is one main colorset option which defines the background of the window and the other colorsets (if any) are drawn on the foreground. The case of <code>FvwmWinList</code> and <code>FvwmProxy</code> are simpler. With <code>FvwmWinList</code> all the colorsets are drawn on the foreground and with <code>FvwmProxy</code> the two colorsets refer to the window backgrounds. <code>FvwmPager</code> is more complicated as almost everything in the pager are windows with some parental relations (the mini windows are the child and the desktops are the parents and all this is complicated by the hilighted page). So, the colorsets apply to the background of these windows. You should experiment. For <code>FvwmForm</code> and <code>FvwmScript</code> the situation is similar. There is a main window (a child of the root window) which corresponds to the main colorset and most of the widgets are windows which are children of the main window. <i>Tint</i> may work or not with the <i>Transparent</i> option. When the colorset is drawn on the foreground <i>Tint</i> should work. In some cases, tinting may be very slow. Tinting may work with fvwm menu (without animation). Tinting may work better if your X server has backing store enabled (try xdpyinfo to see if this the case). There is a chance that the backing store support of your X server does not work well with the terrible hack used to Tint the ParentRelative Pixmap. So, to get tinted root transparency it is more safe to use the <i>RootTransparent</i> option. </p>
<p> <i>RootTransparent</i> [ <i>buffer</i> ] creates a root transparent background. To make this option work, you must use an <code>Esetroot</code> compatible program, fvwm-root with the &#8211;retain-pixmap option or <code>FvwmBacker</code> with the RetainPixmap option (and colorset or solid backgrounds). The <i>buffer</i> keyword is useful only when the <i>Tint</i> option is used too. This speeds up creation of windows which use the colorset (useful for fvwm menus) at the cost of memory usage. It also speeds up opaque move and resize which can be unacceptably slow without <i>buffer</i>. However, this option may add a lot of memory to your X server (depending on the size of the image used to set the background). In summary, using outline move and resize for modules which use such a colorset may be a good idea. </p>
<p> <i>Shape</i>, <i>TiledShape</i> and <i>AspectShape</i> take a file name as an argument, search the <code>ImagePath</code> and use it as the shape bitmap. <i>TiledShape</i> produces repeated copies of the bitmap with no scaling, <i>Shape</i> causes the bitmap to be stretched to fit whatever object the colorset is applied to and <i>AspectShape</i> stretches to fit but retains the bitmap aspect ratio. If the file is a pixmap in xpm format the shape mask (all opaque pixels) of the pixmap is used. For png and svg images, the shape mask is equivalent to all not completely transparent pixels (alpha &gt; 0). </p>
<p> <code>Warning</code> Due to the way X11 implements shapes you cannot take back making windows shaped. You may have to restart fvwm or the shaped application. </p>
<p> <i>?Gradient &#8230;</i> creates a pixmap and stretches it to fit the window. <i>?Gradient</i> may be one of <i>HGradient</i>, <i>VGradient</i>, <i>DGradient</i>, <i>BGradient</i>, <i>SGradient</i>, <i>CGradient</i>, <i>RGradient</i> or <i>YGradient</i>. The gradient types are as follows: H is horizontal; V is vertical; D is diagonal from top left to bottom right; B is a backwards diagonal from bottom left to top right; S is concentric squares; C is concentric circles; R is a radar like pattern and Y is a Yin Yang style (but without the dots). Please refer to the <code>Color Gradients</code> section for the syntax of gradients. </p>
<p> <i>Tint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the image defined using <i>?Pixmap</i> or <i>?Gradient</i> to be tinted with the specified color using the percentage. If the image is transparent <i>Tint</i> tints only the image part. Unfortunately, a colorset background specified using the <i>Transparent</i> option can give strange results. See the <i>Transparent</i> option for details. With no arguments this option removes the tint. </p>
<p> <i>fgTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the color defined using <i>fg</i> to be tinted with the specified color using the percentage. With no arguments this option removes the tint. </p>
<p> <i>bgTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes the color defined using <i>bg</i> to be tinted with the specified color using the percentage. If the <i>sh</i> and <i>hi</i> colors are not specified, they are recomputed from the tinted bg color. With no arguments this option removes the tint. </p>
<p> <i>Alpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the image defined using <i>?Pixmap</i> or <i>?Gradient</i> with the <i>bg</i> color using the percentage. If the percentage is 0 the image is hidden and if it is 100 the image is displayed as usual (no merge). The default is 100 and it is restored if no argument is given. </p>
<p> <i>fgAlpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the text and the colorset background using the percentage. If the percentage is 0 the text is hidden and if it is 100 the text is displayed as usual (no merge). This option has an effect only with fonts loaded by Xft, see the <code>Font Names and Font Loading</code> section. The default is 100 and it is restored if no argument is given. </p>
<p> <i>Dither</i> causes fvwm to dither the image defined using <i>?Pixmap</i> or <i>?Gradient.</i> This is useful only with displays with depth less than or equal to 16 (i.e., on displays which can only display less than 65537 colors at once). The dithering effect lets you simulate having more colors available that you actually have. <i>NoDither</i> causes fvwm to do not dither the images. <i>Dither</i> is the default if the depth is less than or equal to 8 (a screen with 256 colors or less). In depth 15 (32768 colors) and 16 (65536 colors), the default is <i>NoDither</i>, however this effect can be useful with images which contain a lot of close colors. For example a fine gradient looks more smooth. </p>
<p> <i>IconTint</i> takes 2 arguments, a color and a percentage between 0 and 100. It causes fvwm or a module to tint the &quot;icons&quot; which are rendered into the colorset background with the specified color using a percentage. Here &quot;icons&quot; means, fvwm Icons, fvwm menu icons, MiniIcons which represent applications in various modules, images loaded by modules (e.g., images specified by the <i>Icon</i> <code>FvwmButtons</code> button option) &#8230;etc. With no arguments this option removes the icon tint. </p>
<p> <i>IconAlpha</i> takes a percentage between 0 and 100 as an argument. It causes fvwm to merge the &quot;icons&quot; which are rendered into the colorset background using this percentage. The default is 100 and it is restored if no argument is given. </p>
<p> <i>Note</i>: It is equivalent to use &quot;Tint a_color rate&quot; and &quot;Alpha a&quot; if a = 100 and the bg color is a_color. This equivalence does not hold for IconAlpha and IconTint as the background can be an image or a gradient (and not a uniform color background). However, in some cases you can achieve (almost) the same effect by using IconTint in the place of IconAlpha. This is preferable as, in general, IconAlpha generates more redrawing than IconTint. </p>
<p> <i>NoShape</i> removes the shape mask from the colorset while <i>Plain</i> removes the background pixmap or gradient. </p>
<p> Examples </p>
<dl>
<dt>
<dd>
<pre>
Colorset 3 fg tan, bg navy
</pre>
</dl>
<p> If necessary this creates colorsets 0, 1, 2 and 3 and then changes colorset 3 to have a foreground of tan, a background of navy. </p>
<dl>
<dt>
<dd>
<pre>
Colorset 3 bg &quot;navy blue&quot;
</pre>
</dl>
<p> changes the background color of colorset 3 to navy blue. The foreground and pixmap are unchanged. </p>
<dl>
<dt>
<dd>
<pre>
Colorset 3 AspectPixmap large_murky_dungeon.xpm
</pre>
</dl>
<p> causes depression. </p>
<dl>
<dt>
<dd>
<pre>
Colorset 3 bg Average
</pre>
</dl>
<p> Sets the background color and the relief colors to match the background pixmap. This is the default setting but it must be used if a background color was specified and is now not required. </p>
<dl>
<dt>
<dd>
<pre>
Colorset 3 YGradient 200 3 blue 1000 navy 1 blue 1000 navy
</pre>
</dl>
<p> Adds a Yin Yang gradient background pixmap to colorset 3. If the background is set to average it is recomputed along with the foreground if that is set to contrast. </p>
<dl>
<dt>
<dd>
<pre>
#!/bin/sh
<code>FvwmCommand</code> &quot;Colorset 7 fg navy, bg gray&quot;
while true
do
  <code>FvwmCommand</code> &quot;Colorset 7 fg gray&quot;
  sleep 1
  <code>FvwmCommand</code> &quot;Colorset 7 fg navy&quot;
  sleep 1
done
</pre>
</dl>
<p> Makes colorset 7 blink. </p>
<p> The color names used in colorsets are saved as fvwm variables which can be substituted in any fvwm command. For example: </p>
<dl>
<dt>
<dd>
<pre><code>
AddToFunc InitFunction + I Exec exec xterm - fg $[fg.cs0] - bg $[bg.cs0]
</code></pre>
</dl>
<p> Where $[fg.cs0] is the foreground color of colorset zero. Please refer to the <code>Command Expansion</code> section for more information.</dl>
<dt><code>CleanupColorsets</code></p>
<dd>
<dl>
<dt>
<dd> Resets a definition of all colorsets.</dl>
<dt><code>Color Gradients</code></p>
<dd>
<dl>
<dt>
<dd> A color gradient is a background that changes its color gradually from one hue to a different one. Color gradients can be used by various commands and modules of fvwm. There are eight types of gradients: <code>HGradient</code> is a horizontal gradient, <code>VGradient</code> is vertical, <code>DGradient</code> is diagonal from top left to bottom right, <code>BGradient</code> is backwards diagonal from bottom left to top right, <code>SGradient</code> is concentric squares, <code>CGradient</code> is concentric circles, <code>RGradient</code> is a radar like pattern and <code>YGradient</code> is a Yin Yang style (but without the dots). </p>
<p> The color gradient syntax has two forms:</p>
<dl>
<dt> <code>?Gradient</code> <i>colors</i> <i>start-color</i> <i>end-color</i></dl>
<dd>This form specifies a linear gradient. The arguments denote the total number of <i>colors</i> to allocate (between 2 and 1000), the initial color and the final color. </p>
<p> Example: </p>
<dl>
<dt>
<dd>
<pre>
<code>TitleStyle</code> VGradient 20 rgb:b8/ce/bc rgb:5b/85/d0
</pre>
</dl>
<dl>
<dt> <code>?Gradient</code> <i>colors</i> <i>segments</i> <i>color</i> <i>length</i> <i>color</i> [<i>length</i>&nbsp;<wbr><i>color</i>] &#8230;</dl>
<dd>The second form specifies a nonlinear gradient. The arguments are: the total number of <i>colors</i> to allocate (between 2 and 1000), then the number of <i>segments</i>. For each segment, specify the starting <i>color</i>, a relative <i>length</i>, then the ending color. Each subsequent segment begins with the second color of the last segment. The lengths may be any non-negative integers. The length of one segment divided by the sum of all segments lengths is the fraction of the colors that are used for the segment. </p>
<p> Examples: </p>
<dl>
<dt>
<dd>
<pre>
<code>MenuStyle</code> * \
        MenuFace DGradient 128 2 lightgrey 50 blue 50 white
# 20% gradient from red to blue,
# 30% from blue to black,
# 50% from black to grey
<code>MenuStyle</code> * \
        MenuFace DGradient 100 3 Red 20 Blue 30 Black 50 Grey
# 50% from blue to green, then
# 50% from yellow to red
<code>Colorset</code> 0 HGradient 128 3 Blue 1000 Green 1 Yellow 1000 Red
</pre>
</dl>
</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> The environment variables that have an effect on how fvwm operates are the following: </p>
<p> <i>DISPLAY</i></p>
<dl>
<dt>
<dd> Fvwm starts on this display unless the <code>-display</code> option is given.</dl>
<p> <i>FVWM_MODULEDIR</i></p>
<dl>
<dt>
<dd> Set by fvwm to the directory containing the standard fvwm modules.</dl>
<p> <i>FVWM_USERDIR</i></p>
<dl>
<dt>
<dd> Used to determine the user&#8217;s data directory for reading and sometimes writing personal files. If this variable is not already set, it is set by fvwm to <i>$HOME/.fvwm</i>, which is the default user&#8217;s data directory.</dl>
<p> <i>SESSION_MANAGER</i></p>
<dl>
<dt>
<dd> Fvwm tries to contact this session manager.</dl>
<p> <i>SESSION_MANAGER_NAME</i></p>
<dl>
<dt>
<dd> This is used mainly to determine xsm running to work around its bug. If this variable is set to &quot;xsm&quot;, DiscardCommand is set as xsm expects it and not as XSMP requires. If you run fvwm under xsm, you should set this variable to &quot;xsm&quot;, otherwise old state files are not removed.</dl>
<p> <i>SM_SAVE_DIR</i></p>
<dl>
<dt>
<dd> If this is set, fvwm saves its session data in this directory. Otherwise it uses <i>$HOME</i>. Note, the state files are named <i>.fs-??????</i> and normally are removed automatically when not used anymore.</dl>
<h2>AUTHORS</h2>
<p> Robert Nation with help from many people, based on twm code, which was written by Tom LaStrange. After Robert Nation came Charles Hines, followed by Brady Montz. Currently fvwm is developed by a number of people on the fvwm-workers mailing list.</p>
<h2>COPYRIGHT</h2>
<p> Fvwm and all the modules, scripts and other files coming with the distribution are subject to the GNU General Public License (GPL). Please refer to the COPYING file that came with fvwm for details.</p>
<h2>BUGS</h2>
<p> Bug reports can be sent to the fvwm-workers mailing list at &lt;fvwm-workers [at] fvwm.org&gt; </p>
<p> The official fvwm homepage is <i><a rel="nofollow" href="http://fvwm.org/">http://fvwm.org/</a></i>. </p>
<h2>Index</h2>
