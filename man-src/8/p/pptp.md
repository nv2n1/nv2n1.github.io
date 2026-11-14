---
title: "pptp(8)"
name: "pptp"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pptp/"
description: "pptp – PPTP driver"
---

<p>pptp &#8211; PPTP driver</p>
<h2>Synopsis</h2>
<p><code>pptp</code> <i>&lt;pptp-server-IP&gt; &lt;pptp-options&gt; [ppp-options] &#8230;</i></p>
<h2>Description</h2>
<p><code>pptp</code> establishes the client side of a Virtual Private Network (VPN) using the Point-to-Point Tunneling Protocol (PPTP). Use this program to connect to an employer&#8217;s PPTP based VPN, or to certain cable and ADSL service providers. </p>
<p> By default, <code>pptp</code> establishes the PPTP call to the PPTP server, and then starts an instance of <code>pppd</code> to manage the data transfer. However, <code>pptp</code> can also be run as a connection manager within <code>pppd</code>.</p>
<h2>Options</h2>
<p>The first non-option argument on the <code>pptp</code> command line must be the host name or IP address of the PPTP server. </p>
<p> All long options (starting with &quot;&#8211;&quot;) are interpreted as pptp options, and a fatal error occurs if an unrecognised option is used. </p>
<p> All command-line arguments which do not start with &quot;-&quot; are interpreted as ppp options, and passed as is to <code>pppd</code> unless <code>&#8211;nolaunchpppd</code> is given.</p>
<dl>
<dt><code>&#8211;phone &lt;number&gt;</code></p>
<dd>Pass &lt;number&gt; to remote host as phone number</p>
<dt><code>&#8211;nolaunchpppd</code></p>
<dd>Do not launch <code>pppd</code> but use stdin as the network connection. Use this flag when including <code>pptp</code> as a <code>pppd</code> connection process using the <code>pty</code> option. See EXAMPLES.</p>
<dt><code>&#8211;quirks &lt;quirk&gt;</code></p>
<dd>Work around a buggy PPTP implementation, adopts special case handling for particular PPTP servers and ADSL modems. Currently recognised values are BEZEQ_ISRAEL only</p>
<dt><code>&#8211;debug</code></p>
<dd>Run in foreground (for debugging with gdb)</p>
<dt><code>&#8211;sync</code></p>
<dd>Enable Synchronous HDLC (pppd must use it too)</p>
<dt><code>&#8211;timeout &lt;secs&gt;</code></p>
<dd>Time to wait for reordered packets (0.01 to 10 secs)</p>
<dt><code>&#8211;nobuffer</code></p>
<dd>Completely disables buffering and reordering of packets. Any &#8211;timeout specified will be ignored.</p>
<dt><code>&#8211;idle-wait &lt;secs&gt;</code></p>
<dd>Time to wait before sending a control connection echo request. The RFC2637 default is 60 seconds.</p>
<dt><code>&#8211;max-echo-wait &lt;secs&gt;</code></p>
<dd>Time to wait for an echo reply before closing the control connection. The RFC2637 default is 60 seconds.</p>
<dt><code>&#8211;logstring &lt;name&gt;</code></p>
<dd>Use &lt;name&gt; instead of &#8216;anon&#8217; in syslog messages</p>
<dt><code>&#8211;localbind &lt;addr&gt;</code></p>
<dd>Bind to specified IP address instead of wildcard</p>
<dt><code>&#8211;rtmark &lt;n&gt;</code></p>
<dd>Use specified policy routing mark for all packets. This causes both the TCP control connection&#8217;s packets as well as the GRE packets to bear the given policy routing / netfilter mark. This can be used with <i>ip rule</i> (from iproute2) to use a separate routing table for the pptp client. </p>
<p> (requires root privileges or the CAP_NET_ADMIN capability.)</p>
<dt><code>&#8211;nohostroute</code></p>
<dd>Do not configure a host route pointing towards the PPTP server. (cf. ROUTING below) </p>
<dt><code>&#8211;loglevel &lt;level&gt;</code></p>
<dd>Sets the debugging level (0=low, 1=default, 2=high) </p>
<dt><code>&#8211;test-type &lt;n&gt;</code></p>
<dd>Enable packet reordering tests that damage the integrity of the packet stream to the server. Use this only when testing servers. Zero is the default, and means that packets are sent in the correct order. A value of one (1) causes a single swap between two packets, such that the sequence numbers might be 1 2 3 4 6 5 7 8 9. A value of two (2) causes ten packets to be buffered, then sent out of order but ascending, such that the sequence numbers might be 1 2 3 4 16 6 7 8 9 10 11 12 13 14 15 17 18 19 20. A value of three (3) causes ten packets to be buffered, then sent in the reverse order, like this; 1 2 3 4 16 15 14 13 12 11 10 9 8 7 6 5 17 18 19 20. </p>
<dt><code>&#8211;test-rate &lt;n&gt;</code></p>
<dd>Sets the number of packets to pass before causing a reordering test. Default is 100. Has no effect if test-type is zero. The result of test types 2 and 3 are undefined if this value is less than ten. </p>
</dl>
<h2>Routing</h2>
<p>When PPTP is used in conjunction with a default route on top of the tunnel (or just any route encompassing the PPTP server), the mechanics of routing would cause the PPTP packets themselves to be routed over the tunnel. This would result in an encapsulation loop, destroying connectivity. </p>
<p> <code>pptp</code> by default works around this by looking up the route towards the PPTP server at startup and configures a host route with that data. This essentially &quot;freezes&quot; routing for PPTP packets at the startup configuration. This behaviour can be disabled with <code>&#8211;nohostroute</code> if undesired (like when using <code>&#8211;rtmark</code> to implement policy routing). </p>
<p> <code>NB:</code> the route added by <code>pptp</code> is currently not deleted at exit!</p>
<h2>Quirks</h2>
<dl>
<dt><code>BEZEQ_ISRAEL</code></p>
<dd>modifies packets to interoperate with Orckit ADSL modems on the BEZEQ network in Israel. </p>
</dl>
<h2>Examples</h2>
<p><code>Connection to a Microsoft Windows VPN Server</code> pppd noauth nobsdcomp nodeflate require-mppe-128 name domain\\username remotename PPTP pty &quot;pptp 10.0.0.5 &#8211;nolaunchpppd&quot; Note that the <code>chap-secrets</code> file used by <code>pppd</code> must include an entry for domain\username </p>
<h2>Statistics</h2>
<p>The pptp process collects statistics when sending and receiving GRE packets. They are intended to be useful for debugging poor PPTP performance and for general monitoring of link quality. The statistics are cumulative since the pptp process was started. </p>
<p> The statistics can be viewed by sending a SIGUSR1 signal to the &quot;GRE-to-PPP Gateway&quot; process, which will cause it to dump them to the system logs (at the LOG_NOTICE level). A better way to present the statistics to applications is being sought (e.g. SNMP?). </p>
<p> The following statistics are collected at the time of writing (April 2003):</p>
<dl>
<dt><code>rx accepted</code></p>
<dd>the number of GRE packets successfully passed to PPP</p>
<dt><code>rx lost</code></p>
<dd>the number of packets never received, and presumed lost in the network</p>
<dt><code>rx under win</code></p>
<dd>the number of packets which were duplicates or had old sequence numbers (this might be caused by a packet-reordering network if your reordering timeout is set too low)</p>
<dt><code>rx over win</code></p>
<dd>the number of packets which were too far ahead in the sequence to be reordered (might be caused by loss of more than 300 packets in a row)</p>
<dt><code>rx buffered</code></p>
<dd>the number of packets which were slightly ahead of sequence, and were either buffered for reordering, or if buffering is disabled, accepted immediately (resulting in the intermediate packets being discarded).</p>
<dt><code>rx OS errors</code></p>
<dd>the number of times where the operating system reported an error when we tried to read a packet</p>
<dt><code>rx truncated</code></p>
<dd>the number of times we received a packet which was shorter than the length implied by the GRE header</p>
<dt><code>rx invalid</code></p>
<dd>the number of times we received a packet which had invalid or unsupported flags set in the header, wrong version, or wrong protocol.</p>
<dt><code>rx acks</code></p>
<dd>the number of pure acknowledgements received (without data). Too many of these will waste bandwidth, and might be solved by tuning the remote host.</p>
<dt><code>tx sent</code></p>
<dd>the number of GRE packets sent with data</p>
<dt><code>tx failed</code></p>
<dd>the number of packets we tried to send, but the OS reported an error</p>
<dt><code>tx short</code></p>
<dd>the number of times the OS would not let us write a complete packet</p>
<dt><code>tx acks</code></p>
<dd>the number of times we sent a pure ack, without data</p>
<dt><code>tx oversize</code></p>
<dd>the number of times we couldn&#8217;t send a packet because it was over PACKET_MAX bytes long</p>
<dt><code>round trip</code></p>
<dd>the estimated round-trip time in milliseconds </p>
</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-pppd/">pppd</a></i>(8) </p>
<p> Documentation in <i>/usr/share/doc/pptp-linux</i></p>
<h2>Author</h2>
<p>This manual page was written by James Cameron &lt;james.cameron [at] hp.com&gt; from text contributed by Thomas Quinot &lt;thomas [at] debian.org&gt;, for the Debian GNU/Linux system. The description of the available statistics was written by Chris Wilson &lt;chris [at] netservers.co.uk&gt;. Updates for the Debian distribution by Ola Lundqvist &lt;opal [at] debian.org&gt;.</p>
