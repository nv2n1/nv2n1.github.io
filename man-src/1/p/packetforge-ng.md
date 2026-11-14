---
title: "packetforge-ng(1)"
name: "packetforge-ng"
section: "1"
letter: "p"
url: "/docs/linux/man/1-packetforge-ng/"
description: "packetforge-ng – forge packets: ARP, UDP, ICMP or custom packets."
---

<h2 class="name">NAME</h2>
<p> packetforge-ng &#8211; forge packets: ARP, UDP, ICMP or custom packets. </p>
<h2>SYNOPSIS</h2>
<p> <code>packetforge-ng</code> &lt;mode&gt; &lt;options&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>packetforge-ng</code> is a tool to create encrypted packets that can subsequently be used for injection. You may create various types of packets such as arp requests, UDP, ICMP and custom packets. The most common use is to create ARP requests for subsequent injection.<br />
 To create an encrypted packet, you must have a PRGA (pseudo random genration algorithm) file. This is used to encrypt the packet you create. This is typically obtained from aireplay-ng chopchop or fragmentation attacks.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><i>-p &lt;fctrl&gt;</i></p>
<dd> Set frame control word (hex)</p>
<dt><i>-a &lt;bssid&gt;</i></p>
<dd> Set Access Point MAC addres</p>
<dt><i>-c &lt;dmac&gt;</i></p>
<dd> Set Destination MAC address</p>
<dt><i>-h &lt;smac&gt;</i></p>
<dd> Set Source MAC address</p>
<dt><i>-j</i></p>
<dd> set FromDS bit</p>
<dt><i>-o</i></p>
<dd> clear ToDS bit</p>
<dt><i>-e</i></p>
<dd> disable WEP encryption</p>
<dt><i>-k &lt;ip:[port]&gt;</i></p>
<dd> Set destination IP (and port)</p>
<dt><i>-l &lt;ip:[port]&gt;</i></p>
<dd> Set source IP (and port)</p>
<dt><i>-w &lt;file&gt;</i></p>
<dd> Write packet to this pcap file</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd> Read packet from this pcap file</p>
<dt><i>-y &lt;file&gt;</i></p>
<dd> Read PRGA from this file</p>
<dt><i>-t &lt;ttl&gt;</i></p>
<dd> Set Time To Live in IP-Header</p>
<dt><i>-s &lt;size&gt;</i></p>
<dd> Set size of the generated null packet.</p>
<dt><i>-0, &#8211;arp</i></p>
<dd> Forge an ARP packet</p>
<dt><i>-1, &#8211;udp</i></p>
<dd> Forge an UDP packet</p>
<dt><i>-2, &#8211;icmp</i></p>
<dd> Forge an ICMP packet</p>
<dt><i>-3, &#8211;null</i></p>
<dd> Forge a llc null packet</p>
<dt><i>-9, &#8211;custom</i></p>
<dd> Build a custom packet, requires -r to read an unencrypted frame out of a pcap file.</dl>
<h2>EXAMPLE</h2>
<p> <code>packetforge-ng</code> -y test.xor -a 00:09:5b:12:40:cc -h 00:10:2a:cb:30:14 -k 192.168.1.100 -l 192.168.1.1 -w arp-request.cap</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airtun-ng/">airtun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-besside-ng/">besside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-easside-ng/">easside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-tkiptun-ng/">tkiptun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-wesside-ng/">wesside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
<h2>Index</h2>
