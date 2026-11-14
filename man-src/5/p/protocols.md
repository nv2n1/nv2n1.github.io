---
title: "protocols(5)"
name: "protocols"
section: "5"
letter: "p"
url: "/docs/linux/man/5-protocols/"
description: "protocols – protocols definition file"
---

<p>protocols &#8211; protocols definition file</p>
<h2>Description</h2>
<p>This file is a plain ASCII file, describing the various DARPA internet protocols that are available from the TCP/IP subsystem. It should be consulted instead of using the numbers in the ARPA include files, or, even worse, just guessing them. These numbers will occur in the protocol field of any IP header. </p>
<p> Keep this file untouched since changes would result in incorrect IP packages. Protocol numbers and names are specified by the IANA (Internet Assigned Numbers Authority). </p>
<p> Each line is of the following format: </p>
<dl>
<dd><i>protocol number aliases &#8230;</i></dl>
<p> where the fields are delimited by spaces or tabs. Empty lines are ignored. If a line contains a hash mark (#), the hash mark and the part of the line following it are ignored. </p>
<p> The field descriptions are:</p>
<dl>
<dt><i>protocol</i></p>
<dd>the native name for the protocol. For example <i>ip</i>, <i>tcp</i>, or <i>udp</i>.</p>
<dt><i>number</i></p>
<dd>the official number for this protocol as it will appear within the IP header.</p>
<dt><i>aliases</i></p>
<dd>optional aliases for the protocol.</dl>
<p> This file might be distributed over a network using a network-wide naming service like Yellow Pages/NIS or BIND/Hesiod.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/protocols</i></p>
<dd>The protocols definition file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getprotoent/">getprotoent</a></code>(3) </p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
