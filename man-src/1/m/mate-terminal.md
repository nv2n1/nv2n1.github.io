---
title: "mate-terminal(1)"
name: "mate-terminal"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-terminal/"
description: "mate-terminal – manual page for MATE Terminal Emulator"
---

<h2 class="name">NAME</h2>
<p> mate-terminal &#8211; manual page for MATE Terminal Emulator </p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
<dd> mate-terminal [OPTION&#8230;]</dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show help options</p>
<dt><code>&#8211;help-all</code></p>
<dd> Show all help options</p>
<dt><code>&#8211;help-terminal</code></p>
<dd> Show terminal options</p>
<dt><code>&#8211;help-window-options</code></p>
<dd> Show per-window options</p>
<dt><code>&#8211;help-terminal-options</code></p>
<dd> Show per-terminal options</p>
<dt><code>&#8211;help-gtk</code></p>
<dd> Show GTK+ Options</p>
<dt><code>&#8211;help-sm-client</code></p>
<dd> Show session management options</dl>
<h3>Options to open new windows or terminal tabs; more than one of these may be specified:</h3>
<dl>
<dt><code>&#8211;window</code></p>
<dd> Open a new window containing a tab with the default profile</p>
<dt><code>&#8211;tab</code></p>
<dd> Open a new tab in the last-opened window with the default profile</dl>
<h3>Window options; if used before the first &#8211;window or &#8211;tab argument, sets the default for all windows:</h3>
<dl>
<dt><code>&#8211;show-menubar</code></p>
<dd> Turn on the menubar</p>
<dt><code>&#8211;hide-menubar</code></p>
<dd> Turn off the menubar</p>
<dt><code>&#8211;maximize</code></p>
<dd> Maximize the window</p>
<dt><code>&#8211;full-screen</code></p>
<dd> Full-screen the window</p>
<dt><code>&#8211;geometry</code>=<i>GEOMETRY</i></p>
<dd> Set the window size; for example: 80&#215;24, or 80&#215;24+200+200 (COLSxROWS+X+Y)</p>
<dt><code>&#8211;role</code>=<i>ROLE</i></p>
<dd> Set the window role</p>
<dt><code>&#8211;active</code></p>
<dd> Set the last specified tab as the active one in its window</dl>
<h3>Terminal options; if used before the first &#8211;window or &#8211;tab argument, sets the default for all terminals:</h3>
<dl>
<dt><code>-e</code>, <code>&#8211;command</code></p>
<dd> Execute the argument to this option inside the terminal</p>
<dt><code>-x</code>, <code>&#8211;execute</code></p>
<dd> Execute the remainder of the command line inside the terminal</p>
<dt><code>&#8211;profile</code>=<i>PROFILE-NAME</i></p>
<dd> Use the given profile instead of the default profile</p>
<dt><code>-t</code>, <code>&#8211;title</code>=<i>TITLE</i></p>
<dd> Set the terminal title</p>
<dt><code>&#8211;working-directory</code>=<i>DIRNAME</i></p>
<dd> Set the working directory</p>
<dt><code>&#8211;zoom</code>=<i>ZOOM</i></p>
<dd> Set the terminal&#8217;s zoom factor (1.0 = normal size)</dl>
<p> GTK+ Options</p>
<dl>
<dt><code>&#8211;class</code>=<i>CLASS</i></p>
<dd> Program class as used by the window manager</p>
<dt><code>&#8211;name</code>=<i>NAME</i></p>
<dd> Program name as used by the window manager</p>
<dt><code>&#8211;screen</code>=<i>SCREEN</i></p>
<dd> X screen to use</p>
<dt><code>&#8211;sync</code></p>
<dd> Make X calls synchronous</p>
<dt><code>&#8211;gtk-module</code>=<i>MODULES</i></p>
<dd> Load additional GTK+ modules</p>
<dt><code>&#8211;g-fatal-warnings</code></p>
<dd> Make all warnings fatal</dl>
<h3>Session management options:</h3>
<dl>
<dt><code>&#8211;sm-client-disable</code></p>
<dd> Disable connection to session manager</p>
<dt><code>&#8211;sm-client-state-file</code>=<i>FILE</i></p>
<dd> Specify file containing saved configuration</p>
<dt><code>&#8211;sm-client-id</code>=<i>ID</i></p>
<dd> Specify session management ID</dl>
<h3>Application Options:</h3>
<dl>
<dt><code>&#8211;disable-factory</code></p>
<dd> Do not register with the activation nameserver, do not re-use an active terminal</p>
<dt><code>&#8211;load-config</code>=<i>FILE</i></p>
<dd> Load a terminal configuration file</p>
<dt><code>&#8211;save-config</code>=<i>FILE</i></p>
<dd> Save the terminal configuration to a file</p>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></p>
<dd> X display to use</dl>
<h2>Author</h2>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014) and Abel McClendon &lt;hcmmac [at] hosscomm.com&gt; (2014) </p>
<p> for the <code>Mate Documentation Team.</code></p>
<h2>See Also</h2>
<p> The full documentation for <code>mate-terminal</code> is maintained as a Texinfo manual. </p>
<p> If the <code>info</code> and <code>mate-terminal</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info mate-terminal</code></dl>
<p> should give you access to the complete manual. </p>
<p> More <code>MATE Terminal</code> documentation can be found from the <code>Help</code> menu, or by pressing the <code>F1</code> key. </p>
<p> Further information may also be available at: <code><a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></code> </p>
<h2>Index</h2>
