---
title: "sctp(7)"
name: "sctp"
section: "7"
letter: "s"
url: "/docs/linux/man/7-sctp/"
description: "sctp – SCTP protocol."
---

<p>sctp &#8211; SCTP protocol.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/socket.h&gt;
#include &lt;netinet/in.h&gt;
#include &lt;netinet/sctp.h&gt;

sctp_socket = socket(PF_INET, SOCK_STREAM, IPPROTO_SCTP);
sctp_socket = socket(PF_INET, SOCK_SEQPACKET, IPPROTO_SCTP);</code></pre>
<h2>Description</h2>
<p>This is an implementation of the SCTP protocol as defined in RFC2960 and RFC3309. It is a message oriented, reliable transport protocol with direct support for multihoming that runs on top of <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), and supports both v4 and v6 versions. Like TCP, SCTP provides reliable, connection oriented data delivery with congestion control. Unlike TCP, SCTP also provides message boundary preservation, ordered and unordered message delivery, multi-streaming and multi-homing. Detection of data corruption, loss of data and duplication of data is achieved by using checksums and sequence numbers. A selective retransmission mechanism is applied to correct loss or corruption of data. This implementation supports a mapping of SCTP into sockets API as defined in the draft-ietf-tsvwg-sctpsocket-10.txt(Sockets API extensions for SCTP). Two styles of interfaces are supported. A <code>one-to-many</code> style interface with 1 to MANY relationship between socket and associations where the outbound association setup is implicit. The syntax of a one-to-many style socket() call is sd = socket(PF_INET, SOCK_STREAM, IPPROTO_SCTP); A typical server in this style uses the following socket calls in sequence to prepare an endpoint for servicing requests.<br />
&nbsp;<wbr>&nbsp;<wbr>1. socket()<br />
&nbsp;<wbr>&nbsp;<wbr>2. bind()<br />
&nbsp;<wbr>&nbsp;<wbr>3. listen()<br />
&nbsp;<wbr>&nbsp;<wbr>4. recvmsg()<br />
&nbsp;<wbr>&nbsp;<wbr>5. sendmsg()<br />
&nbsp;<wbr>&nbsp;<wbr>6. close() A typical client uses the following calls in sequence to setup an association with a server to request services.<br />
&nbsp;<wbr>&nbsp;<wbr>1. socket()<br />
&nbsp;<wbr>&nbsp;<wbr>2. sendmsg()<br />
&nbsp;<wbr>&nbsp;<wbr>3. recvmsg()<br />
&nbsp;<wbr>&nbsp;<wbr>4. close() A <code>one-to-one style</code> interface with a 1 to 1 relationship between socket and association which enables existing TCP applications to be ported to SCTP with very little effort. The syntax of a one-to-one style socket() call is </p>
<pre><code>sd = socket(PF_INET, SOCK_STREAM, IPPROTO_SCTP);</code></pre>
<p> A typical server in one-to-one style uses the following system call sequence to prepare an SCTP endpoint for servicing requests:<br />
&nbsp;<wbr>&nbsp;<wbr>1. socket()<br />
&nbsp;<wbr>&nbsp;<wbr>2. bind()<br />
&nbsp;<wbr>&nbsp;<wbr>3. listen()<br />
&nbsp;<wbr>&nbsp;<wbr>4. accept() The accept() call blocks until a new association is set up. It returns with a new socket descriptor. The server then uses the new socket descriptor to communicate with the client, using recv() and send() calls to get requests and send back responses. Then it calls<br />
&nbsp;<wbr>&nbsp;<wbr>5. close() to terminate the association. A typical client uses the following system call sequence to setup an association with a server to request services:<br />
&nbsp;<wbr>&nbsp;<wbr>1. socket()<br />
&nbsp;<wbr>&nbsp;<wbr>2. connect() After returning from connect(), the client uses send() and recv() calls to send out requests and receive responses from the server. The client calls<br />
&nbsp;<wbr>&nbsp;<wbr>3. close() to terminate this association when done.</p>
<h2>Address Formats</h2>
<p>SCTP is built on top of IP (see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7)). The address formats defined by <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7) apply to SCTP. SCTP only supports point-to-point communication; broadcasting and multicasting are not supported.</p>
<h2>Sysctls</h2>
<p>These variables can be accessed by the <code>/proc/sys/net/sctp/* </code> files or with the <code><a href="/docs/linux/man/2-sysctl/">sysctl</a></code>(2) interface. In addition, most IP sysctls also apply to SCTP. See <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dl>
<dt>Please check kernel documentation for this, at Documentation/networking/ip-sysctl.txt.</p>
<dd></dl>
<h2>Statistics</h2>
<p>These variables can be accessed by the <code>/proc/net/sctp/* </code> files.</p>
<dl>
<dt><code>assocs</code></p>
<dd>Displays the following information about the active associations. assoc ptr, sock ptr, socket style, sock state, association state, hash bucket, association id, bytes in transmit queue, bytes in receive queue, user id, inode, local port, remote port, local addresses and remote addresses.</p>
<dt><code>eps</code></p>
<dd>Displays the following information about the active endpoints. endpoint ptr, sock ptr, socket style, sock state, hash bucket, local port, user id, inode and local addresses.</p>
<dt><code>snmp</code></p>
<dd>Displays the following statistics related to SCTP states, packets and chunks.</p>
<dt>
<dt><code>SctpCurrEstab</code></p>
<dd>
<dd>The number of associations for which the current state is either ESTABLISHED, SHUTDOWN-RECEIVED or SHUTDOWN-PENDING.</p>
<dt><code>SctpActiveEstabs</code></p>
<dd>The number of times that associations have made a direct transition to the ESTABLISHED state from the COOKIE-ECHOED state. The upper layer initiated the association attempt.</p>
<dt><code>SctpPassiveEstabs</code></p>
<dd>The number of times that associations have made a direct transition to the ESTABLISHED state from the CLOSED state. The remote endpoint initiated the association attempt.</p>
<dt><code>SctpAborteds</code></p>
<dd>The number of times that associations have made a direct transition to the CLOSED state from any state using the primitive &#8216;ABORT&#8217;. Ungraceful termination of the association.</p>
<dt><code>SctpShutdowns</code></p>
<dd>The number of times that associations have made a direct transition to the CLOSED state from either the SHUTDOWN-SENT state or the SHUTDOWN-ACK-SENT state. Graceful termination of the association.</p>
<dt><code>SctpOutOfBlues</code></p>
<dd>The number of out of the blue packets received by the host. An out of the blue packet is an SCTP packet correctly formed, including the proper checksum, but for which the receiver was unable to identify an appropriate association.</p>
<dt><code>SctpChecksumErrors</code></p>
<dd>The number of SCTP packets received with an invalid checksum.</p>
<dt><code>SctpOutCtrlChunks</code></p>
<dd>The number of SCTP control chunks sent (retransmissions are not included). Control chunks are those chunks different from DATA.</p>
<dt><code>SctpOutOrderChunks</code></p>
<dd>The number of SCTP ordered data chunks sent (retransmissions are not included).</p>
<dt><code>SctpOutUnorderChunks</code></p>
<dd>The number of SCTP unordered chunks(data chunks in which the U bit is set to 1) sent (retransmissions are not included).</p>
<dt><code>SctpInCtrlChunks</code></p>
<dd>The number of SCTP control chunks received (no duplicate chunks included).</p>
<dt><code>SctpInOrderChunks</code></p>
<dd>The number of SCTP ordered data chunks received (no duplicate chunks included).</p>
<dt><code>SctpInUnorderChunks</code></p>
<dd>The number of SCTP unordered chunks(data chunks in which the U bit is set to 1) received (no duplicate chunks included).</p>
<dt><code>SctpFragUsrMsgs</code></p>
<dd>The number of user messages that have to be fragmented because of the MTU.</p>
<dt><code>SctpReasmUsrMsgs</code></p>
<dd>The number of user messages reassembled, after conversion into DATA chunks.</p>
<dt><code>SctpOutSCTPPacks</code></p>
<dd>The number of SCTP packets sent. Retransmitted DATA chunks are included.</p>
<dt><code>SctpInSCTPPacks</code></p>
<dd>The number of SCTP packets received. Duplicates are included.</dl>
<h2>Socket Options</h2>
<p>To set or get a SCTP socket option, call <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2) to read or <code><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></code>(2) to write the option with the option level argument set to <code>SOL_SCTP.</code></p>
<dl>
<dt><code>SCTP_RTOINFO.</code></p>
<dd>This option is used to get or set the protocol parameters used to initialize and bound retransmission timout(RTO). The structure sctp_rtoinfo defined in /usr/include/netinet/sctp.h is used to access and modify these parameters.</p>
<dt><code>SCTP_ASSOCINFO</code></p>
<dd>This option is used to both examine and set various association and endpoint parameters. The sturcture sctp_assocparams defined in /usr/include/netinet/sctp.h is used to access and modify these parameters.</p>
<dt><code>SCTP_INITMSG</code></p>
<dd>This option is used to get or set the protocol parameters for the default association initialization. The structure sctp_initmsg defined in /usr/include/netinet/sctp.h is used to access and modify these parameters. </p>
<p> Setting initialization parameters is effective only on an unconnected socket (for one-to-many style sockets only future associations are effected by the change). With one-to-one style sockets, this option is inherited by sockets derived from a listener socket.</p>
<dt><code>SCTP_NODELAY</code></p>
<dd>Turn on/off any Nagle-like algorithm. This means that packets are generally sent as soon as possible and no unnecessary delays are introduced, at the cost of more packets in the network. Expects an integer boolean flag.</p>
<dt><code>SCTP_AUTOCLOSE</code></p>
<dd>This socket option is applicable to the one-to-many style socket only. When set it will cause associations that are idle for more than the specified number of seconds to automatically close. An association being idle is defined an association that has NOT sent or received user data. The special value of 0 indicates that no automatic close of any associations should be performed. The option expects an integer defining the number of seconds of idle time before an association is closed.</p>
<dt><code>SCTP_SET_PEER_PRIMARY_ADDR</code></p>
<dd>Requests that the peer mark the enclosed address as the association primary. The enclosed address must be one of the association&#8217;s locally bound addresses. The structure sctp_setpeerprim defined in /usr/include/netinet/sctp.h is used to make a set peer primary request.</p>
<dt><code>SCTP_PRIMARY_ADDR</code></p>
<dd>Requests that the local SCTP stack use the enclosed peer address as the association primary. The enclosed address must be one of the association peer&#8217;s addresses. The structure sctp_prim defined in /usr/include/netinet/sctp.h is used to make a get/set primary request.</p>
<dt><code>SCTP_DISABLE_FRAGMENTS</code></p>
<dd>This option is a on/off flag and is passed an integer where a non-zero is on and a zero is off. If enabled no SCTP message fragmentation will be performed. Instead if a message being sent exceeds the current PMTU size, the message will NOT be sent and an error will be indicated to the user.</p>
<dt><code>SCTP_PEER_ADDR_PARAMS</code></p>
<dd>Using this option, applications can enable or disable heartbeats for any peer address of an association, modify an address&#8217;s heartbeat interval, force a heartbeat to be sent immediately, and adjust the address&#8217;s maximum number of retransmissions sent before an address is considered unreachable. The structure sctp_paddrparams defined in /usr/include/netinet/sctp.h is used to access and modify an address&#8217;s parameters.</p>
<dt><code>SCTP_DEFAULT_SEND_PARAM</code></p>
<dd>Applications that wish to use the sendto() system call may wish to specify a default set of parameters that would normally be supplied through the inclusion of ancillary data. This socket option allows such an application to set the default sctp_sndrcvinfo structure. The application that wishes to use this socket option simply passes in to this call the sctp_sndrcvinfo structure defined in /usr/include/netinet/sctp.h. The input parameters accepted by this call include sinfo_stream, sinfo_flags, sinfo_ppid, sinfo_context, sinfo_timetolive. The user must set the sinfo_assoc_id field to identify the<br />
&nbsp;<wbr>association to affect if the caller is using the one-to-many style.</p>
<dt><code>SCTP_EVENTS</code></p>
<dd>This socket option is used to specify various notifications and ancillary data the user wishes to receive. The structure sctp_event_subscribe defined in /usr/include/netinet/sctp.h is used to access or modify the events of interest to the user.</p>
<dt><code>SCTP_I_WANT_MAPPED_V4_ADDR</code></p>
<dd>This socket option is a boolean flag which turns on or off mapped V4 addresses. If this option is turned on and the socket is type PF_INET6, then IPv4 addresses will be mapped to V6 representation. If this option is turned off, then no mapping will be done of V4 addresses and a user will receive both PF_INET6 and PF_INET type addresses on the socket. </p>
<p> By default this option is turned on and expects an integer to be passed where non-zero turns on the option and zero turns off the option.</p>
<dt><code>SCTP_MAXSEG</code></p>
<dd>This socket option specifies the maximum size to put in any outgoing SCTP DATA chunk. If a message is larger than this size it will be fragmented by SCTP into the specified size. Note that the underlying SCTP implementation may fragment into smaller sized chunks when the PMTU of the underlying association is smaller than the value set by the user. The option expects an integer. </p>
<p> The default value for this option is 0 which indicates the user is NOT limiting fragmentation and only the PMTU will effect SCTP&#8217;s choice of DATA chunk size.</p>
<dt><code>SCTP_STATUS</code></p>
<dd>Applications can retrieve current status information about an association, including association state, peer receiver window size, number of unacked data chunks, and number of data chunks pending receipt. This information is read-only. The structure sctp_status defined in /usr/include/netinet/sctp.h is used to access this information.</p>
<dt><code>SCTP_GET_PEER_ADDR_INFO</code></p>
<dd>Applications can retrieve information about a specific peer address of an association, including its reachability state, congestion window, and retransmission timer values. This information is read-only. The structure sctp_paddr_info defined in /usr/include/netinet/sctp.h is used to access this information.</p>
<dt><code>SCTP_GET_ASSOC_STATS</code></p>
<dd>Applications can retrieve current statistics about an association, including SACKs sent and received, SCTP packets sent and received. The complete list can be found in /usr/include/netinet/sctp.h in struct sctp_assoc_stats.</dl>
<h2>Authors</h2>
<p>Sridhar Samudrala &lt;sri [at] us.ibm.com&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-socket/">socket</a></code>(7), <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7), <code><a href="/docs/linux/man/2-bind/">bind</a></code>(2), <code><a href="/docs/linux/man/2-listen/">listen</a></code>(2), <code><a href="/docs/linux/man/2-accept/">accept</a></code>(2), <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2), <code><a href="/docs/linux/man/2-sendmsg/">sendmsg</a></code>(2), <code><a href="/docs/linux/man/2-recvmsg/">recvmsg</a></code>(2), <code><a href="/docs/linux/man/2-sysctl/">sysctl</a></code>(2), <code><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></code>(2), <code><a href="/docs/linux/man/3-sctp_bindx/">sctp_bindx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_connectx/">sctp_connectx</a></code>(3), <code><a href="/docs/linux/man/3-sctp_sendmsg/">sctp_sendmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_send/">sctp_send</a></code>(3), <code><a href="/docs/linux/man/3-sctp_recvmsg/">sctp_recvmsg</a></code>(3), <code><a href="/docs/linux/man/3-sctp_peeloff/">sctp_peeloff</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getladdrs/">sctp_getladdrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_getpaddrs/">sctp_getpaddrs</a></code>(3), <code><a href="/docs/linux/man/3-sctp_opt_info/">sctp_opt_info</a></code>(3). RFC2960, RFC3309 for the SCTP specification. </p>
