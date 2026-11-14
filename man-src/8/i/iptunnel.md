---
title: "iptunnel(8)"
name: "iptunnel"
section: "8"
letter: "i"
url: "/docs/linux/man/8-iptunnel/"
description: "iptunnel – Create and manage IP tunnels"
---

<p>iptunnel &#8211; Create and manage IP tunnels</p>
<h2>Synopsis</h2>
<p><code>iptunnel</code> { add | change | del | show } [ NAME ]<br />
&nbsp;<wbr>&nbsp;[&nbsp;mode&nbsp;{&nbsp;ipip | gre | sit&nbsp;}&nbsp;]&nbsp;[&nbsp;remote ADDR&nbsp;]&nbsp;[&nbsp;local ADDR&nbsp;]<br />
&nbsp;<wbr>&nbsp;[&nbsp;[i|o]seq&nbsp;]&nbsp;[&nbsp;[i|o]key KEY&nbsp;]&nbsp;[&nbsp;[i|o]csum&nbsp;]<br />
&nbsp;<wbr>&nbsp;[&nbsp;ttl TTL&nbsp;]&nbsp;[&nbsp;tos TOS&nbsp;]&nbsp;[&nbsp;nopmtudisc&nbsp;]&nbsp;[&nbsp;dev PHYS_DEV&nbsp;] <code>iptunnel</code> -V | &#8211;version </p>
<pre><code>Where: NAME := STRING
ADDR := { IP_ADDRESS | any }
TOS  := { NUMBER | inherit }
TTL  := { 1..255 | inherit }
KEY  := { DOTTED_QUAD | NUMBER }
</code></pre>
<h2>Description</h2>
<p><code>iptunnel</code> can be used to add, change, delete and show IP tunnels on the machine. </p>
<h2>Options</h2>
<dl>
<dt><code>help</code></p>
<dd>Show the help text. </p>
<dt><code>show</code></p>
<dd>List existing IP tunnels. </p>
<dt><code>{ add | change | del } [ NAME ]</code></p>
<dd>Specify an action (<code>add</code>, <code>change</code> or <code>delete</code> an IP tunnel) to be executed by <code>iptunnel</code> on the tunnel named <code>NAME</code>, which must be a string. You must specify one action. </p>
<dt><code>mode PROTOCOL</code></p>
<dd>Specify the <code>PROTOCOL</code> to be used for the IP tunnel. It can be <code>ipip</code> for TCP/IP, <code>gre</code> for Cisco GRE tunnel (RFCs 1701 and 1702), or <code>sit</code> for IPv6-in-IPv4 tunneling. </p>
<dt><code>remote ADDR</code></p>
<dd>Set the remote (i.e., destination) address of the tunnel. <code>ADDR</code> must be an IP address or the word <code>any</code>. </p>
<dt><code>local ADDR</code></p>
<dd>Set the local (i.e., source) address of the tunnel. <code>ADDR</code> must be an IP address or the word <code>any</code>. </p>
<dt><code>iseq</code></p>
<dd>Require that all incoming packets are serialized. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>oseq</code></p>
<dd>Enable serialization (sequencing) for all outgoing packets. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>ikey KEY</code></p>
<dd>Specify the input key for the Cisco GRE tunnel. <code>KEY</code> must be either in dotted quad (dotted decimal) or a number. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>okey KEY</code></p>
<dd>Same as <code>ikey</code>, but set the output key instead. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>icsum</code></p>
<dd>Require that all incoming packets have the correct checksum. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>ocsum</code></p>
<dd>Calculate checksums for all outgoing packets. Only applicable for <code>GRE</code> tunnels. </p>
<dt><code>ttl TTL</code></p>
<dd>Specify the <code>Time-To-Live</code> value for the IP tunnel. <code>TTL</code> must be a value between <code>1</code> and <code>255</code>, or the word <code>inherit</code>, which causes the field to be copied from the original IP header. </p>
<dt><code>tos TOS</code></p>
<dd>Specify the <code>Type-Of-Service</code> value for the IP tunnel. <code>TOS</code> must be a value between <code>1</code> and <code>255</code>, or the word <code>inherit</code>, which causes the field to be copied from the original IP header. </p>
<dt><code>nopmtudisc</code></p>
<dd>Disable <code>Path MTU Discovery</code> on this tunnel. Note that a fixed <code>ttl</code> is incompatible with this option. </p>
<dt><code>dev PHYS_DEV</code></p>
<dd>Bind the tunnel to the device <code>PHYS_DEV</code>. </p>
</dl>
<h2>Homepage</h2>
<p><code>&lt;<a rel="nofollow" href="https://sourceforge.net/projects/net-tools/">https://sourceforge.net/projects/net-tools/</a>&gt;</code></p>
<h2>Authors</h2>
<p>This manpage was written by Sergio Durigan Junior &lt;sergiodj (at) sergiodj (dot) net&gt;. A few parts were inspired by <code><a href="/docs/linux/man/1-ip-tunnel/">ip-tunnel</a>(1)</code>&#8216;s manpage. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation.</p>
