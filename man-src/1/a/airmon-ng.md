---
title: "airmon-ng(1)"
name: "airmon-ng"
section: "1"
letter: "a"
url: "/docs/linux/man/1-airmon-ng/"
description: "airmon-ng – bash script designed to turn wireless cards into monitor mode."
---

<h2 class="name">NAME</h2>
<p> airmon-ng &#8211; bash script designed to turn wireless cards into monitor mode. </p>
<h2>SYNOPSIS</h2>
<p> <code>airmon-ng</code> &lt;start|stop&gt; &lt;interface&gt; [channel] <code>airmon-ng</code> &lt;check&gt; [kill]</p>
<h2>DESCRIPTION</h2>
<p> <code>airmon-ng</code> is script can be used to enable monitor mode on wireless interfaces. It may also be used to go back from monitor mode to managed mode. Entering the airmon-ng command without parameters will show the interfaces status. It can list/kill programs that can interfere with the wireless card and set the right sources in /etc/kismet/kismet.conf too.</p>
<h2>OPTIONAL PARAMETERS</h2>
<dl>
<dt><i>start &lt;interface&gt; [channel]</i></p>
<dd> Enable monitor mode on an interface (and specify a channel). Note: Madwifi-ng is a special case, &#8216;start&#8217; has to be used on wifi interfaces and &#8216;stop&#8217; on ath interfaces. <i>stop &lt;interface&gt;</i> Disable monitor mode and go back to managed mode (except for madwifi-ng where it kills the ath VAP).</p>
<dt><i>check [kill]</i></p>
<dd> List all possible programs that could interfere with the wireless card. If &#8216;kill&#8217; is specified, it will try to kill all of them.</dl>
<h2>AUTHOR</h2>
<p> This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-airbase-ng/">airbase-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aircrack-ng/">aircrack-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecap-ng/">airdecap-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdecloak-ng/">airdecloak-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-airdriver-ng/">airdriver-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-aireplay-ng/">aireplay-ng</a>(1)</code><br />
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
 <code><a href="/docs/linux/man/1-tkiptun-ng/">tkiptun-ng</a>(1)</code><br />
 <code><a href="/docs/linux/man/1-wesside-ng/">wesside-ng</a>(1)</code> </p>
<h2>Index</h2>
