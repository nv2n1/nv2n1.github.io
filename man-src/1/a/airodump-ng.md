---
title: "airodump-ng(1)"
name: "airodump-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airodump-ng/"
description: "airodump-ng – a wireless packet capture tool for aircrack-ng"
---

<h2 class="name">NAME</h2>
<p> airodump-ng &#8211; a wireless packet capture tool for aircrack-ng </p>
<h2>SYNOPSIS</h2>
<p> <code>airodump-ng</code> [options] &lt;interface name&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>airodump-ng</code> is used for packet capturing of raw 802.11 frames for the intent of using them with aircrack-ng. If you have a GPS receiver connected to the computer, airodump-ng is capable of logging the coordinates of the found access points. Additionally, airodump-ng writes out a text file containing the details of all access points and clients seen.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><i>-i, &#8211;ivs</i></p>
<dd> It only saves IVs (only useful for cracking). If this option is specified, you have to give a dump prefix (&#8211;write option)</p>
<dt><i>-g, &#8211;gpsd</i></p>
<dd> Indicate that airodump-ng should try to use GPSd to get coordinates.</p>
<dt><i>-w &lt;prefix&gt;, &#8211;write &lt;prefix&gt;</i></p>
<dd> Is the dump file prefix to use. If this option is not given, it will only show data on the screen. Beside this file a CSV file with the same filename as the capture will be created.</p>
<dt><i>-e, &#8211;beacons</i></p>
<dd> It will record all beacons into the cap file. By default it only records one beacon for each network.</p>
<dt><i>-u &lt;secs&gt;, &#8211;update &lt;secs&gt;</i></p>
<dd> Delay &lt;secs&gt; seconds delay between display updates (default: 1 second). Useful for slow CPU.</p>
<dt><i>&#8211;showack</i></p>
<dd> Prints ACK/CTS/RTS statistics. Helps in debugging and general injection optimization. It is indication if you inject, inject too fast, reach the AP, the frames are valid encrypted frames. Allows to detect &quot;hidden&quot; stations, which are too far away to capture high bitrate frames, as ACK frames are sent at 1Mbps.</p>
<dt><i>-h</i></p>
<dd> Hides known stations for &#8211;showack.</p>
<dt><i>&#8211;berlin &lt;secs&gt;</i></p>
<dd> Time before removing the AP/client from the screen when no more packets are received (Default: 120 seconds). See airodump-ng source for the history behind this option ;).</p>
<dt><i>-c &lt;channel&gt;[,&lt;channel&gt;[,&#8230;]], &#8211;channel &lt;channel&gt;[,&lt;channel&gt;[,&#8230;]]</i></p>
<dd> Indicate the channel(s) to listen to. By default airodump-ng hop on all 2.4Ghz channels.</p>
<dt><i>-b &lt;abg&gt;, &#8211;band &lt;abg&gt;</i></p>
<dd> Indicate the band on which airodump-ng should hop. It can be a combination of &#8216;a&#8217;, &#8216;b&#8217; and &#8216;g&#8217; letters (&#8216;b&#8217; and &#8216;g&#8217; uses 2.4Ghz and &#8216;a&#8217; uses 5Ghz). Incompatible with &#8211;channel option.</p>
<dt><i>-s &lt;method&gt;, &#8211;cswitch &lt;method&gt;</i></p>
<dd> Defines the way airodump-ng sets the channels when using more than one card. Valid values: 0, 1 or 2.</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd> Reads packet from a file.</p>
<dt><i>-x &lt;msecs&gt;</i></p>
<dd> Active Scanning Simulation (send probe requests and parse the probe responses).</p>
<dt><i>&#8211;output-format &lt;formats&gt;</i></p>
<dd> Define the formats to use (separated by a comma). Possible values are: pcap, ivs, csv, gps, kismet, netxml. The default values are: pcap, csv, kismet, kismet-newcore.<br />
 Theses values can be combined with the exception of ivs and pcap.</dl>
<p> <code>Filter options:</code></p>
<dl>
<dt><i>-t &lt;OPN|WEP|WPA|WPA1|WPA2&gt;, &#8211;encrypt &lt;OPN|WEP|WPA|WPA1|WPA2&gt;</i></p>
<dd> It will only show networks matching the given encryption. May be specified more than once: &#8216;-t OPN -t WPA2&#8217;</p>
<dt><i>-d &lt;bssid&gt;, &#8211;bssid &lt;bssid&gt;</i></p>
<dd> It will only show networks, matching the given bssid.</p>
<dt><i>-m &lt;mask&gt;, &#8211;netmask &lt;mask&gt;</i></p>
<dd> It will only show networks, matching the given bssid ^ netmask combination. Need &#8211;bssid (or -d) to be specified.</p>
<dt><i>-a</i></p>
<dd> It will only show associated clients.</dl>
<h2>EXAMPLES</h2>
<p> <code>airodump-ng</code> &#8211;band bg ath0 </p>
<p> Here is an example screenshot: </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
 CH 9 ][ Elapsed: 1 min ][ 2007-04-26 17:41 ][ BAT: 2 hours 10 mins ][ WPA handshake: 00:14:6C:7E:40:80<br />
 BSSID PWR RXQ Beacons #Data, #/s CH MB ENC CIPHER AUTH ESSID </p>
<p> 00:09:5B:1C:AA:1D 11 16 10 0 0 11 54. OPN &lt;length: 7&gt; 00:14:6C:7A:41:81 34 100 57 14 1 9 11 WEP WEP bigbear 00:14:6C:7E:40:80 32 100 752 73 2 9 54 WPA TKIP PSK teddy </p>
<p> BSSID STATION PWR Rate Lost Packets Probes </p>
<p> 00:14:6C:7A:41:81 00:0F:B5:32:31:31 51 11-11 2 14 bigbear (not associated) 00:14:A4:3F:8D:13 19 11-11 0 4 mossy 00:14:6C:7A:41:81 00:0C:41:52:D1:D1 -1 11-2 0 5 bigbear 00:14:6C:7E:40:80 00:0F:B5:FD:FB:C2 35 36-24 0 99 teddy<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; BSSID: MAC address of the access point. In the Client section, a BSSID of&nbsp;<wbr>&quot;(not associated)&quot;&nbsp;<wbr>means that the client is not associated with any AP. In this unassociated state, it is searching for an AP to connect with.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; PWR: Signal level reported by the card. Its signification depends on the driver, but as the signal gets higher you get closer to the AP or the station. If the BSSID PWR is -1, then the driver doesn&#8217;t support signal level reporting. If the PWR is -1 for a limited number of stations then this is for a packet which came from the AP to the client but the client transmissions are out of range for your card. Meaning you are hearing only 1/2 of the communication. If all clients have PWR as -1 then the driver doesn&#8217;t support signal level reporting.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; RXQ&nbsp;<wbr>(Only shown when on a fixed channel): Receive Quality as measured by the percentage of packets&nbsp;<wbr>(management and data frames)&nbsp;<wbr>successfully received over the last 10 seconds. It&#8217;s measured over all management and data frames. That&#8217;s the clue, this allows you to read more things out of this value. Lets say you got 100 percent RXQ and all 10&nbsp;<wbr>(or whatever the rate)&nbsp;<wbr>beacons per second coming in. Now all of a sudden the RXQ drops below 90, but you still capture all sent beacons. Thus you know that the AP is sending frames to a client but you can&#8217;t hear the client nor the AP sending to the client&nbsp;<wbr>(need to get closer). Another thing would be, that you got a 11MB card to monitor and capture frames&nbsp;<wbr>(say a prism2.5)&nbsp;<wbr>and you have a very good position to the AP. The AP is set to 54MBit and then again the RXQ drops, so you know that there is at least one 54MBit client connected to the AP.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Beacons: Number of beacons sent by the AP. Each access point sends about ten beacons per second at the lowest rate&nbsp;<wbr>(1M), so they can usually be picked up from very far.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>#Data: Number of captured data packets&nbsp;<wbr>(if WEP, unique IV count), including data broadcast packets.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211;&nbsp;<wbr>#/s: Number of data packets per second measure over the last 10 seconds.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; CH: Channel number&nbsp;<wbr>(taken from beacon packets). Note: sometimes packets from other channels are captured even if airodump-ng is not hopping, because of radio interference.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; MB: Maximum speed supported by the AP. If MB&nbsp;<wbr>=&nbsp;<wbr>11, it&#8217;s 802.11b, if MB&nbsp;<wbr>=&nbsp;<wbr>22 it&#8217;s 802.11b+&nbsp;<wbr>and higher rates are 802.11g. The dot&nbsp;<wbr>(after 54 above)&nbsp;<wbr>indicates short preamble is supported.&nbsp;<wbr>&#8216;e&#8217;&nbsp;<wbr>indicates that the network has QoS&nbsp;<wbr>(802.11e)&nbsp;<wbr>enabled.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; ENC: Encryption algorithm in use. OPN&nbsp;<wbr>=&nbsp;<wbr>no encryption,&quot;WEP?&quot;&nbsp;<wbr>=&nbsp;<wbr>WEP or higher&nbsp;<wbr>(not enough data to choose between WEP and WPA/WPA2), WEP&nbsp;<wbr>(without the question mark)&nbsp;<wbr>indicates static or dynamic WEP, and WPA or WPA2 if TKIP or CCMP or MGT is present.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; CIPHER: The cipher detected. One of CCMP, WRAP, TKIP, WEP, WEP40, or WEP104. Not mandatory, but TKIP is typically used with WPA and CCMP is typically used with WPA2. WEP40 is displayed when the key index is greater then 0. The standard states that the index can be 0-3 for 40bit and should be 0 for 104 bit.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; AUTH: The authentication protocol used. One of MGT&nbsp;<wbr>(WPA/WPA2 using a separate authentication server), SKA&nbsp;<wbr>(shared key for WEP), PSK&nbsp;<wbr>(pre-shared key for WPA/WPA2), or OPN&nbsp;<wbr>(open for WEP).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; ESSID: The so-called&nbsp;<wbr>&quot;SSID&quot;, which can be empty if SSID hiding is activated. In this case, airodump-ng will try to recover the SSID from probe responses and association requests.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; STATION: MAC address of each associated station or stations searching for an AP to connect with. Clients not currently associated with an AP have a BSSID of&nbsp;<wbr>&quot;(not associated)&quot;.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Rate: This is only displayed when using a single channel. The first number is the last data rate from the AP&nbsp;<wbr>(BSSID)&nbsp;<wbr>to the Client&nbsp;<wbr>(STATION). The second number is the last data rate from Client&nbsp;<wbr>(STATION)&nbsp;<wbr>to the AP&nbsp;<wbr>(BSSID).<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Lost: It means lost packets coming from the client. To determine the number of packets lost, there is a sequence field on every non-control frame, so you can subtract the second last sequence number from the last sequence number and you know how many packets you have lost.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Packets: The number of data packets sent by the client.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&#8211; Probes: The ESSIDs probed by the client. These are the networks the client is trying to connect to if it is not currently connected. </p>
<p> The first part is the detected access points. The second part is a list of detected wireless clients, stations. By relying on the signal power, one can even physically pinpoint the location of a given station.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airserv-ng/">airserv-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airtun-ng/">airtun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
<h2>Index</h2>
