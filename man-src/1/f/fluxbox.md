---
title: "fluxbox(1)"
name: "fluxbox"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fluxbox/"
description: "fluxbox – A lightweight window manager for the X Windowing System"
---

<h2 class="name">NAME</h2>
<p> fluxbox &#8211; A lightweight window manager for the X Windowing System </p>
<h2>SYNOPSIS</h2>
<p> <code>fluxbox</code> [-rc <i>rcfile</i>] [-log <i>logfile</i>] [-display <i>display</i>] [-screen all|<i>scr</i>,<i>scr</i>&#8230;] [-verbose] [-sync] </p>
<p> <code>fluxbox</code> [-v | -version] | [-h | -help] | [-i | -info] | [-list-commands]</p>
<h2>DESCRIPTION</h2>
<p> <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> is a window manager. As such it provides configurable window decorations, a root menu to launch applications and a toolbar that shows the current workspace name, a set of application names and the current time. There is also a workspace menu to add or remove workspaces. </p>
<p> Fluxbox can iconify (or minimize) windows to the toolbar One click and they reappear. A double-click on the titlebar of the window will <i>shade</i> it; i.e. the window will disappear, and only the titlebar will remain visible. </p>
<p> There are also two areas commonly used by small applets: the &#8216;slit&#8217; can be used to dock small applications; e.g. most of the &#8220;bbtools&#8221; and &#8220;Window Maker dockapps&#8221; can use the slit, and the &#8216;systray&#8217; which lives in the toolbar supports standard system tray icons provided by some applications. </p>
<p> Fluxbox uses its own graphics class to render its images on the fly. By using style files, you can determine in great detail how your desktop looks. fluxbox styles are compatible with those of Blackbox 0.65 or earlier versions, so users migrating can still use their current favourite themes. </p>
<p> Most of the default keyboard and mouse button actions mentioned in this manual can be changed and configured in the &#8216;keys&#8217; file. This powerful configuration file can also be used to automate almost any action you may want to perform, from launching applications to moving windows around the screen. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> for details. </p>
<p> Fluxbox can also remember certain attributes of individual application windows and restore these settings the next time the window opens. See the <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for details. </p>
<p> Fluxbox supports the majority of the Extended Window Manager Hints (EWMH) specification, as well as numerous other Window Hinting standards. This allows all compliant window managers to provide a common interface to standard features used by applications and desktop utilities.</p>
<h2>OPTIONS</h2>
<p> <code>-display</code> <i>display</i></p>
<dl>
<dt>
<dd> Start fluxbox on the specified display. Programs started by fluxbox will share the DISPLAY environment variable also.</dl>
<p> <code>-h</code>, <code>-help</code></p>
<dl>
<dt>
<dd> Display command line options.</dl>
<p> <code>-i</code>, <code>-info</code></p>
<dl>
<dt>
<dd> Display useful information concerning the defaults and compiled-in options.</dl>
<p> <code>-log</code> <i>logfile</i></p>
<dl>
<dt>
<dd> Starting fluxbox with this option will designate a file in which you want to log events to.</dl>
<p> <code>-rc</code> <i>rcfile</i></p>
<dl>
<dt>
<dd> Use a different config file other than the default <code>~/.fluxbox/init</code>.</dl>
<p> <code>-v</code>, <code>-version</code></p>
<dl>
<dt>
<dd> The version of fluxbox installed.</dl>
<p> <code>-screen</code> all|<i>scr</i>,<i>scr</i>&#8230;</p>
<dl>
<dt>
<dd> Run on specified screens only or all (by default).</dl>
<p> <code>-verbose</code></p>
<dl>
<dt>
<dd> Print more information in process.</dl>
<p> <code>-sync</code></p>
<dl>
<dt>
<dd> Synchronize with the X server for debugging.</dl>
<p> <code>-list-commands</code></p>
<dl>
<dt>
<dd> Lists all available internal commands.</dl>
<h2>STARTING FLUXBOX</h2>
<p> <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> comes with a program called <code><a href="/docs/linux/man/1-startfluxbox/">startfluxbox</a>(1)</code> usually located wherever you installed fluxbox. This script provides you with many options and variables that can be set when starting fluxbox. To actually call fluxbox and begin using it, you should place &#8220;exec startfluxbox&#8221; in your <code>~/.xinitrc</code> as the last executed command. This is assuming that the location of <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> and <code><a href="/docs/linux/man/1-startfluxbox/">startfluxbox</a>(1)</code> are in your shell&#8217;s $PATH. Also note that you may need to create the <code>~/.xinitrc</code> file or your setup may use <code>~/.xsession</code> instead, depending on your X setup. Some X login managers like <code><a href="/docs/linux/man/1-gdm/">gdm</a>(1)</code> or <code><a href="/docs/linux/man/1-kdm/">kdm</a>(1)</code> may simply provide a &#8220;Fluxbox&#8221; session for you without having to alter any settings. </p>
<p> By using fluxbox -i you&#8217;ll see the defaults used by <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code>. These are what fluxbox looks for upon startup. In the list of &#8220;Defaults:&#8221; you&#8217;ll see a menu file location, this is where you can provide a system-wide menu file for your users. </p>
<p> On exit or restart, fluxbox will save user defaults in the file <code>~/.fluxbox/init</code>. Resources in this file can also be edited by hand, see the <code>RESOURCES</code> section for more details. <code><a href="/docs/linux/man/1-fluxbox/">fluxbox</a>(1)</code> also has many tools to edit these; look through the main menu once fluxbox has started to find different ways of managing your session.</p>
<h2>USING FLUXBOX</h2>
<p> When using fluxbox for the first time, users who are more accustomed to full desktop environments such as KDE or Gnome may be a little surprised by the minimal screen content. fluxbox is designed to be fast and powerful, so it may take a bit of getting used to &#8212; however, the rewards are worthwhile. </p>
<p> In this section, we&#8217;ll give a quick summary of the common things. However, we recommend that you consult the referenced sections of this manual to further develop your understanding of what you can do with fluxbox.</p>
<h3>Root Window (Main)</h3>
<p> Looking at the fluxbox desktop immediately after startup you&#8217;ll generally see only one thing: the toolbar. If you right-click (mouse button 3) somewhere on the desktop, you can access the Root Menu. A middle-click (mouse button 2) on the desktop shows you the Workspace Menu.</p>
<h3>Root Menu and Workspace Menu</h3>
<p> From the RootMenu you can launch applications and configure fluxbox. The WorkspaceMenu shows all windows and on which workspaces they are. See section <code>MENUS</code> on how to customize these menus.</p>
<h3>Toolbar</h3>
<p> The toolbar contains any combination of the following tools, by default in this order: </p>
<dl>
<dt>
<dd> &bull; <code>Workspace Name</code>: Name of the current visible workspace</dl>
<dl>
<dt>
<dd> &bull; <code>Workspace Arrows</code>: Previous/Next Workspace</dl>
<dl>
<dt>
<dd> &bull; <code>Iconbar</code>: List of windows managed by fluxbox</dl>
<dl>
<dt>
<dd> &bull; <code>Window Arrows</code>: Previous/Next Application Window</dl>
<dl>
<dt>
<dd> &bull; <code>System Tray</code>: Area for applets</dl>
<dl>
<dt>
<dd> &bull; <code>Clock</code>: Date and Time</dl>
<p> The contents and behavior of the toolbar can be configured, see the <code>TOOLBAR</code> section for details.</p>
<h3>Slit</h3>
<p> Initially you won&#8217;t be able to see the slit. It is there, but it isn&#8217;t being used yet, which confuses some people initially. Think of it as a dock where you can place smaller programs. If you&#8217;ve looked at any screenshots on the official fluxbox web site, you will have noticed some small programs on the edge of some of the screens. These were more than likely docked programs in the slit. To learn more about the slit, we have an entire <code>SLIT</code> section below that goes into detail about the options you have.</p>
<h3>Layers</h3>
<p> fluxbox manages the following layers (from highest to lowest): </p>
<dl>
<dt>
<dd> &bull; Above Dock</dl>
<dl>
<dt>
<dd> &bull; Dock</dl>
<dl>
<dt>
<dd> &bull; Top</dl>
<dl>
<dt>
<dd> &bull; Normal</dl>
<dl>
<dt>
<dd> &bull; Bottom</dl>
<dl>
<dt>
<dd> &bull; Desktop</dl>
<p> Windows on a higher layer will always appear above those on a lower one. These layers can be used on application windows, the slit or the toolbar. You can assign applications to a certain layer by specifying it in the &#8216;apps&#8217; file or through the WindowMenu. We discuss the &#8216;apps&#8217; file in <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code>. We discuss the WindowMenu in the <code>MENUS</code> section. We discuss layers in more detail in the <code>LAYERS</code> section.</p>
<h3>Focus Model</h3>
<p> The window that has the focus is the one that receives key and mouse events. The focus model is selectable via the Configuration menu located in the root menu. We&#8217;ll discuss the different types of focus below in the <code>FOCUS MODEL</code> section.</p>
<h3>Windows</h3>
<p> A left-click (mouse button 1) on any part of the window&#8217;s border will raise it. Dragging then moves the window to another part of the desktop. A right click and drag on the border resizes the window. Dragging the resize grips at the left and right bottom corners also will resize the window. Middle clicking on a border or titlebar will immediately lower the window. Right clicking on the titlebar opens the Window menu. The commands unique to this menu are discussed in detail in the <code>Window Menu</code> section.</p>
<h3>Tabs</h3>
<p> fluxbox allows windows to be &#8216;grouped&#8217; by middle clicking and holding on a window&#8217;s tab and dragging it onto another window. This &#8216;tabbing&#8217; allows you to put multiple applications in one location on the desktop and do several operations (for example, moving or resizing) to all windows in the group. By default, tabs are located just above the window, but they may be embedded in the titlebar or moved to other locations on the outside of the window. Configuration is discussed in TAB OPTIONS section. </p>
<p> You can also set up automatic grouping using the &#8216;apps&#8217; file. See <code>GROUP SECTIONS</code> in <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for details.</p>
<h3>Key Bindings</h3>
<p> There are a number of key bindings set up by default, which can be configured and extended to just about anything you can imagine with the keyboard. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> for details on how to do this. </p>
<p> The default bindings set up by fluxbox are as follows: </p>
<p> Mouse clicks on the empty desktop: </p>
<dl>
<dt>
<dd> &bull; <code>Left-click</code> (Button 1): hides all fluxbox menus</dl>
<dl>
<dt>
<dd> &bull; <code>Middle-click</code> (Button 2): shows the Workspace Menu</dl>
<dl>
<dt>
<dd> &bull; <code>Right-click</code> (Button 3): shows the Root Menu</dl>
<dl>
<dt>
<dd> &bull; <code>Scroll wheel</code> (Buttons 4 and 5): jump to the previous/next workspace</dl>
<p> Mouse gestures on a window: </p>
<dl>
<dt>
<dd> &bull; <code>ALT+Drag Left-click</code> anywhere on a window moves the window.</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+Drag Right-click</code> anywhere on a window resizes the window.</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+Middle-click</code> anywhere on a window lowers the current window.</dl>
<p> Mouse gestures on a window&#8217;s titlebar: </p>
<dl>
<dt>
<dd> &bull; <code>CTRL+Drag Left-click</code> on a window&#8217;s titlebar lets you drag to attach the window to another&#8217;s tab group</dl>
<dl>
<dt>
<dd> &bull; <code>Double Left-click</code> on a window&#8217;s titlebar shades the window</dl>
<dl>
<dt>
<dd> &bull; <code>Middle-click</code> on a window&#8217;s titlebar lowers the window</dl>
<dl>
<dt>
<dd> &bull; <code>Right-click</code> on a window&#8217;s titlebar pops up the <code>Window Menu</code></dl>
<p> Mouse gestures on the toolbar: </p>
<dl>
<dt>
<dd> &bull; <code>Scroll wheel</code> on the toolbar cycles through windows</dl>
<p> Keyboard bindings: </p>
<dl>
<dt>
<dd> &bull; <code>ALT+Tab</code> / <code>ALT+Shift+Tab</code>: Cycle through windows</dl>
<dl>
<dt>
<dd> &bull; <code>WIN+Tab</code> / <code>WIN+Shift+Tab</code>: Cycle through tabs</dl>
<dl>
<dt>
<dd> &bull; <code>WIN+1</code> &#8211; <code>WIN+9</code>: Select the 1st &rarr; 9th tab in the current window</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F1</code>: Run <code><a href="/docs/linux/man/1-xterm/">xterm</a>(1)</code> to open a new terminal</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F2</code>: Run <code><a href="/docs/linux/man/1-fbrun/">fbrun</a>(1)</code> for a small &#8220;run program&#8221; dialog</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F4</code>: Close the current window</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F5</code>: Kill the current window (like <code><a href="/docs/linux/man/1-xkill/">xkill</a>(1)</code>)</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F9</code>: Minimize (iconify) the current window</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F10</code>: Maximize the current window</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+F11</code>: Full-screen the current window</dl>
<dl>
<dt>
<dd> &bull; <code>ALT+Space</code>: Open the <code>Window Menu</code></dl>
<dl>
<dt>
<dd> &bull; <code>CTRL+ALT+Del</code>: Exit fluxbox (log out)</dl>
<dl>
<dt>
<dd> &bull; <code>CTRL+ALT+Left</code> / <code>CTRL+ALT+Right</code>: Go to the previous/next workspace</dl>
<dl>
<dt>
<dd> &bull; <code>WIN+Left</code> / <code>WIN+Right</code>: Send the current window to the previous/next workspace, but remain on this workspace</dl>
<dl>
<dt>
<dd> &bull; <code>CTRL+WIN+Left</code> / <code>CTRL+WIN+Right</code>: Take the current window to the previous/next workspace, and switch to that workspace</dl>
<dl>
<dt>
<dd> &bull; <code>CTRL+F1</code> &#8211; <code>CTRL+F12</code>: Switch to the 1st &rarr; 12th workspace</dl>
<dl>
<dt>
<dd> &bull; <code>WIN+F1</code> &#8211; <code>WIN+F12</code>: Send the current window to a specific workspace</dl>
<dl>
<dt>
<dd> &bull; <code>CTRL+WIN+F1</code> &#8211; <code>CTRL+WIN+F12</code>: Take the current window to a specific workspace</dl>
<h2>MENUS</h2>
<p> fluxbox provides a popup menu facility that is used by a few different types of native menus. </p>
<p> When a menu is open, you can click on items with the mouse to activate them. Some special menu items react slightly differently depending on the mouse button you use, but normally you will want to use a left-click (button 1). </p>
<p> You can also use the the keyboard arrow key to navigate, or even type the first few letters of the item&#8217;s label to select it, and &#8220;enter&#8221; to activate the item. </p>
<p> Normally activating a menu item should close the menu. You can also right-click the title are of a menu or press &#8220;esc&#8221; to close it without activating an item.</p>
<h3>Root Menu</h3>
<p> The root menu is where you can launch commonly-used applications and change different aspects of fluxbox by simply clicking on a menu item. By default it is opened by a right-click on the empty area of the desktop. </p>
<p> The contents of this menu can be configured, see <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code> for details. </p>
<p> The default menu, which is created by the &#8220;fluxbox-generate_menu&#8221; command, contains menus for installed applications, as well as a special &#8220;Fluxbox menu&#8221; item with the items detailed below: </p>
<p> <code>Configure</code></p>
<dl>
<dt>
<dd> The next level under this menu is where you can set certain resources and really begin to customize the look and feel of your desktop. See the <code>Configure Menu</code> section below for more details.</dl>
<p> <code>System Styles</code></p>
<dl>
<dt>
<dd> This is where the standard styles are listed. You can select one of these by clicking on it, and it will be applied immediately. System styles are located in <code>/usr/local/share/fluxbox/styles/</code> upon a default install. Remember that you can confirm this with fluxbox -i. </p>
<p> <code>User Styles</code></p>
<dl>
<dt>
<dd> This is where your custom styles are listed. It will list any styles from <code>~/.fluxbox/styles/</code>, which may be styles you grab from the Internet, or your own custom styles, provided you follow the standards described in <code><a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5)</code>.</dl>
<p> <code>Workspace List</code></p>
<dl>
<dt>
<dd> This is the same as the <code>Workspace Menu</code> detailed below.</dl>
<p> <code>Tools</code></p>
<dl>
<dt>
<dd> Listed here are different tools that you can use. You can rename your workspace, run programs from a command line or regenerate your menu.</dl>
<p> <code>Window Managers</code></p>
<dl>
<dt>
<dd> Allows you to switch your window manager. (Only listed if you have other window managers/desktop environments installed.)</dl>
<p> <code>Lock Screen</code></p>
<dl>
<dt>
<dd> Locks the screen, if a suitable locking program has been detected.</dl>
<p> <code>Fluxbox Command</code></p>
<dl>
<dt>
<dd> A little Commandline will popup where you can enter a fluxbox command. These commands are the same as those detailed in <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code>.</dl>
<p> <code>Reload config</code></p>
<dl>
<dt>
<dd> Use this to reload the fluxbox configuration files. You must do this after editing the &#8216;keys&#8217; file, &#8216;init&#8217; file, or the current style.</dl>
<p> <code>Restart</code></p>
<dl>
<dt>
<dd> Restart the whole darn thing. This starts a completely new fluxbox process, rereads files and redraws all graphical elements. Running applications will remain open, however, and restored to the same workspaces they were previously in once fluxbox returns.</dl>
<p> <code>Exit</code></p>
<dl>
<dt>
<dd> Exits fluxbox, which in turn either shuts down the X Window server or returns you to the graphical login screen.</dl>
</dl>
<h3>Configuration Menu</h3>
<p> This menu offers the opportunity to set up fluxbox. It contains many options which can be altered manually in the &#8216;init&#8217; file, but this is an easier and faster way to change the most common settings. </p>
<p> All changes take effect immediately. </p>
<p> <code>Focus Model</code></p>
<dl>
<dt>
<dd> Lets you configure the window focus model. For details, see <code>FOCUS MODEL</code>, below.</dl>
<p> <code>Maximize Options</code></p>
<dl>
<dt>
<dd> Lets you configure what happens when you maximize a window. The four options are: </p>
<p> <code>Full Maximization</code>:</p>
<dl>
<dt>
<dd> Normally, a maximized window will not overlap the toolbar, slit, or any docked windows (like panels). Enabling this option allows maximized windows to be as large as the actual screen resolution.</dl>
<p> <code>Ignore Resize Increment</code>:</p>
<dl>
<dt>
<dd> Normally, terminal windows specify a &#8220;resize increment&#8221; which mean fluxbox will only resize the window to an even multiple of the character size. Enabling this option will ignore this specification when maximizing.</dl>
<p> <code>Disable Moving</code> / <code>Disable Resizing</code>:</p>
<dl>
<dt>
<dd> Normally, maximized windows can still be moved and resized. Enabling these options prevents these behaviour.</dl>
</dl>
<p> <code>Tab Options</code></p>
<dl>
<dt>
<dd> Lets you configure the properties of tabs. Detailed in <code>TAB OPTIONS</code>, below.</dl>
<p> <code>Slit</code></p>
<dl>
<dt>
<dd> This menu can also be found by right-clicking the slit (if visible). Find more information about this menu&#8217;s options in the <code>Slit Menu</code> section, below.</dl>
<p> <code>Toolbar</code></p>
<dl>
<dt>
<dd> This menu can also be found by right-clicking any non-icon part of the toolbar. Find more information about this menu&#8217;s options in the <code>Toolbar Menu</code> section, below.</dl>
<p> <code>Transparency</code></p>
<dl>
<dt>
<dd> This sets the default transparency for a focused windows, unfocused window and the menu. Use the left mouse button to decrease and the right mouse button to increase the value. 0 is invisible, 255 is not transparent at all. </p>
<p> The transparency of individual application windows can be overridden in the &#8216;apps&#8217; file (<code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code>). </p>
<p> The <code>Force Pseudo Transparency</code> option will force fluxbox to ignore the xcomposite extension and use pseudo-transparency instead of true transparency. Note: When pseudo-transparency is on, the transparency values here only affect titlebars, not window contents.</dl>
<p> <code>Opaque Window Moving</code></p>
<dl>
<dt>
<dd> If enabled, you will see the window content while dragging it. Otherwise only an outline of the window will be shown.</dl>
<p> <code>Workspace Warping</code></p>
<dl>
<dt>
<dd> If enabled, you can drag windows from one workspace to another. The previous workspace is to the left, the next workspace is to the right.</dl>
<h3>Window Menu</h3>
<p> The Window menu is displayed when you right click on the titlebar of a window. </p>
<p> To customize this menu, see the <code>WINDOW MENU</code> section of <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code>. </p>
<p> By default, this menu contains: </p>
<p> <code>Shade</code></p>
<dl>
<dt>
<dd> Shade the window (display the titlebar only).</dl>
<p> <code>Stick</code></p>
<dl>
<dt>
<dd> (Un)Stick window. A &#8216;stuck&#8217; window will always be displayed on all workspaces.</dl>
<p> <code>Send To&#8230;</code></p>
<dl>
<dt>
<dd> Send window to another workspace. When you select the workspace with a middle click, fluxbox will send you along with the application to the selected workspace.</dl>
<p> <code>Maximize</code></p>
<dl>
<dt>
<dd> (Un)Maximize window. Depending on your toolbar and slit configuration, maximize may cover them. You can use the different mouse buttons for different aspects of maximize function. </p>
<dl>
<dt>
<dd> &bull; Button 1 (Un)Maximize as normal.</dl>
<dl>
<dt>
<dd> &bull; Button 2 (Un)Maximize window vertically.</dl>
<dl>
<dt>
<dd> &bull; Button 3 (Un)Maximize window horizontally.</dl>
</dl>
<p> <code>Iconify</code></p>
<dl>
<dt>
<dd> Iconify (or minimize) a window. The &#8216;icon&#8217; can be found in the Icons submenu of the workspace menu as well as in the toolbar (if a Toolbar mode showing Icons is selected).</dl>
<p> <code>Raise</code></p>
<dl>
<dt>
<dd> Raise the window above all others in the same layer.</dl>
<p> <code>Lower</code></p>
<dl>
<dt>
<dd> Lower the window below all others in the same layer.</dl>
<p> <code>Layer&#8230;</code></p>
<dl>
<dt>
<dd> Change the layer of this window. See <code>LAYERS</code> for more details.</dl>
<p> <code>Transparency</code></p>
<dl>
<dt>
<dd> Change this window&#8217;s transparency, overriding the defaults from the <code>Configuration Menu</code>.</dl>
<p> <code>Remember&#8230;</code></p>
<dl>
<dt>
<dd> Specify which window settings should be stored in the &#8216;apps&#8217; file and resumed the next time this window is opened. </p>
<p> Specifically the setting you may store are: </p>
<p> <code>Workpace:</code></p>
<dl>
<dt>
<dd> Open this in the same workspace as where the window currently resides.</dl>
<p> <code>Jump to workspace:</code></p>
<dl>
<dt>
<dd> When <code>Workspace</code> is selected, fluxbox will jump to the appropriate workspace when this window is opened there. If not selected, the window will open in the background.</dl>
<p> <code>Head</code>:</p>
<dl>
<dt>
<dd> For xinerama users only, start this window on the current head (or screen).</dl>
<p> <code>Dimensions</code>:</p>
<dl>
<dt>
<dd> Record the current window height and width.</dl>
<p> <code>Position</code>:</p>
<dl>
<dt>
<dd> Record the current X and Y coordinates of the window.</dl>
<p> <code>Sticky</code>:</p>
<dl>
<dt>
<dd> Record whether the window is on all desktops, or not.</dl>
<p> <code>Decorations</code>:</p>
<dl>
<dt>
<dd> Record the current set of decorations (title bar, grips, tabs, etc) on the window.</dl>
<p> <code>Shaded</code>:</p>
<dl>
<dt>
<dd> Record whether the window is shaded (or rolled-up) or not.</dl>
<p> <code>Minimized</code>:</p>
<dl>
<dt>
<dd> Record whether the window is iconified (or minimized) or not.</dl>
<p> <code>Maximized</code>:</p>
<dl>
<dt>
<dd> Record whether the window is maximized or not.</dl>
<p> <code>Fullscreen</code>:</p>
<dl>
<dt>
<dd> Record whether the window is in fullscreen mode or not.</dl>
<p> <code>Transparency</code>:</p>
<dl>
<dt>
<dd> Record the current <code>Transparency</code> settings.</dl>
<p> <code>Layer</code>:</p>
<dl>
<dt>
<dd> Record the current layer.</dl>
<p> <code>Save on close</code>:</p>
<dl>
<dt>
<dd> If selected, any of the above items which are also selected will be updated with the window&#8217;s current values as it is closed.</dl>
<p> These are is covered in more detail in <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code>.</dl>
<p> <code>Close</code></p>
<dl>
<dt>
<dd> Close the application softly.</dl>
<p> <code>Kill</code></p>
<dl>
<dt>
<dd> Kill the window&#8217;s parent process, like <code><a href="/docs/linux/man/1-xkill/">xkill</a>(1)</code>.</dl>
<h3>Workspace Menu</h3>
<p> The workspace menu can be found, by default, by middle-clicking on the background. This menu contains entries to explore the currently defined workspaces, windows, and add/remove/rename workspaces. </p>
<p> <code>Icons</code></p>
<dl>
<dt>
<dd> This menu shows any iconified (or, minimized) windows. Clicking on a window in this menu will raise it on the current workspace.</dl>
<p> <i>Workspaces</i></p>
<dl>
<dt>
<dd> The next section provides one submenu per workspace. Middle-clicking on a workspace name will take you to that workspace. The submenu contains a list of all open windows on that workspace. Clicking on a window name will take you to that window and raise it, changing the active workspace if necessary.</dl>
<p> <code>New Workspace</code></p>
<dl>
<dt>
<dd> This entry adds a new workspace to the end of the list of current workspaces.</dl>
<p> <code>Edit current workspace name</code></p>
<dl>
<dt>
<dd> Pops up a dialog to enter a new name for the current workspace.</dl>
<p> <code>Remove Last</code></p>
<dl>
<dt>
<dd> Remove the last workspace in the list. Any windows currently open there will be sent to the next-to-last workspace.</dl>
<h2>TOOLBAR</h2>
<p> The toolbar is a small area to display information like a clock, workspace name, a system tray or a taskbar (iconbar) that can contain the running programs. The color, look, font etc. is defined in the <code>STYLE</code>. </p>
<p> The tools in the toolbar can be enabled/disabled in the &#8216;init&#8217; file with the <code>session.screen0.toolbar.tools</code> resource. See the <code>RESOURCES</code> section for details on how to alter this value. </p>
<p> The possible tools are: </p>
<p> <code>Clock</code></p>
<dl>
<dt>
<dd> This will show an area to display a clock and the date according to the format specification listed in &quot;man strtftime&quot;</dl>
<p> <code>Iconbar</code></p>
<dl>
<dt>
<dd> This is the area that contains all windows (all running applications, all minimized windows or maybe no window, all depending on the Toolbar Settings).</dl>
<p> <code>Systemtray</code></p>
<dl>
<dt>
<dd> The Systemtray can hold applications that are made to use it.</dl>
<p> <code>WorkspaceName</code></p>
<dl>
<dt>
<dd> This displays the name of the current workspace. Also, one is able to switch to the workspace left of the current one with a left click and to the workspace right of the current one with a right click.</dl>
<p> <code>PrevWorkspace</code></p>
<dl>
<dt>
<dd> This displays an arrow that allows one to switch to the workspace left of the current one.</dl>
<p> <code>NextWorkspace</code></p>
<dl>
<dt>
<dd> This displays an arrow that allows one to switch to the workspace right of the current one.</dl>
<p> <code>PrevWindow</code></p>
<dl>
<dt>
<dd> This displays an arrow that switches focus to the previous visible window on the current workspace.</dl>
<p> <code>NextWindow</code></p>
<dl>
<dt>
<dd> This displays an arrow that switches focus to the next visible window on the current workspace.</dl>
<p> Other aspects of the toolbar can be configured in two ways: through the toolbar menu, which is accessible in the Configuration part of the RootMenu or with a middle click on the edge the toolbar, or by editing the init file (see the <code>RESOURCES</code> section for more information about that).</p>
<h3>Toolbar Menu</h3>
<p> This menu can be opened by right-clicking on the toolbar (though not on a window&#8217;s name in the iconbar), or from the <code>Configuration Menu</code>. </p>
<p> All changes take effect immediately. Here are the settings: </p>
<p> <code>Visible</code></p>
<dl>
<dt>
<dd> Sets the toolbar either to visible or invisible.</dl>
<p> <code>Auto hide</code></p>
<dl>
<dt>
<dd> If this is enabled the toolbar will disappear after a defined time when the mouse pointer leaves the toolbar. It will slide in when the cursor hits the remaining edge of the toolbar. See the <code>session.autoRaiseDelay</code> resource for the delay time.</dl>
<p> <code>Toolbar width percentage</code></p>
<dl>
<dt>
<dd> Sets the width of the toolbar in a percentage of your total screen size. Use the left mouse button to decrease and the right mouse-button to increase the value. The value can be from 1-100.</dl>
<p> <code>Maximize Over</code></p>
<dl>
<dt>
<dd> Enabling this option will allow windows to maximize over the toolbar. With this switched on they will only expand to the edge of the bar. This option may be overridden by the &#8220;Full Maximization&#8221; from the <code>Configuration Menu</code>. If that option is enabled, this option will have no effect..</dl>
<p> <code>Layer&#8230;</code></p>
<dl>
<dt>
<dd> This sets the layer on which the toolbar is set. With this you can set the toolbar to &quot;Always on top&quot;.</dl>
<p> <code>Placement</code></p>
<dl>
<dt>
<dd> Sets the toolbar to any edge of the screen, either centered or aligned with a corner.</dl>
<p> <code>Alpha</code></p>
<dl>
<dt>
<dd> This sets the alpha value for the toolbar. Use the left mouse button to decrease and the right mouse button to increase the value. 0 is invisible, 255 is not transparent at all.</dl>
<p> <code>Iconbar Mode</code></p>
<dl>
<dt>
<dd> Specifies various modes of the iconbar&#8217;s operation. </p>
<p> The first section outlines what types of windows will be shown in the iconbar: </p>
<p> <code>None</code>:</p>
<dl>
<dt>
<dd> Will not show any windows</dl>
<p> <code>Icons</code>:</p>
<dl>
<dt>
<dd> Shows windows from all workspaces that are iconified (or, minimized)</dl>
<p> <code>NoIcons</code>:</p>
<dl>
<dt>
<dd> Shows windows from all workspaces that are not iconified</dl>
<p> <code>WorkspaceIcons</code>:</p>
<dl>
<dt>
<dd> Shows windows from the current workspace that are iconified</dl>
<p> <code>WorkspaceNoIcons</code>:</p>
<dl>
<dt>
<dd> Shows windows from the current workspace that are not iconified</dl>
<p> <code>Workspace</code>:</p>
<dl>
<dt>
<dd> Shows all windows (iconified or not) from the current workspace</dl>
<p> <code>All Windows</code>:</p>
<dl>
<dt>
<dd> Shows all windows (iconified or not) from all workspaces</dl>
<p> The next section specifies the alignment of the window names shown in the iconbar. The width is specified via the <code>session.screen0.iconbar.iconWidth</code> resource: </p>
<p> <code>Left</code>:</p>
<dl>
<dt>
<dd> All icons will be left-aligned with the width set in the &#8216;init&#8217; file</dl>
<p> <code>Relative</code>:</p>
<dl>
<dt>
<dd> All icons will be sized evenly to fill the iconbar completely</dl>
<p> <code>Right</code>:</p>
<dl>
<dt>
<dd> All icons will be right-aligned with the width set in the &#8216;init&#8217; file</dl>
<p> The last option in this submenu is: </p>
<p> <code>Show Pictures</code>:</p>
<dl>
<dt>
<dd> If enabled the iconbar will show the application&#8217;s icon (if provided by the application)</dl>
</dl>
<p> <code>Clock</code></p>
<dl>
<dt>
<dd> Lets you switch between the 00:00am &#8211; 11:59pm and 00:00 &#8211; 23:59 notation</dl>
<p> <code>Edit Clock Format</code></p>
<dl>
<dt>
<dd> clicking this entry will pop up a dialog window in which the clock format can be set according to <i>man strftime</i> (or <i>man date</i>).</dl>
<h2>FOCUS MODEL</h2>
<p> The Focus Model defines how windows gain focus (i.e. become the active window, which receives keyboard and mouse events). The focus model can be changed in the configuration menu (usually located under <i>fluxbox menu</i> in the Root Menu. </p>
<p> There are two main aspects of the focus model: how windows gain focus and how tabs gain focus. Each of these has two options: focus follows mouse and click to focus. Focus follows mouse means that windows will gain focus when the mouse hovers over them. Click to focus means that windows will gain focus when the mouse clicks on them. </p>
<p> Thus, there are four main options when choosing a focus model. You should choose one of the first two and one of the last two. They are: </p>
<p> <code>Click To Focus</code></p>
<dl>
<dt>
<dd> Click to focus windows.</dl>
<p> <code>Mouse Focus</code></p>
<dl>
<dt>
<dd> Window focus follows mouse.</dl>
<p> <code>ClickTabFocus</code></p>
<dl>
<dt>
<dd> Click to focus tabs.</dl>
<p> <code>MouseTabFocus</code></p>
<dl>
<dt>
<dd> Tab focus follows mouse.</dl>
<p> There are three more settings in the &#8220;Focus Model&#8221; menu: </p>
<p> <code>Focus New Windows</code></p>
<dl>
<dt>
<dd> If enabled, a new window will grab X focus as soon as it is opened. </p>
<p> <code>Auto Raise</code></p>
<dl>
<dt>
<dd> If enabled, focusing on a new window will automatically raise that window above all others within its layer. When disabled, you must explicitly raise a focused window using the window menu, keybinding, or <code>Click Raises</code>.</dl>
<p> <code>Click Raises</code></p>
<dl>
<dt>
<dd> If enabled, clicking anywhere on a window will raise it above all others within its layer.</dl>
</dl>
<h2>TAB OPTIONS</h2>
<p> This section of fluxbox configuration menu lets you configure many features of tabs. Inside of it there are three main options: </p>
<p> <code>Placement</code></p>
<dl>
<dt>
<dd> You can choose where the external tabs will be positioned relative to the window. For these options to work, <i>Tabs in Titlebar</i> must be off.</dl>
<p> <code>Tabs in Titlebar</code></p>
<dl>
<dt>
<dd> When this option is on, tabs are fixed in window titlebar and the width varies according to the amount of windows grouped.</dl>
<p> <code>Maximize Over</code></p>
<dl>
<dt>
<dd> When this option is on, maximizing a window will disregard the size and location of external tabs, which means they may be pushed out of the screen entirely.</dl>
<p> <code>External Tab Width</code></p>
<dl>
<dt>
<dd> This specifies in pixels the width of external tabs.</dl>
<h2>STYLES</h2>
<p> fluxbox enables you to use specialized files that contain <code><a href="/docs/linux/man/1-x/">X</a>(1)</code> resources to specify colors, textures, pixmaps and fonts, and thus the overall look of your window borders, menus and the toolbar. </p>
<p> The default installation of fluxbox provides some of these style files. See <code><a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5)</code> to accommodate the growing number of style components.</p>
<h3>Style Overlay</h3>
<p> In addition to the style file, the overlay file, whose location is specified by <code>session.screen0.styleOverlay</code> (default: <code>~/.fluxbox/overlay</code>) can be used to set style resources that override all styles. For more information about which parts of fluxbox can be controlled by the overlay file, see <code><a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5)</code>.</p>
<h2>THE SLIT</h2>
<p> The slit is a special fluxbox window frame that can contain dockable applications, such as &#8220;bbtools&#8221; or &#8220;window maker dockapps&#8221;. </p>
<p> When applications are run in the slit they have no window borders of their own; instead they are framed in the slit, and they are always visible in the current workspace. </p>
<p> Most dockable applications use the -w option to run in the slit. For example, you could put in your <code>~/.fluxbox/startup</code>: </p>
<dl>
<dt>
<dd>
<pre>
bbmail -w &amp;
bbpager -w &amp;
wmdrawer &amp;
exec fluxbox
</pre>
</dl>
<p> To use the slit you must have it compiled into fluxbox. This is the default setting.</p>
<h3>Slit Menu</h3>
<p> This menu can be opened by right-clicking on the slit (though not on an application running within the slit), or from the <code>Configuration Menu</code>. </p>
<p> All changes take effect immediately. Here are the settings: </p>
<p> <code>Placement</code></p>
<dl>
<dt>
<dd> This lets you set the position of the slit.</dl>
<p> <code>Layer</code></p>
<dl>
<dt>
<dd> See <code>LAYERS</code> for details on the layer order.</dl>
<p> <code>Auto hide</code></p>
<dl>
<dt>
<dd> If this is enabled the slit will disappear after a defined time when the mouse pointer leaves the slit. It will slide in when the cursor hits the remaining edge of the slit. See the <code>session.autoRaiseDelay</code> resource for the delay time.</dl>
<p> <code>Maximize Over</code></p>
<dl>
<dt>
<dd> Enabling this option will allow windows to maximizing over the slit. With this switched off they will only expand to the edge of the slit. This option may be overridden by the &#8220;Full Maximization&#8221; from the <code>Configuration Menu</code>. If that option is enabled, this option will have no effect..</dl>
<p> <code>Alpha</code></p>
<dl>
<dt>
<dd> This sets the alpha value for the slit. Use the left mouse button to decrease and the right mouse button to increase the value. 0 is invisible, 255 is not transparent at all.</dl>
<p> <code>Clients</code></p>
<dl>
<dt>
<dd> This submenu lets you reorder the the applications running in the slit. You are able to hide apps from the slit by unselecting them in the list showing. This will not kill the app. You can make them re-appear by selecting them in the list. The &quot;Save SlitList&quot; option saves the new order to you slitlist located in <code>~/.fluxbox/slitlist</code>. See the next section for details.</dl>
<h3>Slitlist File</h3>
<p> fluxbox&#8217;s slitlist file is available for those that use dockapps in the slit. This file helps fluxbox keep track of the <code>order</code> of the dockapps when in the slit. The file is generally located at <code>~/.fluxbox/slitlist</code>. </p>
<p> A simple procedure for getting the slit sequences the way you like it is: 1. Run fluxbox with no pre-loaded dockapps 2. Run dockapps individually in the order you want them 3. Add dockapps to your <code><a href="/docs/linux/man/1-startfluxbox/">startfluxbox</a>(1)</code> script </p>
<p> This sequence will be saved by default to <code>~/.fluxbox/slitlist</code> and will be remembered for future instances of fluxbox. </p>
<p> Users are free to manually edit the slitlist file. It is a simple list of window names, as given by <code><a href="/docs/linux/man/1-xprop/">xprop</a>(1)</code>, one per dockapp. Similar to the init file it should not be edited while fluxbox is running. Otherwise changes may get overwritten. </p>
<p> The user also has the option of choosing a different path for the slitlist file, by setting the <code>session.session0.slitlistFile</code> resource.</p>
<h2>LAYERS</h2>
<p> Layers affect the way that windows will overlap each other on the screen. Windows on a higher layer will always appear above those on a lower one, whether they are focused or not. Fluxbox uses 13 layers, starting from 1 (highest). </p>
<p> There are two ways to assign a window to a different layer. When the window is open, you may select the layer in the &#8216;Layer &#8230;&#8217; submenu of the window menu. The menu gives six choices for the layer, which fluxbox manages by name. The names are (from highest to lowest layer): </p>
<dl>
<dt>
<dd> &bull; 2 &#8211; Above Dock</dl>
<dl>
<dt>
<dd> &bull; 4 &#8211; Dock</dl>
<dl>
<dt>
<dd> &bull; 6 &#8211; Top</dl>
<dl>
<dt>
<dd> &bull; 8 &#8211; Normal</dl>
<dl>
<dt>
<dd> &bull; 10 &#8211; Bottom</dl>
<dl>
<dt>
<dd> &bull; 12 &#8211; Desktop</dl>
<p> The other way to set the layer for a window is through the &#8216;apps&#8217; file. This method is described in <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code>.</p>
<h2>RESOURCES</h2>
<p> Usually the <code>~/.fluxbox/init</code> resource file is created and maintained by fluxbox itself. You can use the <code>Configure Menu</code>, mentioned above, to set most of these options. However, we&#8217;ll cover all of the resource options that are available to the user. If you edit this file while fluxbox is running, you must &#8220;reconfigure&#8221; to reload the resource options. </p>
<p> When running fluxbox in a multiple-screen environment the screen0 key can also be screen1, screen2, to customize the behavior of fluxbox on each desktop accordingly. Here are the resources that are currently available: </p>
<p> <code>session.screen0.window.{focus|unfocus}.alpha</code>: <i>integer</i></p>
<dl>
<dt>
<dd> These resources are available to the user to set different levels of transparency for different components of fluxbox. Each one accepts a value between 0-255, 255 being opaque and 0 being completely transparent. </p>
<p> Default: <code>255</code></dl>
<p> <code>session.screen0.{slit|toolbar}.autoHide</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> The autoHide resources allow the user to set the behavior of the toolbar and slit. This behavior can be that they disappear when they are not being used actively by the user, or they remain visible at all times. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.screen0.{slit|toolbar}.layer</code>: <i>layer</i></p>
<dl>
<dt>
<dd> With these two resources, you can set the layer you want the toolbar and the slit to appear on. Please read the LAYER section for more information. </p>
<p> Default: <code>Dock</code></dl>
<p> <code>session.screen0.{slit|toolbar}.placement</code>: <i>placement</i></p>
<dl>
<dt>
<dd> These allow users to place the slit and toolbar where they like. </p>
<p> Possible options are:</p>
<dl>
<dt>
<dd> <code>BottomLeft BottomCenter BottomRight LeftBottom LeftCenter LeftTop RightBottom RightCenter RightTop TopLeft TopCenter TopRight</code></dl>
<p> Slit default: <code>RightBottom</code> </p>
<p> Toolbar default: <code>BottomCenter</code></dl>
<p> <code>session.screen0.{slit|toolbar|tabs}.maxOver</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> Setting these to True will allow application windows to maximize over the complete screen. Setting to False allows the slit, toolbar, and external tabs to hold their territory and will always be visible when an application is maximized. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.screen0.toolbar.height</code>: <i>integer</i></p>
<dl>
<dt>
<dd> Set the height of the toolbar. If the value is set to 0, the style file will gain control over the toolbar height. It is possible to set a fixed height by changing this value to something greater than 0. </p>
<p> Default: <code>0</code></dl>
<p> <code>session.screen0.toolbar.visible</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> The user can set whether they want to have a toolbar on screen at all. Setting to False removes the toolbar from the screen. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.toolbar.widthPercent</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This resource sets the width percentage of the toolbar on the screen. </p>
<p> Default: <code>100</code></dl>
<p> <code>session.screen0.toolbar.tools</code>: <i>tools</i></p>
<dl>
<dt>
<dd> This resource specifies the tools plugged into the toolbar. Read the TOOLBAR section in this manual for a description of each of these. They may be specified in any order, delimited by the <code>,</code> character. They will appear in the order given. </p>
<p> Possible tools:</p>
<dl>
<dt>
<dd> <code>clock iconbar nextwindow prevwindow nextworkspace prevworkspace systemtray workspacename</code></dl>
<p> Default:</p>
<dl>
<dt>
<dd> <code>workspacename, prevworkspace, nextworkspace, iconbar, prevwindow, nextwindow, systemtray, clock</code></dl>
</dl>
<p> <code>session.screen0.{slit|toolbar}.onhead</code>: <i>integer</i></p>
<dl>
<dt>
<dd> For those that use xinerama, users can set this value to the number of the head where they would like to see the slit and toolbar, starting from 1. Setting this to 0 will ignore xinerama information. </p>
<p> Default: <code>0</code> for slit, <code>1</code> for toolbar</dl>
<p> <code>session.screen0.iconbar.mode</code>: <i>pattern</i></p>
<dl>
<dt>
<dd> This determines which windows will be displayed in the iconbar. Any window pattern is acceptable. See the section <code>CLIENT PATTERNS</code> in either <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> or <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for details. </p>
<p> Default: <code>{static groups} (workspace)</code></dl>
<p> <code>session.screen0.iconbar.usePixmap</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This is also set in the Iconbar Mode menu. When set to True, this will show the native icon of applications. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.iconbar.iconTextPadding</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This specifies the space between the window title and the edge of the button. </p>
<p> Default: <code>10</code></dl>
<p> <code>session.screen0.iconbar.alignment</code>: <i>position</i></p>
<dl>
<dt>
<dd> This value should be changed in the Iconbar Mode menu. </p>
<p> Available options:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <code>Left</code>: Fixed width, aligned left</dl>
<dl>
<dt>
<dd> &bull; <code>Relative</code>: Width varies to fill the iconbar</dl>
<dl>
<dt>
<dd> &bull; <code>Right</code>: Fixed width, aligned right</dl>
</dl>
<p> Default: <code>Relative</code></dl>
<p> <code>session.screen0.iconbar.iconWidth</code>: <i>integer</i></p>
<dl>
<dt>
<dd> Used to specify the iconbar button width for Left/Right alignment. </p>
<p> Default: <code>128</code></dl>
<p> <code>session.screen0.strftimeFormat</code>: <i>date</i></p>
<dl>
<dt>
<dd> This adjusts the way the current time is displayed in the toolbar. The <code><a href="/docs/linux/man/3-strftime/">strftime</a>(3)</code> format is used. </p>
<p> Default: <code>%k:%M</code></dl>
<p> <code>session.screen0.tabs.intitlebar</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This specifies whether tabs should be embedded in the titlebar or placed outside the window. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.tab.placement</code>: <i>placement</i></p>
<dl>
<dt>
<dd> This specifies where external tabs will appear on the window. It has the same possible values as <code>sesion.screen0.{slit|toolbar}.placement</code>. </p>
<p> Default: <code>TopLeft</code></dl>
<p> <code>session.screen0.tab.width</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This specifies the width of external tabs in pixels. </p>
<p> Default: <code>64</code></dl>
<p> <code>session.screen0.focusModel</code>: <code>ClickToFocus|MouseFocus|StrictMouseFocus</code></p>
<dl>
<dt>
<dd> This controls how windows gain focus via the mouse. With &#8216;ClickToFocus&#8217;, the user must click on the window. With &#8216;MouseFocus&#8217;, windows gain focus whenever the mouse moves over them, but only when the mouse is moving. With &#8216;StrictMouseFocus&#8217;, windows gain focus whenever the mouse enters any exposed area, even if this is due to layer changes, window movement, changing desktops, closing windows, etc. </p>
<p> Default: <code>ClickToFocus</code></dl>
<p> <code>session.screen0.autoRaise</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> When True, this setting automatically raises any window that gains focus. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.autoRaiseDelay</code>: <i>integer</i></p>
<dl>
<dt>
<dd> Adjusts the delay (in milli-sec) before focused windows will raise when using the Autoraise option. </p>
<p> Default: <code>250</code></dl>
<p> <code>session.screen0.clickRaises</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This setting allows a user to click anywhere on a window to bring it on top of other windows. Otherwise, only the titlebar will work. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.workspacewarping</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This setting enables a user to change workspaces by dragging a window across the edge of the screen. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.showwindowposition</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> Setting this resource to True shows the user, in a little window, the exact position of the application window while the user is dragging it. Allows a precise placement of windows on a screen. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.screen0.defaultDeco</code>: <i>string</i></p>
<dl>
<dt>
<dd> This specifies the default window decorations, according to the same options available to the <code>[Deco]</code> option in the &#8216;apps&#8217; file, described in <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code>. </p>
<p> Default: <code>NORMAL</code></dl>
<p> <code>session.screen0.menuDelay</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This sets the delay in milliseconds for submenus to open when you hover over them or to close when you hover over another item. </p>
<p> Default: <code>200</code></dl>
<p> <code>session.screen0.focusNewWindows</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This sets whether or not new windows will become focused automatically. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.workspaceNames</code>: <i>names</i></p>
<dl>
<dt>
<dd> Here is where the user can name their workspaces, in a comma-delimited list. However it is recommended to use the tool available in the Workspace Menu to set these. </p>
<p> Default: <code>Workspace 1, Workspace 2, Workspace 3, Workspace 4</code></dl>
<p> <code>session.screen0.edgeSnapThreshold</code>: <i>integer</i></p>
<dl>
<dt>
<dd> When moving a window across your screen, fluxbox is able to have it &#8216;snap&#8217; to the edges of the screen and other windows for easy placement. This variable tells fluxbox the distance (in pixels) at which the window will jump to the edge. </p>
<p> Default: <code>10</code></dl>
<p> <code>session.screen0.windowPlacement</code>: <i>strategy</i></p>
<dl>
<dt>
<dd> This resource specifies where to place new windows when not otherwise specified (by the program or the &#8216;apps&#8217; file, for example). </p>
<p> Available strategies:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; RowSmartPlacement: tries to place windows in rows without overlapping</dl>
<dl>
<dt>
<dd> &bull; ColSmartPlacement: tries to place windows in columns without overlapping</dl>
<dl>
<dt>
<dd> &bull; CascadePlacement: places windows below the titlebar of the previous one</dl>
<dl>
<dt>
<dd> &bull; UnderMousePlacement: places new windows underneath the mouse</dl>
</dl>
<p> Default: <code>RowSmartPlacement</code></dl>
<p> <code>session.screen0.rowPlacementDirection</code>: <code>LeftToRight</code>|<code>RightToLeft</code></p>
<dl>
<dt>
<dd> These settings control the direction in which windows are tiled using the RowSmartPlacement and ColSmartPlacement strategies described above. </p>
<p> Default: <code>LeftToRight</code></dl>
<p> <code>session.screen0.colPlacementDirection</code>: <code>TopToBottom</code>|<code>BottomToTop</code></p>
<dl>
<dt>
<dd> These settings control the direction in which windows are tiled using the RowSmartPlacement and ColSmartPlacement strategies described above. </p>
<p> Default: <code>TopToBottom</code></dl>
<p> <code>session.screen0.fullMaximization</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> If this setting is enabled, windows will maximize over the toolbar, slit, and any other window that creates a strut, no matter what their individual settings are. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.screen0.opaqueMove</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> When moving a window, setting this to True will draw the window contents as it moves (this is nasty on slow systems). If False, it will only draw an outline of the window border. </p>
<p> Default: <code>True</code></dl>
<p> <code>session.screen0.workspaces</code>: <i>integer</i></p>
<dl>
<dt>
<dd> Set this to the number of workspaces the users wants. </p>
<p> Default: <code>4</code></dl>
<p> <code>session.cacheLife</code>: <i>minutes</i></p>
<dl>
<dt>
<dd> This tells fluxbox how long unused pixmaps may stay in the X server&#8217;s memory. </p>
<p> Default: <code>5</code></dl>
<p> <code>session.cacheMax</code>: <i>KbSize</i></p>
<dl>
<dt>
<dd> This tells fluxbox how much memory it may use to store cached pixmaps on the X server. If your machine runs short of memory, you may lower this value. </p>
<p> Default: <code>200</code></dl>
<p> <code>session.colorsPerChannel</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This tells fluxbox how many colors to take from the X server on pseudo-color displays. A channel would be red, green, or blue. fluxbox will allocate this variable ^ 3 and make them always available. Value must be between 2-6. When you run fluxbox on an 8bpp display, you must set this resource to 4. </p>
<p> Default: <code>4</code></dl>
<p> <code>session.doubleClickInterval</code>: <i>integer</i></p>
<dl>
<dt>
<dd> Adjust the delay in milliseconds between mouse clicks for fluxbox to consider a double click. </p>
<p> Default: <code>250</code></dl>
<p> <code>session.forcePseudoTransparency</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> If you have Xorg&#8217;s composite extension enabled, this setting will force the menu, windows, toolbar, and slit to use pseudo-transparency instead of true transparency. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.ignoreBorder</code>: <i>boolean</i></p>
<dl>
<dt>
<dd> This configures the ability to move windows by dragging the border. </p>
<p> Default: <code>False</code></dl>
<p> <code>session.tabPadding</code>: <i>integer</i></p>
<dl>
<dt>
<dd> This specifies the spacing between tabs. </p>
<p> Default: <code>0</code></dl>
<p> <code>session.tabsAttachArea</code>: <code>Window|Titlebar</code></p>
<dl>
<dt>
<dd> With this set to &#8216;Window&#8217;, windows may be grouped by dragging one tab with the middle mouse button and dropping it anywhere on another window. With &#8216;Titlebar&#8217;, the user must drop the tab on the target window&#8217;s titlebar. </p>
<p> Default: <code>Window</code></dl>
<p> <code>session.titlebar.{left|right}</code>: <i>buttons</i></p>
<dl>
<dt>
<dd> The buttons or icons to place in the titlebar of decorated windows. You may specify any number, space-delimited. </p>
<p> The available options are:</p>
<dl>
<dt>
<dd> <code>Close Maximize MenuIcon Minimize Shade Stick LHalf RHalf</code></dl>
<p> Default left: <code>Stick</code> </p>
<p> Default right: <code>Shade Minimize Maximize Close</code> </p>
<p> <i>LHalf</i> and <i>RHalf</i> are buttons to quickly place a window into the left and right half of the current monitor.</dl>
<p> All of the <i>location</i> resources following require a pathname to their specific files. This is where you can specify different files. Most of the defaults will be located in the user&#8217;s <code>~/.fluxbox</code> directory. </p>
<p> <code>session.appsFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of persistent application settings, or the &#8216;apps&#8217; file. See the <code>Remember&#8230;</code> item in the <code>Window Menu</code> section above or <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for details.</dl>
<p> <code>session.groupFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Deprecated, auto-grouping is now done in the &#8216;apps&#8217; file, see <code><a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5)</code> for details.</dl>
<p> <code>session.keyFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of the keyboard mapping settings, or the &#8216;keys&#8217; file. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> for details.</dl>
<p> <code>session.menuFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of the Root Menu file. See <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code> for details.</dl>
<p> <code>session.slitlistFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of the file used to remember slit client ordering. See <code>SLIT</code> above for details.</dl>
<p> <code>session.styleFile</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of the currently selected style. See <code><a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5)</code> for details.</dl>
<p> <code>session.styleOverlay</code>: <i>location</i></p>
<dl>
<dt>
<dd> Location of the style overlay file. See <code><a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5)</code> for details.</dl>
<p> <code>session.screen0.windowMenu</code>: <i>location</i></p>
<dl>
<dt>
<dd> This optionally specifies the location of a user-defined window menu. If left blank, it will use <code>~/.fluxbox/windowmenu</code>. </p>
<p> Default: <code>blank</code></dl>
<h2>ENVIRONMENT</h2>
<p> <code>HOME</code></p>
<dl>
<dt>
<dd> fluxbox uses <code>$HOME</code> to find the .fluxbox/init file and to resolve style file and -directory names.</dl>
<p> <code>DISPLAY</code></p>
<dl>
<dt>
<dd> When no other display was given on the command line, fluxbox will start on the display specified by this variable.</dl>
<p> fluxbox can also take advantage of other environment variables if they are set before fluxbox is started. For example, if $TERM is set, then it will be available whenever fluxbox uses the shell, such as the &#8216;keys&#8217; file <code>ExecCommand</code> or the root menu&#8217;s <code>[exec]</code> tag. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> and <code><a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5)</code> for details. </p>
<p> The &#8216;keys&#8217; file also provides two commands that can alter the current environment of fluxbox: <code>SetEnv</code> and <code>Export</code>. Any changes made by these commands will also affect the environment as seen by fluxbox and all child processes started after that point. See <code><a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5)</code> for details. </p>
<p> For more information about environment variables in general, see your shell&#8217;s manual.</p>
<h2>SIGNALS</h2>
<p> fluxbox responds to the following signals: </p>
<dl>
<dt>
<dd> &bull; SIGUSR1 restarts fluxbox.</dl>
<dl>
<dt>
<dd> &bull; SIGUSR2 Forces reloading of configuration.</dl>
<h2>AUTHORS</h2>
<p> fluxbox is written and maintained by Henrik Kinnunen &lt;fluxgen at fluxbox org&gt;, Simon Bowden &lt;rathnor at fluxbox org&gt;, Mathias Gumz &lt;akira at fluxbox org&gt;, and Mark Tiefenbruck &lt;mark at fluxbox org&gt;, with contributions and patches merged from many individuals around the world. </p>
<p> Blackbox was written and maintained by Brad Hughes &lt;blackbox at alug org&gt; and Jeff Raven &lt;jraven at psu edu&gt;. </p>
<p> This manpage is the combined work of: </p>
<dl>
<dt>
<dd> &bull; Jim Ramsay &lt;i.am at jimramsay com&gt; (&gt;fluxbox-1.0.0)</dl>
<dl>
<dt>
<dd> &bull; Curt Micol &lt;asenchi at asenchi com&gt; (&gt;fluxbox-0.9.11)</dl>
<dl>
<dt>
<dd> &bull; Tobias Klausmann &lt;klausman at users sourceforge net&gt; (&lt;fluxbox-0.9.11)</dl>
<dl>
<dt>
<dd> &bull; Grubert &lt;grubert at users sourceforge net&gt; (fluxbox)</dl>
<dl>
<dt>
<dd> &bull; Matthew Hawkins &lt;matt at mh dropbear id au&gt; (blackbox)</dl>
<dl>
<dt>
<dd> &bull; Wilbert Berendsen &lt;wbsoft at xs4all nl&gt; (blackbox)</dl>
<dl>
<dt>
<dd> &bull; Numerous other languages could be available if someone jumps in.</dl>
<h2>ONLINE DOCUMENTATION</h2>
<p> The Official fluxbox website: m[blue]<code><a rel="nofollow" href="http://www.fluxbox.org">http://www.fluxbox.org</a></code>m[] </p>
<p> The Official fluxbox wiki: m[blue]<code><a rel="nofollow" href="http://www.fluxbox-wiki.org">http://www.fluxbox-wiki.org</a></code>m[] </p>
<p> Many compatible themes: m[blue]<code><a rel="nofollow" href="http://tenr.de">http://tenr.de</a></code>m[]</p>
<h2>BUGS</h2>
<p> If you find any bugs, please visit the #fluxbox irc channel on irc.freenode.net or submit them to the bug tracker at m[blue]<code><a rel="nofollow" href="http://sf.net/projects/fluxbox">http://sf.net/projects/fluxbox</a></code>m[] . Or you may subscribe to one of the mailinglists. More information can be found on the official website.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/5-fluxbox-apps/">fluxbox-apps</a>(5) <a href="/docs/linux/man/5-fluxbox-keys/">fluxbox-keys</a>(5) <a href="/docs/linux/man/5-fluxbox-style/">fluxbox-style</a>(5) <a href="/docs/linux/man/5-fluxbox-menu/">fluxbox-menu</a>(5) <a href="/docs/linux/man/1-fluxbox-remote/">fluxbox-remote</a>(1) <a href="/docs/linux/man/1-fbsetroot/">fbsetroot</a>(1) <a href="/docs/linux/man/1-fbsetbg/">fbsetbg</a>(1) <a href="/docs/linux/man/1-fbrun/">fbrun</a>(1) <a href="/docs/linux/man/1-startfluxbox/">startfluxbox</a>(1)</p>
<h2>AUTHOR</h2>
<p> <code>Henrik Kinnunen</code> &lt;fluxgen [at] fluxbox.org&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
