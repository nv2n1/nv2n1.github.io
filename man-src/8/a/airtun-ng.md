---
title: "airtun-ng(8)"
name: "airtun-ng"
section: "8"
letter: "a"
url: "/docs/linux/man/8-airtun-ng/"
description: "airtun-ng – a virtual tunnel interface creator for aircrack-ng"
---

<p>airtun-ng &#8211; a virtual tunnel interface creator for aircrack-ng</p>
<h2>Synopsis</h2>
<p><code>airtun-ng</code> [options] &lt;interface name&gt;</p>
<h2>Description</h2>
<p><code>airtun-ng</code> creates a virtual tunnel interface (atX) for sending arbitrary IP packets by using raw ieee802.11 packet injection.</p>
<h2>Options</h2>
<dl>
<dt><i>-H, &#8211;help</i></p>
<dd>Shows the help screen.</p>
<dt><i>-x &lt;pps&gt;</i></p>
<dd>Sets maximum number of packets per second.</p>
<dt><i>-a &lt;BSSID&gt;</i></p>
<dd>Specifies the BSSID for the iee802.11 header. In WDS Mode this sets the Receiver.</p>
<dt><i>-h &lt;SMAC&gt;</i></p>
<dd>Specifies the source MAC for the iee802.11 header.</p>
<dt><i>-i &lt;iface&gt;</i></p>
<dd>Sets the capture interface.</p>
<dt><i>-r &lt;file&gt;</i></p>
<dd>Specifies a file to read 802.11 frames.</p>
<dt><i>-y &lt;PRGA-file&gt;</i></p>
<dd>Is the name of the file, which provides the keystream for WEP encoding. (No receiving, just transmitting of IP packets.)</p>
<dt><i>-w &lt;WEP-key&gt;</i></p>
<dd>This is the WEP key to en-/decrypt all traffic going through the tunnel.</p>
<dt><i>-t &lt;tods&gt;</i></p>
<dd>Defines the ToDS and FromDS bit in the ieee802.11 header. For tods=1, the ToDS bit is set to 1 and FromDS to 0, while tods=0 sets them the other way around. If set to 2, it will be tunneled in a WDS/bridge.</p>
<dt><i>-m &lt;netmask&gt;, &#8211;netmask &lt;netmask&gt;</i></p>
<dd>Filters networks based on bssid ^ netmask combination. Needs -d, used in replay mode.</p>
<dt><i>-d &lt;BSSID&gt;, &#8211;bssid &lt;BSSID&gt;</i></p>
<dd>Filters networks based on the &lt;BSSID&gt;. Used in replay mode.</p>
<dt><i>-f, &#8211;repeat</i></p>
<dd>Enables replay mode. All read frames, filtered by bssid and netmask (if specified), will be replayed.</p>
<dt><i>-s &lt;transmitter&gt;</i></p>
<dd>Set Transmitter MAC address for WDS Mode.</p>
<dt><i>-b</i></p>
<dd>Bidirectional mode. This enables communication in Transmitter&#8217;s AND Receiver&#8217;s networks. Works only if you can see both stations.</dl>
<h2>Examples</h2>
<p><code>airtun-ng</code> -a 00:14:22:56:F3:4E -t 0 -y keystream.xor wlan0 </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airmon-ng/">airmon-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng/">airodump-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airodump-ng-oui-update/">airodump-ng-oui-update</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-airserv-ng/">airserv-ng</a>(8)</code><br />
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
