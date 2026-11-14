---
title: "airodump-ng(8)"
name: "airodump-ng"
section: "8"
letter: "a"
url: "/docs/linux/man/8-airodump-ng/"
description: "airodump-ng – a wireless packet capture tool for aircrack-ng"
---

<p>airodump-ng &#8211; a wireless packet capture tool for aircrack-ng</p>
<h2>Synopsis</h2>
<p><code>airodump-ng</code> [options] &lt;interface name&gt;</p>
<h2>Description</h2>
<p><code>airodump-ng</code> is used for packet capturing of raw 802.11 frames for the intent of using them with aircrack-ng. If you have a GPS receiver connected to the computer, airodump-ng is capable of logging the coordinates of the found access points. Additionally, airodump-ng writes out a text file containing the details of all access points and clients seen.</p>
<h2>Options</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd>Shows the help screen.</p>
<dt><i>-i, &#8211;ivs</i></p>
<dd>It only saves IVs (only useful for cracking). If this option is specified, you have to give a dump prefix (&#8211;write option)</p>
<dt><i>-g, &#8211;gpsd</i></p>
<dd>Indicate that airodump-ng should try to use GPSd to get coordinates.</p>
<dt><i>-w &lt;prefix&gt;, &#8211;write &lt;prefix&gt;</i></p>
<dd>Is the dump file prefix to use. If this option is not given, it will only show data on the screen. Beside this file a CSV file with the same filename as the capture will be created.</p>
<dt><i>-e, &#8211;beacons</i></p>
<dd>It will record all beacons into the cap file. By default it only records one beacon for each network.</p>
<dt><i>-u &lt;secs&gt;, &#8211;update &lt;secs&gt;</i></p>
<dd>Delay &lt;secs&gt; seconds delay between display updates (default: 1 second). Useful for slow CPU.</p>
<dt><i>&#8211;showack</i></p>
<dd>Prints ACK/CTS/RTS statistics. Helps in debugging and general injection optimization. It is indication if you inject, inject too fast, reach the AP, the frames are valid encrypted frames. Allows one to detect &quot;hidden&quot; stations, which are too far away to capture high bitrate frames, as ACK frames are sent at 1Mbps.</p>
<dt><i>-h</i></p>
<dd>Hides known stations for &#8211;showack.</p>
<dt><i>&#8211;berlin &lt;secs&gt;</i></p>
<dd>Time before removing the AP/client from the screen when no more packets are received (Default: 120 seconds). See airodump-ng source for the history behind this option ;).</p>
<dt><i>-c &lt;channel&gt;[,&lt;channel&gt;[,&#8230;]], &#8211;channel &lt;channel&gt;[,&lt;channel&gt;[,&#8230;]]</i></p>
<dd>Indicate the channel(s) to listen to. By default airodump-ng hop on all 2.4GHz channels.</p>
<dt><i>-b &lt;abg&gt;, &#8211;band &lt;abg&gt;</i></p>
<dd>Indicate the band on which airodump-ng should hop. It can be a combination of &#8216;a&#8217;, &#8216;b&#8217; and &#8216;g&#8217; letters (&#8216;b&#8217; and &#8216;g&#8217; uses 2.4GHz and &#8216;a&#8217; uses 5GHz). Incompatible with &#8211;channel option.</p>
<dt><i>-s &lt;method&gt;, &#8211;cswitch &lt;method&gt;</i></p>
<dd>Defines the way airodump-ng sets the channels when using more than one card. Valid values: 0 (FIFO, default value), 1 (Round Robin) or 2 (Hop on last).</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd>Reads packet from a file.</p>
<dt><i>-x &lt;msecs&gt;</i></p>
<dd>Active Scanning Simulation (send probe requests and parse the probe responses).</p>
<dt><i>-M, &#8211;manufacturer</i></p>
<dd>Display a manufacturer column with the information obtained from the IEEE OUI list. See <a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</p>
<dt><i>-U, &#8211;uptime</i></p>
<dd>Display APs uptime obtained from its beacon timestamp.</p>
<dt><i>-W, &#8211;wps</i></p>
<dd>Display a WPS column with WPS version, config method(s), AP Setup Locked obtained from APs beacon or probe response (if any).</p>
<dt><i>&#8211;output-format &lt;formats&gt;</i></p>
<dd>Define the formats to use (separated by a comma). Possible values are: pcap, ivs, csv, gps, kismet, netxml. The default values are: pcap, csv, kismet, kismet-newcore. &#8216;pcap&#8217; is for recording a capture in pcap format, &#8216;ivs&#8217; is for ivs format (it is a shortcut for &#8211;ivs). &#8216;csv&#8217; will create an airodump-ng CSV file, &#8216;kismet&#8217; will create a kismet csv file and &#8216;kismet-newcore&#8217; will create the kismet netxml file. &#8216;gps&#8217; is a shortcut for &#8211;gps.<br />
 Theses values can be combined with the exception of ivs and pcap.</p>
<dt><i>-I &lt;seconds&gt;, &#8211;write-interval &lt;seconds&gt;</i></p>
<dd>Output file(s) write interval for CSV, Kismet CSV and Kismet NetXML in seconds (minimum: 1 second). By default: 5 seconds. Note that an interval too small might slow down airodump-ng.</p>
<dt><i>&#8211;ignore-negative-one</i></p>
<dd>Removes the message that says &#8216;fixed channel &lt;interface&gt;: -1&#8217;.</dl>
<p> <code>Filter options:</code></p>
<dl>
<dt><i>-t &lt;OPN|WEP|WPA|WPA1|WPA2&gt;, &#8211;encrypt &lt;OPN|WEP|WPA|WPA1|WPA2&gt;</i></p>
<dd>It will only show networks matching the given encryption. May be specified more than once: &#8216;-t OPN -t WPA2&#8217;</p>
<dt><i>-d &lt;bssid&gt;, &#8211;bssid &lt;bssid&gt;</i></p>
<dd>It will only show networks, matching the given bssid.</p>
<dt><i>-m &lt;mask&gt;, &#8211;netmask &lt;mask&gt;</i></p>
<dd>It will only show networks, matching the given bssid ^ netmask combination. Need &#8211;bssid (or -d) to be specified.</p>
<dt><i>-a</i></p>
<dd>It will only show associated clients.</p>
<dt><i>-N, &#8211;essid</i></p>
<dd>Filter APs by ESSID. Can be used several times to match a set of ESSID.</p>
<dt><i>-R, &#8211;essid-regex</i></p>
<dd>Filter APs by ESSID using a regular expression.</dl>
<h2>Interaction</h2>
<p><code>airodump-ng</code> can receive and interpret key strokes while running. The following list describes the currently assigned keys and supposed actions:</p>
<dl>
<dt><i>a</i></p>
<dd>Select active areas by cycling through these display options: AP+STA; AP+STA+ACK; AP only; STA only</p>
<dt><i>d</i></p>
<dd>Reset sorting to defaults (Power)</p>
<dt><i>i</i></p>
<dd>Invert sorting algorithm</p>
<dt><i>m</i></p>
<dd>Mark the selected AP or cycle through different colors if the selected AP is already marked</p>
<dt><i>r</i></p>
<dd>(De-)Activate realtime sorting &#8211; applies sorting algorithm everytime the display will be redrawn</p>
<dt><i>s</i></p>
<dd>Change column to sort by, which currently includes: First seen; BSSID; PWR level; Beacons; Data packets; Packet rate; Channel; Max. data rate; Encryption; Strongest Ciphersuite; Strongest Authentication; ESSID</p>
<dt><i>SPACE</i></p>
<dd>Pause display redrawing/ Resume redrawing</p>
<dt><i>TAB</i></p>
<dd>Enable/Disable scrolling through AP list</p>
<dt><i>UP</i></p>
<dd>Select the AP prior to the currently marked AP in the displayed list if available</p>
<dt><i>DOWN</i></p>
<dd>Select the AP after the currently marked AP if available</dl>
<p> If an AP is selected or marked, all the connected stations will also be selected or marked with the same color as the corresponding Access Point.</p>
<h2>Examples</h2>
<p><code>airodump-ng</code> &#8211;band bg ath0 </p>
<p> Here is an example screenshot: </p>
<p> &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211;<br />
 CH 9 ][ Elapsed: 1 min ][ 2007-04-26 17:41 ][ BAT: 2 hours 10 mins ][ WPA handshake: 00:14:6C:7E:40:80 </p>
<p> BSSID PWR RXQ Beacons #Data, #/s CH MB ENC CIPHER AUTH ESSID </p>
<p> 00:09:5B:1C:AA:1D 11 16 10 0 0 11 54. OPN &lt;length: 7&gt;<br />
 00:14:6C:7A:41:81 34 100 57 14 1 9 11 WEP WEP bigbear<br />
 00:14:6C:7E:40:80 32 100 752 73 2 9 54 WPA TKIP PSK teddy </p>
<p> BSSID STATION PWR Rate Lost Frames Probes </p>
<p> 00:14:6C:7A:41:81 00:0F:B5:32:31:31 51 11-11 2 14 bigbear<br />
 (not associated) 00:14:A4:3F:8D:13 19 11-11 0 4 mossy<br />
 00:14:6C:7A:41:81 00:0C:41:52:D1:D1 -1 11-2 0 5 bigbear<br />
 00:14:6C:7E:40:80 00:0F:B5:FD:FB:C2 35 36-24 0 99 teddy<br />
 &#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8212;&#8211; </p>
<dl>
<dt><i>BSSID</i></p>
<dd>MAC address of the access point. In the Client section, a BSSID of &quot;(not associated)&quot; means that the client is not associated with any AP. In this unassociated state, it is searching for an AP to connect with.</p>
<dt><i>PWR</i></p>
<dd>Signal level reported by the card. Its signification depends on the driver, but as the signal gets higher you get closer to the AP or the station. If the BSSID PWR is -1, then the driver doesn&#8217;t support signal level reporting. If the PWR is -1 for a limited number of stations then this is for a packet which came from the AP to the client but the client transmissions are out of range for your card. Meaning you are hearing only 1/2 of the communication. If all clients have PWR as -1 then the driver doesn&#8217;t support signal level reporting.</p>
<dt><i>RXQ</i></p>
<dd>Only shown when on a fixed channel. Receive Quality as measured by the percentage of packets (management and data frames) successfully received over the last 10 seconds. It&#8217;s measured over all management and data frames. That&#8217;s the clue, this allows you to read more things out of this value. Lets say you got 100 percent RXQ and all 10 (or whatever the rate) beacons per second coming in. Now all of a sudden the RXQ drops below 90, but you still capture all sent beacons. Thus you know that the AP is sending frames to a client but you can&#8217;t hear the client nor the AP sending to the client (need to get closer). Another thing would be, that you got a 11MB card to monitor and capture frames (say a prism2.5) and you have a very good position to the AP. The AP is set to 54MBit and then again the RXQ drops, so you know that there is at least one 54MBit client connected to the AP.</p>
<dt><i>Beacons</i></p>
<dd>Number of beacons sent by the AP. Each access point sends about ten beacons per second at the lowest rate (1M), so they can usually be picked up from very far.</p>
<dt><i>#Data</i></p>
<dd>Number of captured data packets (if WEP, unique IV count), including data broadcast packets.</p>
<dt><i>#/s</i></p>
<dd>Number of data packets per second measure over the last 10 seconds.</p>
<dt><i>CH</i></p>
<dd>Channel number (taken from beacon packets). Note: sometimes packets from other channels are captured even if airodump-ng is not hopping, because of radio interference.</p>
<dt><i>MB</i></p>
<dd>Maximum speed supported by the AP. If MB = 11, it&#8217;s 802.11b, if MB = 22 it&#8217;s 802.11b+ and higher rates are 802.11g. The dot (after 54 above) indicates short preamble is supported. &#8216;e&#8217; indicates that the network has QoS (802.11e) enabled.</p>
<dt><i>ENC</i></p>
<dd>Encryption algorithm in use. OPN = no encryption,&quot;WEP?&quot; = WEP or higher (not enough data to choose between WEP and WPA/WPA2), WEP (without the question mark) indicates static or dynamic WEP, and WPA or WPA2 if TKIP or CCMP or MGT is present.</p>
<dt><i>CIPHER</i></p>
<dd>The cipher detected. One of CCMP, WRAP, TKIP, WEP, WEP40, or WEP104. Not mandatory, but TKIP is typically used with WPA and CCMP is typically used with WPA2. WEP40 is displayed when the key index is greater then 0. The standard states that the index can be 0-3 for 40bit and should be 0 for 104 bit.</p>
<dt><i>AUTH</i></p>
<dd>The authentication protocol used. One of MGT (WPA/WPA2 using a separate authentication server), SKA (shared key for WEP), PSK (pre-shared key for WPA/WPA2), or OPN (open for WEP).</p>
<dt><i>WPS</i></p>
<dd>This is only displayed when &#8211;wps (or -W) is specified. If the AP supports WPS, the first field of the column indicates version supported. The second field indicates WPS config methods (can be more than one method, separated by comma): USB = USB method, ETHER = Ethernet, LAB = Label, DISP = Display, EXTNFC = External NFC, INTNFC = Internal NFC, NFCINTF = NFC Interface, PBC = Push Button, KPAD = Keypad. Locked is displayed when AP setup is locked.</p>
<dt><i>ESSID</i></p>
<dd>The so-called &quot;SSID&quot;, which can be empty if SSID hiding is activated. In this case, airodump-ng will try to recover the SSID from probe responses and association requests.</p>
<dt><i>STATION</i></p>
<dd>MAC address of each associated station or stations searching for an AP to connect with. Clients not currently associated with an AP have a BSSID of &quot;(not associated)&quot;.</p>
<dt><i>Rate</i></p>
<dd>This is only displayed when using a single channel. The first number is the last data rate from the AP (BSSID) to the Client (STATION). The second number is the last data rate from Client (STATION) to the AP (BSSID).</p>
<dt><i>Lost</i></p>
<dd>It means lost packets coming from the client. To determine the number of packets lost, there is a sequence field on every non-control frame, so you can subtract the second last sequence number from the last sequence number and you know how many packets you have lost.</p>
<dt><i>Packets</i></p>
<dd>The number of data packets sent by the client.</p>
<dt><i>Probes</i></p>
<dd>The ESSIDs probed by the client. These are the networks the client is trying to connect to if it is not currently connected.</dl>
<p> The first part is the detected access points. The second part is a list of detected wireless clients, stations. By relying on the signal power, one can even physically pinpoint the location of a given station.</p>
<h2>Author</h2>
<p>This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
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
