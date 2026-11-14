---
title: "ipsec-conf(5)"
name: "ipsec-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsec-conf/"
description: "ipsec.conf – IPsec configuration and connections"
---

<p>ipsec.conf &#8211; IPsec configuration and connections</p>
<h2>Description</h2>
<p>The <i>ipsec.conf</i> file specifies most configuration and control information for the Libreswan IPsec subsystem. (The major exception is secrets for authentication; see <code><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></code>(5).) Its contents are not security-sensitive. Configurations can be added using this configuration file or by using ipsec whack directly. This means that technically, the ipsec.conf file is optional, but a few warning might show up when this file is missing. </p>
<p> The file is a text file, consisting of one or more <i>sections</i>. White space followed by <code>#</code> followed by anything to the end of the line is a comment and is ignored, as are empty lines which are not within a section. </p>
<p> A line which contains <code>include</code> and a file name, separated by white space, is replaced by the contents of that file, preceded and followed by empty lines. If the file name is not a full pathname, it is considered to be relative to the directory containing the including file. Such inclusions can be nested. Only a single filename may be supplied, and it may not contain white space, but it may include shell wildcards (see <code><a href="/docs/linux/man/1-sh/">sh</a></code>(1)); for example: </p>
<p> <code>include </code><code>/etc/ipsec.d/*.conf</code> </p>
<p> The intention of the include facility is mostly to permit keeping information on connections, or sets of connections, separate from the main configuration file. This permits such connection descriptions to be changed, copied to the other security gateways involved, etc., without having to constantly extract them from the configuration file and then insert them back into it. Note also the <code>also</code> and <code>alsoflip</code> parameters (described below) which permit splitting a single logical section (e.g. a connection description) into several actual sections. </p>
<p> The first significant line of the file may specify a version of this specification for backwards compatibility with freeswan and openswan. It is ignored and unused. For compatibility with openswan, specify: </p>
<p> <code>version 2</code> </p>
<p> A section begins with a line of the form: </p>
<p> <i>type</i>&nbsp;<wbr><i>name</i> </p>
<p> where <i>type</i> indicates what type of section follows, and <i>name</i> is an arbitrary name which distinguishes the section from others of the same type. (Names must start with a letter and may contain only letters, digits, periods, underscores, and hyphens.) All subsequent non-empty lines which begin with white space are part of the section; comments within a section must begin with white space too. There may be only one section of a given type with a given name. </p>
<p> Lines within the section are generally of the form </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>parameter</i><code>=</code><i>value</i> </p>
<p> (note the mandatory preceding white space). There can be white space on either side of the <code>=</code>. Parameter names follow the same syntax as section names, and are specific to a section type. Unless otherwise explicitly specified, no parameter name may appear more than once in a section. </p>
<p> An empty <i>value</i> stands for the system default value (if any) of the parameter, i.e. it is roughly equivalent to omitting the parameter line entirely. A <i>value</i> may contain white space only if the entire <i>value</i> is enclosed in double quotes (<code>&quot;</code>); a <i>value</i> cannot itself contain a double quote, nor may it be continued across more than one line. </p>
<p> Numeric values are specified to be either an &#8220;integer&#8221; (a sequence of digits) or a &#8220;decimal number&#8221; (sequence of digits optionally followed by `.&#8217; and another sequence of digits). </p>
<p> There is currently one parameter which is available in any type of section: </p>
<p> <code>also</code></p>
<dl>
<dd>the value is a section name; the parameters of that section are appended to this section, as if they had been written as part of it. The specified section must exist, must follow the current one, and must have the same section type. (Nesting is permitted, and there may be more than one <code>also</code> in a single section, although it is forbidden to append the same section more than once.) This allows, for example, keeping the encryption keys for a connection in a separate file from the rest of the description, by using both an <code>also</code> parameter and an <code>include</code> line. (Caution, see BUGS below for some restrictions.)</dl>
<p> <code>alsoflip</code></p>
<dl>
<dd>can be used in a <code>conn</code> section. It acts like an <code>also</code> that flips the referenced section&#8217;s entries left-for-right.</dl>
<p> Parameter names beginning with <code>x-</code> (or <code>X-</code>, or <code>x_</code>, or <code>X_</code>) are reserved for user extensions and will never be assigned meanings by IPsec. Parameters with such names must still observe the syntax rules (limits on characters used in the name; no white space in a non-quoted value; no newlines or double quotes within the value). All other as-yet-unused parameter names are reserved for future IPsec improvements. </p>
<p> A section with name <code>%default</code> specifies defaults for sections of the same type. For each parameter in it, any section of that type which does not have a parameter of the same name gets a copy of the one from the <code>%default</code> section. There may be multiple <code>%default</code> sections of a given type, but only one default may be supplied for any specific parameter name. <code>%default</code> sections may not contain <code>also</code> or <code>alsoflip</code> parameters. </p>
<p> Currently there are two types of section: a <code>config</code> section specifies general configuration information for IPsec, while a <code>conn</code> section specifies an IPsec connection.</p>
<h2>Conn Sections</h2>
<p>A <code>conn</code> section contains a <i>connection specification</i>, defining a network connection to be made using IPsec. The name given is arbitrary, and is used to identify the connection to <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8) Here&#8217;s a simple example: </p>
<dl>
<dd>
<pre><code>conn snt
 left=10.11.11.1
 leftsubnet=10.0.1.0/24
 leftnexthop=172.16.55.66
 leftsourceip=10.0.1.1
 right=192.168.22.1
 rightsubnet=10.0.2.0/24
 rightnexthop=172.16.88.99
 rightsourceip=10.0.2.1
 keyingtries=%forever</code></pre>
</dl>
<p> A note on terminology&#8230; In automatic keying, there are two kinds of communications going on: transmission of user IP packets, and gateway-to-gateway negotiations for keying, rekeying, and general control. The data path (a set of &#8220;IPsec SAs&#8221;) used for user packets is herein referred to as the &#8220;connection&#8221;; the path used for negotiations (built with &#8220;ISAKMP SAs&#8221;) is referred to as the &#8220;keying channel&#8221;. </p>
<p> To avoid trivial editing of the configuration file to suit it to each system involved in a connection, connection specifications are written in terms of <i>left</i> and <i>right</i> participants, rather than in terms of local and remote. Which participant is considered <i>left</i> or <i>right</i> is arbitrary; IPsec figures out which one it is being run on based on internal information. This permits using identical connection specifications on both ends. There are cases where there is no symmetry; a good convention is to use <i>left</i> for the local side and <i>right</i> for the remote side (the first letters are a good mnemonic). </p>
<p> Many of the parameters relate to one participant or the other; only the ones for <i>left</i> are listed here, but every parameter whose name begins with <code>left</code> has a <code>right</code> counterpart, whose description is the same but with <code>left</code> and <code>right</code> reversed. </p>
<p> Parameters are optional unless marked &#8220;(required)&#8221;</p>
<h3>Conn Parameters: General</h3>
<p>The following parameters are relevant to IKE automatic keying. Unless otherwise noted, for a connection to work, in general it is necessary for the two ends to agree exactly on the values of these parameters. </p>
<p> <code>keyexchange</code></p>
<dl>
<dd>method of key exchange; the default and currently the only accepted value is <code>ike</code></dl>
<p> <code>connaddrfamily</code></p>
<dl>
<dd>the connection address family of the connection; currently the accepted values are <code>ipv4</code> (the default); or <code>ipv6</code>. This option is confusing, especially when doing IPv4-in-IPv6 or IPv6-in-IPv4 tunnels. The developers hope to remove this option in the near future for proper auto-detection. For now, set connaddrfamily= to the family of the *subnet= options, and if those are not defined, to the family of the left=/right= options. </p>
<p> IPv6 is supported with NETKEY and with KLIPS in all Libreswan versions</dl>
<p> <code>type</code></p>
<dl>
<dd>the type of the connection; currently the accepted values are <code>tunnel</code> (the default) signifying a host-to-host, host-to-subnet, or subnet-to-subnet tunnel; <code>transport</code>, signifying host-to-host transport mode; <code>passthrough</code>, signifying that no IPsec processing should be done at all; <code>drop</code>, signifying that packets should be discarded; and <code>reject</code>, signifying that packets should be discarded and a diagnostic ICMP returned.</dl>
<p> <code>left</code></p>
<dl>
<dd>(required) the IP address of the left participant&#8217;s public-network interface, in any form accepted by <code><a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a></code>(3). Currently, IPv4 and IPv6 IP addresses are supported. There are several magic values. If it is <code>%defaultroute</code>, and the <code>config setup</code> section&#8217;s, <code>interfaces</code> specification contains <code>%defaultroute</code>, <code>left</code> will be filled in automatically with the local address of the default-route interface (as determined at IPsec startup time); this also overrides any value supplied for <code>leftnexthop</code>. (Either <code>left</code> or <code>right</code> may be <code>%defaultroute</code>, but not both.) The value <code>%any</code> signifies an address to be filled in (by automatic keying) during negotiation. The value <code>%opportunistic</code> signifies that both <code>left</code> and <code>leftnexthop</code> are to be filled in (by automatic keying) from DNS data for <code>left</code>&#8216;s client. The value can also contain the interface name, which will then later be used to obtain the IP address from to fill in. For example <code>%ppp0</code> The values <code>%group</code> and <code>%opportunisticgroup</code> makes this a policy group conn: one that will be instantiated into a regular or opportunistic conn for each CIDR block listed in the policy group file with the same name as the conn. </p>
<p> If using IP addresses in combination with NAT, always use the actual local machine&#8217;s (NATed) IP address, and if the remote (eg right=) is NATed as well, the remote&#8217;s public (<code>not</code> NATed) IP address. Note that this makes the configuration no longer symmetrical on both sides, so you cannot use an identical configuration file on both hosts.</dl>
<p> <code>leftsubnet</code></p>
<dl>
<dd>private subnet behind the left participant, expressed as <i>network</i><code>/</code><i>netmask</i> (actually, any form acceptable to <code><a href="/docs/linux/man/3-ipsec_ttosubnet/">ipsec_ttosubnet</a></code>(3)); Currently, IPv4 and IPv6 ranges are supported. if omitted, essentially assumed to be <i>left</i>/32, signifying that the left end of the connection goes to the left participant only </p>
<p> It supports two magic shorthands <i>vhost:</i> and <i>vnet:</i>, which can list subnets in the same syntax as <i>virtual-private</i>. The value <i>%priv</i> expands to the networks specified in <i>virtual-private</i>. The value <i>%no</i> means no subnet. A common use for allowing roadwarriors to come in on public IPs or via accepted NATed networks from RFC1918 is to use <i>leftsubnet=vhost:%no,%priv</i>. The <i>vnet:</i> option can be used to allow RFC1918 subnets without hardcoding them. When using vnet the connection will instantiate, allowing for multiple tunnels with different subnets.</dl>
<p> <code>leftsubnets</code></p>
<dl>
<dd>specify multiple private subnets behind the left participant, expressed as { <i>networkA</i><code>/</code><i>netmaskA</i><i>networkB</i><code>/</code><i>netmaskB</i><i>[&#8230;]</i> } If both a leftsubnets= and rightsubnets= are defined, all combinations of subnet tunnels will be established as IPsec tunnels. You cannot use leftsubnet= and leftsubnets= together. For examples see <i>testing/pluto/multinet-*</i>.</dl>
<p> <code>leftvti</code></p>
<dl>
<dd>the address/mask to configure on the VTI interface when <i>vti-interface</i> is set. It takes the form of <i>network</i><code>/</code><i>netmask</i> (actually, any form acceptable to <code><a href="/docs/linux/man/3-ipsec_ttosubnet/">ipsec_ttosubnet</a></code>(3)); Currently, IPv4 and IPv6 ranges are supported. This option is often used in combination with routed based VPNs.</dl>
<p> <code>leftaddresspool</code></p>
<dl>
<dd>address pool from with the XAUTH server can assign IP addresses to clients. When configured as an XAUTH server, using <i>leftxauthserver=yes</i> this option specifies the address pool from which IP addresses are taken to assign the the XAUTH clients. The syntax of the address pool specifies a range (not a CIDR), in the following syntax: <i>rightaddresspool=192.168.1.100-192.168.1.200</i>. Generally, the <i>rightaddresspool=</i> option will be accompanied by <i>rightxauthclient=yes</i>, <i>leftxauthserver=yes</i> and <i>leftsubnet=0.0.0.0/0</i> option. </p>
<p> When <i>leftaddresspool=</i> is specified, the connection may not specify either <i>leftsubnet=</i> or <i>leftsubnets=</i>. Address pools are fully allocated when the connection is loaded, so the ranges should be sane. For example, specifying a range <i>rightaddresspool=10.0.0.0-11.0.0.0</i> will lead to massive memory allocation. Address pools specifying the exact same range are shared between different connections. Different addresspools should not be defined to partially overlap.</dl>
<p> <code>leftprotoport</code></p>
<dl>
<dd>allowed protocols and ports over connection, also called Port Selectors. The argument is in the form <i>protocol</i>, which can be a number or a name that will be looked up in <i>/etc/protocols</i>, such as <i>leftprotoport=icmp</i>, or in the form of <i>protocol/port</i>, such as <i>tcp/smtp</i>. Ports can be defined as a number (eg. 25) or as a name (eg smtp) which will be looked up in <i>/etc/services</i>. A special keyword <i>%any</i> can be used to allow all ports of a certain protocol. The most common use of this option is for L2TP connections to only allow l2tp packets (UDP port 1701), eg: <i>leftprotoport=17/1701</i>. </p>
<p> To filter on specific icmp type and code, use the higher 8 bits for type and the lower 8 bits for port. For example, to allow icmp echo packets (type 8, code 0) the &#8216;port&#8217; would be 0x0800, or 2048 in decimal, so you configure <i>leftprotoport=icmp/2048</i>. Similarly, to allow ipv6-icmp Neighbour Discovery which has type 136 (0x88) and code 0(0x00) this becomes 0x8800 or in decimal 34816 resulting in <i>leftprotoport=ipv6-icmp/34816</i> . </p>
<p> Some clients, notably older Windows XP and some Mac OSX clients, use a random high port as source port. In those cases <i>rightprotoport=17/%any</i> can be used to allow all UDP traffic on the connection. Note that this option is part of the proposal, so it cannot be arbitrarily left out if one end does not care about the traffic selection over this connection &#8211; both peers have to agree. The Port Selectors show up in the output of <i>ipsec eroute</i> and <i>ipsec auto &#8211;status</i> eg:<i>&quot;l2tp&quot;: 193.110.157.131[@aivd.libreswan.org]:7/1701&#8230;%any:17/1701</i> This option only filters outbound traffic. Inbound traffic selection must still be based on firewall rules activated by an updown script. The variables $PLUTO_MY_PROTOCOL, $PLUTO_PEER_PROTOCOL, $PLUTO_MY_PORT, and $PLUTO_PEER_PORT are available for use in <i>updown</i> scripts. Older workarounds for bugs involved a setting of <i>17/0</i> to denote <i>any single UDP port</i> (not UDP port 0). Some clients, most notably OSX, uses a random high port, instead of port 1701 for L2TP.</dl>
<p> <code>leftnexthop</code></p>
<dl>
<dd>next-hop gateway IP address for the left participant&#8217;s connection to the public network; defaults to <code>%direct</code> (meaning <i>right</i>). If the value is to be overridden by the <code>left=%defaultroute</code> method (see above), an explicit value must <i>not</i> be given. If that method is not being used, but <code>leftnexthop</code> is <code>%defaultroute</code>, and <code>interfaces=%defaultroute</code> is used in the <code>config setup</code> section, the next-hop gateway address of the default-route interface will be used. The magic value <code>%direct</code> signifies a value to be filled in (by automatic keying) with the peer&#8217;s address. Relevant only locally, other end need not agree on it.</dl>
<p> <code>leftsourceip</code></p>
<dl>
<dd>the IP address for this host to use when transmitting a packet to the other side of this link. Relevant only locally, the other end need not agree. This option is used to make the gateway itself use its internal IP, which is part of the leftsubnet, to communicate to the rightsubnet or right. Otherwise, it will use its <code>nearest</code> IP address, which is its public IP address. This option is mostly used when defining subnet-subnet connections, so that the gateways can talk to each other and the subnet at the other end, without the need to build additional host-subnet, subnet-host and host-host tunnels. Both IPv4 and IPv6 addresses are supported.</dl>
<p> <code>leftupdown</code></p>
<dl>
<dd>what &#8220;updown&#8221; script to run to adjust routing and/or firewalling when the status of the connection changes (default <code>ipsec _updown</code>). May include positional parameters separated by white space (although this requires enclosing the whole string in quotes); including shell metacharacters is unwise. An example to enable routing when using the NETKEY stack, one can use: </p>
<p> leftupdown=&quot;ipsec _updown &#8211;route yes&quot; </p>
<p> See <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8) for details. Relevant only locally, other end need not agree on it.</dl>
<p> <code>leftfirewall</code></p>
<dl>
<dd>This option is obsolete and should not used anymore.</dl>
<p> If one or both security gateways are doing forwarding firewalling (possibly including masquerading), and this is specified using the firewall parameters, tunnels established with IPsec are exempted from it so that packets can flow unchanged through the tunnels. (This means that all subnets connected in this manner must have distinct, non-overlapping subnet address blocks.) This is done by the default <i>updown</i> script (see <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8)). </p>
<p> The implementation of this makes certain assumptions about firewall setup, and the availability of the <i>Linux Advanced Routing</i> tools. In situations calling for more control, it may be preferable for the user to supply his own <i>updown</i> script, which makes the appropriate adjustments for his system.</p>
<h3>Conn Parameters: Automatic Keying</h3>
<p>The following parameters are relevant to automatic keying via IKE. Unless otherwise noted, for a connection to work, in general it is necessary for the two ends to agree exactly on the values of these parameters. </p>
<p> <code>auto</code></p>
<dl>
<dd>what operation, if any, should be done automatically at IPsec startup; currently-accepted values are <code>add</code> (signifying an <code>ipsec auto</code><code>&#8211;add</code>), <code>ondemand</code> (signifying that plus an <code>ipsec auto</code><code>&#8211;ondemand</code>), <code>start</code> (signifying that plus an <code>ipsec auto</code><code>&#8211;up</code>), and <code>ignore</code> (also the default) (signifying no automatic startup operation). See the <code>config setup</code> discussion below. Relevant only locally, other end need not agree on it (but in general, for an intended-to-be-permanent connection, both ends should use <code>auto=start</code> to ensure that any reboot causes immediate renegotiation). </p>
<p> The option <code>ondemand</code> used to be called <code>route</code></dl>
<p> <code>authby</code></p>
<dl>
<dd>how the two security gateways should authenticate each other; acceptable values are <code>rsasig</code> (the default) for RSA digital signatures based authentication, <code>secret</code> for shared secrets (PSK) authentication, <code>secret|rsasig</code> for either, <code>never</code> if negotiation is never to be attempted or accepted (useful for shunt-only conns), and <code>null</code> for null-authentication. </p>
<p> If asymmetric authentication is requested, IKEv2 must be enabled, and the options <code>leftauth=</code> and <code>rightauth=</code> should be used instead of authby. </p>
<p> Digital signatures are superior in every way to shared secrets. Especially IKEv1 in Aggressive Mode is vulnerable to offline dictionary attacks and is performed routinely by at least the NSA on monitored internet traffic globally. The never option is only used for connections that do not actually start an IKE negotiation, such as type=passthrough connections. The auth method null is used for &quot;anonymous opportunistic IPsec&quot; and should not be used for regular pre-configured IPsec VPNs.</dl>
<p> <code>ike</code></p>
<dl>
<dd>IKE encryption/authentication algorithm to be used for the connection (phase 1 aka ISAKMP SA). The format is <i>&quot;cipher-hash;modpgroup, cipher-hash;modpgroup, &#8230;&quot;</i> Any left out option will be filled in with all allowed default options. Multiple proposals are separated by a comma. If an <code>ike=</code> line is specified, no other received proposals will be accepted. Formerly there was a distinction (by using a <code>&quot;!&quot;</code> symbol) between &quot;strict mode&quot; or not. That mode has been obsoleted. If an <code>ike=</code> option is specified, the mode is always strict, meaning no other received proposals will be accepted. Some examples are <code>ike=3des-sha1,aes-sha1</code>, <code>ike=aes</code>, <code>ike=aes_ctr</code>, <code>ike=aes_gcm256-sha2</code>, <code>ike=aes128-md5;modp2048</code>, <code>ike=aes256-sha2;dh19</code>, <code>ike=aes128-sha1;dh22</code>, <code>ike=3des-md5;modp1024,aes-sha1;modp1536</code>. The options must be suitable as a value of <code><a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a></code>(8)&#8217;s <code>&#8211;ike</code> option. The default IKE proposal depends on the version of libreswan used. It follow the recommendations of RFC4306, RFC7321 and as of this writing their successor draft documents RFC4306bis and RFC7321bis. For IKEv1, 3DES, SHA1 and MODP1536 are still allowed per default for backwards compatibility. IKEv2&#8217;s minimum is AES, MODP2048 and SHA2. The default key size is 256 bits. The default AES_GCM ICV is 16 bytes. </p>
<p> Note that AES-GCM is an AEAD algorithm, meaning that it performs encryption+authentication in one step. This means that AES-GCM must not specify an authentication algorithm. However, it does require a PRF function, so the second argument to an AEAD algorithm denotes the PRF. So ike=aes_gcm-sha2 means propose AES_GCM with no authentication and using SHA2 as the prf. Note that for phase2alg, there is no prf, so AES-GCM is specified for ESP as phase2alg=aes_gcm-null. The AES-GCM and AES-CCM algorithms support 8,12 and 16 byte ICV&#8217;s. These can be specified using a postfix, for example aes_gcm_a (for 8), aes_gcm_b (for 12) and aes_gcm_c (for 16). The default (aes_gcm without postfix) refers to the 16 byte ICV version. It is strongly recommended to NOT use the 8 or 12 byte versions of GCM or CCM. </p>
<p> Weak algorithms are regularly removed from libreswan. Currently, 1DES and modp768 have been removed and modp1024 will be removed in the near future. Additionally, md5 and sha1 will be removed within the next few years. Null encryption is available, and should only be used for testing or benchmarking purposes. Please do not request for insecure algorithms to be re-added to libreswan. </p>
<p> Diffie-Hellman groups 19,20 and 21 from RFC- 5903 and 22, 23 and 24 from RFC-5114 are also supported. For all groups, the &quot;dh&quot; keyword can be used. For the MODP based groups, the modp= keyword can be used. for example <i>ike=3des-sha1;dh19</i>. The RFC-5114 DH groups are extremely controversial and MUST NOT be used unless forced (administratively) by the other party. Support for these groups will most likely be removed in 2017, as it cannot be proven these DH groups do not have a cryptographic trapdoor embedded in them (a backdoor by the USG who provided these primes without revealing the seeds and generation process used). Due the the weakness od DH22, support for this group is not compiled in by default and can be re-enabled using USE_DH22=true. </p>
<p> The modp syntax will be removed in favour of the dh syntax in the future</dl>
<p> <code>phase2</code></p>
<dl>
<dd>Sets the type of SA that will be produced. Valid options are: <code>esp</code> for encryption (the default), <code>ah</code> for authentication only. </p>
<p> The very first IPsec designs called for use of AH plus ESP to offer authentication, integrity and confidentiality. That dual protocol use was a significant burden, so ESP was extended to offer all three services, and AH remained as an auth/integ. Only broken configurations (often used with racoon) require the strange double authentication using <code>ah+esp</code>. Additionally, AH does not play well with NATs, so it is strongly recommended to use ESP with the null cipher if you require unencrypted authenticated transport.</dl>
<p> <code>phase2alg</code></p>
<dl>
<dd>Specifies the algorithms that will be offered/accepted for a phase2 negotiation. If not specified, a secure set of defaults will be used. Sets are separated using comma&#8217;s. </p>
<p> The default values are the same as for ike= Note also that not all ciphers available to the kernel (eg through CryptoAPI) are necessarily supported here. </p>
<p> The format for ESP is ENC-AUTH followed by one optional PFSgroup. For instance, &quot;3des-md5&quot; or &quot;aes256-sha1;modp2048&quot; or &quot;aes-sha1,aes-md5&quot;. When specifying multiple algorithms, specify the PFSgroup last, e.g. &quot;3des-md5,aes256-sha1;modp2048&quot;. </p>
<p> For RFC-5114 DH groups, use the &quot;dh&quot; keyword, eg &quot;aes256-sha1;dh23&quot;. These specific DH groups are extremely controversial and MUST NOT be used unless forced (administratively) by the other party. Support for these groups will most likely be removed in 2017, as it cannot be proven these DH groups do not have a cryptographic trapdoor embedded in them (a backdoor by the USG who gave us these primes without revealing the seeds and generation process) </p>
<p> The format for AH is AUTH followed by an optional PFSgroup. For instance, &quot;md5&quot; or &quot;sha1;modp1536&quot;. </p>
<p> AEAD algorithms such as AES-GCM and AES-CCM require null for the authentication algorithm, for example <i>phase2alg=aes_ccm-null</i> or <i>phase2alg=aes_gcm-null</i>. Note that the ike= syntax for aes_gcm does not specify a null authentication but specifies the prf instead. The supported key sizes are 128, 192 and 256, which are specified similarly to plain aes, i.e. <i>phase2alg=aes_gcm256</i>. A subscript of <i>_c</i>, <i>_b</i> or <i>_a</i> can be used to refer to the different ICV variants where a means 8 bytes, b means 12 bytes and c means 16 bytes. The default when not using a subscript is the 16 byte ICV, the recommended value by RFC-4106. Therefor phase2alg=aes_gcm256-null is equivalent to phase2alg=aes_gcm_c256-null. It is recommended to migrate to the _c versions (without specifying _c), as support for smaller ICV&#8217;s might be removed in the near future. </p>
<p> The supported algorithms depend on the libreswan version, OS and kernel stack used. Possible ciphers are aes, 3des, aes_ctr, aes_gcm, aes_ccm, camellia, serpent and twofish. </p>
<p> Note that openswan and versions of libreswan up to 3.6 require manually adding the salt size to the key size. Therefor, to configure an older version of openswan or libreswan, use: &quot;phase2alg=aes_ccm_c-280-null&quot; to interop with a new libreswan using &quot;phase2alg=aes_ccm256&quot;. For CCM, the &#8216;keysize&#8217; needs to be increased by 24, resulted in valid keysizes of 152, 215 and 280. For GCM the &#8216;keysize&#8217; needs to be increased by 32, resulting valid &#8216;keysizes&#8217; of 160, 224 and 288.</dl>
<p> <code>sha2-truncbug</code></p>
<dl>
<dd>The default ESP hash truncation for sha2_256 is 128 bits. Some IPsec implementations (Linux before 2.6.33, some Cisco (2811?) routers) implement the draft version which stated 96 bits. If a draft implementation communicates with an RFC implementation, both ends will reject encrypted packets from each other. </p>
<p> This option enables using the draft 96 bits version to interop with those implementations. Currently the accepted values are <code>no</code>, (the default) signifying default RFC truncation of 128 bits, or <code>yes</code>, signifying the draft 96 bits truncation. </p>
<p> Another workaround is to switch from sha2_256 to sha2_128 or sha2_512.</dl>
<p> <code>nat-ikev1-method</code></p>
<dl>
<dd>NAT Traversal in IKEv1 is negotiated via Vendor ID options as specified in RFC 3947. However, many implementations only support the draft version of the RFC. Libreswan sends both the RFC and the most common draft versions (02, 02_n and 03) to maximize interoperability. Unfortunately, there are known broken implementations of RFC 3947, notably Cisco routers that have not been updated to the latest firmware. As the NAT-T payload is sent in the very first packet of the initiator, there is no method to auto-detect this problem and initiate a workaround. </p>
<p> This option allows fine tuning which of the NAT-T payloads to consider for sending and processing. Currently the accepted values are <code>drafts</code>, <code>rfc</code> or <code>both</code> (the default). To interoperate with known broken devices, use nat-ikev1-method=drafts.</dl>
<p> <code>esp</code></p>
<dl>
<dd>This option is obsolete. Please use <code>phase2alg</code> instead.</dl>
<p> <code>ah</code></p>
<dl>
<dd>AH authentication algorithm to be used for the connection, e.g here. <code>hmac-md5</code> The options must be suitable as a value of <code><a href="/docs/linux/man/8-ipsec_spi/">ipsec_spi</a></code>(8)&#8217;s <code>&#8211;ah</code> option. The default is not to use AH. If for some (invalid) reason you still think you need AH, please use esp with the null encryption cipher instead. Note also that not all ciphers available to the kernel (eg through CryptoAPI) are necessarily supported here.</dl>
<p> <code>fragmentation</code></p>
<dl>
<dd>Whether or not to allow IKE fragmentation. Valid values are are <code>yes</code>, (the default), <code>no</code> or <code>force</code>. </p>
<p> IKEv1 fragmentation capabilities are negotiated via a well-known private <i>vendor id</i>. IKEv2 fragmentation support is implemented using RFC 7383. If pluto does not receive the fragmentation payload, no IKE fragments will be sent, regardless of the fragmentation= setting. When set to <code>yes</code>, IKE fragmentation will be attempted on the first re-transmit of an IKE packet of a size larger then 576 bytes for IPv4 and 1280 bytes for IPv6. If fragmentation is set to force, IKE fragmentation is used on initial transmits of such sized packets as well. When we have received IKE fragments for a connection, pluto behaves as if in force mode.</dl>
<p> <code>ikepad</code></p>
<dl>
<dd>Whether or not to pad IKEv1 messages to a multiple of 4 bytes. Valid values are are <code>yes</code>, (the default) and <code>no</code>. </p>
<p> IKE padding is allowed in IKEv1 but it is known to cause interoperability issues. The ikepad= option can be used to disable IKEv1 padding. This is required for some devices (such as Checkpoint in Aggressive Mode) that reject padded IKEv1 packets. In IKEv2, no padding is allowed, and this option has no effect. If you find a device that seems to require IKE padding in IKEv2, please contact the libreswan developers. This option should almost never be enabled.</dl>
<p> <code>ikev2</code></p>
<dl>
<dd>IKEv2 (RFC4309) settings to be used. Currently the accepted values are <code>permit</code>, (the default) signifying no IKEv2 should be transmitted, but will be accepted if the other ends initiates to us with IKEv2; <code>never</code> or <code>no</code> signifying no IKEv2 negotiation should be transmitted or accepted; <code>propose</code> or <code>yes</code> signifying that we permit IKEv2, and also use it as the default to initiate; <code>insist</code>, signifying we only accept and receive IKEv2 &#8211; IKEv1 negotiations will be rejected. </p>
<p> If the ikev2= setting is set to <code>permit</code> or <code>propose</code>, Libreswan will try and detect a &quot;bid down&quot; attack from IKEv2 to IKEv1. Since there is no standard for transmitting the IKEv2 capability with IKEv1, Libreswan uses a special Vendor ID &quot;CAN-IKEv2&quot;. If a fall back from IKEv2 to IKEv1 was detected, and the IKEv1 negotiation contains Vendor ID &quot;CAN-IKEv2&quot;, Libreswan will immediately attempt and IKEv2 rekey and refuse to use the IKEv1 connection. With an ikev2= setting of <code>insist</code>, no IKEv1 negotiation is allowed, and no bid down attack is possible.</dl>
<p> <code>esn</code></p>
<dl>
<dd>Whether or not to enable Extended Sequence Number (ESN) for the IPsec SA. ESN is typically used for very high-speed links (10Gbps or faster) where the standard 32 bit sequence number is exhausted too quickly, causing IPsec SA&#8217;s rekeys to happen too often. Accepted values are <code>no</code> (the default), <code>yes</code> and <code>either</code>. If <i>either</i> is specified as an initiator, the responder will make the choice. As a responder, if <i>either</i> is received, <i>no</i> is picked.</dl>
<p> <code>narrowing</code></p>
<dl>
<dd>IKEv2 (RFC5996) Section 2.9 Traffic Selector narrowing options. Currently the accepted values are <code>no</code>, (the default) signifying no narrowing will be proposed or accepted, or <code>yes</code>, signifying IKEv2 negotiation may allow establishing an IPsec connection with narrowed down traffic selectors. This option is ignored for IKEv1. </p>
<p> There are security implications in allowing narrowing down the proposal. For one, what should be done with packets that we hoped to tunnel, but cannot. Should these be dropped or send in the clear? Second, this could cause thousands of narrowed down Child SAs to be created if the conn has a broad policy (eg 0/0 to 0/0). One possible good use case scenario is that a remote end (that you fully trust) allows you to define a 0/0 to them, while adjusting what traffic you route via them, and what traffic remains outside the tunnel. However, it is always preferred to setup the exact tunnel policy you want, as this will be much clearer to the user.</dl>
<p> <code>sareftrack</code></p>
<dl>
<dd>Set the method of tracking reply packets with SArefs when using an SAref compatible stack. Currently only the <i>mast</i> stack supports this. Acceptable values are <code>yes</code> (the default), <code>no</code> or <code>conntrack</code>. This option is ignored when SArefs are not supported. This option is passed as PLUTO_SAREF_TRACKING to the <i>updown</i> script which makes the actual decisions whether to perform any iptables/ip_conntrack manipulation. A value of yes means that an IPSEC mangle table will be created. This table will be used to match reply packets. A value of conntrack means that additionally, subsequent packets using this connection will be marked as well, reducing the lookups needed to find the proper SAref by using the ip_conntrack state. A value of no means no IPSEC mangle table is created, and SAref tracking is left to a third-party (kernel) module. In case of a third party module, the SArefs can be relayed using the <i>statsbin=</i> notification helper.</dl>
<p> <code>leftid</code></p>
<dl>
<dd>how the left participant should be identified for authentication; defaults to <code>left</code>. Can be an IP address (in any <code><a href="/docs/linux/man/3-ipsec_ttoaddr/">ipsec_ttoaddr</a></code>(3) syntax) or a fully-qualified domain name which will be resolved. If preceded by <code>@</code>, the value is used as a literal string and will not be resolved. To support opaque identifiers (usually of type ID_KEY_ID, such as used by Cisco to specify Group Name, use square brackets, eg <code>rightid=@[GroupName]</code>. The magic value <code>%fromcert</code> causes the ID to be set to a DN taken from a certificate that is loaded. Prior to 2.5.16, this was the default if a certificate was specified. The magic value <code>%none</code> sets the ID to no ID. This is included for completeness, as the ID may have been set in the default conn, and one wishes for it to default instead of being explicitly set. The magic value <code>%myid</code> stands for the current setting of <i>myid</i>. This is set in <code>config setup</code> or by <code><a href="/docs/linux/man/8-ipsec_whack/">ipsec_whack</a></code>(8)), or, if not set, it is the IP address in <code>%defaultroute</code> (if that is supported by a TXT record in its reverse domain), or otherwise it is the system&#8217;s hostname (if that is supported by a TXT record in its forward domain), or otherwise it is undefined. </p>
<p> When using certificate based ID&#8217;s, one need to specify the full RDN, optionally using wildcard matching (eg CN=&#8217;*&#8217;). If the RDN contains a comma, this can be masked using a comma (eg OU=&#8217;Foo,, Bar and associates&#8217;)</dl>
<p> <code>leftrsasigkey</code></p>
<dl>
<dd>the left participant&#8217;s public key for RSA signature authentication, in RFC 2537 format using <code><a href="/docs/linux/man/3-ipsec_ttodata/">ipsec_ttodata</a></code>(3) encoding. The magic value <code>%none</code> means the same as not specifying a value (useful to override a default). The value <code>%dnsondemand</code> (the default) means the key is to be fetched from DNS at the time it is needed. The value <code>%dnsonload</code> means the key is to be fetched from DNS at the time the connection description is read from <i>ipsec.conf</i>; currently this will be treated as <code>%none</code> if <code>right=%any</code> or <code>right=%opportunistic</code>. The value <code>%dns</code> is currently treated as <code>%dnsonload</code> but will change to <code>%dnsondemand</code> in the future. The identity used for the left participant must be a specific host, not <code>%any</code> or another magic value. The value <code>%cert</code> will load the information required from a certificate defined in <code>%leftcert</code> and automatically define leftid for you. <code>Caution:</code> if two connection descriptions specify different public keys for the same <code>leftid</code>, confusion and madness will ensue.</dl>
<p> <code>leftrsasigkey2</code></p>
<dl>
<dd>if present, a second public key. Either key can authenticate the signature, allowing for key rollover.</dl>
<p> <code>leftcert</code></p>
<dl>
<dd>If you are using <code>leftrsasigkey=%cert</code> this defines the certificate nickname of your certificate in the NSS database. This can be on software or hardware security device.</dl>
<p> <code>leftckaid</code></p>
<dl>
<dd>The hex CKAID of the X.509 certificate. Certificates are stored in the NSS database.</dl>
<p> <code>leftauth</code></p>
<dl>
<dd>How the security gateways will authenticate to the other side in the case of asymmetric authentication; acceptable values are <code>rsasig</code> for RSA digital signatures based authentication, <code>secret</code> for shared secrets (PSK) authentication and <code>null</code> for null-authentication. There is no default value &#8211; if unset, the symmetrical <code>authby=</code> keyword is used to determine the authentication policy of the connection. </p>
<p> If asymmetric authentication is requested, IKEv1 must be disabled. If symmetric authentication is required, use <code>authby=</code> instead of leftauth/rightauth. If leftauth is set, rightauth must also be set and authby= must not be set. Asymmetric authentication cannot use secret (psk) on one side and null on the other side &#8211; use psk on both ends instead. </p>
<p> Be aware that the symmetric keyword is <code>authby=</code> but the asymmetric keyword is <code>leftauth</code> and <code>rightauth</code> (without the &quot;by&quot;).</dl>
<p> <code>leftca</code></p>
<dl>
<dd>specifies the authorized Certificate Authority (CA) that signed the certificate of the peer. If undefined, it defaults to the CA that signed the certificate specified in <code>leftcert</code>. The special <code>rightca=%same</code> is implied when not specifying a <code>rightca</code> and means that only peers with certificates signed by the same CA as the leftca will be allowed. This option is only useful in complex multi CA certificate situations. When using a single CA, it can be safely omitted for both left and right.</dl>
<p> <code>leftsendcert</code></p>
<dl>
<dd>This option configures when Libreswan will send X.509 certificates to the remote host. Acceptable values are <code>yes|always</code> (signifying that we should always send a certificate), <code>sendifasked</code> (signifying that we should send a certificate if the remote end asks for it), and <code>no|never</code> (signifying that we will never send a X.509 certificate). The default for this option is <code>sendifasked</code> which may break compatibility with other vendor&#8217;s IPsec implementations, such as Cisco and SafeNet. If you find that you are getting errors about no ID/Key found, you likely need to set this to <code>always</code>. This per-conn option replaces the obsolete global <code>nocrsend</code> option.</dl>
<p> <code>leftxauthserver</code></p>
<dl>
<dd>Left is an XAUTH server. This can use PAM for authentication or md5 passwords in <i>/etc/ipsec.d/passwd</i>. These are additional credentials to verify the user identity, and should not be confused with the XAUTH <code>group secret</code>, which is just a regular PSK defined in <i>ipsec.secrets</i>. The other side of the connection should be configured as <code>rightxauthclient</code>. XAUTH connections cannot rekey, so <code>rekey=no</code> should be specified in this conn. For further details on how to compile and use XAUTH, see README.XAUTH. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>leftxauthclient</code></p>
<dl>
<dd>Left is an XAUTH client. The xauth connection will have to be started interactively and cannot be configured using <code>auto=start</code>. Instead, it has to be started from the commandline using <i>ipsec auto &#8211;up connname</i>. You will then be prompted for the username and password. To setup an XAUTH connection non-interactively, which defeats the whole purpose of XAUTH, but is regularly requested by users, it is possible to use a whack command &#8211; <i>ipsec whack &#8211;name baduser &#8211;ipsecgroup-xauth &#8211;xauthname badusername &#8211;xauthpass password &#8211;initiate</i> The other side of the connection should be configured as <code>rightxauthserver</code>. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>leftusername</code></p>
<dl>
<dd>The username associated with this connection. The username can be the IKEv2 XAUTH username, a GSSAPI username or IKEv2 CP username. For the XAUTH username, the XAUTH password can be configured in the <i>ipsec.secrets</i> file. This option was previously called leftxauthusername.</dl>
<p> <code>leftmodecfgserver</code></p>
<dl>
<dd>Left is a Mode Config server. It can push network configuration to the client. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>leftmodecfgclient</code></p>
<dl>
<dd>Left is a Mode Config client. It can receive network configuration from the server. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>xauthby</code></p>
<dl>
<dd>When IKEv1 XAUTH support is available, set the method used by XAUTH to authenticate the user with IKEv1. The currently supported values are <i>file</i> (the default), <i>pam</i> or <i>alwaysok</i>. The password file is located at <i>/etc/ipsec.d/passwd</i>, and follows a syntax similar to the Apache htpasswd file, except an additional connection name argument (and optional static IP address) are also present: </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr> <i>username:password:conname:ipaddress</i> </p>
<p> For supported password hashing methods, see <code><a href="/docs/linux/man/3-crypt/">crypt</a></code>(3). If pluto is running in FIPS mode, some hash methods, such as MD5, might not be available. Threads are used to launch an xauth authentication helper for file as well as PAM methods. </p>
<p> The <i>alwaysok</i> should only be used if the XAUTH user authentication is not really used, but is required for interoperability, as it defeats the whole point of XAUTH which is to rely on a secret only known by a human. See also <i>pam-authorize=yes</i></dl>
<p> <code>xauthfail</code></p>
<dl>
<dd>When XAUTH support is available, set the failure method desired when authentication has failed. The currently supported values are <i>hard</i> (the default) and <i>soft</i>. A soft failure means the IPsec SA is allowed to be established, as if authentication had passed successfully, but the XAUTH_FAILED environment variable will be set to 1 for the updown script, which can then be used to redirect the user into a walled garden, for example a payment portal.</dl>
<p> <code>pam-authorize</code></p>
<dl>
<dd>IKEv1 supports PAM authorization via XAUTH using <i>xauthby=pam</i>. IKEv2 does not support receiveing a plaintext username and password. Libreswan does not yet support EAP authentication methods for IKE. The pam-authorize=yes option performs an authorization call via PAM, but only includes the remote ID (not username or password). This allows for backends to disallow an ID based on non-password situations, such as &quot;user disabled&quot; or &quot;user over quota&quot;. See also <i>xauthby=pam</i></dl>
<p> <code>modecfgpull</code></p>
<dl>
<dd>Pull the Mode Config network information from the server. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>modecfgdns1</code>, <code>modecfgdns2</code>, <code>modecfgdomain</code>, <code>modecfgbanner</code></p>
<dl>
<dd>When configured as modecfg server, specifying any of these options will cause those options and values to be sent to the modecfg client during the XAUTH+ModeCFG phase (phase 1.5). </p>
<p> When we are an XAUTH client, these options will be treated as defaults. If the remote XAUTH server did not pass us one of these options, the configured defaults are used to reconfigure the local DNS setup. </p>
<p> The split tunneling directive will be sent automatically if the xauth server side has configured a network other than 0.0.0.0/0</dl>
<p> <code>remote-peer-type</code></p>
<dl>
<dd>Set the remote peer type. This can enable additional processing during the IKE negotiation. Acceptable values are <code>cisco</code> or <code>ietf</code> (the default). When set to cisco, support for Cisco IPsec gateway redirection and Cisco obtained DNS and domainname are enabled. This includes automatically updating (and restoring) /etc/resolv.conf. These options require that XAUTH is also enabled on this connection.</dl>
<p> <code>nm-configured</code></p>
<dl>
<dd>Mark this connection as controlled by Network Manager. Acceptable values are <code>yes</code> or <code>no</code> (the default). Currently, setting this to yes will cause libreswan to skip reconfiguring resolv.conf when used with XAUTH and ModeConfig.</dl>
<p> <code>encapsulation</code></p>
<dl>
<dd>In some cases, for example when ESP packets are filtered or when a broken IPsec peer does not properly recognise NAT, it can be useful to force RFC-3948 encapsulation. In other cases, where IKE is NAT&#8217;ed but ESP packets can or should flow without encapsulation, it can be useful to ignore the NAT-Traversal auto-detection. <code>encapsulation=yes</code> forces the NAT detection code to lie and tell the remote peer that RFC-3948 encapsulation (ESP in port 4500 packets) is required. <code>encapsulation=no</code> ignores the NAT detection causing ESP packets to send send without encapsulation. The default value of <code>encapsulation=auto</code> follows the regular outcome of the NAT auto-detection code performed in IKE. This option replaced the obsoleted forceencaps option.</dl>
<p> <code>nat-keepalive</code></p>
<dl>
<dd>whether to send any NAT-T keep-alives. These one byte packets are send to prevent the NAT router from closing its port when there is not enough traffic on the IPsec connection. Acceptable values are: <code>yes</code> (the default) and <code>no</code>.</dl>
<p> <code>initial-contact</code></p>
<dl>
<dd>whether to send an INITIAL_CONTACT payload to the peer we are initiating to, if we currently have no IPsec SAs up with that peer. Acceptable values are: <code>no</code> (the default) and <code>yes</code>. It is recommended to leave this option unset, unless the remote peer requires it to allow reconnects. The only known peer at this time is Cisco, which will not allow a reconnect (despite authentication) to replace an existing IPsec SA unless it receives an INITIAL_CONTACT payload. Receiving this payload is ignored and the choice to replace or add an IPsec SA when libreswan is a responder is purely based on the <code>uniqueids</code> setting, which should be left enabled unless libreswan acts as an XAUTH server using PSK (&quot;group secret&quot;). This option can cause a few seconds of downtime on the IPsec tunnel between the time the remote clears the old IPsec SA in response to our INITIAL_CONTACT message, and the time we finish setting up the new IPsec SA. If there is an XAUTH step in between, and especially when XAUTH requires the use of some two-factor token, this downtime could be even longer.</dl>
<p> <code>cisco-unity</code></p>
<dl>
<dd>whether to send a CISCO_UNITY payload to the peer. Acceptable values are: <code>no</code> (the default) and <code>yes</code>. It is recommended to leave this option unset, unless the remote peer (Cisco client or server) requires it. This option does not modify local behaviour. It can be needed to connect as a client to a Cisco server. It can also be needed to act as a server for a Cisco client, which otherwise might send back an error DEL_REASON_NON_UNITY_PEER.</dl>
<p> <code>fake-strongswan</code></p>
<dl>
<dd>whether to send a STRONGSWAN Vendor ID payload to the peer. Acceptable values are: <code>no</code> (the default) and <code>yes</code>. Strongswan rejects certain proposals with private use numbers such as esp=twofish or esp=serpent unless it receives a strongswan vendorid by the peer. This option sends such an (unversioned) vendor id.</dl>
<p> <code>send-vendorid</code></p>
<dl>
<dd>whether to send our Vendor ID during IKE. Acceptable values are: <code>no</code> (the default) and <code>yes</code>. The vendor id sent can be configured using the &quot;config setup&quot; option <code>myvendorid=</code>. It defaults to OE-Libreswan-VERSION. </p>
<p> Vendor ID&#8217;s can be useful in tracking interoperability problems. However, specific vendor identification and software versions can be useful to an attacker when there are known vulnerabilities to a specific vendor/version. </p>
<p> The prefix OE stands for &quot;Opportunistic Encryption&quot;. This prefix was historically used by The FreeS/WAN Project and The Openswan Project (openswan up to version 2.6.38) and in one Xeleranized openswan versions (2.6.39). Further Xeleranized openswan&#8217;s use the prefix OSW.</dl>
<p> <code>overlapip</code></p>
<dl>
<dd>a boolean (yes/no) that determines, when *subnet=vhost: is used, if the virtual IP claimed by this states created from this connection can with states created from other connections. </p>
<p> Note that connection instances created by the Opportunistic Encryption or PKIX (x.509) instantiation system are distinct internally. They will inherit this policy bit. </p>
<p> The default is no. </p>
<p> This feature is only available with kernel drivers that support SAs to overlapping conns. At present only the (klips) mast protocol stack supports this feature.</dl>
<p> <code>reqid</code></p>
<dl>
<dd>a unique identifier used to match IPsec SAs using iptables with NETKEY/XFRM. This identifier is normally automatically allocated in groups of 4. It is exported to the _updown script as REQID. On Linux, reqids are supported with IP Connection Tracking and NAT (iptables). Automatically generated values use the range 16380 and higher. Manually specified reqid values therefor must be between 1 and 16379. </p>
<p> Automatically generated reqids use a range of 0-3 (eg 16380-16383 for the first reqid). These are used depending on the exact policy (AH, AH+ESP, IPCOMP, etc). </p>
<p> WARNING: Manually assigned reqids are all identical. Instantiations of connections (those using %any wildcards) will all use the same reqid. If you use manual assigning you should make sure your connections only match single road warrior only or you break multiple road warriors behind same NAT router because this feature requires unique reqids to work. </p>
<p> For KLIPS, when using the MAST variant, a different mechanism called SAref is in use. See overlapip and sareftrack.</dl>
<p> <code>dpddelay</code></p>
<dl>
<dd>Set the delay (in time units, defaults to seconds) between Dead Peer Detection (IKEv1 RFC 3706) or IKEv2 Liveness keepalives that are sent for this connection (default 30 seconds). If dpddelay is set, dpdtimeout also needs to be set.</dl>
<p> <code>dpdtimeout</code></p>
<dl>
<dd>Set the length of time (in time units, defaults to seconds) that we will idle without hearing back from our peer. After this period has elapsed with no response and no traffic, we will declare the peer dead, and remove the SA (default 120 seconds). If dpdtimeout is set, dpdaction also needs to be set.</dl>
<p> <code>dpdaction</code></p>
<dl>
<dd>When a DPD enabled peer is declared dead, what action should be taken. <code>hold</code> (default) means the eroute will be put into %hold status, while <code>clear</code> means the eroute and SA with both be cleared. <code>restart</code> means that <i>ALL</i> SAs to the dead peer will renegotiated. </p>
<p> <i>dpdaction=clear</i> is really only useful on the server of a Road Warrior config. </p>
<p> The value <code>restart_by_peer</code> has been obsoleted and its functionality moved into the regular restart action.</dl>
<p> <code>pfs</code></p>
<dl>
<dd>whether Perfect Forward Secrecy of keys is desired on the connection&#8217;s keying channel (with PFS, penetration of the key-exchange protocol does not compromise keys negotiated earlier); Since there is no reason to ever refuse PFS, Libreswan will allow a connection defined with <code>pfs=no</code> to use PFS anyway. Acceptable values are <code>yes</code> (the default) and <code>no</code>.</dl>
<p> <code>pfsgroup</code></p>
<dl>
<dd>This option is obsoleted, please use phase2alg if you need the PFS to be different from phase1 (the default) using: phase2alg=aes128-md5;modp1024</dl>
<p> <code>aggrmode</code></p>
<dl>
<dd>Use IKEv1 Aggressive Mode instead of IKEv1 Main Mode. This option has no effect when IKEv2 is used. Acceptable values are <code>no</code> (the default) or <code>yes</code>. When this option is enabled, IKEv1 Main Mode will no longer be allowed for this connection. </p>
<p> Aggressive Mode is less secure, and more vulnerable to Denial Of Service attacks. It is also vulnerable to brute force attacks with software such as <code>ikecrack</code>. It should not be used, and it should especially not be used with XAUTH and group secrets (PSK). If the remote system administrator insists on staying irresponsible, enable this option. </p>
<p> Aggressive Mode is further limited to only proposals with one DH group as there is no room to negotiate the DH group. Therefor it is mandatory for Aggressive Mode connections that both <code>ike=</code> and <code>phase2alg=</code> options are specified with only one fully specified proposal using one DH group. </p>
<p> The KE payload is created in the first exchange packet when using aggressive mode. The KE payload depends on the DH group used. This is why there cannot be multiple DH groups in IKEv1 aggressive mode. In IKEv2, which uses a similar method to IKEv1 Aggressive Mode, there is an INVALID_KE response payload that can inform the initiator of the responder&#8217;s desired DH group and so an IKEv2 connection can actually recover from picking the wrong DH group by restarting its negotiation.</dl>
<p> <code>salifetime</code></p>
<dl>
<dd>how long a particular instance of a connection (a set of encryption/authentication keys for user packets) should last, from successful negotiation to expiry; acceptable values are an integer optionally followed by <code>s</code> (a time in seconds) or a decimal number followed by <code>m</code>, <code>h</code>, or <code>d</code> (a time in minutes, hours, or days respectively) (default <code>8h</code>, maximum <code>24h</code>). Normally, the connection is renegotiated (via the keying channel) before it expires. The two ends need not exactly agree on <code>salifetime</code>, although if they do not, there will be some clutter of superseded connections on the end which thinks the lifetime is longer. </p>
<p> The keywords &quot;keylife&quot; and &quot;lifetime&quot; are obsoleted aliases for &quot;salifetime.&quot; Change your configs to use &quot;salifetime&quot; instead.</dl>
<p> <code>replay-window</code></p>
<dl>
<dd>The size of the IPsec SA replay window protection. The default is kernel stack specific, but usually 32. Linux NETKEY/XFRM allows at least up to 2048. A value of of 0 disables replay protection. Disabling of replay protection is sometimes used on a pair of IPsec servers in a High Availability setup, or on servers with very unpredictable latency, such as mobile networks, which can cause an excessive amount of out of order packets. Sequence errors can be seen in /proc/net/xfrm_stat. Note that technically, at least the Linux kernel can install IPsec SA&#8217;s with an IPsec SA Sequence Number, but this is currently not supported by libreswan.</dl>
<p> <code>rekey</code></p>
<dl>
<dd>whether a connection should be renegotiated when it is about to expire; acceptable values are <code>yes</code> (the default) and <code>no</code>. The two ends need not agree, but while a value of <code>no</code> prevents Pluto from requesting renegotiation, it does not prevent responding to renegotiation requested from the other end, so <code>no</code> will be largely ineffective unless both ends agree on it.</dl>
<p> <code>rekeymargin</code></p>
<dl>
<dd>how long before connection expiry or keying-channel expiry should attempts to negotiate a replacement begin; acceptable values as for <code>salifetime</code> (default <code>9m</code>). Relevant only locally, other end need not agree on it.</dl>
<p> <code>rekeyfuzz</code></p>
<dl>
<dd>maximum percentage by which <code>rekeymargin</code> should be randomly increased to randomize rekeying intervals (important for hosts with many connections); acceptable values are an integer, which may exceed 100, followed by a `%&#8217; (default set by <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8), currently <code>100%</code>). The value of <code>rekeymargin</code>, after this random increase, must not exceed <code>salifetime</code>. The value <code>0%</code> will suppress time randomization. Relevant only locally, other end need not agree on it.</dl>
<p> <code>keyingtries</code></p>
<dl>
<dd>how many attempts (a whole number or <code>%forever</code>) should be made to negotiate a connection, or a replacement for one, before giving up (default <code>%forever</code>). The value <code>%forever</code> means &#8220;never give up&#8221; (obsolete: this can be written 0). Relevant only locally, other end need not agree on it.</dl>
<p> <code>ikelifetime</code></p>
<dl>
<dd>how long the keying channel of a connection (buzzphrase: &#8220;ISAKMP SA&#8221;) should last before being renegotiated; acceptable values as for <code>salifetime</code> (default set by <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8), currently <code>1h</code>, maximum <code>24h</code>). The two-ends-disagree case is similar to that of <code>salifetime</code>.</dl>
<p> <code>retransmit-timeout</code></p>
<dl>
<dd>how long a single packet, including retransmits of that packet, may take before the IKE attempt is aborted. If rekeying is enabled, a new IKE attempt is started. The default set by <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8), currently is <code>60s</code>. See also: <i>retransmit-interval</i>, <i>rekey</i> and <i>keyingtries</i>.</dl>
<p> <code>retransmit-interval</code></p>
<dl>
<dd>the initial interval time period, specified in msecs, that pluto waits before retransmitting an IKE packet. This interval is doubled for each attempt (exponential back-off). The default set by <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8), currently is <code>500</code>. See also: <i>retransmit-timeout</i>, <i>rekey</i> and <i>keyingtries</i>.</dl>
<p> <code>compress</code></p>
<dl>
<dd>whether IPComp compression of content is proposed on the connection (link-level compression does not work on encrypted data, so to be effective, compression must be done <i>before</i> encryption); acceptable values are <code>yes</code> and <code>no</code> (the default). </p>
<p> As of libreswan 3.1, both ends <code>must</code> agree. In previous versions of libreswan, openswan and freeswan, compression was always accepted even if not configured. In light of the BEAST attacks on TLS, using compression and encryptions has come under more scrutiny, and it was decided that it should be possible for the local policy of an endpoint to disallow compression. A value of <code>yes</code> causes pluto to propose compression and reject proposals without it. A value of <code>no</code> prevents pluto from proposing compression; a proposal to compress will be <code>rejected</code>.</dl>
<p> <code>metric</code></p>
<dl>
<dd>Set the metric for the routes to the ipsecX or mastX interface. This makes it possible to do host failover from another interface to ipsec using route management. This value is passed to the _updown scripts as PLUTO_METRIC. This option is only available with KLIPS or MAST on Linux. Acceptable values are positive numbers, with the default being <code>1</code>.</dl>
<p> <code>mtu</code></p>
<dl>
<dd>Set the MTU for the route(s) to the remote endpoint and/or subnets. This is sometimes required when the overhead of the IPsec encapsulation would cause the packet the become too big for a router on the path. Since IPsec cannot trust any unauthenticated ICMP messages, PATH MTU discovery does not work. This can also be needed when using &quot;6to4&quot; IPV6 deployments, which adds another header on the packet size. Acceptable values are positive numbers. There is no default.</dl>
<p> <code>tfc</code></p>
<dl>
<dd>Enable Traffic Flow Confidentiality (&quot;TFC&quot;) (RFC-4303) for outgoing ESP packets in Tunnel Mode. When enabled, ESP packets are padded to the specified size (up to the PMTU size) to prevent leaking information based on ESP packet size. This option is ignored for AH and for ESP in Transport Mode as those always leak traffic characteristics and applying TFC will not do anything. Acceptable values are positive numbers. The value 0 means TFC padding is not performed. Currently this feature is only implemented for the Linux XFRM/NETKEY stack. In IKEv2, when the notify payload ESP_TFC_PADDING_NOT_SUPPORTED is received, TFC padding is disabled. The default is not to do any TFC padding, but this might change in the near future.</dl>
<p> <code>send-no-esp-tfc</code></p>
<dl>
<dd>Whether or not to tell the remote peer that we do not support Traffic Flow Confidentiality (&quot;TFC&quot;) (RFC-4303). Possible values are <code>no</code> (the default) which allows the peer to use TFC or <code>yes</code> which prevents to peer from using TFC. This does not affect whether this endpoint uses TFC, which only depends on the local <code>tfc</code> setting. This option is only valid for IKEv2.</dl>
<p> <code>nflog</code></p>
<dl>
<dd>If set, the NFLOG group number to log <code>this connection&#8217;s</code> pre-crypt and post-decrypt traffic to. The default value of <code>0</code> means no logging at all. This option is only available on linux kernel 2.6.14 and later. It allows common network utilities such as tcpdump, wireshark and dumpcap, to use nflog:XXX pseudo interfaces where XXX is the nflog group number. During the updown phase of a connection, iptables will be used to add and remove the source/destination pair to the nflog group specified. The rules are setup with the nflog-prefix matching the connection name. See also the global <code>nflog-all</code> option.</dl>
<p> <code>mark</code></p>
<dl>
<dd>If set, the MARK to set for the IPsec SA of this connection. The format of a CONNMARK is <code>mark/mask</code>. If the mask is left out, a default mask of 0xffffffff is used. A mark value of -1 means to assign a new global unique mark number for each instance of the connection. Global marks start at 1001. This option is only available on linux NETKEY/XFRM kernels. It can be used with iptables to create custom iptables rules using CONNMARK. It can also be used with Virtual Tunnel Interfaces (&quot;VTI&quot;) to direct marked traffic to specific vtiXX devices.</dl>
<p> <code>mark-in</code></p>
<dl>
<dd>The same as <code>mark</code>, but mark-in only applies to the inbound half of the IPsec SA. It overrides any mark= setting.</dl>
<p> <code>mark-out</code></p>
<dl>
<dd>The same as <code>mark</code>, but mark-out only applies to the outbound half of the IPsec SA. It overrides any mark= setting.</dl>
<p> <code>vti-interface</code></p>
<dl>
<dd>This option is used to create &quot;Routing based VPNs&quot; (as opposed to &quot;Policy based VPNs&quot;). It will create a new interface that can be used to route traffic in for encryption/decryption. The Virtual Tunnel Interface (&quot;VTI&quot;) interface name is used to for all IPsec SA&#8217;s created by this connection. This requires that the connection also enables either the <code>mark=</code> or <code>mark-in= / mark-out-</code> option(s). All traffic marked with the proper MARKs will be automatically encrypted if there is an IPsec SA policy covering the source/destination traffic. Tools such as tcpdump and iptables can be used on all cleartext pre-encrypt and post-decrypt traffic on the device. See the libreswan wiki for example configurations that use VTI. </p>
<p> VTI interfaces are currently only supported on Linux with XFRM/NETKEY. The _updown script handles certain Linux specific interfaces settings required for proper functioning (disable_policy, rp_filter, forwarding, etc). Interface names are limited to 16 characters and may not allow all characters to be used. If marking and <i>vti-routing=yes</i> is used, no manual iptables should be required. However, administrators can use the iptables mangle table to mark traffic manually if desired.</dl>
<p> <code>vti-routing</code></p>
<dl>
<dd>Whether or not to add network rules or routes for IPsec SA&#8217;s to the respective VTI devices. Valid values are <code>yes</code> (the default) or <code>no</code>. When using &quot;routing based VPNs&quot; with a subnets policy of 0.0.0.0/0, this setting needs to set to <i>no</i> to prevent imploding the tunnel, and the administrator is expected to manually add ip rules and ip routes to configure what traffic must be encrypted. When set to <i>yes</i>, the _updown script will automatically route the leftsubnet/rightsubnet traffic into the VTI device specified with <i>vti-interface</i></dl>
<p> <code>vti-shared</code></p>
<dl>
<dd>Whether or not the VTI device is shared amongst connections. Valid values are <code>no</code> (the default) or <code>yes</code>. When set to no, the VTI device is automatically deleted if the connection is a single non-instantiated connection. If a connection instantiates (eg right=%any) then this option has no effect, as the VTI device is not removed as it is shared with multiple roadwarriors.</dl>
<p> <code>priority</code></p>
<dl>
<dd>The priority in the kernel SPD/SAD database, when matching up packets. Each kernel (NETKEY, KLIPS, OSX, etc) has its own mechanism for setting the priority. Setting this option to non-zero passes the priority to the kernel stack unmodified. The maximum value depends on the stack. It is recommended not to exceed 65536 </p>
<p> KLIPS and NETKEY use a priority system based on &quot;most specific match first&quot;. It uses an internal algorithm to calculate these based on network prefix length, protocol and port selectors. A lower value means a higher priority. </p>
<p> Typical values are about the 2000 range. These can be seen on the NETKEY stack using <code>ip xfrm policy</code> when the connection is up. For &quot;anonymous IPsec&quot; or Opportunistic Encryption based connections, a much lower priority (65535) is used to ensure administrator configured IPsec always takes precedence over opportunistic IPsec.</dl>
<p> <code>sendca</code></p>
<dl>
<dd>How much of our available X.509 trust chain to send with the End certificate, excluding any root CA&#8217;s. Specifying <code>issuer</code> sends just the issuing intermediate CA, while <code> all</code> will send the entire chain of intermediate CA&#8217;s.<code>none</code> (the default) will not send any CA certs.</dl>
<p> <code>disablearrivalcheck</code></p>
<dl>
<dd>whether KLIPS&#8217;s normal tunnel-exit check (that a packet emerging from a tunnel has plausible addresses in its header) should be disabled; acceptable values are <code>yes</code> and <code>no</code> (the default). Tunnel-exit checks improve security and do not break any normal configuration. Relevant only locally, other end need not agree on it.</dl>
<p> <code>labeled-ipsec</code></p>
<dl>
<dd>Whether labeled IPsec should be enabled or not; acceptable values are <code>no</code> (the default) and <code>yes</code>. See also policy-label= and secctx-attr-type=</dl>
<p> <code>policy-label</code></p>
<dl>
<dd>The string representation of an access control security label that is interpreted by the LSM (e.g. SELinux) for use with Labeled IPsec. See also loopback=, labeled-ipsec= and secctx-attr-type=. For example, <i>policy-label=system_u:object_r:ipsec_spd_t:s0-s15:c0.c1023</i></dl>
<p> <code>failureshunt</code></p>
<dl>
<dd>what to do with packets when negotiation fails. The default is <code>none</code>: no shunt; <code>passthrough</code>, <code>drop</code>, and <code>reject</code> have the obvious meanings.</dl>
<p> <code>negotiationshunt</code></p>
<dl>
<dd>What to do with packets during the IKE negotiation. Valid options are <code>hold</code> (the default) or <code>passthrough</code>. This should almost always be left to the default hold value to avoid cleartext packet leaking. The only reason to set this to passthrough is if plaintext service availability is more important than service security or privacy, a scenario that also implies failureshunt=passthrough and most likely authby=%null using Opportunistic Encryption.</dl>
<h2>Config Sections</h2>
<p>At present, the only <code>config</code> section known to the IPsec software is the one named <code>setup</code>, which contains information used when the software is being started (see <code><a href="/docs/linux/man/8-ipsec_setup/">ipsec_setup</a></code>(8)). Here&#8217;s an example: </p>
<dl>
<dd>
<pre><code>config setup
 interfaces=&quot;ipsec0=eth1 ipsec1=ppp0&quot;
 klipsdebug=none
 plutodebug=control
 protostack=auto</code></pre>
</dl>
<p> Parameters are optional unless marked &#8220;(required)&#8221;. </p>
<p> The currently-accepted <i>parameter</i> names in a <code>config setup</code> section are: </p>
<p> <code>myid</code></p>
<dl>
<dd>the identity to be used for <code>%myid</code>. <code>%myid</code> is used in the implicit policy group conns and can be used as an identity in explicit conns. If unspecified, <code>%myid</code> is set to the IP address in <code>%defaultroute</code> (if that is supported by a TXT record in its reverse domain), or otherwise the system&#8217;s hostname (if that is supported by a TXT record in its forward domain), or otherwise it is undefined. An explicit value generally starts with &#8220;<code>@</code>&#8221;.</dl>
<p> <code>protostack</code></p>
<dl>
<dd>decide which protocol stack is going to be used. Valid values are &quot;klips&quot;, &quot;netkey&quot; (the default) and &quot;mast&quot;. The &quot;mast&quot; stack is a variation for the KLIPS stack. The value &quot;auto&quot; has been obsoleted.</dl>
<p> <code>interfaces</code></p>
<dl>
<dd>virtual and physical interfaces for IPsec to use: a single <i>virtual</i><code>=</code><i>physical</i> pair, a (quoted!) list of pairs separated by white space, or <code>%none</code>. One of the pairs may be written as <code>%defaultroute</code>, which means: find the interface <i>d</i> that the default route points to, and then act as if the value was &#8220;<code>ipsec0=</code><i>d</i>&#8221;. <code>%defaultroute</code> is the default; <code>%none</code> must be used to denote no interfaces, or when using the NETKEY stack. If <code>%defaultroute</code> is used (implicitly or explicitly) information about the default route and its interface is noted for use by <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8).)</dl>
<p> <code>listen</code></p>
<dl>
<dd>IP address to listen on (default depends on <code>interfaces=</code> setting). Currently only accepts one IP address.</dl>
<p> <code>ikeport</code></p>
<dl>
<dd>The IKE port to listen on. The default value is <code>500</code>. As IKE is an internet standard, changing this means pluto will no longer be able to interop with other devices, unless they have also been explicitly configured to use a non-standard IKE port. There might also be other subtle assumptions within the kernel that port 500 is used. Changing this port is strongly discouraged, and should probably only be done for testing or when required to circumvent VPN blocking technologies as employed by certain commercial companies and national governments. See also <code>nat-ikeport</code>.</dl>
<p> <code>nflog-all</code></p>
<dl>
<dd>If set, the NFLOG group number to log <code>all</code> pre-crypt and post-decrypt traffic to. The default value of <code>0</code> means no logging at all. This option is only available on linux kernel 2.6.14 and later. It allows common network utilities such as tcpdump, wireshark and dumpcap, to use nflog:XXX pseudo interfaces where XXX is the nflog group number. During startup and shutdown of the IPsec service, iptables commands will be used to add or remove the global NFLOG table rules. The rules are setup with the nflog-prefix <i>all-ipsec</i>. See also the per-connection <code>nflog</code> option.</dl>
<p> <code>nat_traversal</code></p>
<dl>
<dd>OBSOLETE. Support for NAT Traversal is always enabled.</dl>
<p> <code>disable_port_floating</code></p>
<dl>
<dd>OBSOLETE</dl>
<p> <code>force_keepalive</code></p>
<dl>
<dd>This option has been obsoleted since libreswan version 3.2. See the <i>nat-keepalive</i> option.</dl>
<p> <code>nat-ikeport</code></p>
<dl>
<dd>The IKE NAT Traversal floating port (see RFC-3947) to listen on. The default value is <code>4500</code>. As IKE/NATT is an internet standard, changing this means pluto will no longer be able to interoperate with other devices, unless they have also been explicitly configured to use a non-standard IKE/NATT port. There might also be other subtle assumptions within the kernel that port 4500 is used. Changing this port is strongly discouraged, and should probably only be done for testing or when required to circumvent VPN blocking technologies as employed by certain commercial companies and national governments. See also <code>ikeport</code>.</dl>
<p> <code>keep-alive</code></p>
<dl>
<dd>The delay (in seconds) for NAT-T keep-alive packets, if these are enabled using <code>nat-keepalive</code> This parameter may eventually become per-connection.</dl>
<p> <code>virtual-private</code></p>
<dl>
<dd>contains the networks that are allowed as subnet= for the remote clients when using the <code>vhost:</code> or <code>vnet:</code> keywords in the <code>subnet=</code> parameters. In other words, the address ranges that may live behind a NAT router through which a client connects. This value is usually set to all the RFC-1918 address space, excluding the space used in the local subnet behind the NAT (An IP address cannot live at two places at once). IPv4 address ranges are denoted as <i>%v4:a.b.c.d/mm</i> and IPv6 is denoted as <i>%v6:aaaa::bbbb:cccc:dddd:eeee/mm</i>. One can exclude subnets by using the <code>!</code>. For example, if the VPN server is giving access to 192.168.1.0/24, this option should be set to: <i>virtual-private=%v4:10.0.0.0/8,%v4:192.168.0.0/16,%v4:172.16.0.0/12,%v4:!192.168.1.0/24</i>. This parameter is only needed on the server side and not on the client side that resides behind the NAT router, as the client will just use its IP address for the inner IP setting. This parameter may eventually become per-connection. See also <code>leftsubnet=</code> </p>
<p> Note: It seems that T-Mobile in the US and Rogers/Fido in Canada have started using 25.0.0.0/8 as their pre-NAT range. This range technically belongs to the Defence Interoperable Network Services Authority (DINSA), an agency of the Ministry of Defence of the United Kingdom. The network range seems to not have been announced for decades, which is probably why these organisations &quot;borrowed&quot; this range. To support roadwarriors on these 3G networks, you might have to add it to the virtual-private= line.</dl>
<p> <code>myvendorid</code></p>
<dl>
<dd>The string to use as our vendor id (VID) when send-vendorid=yes. The default is OE-Libreswan-VERSION.</dl>
<p> <code>oe</code></p>
<dl>
<dd>This option is ignored for now. It used to determine if Opportunistic Encryption will be enabled. Opportunistic Encryption is the term to describe using IPsec tunnels without prearrangement. It uses IPSECKEY or TXT records to announce public RSA keys for certain IP&#8217;s or identities. However, this feature is going to be moved outside of the pluto IKE daemon into a separate process, more closely tied with a local DNS(SEC) server. The default value used to be <code>no</code>, so this should not affect anyone. Contact the developers if you are interested in working on the re-implementation of OE.</dl>
<p> <code>nhelpers</code></p>
<dl>
<dd>how many <i>pluto helpers</i> are started to help with cryptographic operations. Pluto will start <i>(n-1)</i> of them, where <i>n</i> is the number of CPU&#8217;s you have (including hypherthreaded CPU&#8217;s). A value of 0 forces pluto to do all operations in the main process. A value of -1 tells pluto to perform the above calculation. Any other value forces the number to that amount.</dl>
<p> <code>seedbits</code></p>
<dl>
<dd>Pluto uses the NSS crypto library as its random source. Some government Three Letter Agencies require that pluto reads additional bits from /dev/random and feed these into the NSS RNG before drawing random from the NSS library, despite the NSS library itself already seeding its internal state. This process can block pluto for an extended time during startup, depending on the entropy of the system. Therefor, the default is to not perform this redundant seeding. If specifying a value, it is recommended to specify at least 460 bits (for FIPS) or 440 bits (for BSI).</dl>
<p> <code>secctx-attr-type</code></p>
<dl>
<dd>The value for the IPsec SA security context attribute identifier which is used for Labeled IPsec. Defaults to the private use IANA value 32001 from the IPsec SA attributes registry. Old openswan versions might still be using the (stolen) value 10, which has since been assigned by IANA for something else. Other values are not recommended unless IANA assigns an actual value for this. See also labeled-ipsec=, loopback= and policy-label=</dl>
<p> <code>plutofork</code></p>
<dl>
<dd>This option has been obsoleted. The pluto daemon always forks unless it is started with the &#8211;nofork option.</dl>
<p> <code>crlcheckinterval</code></p>
<dl>
<dd>interval expressed in second units, for example crlcheckinterval=8h for 8 hours, after which pluto will fetch new Certificate Revocation List (CRL) from crl distribution points. List of used CRL distribution points are collected from CA certificates and end certificates. Loaded X.509 CRL&#8217;s are verified to be valid and updates are imported to NSS database. If set to <code>0</code>, which is also the default value if this option is not specified, CRL updating is disabled.</dl>
<p> <code>crl-strict</code></p>
<dl>
<dd>if not set, pluto is tolerant about missing or expired X.509 Certificate Revocation Lists (CRL&#8217;s), and will allow peer certificates as long as they do not appear on an expired CRL. When this option is enabled, all connections with an expired or missing CRL will be denied. Active connections will be terminated at rekey time. This setup is more secure, but vulnerable to downtime if the CRL expires. Acceptable values are <code>yes</code> or <code>no</code> (the default). This option used to be called strictcrlpolicy.</dl>
<p> <code>curl-iface</code></p>
<dl>
<dd>The name of the interface that is used for CURL lookups. This is needed on rare situations where the interface needs to be forced to be different from the default interface used based on the routing table.</dl>
<p> <code>curl-timeout</code></p>
<dl>
<dd>The timeout for the curl library calls used to fetch CRL and OCSP requests. The default is 5s.</dl>
<p> <code>ocsp-enable</code></p>
<dl>
<dd>Whether to perform Online Certificate Store Protocol (&quot;OCSP&quot;) checks on those certificates that have an OCSP URI defined. Acceptable values are <code>yes</code> or <code>no</code> (the default).</dl>
<p> <code>ocsp-strict</code></p>
<dl>
<dd>if set to no, pluto is tolerant about failing to obtain an OCSP responses and a certificate is not rejected when the OCSP request fails, only when the OCSP request succeeds and lists the certificate as revoked. If set to yes, any failure on obtaining an OCSP status for a certificate will be fatal and the certificate will be rejected. Acceptable values are <code>yes</code> or <code>no</code> (the default). </p>
<p> The strict mode refers to the NSS ocspMode_FailureIsVerificationFailure mode, while non-strict mode refers to the NSS ocspMode_FailureIsNotAVerificationFailure mode.</dl>
<p> <code>ocsp-method</code></p>
<dl>
<dd>The HTTP methods used for fetching OCSP data. Valid options are <code>get</code> (the default) and <code>post</code>. Note that this behaviour depends on the NSS crypto library that is actually performing the fetching. When set to the get method, post is attempted only as fallback in case of failure. When set to post, only the post method is ever used.</dl>
<p> <code>ocsp-timeout</code></p>
<dl>
<dd>The time until an OCSP request is aborted and considered failed. The default value is 2 seconds.</dl>
<p> <code>ocsp-uri</code></p>
<dl>
<dd>The URI to use for OCSP requests instead of the default OCSP URI listed in the CA certificate. This requires the ocsp-trustname option to be set to the nick (friendly name) of the OCSP server certificate, which needs to be present in the NSS database. These option combined with the next option sets the OCSP <i>default responder</i>.</dl>
<p> <code>ocsp-trustname</code></p>
<dl>
<dd>The nickname of the certificate that has been imported into the NSS database of the server handling the OCSP requests. This requires the ocsp-uri option to be set as well. This option and the previous options sets the OCSP <i>default responder</i>.</dl>
<p> <code>ocsp-cache-size</code></p>
<dl>
<dd>The maximum size (in number of certificates) of OCSP responses that will be kept in the cache. The default is 1000. Setting this value to 0 means the cache is disabled.</dl>
<p> <code>ocsp-cache-min-age</code></p>
<dl>
<dd>The minimum age (in seconds) before a new fetch will be attempted. The default is 1 hour.</dl>
<p> <code>ocsp-cache-max-age</code></p>
<dl>
<dd>The maximum age (in seconds) before a new fetch will be attempted. The default is 1 day.</dl>
<p> <code>forwardcontrol</code></p>
<dl>
<dd>This option is obsolete and ignored. Please use <code>net.ipv4.ip_forward&nbsp;<wbr>=&nbsp;<wbr>0</code> in /etc/sysctl.conf instead to control the ip forwarding behaviour.</dl>
<p> <code>rp_filter</code></p>
<dl>
<dd>This option is obsolete and ignored. Please use the <code>net.ipv4.conf/[iface]/rp_filter&nbsp;<wbr>=&nbsp;<wbr>0</code> options in /etc/sysctl.conf instead. This option is badly documented; it must be 0 in many cases for ipsec to function.</dl>
<p> <code>syslog</code></p>
<dl>
<dd>the <code><a href="/docs/linux/man/2-syslog/">syslog</a></code>(2) &#8220;facility&#8221; name and priority to use for startup/shutdown log messages, default <code>daemon.error</code>.</dl>
<p> <code>klipsdebug</code></p>
<dl>
<dd>how much KLIPS debugging output should be logged. An empty value, or the magic value <code>none</code>, means no debugging output (the default). The magic value <code>all</code> means full output. Otherwise only the specified types of output (a quoted list, names separated by white space) are enabled; for details on available debugging types, see <code><a href="/docs/linux/man/8-ipsec_klipsdebug/">ipsec_klipsdebug</a></code>(8). This KLIPS option has no effect on NETKEY, Windows or BSD stacks.</dl>
<p> <code>plutodebug</code></p>
<dl>
<dd>how much Pluto debugging output should be logged. An empty value, or the magic value <code>none</code>, means no debugging output (the default). The magic value <code>all</code> means full output. Otherwise only the specified types of output (a quoted list, names without the <code>&#8211;debug-</code> prefix, separated by white space) are enabled; for details on available debugging types, see <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8).</dl>
<p> <code>uniqueids</code></p>
<dl>
<dd>Whether IDs should be considered identifying remote parties uniquely. Acceptable values are <code>yes</code> (the default) and <code>no</code>. Participant IDs normally are unique, so a new connection instance using the same remote ID is almost invariably intended to replace an old existing connection. </p>
<p> When the connection is defined to be a server (using xauthserver=) and the connection policy is authby=secret, this option is ignored (as of 3.20) and old connections will never be replaced. This situation is commonly known as clients using a &quot;Group ID&quot;. </p>
<p> This option may disappear in the near future. People using identical X.509 certificates on multiple devices are urged to upgrade to use seperate certificates per client and device.</dl>
<p> <code>plutorestartoncrash</code></p>
<dl>
<dd>prevent pluto from restarting after it crashed. This option should only be used by developers when debugging a crasher. It will prevent overwriting a core file on a new start, or a cascade of core files. This option is also required if used with plutostderrlog= to avoid clearing the logs of the crasher. Values can be yes (the default) or no. </p>
<p> This option is ignored on modern init systems such as <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1) and upstart. For systemd, change the <i>ipsec.service</i> file to contain <i>Restart=no</i>. See <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5)</dl>
<p> <code>logfile</code></p>
<dl>
<dd>do not use syslog, but rather log to stderr, and direct stderr to the argument file. This option used to be called plutostderrlog=</dl>
<p> <code>logappend</code></p>
<dl>
<dd>If pluto is instructed to log to a file using <code>logfile=</code>, this option determines whether the log file should be appended to or overwritten. Valid options are <code>yes</code> (the default) to append and <code>no</code> to overwrite. Since on modern systems, pluto is restarted by other daemons, such as systemd, this option should be left at its default yes value to preserve the log entries of previous runs of pluto. The option is mainly of use for running the test suite, which needs to create new log files from scratch.</dl>
<p> <code>logtime</code></p>
<dl>
<dd>When pluto is directed to log to a file using <code>logfile=</code>, this option determines whether or not to log the current timestamp as prefix. Values are <code>yes</code> (the default) or <code>no</code>. The no value can be used to create logs without ephemeral timestamps, such as those created when running the test suite. This option used to be called plutostderrlogtime=</dl>
<p> <code>force-busy</code></p>
<dl>
<dd>This option has been obsoleted, please see <i>ddos-mode</i>.</dl>
<p> <code>ddos-mode</code></p>
<dl>
<dd>The startup mode of the DDOS defense mechanism. Acceptable values are <code>busy</code>, <code>unlimited</code> or <code>auto</code> (the default). This option can also be given to the IKE daemon while running, for example by issuing <i>ipsec whack &#8211;ddos&#8211;busy</i>. When in busy mode, pluto activates anti-DDoS counter measures. Currently, counter measures consist of requiring IKEv2 anti-DDoS cookies on new incoming IKE requests, and a more aggressive cleanup of partially established or AUTH_NULL connections.</dl>
<p> <code>ddos-ike-threshold</code></p>
<dl>
<dd>The number of half-open IKE SAs before the pluto IKE daemon will be placed in busy mode. When in busy mode, pluto activates anti-DDoS counter measures. The default is 25000. See also <code>ddos-mode</code> and <i>ipsec whack &#8211;ddos-XXX</i>.</dl>
<p> <code>max-halfopen-ike</code></p>
<dl>
<dd>The number of half-open IKE SAs before the IKE daemon starts refusing all new IKE attempts. Established IKE peers are not affected. The default value is 50000.</dl>
<p> <code>shuntlifetime</code></p>
<dl>
<dd>The time until bare shunts (kernel policies not associated with connections) are deleted from the kernel. The default value is 15m. When using Opportunistic Encryption to a specific host fails, the system will either install a %pass or %hold shunt to let the traffic out clear text or block it. During the the shuntlifetime, no new Opportunistic Encryption attempt will be started, although the system will still respond to incoming OE requests from the remote IP. See also <code>failureshunt</code> and <code>negotiationshunt</code></dl>
<p> <code>xfrmlifetime</code></p>
<dl>
<dd>The time in seconds until the NETKEY/XFRM acquire state times out. The default value is 300 seconds. For auto=ondemand connections and Opportunistic connections an IPsec policy is installed in the kernel. If an incoming or outgoing packet matches this policy, a state is created in the kernel and the kernel sends an ACQUIRE message to the IKE daemon pluto. While this state is in place, no new acquires will come in for this connection. The default should be fine for most people. One use case of shortening these is if opportunistc encryption is used towards cloud instances that can quickly re-use IP addresses. This value is only used during the libreswan startup process by the ipsec _stackmanager helper. See also <code>failureshunt</code> and <code>negotiationshunt</code></dl>
<p> <code>dumpdir</code></p>
<dl>
<dd>in what directory should things started by <i>setup</i> (notably the Pluto daemon) be allowed to dump core? The default value is <i>/var/run/pluto</i>. When SELinux runs in enforced mode, changing this requires a similar change in the SELinux policy for the pluto daemon.</dl>
<p> <code>statsbin</code></p>
<dl>
<dd>This option specifies an optional external program to report tunnel state changes too. The default is not to report tunnel state changes. This program can be used to notify the user&#8217;s desktop (dbus, NetworkManager) or to report tunnel changes to a central logging server.</dl>
<p> <code>ipsecdir</code></p>
<dl>
<dd>Specifies a directory for administrator-controlled configuration files and directories. The default value is <i>/etc/ipsec.d</i>. It may contain the following files and directories: </p>
<p> passwd</p>
<dl>
<dd>(optional) for XAUTH support if not using PAM (this file should not be world-readable). See README.XAUTH for more information.</dl>
<p> nsspassword</p>
<dl>
<dd>(optional) passwords needed to unlock the NSS database in /etc/ipsec.d (this file should not be world-readable). See README.nss for more information.</dl>
<p> policies/</p>
<dl>
<dd>a directory containing policy group configuration information. See <code>POLICY GROUP FILES</code> in this document for more information.</dl>
<p> cacerts/</p>
<dl>
<dd>DEPRECATED: a directory to store trust anchors (root certificate authority certificates). The preferred (and default) approach is to store CA certs in the NSS database instead. See README.nss for more information.</dl>
<p> crls/</p>
<dl>
<dd>DEPRECATED: a directory to store certificate revocation lists. The preferred (and default) approach is to store CRLs in the NSS database instead. See README.nss for more information.</dl>
<p> When SELinux runs in enforced mode, changing this requires a similar change in the SELinux policy for the pluto daemon. </p>
<p> On debian systems, the NSS database itself is not controlled by this value, and is instead located in /etc/ipsec.d.</dl>
<p> <code>secretsfile</code></p>
<dl>
<dd>in which file the secret credentials such as preshared keys (PSKs) are stored. See <i>man ipsec.secrets</i> for the syntax. The default value is /etc/ipsec.secrets.</dl>
<p> <code>perpeerlog</code></p>
<dl>
<dd>if pluto should split the logs in a per-peer directory. Valid options are <code>no</code>(the default) and <code>yes</code>. When enabled, logging is split into directories based on IP address. When disabled, logging is done via syslog or a single log file, as defined by <code>logfile=</code></dl>
<p> <code>perpeerlogdir</code></p>
<dl>
<dd>in what directory the per-peer log should be created, if enabled via the <code>perpeerlog</code> option. This will result in sub directories in the structure /192/0/2. The default value is <i>/var/log/pluto/peer/</i>. When SELinux runs in enforced mode, changing this requires a similar change in the SELinux policy for the pluto daemon.</dl>
<p> <code>fragicmp</code></p>
<dl>
<dd>whether a tunnel&#8217;s need to fragment a packet should be reported back with an ICMP message, in an attempt to make the sender lower his PMTU estimate; acceptable values are <code>no</code> (the default) and <code>yes</code>. This KLIPS option has no effect on NETKEY, Windows or BSD stacks.</dl>
<p> <code>hidetos</code></p>
<dl>
<dd>whether a tunnel packet&#8217;s TOS field should be set to 0 rather than copied from the user packet inside; acceptable values are <code>yes</code> (the default) and <code>no</code>. This KLIPS option has no effect on NETKEY, Windows or BSD stacks.</dl>
<p> <code>overridemtu</code></p>
<dl>
<dd>value that the MTU of the ipsec<i>n</i> interface(s) should be set to, overriding IPsec&#8217;s (large) default. This parameter is needed only in special situations. This KLIPS option has no effect on NETKEY, Windows or BSD stacks.</dl>
<p> <code>seccomp</code></p>
<dl>
<dd>Set the seccomp kernel syscall whitelisting feature. When set to <i>enabled</i>, if pluto calls a syscall that is not on the compiled-in whitelist, the kernel will assume an exploit is attempting to use pluto for malicious access to the system and terminate the pluto daemon. When set to <i>tolerant</i>, the kernel will only block the rogue syscall and pluto will attempt to continue. If set to <i>disabled</i>, pluto is allowed to call any syscall offered by the kernel, although it might be restricted via other security mechanisms, such as capabilities, SElinux, AppArmor or other OS security features. </p>
<p> The current default is disabled, but it is expected that in the future this feature will be enabled on all supported operating systems. Similarly, it is expected that further privilege separation will reduce the allowed syscalls &#8211; for example for the crypto helpers or DNS helpers. </p>
<p> <code>Warning:</code> The restrictions of pluto are inherited by the updown scripts, so these scripts are also not allowed to use syscalls that are forbidden for pluto. </p>
<p> This feature can be tested using <i>ipsec whack &#8211;seccomp-crashtest</i>. <code>Warning: </code> With seccomp=enabled, pluto will be terminated by the kernel. With seccomp=tolerant or seccomp=disabled, pluto will report the results of the seccomp test. SECCOMP will log the forbidden syscall numbers to the audit log, but only with seccomp=enabled. The tool scmp_sys_resolver from the libseccomp development package can be used to translate the syscall number into a name. See programs/pluto/pluto_seccomp.c for the list of allowed syscalls.</dl>
<h2>Implicit Conns</h2>
<p>The system automatically defines several conns to implement default policy groups. Each can be overridden by explicitly defining a new conn with the same name. If the new conn has <code>auto=ignore</code>, the definition is suppressed. </p>
<p> Here are the automatically supplied definitions. </p>
<dl>
<dd>
<pre><code>conn clear
 type=passthrough
 authby=never
 left=%defaultroute
 right=%group
 auto=route
conn clear-or-private
 type=passthrough
 left=%defaultroute
 leftid=%myid
 right=%opportunisticgroup
 failureshunt=passthrough
 keyingtries=3
 ikelifetime=1h
 salifetime=1h
 rekey=no
 auto=route
conn private-or-clear
 type=tunnel
 left=%defaultroute
 leftid=%myid
 right=%opportunisticgroup
 failureshunt=passthrough
 keyingtries=3
 ikelifetime=1h
 salifetime=1h
 rekey=no
 auto=route
conn private
 type=tunnel
 left=%defaultroute
 leftid=%myid
 right=%opportunisticgroup
 failureshunt=drop
 keyingtries=3
 ikelifetime=1h
 salifetime=1h
 rekey=no
 auto=route
conn block
 type=reject
 authby=never
 left=%defaultroute
 right=%group
 auto=route
# default policy
conn packetdefault
 type=tunnel
 left=%defaultroute
 leftid=%myid
 left=0.0.0.0/0
 right=%opportunistic
 failureshunt=passthrough
 keyingtries=3
 ikelifetime=1h
 salifetime=1h
 rekey=no
 auto=route</code></pre>
</dl>
<p> These conns are <i>not</i> affected by anything in <code>conn %default</code>. They will only work if <code>%defaultroute</code> works. The <code>leftid</code> will be the interfaces IP address; this requires that reverse DNS records be set up properly. </p>
<p> The implicit conns are defined after all others. It is appropriate and reasonable to use <code>also=private-or-clear</code> (for example) in any other opportunistic conn.</p>
<h2>Policy Group Files</h2>
<p>The optional files under /etc/ipsec.d/policies, including </p>
<dl>
<dd>
<pre>/etc/ipsec.d/policies/clear
/etc/ipsec.d/policies/clear-or-private
/etc/ipsec.d/policies/private-or-clear
/etc/ipsec.d/policies/private
/etc/ipsec.d/policies/block</pre>
</dl>
<p> may contain policy group configuration information to supplement <i>ipsec.conf</i>. Their contents are not security-sensitive. </p>
<p> These files are text files. Each consists of a list of CIDR blocks, one per line. White space followed by # followed by anything to the end of the line is a comment and is ignored, as are empty lines. </p>
<p> A connection in ipsec.conf which has <code>right=%group</code> or <code>right=%opportunisticgroup</code> is a policy group connection. When a policy group file of the same name is loaded, with </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><code>ipsec auto &#8211;rereadgroups</code> </p>
<p> or at system start, the connection is instantiated such that each CIDR block serves as an instance&#8217;s <code>right</code> value. The system treats the resulting instances as normal connections. </p>
<p> For example, given a suitable connection definition <code>private</code>, and the file /etc/ipsec.d/policies/private with an entry 192.0.2.3, the system creates a connection instance <code>private#192.0.2.3.</code> This connection inherits all details from <code>private</code>, except that its right client is 192.0.2.3.</p>
<h2>Default Policy Groups</h2>
<p>The standard Libreswan install includes several policy groups which provide a way of classifying possible peers into IPsec security classes: <code>private</code> (talk encrypted only), <code>private-or-clear</code> (prefer encryption), <code>clear-or-private</code> (respond to requests for encryption), <code>clear</code> and <code>block</code>. Implicit policy groups apply to the local host only, and are implemented by the <code>IMPLICIT CONNECTIONS</code> described above.</p>
<h2>Obsolete</h2>
<p>Various options have recently been obsoleted and are ignored. The options <code>prepluto=</code> and <code>plutopost=</code> have been obsoleted because these were used by the (obsoleted) shell wrappers launching the pluto daemon. If this functionality is needed, look at your initsystem for support. For example, the <code>systemd</code> initsystem has the options <code>ExecStartPre=</code> and <code>ExecStopPost=</code> to accomplish the same. The option <code>plutoopts=</code> has also been obsoleted for this reason. A replacement can be found in the <code>PLUTO_OPTS</code> environment variable in the file <code>/etc/sysconfig/pluto</code> (Fedora/RHEL) or <code>/etc/defaults/pluto</code> (Debian/Ubuntu). The last two options obsoleted by the removal of the old shell scripts are <code>pluto=</code> and <code>plutowait=</code>. </p>
<p> The following ipsec commands have been obsoleted: <code>ipsec _confread</code>, <code>ipsec _include</code>, <code>ipsec _plutoload</code>, <code>ipsec _realsetup</code>, <code>ipsec _startklips</code> and <code>ipsec _startnetkey</code> due to the new parsing and startup methods and <code>ipsec copyright</code>, <code>ipsec lwdnsq</code>, <code>ipsec mailkey</code>, <code>ipsec policy</code>, <code>ipsec showdefaults</code> and <code>ipsec showpolicy</code> because they were no longer needed or current.</p>
<h2>Choosing A Connection [This Section Is Extremely Out Of Date</h2>
<p>When choosing a connection to apply to an outbound packet caught with a <code>%trap,</code> the system prefers the one with the most specific eroute that includes the packet&#8217;s source and destination IP addresses. Source subnets are examined before destination subnets. For initiating, only routed connections are considered. For responding, unrouted but added connections are considered. </p>
<p> When choosing a connection to use to respond to a negotiation which doesn&#8217;t match an ordinary conn, an opportunistic connection may be instantiated. Eventually, its instance will be /32 -&gt; /32, but for earlier stages of the negotiation, there will not be enough information about the client subnets to complete the instantiation.</p>
<h2>Files</h2>
<dl>
<dd>
<pre>/etc/ipsec.conf
/etc/ipsec.d/policies/clear
/etc/ipsec.d/policies/clear-or-private
/etc/ipsec.d/policies/private-or-clear
/etc/ipsec.d/policies/private
/etc/ipsec.d/policies/block</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-ipsec/">ipsec</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_ttoaddr/">ipsec_ttoaddr</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_auto/">ipsec_auto</a></code>(8), <code><a href="/docs/linux/man/8-ipsec_rsasigkey/">ipsec_rsasigkey</a></code>(8)</p>
<h2>History</h2>
<p>Designed for the FreeS/WAN project &lt;m[blue]<code><a rel="nofollow" href="http://www.freeswan.org">http://www.freeswan.org</a></code>m[]&gt; by Henry Spencer.</p>
<h2>Bugs</h2>
<p>Before reporting new bugs, please ensure you are using the latest version of Libreswan, and if not using KLIPS, please ensure you are using the latest kernel code for your IPsec stack. </p>
<p> When <code>type</code> or <code>failureshunt</code> is set to <code>drop</code> or <code>reject,</code> Libreswan blocks outbound packets using eroutes, but assumes inbound blocking is handled by the firewall. Libreswan offers firewall hooks via an &#8220;updown&#8221; script. However, the default <code>ipsec _updown</code> provides no help in controlling a modern firewall. </p>
<p> Including attributes of the keying channel (authentication methods, <code>ikelifetime</code>, etc.) as an attribute of a connection, rather than of a participant pair, is dubious and incurs limitations. </p>
<p> The use of <code>%any</code> with the <i>protoport=</i> option is ambiguous. Should the SA permits any port through or should the SA negotiate any single port through? The first is a basic conn with a wildcard. The second is a template. The second is the current behaviour, and it&#8217;s wrong for quite a number of uses involving TCP. The keyword <code>%one</code> may be introduced in the future to separate these two cases. </p>
<p> It would be good to have a line-continuation syntax, especially for the very long lines involved in RSA signature keys. </p>
<p> <code>First packet caching</code> is only implemented for the KLIPS(NG) and MAST stacks. NETKEY returns POSIX-breaking responses, visible as <i>connect: Resource temporarily unavailable</i> errors. This affects Opportunistic Encryption and DPD. Functionality on the BSD and Windows stacks is unknown. </p>
<p> Some state information is only available when using KLIPS, and will return errors on other IPsec stacks. These include <i>ipsec eroute</i>, <i>ipsec spi</i> and <i>ipsec look</i>. </p>
<p> Multiple L2TP clients behind the same NAT router, and multiple L2TP clients behind different NAT routers using the same Virtual IP is currently only working for the KLIPSNG stack. </p>
<p> The ability to specify different identities, <code>authby</code>, and public keys for different automatic-keyed connections between the same participants is misleading; this doesn&#8217;t work dependably because the identity of the participants is not known early enough. This is especially awkward for the &#8220;Road Warrior&#8221; case, where the remote IP address is specified as 0.0.0.0, and that is considered to be the &#8220;participant&#8221; for such connections. </p>
<p> In principle it might be necessary to control MTU on an interface-by-interface basis, rather than with the single global override that <code>overridemtu</code> provides. This feature is planned for a future release. </p>
<p> If conns are to be added before DNS is available, <code>left=</code><i>FQDN</i>, <code>leftnextop=</code><i>FQDN</i>, and <code>leftrsasigkey=%dnsonload</code> will fail. <code><a href="/docs/linux/man/8-ipsec_pluto/">ipsec_pluto</a></code>(8) does not actually use the public key for our side of a conn but it isn&#8217;t generally known at a add-time which side is ours (Road Warrior and Opportunistic conns are currently exceptions). </p>
<p> The <code>myid</code> option does not affect explicit <code> ipsec auto &#8211;add</code> or <code>ipsec auto &#8211;replace</code> commands for implicit conns.</p>
<h2>Author</h2>
<p><code>Paul Wouters</code></p>
<dl>
<dd>documenter</dl>
