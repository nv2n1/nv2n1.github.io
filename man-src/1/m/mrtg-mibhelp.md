---
title: "mrtg-mibhelp(1)"
name: "mrtg-mibhelp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mrtg-mibhelp/"
description: "mrtg-mibhelp – A Table of some interesting OIDs"
---

<h2 class="name">NAME</h2>
<p> mrtg-mibhelp &#8211; A Table of some interesting OIDs </p>
<h2>OVERVIEW</h2>
<p> This File Contains a collection of interesting <font SIZE="-1">MIB</font> Entries &#8230; mrtg knows about their names &#8230; depending on the <font SIZE="-1">ASN</font>.1 Syntax you may have to put <code>gauge</code> into the <code>Options[]:</code> parameter. </p>
<p> For information about how to create a <code>Target[]:</code> parameter which references these <font SIZE="-1">MIB</font> entries, please consult mrtg-reference.</p>
<h2>MIB LIST</h2>
<h3>ifOperStatus</h3>
<pre>
 Descriptor:            ifOperStatus
 Identifier:            1.3.6.1.2.1.2.2.1.8
 ASN.1 Syntax:          INTEGER
 Enumeration:           up 1, down 2, testing 3
</pre>
<p> The current operational state of the interface. The <i><a href="/docs/linux/man/3-testing/">testing</a></i>(3) state indicates that no operational packets can be passed.</p>
<h3>ifAdminStatus</h3>
<pre>
 Descriptor:            ifAdminStatus
 Identifier:            1.3.6.1.2.1.2.2.1.7
 ASN.1 Syntax:          INTEGER
 Enumeration:           up 1, down 2, testing 3
</pre>
<p> The current administrative state of the interface. The <i><a href="/docs/linux/man/3-testing/">testing</a></i>(3) state indicates that no operational packets can be passed.</p>
<h3>ifInOctets</h3>
<pre>
 Descriptor:            ifInOctets
 Identifier:            1.3.6.1.2.1.2.2.1.10
 ASN.1 Syntax:          Counter32
</pre>
<p> The total number of octets received on the interface, including framing characters.</p>
<h3>ifInUcastPkts</h3>
<pre>
 Descriptor:            ifInUcastPkts
 Identifier:            1.3.6.1.2.1.2.2.1.11
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of subnetwork-unicast packets delivered to a higher-layer protocol.</p>
<h3>ifInNUcastPkts</h3>
<pre>
 Descriptor:            ifInNUcastPkts
 Identifier:            1.3.6.1.2.1.2.2.1.12
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of non-unicast (i.e., subnetwork- broadcast or subnetwork-multicast) packets delivered to a higher-layer protocol.</p>
<h3>ifInDiscards</h3>
<pre>
 Descriptor:            ifInDiscards
 Identifier:            1.3.6.1.2.1.2.2.1.13
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of inbound packets which were chosen to be discarded even though no errors had been detected to prevent their being deliverable to a higher-layer protocol. One possible reason for discarding such a packet could be to free up buffer space.</p>
<h3>ifInErrors</h3>
<pre>
 Descriptor:            ifInErrors
 Identifier:            1.3.6.1.2.1.2.2.1.14
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of inbound packets that contained errors preventing them from being deliverable to a higher-layer protocol.</p>
<h3>ifInUnknownProtos</h3>
<pre>
 Descriptor:            ifInUnknownProtos
 Identifier:            1.3.6.1.2.1.2.2.1.15
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of packets received via the interface which were discarded because of an unknown or unsupported protocol.</p>
<h3>ifOutOctets</h3>
<pre>
 Descriptor:            ifOutOctets
 Identifier:            1.3.6.1.2.1.2.2.1.16
 ASN.1 Syntax:          Counter32
</pre>
<p> The total number of octets transmitted out of the interface, including framing characters.</p>
<h3>ifOutUcastPkts</h3>
<pre>
 Descriptor:            ifOutUcastPkts
 Identifier:            1.3.6.1.2.1.2.2.1.17
 ASN.1 Syntax:          Counter32
</pre>
<p> The total number of packets that higher-level protocols requested be transmitted to a subnetwork-unicast address, including those that were discarded or not sent.</p>
<h3>ifOutNUcastPkts</h3>
<pre>
 Descriptor:             ifOutNUcastPkts
 Identifier:            1.3.6.1.2.1.2.2.1.18
 ASN.1 Syntax:          Counter32
</pre>
<p> The total number of packets that higher-level protocols requested be transmitted to a non- unicast (i.e., a subnetwork-broadcast or subnetwork-multicast) address, including those that were discarded or not sent.</p>
<h3>ifOutDiscards</h3>
<pre>
 Descriptor:             ifOutDiscards
 Identifier:            1.3.6.1.2.1.2.2.1.19
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of outbound packets which were chosen to be discarded even though no errors had been detected to prevent their being transmitted. One possible reason for discarding such a packet could be to free up buffer space.</p>
<h3>ifOutErrors</h3>
<pre>
 Descriptor:             ifOutErrors
 Identifier:            1.3.6.1.2.1.2.2.1.20
 ASN.1 Syntax:          Counter32
</pre>
<p> The number of outbound packets that could not be transmitted because of errors.</p>
<h3>ifOutQLen</h3>
<pre>
 Descriptor:             ifOutQLen
 Identifier:            1.3.6.1.2.1.2.2.1.21
 ASN.1 Syntax:          Unsigned32
</pre>
<p> The length of the output packet queue (in packets).</p>
<h3>frInOctets</h3>
<p> From: Simon Ferrett &lt;simonf [at] world.net&gt; </p>
<pre>
 'frInOctets' =&gt; '1.3.6.1.2.1.10.32.2.1.9'
 'frOutOctets' =&gt; '1.3.6.1.2.1.10.32.2.1.7'
</pre>
<p> which when used in the form: </p>
<pre>
 frInOctets.pp.dd&amp;frOutOctets.pp.dd:community [at] cisco.router
</pre>
<p> where pp is the physical port that the frame relay pvc is defined on and dd is the <font SIZE="-1">DLCI</font> of the pvc gets you the in and out octets for just that pvc.</p>
<h3>ifAdminHack and ifOperHack</h3>
<p> The return values of ifAdminStatus and ifOperStatus are not very useful for graphing. Use ifOperHack and ifAdminHack instead. They return 1 for <font SIZE="-1">UP</font> and 0 otherwise. </p>
<p> Note these are not real <font SIZE="-1">MIB</font> entities but mrtg hacks</p>
<h3>PseudoZero and PseudoOne</h3>
<p> will return 0 and 1 respectively </p>
<p> Note these are not real <font SIZE="-1">MIB</font> entities but mrtg hacks</p>
<h2>AUTHOR</h2>
<p> Tobias Oetiker &lt;tobi [at] oetiker.ch&gt; </p>
<h2>Index</h2>
