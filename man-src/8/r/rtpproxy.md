---
title: "rtpproxy(8)"
name: "rtpproxy"
section: "8"
letter: "r"
url: "/docs/linux/man/8-rtpproxy/"
description: "rtpproxy – RTP (Real-time Transport Protocol) Proxy Server"
---

<p>rtpproxy &#8211; RTP (Real-time Transport Protocol) Proxy Server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rtpproxy</code> [<code>-?</code>] [<code>-2</code>] [<code>-f</code>] [<code>-v</code>] [<code>-V</code>] [<code>-R</code>] [<code>-l</code>&nbsp;<wbr><i>addr1</i><i>[/addr2]</i>] [<code>-6</code>&nbsp;<wbr><i>addr1</i><i>[/addr2]</i>] [<code>-s</code>&nbsp;<wbr><i>ctrl_socket</i>] [<code>-t</code>&nbsp;<wbr><i>tos</i>] [<code>-p</code>&nbsp;<wbr><i>pidfile</i>] [<code>-T</code>&nbsp;<wbr><i>max_ttl</i>] [<code>-r</code>&nbsp;<wbr><i>rdir</i>&nbsp;<wbr>[<code>-S</code>&nbsp;<wbr><i>sdir</i>]] [<code>-L</code>&nbsp;<wbr><i>nofile_limit</i>] [<code>-A</code>&nbsp;<wbr><i>advaddr1</i><i>[/advaddr2]</i>] [<code>-m</code>&nbsp;<wbr><i>min_port</i>] [<code>-M</code>&nbsp;<wbr><i>max_port</i>] [<code>-u</code>&nbsp;<wbr><i>uname</i><i>[:gname]</i>] [<code>-w</code>&nbsp;<wbr><i>sock_mode</i>] [<code>-F</code>] [<code>-i</code>] [<code>-n</code>&nbsp;<wbr><i>timeout_socket</i>] [<code>-P</code>] [<code>-a</code>] [<code>-d</code>&nbsp;<wbr><i>log_level</i><i>[:log_facility]</i>] [<code>-W</code>&nbsp;<wbr><i>setup_ttl</i>]</dl>
<h2>Description</h2>
<p><code>rtpproxy</code></p>
<dd>is a symmetric RTP proxy designed to be used in conjunction with the SIP Express Router (SER) or any other SIP proxy or SIP B2BUA capable of rewriting SDP bodies in SIP messages that it processes. </p>
<p> The main purpose of rtpproxy is to make the communication between SIP user agents behind NAT(s) (Network Address Translator) possible. Several cases exists when direct end-to-end communication is not possible and RTP streams have to be relayed through another host. Rtpproxy can be used to setup such a relaying host. </p>
<p> When two listen interfaces have been specified using the command line parameters described below then rtpproxy will enter so called bridging mode. In briding mode rtpproxy forwards RTP packets received on one interface to the other interface and vice versa. This mode can be used to forward RTP packets between networks without direct network level connectivy (provided that the host running rtpproxy has one interface in both of them). One particular application of bridging mode is IPv4/IPv6 traversal of RTP packets. </p>
<p> When instructured by SER rtpproxy can also record the entire RTP session in a file on a local harddisk or play a pre-recorded file to the user agent (so called Music-on-Hold).</p>
<h2>Options</h2>
<p><code>-?</code></p>
<dl>
<dd>Show summary of options.</dl>
<p> <code>-2</code></p>
<dl>
<dd>Send every RTP packet twice in sessions that use low-bitrate codecs. Only packets that are smaller than 128 bytes will be sent twice. This option can improve audio quality on lossy links.</dl>
<p> <code>-f</code></p>
<dl>
<dd>Rtpproxy will stay in foreground mode if this option is set.</dl>
<p> <code>-v</code></p>
<dl>
<dd>Show version of program.</dl>
<p> <code>-V</code></p>
<dl>
<dd>Show command protocol version.</dl>
<p> <code>-l</code> <i>addr1</i><i>[/addr2]</i></p>
<dl>
<dd>IPv4 listen IP address(es). You can specify either one or two addresses. If two addresses have been specified then rtpproxy will work in bridging mode.</dl>
<p> <code>-6</code> <i>addr1</i><i>[/addr2]</i></p>
<dl>
<dd>IPv6 listen IP address(es). You can specify either one or two addresses. If two addresses have been specified then rtpproxy will work in bridging mode.</dl>
<p> <code>-s</code> <i>ctrl_socket</i></p>
<dl>
<dd>This parameter configures rtpproxy control socket. The control socket is used by nathelper module of SER to create/modify/delete RTP sessions to be relayed. Format of <i>ctrl_socket</i> is &lt;type&gt;:&lt;socket&gt;. Following types are supported: </p>
<dl>
<dd>&bull; </p>
<p> <i>udp:</i> Create UDP control socket. In this mode RTPProxy will listen on UDP for control messages from SER/nathelper. </p>
<p> Example: -s udp:127.0.0.1:9000 </p>
<p> IP address can be &#8216;*&#8217; in which case rtpproxy will listen on all local interfaces. If omitted port 22222 is used. </p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 RTPProxy control protocol has no built-in security mechanisms. Make sure that you protect the listening IP and port properly when using RTPProxy with UDP control socket. </p>
</dl>
</dl>
<dl>
<dd>&bull; </p>
<p> <i>udp6:</i> Create IPv6 UDP control socket. In this mode RTPProxy will listen on UDP/IPv6 for control messages from SER/nathelper. </p>
<p> Example: -s udp6:::1:9000</dl>
<dl>
<dd>&bull; </p>
<p> <i>unix:</i> Create UNIX domain socket for control interface. In this mode SER/nathelper and RTPProxy must be running on the same host. This is the default setting for both SER/nathelper and rtpproxy. </p>
<p> Example: -s unix:/var/run/rtpproxy.sock </p>
<p> Default value is /var/run/rtpproxy.sock.</dl>
</dl>
<p> <code>-t</code> <i>tos</i></p>
<dl>
<dd>Set ToS (Type of Service) in the outgoing UDP packets to this value. Default value is 0xB8. Setting this parameter to -1 disables setting ToS resulting in operating system default ToS being used instead.</dl>
<p> <code>-r</code> <i>rec_dir</i></p>
<dl>
<dd>Directory where recorded RTP sessions will be stored.</dl>
<p> <code>-S</code> <i>spool_dir</i></p>
<dl>
<dd>Spool directory for RTP sessions being recorded. The file will be moved to directory configured in <code>-r</code> option after the session finishes.</dl>
<p> <code>-R</code></p>
<dl>
<dd>Do not record RTCP when recording an RTP session. This option is disabled (rtpproxy will record RTCP) by default.</dl>
<p> <code>-p</code> <i>pid_file</i></p>
<dl>
<dd>This parameter configures the name of the file where PID of running rtpproxy will be stored. Default is /var/run/rtpproxy.pid.</dl>
<p> <code>-T</code> <i>max_ttl</i></p>
<dl>
<dd>Limit the maximum TTL (Time To Live) of outgoing IP packets to the value of <i>max_ttl</i>.</dl>
<p> <code>-L</code> <i>nofile_limit</i></p>
<dl>
<dd>Adjust the number of simultaneous open connections. Please note that each RTP media stream requires four open connections. A SIP call can open more than one RTP media stream depending on the client&#8217;s setup.</dl>
<p> <code>-A</code> <i>advaddr1</i><i>[/advaddr2]</i></p>
<dl>
<dd>Setup advertised address if necessary.</dl>
<p> <code>-m</code> <i>min_port</i></p>
<dl>
<dd>Set lower limit on UDP ports range that the RTPproxy uses for RTP/RTCP sessions to <i>min_port</i>. Default is 35000.</dl>
<p> <code>-M</code> <i>max_port</i></p>
<dl>
<dd>Set upper limit on UDP ports range that the RTPproxy uses for RTP/RTCP sessions to <i>max_port</i>. Default is 65000.</dl>
<p> <code>-u</code> <i>uname</i><i>[:gname]</i></p>
<dl>
<dd>Switch RTPproxy to UID identified by the <i>uname</i> and optional GID identified by <i>gname</i> when proxy is up and running.</dl>
<p> <code>-w</code> <i>sock_mode</i></p>
<dl>
<dd>Set access mode for the controlling UNIX-socket (if used). Only applies if RTPproxy runs under a different GID using <code>-u</code> option.</dl>
<p> <code>-F</code></p>
<dl>
<dd>By default the RTPproxy will warn user if running as superuser (UID 0) in local control mode and refuse to run in remote control mode at all. This switch removes the check.</dl>
<p> <code>-i</code></p>
<dl>
<dd>Enable independent timeout mode. By default, a timeout (which results in automatic destruction of the session) can only occur if no RTP packets are received on any of the session&#8217;s ports. This option if set varies that behaviour, such that a timeout will occur if packets are still being received on one port but not the other. The option should be used with caution since in some cases it&#8217;s perfectly fine to have packets coming from only one side of conversation (i.e. when the second party has muted its audio).</dl>
<p> <code>-n</code> <i>timeout_socket</i></p>
<dl>
<dd>This parameter configures the optional timeout notification socket. The socket should be created by another application, preferably before starting rtpproxy. For those sessions where the timeout mechanism is enabled, notifications are sent on this socket if the session times out. </p>
<p> Format of <i>timeout_socket</i> is &lt;type&gt;:&lt;socket&gt;. Following types are supported: </p>
<dl>
<dd>&bull; </p>
<p> <i>unix:</i>Connect to UNIX domain socket for sending timeout notifications. In this mode B2BUA and RTPProxy must be running on the same host. </p>
<p> Example: -n unix:/var/run/rtpproxy_timeout.sock</dl>
<dl>
<dd>&bull; </p>
<p> <i>tcp:</i>Connect to a remote host using TCP/IP for sending timeout notifications. Format of the <i>socket</i> parameter in this case is &lt;host&gt;:&lt;port&gt;. </p>
<p> Example: -n tcp:10.20.30:12345</dl>
<p> There is no default value, notifications are not sent and not permitted unless a value is specified explicitly.</dl>
<p> <code>-P</code></p>
<dl>
<dd>Record sessions using PCAP file format instead of non-standard ad-hoc format. The PCAP format, which is the de-facto standard for packet capturing software, has the advantage of being compatible with numerous third-party tools and utilities, such as Wireshark (Ethereal) for example. The drawback of PCAP is sligtly larger overhead (extra 12 bytes for every saved RTP packet for IPv4). Also, recording IPv6 sessions in PCAP format is not supported at the moment.</dl>
<p> <code>-a</code></p>
<dl>
<dd>Record all sessions going through the RTPproxy unconditionally. By default the RTPproxy requires call control software (i.e. SER, OpenSER or B2BUA) to enable recording explicitly on per-session basis by sending appropriate record command.</dl>
<p> <code>-d</code> <i>log_level</i><i>[:log_facility]</i></p>
<dl>
<dd>This parameter configures the verbosity level of the log output. Possible <i>log_level</i> values in the order from the most verboe to the least verbose are: DBUG, INFO, WARN, ERR and CRIT. </p>
<p> The optional <i>log_facility</i> parameter sets <a href="/docs/linux/man/3-syslog/">syslog</a>(3) facility assigned to log messages. </p>
<p> Example: -d WARN:LOG_LOCAL5 </p>
<p> The default level in foreground mode is is DBUG, in background &#8211; WARN and facility is LOG_DAEMON.</dl>
<h2>Howitworks</h2>
<p>When SER receives an INVITE request, it extracts Call-ID from it and communicates it to rtpproxy via Unix domain socket or UDP. Rtproxy looks for an existing session with such Call-ID. If the session exists it returns UDP port for that session, if not, then it creates a new session, binds to a first empty UDP port from the range specified at the compile time and returns number of that port to a SER. After receiving reply from the proxy, SER replaces media ip:port in the SDP to point to the proxy and forwards request as usually. </p>
<p> When SER receives a non-negative SIP reply with SDP it again extracts Call-ID from it and communicates it to the proxy. In this case the proxy does not allocate a new session if it doesn&#8217;t exist, but simply performs a lookup among existing sessions and returns either a port number if the session is found, or error code indicating that there is no session with such id. After receiving positive reply from the proxy, SER replaces media ip:port in the SIP reply to point to the proxy and forwards reply as usually. </p>
<p> After the session has been created, the proxy listens on the port it has allocated for that session and waits for receiving at least one UDP packet from each of two parties participating in the call. Once such packet is received, the proxy fills one of two ip:port structures associated with each call with source ip:port of that packet. When both structures are filled in, the proxy starts relaying UDP packets between parties. </p>
<p> The proxy tracks idle time for each of existing sessions (i.e. the time within which there were no packets relayed), and automatically cleans up a sessions whose idle times exceed the value specified at compile time (60 seconds by default).</p>
<h2>Files</h2>
<p>/usr/sbin/rtpproxy</p>
<h2>License</h2>
<p>This program is licensed under the BSD license. See COPYING file in the rtpproxy sources for details.</p>
<h2>Availability</h2>
<p>The latest version of this program can be found at m[blue]<code><a rel="nofollow" href="http://www.rtpproxy.org/">http://www.rtpproxy.org/</a></code>m[].</p>
<h2>Seealso</h2>
<p><a href="/docs/linux/man/8-ser/">ser</a>(8).</p>
<h2>Author</h2>
<p><code>Maxim Sobolev</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2006 janakj</p>
