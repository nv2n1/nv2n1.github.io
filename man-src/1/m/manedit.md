---
title: "manedit(1)"
name: "manedit"
section: "1"
letter: "m"
url: "/docs/linux/man/1-manedit/"
description: "manedit – UNIX Manual Page IDE"
---

<h2>NAME</h2>
<p> manedit &#8211; UNIX Manual Page IDE</p>
<h2>SYNTAX</h2>
<p> <code>manedit</code> [<i>section</i>] [<i>manual_page</i>] [<i>options</i>] [<i>GUI_options</i>]</p>
<h2>DESCRIPTION</h2>
<p> ManEdit is an integrated UNIX manual page development environment (IDE) using the GIMP Tool Kit (GTK). </p>
<p> Editing of UNIX manual pages is done using ManEdit&#8217;s Editor, which edits UNIX manual pages using a simplified version of the XML format, eliminating the need for the user to use the more complex GROFF/TROFF format (native UNIX manual page format). </p>
<p> The UNIX manual page that you are editing can then be viewed at any time using ManEdit&#8217;s Viewer by going to View-&gt;Preview. </p>
<p> To start learning how to create and edit UNIX manual pages using ManEdit, run <code>manedit</code> and go to Help-&gt;Tutorial. </p>
<p> The [<i>section</i>] specifies the section number from 1 to 8 (used only with the <code>&#8211;viewer</code> option). </p>
<p> The [<i>manual_page</i>] specifies the path to the manual page file to open at startup or the name of the manual page when using the <code>&#8211;viewer</code> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config</code> &lt;<i>path</i>&gt;</p>
<dd> Specifies the configuration file.</p>
<dt><code>&#8211;rcfile</code></p>
<dd> Same as <code>&#8211;config</code>.</p>
<dt><code>-f</code></p>
<dd> Same as <code>&#8211;config</code>.</p>
<dt><code>&#8211;viewer</code></p>
<dd> Specifies to start up with the Viewer.</p>
<dt><code>&#8211;help</code></p>
<dd> Prints the help screen and exits.</p>
<dt><code>&#8211;version</code></p>
<dd> Prints the version information and exits.</dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.maneditrc</p>
<dd> Local configuration file.</p>
<dt>/usr/share/manedit/</p>
<dd> Global program directory.</p>
<dt>/usr/share/manedit/help/</p>
<dd> Help and tutorial files.</p>
<dt>/usr/share/manedit/templates/</p>
<dd> Manual page template files, used in the creation of new manual pages.</p>
<dt>/usr/man</p>
<dd> Global manual pages directory.</p>
<dt>/usr/share/man</p>
<dd> Global manual pages directory (used by newer UNIX distributions).</p>
<dt>/usr/share/man</p>
<dd> Global X11 manual pages directory.</p>
<dt>/usr/local/share/man</p>
<dd> Global local manual pages directory.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>BROWSER</code></p>
<dd> Fallback for <code>HELPBROWSER</code>.</p>
<dt><code>HELPBROWSER</code></p>
<dd> Specifies the command to execute the preferred help browser.</p>
<dt><code>HOME</code></p>
<dd> Specifies the path to the user&#8217;s home directory.</p>
<dt><code>TMPDIR</code></p>
<dd> Specifies the path to the temporary files directory.</p>
<dt><code>USER</code></p>
<dd> Fallback for <code>USERNAME</code>.</p>
<dt><code>USERNAME</code></p>
<dd> Specifies the user&#8217;s name.</dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way, type: </p>
<p> # manedit &amp; </p>
<p> To run this program and load a manual page at startup, type: </p>
<p> # manedit [<i>manual_page</i>] &amp; </p>
<p> You can run it as a viewer by specifying the &#8211;viewer option so that it starts up with a viewer instead of an editor window: </p>
<p> # manedit &#8211;viewer [<i>manual_page</i>] &amp;</p>
<h2>AUTHORS</h2>
<dl>
<dt>Tara Milana</p>
<dd> Head programmer</p>
<dt>Dan Stimits</p>
<dd> Programmer</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1) <code><a href="/docs/linux/man/1-manview/">manview</a></code>(1) </p>
<h2>Index</h2>
