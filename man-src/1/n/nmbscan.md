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
<dt><code>&#8211;help</code></dt>
<dd>
 Show summary of options.</dd>
<dt><code>-L</code></dt>
<dd> Show license agreement (GPL).</dd>
<dt><code>-d</code></dt>
<dd> Show all domains.</dd>
<dt><code>-m</code></dt>
<dd> Show all domains with master browsers.</dd>
<dt><code>-a</code></dt>
<dd> Show all domains, master browsers, and servers.</dd>
<dt><code>-h</code></dt>
<dd> Show information on hosts, known by ip name/address.</dd>
<dt><code>-n</code></dt>
<dd> Show information on hosts, known by nmb name.</dd></dl>
<h2>AUTHOR</h2>
<p> nmbscan was written by Grégoire Barbier. </p>
