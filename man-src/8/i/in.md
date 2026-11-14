---
title: "in(8)"
name: "in"
section: "8"
letter: "i"
url: "/docs/linux/man/8-in/"
description: "fingerd – remote user information server"
---

<p><code>fingerd</code> &#8211; remote user information server</p>
<h2>Synopsis</h2>
<p><code>fingerd</code> [-<code>wulf</code> ] [-<code>pL </code><i>path</i> ] [-<code>t </code><i>timeout</i> ]</p>
<h2>Description</h2>
<p><code>Fingerd</code> is a simple daemon based on <i>RFC1196</i> that provides an interface to the &#8220;finger&#8221; program at most network sites. The program is supposed to return a friendly, human-oriented status report on either the system at the moment or a particular person in depth. </p>
<p> If the &#8211;<code>w</code> option is given, remote users will get an additional &#8220;Welcome to &#8230;&#8221; banner which also shows some informations (e.g. uptime, operating system name and release) about the system the <code>fingerd</code> is running on. Some sites may consider this a security risk as it gives out information that may be useful to crackers. </p>
<p> If the &#8211;<code>u</code> option is given, requests of the form &#8220;finger @host&#8221; are rejected. </p>
<p> If the &#8211;<code>l</code> option is given, information about requests made is logged. This option probably violates users&#8217; privacy and should not be used on multiuser boxes. </p>
<p> If the &#8211;<code>f</code> option is given, finger forwarding (user [at] host1@host2) is allowed. Useful behind firewalls, but probably not wise for security and resource reasons. </p>
<p> The &#8211;<code>p</code> option allows specification of an alternate location for fingerd to find the &#8220;finger&#8221; program. The &#8211;<code>L</code> option is equivalent. </p>
<p> The &#8211;<code>t</code> option specifies the time to wait for a request before closing the connection. A value of 0 waits forever. The default is 60 seconds. </p>
<p> Options to fingerd should be specified in /etc/xinetd.d/finger </p>
<p> The finger protocol consists mostly of specifying command arguments. The <a href="/docs/linux/man/8-xinetd/">xinetd</a>(8) &#8220;super-server&#8221; runs <code>fingerd</code> for <code>TCP</code> requests received on port 79. Once connected <code>fingerd</code> reads a single command line terminated by a Aq Tn CRLF which is passed to <a href="/docs/linux/man/1-finger/">finger</a>(1). It closes its connections as soon as all output is finished. </p>
<p> If the line is empty (i.e. just a Aq Tn CRLF is sent) then finger returns a &#8220;default&#8221; report that lists all people logged into the system at that moment. This feature is blocked by the &#8211;<code>u</code> option. </p>
<p> If a user name is specified (e.g. eric Aq <code>CRLF</code> then the response lists more extended information for only that particular user, whether logged in or not. Allowable &#8220;names&#8221; in the command line include both &#8220;login names&#8221; and &#8220;user names&#8221; If a name is ambiguous, all possible derivations are returned.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-finger/">finger</a>(1), <a href="/docs/linux/man/8-xinetd/">xinetd</a>(8)</p>
<h2>Restrictions</h2>
<p>Connecting directly to the server from a <code>TIP</code> or an equally narrow-minded <code>TELNET -protocol</code> user program can result in meaningless attempts at option negotiation being sent to the server, which will foul up the command line interpretation.</p>
<h2>History</h2>
<p>The finger daemon appeared in BSD 4.3</p>
