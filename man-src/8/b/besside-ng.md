---
title: "besside-ng(8)"
name: "besside-ng"
section: "8"
letter: "b"
url: "/docs/linux/man/8-besside-ng/"
description: "besside-ng – crack a WEP or WPA key without user intervention and collaborate with WPA cracking statistics"
---

<p>besside-ng &#8211; crack a WEP or WPA key without user intervention and collaborate with WPA cracking statistics</p>
<h2>Synopsis</h2>
<p><code>besside-ng</code> [options] &lt;interface&gt; </p>
<h2>Description</h2>
<p><code>besside-ng</code> is a tool wich will crack all the WEP networks in range and log all the WPA handshakes. WPA handshakes can be uploaded to the online cracking service at wpa.darkircop.org. Wpa.darkircop.com also provides useful statistics based on user-submitted capture files about the feaseability of WPA cracking.</p>
<dl>
<dt><i>-b &lt;target mac&gt;</i></p>
<dd>Specifies the target&#8217;s BSSID</p>
<dt><i>-s &lt;WPA server&gt;</i></p>
<dd>Where to upload capture file for cracking. A good choice is wpa.darkircop.org</p>
<dt><i>-c &lt;chan&gt;</i></p>
<dd>Channel lock</p>
<dt><i>-p &lt;pps&gt;</i></p>
<dd>Packages per second to send (flood rate).</p>
<dt><i>-W</i></p>
<dd>Crack only WPA networks</p>
<dt><i>-v</i></p>
<dd>Verbos mode. Use -vv for more verbose, -vv for even more and so on.</p>
<dt><i>-h</i></p>
<dd>Help screen </p>
<h2>Author</h2>
<p>This manual page was written by David Francos Cuartero. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airtun-ng/">airtun-ng</a>(8)</code><br />
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
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
