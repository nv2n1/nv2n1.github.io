---
title: "jack_netsource(1)"
name: "jack_netsource"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_netsource/"
description: "jack_netsource – Netjack Master client for one slave"
---

<h2>NAME</h2>
<p> jack_netsource &#8211; Netjack Master client for one slave</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_netsource</code> [ <i>-H</i> hostname ] [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>jack_netsource</code> The Master side of a netjack connection. Represents the slave jackd -dnet in the master jack graph. Most connection parameters are configured via the netsource, and the slave will set itself up according to the commandline option given to jack_netsource.<br />
 Netjack allows low latency audio connections over general IP networks. When using celt for compression, it is even possible to establish transatlantic links, with latencies not much over the actual ping time.<br />
 But the main usecase is of course a LAN, where it can achieve one jack period of latency. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> this help text</p>
<dd>
<dt><code>-H</code> <i>slave host</i></p>
<dd>
 Host name of the slave JACK</p>
<dt><code>-o</code> <i>num channels</i></p>
<dd>
 Number of audio playback channels</p>
<dt><code>-i</code> <i>num channels</i></p>
<dd>
 Number of audio capture channels</p>
<dt><code>-O</code> <i>num channels</i></p>
<dd>
 Number of midi playback channels</p>
<dt><code>-I</code> <i>num channels</i></p>
<dd>
 Number of midi capture channels</p>
<dt><code>-n</code> <i>periods</i></p>
<dd>
 Network latency in JACK periods</p>
<dt><code>-p</code> <i>port</i></p>
<dd>
 UDP port that the slave is listening on</p>
<dt><code>-r</code> <i>reply port</i></p>
<dd>
 UDP port that we are listening on</p>
<dt><code>-B</code> <i>bind port</i></p>
<dd>
 reply port, for use in NAT environments</p>
<dt><code>-b</code> <i>bitdepth</i></p>
<dd>
 Set transport to use 16bit or 8bit</p>
<dt><code>-c</code> <i>bytes</i></p>
<dd>
 Use CELT encoding with &lt;bytes&gt; per period and channel</p>
<dt><code>-m</code> <i>mtu</i></p>
<dd>
 Assume this mtu for the link</p>
<dt><code>-R</code> <i>N</i></p>
<dd>
 Redundancy: send out packets N times.</p>
<dt><code>-e</code></p>
<dd>
 skip host-to-network endianness conversion</p>
<dt><code>-N</code> <i>jack name</i></p>
<dd>
 Reports a different client name to jack</p>
<dt>
<dt><code>-s</code>, <code>&#8211;server</code> <i>servername</i></p>
<dd>
<dd>
 Connect to the jack server named <i>servername</i></p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
 Display help/usage message</p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd>
 Output version information and exit </p>
</dl>
<h2>EXAMPLES</h2>
<p> run a 4 audio channel bidirectional link with one period of latency and no midi channels. Audio data is flowing uncompressed over the wire:<br />
 On <i>hostA</i>:</p>
<dl>
<dt>
<dd> <code>jackd -d alsa </code><br />
 <code>jack_netsource -H hostB -n1 -i4 -o4 -I0 -O0 </code></dl>
<p> On <i>hostB</i>:</p>
<dl>
<dt>
<dd> <code>jackd -d net </code> </p>
</dl>
<h2>Index</h2>
