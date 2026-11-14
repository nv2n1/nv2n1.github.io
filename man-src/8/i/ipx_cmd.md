---
title: "ipx_cmd(8)"
name: "ipx_cmd"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipx_cmd/"
description: "ipx_cmd – bridge between Novell’s SCMD driver and local IPX network"
---

<p>ipx_cmd &#8211; bridge between Novell&#8217;s SCMD driver and local IPX network</p>
<h2>Synopsis</h2>
<p><code>ipx_cmd</code> <code>-A</code> <i>server name</i> [ <code>-l</code> <i>local interface name</i> ]</p>
<h2>Description</h2>
<p><code>ipx_cmd</code> moves packets from <i>tap</i><code>N</code> to <i>server</i> and vice versa. It is something like <code>IPX Tunnel</code>, but it uses Novell Netware 5 server <code>Compatibility Mode Driver</code> (AKA <code>Migration Agent</code>) on the other end of wire. You must first configure your kernel <i>tap</i><code>N</code> device with IPX <code>EthernetII</code> frame and with network number set up on server (you can use kernel autodetection).</p>
<h2>Options</h2>
<dl>
<dt><code>-A</code> <i>server name</i></p>
<dd>This is IP name of compatibility mode server. You can use DNS name or dotted quad to specify server address.</p>
<dt><code>-l</code> <i>local interface name</i></p>
<dd>This allows you to specify, which of your IP addresses should be used as IP address of client side of CMD driver. You must configure your <i>tap</i><code>N</code> device with hardware address <code>7E:01:AA:BB:CC:DD</code>, where AA:BB:CC:DD is your IP address in hexa.</dl>
<h2>Example</h2>
<p>If you are on server <i>platan.vc.cvut.cz</i> (<i>147.32.240.81</i>) and your migration agent runs on server <i>boris.vc.cvut.cz</i>, you can configure your system with: </p>
<dl>
<dd>insmod ethertap<br />
 ifconfig tap0 hw ether 7E:01:93:20:F0:51 up<br />
 ipx_interface add -p tap0 EtherII<br />
 ipx_cmd -A boris.vc.cvut.cz -l 147.32.240.81 &amp;</dl>
<h2>Bugs</h2>
<p>This program was written to satisfy my own needs and should be really improved. At least it should configure <i>tap</i> interface itself.</p>
<h2>Author</h2>
<p>Petr Vandrovec &lt;vandrove [at] vc.cvut.cz&gt;</p>
