---
title: "gnome-terminal-wrapper(1)"
name: "gnome-terminal-wrapper"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gnome-terminal-wrapper/"
description: "gnome-terminal – A terminal emulator for GNOME"
---

<p>gnome-terminal &#8211; A terminal emulator for GNOME </p>
<h2>Synopsis</h2>
<dl>
<dt> <code>gnome-terminal</code> [<i>OPTION</i>&#8230;] [&#8211; <i>PROGRAM</i> [<i>ARG</i>&#8230;]]</dl>
<h2>Description</h2>
<p><code>gnome-terminal</code></p>
<dd>is a terminal emulator application for accessing a UNIX shell environment which can be used to run programs available on your system. It supports several profiles, multiple tabs and implements several keyboard shortcuts.</p>
<h2>Options</h2>
<p><code>&#8211;help, -h</code></p>
<dl>
<dd>Show a brief overview of all the options.</dl>
<p> <code>&#8211;help-all</code></p>
<dl>
<dd>Show all the options in detail.</dl>
<p> <code>&#8211;help-gtk</code></p>
<dl>
<dd>Show all the GTK options.</dl>
<p> <code>&#8211;help-terminal</code></p>
<dl>
<dd>Show all the options to select between new terminal tabs or windows.</dl>
<p> <code>&#8211;help-terminal-options</code></p>
<dl>
<dd>Show all the options to change the attributes of terminals regardless of whether they are in separate tabs or windows.</dl>
<p> <code>&#8211;help-window-options</code></p>
<dl>
<dd>Show all the options to change the attributes of windows containing terminals.</dl>
<p> <code>&#8211;load-config=FILE</code></p>
<dl>
<dd>Restore the application to a previously saved state by loading it from a configuration file.</dl>
<p> <code>&#8211;preferences</code></p>
<dl>
<dd>Show the preferences window.</dl>
<p> <code>&#8211;print-environment, -p</code></p>
<dl>
<dd>Print the environment variables to interact with newly created terminals.</dl>
<p> <code>&#8211;quiet, -q</code></p>
<dl>
<dd>Suppress diagnostics.</dl>
<p> <code>&#8211;verbose, -v</code></p>
<dl>
<dd>Increase diagnostic verbosity.</dl>
<p> <code>&#8211;tab</code></p>
<dl>
<dd>Open a new tab containing a terminal in the last-opened window with the default profile.</dl>
<p> <code>&#8211;window</code></p>
<dl>
<dd>Open a new window with a tab containing a terminal with the default profile.</dl>
<p> <code>&#8211;command, -e=COMMAND</code></p>
<dl>
<dd>Split the argument to this option into a program and arguments in the same way a shell would, and execute the resulting command-line inside the terminal. </p>
<p> This option is deprecated. Instead, use <code>&#8212;</code> to terminate the options, and put the program and arguments to execute after it: for example, instead of <code>gnome-terminal -e &quot;python3 -q&quot;</code>, prefer to use <code>gnome-terminal &#8212; python3 -q</code>. </p>
<p> Note that the <i>COMMAND</i> is not run via a shell: it is split into words and executed as a program. If shell syntax is required, use the form <code>gnome-terminal &#8212; sh -c &#8216;&#8230;&#8217;</code>.</dl>
<p> <code>&#8211;execute PROGRAM [ARGS], -x PROGRAM [ARGS]</code></p>
<dl>
<dd>Stop parsing options at this point, and interpret all subsequent options as a program and arguments to execute inside the terminal. </p>
<p> This option is deprecated: use <code>&#8212;</code> instead. For example, instead of <code>gnome-terminal -x python3 -q</code>, prefer to use <code>gnome-terminal &#8212; python3 -q</code>.</dl>
<p> <code>&#8211;fd=FD</code></p>
<dl>
<dd>Forward file descriptor.</dl>
<p> <code>&#8211;profile=PROFILE-NAME</code></p>
<dl>
<dd>Use the given profile instead of the default profile.</dl>
<p> <code>&#8211;title, -t=TITLE</code></p>
<dl>
<dd>Set the initial terminal title.</dl>
<p> <code>&#8211;wait</code></p>
<dl>
<dd>Wait until the terminal&#8217;s child exits.</dl>
<p> <code>&#8211;working-directory=DIRNAME</code></p>
<dl>
<dd>Set the terminal&#8217;s working directory.</dl>
<p> <code>&#8211;zoom=ZOOM</code></p>
<dl>
<dd>Set the terminal&#8217;s zoom factor. 1.0 is normal size.</dl>
<p> <code>&#8211;active</code></p>
<dl>
<dd>Set the last specified tab as the active one in its window.</dl>
<p> <code>&#8211;full-screen</code></p>
<dl>
<dd>Full-screen the window.</dl>
<p> <code>&#8211;geometry=GEOMETRY</code></p>
<dl>
<dd>Set the window size as COLSxROWS+X+Y. For example, 80&#215;24 or 80&#215;24+200+200.</dl>
<p> <code>&#8211;hide-menubar</code></p>
<dl>
<dd>Turn off the menubar for the window.</dl>
<p> <code>&#8211;show-menubar</code></p>
<dl>
<dd>Turn on the menubar for the window.</dl>
<p> <code>&#8211;maximize</code></p>
<dl>
<dd>Maximize the window.</dl>
<p> <code>&#8211;role=ROLE</code></p>
<dl>
<dd>Set the X window role.</dl>
<p> <code>&#8211;class=CLASS</code></p>
<dl>
<dd>Program class as used by the window manager.</dl>
<p> <code>&#8211;display=DISPLAY</code></p>
<dl>
<dd>X display to use.</dl>
<p> <code>&#8211;g-fatal-warnings</code></p>
<dl>
<dd>Make all warnings fatal.</dl>
<p> <code>&#8211;gdk-debug=FLAGS</code></p>
<dl>
<dd>GDK debugging flags to set.</dl>
<p> <code>&#8211;gdk-no-debug=FLAGS</code></p>
<dl>
<dd>GDK debugging flags to unset.</dl>
<p> <code>&#8211;gtk-debug=FLAGS</code></p>
<dl>
<dd>GTK debugging flags to set.</dl>
<p> <code>&#8211;gtk-no-debug=FLAGS</code></p>
<dl>
<dd>GTK debugging flags to unset.</dl>
<p> <code>&#8211;gtk-module=MODULES</code></p>
<dl>
<dd>Load additional GTK modules.</dl>
<p> <code>&#8211;name=NAME</code></p>
<dl>
<dd>Program name as used by the window manager.</dl>
<h2>Bugs</h2>
<p>Please read m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/Apps/Terminal/ReportingBugs">https://wiki.gnome.org/Apps/Terminal/ReportingBugs</a></code>m[] on how to report bugs.</p>
<h2>Examples</h2>
<p>To run a terminal containing an interactive Python prompt: </p>
<dl>
<dd>
<pre> gnome-terminal --title=Python -- python3 -q</pre>
</dl>
<p> To interpret shell syntax in a terminal, either write it in a separate shell script, or use sh -c: </p>
<dl>
<dd>
<pre> gnome-terminal -- sh -c 'if [ &quot;$(id -u)&quot; = 0 ]; then ...'</pre>
</dl>
<h2>See Also</h2>
<p>For further information, visit the website m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/Apps/Terminal">https://wiki.gnome.org/Apps/Terminal</a></code>m[]. There&#8217;s a list of frequently asked questions at m[blue]<code><a rel="nofollow" href="https://wiki.gnome.org/Apps/Terminal/FAQ">https://wiki.gnome.org/Apps/Terminal/FAQ</a></code>m[].</p>
