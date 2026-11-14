---
title: "irnet(4)"
name: "irnet"
section: "4"
letter: "i"
url: "/docs/linux/man/4-irnet/"
description: "irnet – IrNET protocol device"
---

<p>irnet &#8211; IrNET protocol device</p>
<h2>Description</h2>
<p>File <code>/dev/irnet</code> is used to access and configure the IrNET protocol part of the Linux-IrDA stack. </p>
<p> <code>IrNET</code> is a protocol allowing to create <i>TCP/IP connections</i> between two IrDA peers in an efficient fashion, and generally to enable standard networking over IrDA. It is a thin layer, passing PPP packets to IrTTP and vice versa. It uses <i>PPP</i> in synchronous mode, because IrTTP offer a reliable sequenced packet service (as opposed to a byte stream). In fact, you could see IrNET as carrying TCP/IP in a IrDA socket, using PPP to provide the glue. </p>
<p> The main difference with traditional <i>PPP over IrCOMM</i> is that it avoids the framing and serial emulation which are a performance bottleneck. It also allows multipoint communications in a sensible fashion. And finally, it can automatically handle incoming connections through <code>irnetd.</code> </p>
<p> The main difference with <i>IrLAN</i> is that we use PPP for the link management, which is more standard, interoperable and flexible than the IrLAN protocol. For example, PPP adds authentication, encryption, compression, header compression and automated routing setup. And, as IrNET let PPP do the hard work, the implementation is much simpler than IrLAN. </p>
<p> <code>IrNET</code> connections are initiated and managed with <i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8). File <code>/dev/irnet</code> also offer a <i>control channel</i>. Reads from <code>/dev/irnet</code> will return various <i>IrNET events</i>. Write to <code>/dev/irnet</code> allow to <i>configure</i> the IrNET connection.</p>
<h2>Configuration</h2>
<p>If your system does not have <code>/dev/irnet</code> created already, it can be created with the following commands: </p>
<pre> mknod -m 644 /dev/irnet c 10 187
 chown root:root /dev/irnet</pre>
<p>You will also need to have IrNET support in your kernel or as module and the Linux-IrDA stack installed and configured (see <i><a href="/docs/linux/man/8-irattach/">irattach</a></i>(8)). </p>
<p> File <code>/dev/irnet</code> is supposed to only be used with the <i>PPP line discipline</i> or for accessing the <i>control channel</i>, other use are unsupported. <code>IrNET</code> support multiple concurrent connections (limited by the IrDA stack), all those connections are multiplexed on a single <code>/dev/irnet</code> device (as opposed to IrCOMM which as one device per connection).</p>
<h2>Parameters</h2>
<p>Writing commands to <code>/dev/irnet</code> allow to <i>configure</i> the IrNET connection being made. This need to be done through <i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8) (see below for examples). Commands are separated by comas.</p>
<dl>
<dt><code>name</code><i> &lt;peer&gt;</i></p>
<dd>Connect to the IrDA device which IrDA nickname is <i>&lt;peer&gt;</i>. The IrDA nickname is a string up to 31 characters.</p>
<dt><code>daddr</code><i> &lt;peer&gt;</i></p>
<dd>Connect to the IrDA device which IrDA address is <i>&lt;peer&gt;</i>. The IrDA address is a 32 bits hexadecimal number.</p>
<dt><code>raddr</code><i> &lt;port&gt;</i></p>
<dd>Restrict connections to the local IrDA interface which IrDA address is <i>&lt;port&gt;</i>. The IrDA address is a 32 bits hexadecimal number.</dl>
<h2>Display</h2>
<p>Reading from <code>/dev/irnet</code> will show various <i>IrNET events</i>. This is usually done with the command <i>cat /dev/irnet</i>.</p>
<dl>
<dt><code>Found</code></p>
<dd>Dump of the current IrNET discovery log.</p>
<dt><code>Discovered </code></p>
<dd>New IrNET device discovered.</p>
<dt><code>Expired</code></p>
<dd>Previously discovered IrNET device no longer present.</p>
<dt><code>Connected to </code></p>
<dd>This computer successfully established an IrNET connection to a peer.</p>
<dt><code>Connection from </code></p>
<dd>A peer successfully established an IrNET connection to this computer.</p>
<dt><code>Request from</code></p>
<dd>A peer attempted to connect to this computer, but no IrNET connection was waiting for it.</p>
<dt><code>No-answer from</code></p>
<dd>This computer attempted to connect to a peer, but no IrNET connection was waiting for it.</p>
<dt><code>Blocked link with</code></p>
<dd>The IrDA link of the IrNET connection is currently blocked.</p>
<dt><code>Disconnection from</code></p>
<dd>A peer successfully terminated an IrNET connection with this computer.</p>
<dt><code>Disconnected to</code></p>
<dd>This computer successfully terminated an IrNET connection with a peer.</dl>
<p> File <code>/proc/net/irda/irnet</code> will also show the current state of the various IrNET connections.</p>
<h2>Example</h2>
<p>Start a IrNET server accepting any incoming connection:<br />
 <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pppd /dev/irnet 9600 local noauth nolock passive</code> </p>
<p> Start a IrNET client connecting to any IrDA peer:</p>
<p> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pppd /dev/irnet 9600 local noauth nolock</code> </p>
<p> Start a IrNET client connecting to the IrDA peer called<br />
 <i>MyIrDANode</i>:<br />
 <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pppd /dev/irnet 9600 local noauth nolock connect echo name MyIrDANode</code> </p>
<p> Start a IrNET server accepting incoming connection from peer with IrDA address 0x12345678 only on IrDA port 0x87654321:</p>
<p> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>pppd /dev/irnet 9600 local noauth nolock passive connect echo daddr 0x12345678 , saddr 0x87654321</code></p>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>Files</h2>
<p><i>/dev/irnet</i><br />
 <i>/proc/net/irda/irnet</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-irda/">irda</a></code>(7), <code><a href="/docs/linux/man/8-irnetd/">irnetd</a></code>(8), <code><a href="/docs/linux/man/8-pppd/">pppd</a></code>(8), <code><a href="/docs/linux/man/8-irattach/">irattach</a></code>(8), <code><a href="/docs/linux/man/8-irdadump/">irdadump</a></code>(8). </p>
