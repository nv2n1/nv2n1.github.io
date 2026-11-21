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
<p> ManEdit is an integrated UNIX manual page development environment (IDE) using the GIMP Tool Kit (GTK). </p>
<p> Editing of UNIX manual pages is done using ManEdit&#8217;s Editor, which edits UNIX manual pages using a simplified version of the XML format, eliminating the need for the user to use the more complex GROFF/TROFF format (native UNIX manual page format). </p>
<p> The UNIX manual page that you are editing can then be viewed at any time using ManEdit&#8217;s Viewer by going to View-&gt;Preview. </p>
<p> To start learning how to create and edit UNIX manual pages using ManEdit, run <code>manedit</code> and go to Help-&gt;Tutorial. </p>
<p> The [<i>section</i>] specifies the section number from 1 to 8 (used only with the <code>&#8211;viewer</code> option). </p>
<p> The [<i>manual_page</i>] specifies the path to the manual page file to open at startup or the name of the manual page when using the <code>&#8211;viewer</code> option.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;config</code> &lt;<i>path</i>&gt;</dt>
<dd> Specifies the configuration file.</dd>
<dt><code>&#8211;rcfile</code></dt>
<dd> Same as <code>&#8211;config</code>.</dd>
<dt><code>-f</code></dt>
<dd> Same as <code>&#8211;config</code>.</dd>
<dt><code>&#8211;viewer</code></dt>
<dd> Specifies to start up with the Viewer.</dd>
<dt><code>&#8211;help</code></dt>
<dd> Prints the help screen and exits.</dd>
<dt><code>&#8211;version</code></dt>
<dd> Prints the version information and exits.</dd></dl>
<h2>FILES</h2>
<dl>
<dt>$HOME/.maneditrc</dt>
<dd> Local configuration file.</dd>
<dt>/usr/share/manedit/</dt>
<dd> Global program directory.</dd>
<dt>/usr/share/manedit/help/</dt>
<dd> Help and tutorial files.</dd>
<dt>/usr/share/manedit/templates/</dt>
<dd> Manual page template files, used in the creation of new manual pages.</dd>
<dt>/usr/man</dt>
<dd> Global manual pages directory.</dd>
<dt>/usr/share/man</dt>
<dd> Global manual pages directory (used by newer UNIX distributions).</dd>
<dt>/usr/share/man</dt>
<dd> Global X11 manual pages directory.</dd>
<dt>/usr/local/share/man</dt>
<dd> Global local manual pages directory.</dd></dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>BROWSER</code></dt>
<dd> Fallback for <code>HELPBROWSER</code>.</dd>
<dt><code>HELPBROWSER</code></dt>
<dd> Specifies the command to execute the preferred help browser.</dd>
<dt><code>HOME</code></dt>
<dd> Specifies the path to the user&#8217;s home directory.</dd>
<dt><code>TMPDIR</code></dt>
<dd> Specifies the path to the temporary files directory.</dd>
<dt><code>USER</code></dt>
<dd> Fallback for <code>USERNAME</code>.</dd>
<dt><code>USERNAME</code></dt>
<dd> Specifies the user&#8217;s name.</dd></dl>
<h2>EXAMPLES</h2>
<p> To run this program the standard way, type: </p>
<p> # manedit &amp; </p>
<p> To run this program and load a manual page at startup, type: </p>
<p> # manedit [<i>manual_page</i>] &amp; </p>
<p> You can run it as a viewer by specifying the &#8211;viewer option so that it starts up with a viewer instead of an editor window: </p>
<p> # manedit &#8211;viewer [<i>manual_page</i>] &amp;</p>
<h2>AUTHORS</h2>
<dl>
<dt>Tara Milana</dt>
<dd> Head programmer</dd>
<dt>Dan Stimits</dt>
<dd> Programmer</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-man/">man</a></code>(1) <code>manview</code>(1) </p>
