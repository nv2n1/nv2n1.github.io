---

title: "aireplay-ng(1)"
name: "aireplay-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aireplay-ng/"
description: "aireplay-ng – inject packets into a wireless network to generate traffic"
---

<p> aireplay-ng &#8211; inject packets into a wireless network to generate traffic </p>
<h2>SYNOPSIS</h2>
<p> <code>aireplay-ng</code> [options] &lt;replay interface&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>aireplay-ng</code> is used to inject/replay frames. The primary function is to generate traffic for the later use in aircrack-ng for cracking the WEP and WPA-PSK keys. There are different attacks which can cause deauthentications for the purpose of capturing WPA handshake data, fake authentications, Interactive packet replay, hand-crafted ARP request injection and ARP-request reinjection. With the packetforge-ng tool it&#8217;s possible to create arbitrary frames. </p>
<p> <code>aireplay-ng</code> supports single-NIC injection/monitor.<br/>
 This feature needs driver patching. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-H, &#8211;help</i></dt>
<dd> Shows the help screen.</dd></dl>
<dl>
<dt><code>Filter options:</code></dt>
<dd>
</dd><dt><i>-b &lt;bssid&gt;</i></dt>
<dd> MAC address of access point.</dd>
<dt><i>-d &lt;dmac&gt;</i></dt>
<dd> MAC address of destination.</dd>
<dt><i>-s &lt;smac&gt;</i></dt>
<dd> MAC address of source.</dd>
<dt><i>-m &lt;len&gt;</i></dt>
<dd> Minimum packet length.</dd>
<dt><i>-n &lt;len&gt;</i></dt>
<dd> Maximum packet length.</dd>
<dt><i>-u &lt;type&gt;</i></dt>
<dd> Frame control, type field.</dd>
<dt><i>-v &lt;subt&gt;</i></dt>
<dd> Frame control, subtype field.</dd>
<dt><i>-t &lt;tods&gt;</i></dt>
<dd> Frame control, &quot;To&quot; DS bit (0 or 1).</dd>
<dt><i>-f &lt;fromds&gt;</i></dt>
<dd> Frame control, &quot;From&quot; DS bit (0 or 1).</dd>
<dt><i>-w &lt;iswep&gt;</i></dt>
<dd> Frame control, WEP bit (0 or 1).</dd>
<dt><i>-D </i></dt>
<dd> Disable AP Detection.</dd></dl>
<dl>
<dt><code>Replay options:</code></dt>
<dd>
</dd><dt><i>-x &lt;nbpps&gt;</i></dt>
<dd> Number of packets per second.</dd>
<dt><i>-p &lt;fctrl&gt;</i></dt>
<dd> Set frame control word (hex).</dd>
<dt><i>-a &lt;bssid&gt;</i></dt>
<dd> Set Access Point MAC address.</dd>
<dt><i>-c &lt;dmac&gt;</i></dt>
<dd> Set destination MAC address.</dd>
<dt><i>-h &lt;smac&gt;</i></dt>
<dd> Set source MAC address.</dd>
<dt><i>-g &lt;nb_packets&gt;</i></dt>
<dd> Change ring buffer size (default: 8 packets). The minimum is 1.</dd>
<dt><i>-F</i></dt>
<dd> Choose first matching packet.</dd>
<dt><i>-e &lt;essid&gt;</i></dt>
<dd> Fake Authentication attack: Set target SSID (see below). For SSID containing special characters, see <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names">http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names</a></dd>
<dt><i>-o &lt;npackets&gt;</i></dt>
<dd> Fake Authentication attack: Set the number of packets for every authentication and association attempt (Default: 1). 0 means auto</dd>
<dt><i>-q &lt;seconds&gt;</i></dt>
<dd> Fake Authentication attack: Set the time between keep-alive packets in fake authentication mode.</dd>
<dt><i>-y &lt;prga&gt;</i></dt>
<dd> Fake Authentication attack: Specifies the keystream file for fake shared key authentication.</dd>
<dt><i>-T n</i></dt>
<dd> Fake Authentication attack: Exit if fake authentication fails &#8216;n&#8217; time(s).</dd>
<dt><i>-j</i></dt>
<dd> ARP Replay attack : inject FromDS pakets (see below).</dd>
<dt><i>-k &lt;IP&gt;</i></dt>
<dd> Fragmentation attack: Set destination IP in fragments.</dd>
<dt><i>-l &lt;IP&gt;</i></dt>
<dd> Fragmentation attack: Set source IP in fragments.</dd>
<dt><i>-B</i></dt>
<dd> Test option: bitrate test.</dd></dl>
<dl>
<dt><code>Source options:</code></dt>
<dd>
</dd><dt><i>-i &lt;iface&gt;</i></dt>
<dd> Capture packets from this interface.</dd>
<dt><i>-r &lt;file&gt;</i></dt>
<dd> Extract packets from this pcap file.</dd></dl>
<dl>
<dt><code>Miscellaneous options:</code></dt>
<dd>
</dd><dt><i>-R</i></dt>
<dd> disable /dev/rtc usage.</dd></dl>
<dl>
<dt><code>Attack modes: </code></dt>
<dd>
</dd><dt><i>-0 &lt;count&gt;, &#8211;deauth=&lt;count&gt;</i></dt>
<dd> This attack sends disassocate packets to one or more clients which are currently associated with a particular access point. Disassociating clients can be done for a number of reasons: Recovering a hidden ESSID. This is an ESSID which is not being broadcast. Another term for this is &quot;cloaked&quot; or Capturing WPA/WPA2 handshakes by forcing clients to reauthenticate or Generate ARP requests (Windows clients sometimes flush their ARP cache when disconnected). Of course, this attack is totally useless if there are no associated wireless client or on fake authentications.</dd>
<dt><i>-1 &lt;delay&gt;, &#8211;fakeauth=&lt;delay&gt;</i></dt>
<dd> The fake authentication attack allows you to perform the two types of WEP authentication (Open System and Shared Key) plus associate with the access point (AP). This is useful is only useful when you need an associated MAC address in various aireplay-ng attacks and there is currently no associated client. It should be noted that the fake authentication attack does NOT generate any ARP packets. Fake authentication cannot be used to authenticate/associate with WPA/WPA2 Access Points.</dd>
<dt><i>-2, &#8211;interactive</i></dt>
<dd> This attack allows you to choose a specific packet for replaying (injecting). The attack can obtain packets to replay from two sources. The first being a live flow of packets from your wireless card. The second being from a pcap file. Reading from a file is an often overlooked feature of aireplay-ng. This allows you read packets from other capture sessions or quite often, various attacks generate pcap files for easy reuse. A common use of reading a file containing a packet your created with packetforge-ng.</dd>
<dt><i>-3, &#8211;arpreplay</i></dt>
<dd> The classic ARP request replay attack is the most effective way to generate new initialization vectors (IVs), and works very reliably. The program listens for an ARP packet then retransmits it back to the access point. This, in turn, causes the access point to repeat the ARP packet with a new IV. The program retransmits the same ARP packet over and over. However, each ARP packet repeated by the access point has a new IVs. It is all these new IVs which allow you to determine the WEP key.</dd>
<dt><i>-4, &#8211;chopchop</i></dt>
<dd> This attack, when successful, can decrypt a WEP data packet without knowing the key. It can even work against dynamic WEP. This attack does not recover the WEP key itself, but merely reveals the plaintext. However, some access points are not vulnerable to this attack. Some may seem vulnerable at first but actually drop data packets shorter that 60 bytes. If the access point drops packets shorter than 42 bytes, aireplay tries to guess the rest of the missing data, as far as the headers are predictable. If an IP packet is captured, it additionally checks if the checksum of the header is correct after guessing the missing parts of it. This attack requires at least one WEP data packet.</dd>
<dt><i>-5, &#8211;fragment</i></dt>
<dd> This attack, when successful, can obtain 1500 bytes of PRGA (pseudo random generation algorithm). This attack does not recover the WEP key itself, but merely obtains the PRGA. The PRGA can then be used to generate packets with packetforge-ng which are in turn used for various injection attacks. It requires at least one data packet to be received from the access point in order to initiate the attack.</dd>
<dt><i>-6, &#8211;caffe-latte</i></dt>
<dd> In general, for an attack to work, the attacker has to be in the range of an AP and a connected client (fake or real). Caffe Latte attacks allows to gather enough packets to crack a WEP key without the need of an AP, it just need a client to be in range.</dd>
<dt><i>-7, &#8211;cfrag</i></dt>
<dd> This attack turns IP or ARP packets from a client into ARP request against the client. This attack works especially well against ad-hoc networks. As well it can be used against softAP clients and normal AP clients.</dd>
<dt><i>-9, &#8211;test</i></dt>
<dd> Tests injection and quality.</dd></dl>
<h2>FRAGMENTATION VERSUS CHOPCHOP</h2>
<p> <code>Fragmentation:</code></p>
<dl>
<dt></dt></dl>
<dd> <i>Pros</i><br/>
 &#8211; Can obtain the full packet length of 1500 bytes XOR. This means you can subsequently pretty well create any size of packet.<br/>
 &#8211; May work where chopchop does not<br/>
 &#8211; Is extremely fast. It yields the XOR stream extremely quickly when successful.</dd>
<dl>
<dt></dt></dl>
<dd> <i>Cons</i><br/>
 &#8211; Setup to execute the attack is more subject to the device drivers. For example, Atheros does not generate the correct packets unless the wireless card is set to the mac address you are spoofing.<br/>
 &#8211; You need to be physically closer to the access point since if any packets are lost then the attack fails. </dd>
<p> <code>Chopchop</code></p>
<dl>
<dt></dt></dl>
<dd> <i>Pro</i><br/>
 &#8211; May work where frag does not work.</dd>
<dl>
<dt></dt></dl>
<dd> <i>Cons</i><br/>
 &#8211; Cannot be used against every access point.<br/>
 &#8211; The maximum XOR bits is limited to the length of the packet you chopchop against.<br/>
 &#8211; Much slower then the fragmentation attack. </dd>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airodump-ng/">airodump-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airserv-ng/">airserv-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-airtun-ng/">airtun-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code><br/>
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
