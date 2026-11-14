---
title: "strongswan_ipsec-conf(5)"
name: "strongswan_ipsec-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-strongswan_ipsec-conf/"
description: "ipsec.conf – IPsec configuration and connections"
---

<p>ipsec.conf &#8211; IPsec configuration and connections</p>
<h2>Description</h2>
<p>The optional <i>ipsec.conf</i> file specifies most configuration and control information for the strongSwan IPsec subsystem. The major exception is secrets for authentication; see <i><a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a></i>(5). Its contents are not security-sensitive. </p>
<p> The file is a text file, consisting of one or more <i>sections</i>. White space followed by <code>#</code> followed by anything to the end of the line is a comment and is ignored, as are empty lines which are not within a section. </p>
<p> A line which contains <code>include</code> and a file name, separated by white space, is replaced by the contents of that file. If the file name is not a full pathname, it is considered to be relative to the directory containing the including file. Such inclusions can be nested. Only a single filename may be supplied, and it may not contain white space, but it may include shell wildcards (see <i><a href="/docs/linux/man/1-sh/">sh</a></i>(1)); for example: </p>
<p> <code>include</code> <code>ipsec.*.conf</code> </p>
<p> The intention of the include facility is mostly to permit keeping information on connections, or sets of connections, separate from the main configuration file. This permits such connection descriptions to be changed, copied to the other security gateways involved, etc., without having to constantly extract them from the configuration file and then insert them back into it. Note also the <code>also</code> parameter (described below) which permits splitting a single logical section (e.g. a connection description) into several actual sections. </p>
<p> A section begins with a line of the form: </p>
<p> <i>type</i> <i>name</i> </p>
<p> where <i>type</i> indicates what type of section follows, and <i>name</i> is an arbitrary name which distinguishes the section from others of the same type. All subsequent non-empty lines which begin with white space are part of the section. Sections of the same type that share the same name are merged. </p>
<p> Lines within the section are generally of the form </p>
<p> &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr><i>parameter</i><code>=</code><i>value</i> </p>
<p> (note the mandatory preceding white space). There can be white space on either side of the <code>=</code>. Parameter names are specific to a section type. </p>
<p> An empty <i>value</i> stands for the system default value (if any) of the parameter, i.e. it is roughly equivalent to omitting the parameter line entirely. This may be useful to clear a setting inherited from a <code>%default</code> section or via <code>also</code> parameter (see below). A <i>value</i> may contain single spaces (additional white space is reduced to one space). To preserve white space as written enclose the entire <i>value</i> in double quotes (<code>&quot;</code>); in such values double quotes themselves may be escaped by prefixing them with <code>\</code> characters. A double-quoted string may span multiple lines by ending them with <code>\</code> characters (following lines don&#8217;t have to begin with white space, as that will be preserved). Additionally, the following control characters may be encoded in double-quoted strings: 
, , 	, , . </p>
<p> Numeric values are specified to be either an &#8220;integer&#8221; (a sequence of digits) or a &#8220;decimal number&#8221; (sequence of digits optionally followed by `.&#8217; and another sequence of digits). </p>
<p> There is currently one parameter which is available in any type of section:</p>
<dl>
<dt><code>also</code></p>
<dd>the value is a section name; the parameters of that section are inherited by the current section. Parameters in the current section always override inherited parameters, even if an <code>also</code> follows after them. The specified section must exist and must have the same section type; it doesn&#8217;t if it is defined before or after the current section. Nesting is permitted, and there may be more than one <code>also</code> in a single section (parameters from referenced sections are inherited and overridden in the order of these <code>also</code> parameters).</dl>
<p> A section with name <code>%default</code> specifies defaults for sections of the same type. All parameters in it, are inherited by all other sections of that type. </p>
<p> Currently there are three types of sections: a <code>config</code> section specifies general configuration information for IPsec, a <code>conn</code> section specifies an IPsec connection, while a <code>ca</code> section specifies special properties of a certification authority.</p>
<h2>Conn Sections</h2>
<p>A <code>conn</code> section contains a <i>connection specification</i>, defining a network connection to be made using IPsec. The name given is arbitrary, and is used to identify the connection. Here&#8217;s a simple example: </p>
<pre><code>conn snt
 left=192.168.0.1
 leftsubnet=10.1.0.0/16
 right=192.168.0.2
 rightsubnet=10.1.0.0/16
 keyingtries=%forever
 auto=add
</code></pre>
<p>A note on terminology: There are two kinds of communications going on: transmission of user IP packets, and gateway-to-gateway negotiations for keying, rekeying, and general control. The path to control the connection is called &#8216;ISAKMP SA&#8217; in IKEv1 and &#8216;IKE SA&#8217; in the IKEv2 protocol. That what is being negotiated, the kernel level data path, is called &#8216;IPsec SA&#8217; or &#8216;Child SA&#8217;. strongSwan previously used two separate keying daemons, <i>pluto</i> and <i>charon</i>. This manual does not discuss <i>pluto</i> options anymore, but only <i>charon</i> that since strongSwan 5.0 supports both IKEv1 and IKEv2. </p>
<p> To avoid trivial editing of the configuration file to suit it to each system involved in a connection, connection specifications are written in terms of <i>left</i> and <i>right</i> participants, rather than in terms of local and remote. Which participant is considered <i>left</i> or <i>right</i> is arbitrary; for every connection description an attempt is made to figure out whether the local endpoint should act as the <i>left</i> or <i>right</i> endpoint. This is done by matching the IP addresses defined for both endpoints with the IP addresses assigned to local network interfaces. If a match is found then the role (left or right) that matches is going to be considered local. If no match is found during startup, <i>left</i> is considered local. This permits using identical connection specifications on both ends. There are cases where there is no symmetry; a good convention is to use <i>left</i> for the local side and <i>right</i> for the remote side (the first letters are a good mnemonic). </p>
<p> Many of the parameters relate to one participant or the other; only the ones for <i>left</i> are listed here, but every parameter whose name begins with <code>left</code> has a <code>right</code> counterpart, whose description is the same but with <code>left</code> and <code>right</code> reversed. </p>
<p> Parameters are optional unless marked &#8216;(required)&#8217;.</p>
<h3>Conn Parameters</h3>
<p>Unless otherwise noted, for a connection to work, in general it is necessary for the two ends to agree exactly on the values of these parameters.</p>
<dl>
<dt><code>aaa_identity</code> = &lt;id&gt;</p>
<dd>defines the identity of the AAA backend used during IKEv2 EAP authentication. This is required if the EAP client uses a method that verifies the server identity (such as EAP-TLS), but it does not match the IKEv2 gateway identity.</p>
<dt><code>aggressive</code> = yes | <code>no</code></p>
<dd>whether to use IKEv1 Aggressive or Main Mode (the default).</p>
<dt><code>ah</code> = &lt;cipher suites&gt;</p>
<dd>comma-separated list of AH algorithms to be used for the connection, e.g. <code>sha1-sha256-modp1024</code>. The notation is <code>integrity[-dhgroup]</code>. For IKEv2, multiple algorithms (separated by -) of the same type can be included in a single proposal. IKEv1 only includes the first algorithm in a proposal. Only either the <code>ah</code> or <code>esp</code> keyword may be used, AH+ESP bundles are not supported. </p>
<p> There is no default AH cipher suite since by default ESP is used. The daemon adds its extensive default proposal to the configured value. To restrict it to the configured proposal an exclamation mark (<code>!</code>) can be added at the end. </p>
<p> If <code>dh-group</code> is specified, CHILD_SA/Quick Mode setup and rekeying include a separate Diffie-Hellman exchange (refer to the <code>esp</code> keyword for details).</p>
<dt><code>also</code> = &lt;name&gt;</p>
<dd>includes conn section <code>&lt;name&gt;</code>.</p>
<dt><code>auth</code> = &lt;value&gt;</p>
<dd>was used by the <code>pluto</code> IKEv1 daemon to use AH integrity protection for ESP encrypted packets, but is not supported in charon. The <code>ah</code> keyword specifies algorithms to use for integrity protection with AH, but without encryption. AH+ESP bundles are not supported.</p>
<dt><code>authby</code> = <code>pubkey</code> | rsasig | ecdsasig | psk | secret | never | xauthpsk | xauthrsasig</p>
<dd>how the two security gateways should authenticate each other; acceptable values are <code>psk</code> or <code>secret</code> for pre-shared secrets, <code>pubkey</code> (the default) for public key signatures as well as the synonyms <code>rsasig</code> for RSA digital signatures and <code>ecdsasig</code> for Elliptic Curve DSA signatures. <code>never</code> can be used if negotiation is never to be attempted or accepted (useful for shunt-only conns). Digital signatures are superior in every way to shared secrets. IKEv1 additionally supports the values <code>xauthpsk</code> and <code>xauthrsasig</code> that will enable eXtended AUTHentication (XAUTH) in addition to IKEv1 main mode based on shared secrets or digital RSA signatures, respectively. This parameter is deprecated, as two peers do not need to agree on an authentication method in IKEv2. Use the <code>leftauth</code> parameter instead to define authentication methods.</p>
<dt><code>auto</code> = <code>ignore</code> | add | route | start</p>
<dd>what operation, if any, should be done automatically at IPsec startup; currently-accepted values are <code>add</code>, <code>route</code>, <code>start</code> and <code>ignore</code> (the default). <code>add</code> loads a connection without starting it. <code>route</code> loads a connection and installs kernel traps. If traffic is detected between <code>leftsubnet</code> and <code>rightsubnet</code>, a connection is established. <code>start</code> loads a connection and brings it up immediately. <code>ignore</code> ignores the connection. This is equal to deleting a connection from the config file. Relevant only locally, other end need not agree on it.</p>
<dt><code>closeaction</code> = <code>none</code> | clear | hold | restart</p>
<dd>defines the action to take if the remote peer unexpectedly closes a CHILD_SA (see <code>dpdaction</code> for meaning of values). A <code>closeaction should not be</code> used if the peer uses reauthentication or uniquids checking, as these events might trigger the defined action when not desired.</p>
<dt><code>compress</code> = yes | <code>no</code></p>
<dd>whether IPComp compression of content is proposed on the connection (link-level compression does not work on encrypted data, so to be effective, compression must be done <i>before</i> encryption); acceptable values are <code>yes</code> and <code>no</code> (the default). A value of <code>yes</code> causes the daemon to propose both compressed and uncompressed, and prefer compressed. A value of <code>no</code> prevents the daemon from proposing or accepting compression.</p>
<dt><code>dpdaction</code> = <code>none</code> | clear | hold | restart</p>
<dd>controls the use of the Dead Peer Detection protocol (DPD, RFC 3706) where R_U_THERE notification messages (IKEv1) or empty INFORMATIONAL messages (IKEv2) are periodically sent in order to check the liveliness of the IPsec peer. The values <code>clear</code>, <code>hold</code>, and <code>restart</code> all activate DPD and determine the action to perform on a timeout. With <code>clear</code> the connection is closed with no further actions taken. <code>hold</code> installs a trap policy, which will catch matching traffic and tries to re-negotiate the connection on demand. <code>restart</code> will immediately trigger an attempt to re-negotiation the connection. The default is <code>none</code> which disables the active sending of DPD messages.</p>
<dt><code>dpddelay</code> = <code>30s</code> | &lt;time&gt;</p>
<dd>defines the period time interval with which R_U_THERE messages/INFORMATIONAL exchanges are sent to the peer. These are only sent if no other traffic is received. In IKEv2, a value of 0 sends no additional INFORMATIONAL messages and uses only standard messages (such as those to rekey) to detect dead peers.</p>
<dt><code>dpdtimeout</code> = <code>150s</code> | &lt;time&gt;</p>
<dd>defines the timeout interval, after which all connections to a peer are deleted in case of inactivity. This only applies to IKEv1, in IKEv2 the default retransmission timeout applies, as every exchange is used to detect dead peers.</p>
<dt><code>inactivity</code> = &lt;time&gt;</p>
<dd>defines the timeout interval, after which a CHILD_SA is closed if it did not send or receive any traffic. The inactivity counter is reset during CHILD_SA rekeying. This means that the inactivity timeout must be smaller than the rekeying interval to have any effect.</p>
<dt><code>eap_identity</code> = &lt;id&gt;</p>
<dd>defines the identity the client uses to reply to an EAP Identity request. If defined on the EAP server, the defined identity will be used as peer identity during EAP authentication. The special value <code>%identity</code> uses the EAP Identity method to ask the client for an EAP identity. If not defined, the IKEv2 identity will be used as EAP identity.</p>
<dt><code>esp</code> = &lt;cipher suites&gt;</p>
<dd>comma-separated list of ESP encryption/authentication algorithms to be used for the connection, e.g. <code>aes128-sha256</code>. The notation is <code>encryption-integrity[-dhgroup][-esnmode]</code>. For IKEv2, multiple algorithms (separated by -) of the same type can be included in a single proposal. IKEv1 only includes the first algorithm in a proposal. Only either the <code>ah</code> or <code>esp</code> keyword may be used, AH+ESP bundles are not supported. </p>
<p> Defaults to <code>aes128-sha256</code>. The daemon adds its extensive default proposal to this default or the configured value. To restrict it to the configured proposal an exclamation mark (<code>!</code>) can be added at the end. </p>
<p> <code>Note</code>: As a responder, the daemon defaults to selecting the first configured proposal that&#8217;s also supported by the peer. This may be changed via <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5) to selecting the first acceptable proposal sent by the peer instead. In order to restrict a responder to only accept specific cipher suites, the strict flag (<code>!</code>, exclamation mark) can be used, e.g: aes256-sha512-modp4096! </p>
<p> If <code>dh-group</code> is specified, CHILD_SA/Quick Mode rekeying and initial negotiation use a separate Diffie-Hellman exchange using the specified group. However, for IKEv2, the keys of the CHILD_SA created implicitly with the IKE_SA will always be derived from the IKE_SA&#8217;s key material. So any DH group specified here will only apply when the CHILD_SA is later rekeyed or is created with a separate CREATE_CHILD_SA exchange. Therefore, a proposal mismatch might not immediately be noticed when the SA is established, but may later cause rekeying to fail. </p>
<p> Valid values for <code>esnmode</code> are <code>esn</code> and <code>noesn</code>. Specifying both negotiates Extended Sequence Number support with the peer, the default is <code>noesn.</code></p>
<dt><code>forceencaps</code> = yes | <code>no</code></p>
<dd>force UDP encapsulation for ESP packets even if no NAT situation is detected. This may help to surmount restrictive firewalls. In order to force the peer to encapsulate packets, NAT detection payloads are faked.</p>
<dt><code>fragmentation</code> = <code>yes</code> | accept | force | no</p>
<dd>whether to use IKE fragmentation (proprietary IKEv1 extension or IKEv2 fragmentation as per RFC 7383). Acceptable values are <code>yes</code> (the default), <code>accept</code>, <code>force</code> and <code>no</code>. If set to <code>yes</code>, and the peer supports it, oversized IKE messages will be sent in fragments. If set to <code>accept</code>, support for fragmentation is announced to the peer but the daemon does not send its own messages in fragments. If set to <code>force</code> (only supported for IKEv1) the initial IKE message will already be fragmented if required. Finally, setting the option to <code>no</code> will disable announcing support for this feature. </p>
<p> Note that fragmented IKE messages sent by a peer are always accepted irrespective of the value of this option (even when set to <code>no</code>).</p>
<dt><code>ike</code> = &lt;cipher suites&gt;</p>
<dd>comma-separated list of IKE/ISAKMP SA encryption/authentication algorithms to be used, e.g. <code>aes128-sha256-modp3072</code>. The notation is <code>encryption-integrity[-prf]-dhgroup</code>. If no PRF is given, the algorithms defined for integrity are used for the PRF. The prf keywords are the same as the integrity algorithms, but have a <code>prf</code> prefix (such as <code>prfsha1</code>, <code>prfsha256</code> or <code>prfaesxcbc</code>).<br />
 In IKEv2, multiple algorithms and proposals may be included, such as <code>aes128-aes256-sha1-modp3072-modp2048,3des-sha1-md5-modp1024</code>. </p>
<p> Defaults to <code>aes128-sha256-modp3072</code>. The daemon adds its extensive default proposal to this default or the configured value. To restrict it to the configured proposal an exclamation mark (<code>!</code>) can be added at the end. </p>
<p> <code>Note</code>: As a responder the daemon accepts the first supported proposal received from the peer. In order to restrict a responder to only accept specific cipher suites, the strict flag (<code>!</code>, exclamation mark) can be used, e.g: <code>aes256-sha512-modp4096!</code></p>
<dt><code>ikedscp</code> = <code>000000</code> | &lt;DSCP field&gt;</p>
<dd>Differentiated Services Field Codepoint to set on outgoing IKE packets sent from this connection. The value is a six digit binary encoded string defining the Codepoint to set, as defined in RFC 2474.</p>
<dt><code>ikelifetime</code> = <code>3h</code> | &lt;time&gt;</p>
<dd>how long the keying channel of a connection (ISAKMP or IKE SA) should last before being renegotiated. Also see EXPIRY/REKEY below.</p>
<dt><code>installpolicy</code> = <code>yes</code> | no</p>
<dd>decides whether IPsec policies are installed in the kernel by the charon daemon for a given connection. Allows peaceful cooperation e.g. with the Mobile IPv6 daemon mip6d who wants to control the kernel policies. Acceptable values are <code>yes</code> (the default) and <code>no</code>.</p>
<dt><code>keyexchange</code> = <code>ike</code> | ikev1 | ikev2</p>
<dd>which key exchange protocol should be used to initiate the connection. Connections marked with <code>ike</code> use IKEv2 when initiating, but accept any protocol version when responding.</p>
<dt><code>keyingtries</code> = <code>3</code> | &lt;number&gt; | %forever</p>
<dd>how many attempts (a whole number or <code>%forever</code>) should be made to negotiate a connection, or a replacement for one, before giving up (default <code>3</code>). The value <code>%forever</code> means &#8216;never give up&#8217;. Relevant only locally, other end need not agree on it.</p>
<dt><code>keylife</code></p>
<dd>synonym for <code>lifetime</code>.</p>
<dt><code>left</code> = &lt;ip address&gt; | &lt;fqdn&gt; | <code>%any</code> | &lt;range&gt; | &lt;subnet&gt;</p>
<dd>The IP address of the left participant&#8217;s public-network interface or one of several magic values. The value <code>%any</code> (the default) for the local endpoint signifies an address to be filled in (by automatic keying) during negotiation. If the local peer initiates the connection setup the routing table will be queried to determine the correct local IP address. In case the local peer is responding to a connection setup then any IP address that is assigned to a local interface will be accepted. </p>
<p> The prefix <code>%</code> in front of a fully-qualified domain name or an IP address will implicitly set <code>leftallowany</code>=yes. </p>
<p> If <code>%any</code> is used for the remote endpoint it literally means any IP address. </p>
<p> If an <code>FQDN</code> is assigned it is resolved every time a configuration lookup is done. If DNS resolution times out, the lookup is delayed for that time. </p>
<p> To limit the connection to a specific range of hosts, a range ( <code>10.1.0.0-10.2.255.255</code> ) or a subnet ( <code>10.1.0.0/16</code> ) can be specified, and multiple addresses, ranges and subnets can be separated by commas. While one can freely combine these items, to initiate the connection at least one non-range/subnet is required. </p>
<p> Please note that with the usage of wildcards multiple connection descriptions might match a given incoming connection attempt. The most specific description is used in that case.</p>
<dt><code>leftallowany</code> = yes | <code>no</code></p>
<dd>a modifier for <code>left</code>, making it behave as <code>%any</code> although a concrete IP address or domain name has been assigned.</p>
<dt><code>leftauth</code> = &lt;auth method&gt;</p>
<dd>Authentication method to use locally (left) or require from the remote (right) side. Acceptable values are <code>pubkey</code> for public key authentication (RSA/ECDSA), <code>psk</code> for pre-shared key authentication, <code>eap</code> to (require the) use of the Extensible Authentication Protocol in IKEv2, and <code>xauth</code> for IKEv1 eXtended Authentication. </p>
<p> To require a trustchain public key strength for the remote side, specify the key type followed by the minimum strength in bits (for example <code>ecdsa-384</code> or <code>rsa-2048-ecdsa-256</code>). To limit the acceptable set of hashing algorithms for trustchain validation, append hash algorithms to <code>pubkey</code> or a key strength definition (for example <code>pubkey-sha1-sha256</code> or <code>rsa-2048-ecdsa-256-sha256-sha384-sha512</code>). Unless disabled in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5), or explicit IKEv2 signature constraints are configured (see below), such key types and hash algorithms are also applied as constraints against IKEv2 signature authentication schemes used by the remote side. </p>
<p> If both peers support RFC 7427 (&quot;Signature Authentication in IKEv2&quot;) specific hash algorithms to be used during IKEv2 authentication may be configured. The syntax is the same as above, but with ike: prefix. For example, with <code>ike:pubkey-sha384-sha256</code> a public key signature scheme with either SHA-384 or SHA-256 would get used for authentication, in that order and depending on the hash algorithms supported by the peer. If no specific hash algorithms are configured, the default is to prefer an algorithm that matches or exceeds the strength of the signature key. If no constraints with ike: prefix are configured any signature scheme constraint (without ike: prefix) will also apply to IKEv2 authentication, unless this is disabled in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<p> For <code>eap</code>, an optional EAP method can be appended. Currently defined methods are <code>eap-aka</code>, <code>eap-gtc</code>, <code>eap-md5</code>, <code>eap-mschapv2</code>, <code>eap-peap</code>, <code>eap-sim</code>, <code>eap-tls</code>, <code>eap-ttls</code>, <code>eap-dynamic</code>, and <code>eap-radius</code>. Alternatively, IANA assigned EAP method numbers are accepted. Vendor specific EAP methods are defined in the form <code>eap-type-vendor</code> (e.g. <code>eap-7-12345</code>). To specify signature and trust chain constraints for EAP-(T)TLS, append a colon to the EAP method, followed by the key type/size and hash algorithm as discussed above. For <code>xauth,</code> an XAuth authentication backend can be specified, such as <code>xauth-generic</code> or <code>xauth-eap</code>. If XAuth is used in <code>leftauth</code>, Hybrid authentication is used. For traditional XAuth authentication, define XAuth in <code>lefauth2</code>.</p>
<dt><code>leftauth2</code> = &lt;auth method&gt;</p>
<dd>Same as <code>leftauth</code>, but defines an additional authentication exchange. In IKEv1, only XAuth can be used in the second authentication round. IKEv2 supports multiple complete authentication rounds using &quot;Multiple Authentication Exchanges&quot; defined in RFC 4739. This allows, for example, separated authentication of host and user.</p>
<dt><code>leftca</code> = &lt;issuer dn&gt; | %same</p>
<dd>the distinguished name of a certificate authority which is required to lie in the trust path going from the left participant&#8217;s certificate up to the root certification authority. <code>%same</code> means that the value configured for the right participant should be reused.</p>
<dt><code>leftca2</code> = &lt;issuer dn&gt; | %same</p>
<dd>Same as <code>leftca</code>, but for the second authentication round (IKEv2 only).</p>
<dt><code>leftcert</code> = &lt;path&gt;</p>
<dd>the path to the left participant&#8217;s X.509 certificate. The file can be encoded either in PEM or DER format. OpenPGP certificates are supported as well. Both absolute paths or paths relative to <i>/etc/ipsec.d/certs</i> are accepted. By default <code>leftcert</code> sets <code>leftid</code> to the distinguished name of the certificate&#8217;s subject. The left participant&#8217;s ID can be overridden by specifying a <code>leftid</code> value which must be certified by the certificate, though.<br />
 A value in the form <code>%smartcard[&lt;slot nr&gt;[@&lt;module&gt;]]:&lt;keyid&gt;</code> defines a specific certificate to load from a PKCS#11 backend for this connection. See <a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a>(5) for details about smartcard definitions. <code>leftcert</code> is required only if selecting the certificate with <code>leftid</code> is not sufficient, for example if multiple certificates use the same subject.<br />
 Multiple certificate paths or PKCS#11 backends can be specified in a comma separated list. The daemon chooses the certificate based on the received certificate requests if possible before enforcing the first.</p>
<dt><code>leftcert2</code> = &lt;path&gt;</p>
<dd>Same as <code>leftcert,</code> but for the second authentication round (IKEv2 only).</p>
<dt><code>leftcertpolicy</code> = &lt;OIDs&gt;</p>
<dd>Comma separated list of certificate policy OIDs the peer&#8217;s certificate must have. OIDs are specified using the numerical dotted representation.</p>
<dt><code>leftdns</code> = &lt;servers&gt;</p>
<dd>Comma separated list of DNS server addresses to exchange as configuration attributes. On the initiator, a server is a fixed IPv4/IPv6 address, or <code>%config4</code>/<code>%config6</code> to request attributes without an address. On the responder, only fixed IPv4/IPv6 addresses are allowed and define DNS servers assigned to the client.</p>
<dt><code>leftfirewall</code> = yes | <code>no</code></p>
<dd>whether the left participant is doing forwarding-firewalling (including masquerading) using iptables for traffic from <i>leftsubnet</i>, which should be turned off (for traffic to the other subnet) once the connection is established; acceptable values are <code>yes</code> and <code>no</code> (the default). May not be used in the same connection description with <code>leftupdown</code>. Implemented as a parameter to the default <code>ipsec _updown</code> script. See notes below. Relevant only locally, other end need not agree on it. </p>
<p> If one or both security gateways are doing forwarding firewalling (possibly including masquerading), and this is specified using the firewall parameters, tunnels established with IPsec are exempted from it so that packets can flow unchanged through the tunnels. (This means that all subnets connected in this manner must have distinct, non-overlapping subnet address blocks.) This is done by the default <code>ipsec _updown</code> script. </p>
<p> In situations calling for more control, it may be preferable for the user to supply his own <i>updown</i> script, which makes the appropriate adjustments for his system.</p>
<dt><code>leftgroups</code> = &lt;group list&gt;</p>
<dd>a comma separated list of group names. If the <code>leftgroups</code> parameter is present then the peer must be a member of at least one of the groups defined by the parameter.</p>
<dt><code>leftgroups2</code> = &lt;group list&gt;</p>
<dd>Same as <code>leftgroups,</code> but for the second authentication round defined with <code>leftauth2.</code></p>
<dt><code>lefthostaccess</code> = yes | <code>no</code></p>
<dd>inserts a pair of INPUT and OUTPUT iptables rules using the default <code>ipsec _updown</code> script, thus allowing access to the host itself in the case where the host&#8217;s internal interface is part of the negotiated client subnet. Acceptable values are <code>yes</code> and <code>no</code> (the default).</p>
<dt><code>leftid</code> = &lt;id&gt;</p>
<dd>how the left participant should be identified for authentication; defaults to <code>left</code> or the subject of the certificate configured with <code>leftcert</code>. If <code>leftcert</code> is configured the identity has to be confirmed by the certificate. </p>
<p> Can be an IP address, a fully-qualified domain name, an email address or a Distinguished Name for which the ID type is determined automatically and the string is converted to the appropriate encoding. The rules for this conversion are described in IDENTITY PARSING below. </p>
<p> In certain special situations the identity parsing above might be inadequate or produce the wrong result. Examples are the need to encode a FQDN as KEY_ID or the string parser being unable to produce the correct binary ASN.1 encoding of a certificate&#8217;s DN. For these situations it is possible to enforce a specific identity type and to provide the binary encoding of the identity. To do this a prefix may be used, followed by a colon (:). If the number sign (#) follows the colon, the remaining data is interpreted as hex encoding, otherwise the string is used as is as the identification data. <code>Note</code>: The latter implies that no conversion is performed for non-string identities. For example, <i>ipv4:10.0.0.1</i> does not create a valid ID_IPV4_ADDR IKE identity, as it does not get converted to binary 0x0a000001. Instead, one could use <i>ipv4:#0a000001</i> to get a valid identity, but just using the implicit type with automatic conversion is usually simpler. The same applies to the ASN.1 encoded types. The following prefixes are known: <code>ipv4</code>, <code>ipv6</code>, <code>rfc822</code>, <code>email</code>, <code>userfqdn</code>, <code>fqdn</code>, <code>dns</code>, <code>asn1dn</code>, <code>asn1gn</code> and <code>keyid</code>. Custom type prefixes may be specified by surrounding the numerical type value by curly brackets. </p>
<p> For IKEv2 and <code>rightid</code> the prefix <code>%</code> in front of the identity prevents the daemon from sending IDr in its IKE_AUTH request and will allow it to verify the configured identity against the subject and subjectAltNames contained in the responder&#8217;s certificate (otherwise it is only compared with the IDr returned by the responder). The IDr sent by the initiator might otherwise prevent the responder from finding a config if it has configured a different value for <code>leftid</code>.</p>
<dt><code>leftid2</code> = &lt;id&gt;</p>
<dd>identity to use for a second authentication for the left participant (IKEv2 only); defaults to <code>leftid</code>.</p>
<dt><code>leftikeport</code> = &lt;port&gt;</p>
<dd>UDP port the left participant uses for IKE communication. If unspecified, port 500 is used with the port floating to 4500 if a NAT is detected or MOBIKE is enabled. Specifying a local IKE port different from the default additionally requires a socket implementation that listens on this port.</p>
<dt><code>leftprotoport</code> = &lt;protocol&gt;/&lt;port&gt;</p>
<dd>restrict the traffic selector to a single protocol and/or port. This option is now deprecated, protocol/port information can be defined for each subnet directly in <code>leftsubnet</code>.</p>
<dt><code>leftsigkey</code> = &lt;raw public key&gt; | &lt;path to public key&gt;</p>
<dd>the left participant&#8217;s public key for public key signature authentication, in PKCS#1 format using hex (0x prefix) or base64 (0s prefix) encoding. With the optional <code>dns:</code> or <code>ssh:</code> prefix in front of 0x or 0s, the public key is expected to be in either the RFC 3110 (not the full RR, only RSA key part) or RFC 4253 public key format, respectively. Also accepted is the path to a file containing the public key in PEM, DER or SSH encoding. Both absolute paths or paths relative to <i>/etc/ipsec.d/certs</i> are accepted.</p>
<dt><code>leftsendcert</code> = never | no | <code>ifasked</code> | always | yes</p>
<dd>Accepted values are <code>never</code> or <code>no</code>, <code>always</code> or <code>yes</code>, and <code>ifasked</code> (the default), the latter meaning that the peer must send a certificate request payload in order to get a certificate in return.</p>
<dt><code>leftsourceip</code> = %config4 | %config6 | &lt;ip address&gt;</p>
<dd>Comma separated list of internal source IPs to use in a tunnel, also known as virtual IP. If the value is one of the synonyms <code>%config</code>, <code>%cfg</code>, <code>%modeconfig</code>, or <code>%modecfg</code>, an address (from the tunnel address family) is requested from the peer. With <code>%config4</code> and <code>%config6</code> an address of the given address family will be requested explicitly. If an IP address is configured, it will be requested from the responder, which is free to respond with a different address.</p>
<dt><code>rightsourceip</code> = %config | &lt;network&gt;/&lt;netmask&gt; | &lt;from&gt;-&lt;to&gt; | %poolname</p>
<dd>Comma separated list of internal source IPs to use in a tunnel for the remote peer. If the value is <code>%config</code> on the responder side, the initiator must propose an address which is then echoed back. Also supported are address pools expressed as <i>network</i><code>/</code><i>netmask</i> and <i>from</i><code>&#8211;</code><i>to</i> or the use of an external IP address pool using %<i>poolname</i>, where <i>poolname</i> is the name of the IP address pool used for the lookup.</p>
<dt><code>leftsubnet</code> = &lt;ip subnet&gt;[[&lt;proto/port&gt;]][,&#8230;]</p>
<dd>private subnet behind the left participant, expressed as <i>network</i><code>/</code><i>netmask</i>; if omitted, essentially assumed to be <i>left</i><code>/32</code>, signifying that the left end of the connection goes to the left participant only. Configured subnets of the peers may differ, the protocol narrows it to the greatest common subnet. In IKEv1, this may lead to problems with other implementations, make sure to configure identical subnets in such configurations. IKEv2 supports multiple subnets separated by commas. IKEv1 only interprets the first subnet of such a definition, unless the Cisco Unity extension plugin is enabled. This is due to a limitation of the IKEv1 protocol, which only allows a single pair of subnets per CHILD_SA. So to tunnel several subnets a conn entry has to be defined and brought up for each pair of subnets. </p>
<p> The optional part after each subnet enclosed in square brackets specifies a protocol/port to restrict the selector for that subnet. </p>
<p> Examples: <code>leftsubnet=10.0.0.1[tcp/http],10.0.0.2[6/80]</code> or <code>leftsubnet=fec1::1[udp],10.0.0.0/16[/53]</code>. Instead of omitting either value <code>%any</code> can be used to the same effect, e.g. <code>leftsubnet=fec1::1[udp/%any],10.0.0.0/16[%any/53]</code>. </p>
<p> If the protocol is <code>icmp</code> or <code>ipv6-icmp</code> the port is interpreted as ICMP message type if it is less than 256 or as type and code if it is greater or equal to 256, with the type in the most significant 8 bits and the code in the least significant 8 bits. </p>
<p> The port value can alternatively take the value <code>%opaque</code> for RFC 4301 OPAQUE selectors, or a numerical range in the form <code>1024-65535</code>. None of the kernel backends currently supports opaque or port ranges and uses <code>%any</code> for policy installation instead. </p>
<p> Instead of specifying a subnet, <code>%dynamic</code> can be used to replace it with the IKE address, having the same effect as omitting <code>leftsubnet</code> completely. Using <code>%dynamic</code> can be used to define multiple dynamic selectors, each having a potentially different protocol/port definition. </p>
<dt><code>leftupdown</code> = &lt;path&gt;</p>
<dd>what &#8220;updown&#8221; script to run to adjust routing and/or firewalling when the status of the connection changes (default <code>ipsec _updown</code>). May include positional parameters separated by white space (although this requires enclosing the whole string in quotes); including shell metacharacters is unwise. Relevant only locally, other end need not agree on it. Charon uses the updown script to insert firewall rules only, since routing has been implemented directly into the daemon.</p>
<dt><code>lifebytes</code> = &lt;number&gt;</p>
<dd>the number of bytes transmitted over an IPsec SA before it expires.</p>
<dt><code>lifepackets</code> = &lt;number&gt;</p>
<dd>the number of packets transmitted over an IPsec SA before it expires.</p>
<dt><code>lifetime</code> = <code>1h</code> | &lt;time&gt;</p>
<dd>how long a particular instance of a connection (a set of encryption/authentication keys for user packets) should last, from successful negotiation to expiry; acceptable values are an integer optionally followed by <code>s</code> (a time in seconds) or a decimal number followed by <code>m</code>, <code>h</code>, or <code>d</code> (a time in minutes, hours, or days respectively) (default <code>1h</code>, maximum <code>24h</code>). Normally, the connection is renegotiated (via the keying channel) before it expires (see <code>margintime</code>). The two ends need not exactly agree on <code>lifetime</code>, although if they do not, there will be some clutter of superseded connections on the end which thinks the lifetime is longer. Also see EXPIRY/REKEY below.</p>
<dt><code>marginbytes</code> = &lt;number&gt;</p>
<dd>how many bytes before IPsec SA expiry (see <code>lifebytes</code>) should attempts to negotiate a replacement begin.</p>
<dt><code>marginpackets</code> = &lt;number&gt;</p>
<dd>how many packets before IPsec SA expiry (see <code>lifepackets</code>) should attempts to negotiate a replacement begin.</p>
<dt><code>margintime</code> = <code>9m</code> | &lt;time&gt;</p>
<dd>how long before connection expiry or keying-channel expiry should attempts to negotiate a replacement begin; acceptable values as for <code>lifetime</code> (default <code>9m</code>). Relevant only locally, other end need not agree on it. Also see EXPIRY/REKEY below.</p>
<dt><code>mark</code> = &lt;value&gt;[/&lt;mask&gt;]</p>
<dd>sets an XFRM mark in the inbound and outbound IPsec SAs and policies. If the mask is missing then a default mask of <code>0xffffffff</code> is assumed. The special value <code>%unique</code> assigns a unique value to each newly created IPsec SA.</p>
<dt><code>mark_in</code> = &lt;value&gt;[/&lt;mask&gt;]</p>
<dd>sets an XFRM mark in the inbound IPsec SA and policy. If the mask is missing then a default mask of <code>0xffffffff</code> is assumed.</p>
<dt><code>mark_out</code> = &lt;value&gt;[/&lt;mask&gt;]</p>
<dd>sets an XFRM mark in the outbound IPsec SA and policy. If the mask is missing then a default mask of <code>0xffffffff</code> is assumed.</p>
<dt><code>mobike</code> = <code>yes</code> | no</p>
<dd>enables the IKEv2 MOBIKE protocol defined by RFC 4555. Accepted values are <code>yes</code> (the default) and <code>no</code>. If set to <code>no</code>, the charon daemon will not actively propose MOBIKE as initiator and ignore the MOBIKE_SUPPORTED notify as responder.</p>
<dt><code>modeconfig</code> = push | <code>pull</code></p>
<dd>defines which mode is used to assign a virtual IP. Accepted values are <code>push</code> and <code>pull</code> (the default). Push mode is currently not supported with IKEv2. The setting must be the same on both sides.</p>
<dt><code>reauth</code> = <code>yes</code> | no</p>
<dd>whether rekeying of an IKE_SA should also reauthenticate the peer. In IKEv1, reauthentication is always done. In IKEv2, a value of <code>no</code> rekeys without uninstalling the IPsec SAs, a value of <code>yes</code> (the default) creates a new IKE_SA from scratch and tries to recreate all IPsec SAs.</p>
<dt><code>rekey</code> = <code>yes</code> | no</p>
<dd>whether a connection should be renegotiated when it is about to expire; acceptable values are <code>yes</code> (the default) and <code>no</code>. The two ends need not agree, but while a value of <code>no</code> prevents charon from requesting renegotiation, it does not prevent responding to renegotiation requested from the other end, so <code>no</code> will be largely ineffective unless both ends agree on it. Also see <code>reauth</code>.</p>
<dt><code>rekeyfuzz</code> = <code>100%</code> | &lt;percentage&gt;</p>
<dd>maximum percentage by which <code>marginbytes</code>, <code>marginpackets</code> and <code>margintime</code> should be randomly increased to randomize rekeying intervals (important for hosts with many connections); acceptable values are an integer, which may exceed 100, followed by a `%&#8217; (defaults to <code>100%</code>). The value of <code>marginTYPE</code>, after this random increase, must not exceed <code>lifeTYPE</code> (where TYPE is one of <i>bytes</i>, <i>packets</i> or <i>time</i>). The value <code>0%</code> will suppress randomization. Relevant only locally, other end need not agree on it. Also see EXPIRY/REKEY below.</p>
<dt><code>rekeymargin</code></p>
<dd>synonym for <code>margintime</code>.</p>
<dt><code>replay_window</code> = <code>-1</code> | &lt;number&gt;</p>
<dd>The IPsec replay window size for this connection. With the default of -1 the value configured with <i>charon.replay_window</i> in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5) is used. Larger values than 32 are supported using the Netlink backend only, a value of 0 disables IPsec replay protection.</p>
<dt><code>reqid</code> = &lt;number&gt;</p>
<dd>sets the reqid for a given connection to a pre-configured fixed value.</p>
<dt><code>sha256_96</code> = <code>no</code> | yes</p>
<dd>HMAC-SHA-256 is used with 128-bit truncation with IPsec. For compatibility with implementations that incorrectly use 96-bit truncation this option may be enabled to configure the shorter truncation length in the kernel. This is not negotiated, so this only works with peers that use the incorrect truncation length (or have this option enabled).</p>
<dt><code>tfc</code> = &lt;value&gt;</p>
<dd>number of bytes to pad ESP payload data to. Traffic Flow Confidentiality is currently supported in IKEv2 and applies to outgoing packets only. The special value <code>%mtu</code> fills up ESP packets with padding to have the size of the MTU.</p>
<dt><code>type</code> = <code>tunnel</code> | transport | transport_proxy | passthrough | drop</p>
<dd>the type of the connection; currently the accepted values are <code>tunnel</code> (the default) signifying a host-to-host, host-to-subnet, or subnet-to-subnet tunnel; <code>transport</code>, signifying host-to-host transport mode; <code>transport_proxy</code>, signifying the special Mobile IPv6 transport proxy mode; <code>passthrough</code>, signifying that no IPsec processing should be done at all; <code>drop</code>, signifying that packets should be discarded.</p>
<dt><code>xauth</code> = <code>client</code> | server</p>
<dd>specifies the role in the XAuth protocol if activated by <code>authby=xauthpsk</code> or <code>authby=xauthrsasig.</code> Accepted values are <code>server</code> and <code>client</code> (the default).</p>
<dt><code>xauth_identity</code> = &lt;id&gt;</p>
<dd>defines the identity/username the client uses to reply to an XAuth request. If not defined, the IKEv1 identity will be used as XAuth identity. </p>
</dl>
<h3>CONN PARAMETERS: IKEv2 MEDIATION EXTENSION</h3>
<p>The following parameters are relevant to IKEv2 Mediation Extension operation only.</p>
<dl>
<dt><code>mediation</code> = yes | <code>no</code></p>
<dd>whether this connection is a mediation connection, ie. whether this connection is used to mediate other connections. Mediation connections create no child SA. Acceptable values are <code>no</code> (the default) and <code>yes</code>.</p>
<dt><code>mediated_by</code> = &lt;name&gt;</p>
<dd>the name of the connection to mediate this connection through. If given, the connection will be mediated through the named mediation connection. The mediation connection must set <code>mediation=yes</code>.</p>
<dt><code>me_peerid</code> = &lt;id&gt;</p>
<dd>ID as which the peer is known to the mediation server, ie. which the other end of this connection uses as its <code>leftid</code> on its connection to the mediation server. This is the ID we request the mediation server to mediate us with. If <code>me_peerid</code> is not given, the <code>rightid</code> of this connection will be used as peer ID. </p>
</dl>
<h2>Ca Sections</h2>
<p>These are optional sections that can be used to assign special parameters to a Certification Authority (CA). Because the daemons automatically import CA certificates from <i>/etc/ipsec.d/cacerts</i>, there is no need to explicitly add them with a CA section, unless you want to assign special parameters (like a CRL) to a CA.</p>
<dl>
<dt><code>also</code> = &lt;name&gt;</p>
<dd>includes ca section <code>&lt;name&gt;</code>.</p>
<dt><code>auto</code> = <code>ignore</code> | add</p>
<dd>currently can have either the value <code>ignore</code> (the default) or <code>add</code>.</p>
<dt><code>cacert</code> = &lt;path&gt;</p>
<dd>defines a path to the CA certificate either relative to <i>/etc/ipsec.d/cacerts</i> or as an absolute path.<br />
 A value in the form <code>%smartcard[&lt;slot nr&gt;[@&lt;module&gt;]]:&lt;keyid&gt;</code> defines a specific CA certificate to load from a PKCS#11 backend for this CA. See <a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a>(5) for details about smartcard definitions.</p>
<dt><code>crluri</code> = &lt;uri&gt;</p>
<dd>defines a CRL distribution point (ldap, http, or file URI)</p>
<dt><code>crluri1</code></p>
<dd>synonym for <code>crluri.</code></p>
<dt><code>crluri2</code> = &lt;uri&gt;</p>
<dd>defines an alternative CRL distribution point (ldap, http, or file URI)</p>
<dt>
<dt><code>ocspuri</code> = &lt;uri&gt;</p>
<dd>
<dd>defines an OCSP URI.</p>
<dt><code>ocspuri1</code></p>
<dd>synonym for <code>ocspuri.</code></p>
<dt><code>ocspuri2</code> = &lt;uri&gt;</p>
<dd>defines an alternative OCSP URI.</p>
<dt><code>certuribase</code> = &lt;uri&gt;</p>
<dd>defines the base URI for the Hash and URL feature supported by IKEv2. Instead of exchanging complete certificates, IKEv2 allows one to send an URI that resolves to the DER encoded certificate. The certificate URIs are built by appending the SHA1 hash of the DER encoded certificates to this base URI.</dl>
<h2>Config Sections</h2>
<p>At present, the only <code>config</code> section known to the IPsec software is the one named <code>setup</code>, which contains information used when the software is being started. The currently-accepted <i>parameter</i> names in a <code>config</code> <code>setup</code> section are:</p>
<dl>
<dt><code>cachecrls</code> = yes | <code>no</code></p>
<dd>if enabled, certificate revocation lists (CRLs) fetched via HTTP or LDAP will be cached in <i>/etc/ipsec.d/crls/</i> under a unique file name derived from the certification authority&#8217;s public key.</p>
<dt><code>charondebug</code> = &lt;debug list&gt;</p>
<dd>how much charon debugging output should be logged. A comma separated list containing type/level-pairs may be specified, e.g: <code>dmn 3, ike 1, net -1.</code> Acceptable values for types are <code>dmn, mgr, ike, chd, job, cfg, knl, net, asn, enc, lib, esp, tls,</code> <code>tnc, imc, imv, pts</code> and the level is one of <code>-1, 0, 1, 2, 3, 4</code> (for silent, audit, control, controlmore, raw, private). By default, the level is set to <code>1</code> for all types. For more flexibility see LOGGER CONFIGURATION in <i><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></i>(5).</p>
<dt><code>strictcrlpolicy</code> = yes | ifuri | <code>no</code></p>
<dd>defines if a fresh CRL must be available in order for the peer authentication based on RSA signatures to succeed. IKEv2 additionally recognizes <code>ifuri</code> which reverts to <code>yes</code> if at least one CRL URI is defined and to <code>no</code> if no URI is known.</p>
<dt><code>uniqueids</code> = <code>yes</code> | no | never | replace | keep</p>
<dd>whether a particular participant ID should be kept unique, with any new IKE_SA using an ID deemed to replace all old ones using that ID; acceptable values are <code>yes</code> (the default), <code>no</code> and <code>never</code>. Participant IDs normally <i>are</i> unique, so a new IKE_SA using the same ID is almost invariably intended to replace an old one. The difference between <code>no</code> and <code>never</code> is that the daemon will replace old IKE_SAs when receiving an INITIAL_CONTACT notify if the option is <code>no</code> but will ignore these notifies if <code>never</code> is configured. The daemon also accepts the value <code>replace</code> which is identical to <code>yes</code> and the value <code>keep</code> to reject new IKE_SA setups and keep the duplicate established earlier. </p>
</dl>
<h2>Identity Parsing</h2>
<p>The type and binary encoding of identity strings specified in <i>leftid</i> are detected as follows:</p>
<dl>
<dt>&bull;</p>
<dd>If the string value contains an equal sign (=) it is assumed to be a Distinguished Name, with RDNs separated by commas (,) <i>or</i> slashes (/ &#8211; the string must start with a slash to use this syntax). An attempt is made to create a binary ASN.1 encoding from this string. If that fails the type is set to KEY_ID with the literal string value adopted as encoding.</p>
<dt>&bull;</p>
<dd>If the string value contains an @ the type depends on the position of that character:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the string begins with @# the type is set to KEY_ID and the string following that prefix is assumed to be the hex-encoded binary value of the identity.</p>
<dt>&bull;</p>
<dd>If the string begins with @@ the type is set to USER_FQDN and the encoding is the literal string after that prefix.</p>
<dt>&bull;</p>
<dd>If the string begins with @ the type is set to FQDN and the encoding is the literal string after that prefix.</p>
<dt>&bull;</p>
<dd>All remaining strings containing an @ are assumed to be of type USER_FQDN/RFC822 with the literal string value as encoding.</dl>
</dl>
<dt>&bull;</p>
<dd>If the value does not contain any @ or = characters it is parsed as follows:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>If the value is an empty string, or equals %any[6], 0.0.0.0, ::, or * the type is set to ID_ANY, which matches any other identity.</p>
<dt>&bull;</p>
<dd>If the value contains a colon (:) it is assumed to be an IPv6 address. But if parsing the address and converting it to its binary encoding fails the type is set to KEY_ID and the encoding is the literal value.</p>
<dt>&bull;</p>
<dd>For all other strings an attempt at parsing them as IPv4 addresses is made. If that fails the type is set to FQDN and the literal value is adopted as encoding (this is where domain names and simple names end up).</dl>
</dl>
</dl>
<h2>Sa Expiry/Rekey</h2>
<p>The IKE SAs and IPsec SAs negotiated by the daemon can be configured to expire after a specific amount of time. For IPsec SAs this can also happen after a specified number of transmitted packets or transmitted bytes. The following settings can be used to configure this: </p>
<table>
<tr VALIGN=top>
<td>Setting</td>
<td ALIGN=right>Default</td>
<td>Setting</td>
<td ALIGN=right>Default
</td>
</tr>
<tr VALIGN=top>
<td>IKE SA</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2><code>ikelifetime</code></td>
<td><code>3h</code></td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=right></td>
<td>lifepackets</td>
<td ALIGN=right>&#8211;
</td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=right></td>
<td>lifetime</td>
<td ALIGN=right>1h
</td>
</tr>
</table>
<h3>Rekeying</h3>
<p>IKE SAs as well as IPsec SAs can be rekeyed before they expire. This can be configured using the following settings: </p>
<table>
<tr VALIGN=top>
<td>Setting</td>
<td ALIGN=right>Default</td>
<td>Setting</td>
<td ALIGN=right>Default
</td>
</tr>
<tr VALIGN=top>
<td>IKE and IPsec SA</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2><code>margintime</code></td>
<td><code>9m</code></td>
</tr>
<tr VALIGN=top>
<td></td>
<td ALIGN=right></td>
<td>marginpackets</td>
<td ALIGN=right>&#8211;
</td>
</tr>
</table>
<h3>Randomization</h3>
<p>To avoid collisions the specified margins are increased randomly before subtracting them from the expiration limits (see formula below). This is controlled by the <code>rekeyfuzz</code> setting: </p>
<table>
<tr VALIGN=top>
<td>Setting</td>
<td ALIGN=right>Default
</td>
</tr>
<tr VALIGN=top>
<td>IKE and IPsec SA</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2><code>rekeyfuzz</code>
</td>
</tr>
</table>
<p> Randomization can be disabled by setting <code>rekeyfuzz</code> to <code>0%</code>.</p>
<h3>Formula</h3>
<p>The following formula is used to calculate the rekey time of IPsec SAs: </p>
<p>&nbsp;<wbr>rekeytime&nbsp;<wbr>=&nbsp;<wbr>lifetime &#8211;&nbsp;<wbr>(margintime&nbsp;<wbr>+&nbsp;<wbr>random(0, margintime&nbsp;<wbr>*&nbsp;<wbr>rekeyfuzz)) </p>
<p> It applies equally to IKE SAs and byte and packet limits for IPsec SAs.</p>
<h3>Example</h3>
<p>Let&#8217;s consider the default configuration: </p>
<p> lifetime = 1h<br />
 <tt>&nbsp;<wbr></tt>margintime = 9m<br />
 <tt>&nbsp;<wbr></tt>rekeyfuzz = 100%</p>
<p> From the formula above follows that the rekey time lies between: </p>
<p> rekeytime_min = 1h &#8211; (9m + 9m) = 42m<br />
 <tt>&nbsp;<wbr></tt>rekeytime_max = 1h &#8211; (9m + 0m) = 51m</p>
<p> Thus, the daemon will attempt to rekey the IPsec SA at a random time between 42 and 51 minutes after establishing the SA. Or, in other words, between 9 and 18 minutes before the SA expires.</p>
<h3>Notes</h3>
<dl>
<dt>&bull;</p>
<dd>Since the rekeying of an SA needs some time, the margin values must not be too low.</p>
<dt>&bull;</p>
<dd>The value <code>margin&#8230; + margin&#8230; * rekeyfuzz</code> must not exceed the original limit. For example, specifying <code>margintime = 30m</code> in the default configuration is a bad idea as there is a chance that the rekey time equals zero and, thus, rekeying gets disabled. </p>
</dl>
<h2>Files</h2>
<pre>/etc/ipsec.conf
/etc/ipsec.d/aacerts
/etc/ipsec.d/acerts
/etc/ipsec.d/cacerts
/etc/ipsec.d/certs
/etc/ipsec.d/crls</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a>(5), <a href="/docs/linux/man/5-ipsec-secrets/">ipsec.secrets</a>(5), <a href="/docs/linux/man/8-ipsec/">ipsec</a>(8)</p>
<h2>History</h2>
<p>Originally written for the FreeS/WAN project by Henry Spencer. Updated and extended for the strongSwan project &lt;<a rel="nofollow" href="http://www.strongswan.org">http://www.strongswan.org</a>&gt; by Tobias Brunner, Andreas Steffen and Martin Willi.</p>
