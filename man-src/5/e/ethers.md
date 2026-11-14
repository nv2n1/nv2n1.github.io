---
title: "ethers(5)"
name: "ethers"
section: "5"
letter: "e"
url: "/docs/linux/man/5-ethers/"
---

<h2>NAME ethers &#8211; Ethernet address to IP number database</h2>
<h2>DESCRIPTION <code>/etc/ethers</code> contains 48 bit Ethernet addresses and their corresponding</h2>
<p>IP numbers, one line for each IP number: </p>
<dl>
<dd><i>Ethernet-address</i> <i>IP-number</i></dl>
<p> The two items are separated by any number of SPACE and/or TAB characters. A <code>#</code> at the beginning of a line starts a comment which extends to the end of the line. The <i>Ethernet-address</i> is written as <i>x</i>:<i>x</i>:<i>x</i>:<i>x</i>:<i>x</i>:<i>x</i>, where <i>x</i> is a hexadecimal number between <code>0</code> and <code>ff</code> which represents one byte of the address, which is in network byte order (big-endian). The <i>IP-number</i> may be a hostname which can be resolved by DNS or a dot separated number.</p>
<h2>EXAMPLES 08:00:20:00:61:CA pal</h2>
<h2>FILES /etc/ethers</h2>
<h2>SEE ALSO <a href="/docs/linux/man/8-rarp/">rarp</a>(8)</h2>
