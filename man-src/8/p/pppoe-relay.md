---
title: "pppoe-relay(8)"
name: "pppoe-relay"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pppoe-relay/"
description: "pppoe-relay – user-space PPPoE relay agent."
---

<p>pppoe-relay &#8211; user-space PPPoE relay agent.</p>
<h2>Synopsis</h2>
<p><code>pppoe-relay </code>[<i>options</i>] </p>
<h2>Description</h2>
<p><code>pppoe-relay</code> is a user-space relay agent for PPPoE (Point-to-Point Protocol over Ethernet) for Linux. <code>pppoe-relay</code> works in concert with the <code>pppoe</code> client and <code>pppoe-server</code> server. See the OPERATION section later in this manual for details on how <code>pppoe-relay</code> works. </p>
<h2>Options</h2>
<dl>
<dt><code>-S </code><i>interface</i></p>
<dd>Adds the Ethernet interface <i>interface</i> to the list of interfaces managed by <code>pppoe-relay</code>. Only PPPoE servers may be connected to this interface. </p>
<dt><code>-C </code><i>interface</i></p>
<dd>Adds the Ethernet interface <i>interface</i> to the list of interfaces managed by <code>pppoe-relay</code>. Only PPPoE clients may be connected to this interface. </p>
<dt><code>-B </code><i>interface</i></p>
<dd>Adds the Ethernet interface <i>interface</i> to the list of interfaces managed by <code>pppoe-relay</code>. Both PPPoE clients and servers may be connected to this interface. </p>
<dt><code>-n </code><i>num</i></p>
<dd>Allows at most <i>num</i> concurrent PPPoE sessions. If not specified, the default is 5000. <i>num</i> can range from 1 to 65534. </p>
<dt><code>-i </code><i>timeout</i></p>
<dd>Specifies the session idle timeout. If both peers in a session are idle for more than <i>timeout</i> seconds, the session is terminated. If <i>timeout</i> is specified as zero, sessions will never be terminated because of idleness. </p>
<p> Note that the idle-session expiry routine is never run more frequently than every 30 seconds, so the timeout is approximate. The default value for <i>timeout</i> is 600 seconds (10 minutes.) </p>
<dt><code>-F</code></p>
<dd>The <code>-F</code> option causes <code>pppoe-relay</code> <i>not</i> to fork into the background; instead, it remains in the foreground. </p>
<dt><code>-h</code></p>
<dd>The <code>-h</code> option prints a brief usage message and exits. </p>
</dl>
<h2>Operation</h2>
<p><code>pppoe-relay</code> listens for incoming PPPoE PADI frames on all interfaces specified with <code>-B</code> or <code>-C</code> options. When a PADI frame appears, <code>pppoe-relay</code> adds a Relay-Session-ID tag and broadcasts the PADI on all interfaces specified with <code>-B</code> or <code>-S</code> options (except the interface on which the frame arrived.) </p>
<p> Any PADO frames received are relayed back to the client which sent the PADI (assuming they contain valid Relay-Session-ID tags.) Likewise, PADR frames from clients are relayed back to the matching access concentrator. </p>
<p> When a PADS frame is received, <code>pppoe-relay</code> enters the two peers&#8217; MAC addresses and session-ID&#8217;s into a hash table. (The session-ID seen by the access concentrator may be different from that seen by the client; <code>pppoe-relay</code> must renumber sessions to avoid the possibility of duplicate session-ID&#8217;s.) Whenever either peer sends a session frame, <code>pppoe-relay</code> looks up the session entry in the hash table and relays the frame to the correct peer. </p>
<p> When a PADT frame is received, <code>pppoe-relay</code> relays it to the peer and deletes the session entry from its hash table. </p>
<p> If a client and server crash (or frames are lost), PADT frames may never be sent, and <code>pppoe-relay</code>&#8216;s hash table can fill up with stale sessions. Therefore, a session-cleaning routine runs periodically, and removes old sessions from the hash table. A session is considered &quot;old&quot; if no traffic has been seen within <i>timeout</i> seconds. When a session is deleted because of a timeout, a PADT frame is sent to each peer to make certain that they are aware the session has been killed.</p>
<h2>Example Invocations</h2>
<pre>pppoe-relay -C eth0 -S eth1</pre>
<p>The example above relays frames between PPPoE clients on the eth0 network and PPPoE servers on the eth1 network. </p>
<pre>pppoe-relay -B eth0 -B eth1</pre>
<p>This example is a transparent relay &#8212; frames are relayed between any mix of clients and servers on the eth0 and eth1 networks. </p>
<pre>pppoe-relay -S eth0 -C eth1 -C eth2 -C eth3</pre>
<p>This example relays frames between servers on the eth0 network and clients on the eth1, eth2 and eth3 networks.</p>
<h2>Authors</h2>
<p><code>pppoe-relay</code> was written by David F. Skoll &lt;dfs [at] roaringpenguin.com&gt;. </p>
<p> The <code>pppoe</code> home page is <i><a rel="nofollow" href="http://www.roaringpenguin.com/pppoe/">http://www.roaringpenguin.com/pppoe/</a></i>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-pppoe-start/">pppoe-start</a>(8), <a href="/docs/linux/man/8-pppoe-stop/">pppoe-stop</a>(8), <a href="/docs/linux/man/8-pppoe-connect/">pppoe-connect</a>(8), <a href="/docs/linux/man/8-pppd/">pppd</a>(8), <a href="/docs/linux/man/5-pppoe-conf/">pppoe.conf</a>(5), <a href="/docs/linux/man/8-pppoe/">pppoe</a>(8), <a href="/docs/linux/man/8-pppoe-setup/">pppoe-setup</a>(8), <a href="/docs/linux/man/8-pppoe-status/">pppoe-status</a>(8), <a href="/docs/linux/man/8-pppoe-sniff/">pppoe-sniff</a>(8), <a href="/docs/linux/man/8-pppoe-server/">pppoe-server</a>(8) </p>
