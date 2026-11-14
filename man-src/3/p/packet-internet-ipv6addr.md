---
title: "packet-internet-ipv6addr(3)"
name: "packet-internet-ipv6addr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-internet-ipv6addr/"
description: "packet.internet.ipv6addr – IPv6Addr module"
---

<p>packet.internet.ipv6addr &#8211; IPv6Addr module</p>
<h2>Description</h2>
<p>Create an object to represent an IPv6 address. An IPv6 address is given either by a series of hexadecimal numbers or using the &quot;:&quot; notation. It provides a mechanism for comparing this object with a regular string. It also takes care of &#8216;::&#8217; notation and leading zeroes.</p>
<h2>Classes</h2>
<h3>class IPv6Addr(__builtin__.str)</h3>
<pre>IPv6Addr address object
Usage:
 from packet.internet.ipv6addr import IPv6Addr
 ip = IPv6Addr('fe80000000000000020c29fffe5409ef')
The following expressions are equivalent:
 ip == 0xFE80000000000000020C29FFFE5409EF
 ip == 0xfe80000000000000020c29fffe5409ef
 ip == '0xFE80000000000000020C29FFFE5409EF'
 ip == '0xfe80000000000000020c29fffe5409ef'
 ip == 'FE80000000000000020C29FFFE5409EF'
 ip == 'fe80000000000000020c29fffe5409ef'
 ip == 'FE80:0000:0000:0000:020C:29FF:FE54:09EF'
 ip == 'fe80:0000:0000:0000:020c:29ff:fe54:09ef'
 ip == 'FE80::020C:29FF:FE54:09EF'
 ip == 'fe80::020c:29ff:fe54:09ef'
 ip == 'FE80::20C:29FF:FE54:9EF'
 ip == 'fe80::20c:29ff:fe54:9ef'
<code>Methods defined here:</code>
---------------------
<code>__eq__(self, other)</code>
Compare two IPv6 addresses and return True if both are equal.
<code>__ne__(self, other)</code>
Compare two IPv6 addresses and return False if both are equal.
<code>Static methods defined here:</code>
----------------------------
<code>__new__(cls, ip)</code>
Create new instance by converting input int/string into a persistent
representation of an IPv6 address.</pre>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
