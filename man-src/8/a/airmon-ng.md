---
title: "airmon-ng(8)"
name: "airmon-ng"
section: "8"
letter: "a"
url: "/docs/linux/man/8-airmon-ng/"
description: "airmon-ng – bash script designed to turn wireless cards into monitor mode."
---

<p>airmon-ng &#8211; bash script designed to turn wireless cards into monitor mode.</p>
<h2>Synopsis</h2>
<p><code>airmon-ng</code> &lt;start|stop&gt; &lt;interface&gt; [channel] <code>airmon-ng</code> &lt;check&gt; [kill]</p>
<h2>Description</h2>
<p><code>airmon-ng</code> is script can be used to enable monitor mode on wireless interfaces. It may also be used to go back from monitor mode to managed mode. Entering the airmon-ng command without parameters will show the interfaces status. It can list/kill programs that can interfere with the wireless card and set the right sources in /etc/kismet/kismet.conf too.</p>
<h2>Optional Parameters</h2>
<dl>
<dt><i>start &lt;interface&gt; [channel]</i></p>
<dd>Enable monitor mode on an interface (and specify a channel). Note: Madwifi-ng is a special case, &#8216;start&#8217; has to be used on wifi interfaces and &#8216;stop&#8217; on ath interfaces. <i>stop &lt;interface&gt;</i> Disable monitor mode and go back to managed mode (except for madwifi-ng where it kills the ath VAP).</p>
<dt><i>check [kill]</i></p>
<dd>List all possible programs that could interfere with the wireless card. If &#8216;kill&#8217; is specified, it will try to kill all of them.</dl>
<h2>Author</h2>
<p>This manual page was written by Adam Cecile &lt;gandalf [at] le-vert.net&gt; for the Debian system (but may be used by others). And modified to fit airmon-ng by David Francos Cuartero &lt;xayon [at] xayon.net&gt;. Permission is granted to copy, distribute and/or modify this document under the terms of the GNU General Public License, Version 2 or any later version published by the Free Software Foundation On Debian systems, the complete text of the GNU General Public License can be found in /usr/share/common-licenses/GPL.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-airbase-ng/">airbase-ng</a>(8)</code><br />
 <code><a href="/docs/linux/man/8-aireplay-ng/">aireplay-ng</a>(8)</code><br />
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
