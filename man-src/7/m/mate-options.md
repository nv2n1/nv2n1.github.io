---
title: "mate-options(7)"
name: "mate-options"
section: "7"
letter: "m"
url: "/docs/linux/man/7-mate-options/"
description: "mate-options – Standard Command Line Options for MATE Programs"
---

<p>mate-options &#8211; Standard Command Line Options for MATE Programs</p>
<h2>Synopsis</h2>
<p><i>program </i>[<i>standard options</i>] [<i>specific options</i>] <i>arguments</i></p>
<h2>Description</h2>
<p>This manual page describes the command line options, which are common to all Mate applications.</p>
<h2>Options</h2>
<h3>Help options</h3>
<dl>
<dt><code>-?</code>, <code>&#8211;help</code></p>
<dd>Show the applications help message.</p>
<dt><code>&#8211;usage</code></p>
<dd>Display a brief usage message.</p>
<dt><code>&#8211;version</code></p>
<dd>Show the applications&#8217;s version information.</dl>
<h3>MateComponent Activation support</h3>
<dl>
<dt><code>&#8211;oaf-ior-fd</code>=<i>FD</i></p>
<dd>File descriptor to print IOR on</p>
<dt><code>&#8211;oaf-activate-iid</code>=<i>IID</i></p>
<dd>IID to activate</p>
<dt><code>&#8211;oaf-private</code></p>
<dd>Prevent registering of server with OAF</dl>
<h3>MATE library options</h3>
<dl>
<dt><code>&#8211;disable-sound</code></p>
<dd>Disable sound server usage</p>
<dt><code>&#8211;enable-sound</code></p>
<dd>Enable sound server usage</p>
<dt><code>&#8211;espeaker</code>=<i>HOSTNAME</i>:PORT</p>
<dd><i>Host</i>:<i>port</i> on which the <code>esd</code> sound server to use is running. This is useful if you simultaneously run programs on several machines.</dl>
<h3>MATE GUI options</h3>
<dl>
<dt><code>&#8211;disable-crash-dialog</code></p>
<dd>Disable the crash dialog, which is normally shown when the application segfaults.</dl>
<h3>Session management options</h3>
<dl>
<dt><code>&#8211;sm-client-id</code>=<i>ID</i></p>
<dd>Specify session management ID. Only used by the session manager itself while restarting the application.</p>
<dt><code>&#8211;sm-config-prefix</code>=<i>PREFIX</i></p>
<dd>Specify prefix of saved configuration.</p>
<dt><code>&#8211;sm-disable</code></p>
<dd>Disable connection to session manager.</dl>
<h3>Other options</h3>
<dl>
<dt><code>&#8211;load-modules</code>=<i>MODULE1</i>,MODULE2,&#8230;</p>
<dd>Dynamic modules to load</dl>
<h2>See Also</h2>
<p>For most MATE programs there will be additional command line options, which are specific to the program. These will be explained in the <i>Application options</i> section of the <i>&#8211;help</i> output and in the application&#8217;s online help.</p>
<h2>Author</h2>
<p>This manual page was written by Jochen Voss &lt;voss [at] debian.org&gt;. A first version was generated with the help of the <i>help2man</i> program. The program&#8217;s output was manually edited later.</p>
