---
title: "udp-receiver(1)"
name: "udp-receiver"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udp-receiver/"
description: "udp-receiver – receive files broadcast by udp-sender"
---

<h2 class="name">NAME</h2>
<p> udp-receiver &#8211; receive files broadcast by udp-sender </p>
<h2>SYNOPSIS</h2>
<p> ./udp-receiver [&#8211;file <i>file</i>] [&#8211;pipe <i>pipe</i>] [&#8211;portbase <i>portbase</i>] [&#8211;interface <i>net-interface</i>] [&#8211;log <i>file</i>] [&#8211;ttl <i>time-to-live</i>] [&#8211;mcast-rdv-address <i>mcast-rdv-address</i>] [&#8211;nokbd] [&#8211;exitWait milliseconds] [&#8211;stat-period <i>n</i>] [&#8211;print-uncompressed-position <i>flag</i>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;Udp-receiver&quot;</tt> is used to receive files sent by <tt>&quot;udp-sender&quot;</tt> (for instance a disk image).</p>
<h2>OPTIONS</h2>
<h3>Basic options</h3>
<dl>
<dt>&#8211;file <i>file</i></p>
<dd> Writes received data to <i>file</i>. If this parameter is not supplied, received data is written to stdout instead.</p>
<dt>&#8211;pipe <i>command</i></p>
<dd> Sends data through <i>pipe</i> after receiving it. This is useful for decompressing the data, or for filling in unused filesystem blocks that may have been stripped out by udp-sender. The <i>command</i> gets a direct handle on the output file or device, and thus may seek inside it, if needed. <tt>&quot;Udpcast&quot;</tt> itself also keeps a handle on the file, which is used for an informational progress display. The <i>command</i>&#8216;s stdin is a pipe from udp-receiver. Example: <tt>&quot;udp-receiver -p &quot;gzip -dc&quot;&quot;</tt></p>
<dt>&#8211;log <i>file</i></p>
<dd> Logs some stuff into <i>file</i>.</p>
<dt>&#8211;nosync</p>
<dd> Do not open target in synchronous mode. This is the default when writing to a file or a pipe.</p>
<dt>&#8211;sync</p>
<dd> Write to target in synchronous mode. This is the default when writing to a device (character or block)</p>
<dt>&#8211;nokbd</p>
<dd> Do not read start signal from keyboard, and do not display any message telling the user to press any key to start.</p>
<dt>&#8211;start-timeout <i>sec</i></p>
<dd> receiver aborts at start if it doesn&#8217;t see a sender within this many seconds. Furthermore, the sender needs to start transmission of data within this delay. Once transmission is started, the timeout no longer applies.</p>
<dt>&#8211;receive-timeout <i>sec</i></p>
<dd> receiver aborts during transmission if it doesn&#8217;t see a packet from the sender within this many seconds. This timeout only applies once transmission has started.</dl>
<h3>Networking options</h3>
<dl>
<dt>&#8211;portbase <i>portbase</i></p>
<dd> Default ports to use for udpcast. Two ports are used: <i>portbase</i> and <i>portbase+1</i> . Thus, <i>Portbase</i> must be even. Default is <tt>9000</tt>. The same <i>portbase</i> must be specified for both <tt>&quot;udp-sender&quot;</tt> and <tt>&quot;udp-receiver&quot;</tt>.</p>
<dt>&#8211;interface <i>interface</i></p>
<dd> Network interface used to send out the data. Default is <tt>&quot;eth0&quot;</tt></p>
<dt>&#8211;ttl <i>ttl</i></p>
<dd> Time to live for connection request packet (by default connection request is broadcast to the <font SIZE="-1">LAN</font>&#8216;s broadcast address. If ttl is set, the connection request is multicast instead to <tt>224.0.0.1</tt> with the given ttl, which should enable udpcast to work between LANs. Not tested though.</p>
<dt>&#8211;mcast-rdv-address <i>address</i></p>
<dd> Uses a non-standard multicast address for the control connection (which is used by the sender and receivers to &#8220;find&#8221; each other). This is <code>not</code> the address that is used to transfer the data. By default <tt>&quot;mcast-rdv-address&quot;</tt> is the Ethernet broadcast address if <tt>&quot;ttl&quot;</tt> is 1, and <tt>224.0.0.1</tt> otherwise. This setting should not be used except in very special situations, such as when <tt>224.0.0.1</tt> cannot be used for policy reasons.</p>
<dt>&#8211;exit-wait <i>milliseconds</i></p>
<dd> When transmission is over, receiver will wait for this time after receiving the final <font SIZE="-1">REQACK.</font> This is done in order to guard against loss of the final <font SIZE="-1">ACK.</font> Is 500 milliseconds by default.</p>
<dt>&#8211;ignore-lost-data</p>
<dd> Do not stop reception when data loss is detected, but instead fill with random data. This is useful for multimedia transmission where 100% integrity is not need.</dl>
<h3>Statistics options</h3>
<dl>
<dt>&#8211;stat-period <i>seconds</i></p>
<dd> Every so much milliseconds, print some statistics to stderr: how much bytes received so far log, position in uncompressed file (if applicable), overall bitrate&#8230; By default, this is printed every half second.</p>
<dt>&#8211;print-uncompressed-position <i>flag</i></p>
<dd> By default, udp-receiver only prints the position in uncompressed file if the 2 following conditions are met:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Output is piped via a compressor (<tt>&quot;-p &quot;</tt> option).</p>
<dt>&bull;</p>
<dd> The final output is seekable (file or device)</dl>
</dl>
<dl>
<dt>
<dd>
<p> With the <tt>&quot;--print-uncompressed-position&quot;</tt>, options, you can change this behavior:</p>
<dl>
<dt>&bull;</p>
<dd> If flag is 0, uncompressed position will <code>never</code> be printed, even if above conditions are met</p>
<dt>&bull;</p>
<dd> If flag is 1, uncompressed position will <code>always</code> be printed, even if above conditions are <code>not</code> met</dl>
</dl>
<dl>
<dt>
<dd></dl>
</dl>
<h2>SEE ALSO</h2>
<p> udp-sender</p>
<h2>AUTHOR</h2>
<p> Alain Knaff </p>
<h2>Index</h2>
