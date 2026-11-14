---
title: "xfce4-terminal(1)"
name: "xfce4-terminal"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xfce4-terminal/"
description: "xfce4-terminal – A Terminal emulator for X"
---

<h2 class="name">NAME</h2>
<p> xfce4-terminal &#8211; A Terminal emulator for X </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>xfce4-terminal</code> [OPTION&#8230;]</dl>
<h2>DESCRIPTION</h2>
<dd>xfce4-terminal is what is known as an X terminal emulator, often referred to as terminal or shell. It provides an equivalent to the old-fashioned text screen on your desktop, but one which can easily share the screen with other graphical applications. Windows users may already be familiar with the MS-DOS Prompt utility, which has the analogous function of offering a DOS command-line under Windows, though one should note that the UNIX CLI offer far more power and ease of use than does DOS. </p>
<p> xfce4-terminal emulates the xterm application developed by the X Consortium. In turn, the xterm application emulates the DEC VT102 terminal and also supports the DEC VT220 escape sequences. An escape sequence is a series of characters that start with the Esc character. xfce4-terminal accepts all of the escape sequences that the VT102 and VT220 terminals use for functions such as to position the cursor and to clear the screen.</p>
<h2>OPTIONS</h2>
<h3>Option Summary</h3>
<p> Here is a summary of all the options, grouped by type. Explanations are in the following sections. </p>
<p> General Options</p>
<dl>
<dt>
<dd> <code>-h</code>, <code>&#8211;help</code>; <code>-V</code>, <code>&#8211;version</code>; <code>&#8211;disable-server</code>; <code>&#8211;color-table</code>; <code>&#8211;default-display=</code><i>display</i>; <code>&#8211;default-working-directory=</code><i>directory</i></dl>
<p> Window or Tab Separators</p>
<dl>
<dt>
<dd> <code>&#8211;tab</code>; <code>&#8211;window</code></dl>
<p> Tab Options</p>
<dl>
<dt>
<dd> <code>-x</code>, <code>&#8211;execute</code>; <code>-e</code>, <code>&#8211;command=</code><i>command</i>; <code>-T</code>, <code>&#8211;title=</code><i>title</i>; <code>&#8211;dynamic-title-mode=</code><i>mode</i>; <code>&#8211;initial-title=</code><i>title</i>; <code>&#8211;working-directory=</code><i>directory</i>; <code>-H</code>, <code>&#8211;hold</code>; <code>&#8211;active-tab</code>; <code>&#8211;color-text=</code><i>color</i>; <code>&#8211;color-bg=</code><i>color</i></dl>
<p> Window Options</p>
<dl>
<dt>
<dd> <code>&#8211;display=</code><i>display</i>; <code>&#8211;drop-down</code>; <code>&#8211;geometry=</code><i>geometry</i>; <code>&#8211;role=</code><i>role</i>; <code>&#8211;startup-id=</code><i>string</i>; <code>-I, &#8211;icon=</code><i>icon</i>; <code>&#8211;fullscreen</code>; <code>&#8211;maximize</code>; <code>&#8211;minimize</code>; <code>&#8211;show-menubar</code>, <code>&#8211;hide-menubar</code>; <code>&#8211;show-borders</code>, <code>&#8211;hide-borders</code>; <code>&#8211;show-toolbar</code>, <code>&#8211;hide-toolbar</code>; <code>&#8211;show-scrollbar</code>, <code>&#8211;hide-scrollbar</code>; <code>&#8211;font=</code><i>font</i>; <code>&#8211;zoom=</code><i>zoom</i></dl>
<h3>General Options</h3>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> List the various command line options supported by xfce4-terminal and exit</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit</dl>
<p> <code>&#8211;disable-server</code></p>
<dl>
<dt>
<dd> Do not register with the D-BUS session message bus</dl>
<p> <code>&#8211;color-table</code></p>
<dl>
<dt>
<dd> Echo the color codes</dl>
<p> <code>&#8211;default-display=</code><i>display</i></p>
<dl>
<dt>
<dd> Default X display to use.</dl>
<p> <code>&#8211;default-working-directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Set <i>directory</i> as the default working directory for the terminal</dl>
<h3>Window or Tab Separators</h3>
<p> <code>&#8211;tab</code></p>
<dl>
<dt>
<dd> Open a new tab in the last-specified window; more than one of these options can be provided. </p>
<p> If you use this as the first option, without &#8211;window separators, the last window will be re-used.</dl>
<p> <code>&#8211;window</code></p>
<dl>
<dt>
<dd> Open a new window containing one tab; more than one of these options can be provided.</dl>
<h3>Tab Options</h3>
<p> <code>-x</code>, <code>&#8211;execute</code></p>
<dl>
<dt>
<dd> Execute the remainder of the command line inside the terminal</dl>
<p> <code>-e</code>, <code>&#8211;command=</code><i>command</i></p>
<dl>
<dt>
<dd> Execute <i>command</i> inside the terminal</dl>
<p> <code>-T</code>, <code>&#8211;title=</code><i>title</i></p>
<dl>
<dt>
<dd> Set <i>title</i> as the window title for the terminal (ignores dynamically-set title)</dl>
<p> <code>&#8211;dynamic-title-mode=</code><i>mode</i></p>
<dl>
<dt>
<dd> Set <i>mode</i> as the dynamically-set title mode for the terminal, one of: &#8216;replace&#8217;, &#8216;before&#8217;, &#8216;after&#8217;, &#8216;none&#8217;</dl>
<p> <code>&#8211;initial-title=</code><i>title</i></p>
<dl>
<dt>
<dd> Set <i>title</i> as the initial window title for the terminal (respects dynamically-set title)</dl>
<p> <code>&#8211;working-directory=</code><i>directory</i></p>
<dl>
<dt>
<dd> Set <i>directory</i> as the working directory for the terminal</dl>
<p> <code>-H</code>, <code>&#8211;hold</code></p>
<dl>
<dt>
<dd> Causes the terminal to be kept around after the child command has terminated</dl>
<p> <code>&#8211;active-tab</code></p>
<dl>
<dt>
<dd> Makes the terminal active: useful when a terminal window contains multiple tabs</dl>
<p> <code>&#8211;color-text=</code><i>color</i></p>
<dl>
<dt>
<dd> Set <i>color</i> as the text color for the terminal per the following specification: <a rel="nofollow" href="https://developer.gnome.org/gdk3/stable/gdk3-RGBA-Colors.html#gdk-rgba-parse">https://developer.gnome.org/gdk3/stable/gdk3-RGBA-Colors.html#gdk-rgba-parse</a></dl>
<p> <code>&#8211;color-bg=</code><i>color</i></p>
<dl>
<dt>
<dd> Set <i>color</i> as the background color for the terminal per the following specification: <a rel="nofollow" href="https://developer.gnome.org/gdk3/stable/gdk3-RGBA-Colors.html#gdk-rgba-parse">https://developer.gnome.org/gdk3/stable/gdk3-RGBA-Colors.html#gdk-rgba-parse</a></dl>
<h3>Window Options</h3>
<p> <code>&#8211;display=</code><i>display</i></p>
<dl>
<dt>
<dd> X display to use for the last- specified window.</dl>
<p> <code>&#8211;drop-down</code></p>
<dl>
<dt>
<dd> Will start the window in drop-down mode (also called a Quake-style terminal). This will only apply to the first window started with this option. It is advised to bind this to a shortcut in the keyboard preferences.</dl>
<p> <code>&#8211;geometry=</code><i>geometry</i></p>
<dl>
<dt>
<dd> Sets the geometry of the last-specified window to <i>geometry</i>. Read <code><a href="/docs/linux/man/7-x/">X</a></code>(7) for more information on how to specify window geometries.</dl>
<p> <code>&#8211;role=</code><i>role</i></p>
<dl>
<dt>
<dd> Sets the window role of the last-specified window to <i>role</i>. Applies to only one window and can be specified once for each window you create from the command line. The <i>role</i> is a unique identifier for the window to be used when restoring a session.</dl>
<p> <code>&#8211;startup-id=</code><i>string</i></p>
<dl>
<dt>
<dd> Specifies the startup notification id for the last-specified window. Used internally to forward the startup notification id when using the D-BUS service.</dl>
<p> <code>-I, &#8211;icon=</code><i>icon</i></p>
<dl>
<dt>
<dd> Set the terminal&#8217;s icon as an icon name or filename.</dl>
<p> <code>&#8211;fullscreen</code></p>
<dl>
<dt>
<dd> Set the last-specified window into fullscreen mode; applies to only one window; can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;maximize</code></p>
<dl>
<dt>
<dd> Set the last-specified window into maximized mode; applies to only one window; can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;minimize</code></p>
<dl>
<dt>
<dd> Set the last-specified window into minimized mode; applies to only one window; can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;show-menubar</code></p>
<dl>
<dt>
<dd> Turn on the menubar for the last-specified window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;hide-menubar</code></p>
<dl>
<dt>
<dd> Turn off the menubar for the last-specified window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;show-borders</code></p>
<dl>
<dt>
<dd> Turn on the window decorations for the last-specified window. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;hide-borders</code></p>
<dl>
<dt>
<dd> Turn off the window decorations for the last-specified window. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;show-toolbar</code></p>
<dl>
<dt>
<dd> Turn on the toolbar for the last-specified window. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;hide-toolbar</code></p>
<dl>
<dt>
<dd> Turn off the toolbar for the last-specified window. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;show-scrollbar</code></p>
<dl>
<dt>
<dd> Turn on the scrollbar for the last-specified window. Scrollbar position is taken from the settings; if position is None, the default position is Right side. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;hide-scrollbar</code></p>
<dl>
<dt>
<dd> Turn off the scrollbar for the last-specified window. Applies to only one window. Can be specified once for each window you create from the command line.</dl>
<p> <code>&#8211;font=</code><i>font</i></p>
<dl>
<dt>
<dd> Set the terminal font.</dl>
<p> <code>&#8211;zoom=</code><i>zoom</i></p>
<dl>
<dt>
<dd> Set the zoom level: the font size will be multiplied by this level. The range is from -7 to 7, default is 0. Each step multiplies the size by 1.2, i.e. level 7 is 3.5831808 (1.2^7) times larger than the default size.</dl>
<h2>EXAMPLES</h2>
<p> xfce4-terminal &#8211;geometry 80&#215;40 &#8211;command mutt &#8211;tab &#8211;command mc</p>
<dl>
<dt>
<dd> Opens a new terminal window with a geometry of 80 columns and 40 rows and two tabs in it, where the first tab runs <code>mutt</code> and the second tab runs <code>mc</code>.</dl>
<h2>ENVIRONMENT</h2>
<p> xfce4-terminal uses the Basedir Specification as defined on m[blue]<code>Freedesktop.org</code>m[]<font SIZE="-2">[1]</font> to locate its data and configuration files. This means that file locations will be specified as a path relative to the directories described in the specification. </p>
<p> <i>${XDG_CONFIG_HOME}</i></p>
<dl>
<dt>
<dd> The first base directory to look for configuration files. By default this is set to ~/.config/.</dl>
<p> <i>${XDG_CONFIG_DIRS}</i></p>
<dl>
<dt>
<dd> A colon separated list of base directories that contain configuration data. By default the application will look in ${sysconfdir}/xdg/. The value of <i>${sysconfdir}</i> depends on how the program was build and will often be /etc/ for binary packages.</dl>
<p> <i>${XDG_DATA_HOME}</i></p>
<dl>
<dt>
<dd> The root for all user-specific data files. By default this is set to ~/.local/share/.</dl>
<p> <i>${XDG_DATA_DIRS}</i></p>
<dl>
<dt>
<dd> A set of preference ordered base directories relative to which data files should be searched in addition to the <i>${XDG_DATA_HOME}</i> base directory. The directories should be separated with a colon.</dl>
<h2>FILES</h2>
<p> ${XDG_CONFIG_DIRS}/xfce4/terminal/terminalrc</p>
<dl>
<dt>
<dd> This is the location of the configuration file that includes the preferences which control the look and feel of xfce4-terminal. Note: any update made to the configuration file via an external editor will be picked up by xfce4-terminal instances running.</dl>
<p> ${XDG_CONFIG_DIRS}/xfce4/terminal/accels.scm</p>
<dl>
<dt>
<dd> This is the location of the keyboard shortcuts configuration file for xfce4-terminal. Editing this file allows one to modify or disable shortcuts for the supported actions.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-bash/">bash</a></code>(1), <code><a href="/docs/linux/man/7-x/">X</a></code>(7)</p>
<h2>AUTHORS</h2>
<p> <code>Igor Zakharov</code> &lt;f2404 [at] yandex.ru&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<p> <code>Nick Schermer</code> &lt;nick [at] xfce.org&gt;</p>
<dl>
<dt>
<dd> Developer</dl>
<p> <code>Benedikt Meurer</code> &lt;benny [at] xfce.org&gt;<br />
 Software developer, os-cillation, System development,</p>
<dl>
<dt>
<dd> Developer</dl>
<h2>NOTES</h2>
<dl>
<dt> 1.</p>
<dd> Freedesktop.org</p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://freedesktop.org/">http://freedesktop.org/</a></dl>
</dl>
<h2>Index</h2>
