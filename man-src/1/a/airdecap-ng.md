---
title: "airdecap-ng(1)"
name: "airdecap-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airdecap-ng/"
description: "airdecap-ng – decrypt a WEP/WPA crypted pcap file"
---

<h2 class="name">NAME</h2>
<p> airdecap-ng &#8211; decrypt a WEP/WPA crypted pcap file </p>
<h2>SYNOPSIS</h2>
<p> <code>airdecap-ng</code> [options] &lt;pcap file&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>airdecap-ng</code> decrypts a WEP/WPA crypted pcap file to a uncrypted one by using the right WEP/WPA keys.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><i>-l</i></p>
<dd> Do not remove the 802.11 header.</p>
<dt><i>-b &lt;bssid&gt;</i></p>
<dd> Access point MAC address filter.</p>
<dt><i>-k &lt;pmk&gt;</i></p>
<dd> WPA Pairwise Master Key in hex.</p>
<dt><i>-e &lt;essid&gt;</i></p>
<dd> Target network SSID. For SSID containing special characters, see <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names">http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names</a></p>
<dt><i>-p &lt;pass&gt;</i></p>
<dd> Target network WPA passphrase.</p>
<dt><i>-w &lt;key&gt;</i></p>
<dd> Target network WEP key in hex.</dl>
<h2>EXAMPLES</h2>
<p> airdecap-ng -b 00:09:5B:10:BC:5A open-network.cap<br />
 airdecap-ng -w 11A3E229084349BC25D97E2939 wep.cap<br />
 airdecap-ng -e my_essid -p my_passphrase tkip.cap </p>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
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
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
<h2>Index</h2>
