---
title: "rtmpsuck(1)"
name: "rtmpsuck"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rtmpsuck/"
description: "rtmpsuck – a transparent RTMP proxy"
---

<h2 class="name">NAME</h2>
<p> rtmpsuck &#8211; a transparent RTMP proxy </p>
<h2>SYNOPSIS</h2>
<p> <code>rtmpsuck</code> [<code>-z</code>] </p>
<h2>DESCRIPTION</h2>
<p> <code>rtmpsuck</code> is a transparent RTMP proxy. It listens on port 1935 for RTMP sessions, but you can also redirect other ports to it as needed. It first performs an RTMP handshake with the client, then waits for the client to send a connect request. It parses and prints the connect parameters, then makes an outbound connection to the real RTMP server. It performs an RTMP handshake with that server, forwards the connect request, and from that point on it just relays packets back and forth between the two endpoints.<br />
 It also checks for a few packets that it treats specially: a play packet from the client will get parsed so that the playpath can be displayed. It also handles SWF Verification requests from the server, without forwarding them to the client.<br />
 Once the play command is processed, all subsequent audio/video data received from the server will be written to a file, as well as being delivered back to the client.<br />
 The point of all this, instead of just using a sniffer, is that since <code>rtmpsuck</code> has performed real handshakes with both the client and the server, it can negotiate whatever encryption keys are needed and so record the unencrypted data.</p>
<h2>OPTIONS</h2>
<p> <code>-z</code> Debug level output. Extremely verbose.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-rtmpdump/">rtmpdump</a></code>(1)</p>
<h2>AUTHORS</h2>
<p> Andrej Stepanchuk, Howard Chu<br />
 &lt;<a rel="nofollow" href="http://rtmpdump.mplayerhq.hu">http://rtmpdump.mplayerhq.hu</a>&gt; </p>
<h2>Index</h2>
