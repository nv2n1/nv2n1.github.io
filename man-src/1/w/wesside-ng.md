---
title: "wesside-ng(1)"
name: "wesside-ng"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wesside-ng/"
description: "wesside-ng – crack a WEP key of an open network without user intervention"
---

<h2 class="name">NAME</h2>
<p> wesside-ng &#8211; crack a WEP key of an open network without user intervention </p>
<h2>SYNOPSIS</h2>
<p> <code>wesside-ng</code> &lt;options&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>wesside-ng</code> is an auto-magic tool which incorporates a number of techniques to seamlessly obtain a WEP key in minutes. It first identifies a network, then proceeds to associate with it, obtain PRGA (pseudo random generation algorithm) xor data, determine the network IP scheme, reinject ARP requests and finally determine the WEP key. All this is done without your intervention.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h</i></p>
<dd> Shows the help screen.</p>
<dt><i>-i &lt;iface&gt;</i></p>
<dd> Wireless interface name. (Mandatory)</p>
<dt><i>-n &lt;network ip&gt;</i></p>
<dd> Network IP as in &#8216;who has destination IP (netip) tell source IP (myip)&#8217;. Defaults to the source IP on the ARP request which is captured and decrypted. (Optional)</p>
<dt><i>-m &lt;my ip&gt;</i></p>
<dd> &#8216;who has destination IP (netip) tell source IP (myip)&#8217;. Defaults to the network.123 on the ARP request captured (Optional).</p>
<dt><i>-a &lt;source mac&gt;</i></p>
<dd> Source MAC address (Optional)</p>
<dt><i>-c</i></p>
<dd> Do not crack the key. Simply capture the packets until control-C is hit to stop the program! (Optional)</p>
<dt><i>-p &lt;min PRGA&gt;</i></p>
<dd> Determines the minimum number of bytes of PRGA which is gathered. Defaults to 128 bytes. (Optional).</p>
<dt><i>-v &lt;victim MAC&gt;</i></p>
<dd> Wireless access point MAC address (Optional).</p>
<dt><i>-t &lt;threshold&gt;</i></p>
<dd> For each number of IVs specified, restart the airecrack-ng PTW engine (Optional). It will restart PTW every &lt;threshold&gt; IVs.</p>
<dt><i>-f &lt;channel&gt;</i></p>
<dd> Allows the highest channel for scanning to be defined. Defaults to channel 11 (Optional).</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airodump-ng/">airodump-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airserv-ng/">airserv-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airtun-ng/">airtun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code> </p>
<h2>Index</h2>
