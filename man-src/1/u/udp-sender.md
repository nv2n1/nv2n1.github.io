---
title: "udp-sender(1)"
name: "udp-sender"
section: "1"
letter: "u"
url: "/docs/linux/man/1-udp-sender/"
description: "udp-sender – broadcast file on a LAN"
---

<h2 class="name">NAME</h2>
<p> udp-sender &#8211; broadcast file on a LAN </p>
<h2>SYNOPSIS</h2>
<p> udp-sender [&#8211;file <i>file</i>] [&#8211;full-duplex] [&#8211;half-duplex] [&#8211;pipe <i>pipe</i>] [&#8211;portbase <i>portbase</i>] [&#8211;blocksize <i>size</i>] [&#8211;interface <i>net-interface</i>] [&#8211;mcast-data-address <i>data-mcast-address</i>] [&#8211;mcast-rdv-address <i>mcast-rdv-address</i>] [&#8211;max-bitrate <i>bitrate</i>] [&#8211;pointopoint] [&#8211;async] [&#8211;log <i>file</i>] [&#8211;min-slice-size <i>min</i>] [&#8211;max-slice-size <i>max</i>] [&#8211;slice-size] [&#8211;ttl <i>time-to-live</i>] [&#8211;fec <i>stripes</i>x<i>redundancy</i>/<i>stripesize</i>] [&#8211;print-seed] [&#8211;rexmit-hello-interval <i>interval</i>] [&#8211;autostart <i>autostart</i>] [&#8211;broadcast] [&#8211;min-receivers receivers] [&#8211;min-wait <i>sec</i>] [&#8211;max-wait <i>sec</i>] [&#8211;nokbd] [&#8211;retries-until-drop <i>n</i>] [&#8211;bw-period <i>n</i>] [&#8211;rate-governor <i>module.so:key1=value1,key2=value2</i>] [&#8211;stat-period <i>n</i>] [&#8211;print-uncompressed-position <i>flag</i>]</p>
<h2>DESCRIPTION</h2>
<p> <tt>&quot;Udp-sender&quot;</tt> is used to broadcast a file (for instance a disk image) to multiple <tt>&quot;udp-receivers&quot;</tt> on the local <font SIZE="-1">LAN.</font> In order to do this, it uses Ethernet multicast or broadcast, so that all receivers profit from the same physical datastream. Thus, sending to 10 destinations does not take more time than it would take to send just 2.</p>
<h2>OPTIONS</h2>
<h3>Basic options</h3>
<dl>
<dt>&#8211;file <i>file</i></p>
<dd> Reads data to be transmitted from <i>file</i>. If this parameter is not supplied, data to be transmitted is read from stdin instead.</p>
<dt>&#8211;pipe <i>command</i></p>
<dd> Sends data through <i>pipe</i> before transmitting it. This is useful for compressing/decompressing it, or for stripping out unused blocks. The <i>command</i> gets a direct handle on the input file or device, and thus may seek inside it, if needed. <tt>&quot;Udpcast&quot;</tt> itself also keeps a handle on the file, which is used for an informal progress display. The <i>command</i>&#8216;s stdout is a pipe to udpcast.</p>
<dt>&#8211;autostart <i>n</i></p>
<dd> Starts transmission after <i>n</i> retransmissions of hello packet, without waiting for a key stroke. Useful for unattended operation, where udp-sender is started from a cron-job for a broadcast/multicast at a scheduled time.</dl>
<h3>Networking options</h3>
<p> The following networking options should be supplied both on the sender and the receivers:</p>
<dl>
<dt>&#8211;portbase <i>portbase</i></p>
<dd> Default ports to use for udpcast. Two ports are used: <i>portbase</i> and <i>portbase+1</i> . Thus, <i>Portbase</i> must be even. Default is <tt>9000</tt>. The same <i>portbase</i> must be specified for both <tt>&quot;udp-sender&quot;</tt> and <tt>&quot;udp-receiver&quot;</tt>.</p>
<dt>&#8211;interface <i>interface</i></p>
<dd> Network interface used to send out the data. Default is <tt>&quot;eth0&quot;</tt></p>
<dt>&#8211;ttl <i>time to live</i></p>
<dd> Sets the <i>time-to-live</i> parameter for the multicast packets. Should theoretically allow to use UDPCast beyond the local network, but not tested for lack of a multicast router.</p>
<dt>&#8211;mcast-rdv-address <i>address</i></p>
<dd> Uses a non-standard multicast address for the control (rendez-vous) connection. This address is used by the sender and receivers to &#8220;find&#8221; each other. This is <code>not</code> the address that is used to transfer the actual data. </p>
<p> By default <tt>&quot;mcast-rdv-address&quot;</tt> is the Ethernet broadcast address if <tt>&quot;ttl&quot;</tt> is 1, and <tt>224.0.0.1</tt> otherwise. This setting should not be used except in very special situations, such as when <tt>224.0.0.1</tt> cannot be used for policy reasons.</dl>
<p> The following networking options should be supplied only on the sender:</p>
<dl>
<dt>&#8211;mcast-data-address <i>address</i></p>
<dd> Uses the given address for multicasting the data. If not specified, the program will automatically derive a multicast address from its own <font SIZE="-1">IP </font>(by keeping the last 27 bits of the <font SIZE="-1">IP</font> and then prepending 232).</p>
<dt>&#8211;pointopoint</p>
<dd> Point-to-point mode. Only a single receiver is allowed, but the data will be directly send to this receiver (in unicast mode), rather than multicast/broadcast all over the place. If no async mode is chosen, and there happens to be only one receiver, point-to-point is activated automatically.</p>
<dt>&#8211;nopointopoint</p>
<dd> Don&#8217;t use point-to-point, even if there is only one single receiver.</p>
<dt>&#8211;full-duplex</p>
<dd> Use this option if you use a full-duplex network. T-base-10 or 100 is full duplex if equipped with a switch. Hub based networks, or T-base-2 networks (coaxial cable) are only <code>half-duplex</code> and you should not use this option with these networks, or else you may experience a 10% performance hit. </p>
<p> N.B. On high-latency <font SIZE="-1">WAN</font> links, the full-duplex option can lead to substantial performance improvements, because it allows udp-sender to send more data while it is still waiting for the previous batch to get acknowledged.</p>
<dt>&#8211;half-duplex</p>
<dd> Use half duplex mode (needed for Hub based or T-base-2 networks). This is the default behavior in this version of udpcast.</p>
<dt>&#8211;broadcast</p>
<dd> Use Ethernet broadcast, rather than multicast. Useful if you have Ethernet cards which don&#8217;t support multicast. </p>
<p> By default, <tt>&quot;udpcast&quot;</tt> uses multicast. This allows sending the data only to those receivers that requested it. Ethernet cards of machines which <i>don&#8217;t</i> participate in the transmission automatically block out the packets at the hardware level. Moreover, network switches are able to selectively transmit the packets only to those network ports to which receivers are connected. Both features thus allow a much more efficient operation than broadcast. This option should only be supplied on the sender.</p>
<dt>-b blocksize</p>
<dd> Choses the packet size. Default (and also maximum) is 1456.</dl>
<h3>Unidirectional mode (without return channel)</h3>
<p> The options described below are useful in situations where no &#8220;return channel&#8221; is available, or where such a channel is impractical due to high latency. In an unidirectional setup (i.e. without return channel), the sender only sends data but doesn&#8217;t expect any reply from the receiver. </p>
<p> Unidirectional options must be used together, or else the transfer will not work correctly. You may for example use the following command line: </p>
<p> <tt>&quot;udp-sender --async --max-bitrate 10m --fec 8x8&quot;</tt></p>
<dl>
<dt>&#8211;async</p>
<dd> Asynchronous mode. Do not request confirmations from the receiver. Best used together with forward error correction and bandwidth limitation, or else the receiver will abort the reception as soon as it misses a packet. When the receiver aborts the reception in such a way, it will print a list of packets lost in the slice causing the problem. You can use this list to tune the forward error correction parameters.</p>
<dt>&#8211;max-bitrate <i>bitrate</i></p>
<dd> Limits bandwidth used by udpcast. Useful in asynchronous mode, or else the sender may send too fast for the switch and/or receiver to keep up. Bitrate may be expressed in bits per second (&#8211;bitrate 5000000), kilobits per second (<tt>&quot;--bitrate 5000k&quot;</tt>) or megabits per second (<tt>&quot;--bitrate 5m&quot;</tt>). This is the raw bitrate, including packet headers, forward error correction, retransmissions, etc. Actual payload bitrate will be lower.</p>
<dt>&#8211;fec <i>interleave&quot;x&quot;redundancy</i>&quot;/&quot;<i>stripesize</i></p>
<dd> Enables forward error correction. The goal of forward error correction is to transmit redundant data, in order to make up for packets lost in transit. Indeed, in unidirectional mode, the receivers have no way of requesting retransmission of lost packets, thus the only way to address packet loss is to include redundant information to begin with. The algorithm is designed in such a way that if <i>r</i> redundant packets are transmitted, that those can be used to compensate for the loss of <i>any</i> r packets in the same <font SIZE="-1">FEC</font> group (stripe). </p>
<p> In order to increase robustness of the <font SIZE="-1">FEC</font> algorithm against burst packet losses, each <i>slice</i> is divided in <i>interleave</i> stripes. Each stripe has <i>stripesize</i> blocks (if not specified, stripesize is calculated by diving <i>slice-size</i> by <i>interleave</i>). For each stripe, <i>redundancy</i> <font SIZE="-1">FEC</font> packets are added. Stripes are organized in such a fashion that consecutive packets belong to different stripes. This way, we ensure that burst losses affect different stripes, rather than using all <font SIZE="-1">FEC</font> packets of a single stripe. Example: <tt>&quot;--fec 8x8/128&quot;</tt></p>
<dt>&#8211;rate-governor <i>module.so:key1=value1,key2=value2</i></p>
<dd> Applies a dynamically loadable rate governor. <i>module.so</i> is the name of the preloadable module, which is followed by a number of property assignments (<i>key1=value1</i>). The rate governor controls the transmission rate according to various criteria, such as congestion information received from a routing or encapsulating device. See comments in <tt>&quot;/usr/include/udpcast/rateGovernor.h&quot;</tt> and example in <tt>&quot;examples/rateGovernor&quot;</tt> for more details</p>
<dt>&#8211;rexmit-hello-interval <i>timeout</i></p>
<dd> If set, rebroadcasts the <font SIZE="-1">HELLO</font> packet used for initiating the casting each <i>timeout</i> milliseconds. </p>
<p> This option is useful together with <i>asyc mode</i>, because with async mode the receiver won&#8217;t send a connection request to the sender (and hence won&#8217;t get a connection reply). In <i>async mode</i>, the receivers get all needed information from the <i>hello</i> packet instead, and are thus particularly dependant on the reception of this packet, makeing retransmission useful. </p>
<p> This option is also useful on networks where packet loss is so high that even with connection requests, sender and receiver would not find each other otherwise.</p>
<dt>&#8211;retries-until-drop <i>retries</i></p>
<dd> How many time to send a <font SIZE="-1">REQACK</font> until dropping a receiver. Lower retrycounts make <tt>&quot;udp-sender&quot;</tt> faster to react to crashed receivers, but they also increase the probability of false alerts (dropping receivers that are not actually crashed, but merely slow to respond for whatever reason)</p>
<dt>&#8211;streaming</p>
<dd> Allows receivers to join an ongoing transmission mid through</dl>
<h3>Keyboardless mode</h3>
<p> The options below help to run a sender in unattended mode.</p>
<dl>
<dt>&#8211;min-receivers <i>n</i></p>
<dd> Automatically start as soon as a minimal number of receivers have connected.</p>
<dt>&#8211;min-wait <i>t</i></p>
<dd> Even when the necessary amount of receivers <i>do</i> have connected, still wait until <i>t</i> seconds since first receiver connection have passed.</p>
<dt>&#8211;max-wait <i>t</i></p>
<dd> When not enough receivers have connected (but at least one), start anyways when <i>t</i> seconds since first receiver connection have pased.</p>
<dt>&#8211;nokbd</p>
<dd> Do not read start signal from keyboard, and do not display any message telling the user to press any key to start.</p>
<dt>&#8211;start-timeout <i>sec</i></p>
<dd> sender aborts at start if it doesn&#8217;t see a receiver within this many seconds. Furthermore, transmission of data needs to start within this delay. Once transmission is started, the timeout no longer applies.</p>
<dt>&#8211;daemon-mode</p>
<dd> Do not exit when done, but instead wait for the next batch of receivers. If this option is given twice, udp-sender puts itself into the background, closes its standard file descriptors, and acts as a real daemon.</p>
<dt>&#8211;pid-file <i>file</i></p>
<dd> Allow to specify a pid file. If given together with <tt>&quot;--daemon-mode&quot;</tt>, udp-sender will write its pid into this file. If given together with <tt>&quot;--kill&quot;</tt>, the process with the given pid will be killed.</p>
<dt>&#8211;kill</p>
<dd> Shuts down the udp-sender identified by the pid file (which also must be specified). Kill does not interrupt an ongoing transmission, but instead waits until it is finished.</dl>
<p> Example: </p>
<p> <tt>&quot;udp-sender -f zozo --min-receivers 5 --min-wait 20 --max-wait 80&quot;</tt></p>
<dl>
<dt>&bull;</p>
<dd> If one receiver connects at 18h00.00, and 4 more within the next 5 minutes, start at 18h00.20. (5 receivers connected, but min-wait not yet pased)</p>
<dt>&bull;</p>
<dd> If one receiver connects at 18h00.00, and 3 more within the next 5 minutes, then a last one at 18h00.25, start right after.</p>
<dt>&bull;</p>
<dd> If one receiver connects at 18h00.00, then 3 more within the next 15 minutes, then no one, start at 18h01.20. (not enough receivers, but we start anyways after max-wait).</dl>
<h3>Logging and statistics options</h3>
<p> The options instruct <tt>&quot;udp-sender&quot;</tt> to log some additional statistics to a file:</p>
<dl>
<dt>&#8211;stat-period <i>seconds</i></p>
<dd> Every so much milliseconds, print some statistics to stderr: how much bytes sent so far log, position in uncompressed file (if applicable), retransmit count&#8230; By default, this is printed every half second.</p>
<dt>&#8211;print-uncompressed-position <i>flag</i></p>
<dd> By default, udp-sender only prints the position in uncompressed file if the 2 following conditions are met:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> Input is piped via a compressor (<tt>&quot;-p &quot;</tt> option).</p>
<dt>&bull;</p>
<dd> The primary input is seekable (file or device)</dl>
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
<dt>&#8211;log <i>file</i></p>
<dd> Logs some stuff into <i>file</i>.</p>
<dt>&#8211;no-progress</p>
<dd> Do not display progress statistics.</p>
<dt>&#8211;bw-period <i>seconds</i></p>
<dd> Every so much seconds, log instantenous bandwidth seen during that period. Note: this is different from the bandwidth displayed to stderr of the receiver, which is the average since start of transmission.</dl>
<h3>Tuning options (sender)</h3>
<p> The following tuning options are all about slice size. Udpcast groups its data in <i>slices</i>, which are a series of blocks (<font SIZE="-1">UDP</font> packets). These groups are relevant for</p>
<dl>
<dt>&bull;</p>
<dd> data retransmission: after each slice, the server asks the receivers whether they have received all blocks, and if needed retransmits what has been missing</p>
<dt>&bull;</p>
<dd> forward error correction: each slice has its set of data blocks, and matching <font SIZE="-1">FEC</font> blocks.</p>
<dt>&#8211;min-slice-size <i>size</i></p>
<dd> minimum slice size (expressed in blocks). Default is 16. When dynamically adjusting slice size (only in non-duplex mode), never use smaller slices than this. Ignored in duplex mode (default).</p>
<dt>&#8211;max-slice-size <i>size</i></p>
<dd> maximum slice size (expressed in blocks). Default is 1024. When dynamically adjusting slice size (only in non-duplex mode), never use larger slices than this. Ignored in duplex mode (default).</p>
<dt>&#8211;default-slice-size <i>size</i></p>
<dd> Slice size used (starting slice size in half-duplex mode).</p>
<dt>&#8211;rehello-offset <i>offs</i></p>
<dd> in streaming mode, how many packets before end of slice the hello packet will be transferred (default 50). Chose larger values if you notice that receivers are excessively slow to pick up running transmission</dl>
<h3>Tuning the forward error correction</h3>
<p> There are three parameters on which to act:</p>
<dl>
<dt>redundancy</p>
<dd> This influences how much extra packets are included per stripe. The higher this is, the more redundancy there is, which means that the transmission becomes more robust against loss. However, <font SIZE="-1">CPU</font> time necessary is also proportional to redundancy (a factor to consider on slow <font SIZE="-1">PC</font>&#8216;s), and of course, a higher redundancy augments the amount of data to be transmitted.</p>
<dt>interleave</p>
<dd> This influences among how many stripes the data is divided. Higher interleave improves robustness against burst loss (for example, 64 packets in a row&#8230;). It doesn&#8217;t increase robustness against randomly spread packet loss. <code>Note</code>: interleave bigger than 8 will force a smaller stripesize, due to the fact that slicesize is limited to 1024.</p>
<dt>stripesize</p>
<dd> How many data blocks there are in a stripe. Due to the algorithm used, this cannot be more than 128. Reducing stripe size is an indirect way of augmenting (relative) redundancy, without incurring the <font SIZE="-1">CPU</font> penalty of larger (absolute) redundancy. However, a larger absolute redundancy is still preferable over a smaller stripesize, because it improves robustness against clustered losses. For instance, if 8/128 is preferable over 4/64, because with 8/128 the 8 <font SIZE="-1">FEC</font> packets can be used to compensate for the loss of any of the 128 data packets, whereas with 4/64, each group of 4 <font SIZE="-1">FEC</font> packets can only be used against its own set of 64 data packets. If for instance the first 8 packets were lost, they would be recoverable with 8/128, but not with 4/64.</dl>
<p> Considering these, change parameters as follows:</p>
<dl>
<dt>&bull;</p>
<dd> If you observe long stretches of lost packets, increase interleave</p>
<dt>&bull;</p>
<dd> If you observe that transfer is slowed down by <font SIZE="-1">CPU</font> saturation, decrease redundancy and stripesize proportionnally.</p>
<dt>&bull;</p>
<dd> If you observe big <i>variations</i> in packet loss rate, increase redundancy and stripesize proportionnally.</p>
<dt>&bull;</p>
<dd> If you just observe high loss, but not necessarily clustered in any special way, increase redundancy or decrease stripesize</p>
<dt>&bull;</p>
<dd> Be aware that network equipment or the receiver may be dropping packets because of a bandwidth which is too high. Try limiting it using <tt>&quot;max-bitrate&quot;</tt></p>
<dt>&bull;</p>
<dd> The receiver may also be dropping packets because it cannot write the data to disk fast enough. Use hdparm to optimize disk access on the receiver. Try playing with the settings in <tt>&quot;/proc/sys/net/core/rmem_default&quot;</tt> and <tt>&quot;/proc/sys/net/core/rmem_max&quot;</tt>, i.e. setting them to a higher value.</dl>
<h2>SEE ALSO</h2>
<p> udp-receiver</p>
<h2>AUTHOR</h2>
<p> Alain Knaff </p>
<h2>Index</h2>
