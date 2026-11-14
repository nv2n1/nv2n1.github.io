---
title: "packet-link-macaddr(3)"
name: "packet-link-macaddr"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-link-macaddr/"
description: "packet.link.macaddr – MacAddr module"
---

<p>packet.link.macaddr &#8211; MacAddr module</p>
<h2>Description</h2>
<p>Create an object to represent a MAC address. A MAC address is given either by a series of hexadecimal numbers or using the &quot;:&quot; notation. It provides a mechanism for comparing this object with a regular string.</p>
<h2>Classes</h2>
<h3>class MacAddr(__builtin__.str)</h3>
<pre>MacAddr address object
Usage:
 from packet.link.macaddr import MacAddr
 mac = MacAddr('E4CE8F589FF4')
The following expressions are equivalent:
 mac == 'E4CE8F589FF4'
 mac == 'e4ce8f589ff4'
 mac == 'e4:ce:8f:58:9f:f4'
<code>Methods defined here:</code>
---------------------
<code>__eq__(self, other)</code>
Compare two MAC addresses and return True if both are equal.
<code>__ne__(self, other)</code>
Compare two MAC addresses and return False if both are equal.
<code>Static methods defined here:</code>
----------------------------
<code>__new__(cls, mac)</code>
Create new instance by converting input string into a persistent
representation of a MAC address.</pre>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
