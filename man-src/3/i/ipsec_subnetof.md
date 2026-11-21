---

title: "ipsec_subnetof(3)"
name: "ipsec_subnetof"
section: "3"
letter: "i"
url: "/docs/linux/man/3-ipsec_subnetof/"
description: "ipsec_subnetof, ipsec_hostof, ipsec_broadcastof – given Internet address and subnet mask return subnet number, host part, broadcast address"
---

<h2>NAME</h2>
<p> ipsec_subnetof, ipsec_hostof, ipsec_broadcastof &#8211; given Internet address and subnet mask return subnet number, host part, broadcast address</p>
<p> <code>#include &lt;libreswan.h&gt;</code> </p>
<p> <code>struct in_addr subnetof(struct in_addr addr,</code><br />
 &nbsp;<wbr> <code>struct in_addr mask);</code><br />
 <code>struct in_addr hostof(struct in_addr addr,</code><br />
 &nbsp;<wbr> <code>struct in_addr mask);</code><br />
 <code>struct in_addr broadcastof(struct in_addr addr,</code><br />
 &nbsp;<wbr> <code>struct in_addr mask);</code></p>
<p> These functions are obsolete; see <i>ipsec_networkof</i>(3) for their replacements. </p>
<p> <i>Subnetof</i> takes an Internet <i>address</i> and a subnet <i>mask</i> and returns the network part of the address (all in network byte order). <i>Hostof</i> similarly returns the host part, and <i>broadcastof</i> returns the broadcast address (all-1s convention) for the network. </p>
<p> These functions are provided to hide the Internet bit-munging inside an API, in hopes of easing the eventual transition to IPv6.</p>
<h2>SEE ALSO</h2>
<p> inet(3), ipsec_atosubnet(3)</p>
<h2>HISTORY</h2>
<p> Written for the FreeS/WAN project by Henry Spencer.</p>
<h2>BUGS</h2>
<p> Calling functions for this is more costly than doing it yourself. </p>
