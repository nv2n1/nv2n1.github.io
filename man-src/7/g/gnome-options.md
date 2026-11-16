---
title: "gnome-options(7)"
name: "gnome-options"
section: "7"
letter: "g"
url: "/docs/linux/man/7-gnome-options/"
description: "gnome-options – Standard Command Line Options for GNOME 2 Programs"
---

<p>gnome-options &#8211; Standard Command Line Options for GNOME 2 Programs</p>
<h2>Synopsis</h2>
<p><i>program </i>[<i>standard options</i>] [<i>specific options</i>] <i>arguments</i></p>
<h2>Description</h2>
<p>This manual page describes the command line options, which are common to all Gnome applications.</p>
<h2>Options</h2>
<h3>Help options</h3>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></dt>
<dd>Show the application&#8217;s help message.</dd>
<dt><code>&#8211;usage</code></dt>
<dd>Display a brief usage message.</dd>
<dt><code>&#8211;version</code></dt>
<dd>Show the application&#8217;s version information.</dd></dl>
<h3>Bonobo Activation support</h3>
<dl>
<dt><code>&#8211;oaf-ior-fd</code>=<i>FD</i></dt>
<dd>File descriptor to print IOR on</dd>
<dt><code>&#8211;oaf-activate-iid</code>=<i>IID</i></dt>
<dd>IID to activate</dd>
<dt><code>&#8211;oaf-private</code></dt>
<dd>Prevent registering of server with OAF</dd></dl>
<h3>GNOME library options</h3>
<dl>
<dt><code>&#8211;disable-sound</code></dt>
<dd>Disable sound server usage</dd>
<dt><code>&#8211;enable-sound</code></dt>
<dd>Enable sound server usage</dd>
<dt><code>&#8211;espeaker</code>=<i>HOSTNAME</i>:PORT</dt>
<dd><i>Host</i>:<i>port</i> on which the <code>esd</code> sound server to use is running. This is useful if you simultaneously run programs on several machines.</dd></dl>
<h3>GNOME GUI options</h3>
<dl>
<dt><code>&#8211;disable-crash-dialog</code></dt>
<dd>Disable the crash dialog, which is normally shown when the application segfaults.</dd></dl>
<h3>Session management options</h3>
<dl>
<dt><code>&#8211;sm-client-id</code>=<i>ID</i></dt>
<dd>Specify session management ID. Only used by the session manager itself while restarting the application.</dd>
<dt><code>&#8211;sm-config-prefix</code>=<i>PREFIX</i></dt>
<dd>Specify prefix of saved configuration.</dd>
<dt><code>&#8211;sm-disable</code></dt>
<dd>Disable connection to session manager.</dd></dl>
<h3>Other options</h3>
<dl>
<dt><code>&#8211;load-modules</code>=<i>MODULE1</i>,MODULE2,&#8230;</dt>
<dd>Dynamic modules to load</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-gtk-options/">gtk-options</a></code>(7) </p>
<p> For most GNOME programs there will be additional command line options, which are specific to the program. These will be explained in the <i>Application options</i> section of the <i>&#8211;help</i> output and in the application&#8217;s online help.</p>
<h2>Author</h2>
<p>This manual page was written by Jochen Voss &lt;voss [at] debian.org&gt;. A first version was generated with the help of the <i>help2man</i> program. The program&#8217;s output was manually edited later.</p>
