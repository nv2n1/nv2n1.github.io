---
title: "xscreensaver-demo(1)"
name: "xscreensaver-demo"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xscreensaver-demo/"
description: "xscreensaver-demo – interactively control the background xscreensaver daemon"
---

<h2 class="name">NAME</h2>
<p> xscreensaver-demo &#8211; interactively control the background xscreensaver daemon </p>
<h2>SYNOPSIS</h2>
<p> <code>xscreensaver-demo</code> [-display <i>host:display.screen</i>] [-prefs] [&#8211;debug]</p>
<h2>DESCRIPTION</h2>
<p> The <i>xscreensaver-demo</i> program is a graphical front-end for setting the parameters used by the background <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) daemon. It is essentially two things: a tool for editing the <i>~/.xscreensaver</i> file; and a tool for demoing the various graphics hacks that the <i>xscreensaver</i> daemon will launch. </p>
<p> The main window consists of a menu bar and two tabbed pages. The first page is for editing the list of demos, and the second is for editing various other parameters of the screensaver.</p>
<h2>MENU COMMANDS</h2>
<p> All of these commands are on either the <code>File</code> or <code>Help</code> menus:</p>
<dl>
<dt><code>Blank Screen Now</code></p>
<dd> Activates the background <i>xscreensaver</i> daemon, which will then run a demo at random. This is the same as running <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) with the <i>-activate</i> option.</p>
<dt><code>Lock Screen Now</code></p>
<dd> Just like <code>Blank Screen Now</code>, except the screen will be locked as well (even if it is not configured to lock all the time.) This is the same as running <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) with the <i>-lock</i> option.</p>
<dt><code>Kill Daemon</code></p>
<dd> If the xscreensaver daemon is running on this screen, kill it. This is the same as running <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) with the <i>-exit</i> option.</p>
<dt><code>Restart Daemon</code></p>
<dd> If the xscreensaver daemon is running on this screen, kill it. Then launch it again. This is the same as doing &#8220;<i>xscreensaver-command -exit</i>&#8221; followed by &#8220;<i>xscreensaver</i>&#8221;. </p>
<p> Note that it is <i>not</i> the same as doing &#8220;<i>xscreensaver-command -restart</i>&#8221;.</p>
<dt><code>Exit</code></p>
<dd> Exits the <i>xscreensaver-demo</i> program (this program) without affecting the background <i>xscreensaver</i> daemon, if any.</p>
<dt><code>About&#8230;</code></p>
<dd> Displays the version number of this program, <i>xscreensaver-demo</i>.</p>
<dt><code>Documentation&#8230;</code></p>
<dd> Opens up a web browser looking at the XScreenSaver web page, where you can find online copies of the <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-demo/">xscreensaver-demo</a></code>(1), and <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1) manuals.</dl>
<h2>DISPLAY MODES TAB</h2>
<p> This page contains a list of the names of the various display modes, a preview area, and some fields that let you configure screen saver behavior.</p>
<dl>
<dt><code>Mode</code></p>
<dd> This option menu controls the activation behavior of the screen saver. The options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Disable Screen Saver</code></p>
<dd> Don&#8217;t ever blank the screen, and don&#8217;t ever allow the monitor to power down.</p>
<dt><code>Blank Screen Only</code></p>
<dd> When blanking the screen, just go black: don&#8217;t run any graphics.</p>
<dt><code>Only One Screen Saver</code></p>
<dd> When blanking the screen, only ever use one particular display mode (the one selected in the list.)</p>
<dt><code>Random Screen Saver</code></p>
<dd> When blanking the screen, select a random display mode from among those that are enabled and applicable. If there are multiple monitors connected, run a different display mode on each one. This is the default.</p>
<dt><code>Random Same Saver</code></p>
<dd> This is just like <code>Random Screen Saver</code>, except that the <i>same</i> randomly-chosen display mode will be run on all monitors, instead of different ones on each.</dl>
</dl>
<dt><code>Demo List</code></p>
<dd> Double-clicking in the list on the left will let you try out the indicated demo. The screen will go black, and the program will run in full-screen mode, just as it would if the <i>xscreensaver</i> daemon had launched it. Clicking the mouse again will stop the demo and un-blank the screen. </p>
<p> Single-clicking in the list will run it in the small preview pane on the right. (But beware: many of the display modes behave somewhat differently when running in full-screen mode, so the scaled-down view might not give an accurate impression.) </p>
<p> When <code>Mode</code> is set to <code>Random Screen Saver</code>, each name in the list has a checkbox next to it: this controls whether this display mode is enabled. If it is unchecked, then that mode will not be chosen. (Though you can still run it explicitly by double-clicking on its name.)</p>
<dt><code>Arrow Buttons</code></p>
<dd> Beneath the list are a pair of up and down arrows. Clicking on the down arrow will select the next item in the list, and then run it in full-screen mode, just as if you had double-clicked on it. The up arrow goes the other way. This is just a shortcut for trying out all of the display modes in turn.</p>
<dt><code>Blank After</code></p>
<dd> After the user has been idle this long, the <i>xscreensaver</i> daemon will blank the screen.</p>
<dt><code>Cycle After</code></p>
<dd> After the screensaver has been running for this long, the currently running graphics demo will be killed, and a new one started. If this is 0, then the graphics demo will never be changed: only one demo will run until the screensaver is deactivated by user activity. </p>
<p> The running saver will be restarted every this-many minutes even in <i>Only One Screen Saver</i> mode, since some savers tend to converge on a steady state.</p>
<dt><code>Lock Screen</code></p>
<dd> When this is checked, the screen will be locked when it activates.</p>
<dt><code>Lock Screen After</code></p>
<dd> This controls the length of the &#8220;grace period&#8221; between when the screensaver activates, and when the screen becomes locked. For example, if this is 5 minutes, and <i>Blank After</i> is 10 minutes, then after 10 minutes, the screen would blank. If there was user activity at 12 minutes, no password would be required to un-blank the screen. But, if there was user activity at 15 minutes or later (that is, <i>Lock Screen After</i> minutes after activation) then a password would be required. The default is 0, meaning that if locking is enabled, then a password will be required as soon as the screen blanks.</p>
<dt><code>Preview</code></p>
<dd> This button, below the small preview window, runs the demo in full-screen mode so that you can try it out. This is the same thing that happens when you double-click an element in the list. Click the mouse to dismiss the full-screen preview.</p>
<dt><code>Settings</code></p>
<dd> This button will pop up a dialog where you can configure settings specific to the display mode selected in the list.</dl>
<h2>SETTINGS DIALOG</h2>
<p> When you click on the <i>Settings</i> button on the <i>Display Modes</i> tab, a configuration dialog will pop up that lets you customize settings of the selected display mode. Each display mode has its own custom configuration controls on the left side. </p>
<p> On the right side is a paragraph or two describing the display mode. Below that is a <code>Documentation</code> button that will display the display mode&#8217;s manual page, if it has one, in a new window (since each of the display modes is actually a separate program, they each have their own manual.) </p>
<p> The <code>Advanced</code> button reconfigures the dialog box so that you can edit the display mode&#8217;s command line directly, instead of using the graphical controls.</p>
<h2>ADVANCED TAB</h2>
<p> This tab lets you change various settings used by the xscreensaver daemon itself, as well as some global options shared by all of the display modes. </p>
<p> <code>Image Manipulation</code> </p>
<p> Some of the graphics hacks manipulate images. These settings control where those source images come from. (All of these options work by invoking the <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1) program, which is what actually does the work.)</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Grab Desktop Images</code></p>
<dd> If this option is selected, then they are allowed to manipulate the desktop image, that is, a display mode might draw a picture of your desktop melting, or being distorted in some way. The security-paranoid might want to disable this option, because if it is set, it means that the windows on your desktop will occasionally be visible while your screen is locked. Others will not be able to <i>do</i> anything, but they may be able to <i>see</i> whatever you left on your screen.</p>
<dt><code>Grab Video Frames</code></p>
<dd> If your system has a video capture card, selecting this option will allow the image-manipulating modes to capture a frame of video to operate on.</p>
<dt><code>Choose Random Image</code></p>
<dd> If this option is set, then the image-manipulating modes will select a random image file to operate on, from the specified source. That source may be a local directory, which will be recursively searched for images. Or, it may be the URL of an RSS or Atom feed (e.g., a Flickr gallery), in which case a random image from that feed will be selected instead. The contents of the feed will be cached locally and refreshed periodically as needed.</dl>
<p> If more than one of the above image-related options are selected, then one will be chosen at random. If none of them are selected, then an image of video colorbars will be used instead.</dl>
<p> <code>Text Manipulation</code> </p>
<p> Some of the display modes display and manipulate text. The following options control how that text is generated. (These parameters control the behavior of the <code><a href="/docs/linux/man/1-xscreensaver-text/">xscreensaver-text</a></code>(1) program, which is what actually does the work.)</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Host Name and Time</code></p>
<dd> If this checkbox is selected, then the text used by the screen savers will be the local host name, OS version, date, time, and system load.</p>
<dt><code>Text</code></p>
<dd> If this checkbox is selected, then the literal text typed in the field to its right will be used. If it contains % escape sequences, they will be expanded as per <code><a href="/docs/linux/man/2-strftime/">strftime</a></code>(2).</p>
<dt><code>Text File</code></p>
<dd> If this checkbox is selected, then the contents of the corresponding file will be displayed.</p>
<dt><code>Program</code></p>
<dd> If this checkbox is selected, then the given program will be run, repeatedly, and its output will be displayed.</p>
<dt><code>URL</code></p>
<dd> If this checkbox is selected, then the given HTTP URL will be downloaded and displayed repeatedly. If the document contains HTML, RSS, or Atom, it will be converted to plain-text first. </p>
<p> Note: this re-downloads the document every time the screen saver runs out of text, so it will probably be hitting that web server multiple times a minute. Be careful that the owner of that server doesn&#8217;t consider that to be abusive.</dl>
</dl>
<p> <code>Power Management Settings</code> </p>
<p> These settings control whether, and when, your monitor powers down.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Power Management Enabled</code></p>
<dd> Whether the monitor should be powered down after a period of inactivity. </p>
<p> If this option is grayed out, it means your X server does not support the XDPMS extension, and so control over the monitor&#8217;s power state is not available. </p>
<p> If you&#8217;re using a laptop, don&#8217;t be surprised if this has no effect: many laptops have monitor power-saving behavior built in at a very low level that is invisible to Unix and X. On such systems, you can typically only adjust the power-saving delays by changing settings in the BIOS in some hardware-specific way.</p>
<dt><code>Standby After</code></p>
<dd> If <i>Power Management Enabled</i> is selected, the monitor will go black after this much idle time. (Graphics demos will stop running, also.)</p>
<dt><code>Suspend After</code></p>
<dd> If <i>Power Management Enabled</i> is selected, the monitor will go into power-saving mode after this much idle time. This duration should be greater than or equal to <i>Standby</i>.</p>
<dt><code>Off After</code></p>
<dd> If <i>Power Management Enabled</i> is selected, the monitor will fully power down after this much idle time. This duration should be greater than or equal to <i>Suspend</i>.</p>
<dt><code>Quick Power-off in Blank Only Mode</code></p>
<dd> If the display mode is set to <i>Blank Screen Only</i> and this is checked, then the monitor will be powered off immediately upon blanking, regardless of the other power-management settings. In this way, the power management idle-timers can be completely disabled, but the screen will be powered off when black. (This might be preferable on laptops.)</dl>
</dl>
<p> <code>Fading and Colormaps</code> </p>
<p> These options control how the screen fades to or from black when a screen saver begins or ends.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>Fade To Black When Blanking</code></p>
<dd> If selected, then when the screensaver activates, the current contents of the screen will fade to black instead of simply winking out. (Note: this doesn&#8217;t work with all X servers.) A fade will also be done when switching graphics hacks (when the <i>Cycle After</i> expires.)</p>
<dt><code>Unfade From Black When Unblanking</code></p>
<dd> The complement to <i>Fade Colormap</i>: if selected, then when the screensaver deactivates, the original contents of the screen will fade in from black instead of appearing immediately. This is only done if <i>Fade Colormap</i> is also selected.</p>
<dt><code>Fade Duration</code></p>
<dd> When fading or unfading are selected, this controls how long the fade will take.</p>
<dt><code>Install Colormap</code></p>
<dd> On 8-bit screens, whether to install a private colormap while the screensaver is active, so that the graphics hacks can get as many colors as possible. This does nothing if you are running in 16-bit or better.</dl>
</dl>
<p> There are more settings than these available, but these are the most commonly used ones; see the manual for <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1) for other parameters that can be set by editing the <i>~/.xscreensaver</i> file, or the X resource database.</p>
<h2>COMMAND-LINE OPTIONS</h2>
<p> <i>xscreensaver-demo</i> accepts the following command line options.</p>
<dl>
<dt><code>-display </code><i>host:display.screen</i></p>
<dd> The X display to use. The <i>xscreensaver-demo</i> program will open its window on that display, and also control the <i>xscreensaver</i> daemon that is managing that same display.</p>
<dt><code>-prefs</code></p>
<dd> Start up with the <code>Advanced</code> tab selected by default instead of the <code>Display Modes</code> tab.</p>
<dt><code>-debug</code></p>
<dd> Causes lots of diagnostics to be printed on stderr.</dl>
<p> It is important that the <i>xscreensaver</i> and <i>xscreensaver-demo</i> processes be running on the same machine, or at least, on two machines that share a file system. When <i>xscreensaver-demo</i> writes a new version of the <i>~/.xscreensaver</i> file, it&#8217;s important that the <i>xscreensaver</i> see that same file. If the two processes are seeing different <i>~/.xscreensaver</i> files, things will malfunction.</p>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>DISPLAY</code></p>
<dd> to get the default host and display number.</p>
<dt><code>PATH</code></p>
<dd> to find the sub-programs to run. However, note that the sub-programs are actually launched by the <i>xscreensaver</i> daemon, not by <i>xscreensaver-demo</i> itself. So, what matters is what <code>$PATH</code> that the <i>xscreensaver</i> program sees.</p>
<dt><code>HOME</code></p>
<dd> for the directory in which to read and write the <i>.xscreensaver</i> file.</p>
<dt><code>XENVIRONMENT</code></p>
<dd> to get the name of a resource file that overrides the global resources stored in the RESOURCE_MANAGER property.</p>
<dt><code>HTTP_PROXY</code> or http_proxy</p>
<dd> to get the default HTTP proxy host and port.</dl>
<h2>UPGRADES</h2>
<p> The latest version of xscreensaver, an online version of this manual, and a FAQ can always be found at <a rel="nofollow" href="https://www.jwz.org/xscreensaver/">https://www.jwz.org/xscreensaver/</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver/">xscreensaver</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-command/">xscreensaver-command</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-getimage/">xscreensaver-getimage</a></code>(1), <code><a href="/docs/linux/man/1-xscreensaver-text/">xscreensaver-text</a></code>(1)</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1992-2015 by Jamie Zawinski. Permission to use, copy, modify, distribute, and sell this software and its documentation for any purpose is hereby granted without fee, provided that the above copyright notice appear in all copies and that both that copyright notice and this permission notice appear in supporting documentation. No representations are made about the suitability of this software for any purpose. It is provided &quot;as is&quot; without express or implied warranty.</p>
<h2>AUTHOR</h2>
<p> Jamie Zawinski &lt;jwz [at] jwz.org&gt;, 13-aug-92. </p>
<p> Please let me know if you find any bugs or make any improvements. </p>
<h2>Index</h2>
