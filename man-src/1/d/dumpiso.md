---
title: "dumpiso(1)"
name: "dumpiso"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dumpiso/"
description: "dumpiso – dump IEEE 1394 isochronous channel packets"
---

<h2>NAME</h2>
<p> dumpiso &#8211; dump IEEE 1394 isochronous channel packets</p>
<h2>SYNOPSIS</h2>
<p> <code>dumpiso</code> [ <i>options</i> ] [ <i>FILE</i> ]</p>
<h2>DESCRIPTION</h2>
<p> dumpiso listens on a selected range of channels and dumps all received packets into the file <i>FILE</i> or, if not given, to standard output. While dumping, the current number of received packets is written to standard error and updated with every packet. </p>
<p> It uses a simple file format for the dumps which is described in <code><a href="/docs/linux/man/5-isodump/">isodump</a></code>(5). The dumped packets can be sent out again with <code><a href="/docs/linux/man/1-sendiso/">sendiso</a></code>(1).</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code>,<code> &#8211;channels=</code><i>CHANNELS</i></p>
<dd> Sets the channels to listen on. <i>CHANNELS</i> can be either a single number, in which case this is the only channel to listen on, or a range of channels in the form X-Y. Channel numbers can range from 0 to 63. You can give this option multiple times, new channels are added to the list of already set channels. Defaults to all channels.</p>
<dt><code>-p</code>,<code> &#8211;port=</code><i>PORT</i></p>
<dd> Choose port <i>PORT</i> for receiving. A port is a 1394 card or chip and represents one connected bus, therefore this is only relevant when you have multiple of these. Defaults to 0.</p>
<dt><code>-h</code>,<code> &#8211;help</code></p>
<dd> Show help text and exit.</dl>
<h2>BUGS</h2>
<p> None known.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-sendiso/">sendiso</a></code>(1), <code><a href="/docs/linux/man/5-isodump/">isodump</a></code>(5)</p>
<h2>AUTHOR</h2>
<p> Andreas Bombe &lt;aeb [at] debian.org&gt; </p>
<h2>Index</h2>
