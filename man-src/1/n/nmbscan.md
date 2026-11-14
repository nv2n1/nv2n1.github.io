---
title: "nmbscan(1)"
name: "nmbscan"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nmbscan/"
description: "nmbscan – NMB/SMB network scanner"
---

<h2>NAME</h2>
<p> nmbscan &#8211; NMB/SMB network scanner</p>
<h2>SYNOPSIS</h2>
<p> <code>nmbscan</code> -L<br />
 <code>nmbscan</code> {-d|-m|-a}<br />
 <code>nmbscan</code> {-h|-n} host1 [host2 [&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>nmbscan</code> command. </p>
<p> <code>nmbscan</code> scans the shares of a SMB/NetBIOS network, using the NMB/SMB/NetBIOS protocols. It is useful for acquiring information on a local area network for such purposes as security auditing. </p>
<p> It can obtain such information as NMB/SMB/NetBIOS/Windows host name, IP address, IP host name, Ethernet MAC address, Windows user name, NMB/SMB/NetBIOS/Windows domain name, and master browser. </p>
<p> It can discover all the NMB/SMB/NetBIOS/Windows hosts on a local area network by using the hosts lists maintained by master browsers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd>
 Show summary of options.</p>
<dt><code>-L</code></p>
<dd> Show license agreement (GPL).</p>
<dt><code>-d</code></p>
<dd> Show all domains.</p>
<dt><code>-m</code></p>
<dd> Show all domains with master browsers.</p>
<dt><code>-a</code></p>
<dd> Show all domains, master browsers, and servers.</p>
<dt><code>-h</code></p>
<dd> Show information on hosts, known by ip name/address.</p>
<dt><code>-n</code></p>
<dd> Show information on hosts, known by nmb name.</dl>
<h2>AUTHOR</h2>
<p> nmbscan was written by Grégoire Barbier. </p>
<h2>Index</h2>
