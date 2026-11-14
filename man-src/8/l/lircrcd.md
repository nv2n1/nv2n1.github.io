---
title: "lircrcd(8)"
name: "lircrcd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lircrcd/"
description: "lircrcd – daemon to handle consistent .lircrc state among client applications"
---

<p>lircrcd &#8211; daemon to handle consistent .lircrc state among client applications</p>
<h2>Synopsis</h2>
<p><code>lircrcd</code> [<i>options</i>] <i>config-file</i></p>
<h2>Description</h2>
<p><code>lircrcd</code> reads the given .lircrc config file and synchronises the mode that the LIRC clients such as (<code><a href="/docs/linux/man/1-irexec/">irexec</a></code>(1), <code><a href="/docs/linux/man/1-irxevent/">irxevent</a></code>(1) , etc.) are in. Using <code>lircrcd</code> has to be explicitly enabled in the lircrc config file by adding the following line at the beginning of the file:</p>
<dl>
<dd>lircrc_class default</dl>
<p> This must be done at the top-level file, not an included one. The lircrc_class string (here &quot;default&quot;) could actually be anything; clients using the same string in their lircrc will be synchronized.</p>
<h2>Options</h2>
<dl>
<dt><code>-h</code> <code>&#8211;help</code></p>
<dd>display help message</p>
<dt><code>-v</code> <code>&#8211;version</code></p>
<dd>display version</p>
<dt><code>-p, &#8211;permission=</code><i>mode</i></p>
<dd>The &#8211;permission option gives the file permission of the Unix domain socket lircrcd creates on startup in octal representation. Read the documentation for chmod for further details. If no &#8211;permission option is given when the socket is created the default is to give only the user owning the file read and write permissions (0600 in octal representation).</p>
<dt><code>-o, &#8211;output=</code><i>socket</i></p>
<dd>With the &#8211;output option you can select the Unix domain socket, which lircrcd will create. The default is to create a socket in VARRUNDIR (usually /var/run/lirc), see FILES.</dl>
<h2>Files</h2>
<p>lircrcd creates its socket(s) in the VARRUNDIR directory, usually /var/run/lirc. The socket basename includes the user UID and the string from the lircrc_class option.</p>
<h2>See Also</h2>
<p>The documentation for <code>lirc</code> is maintained as html pages. They are located under html/ in the documentation directory. </p>
