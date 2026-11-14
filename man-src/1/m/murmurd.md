---
title: "murmurd(1)"
name: "murmurd"
section: "1"
letter: "m"
url: "/docs/linux/man/1-murmurd/"
description: "murmurd – VoIP server."
---

<h2>NAME</h2>
<p> murmurd &#8211; VoIP server.</p>
<h2>SYNOPSIS</h2>
<p> <code>murmurd</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> Murmur is the server component of Mumble, a low-latency, high quality VoIP application.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a summary of the options.</p>
<dt><code>-ini</code><i>&nbsp;<wbr>inifile</i></p>
<dd> Specify which inifile to use. Without this option, murmur will search for a murmur.ini file and will fall back to builtin defaults if one isn&#8217;t found.</p>
<dt><code>-fg</code></p>
<dd> Run in the foreground (do not fork).<br />
 This is very useful for debugging.</p>
<dt><code>-v</code></p>
<dd> Verbose mode, slightly more information is logged.</p>
<dt><code>-supw</code><i>&nbsp;<wbr>password</i><code>&nbsp;<wbr>[</code><i>serverid</i><code>]</code></p>
<dd> This will forcefully set the SuperUser password for a server. SuperUser is a special account (similar to root ) which bypasses all access controls. This command may be used while the server is running.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mumble/">mumble</a></code>(1), <code><a href="/docs/linux/man/1-murmur-wrapper/">murmur-wrapper</a></code>(1). </p>
<h2>AUTHOR</h2>
<p> mumble and murmurd was written by Thorvald Natvig &lt;slicer [at] users.sourceforge.net&gt;. </p>
<h2>Index</h2>
