---

title: "mate-terminal(1)"
name: "mate-terminal"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mate-terminal/"
description: "mate-terminal – manual page for MATE Terminal Emulator"
---

<p> mate-terminal &#8211; manual page for MATE Terminal Emulator </p>
<h2>DESCRIPTION</h2>
<h3>Usage:</h3>
<dl>
<dt>
</dt><dd> mate-terminal [OPTION&#8230;]</dd></dl>
<h3>Help Options:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> Show help options</dd>
<dt><code>&#8211;help-all</code></dt>
<dd> Show all help options</dd>
<dt><code>&#8211;help-terminal</code></dt>
<dd> Show terminal options</dd>
<dt><code>&#8211;help-window-options</code></dt>
<dd> Show per-window options</dd>
<dt><code>&#8211;help-terminal-options</code></dt>
<dd> Show per-terminal options</dd>
<dt><code>&#8211;help-gtk</code></dt>
<dd> Show GTK+ Options</dd>
<dt><code>&#8211;help-sm-client</code></dt>
<dd> Show session management options</dd></dl>
<h3>Options to open new windows or terminal tabs; more than one of these may be specified:</h3>
<dl>
<dt><code>&#8211;window</code></dt>
<dd> Open a new window containing a tab with the default profile</dd>
<dt><code>&#8211;tab</code></dt>
<dd> Open a new tab in the last-opened window with the default profile</dd></dl>
<h3>Window options; if used before the first &#8211;window or &#8211;tab argument, sets the default for all windows:</h3>
<dl>
<dt><code>&#8211;show-menubar</code></dt>
<dd> Turn on the menubar</dd>
<dt><code>&#8211;hide-menubar</code></dt>
<dd> Turn off the menubar</dd>
<dt><code>&#8211;maximize</code></dt>
<dd> Maximize the window</dd>
<dt><code>&#8211;full-screen</code></dt>
<dd> Full-screen the window</dd>
<dt><code>&#8211;geometry</code>=<i>GEOMETRY</i></dt>
<dd> Set the window size; for example: 80&#215;24, or 80&#215;24+200+200 (COLSxROWS+X+Y)</dd>
<dt><code>&#8211;role</code>=<i>ROLE</i></dt>
<dd> Set the window role</dd>
<dt><code>&#8211;active</code></dt>
<dd> Set the last specified tab as the active one in its window</dd></dl>
<h3>Terminal options; if used before the first &#8211;window or &#8211;tab argument, sets the default for all terminals:</h3>
<dl>
<dt><code>-e</code>, <code>&#8211;command</code></dt>
<dd> Execute the argument to this option inside the terminal</dd>
<dt><code>-x</code>, <code>&#8211;execute</code></dt>
<dd> Execute the remainder of the command line inside the terminal</dd>
<dt><code>&#8211;profile</code>=<i>PROFILE-NAME</i></dt>
<dd> Use the given profile instead of the default profile</dd>
<dt><code>-t</code>, <code>&#8211;title</code>=<i>TITLE</i></dt>
<dd> Set the terminal title</dd>
<dt><code>&#8211;working-directory</code>=<i>DIRNAME</i></dt>
<dd> Set the working directory</dd>
<dt><code>&#8211;zoom</code>=<i>ZOOM</i></dt>
<dd> Set the terminal&#8217;s zoom factor (1.0 = normal size)</dd></dl>
<p> GTK+ Options</p>
<dl>
<dt><code>&#8211;class</code>=<i>CLASS</i></dt>
<dd> Program class as used by the window manager</dd>
<dt><code>&#8211;name</code>=<i>NAME</i></dt>
<dd> Program name as used by the window manager</dd>
<dt><code>&#8211;screen</code>=<i>SCREEN</i></dt>
<dd> X screen to use</dd>
<dt><code>&#8211;sync</code></dt>
<dd> Make X calls synchronous</dd>
<dt><code>&#8211;gtk-module</code>=<i>MODULES</i></dt>
<dd> Load additional GTK+ modules</dd>
<dt><code>&#8211;g-fatal-warnings</code></dt>
<dd> Make all warnings fatal</dd></dl>
<h3>Session management options:</h3>
<dl>
<dt><code>&#8211;sm-client-disable</code></dt>
<dd> Disable connection to session manager</dd>
<dt><code>&#8211;sm-client-state-file</code>=<i>FILE</i></dt>
<dd> Specify file containing saved configuration</dd>
<dt><code>&#8211;sm-client-id</code>=<i>ID</i></dt>
<dd> Specify session management ID</dd></dl>
<h3>Application Options:</h3>
<dl>
<dt><code>&#8211;disable-factory</code></dt>
<dd> Do not register with the activation nameserver, do not re-use an active terminal</dd>
<dt><code>&#8211;load-config</code>=<i>FILE</i></dt>
<dd> Load a terminal configuration file</dd>
<dt><code>&#8211;save-config</code>=<i>FILE</i></dt>
<dd> Save the terminal configuration to a file</dd>
<dt><code>&#8211;display</code>=<i>DISPLAY</i></dt>
<dd> X display to use</dd></dl>
<h2>Author</h2>
<p> Adam Erdman &lt;hekel [at] archlinux.info&gt; (2014) and Abel McClendon &lt;hcmmac [at] hosscomm.com&gt; (2014) </p>
<p> for the <code>Mate Documentation Team.</code></p>
<h2>See Also</h2>
<p> The full documentation for <code>mate-terminal</code> is maintained as a Texinfo manual. </p>
<p> If the <code>info</code> and <code>mate-terminal</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info mate-terminal</code></dd></dl>
<p> should give you access to the complete manual. </p>
<p> More <code>MATE Terminal</code> documentation can be found from the <code>Help</code> menu, or by pressing the <code>F1</code> key. </p>
<p> Further information may also be available at: <code><a rel="nofollow" href="http://wiki.mate-desktop.org/docs">http://wiki.mate-desktop.org/docs</a></code> </p>
