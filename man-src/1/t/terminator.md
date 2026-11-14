---
title: "terminator(1)"
name: "terminator"
section: "1"
letter: "t"
url: "/docs/linux/man/1-terminator/"
description: "Terminator – Multiple GNOME terminals in one window"
---

<h2 class="name">NAME</h2>
<p> Terminator &#8211; Multiple GNOME terminals in one window </p>
<h2>SYNOPSIS</h2>
<p> <code>terminator</code> [<i>options</i>] </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents <code>Terminator</code>, a terminal emulator application. </p>
<p> <code>Terminator</code> is a program that allows users to set up flexible arrangements of GNOME terminals. It is aimed at those who normally arrange lots of terminals near each other, but don&#8217;t want to use a frame based window manager.</p>
<h2>OPTIONS</h2>
<p> This program follow the usual GNU command line syntax, with long options starting with two dashes (`-&#8216;). A summary of options is included below.</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options</p>
<dt><code>-v, &#8211;version</code></p>
<dd> Show the version of the Terminator installation</p>
<dt><code>-m, &#8211;maximise</code></p>
<dd> Start with a maximised window <code>-M, &#8211;maximize</code> Start with a maximized window</p>
<dt><code>-f, &#8211;fullscreen</code></p>
<dd> Start with a fullscreen window</p>
<dt><code>-b, &#8211;borderless</code></p>
<dd> Instruct the window manager not to render borders/decoration on the Terminator window (this works well with -m)</p>
<dt><code>-H, &#8211;hidden</code></p>
<dd> Hide the Terminator window by default. Its visibility can be toggled with the <code>hide_window</code> keyboard shortcut (Ctrl-Shift-Alt-a by default)</p>
<dt><code>-T, &#8211;title</code></p>
<dd> Force the Terminator window to use a specific name rather than updating it dynamically based on the wishes of the child shell.</p>
<dt><code>&#8211;geometry=GEOMETRY</code></p>
<dd> Specifies the preferred size and position of Terminator&#8217;s window; see <a href="/docs/linux/man/7-x/">X</a>(7).</p>
<dt><code>-e, &#8211;command=COMMAND</code></p>
<dd> Runs the specified command instead of your default shell or profile specified command. Note: if Terminator is launched as x-terminal-emulator -e behaves like -x, and the longform becomes &#8211;execute2=COMMAND</p>
<dt><code>-x, &#8211;execute COMMAND [ARGS]</code></p>
<dd> Runs <code>the rest of the command line</code> instead of your default shell or profile specified command.</p>
<dt><code>&#8211;working-directory=DIR</code></p>
<dd> Set the terminal&#8217;s working directory</p>
<dt><code>-g, &#8211;config FILE</code></p>
<dd> Use the specified FILE for configuration</p>
<dt><code>-r, &#8211;role=ROLE</code></p>
<dd> Set a custom WM_WINDOW_ROLE property on the window</p>
<dt><code>-l, &#8211;layout=LAYOUT</code></p>
<dd> Start Terminator with a specific layout. The argument here is the name of a saved layout.</p>
<dt><code>-s, &#8211;select-layout=LAYOUT</code></p>
<dd> Open the layout launcher window instead of the normal terminal.</p>
<dt><code>-p, &#8211;profile=PROFILE</code></p>
<dd> Use a different profile as the default</p>
<dt><code>-i, &#8211;icon=FORCEDICON</code></p>
<dd> Set a custom icon for the window (by file or name)</p>
<dt><code>-u, &#8211;no-dbus</code></p>
<dd> Disable DBus</p>
<dt><code>-d, &#8211;debug</code></p>
<dd> Enable debugging output (please use this when reporting bugs). This can be specified twice to enable a built-in python debugging server.</p>
<dt><code>&#8211;debug-classes=DEBUG_CLASSES</code></p>
<dd> If this is specified as a comma separated list, debugging output will only be printed from the specified classes.</p>
<dt><code>&#8211;debug-methods=DEBUG_METHODS</code></p>
<dd> If this is specified as a comma separated list, debugging output will only be printed from the specified functions. If this is specified in addition to &#8211;debug-classes, only the intersection of the two lists will be displayed</p>
<dt><code>&#8211;new-tab</code></p>
<dd> If this is specified and Terminator is already running, DBus will be used to spawn a new tab in the first Terminator window.</dl>
<h2>KEYBINDINGS</h2>
<p> The following default keybindings can be used to control Terminator:</p>
<dl>
<dt><code>F1</code></p>
<dd> Launches the full HTML manual.</dl>
<h3>Creation &amp; Destruction</h3>
<p> The following items relate to creating and destroying terminals.</p>
<dl>
<dt><code>Ctrl+Shift+O</code></p>
<dd> Split terminals H<code>o</code>rizontally.</p>
<dt><code>Ctrl+Shift+E</code></p>
<dd> Split terminals V<code>e</code>rtically.</p>
<dt><code>Ctrl+Shift+T</code></p>
<dd> Open new <code>t</code>ab.</p>
<dt><code>Ctrl+Shift+I</code></p>
<dd> Open a new window. (Note: Unlike in previous releases, this window is part of the same Terminator process.)</p>
<dt><code>Super+I</code></p>
<dd> Spawn a new Terminator process.</p>
<dt><code>Alt+L</code></p>
<dd> Open <code>l</code>ayout launcher.</p>
<dt><code>Ctrl+Shift+W</code></p>
<dd> Close the current terminal.</p>
<dt><code>Ctrl+Shift+Q</code></p>
<dd> Close the current window.</dl>
<h3>Navigation</h3>
<p> The following items relate to moving between and around terminals.</p>
<dl>
<dt><code>Alt+Up</code></p>
<dd> Move to the terminal <code>above</code> the current one.</p>
<dt><code>Alt+Down</code></p>
<dd> Move to the terminal <code>below</code> the current one.</p>
<dt><code>Alt+Left</code></p>
<dd> Move to the terminal <code>left of</code> the current one.</p>
<dt><code>Alt+Right</code></p>
<dd> Move to the terminal <code>right of</code> the current one.</p>
<dt><code>Ctrl+PageDown</code></p>
<dd> Move to next Tab.</p>
<dt><code>Ctrl+PageUp</code></p>
<dd> Move to previous Tab.</p>
<dt><code>Ctrl+Shift+N or Ctrl+Tab</code></p>
<dd> Move to <code>n</code>ext terminal within the same tab, use Ctrl+PageDown to move to the next tab. If <code>cycle_term_tab</code> is <code>False</code>, cycle within the same tab will be disabled.</p>
<dt><code>Ctrl+Shift+P or Ctrl+Shift+Tab</code></p>
<dd> Move to <code>p</code>revious terminal within the same tab, use Ctrl+PageUp to move to the previous tab. If <code>cycle_term_tab</code> is <code>False</code>, cycle within the same tab will be disabled.</dl>
<h3>Organisation</h3>
<p> The following items relate to arranging and resizing terminals.</p>
<dl>
<dt><code>Ctrl+Shift+Right</code></p>
<dd> Move parent dragbar <code>Right</code>.</p>
<dt><code>Ctrl+Shift+Left</code></p>
<dd> Move parent dragbar <code>Left</code>.</p>
<dt><code>Ctrl+Shift+Up</code></p>
<dd> Move parent dragbar <code>Up</code>.</p>
<dt><code>Ctrl+Shift+Down</code></p>
<dd> Move parent dragbar <code>Down</code>.</p>
<dt><code>Super+R</code></p>
<dd> <code>R</code>otate terminals clockwise.</p>
<dt><code>Super+Shift+R</code></p>
<dd> <code>R</code>otate terminals counter-clockwise.</p>
<dt></dl>
<h2>Drag and Drop</h2>
<dd> The layout can be modified by moving terminals with Drag and Drop. To start dragging a terminal, click and hold on its titlebar. Alternatively, hold down <code>Ctrl</code>, click and hold the <code>right</code> mouse button. Then, <code>**Release Ctrl**</code>. You can now drag the terminal to the point in the layout you would like it to be. The zone where the terminal would be inserted will be highlighted.</p>
<dl>
<dt><code>Ctrl+Shift+PageDown</code></p>
<dd> Swap tab position with next Tab.</p>
<dt><code>Ctrl+Shift+PageUp</code></p>
<dd> Swap tab position with previous Tab.</dl>
<h3>Miscellaneous</h3>
<p> The following items relate to miscellaneous terminal related functions.</p>
<dl>
<dt><code>Ctrl+Shift+C</code></p>
<dd> Copy selected text to clipboard.</p>
<dt><code>Ctrl+Shift+V</code></p>
<dd> Paste clipboard text.</p>
<dt><code>Ctrl+Shift+S</code></p>
<dd> Hide/Show <code>S</code>crollbar.</p>
<dt><code>Ctrl+Shift+F</code></p>
<dd> Search within terminal scrollback.</p>
<dt><code>Ctrl+Shift+R</code></p>
<dd> Reset terminal state.</p>
<dt><code>Ctrl+Shift+G</code></p>
<dd> Reset terminal state and clear window.</p>
<dt><code>Ctrl+Plus (+)</code></p>
<dd> Increase font size. <code>Note:</code> This may require you to press shift, depending on your keyboard.</p>
<dt><code>Ctrl+Minus (-)</code></p>
<dd> Decrease font size. <code>Note:</code> This may require you to press shift, depending on your keyboard.</p>
<dt><code>Ctrl+Zero (0)</code></p>
<dd> Restore font size to original setting.</p>
<dt><code>Ctrl+Alt+W</code></p>
<dd> Rename window title.</p>
<dt><code>Ctrl+Alt+A</code></p>
<dd> Rename tab title.</p>
<dt><code>Ctrl+Alt+X</code></p>
<dd> Rename terminal title.</p>
<dt><code>Super+1</code></p>
<dd> Insert terminal number, i.e. 1 to 12.</p>
<dt><code>Super+0</code></p>
<dd> Insert padded terminal number, i.e. 01 to 12.</dl>
<h3>Grouping &amp; Broadcasting</h3>
<p> The following items relate to helping to focus on a specific terminal.</p>
<dl>
<dt><code>F11</code></p>
<dd> Toggle window to fullscreen.</p>
<dt><code>Ctrl+Shift+X</code></p>
<dd> Toggle between showing all terminals and only showing the current one (maximise).</p>
<dt><code>Ctrl+Shift+Z</code></p>
<dd> Toggle between showing all terminals and only showing a scaled version of the current one (zoom).</p>
<dt><code>Ctrl+Shift+Alt+A</code></p>
<dd> Hide the initial window. Note that this is a global binding, and can only be bound once.</dl>
<p> The following items relate to grouping and broadcasting.</p>
<dl>
<dt><code>Super+T</code></p>
<dd> Group all terminals in the current tab so input sent to one of them, goes to all terminals in the current tab.</p>
<dt><code>Super+Shift+T</code></p>
<dd> Remove grouping from all terminals in the current tab.</p>
<dt><code>Super+G</code></p>
<dd> Group all terminals so that any input sent to one of them, goes to all of them.</p>
<dt><code>Super+Shift+G</code></p>
<dd> Remove grouping from all terminals.</p>
<dt><code>Alt+A</code></p>
<dd> Broadcast to All terminals.</p>
<dt><code>Alt+G</code></p>
<dd> Broadcast to Grouped terminals.</p>
<dt><code>Alt+O</code></p>
<dd> Broadcast Off.</dl>
<p> Most of these keybindings are changeable in the Preferences.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-terminator_config/">terminator_config</a>(5)</code></p>
<h2>AUTHOR</h2>
<p> Terminator was written by Chris Jones &lt;cmsj [at] tenshu.net&gt; and others. </p>
<p> This manual page was written by Chris Jones &lt;cmsj [at] tenshu.net&gt; and others. </p>
<h2>Index</h2>
