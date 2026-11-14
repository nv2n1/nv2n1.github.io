---
title: "aireplay-ng(8)"
name: "aireplay-ng"
section: "8"
letter: "a"
url: "/docs/linux/man/8-aireplay-ng/"
description: "aireplay-ng – inject packets into a wireless network to generate traffic"
---

<p>aireplay-ng &#8211; inject packets into a wireless network to generate traffic</p>
<h2>Synopsis</h2>
<p><code>aireplay-ng</code> [options] &lt;replay interface&gt;</p>
<h2>Description</h2>
<p><code>aireplay-ng</code> is used to inject/replay frames. The primary function is to generate traffic for the later use in aircrack-ng for cracking the WEP and WPA-PSK keys. There are different attacks which can cause deauthentications for the purpose of capturing WPA handshake data, fake authentications, Interactive packet replay, hand-crafted ARP request injection and ARP-request reinjection. With the packetforge-ng tool it&#8217;s possible to create arbitrary frames. </p>
<p> <code>aireplay-ng</code> supports single-NIC injection/monitor.<br />
 This feature needs driver patching.</p>
<h2>Options</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd>Shows the help screen.</dl>
<dl>
<dt><code>Filter options:</code></p>
<dd>
<dt><i>-b &lt;bssid&gt;</i></p>
<dd>MAC address of access point.</p>
<dt><i>-d &lt;dmac&gt;</i></p>
<dd>MAC address of destination.</p>
<dt><i>-s &lt;smac&gt;</i></p>
<dd>MAC address of source.</p>
<dt><i>-m &lt;len&gt;</i></p>
<dd>Minimum packet length.</p>
<dt><i>-n &lt;len&gt;</i></p>
<dd>Maximum packet length.</p>
<dt><i>-u &lt;type&gt;</i></p>
<dd>Frame control, type field.</p>
<dt><i>-v &lt;subt&gt;</i></p>
<dd>Frame control, subtype field.</p>
<dt><i>-t &lt;tods&gt;</i></p>
<dd>Frame control, &quot;To&quot; DS bit (0 or 1).</p>
<dt><i>-f &lt;fromds&gt;</i></p>
<dd>Frame control, &quot;From&quot; DS bit (0 or 1).</p>
<dt><i>-w &lt;iswep&gt;</i></p>
<dd>Frame control, WEP bit (0 or 1).</p>
<dt><i>-D </i></p>
<dd>Disable AP Detection.</dl>
<dl>
<dt><code>Replay options:</code></p>
<dd>
<dt><i>-x &lt;nbpps&gt;</i></p>
<dd>Number of packets per second.</p>
<dt><i>-p &lt;fctrl&gt;</i></p>
<dd>Set frame control word (hex).</p>
<dt><i>-a &lt;bssid&gt;</i></p>
<dd>Set Access Point MAC address.</p>
<dt><i>-c &lt;dmac&gt;</i></p>
<dd>Set destination MAC address.</p>
<dt><i>-h &lt;smac&gt;</i></p>
<dd>Set source MAC address.</p>
<dt><i>-g &lt;nb_packets&gt;</i></p>
<dd>Change ring buffer size (default: 8 packets). The minimum is 1.</p>
<dt><i>-F</i></p>
<dd>Choose first matching packet.</p>
<dt><i>-e &lt;essid&gt;</i></p>
<dd>Fake Authentication attack: Set target SSID (see below). For SSID containing special characters, see <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names">http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names</a></p>
<dt><i>-o &lt;npackets&gt;</i></p>
<dd>Fake Authentication attack: Set the number of packets for every authentication and association attempt (Default: 1). 0 means auto</p>
<dt><i>-q &lt;seconds&gt;</i></p>
<dd>Fake Authentication attack: Set the time between keep-alive packets in fake authentication mode.</p>
<dt><i>-Q</i></p>
<dd>Fake Authentication attack: Sends reassociation requests instead of performing a complete authentication and association after each delay period.</p>
<dt><i>-y &lt;prga&gt;</i></p>
<dd>Fake Authentication attack: Specifies the keystream file for fake shared key authentication.</p>
<dt><i>-T n</i></p>
<dd>Fake Authentication attack: Exit if fake authentication fails &#8216;n&#8217; time(s).</p>
<dt><i>-j</i></p>
<dd>ARP Replay attack : inject FromDS pakets (see below).</p>
<dt><i>-k &lt;IP&gt;</i></p>
<dd>Fragmentation attack: Set destination IP in fragments.</p>
<dt><i>-l &lt;IP&gt;</i></p>
<dd>Fragmentation attack: Set source IP in fragments.</p>
<dt><i>-B</i></p>
<dd>Test option: bitrate test.</dl>
<dl>
<dt><code>Source options:</code></p>
<dd>
<dt><i>-i &lt;iface&gt;</i></p>
<dd>Capture packets from this interface.</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd>Extract packets from this pcap file.</dl>
<dl>
<dt><code>Miscellaneous options:</code></p>
<dd>
<dt><i>-R</i></p>
<dd>disable /dev/rtc usage.</dl>
<p> <i>&#8211;ignore-negative-one</i> if the interface&#8217;s channel can&#8217;t be determined ignore the mismatch, needed for unpatched cfg80211 </p>
<dl>
<dt><code>Attack modes: </code></p>
<dd>
<dt><i>-0 &lt;count&gt;, &#8211;deauth=&lt;count&gt;</i></p>
<dd>This attack sends deauthentication packets to one or more clients which are currently associated with a particular access point. Deauthenticating clients can be done for a number of reasons: Recovering a hidden ESSID. This is an ESSID which is not being broadcast. Another term for this is &quot;cloaked&quot; or Capturing WPA/WPA2 handshakes by forcing clients to reauthenticate or Generate ARP requests (Windows clients sometimes flush their ARP cache when disconnected). Of course, this attack is totally useless if there are no associated wireless client or on fake authentications.</p>
<dt><i>-1 &lt;delay&gt;, &#8211;fakeauth=&lt;delay&gt;</i></p>
<dd>The fake authentication attack allows you to perform the two types of WEP authentication (Open System and Shared Key) plus associate with the access point (AP). This is useful is only useful when you need an associated MAC address in various aireplay-ng attacks and there is currently no associated client. It should be noted that the fake authentication attack does NOT generate any ARP packets. Fake authentication cannot be used to authenticate/associate with WPA/WPA2 Access Points.</p>
<dt><i>-2, &#8211;interactive</i></p>
<dd>This attack allows you to choose a specific packet for replaying (injecting). The attack can obtain packets to replay from two sources. The first being a live flow of packets from your wireless card. The second being from a pcap file. Reading from a file is an often overlooked feature of aireplay-ng. This allows you read packets from other capture sessions or quite often, various attacks generate pcap files for easy reuse. A common use of reading a file containing a packet your created with packetforge-ng.</p>
<dt><i>-3, &#8211;arpreplay</i></p>
<dd>The classic ARP request replay attack is the most effective way to generate new initialization vectors (IVs), and works very reliably. The program listens for an ARP packet then retransmits it back to the access point. This, in turn, causes the access point to repeat the ARP packet with a new IV. The program retransmits the same ARP packet over and over. However, each ARP packet repeated by the access point has a new IVs. It is all these new IVs which allow you to determine the WEP key.</p>
<dt><i>-4, &#8211;chopchop</i></p>
<dd>This attack, when successful, can decrypt a WEP data packet without knowing the key. It can even work against dynamic WEP. This attack does not recover the WEP key itself, but merely reveals the plaintext. However, some access points are not vulnerable to this attack. Some may seem vulnerable at first but actually drop data packets shorter that 60 bytes. If the access point drops packets shorter than 42 bytes, aireplay tries to guess the rest of the missing data, as far as the headers are predictable. If an IP packet is captured, it additionally checks if the checksum of the header is correct after guessing the missing parts of it. This attack requires at least one WEP data packet.</p>
<dt><i>-5, &#8211;fragment</i></p>
<dd>This attack, when successful, can obtain 1500 bytes of PRGA (pseudo random generation algorithm). This attack does not recover the WEP key itself, but merely obtains the PRGA. The PRGA can then be used to generate packets with packetforge-ng which are in turn used for various injection attacks. It requires at least one data packet to be received from the access point in order to initiate the attack.</p>
<dt><i>-6, &#8211;caffe-latte</i></p>
<dd>In general, for an attack to work, the attacker has to be in the range of an AP and a connected client (fake or real). Caffe Latte attacks allows one to gather enough packets to crack a WEP key without the need of an AP, it just need a client to be in range.</p>
<dt><i>-7, &#8211;cfrag</i></p>
<dd>This attack turns IP or ARP packets from a client into ARP request against the client. This attack works especially well against ad-hoc networks. As well it can be used against softAP clients and normal AP clients.</p>
<dt><i>-8, &#8211;migmode</i></p>
<dd>This attack works against Cisco Aironet access points configured in WPA Migration Mode, which enables both WPA and WEP clients to associate to an access point using the same Service Set Identifier (SSID). The program listens for a WEP-encapsulated broadcast ARP packet, bitflips it to make it into an ARP coming from the attacker&#8217;s MAC address and retransmits it to the access point. This, in turn, causes the access point to repeat the ARP packet with a new IV and also to forward the ARP reply to the attacker with a new IV. The program retransmits the same ARP packet over and over. However, each ARP packet repeated by the access point has a new IV as does the ARP reply forwarded to the attacker by the access point. It is all these new IVs which allow you to determine the WEP key.</p>
<dt><i>-9, &#8211;test</i></p>
<dd>Tests injection and quality.</dl>
<h2>Fragmentation Versus Chopchop</h2>
<p><code>Fragmentation:</code></p>
<dl>
<dt></dl>
<dd><i>Pros</i><br />
 &#8211; Can obtain the full packet length of 1500 bytes XOR. This means you can subsequently pretty well create any size of packet.<br />
 &#8211; May work where chopchop does not<br />
 &#8211; Is extremely fast. It yields the XOR stream extremely quickly when successful.</p>
<dl>
<dt></dl>
<dd><i>Cons</i><br />
 &#8211; Setup to execute the attack is more subject to the device drivers. For example, Atheros does not generate the correct packets unless the wireless card is set to the mac address you are spoofing.<br />
 &#8211; You need to be physically closer to the access point since if any packets are lost then the attack fails. </p>
<p> <code>Chopchop</code></p>
<dl>
<dt></dl>
<dd><i>Pro</i><br />
 &#8211; May work where frag does not work.</p>
<dl>
<dt></dl>
<dd><i>Cons</i><br />
 &#8211; Cannot be used against every access point.<br />
 &#8211; The maximum XOR bits is limited to the length of the packet you chopchop against.<br />
 &#8211; Much slower then the fragmentation attack.</p>
<h2>Author</h2>
<p>This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
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
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
