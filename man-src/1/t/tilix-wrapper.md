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
<dt><code>-h &#8211;help </code></p>
<dd>Show help options.</p>
<dt><code>-v &#8211;version</code></p>
<dd>Show the version of Tilix as well as the versions of dependent components.</p>
<dt><code>-w &#8211;working-directory=DIRECTORY</code></p>
<dd>Set the working directory of the terminal.</p>
<dt><code>-p &#8211;profile=PROFILE_NAME</code></p>
<dd>Set the starting profile using the name of one of the existing profiles. If a name is passed that does not correspond to an existing profile, the default profile will be used.</p>
<dt><code>-t &#8211;title=TITLE</code></p>
<dd>Set the title of the new terminal.</p>
<dt><code>-s &#8211;session=SESSION_NAME</code></p>
<dd>Open the specified session file which has been previously saved. Session files are saved from within Tilix, they store the complete layout of the session enabling the user to re-load it when required. Note that only the layout and layout options are saved, this will not restore the terminal to where it was left off, rather new terminals are created.</p>
<dt><code>-a &#8211;action=ACTION_NAME</code></p>
<dd>Perform an action in the current Tilix instance, the following actions are supported:</p>
<dd><code>session-add-right</code> Adds a new terminal to the right of the current terminal.</p>
<dd><code>session-add-down</code> Adds a new terminal down from the current terminal.</p>
<dd><code>app-new-session</code> Creates a new Tilix session within the current window.</p>
<dd><code>app-new-window</code> Creates a new Tilix window.</p>
<dt><code>-e &#8211;command=COMMAND</code></p>
<dd>Execute all text after this parameter as a command, thus this parameter must be the last parameter.</p>
<dt><code>&#8211;maximize</code></p>
<dd>Maximize the terminal window.</p>
<dt><code>&#8211;minimize</code></p>
<dd>Minimize the terminal window.</p>
<dt><code>&#8211;full-screen</code></p>
<dd>Full-screen the terminal window.</p>
<dt><code>&#8211;focus-window</code></p>
<dd>Focus the existing window.</p>
<dt><code>&#8211;new-process</code></p>
<dd>Start an additional Tilix instance as a new process. By default and as per GTK+ 3 guidelines, Tilix maintains a single process that all windows belong to. This option forces Tilix to start as a separate process. This is not recommended and is intended for debugging purposes only, using this option will prevent different Tilix windows from communicating with each other.</p>
<dt><code>&#8211;geometry=GEOMETRY</code></p>
<dd>Set the window size; for example: 80&#215;24, or 80&#215;24+200+200 (COLSxROWS+X+Y).</p>
<dt><code>-q &#8211;quake</code></p>
<dd>Open a window in quake mode or toggle existing quake mode window visibility.</p>
<dt><code>&#8211;preferences</code></p>
<dd>Show the Tilix preferences dialog directly.</dl>
<h2>See Also</h2>
<p>None</p>
<h2>Bugs</h2>
<p>See bugs at <a rel="nofollow" href="https://github.com/gnunn1/tilix/issues">https://github.com/gnunn1/tilix/issues</a></p>
<h2>Author</h2>
<p>Gerald Nunn and other contributors.</p>
