---
title: "racoon-conf(5)"
name: "racoon-conf"
section: "5"
letter: "r"
url: "/docs/linux/man/5-racoon-conf/"
description: "racoon.conf – configuration file for racoon"
---

<p><code>racoon.conf</code> &#8211; configuration file for racoon</p>
<h2>Description</h2>
<p>is the configuration file for the <a href="/docs/linux/man/8-racoon/">racoon</a>(8) ISAKMP daemon. <a href="/docs/linux/man/8-racoon/">racoon</a>(8) negotiates security associations for itself (ISAKMP SA, or phase 1 SA) and for kernel IPsec (IPsec SA, or phase 2 SA). The file consists of a sequence of directives and statements. Each directive is composed by a tag and statements, enclosed by `{&#8216; and `}&#8217; Lines beginning with `#&#8217; are comments.</p>
<h3>Meta Syntax</h3>
<p>Keywords and special characters that the parser expects exactly are displayed using <code>this</code> font. Parameters are specified with <i>this</i> font. Square brackets Po `[&#8216; and `]&#8217; Pc are used to show optional keywords and parameters. Note that you have to pay attention when this manual is describing <i>port</i> numbers. The <i>port</i> number is always enclosed by `[&#8216; and `]&#8217; In this case, the port number is not an optional keyword. If it is possible to omit the <i>port</i> number, the expression becomes Bq Bq Ar port . The vertical bar (`|&#8217; ) is used to indicate a choice between optional parameters. Parentheses Po `(&#8216; and `)&#8217; Pc are used to group keywords and parameters when necessary. Major parameters are listed below. </p>
<dt><i>number</i></p>
<dd>means a hexadecimal or a decimal number. The former must be prefixed with `<code>0x</code> &#8216;</p>
<dt><i>string</i></p>
<dd>
<dt><i>path</i></p>
<dd>
<dt><i>file</i></p>
<dd>means any string enclosed in `&#8217; (double quotes)</p>
<dt><i>address</i></p>
<dd>means IPv6 and/or IPv4 address.</p>
<dt><i>port</i></p>
<dd>means a TCP/UDP port number. The port number is always enclosed by `[&#8216; and `]&#8217;</p>
<dt><i>timeunit</i></p>
<dd>is one of following: <code>sec , secs , second , seconds</code> <code>min , mins , minute , minutes</code> <code>hour , hours</code></dl>
<h3>Privilege separation</h3>
<dl>
<dt><code>privsep { </code><i>statements </i><code>}</code></p>
<dd>Specifies privilege separation parameters. When enabled, these enable <a href="/docs/linux/man/8-racoon/">racoon</a>(8) to operate with an unprivileged instance doing most of the work, while a privileged instance takes care of performing the following operations as root: reading PSK and private keys, launching hook scripts, and validating passwords against system databases or against PAM. Please note that using privilege separation makes changes to the <i>listen</i> and <i>paths</i> sections ignored upon configuration reloads. A <a href="/docs/linux/man/8-racoon/">racoon</a>(8) restart is required if you want such changes to be taken into account. </p>
<dt><code>user </code><i>user</i></p>
<dd>The user to which the unprivileged instance of <a href="/docs/linux/man/8-racoon/">racoon</a>(8), should switch. This can be a quoted user name or a numeric UID.</p>
<dt><code>group </code><i>group</i></p>
<dd>The group the unprivileged instance of <a href="/docs/linux/man/8-racoon/">racoon</a>(8), should switch. This can be a quoted group name or a numeric GID.</p>
<dt><code>chroot </code><i>path</i></p>
<dd>A directory to which the unprivileged instance of <a href="/docs/linux/man/8-racoon/">racoon</a>(8) should <a href="/docs/linux/man/2-chroot/">chroot</a>(2). This directory should hold a tree where the following files must be reachable:</p>
<dl>
<dt><code>/dev/random </code></p>
<dd>
<dt><code>/dev/urandom </code></p>
<dd>
<dt><code>The certificates</code></p>
<dd>
<dt><code>The file containing the Xauth banner</code></p>
<dd></dl>
<p> The PSK file, the private keys, and the hook scripts are accessed through the privileged instance of <a href="/docs/linux/man/8-racoon/">racoon</a>(8) and do not need to be reachable in the <a href="/docs/linux/man/2-chroot/">chroot</a>(2)Aped tree.</dl>
<h3>Path Specification</h3>
<p>This section specifies various paths used by racoon. When running in privilege separation mode, <code>certificate</code> and <code>script</code> paths are mandatory. A <a href="/docs/linux/man/8-racoon/">racoon</a>(8) restart is required if you want path changes to be taken into account.</p>
<dl>
<dt><code>path include </code><i>path</i></p>
<dd>Specifies a path to include a file. See Sx File Inclusion .</p>
<dt><code>path pre_shared_key </code><i>file</i></p>
<dd>Specifies a file containing pre-shared key(s) for various ID(s). See Sx Pre-shared key File .</p>
<dt><code>path certificate </code><i>path</i></p>
<dd><a href="/docs/linux/man/8-racoon/">racoon</a>(8) will search this directory if a certificate or certificate request is received. If you run with privilege separation, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will refuse to use a certificate stored outside of this directory.</p>
<dt><code>path backupsa </code><i>file</i></p>
<dd>Specifies a file to which SA information negotiated by racoon should be stored. <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will install SA(s) from the file when started with the &#8211;<code>B</code> flag. The file is growing because <a href="/docs/linux/man/8-racoon/">racoon</a>(8) simply adds SAs to it. You should maintain the file manually.</p>
<dt><code>path script </code><i>path</i></p>
<dd><a href="/docs/linux/man/8-racoon/">racoon</a>(8) will search this directory for scripts hooks. If you run with privilege separation, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will refuse to execute a script stored outside of this directory.</p>
<dt><code>path pidfile </code><i>file</i></p>
<dd>Specifies file where to store PID of process. If path starts with / it is treated as an absolute path. Otherwise, it is treated as a relative path to the VARRUN directory specified at compilation time. Default is racoon.pid</dl>
<h3>File Inclusion</h3>
<dl>
<dt><code>include </code><i>file</i></p>
<dd>Specifies other configuration files to be included.</dl>
<h3>Timer Specification</h3>
<dl>
<dt><code>timer { </code><i>statements </i><code>}</code></p>
<dd>This section specifies various timer values used by racoon. </p>
<dt><code>counter </code><i>number</i></p>
<dd>The maximum number of retries to send. The default is 5.</p>
<dt><code>interval </code><i>number timeunit</i></p>
<dd>The interval to resend, in seconds. The default time is 10 seconds.</p>
<dt><code>persend </code><i>number</i></p>
<dd>The number of packets per send. The default is 1.</p>
<dt><code>phase1 </code><i>number timeunit</i></p>
<dd>The maximum time it should take to complete phase 1. The default time is 15 seconds.</p>
<dt><code>phase2 </code><i>number timeunit</i></p>
<dd>The maximum time it should take to complete phase 2. The default time is 10 seconds.</p>
<dt><code>natt_keepalive </code><i>number timeunit</i></p>
<dd>The interval between sending NAT-Traversal keep-alive packets. The default time is 20 seconds. Set to 0s to disable keep-alive packets.</dl>
<h3>Listening Port Specification</h3>
<dl>
<dt><code>listen { </code><i>statements </i><code>}</code></p>
<dd>If no <i>listen</i> directive is specified, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will listen on all available interface addresses. The following is the list of valid statements: </p>
<dt><code>isakmp </code><i>address Bq </i>Bq <i>port</i></p>
<dd>If this is specified, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will only listen on the defined <i>address</i> The default port is 500, which is specified by IANA. You can provide more than one address definition.</p>
<dt><code>isakmp_natt </code><i>address Bq </i><i>port</i></p>
<dd>Same as <code>isakmp</code> but also sets the socket options to accept UDP-encapsulated ESP traffic for NAT-Traversal. If you plan to use NAT-T, you should provide at least one address with port 4500, which is specified by IANA. There is no default.</p>
<dt><code>strict_address</code></p>
<dd>Requires that all addresses for ISAKMP be bound. This statement will be ignored if you do not specify address definitions.</dl>
<p> When running in privilege separation mode, you need to restart <a href="/docs/linux/man/8-racoon/">racoon</a>(8) to have changes to the <i>listen</i> section taken into account. The <i>listen</i> section can also be used to specify the admin socket mode and ownership if racoon was built with support for admin port.</p>
<dl>
<dt><code>adminsock </code><i>path </i>[<i>owner group mode</i> ]</p>
<dd>The <i>path</i> <i>owner</i> and <i>group</i> values specify the socket path, owner, and group. They must be quoted. The defaults are /var/racoon/racoon.sock UID 0, and GID 0. <i>mode</i> is the access mode in octal. The default is 0600.</p>
<dt><code>adminsock disabled</code></p>
<dd>This directive tells racoon to not listen on the admin socket.</dl>
<h3>Miscellaneous Global Parameters</h3>
<dl>
<dt><code>gss_id_enc </code><i>enctype</i></p>
<dd>Older versions of <a href="/docs/linux/man/8-racoon/">racoon</a>(8) used ISO-Latin-1 as the encoding of the GSS-API identifier attribute. For interoperability with Microsoft Windows&#8217; GSS-API authentication scheme, the default encoding has been changed to UTF-16LE. The <code>gss_id_enc</code> parameter allows <a href="/docs/linux/man/8-racoon/">racoon</a>(8) to be configured to use the old encoding for compatibility with existing <a href="/docs/linux/man/8-racoon/">racoon</a>(8) installations. The following are valid values for <i>enctype</i> </p>
<dt><code>utf-16le</code></p>
<dd>Use UTF-16LE to encode the GSS-API identifier attribute. This is the default encoding. This encoding is compatible with Microsoft Windows.</p>
<dt><code>latin1</code></p>
<dd>Use ISO-Latin-1 to encode the GSS-API identifier attribute. This is the encoding used by older versions of <a href="/docs/linux/man/8-racoon/">racoon</a>(8).</dl>
<dt><code>pfkey_buffer </code><i>kBytes</i></p>
<dd>Specifies the socket send/receive buffer size in kilobytes. Numerous kernel PF_KEY implementations have problems with dumping SAD/SDP with large amount of entries (this happens when 100s to 1000s of tunnels are configured). The default value of 0 leaves everything at the OS-specific default value. If the default buffer size is greater than what is specified here racoon will not decrease it. This problem is known to be fixed in Linux 2.6.25 and later.</dl>
<h3>Remote Nodes Specifications</h3>
<dl>
<dt><code>remote </code><i>name Bo </i><code>inherit </code><i>parent_name Bc </i><code>({ </code><i>statements </i><code>} | ;)</code></p>
<dd>Specifies the IKE phase 1 parameters for each remote node. If connection is initiated using racoonctl, a unique match using the remote IP must be found or the remote block name has to be given. For received acquires (kernel notices traffic requiring a new SA) the remote IP and remoteid from matching sainfo block are used to decide the remoteblock. If no uniquely matching remoteblock is found using these criteria, no connection attempt is done. When acting as responder, racoon picks the first proposal that has one or more acceptable remote configurations. When determining if a remote specification is matching the following information is checked: </p>
<ul>
<li> The remote IP is checked against <code>remote_address</code>
<li> ISAKMP exchange type is checked against <code>exchange_mode</code>
<li> ISAKMP SA attributes must match a <code>proposal</code> block.
<li> The remote identity is matched against <code>peers_identifier</code> if <code>verify_identifier</code> is on.
<li> If a certificate request was received, it must match the issuer of <code>certificate_type x509</code> certificate. If certificate request without issuer name was sent, the <code>match_empty_cr</code> parameter specifies whether or not remote block matches. </ul>
<p> Similarly, NAT-T is enabled if any of the initial remote configuration candidates allow NAT-T. Sections with <code>inherit </code><i>parent</i> statements (where <i>parent</i> is either <i>address</i> or a keyword <code>anonymous</code> that have all values predefined to those of a given <i>parent</i> In these sections it is enough to redefine only the changed parameters. The following are valid statements. </p>
<dt><code>remote_address </code><i>address</i></p>
<dd>Defines the IP address of the peer.</p>
<dt><code>exchange_mode ( main | aggressive | base</code></p>
<dd>Defines the exchange mode for phase 1 when racoon is the initiator. It also means the acceptable exchange mode when racoon is the responder. More than one mode can be specified by separating them with a comma. All of the modes are acceptable. The first exchange mode is what racoon uses when it is the initiator.</p>
<dt><code>doi ipsec_doi</code></p>
<dd>Means to use IPsec DOI as specified in RFC 2407. You can omit this statement.</p>
<dt><code>situation identity_only</code></p>
<dd>Means to use SIT_IDENTITY_ONLY as specified in RFC 2407. You can omit this statement.</p>
<dt><code>my_identifier Bo </code><i>qualifier Bc </i><i>idtype &#8230;</i></p>
<dd>Specifies the identifier sent to the remote host and the type to use in the phase 1 negotiation. <code>address, fqdn , user_fqdn , keyid</code> and <code>asn1dn</code> can be used as an <i>idtype</i> The <i>qualifier</i> is currently only used for <code>keyid</code> and can be either <code>file</code> or <code>tag</code> The possible values are :</p>
<dl>
<dt><code>my_identifier address Bq </code><i>address</i></p>
<dd>The type is the IP address. This is the default type if you do not specify an identifier to use.</p>
<dt><code>my_identifier user_fqdn </code><i>string</i></p>
<dd>The type is a USER_FQDN (user fully-qualified domain name).</p>
<dt><code>my_identifier fqdn </code><i>string</i></p>
<dd>The type is a FQDN (fully-qualified domain name).</p>
<dt><code>my_identifier keyid Bo </code><code>file Bc </code><i>file</i></p>
<dd>The type is a KEY_ID, read from the file.</p>
<dt><code>my_identifier keyid tag </code><i>string</i></p>
<dd>The type is a KEY_ID, specified in the quoted string.</p>
<dt><code>my_identifier asn1dn Bq </code><i>string</i></p>
<dd>The type is an ASN.1 distinguished name. If <i>string</i> is omitted, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will get the DN from the Subject field in the certificate.</dl>
<dt><code>xauth_login Bq </code><i>string</i></p>
<dd>Specifies the login to use in client-side Hybrid authentication. It is available only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) has been built with this option. The associated password is looked up in the pre-shared key files, using the login <code>string</code> as the key id.</p>
<dt><code>peers_identifier </code><i>idtype &#8230;</i></p>
<dd>Specifies the peer&#8217;s identifier to be received. If it is not defined then <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will not verify the peer&#8217;s identifier in ID payload transmitted from the peer. If it is defined, the behavior of the verification depends on the flag of <code>verify_identifier</code> The usage of <i>idtype</i> is the same as <code>my_identifier</code> except that the individual component values of an <code>asn1dn</code> identifier may specified as <code>*</code> to match any value (e.g. &quot;C=XX, O=MyOrg, OU=*, CN=Mine&quot;). The format of the specification should correspond to RFC 2253; in particular, commas and certain other characters &#8211; <code>,=+&lt;&gt;#;</code> &#8211; may be included in a name by preceeding them with a backslash &quot;\&quot;, and arbitrary characters may be inserted in a name with the &quot;
n&quot; escape, where nn is the hex representation of the ascii value of the desired character. Alternative acceptable peer identifiers may be specified by repeating the <code>peers_identifier</code> statement.</p>
<dt><code>verify_identifier (on | off)</code></p>
<dd>If you want to verify the peer&#8217;s identifier, set this to on. In this case, if the value defined by <code>peers_identifier</code> is not the same as the peer&#8217;s identifier in the ID payload, the negotiation will fail. The default is off.</p>
<dt><code>certificate_type </code><i>certspec</i></p>
<dd>Specifies a certificate specification. <i>certspec</i> is one of followings:</p>
<dl>
<dt><code>x509 </code><i>certfile privkeyfile</i></p>
<dd><i>certfile</i> means a file name of a certificate. <i>privkeyfile</i> means a file name of a secret key.</dl>
<dt><code>plain_rsa </code><i>privkeyfile</i></p>
<dd><i>privkeyfile</i> means a file name of a private key generated by plainrsa-gen8. Required for RSA authentication.</dl>
<dt><code>ca_type </code><i>cacertspec</i></p>
<dd>Specifies a root certificate authority specification. <i>cacertspec</i> is one of followings:</p>
<dl>
<dt><code>x509 </code><i>cacertfile</i></p>
<dd><i>cacertfile</i> means a file name of the root certificate authority. Default is /etc/openssl/cert.pem</dl>
<dt><code>mode_cfg (on | off)</code></p>
<dd>Gather network information through ISAKMP mode configuration. Default is off.</p>
<dt><code>weak_phase1_check (on | off)</code></p>
<dd>Tells racoon to act on unencrypted deletion messages during phase 1. This is a small security risk, so the default is off, meaning that racoon will keep on trying to establish a connection even if the user credentials are wrong, for instance.</p>
<dt><code>peers_certfile ( dnssec | </code><i>certfile | </i><code>plain_rsa </code><i>pubkeyfile</i></p>
<dd>If <code>dnssec</code> is defined, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will ignore the CERT payload from the peer, and try to get the peer&#8217;s certificate from DNS instead. If <i>certfile</i> is defined, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will ignore the CERT payload from the peer, and will use this certificate as the peer&#8217;s certificate. If <code>plain_rsa</code> is defined, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will expect <i>pubkeyfile</i> to be the peer&#8217;s public key that was generated by plainrsa-gen8.</p>
<dt><code>script </code><i>script </i><code>phase1_up</code></p>
<dd>
<dt><code>script </code><i>script </i><code>phase1_down</code></p>
<dd>
<dt><code>script </code><i>script </i><code>phase1_dead</code></p>
<dd>Shell scripts that get executed when a phase 1 SA goes up or down, or when it is detected as dead by DPD. All scripts get either <code>phase1_up</code> , <code>phase1_down</code> or <code>phase1_dead</code> as first argument, and the following variables are set in their environment:</p>
<dl>
<dt><code>LOCAL_ADDR</code></p>
<dd>The local address of the phase 1 SA.</p>
<dt><code>LOCAL_PORT</code></p>
<dd>The local port used for IKE for the phase 1 SA.</p>
<dt><code>REMOTE_ADDR</code></p>
<dd>The remote address of the phase 1 SA.</p>
<dt><code>REMOTE_PORT</code></p>
<dd>The remote port used for IKE for the phase 1 SA.</p>
<dt><code>REMOTE_ID</code></p>
<dd>The remote identity received in IKE for the phase 1 SA.</dl>
<p> The following variables are only set if <code>mode_cfg</code> was enabled:</p>
<dl>
<dt><code>INTERNAL_ADDR4</code></p>
<dd>An IPv4 internal address obtained by ISAKMP mode config.</p>
<dt><code>INTERNAL_NETMASK4</code></p>
<dd>An IPv4 internal netmask obtained by ISAKMP mode config.</p>
<dt><code>INTERNAL_CIDR4</code></p>
<dd>An IPv4 internal netmask obtained by ISAKMP mode config, in CIDR notation.</p>
<dt><code>INTERNAL_DNS4</code></p>
<dd>The first internal DNS server IPv4 address obtained by ISAKMP mode config.</p>
<dt><code>INTERNAL_DNS4_LIST</code></p>
<dd>A list of internal DNS servers IPv4 address obtained by ISAKMP mode config, separated by spaces.</p>
<dt><code>INTERNAL_WINS4</code></p>
<dd>The first internal WINS server IPv4 address obtained by ISAKMP mode config.</p>
<dt><code>INTERNAL_WINS4_LIST</code></p>
<dd>A list of internal WINS servers IPv4 address obtained by ISAKMP mode config, separated by spaces.</p>
<dt><code>SPLIT_INCLUDE</code></p>
<dd>The space separated list of IPv4 addresses and masks (address slash mask) that define the networks to be encrypted (as opposed to the default where all the traffic should be encrypted) ; obtained by ISAKMP mode config ; SPLIT_INCLUDE and SPLIT_LOCAL are mutually exclusive.</p>
<dt><code>SPLIT_LOCAL</code></p>
<dd>The space separated list of IPv4 addresses and masks (address slash mask) that define the networks to be considered local, and thus excluded from the tunnels ; obtained by ISAKMP mode config.</p>
<dt><code>SPLIT_INCLUDE_CIDR</code></p>
<dd>Same as SPLIT_INCLUDE, with netmasks in CIDR notation.</p>
<dt><code>SPLIT_LOCAL_CIDR</code></p>
<dd>Same as SPLIT_LOCAL, with netmasks in CIDR notation.</p>
<dt><code>DEFAULT_DOMAIN</code></p>
<dd>The DNS default domain name obtained by ISAKMP mode config.</dl>
<dt><code>send_cert (on | off)</code></p>
<dd>If you do not want to send a certificate, set this to off. The default is on.</p>
<dt><code>send_cr (on | off)</code></p>
<dd>If you do not want to send a certificate request, set this to off. The default is on.</p>
<dt><code>match_empty_cr (on | off)</code></p>
<dd>Specifies whether this remote block is a valid match when a non-specific certificate request is received. The default is on.</p>
<dt><code>verify_cert (on | off)</code></p>
<dd>By default, the identifier sent by the remote host (as specified in its <code>my_identifier</code> statement) is compared with the credentials in the certificate used to authenticate the remote host as follows:</p>
<dl>
<dt><code>Type asn1dn</code></p>
<dd>The entire certificate subject name is compared with the identifier, e.g. &quot;C=XX, O=YY, &#8230;&quot;.</p>
<dt><code>Type address, fqdn, or user_fqdn</code></p>
<dd>The certificate&#8217;s subjectAltName is compared with the identifier.</dl>
<p> If the two do not match the negotiation will fail. If you do not want to verify the identifier using the peer&#8217;s certificate, set this to off.</p>
<dt><code>lifetime time </code><i>number timeunit</i></p>
<dd>Define a lifetime of a certain time which will be proposed in the phase 1 negotiations. Any proposal will be accepted, and the attribute(s) will not be proposed to the peer if you do not specify it (them). They can be individually specified in each proposal.</p>
<dt><code>ike_frag (on | off | force)</code></p>
<dd>Enable receiver-side IKE fragmentation if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) has been built with this feature. If set to on, racoon will advertise itself as being capable of receiving packets split by IKE fragmentation. This extension is there to work around broken firewalls that do not work with fragmented UDP packets. IKE fragmentation is always enabled on the sender-side, and it is used if the peer advertises itself as IKE fragmentation capable. By selecting force, IKE Fragmentation will be used when racoon is acting as the initiator even before the remote peer has advertised itself as IKE fragmentation capable.</p>
<dt><code>esp_frag </code><i>fraglen</i></p>
<dd>This option is only relevant if you use NAT traversal in tunnel mode. Its purpose is to work around broken DSL routers that reject UDP fragments, by fragmenting the IP packets before ESP encapsulation. The result is ESP over UDP of fragmented packets instead of fragmented ESP over UDP packets (i.e., IP:UDP:ESP:frag(IP) instead of frag(IP:UDP:ESP:IP)). <i>fraglen</i> is the maximum size of the fragments. 552 should work anywhere, but the higher <i>fraglen</i> is, the better the performance. Note that because PMTU discovery is broken on many sites, you will have to use MSS clamping if you want TCP to work correctly.</p>
<dt><code>initial_contact (on | off)</code></p>
<dd>Enable this to send an INITIAL-CONTACT message. The default value is <code>on</code> This message is useful only when the responder implementation chooses an old SA when there are multiple SAs with different established time and the initiator reboots. If racoon did not send the message, the responder would use an old SA even when a new SA was established. For systems that use a KAME derived IPSEC stack, the <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8) variable net.key.preferred_oldsa can be used to control this preference. When the value is zero, the stack always uses a new SA.</p>
<dt><code>passive (on | off)</code></p>
<dd>If you do not want to initiate the negotiation, set this to on. The default value is <code>off</code> It is useful for a server.</p>
<dt><code>proposal_check </code><i>level</i></p>
<dd>Specifies the action of lifetime length, key length, and PFS of the phase 2 selection on the responder side, and the action of lifetime check in phase 1. The default level is <code>strict</code> If the <i>level</i> is:</p>
<dl>
<dt><code>obey</code></p>
<dd>The responder will obey the initiator anytime.</p>
<dt><code>strict</code></p>
<dd>If the responder&#8217;s lifetime length is longer than the initiator&#8217;s or the responder&#8217;s key length is shorter than the initiator&#8217;s, the responder will use the initiator&#8217;s value. Otherwise, the proposal will be rejected. If PFS is not required by the responder, the responder will obey the proposal. If PFS is required by both sides and the responder&#8217;s group is not equal to the initiator&#8217;s, then the responder will reject the proposal.</p>
<dt><code>claim</code></p>
<dd>If the responder&#8217;s lifetime length is longer than the initiator&#8217;s or the responder&#8217;s key length is shorter than the initiator&#8217;s, the responder will use the initiator&#8217;s value. If the responder&#8217;s lifetime length is shorter than the initiator&#8217;s, the responder uses its own length AND sends a RESPONDER-LIFETIME notify message to an initiator in the case of lifetime (phase 2 only). For PFS, this directive behaves the same as <code>strict</code></p>
<dt><code>exact</code></p>
<dd>If the initiator&#8217;s lifetime or key length is not equal to the responder&#8217;s, the responder will reject the proposal. If PFS is required by both sides and the responder&#8217;s group is not equal to the initiator&#8217;s, then the responder will reject the proposal.</dl>
<dt><code>support_proxy (on | off)</code></p>
<dd>If this value is set to on, then both values of ID payloads in the phase 2 exchange are always used as the addresses of end-point of IPsec-SAs. The default is off.</p>
<dt><code>generate_policy (on | off | require | unique)</code></p>
<dd>This directive is for the responder. Therefore you should set <code>passive</code> to on in order that <a href="/docs/linux/man/8-racoon/">racoon</a>(8) only becomes a responder. If the responder does not have any policy in SPD during phase 2 negotiation, and the directive is set to on, then <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will choose the first proposal in the SA payload from the initiator, and generate policy entries from the proposal. It is useful to negotiate with clients whose IP address is allocated dynamically. Note that an inappropriate policy might be installed into the responder&#8217;s SPD by the initiator, so other communications might fail if such policies are installed due to a policy mismatch between the initiator and the responder. <code>on</code> and <code>require</code> values mean the same thing (generate a require policy). <code>unique</code> tells racoon to set up unique policies, with a monotoning increasing reqid number (between 1 and IPSEC_MANUAL_REQID_MAX). This directive is ignored in the initiator case. The default value is <code>off</code></p>
<dt><code>nat_traversal (on | off | force)</code></p>
<dd>This directive enables use of the NAT-Traversal IPsec extension (NAT-T). NAT-T allows one or both peers to reside behind a NAT gateway (i.e., doing address- or port-translation). If a NAT gateway is detected during the phase 1 handshake, racoon will attempt to negotiate the use of NAT-T with the remote peer. If the negotiation succeeds, all ESP and AH packets for the given connection will be encapsulated into UDP datagrams (port 4500, by default). Possible values are:</p>
<dl>
<dt><code>on</code></p>
<dd>NAT-T is used when a NAT gateway is detected between the peers.</p>
<dt><code>off</code></p>
<dd>NAT-T is not proposed/accepted. This is the default.</p>
<dt><code>force</code></p>
<dd>NAT-T is used regardless of whether a NAT gateway is detected between the peers or not.</dl>
<p> Please note that NAT-T support is a compile-time option. Although it is enabled in the source distribution by default, it may not be available in your particular build. In that case you will get a warning when using any NAT-T related config options.</p>
<dt><code>dpd_delay </code><i>delay</i></p>
<dd>This option activates the DPD and sets the time (in seconds) allowed between 2 proof of liveliness requests. The default value is <code>0</code> which disables DPD monitoring, but still negotiates DPD support.</p>
<dt><code>dpd_retry </code><i>delay</i></p>
<dd>If <code>dpd_delay</code> is set, this sets the delay (in seconds) to wait for a proof of liveliness before considering it as failed and send another request. The default value is <code>5</code></p>
<dt><code>dpd_maxfail </code><i>number</i></p>
<dd>If <code>dpd_delay</code> is set, this sets the maximum number of liveliness proofs to request (without reply) before considering the peer is dead. The default value is <code>5</code></p>
<dt><code>rekey (on | off | force)</code></p>
<dd>Enable automatic renegotiation of expired phase1 when there are non-dying phase2 SAs. Possible values are:</p>
<dl>
<dt><code>force</code></p>
<dd>Rekeying is done unconditionally.</p>
<dt><code>on</code></p>
<dd>Rekeying is done only if DPD monitoring is active. This is the default.</p>
<dt><code>off</code></p>
<dd>No automatic rekeying. Do note that turning off automatic rekeying will result in inaccurate DPD monitoring.</dl>
<dt><code>nonce_size </code><i>number</i></p>
<dd>define the byte size of nonce value. Racoon can send any value although RFC2409 specifies that the value MUST be between 8 and 256 bytes. The default size is 16 bytes.</p>
<dt><code>ph1id </code><i>number</i></p>
<dd>An optional number to identify the remote proposal and to link it only with sainfos who have the same number. Defaults to 0.</p>
<dt><code>proposal { </code><i>sub-substatements </i><code>}</code></p>
<dd>
<dl>
<dt><code>encryption_algorithm </code><i>algorithm</i></p>
<dd>Specifies the encryption algorithm used for the phase 1 negotiation. This directive must be defined. <i>algorithm</i> is one of following: <code>des, 3des, blowfish, cast128, aes, camellia</code> for Oakley. For other transforms, this statement should not be used.</p>
<dt><code>hash_algorithm </code><i>algorithm</i></p>
<dd>Defines the hash algorithm used for the phase 1 negotiation. This directive must be defined. <i>algorithm</i> is one of following: <code>md5, sha1, sha256, sha384, sha512</code> for Oakley.</p>
<dt><code>authentication_method </code><i>type</i></p>
<dd>Defines the authentication method used for the phase 1 negotiation. This directive must be defined. <i>type</i> is one of: <code>pre_shared_key , rsasig</code> (for plain RSA authentication), <code>gssapi_krb , hybrid_rsa_server</code> <code>hybrid_rsa_client , xauth_rsa_server , xauth_rsa_client , xauth_psk_server</code> or <code>xauth_psk_client</code></p>
<dt><code>dh_group </code><i>group</i></p>
<dd>Defines the group used for the Diffie-Hellman exponentiations. This directive must be defined. <i>group</i> is one of following: <code>modp768 , modp1024 , modp1536</code> <code>modp2048 , modp3072 , modp4096</code> <code>modp6144 , modp8192</code> Or you can define 1, 2, 5, 14, 15, 16, 17, or 18 as the DH group number. When you want to use aggressive mode, you must define the same DH group in each proposal.</p>
<dt><code>lifetime time </code><i>number timeunit</i></p>
<dd>Defines the lifetime of the phase 1 SA proposal. Refer to the description of the <code>lifetime</code> directive defined in the <code>remote</code> directive.</p>
<dt><code>gss_id </code><i>string</i></p>
<dd>Defines the GSS-API endpoint name, to be included as an attribute in the SA, if the <code>gssapi_krb</code> authentication method is used. If this is not defined, the default value of `host/hostname&#8217; is used, where hostname is the value returned by the <a href="/docs/linux/man/1-hostname/">hostname</a>(1) command.</dl>
<dt><code>remote Po </code><i>address | </i><code>anonymous Pc </code>Bo Bo <i>port Bc </i>Bc Bo <code>inherit </code><i>parent Bc </i><code>{ </code><i>statements </i><code>}</code></p>
<dd>Deprecated format of specifying a remote block. This will be removed in future. It is a remnant from time when remote block was decided solely based on the peers IP address. This is equivalent to: </p>
<pre>remote &quot;address&quot; [inherit &quot;parent-address&quot;] {
 remote_address address;
}</pre>
</dl>
<h3>Sainfo Specifications</h3>
<dl>
<dt><code>sainfo Po </code><i>local_id | </i><code>anonymous Pc </code>Po <i>remote_id | </i><code>clientaddr | anonymous Pc </code>Bo <code>from </code><i>idtype Bo </i><i>string Bc </i>Bc Bo <code>group </code><i>string Bc </i><code>{ </code><i>statements </i><code>}</code></p>
<dd>Defines the parameters of the IKE phase 2 (IPsec-SA establishment). The <i>local_id</i> and <i>remote_id</i> strings are constructed like: <code>address </code><i>address</i> Bq Ic / Ar prefix Bq Ic [ Ar port ] <i>ul_proto</i> or <code>subnet </code><i>address</i> Bq Ic / Ar prefix Bq Ic [ Ar port ] <i>ul_proto</i> An id string should be expressed to match the exact value of an ID payload. This is not like a filter rule. For example, if you define 3ffe:501:4819::/48 as <i>local_id</i> 3ffe:501:4819:1000:/64 will not match. In the case of a longest prefix (selecting a single host), <i>address</i> instructs to send ID type of ADDRESS while <i>subnet</i> instructs to send ID type of SUBNET. Otherwise, these instructions are identical. The <code>anonymous</code> keyword can be used to match any id. The <code>clientaddr</code> keyword can be used to match a remote id that is equal to either the peer ip address or the mode_cfg ip address (if assigned). This can be useful to restrict policy generation when racoon is acting as a client gateway for peers with dynamic ip addresses. The <code>from</code> keyword allows an sainfo to only match for peers that use a specific phase1 id value during authentication. The <code>group</code> keyword allows an XAuth group membership check to be performed for this sainfo section. When the mode_cfg auth source is set to <code>system</code> or <code>ldap</code> the XAuth user is verified to be a member of the specified group before allowing a matching SA to be negotiated. </p>
<dt><code>pfs_group </code><i>group</i></p>
<dd>define the group of Diffie-Hellman exponentiations. If you do not require PFS then you can omit this directive. Any proposal will be accepted if you do not specify one. <i>group</i> is one of following: <code>modp768 , modp1024 , modp1536</code> <code>modp2048 , modp3072 , modp4096</code> <code>modp6144 , modp8192</code> Or you can define 1, 2, 5, 14, 15, 16, 17, or 18 as the DH group number.</p>
<dt><code>lifetime time </code><i>number timeunit</i></p>
<dd>define how long an IPsec-SA will be used, in timeunits. Any proposal will be accepted, and no attribute(s) will be proposed to the peer if you do not specify it(them). See the <code>proposal_check</code> directive.</p>
<dt><code>remoteid </code><i>number</i></p>
<dd>Sainfos will only be used if their remoteid matches the ph1id of the remote section used for phase 1. Defaults to 0, which is also the default for ph1id.</dl>
<p> <a href="/docs/linux/man/8-racoon/">racoon</a>(8) does not have a list of security protocols to be negotiated. The list of security protocols are passed by SPD in the kernel. Therefore you have to define all of the potential algorithms in the phase 2 proposals even if there are algorithms which will not be used. These algorithms are define by using the following three directives, with a single comma as the separator. For algorithms that can take variable-length keys, algorithm names can be followed by a key length, like &#8220;<code>blowfish 448</code> &#8221; <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will compute the actual phase 2 proposals by computing the permutation of the specified algorithms, and then combining them with the security protocol specified by the SPD. For example, if <code>des , 3des , hmac_md5</code> and <code>hmac_sha1</code> are specified as algorithms, we have four combinations for use with ESP, and two for AH. Then, based on the SPD settings, <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will construct the actual proposals. If the SPD entry asks for ESP only, there will be 4 proposals. If it asks for both AH and ESP, there will be 8 proposals. Note that the kernel may not support the algorithm you have specified.</p>
<dl>
<dt><code>encryption_algorithm </code><i>algorithms</i></p>
<dd><code>des , 3des , des_iv64 , des_iv32</code> <code>rc5 , rc4 , idea , 3idea</code> <code>cast128 , blowfish , null_enc</code> <code>twofish , rijndael , aes , camellia</code> (used with ESP)</p>
<dt><code>authentication_algorithm </code><i>algorithms</i></p>
<dd><code>des , 3des , des_iv64 , des_iv32</code> <code>hmac_md5 , hmac_sha1 , hmac_sha256, hmac_sha384, hmac_sha512, non_auth</code> (used with ESP authentication and AH)</p>
<dt><code>compression_algorithm </code><i>algorithms</i></p>
<dd><code>deflate</code> (used with IPComp)</dl>
<h3>Logging level</h3>
<dl>
<dt><code>log </code><i>level</i></p>
<dd>Defines the logging level. <i>level</i> is one of following: <code>error , warning , notify , info , debug</code> or <code>debug2</code> The default is <code>info</code> If you set the logging level too high on slower machines, IKE negotiation can fail due to timing constraint changes.</dl>
<h3>Specifies the way to pad</h3>
<dl>
<dt><code>padding { </code><i>statements </i><code>}</code></p>
<dd>specifies the padding format. The following are valid statements:</p>
<dl>
<dt><code>randomize (on | off)</code></p>
<dd>Enables the use of a randomized value for padding. The default is on.</p>
<dt><code>randomize_length (on | off)</code></p>
<dd>The pad length will be random. The default is off.</p>
<dt><code>maximum_length </code><i>number</i></p>
<dd>Defines a maximum padding length. If <code>randomize_length</code> is off, this is ignored. The default is 20 bytes.</p>
<dt><code>exclusive_tail (on | off)</code></p>
<dd>Means to put the number of pad bytes minus one into the last part of the padding. The default is on.</p>
<dt><code>strict_check (on | off)</code></p>
<dd>Means to constrain the peer to set the number of pad bytes. The default is off.</dl>
<h3>ISAKMP mode configuration settings</h3>
<dl>
<dt><code>mode_cfg { </code><i>statements </i><code>}</code></p>
<dd>Defines the information to return for remote hosts&#8217; ISAKMP mode config requests. Also defines the authentication source for remote peers authenticating through Xauth. The following are valid statements:</p>
<dl>
<dt><code>auth_source (system | radius | pam | ldap)</code></p>
<dd>Specifies the source for authentication of users through Xauth. <i>system</i> means to use the Unix user database. This is the default. <i>radius</i> means to use a RADIUS server. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libradius support. Radius configuration is handled by statements in the <code>radiuscfg</code> section. <i>pam</i> means to use PAM. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libpam support. <i>ldap</i> means to use LDAP. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libldap support. LDAP configuration is handled by statements in the <code>ldapcfg</code> section.</p>
<dt><code>auth_groups </code><i>group1, &#8230;</i></p>
<dd>Specifies the group memberships for Xauth in quoted group name strings. When defined, the authenticating user must be a member of at least one group for Xauth to succeed.</p>
<dt><code>group_source (system | ldap)</code></p>
<dd>Specifies the source for group validation of users through Xauth. <i>system</i> means to use the Unix user database. This is the default. <i>ldap</i> means to use LDAP. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libldap support and requires LDAP authentication. LDAP configuration is handled by statements in the <code>ldapcfg</code> section.</p>
<dt><code>conf_source (local | radius | ldap)</code></p>
<dd>Specifies the source for IP addresses and netmask allocated through ISAKMP mode config. <i>local</i> means to use the local IP pool defined by the <code>network4</code> and <code>pool_size</code> statements. This is the default. <i>radius</i> means to use a RADIUS server. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libradius support and requires RADIUS authentication. RADIUS configuration is handled by statements in the <code>radiuscfg</code> section. <i>ldap</i> means to use an LDAP server. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libldap support and requires LDAP authentication. LDAP configuration is handled by statements in the <code>ldapcfg</code> section.</p>
<dt><code>accounting (none | system | radius | pam)</code></p>
<dd>Enables or disables accounting for Xauth logins and logouts. The default is <i>none</i> which disable accounting. Specifying <i>system</i> enables system accounting through <a href="/docs/linux/man/5-utmp/">utmp</a>(5). Specifying <i>radius</i> enables RADIUS accounting. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was built with libradius support and requires RADIUS authentication. RADIUS configuration is handled by statements in the <code>radiuscfg</code> section. Specifying <i>pam</i> enables PAM accounting. It works only if <a href="/docs/linux/man/8-racoon/">racoon</a>(8) was build with libpam support and requires PAM authentication.</p>
<dt><code>pool_size </code><i>size</i></p>
<dd>Specify the size of the IP address pool, either local or allocated through RADIUS. <code>conf_source</code> selects the local pool or the RADIUS configuration, but in both configurations, you cannot have more than <i>size</i> users connected at the same time. The default is 255.</p>
<dt><code>network4 </code><i>address</i></p>
<dd>
<dt><code>netmask4 </code><i>address</i></p>
<dd>The local IP pool base address and network mask from which dynamically allocated IPv4 addresses should be taken. This is used if <code>conf_source</code> is set to <i>local</i> or if the RADIUS server returned <i>255.255.255.254</i> Default is <i>0.0.0.0/0.0.0.0</i></p>
<dt><code>dns4 </code><i>addresses</i></p>
<dd>A list of IPv4 addresses for DNS servers, separated by commas, or on multiple <code>dns4</code> lines.</p>
<dt><code>wins4 </code><i>addresses</i></p>
<dd>A list of IPv4 address for WINS servers. The keyword</p>
<dt><code>nbns4</code></p>
<dd>can also be used as an alias for</p>
<dt><code>wins4</code></p>
<dd>
<dt><code>split_network (include | local_lan) </code><i>network/mask, &#8230;</i></p>
<dd>The network configuration to send, in CIDR notation (e.g. 192.168.1.0/24). If <code>include</code> is specified, the tunnel should be only used to encrypt the indicated destinations ; otherwise, if <code>local_lan</code> is used, everything will pass through the tunnel but those destinations.</p>
<dt><code>default_domain </code><i>domain</i></p>
<dd>The default DNS domain to send.</p>
<dt><code>split_dns </code><i>domain, &#8230;</i></p>
<dd>The split dns configuration to send, in quoted domain name strings. This list can be used to describe a list of domain names for which a peer should query a modecfg assigned dns server. DNS queries for all other domains would be handled locally. (Cisco VPN client only).</p>
<dt><code>banner </code><i>path</i></p>
<dd>The path of a file displayed on the client at connection time. Default is <i>/etc/motd</i></p>
<dt><code>auth_throttle </code><i>delay</i></p>
<dd>On each failed Xauth authentication attempt, refuse new attempts for a set <i>delay</i> of seconds. This is to avoid dictionary attacks on Xauth passwords. Default is one second. Set to zero to disable authentication delay.</p>
<dt><code>pfs_group </code><i>group</i></p>
<dd>Sets the PFS group used in the client proposal (Cisco VPN client only). Default is 0.</p>
<dt><code>save_passwd (on | off)</code></p>
<dd>Allow the client to save the Xauth password (Cisco VPN client only). Default is off.</dl>
<h3>Ldap configuration settings</h3>
<dl>
<dt><code>ldapcfg { </code><i>statements </i><code>}</code></p>
<dd>Defines the parameters that will be used to communicate with an ldap server for <code>xauth</code> authentication. The following are valid statements:</p>
<dl>
<dt><code>version (2 | 3)</code></p>
<dd>The ldap protocol version used to communicate with the server. The default is <code>3</code></p>
<dt><code>host </code><i>(hostname | address)</i></p>
<dd>The host name or ip address of the ldap server. The default is <code>localhost</code></p>
<dt><code>port </code><i>number</i></p>
<dd>The port that the ldap server is configured to listen on. The default is <code>389</code></p>
<dt><code>base </code><i>distinguished name</i></p>
<dd>The ldap search base. This option has no default value.</p>
<dt><code>subtree (on | off)</code></p>
<dd>Use the subtree ldap search scope. Otherwise, use the one level search scope. The default is <code>off</code></p>
<dt><code>bind_dn </code><i>distinguished name</i></p>
<dd>The user dn used to optionally bind as before performing ldap search operations. If this option is not specified, anonymous binds are used.</p>
<dt><code>bind_pw </code><i>string</i></p>
<dd>The password used when binding as <code>bind_dn</code></p>
<dt><code>attr_user </code><i>attribute name</i></p>
<dd>The attribute used to specify a users name in an ldap directory. For example, if a user dn is &quot;cn=jdoe,dc=my,dc=net&quot; then the attribute would be &quot;cn&quot;. The default value is <code>cn</code></p>
<dt><code>attr_addr </code><i>attribute name</i></p>
<dd>
<dt><code>attr_mask </code><i>attribute name</i></p>
<dd>The attributes used to specify a users network address and subnet mask in an ldap directory. These values are forwarded during mode_cfg negotiation when the conf_source is set to ldap. The default values are <code>racoon-address</code> and <code>racoon-netmask</code></p>
<dt><code>attr_group </code><i>attribute name</i></p>
<dd>The attribute used to specify a group name in an ldap directory. For example, if a group dn is &quot;cn=users,dc=my,dc=net&quot; then the attribute would be &quot;cn&quot;. The default value is <code>cn</code></p>
<dt><code>attr_member </code><i>attribute name</i></p>
<dd>The attribute used to specify group membership in an ldap directory. The default value is <code>member</code></dl>
<h3>Radius configuration settings</h3>
<dl>
<dt><code>radiuscfg { </code><i>statements </i><code>}</code></p>
<dd>Defines the parameters that will be used to communicate with radius servers for <code>xauth</code> authentication. If radius is selected as the xauth authentication or accounting source and no servers are defined in this section, settings from the system radius.conf5 configuration file will be used instead. The following are valid statements:</p>
<dl>
<dt><code>auth </code><i>(hostname | address) [port] sharedsecret</i></p>
<dd>The host name or ip address, optional port value and shared secret value of a radius authentication server. Up to 5 radius authentication servers may be specified using multiple lines.</p>
<dt><code>acct </code><i>(hostname | address) [port] sharedsecret</i></p>
<dd>The host name or ip address, optional port value and shared secret value of a radius accounting server. Up to 5 radius accounting servers may be specified using multiple lines.</p>
<dt><code>timeout </code><i>seconds</i></p>
<dd>The timeout for receiving replies from radius servers. The default is <code>3</code></p>
<dt><code>retries </code><i>count</i></p>
<dd>The maximum number of repeated requests to make before giving up on a radius server. The default is <code>3</code></dl>
<h3>Special directives</h3>
<dl>
<dt><code>complex_bundle (on | off)</code></p>
<dd>defines the interpretation of proposal in the case of SA bundle. Normally &#8220;IP AH ESP IP payload&#8221; is proposed as &#8220;AH tunnel and ESP tunnel&#8221; The interpretation is more common to other IKE implementations, however, it allows very limited set of combinations for proposals. With the option enabled, it will be proposed as &#8220;AH transport and ESP tunnel&#8221; The default value is <code>off</code></dl>
<h3>Pre-shared key File</h3>
<p>The pre-shared key file defines pairs of identifiers and corresponding shared secret keys which are used in the pre-shared key authentication method in phase 1. The pair in each line is separated by some number of blanks and/or tab characters like in the <a href="/docs/linux/man/5-hosts/">hosts</a>(5) file. Key can include blanks because everything after the first blanks is interpreted as the secret key. Lines starting with `#&#8217; are ignored. Keys which start with `0x&#8217; are interpreted as hexadecimal strings. Note that the file must be owned by the user ID running <a href="/docs/linux/man/8-racoon/">racoon</a>(8) (usually the privileged user) and must not be accessible by others.</p>
<h2>Examples</h2>
<p>The following shows how the remote directive should be configured. </p>
<pre>path pre_shared_key &quot;/usr/local/v6/etc/psk.txt&quot; ;
remote anonymous
{
 exchange_mode aggressive,main,base;
 lifetime time 24 hour;
 proposal {
 encryption_algorithm 3des;
 hash_algorithm sha1;
 authentication_method pre_shared_key;
 dh_group 2;
 }
}
sainfo anonymous
{
 pfs_group 2;
 lifetime time 12 hour ;
 encryption_algorithm 3des, blowfish 448, twofish, rijndael ;
 authentication_algorithm hmac_sha1, hmac_md5 ;
 compression_algorithm deflate ;
}</pre>
<p>If you are configuring plain RSA authentication, the remote directive should look like the following: </p>
<pre>path certificate &quot;/usr/local/v6/etc&quot; ;
remote anonymous
{
 exchange_mode main,base ;
 lifetime time 12 hour ;
 certificate_type plain_rsa &quot;/usr/local/v6/etc/myrsakey.priv&quot;;
 peers_certfile plain_rsa &quot;/usr/local/v6/etc/yourrsakey.pub&quot;;
 proposal {
 encryption_algorithm aes ;
 hash_algorithm sha1 ;
 authentication_method rsasig ;
 dh_group 2 ;
 }
}</pre>
<p>The following is a sample for the pre-shared key file. </p>
<pre>10.160.94.3 mekmitasdigoat
172.16.1.133 0x12345678
194.100.55.1 whatcertificatereally
3ffe:501:410:ffff:200:86ff:fe05:80fa mekmitasdigoat
3ffe:501:410:ffff:210:4bff:fea2:8baa mekmitasdigoat
foo [at] kame.net mekmitasdigoat
foo.kame.net hoge</pre>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-racoon/">racoon</a>(8), <a href="/docs/linux/man/8-racoonctl/">racoonctl</a>(8), <a href="/docs/linux/man/8-setkey/">setkey</a>(8)</p>
<h2>History</h2>
<p>The configuration file first appeared in the &#8220;YIPS&#8221; Yokogawa IPsec implementation.</p>
<h2>Bugs</h2>
<p>Some statements may not be handled by <a href="/docs/linux/man/8-racoon/">racoon</a>(8) yet. </p>
<p> Diffie-Hellman computation can take a very long time, and may cause unwanted timeouts, specifically when a large D-H group is used.</p>
<h2>Security Considerations</h2>
<p>The use of IKE phase 1 aggressive mode is not recommended, as described in <code><a rel="nofollow" href="http://www.kb.cert.org/vuls/id/886601">http://www.kb.cert.org/vuls/id/886601</a></code></p>
