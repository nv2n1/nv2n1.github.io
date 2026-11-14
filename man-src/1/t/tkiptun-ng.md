---
title: "tkiptun-ng(1)"
name: "tkiptun-ng"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tkiptun-ng/"
description: "tkiptun-ng – inject a few frames into a WPA TKIP network with QoS"
---

<h2 class="name">NAME</h2>
<p> tkiptun-ng &#8211; inject a few frames into a WPA TKIP network with QoS </p>
<h2>SYNOPSIS</h2>
<p> <code>tkiptun-ng</code> [options] &lt;replay interface&gt;</p>
<h2>DESCRIPTION</h2>
<p> <code>tkiptun-ng</code> is a tool created by Martin Beck aka hirte, a member of aircrack-ng team. This tool is able to inject a few frames into a WPA TKIP network with QoS. He worked with Erik Tews (who created PTW attack) for a conference in PacSec 2008: &quot;Gone in 900 Seconds, Some Crypto Issues with WPA&quot;.</p>
<h2>OPERATION</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd> Shows the help screen.</p>
<dt><code>Filter options:</code></p>
<dd>
<dt><i>-d &lt;dmac&gt;</i></p>
<dd> MAC address of destination.</p>
<dt><i>-s &lt;smac&gt;</i></p>
<dd> MAC address of source.</p>
<dt><i>-m &lt;len&gt;</i></p>
<dd> Minimum packet length.</p>
<dt><i>-n &lt;len&gt;</i></p>
<dd> Maximum packet length.</p>
<dt><i>-t &lt;tods&gt;</i></p>
<dd> Frame control, &quot;To&quot; DS bit.</p>
<dt><i>-f &lt;fromds&gt;</i></p>
<dd> Frame control, &quot;From&quot; DS bit.</p>
<dt><i>-D </i></p>
<dd> Disable AP Detection.</dl>
<dl>
<dt><code>Replay options:</code></p>
<dd>
<dt><i>-x &lt;nbpps&gt;</i></p>
<dd> Number of packets per second.</p>
<dt><i>-p &lt;fctrl&gt;</i></p>
<dd> Set frame control word (hex).</p>
<dt><i>-a &lt;bssid&gt;</i></p>
<dd> Set Access Point MAC address.</p>
<dt><i>-c &lt;dmac&gt;</i></p>
<dd> Set destination MAC address.</p>
<dt><i>-h &lt;smac&gt;</i></p>
<dd> Set source MAC address.</p>
<dt><i>-F</i></p>
<dd> Choose first matching packet.</p>
<dt><i>-e &lt;essid&gt;</i></p>
<dd> Set target SSID.</dl>
<dl>
<dt><code>Debug options:</code></p>
<dd>
<dt><i>-K &lt;prga&gt;</i></p>
<dd> Keystream for continuation.</p>
<dt><i>-y &lt;file&gt;</i></p>
<dd> Keystream file for continuation.</p>
<dt><i>-j</i></p>
<dd> Inject FromFS packets.</p>
<dt><i>-P &lt;PMK&gt;</i></p>
<dd> Pairwise Master key (PMK) for verification or vulnerability testing.</p>
<dt><i>-p &lt;PSK&gt;</i></p>
<dd> Preshared key (PSK) to calculate PMK with essid.</dl>
<dl>
<dt><code>Source options:</code></p>
<dd>
<dt><i>-i &lt;iface&gt;</i></p>
<dd> Capture packets from this interface.</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd> Extract packets from this pcap file.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Thomas d&#8217;Otreppe. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airmon-ng/">airmon-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airodump-ng/">airodump-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airolib-ng/">airolib-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airserv-ng/">airserv-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airtun-ng/">airtun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-buddy-ng/">buddy-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-easside-ng/">easside-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-ivstools/">ivstools</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-kstats/">kstats</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-makeivs-ng/">makeivs-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-packetforge-ng/">packetforge-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
<h2>Index</h2>
