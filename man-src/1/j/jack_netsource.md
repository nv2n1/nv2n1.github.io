---

title: "jack_netsource(1)"
name: "jack_netsource"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jack_netsource/"
description: "jack_netsource – Netjack Master client for one slave"
---

<p> jack_netsource &#8211; Netjack Master client for one slave</p>
<h2>SYNOPSIS</h2>
<p> <code>jack_netsource</code> [ <i>-H</i> hostname ] [ <i>options</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>jack_netsource</code> The Master side of a netjack connection. Represents the slave jackd -dnet in the master jack graph. Most connection parameters are configured via the netsource, and the slave will set itself up according to the commandline option given to jack_netsource.<br />
 Netjack allows low latency audio connections over general IP networks. When using celt for compression, it is even possible to establish transatlantic links, with latencies not much over the actual ping time.<br />
 But the main usecase is of course a LAN, where it can achieve one jack period of latency. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code> this help text</dt>
<dd>
</dd><dt><code>-H</code> <i>slave host</i></dt>
<dd>
 Host name of the slave JACK</dd>
<dt><code>-o</code> <i>num channels</i></dt>
<dd>
 Number of audio playback channels</dd>
<dt><code>-i</code> <i>num channels</i></dt>
<dd>
 Number of audio capture channels</dd>
<dt><code>-O</code> <i>num channels</i></dt>
<dd>
 Number of midi playback channels</dd>
<dt><code>-I</code> <i>num channels</i></dt>
<dd>
 Number of midi capture channels</dd>
<dt><code>-n</code> <i>periods</i></dt>
<dd>
 Network latency in JACK periods</dd>
<dt><code>-p</code> <i>port</i></dt>
<dd>
 UDP port that the slave is listening on</dd>
<dt><code>-r</code> <i>reply port</i></dt>
<dd>
 UDP port that we are listening on</dd>
<dt><code>-B</code> <i>bind port</i></dt>
<dd>
 reply port, for use in NAT environments</dd>
<dt><code>-b</code> <i>bitdepth</i></dt>
<dd>
 Set transport to use 16bit or 8bit</dd>
<dt><code>-c</code> <i>bytes</i></dt>
<dd>
 Use CELT encoding with &lt;bytes&gt; per period and channel</dd>
<dt><code>-m</code> <i>mtu</i></dt>
<dd>
 Assume this mtu for the link</dd>
<dt><code>-R</code> <i>N</i></dt>
<dd>
 Redundancy: send out packets N times.</dd>
<dt><code>-e</code></dt>
<dd>
 skip host-to-network endianness conversion</dd>
<dt><code>-N</code> <i>jack name</i></dt>
<dd>
 Reports a different client name to jack</dd>
<dt>
</dt><dt><code>-s</code>, <code>&#8211;server</code> <i>servername</i></dt>
<dd>
</dd><dd>
 Connect to the jack server named <i>servername</i></dd>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>
 Display help/usage message</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>
 Output version information and exit </dd>
</dl>
<h2>EXAMPLES</h2>
<p> run a 4 audio channel bidirectional link with one period of latency and no midi channels. Audio data is flowing uncompressed over the wire:<br />
 On <i>hostA</i>:</p>
<dl>
<dt>
</dt><dd> <code>jackd -d alsa </code><br />
 <code>jack_netsource -H hostB -n1 -i4 -o4 -I0 -O0 </code></dd></dl>
<p> On <i>hostB</i>:</p>
<dl>
<dt>
</dt><dd> <code>jackd -d net </code> </dd>
</dl>
