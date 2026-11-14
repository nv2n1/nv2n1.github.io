---
title: "ipsec__updown(8)"
name: "ipsec__updown"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec__updown/"
description: "ipsec__updown – kernel and routing manipulation script"
---

<p>ipsec__updown &#8211; kernel and routing manipulation script</p>
<h2>Synopsis</h2>
<p><i>_updown</i> is invoked by pluto when it has brought up a new connection. This script is used to insert the appropriate routing entries for IPsec operation on some kernel IPsec stacks, such as KLIPS and MAST, and may do other necessary work that is kernel or user specific, such as defining custom firewall rules. The interface to the script is documented in the pluto man page.</p>
<h2>Variables</h2>
<p>The <i>_updown</i> is passed along a number of variables which can be used to act differently based on the information: </p>
<p> <code>PLUTO_VERSION</code></p>
<dl>
<dd>indicates what version of this interface is being used. This document describes version 1.1. This is upwardly compatible with version 1.0.</dl>
<p> <code>PLUTO_VERB</code></p>
<dl>
<dd>specifies the name of the operation to be performed, which can be one of <code>prepare-host</code>, <code>prepare-client</code>, <code>up-host</code>, <code>up-client</code>, <code>down-host</code> or <code>down-client</code>. If the address family for security gateway to security gateway communications is IPv6, then a suffix of -v6 is added to this verb.</dl>
<p> <code>PLUTO_CONNECTION</code></p>
<dl>
<dd>is the name of the connection for which we are routing.</dl>
<p> <code>PLUTO_NEXT_HOP</code></p>
<dl>
<dd>is the next hop to which packets bound for the peer must be sent.</dl>
<p> <code>PLUTO_INTERFACE</code></p>
<dl>
<dd>is the name of the ipsec interface to be used.</dl>
<p> <code>PLUTO_ME</code></p>
<dl>
<dd>is the IP address of our host.</dl>
<p> <code>PLUTO_MY_CLIENT</code></p>
<dl>
<dd>is the IP address / count of our client subnet. If the client is just the host, this will be the host&#8217;s own IP address / max (where max is 32 for IPv4 and 128 for IPv6).</dl>
<p> <code>PLUTO_MY_CLIENT_NET</code></p>
<dl>
<dd>is the IP address of our client net. If the client is just the host, this will be the host&#8217;s own IP address.</dl>
<p> <code>PLUTO_MY_CLIENT_MASK</code></p>
<dl>
<dd>is the mask for our client net. If the client is just the host, this will be 255.255.255.255.</dl>
<p> <code>PLUTO_PEER</code></p>
<dl>
<dd>is the IP address of our peer.</dl>
<p> <code>PLUTO_PEER_CLIENT</code></p>
<dl>
<dd>is the IP address / count of the peer&#8217;s client subnet. If the client is just the peer, this will be the peer&#8217;s own IP address / max (where max is 32 for IPv4 and 128 for IPv6).</dl>
<p> <code>PLUTO_PEER_CLIENT_NET</code></p>
<dl>
<dd>is the IP address of the peer&#8217;s client net. If the client is just the peer, this will be the peer&#8217;s own IP address.</dl>
<p> <code>PLUTO_PEER_CLIENT_MASK</code></p>
<dl>
<dd>is the mask for the peer&#8217;s client net. If the client is just the peer, this will be 255.255.255.255.</dl>
<p> <code>PLUTO_MY_PROTOCOL</code></p>
<dl>
<dd>lists the protocols allowed over this IPsec SA.</dl>
<p> <code>PLUTO_PEER_PROTOCOL</code></p>
<dl>
<dd>lists the protocols the peer allows over this IPsec SA.</dl>
<p> <code>PLUTO_MY_PORT</code></p>
<dl>
<dd>lists the ports allowed over this IPsec SA.</dl>
<p> <code>PLUTO_PEER_PORT</code></p>
<dl>
<dd>lists the ports the peer allows over this IPsec SA.</dl>
<p> <code>PLUTO_MY_ID</code></p>
<dl>
<dd>lists our id.</dl>
<p> <code>PLUTO_PEER_ID</code></p>
<dl>
<dd>lists our peer&#8217;s id.</dl>
<p> <code>PLUTO_PEER_CA</code></p>
<dl>
<dd>lists the peer&#8217;s CA.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8).</p>
<h2>History</h2>
<p>Man page written for the Linux FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org/">http://www.freeswan.org/</a></code>m[]&gt; by Michael Richardson. Original program written by Henry Spencer.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
