---
title: "ipsec_pluto(8)"
name: "ipsec_pluto"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ipsec_pluto/"
description: "ipsec_pluto, ipsec_whack, pluto – ipsec whack : IPsec IKE keying daemon and control interface"
---

<p>ipsec_pluto, ipsec_whack, pluto &#8211; ipsec whack : IPsec IKE keying daemon and control interface</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ipsec</code> <i>pluto</i> [&#8211;help] [&#8211;version] [&#8211;leak-detective] [&#8211;config&nbsp;<wbr><i>filename</i>] [&#8211;vendorid&nbsp;<wbr><i>VID</i>] [&#8211;nofork] [&#8211;stderrlog] [&#8212;-plutostderrlogtime] [&#8211;logfile&nbsp;<wbr><i>filename</i>] [&#8211;use-klips] [&#8211;use-mast] [&#8211;use-netkey] [&#8211;use-nostack] [&#8211;uniqueids] [&#8211;virtual-private&nbsp;<wbr><i>network_list</i>] [&#8211;keep-alive&nbsp;<wbr><i>delay_sec</i>] [&#8211;force-busy] [&#8211;nocrsend] [&#8211;strictcrlpolicy] [&#8211;crlcheckinterval] [&#8211;interface&nbsp;<wbr><i>interfacename</i>] [&#8211;listen&nbsp;<wbr><i>ipaddr</i>] [&#8211;ikeport&nbsp;<wbr><i>portnumber</i>] [&#8211;natikeport&nbsp;<wbr><i>portnumber</i>] [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;secretsfile&nbsp;<wbr><i>secrets-file</i>] [&#8211;nhelpers&nbsp;<wbr><i>number</i>] [&#8211;seedbits&nbsp;<wbr><i>numbits</i>] [&#8211;perpeerlog] [&#8211;perpeerlogbase&nbsp;<wbr><i>dirname</i>] [&#8211;ipsecdir&nbsp;<wbr><i>dirname</i>] [&#8211;nssdir&nbsp;<wbr><i>dirname</i>] [&#8211;coredir&nbsp;<wbr><i>dirname</i>] [&#8211;statsbin&nbsp;<wbr><i>filename</i>] [&#8211;secctx-attr-type&nbsp;<wbr><i>number</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> [&#8211;help] [&#8211;version]</p>
<dt> <code>ipsec</code> <i>whack</i> [&#8211;debug-none] [&#8211;debug-all] [&#8211;debug-raw] [&#8211;debug-crypt] [&#8211;debug-parsing] [&#8211;debug-emitting] [&#8211;debug-control] [&#8211;debug-lifecycle] [&#8211;debug-kernel] [&#8211;debug-pfkey] [&#8211;debug-nat-t] [&#8211;debug-dpd] [&#8211;debug-dns] [&#8211;debug-oppo] [&#8211;debug-oppoinfo] [&#8211;debug-whackwatch] [&#8211;debug-private] [&#8211;debug-x509]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;name&nbsp;<wbr><i>connection-name</i> [[&#8211;ipv4] | [&#8211;ipv6]] [[&#8211;tunnelipv4] | [&#8211;tunnelipv6]]</p>
<dd>[&#8211;id&nbsp;<wbr><i>identity</i>] [&#8211;host&nbsp;<wbr><i>ip-address</i>] [&#8211;cert&nbsp;<wbr><i>friendly_name</i>] [&#8211;ckaid&nbsp;<wbr><i>CKAID</i>] [&#8211;ca&nbsp;<wbr><i>distinguished name</i>] [&#8211;groups&nbsp;<wbr><i>access control groups</i>] [&#8211;sendcert yes | forced | always | ifasked | no | never] [&#8211;sendca none | issuer | all] [&#8211;certtype&nbsp;<wbr><i>number</i>] [&#8211;ikeport&nbsp;<wbr><i>portnumber</i>] [&#8211;nexthop&nbsp;<wbr><i>ip-address</i>] [[&#8211;client&nbsp;<wbr><i>subnet</i>] | [&#8211;clientwithin&nbsp;<wbr><i>subnet</i>]] [&#8211;clientprotoport&nbsp;<wbr><i>protocol</i>/<i>port</i>] [&#8211;srcip&nbsp;<wbr><i>ip-address</i>] [&#8211;xauthserver] [&#8211;xauthclient] [&#8211;modecfgserver] [&#8211;modecfgclient] [&#8211;modecfgdns1&nbsp;<wbr><i>ip-address</i>] [&#8211;modecfgdns2&nbsp;<wbr><i>ip-address</i>] [&#8211;modecfgdomain&nbsp;<wbr><i>DNS-domain</i>] [&#8211;modecfgbanner&nbsp;<wbr><i>login-banner</i>] [&#8211;dnskeyondemand] [&#8211;updown&nbsp;<wbr><i>updown</i>]</p>
<dd>&#8211;to</p>
<dd>[&#8211;id&nbsp;<wbr><i>identity</i>] [&#8211;host&nbsp;<wbr><i>ip-address</i>] [&#8211;cert&nbsp;<wbr><i>friendly_name</i>] [&#8211;ckaid&nbsp;<wbr><i>CKAID</i>] [&#8211;ca&nbsp;<wbr><i>distinguished name</i>] [&#8211;groups&nbsp;<wbr><i>access control groups</i>] [&#8211;sendcert yes | always | ifasked | no | never] [&#8211;certtype&nbsp;<wbr><i>number</i>] [&#8211;ikeport&nbsp;<wbr><i>port-number</i>] [&#8211;nexthop&nbsp;<wbr><i>ip-address</i>] [&#8211;client&nbsp;<wbr><i>subnet</i>] [&#8211;clientwithin&nbsp;<wbr><i>subnet</i>] [&#8211;clientprotoport&nbsp;<wbr><i>protocol</i>/<i>port</i>] [&#8211;srcip&nbsp;<wbr><i>ip-address</i>] [&#8211;xauthserver] [&#8211;xauthclient] [&#8211;modecfgserver] [&#8211;modecfgclient] [&#8211;modecfgdns1&nbsp;<wbr><i>ip-address</i>] [&#8211;modecfgdns2&nbsp;<wbr><i>ip-address</i>] [&#8211;modecfgdomain&nbsp;<wbr><i>DNS-domain</i>] [&#8211;dnskeyondemand] [&#8211;updown&nbsp;<wbr><i>updown</i>]</p>
<dd>
<dd>[&#8211;tunnel] [&#8211;psk] [&#8211;rsasig] [&#8211;encrypt] [&#8211;authenticate] [&#8211;compress] [&#8211;pfs] [&#8211;pfsgroup&nbsp;<wbr>[modp1024]&nbsp;<wbr>|&nbsp;<wbr>[modp1536]&nbsp;<wbr>|&nbsp;<wbr>[modp2048]&nbsp;<wbr>|&nbsp;<wbr>[modp3072]&nbsp;<wbr>|&nbsp;<wbr>[modp4096]&nbsp;<wbr>|&nbsp;<wbr>[modp6144]&nbsp;<wbr>|&nbsp;<wbr>[modp8192]&nbsp;<wbr>|&nbsp;<wbr>[dh22]&nbsp;<wbr>|&nbsp;<wbr>[dh23]&nbsp;<wbr>|&nbsp;<wbr>[dh24]] [&#8211;disablearrivalcheck] [&#8211;ikelifetime&nbsp;<wbr><i>seconds</i>] [&#8211;ipseclifetime&nbsp;<wbr><i>seconds</i>] [&#8211;rekeymargin&nbsp;<wbr><i>seconds</i>] [&#8211;rekeyfuzz&nbsp;<wbr><i>percentage</i>] [&#8211;keyingtries&nbsp;<wbr><i>count</i>] [&#8211;esp&nbsp;<wbr><i>esp-algos</i>] [&#8211;dontrekey] [&#8211;aggrmode] [&#8211;modecfgpull] [&#8211;metric&nbsp;<wbr><i>metric</i>] [&#8211;nflog-group&nbsp;<wbr><i>nflognum</i>] [&#8211;conn-mark&nbsp;<wbr><i>mark/mask</i>] [[&#8211;dpddelay&nbsp;<wbr><i>seconds</i>] | [&#8211;dpdtimeout&nbsp;<wbr><i>seconds</i>]] [&#8211;dpdaction&nbsp;<wbr>[clear]&nbsp;<wbr>|&nbsp;<wbr>[hold]&nbsp;<wbr>|&nbsp;<wbr>[restart]] [&#8211;forceencaps] [&#8211;no-keep-alive] [[&#8211;initiateontraffic]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;pass]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;drop]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;reject]] [[&#8211;failnone]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;failpass]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;faildrop]&nbsp;<wbr>|&nbsp;<wbr>[&#8211;failreject]] [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;keyid&nbsp;<wbr><i>id</i> [&#8211;addkey] [&#8211;pubkeyrsa&nbsp;<wbr><i>key</i>] [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;myid&nbsp;<wbr><i>id</i></p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;listen | &#8211;unlisten [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;busy | &#8211;relax [&#8211;ctlbase&nbsp;<wbr><i>path</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;route | &#8211;unroute &#8211;name&nbsp;<wbr><i>connection-name</i> [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;initiate | [&#8211;remote-host&nbsp;<wbr><i>ip-address</i>] | &#8211;terminate &#8211;name&nbsp;<wbr><i>connection-name</i> [&#8211;xauthuser&nbsp;<wbr><i>user</i>] [&#8211;xauthpass&nbsp;<wbr><i>pass</i>] [&#8211;asynchronous] [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> [[&#8211;tunnelipv4] | [&#8211;tunnelipv6]] &#8211;oppohere&nbsp;<wbr><i>ip-address</i> &#8211;oppothere&nbsp;<wbr><i>ip-address</i></p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;crash [ipaddress]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;whackrecord [filename]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;whackstoprecord</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;name&nbsp;<wbr><i>connection-name</i> &#8211;delete [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;deletestate&nbsp;<wbr><i>state-number</i> [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;deleteuser &#8211;name&nbsp;<wbr><i>username</i> [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> [&#8211;name&nbsp;<wbr><i>connection-name</i>] [&#8211;debug-none] [&#8211;debug-all] [&#8211;debug-raw] [&#8211;debug-crypt] [&#8211;debug-parsing] [&#8211;debug-emitting] [&#8211;debug-control] [&#8211;debug-controlmore] [&#8211;debug-lifecycle] [&#8211;debug-klips] [&#8211;debug-pfkey] [&#8211;debug-dns] [&#8211;debug-dpd] [&#8211;debug-natt] [&#8211;debug-oppo] [&#8211;debug-oppoinfo] [&#8211;debug-whackwatch] [&#8211;debug-private] [&#8211;impair-bust-mi2] [&#8211;impair-bust-mr2] [&#8211;impair-sa-fail] [&#8211;impair-die-oninfo] [&#8211;impair-jacob-two-two] [&#8211;impair-major-version-bump] [&#8211;impair-minor-version-bump] [&#8211;impair-retransmits] [&#8211;impair-send-bogus-isakmp-flag] [&#8211;impair-send-ikev2-ke] [&#8211;impair-send-key-size-check] [&#8211;impair-send-no-delete]</p>
<dt> <code>ipsec</code> <i>whack</i> [&#8211;utc] [&#8211;listall] [&#8211;listpubkeys] [&#8211;listcerts] [&#8211;listcacerts] [&#8211;listcrls]</p>
<dt> <code>ipsec</code> <i>whack</i> [&#8211;utc] [&#8211;rereadsecrets] [&#8211;fetchcrls] [&#8211;rereadall]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;listevents</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;purgeocsp</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;status [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;trafficstatus &#8211;shuntstatus [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</p>
<dt> <code>ipsec</code> <i>whack</i> &#8211;shutdown [&#8211;ctlbase&nbsp;<wbr><i>path</i>] [&#8211;label&nbsp;<wbr><i>string</i>]</dl>
<h2>Description</h2>
<p><code>pluto</code></p>
<dd>is an IKE (&quot;IPsec Key Exchange&quot;) daemon. <code>whack</code> is an auxiliary program to allow requests to be made to a running <code>pluto</code>. </p>
<p> <code>pluto</code> is used to automatically build shared &quot;security associations&quot; on a system that has IPsec, the secure IP protocol. In other words, <code>pluto</code> can eliminate much of the work of manual keying. The actual secure transmission of packets is the responsibility of other parts of the system &#8211; the kernel. Pluto can talk to various kernel implementations, such as <code>KLIPS</code>, such as <code>NETKEY</code>, and such as <code>KAME</code> IPsec stacks. <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) provides a more convenient interface to <code>pluto</code> and <code>whack</code>.</p>
<h3>IKE&#8217;s Job</h3>
<p>A <i>Security Association</i> (<i>SA</i>) is an agreement between two network nodes on how to process certain traffic between them. This processing involves encapsulation, authentication, encryption, or compression. </p>
<p> IKE can be deployed on a network node to negotiate Security Associations for that node. These IKE implementations can only negotiate with other IKE implementations, so IKE must be on each node that is to be an endpoint of an IKE-negotiated Security Association. No other nodes need to be running IKE. </p>
<p> An IKE instance (i.e. an IKE implementation on a particular network node) communicates with another IKE instance using UDP IP packets, so there must be a route between the nodes in each direction. </p>
<p> The negotiation of Security Associations requires a number of choices that involve tradeoffs between security, convenience, trust, and efficiency. These are policy issues and are normally specified to the IKE instance by the system administrator. </p>
<p> IKE deals with two kinds of Security Associations. The first part of a negotiation between IKE instances is to build an ISAKMP SA. An ISAKMP SA is used to protect communication between the two IKEs. IPsec SAs can then be built by the IKEs &#8211; these are used to carry protected IP traffic between the systems. </p>
<p> The negotiation of the ISAKMP SA is known as Phase 1. In theory, Phase 1 can be accomplished by a couple of different exchange types. Currently, Main Mode and Aggressive Mode are implemented. </p>
<p> Any negotiation under the protection of an ISAKMP SA, including the negotiation of IPsec SAs, is part of Phase 2. The exchange type that we use to negotiate an IPsec SA is called Quick Mode. </p>
<p> IKE instances must be able to authenticate each other as part of their negotiation of an ISAKMP SA. This can be done by several mechanisms described in the draft standards. </p>
<p> IKE negotiation can be initiated by any instance with any other. If both can find an agreeable set of characteristics for a Security Association, and both recognize each others authenticity, they can set up a Security Association. The standards do not specify what causes an IKE instance to initiate a negotiation. </p>
<p> In summary, an IKE instance is prepared to automate the management of Security Associations in an IPsec environment, but a number of issues are considered policy and are left in the system administrator&#8217;s hands.</p>
<h3>Pluto</h3>
<p><code>pluto</code> is an implementation of IKE. It runs as a daemon on a network node. Currently, this network node must be a LINUX system running the <code>KLIPS</code> or <code>NETKEY</code> implementation of IPsec, or a FreeBSD/NetBSD/Mac OSX system running the <code>KAME</code> implementation of IPsec. </p>
<p> <code>pluto</code> implements a large subset of IKE. This is enough for it to interoperate with other instances of <code>pluto</code>, and many other IKE implementations. </p>
<p> The policy for acceptable characteristics for Security Associations is mostly hardwired into the code of <code>pluto</code> (spdb.c). Eventually this will be moved into a security policy database with reasonable expressive power and more convenience. </p>
<p> <code>pluto</code> uses shared secrets or RSA signatures to authenticate peers with whom it is negotiating. These RSA signatures can come from DNS(SEC), a configuration file, or from X.509 and CA certificates. </p>
<p> <code>pluto</code> initiates negotiation of a Security Association when it is manually prodded: the program <code>whack</code> is run to trigger this. It will also initiate a negotiation when <code>KLIPS</code> traps an outbound packet for Opportunistic Encryption. </p>
<p> <code>pluto</code> implements ISAKMP SAs itself. After it has negotiated the characteristics of an IPsec SA, it directs the <code>kernel</code> to implement it. If necessary, it also invokes a script to adjust any firewall and issue <code><a href="/docs/linux/man/8-route/">route</a></code>(8) commands to direct IP packets. </p>
<p> When <code>pluto</code> shuts down, it closes all Security Associations.</p>
<h3>Before Running Pluto</h3>
<p><code>pluto</code> runs as a daemon with userid root. Before running it, a few things must be set up. </p>
<p> <code>pluto</code> requires a working IPsec stack. </p>
<p> <code>pluto</code> supports multiple public networks (that is, networks that are considered insecure and thus need to have their traffic encrypted or authenticated). It discovers the public interfaces to use by looking at all interfaces that are configured (the <code>&#8211;interface</code> option can be used to limit the interfaces considered). It does this only when <code>whack</code> tells it to &#8211;listen, so the interfaces must be configured by then. Each interface with a name of the form <code>ipsec</code>[0-9] is taken as a <code>KLIPS</code> virtual public interface. Another network interface with the same IP address (the first one found will be used) is taken as the corresponding real public interface. The <code>&#8211;listen</code> can be used to limit listening on only 1 IP address of a certain interface. <code><a href="/docs/linux/man/8-ifconfig/">ifconfig</a></code>(8) or <code><a href="/docs/linux/man/8-ip/">ip</a></code>(8) with the <code>-a</code> flag will show the name and status of each network interface. </p>
<p> <code>pluto</code> requires a database of preshared secrets and RSA private keys. This is described in the <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5). <code>pluto</code> is told of RSA public keys via <code>whack</code> commands. If the connection is Opportunistic, and no RSA public key is known, <code>pluto</code> will attempt to fetch RSA keys using the Domain Name System.</p>
<h3>Setting up KLIPS for pluto</h3>
<p>The most basic network topology that <code>pluto</code> supports has two security gateways negotiating on behalf of client subnets. The diagram of RGB&#8217;s testbed is a good example (see <i>klips/doc/rgb_setup.txt</i>). </p>
<p> The file INSTALL in the base directory of this distribution explains how to start setting up the whole system, including <code>KLIPS</code>. </p>
<p> Make sure that the security gateways have routes to each other. This is usually covered by the default route, but may require issuing <code><a href="/docs/linux/man/8-route/">route</a></code>(8) commands. The route must go through a particular IP interface (we will assume it is <i>eth0</i>, but it need not be). The interface that connects the security gateway to its client must be a different one. </p>
<p> It is necessary to issue a <code><a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a></code>(8) command on each gateway. The required command is: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec tncfg &#8211;attach &#8211;virtual ipsec0 &#8211;physical eth0 </p>
<p> A command to set up the ipsec0 virtual interface will also need to be run. It will have the same parameters as the command used to set up the physical interface to which it has just been connected using <code><a href="/docs/linux/man/8-ipsec_tncfg/">ipsec_tncfg</a></code>(8).</p>
<h3>Setting up NETKEY for pluto</h3>
<p>No special requirements are necessary to use NETKEY &#8211; it ships with all modern versions of Linux 2.4 and 2.6. however, note that certain vendors or older distributions use old versions or backports of NETKEY which are broken. If possible use a NETKEY version that is at least based on, or backported from Linux 2.6.11 or newer.</p>
<h3>ipsec.secrets file</h3>
<p>A <code>pluto</code> daemon and another IKE daemon (for example, another instance of <code>pluto</code>) must convince each other that they are who they are supposed to be before any negotiation can succeed. This authentication is accomplished by using either secrets that have been shared beforehand (manually) or by using RSA signatures. There are other techniques, but they have not been implemented in <code>pluto</code>. </p>
<p> The file /etc/ipsec.secrets is used to keep preshared secret keys and XAUTH passwords. RSA private keys, X.509 certificates, CRLs, OCSP and smartcards are handled via NSS. For debugging, there is an argument to the <code>pluto</code> command to use a different file. This file is described in <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5).</p>
<h3>Running Pluto</h3>
<p>To fire up the daemon, just type <code>pluto</code> (be sure to be running as the superuser). The default IKE port number is 500, the UDP port assigned by IANA for IKE Daemons. <code>pluto</code> must be run by the superuser to be able to use the UDP 500 port. If pluto is told to enable NAT-Traversal, then UDP port 4500 is also taken by pluto to listen on. </p>
<p> Pluto supports different IPstacks on different operating systems. This can be configured using one of the options <code>&#8211;use-netkey</code> (the default), <code>&#8211;use-klips</code>, <code>&#8211;use-mast</code>, <code>&#8211;use-bsdkame</code>, <code>&#8211;use-win2k</code> or <code>&#8211;use-nostack</code>. The latter is meant for testing only &#8211; no actual IPsec connections will be loaded into the kernel. The option <code>&#8211;use-auto</code> has been obsoleted. On startup, pluto might also read the <code>protostack=</code> option to select the IPsec stack to use if <code>&#8211;config /etc/ipsec.conf</code> is given as argument to pluto. If both <code>&#8211;use-XXX</code> and <code>&#8211;config /etc/ipsec.conf</code> are specified, the last command line argument specified takes precedence. </p>
<p> Pluto supports RFC 3947 NAT-Traversal. The allowed range behind the NAT routers is submitted using the <code>&#8211;virtual-private</code> option. See <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) for the syntax. The option <code>&#8211;force-keepalive</code> forces the sending of the <i>keep-alive packets</i>, which are send to prevent the NAT router from closing its port when there is not enough traffic on the IPsec connection. The <code>&#8211;keep-alive</code> sets the delay (in seconds) of these keep-alive packets. The newer NAT-T standards support <i>port floating</i>, and Libreswan enables this per default. </p>
<p> Pluto supports the use of X.509 certificates and sends certificates when needed. This can confuse IKE implementations that do not implement this, such as the old FreeS/WAN implementation. The <code>&#8211;nocrsend</code> prevents pluto from sending these. Pluto uses NSS for all X.509 related data, including CAcerts, certs, CRLs and private keys. The <i>Certificate Revocation Lists</i> can also be retrieved from an URL. The option <code>&#8211;crlcheckinterval</code> sets the time between checking for CRL expiration and issuing new fetch commands. The first attempt to update a CRL is started at <i>2*crlcheckinterval</i> before the next update time. Pluto logs a warning if no valid CRL was loaded or obtained for a connection. If <code>&#8211;strictcrlpolicy</code> is given, the connection will be rejected until a valid CRL has been loaded. </p>
<p> Pluto can also use helper children to off-load cryptographic operations. This behavior can be fine tuned using the <code>&#8211;nhelpers</code>. Pluto will start <i>(n-1)</i> of them, where <i>n</i> is the number of CPU&#8217;s you have (including hypherthreaded CPU&#8217;s). A value of <i>0</i> forces pluto to do all operations in the main process. A value of <i>-1</i> tells pluto to perform the above calculation. Any other value forces the number to that amount. </p>
<p> Pluto uses the NSS crypto library as its random source. Some government Three Letter Agency requires that pluto reads 440 bits from /dev/random and feed this into the NSS RNG before drawing random from the NSS library, despite the NSS library itself already seeding its internal state. As this process can block pluto for an extended time, the default is to not perform this redundant seeding. The <code>&#8211;seedbits</code> option can be used to specify the number of bits that will be pulled from /dev/random and seeded into the NSS RNG. This can also be accomplished by specifying seedbits in the &quot;config setup&quot; section of ipsec.conf. This option should not be used by most people. </p>
<p> <code>pluto</code> attempts to create a lockfile with the name /var/run/pluto/pluto.pid. If the lockfile cannot be created, <code>pluto</code> exits &#8211; this prevents multiple <code>pluto</code>s from competing Any &quot;leftover&quot; lockfile must be removed before <code>pluto</code> will run. <code>pluto</code> writes its PID into this file so that scripts can find it. This lock will not function properly if it is on an NFS volume (but sharing locks on multiple machines doesn&#8217;t make sense anyway). </p>
<p> <code>pluto</code> then forks and the parent exits. This is the conventional &quot;daemon fork&quot;. It can make debugging awkward, so there is an option to suppress this fork. In certain configurations, pluto might also launch helper programs to assist with DNS queries or to offload cryptographic operations. </p>
<p> All logging, including diagnostics, is sent to <code><a href="/docs/linux/man/3-syslog/">syslog</a></code>(3) with facility=authpriv; it decides where to put these messages (possibly in /var/log/secure or /var/log/auth.log). Since this too can make debugging awkward, the option <code>&#8211;stderrlog</code> is used to steer logging to stderr. </p>
<p> Alternatively, <code>&#8211;logfile</code> can be used to send all logging information to a specific file. </p>
<p> If the <code>&#8211;perpeerlog</code> option is given, then pluto will open a log file per connection. By default, this is in /var/log/pluto/peer, in a subdirectory formed by turning all dot (.) [IPv4] or colon (:) [IPv6] into slashes (/). </p>
<p> The base directory can be changed with the <code>&#8211;perpeerlogbase</code>. </p>
<p> Once <code>pluto</code> is started, it waits for requests from <code>whack</code>.</p>
<h3>Pluto&#8217;s Internal State</h3>
<p>To understand how to use <code>pluto</code>, it is helpful to understand a little about its internal state. Furthermore, the terminology is needed to decipher some of the diagnostic messages. </p>
<p> Pluto supports <code>food groups</code> for Opportunistic IPsec. The policies for these are located in /etc/ipsec.d/policies, or another directory as specified by <code>&#8211;ipsecdir</code>. </p>
<p> Pluto supports X.509 Certificates. All certificate handling is done using the NSS library and all certificate material is stored in an NSS database in /etc/ipsec.d or another directory as specified by <code>&#8211;ipsecdir</code>. </p>
<p> Pluto may core dump. It will normally do so into the current working directory. You can specify the &#8211;coredir option for pluto, or specify the dumpdir= option in ipsec.conf. </p>
<p> If you are investigating a potential memory leak in pluto, start pluto with the &#8211;leak-detective option. Before the leak causes the system or pluto to die, shut down pluto in the regular way. pluto will display a list of leaks it has detected. </p>
<p> The <i>(potential) connection</i> database describes attributes of a connection. These include the IP addresses of the hosts and client subnets and the security characteristics desired. <code>pluto</code> requires this information (simply called a connection) before it can respond to a request to build an SA. Each connection is given a name when it is created, and all references are made using this name. </p>
<p> During the IKE exchange to build an SA, the information about the negotiation is represented in a <i>state object</i>. Each state object reflects how far the negotiation has reached. Once the negotiation is complete and the SA established, the state object remains to represent the SA. When the SA is terminated, the state object is discarded. Each State object is given a serial number and this is used to refer to the state objects in logged messages. </p>
<p> Each state object corresponds to a connection and can be thought of as an instantiation of that connection. At any particular time, there may be any number of state objects corresponding to a particular connection. Often there is one representing an ISAKMP SA and another representing an IPsec SA. </p>
<p> <code>KLIPS</code> hooks into the routing code in a LINUX kernel. Traffic to be processed by an IPsec SA must be directed through <code>KLIPS</code> by routing commands. Furthermore, the processing to be done is specified by <i>ipsec <a href="/docs/linux/man/8-eroute/">eroute</a>(8)</i> commands. <code>pluto</code> takes the responsibility of managing both of these special kinds of routes. </p>
<p> <code>NETKEY</code> requires no special routing. </p>
<p> Each connection may be routed, and must be while it has an IPsec SA. The connection specifies the characteristics of the route: the interface on this machine, the &quot;gateway&quot; (the nexthop), and the peer&#8217;s client subnet. Two connections may not be simultaneously routed if they are for the same peer&#8217;s client subnet but use different interfaces or gateways (<code>pluto</code>&#8216;s logic does not reflect any advanced routing capabilities). </p>
<p> On KLIPS, each eroute is associated with the state object for an IPsec SA because it has the particular characteristics of the SA. Two eroutes conflict if they specify the identical local and remote clients (unlike for routes, the local clients are taken into account). </p>
<p> When <code>pluto</code> needs to install a route for a connection, it must make sure that no conflicting route is in use. If another connection has a conflicting route, that route will be taken down, as long as there is no IPsec SA instantiating that connection. If there is such an IPsec SA, the attempt to install a route will fail. </p>
<p> There is an exception. If <code>pluto</code>, as Responder, needs to install a route to a fixed client subnet for a connection, and there is already a conflicting route, then the SAs using the route are deleted to make room for the new SAs. The rationale is that the new connection is probably more current. The need for this usually is a product of Road Warrior connections (these are explained later; they cannot be used to initiate). </p>
<p> When <code>pluto</code> needs to install an eroute for an IPsec SA (for a state object), first the state object&#8217;s connection must be routed (if this cannot be done, the eroute and SA will not be installed). If a conflicting eroute is already in place for another connection, the eroute and SA will not be installed (but note that the routing exception mentioned above may have already deleted potentially conflicting SAs). If another IPsec SA for the same connection already has an eroute, all its outgoing traffic is taken over by the new eroute. The incoming traffic will still be processed. This characteristic is exploited during rekeying. </p>
<p> All of these routing characteristics are expected change when <code>KLIPS</code> and <code>NETKEY</code> merge into a single new stack.</p>
<h3>Using whack</h3>
<p><code>whack</code> is used to command a running <code>pluto</code>. <code>whack</code> uses a UNIX domain socket to speak to <code>pluto</code> (by default, /var/pluto.ctl). </p>
<p> <code>whack</code> has an intricate argument syntax. This syntax allows many different functions to be specified. The help form shows the usage or version information. The connection form gives <code>pluto</code> a description of a potential connection. The public key form informs <code>pluto</code> of the RSA public key for a potential peer. The delete form deletes a connection description and all SAs corresponding to it. The listen form tells <code>pluto</code> to start or stop listening on the public interfaces for IKE requests from peers. The route form tells <code>pluto</code> to set up routing for a connection; the unroute form undoes this. The initiate form tells <code>pluto</code> to negotiate an SA corresponding to a connection. The terminate form tells <code>pluto</code> to remove all SAs corresponding to a connection, including those being negotiated. The status form displays the <code>pluto</code>&#8216;s internal state. The debug form tells <code>pluto</code> to change the selection of debugging output &quot;on the fly&quot;. The shutdown form tells <code>pluto</code> to shut down, deleting all SAs. </p>
<p> The crash option asks pluto to consider a particularly target IP to have crashed, and to attempt to restart all connections with that IP address as a gateway. In general, you should use Dead Peer Detection to detect this kind of situation automatically, but this is not always possible. </p>
<p> Most options are specific to one of the forms, and will be described with that form. There are three options that apply to all forms. </p>
<p> <code>&#8211;ctlbase</code>&nbsp;<wbr><i>path</i></p>
<dl>
<dd><i>path</i>.ctl is used as the UNIX domain socket for talking to <code>pluto</code>. This option facilitates debugging.</dl>
<p> <code>&#8211;label</code>&nbsp;<wbr><i>string</i></p>
<dl>
<dd>adds the string to all error messages generated by <code>whack</code>.</dl>
<p> The help form of <code>whack</code> is self-explanatory. </p>
<p> <code>&#8211;help</code></p>
<dl>
<dd>display the usage message.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>display the version of <code>whack</code>.</dl>
<p> The connection form describes a potential connection to <code>pluto</code>. <code>pluto</code> needs to know what connections can and should be negotiated. When <code>pluto</code> is the initiator, it needs to know what to propose. When <code>pluto</code> is the responder, it needs to know enough to decide whether is is willing to set up the proposed connection. </p>
<p> The description of a potential connection can specify a large number of details. Each connection has a unique name. This name will appear in a updown shell command, so it should not contain punctuation that would make the command ill-formed. </p>
<p> <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i></p>
<dl>
<dd>sets the name of the connection</dl>
<p> The topology of a connection is symmetric, so to save space here is half a picture: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>client_subnet&lt;&#8211;&gt;host:ikeport&lt;&#8211;&gt;nexthop&lt;&#8212; </p>
<p> A similar trick is used in the flags. The same flag names are used for both ends. Those before the <code>&#8211;to</code> flag describe the left side and those afterwards describe the right side. When <code>pluto</code> attempts to use the connection, it decides whether it is the left side or the right side of the connection, based on the IP numbers of its interfaces. </p>
<p> <code>&#8211;id</code>&nbsp;<wbr><i>id</i></p>
<dl>
<dd>the identity of the end. Currently, this can be an IP address (specified as dotted quad or as a Fully Qualified Domain Name, which will be resolved immediately) or as a Fully Qualified Domain Name itself (prefixed by &quot;@&quot; to signify that it should not be resolved), or as user [at] FQDN, or an X.509 DN, or as the magic value <code>%myid</code>. <code>Pluto</code> only authenticates the identity, and does not use it for addressing, so, for example, an IP address need not be the one to which packets are to be sent. If the option is absent, the identity defaults to the IP address specified by <code>&#8211;host</code>. <code>%myid</code> allows the identity to be separately specified (by the <code>pluto</code> or <code>whack</code> option <code>&#8211;myid</code> or by the <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5)<code>config setup</code> parameter <i>myid</i>). Otherwise, <code>pluto</code> tries to guess what <code>%myid</code> should stand for: the IP address of <code>%defaultroute</code>, if it is supported by a suitable TXT record in the reverse domain for that IP address, or the system&#8217;s hostname, if it is supported by a suitable TXT record in its forward domain.</dl>
<p> <code>&#8211;host</code>&nbsp;<wbr><i>ip-address</i>, <code>&#8211;host</code>&nbsp;<wbr><code>%any</code>, <code>&#8211;host</code>&nbsp;<wbr><code>%opportunistic</code></p>
<dl>
<dd>the IP address of the end (generally the public interface). If <code>pluto</code> is to act as a responder for IKE negotiations initiated from unknown IP addresses (the &quot;Road Warrior&quot; case), the IP address should be specified as <code>%any</code> (currently, the obsolete notation 0.0.0.0 is also accepted for this). If <code>pluto</code> is to opportunistically initiate the connection, use <code>%opportunistic</code></dl>
<p> <code>&#8211;cert</code>&nbsp;<wbr><i>friendly_name</i></p>
<dl>
<dd>The friendly_name (or nickname) of the X.509 certificate that was used when imported the certificate into the NSS database. See <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) on how to extrac this from the PKCS#12 file.</dl>
<p> <code>&#8211;ckaid</code>&nbsp;<wbr><i>CKAID</i></p>
<dl>
<dd>The hex CKAID of the X.509 certificate. Certificates are stored in the NSS database.</dl>
<p> <code>&#8211;ca</code>&nbsp;<wbr><i>distinguished name</i></p>
<dl>
<dd>the X.509 Certificate Authority&#8217;s Distinguished Name (DN) used as trust anchor for this connection. This is the CA certificate that signed the host certificate, as well as the certificate of the incoming client.</dl>
<p> <code>&#8211;groups</code>&nbsp;<wbr><i>access control groups</i></p>
<dl>
<dd>the access control groups used.</dl>
<p> <code>&#8211;sendcert</code>&nbsp;<wbr><i>yes|forced|always|ifasked|no|never</i></p>
<dl>
<dd>Whether or not to send our X.509 certificate credentials. This could potentially give an attacker too much information about which identities are allowed to connect to this host. The default is to use <code>ifasked</code> when we are a Responder, and to use <code>yes</code> (which is the same as <code>forced</code> and <code>always</code> if we are an Initiator. The values <code>no</code> and <code>never</code> are equivalent. NOTE: &quot;forced&quot; does not seem to be actually implemented &#8211; do not use it.</dl>
<p> <code>&#8211;sendca</code>&nbsp;<wbr><i>none|issuer|all</i></p>
<dl>
<dd>How much of our available X.509 trust chain to send with the end certificate, excluding any root CAs. Specifying <code>issuer</code> sends just the issuing intermediate CA, while <code> all</code> will send the entire chain of intermediate CAs.<code>none</code> will not send any CA certs. The default is <code>none</code> which maintains the current libreswan behavior.</dl>
<p> <code>&#8211;certtype</code>&nbsp;<wbr><i>number</i></p>
<dl>
<dd>The X.509 certificate type number.</dl>
<p> <code>&#8211;ikeport</code>&nbsp;<wbr><i>port-number</i></p>
<dl>
<dd>the UDP port that IKE listens to on that host. The default is 500. (<code>pluto</code> on this machine uses the port specified by its own command line argument, so this only affects where <code>pluto</code> sends messages.)</dl>
<p> <code>&#8211;nexthop</code>&nbsp;<wbr><i>ip-address</i></p>
<dl>
<dd>where to route packets for the peer&#8217;s client (presumably for the peer too, but it will not be used for this). When <code>pluto</code> installs an IPsec SA, it issues a route command. It uses the nexthop as the gateway. The default is the peer&#8217;s IP address (this can be explicitly written as <code>%direct</code>; the obsolete notation 0.0.0.0 is accepted). This option is necessary if <code>pluto</code>&#8216;s host&#8217;s interface used for sending packets to the peer is neither point-to-point nor directly connected to the peer.</dl>
<p> <code>&#8211;client</code>&nbsp;<wbr><i>subnet</i></p>
<dl>
<dd>the subnet for which the IPsec traffic will be destined. If not specified, the host will be the client. The subnet can be specified in any of the forms supported by <code><a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a></code>(3). The general form is <i>address</i>/<i>mask</i>. The <i>address</i> can be either a domain name or four decimal numbers (specifying octets) separated by dots. The most convenient form of the <i>mask</i> is a decimal integer, specifying the number of leading one bits in the mask. So, for example, 10.0.0.0/8 would specify the class A network &quot;Net 10&quot;.</dl>
<p> <code>&#8211;clientwithin</code>&nbsp;<wbr><i>subnet</i></p>
<dl>
<dd>This option is obsolete and will be removed. Do not use this option anymore.</dl>
<p> <code>&#8211;clientprotoport</code>&nbsp;<wbr><i>protocol/port</i></p>
<dl>
<dd>specify the Port Selectors (filters) to be used on this connection. The general form is <i>protocol</i>/<i>port</i>. This is most commonly used to limit the connection to L2TP traffic only by specifying a value of <i>17/1701</i> for UDP (protocol 17) and port 1701. The notation <i>17/%any</i> can be used to allow all UDP traffic and is needed for L2TP connections with Windows XP machines before Service Pack 2.</dl>
<p> <code>&#8211;srcip</code>&nbsp;<wbr><i>ip-address</i></p>
<dl>
<dd>the IP address for this host to use when transmitting a packet to the remote IPsec gateway itself. This option is used to make the gateway itself use its internal IP, which is part of the <code>&#8211;client subnet</code>. Otherwise it will use its nearest IP address, which is its public IP address, which is not part of the subnet-subnet IPsec tunnel, and would therefor not get encrypted.</dl>
<p> <code>&#8211;xauthserver</code></p>
<dl>
<dd>this end is an xauthserver. It will lookup the xauth user name and password and verify this before allowing the connection to get established.</dl>
<p> <code>&#8211;xauthclient</code></p>
<dl>
<dd>this end is an xauthclient. To bring this connection up with the <code>&#8211;initiate</code> also requires the client to specify <code>&#8211;xauthuser username</code> and <code>&#8211;xauthpass password </code></dl>
<p> <code>&#8211;xauthuser</code></p>
<dl>
<dd>The username for the xauth authentication.This option is normally passed along by <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) when an xauth connection is started using <i>ipsec auto &#8211;up conn</i></dl>
<p> <code>&#8211;xauthpass</code></p>
<dl>
<dd>The password for the xauth authentication. This option is normally passed along by <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) when an xauth connection is started using <i>ipsec auto &#8211;up conn</i></dl>
<p> <code>&#8211;modecfgserver</code></p>
<dl>
<dd>this end is an Mode Config server</dl>
<p> <code>&#8211;modecfgclient</code></p>
<dl>
<dd>this end is an Mode Config client</dl>
<p> <code>&#8211;modecfgdns1</code></p>
<dl>
<dd>The IP address of the first DNS server to pass along to the ModeConfig Client</dl>
<p> <code>&#8211;modecfgdns2</code></p>
<dl>
<dd>The IP address of the second DNS server to pass along to the ModeConfig Client</dl>
<p> <code>&#8211;dnskeyondemand</code></p>
<dl>
<dd>specifies that when an RSA public key is needed to authenticate this host, and it isn&#8217;t already known, fetch it from DNS.</dl>
<p> <code>&#8211;updown</code>&nbsp;<wbr><i>updown</i></p>
<dl>
<dd>specifies an external shell command to be run whenever <code>pluto</code> brings up or down a connection. The script is used to build a shell command, so it may contain positional parameters, but ought not to have punctuation that would cause the resulting command to be ill-formed. The default is <i>ipsec _updown</i>. Pluto passes a dozen environment variables to the script about the connection involved.</dl>
<p> <code>&#8211;to</code></p>
<dl>
<dd>separates the specification of the left and right ends of the connection. Pluto tries to decide whether it is <i>left</i> or <i>right</i> based on the information provided on both sides of this option.</dl>
<p> The potential connection description also specifies characteristics of rekeying and security. </p>
<p> <code>&#8211;psk</code></p>
<dl>
<dd>Propose and allow preshared secret authentication for IKE peers. This authentication requires that each side use the same secret. May be combined with <code>&#8211;rsasig</code>; at least one must be specified.</dl>
<p> <code>&#8211;rsasig</code></p>
<dl>
<dd>Propose and allow RSA signatures for authentication of IKE peers. This authentication requires that each side have have a private key of its own and know the public key of its peer. May be combined with <code>&#8211;psk</code>; at least one must be specified.</dl>
<p> <code>&#8211;encrypt</code></p>
<dl>
<dd>All proposed or accepted IPsec SAs will include non-null ESP. The actual choices of transforms are wired into <code>pluto</code>.</dl>
<p> <code>&#8211;authenticate</code></p>
<dl>
<dd>All proposed IPsec SAs will include AH. All accepted IPsec SAs will include AH or ESP with authentication. The actual choices of transforms are wired into <code>pluto</code>. Note that this has nothing to do with IKE authentication.</dl>
<p> <code>&#8211;compress</code></p>
<dl>
<dd>All proposed IPsec SAs will include IPCOMP (compression). This will be ignored if KLIPS is not configured with IPCOMP support.</dl>
<p> <code>&#8211;tunnel</code></p>
<dl>
<dd>the IPsec SA should use tunneling. Implicit if the SA is for clients. Must only be used with <code>&#8211;authenticate</code> or <code>&#8211;encrypt</code>.</dl>
<p> <code>&#8211;ipv4</code></p>
<dl>
<dd>The host addresses will be interpreted as IPv4 addresses. This is the default. Note that for a connection, all host addresses must be of the same Address Family (IPv4 and IPv6 use different Address Families).</dl>
<p> <code>&#8211;ipv6</code></p>
<dl>
<dd>The host addresses (including nexthop) will be interpreted as IPv6 addresses. Note that for a connection, all host addresses must be of the same Address Family (IPv4 and IPv6 use different Address Families).</dl>
<p> <code>&#8211;tunnelipv4</code></p>
<dl>
<dd>The client addresses will be interpreted as IPv4 addresses. The default is to match what the host will be. This does not imply <code>&#8211;tunnel</code> so the flag can be safely used when no tunnel is actually specified. Note that for a connection, all tunnel addresses must be of the same Address Family.</dl>
<p> <code>&#8211;tunnelipv6</code></p>
<dl>
<dd>The client addresses will be interpreted as IPv6 addresses. The default is to match what the host will be. This does not imply <code>&#8211;tunnel</code> so the flag can be safely used when no tunnel is actually specified. Note that for a connection, all tunnel addresses must be of the same Address Family.</dl>
<p> <code>&#8211;pfs</code></p>
<dl>
<dd>There should be Perfect Forward Secrecy &#8211; new keying material will be generated for each IPsec SA when running Quick Mode in IKEv1 or Create Child in IKEv2. Without this option, the SAKMP SA keying material is used instead. <code>pluto</code> will propose the same group that was used with the original IKE SA.</dl>
<p> <code>&#8211;pfsgroup</code>&nbsp;<wbr><i>modp-group</i></p>
<dl>
<dd>Sets the Diffie-Hellman group used. Currently the following values are supported: <code>modp1024</code> (DHgroup 2), <code>modp1536</code> (DHgroup 5), <code>modp2048</code> (DHgroup 14), <code>modp3072</code> (DHgroup 15), <code>modp4096</code> (DHgroup 16), <code>modp6144</code> (DHgroup 17), and <code>modp8192</code> (DHgroup 18). It is possible to support the weak and broken <code>modp768</code> (DHgroup 1), but this requires a manual recompile and is strongly discouraged.</dl>
<p> <code>&#8211;disablearrivalcheck</code></p>
<dl>
<dd>If the connection is a tunnel, allow packets arriving through the tunnel to have any source and destination addresses.</dl>
<p> <code>&#8211;esp</code>&nbsp;<wbr><i>esp-algos</i></p>
<dl>
<dd>ESP encryption/authentication algorithm to be used for the connection (phase2 aka IPsec SA). The options must be suitable as a value of <code><a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a></code>(8). See <code><a href="/docs/linux/man/5-ipsec-conf/">ipsec.conf</a></code>(5) for a detailed description of the algorithm format.</dl>
<p> <code>&#8211;aggrmode</code></p>
<dl>
<dd>This tunnel is using aggressive mode ISAKMP negotiation. The default is main mode. Aggressive mode is less secure than main mode as it reveals your identity to an eavesdropper, but is needed to support road warriors using PSK keys or to interoperate with other buggy implementations insisting on using aggressive mode.</dl>
<p> <code>&#8211;modecfgpull</code></p>
<dl>
<dd>Pull the Mode Config network information from the peer.</dl>
<p> <code>&#8211;dpddelay</code>&nbsp;<wbr><i>seconds</i></p>
<dl>
<dd>Set the delay (in seconds) between Dead Peer Detection (RFC 3706) keepalives (R_U_THERE, R_U_THERE_ACK) that are sent for this connection (default 30 seconds).</dl>
<p> <code>&#8211;timeout</code>&nbsp;<wbr><i>seconds</i></p>
<dl>
<dd>Set the length of time (in seconds) we will idle without hearing either an R_U_THERE poll from our peer, or an R_U_THERE_ACK reply. After this period has elapsed with no response and no traffic, we will declare the peer dead, and remove the SA (default 120 seconds).</dl>
<p> <code>&#8211;dpdaction</code>&nbsp;<wbr><i>action</i></p>
<dl>
<dd>When a DPD enabled peer is declared dead, what action should be taken. <code>hold</code>(default) means the eroute will be put into <i>%hold</i> status, while <code>clear</code>means the eroute and SA with both be cleared. Clear is really only useful on the server of a Road Warrior config. The action <code>restart</code> is used on tunnels that need to be permanently up, and have static IP addresses. The action <code>restart_by_peer</code>has been obsoleted and its functionality has been moved into the restart action.</dl>
<p> <code>&#8211;forceencaps</code></p>
<dl>
<dd>In some cases, for example when ESP packets are filtered or when a broken IPsec peer does not properly recognise NAT, it can be useful to force RFC-3948 encapsulation using this option. It causes pluto lie and tell the remote peer that RFC-3948 encapsulation (ESP in UDP port 4500 packets) is required.</dl>
<p> If none of the <code>&#8211;encrypt</code>, <code>&#8211;authenticate</code>, <code>&#8211;compress</code>, or <code>&#8211;pfs</code> flags is given, the initiating the connection will only build an ISAKMP SA. For such a connection, client subnets have no meaning and must not be specified. </p>
<p> Apart from initiating directly using the <code>&#8211;initiate</code> option, a tunnel can be loaded with a different policy </p>
<p> <code>&#8211;initiateontraffic</code></p>
<dl>
<dd>Only initiate the connection when we have traffic to send over the connection</dl>
<p> <code>&#8211;pass</code></p>
<dl>
<dd>Allow <code>unencrypted</code> traffic to flow until the tunnel is initiated.</dl>
<p> <code>&#8211;drop</code></p>
<dl>
<dd>Drop unencrypted traffic silently.</dl>
<p> <code>&#8211;reject</code></p>
<dl>
<dd>Drop unencrypted traffic silently, but send an ICMP message notifying the other end.</dl>
<p> These options need to be documented </p>
<p> <code>&#8211;failnone</code></p>
<dl>
<dd>to be documented</dl>
<p> <code>&#8211;failpass</code></p>
<dl>
<dd>to be documented</dl>
<p> <code>&#8211;faildrop</code></p>
<dl>
<dd>to be documented</dl>
<p> <code>&#8211;failreject</code></p>
<dl>
<dd>to be documented</dl>
<p> <code>pluto</code> supports various X.509 Certificate related options. </p>
<p> <code>&#8211;utc</code></p>
<dl>
<dd>display all times in UTC.</dl>
<p> <code>&#8211;listall</code></p>
<dl>
<dd>lists all of the X.509 information known to pluto.</dl>
<p> <code>&#8211;listpubkeys</code></p>
<dl>
<dd>list all the public keys that have been successfully loaded.</dl>
<p> <code>&#8211;listcerts</code></p>
<dl>
<dd>list all the X.509 certificates that are currently loaded.</dl>
<p> <code>&#8211;checkpubkeys</code></p>
<dl>
<dd>list all the loaded X.509 certificates which are about to expire or have been expired.</dl>
<p> <code>&#8211;listcacerts</code></p>
<dl>
<dd>list all the Certificate Authority X.509 certificates that are currently loaded.</dl>
<p> <code>&#8211;listcrls</code></p>
<dl>
<dd>list all the loaded <i>Certificate Revocation Lists</i> (CRLs)</dl>
<p> The corresponding options <code>&#8211;rereadsecrets</code>, <code>&#8211;rereadall</code>, and <code>&#8211;rereadcrls</code> options reread this information from their respective sources, and purge all the online obtained information. The option <code>&#8211;listevents</code> lists all pending CRL fetch commands. </p>
<p> <code>&#8211;ikelifetime</code>&nbsp;<wbr><i>seconds</i></p>
<dl>
<dd>how long <code>pluto</code> will propose that an ISAKMP SA be allowed to live. The default is 3600 (one hour) and the maximum is 86400 (1 day). This option will not affect what is accepted. <code>pluto</code> will reject proposals that exceed the maximum.</dl>
<p> <code>&#8211;ipseclifetime</code>&nbsp;<wbr><i>seconds</i></p>
<dl>
<dd>how long <code>pluto</code> will propose that an IPsec SA be allowed to live. The default is 28800 (eight hours) and the maximum is 86400 (one day). This option will not affect what is accepted. <code>pluto</code> will reject proposals that exceed the maximum.</dl>
<p> <code>&#8211;rekeymargin</code>&nbsp;<wbr><i>seconds</i></p>
<dl>
<dd>how long before an SA&#8217;s expiration should <code>pluto</code> try to negotiate a replacement SA. This will only happen if <code>pluto</code> was the initiator. The default is 540 (nine minutes).</dl>
<p> <code>&#8211;rekeyfuzz</code>&nbsp;<wbr><i>percentage</i></p>
<dl>
<dd>maximum size of random component to add to rekeymargin, expressed as a percentage of rekeymargin. <code>pluto</code> will select a delay uniformly distributed within this range. By default, the percentage will be 100. If greater determinism is desired, specify 0. It may be appropriate for the percentage to be much larger than 100.</dl>
<p> <code>&#8211;keyingtries</code>&nbsp;<wbr><i>count</i></p>
<dl>
<dd>how many times <code>pluto</code> should try to negotiate an SA, either for the first time or for rekeying. The default value of 0 means to keep trying forever.</dl>
<p> <code>&#8211;dontrekey</code></p>
<dl>
<dd>A misnomer. Only rekey a connection if we were the Initiator and there was recent traffic on the existing connection. This applies to Phase 1 and Phase 2. This is currently the only automatic way for a connection to terminate. It may be useful with Road Warrior or Opportunistic connections. Since SA lifetime negotiation is take-it-or-leave it, a Responder normally uses the shorter of the negotiated or the configured lifetime. This only works because if the lifetime is shorter than negotiated, the Responder will rekey in time so that everything works. This interacts badly with <code>&#8211;dontrekey</code>. In this case, the Responder will end up rekeying to rectify a shortfall in an IPsec SA lifetime; for an ISAKMP SA, the Responder will accept the negotiated lifetime.</dl>
<p> <code>&#8211;delete</code></p>
<dl>
<dd>when used in the connection form, it causes any previous connection with this name to be deleted before this one is added. Unlike a normal delete, no diagnostic is produced if there was no previous connection to delete. Any routing in place for the connection is undone.</dl>
<p> <code>&#8211;delete</code>, <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i></p>
<dl>
<dd>The delete form deletes a named connection description and any SAs established or negotiations initiated using this connection. Any routing in place for the connection is undone.</dl>
<p> <code>&#8211;deletestate</code>&nbsp;<wbr><i>state-number</i></p>
<dl>
<dd>The deletestate form deletes the state object with the specified serial number. This is useful for selectively deleting instances of connections.</dl>
<p> The route form of the <code>whack</code> command tells <code>pluto</code> to set up routing for a connection. Although like a traditional route, it uses an ipsec device as a virtual interface. Once routing is set up, no packets will be sent &quot;in the clear&quot; to the peer&#8217;s client specified in the connection. A TRAP shunt eroute will be installed; if outbound traffic is caught, Pluto will initiate the connection. An explicit <code>whack</code> route is not always needed: if it hasn&#8217;t been done when an IPsec SA is being installed, one will be automatically attempted. </p>
<p> <code>&#8211;route</code>, <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i></p>
<dl>
<dd>When a routing is attempted for a connection, there must not already be a routing for a different connection with the same subnet but different interface or destination, or if there is, it must not be being used by an IPsec SA. Otherwise the attempt will fail.</dl>
<p> <code>&#8211;unroute</code>, <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i></p>
<dl>
<dd>The unroute form of the <code>whack</code> command tells <code>pluto</code> to undo a routing. <code>pluto</code> will refuse if an IPsec SA is using the connection. If another connection is sharing the same routing, it will be left in place. Without a routing, packets will be sent without encryption or authentication.</dl>
<p> The initiate form tells <code>pluto</code> to initiate a negotiation with another <code>pluto</code> (or other IKE daemon) according to the named connection. Initiation requires a route that <code>&#8211;route</code> would provide; if none is in place at the time an IPsec SA is being installed, <code>pluto</code> attempts to set one up. </p>
<p> <code>&#8211;initiate</code>, <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i>, <code>&#8211;asynchronous</code></p>
<dl>
<dd>The initiate form of the <code>whack</code> command will relay back from <code>pluto</code> status information via the UNIX domain socket (unless &#8211;asynchronous is specified). The status information is meant to look a bit like that from <code>FTP</code>. Currently <code>whack</code> simply copies this to stderr. When the request is finished (eg. the SAs are established or <code>pluto</code> gives up), <code>pluto</code> closes the channel, causing <code>whack</code> to terminate.</dl>
<p> The opportunistic initiate form is mainly used for debugging. </p>
<p> <code>&#8211;tunnelipv4</code>, <code>&#8211;tunnelipv6</code>, <code>&#8211;oppohere</code>&nbsp;<wbr><i>ip-address</i>, <code>&#8211;oppothere</code>&nbsp;<wbr><i>ip-address</i></p>
<dl>
<dd>This will cause <code>pluto</code> to attempt to opportunistically initiate a connection from here to the there, even if a previous attempt had been made. The whack log will show the progress of this attempt.</dl>
<p> Ending an connection </p>
<p> <code>&#8211;terminate</code>, <code>&#8211;name</code>&nbsp;<wbr><i>connection-name</i></p>
<dl>
<dd>the terminate form tells <i>pluto</i> to delete any SAs that use the specified connection and to stop any negotiations in process. it does not prevent new negotiations from starting (the delete form has this effect).</dl>
<p> <code>&#8211;crash</code>&nbsp;<wbr><i>ip-address</i></p>
<dl>
<dd>If the remote peer has crashed, and therefor did not notify us, we keep sending encrypted traffic, and rejecting all plaintext (non-IKE) traffic from that remote peer. The <code>&#8211;crash</code> brings our end down as well for all the known connections to the specified <i>ip-address</i></dl>
<p> <code>&#8211;whackrecord</code><i>filename</i>, <code>&#8211;whackstoprecord</code></p>
<dl>
<dd>this causes <i>pluto</i>to open the given filename for write, and record each of the messages received from whack or addconn. This continues until the whackstoprecord option is used. This option may not be combined with any other command. The start/stop commands are not recorded themselves. These files are usually used to create input files for unit tests, particularly for complex setups where policies may in fact overlap. </p>
<p> The format of the file consists of a line starting with #!pluto-whack and the date that the file was started, as well as the hostname, and a linefeed. What follows are binary format records consisting of a 32-bit record length in bytes, (including the length record itself), a 64-bit timestamp, and then the literal contents of the whack message that was received. All integers are in host format. In order to unambigously determine the host order, the first record is an empty record that contains only the current WHACK_MAGIC value. This record is 16 bytes long.</dl>
<p> <i>ip-address</i></p>
<dl>
<dd>If the remote peer has crashed, and therefor did not notify us, we keep sending encrypted traffic, and rejecting all plaintext (non-IKE) traffic from that remote peer. The <code>&#8211;crash</code> brings our end down as well for all the known connections to the specified <i>ip-address</i></dl>
<p> The public key for informs <code>pluto</code> of the RSA public key for a potential peer. Private keys must be kept secret, so they are kept in <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5). </p>
<p> <code>&#8211;keyid&nbsp;<wbr></code><i>id</i></p>
<dl>
<dd>specififies the identity of the peer for which a public key should be used. Its form is identical to the identity in the connection. If no public key is specified, <code>pluto</code> attempts to find KEY records from DNS for the id (if a FQDN) or through reverse lookup (if an IP address). Note that there several interesting ways in which this is not secure.</dl>
<p> <code>&#8211;addkey</code></p>
<dl>
<dd>specifies that the new key is added to the collection; otherwise the new key replaces any old ones.</dl>
<p> <code>&#8211;pubkeyrsa&nbsp;<wbr></code><i>key</i></p>
<dl>
<dd>specifies the value of the RSA public key. It is a sequence of bytes as described in RFC 2537 &quot;RSA/MD5 KEYs and SIGs in the Domain Name System (DNS)&quot;. It is denoted in a way suitable for <code><a href="/docs/linux/man/3-ipsec_ttodata/">ipsec_ttodata</a></code>(3). For example, a base 64 numeral starts with 0s.</dl>
<p> The listen form tells <code>pluto</code> to start listening for IKE requests on its public interfaces. To avoid race conditions, it is normal to load the appropriate connections into <code>pluto</code> before allowing it to listen. If <code>pluto</code> isn&#8217;t listening, it is pointless to initiate negotiations, so it will refuse requests to do so. Whenever the listen form is used, <code>pluto</code> looks for public interfaces and will notice when new ones have been added and when old ones have been removed. This is also the trigger for <code>pluto</code> to read the <i>ipsec.secrets</i> file. So listen may useful more than once. </p>
<p> <code>&#8211;listen</code></p>
<dl>
<dd>start listening for IKE traffic on public interfaces.</dl>
<p> <code>&#8211;unlisten</code></p>
<dl>
<dd>stop listening for IKE traffic on public interfaces.</dl>
<p> The busy and relax options tells <code>pluto</code> to explicitly activate or deactivate additional DDoS protection. Normally, these meassures are automatically activate or deactivate based on the number of states inside pluto. One of these DDoS protection methods is to active IKEv2 DCOOKIEs to defend against spoofed IKE packets. </p>
<p> <code>&#8211;busy</code></p>
<dl>
<dd>place pluto into busy mode and activate anti-DDoS measures.</dl>
<p> <code>&#8211;relax</code></p>
<dl>
<dd>pull pluto out of busy mode and deactivate anti-DDoS measures.</dl>
<p> The status form will display information about the internal state of <code>pluto</code>: information about each potential connection, about each state object, and about each shunt that <code>pluto</code> is managing without an associated connection. </p>
<p> <code>&#8211;status</code></p>
<dl>
<dd></dl>
<p> The trafficstatus form will display the xauth username, add_time and the total in and out bytes of the IPsec SA&#8217;s. </p>
<p> <code>&#8211;trafficstatus</code></p>
<dl>
<dd></dl>
<p> The shutdown form is the proper way to shut down <code>pluto</code>. It will tear down the SAs on this machine that <code>pluto</code> has negotiated. It does not inform its peers, so the SAs on their machines remain. </p>
<p> <code>&#8211;shutdown</code></p>
<dl>
<dd></dl>
<h3>Examples</h3>
<p>It would be normal to start <code>pluto</code> in one of the system initialization scripts. It needs to be run by the superuser. Generally, no arguments are needed. To run in manually, the superuser can simply type </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec pluto </p>
<p> The command will immediately return, but a <code>pluto</code> process will be left running, waiting for requests from <code>whack</code> or a peer. </p>
<p> Using <code>whack</code>, several potential connections would be described: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;name silly &#8211;host 127.0.0.1 &#8211;to &#8211;host 127.0.0.2 &#8211;ikelifetime 900 &#8211;ipseclifetime 800 &#8211;keyingtries 3 </p>
<p> Since this silly connection description specifies neither encryption, authentication, nor tunneling, it could only be used to establish an ISAKMP SA. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;name conn_name &#8211;host 10.0.0.1 &#8211;client 10.0.1.0/24 &#8211;to &#8211;host 10.0.0.2 &#8211;client 10.0.2.0/24 &#8211;encrypt </p>
<p> This is something that must be done on both sides. If the other side is <code>pluto</code>, the same <code>whack</code> command could be used on it (the command syntax is designed to not distinguish which end is ours). </p>
<p> Now that the connections are specified, <code>pluto</code> is ready to handle requests and replies via the public interfaces. We must tell it to discover those interfaces and start accepting messages from peers: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;listen </p>
<p> If we don&#8217;t immediately wish to bring up a secure connection between the two clients, we might wish to prevent insecure traffic. The routing form asks <code>pluto</code> to cause the packets sent from our client to the peer&#8217;s client to be routed through the ipsec0 device; if there is no SA, they will be discarded: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;route conn_name </p>
<p> Finally, we are ready to get <code>pluto</code> to initiate negotiation for an IPsec SA (and implicitly, an ISAKMP SA): </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;initiate &#8211;name conn_name </p>
<p> A small log of interesting events will appear on standard output (other logging is sent to syslog). </p>
<p> <code>whack</code> can also be used to terminate <code>pluto</code> cleanly, tearing down all SAs that it has negotiated. </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ipsec whack &#8211;shutdown </p>
<p> Notification of any IPSEC SA deletion, but not ISAKMP SA deletion is sent to the peer. Unfortunately, such Notification is not reliable. Furthermore, <code>pluto</code> itself ignores Notifications.</p>
<h3>Xauth</h3>
<p>If <code>pluto</code> needs additional authentication, such as defined by the XAUTH specifications, then it may ask <code>whack</code> to prompt the operator for username or passwords. Typically, these will be entered interactively. A GUI that wraps around <code>whack</code> may look for the 041 (username) or 040 (password) prompts, and display them to the user. </p>
<p> For testing purposes, the options <code>&#8211;xauthuser&nbsp;<wbr></code><i>user</i><code>&#8211;xauthpass&nbsp;<wbr></code><i>pass</i> may be be given prior to the <code>&#8211;initiate&nbsp;<wbr></code> to provide responses to the username and password prompts.</p>
<h3>The updown command</h3>
<p>Whenever <code>pluto</code> brings a connection up or down, it invokes the updown command. This command is specified using the <code>&#8211;updown</code> option. This allows for customized control over routing and firewall manipulation. </p>
<p> The updown is invoked for five different operations. Each of these operations can be for our client subnet or for our host itself. </p>
<p> <code>prepare-host</code> or <code>prepare-client</code></p>
<dl>
<dd>is run before bringing up a new connection if no other connection with the same clients is up. Generally, this is useful for deleting a route that might have been set up before <code>pluto</code> was run or perhaps by some agent not known to <code>pluto</code>.</dl>
<p> <code>route-host</code> or <code>route-client</code></p>
<dl>
<dd>is run when bringing up a connection for a new peer client subnet (even if <code>prepare-host</code> or <code>prepare-client</code> was run). The command should install a suitable route. Routing decisions are based only on the destination (peer&#8217;s client) subnet address, unlike eroutes which discriminate based on source too.</dl>
<p> <code>unroute-host</code> or <code>unroute-client</code></p>
<dl>
<dd>is run when bringing down the last connection for a particular peer client subnet. It should undo what the <code>route-host</code> or <code>route-client</code> did.</dl>
<p> <code>up-host</code> or <code>up-client</code></p>
<dl>
<dd>is run when bringing up a tunnel eroute with a pair of client subnets that does not already have a tunnel eroute. This command should install firewall rules as appropriate. It is generally a good idea to allow IKE messages (UDP port 500) travel between the hosts.</dl>
<p> <code>down-host</code> or <code>down-client</code></p>
<dl>
<dd>is run when bringing down the eroute for a pair of client subnets. This command should delete firewall rules as appropriate. Note that there may remain some inbound IPsec SAs with these client subnets.</dl>
<p> The script is passed a large number of environment variables to specify what needs to be done. </p>
<p> <code>PLUTO_VERSION</code></p>
<dl>
<dd>indicates what version of this interface is being used. This document describes version 1.1. This is upwardly compatible with version 1.0.</dl>
<p> <code>PLUTO_VERB</code></p>
<dl>
<dd>specifies the name of the operation to be performed (<code>prepare-host</code>,r <code>prepare-client</code>, <code>up-host</code>, <code>up-client</code>, <code>down-host</code>, or <code>down-client</code>). If the address family for security gateway to security gateway communications is IPv6, then a suffix of -v6 is added to the verb.</dl>
<p> <code>PLUTO_CONNECTION</code></p>
<dl>
<dd>is the name of the connection for which we are routing.</dl>
<p> <code>PLUTO_NEXT_HOP</code></p>
<dl>
<dd>is the next hop to which packets bound for the peer must be sent.</dl>
<p> <code>PLUTO_INTERFACE</code></p>
<dl>
<dd>is the name of the ipsec interface to be used.</dl>
<p> <code>PLUTO_ME</code></p>
<dl>
<dd>is the IP address of our host.</dl>
<p> <code>PLUTO_MY_CLIENT</code></p>
<dl>
<dd>is the IP address / count of our client subnet. If the client is just the host, this will be the host&#8217;s own IP address / max (where max is 32 for IPv4 and 128 for IPv6).</dl>
<p> <code>PLUTO_MY_CLIENT_NET</code></p>
<dl>
<dd>is the IP address of our client net. If the client is just the host, this will be the host&#8217;s own IP address.</dl>
<p> <code>PLUTO_MY_CLIENT_MASK</code></p>
<dl>
<dd>is the mask for our client net. If the client is just the host, this will be 255.255.255.255.</dl>
<p> <code>PLUTO_PEER</code></p>
<dl>
<dd>is the IP address of our peer.</dl>
<p> <code>PLUTO_PEER_CLIENT</code></p>
<dl>
<dd>is the IP address / count of the peer&#8217;s client subnet. If the client is just the peer, this will be the peer&#8217;s own IP address / max (where max is 32 for IPv4 and 128 for IPv6).</dl>
<p> <code>PLUTO_PEER_CLIENT_NET</code></p>
<dl>
<dd>is the IP address of the peer&#8217;s client net. If the client is just the peer, this will be the peer&#8217;s own IP address.</dl>
<p> <code>PLUTO_PEER_CLIENT_MASK</code></p>
<dl>
<dd>is the mask for the peer&#8217;s client net. If the client is just the peer, this will be 255.255.255.255.</dl>
<p> <code>PLUTO_MY_PROTOCOL</code></p>
<dl>
<dd>lists the protocols allowed over this IPsec SA.</dl>
<p> <code>PLUTO_PEER_PROTOCOL</code></p>
<dl>
<dd>lists the protocols the peer allows over this IPsec SA.</dl>
<p> <code>PLUTO_MY_PORT</code></p>
<dl>
<dd>lists the ports allowed over this IPsec SA.</dl>
<p> <code>PLUTO_PEER_PORT</code></p>
<dl>
<dd>lists the ports the peer allows over this IPsec SA.</dl>
<p> <code>PLUTO_MY_ID</code></p>
<dl>
<dd>lists our id.</dl>
<p> <code>PLUTO_PEER_ID</code></p>
<dl>
<dd>Dlists our peer&#8217;s id.</dl>
<p> <code>PLUTO_PEER_CA</code></p>
<dl>
<dd>lists the peer&#8217;s CA.</dl>
<p> All output sent by the script to stderr or stdout is logged. The script should return an exit status of 0 if and only if it succeeds. </p>
<p> <code>Pluto</code> waits for the script to finish and will not do any other processing while it is waiting. The script may assume that <code>pluto</code> will not change anything while the script runs. The script should avoid doing anything that takes much time and it should not issue any command that requires processing by <code>pluto</code>. Either of these activities could be performed by a background subprocess of the script.</p>
<h3>Rekeying</h3>
<p>When an SA that was initiated by <code>pluto</code> has only a bit of lifetime left, <code>pluto</code> will initiate the creation of a new SA. This applies to ISAKMP and IPsec SAs. The rekeying will be initiated when the SA&#8217;s remaining lifetime is less than the rekeymargin plus a random percentage, between 0 and rekeyfuzz, of the rekeymargin. </p>
<p> Similarly, when an SA that was initiated by the peer has only a bit of lifetime left, <code>pluto</code> will try to initiate the creation of a replacement. To give preference to the initiator, this rekeying will only be initiated when the SA&#8217;s remaining lifetime is half of rekeymargin. If rekeying is done by the responder, the roles will be reversed: the responder for the old SA will be the initiator for the replacement. The former initiator might also initiate rekeying, so there may be redundant SAs created. To avoid these complications, make sure that rekeymargin is generous. </p>
<p> One risk of having the former responder initiate is that perhaps none of its proposals is acceptable to the former initiator (they have not been used in a successful negotiation). To reduce the chances of this happening, and to prevent loss of security, the policy settings are taken from the old SA (this is the case even if the former initiator is initiating). These may be stricter than those of the connection. </p>
<p> <code>pluto</code> will not rekey an SA if that SA is not the most recent of its type (IPsec or ISAKMP) for its potential connection. This avoids creating redundant SAs. </p>
<p> The random component in the rekeying time (rekeyfuzz) is intended to make certain pathological patterns of rekeying unstable. If both sides decide to rekey at the same time, twice as many SAs as necessary are created. This could become a stable pattern without the randomness. </p>
<p> Another more important case occurs when a security gateway has SAs with many other security gateways. Each of these connections might need to be rekeyed at the same time. This would cause a high peek requirement for resources (network bandwidth, CPU time, entropy for random numbers). The rekeyfuzz can be used to stagger the rekeying times. </p>
<p> Once a new set of SAs has been negotiated, <code>pluto</code> will never send traffic on a superseded one. Traffic will be accepted on an old SA until it expires.</p>
<h3>Selecting a Connection When Responding: Road Warrior Support</h3>
<p>When <code>pluto</code> receives an initial Main Mode message, it needs to decide which connection this message is for. It picks based solely on the source and destination IP addresses of the message. There might be several connections with suitable IP addresses, in which case one of them is arbitrarily chosen. (The ISAKMP SA proposal contained in the message could be taken into account, but it is not.) </p>
<p> The ISAKMP SA is negotiated before the parties pass further identifying information, so all ISAKMP SA characteristics specified in the connection description should be the same for every connection with the same two host IP addresses. At the moment, the only characteristic that might differ is authentication method. </p>
<p> Up to this point, all configuring has presumed that the IP addresses are known to all parties ahead of time. This will not work when either end is mobile (or assigned a dynamic IP address for other reasons). We call this situation &quot;Road Warrior&quot;. It is fairly tricky and has some important limitations, most of which are features of the IKE protocol. </p>
<p> Only the initiator may be mobile: the initiator may have an IP number unknown to the responder. When the responder doesn&#8217;t recognize the IP address on the first Main Mode packet, it looks for a connection with itself as one end and <code>%any</code> as the other. If it cannot find one, it refuses to negotiate. If it does find one, it creates a temporary connection that is a duplicate except with the <code>%any</code> replaced by the source IP address from the packet; if there was no identity specified for the peer, the new IP address will be used. </p>
<p> When <code>pluto</code> is using one of these temporary connections and needs to find the preshared secret or RSA private key in <i>ipsec.secrets</i>, and and the connection specified no identity for the peer, <code>%any</code> is used as its identity. After all, the real IP address was apparently unknown to the configuration, so it is unreasonable to require that it be used in this table. </p>
<p> Part way into the Phase 1 (Main Mode) negotiation using one of these temporary connection descriptions, <code>pluto</code> will be receive an Identity Payload. At this point, <code>pluto</code> checks for a more appropriate connection, one with an identity for the peer that matches the payload but which would use the same keys so-far used for authentication. If it finds one, it will switch to using this better connection (or a temporary derived from this, if it has <code>%any</code> for the peer&#8217;s IP address). It may even turn out that no connection matches the newly discovered identity, including the current connection; if so, <code>pluto</code> terminates negotiation. </p>
<p> Unfortunately, if preshared secret authentication is being used, the Identity Payload is encrypted using this secret, so the secret must be selected by the responder without knowing this payload. This limits there to being at most one preshared secret for all Road Warrior systems connecting to a host. RSA Signature authentications does not require that the responder know how to select the initiator&#8217;s public key until after the initiator&#8217;s Identity Payload is decoded (using the responder&#8217;s private key, so that must be preselected). </p>
<p> When <code>pluto</code> is responding to a Quick Mode negotiation via one of these temporary connection descriptions, it may well find that the subnets specified by the initiator don&#8217;t match those in the temporary connection description. If so, it will look for a connection with matching subnets, its own host address, a peer address of <code>%any</code> and matching identities. If it finds one, a new temporary connection is derived from this one and used for the Quick Mode negotiation of IPsec SAs. If it does not find one, <code>pluto</code> terminates negotiation. </p>
<p> Be sure to specify an appropriate nexthop for the responder to send a message to the initiator: <code>pluto</code> has no way of guessing it (if forwarding isn&#8217;t required, use an explicit <code>%direct</code> as the nexthop and the IP address of the initiator will be filled in; the obsolete notation 0.0.0.0 is still accepted). </p>
<p> <code>pluto</code> has no special provision for the initiator side. The current (possibly dynamic) IP address and nexthop must be used in defining connections. These must be properly configured each time the initiator&#8217;s IP address changes. <code>pluto</code> has no mechanism to do this automatically. </p>
<p> Although we call this Road Warrior Support, it could also be used to support encrypted connections with anonymous initiators. The responder&#8217;s organization could announce the preshared secret that would be used with unrecognized initiators and let anyone connect. Of course the initiator&#8217;s identity would not be authenticated. </p>
<p> If any Road Warrior connections are supported, <code>pluto</code> cannot reject an exchange initiated by an unknown host until it has determined that the secret is not shared or the signature is invalid. This must await the third Main Mode message from the initiator. If no Road Warrior connection is supported, the first message from an unknown source would be rejected. This has implications for ease of debugging configurations and for denial of service attacks. </p>
<p> Although a Road Warrior connection must be initiated by the mobile side, the other side can and will rekey using the temporary connection it has created. If the Road Warrior wishes to be able to disconnect, it is probably wise to set <code>&#8211;keyingtries</code> to 1 in the connection on the non-mobile side to prevent it trying to rekey the connection. Unfortunately, there is no mechanism to unroute the connection automatically.</p>
<h3>Debugging</h3>
<p><code>pluto</code> accepts several optional arguments, useful mostly for debugging. Except for <code>&#8211;interface</code>, each should appear at most once. </p>
<p> <code>&#8211;interface</code> <i>interfacename</i></p>
<dl>
<dd>specifies that the named real public network interface should be considered. The interface name specified should not be <code>ipsec</code><i>N</i>. If the option doesn&#8217;t appear, all interfaces are considered. To specify several interfaces, use the option once for each. One use of this option is to specify which interface should be used when two or more share the same IP address.</dl>
<p> <code>&#8211;ikeport</code> <i>port-number</i></p>
<dl>
<dd>changes the UDP port that <code>pluto</code> will use (default, specified by IANA: 500)</dl>
<p> <code>&#8211;ctlbase</code> <i>path</i></p>
<dl>
<dd>basename for control files. <i>path</i>.ctl is the socket through which <code>whack</code> communicates with <code>pluto</code>. <i>path</i>.pid is the lockfile to prevent multiple <code>pluto</code> instances. The default is /var/run/pluto/pluto).</dl>
<p> <code>&#8211;secretsfile</code> <i>file</i></p>
<dl>
<dd>specifies the file for authentication secrets (default: /etc/ipsec.secrets). This name is subject to &quot;globbing&quot; as in <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1), so every file with a matching name is processed. Quoting is generally needed to prevent the shell from doing the globbing.</dl>
<p> <code>&#8211;nofork</code></p>
<dl>
<dd>disable &quot;daemon fork&quot; (default is to fork). In addition, after the lock file and control socket are created, print the line &quot;Pluto initialized&quot; to standard out.</dl>
<p> <code>&#8211;uniqueids</code></p>
<dl>
<dd>if this option has been selected, whenever a new ISAKMP SA is established, any connection with the same Peer ID but a different Peer IP address is unoriented (causing all its SAs to be deleted). This helps clean up dangling SAs when a connection is lost and then regained at another IP address.</dl>
<p> <code>&#8211;force-busy</code></p>
<dl>
<dd>if this option has been selected, pluto will be forced to be &quot;busy&quot;. In this state, which happens when there is a Denial of Service attack, will force pluto to use cookies before accepting new incoming IKE packets. Cookies are send and required in ikev1 Aggressive Mode and in ikev2. This option is mostly used for testing purposes, but can be selected by paranoid administrators as well.</dl>
<p> <code>&#8211;stderrlog</code></p>
<dl>
<dd>log goes to standard out {default is to use <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8))</dl>
<p> For example </p>
<p> pluto &#8211;secretsfile ipsec.secrets &#8211;ctlbase pluto.base &#8211;ikeport 8500 &#8211;nofork &#8211;use-nostack &#8211;stderrlog</p>
<dl>
<dd></dl>
<p> lets one test <code>pluto</code> without using the superuser account. </p>
<p> <code>pluto</code> is willing to produce a prodigious amount of debugging information. There are several classes of debugging output, and <code>pluto</code> may be directed to produce a selection of them. All lines of debugging output are prefixed with &quot;|&nbsp;<wbr>&quot; to distinguish them from error messages. </p>
<p> When <code>pluto</code> is invoked, it may be given arguments to specify which classes to output. The current options are: </p>
<p> <code>&#8211;debug-none</code></p>
<dl>
<dd>disable all debugging</dl>
<p> <code>&#8211;debug-all</code></p>
<dl>
<dd>enable all debugging</dl>
<p> <code>&#8211;debug-raw</code></p>
<dl>
<dd>show the raw bytes of messages</dl>
<p> <code>&#8211;debug-crypt</code></p>
<dl>
<dd>show the encryption and decryption of messages</dl>
<p> <code>&#8211;debug-parsing</code></p>
<dl>
<dd>show the structure of input messages</dl>
<p> <code>&#8211;debug-emitting</code></p>
<dl>
<dd>show the structure of output messages</dl>
<p> <code>&#8211;debug-control</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s decision making</dl>
<p> <code>&#8211;debug-controlmore</code></p>
<dl>
<dd>show even more detailed <code>pluto</code> decision making</dl>
<p> <code>&#8211;debug-lifecycle</code></p>
<dl>
<dd>[this option is temporary] log more detail of lifecycle of SAs</dl>
<p> <code>&#8211;debug-klips</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s interaction with <code>KLIPS</code></dl>
<p> <code>&#8211;debug-pfkey</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s <code>PFKEY</code>interface communication</dl>
<p> <code>&#8211;debug-dns</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s interaction with <code>DNS</code> for KEY and TXT records</dl>
<p> <code>&#8211;debug-dpd</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s <code>Dead Peer Detection</code> handling</dl>
<p> <code>&#8211;debug-natt</code></p>
<dl>
<dd>show <code>pluto</code>&#8216;s <code>NAT Traversal</code> handling</dl>
<p> <code>&#8211;debug-oppo</code></p>
<dl>
<dd>show why <code>pluto</code> didn&#8217;t find a suitable DNS TXT record to authorize opportunistic initiation</dl>
<p> <code>&#8211;debug-oppoinfo</code></p>
<dl>
<dd>log when connections are initiated due to acquires from the kernel. This is often useful to know, but can be extremely chatty on a busy system.</dl>
<p> <code>&#8211;debug-whackwatch</code></p>
<dl>
<dd>if set, causes pluto not to release the whack &#8211;initiate channel until the SA is completely up. This will cause the requestor to possibly wait forever while pluto unsuccessfully negotiates. Used often in test cases.</dl>
<p> <code>&#8211;debug-private</code></p>
<dl>
<dd>allow debugging output with private keys.</dl>
<p> The debug form of the <code>whack</code> command will change the selection in a running <code>pluto</code>. If a connection name is specified, the flags are added whenever <code>pluto</code> has identified that it is dealing with that connection. Unfortunately, this is often part way into the operation being observed. </p>
<p> For example, to start a <code>pluto</code> with a display of the structure of input and output: </p>
<p> pluto &#8211;debug-emitting &#8211;debug-parsing </p>
<p> To later change this <code>pluto</code> to only display raw bytes: </p>
<p> whack &#8211;debug-raw </p>
<p> Hint: ISAKMP SAs are often kept alive by IKEs even after the IPsec SA is established. This allows future IPsec SA&#8217;s to be negotiated directly. If one of the IKEs is restarted, the other may try to use the ISAKMP SA but the new IKE won&#8217;t know about it. This can lead to much confusion. <code>pluto</code> is not yet smart enough to get out of such a mess.</p>
<h3>Pluto&#8217;s Behaviour When Things Go Wrong</h3>
<p>When <code>pluto</code> doesn&#8217;t understand or accept a message, it just ignores the message. It is not yet capable of communicating the problem to the other IKE daemon (in the future it might use Notifications to accomplish this in many cases). It does log a diagnostic. </p>
<p> When <code>pluto</code> gets no response from a message, it resends the same message (a message will be sent at most three times). This is appropriate: UDP is unreliable. </p>
<p> When pluto gets a message that it has already seen, there are many cases when it notices and discards it. This too is appropriate for UDP. </p>
<p> Combine these three rules, and you can explain many apparently mysterious behaviours. In a <code>pluto</code> log, retrying isn&#8217;t usually the interesting event. The critical thing is either earlier (<code>pluto</code> got a message which it didn&#8217;t like and so ignored, so it was still awaiting an acceptable message and got impatient) or on the other system (<code>pluto</code> didn&#8217;t send a reply because it wasn&#8217;t happy with the previous message).</p>
<h3>Notes</h3>
<p>If <code>pluto</code> is compiled without -DKLIPS, it negotiates Security Associations but never ask the kernel to put them in place and never makes routing changes. This allows <code>pluto</code> to be tested on systems without <code>KLIPS</code>, but makes it rather useless. </p>
<p> Each IPsec SA is assigned an SPI, a 32-bit number used to refer to the SA. The IKE protocol lets the destination of the SA choose the SPI. The range 0 to 0xFF is reserved for IANA. <code>Pluto</code> also avoids choosing an SPI in the range 0x100 to 0xFFF, leaving these SPIs free for manual keying. Remember that the peer, if not <code>pluto</code>, may well chose SPIs in this range.</p>
<h3>Policies</h3>
<p>This catalogue of policies may be of use when trying to configure <code>Pluto</code> and another IKE implementation to interoperate. </p>
<p> In Phase 1, only Main Mode is supported. We are not sure that Aggressive Mode is secure. For one thing, it does not support identity protection. It may allow more severe Denial Of Service attacks. </p>
<p> No Informational Exchanges are supported. These are optional and since their delivery is not assured, they must not matter. It is the case that some IKE implementations won&#8217;t interoperate without Informational Exchanges, but we feel they are broken. </p>
<p> No Informational Payloads are supported. These are optional, but useful. It is of concern that these payloads are not authenticated in Phase 1, nor in those Phase 2 messages authenticated with <a href="/docs/linux/man/3-hash/">HASH</a>(3). </p>
<p> &bull;</p>
<dl>
<dd>Diffie Hellman Groups MODP 1024 and MODP 1536 (2 and 5) are supported. Group MODP768 (1) is not supported because it is too weak.</dl>
<p> &bull;</p>
<dl>
<dd>Host authentication can be done by RSA Signatures or Pre-Shared Secrets.</dl>
<p> &bull;</p>
<dl>
<dd>3DES CBC (Cypher Block Chaining mode) is the only encryption supported, both for ISAKMP SAs and IPSEC SAs.</dl>
<p> &bull;</p>
<dl>
<dd>MD5 and SHA1 hashing are supported for packet authentication in both kinds of SAs.</dl>
<p> &bull;</p>
<dl>
<dd>The ESP, AH, or AH plus ESP are supported. If, and only if, AH and ESP are combined, the ESP need not have its own authentication component. The selection is controlled by the &#8211;encrypt and &#8211;authenticate flags.</dl>
<p> &bull;</p>
<dl>
<dd>Each of these may be combined with IPCOMP Deflate compression, but only if the potential connection specifies compression and only if KLIPS is configured with IPCOMP support.</dl>
<p> &bull;</p>
<dl>
<dd>The IPSEC SAs may be tunnel or transport mode, where appropriate. The &#8211;tunnel flag controls this when <code>pluto</code> is initiating.</dl>
<p> &bull;</p>
<dl>
<dd>When responding to an ISAKMP SA proposal, the maximum acceptable lifetime is eight hours. The default is one hour. There is no minimum. The &#8211;ikelifetime flag controls this when <code>pluto</code> is initiating.</dl>
<p> &bull;</p>
<dl>
<dd>When responding to an IPSEC SA proposal, the maximum acceptable lifetime is one day. The default is eight hours. There is no minimum. The &#8211;ipseclifetime flag controls this when <code>pluto</code> is initiating.</dl>
<p> &bull;</p>
<dl>
<dd>PFS is acceptable, and will be proposed if the &#8211;pfs flag was specified. The DH group proposed will be the same as negotiated for Phase 1.</dl>
<h2>Signals</h2>
<p><code>Pluto</code> responds to <code>SIGHUP</code> by issuing a suggestion that &#8220;<code>whack</code> &#8211;listen&#8221; might have been intended. </p>
<p> <code>Pluto</code> exits when it receives <code>SIGTERM</code>.</p>
<h2>Exit Status</h2>
<p><code>pluto</code> normally forks a daemon process, so the exit status is normally a very preliminary result. </p>
<p> 0</p>
<dl>
<dd>means that all is OK so far.</dl>
<p> 1</p>
<dl>
<dd>means that something was wrong.</dl>
<p> 10</p>
<dl>
<dd>means that the lock file already exists.</dl>
<p> If <code>whack</code> detects a problem, it will return an exit status of 1. If it received progress messages from <code>pluto</code>, it returns as status the value of the numeric prefix from the last such message that was not a message sent to syslog or a comment (but the prefix for success is treated as 0). Otherwise, the exit status is 0.</p>
<h2>Files</h2>
<p>/var/run/pluto/pluto.pid/var/run/pluto/pluto.ctl/etc/ipsec.secrets/dev/urandom</p>
<h2>Environment</h2>
<p><i>IPSEC_EXECDIR</i><i>IPSECmyid</i><i>PLUTO_CORE_DIR</i></p>
<h2>See Also</h2>
<p>The rest of the Libreswan distribution, in particular <code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8). </p>
<p> <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) is designed to make using <code>pluto</code> more pleasant. Use it! </p>
<p> <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5) describes the format of the secrets file. </p>
<p> <code><a href="/docs/linux/man/3-ipsec_atoaddr/">ipsec_atoaddr</a></code>(3), part of the Libreswan distribution, describes the forms that IP addresses may take. <code><a href="/docs/linux/man/3-ipsec_atosubnet/">ipsec_atosubnet</a></code>(3), part of the Libreswan distribution, describes the forms that subnet specifications. </p>
<p> For more information on IPsec, the mailing list, and the relevant documents, see: </p>
<p> <i>m[blue]</i><code><a rel="nofollow" href="https://datatracker.ietf.org/wg/ipsecme/charter/">https://datatracker.ietf.org/wg/ipsecme/charter/</a></code>m[] </p>
<p> At the time of writing, the most relevant IETF RFCs are: </p>
<p> RFC5996 Internet Key Exchange Protocol Version 2 (IKEv2) </p>
<p> The Libreswan web site &lt;<a rel="nofollow" href="https://libreswan.org">https://libreswan.org</a>&gt; and the mailing lists described there.</p>
<h2>History</h2>
<p>This code is released under the GPL terms. See the accompanying files COPYING and CREDITS.* for more details. </p>
<p> This software was originally written for the FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt;, founded by John Gilmore and managed by Hugh Daniel. It was written by Angelos D. Keromytis (angelos [at] dsl.cis.upenn.edu), in May/June 1997, in Athens, Greece. Thanks go to John Ioannidis for his help. </p>
<p> FreeS/WAN&#8217;s Pluto was developed/maintained from 2000-2004 by D. Hugh Redelmeier (hugh [at] mimosa.com), in Canada. The regulations of Greece and Canada allow the code to be freely redistributable. </p>
<p> Richard Guy Briggs &lt;rgb [at] conscoop.ottawa.on.ca&gt; was the main resource on KLIPS development </p>
<p> IKE version 2 was initially written by Michael Richardson, Antony Antony and Paul Wouters. It has since been extended by Avesh Agarwal, D. Hugh Redelmeier, Matt Rogers, Antony Antony and Paul Wouters. </p>
<p> From 2003 onwards, the code was developed and maintained by The Openswan Project by developers worldwide and distributed from The Netherland and Finland. Due to a lawsuit by Xelerance over the trademark, the project was forced to rename itself and the code to The Libreswan Project in 2012. </p>
<p> See further: the CHANGES/CREDITS files in the main directory and the doc/ directory.</p>
<h2>Bugs</h2>
<p>Please see &lt;m[blue]<code><a rel="nofollow" href="https://bugs.libreswan.org">https://bugs.libreswan.org</a></code>m[]&gt; for a list of currently known bugs and missing features. </p>
<p> Bugs should be reported to the &lt;swan-dev [at] lists.libreswan.org&gt; mailing list.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>placeholder to suppress warning</dl>
