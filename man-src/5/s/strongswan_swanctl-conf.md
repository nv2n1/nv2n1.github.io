---
title: "strongswan_swanctl-conf(5)"
name: "strongswan_swanctl-conf"
section: "5"
letter: "s"
url: "/docs/linux/man/5-strongswan_swanctl-conf/"
description: "swanctl.conf – swanctl configuration file"
---

<p>swanctl.conf &#8211; swanctl configuration file</p>
<h2>Description</h2>
<p>swanctl.conf is the configuration file used by the <code><a href="/docs/linux/man/8-swanctl/">swanctl</a></code>(8) tool to load configurations and credentials into the strongSwan IKE daemon. For a description of the basic file syntax, including how to split the configuration in multiple files by including other files, refer to <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<h2>Time Formats</h2>
<p>For all options that define a time, the time is specified in seconds. The <i>s</i>, <i>m</i>, <i>h</i> and <i>d</i> suffixes explicitly define the units for seconds, minutes, hours and days, respectively.</p>
<h2>Settings</h2>
<p>The following settings can be used to configure connections, credentials and pools.</p>
<dl>
<dt><code>connections</code></p>
<dd>Section defining IKE connection configurations. </p>
<p> The connections section defines IKE connection configurations, each in its own subsections. In the keyword description below, the connection is named <i>&lt;conn&gt;</i>, but an arbitrary yet unique connection name can be chosen for each connection subsection. </p>
<dt><code>connections.&lt;conn&gt;</code></p>
<dd>Section for an IKE connection named &lt;conn&gt;. </p>
<dt><code>connections.&lt;conn&gt;.version</code> [0]</p>
<dd>IKE major version to use for connection. <i>1</i> uses IKEv1 aka ISAKMP, <i>2</i> uses IKEv2. A connection using the default of <i>0</i> accepts both IKEv1 and IKEv2 as responder, and initiates the connection actively with IKEv2. </p>
<dt><code>connections.&lt;conn&gt;.local_addrs</code> [%any]</p>
<dd>Local address(es) to use for IKE communication, comma separated. Takes single IPv4/IPv6 addresses, DNS names, CIDR subnets or IP address ranges. </p>
<p> As initiator, the first non-range/non-subnet is used to initiate the connection from. As responder, the local destination address must match at least to one of the specified addresses, subnets or ranges. </p>
<p> If FQDNs are assigned they are resolved every time a configuration lookup is done. If DNS resolution times out, the lookup is delayed for that time. </p>
<dt><code>connections.&lt;conn&gt;.remote_addrs</code> [%any]</p>
<dd>Remote address(es) to use for IKE communication, comma separated. Takes single IPv4/IPv6 addresses, DNS names, CIDR subnets or IP address ranges. </p>
<p> As initiator, the first non-range/non-subnet is used to initiate the connection to. As responder, the initiator source address must match at least to one of the specified addresses, subnets or ranges. </p>
<p> If FQDNs are assigned they are resolved every time a configuration lookup is done. If DNS resolution times out, the lookup is delayed for that time. </p>
<p> To initiate a connection, at least one specific address or DNS name must be specified. </p>
<dt><code>connections.&lt;conn&gt;.local_port</code> [500]</p>
<dd>Local UDP port for IKE communication. By default the port of the socket backend is used, which is usually <i>500</i>. If port <i>500</i> is used, automatic IKE port floating to port 4500 is used to work around NAT issues. </p>
<p> Using a non-default local IKE port requires support from the socket backend in use (socket-dynamic). </p>
<dt><code>connections.&lt;conn&gt;.remote_port</code> [500]</p>
<dd>Remote UDP port for IKE communication. If the default of port <i>500</i> is used, automatic IKE port floating to port 4500 is used to work around NAT issues. </p>
<dt><code>connections.&lt;conn&gt;.proposals</code> [default]</p>
<dd>A proposal is a set of algorithms. For non-AEAD algorithms, this includes for IKE an encryption algorithm, an integrity algorithm, a pseudo random function and a Diffie-Hellman group. For AEAD algorithms, instead of encryption and integrity algorithms, a combined algorithm is used. </p>
<p> In IKEv2, multiple algorithms of the same kind can be specified in a single proposal, from which one gets selected. In IKEv1, only one algorithm per kind is allowed per proposal, more algorithms get implicitly stripped. Use multiple proposals to offer different algorithms combinations in IKEv1. </p>
<p> Algorithm keywords get separated using dashes. Multiple proposals may be separated by commas. The special value <i>default</i> forms a default proposal of supported algorithms considered safe, and is usually a good choice for interoperability. </p>
<dt><code>connections.&lt;conn&gt;.vips</code> []</p>
<dd>Comma separated list of virtual IPs to request in IKEv2 configuration payloads or IKEv1 Mode Config. The wildcard addresses <i>0.0.0.0</i> and <i>::</i> request an arbitrary address, specific addresses may be defined. The responder may return a different address, though, or none at all. </p>
<dt><code>connections.&lt;conn&gt;.aggressive</code> [no]</p>
<dd>Enables Aggressive Mode instead of Main Mode with Identity Protection. Aggressive Mode is considered less secure, because the ID and HASH payloads are exchanged unprotected. This allows a passive attacker to snoop peer identities, and even worse, start dictionary attacks on the Preshared Key. </p>
<dt><code>connections.&lt;conn&gt;.pull</code> [yes]</p>
<dd>If the default of <i>yes</i> is used, Mode Config works in pull mode, where the initiator actively requests a virtual IP. With <i>no</i>, push mode is used, where the responder pushes down a virtual IP to the initiating peer. </p>
<p> Push mode is currently supported for IKEv1, but not in IKEv2. It is used by a few implementations only, pull mode is recommended. </p>
<dt><code>connections.&lt;conn&gt;.dscp</code> [000000]</p>
<dd>Differentiated Services Field Codepoint to set on outgoing IKE packets for this connection. The value is a six digit binary encoded string specifying the Codepoint to set, as defined in RFC 2474. </p>
<dt><code>connections.&lt;conn&gt;.encap</code> [no]</p>
<dd>To enforce UDP encapsulation of ESP packets, the IKE daemon can fake the NAT detection payloads. This makes the peer believe that NAT takes place on the path, forcing it to encapsulate ESP packets in UDP. </p>
<p> Usually this is not required, but it can help to work around connectivity issues with too restrictive intermediary firewalls. </p>
<dt><code>connections.&lt;conn&gt;.mobike</code> [yes]</p>
<dd>Enables MOBIKE on IKEv2 connections. MOBIKE is enabled by default on IKEv2 connections, and allows mobility of clients and multi-homing on servers by migrating active IPsec tunnels. </p>
<p> Usually keeping MOBIKE enabled is unproblematic, as it is not used if the peer does not indicate support for it. However, due to the design of MOBIKE, IKEv2 always floats to port 4500 starting from the second exchange. Some implementations don&#8217;t like this behavior, hence it can be disabled. </p>
<dt><code>connections.&lt;conn&gt;.dpd_delay</code> [0s]</p>
<dd>Interval to check the liveness of a peer actively using IKEv2 INFORMATIONAL exchanges or IKEv1 R_U_THERE messages. Active DPD checking is only enforced if no IKE or ESP/AH packet has been received for the configured DPD delay. </p>
<dt><code>connections.&lt;conn&gt;.dpd_timeout</code> [0s]</p>
<dd>Charon by default uses the normal retransmission mechanism and timeouts to check the liveness of a peer, as all messages are used for liveness checking. For compatibility reasons, with IKEv1 a custom interval may be specified; this option has no effect on connections using IKE2. </p>
<dt><code>connections.&lt;conn&gt;.fragmentation</code> [yes]</p>
<dd>Use IKE fragmentation (proprietary IKEv1 extension or RFC 7383 IKEv2 fragmentation). Acceptable values are <i>yes</i> (the default), <i>accept</i>, <i>force</i> and <i>no</i>. If set to <i>yes</i>, and the peer supports it, oversized IKE messages will be sent in fragments. If set to <i>accept</i>, support for fragmentation is announced to the peer but the daemon does not send its own messages in fragments. If set to <i>force</i> (only supported for IKEv1) the initial IKE message will already be fragmented if required. Finally, setting the option to <i>no</i> will disable announcing support for this feature. </p>
<p> Note that fragmented IKE messages sent by a peer are always accepted irrespective of the value of this option (even when set to <i>no</i>). </p>
<dt><code>connections.&lt;conn&gt;.send_certreq</code> [yes]</p>
<dd>Send certificate request payloads to offer trusted root CA certificates to the peer. Certificate requests help the peer to choose an appropriate certificate/private key for authentication and are enabled by default. </p>
<p> Disabling certificate requests can be useful if too many trusted root CA certificates are installed, as each certificate request increases the size of the initial IKE packets. </p>
<dt><code>connections.&lt;conn&gt;.send_cert</code> [ifasked]</p>
<dd>Send certificate payloads when using certificate authentication. With the default of <i>ifasked</i> the daemon sends certificate payloads only if certificate requests have been received. <i>never</i> disables sending of certificate payloads altogether, <i>always</i> causes certificate payloads to be sent unconditionally whenever certificate authentication is used. </p>
<dt><code>connections.&lt;conn&gt;.keyingtries</code> [1]</p>
<dd>Number of retransmission sequences to perform during initial connect. Instead of giving up initiation after the first retransmission sequence with the default value of <i>1</i>, additional sequences may be started according to the configured value. A value of <i>0</i> initiates a new sequence until the connection establishes or fails with a permanent error. </p>
<dt><code>connections.&lt;conn&gt;.unique</code> [no]</p>
<dd>Connection uniqueness policy to enforce. To avoid multiple connections from the same user, a uniqueness policy can be enforced. The value <i>never</i> does never enforce such a policy, even if a peer included INITIAL_CONTACT notification messages, whereas <i>no</i> replaces existing connections for the same identity if a new one has the INITIAL_CONTACT notify. <i>keep</i> rejects new connection attempts if the same user already has an active connection, <i>replace</i> deletes any existing connection if a new one for the same user gets established. </p>
<p> To compare connections for uniqueness, the remote IKE identity is used. If EAP or XAuth authentication is involved, the EAP-Identity or XAuth username is used to enforce the uniqueness policy instead. </p>
<p> On initiators this setting specifies whether an INITIAL_CONTACT notify is sent during IKE_AUTH if no existing connection is found with the remote peer (determined by the identities of the first authentication round). Only if set to <i>keep</i> or <i>replace</i> will the client send a notify. </p>
<dt><code>connections.&lt;conn&gt;.reauth_time</code> [0s]</p>
<dd>Time to schedule IKE reauthentication. IKE reauthentication recreates the IKE/ISAKMP SA from scratch and re-evaluates the credentials. In asymmetric configurations (with EAP or configuration payloads) it might not be possible to actively reauthenticate as responder. The IKEv2 reauthentication lifetime negotiation can instruct the client to perform reauthentication. </p>
<p> Reauthentication is disabled by default. Enabling it usually may lead to small connection interruptions, as strongSwan uses a break-before-make policy with IKEv2 to avoid any conflicts with associated tunnel resources. </p>
<dt><code>connections.&lt;conn&gt;.rekey_time</code> [4h]</p>
<dd>IKE rekeying refreshes key material using a Diffie-Hellman exchange, but does not re-check associated credentials. It is supported in IKEv2 only, IKEv1 performs a reauthentication procedure instead. </p>
<p> With the default value IKE rekeying is scheduled every 4 hours, minus the configured <code>rand_time</code>. If a <code>reauth_time</code> is configured, <code>rekey_time</code> defaults to zero disabling rekeying; explicitly set both to enforce rekeying and reauthentication. </p>
<dt><code>connections.&lt;conn&gt;.over_time</code> [10% of rekey_time/reauth_time]</p>
<dd>Hard IKE_SA lifetime if rekey/reauth does not complete, as time. To avoid having an IKE/ISAKMP kept alive if IKE reauthentication or rekeying fails perpetually, a maximum hard lifetime may be specified. If the IKE_SA fails to rekey or reauthenticate within the specified time, the IKE_SA gets closed. </p>
<p> In contrast to CHILD_SA rekeying, <code>over_time</code> is relative in time to the <code>rekey_time</code> <i>and</i> <code>reauth_time</code> values, as it applies to both. </p>
<p> The default is 10% of the longer of <code>rekey_time</code> and <code>reauth_time</code>. </p>
<dt><code>connections.&lt;conn&gt;.rand_time</code> [over_time]</p>
<dd>Time range from which to choose a random value to subtract from rekey/reauth times. To avoid having both peers initiating the rekey/reauth procedure simultaneously, a random time gets subtracted from the rekey/reauth times. </p>
<p> The default is equal to the configured <code>over_time</code>. </p>
<dt><code>connections.&lt;conn&gt;.pools</code> []</p>
<dd>Comma separated list of named IP pools to allocate virtual IP addresses and other configuration attributes from. Each name references a pool by name from either the <code>pools</code> section or an external pool. </p>
<dt><code>connections.&lt;conn&gt;.mediation</code> [no]</p>
<dd>Whether this connection is a mediation connection, that is, whether this connection is used to mediate other connections using the IKEv2 Mediation Extension. Mediation connections create no CHILD_SA. </p>
<dt><code>connections.&lt;conn&gt;.mediated_by</code> []</p>
<dd>The name of the connection to mediate this connection through. If given, the connection will be mediated through the named mediation connection. The mediation connection must have <code>mediation</code> enabled. </p>
<dt><code>connections.&lt;conn&gt;.mediation_peer</code> []</p>
<dd>Identity under which the peer is registered at the mediation server, that is, the IKE identity the other end of this connection uses as its local identity on its connection to the mediation server. This is the identity we request the mediation server to mediate us with. Only relevant on connections that set <code>mediated_by</code>. If it is not given, the remote IKE identity of the first authentication round of this connection will be used. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;</code></p>
<dd>Section for a local authentication round. A local authentication round defines the rules how authentication is performed for the local peer. Multiple rounds may be defined to use IKEv2 RFC 4739 Multiple Authentication or IKEv1 XAuth. </p>
<p> Each round is defined in a section having <i>local</i> as prefix, and an optional unique suffix. To define a single authentication round, the suffix may be omitted. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.round</code> [0]</p>
<dd>Optional numeric identifier by which authentication rounds are sorted. If not specified rounds are ordered by their position in the config file/VICI message. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.certs</code> []</p>
<dd>Comma separated list of certificate candidates to use for authentication. The certificates may use a relative path from the <code>swanctl</code> <i>x509</i> directory or an absolute path. </p>
<p> The certificate used for authentication is selected based on the received certificate request payloads. If no appropriate CA can be located, the first certificate is used. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.cert&lt;suffix&gt;</code> []</p>
<dd>Section for a certificate candidate to use for authentication. Certificates in <i>certs</i> are transmitted as binary blobs, these sections offer more flexibility. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.cert&lt;suffix&gt;.file</code> []</p>
<dd>Absolute path to the certificate to load. Passed as-is to the daemon, so it must be readable by it. </p>
<p> Configure either this or <i>handle</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.cert&lt;suffix&gt;.handle</code> []</p>
<dd>Hex-encoded CKA_ID of the certificate on a token. </p>
<p> Configure either this or <i>file</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.cert&lt;suffix&gt;.slot</code> []</p>
<dd>Optional slot number of the token that stores the certificate. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.cert&lt;suffix&gt;.module</code> []</p>
<dd>Optional PKCS#11 module name. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.pubkeys</code> []</p>
<dd>Comma separated list of raw public key candidates to use for authentication. The public keys may use a relative path from the <code>swanctl</code> <i>pubkey</i> directory or an absolute path. </p>
<p> Even though multiple local public keys could be defined in principle, only the first public key in the list is used for authentication. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.auth</code> [pubkey]</p>
<dd>Authentication to perform locally. <i>pubkey</i> uses public key authentication using a private key associated to a usable certificate. <i>psk</i> uses pre-shared key authentication. The IKEv1 specific <i>xauth</i> is used for XAuth or Hybrid authentication, while the IKEv2 specific <i>eap</i> keyword defines EAP authentication. </p>
<p> For <i>xauth</i>, a specific backend name may be appended, separated by a dash. The appropriate <i>xauth</i> backend is selected to perform the XAuth exchange. For traditional XAuth, the <i>xauth</i> method is usually defined in the second authentication round following an initial <i>pubkey</i> (or <i>psk</i>) round. Using <i>xauth</i> in the first round performs Hybrid Mode client authentication. </p>
<p> For <i>eap</i>, a specific EAP method name may be appended, separated by a dash. An EAP module implementing the appropriate method is selected to perform the EAP conversation. </p>
<p> If both peers support RFC 7427 (&quot;Signature Authentication in IKEv2&quot;) specific hash algorithms to be used during IKEv2 authentication may be configured. To do so use <i>ike:</i> followed by a trust chain signature scheme constraint (see description of the <code>remote</code> section&#8217;s <code>auth</code> keyword). For example, with <i>ike:pubkey-sha384-sha256</i> a public key signature scheme with either SHA-384 or SHA-256 would get used for authentication, in that order and depending on the hash algorithms supported by the peer. If no specific hash algorithms are configured, the default is to prefer an algorithm that matches or exceeds the strength of the signature key. If no constraints with <i>ike:</i> prefix are configured any signature scheme constraint (without <i>ike:</i> prefix) will also apply to IKEv2 authentication, unless this is disabled in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5). </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.id</code> []</p>
<dd>IKE identity to use for authentication round. When using certificate authentication, the IKE identity must be contained in the certificate, either as subject or as subjectAltName. </p>
<p> The identity can be an IP address, a fully-qualified domain name, an email address or a Distinguished Name for which the ID type is determined automatically and the string is converted to the appropriate encoding. To enforce a specific identity type, a prefix may be used, followed by a colon (:). If the number sign (#) follows the colon, the remaining data is interpreted as hex encoding, otherwise the string is used as-is as the identification data. Note that this implies that no conversion is performed for non-string identities. For example, <i>ipv4:10.0.0.1</i> does not create a valid ID_IPV4_ADDR IKE identity, as it does not get converted to binary 0x0a000001. Instead, one could use <i>ipv4:#0a000001</i> to get a valid identity, but just using the implicit type with automatic conversion is usually simpler. The same applies to the ASN1 encoded types. The following prefixes are known: <i>ipv4</i>, <i>ipv6</i>, <i>rfc822</i>, <i>email</i>, <i>userfqdn</i>, <i>fqdn</i>, <i>dns</i>, <i>asn1dn</i>, <i>asn1gn</i> and <i>keyid</i>. Custom type prefixes may be specified by surrounding the numerical type value by curly brackets. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.eap_id</code> [id]</p>
<dd>Client EAP-Identity to use in EAP-Identity exchange and the EAP method. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.aaa_id</code> [remote-id]</p>
<dd>Server side EAP-Identity to expect in the EAP method. Some EAP methods, such as EAP-TLS, use an identity for the server to perform mutual authentication. This identity may differ from the IKE identity, especially when EAP authentication is delegated from the IKE responder to an AAA backend. </p>
<p> For EAP-(T)TLS, this defines the identity for which the server must provide a certificate in the TLS exchange. </p>
<dt><code>connections.&lt;conn&gt;.local&lt;suffix&gt;.xauth_id</code> [id]</p>
<dd>Client XAuth username used in the XAuth exchange. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;</code></p>
<dd>Section for a remote authentication round. A remote authentication round defines the constraints how the peers must authenticate to use this connection. Multiple rounds may be defined to use IKEv2 RFC 4739 Multiple Authentication or IKEv1 XAuth. </p>
<p> Each round is defined in a section having <i>remote</i> as prefix, and an optional unique suffix. To define a single authentication round, the suffix may be omitted. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.round</code> [0]</p>
<dd>Optional numeric identifier by which authentication rounds are sorted. If not specified rounds are ordered by their position in the config file/VICI message. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.id</code> [%any]</p>
<dd>IKE identity to expect for authentication round. Refer to the <i>local</i> <i>id</i> section for details. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.groups</code> []</p>
<dd>Comma separated authorization group memberships to require. The peer must prove membership to at least one of the specified groups. Group membership can be certified by different means, for example by appropriate Attribute Certificates or by an AAA backend involved in the authentication. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert_policy</code> []</p>
<dd>Comma separated list of certificate policy OIDs the peer&#8217;s certificate must have. OIDs are specified using the numerical dotted representation. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.certs</code> []</p>
<dd>Comma separated list of certificates to accept for authentication. The certificates may use a relative path from the <code>swanctl</code> <i>x509</i> directory or an absolute path. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert&lt;suffix&gt;</code> []</p>
<dd>Section for a certificate to accept for authentication. Certificates in <i>certs</i> are transmitted as binary blobs, these sections offer more flexibility. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert&lt;suffix&gt;.file</code> []</p>
<dd>Absolute path to the certificate to load. Passed as-is to the daemon, so it must be readable by it. </p>
<p> Configure either this or <i>handle</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert&lt;suffix&gt;.handle</code> []</p>
<dd>Hex-encoded CKA_ID of the certificate on a token. </p>
<p> Configure either this or <i>file</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert&lt;suffix&gt;.slot</code> []</p>
<dd>Optional slot number of the token that stores the certificate. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cert&lt;suffix&gt;.module</code> []</p>
<dd>Optional PKCS#11 module name. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacerts</code> []</p>
<dd>Comma separated list of CA certificates to accept for authentication. The certificates may use a relative path from the <code>swanctl</code> <i>x509ca</i> directory or an absolute path. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacert&lt;suffix&gt;</code> []</p>
<dd>Section for a CA certificate to accept for authentication. Certificates in <i>cacerts</i> are transmitted as binary blobs, these sections offer more flexibility. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacert&lt;suffix&gt;.file</code> []</p>
<dd>Absolute path to the certificate to load. Passed as-is to the daemon, so it must be readable by it. </p>
<p> Configure either this or <i>handle</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacert&lt;suffix&gt;.handle</code> []</p>
<dd>Hex-encoded CKA_ID of the CA certificate on a token. </p>
<p> Configure either this or <i>file</i>, but not both, in one section. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacert&lt;suffix&gt;.slot</code> []</p>
<dd>Optional slot number of the token that stores the CA certificate. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.cacert&lt;suffix&gt;.module</code> []</p>
<dd>Optional PKCS#11 module name. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.pubkeys</code> []</p>
<dd>Comma separated list of raw public keys to accept for authentication. The public keys may use a relative path from the <code>swanctl</code> <i>pubkey</i> directory or an absolute path. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.revocation</code> [relaxed]</p>
<dd>Certificate revocation policy for CRL or OCSP revocation. </p>
<p> A <i>strict</i> revocation policy fails if no revocation information is available, i.e. the certificate is not known to be unrevoked. </p>
<p> <i>ifuri</i> fails only if a CRL/OCSP URI is available, but certificate revocation checking fails, i.e. there should be revocation information available, but it could not be obtained. </p>
<p> The default revocation policy <i>relaxed</i> fails only if a certificate is revoked, i.e. it is explicitly known that it is bad. </p>
<dt><code>connections.&lt;conn&gt;.remote&lt;suffix&gt;.auth</code> [pubkey]</p>
<dd>Authentication to expect from remote. See the <code>local</code> section&#8217;s <code>auth</code> keyword description about the details of supported mechanisms. </p>
<p> To require a trustchain public key strength for the remote side, specify the key type followed by the minimum strength in bits (for example <i>ecdsa-384</i> or <i>rsa-2048-ecdsa-256</i>). To limit the acceptable set of hashing algorithms for trustchain validation, append hash algorithms to <i>pubkey</i> or a key strength definition (for example <i>pubkey-sha1-sha256</i> or <i>rsa-2048-ecdsa-256-sha256-sha384-sha512</i>). Unless disabled in <code><a href="/docs/linux/man/5-strongswan-conf/">strongswan.conf</a></code>(5), or explicit IKEv2 signature constraints are configured (refer to the description of the <code>local</code> section&#8217;s <code>auth</code> keyword for details), such key types and hash algorithms are also applied as constraints against IKEv2 signature authentication schemes used by the remote side. </p>
<p> To specify trust chain constraints for EAP-(T)TLS, append a colon to the EAP method, followed by the key type/size and hash algorithm as discussed above (e.g. <i>eap-tls:ecdsa-384-sha384</i>). </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;</code></p>
<dd>CHILD_SA configuration sub-section. Each connection definition may have one or more sections in its <i>children</i> subsection. The section name defines the name of the CHILD_SA configuration, which must be unique within the connection. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.ah_proposals</code> []</p>
<dd>AH proposals to offer for the CHILD_SA. A proposal is a set of algorithms. For AH, this includes an integrity algorithm and an optional Diffie-Hellman group. If a DH group is specified, CHILD_SA/Quick Mode rekeying and initial negotiation uses a separate Diffie-Hellman exchange using the specified group (refer to <i>esp_proposals</i> for details). </p>
<p> In IKEv2, multiple algorithms of the same kind can be specified in a single proposal, from which one gets selected. In IKEv1, only one algorithm per kind is allowed per proposal, more algorithms get implicitly stripped. Use multiple proposals to offer different algorithms combinations in IKEv1. </p>
<p> Algorithm keywords get separated using dashes. Multiple proposals may be separated by commas. The special value <i>default</i> forms a default proposal of supported algorithms considered safe, and is usually a good choice for interoperability. By default no AH proposals are included, instead ESP is proposed. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.esp_proposals</code> [default]</p>
<dd>ESP proposals to offer for the CHILD_SA. A proposal is a set of algorithms. For ESP non-AEAD proposals, this includes an integrity algorithm, an encryption algorithm, an optional Diffie-Hellman group and an optional Extended Sequence Number Mode indicator. For AEAD proposals, a combined mode algorithm is used instead of the separate encryption/integrity algorithms. </p>
<p> If a DH group is specified, CHILD_SA/Quick Mode rekeying and initial negotiation use a separate Diffie-Hellman exchange using the specified group. However, for IKEv2, the keys of the CHILD_SA created implicitly with the IKE_SA will always be derived from the IKE_SA&#8217;s key material. So any DH group specified here will only apply when the CHILD_SA is later rekeyed or is created with a separate CREATE_CHILD_SA exchange. A proposal mismatch might, therefore, not immediately be noticed when the SA is established, but may later cause rekeying to fail. </p>
<p> Extended Sequence Number support may be indicated with the <i>esn</i> and <i>noesn</i> values, both may be included to indicate support for both modes. If omitted, <i>noesn</i> is assumed. </p>
<p> In IKEv2, multiple algorithms of the same kind can be specified in a single proposal, from which one gets selected. In IKEv1, only one algorithm per kind is allowed per proposal, more algorithms get implicitly stripped. Use multiple proposals to offer different algorithms combinations in IKEv1. </p>
<p> Algorithm keywords get separated using dashes. Multiple proposals may be separated by commas. The special value <i>default</i> forms a default proposal of supported algorithms considered safe, and is usually a good choice for interoperability. If no algorithms are specified for AH nor ESP, the <i>default</i> set of algorithms for ESP is included. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.sha256_96</code> [no]</p>
<dd>HMAC-SHA-256 is used with 128-bit truncation with IPsec. For compatibility with implementations that incorrectly use 96-bit truncation this option may be enabled to configure the shorter truncation length in the kernel. This is not negotiated, so this only works with peers that use the incorrect truncation length (or have this option enabled). </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.local_ts</code> [dynamic]</p>
<dd>Comma separated list of local traffic selectors to include in CHILD_SA. Each selector is a CIDR subnet definition, followed by an optional proto/port selector. The special value <i>dynamic</i> may be used instead of a subnet definition, which gets replaced by the tunnel outer address or the virtual IP, if negotiated. This is the default. </p>
<p> A protocol/port selector is surrounded by opening and closing square brackets. Between these brackets, a numeric or <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3) protocol name may be specified. After the optional protocol restriction, an optional port restriction may be specified, separated by a slash. The port restriction may be numeric, a <code><a href="/docs/linux/man/3-getservent/">getservent</a></code>(3) service name, or the special value <i>opaque</i> for RFC 4301 OPAQUE selectors. Port ranges may be specified as well, none of the kernel backends currently support port ranges, though. </p>
<p> When IKEv1 is used only the first selector is interpreted, except if the Cisco Unity extension plugin is used. This is due to a limitation of the IKEv1 protocol, which only allows a single pair of selectors per CHILD_SA. So to tunnel traffic matched by several pairs of selectors when using IKEv1 several children (CHILD_SAs) have to be defined that cover the selectors. </p>
<p> The IKE daemon uses traffic selector narrowing for IKEv1, the same way it is standardized and implemented for IKEv2. However, this may lead to problems with other implementations. To avoid that, configure identical selectors in such scenarios. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.remote_ts</code> [dynamic]</p>
<dd>Comma separated list of remote selectors to include in CHILD_SA. See <code>local_ts</code> for a description of the selector syntax. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rekey_time</code> [1h]</p>
<dd>Time to schedule CHILD_SA rekeying. CHILD_SA rekeying refreshes key material, optionally using a Diffie-Hellman exchange if a group is specified in the proposal. </p>
<p> To avoid rekey collisions initiated by both ends simultaneously, a value in the range of <code>rand_time</code> gets subtracted to form the effective soft lifetime. </p>
<p> By default CHILD_SA rekeying is scheduled every hour, minus <code>rand_time</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.life_time</code> [rekey_time + 10%]</p>
<dd>Maximum lifetime before CHILD_SA gets closed. Usually this hard lifetime is never reached, because the CHILD_SA gets rekeyed before. If that fails for whatever reason, this limit closes the CHILD_SA. </p>
<p> The default is 10% more than the <code>rekey_time</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rand_time</code> [life_time &#8211; rekey_time]</p>
<dd>Time range from which to choose a random value to subtract from <code>rekey_time</code>. The default is the difference between <code>life_time</code> and <code>rekey_time</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rekey_bytes</code> [0]</p>
<dd>Number of bytes processed before initiating CHILD_SA rekeying. CHILD_SA rekeying refreshes key material, optionally using a Diffie-Hellman exchange if a group is specified in the proposal. </p>
<p> To avoid rekey collisions initiated by both ends simultaneously, a value in the range of <code>rand_bytes</code> gets subtracted to form the effective soft volume limit. </p>
<p> Volume based CHILD_SA rekeying is disabled by default. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.life_bytes</code> [rekey_bytes + 10%]</p>
<dd>Maximum bytes processed before CHILD_SA gets closed. Usually this hard volume limit is never reached, because the CHILD_SA gets rekeyed before. If that fails for whatever reason, this limit closes the CHILD_SA. </p>
<p> The default is 10% more than <code>rekey_bytes</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rand_bytes</code> [life_bytes &#8211; rekey_bytes]</p>
<dd>Byte range from which to choose a random value to subtract from <code>rekey_bytes</code>. The default is the difference between <code>life_bytes</code> and <code>rekey_bytes</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rekey_packets</code> [0]</p>
<dd>Number of packets processed before initiating CHILD_SA rekeying. CHILD_SA rekeying refreshes key material, optionally using a Diffie-Hellman exchange if a group is specified in the proposal. </p>
<p> To avoid rekey collisions initiated by both ends simultaneously, a value in the range of <code>rand_packets</code> gets subtracted to form the effective soft packet count limit. </p>
<p> Packet count based CHILD_SA rekeying is disabled by default. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.life_packets</code> [rekey_packets + 10%]</p>
<dd>Maximum number of packets processed before CHILD_SA gets closed. Usually this hard packets limit is never reached, because the CHILD_SA gets rekeyed before. If that fails for whatever reason, this limit closes the CHILD_SA. </p>
<p> The default is 10% more than <code>rekey_bytes</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.rand_packets</code> [life_packets &#8211; rekey_packets]</p>
<dd>Packet range from which to choose a random value to subtract from <code>rekey_packets</code>. The default is the difference between <code>life_packets</code> and <code>rekey_packets</code>. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.updown</code> []</p>
<dd>Updown script to invoke on CHILD_SA up and down events. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.hostaccess</code> [yes]</p>
<dd>Hostaccess variable to pass to <code>updown</code> script. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.mode</code> [tunnel]</p>
<dd>IPsec Mode to establish CHILD_SA with. <i>tunnel</i> negotiates the CHILD_SA in IPsec Tunnel Mode, whereas <i>transport</i> uses IPsec Transport Mode. <i>transport_proxy</i> signifying the special Mobile IPv6 Transport Proxy Mode. <i>beet</i> is the Bound End to End Tunnel mixture mode, working with fixed inner addresses without the need to include them in each packet. </p>
<p> Both <i>transport</i> and <i>beet</i> modes are subject to mode negotiation; <i>tunnel</i> mode is negotiated if the preferred mode is not available. </p>
<p> <i>pass</i> and <i>drop</i> are used to install shunt policies which explicitly bypass the defined traffic from IPsec processing or drop it, respectively. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.policies</code> [yes]</p>
<dd>Whether to install IPsec policies or not. Disabling this can be useful in some scenarios e.g. MIPv6, where policies are not managed by the IKE daemon. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.policies_fwd_out</code> [no]</p>
<dd>Whether to install outbound FWD IPsec policies or not. Enabling this is required in case there is a drop policy that would match and block forwarded traffic for this CHILD_SA. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.dpd_action</code> [clear]</p>
<dd>Action to perform for this CHILD_SA on DPD timeout. The default <i>clear</i> closes the CHILD_SA and does not take further action. <i>trap</i> installs a trap policy, which will catch matching traffic and tries to re-negotiate the tunnel on-demand. <i>restart</i> immediately tries to re-negotiate the CHILD_SA under a fresh IKE_SA. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.ipcomp</code> [no]</p>
<dd>Enable IPComp compression before encryption. If enabled, IKE tries to negotiate IPComp compression to compress ESP payload data prior to encryption. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.inactivity</code> [0s]</p>
<dd>Timeout before closing CHILD_SA after inactivity. If no traffic has been processed in either direction for the configured timeout, the CHILD_SA gets closed due to inactivity. The default value of <i>0</i> disables inactivity checks. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.reqid</code> [0]</p>
<dd>Fixed reqid to use for this CHILD_SA. This might be helpful in some scenarios, but works only if each CHILD_SA configuration is instantiated not more than once. The default of <i>0</i> uses dynamic reqids, allocated incrementally. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.priority</code> [0]</p>
<dd>Optional fixed priority for IPsec policies. This could be useful to install high-priority drop policies. The default of <i>0</i> uses dynamically calculated priorities based on the size of the traffic selectors. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.interface</code> []</p>
<dd>Optional interface name to restrict IPsec policies. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.mark_in</code> [0/0x00000000]</p>
<dd>Netfilter mark and mask for input traffic. On Linux Netfilter may require marks on each packet to match an SA having that option set. This allows Netfilter rules to select specific tunnels for incoming traffic. The special value <i>%unique</i> sets a unique mark on each CHILD_SA instance. </p>
<p> An additional mask may be appended to the mark, separated by _/_. The default mask if omitted is 0xffffffff. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.mark_out</code> [0/0x00000000]</p>
<dd>Netfilter mark and mask for output traffic. On Linux Netfilter may require marks on each packet to match a policy having that option set. This allows Netfilter rules to select specific tunnels for outgoing traffic. The special value <i>%unique</i> sets a unique mark on each CHILD_SA instance. </p>
<p> An additional mask may be appended to the mark, separated by _/_. The default mask if omitted is 0xffffffff. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.tfc_padding</code> [0]</p>
<dd>Pads ESP packets with additional data to have a consistent ESP packet size for improved Traffic Flow Confidentiality. The padding defines the minimum size of all ESP packets sent. </p>
<p> The default value of 0 disables TFC padding, the special value <i>mtu</i> adds TFC padding to create a packet size equal to the Path Maximum Transfer Unit. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.replay_window</code> [32]</p>
<dd>IPsec replay window to configure for this CHILD_SA. Larger values than the default of 32 are supported using the Netlink backend only, a value of 0 disables IPsec replay protection. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.hw_offload</code> [no]</p>
<dd>Enable hardware offload for this CHILD_SA, if supported by the IPsec implementation. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.start_action</code> [none]</p>
<dd>Action to perform after loading the configuration. The default of <i>none</i> loads the connection only, which then can be manually initiated or used as a responder configuration. </p>
<p> The value <i>trap</i> installs a trap policy, which triggers the tunnel as soon as matching traffic has been detected. The value <i>start</i> initiates the connection actively. </p>
<p> When unloading or replacing a CHILD_SA configuration having a <code>start_action</code> different from <i>none</i>, the inverse action is performed. Configurations with <i>start</i> get closed, while such with <i>trap</i> get uninstalled. </p>
<dt><code>connections.&lt;conn&gt;.children.&lt;child&gt;.close_action</code> [none]</p>
<dd>Action to perform after a CHILD_SA gets closed by the peer. The default of <i>none</i> does not take any action, <i>trap</i> installs a trap policy for the CHILD_SA. <i>start</i> tries to re-create the CHILD_SA. </p>
<p> <code>close_action</code> does not provide any guarantee that the CHILD_SA is kept alive. It acts on explicit close messages only, but not on negotiation failures. Use trap policies to reliably re-create failed CHILD_SAs. </p>
<dt><code>secrets</code></p>
<dd>Section defining secrets for IKE/EAP/XAuth authentication and private key decryption. The <code>secrets</code> section takes sub-sections having a specific prefix which defines the secret type. </p>
<p> It is not recommended to define any private key decryption passphrases, as then there is no real security benefit in having encrypted keys. Either store the key unencrypted or enter the keys manually when loading credentials. </p>
<dt><code>secrets.eap&lt;suffix&gt;</code></p>
<dd>EAP secret section for a specific secret. Each EAP secret is defined in a unique section having the <i>eap</i> prefix. EAP secrets are used for XAuth authentication as well. </p>
<dt><code>secrets.eap&lt;suffix&gt;.secret</code> []</p>
<dd>Value of the EAP/XAuth secret. It may either be an ASCII string, a hex encoded string if it has a <i>0x</i> prefix or a Base64 encoded string if it has a <i>0s</i> prefix in its value. </p>
<dt><code>secrets.eap&lt;suffix&gt;.id&lt;suffix&gt;</code> []</p>
<dd>Identity the EAP/XAuth secret belongs to. Multiple unique identities may be specified, each having an <i>id</i> prefix, if a secret is shared between multiple users. </p>
<dt><code>secrets.xauth&lt;suffix&gt;</code></p>
<dd>XAuth secret section for a specific secret. <code>xauth</code> is just an alias for <code>eap</code>, secrets under both section prefixes are used for both EAP and XAuth authentication. </p>
<dt><code>secrets.ntlm&lt;suffix&gt;</code></p>
<dd>NTLM secret section for a specific secret. Each NTLM secret is defined in a unique section having the <i>ntlm</i> prefix. NTLM secrets may only be used for EAP-MSCHAPv2 authentication. </p>
<dt><code>secrets.ntlm&lt;suffix&gt;.secret</code> []</p>
<dd>Value of the NTLM secret, which is the NT Hash of the actual secret, that is, MD4(UTF-16LE(secret)). The resulting 16-byte value may either be given as a hex encoded string with a <i>0x</i> prefix or as a Base64 encoded string with a <i>0s</i> prefix. </p>
<dt><code>secrets.ntlm&lt;suffix&gt;.id&lt;suffix&gt;</code> []</p>
<dd>Identity the NTLM secret belongs to. Multiple unique identities may be specified, each having an <i>id</i> prefix, if a secret is shared between multiple users. </p>
<dt><code>secrets.ike&lt;suffix&gt;</code></p>
<dd>IKE preshared secret section for a specific secret. Each IKE PSK is defined in a unique section having the <i>ike</i> prefix. </p>
<dt><code>secrets.ike&lt;suffix&gt;.secret</code> []</p>
<dd>Value of the IKE preshared secret. It may either be an ASCII string, a hex encoded string if it has a <i>0x</i> prefix or a Base64 encoded string if it has a <i>0s</i> prefix in its value. </p>
<dt><code>secrets.ike&lt;suffix&gt;.id&lt;suffix&gt;</code> []</p>
<dd>IKE identity the IKE preshared secret belongs to. Multiple unique identities may be specified, each having an <i>id</i> prefix, if a secret is shared between multiple peers. </p>
<dt><code>secrets.private&lt;suffix&gt;</code></p>
<dd>Private key decryption passphrase for a key in the <i>private</i> folder. </p>
<dt><code>secrets.private&lt;suffix&gt;.file</code> []</p>
<dd>File name in the <i>private</i> folder for which this passphrase should be used. </p>
<dt><code>secrets.private&lt;suffix&gt;.secret</code> []</p>
<dd>Value of decryption passphrase for private key. </p>
<dt><code>secrets.rsa&lt;suffix&gt;</code></p>
<dd>Private key decryption passphrase for a key in the <i>rsa</i> folder. </p>
<dt><code>secrets.rsa&lt;suffix&gt;.file</code> []</p>
<dd>File name in the <i>rsa</i> folder for which this passphrase should be used. </p>
<dt><code>secrets.rsa&lt;suffix&gt;.secret</code> []</p>
<dd>Value of decryption passphrase for RSA key. </p>
<dt><code>secrets.ecdsa&lt;suffix&gt;</code></p>
<dd>Private key decryption passphrase for a key in the <i>ecdsa</i> folder. </p>
<dt><code>secrets.ecdsa&lt;suffix&gt;.file</code> []</p>
<dd>File name in the <i>ecdsa</i> folder for which this passphrase should be used. </p>
<dt><code>secrets.ecdsa&lt;suffix&gt;.secret</code> []</p>
<dd>Value of decryption passphrase for ECDSA key. </p>
<dt><code>secrets.pkcs8&lt;suffix&gt;</code></p>
<dd>Private key decryption passphrase for a key in the <i>pkcs8</i> folder. </p>
<dt><code>secrets.pkcs8&lt;suffix&gt;.file</code> []</p>
<dd>File name in the <i>pkcs8</i> folder for which this passphrase should be used. </p>
<dt><code>secrets.pkcs8&lt;suffix&gt;.secret</code> []</p>
<dd>Value of decryption passphrase for PKCS#8 key. </p>
<dt><code>secrets.pkcs12&lt;suffix&gt;</code></p>
<dd>PKCS#12 decryption passphrase for a container in the <i>pkcs12</i> folder. </p>
<dt><code>secrets.pkcs12&lt;suffix&gt;.file</code> []</p>
<dd>File name in the <i>pkcs12</i> folder for which this passphrase should be used. </p>
<dt><code>secrets.pkcs12&lt;suffix&gt;.secret</code> []</p>
<dd>Value of decryption passphrase for PKCS#12 container. </p>
<dt><code>secrets.token&lt;suffix&gt;</code></p>
<dd>Definition for a private key that&#8217;s stored on a token/smartcard. </p>
<dt><code>secrets.token&lt;suffix&gt;.handle</code> []</p>
<dd>Hex-encoded CKA_ID of the private key on the token. </p>
<dt><code>secrets.token&lt;suffix&gt;.slot</code> []</p>
<dd>Optional slot number to access the token. </p>
<dt><code>secrets.token&lt;suffix&gt;.module</code> []</p>
<dd>Optional PKCS#11 module name to access the token. </p>
<dt><code>secrets.token&lt;suffix&gt;.pin</code> []</p>
<dd>Optional PIN required to access the key on the token. If none is provided the user is prompted during an interactive &#8211;load-creds call. </p>
<dt><code>pools</code></p>
<dd>Section defining named pools. Named pools may be referenced by connections with the <code>pools</code> option to assign virtual IPs and other configuration attributes. </p>
<dt><code>pools.&lt;name&gt;</code></p>
<dd>Section defining a single pool with a unique name. </p>
<dt><code>pools.&lt;name&gt;.addrs</code> []</p>
<dd>Subnet or range defining addresses allocated in pool. Accepts a single CIDR subnet defining the pool to allocate addresses from or an address range (&lt;from&gt;-&lt;to&gt;). Pools must be unique and non-overlapping. </p>
<dt><code>pools.&lt;name&gt;.&lt;attr&gt;</code> []</p>
<dd>Comma separated list of additional attributes of type <code>&lt;attr&gt;</code>. The attribute type may be one of <i>dns</i>, <i>nbns</i>, <i>dhcp</i>, <i>netmask</i>, <i>server</i>, <i>subnet</i>, <i>split_include</i> and <i>split_exclude</i> to define addresses or CIDR subnets for the corresponding attribute types. Alternatively, <code>&lt;attr&gt;</code> can be a numerical identifier, for which string attribute values are accepted as well. </p>
<dt><code>authorities</code></p>
<dd>Section defining attributes of certification authorities. </p>
<dt><code>authorities.&lt;name&gt;</code></p>
<dd>Section defining a certification authority with a unique name. </p>
<dt><code>authorities.&lt;name&gt;.cacert</code> []</p>
<dd>CA certificate belonging to the certification authority. The certificates may use a relative path from the <code>swanctl</code> <i>x509ca</i> directory or an absolute path. </p>
<p> Configure one of <i>cacert</i>, <i>file</i>, or <i>handle</i> per section. </p>
<dt><code>authorities.&lt;name&gt;.file</code> []</p>
<dd>Absolute path to the certificate to load. Passed as-is to the daemon, so it must be readable by it. </p>
<p> Configure one of <i>cacert</i>, <i>file</i>, or <i>handle</i> per section. </p>
<dt><code>authorities.&lt;name&gt;.handle</code> []</p>
<dd>Hex-encoded CKA_ID of the CA certificate on a token. </p>
<p> Configure one of <i>cacert</i>, <i>file</i>, or <i>handle</i> per section. </p>
<dt><code>authorities.&lt;name&gt;.slot</code> []</p>
<dd>Optional slot number of the token that stores the CA certificate. </p>
<dt><code>authorities.&lt;name&gt;.module</code> []</p>
<dd>Optional PKCS#11 module name. </p>
<dt><code>authorities.&lt;name&gt;.crl_uris</code> []</p>
<dd>Comma-separated list of CRL distribution points (ldap, http, or file URI). </p>
<dt><code>authorities.&lt;name&gt;.ocsp_uris</code> []</p>
<dd>Comma-separated list of OCSP URIs. </p>
<dt><code>authorities.&lt;name&gt;.cert_uri_base</code> []</p>
<dd>Defines the base URI for the Hash and URL feature supported by IKEv2. Instead of exchanging complete certificates, IKEv2 allows one to send an URI that resolves to the DER encoded certificate. The certificate URIs are built by appending the SHA1 hash of the DER encoded certificates to this base URI. </p>
</dl>
<h2>Files</h2>
<pre>/etc/swanctl/swanctl.conf configuration file</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-swanctl/">swanctl</a></code>(8) </p>
