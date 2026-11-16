---
title: "tilix-wrapper(1)"
name: "tilix-wrapper"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tilix-wrapper/"
description: "tilix – Tiling GTK3 terminal emulator for GNOME"
---

<p><code>tilix</code> &#8211; Tiling GTK3 terminal emulator for GNOME </p>
<h2>Synopsis</h2>
<p><code>tilix</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>tilix</code> is an advanced GTK3 tiling terminal emulator designed to adhere to Gnome Human Interface Guidelines.</p>
<h2>Options</h2>
<p>The <code>tilix</code> application accepts the following command line parameters:</p>
<dl COMPACT>
<dt><code>-h &#8211;help </code></dt>
<dd>Show help options.</dd>
<dt><code>-v &#8211;version</code></dt>
<dd>Show the version of Tilix as well as the versions of dependent components.</dd>
<dt><code>-w &#8211;working-directory=DIRECTORY</code></dt>
<dd>Set the working directory of the terminal.</dd>
<dt><code>-p &#8211;profile=PROFILE_NAME</code></dt>
<dd>Set the starting profile using the name of one of the existing profiles. If a name is passed that does not correspond to an existing profile, the default profile will be used.</dd>
<dt><code>-t &#8211;title=TITLE</code></dt>
<dd>Set the title of the new terminal.</dd>
<dt><code>-s &#8211;session=SESSION_NAME</code></dt>
<dd>Open the specified session file which has been previously saved. Session files are saved from within Tilix, they store the complete layout of the session enabling the user to re-load it when required. Note that only the layout and layout options are saved, this will not restore the terminal to where it was left off, rather new terminals are created.</dd>
<dt><code>-a &#8211;action=ACTION_NAME</code></dt>
<dd>Perform an action in the current Tilix instance, the following actions are supported:</dd>
<dd><code>session-add-right</code> Adds a new terminal to the right of the current terminal.</dd>
<dd><code>session-add-down</code> Adds a new terminal down from the current terminal.</dd>
<dd><code>app-new-session</code> Creates a new Tilix session within the current window.</dd>
<dd><code>app-new-window</code> Creates a new Tilix window.</dd>
<dt><code>-e &#8211;command=COMMAND</code></dt>
<dd>Execute all text after this parameter as a command, thus this parameter must be the last parameter.</dd>
<dt><code>&#8211;maximize</code></dt>
<dd>Maximize the terminal window.</dd>
<dt><code>&#8211;minimize</code></dt>
<dd>Minimize the terminal window.</dd>
<dt><code>&#8211;full-screen</code></dt>
<dd>Full-screen the terminal window.</dd>
<dt><code>&#8211;focus-window</code></dt>
<dd>Focus the existing window.</dd>
<dt><code>&#8211;new-process</code></dt>
<dd>Start an additional Tilix instance as a new process. By default and as per GTK+ 3 guidelines, Tilix maintains a single process that all windows belong to. This option forces Tilix to start as a separate process. This is not recommended and is intended for debugging purposes only, using this option will prevent different Tilix windows from communicating with each other.</dd>
<dt><code>&#8211;geometry=GEOMETRY</code></dt>
<dd>Set the window size; for example: 80&#215;24, or 80&#215;24+200+200 (COLSxROWS+X+Y).</dd>
<dt><code>-q &#8211;quake</code></dt>
<dd>Open a window in quake mode or toggle existing quake mode window visibility.</dd>
<dt><code>&#8211;preferences</code></dt>
<dd>Show the Tilix preferences dialog directly.</dd></dl>
<h2>See Also</h2>
<p>None</p>
<h2>Bugs</h2>
<p>See bugs at <a rel="nofollow" href="https://github.com/gnunn1/tilix/issues">https://github.com/gnunn1/tilix/issues</a></p>
<h2>Author</h2>
<p>Gerald Nunn and other contributors.</p>
