---
title: "tinc-conf(5)"
name: "tinc-conf"
section: "5"
letter: "t"
url: "/docs/linux/man/5-tinc-conf/"
description: "tinc.conf – tinc daemon configuration"
---

<p><code>tinc.conf</code> &#8211; tinc daemon configuration</p>
<h2>Description</h2>
<p>The files in the /etc/tinc/ directory contain runtime and security information for the tinc daemon.</p>
<h2>Networks</h2>
<p>It is perfectly ok for you to run more than one tinc daemon. However, in its default form, you will soon notice that you can&#8217;t use two different configuration files without the &#8211;<code>c</code> option. </p>
<p> We have thought of another way of dealing with this: network names. This means that you call with the &#8211;<code>n</code> option, which will assign a name to this daemon. </p>
<p> The effect of this is that the daemon will set its configuration root to /etc/tinc/ <i>NETNAME </i><code>/ </code> where <i>NETNAME</i> is your argument to the &#8211;<code>n</code> option. You&#8217;ll notice that messages appear in syslog as coming from <code>tincd. </code><i>NETNAME</i> </p>
<p> However, it is not strictly necessary that you call tinc with the &#8211;<code>n</code> option. In this case, the network name would just be empty, and it will be used as such. <code>tinc</code> now looks for files in /etc/tinc/ instead of /etc/tinc/ <i>NETNAME </i><code>/ </code> the configuration file should be /etc/tinc/tinc.conf and the host configuration files are now expected to be in /etc/tinc/hosts/ </p>
<p> But it is highly recommended that you use this feature of <code>tinc</code> because it will be so much clearer whom your daemon talks to. Hence, we will assume that you use it.</p>
<h2>Names</h2>
<p>Each tinc daemon must have a name that is unique in the network which it will be part of. The name will be used by other tinc daemons for identification. The name has to be declared in the /etc/tinc/ <i>NETNAME </i><code>/tinc.conf </code> file. </p>
<p> To make things easy, choose something that will give unique and easy to remember names to your tinc daemon(s). You could try things like hostnames, owner surnames or location names.</p>
<h2>Public/Private Keys</h2>
<p>You should use <code>tincd -K</code> to generate public/private keypairs. It will generate two keys. The private key should be stored in a separate file /etc/tinc/ <i>NETNAME </i><code>/rsa_key.priv </code> &#8212; where <i>NETNAME</i> stands for the network (see Sx NETWORKS ) above. The public key should be stored in the host configuration file /etc/tinc/ <i>NETNAME </i><code>/hosts/ </code><i>NAME</i> &#8212; where <i>NAME</i> stands for the name of the local tinc daemon (see Sx NAMES ) .</p>
<h2>Server Configuration</h2>
<p>The server configuration of the daemon is done in the file /etc/tinc/ <i>NETNAME </i><code>/tinc.conf </code> This file consists of comments (lines started with a <code>#</code> or assignments in the form of: </p>
<p> <i>Variable </i><code>= </code><i>Value</i> </p>
<p> The variable names are case insensitive, and any spaces, tabs, newlines and carriage returns are ignored. Note: it is not required that you put in the <code>=</code> sign, but doing so improves readability. If you leave it out, remember to replace it with at least one space character. </p>
<p> The server configuration is complemented with host specific configuration (see the next section). Although all configuration options for the local host listed in this document can also be put in /etc/tinc/ <i>NETNAME </i><code>/tinc.conf </code> it is recommended to put host specific configuration options in the host configuration file, as this makes it easy to exchange with other nodes. </p>
<p> Here are all valid variables, listed in alphabetical order. The default value is given between parentheses.</p>
<dl>
<dt><i>AddressFamily </i><code>= ipv4 | ipv6 | any (any) </code></p>
<dd>This option affects the address family of listening and outgoing sockets. If Qq any is selected, then depending on the operating system both IPv4 and IPv6 or just IPv6 listening sockets will be created.</p>
<dt><i>BindToAddress </i><code>= </code><i>address </i>[<i>port Bq </i>experimental ]</p>
<dd>If your computer has more than one IPv4 or IPv6 address, <code>tinc</code> will by default listen on all of them for incoming connections. Multiple <i>BindToAddress</i> variables may be specified, in which case listening sockets for each specified address are made. </p>
<p> If no <i>port</i> is specified, the socket will be bound to the port specified by the <i>Port</i> option, or to port 655 if neither is given. To only bind to a specific port but not to a specific address, use <code>*</code> for the <i>address</i> </p>
<p> This option may not work on all platforms.</p>
<dt><i>BindToInterface </i><code>= </code><i>interface Bq </i>experimental</p>
<dd>If your computer has more than one network interface, <code>tinc</code> will by default listen on all of them for incoming connections. It is possible to bind only to a single interface with this variable. </p>
<p> This option may not work on all platforms. Also, on some platforms it will not actually bind to an interface, but rather to the address that the interface has at the moment a socket is created.</p>
<dt><i>Broadcast </i><code>= no | mst | direct Po </code>mst Pc Bq experimental</p>
<dd>This option selects the way broadcast packets are sent to other daemons. NOTE: all nodes in a VPN must use the same <i>Broadcast</i> mode, otherwise routing loops can form.</p>
<dl>
<dt><code>no</code></p>
<dd>Broadcast packets are never sent to other nodes.</p>
<dt><code>mst</code></p>
<dd>Broadcast packets are sent and forwarded via the VPN&#8217;s Minimum Spanning Tree. This ensures broadcast packets reach all nodes.</p>
<dt><code>direct</code></p>
<dd>Broadcast packets are sent directly to all nodes that can be reached directly. Broadcast packets received from other nodes are never forwarded. If the IndirectData option is also set, broadcast packets will only be sent to nodes which we have a meta connection to.</dl>
<dt><i>ConnectTo </i><code>= </code><i>name</i></p>
<dd>Specifies which other tinc daemon to connect to on startup. Multiple <i>ConnectTo </i>variables may be specified, in which case outgoing connections to each specified tinc daemon are made. The names should be known to this tinc daemon (i.e., there should be a host configuration file for the name on the <i>ConnectTo </i>line). </p>
<p> If you don&#8217;t specify a host with <i>ConnectTo </i>, <code>tinc</code> won&#8217;t try to connect to other daemons at all, and will instead just listen for incoming connections.</p>
<dt><i>DecrementTTL </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When enabled, <code>tinc</code> will decrement the Time To Live field in IPv4 packets, or the Hop Limit field in IPv6 packets, before forwarding a received packet to the virtual network device or to another node, and will drop packets that have a TTL value of zero, in which case it will send an ICMP Time Exceeded packet back. </p>
<p> Do not use this option if you use switch mode and want to use IPv6.</p>
<dt><i>Device </i><code>= </code><i>device Po </i>/dev/tap0 , /dev/net/tun <code>or other depending on platform Pc </code>The virtual network device to use.</p>
<dd><code>tinc</code> will automatically detect what kind of device it is. Note that you can only use one device per daemon. Under Windows, use <i>Interface</i> instead of <i>Device</i> The info pages of the tinc package contain more information about configuring the virtual network device.</p>
<dt><i>DeviceType </i><code>= </code><i>type (platform dependent) </i></p>
<dd>The type of the virtual network device. Tinc will normally automatically select the right type of tun/tap interface, and this option should not be used. However, this option can be used to select one of the special interface types, if support for them is compiled in.</p>
<dl>
<dt><code>dummy</code></p>
<dd>Use a dummy interface. No packets are ever read or written to a virtual network device. Useful for testing, or when setting up a node that only forwards packets for other nodes.</p>
<dt><code>raw_socket</code></p>
<dd>Open a raw socket, and bind it to a pre-existing <i>Interface</i> (eth0 by default). All packets are read from this interface. Packets received for the local node are written to the raw socket. However, at least on Linux, the operating system does not process IP packets destined for the local host.</p>
<dt><code>multicast</code></p>
<dd>Open a multicast UDP socket and bind it to the address and port (separated by spaces) and optionally a TTL value specified using <i>Device</i> Packets are read from and written to this multicast socket. This can be used to connect to UML, QEMU or KVM instances listening on the same multicast address. Do NOT connect multiple <code>tinc </code> daemons to the same multicast address, this will very likely cause routing loops. Also note that this can cause decrypted VPN packets to be sent out on a real network if misconfigured.</p>
<dt><code>uml (not compiled in by default) </code></p>
<dd>Create a UNIX socket with the filename specified by <i>Device</i> or /var/run/ <i>NETNAME </i><code>.umlsocket </code> if not specified. <code>tinc</code> will wait for a User Mode Linux instance to connect to this socket.</p>
<dt><code>vde (not compiled in by default) </code></p>
<dd>Uses the libvdeplug library to connect to a Virtual Distributed Ethernet switch, using the UNIX socket specified by <i>Device</i> or /var/run/vde.ctl if not specified.</dl>
<p> Also, in case tinc does not seem to correctly interpret packets received from the virtual network device, it can be used to change the way packets are interpreted:</p>
<dl>
<dt><code>tun (BSD and Linux) </code></p>
<dd>Set type to tun. Depending on the platform, this can either be with or without an address family header (see below).</p>
<dt><code>tunnohead (BSD) </code></p>
<dd>Set type to tun without an address family header. Tinc will expect packets read from the virtual network device to start with an IP header. On some platforms IPv6 packets cannot be read from or written to the device in this mode.</p>
<dt><code>tunifhead (BSD) </code></p>
<dd>Set type to tun with an address family header. Tinc will expect packets read from the virtual network device to start with a four byte header containing the address family, followed by an IP header. This mode should support both IPv4 and IPv6 packets.</p>
<dt><code>utun (OS X) </code></p>
<dd>Set type to utun. This is only supported on OS X version 10.6.8 and higher, but doesn&#8217;t require the tuntaposx module. This mode should support both IPv4 and IPv6 packets.</p>
<dt><code>tap (BSD and Linux) </code></p>
<dd>Set type to tap. Tinc will expect packets read from the virtual network device to start with an Ethernet header.</dl>
<dt><i>DirectOnly </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When this option is enabled, packets that cannot be sent directly to the destination node, but which would have to be forwarded by an intermediate node, are dropped instead. When combined with the IndirectData option, packets for nodes for which we do not have a meta connection with are also dropped.</p>
<dt><i>Forwarding </i><code>= off | internal | kernel Po </code>internal Pc Bq experimental</p>
<dd>This option selects the way indirect packets are forwarded.</p>
<dl>
<dt><code>off</code></p>
<dd>Incoming packets that are not meant for the local node, but which should be forwarded to another node, are dropped.</p>
<dt><code>internal</code></p>
<dd>Incoming packets that are meant for another node are forwarded by tinc internally. </p>
<p> This is the default mode, and unless you really know you need another forwarding mode, don&#8217;t change it.</p>
<dt><code>kernel</code></p>
<dd>Incoming packets are always sent to the TUN/TAP device, even if the packets are not for the local node. This is less efficient, but allows the kernel to apply its routing and firewall rules on them, and can also help debugging.</dl>
<dt><i>GraphDumpFile </i><code>= </code><i>filename Bq </i>experimental</p>
<dd>If this option is present, <code>tinc</code> will dump the current network graph to the file <i>filename</i> every minute, unless there were no changes to the graph. The file is in a format that can be read by graphviz tools. If <i>filename</i> starts with a pipe symbol |, then the rest of the filename is interpreted as a shell command that is executed, the graph is then sent to stdin.</p>
<dt><i>Hostnames </i><code>= yes | no (no) </code></p>
<dd>This option selects whether IP addresses (both real and on the VPN) should be resolved. Since DNS lookups are blocking, it might affect tinc&#8217;s efficiency, even stopping the daemon for a few seconds every time it does a lookup if your DNS server is not responding. </p>
<p> This does not affect resolving hostnames to IP addresses from the host configuration files, but whether hostnames should be resolved while logging.</p>
<dt><i>IffOneQueue </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>(Linux only) Set IFF_ONE_QUEUE flag on TUN/TAP devices.</p>
<dt><i>Interface </i><code>= </code><i>interface</i></p>
<dd>Defines the name of the interface corresponding to the virtual network device. Depending on the operating system and the type of device this may or may not actually set the name of the interface. Under Windows, this variable is used to select which network interface will be used. If you specified a <i>Device</i> this variable is almost always already correctly set.</p>
<dt><i>KeyExpire </i><code>= </code><i>seconds (3600) </i></p>
<dd>This option controls the period the encryption keys used to encrypt the data are valid. It is common practice to change keys at regular intervals to make it even harder for crackers, even though it is thought to be nearly impossible to crack a single key.</p>
<dt><i>LocalDiscovery </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When enabled, <code>tinc</code> will try to detect peers that are on the same local network. This will allow direct communication using LAN addresses, even if both peers are behind a NAT and they only ConnectTo a third node outside the NAT, which normally would prevent the peers from learning each other&#8217;s LAN address. </p>
<p> Currently, local discovery is implemented by sending broadcast packets to the LAN during path MTU discovery. This feature may not work in all possible situations.</p>
<dt><i>MACExpire </i><code>= </code><i>seconds (600) </i></p>
<dd>This option controls the amount of time MAC addresses are kept before they are removed. This only has effect when <i>Mode</i> is set to Qq switch .</p>
<dt><i>MaxTimeout </i><code>= </code><i>seconds (900) </i></p>
<dd>This is the maximum delay before trying to reconnect to other tinc daemons.</p>
<dt><i>Mode </i><code>= router | switch | hub (router) </code></p>
<dd>This option selects the way packets are routed to other daemons.</p>
<dl>
<dt><code>router</code></p>
<dd>In this mode <i>Subnet</i> variables in the host configuration files will be used to form a routing table. Only unicast packets of routable protocols (IPv4 and IPv6) are supported in this mode. </p>
<p> This is the default mode, and unless you really know you need another mode, don&#8217;t change it.</p>
<dt><code>switch</code></p>
<dd>In this mode the MAC addresses of the packets on the VPN will be used to dynamically create a routing table just like an Ethernet switch does. Unicast, multicast and broadcast packets of every protocol that runs over Ethernet are supported in this mode at the cost of frequent broadcast ARP requests and routing table updates. </p>
<p> This mode is primarily useful if you want to bridge Ethernet segments.</p>
<dt><code>hub</code></p>
<dd>This mode is almost the same as the switch mode, but instead every packet will be broadcast to the other daemons while no routing table is managed.</dl>
<dt><i>Name </i><code>= </code><i>name Bq </i>required</p>
<dd>This is the name which identifies this tinc daemon. It must be unique for the virtual private network this daemon will connect to. The Name may only consist of alphanumeric and underscore characters. If <i>Name</i> starts with a <code>$</code> then the contents of the environment variable that follows will be used. In that case, invalid characters will be converted to underscores. If <i>Name</i> is <code>$HOST</code> but no such environment variable exist, the hostname will be read using the gethostname() system call.</p>
<dt><i>PingInterval </i><code>= </code><i>seconds (60) </i></p>
<dd>The number of seconds of inactivity that <code>tinc</code> will wait before sending a probe to the other end.</p>
<dt><i>PingTimeout </i><code>= </code><i>seconds (5) </i></p>
<dd>The number of seconds to wait for a response to pings or to allow meta connections to block. If the other end doesn&#8217;t respond within this time, the connection is terminated, and the others will be notified of this.</p>
<dt><i>PriorityInheritance </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When this option is enabled the value of the TOS field of tunneled IPv4 packets will be inherited by the UDP packets that are sent out.</p>
<dt><i>PrivateKey </i><code>= </code><i>key Bq </i>obsolete</p>
<dd>The private RSA key of this tinc daemon. It will allow this tinc daemon to authenticate itself to other daemons.</p>
<dt><i>PrivateKeyFile </i><code>= </code><i>filename Po </i>/etc/tinc/ <i>NETNAME </i><code>/rsa_key.priv Pc </code>The file in which the private RSA key of this tinc daemon resides.</p>
<dd>
<dt><i>ProcessPriority </i><code>= low | normal | high</code></p>
<dd>When this option is used the priority of the tincd process will be adjusted. Increasing the priority may help to reduce latency and packet loss on the VPN.</p>
<dt><i>Proxy </i><code>= socks4 | socks5 | http | exec </code><i>&#8230; Bq </i>experimental</p>
<dd>Use a proxy when making outgoing connections. The following proxy types are currently supported:</p>
<dl>
<dt><code>socks4 </code><i>address port </i>[<i>username</i> ]</p>
<dd>Connects to the proxy using the SOCKS version 4 protocol. Optionally, a <i>username</i> can be supplied which will be passed on to the proxy server. Only IPv4 connections can be proxied using SOCKS 4.</p>
<dt><code>socks5 </code><i>address port </i>[<i>username password</i> ]</p>
<dd>Connect to the proxy using the SOCKS version 5 protocol. If a <i>username</i> and <i>password</i> are given, basic username/password authentication will be used, otherwise no authentication will be used.</p>
<dt><code>http </code><i>address port</i></p>
<dd>Connects to the proxy and sends a HTTP CONNECT request.</p>
<dt><code>exec </code><i>command</i></p>
<dd>Executes the given <i>command</i> which should set up the outgoing connection. The environment variables <code>NAME</code> <code>NODE</code> <code>REMOTEADDRES</code> and <code>REMOTEPORT</code> are available.</dl>
<dt><i>ReplayWindow </i><code>= </code><i>bytes (16) </i></p>
<dd>This is the size of the replay tracking window for each remote node, in bytes. The window is a bitfield which tracks 1 packet per bit, so for example the default setting of 16 will track up to 128 packets in the window. In high bandwidth scenarios, setting this to a higher value can reduce packet loss from the interaction of replay tracking with underlying real packet loss and/or reordering. Setting this to zero will disable replay tracking completely and pass all traffic, but leaves tinc vulnerable to replay-based attacks on your traffic.</p>
<dt><i>StrictSubnets </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When this option is enabled tinc will only use Subnet statements which are present in the host config files in the local /etc/tinc/ <i>NETNAME </i><code>/hosts/ </code> directory. Subnets learned via connections to other nodes and which are not present in the local host config files are ignored.</p>
<dt><i>TunnelServer </i><code>= yes | no Po </code>no Pc Bq experimental</p>
<dd>When this option is enabled tinc will no longer forward information between other tinc daemons, and will only allow connections with nodes for which host config files are present in the local /etc/tinc/ <i>NETNAME </i><code>/hosts/ </code> directory. Setting this options also implicitly sets StrictSubnets.</p>
<dt><i>UDPRcvBuf </i><code>= </code><i>bytes (OS default) </i></p>
<dd>Sets the socket receive buffer size for the UDP socket, in bytes. If unset, the default buffer size will be used by the operating system.</p>
<dt><i>UDPSndBuf </i><code>= </code><i>bytes (OS default) </i></p>
<dd>Sets the socket send buffer size for the UDP socket, in bytes. If unset, the default buffer size will be used by the operating system.</dl>
<h2>Host Configuration Files</h2>
<p>The host configuration files contain all information needed to establish a connection to those hosts. A host configuration file is also required for the local tinc daemon, it will use it to read in it&#8217;s listen port, public key and subnets. </p>
<p> The idea is that these files are portable. You can safely mail your own host configuration file to someone else. That other person can then copy it to his own hosts directory, and now his tinc daemon will be able to connect to your tinc daemon. Since host configuration files only contain public keys, no secrets are revealed by sending out this information.</p>
<dl>
<dt><i>Address </i><code>= </code><i>address </i>[<i>port Bq </i>recommended ]</p>
<dd>The IP address or hostname of this tinc daemon on the real network. This will only be used when trying to make an outgoing connection to this tinc daemon. Optionally, a port can be specified to use for this address. Multiple <i>Address</i> variables can be specified, in which case each address will be tried until a working connection has been established.</p>
<dt><i>Cipher </i><code>= </code><i>cipher (aes-256-cbc) </i></p>
<dd>The symmetric cipher algorithm used to encrypt UDP packets. Any cipher supported by LibreSSL or OpenSSL is recognised. Furthermore, specifying Qq none will turn off packet encryption. It is best to use only those ciphers which support CBC mode.</p>
<dt><i>ClampMSS </i><code>= yes | no (yes) </code></p>
<dd>This option specifies whether tinc should clamp the maximum segment size (MSS) of TCP packets to the path MTU. This helps in situations where ICMP Fragmentation Needed or Packet too Big messages are dropped by firewalls.</p>
<dt><i>Compression </i><code>= </code><i>level (0) </i></p>
<dd>This option sets the level of compression used for UDP packets. Possible values are 0 (off), 1 (fast zlib) and any integer up to 9 (best zlib), 10 (fast lzo) and 11 (best lzo).</p>
<dt><i>Digest </i><code>= </code><i>digest (sha256) </i></p>
<dd>The digest algorithm used to authenticate UDP packets. Any digest supported by LibreSSL or OpenSSL is recognised. Furthermore, specifying Qq none will turn off packet authentication.</p>
<dt><i>IndirectData </i><code>= yes | no (no) </code></p>
<dd>When set to yes, only nodes which already have a meta connection to you will try to establish direct communication with you. It is best to leave this option out or set it to no.</p>
<dt><i>MACLength </i><code>= </code><i>length (4) </i></p>
<dd>The length of the message authentication code used to authenticate UDP packets. Can be anything from Qq 0 up to the length of the digest produced by the digest algorithm.</p>
<dt><i>PMTU </i><code>= </code><i>mtu Po </i>1514 Pc This option controls the initial path MTU to this node.</p>
<dd>
<dt><i>PMTUDiscovery </i><code>= yes | no Po </code>yes Pc When this option is enabled, tinc will try to discover the path MTU to this node.</p>
<dd>After the path MTU has been discovered, it will be enforced on the VPN.</p>
<dt><i>Port </i><code>= </code><i>port (655) </i></p>
<dd>The port number on which this tinc daemon is listening for incoming connections, which is used if no port number is specified in an <i>Address</i> statement.</p>
<dt><i>PublicKey </i><code>= </code><i>key Bq </i>obsolete</p>
<dd>The public RSA key of this tinc daemon. It will be used to cryptographically verify it&#8217;s identity and to set up a secure connection.</p>
<dt><i>PublicKeyFile </i><code>= </code><i>filename Bq </i>obsolete</p>
<dd>The file in which the public RSA key of this tinc daemon resides. </p>
<p> From version 1.0pre4 on <code>tinc</code> will store the public key directly into the host configuration file in PEM format, the above two options then are not necessary. Either the PEM format is used, or exactly one of the above two options must be specified in each host configuration file, if you want to be able to establish a connection with that host.</p>
<dt><i>Subnet </i><code>= </code><i>address </i>[<code>/ </code><i>prefixlength </i>[<code># </code><i>weight</i> ] ]</p>
<dd>The subnet which this tinc daemon will serve. <code>tinc</code> tries to look up which other daemon it should send a packet to by searching the appropriate subnet. If the packet matches a subnet, it will be sent to the daemon who has this subnet in his host configuration file. Multiple <i>Subnet</i> variables can be specified. </p>
<p> Subnets can either be single MAC, IPv4 or IPv6 addresses, in which case a subnet consisting of only that single address is assumed, or they can be a IPv4 or IPv6 network address with a prefixlength. For example, IPv4 subnets must be in a form like 192.168.1.0/24, where 192.168.1.0 is the network address and 24 is the number of bits set in the netmask. Note that subnets like 192.168.1.1/24 are invalid! Read a networking HOWTO/FAQ/guide if you don&#8217;t understand this. IPv6 subnets are notated like fec0:0:0:1::/64. MAC addresses are notated like 0:1a:2b:3c:4d:5e. </p>
<p> A Subnet can be given a weight to indicate its priority over identical Subnets owned by different nodes. The default weight is 10. Lower values indicate higher priority. Packets will be sent to the node with the highest priority, unless that node is not reachable, in which case the node with the next highest priority will be tried, and so on.</p>
<dt><i>TCPOnly </i><code>= yes | no (no Bq </code>obsolete )</p>
<dd>If this variable is set to yes, then the packets are tunnelled over the TCP connection instead of a UDP connection. This is especially useful for those who want to run a tinc daemon from behind a masquerading firewall, or if UDP packet routing is disabled somehow. Setting this options also implicitly sets IndirectData. </p>
<p> Since version 1.0.10, tinc will automatically detect whether communication via UDP is possible or not.</dl>
<h2>Scripts</h2>
<p>Apart from reading the server and host configuration files, tinc can also run scripts at certain moments. Below is a list of filenames of scripts and a description of when they are run. A script is only run if it exists and if it is executable. </p>
<p> Scripts are run synchronously; this means that tinc will temporarily stop processing packets until the called script finishes executing. This guarantees that scripts will execute in the exact same order as the events that trigger them. If you need to run commands asynchronously, you have to ensure yourself that they are being run in the background. </p>
<p> Under Windows (not Cygwin), the scripts must have the extension .bat</p>
<dl>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/tinc-up </code></p>
<dd>This is the most important script. If it is present it will be executed right after the tinc daemon has been started and has connected to the virtual network device. It should be used to set up the corresponding network interface, but can also be used to start other things. </p>
<p> Under Windows you can use the Network Connections control panel instead of creating this script.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/tinc-down </code></p>
<dd>This script is started right before the tinc daemon quits.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/hosts/ </code><i>HOST </i><code>-up </code></p>
<dd>This script is started when the tinc daemon with name <i>HOST</i> becomes reachable.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/hosts/ </code><i>HOST </i><code>-down </code></p>
<dd>This script is started when the tinc daemon with name <i>HOST</i> becomes unreachable.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/host-up </code></p>
<dd>This script is started when any host becomes reachable.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/host-down </code></p>
<dd>This script is started when any host becomes unreachable.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/subnet-up </code></p>
<dd>This script is started when a Subnet becomes reachable. The Subnet and the node it belongs to are passed in environment variables.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/subnet-down </code></p>
<dd>This script is started when a Subnet becomes unreachable.</dl>
<p> The scripts are started without command line arguments, but can make use of certain environment variables. Under UNIX like operating systems the names of environment variables must be preceded by a <code>$ </code> in scripts. Under Windows, in .bat files, they have to be put between <code>%</code> signs.</p>
<dl>
<dt><code>NETNAME</code></p>
<dd>If a netname was specified, this environment variable contains it.</p>
<dt><code>NAME</code></p>
<dd>Contains the name of this tinc daemon.</p>
<dt><code>DEVICE</code></p>
<dd>Contains the name of the virtual network device that tinc uses.</p>
<dt><code>INTERFACE</code></p>
<dd>Contains the name of the virtual network interface that tinc uses. This should be used for commands like ifconfig</p>
<dt><code>NODE</code></p>
<dd>When a host becomes (un)reachable, this is set to its name. If a subnet becomes (un)reachable, this is set to the owner of that subnet.</p>
<dt><code>REMOTEADDRESS</code></p>
<dd>When a host becomes (un)reachable, this is set to its real address.</p>
<dt><code>REMOTEPORT</code></p>
<dd>When a host becomes (un)reachable, this is set to the port number it uses for communication with other tinc daemons.</p>
<dt><code>SUBNET</code></p>
<dd>When a subnet becomes (un)reachable, this is set to the subnet.</p>
<dt><code>WEIGHT</code></p>
<dd>When a subnet becomes (un)reachable, this is set to the subnet weight.</dl>
<p> Do not forget that under UNIX operating systems, you have to make the scripts executable, using the command <code>chmod a+x script </code></p>
<h2>Files</h2>
<p>The most important files are:</p>
<dl>
<dt><code>/etc/tinc/ </code></p>
<dd>The top directory for configuration files.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/tinc.conf </code></p>
<dd>The default name of the server configuration file for net <i>NETNAME</i></p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/conf.d/ </code></p>
<dd>Optional directory from which any *.conf file will be loaded</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/hosts/ </code></p>
<dd>Host configuration files are kept in this directory.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/tinc-up </code></p>
<dd>If an executable file with this name exists, it will be executed right after the tinc daemon has connected to the virtual network device. It can be used to set up the corresponding network interface.</p>
<dt><code>/etc/tinc/ </code><i>NETNAME </i><code>/tinc-down </code></p>
<dd>If an executable file with this name exists, it will be executed right before the tinc daemon is going to close its connection to the virtual network device.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-tincd/">tincd</a>(8), <a rel="nofollow" href="https://www.tinc-vpn.org/">https://www.tinc-vpn.org/</a> <a rel="nofollow" href="http://www.tldp.org/LDP/nag2/">http://www.tldp.org/LDP/nag2/</a> The full documentation for <code>tinc</code> is maintained as a Texinfo manual. If the info and tinc programs are properly installed at your site, the command <code>info tinc</code> should give you access to the complete manual. <code>tinc</code> comes with ABSOLUTELY NO WARRANTY. This is free software, and you are welcome to redistribute it under certain conditions; see the file COPYING for details. </p>
