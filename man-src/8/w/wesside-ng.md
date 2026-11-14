---
title: "wesside-ng(8)"
name: "wesside-ng"
section: "8"
letter: "w"
url: "/docs/linux/man/8-wesside-ng/"
description: "wesside-ng – crack a WEP key of an open network without user intervention"
---

<p>wesside-ng &#8211; crack a WEP key of an open network without user intervention</p>
<h2>Synopsis</h2>
<p><code>wesside-ng</code> &lt;options&gt;</p>
<h2>Description</h2>
<p><code>wesside-ng</code> is an auto-magic tool which incorporates a number of techniques to seamlessly obtain a WEP key in minutes. It first identifies a network, then proceeds to associate with it, obtain PRGA (pseudo random generation algorithm) xor data, determine the network IP scheme, reinject ARP requests and finally determine the WEP key. All this is done without your intervention.</p>
<h2>Options</h2>
<dl>
<dt><i>-h</i></p>
<dd>Shows the help screen.</p>
<dt><i>-i &lt;iface&gt;</i></p>
<dd>Wireless interface name. (Mandatory)</p>
<dt><i>-n &lt;network ip&gt;</i></p>
<dd>Network IP as in &#8216;who has destination IP (netip) tell source IP (myip)&#8217;. Defaults to the source IP on the ARP request which is captured and decrypted. (Optional)</p>
<dt><i>-m &lt;my ip&gt;</i></p>
<dd>\(aqwho has destination IP (netip) tell source IP (myip)\(aq. Defaults to the network.123 on the ARP request captured (Optional).</p>
<dt><i>-a &lt;source mac&gt;</i></p>
<dd>Source MAC address (Optional)</p>
<dt><i>-c</i></p>
<dd>Do not crack the key. Simply capture the packets until control-C is hit to stop the program! (Optional)</p>
<dt><i>-p &lt;min PRGA&gt;</i></p>
<dd>Determines the minimum number of bytes of PRGA which is gathered. Defaults to 128 bytes. (Optional).</p>
<dt><i>-v &lt;victim MAC&gt;</i></p>
<dd>Wireless access point MAC address (Optional).</p>
<dt><i>-t &lt;threshold&gt;</i></p>
<dd>For each number of IVs specified, restart the airecrack-ng PTW engine (Optional). It will restart PTW every &lt;threshold&gt; IVs.</p>
<dt><i>-f &lt;channel&gt;</i></p>
<dd>Allows the highest channel for scanning to be defined. Defaults to channel 11 (Optional).</dl>
<h2>Author</h2>
<p>This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airtun-ng/">airtun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-besside-ng/">besside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-easside-ng/">easside-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-tkiptun-ng/">tkiptun-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
