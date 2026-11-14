---
title: "easside-ng(8)"
name: "easside-ng"
section: "8"
letter: "e"
url: "/docs/linux/man/8-easside-ng/"
description: "easside-ng – an auto-magic tool which allows you to communicate via an WEP-encrypted AP without knowing the key"
---

<p>easside-ng &#8211; an auto-magic tool which allows you to communicate via an WEP-encrypted AP without knowing the key</p>
<h2>Synopsis</h2>
<p><code>easside-ng</code> &lt;options&gt;</p>
<h2>Description</h2>
<p><code>easside-ng</code> is an auto-magic tool which allows you to communicate via an WEP-encrypted access point (AP) without knowing the WEP key. It first identifies a network, then proceeds to associate with it, obtain PRGA (pseudo random generation algorithm) xor data, determine the network IP scheme and then setup a TAP interface so that you can communicate with the AP without requiring the WEP key. All this is done without your intervention.</p>
<h2>Options</h2>
<dl>
<dt><i>-h</i></p>
<dd>Shows the help screen.</p>
<dt><i>-v &lt;victim mac&gt;</i></p>
<dd>Victim BSSID (Optional).</p>
<dt><i>-m &lt;src mac&gt;</i></p>
<dd>Source MAC address to be used (Optional).</p>
<dt><i>-i &lt;ip&gt;</i></p>
<dd>Source IP address to be used on the wireless LAN. Defaults to the decoded network plus &#8216;.123&#8217; (Optional).</p>
<dt><i>-r &lt;router ip&gt;</i></p>
<dd>IP address of the AP router. This could be the WAN IP of the AP or an actual router IP depending on the topology. Defaults to the decoded network plus &#8216;.1&#8217; (Optional).</p>
<dt><i>-s &lt;buddy ip&gt;</i></p>
<dd>IP address of Buddy-ng server (Mandatory)</p>
<dt><i>-f &lt;iface&gt;</i></p>
<dd>Wireless interface to use (Mandatory)</p>
<dt><i>-c &lt;channel&gt;</i></p>
<dd>Lock interface to this channel (Optional).</p>
<dt><i>-n</i></p>
<dd>Determine Internet IP only.</dl>
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
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
