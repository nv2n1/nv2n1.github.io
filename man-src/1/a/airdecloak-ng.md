---
title: "airdecloak-ng(1)"
name: "airdecloak-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airdecloak-ng/"
description: "airuncloak-ng – Removes wep cloaked framed from a pcap file."
---

<h2 class="name">NAME</h2>
<p> airuncloak-ng &#8211; Removes wep cloaked framed from a pcap file. </p>
<h2>SYNOPSIS</h2>
<p> <code>airuncloak-ng</code> &lt;options&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>airuncloak-ng</code> is a tool that removes wep cloaking from a pcap file. Some WIPS (actually one) can actively &quot;prevent&quot; cracking a WEP key by inserting chaff (fake wep frames) in the air to fool aircrack-ng. In some rare cases, cloaking fails and the key can be recovered without removing this chaff. In the cases where the key cannot be recovered, use this tool to filter out chaff. </p>
<p> The program works by reading the input file and selecting packets from a specific network. Each selected packet is put into a list and classified (default status is &quot;unknown&quot;). Filters are then applied (in the order specified by the user) on this list. They will change the status of the packets (unknown, uncloaked, potentially cloaked or cloaked). The order of the filters is really important since each filter will base its analysis amongst other things on the status of the packets and different orders will give different results. </p>
<p> Important requirement: The pcap file needs to have all packets (including beacons and all other &quot;useless&quot; packets) for the analysis (and if possible, prism/radiotap headers).</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><i>-i &lt;file&gt;</i></p>
<dd> Path to the capture file.</p>
<dt><i>&#8211;ssid &lt;ESSID&gt;</i></p>
<dd> Essid of the network (not yet implemented) to filter.</p>
<dt><i>&#8211;bssid &lt;BSSID&gt;</i></p>
<dd> BSSID of the network to filter.</p>
<dt><i>&#8211;null-packets</i></p>
<dd> Assume that null packets can be cloaked.</p>
<dt><i>&#8211;disable-base-filter</i></p>
<dd> Do not apply base filter.</p>
<dt><i>&#8211;drop-frag</i></p>
<dd> Drop fragmented packets.</p>
<dt><i>&#8211;filters &lt;filters&gt;</i></p>
<dd> Apply different filters (separated by a comma). See below.</dl>
<h2>FILTERS</h2>
<dl>
<dt><i>signal</i></p>
<dd> Try to filter based on signal (prism or radiotap headers in the pcap file).</p>
<dt><i>duplicate_sn</i></p>
<dd> Remove all duplicate sequence numbers for both the AP and the client (that are close to each other).</p>
<dt><i>duplicate_sn_ap</i></p>
<dd> Remove duplicate sequence number for the AP only (that are close to each other).</p>
<dt><i>duplicate_sn_client</i></p>
<dd> Remove duplicate sequence number for the client only (that are close to each other).</p>
<dt><i>consecutive_sn</i></p>
<dd> Filter based on the fact that IV should be consecutive (only for AP).</p>
<dt><i>duplicate_iv</i></p>
<dd> Filter out all duplicate IV.</p>
<dt><i>signal_dup_consec_sn</i></p>
<dd> Use signal (if available), duplicate and consecutive sequence number (filtering is much more precise than using all these filters one by one).</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
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
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-besside-ng-crawler/">besside-ng-crawler</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wpaclean/">wpaclean</a>(1)</code> </p>
<h2>Index</h2>
