---
title: "airbase-ng(1)"
name: "airbase-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airbase-ng/"
description: "airbase-ng – multi-purpose tool aimed at attacking clients as opposed to the Access Point (AP) itself"
---

<h2 class="name">NAME</h2>
<p> airbase-ng &#8211; multi-purpose tool aimed at attacking clients as opposed to the Access Point (AP) itself </p>
<h2>SYNOPSIS</h2>
<p> <code>airbase-ng</code> [options] &lt;interface name&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>airbase-ng</code> is multi-purpose tool aimed at attacking clients as opposed to the Access Point (AP) itself. Since it is so versatile and flexible, summarizing it is a challenge. Here are some of the feature highlights:<br />
 &#8211; Implements the Caffe Latte WEP client attack<br />
 &#8211; Implements the Hirte WEP client attack<br />
 &#8211; Ability to cause the WPA/WPA2 handshake to be captured<br />
 &#8211; Ability to act as an ad-hoc Access Point<br />
 &#8211; Ability to act as a full Access Point<br />
 &#8211; Ability to filter by SSID or client MAC addresses<br />
 &#8211; Ability to manipulate and resend packets<br />
 &#8211; Ability to encrypt sent packets and decrypt received packets </p>
<p> The main idea is of the implementation is that it should encourage clients to associate with the fake AP, not prevent them from accessing the real AP. </p>
<p> A tap interface (atX) is created when airbase-ng is run. This can be used to receive decrypted packets or to send encrypted packets. </p>
<p> As real clients will most probably send probe requests for common/configured networks, these frames are important for binding a client to our softAP. In this case, the AP will respond to any probe request with a proper probe response, which tells the client to authenticate to the airbase-ng BSSID. That being said, this mode could possibly disrupt the correct functionality of many APs on the same channel.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><i>-a &lt;bssid&gt;</i></p>
<dd> If the BSSID is not explicitly specified by using &quot;-a &lt;BSSID&gt;&quot;, then the current MAC of the specified interface is used.</p>
<dt><i>-i &lt;iface&gt;</i></p>
<dd> Also capture and process from this interface in addition to the replay interface.</p>
<dt><i>-w &lt;WEP key&gt;</i></p>
<dd> If WEP should be used as encryption, then the parameter &quot;-w &lt;WEP key&gt;&quot; sets the en-/decryption key. This is sufficient to let airbase-ng set all the appropriate flags by itself. If the softAP operates with WEP encryption, the client can choose to use open system authentication or shared key authentication. Both authentication methods are supported by airbase-ng. But to get a keystream, the user can try to force the client to use shared key authentication. &quot;-s&quot; forces a shared key auth and &quot;-S &lt;len&gt;&quot; sets the challenge length.</p>
<dt><i>-h &lt;MAC&gt;</i></p>
<dd> This is the source MAC for the man-in-the-middle attack. The &quot;-M&quot; must also be specified.</p>
<dt><i>-f &lt;disallow&gt;</i></p>
<dd> If this option is not specified, it defaults to &quot;-f allow&quot;. This means the various client MAC filters (-d and -D) define which clients to accept. </p>
<p> By using the &quot;-f disallow&quot; option, this reverses selection and causes airbase to ignore the clients specified by the filters.</p>
<dt><i>-W &lt;0|1&gt;</i></p>
<dd> This sets the beacon WEP flag. Remember that clients will normally only connect to APs which are the same as themselves. Meaning WEP to WEP, open to open. </p>
<p> The &quot;auto&quot; option is to allow airbase-ng to automatically set the flag based on context of the other options specified. For example, if you set a WEP key with -w, then the beacon flag would be set to WEP. </p>
<p> One other use of &quot;auto&quot; is to deal with clients which can automatically adjust their connection type. However, these are few and far between. </p>
<p> In practice, it is best to set the value to the type of clients you are dealing with.</p>
<dt><i>-q</i></p>
<dd> This surpresses printing any statistics or status information.</p>
<dt><i>-v</i></p>
<dd> This prints additional messages and details to assist in debugging.</p>
<dt><i>-M</i></p>
<dd> This option is not implemented yet. It is a man-in-the-middle attack between specified clients and BSSIDs.</p>
<dt><i>-A, &#8211;ad-hoc</i></p>
<dd> This causes airbase-ng to act as an ad-hoc client instead of a normal Access Point. </p>
<p> In ad-hoc mode airbase-ng also sends beacons, but doesn&#8217;t need any authentication/association. It can be activated by using &quot;-A&quot;. The soft AP will adjust all flags needed to simulate a station in ad-hoc mode automatically and generate a random MAC, which is used as CELL MAC instead of the BSSID. This can be overwritten by the &quot;-a &lt;BSSID&gt;&quot; tag. The interface MAC will then be used as source mac, which can be changed with &quot;-h &lt;sourceMAC&gt;&quot;.</p>
<dt><i>-Y &lt;in|out|both&gt;</i></p>
<dd> The parameter &quot;-Y&quot; enables the &quot;external processing&quot; Mode. This creates a second interface &quot;atX&quot;, which is used to replay/modify/drop or inject packets at will. This interface must also be brought up with ifconfig and an external tool is needed to create a loop on that interface. </p>
<p> The packet structure is rather simple: the ethernet header (14 bytes) is ignored and right after that follows the complete ieee80211 frame the same way it is going to be processed by airbase-ng (for incoming packets) or before the packets will be sent out of the wireless card (outgoing packets). This mode intercepts all data packets and loops them through an external application, which decides what happens with them. The MAC and IP of the second tap interface doesn&#8217;t matter, as real ethernet frames on this interface are dropped dropped anyway. </p>
<p> There are 3 arguments for &quot;-Y&quot;: &quot;in&quot;, &quot;out&quot; and &quot;both&quot;, which specify the direction of frames to loop through the external application. Obviously &quot;in&quot; redirects only incoming (through the wireless NIC) frames, while outgoing frames aren&#8217;t touched. &quot;out&quot; does the opposite, it only loops outgoing packets and &quot;both&quot; sends all both directions through the second tap interface. </p>
<p> There is a small and simple example application to replay all frames on the second interface. The tool is called &quot;replay.py&quot; and is located in &quot;./test&quot;. It&#8217;s written in python, but the language doesn&#8217;t matter. It uses pcapy to read the frames and scapy to possibly alter/show and reinject the frames. The tool as it is, simply replays all frames and prints a short summary of the received frames. The variable &quot;packet&quot; contains the complete ieee80211 packet, which can easily be dissected and modified using scapy. </p>
<p> This can be compared to ettercap filters, but is more powerful, as a real programming language can be used to build complex logic for filtering and packet customization. The downside on using python is, that it adds a delay of around 100ms and the cpu utilizations is rather large on a high speed network, but its perfect for a demonstration with only a few lines of code.</p>
<dt><i>-c &lt;channel&gt;</i></p>
<dd> This is used to specify the channel on which to run the Access Point.</p>
<dt><i>-X, &#8211;hidden</i></p>
<dd> This causes the Access Point to hide the SSID and to not broadcast the value.</p>
<dt><i>-s</i></p>
<dd> When specfiied, this forces shared key authentication for all clients. </p>
<p> The soft AP will send an &quot;authentication method unsupported&quot; rejection to any open system authentication request if &quot;-s&quot; is specified.</p>
<dt><i>-S</i></p>
<dd> It sets the shared key challenge length, which can be anything from 16 to 1480. The default is 128 bytes. It is the number of bytes used in the random challenge. Since one tag can contain a maximum size of 255 bytes, any value above 255 creates several challenge tags until all specified bytes are written. Many clients ignore values different than 128 bytes so this option may not always work.</p>
<dt><i>-L, &#8211;caffe-latte</i></p>
<dd> Airbase-ng also contains the new caffe-latte attack, which is also implemented in aireplay-ng as attack &quot;-6&quot;. It can be used with &quot;-L&quot; or &quot;caffe-latte&quot;. This attack specifically works against clients, as it waits for a broadcast arp request, which happens to be a gratuitous arp. See this for an explaination of what a gratuitous arp is. It then flips a few bits in the sender MAC and IP, corrects the ICV (crc32) value and sends it back to the client, where it came from. The point why this attack works in practice is, that at least windows sends gratuitous arps after a connection on layer 2 is established and a static ip is set, or dhcp fails and windows assigned an IP out of 169.254.X.X. </p>
<p> &quot;-x &lt;pps&gt;&quot; sets the number of packets per second to send when performing the caffe-latte attack. At the moment, this attack doesn&#8217;t stop, it continuously sends arp requests. Airodump-ng is needed to capture the replys.</p>
<dt><i>-N, &#8211;cfrag</i></p>
<dd> This attack listens for an ARP request or IP packet from the client. Once one is received, a small amount of PRGA is extracted and then used to create an ARP request packet targeted to the client. This ARP request is actually made of up of multiple packet fragments such that when received, the client will respond. </p>
<p> This attack works especially well against ad-hoc networks. As well it can be used against softAP clients and normal AP clients.</p>
<dt><i>-x &lt;nbpps&gt;</i></p>
<dd> This sets the number of packets per second that packets will be sent (default: 100).</p>
<dt><i>-y</i></p>
<dd> When using this option, the fake AP will not respond to broadcast probes. A broadcast probe is where the the specific AP is not identified uniquely. Typically, most APs will respond with probe responses to a broadcast probe. This flag will prevent this happening. It will only respond when the specific AP is uniquely requested.</p>
<dt><i>-0</i></p>
<dd> This enables all WPA/WPA2/WEP Tags to be enabled in the beacons sent. It cannot be specified when also using -z or -Z.</p>
<dt><i>-z &lt;type&gt;</i></p>
<dd> This specifies the WPA beacon tags. The valid values are: 1=WEP40 2=TKIP 3=WRAP 4=CCMP 5=WEP104.</p>
<dt><i>-Z &lt;type&gt;</i></p>
<dd> same as -z, but for WPA2</p>
<dt><i>-V &lt;type&gt;</i></p>
<dd> This specifies the valid EAPOL types. The valid values are: 1=MD5 2=SHA1 3=auto</p>
<dt><i>-F &lt;prefix&gt;</i></p>
<dd> This option causes airbase-ng to write all sent and received packets to a pcap file on disk. This is the file prefix (like airodump-ng -w).</p>
<dt><i>-P</i></p>
<dd> This causes the fake access point to respond to all probes regardless of the ESSIDs specified.</p>
<dt><i>-I &lt;interval&gt;</i></p>
<dd> This sets the time in milliseconds between each beacon.</p>
<dt><i>-C &lt;seconds&gt;</i></p>
<dd> The wildcard ESSIDs will also be beaconed this number of seconds. A good typical value to use is &quot;-C 60&quot; (require -P).</dl>
<dl>
<dt><code>Filter options:</code></p>
<dd>
<dt><i>&#8211;bssid &lt;MAC&gt;, -b &lt;MAC&gt;</i></p>
<dd> BSSID to filter/use.</p>
<dt><i>&#8211;bssids &lt;file&gt;, -B &lt;file&gt;</i></p>
<dd> Read a list of BSSIDs out of that file.</p>
<dt><i>&#8211;client &lt;MAC&gt;, -d &lt;MAC&gt;</i></p>
<dd> MAC of client to accept.</p>
<dt><i>&#8211;clients &lt;file&gt;, -D &lt;file&gt;</i></p>
<dd> Read a list of client&#8217;s MACs out of that file</p>
<dt><i>&#8211;essid &lt;ESSID&gt;, -e &lt;ESSID&gt;</i></p>
<dd> Specify a single ESSID. For SSID containing special characters, see <a rel="nofollow" href="http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names">http://www.aircrack-ng.org/doku.php?id=faq#how_to_use_spaces_double_quote_and_single_quote_etc._in_ap_names</a></p>
<dt><i>&#8211;essids &lt;file&gt;, -E &lt;file&gt;</i></p>
<dd> read a list of ESSIDs out of that file.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airodump-ng/">airodump-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airserv-ng/">airserv-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
<h2>Index</h2>
