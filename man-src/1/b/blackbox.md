---
title: "blackbox(1)"
name: "blackbox"
section: "1"
letter: "b"
url: "/docs/linux/man/1-blackbox/"
description: "blackbox – a window manager for X11"
---

<h2 class="name">NAME</h2>
<p> blackbox &#8211; a window manager for X11 </p>
<h2>SYNOPSIS</h2>
<p> <code>blackbox</code> -help | -version<br />
 <code>blackbox </code> [ -rc<i> rcfile </i>] [ -display<i> display </i>]</p>
<h2>DESCRIPTION</h2>
<p> Blackbox is a window manager for the Open Group&#8217;s X Window System, Version 11 Release 6 and above. Its design is meant to be visually minimalist and fast. </p>
<p> Blackbox is similar to the NeXT interface and Windowmaker. Applications are launched using a menu which is accessed by right clicking on the root window. Workspaces, a system of virtual desktops are controlled via a menu which is accessed by middle clicking on the root window and by using the toolbar. Individual windows can be controlled by buttons on the title bar and more options are available by right clicking on the title bar. </p>
<p> Blackbox is able to generate beautiful window decorations on the fly at high speed. Themes, called styles in Blackbox terminology, are very flexible but the use of pixmaps has been purposefully avoided to eliminate dependencies and excess memory usage. </p>
<p> Blackbox itself does not directly handle key bindings like most other window managers. This task is handled by a separate utility called bbkeys. Although Blackbox has a built-in workspace (paging) system, bbpager, which provides a graphical pager, is popular with many users. bbkeys, bbpager and several other bbtools can be found by going to </p>
<pre>
<code><a rel="nofollow" href="http://bbtools.thelinuxcommunity.org/">http://bbtools.thelinuxcommunity.org/</a></code>
</pre>
<p> The slit is an edge of the screen which can hold specially designed programs called dock apps (from Windowmaker). In addition, the popular program gkrellm will also run in the slit. There is a huge selection of dockapps available and they run the gamut from must-have gadgets to utterly useless (but cute and/or funny) eye candy. </p>
<pre>
<code><a rel="nofollow" href="http://www.bensinclair.com/dockapp/">http://www.bensinclair.com/dockapp/</a></code>
<code><a rel="nofollow" href="http://dockapps.org/">http://dockapps.org/</a></code>
</pre>
<h2>OPTIONS</h2>
<p> Blackbox supports the following command line options:</p>
<dl>
<dt>
<dd> <code>-help </code> Display command line options, compiled-in features, and exit.</p>
<dt>
<dd> <code>-version</code> Display version and exit.</p>
<dt>
<dd> <code>-rc</code><i>&nbsp;<wbr>rcfile</i> Use an alternate resource file.</p>
<dt>
<dd> <code>-display</code><i>&nbsp;<wbr>display</i> Start Blackbox on the specified display, and set the <code>DISPLAY </code> environment variable to this value for programs started by Blackbox.</dl>
<h2>STARTING AND EXITING BLACKBOX</h2>
<p> The most common method for starting Blackbox is to place the the command &quot;blackbox&quot; (no quotes) at the end of your <code>~/.xinitrc</code> or <code>~/.xsession</code> file. The advantage of putting Blackbox at the end of the file is that the X Server will shutdown when you exit Blackbox. Blackbox can also be started from the command line of a terminal program like xterm in an X session that does not already have a window manager running. </p>
<p> On startup, Blackbox will look for <code>~/.blackboxrc </code> and use the resource <code>session.menuFile </code> to determine where to get the menu for the session. If this file is not found Blackbox will use <code>/usr/share/blackbox/menu</code> as the menu file. If that fails as well Blackbox will use a default menu that contains commands to start an xterm as well as restart and exit the window manager. The other resources available in the <code>~/.blackboxrc </code> file are discussed later in this manual under the heading RESOURCE FILE. </p>
<p> On exit, Blackbox writes its current configuration to <code>~/.blackboxrc. </code> </p>
<pre>
<code>NOTE: </code>
If ~/.blackboxrc is modified during a Blackbox 
session, Blackbox must be restarted with the 
&quot;restart&quot; command on the main menu or the changes 
will be lost on exit. Restart causes Blackbox to 
re-read ~/.blackboxrc and apply the changes immediately.
</pre>
<p> Blackbox can be exited by selecting &quot;exit&quot; on the main menu (discussed shortly), killing it gently from a terminal or by the X Window System shutdown hot key combo Ctrl+Alt+BackSpace. </p>
<h2>USING BLACKBOX</h2>
<p> A three button mouse has the following functions when clicking on the root window:</p>
<dl>
<dt><code>Button Two</code> (Middle Button)</p>
<dd> Open workspace menu</p>
<dt><code>Button Three</code> (Right Button)</p>
<dd> Open main menu</p>
<dt>Note that Button One (Left Button) is not used.</p>
<dd>
<dt><code>Main Menu</code></p>
<dd> The default installation assumes you have a number of common X Window System programs in their typical locations. The default menu is defined by a plain text file named &#8216;menu&#8217;. It is heavily commented and covers a number of details of menu file syntax. This file can also be edited graphically by using the extension program bbconf which makes menu creation very easy. Menu file syntax is discussed later in this manual. </p>
<pre>
<code>Caveat:</code>
Menus can run arbitrary command lines, but
if you wish to use a complex command line 
it is best to place it in a shell script. 
Remember to put #!/bin/sh on the first 
line and chmod 755 on the file to make it 
executable.
</pre>
<dt><code>Workspace Menu</code></p>
<dd> This menu gives the user control of the workspace system. The user can create a new workspace, remove the last workspace or go to an application via either the icon menu or a workspace entry. Workspaces are listed by name. Clicking on the workspace name will take you to that workspace with focus on the program under the mouse. If there are programs already running in the workspace, they will appear in a pop-out menu. Clicking on the application name will jump to the workspace and focus that application. If a middle click is used the window will be brought to the current workspace. </p>
<p> Blackbox uses an external program, bbpager, to provide a traditional, graphical paging interface to the workspace system. Many Blackbox users run another extension program &#8211; bbkeys &#8211; to provide keyboard shortcuts for workspace control. </p>
<pre>
<code>Caveat: </code>
To name a workspace the user must right
click on the toolbar, select &quot;Edit current 
workspace name,&quot; type the workspace name, 
And_Press_Enter to finish.
</pre>
<p> Workspaces can also be named in the .blackboxrc file as described in RESOURCES.</p>
<dt><code>The Slit</code></p>
<dd> The Slit provides a user positionable window for running utility programs called &quot;dockapps&quot;. To learn more about dockapps refer to the web sites mentioned in the Description. Dockapps automatically run in the slit in most cases, but may require a special command switch. Often, -w is used for &quot;withdrawn&quot; into the slit. </p>
<p> gkrellm is a very useful and modern dockapp that gives the user near real time information on machine performance. Other dockapps include clocks, notepads, pagers, key grabbers, fishbowls, fire places and many, many others. </p>
<p> Only mouse button three is captured by the Blackbox slit. This menu allows the user to change the position of the slit, and sets the state of Always on top, and Auto hide. These all do what the user expects. </p>
<pre>
<code>Caveat:</code>
When starting Dockapps from an external script
a race condition can take place where the shell
rapidly forks all of the dockapps, which then
take varied and random times to draw themselves 
for the first time. To get the dockapps to start 
in a given order, follow each dockapp with 
sleep 2; This ensures that each dockapp is placed 
in the correct order by the slit.
</pre>
<pre>
<code>i.e.</code>
#!/bin/sh
speyes -w &amp; sleep 2
gkrellm -w &amp; sleep 2
</pre>
<dt><code>The Toolbar</code></p>
<dd> The toolbar provides an alternate method for cycling through multiple workspaces and applications. The left side of the toolbar is the workspace control, the center is the application control, and the right side is a clock. The format of the clock can be controlled as described under RESOURCES. </p>
<p> Mouse button 3 raises a menu that allows configuration of the toolbar. It can be positioned either at the top or the bottom of the screen and can be set to auto hide and/or to always be on top. </p>
<pre>
<code>Caveat: </code>
The toolbar is a permanent fixture. It 
can only be removed by modifying the source and 
rebuilding, which is beyond the scope of this 
document. Setting the toolbar to auto hide is
the next best thing.
</pre>
<dt><code>Window Decorations</code></p>
<dd> Window decorations include handles at the bottom of each window, a title bar, and three control buttons. The handles at the bottom of the window are divided into three sections. The two corner sections are resizing handles The center section is a window moving handle. The bottom center handle and the title bar respond to a number of mouse clicks and key + mouse click combinations. The three buttons in the title bar, left to right, are iconify, maximize, and close. The resize button has special behavior detailed below.</p>
<dt><code>Button One</code> (Left Button)</p>
<dd> Click and drag on titlebar to move or resize from bottom corners. Click the iconify button to move the window to the icon list. Click the maximize button to fully maximize the window. Click the close button to close the window and application. Double-Click the title bar to shade the window.</p>
<dt><code>Alt + Button One</code></p>
<dd> Click anywhere on client window and drag to move the window.</p>
<dt><code>Button Two</code> (Middle Button)</p>
<dd> Click the titlebar to lower the window. Click the maximize button to maximize the window vertically.</p>
<dt><code>Button Three</code> (Right Button)</p>
<dd> Click on title bar or bottom center handle pulls down a control menu. Click the maximize button to maximize the window horizontally.</p>
<dt><code>Alt + Button Three</code></p>
<dd> Click anywhere on client window and drag to resize the window. </p>
<dt>
<dd> <code>The control menu contains:</code></p>
<dt><code>Send To &#8230;</code></p>
<dd>
<pre>
<code>Button One</code>  (Left Button)
Click to send this window to another workspace.  
</pre>
<pre>
<code>Button Two</code>  (Middle Button)
Click to send this window to another workspace, change 
to that workspace and keep the application focused.
as well.
<dt><code>Shade</code>
<dd>This is the same action as Double-Click with Button One.
<dt><code>Iconify</code>
<dd>Hide the window.  It can be accessed with the icon menu.
<dt><code>Maximize</code>
<dd>Toggle window maximization.
<dt><code>Raise</code>
<dd>Bring window to the front above the other windows and
focus it.
<dt><code>Lower</code>
<dd>Drop the window below the other ones.
<dt><code>Stick</code>
<dd>Stick this window to the glass on the inside of
the monitor so it does not hide when you change 
workspaces.
<dt><code>Kill Client</code>
<dd>This kills the client program with -SIGKILL (-9)
Only use this as a last resort.
<dt><code>Close</code>
<dd>Send a close signal to the client application.
</dl>
</pre>
<h2>STYLES</h2>
<p> Styles are a collection of colors, fonts, and textures that control the appearance of Blackbox. These characteristics are recorded in style files. The default system style files are located in <i>/usr/share/blackbox/styles.</i> The menu system will identify the style by its filename, and styles can be sorted into different directories at the user&#8217;s discretion. </p>
<p> There are over 700 styles available for Blackbox. The official distribution point for Blackbox styles is </p>
<pre>
<code><a rel="nofollow" href="http://blackbox.themes.org/">http://blackbox.themes.org/</a></code>
</pre>
<p> All themes should install by simply downloading them to <code>~/.blackbox/</code> then unzip it, and de-tar it. </p>
<p> On open Unixes this will be: </p>
<p> <code>tar zxvf stylename.tar.gz</code> </p>
<p> On commercial Unixes this will be something like: </p>
<p> <code>gunzip stylename.tar.gz &amp;&amp; tar xvf stylename.tar</code> </p>
<p> Check your system manuals for specifics or check with your network administrator. </p>
<p> An entry should appear in the styles menu immediately. </p>
<pre>
<code>Security Warning</code>
Style files can execute shell scripts and other
executables. It would is wise to check the 
rootCommand in the style file and make sure that 
it is benign.
</pre>
<dl>
<dt><code>Things that go wrong.</code></p>
<dd>
<dt>1. The theme is pre Blackbox 0.51.</p>
<dd> Style file syntax changed with version 0.51</p>
<dt>2. The style tarball was formatted incorrectly.</p>
<dd> Some styles use the directories <code>~/.blackbox/Backgrounds </code> and <code>~/.blackbox/Styles</code> </p>
<p> This can fixed by adding a <code>[stylemenu] (~/.blackbox/Styles)</code> to your menu file. To be a complete purist, hack the style file with the correct paths and move the files into the correct directories</p>
<dt>3. The rootCommmand line is broken.</p>
<dd> The rootCommand line in the style file will run an arbitrary executable. It is important that this executable be set to bsetbg to maintain portability between systems with different graphics software. In addition bsetbg can execute a shell script and do it in a portable fashion as well.</p>
<dt><code>The documented method for creating styles is as follows:</code></p>
<dd>
<dt>1. Create or acquire the background for the style if</p>
<dd> it will not be using <code>bsetroot </code> to draw a patterned background for the root window. </p>
<pre>
<code>NOTE:</code>
Blackbox runs on a wide variety 
of systems ranging from PCs with 640x480 256 color 
displays to ultra high speed workstations with 25&quot; 
screens and extreme resolution. For best results a 
style graphic should be at least 1024x768.
</pre>
<dt>2. Create a style file.</p>
<dd> The best way to do this is to make a copy of a similar style and then edit it. </p>
<p> The style file is a list of X resources and other external variables. Manipulating these variables allows users to completely change the appearance of Blackbox. The user can also change the root window image by using the wrapper program <code>bsetbg.</code> </p>
<p> bsetbg knows how to use a number of programs to set the root window image. This makes styles much more portable since various platforms have different graphics software. For more info see <code>bsetbg (1).</code></p>
<dt>3. Background images should be placed in</p>
<dd> <code>~/.blackbox/backgrounds</code> The style file should be placed in <code>~/.blackbox/styles</code> any other information about the style should be placed in <code>~/.blackbox/about/STYLE_NAME/.</code> This would include README files, licenses, etc. </p>
<p> Previous versions of Blackbox put backgrounds and styles in different directories. The directories listed above are the only officially supported directories. However you may put them whereever you like as long as you update your menu file so it knows where to find your styles.</p>
<dt>4. To create a consistent experience and to ensure</p>
<dd> portability between all systems it is important to use the following format to create your style archive. </p>
<p> first create a new directory named after your style <code>NEW_STYLE</code> </p>
<p> In this directory create the directories </p>
<pre>
<code>backgrounds</code>
<code>styles</code>
<code>about/NEW_STYLE</code>
</pre>
<p> Next put everything for the theme in these locations. Finally type </p>
<p> tar cvzf NEW_STYLE.tar.gz * </p>
<p> If you are using commercial Unix you may need to use gzip and tar separately. </p>
<p> Now when a user downloads a new style file she knows that all she has to do is put the tarball in her Blackbox directory, unzip-&gt;un-tar it and then click on it in her style menu.</p>
<dt>
<dd></dl>
<h2>Style File Syntax and Details</h2>
<p> By far the easiest way to create a new style is to use bbconf. bbconf allows complete control of every facet of style files and gives immediate updates of the current style as changes are made. </p>
<p> The style file format is not currently documented in a man page. There is a readme document included with the Blackbox source containing this information.</p>
<h2>MENU FILE</h2>
<p> The default menu file is installed in <code>/usr/share/blackbox/menu.</code> This menu can be customized as a system default menu or the user can create a personal menu. </p>
<p> To create a personal menu copy the default menu to a file in your home directory. Then, open <code>~/.blackboxrc </code> and add or modify the resource <code>session.menuFile:</code><i> ~/.blackbox/menu</i> </p>
<p> Next, edit the new menu file. This can be done during a Blackbox session and the menu will automatically be updated when the code checks for file changes. </p>
<p> The default menu included with Blackbox has numerous comments describing the use of all menu commands. Menu commands follow this general form: </p>
<p> <code>[command]</code><i> (label|filename) {shell command|filename}</i></p>
<dl>
<dt><code>Blackbox menu commands:</code></p>
<dd>
<dt><code> # </code><i>string&#8230;</i></p>
<dd> Hash (or pound or number sign) is used as the comment delimiter. It can be used as a full line comment or as an end of line comment after a valid command statement.</p>
<dt><code>[begin]</code><i> (string)</i></p>
<dd> This tag is used only once at the beginning of the menu file. &quot;string&quot; is the name or description used at the top of the menu.</p>
<dt><code>[end] </code><i></i></p>
<dd> This tag is used at the end of the menu file and at the end of a submenu block.</p>
<dt><code>[exec]</code><i> (label string) {command string}</i></p>
<dd> This is a very flexible tag that allows the user to run an arbitrary shell command including shell scripts. If a command is too large to type on the command line by hand it is best to put it in a shell script.</p>
<dt><code>[nop]</code><i> (label string)</i></p>
<dd> This tag is used to put a divider in the menu. <i>label string</i> is an optional description.</p>
<dt><code>[submenu]</code><i> (submenu name) {title string}</i></p>
<dd> This creates a sub-menu with the name <i>submenu name</i> and if given, the string <i>title string</i> will be the title of the pop up menu itself.</p>
<dt><code>[include]</code><i> (filename)</i></p>
<dd> This command inserts <i>filename</i> into the menu file at the point at which it is called. <i>filename</i> should not contain a begin end pair. This feature can be used to include the system menu or include a piece of menu that is updated by a separate program.</p>
<dt><code>[stylesdir]</code><i> (description) (path)</i></p>
<dd> Causes Blackbox to search <i>path</i> for style files. Blackbox lists styles in the menu by their file name as returned by the OS.</p>
<dt><code>[stylesmenu]</code><i> (description) {path}</i></p>
<dd> This command creates a submenu with the name <code>description</code> with the contents of <code>path.</code> By creating a submenu and then populating it with stylesmenu entries the user can create an organized library of styles.</p>
<dt><code>[workspaces]</code><i> (description)</i></p>
<dd> Inserts a link into the main menu to the workspace menu. If used, <i>description</i> is an optional description.</p>
<dt><code>[config]</code><i> (label)</i></p>
<dd> This command causes Blackbox to insert a menu that gives the user control over focus models, dithering and other system preferences.</p>
<dt><code>[reconfig]</code><i> (label) {shell command}</i></p>
<dd> The reconfig command causes Blackbox to reread its configuration files. This does not include <code>~/.blackboxrc</code> which is only reread when Blackbox is restarted. If <i>shell command</i> is included Blackbox will run this command or shell script before rereading the files. This can be used to switch between multiple configurations</p>
<dt><code>[restart]</code><i> (label) {shell command}</i></p>
<dd> This command is actually an exit command that defaults to restarting Blackbox. If provided <code>shell command</code> is run instead of Blackbox. This can be used to change versions of Blackbox. Not that you would ever want to do this but, it could also be used to start a different window manager.</p>
<dt><code>[exit]</code><i> (label)</i></p>
<dd> Shuts down Blackbox. If Blackbox is the last command in your <code>~/.xinitrc</code> file, this action will also shutdown X. </p>
<pre><code>
Here is a working example of a menu file : [begin](MenuName)
                                               [exec](xterm) { xterm - ls - bg black - fg green }
                                                   [submenu](X utilities)
                                                       [exec](xcalc){xcalc}
                                                           [end]
                                                           [submenu](styles)
                                                               [stylesmenu](built - in styles){ / usr / share / blackbox / styles}
                                                                   [stylesmenu](custom styles){~ /.blackbox / styles}
                                                                       [end]
                                                                       [workspaces](workspace list)
                                                                           [config](configure)
                                                                               [reconfig](config play desktop){play - config - blackbox}
                                                                                   [reconfig](config work desktop){work - config - blackbox}
                                                                                       [restart](start Blackbox beta 7){blackbox - beta7}
                                                                                           [restart](start Blackbox cvs){blackbox - cvs}
                                                                                               [restart](restart)
                                                                                                   [exit](exit)
                                                                                                       [end]
</code></pre>
</dl>
<h2>RESOURCE FILE</h2>
<p> <code>$HOME</code><i>/.blackboxrc</i> These options are stored in the ~/.blackboxrc file. They control various features of Blackbox and most can be set from menus. Some of these can only be set by editing .blackboxrc directly. </p>
<p> NOTE: Blackbox only reads this file during start up. To make changes take effect during a Blackbox session the user must choose &quot;restart&quot; on the main menu. If you do not do so, your changes will be lost when Blackbox exits. </p>
<p> Some resources are named with a &lt;num&gt; after screen. This should be replaced with the number of the screen that is being configured. The default is 0 (zero).</p>
<dl>
<dt><i>Menu Configurable</i><code> (Slit Menu):</code></p>
<dd> Right click (button 3) on the slit border.</p>
<dt><code>session.screen&lt;num&gt;.slit.placement</code><i> SEE BELOW</i></p>
<dd> Determines the position of the slit. Certain combinations of slit.placement with slit.direction are not terribly useful, i.e. TopCenter with Vertical direction puts the slit through the middle of your screen. Certainly some will think that is cool if only to be different&#8230; </p>
<pre>
<code>Default is CenterLeft.</code>
[  TopLeft  |   TopCenter  |   TopRight  | 
 CenterLeft |              | CenterRight |
 BottomLeft | BottomCenter | BottomRight ]
</pre>
<dt><code>session.screen&lt;num&gt;.slit.direction</code><i> [Horizontal|Vertical]</i></p>
<dd> Determines the direction of the slit. </p>
<pre>
<code>Default is Vertical.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.slit.onTop</code><i> [True|False]</i></p>
<dd> Determines whether the slit is always visible over windows or if the focused window can hide the slit. </p>
<pre>
<code>Default is True.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.slit.autoHide</code><i> [True|False]</i></p>
<dd> Determines whether the slit hides when not in use. The session.autoRaiseDelay time determines how long you must hover to get the slit to raise and how long it stays visible after mouse out. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><i>Menu Configurable</i><code> (Main Menu):</code></p>
<dd>
<dt><code>session.screen&lt;num&gt;.focusModel</code><i> SEE BELOW</i></p>
<dd> Sloppy focus (mouse focus) is the conventional X Window behavior and can be modified with AutoRaise or Click-Raise. </p>
<p> AutoRaise causes the window to automatically raise after session.autoRaiseDelay milliseconds. </p>
<p> ClickRaise causes the window to raise if you click anywhere inside the client area of the window. </p>
<p> Sloppy focus alone requires a click on the titlebar, border or lower grip to raise the window. </p>
<p> ClickToFocus requires a click on a Blackbox decoration or in the client area to focus and raise the window. ClickToFocus cannot be modified by AutoRaise or ClickRaise. </p>
<pre><code>
Default is SloppyFocus
    [SloppyFocus [[AutoRaise &amp; ClickRaise] |
                  [AutoRaise | ClickRaise]] |
     ClickToFocus]
</code></pre>
<dt><code>session.screen&lt;num&gt;.windowPlacement</code><i> SEE BELOW</i></p>
<dd> RowSmartPlacement tries to fit new windows in empty space by making rows. Direction depends on session.screen&lt;num&gt;.rowPlacementDirection </p>
<p> ColSmartPlacement tries to fit new windows in empty space by making columns Direction depends on session.screen&lt;num&gt;.colPlacementDirection </p>
<p> CascadePlacement places the new window down and to the right of the most recently created window. </p>
<pre>
<code>Default is RowSmartPlacement.</code>
[RowSmartPlacement | ColSmartPlacement | CascadePlacement]
</pre>
<dt><code>session.screen&lt;num&gt;.rowPlacementDirection</code><i> [LeftToRight|RightToLeft]</i></p>
<dd> Determines placement direction for new windows. </p>
<pre>
<code>Default is LeftToRight.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.colPlacementDirection</code><i> [TopToBottom|BottomToTop]</i></p>
<dd> Determines placement direction for new windows. </p>
<pre>
<code>Default is TopToBottom.</code>
</pre>
<dt><code>session.imageDither</code><i> [True|False]</i></p>
<dd> This setting is only used when running in low color modes. Image Dithering helps to show an image properly even if there are not enough colors available in the system. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><code>session.opaqueMove</code><i> [True|False]</i></p>
<dd> Determines whether the window&#8217;s contents are drawn as it is moved. When False the behavior is to draw a box representing the window. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.fullMaximization</code><i> [True|False]</i></p>
<dd> Determines if the maximize button will cause an application to maximize over the slit and toolbar. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.focusNewWindows</code><i> [True|False]</i></p>
<dd> Determines if newly created windows are given focus after they initially draw themselves. </p>
<pre>
<code>Default is False. </code>
</pre>
<dt><code>session.screen&lt;num&gt;.focusLastWindow</code><i> [True|False]</i></p>
<dd> This is actually &quot;when moving between workspaces, remember which window has focus when leaving a workspace and return the focus to that window when I return to that workspace.&quot; </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.disableBindingsWithScrollLock</code><i> [True|False]</i></p>
<dd> When this resource is enabled, turning on scroll lock keeps Blackbox from grabbing the Alt and Ctrl keys that it normally uses for mouse controls. This feature allows users of drawing and modeling programs which use keystrokes to modify mouse actions to maintain their sanity. *NOTE* this has _no_ affect on bbkeys. If you need bbkeys to also behave this way it has a similar option in its config file. Refer to the bbkeys manpage for details. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><i>Menu Configurable</i><code> (Workspace Menu):</code></p>
<dd> Middle click (button 2) on the root window (AKA Desktop) to reach this menu</p>
<dt><code>session.screen&lt;num&gt;.workspaces</code><i> [integer]</i></p>
<dd> Workspaces may be created or deleted by middle clicking on the desktop and choosing &quot;New Workspace&quot; or &quot;Remove Last&quot;. After creating a workspace, right click on the toolbar to name it. </p>
<pre>
<code>Default is 1</code>
</pre>
<dt><i>Menu Configurable</i><code> (Toolbar Menu):</code></p>
<dd>
<dt><code>session.screen&lt;num&gt;.workspaceNames</code><i> [string[, string&#8230;]]</i></p>
<dd> Workspaces are named in the order specified in this resource. Names should be delimited by commas. If there are more workspaces than explicit names, un-named workspaces will be named as &quot;Workspace [number]&quot;. </p>
<pre>
<code>Default is </code>
Workspace 1.
</pre>
<dt><code>session.screen&lt;num&gt;.toolbar.placement</code><i> SEE BELOW</i></p>
<dd> Set toolbar screen position. </p>
<pre>
<code>Default is BottomCenter</code>
[  TopLeft  |   TopCenter  |   TopRight  | 
 BottomLeft | BottomCenter | BottomRight ]
</pre>
<dt><code>session.screen&lt;num&gt;.toolbar.onTop</code><i> [True|False]</i></p>
<dd> Determines whether the toolbar is always visible over windows or if the focused window can hide the toolbar. </p>
<pre>
<code>Default is True.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.toolbar.autoHide</code><i> [True|False]</i></p>
<dd> Determines whether the toolbar hides when not in use. The session.autoRaiseDelay time determines how long you must hover to get the toolbar to raise, and how long it stays visible after mouse out. </p>
<pre>
<code>Default is False.</code>
</pre>
<dt><i>Configurable in</i><code> ~/.Blackboxrc only:</code></p>
<dd>
<dt><code>session.screen&lt;num&gt;.toolbar.widthPercent</code><i> [1-100]</i></p>
<dd> Percentage of screen used by the toolbar. A number from 1-100 that sets the width of the toolbar. 0 (zero) does not cause the toolbar to disappear, instead the toolbar is set to the default. If you want to lose the toolbar there are patches that can remove it. </p>
<pre>
<code>Default is 66.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.strftimeFormat</code><i> [string]</i></p>
<dd> A C language date format string, any combination of specifiers can be used. The default is %I:%M %p which generates a 12 hour clock with minutes and an am/pm indicator appropriate to the locale. </p>
<pre>
<i>24 hours and minutes</i><code>    %H:%M</code>
<i>12 hours and minute</i><code>     %I:%M %p</code>
<i>month/day/year</i><code>          %m/%d/%y</code>
<i>day/month/year</i><code>          %d/%m/%y</code>
</pre>
<pre>
<code>Default is hours:minutes am/pm</code>
See
<code>strftime 3</code>
for more details.
</pre>
<dt><code>session.screen&lt;num&gt;.dateFormat</code><i> [American|European]</i></p>
<dd> NOTE: Only used if the strftime() function is not available on your system. </p>
<pre>
<code>Default is American, (mon/day/year).</code>
</pre>
<dt><code>session.screen&lt;num&gt;.clockFormat</code><i> [12/24]</i></p>
<dd> <code>NOTE: </code> Only used if the strftime() function is not available on your system. </p>
<pre>
<code>Default is 12-hour format.</code>
</pre>
<dt><code>session.screen&lt;num&gt;.edgeSnapThreshold</code><i> [integer]</i></p>
<dd> When set to 0 this turns off edge snap. When set to one or greater edge snap will cause a window that is being moved to snap to the nearest screen edge, the slit, or or the toolbar. Windows will not snap to each other. The value represents a number in pixels which is the distance between the window and a screen edge which is required before the window is snapped to the screen edge. If you prefer this functionality values between 6 &#8211; 10 work nicely. </p>
<pre>
<code>Default value is 0</code>
</pre>
<dt><code>session.menuFile</code><i> [filepath]</i></p>
<dd> Full path to the current menu file. </p>
<pre>
<code>Default is /usr/share/blackbox/menu</code>
</pre>
<dt><code>session.colorsPerChannel</code><i> [2-6]</i></p>
<dd> The number of colors taken from the X server for use on pseudo color displays. This value must be set to 4 for 8 bit displays. </p>
<pre>
<code>Default is 4.</code>
</pre>
<dt><code>session.doubleClickInterval</code><i> [integer]</i></p>
<dd> This is the maximum time that Blackbox will wait after one click to catch a double click. This only applies to Blackbox actions, such as double click shading, not to the X server in general. </p>
<pre>
<code>Default is 250 milliseconds.</code>
</pre>
<dt><code>session.autoRaiseDelay</code><i> [integer]</i></p>
<dd> This is the time in milliseconds used for auto raise and auto hide behaviors. More than about 1000 ms is likely useless. </p>
<pre>
<code>Default is 250 millisecond.</code>
</pre>
<dt><code>session.cacheLife</code><i> [integer]</i></p>
<dd> Determines the maximum number of minutes that the X server will cache unused decorations. </p>
<pre>
<code>Default is 5 minutes</code>
</pre>
<dt><code>session.cacheMax</code><i> [integer]</i></p>
<dd> Determines how many kilobytes that Blackbox may take from the X server for storing decorations. Increasing this number may enhance your performance if you have plenty of memory and use lots of different windows. </p>
<pre>
<code>Default is 200 Kilobytes</code>
</pre>
</dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>HOME</code></p>
<dd> Blackbox uses $HOME to find its .blackboxrc rc file and its .blackbox directory for menus and style directories.</p>
<dt><code>DISPLAY</code></p>
<dd> If a display is not specified on the command line, Blackbox will use the value of $DISPLAY. </p>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>blackbox</code></p>
<dd> Application binary</p>
<dt><code>~/.blackboxrc</code></p>
<dd> User&#8217;s startup and resource file.</p>
<dt><code>/usr/share/blackbox/menu</code></p>
<dd> Default system wide menu <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>
</dl>
<h2>WEB SITES</h2>
<dl>
<dt>
<dd> <code>General info website:</code> <a rel="nofollow" href="http://blackboxwm.sourceforge.net/">http://blackboxwm.sourceforge.net/</a></p>
<dt>
<dd> <code>Development website:</code> <a rel="nofollow" href="http://sourceforge.net/projects/blackboxwm/">http://sourceforge.net/projects/blackboxwm/</a> </p>
</dl>
<h2>BUGS</h2>
<p> If you think you have found a bug, please help by going to the development website and select &quot;Bugs&quot; in the upper menu. Check the bug list to see if your problem has already been reported. If it has please read the summary and add any information that you believe would help. If your bug has not been submitted select &quot;Submit New&quot; and fill out the form. </p>
<h2>AUTHORS AND HISTORY</h2>
<p> <code>Sean Shaleh Perry </code> <i> &lt;shaleh [at] debian.org&gt; </i> is the current maintainer and is actively working together with Brad to keep Blackbox up-to-date and stable as a rock. </p>
<p> <code>Brad Hughes</code><i> &lt;bhughes [at] trolltech.com&gt;</i> originally designed and coded Blackbox in 1997 with the intent of creating a memory efficient window manager with no dependencies on external libraries. Brad&#8217;s original idea has become a popular alternative to other window managers. </p>
<p> <code>Jeff Raven</code><i> &lt;jraven [at] psu.edu&gt;</i> then picked up the torch for the 0.61.x series after Brad took a full time job at TrollTech. </p>
<p> This manual page was written by: <code>R.B. Brig Young </code> <i> &lt;secretsaregood [at] yahoo.com&gt; </i> he is solely responsible for errors or omissions. Comments, corrections, and suggestions are welcomed. </p>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-bsetbg/">bsetbg</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-bsetroot/">bsetroot</a>(1), 
<a href="//www.systutorials.com/docs/linux/man/1-bbkeys/">bbkeys</a>(1), <a href="//www.systutorials.com/docs/linux/man/1-bbconf/">bbconf</a>(1)
</pre>
<h2>Index</h2>
