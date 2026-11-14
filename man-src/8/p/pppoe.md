---
title: "pppoe(8)"
name: "pppoe"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe/"
description: "pppoe – user-space PPPoE client."
---

<p>pppoe &#8211; user-space PPPoE client.</p>
<h2>Synopsis</h2>
<p><code>pppd pty &#8216;pppoe </code>[<i>pppoe_options</i>]<code>&#8216; </code>[<i>pppd_options</i>] </p>
<p> <code>pppoe -A </code>[<i>pppoe_options</i>]</p>
<h2>Description</h2>
<p><code>pppoe</code> is a user-space client for PPPoE (Point-to-Point Protocol over Ethernet) for Linux and other UNIX systems. <code>pppoe</code> works in concert with the <code>pppd</code> PPP daemon to provide a PPP connection over Ethernet, as is used by many DSL service providers. </p>
<h2>Options</h2>
<dl>
<dt><code>-I </code><i>interface</i></p>
<dd>The <code>-I</code> option specifies the Ethernet interface to use. Under Linux, it is typically <i>eth0</i> or <i>eth1</i>. The interface should be &quot;up&quot; before you start <code>pppoe</code>, but should <i>not</i> be configured to have an IP address. </p>
<dt><code>-T </code><i>timeout</i></p>
<dd>The <code>-T</code> option causes <code>pppoe</code> to exit if no session traffic is detected for <i>timeout</i> seconds. I recommend that you use this option as an extra safety measure, but if you do, you should make sure that PPP generates enough traffic so the timeout will normally not be triggered. The best way to do this is to use the <i>lcp-echo-interval</i> option to <code>pppd</code>. You should set the PPPoE timeout to be about four times the LCP echo interval. </p>
<dt><code>-D </code><i>file_name</i></p>
<dd>The <code>-D</code> option causes every packet to be dumped to the specified <i>file_name</i>. This is intended for debugging only; it produces huge amounts of output and greatly reduces performance. </p>
<dt><code>-V</code></p>
<dd>The <code>-V</code> option causes <code>pppoe</code> to print its version number and exit. </p>
<dt><code>-A</code></p>
<dd>The <code>-A</code> option causes <code>pppoe</code> to send a PADI packet and then print the names of access concentrators in each PADO packet it receives. Do not use this option in conjunction with <code>pppd</code>; the <code>-A</code> option is meant to be used interactively to give interesting information about the access concentrator. </p>
<dt><code>-S </code><i>service_name</i></p>
<dd>Specifies the desired service name. <code>pppoe</code> will only initiate sessions with access concentrators which can provide the specified service. In most cases, you should <i>not</i> specify this option. Use it only if you know that there are multiple access concentrators or know that you need a specific service name. </p>
<dt><code>-C </code><i>ac_name</i></p>
<dd>Specifies the desired access concentrator name. <code>pppoe</code> will only initiate sessions with the specified access concentrator. In most cases, you should <i>not</i> specify this option. Use it only if you know that there are multiple access concentrators. If both the <code>-S</code> and <code>-C</code> options are specified, they must <i>both</i> match for <code>pppoe</code> to initiate a session. </p>
<dt><code>-U</code></p>
<dd>Causes <code>pppoe</code> to use the Host-Uniq tag in its discovery packets. This lets you run multiple <code>pppoe</code> daemons without having their discovery packets interfere with one another. You must supply this option to <i>all</i> <code>pppoe</code> daemons if you intend to run multiple daemons simultaneously. </p>
<dt><code>-s</code></p>
<dd>Causes <code>pppoe</code> to use <i>synchronous</i> PPP encapsulation. If you use this option, then you <i>must</i> use the <code>sync</code> option with <code>pppd</code>. You are encouraged to use this option if it works, because it greatly reduces the CPU overhead of <code>pppoe</code>. However, it MAY be unreliable on slow machines &#8212; there is a race condition between pppd writing data and pppoe reading it. For this reason, the default setting is asynchronous. If you encounter bugs or crashes with Synchronous PPP, turn it off &#8212; don&#8217;t e-mail me for support! </p>
<dt><code>-m </code><i>MSS</i></p>
<dd>Causes <code>pppoe</code> to <i>clamp</i> the TCP maximum segment size at the specified value. Because of PPPoE overhead, the maximum segment size for PPPoE is smaller than for normal Ethernet encapsulation. This could cause problems for machines on a LAN behind a gateway using PPPoE. If you have a LAN behind a gateway, and the gateway connects to the Internet using PPPoE, you are strongly recommended to use a <code>-m 1412</code> option. This avoids having to set the MTU on all the hosts on the LAN. </p>
<dt><code>-p </code><i>file</i></p>
<dd>Causes <code>pppoe</code> to write its process-ID to the specified file. This can be used to locate and kill <code>pppoe</code> processes. </p>
<dt><code>-e </code><i>sess:mac</i></p>
<dd>Causes <code>pppoe</code> to skip the discovery phase and move directly to the session phase. The session is given by <i>sess</i> and the MAC address of the peer by <i>mac</i>. This mode is <i>not</i> meant for normal use; it is designed only for <code><a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a></code>(8). </p>
<dt><code>-n</code></p>
<dd>Causes <code>pppoe</code> not to open a discovery socket. This mode is <i>not</i> meant for normal use; it is designed only for <code><a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a></code>(8). </p>
<dt><code>-k</code></p>
<dd>Causes <code>pppoe</code> to terminate an existing session by sending a PADT frame, and then exit. You must use the <code>-e</code> option in conjunction with this option to specify the session to kill. This may be useful for killing sessions when a buggy peer does not realize the session has ended. </p>
<dt><code>-d</code></p>
<dd>Causes <code>pppoe</code> to perform discovery and then exit, after printing session information to standard output. The session information is printed in exactly the format expected by the <code>-e</code> option. This option lets you initiate a PPPoE discovery, perform some other work, and then start the actual PPP session. <i>Be careful</i>; if you use this option in a loop, you can create many sessions, which may annoy your peer. </p>
<dt><code>-f disc:sess</code></p>
<dd>The <code>-f</code> option sets the Ethernet frame types for PPPoE discovery and session frames. The types are specified as hexadecimal numbers separated by a colon. Standard PPPoE uses frame types 8863:8864. <i>You should not use this option</i> unless you are absolutely sure the peer you are dealing with uses non-standard frame types. If your ISP uses non-standard frame types, complain! </p>
<dt><code>-h</code></p>
<dd>The <code>-h</code> option causes <code>pppoe</code> to print usage information and exit. </p>
</dl>
<h2>Pppoe Background</h2>
<p>PPPoE (Point-to-Point Protocol over Ethernet) is described in RFC 2516 and is a protocol which allows the session abstraction to be maintained over bridged Ethernet networks. </p>
<p> PPPoE works by encapsulating PPP frames in Ethernet frames. The protocol has two distinct stages: The <i>discovery</i> and the <i>session</i> stage. </p>
<p> In the discovery stage, the host broadcasts a special PADI (PPPoE Active Discovery Initiation) frame to discover any <i>access concentrators</i>. The access concentrators (typically, only one access concentrator) reply with PADO (PPPoE Active Discovery Offer) packets, announcing their presence and the services they offer. The host picks one of the access concentrators and transmits a PADR (PPPoE Active Discovery Request) packet, asking for a session. The access concentrator replies with a PADS (PPPoE Active Discovery Session-Confirmation) packet. The protocol then moves to the session stage. </p>
<p> In the session stage, the host and access concentrator exchange PPP frames embedded in Ethernet frames. The normal Ethernet MTU is 1500 bytes, but the PPPoE overhead plus two bytes of overhead for the encapsulated PPP frame mean that the MTU of the PPP interface is at most 1492 bytes. This causes <i>all kinds of problems</i> if you are using a Linux machine as a firewall and interfaces behind the firewall have an MTU greater than 1492. In fact, to be safe, I recommend setting the MTU of machines behind the firewall to 1412, to allow for worst-case TCP and IP options in their respective headers. </p>
<p> Normally, PPP uses the Link Control Protocol (LCP) to shut down a PPP link. However, the PPPoE specification allows the link to be shut down with a special PADT (PPPoE Active Discovery Terminate) packet. This client recognizes this packet and will correctly terminate if a terminate request is received for the PPP session.</p>
<h2>Design Goals</h2>
<p>My design goals for this PPPoE client were as follows, in descending order of importance: </p>
<dl>
<dt><code>o</code></p>
<dd>It must work. </p>
<dt><code>o</code></p>
<dd>It must be a user-space program and not a kernel patch. </p>
<dt><code>o</code></p>
<dd>The code must be easy to read and maintain. </p>
<dt><code>o</code></p>
<dd>It must be fully compliant with RFC 2516, the proposed PPPoE standard. </p>
<dt><code>o</code></p>
<dd>It must never hang up forever &#8212; if the connection is broken, it must detect this and exit, allowing a wrapper script to restart the connection. </p>
<dt><code>o</code></p>
<dd>It must be fairly efficient. </p>
</dl>
<p> I believe I have achieved all of these goals, but (of course) am open to suggestions, patches and ideas. See my home page, <a rel="nofollow" href="http://www.roaringpenguin.com,">http://www.roaringpenguin.com,</a> for contact information.</p>
<h2>Notes</h2>
<p>For best results, you must give <code>pppd</code> an mtu option of 1492. I have observed problems with excessively-large frames unless I set this option. Also, if <code>pppoe</code> is running on a firewall machine, all machines behind the firewall should have MTU&#8217;s of 1412. If you have problems, check your system logs. <code>pppoe</code> logs interesting things to syslog. You may have to turn on logging of <i>debug</i>-level messages for complete diagnosis. </p>
<h2>Authors</h2>
<p><code>pppoe</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;, with much inspiration from an earlier version by Luke Stras. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8), <a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a>(8), <a href="/docs/linux/man/8-pppoe-relay/">pppoe-relay</a>(8) </p>
