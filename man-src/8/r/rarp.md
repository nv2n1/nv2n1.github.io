---
title: "rarp(8)"
name: "rarp"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rarp/"
description: "rarp – manipulate the system RARP table"
---

<p>rarp &#8211; manipulate the system RARP table</p>
<h2>Synopsis</h2>
<p><code>rarp [-V] [&#8211;version] [-h] [&#8211;help]</code><br />
 <code>rarp -a</code><br />
 <code>rarp [-v] -d hostname &#8230;</code><br />
 <code>rarp [-v] [-t type] -s hostname hw_addr</code></p>
<h2>Note</h2>
<p>This program is obsolete. From version 2.3, the Linux kernel no longer contains RARP support. For a replacement RARP daemon, see <i><a href="ftp://ftp.dementia.org/pub/net-tools">ftp://ftp.dementia.org/pub/net-tools</a></i></p>
<h2>Description</h2>
<p><code>Rarp</code> manipulates the kernel&#8217;s RARP table in various ways. The primary options are clearing an address mapping entry and manually setting up one. For debugging purposes, the <code>rarp</code> program also allows a complete dump of the RARP table.</p>
<h2>Options</h2>
<dl>
<dt><code>-V</code></p>
<dd>Display the version of RARP in use.</p>
<dt><code>-v</code></p>
<dd>Tell the user what is going on by being verbose.</p>
<dt><code>-t type</code></p>
<dd>When setting or reading the RARP table, this optional parameter tells <code>rarp</code> which class of entries it should check for. The default value of this parameter is <code>ether</code> (i.e. hardware code <code>0x01</code> for <code>IEEE 802.3 10Mbps Ethernet.</code> Other values might include network technologies such as <code>AX.25 (ax25)</code> and <code>NET/ROM (netrom).</code></p>
<dt><code>-a</code></p>
<dd>
<dt><code>&#8211;list</code></p>
<dd>Lists the entries in the RARP table.</p>
<dt><code>-d hostname</code></p>
<dd>
<dt><code>&#8211;delete hostname</code></p>
<dd>Remove all RARP entries for the specified host.</p>
<dt><code>-s hostname hw_addr</code></p>
<dd>
<dt><code>&#8211;set hostname hw_addr</code></p>
<dd>Create a RARP address mapping entry for host <code>hostname</code> with hardware address set to <code>hw_addr</code>. The format of the hardware address is dependent on the hardware class, but for most classes one can assume that the usual presentation can be used. For the Ethernet class, this is 6 bytes in hexadecimal, separated by colons.</dl>
<h2>Warning</h2>
<p>Some systems (notably older Suns) assume that the host replying to a RARP query can also provide other remote boot services. Therefore never gratuitously add rarp entries unless you wish to meet the wrath of the network administrator.</p>
<h2>Files</h2>
<p><i>/proc/net/rarp,</i></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-arp/">arp</a>(8), <a href="/docs/linux/man/8-route/">route</a>(8), <a href="/docs/linux/man/8-ifconfig/">ifconfig</a>(8), <a href="/docs/linux/man/8-netstat/">netstat</a>(8)</p>
<h2>Authors</h2>
<p>Ross D. Martin, &lt;martin [at] trcsun3.eas.asu.edu&gt;<br />
 Fred N. van Kempen, &lt;waltje [at] uwalt.nl.mugnet.org&gt;<br />
 Phil Blundell, &lt;Philip.Blundell [at] pobox.com&gt;</p>
