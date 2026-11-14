---
title: "lircrcd(1)"
name: "lircrcd"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lircrcd/"
description: "lircrcd – daemon to handle consistent .lircrc state among client applications"
---

<h2>NAME</h2>
<p> lircrcd &#8211; daemon to handle consistent .lircrc state among client applications</p>
<h2>SYNOPSIS</h2>
<p> <code>lircrcd</code> [<i>options</i>] <i>config-file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>lircrcd</code> reads the given .lircrc config file and synchronises the mode that the LIRC clients using this config file (<code><a href="/docs/linux/man/1-irexec/">irexec</a></code>(1), <code><a href="/docs/linux/man/1-irxevent/">irxevent</a></code>(1) , etc.) are in. Using <code>lircrcd</code> has to be explicitly enabled in the config file by adding the following line at the beginning of the file:<br />
 #! lircrcd</p>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd> display this message</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd> display version</p>
<dt><code>-p</code> <code>&#8211;permission</code>=<i>mode</i></p>
<dd> file permissions for socket</p>
<dt><code>-o</code> <code>&#8211;output</code>=<i>socket</i></p>
<dd> output socket filename</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-p, &#8211;premission=</code><i>mode</i></p>
<dd> The &#8211;permission option gives the file permission of the Unix domain socket lircrcd creates on startup in octal representation. Read the documentation for chmod for further details. If no &#8211;permission option is given when the socket is created the default is to give only the user owning the file read and write permissions (0600 in octal representation).</p>
<dt><code>-o, &#8211;output=</code><i>socket</i></p>
<dd> With the &#8211;output option you can select the Unix domain socket, which lircrcd will create. The default is to append a &quot;d&quot; character to the config filename given.</dl>
<h2>SEE ALSO</h2>
<p> The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
<h2>Index</h2>
