---
title: "irda(7)"
name: "irda"
section: "7"
letter: "i"
url: "/docs/linux/man/7-irda/"
description: "irda – The Linux-IrDA protocol stack"
---

<p>irda &#8211; The Linux-IrDA protocol stack</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;linux/irda.h&gt;
stream_s = socket(PF_INET, SOCK_STREAM, 0);


seqpkt_s = socket(PF_INET, SOCK_SEQPACKET, 0);


dgram_s = socket(PF_INET, SOCK_DGRAM, IRDAPROTO_UNITDATA);


ultra_s = socket(PF_INET, SOCK_DGRAM, IRDAPROTO_ULTRA);</code></pre>
<h2>Description</h2>
<p><code>Linux-IrDA</code> is a complete implementation of the various <i>IrDA protocols</i> and <i>IrDA drivers</i> for Linux. </p>
<p> The configuration of the low level of the IrDA stack (IrDA ports) and the various IrDA drivers are described in <i><a href="/docs/linux/man/8-irattach/">irattach</a></i>(8). </p>
<p> The usage of the higher layers of the IrDA stack (IrCOMM, IrLPT, IrNET, IrLAN, OBEX&#8230;) are described in their respective man pages. </p>
<p> The core of the Linux-IrDA protocol stack is composed of the <i>IrLAP</i>, <i>IrLMP</i>, <i>IrTTP</i> and <i>IrIAS</i> protocols and is implemented as a kernel module. The programmer&#8217;s interface for the IrDA stack is socket based. For more information on sockets, see <a href="/docs/linux/man/7-socket/">socket</a>(7). </p>
<p> Note that higher level IrDA protocols may offer a different programmer&#8217;s interface. For example <i>IrCOMM</i> offers a TTY based interface and <i>OBEX</i> is available through a user space library.</p>
<h2>Sockets Type</h2>
<p>The Linux-IrDA socket interface offers 4 types of sockets:</p>
<dl>
<dt><code>Stream socket &#8211; SOCK_STREAM, 0</code></p>
<dd>Stream sockets provides a reliable, stream oriented, full duplex connection between two sockets on top of <i>IrTTP</i>, similar to TCP sockets. IrTTP guarantees that the data arrives in order and manages flow control, IrLAP retransmits lost packets.<br />
 Stream sockets does not preserve record boundaries.</p>
<dt><code>SeqPacket socket &#8211; SOCK_SEQPACKET, 0</code></p>
<dd>SeqPacket sockets provides a reliable, datagram oriented, full duplex connection between two sockets on top of <i>IrTTP</i>. IrTTP guarantees that the data arrives in order and manages flow control, IrLAP retransmits lost packets.<br />
 SeqPacket sockets preserve record boundaries. Large datagrams will be fragmented as needed.</p>
<dt><code>Datagram socket &#8211; SOCK_DGRAM, IRDAPROTO_UNITDATA</code></p>
<dd>SeqPacket sockets provides a reliable, datagram oriented, full duplex connection between two sockets on top of <i>IrLMP</i>. There is no guarantee that the data arrives in order and there is no flow control, however IrLAP retransmits lost packets.<br />
 Datagram sockets preserve record boundaries. No fragmentation is provided, datagrams larger than the IrDA link MTU are truncated or discarded.</p>
<dt><code>Ultra socket &#8211; SOCK_DGRAM, IRDAPROTO_ULTRA</code></p>
<dd>Ultra sockets provides a connectionless, unreliable datagram packet service on top of <i>IrLAP-Ultra</i>. Ultra datagrams are sent and received only when no IrLAP connection is established and otherwise discarded. They are always transmitted at 9600 bauds. Datagrams may be lost or reordered, and there is no flow control.<br />
 Ultra sockets preserve record boundaries. No fragmentation is provided, datagrams larger than the Ultra MTU (382 bytes) are truncated or discarded.</dl>
<h2>Address Format</h2>
<p>An <code>IrDA socket address</code> is defined as a combination of an IrDA interface address and a <i>service name</i>. Service names are automatically resolved to lsap through the <i>IrIAP</i> protocol. </p>
<pre> struct sockaddr_irda {
 sa_family_t sir_family; /* AF_IRDA */
 __u8 sir_lsap_sel; /* LSAP selector */
 __u32 sir_addr; /* Device address */
 char sir_name[25]; /* Usually &lt;service&gt;:IrDA:TinyTP */
 };</pre>
<p><i>sin_family</i> is always set to AF_IRDA. <i>sir_lsap_sel</i> is usually not used. <i>sir_addr</i> is the optional address of the peer (if no given the first peer discovered will be used). <i>sir_name</i> is the service name of the socket.</p>
<h2>Socket Options</h2>
<p>IrDA sockets supports some protocol specific socket options that can be set with <i><a href="/docs/linux/man/2-setsockopt/">setsockopt</a></i>(2) and read with <i><a href="/docs/linux/man/2-getsockopt/">getsockopt</a></i>(2). The socket option level for IrDA is SOL_IRLMP. </p>
<p> Options that can be set:</p>
<dl>
<dt><code>IRLMP_IAS_SET</code></p>
<dd>Set an entry in the local IAS database.</p>
<dt><code>IRLMP_IAS_DEL</code></p>
<dd>Delete an entry from the local IAS database.</p>
<dt><code>IRLMP_MAX_SDU_SIZE</code></p>
<dd>Set maximum receive MTU for SeqPacket sockets.</p>
<dt><code>IRLMP_HINTS_SET</code></p>
<dd>Set IrDA hint bits to be advertised to peers.</p>
<dt><code>IRLMP_HINT_MASK_SET</code></p>
<dd>Set IrDA hint bits filter to be used when performing discovery.</dl>
<p> Options that can be get:</p>
<dl>
<dt><code>IRLMP_ENUMDEVICES</code></p>
<dd>Perform link level discovery and return the content of the discovery log.</p>
<dt><code>IRLMP_MAX_SDU_SIZE</code></p>
<dd>Get maximum receive MTU.</p>
<dt><code>IRLMP_IAS_GET</code></p>
<dd>Get an entry from the local IAS database.</p>
<dt><code>IRLMP_IAS_QUERY</code></p>
<dd>Query an entry in IAS database of a peer using IrIAP.</p>
<dt><code>IRLMP_WAITDEVICE</code></p>
<dd>Block until a new device is discovered. Experimental feature, use with caution.</dl>
<h2>Author</h2>
<p>Jean Tourrilhes &#8211; jt [at] hpl.hp.com</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-irattach/">irattach</a></code>(8), <code><a href="/docs/linux/man/8-irdadump/">irdadump</a></code>(8), <code><a href="/docs/linux/man/4-irnet/">irnet</a></code>(4), <code><a href="/docs/linux/man/8-irnetd/">irnetd</a></code>(8). </p>
