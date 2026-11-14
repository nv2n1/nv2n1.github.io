---
title: "address_families(7)"
name: "address_families"
section: "7"
letter: "a"
url: "/docs/linux/man/7-address_families/"
description: "address_families – socket address families (domains)"
---

<p>address_families &#8211; socket address families (domains)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;sys/types.h&gt; /* See NOTES */

#include &lt;sys/socket.h&gt;
int socket(int domain, int type, int protocol);</code></pre>
<h2>Description</h2>
<p>The <i>domain</i> argument of the <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) specifies a communication domain; this selects the protocol family which will be used for communication. These families are defined in <i>&lt;sys/socket.h&gt;</i>. The formats currently understood by the Linux kernel include:</p>
<dl>
<dt><code>AF_UNIX</code>, <code>AF_LOCAL</code></p>
<dd>Local communication For further information, see <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7).</p>
<dt><code>AF_INET</code></p>
<dd>IPv4 Internet protocols. For further information, see <code><a href="/docs/linux/man/7-ip/">ip</a></code>(7).</p>
<dt><code>AF_AX25</code></p>
<dd>Amateur radio AX.25 protocol. For further information, see <code><a href="/docs/linux/man/4-ax25/">ax25</a></code>(4).</p>
<dt><code>AF_IPX</code></p>
<dd>IPX &#8211; Novell protocols.</p>
<dt><code>AF_APPLETALK</code></p>
<dd>AppleTalk For further information, see <code><a href="/docs/linux/man/7-ddp/">ddp</a></code>(7).</p>
<dt><code>AF_NETROM</code></p>
<dd>AX.25 packet layer protocol. For further information, see <code><a href="/docs/linux/man/4-netrom/">netrom</a></code>(4), <i>The Packet Radio Protocols and Linux</i> and the <i>AX.25</i>, <i>NET/ROM</i>, and <i>ROSE network programming</i> chapters of the <i>Linux Amateur Radio AX.25 HOWTO</i></p>
<dt><code>AF_BRIDGE</code></p>
<dd>Can&#8217;t be used for creating sockets; mostly used for bridge links in <code><a href="/docs/linux/man/7-rtnetlink/">rtnetlink</a></code>(7) protocol commands.</p>
<dt><code>AF_ATMPVC</code></p>
<dd>Access to raw ATM Permanent Virtual Circuits (PVCs). For further information, see the <i>ATM on Linux HOWTO</i></p>
<dt><code>AF_X25</code></p>
<dd>ITU-T X.25 / ISO-8208 protocol. For further information, see <code><a href="/docs/linux/man/7-x25/">x25</a></code>(7).</p>
<dt><code>AF_INET6</code></p>
<dd>IPv6 Internet protocols. For further information, see <code><a href="/docs/linux/man/7-ipv6/">ipv6</a></code>(7).</p>
<dt><code>AF_ROSE</code></p>
<dd>RATS (Radio Amateur Telecommunications Society) Open Systems environment (ROSE) AX.25 packet layer protocol. For further information, see the resources listed for <code>AF_NETROM</code>.</p>
<dt><code>AF_DECnet</code></p>
<dd>DECet protocol sockets. See <i>Documentation/networking/decnet.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_NETBEUI</code></p>
<dd>Reserved for &quot;802.2LLC project&quot;; never used.</p>
<dt><code>AF_SECURITY</code></p>
<dd>This was a short-lived (between Linux 2.1.30 and 2.1.99pre2) protocol family for firewall upcalls.</p>
<dt><code>AF_KEY</code></p>
<dd>Key management protocol, originally developed for usage with IPsec (since Linux 2.1.38). This has no relation to <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) and the in-kernel key storage facility. See RFC 2367 <i>PF_KEY Key Management API, Version 2</i> for details.</p>
<dt><code>AF_NETLINK</code></p>
<dd>Kernel user interface device For further information, see <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7).</p>
<dt><code>AF_PACKET</code></p>
<dd>Low-level packet interface. For further information, see <code><a href="/docs/linux/man/7-packet/">packet</a></code>(7).</p>
<dt><code>AF_ECONET</code></p>
<dd>Acorn Econet protocol (removed in Linux 3.5). See the Econet documentation for details.</p>
<dt><code>AF_ATMSVC</code></p>
<dd>Access to ATM Switched Virtual Circuits (SVCs) See the <i>ATM on Linux HOWTO</i> for details.</p>
<dt><code>AF_RDS</code></p>
<dd>Reliable Datagram Sockets (RDS) protocol (since Linux 2.6.30). RDS over RDMA has no relation to <code>AF_SMC</code> or <code>AF_XDP</code>. For further information see <code><a href="/docs/linux/man/7-rds/">rds</a></code>(7), <code><a href="/docs/linux/man/7-rds-rdma/">rds-rdma</a></code>(7), and <i>Documentation/networking/rds.txt</i> in the Linux kernel source tree.</p>
<dt><code>AF_IRDA</code></p>
<dd>Socket interface over IrDA (moved to staging in Linux 4.14, removed in Linux 4.17). For further information see <code><a href="/docs/linux/man/7-irda/">irda</a></code>(7).</p>
<dt><code>AF_PPPOX</code></p>
<dd>Generic PPP transport layer, for setting up L2 tunnels (L2TP and PPPoE). See <i>Documentation/networking/l2tp.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_WANPIPE</code></p>
<dd>Legacy protocol for wide area network (WAN) connectivity that was used by Sangoma WAN cards (called &quot;WANPIPE&quot;); removed in Linux 2.6.21.</p>
<dt><code>AF_LLC</code></p>
<dd>Logical link control (IEEE 802.2 LLC) protocol, upper part of data link layer of ISO/OSI networking protocol stack (since Linux 2.4); has no relation to <code>AF_PACKET</code>. See chapter <i>13.5.3. Logical Link Control</i> in <i>Understanding Linux Kernel Internals</i> (O&#8217;Reilly Media, 2006) and <i>IEEE Standards for Local Area Networks: Logical Link Control</i> (The Institute of Electronics and Electronics Engineers, Inc., New York, New York, 1985) for details. See also some historical notes regarding its development.</p>
<dt><code>AF_IB</code></p>
<dd>InfiniBand native addressing (since Linux 3.11).</p>
<dt><code>AF_MPLS</code></p>
<dd>Multiprotocol Label Switching (since Linux 4.1); mostly used for configuring MPLS routing via <code><a href="/docs/linux/man/7-netlink/">netlink</a></code>(7), as it doesn&#8217;t expose ability to create sockets to user space.</p>
<dt><code>AF_CAN</code></p>
<dd>Controller Area Network automotive bus protocol (since Linux 2.6.25). See <i>Documentation/networking/can.rst</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_TIPC</code></p>
<dd>TIPC, &quot;cluster domain sockets&quot; protocol (since Linux 2.6.16). See <i>TIPC Programmer&#8217;s Guide</i> and the protocol description for details.</p>
<dt><code>AF_BLUETOOTH</code></p>
<dd>Bluetooth low-level socket protocol (since Linux 3.11). See <i>Bluetooth Management API overview</i> and <i>An Introduction to Bluetooth Programming</i> by Albert Huang for details.</p>
<dt><code>AF_IUCV</code></p>
<dd>IUCV (inter-user communication vehicle) z/VM protocol for hypervisor-guest interaction (since Linux 2.6.21); has no relation to <code>AF_VSOCK</code> and/or <code>AF_SMC</code> See <i>IUCV protocol overview</i> for details.</p>
<dt><code>AF_RXRPC</code></p>
<dd>Rx, Andrew File System remote procedure call protocol (since Linux 2.6.22). See <i>Documentation/networking/rxrpc.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_ISDN</code></p>
<dd>New &quot;modular ISDN&quot; driver interface protocol (since Linux 2.6.27). See the mISDN wiki for details.</p>
<dt><code>AF_PHONET</code></p>
<dd>Nokia cellular modem IPC/RPC interface (since Linux 2.6.31). See <i>Documentation/networking/phonet.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_IEEE802154</code></p>
<dd>IEEE 802.15.4 WPAN (wireless personal area network) raw packet protocol (since Linux 2.6.31). See <i>Documentation/networking/ieee802154.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_CAIF</code></p>
<dd>Ericsson&#8217;s Communication CPU to Application CPU interface (CAIF) protocol (since Linux 2.6.36). See <i>Documentation/networking/caif/Linux-CAIF.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_ALG</code></p>
<dd>Interface to kernel crypto API (since Linux 2.6.38). See <i>Documentation/crypto/userspace-if.rst</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_VSOCK</code></p>
<dd>VMWare VSockets protocol for hypervisor-guest interaction (since Linux 3.9); has no relation to <code>AF_IUCV</code> and <code>AF_SMC</code>. For further information, see <code><a href="/docs/linux/man/7-vsock/">vsock</a></code>(7).</p>
<dt><code>AF_KCM</code></p>
<dd>KCM (kernel connection multiplexer) interface (since Linux 4.6). See <i>Documentation/networking/kcm.txt</i> in the Linux kernel source tree for details.</p>
<dt><code>AF_QIPCRTR</code></p>
<dd>Qualcomm IPC router interface protocol (since Linux 4.7).</p>
<dt><code>AF_SMC</code></p>
<dd>SMC-R (shared memory communications over RDMA) protocol (since Linux 4.11), and SMC-D (shared memory communications, direct memory access) protocol for intra-node z/VM quest interaction (since Linux 4.19); has no relation to <code>AF_RDS</code>, <code>AF_IUCV</code> or <code>AF_VSOCK</code>. See RFC 7609 <i>IBM&#8217;s Shared Memory Communications over RDMA (SMC-R) Protocol</i> for details regarding SMC-R. See <i>SMC-D Reference Information</i> for details regarding SMC-D.</p>
<dt><code>AF_XDP</code></p>
<dd>XDP (express data path) interface (since Linux 4.18). See <i>Documentation/networking/af_xdp.rst</i> in the Linux kernel source tree for details.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/2-socket/">socket</a></code>(2), <code><a href="/docs/linux/man/7-socket/">socket</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
