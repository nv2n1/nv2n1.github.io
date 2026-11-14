---
title: "ike-scan(1)"
name: "ike-scan"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ike-scan/"
description: "ike-scan – Discover and fingerprint IKE hosts (IPsec VPN servers)"
---

<h2 class="name">NAME</h2>
<p> ike-scan &#8211; Discover and fingerprint IKE hosts (IPsec VPN servers) </p>
<h2>SYNOPSIS</h2>
<p> <code>ike-scan</code> [<i>options</i>]<i> </i>[<i>hosts</i>&#8230;] </p>
<p> Target hosts must be specified on the command line unless the <code>&#8211;file</code> option is specified.</p>
<h2>DESCRIPTION</h2>
<p> <code>ike-scan</code> discovers IKE hosts and can also fingerprint them using the retransmission backoff pattern. </p>
<p> <code>ike-scan</code> does two things:</p>
<dl>
<dt>1)</p>
<dd> Discovery: Determine which hosts are running IKE. This is done by displaying those hosts which respond to the IKE requests sent by <code>ike-scan.</code></p>
<dt>2)</p>
<dd> Fingerprinting: Determine which IKE implementation the hosts are using. There are several ways to do this: (a) Backoff fingerprinting &#8211; recording the times of the IKE response packets from the target hosts and comparing the observed retransmission backoff pattern against known patterns; (b) vendor id fingerprinting &#8211; matching the vendor-specific vendor IDs against known vendor ID patterns; and (c) proprietary notify message codes.</dl>
<p> The retransmission backoff fingerprinting concept is discussed in more detail in the UDP backoff fingerprinting paper which should be included in the ike-scan kit as <i>udp-backoff-fingerprinting-paper.txt.</i> </p>
<p> The program sends IKE Phase-1 requests to the specified hosts and displays any responses that are received. It handles retry and retransmission with backoff to cope with packet loss. It also limits the amount of bandwidth used by the outbound IKE packets. </p>
<p> IKE is the Internet Key Exchange protocol which is the key exchange and authentication mechanism used by IPsec. Just about all modern VPN systems implement IPsec, and the vast majority of IPsec VPNs use IKE for key exchange. </p>
<p> Phase-1 has two modes: Main Mode and Aggressive Mode. ike-scan supports both Main and Aggressive mode, and uses Main Mode by default. RFC 2409 (IKE) section 5 specifies that main mode must be implemented, therefore all IKE implementations can be expected to support main mode.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help or -h</code></p>
<dd> Display this usage message and exit.</p>
<dt><code>&#8211;file=&lt;fn&gt; or -f &lt;fn&gt;</code></p>
<dd> Read hostnames or addresses from the specified file instead of from the command line. One name or IP address per line. Use &quot;-&quot; for standard input.</p>
<dt><code>&#8211;sport=&lt;p&gt; or -s &lt;p&gt;</code></p>
<dd> Set UDP source port to &lt;p&gt;, default=500, 0=random. Some IKE implementations require the client to use UDP source port 500 and will not talk to other ports. Note that superuser privileges are normally required to use non-zero source ports below 1024. Also only one process on a system may bind to a given source port at any one time. Use of the &#8211;nat-t option changes the default source port to 4500</p>
<dt><code>&#8211;dport=&lt;p&gt; or -d &lt;p&gt;</code></p>
<dd> Set UDP destination port to &lt;p&gt;, default=500. UDP port 500 is the assigned port number for ISAKMP and this is the port used by most if not all IKE implementations. Use of the &#8211;nat-t option changes the default destination port to 4500</p>
<dt><code>&#8211;retry=&lt;n&gt; or -r &lt;n&gt;</code></p>
<dd> Set total number of attempts per host to &lt;n&gt;, default=3.</p>
<dt><code>&#8211;timeout=&lt;n&gt; or -t &lt;n&gt;</code></p>
<dd> Set initial per host timeout to &lt;n&gt; ms, default=500. This timeout is for the first packet sent to each host. subsequent timeouts are multiplied by the backoff factor which is set with &#8211;backoff.</p>
<dt><code>&#8211;bandwidth=&lt;n&gt; or -B &lt;n&gt;</code></p>
<dd> Set desired outbound bandwidth to &lt;n&gt;, default=56000 The value is in bits per second by default. If you append &quot;K&quot; to the value, then the units are kilobits per second; and if you append &quot;M&quot; to the value, the units are megabits per second. The &quot;K&quot; and &quot;M&quot; suffixes represent the decimal, not binary, multiples. So 64K is 64000, not 65536.</p>
<dt><code>&#8211;interval=&lt;n&gt; or -i &lt;n&gt;</code></p>
<dd> Set minimum packet interval to &lt;n&gt; ms. The packet interval will be no smaller than this number. The interval specified is in milliseconds by default. if &quot;u&quot; is appended to the value, then the interval is in microseconds, and if &quot;s&quot; is appended, the interval is in seconds. If you want to use up to a given bandwidth, then it is easier to use the &#8211;bandwidth option instead. You cannot specify both &#8211;interval and &#8211;bandwidth because they are just different ways to change the same underlying variable.</p>
<dt><code>&#8211;backoff=&lt;b&gt; or -b &lt;b&gt;</code></p>
<dd> Set timeout backoff factor to &lt;b&gt;, default=1.50. The per-host timeout is multiplied by this factor after each timeout. So, if the number of retries is 3, the initial per-host timeout is 500ms and the backoff factor is 1.5, then the first timeout will be 500ms, the second 750ms and the third 1125ms.</p>
<dt><code>&#8211;verbose or -v</code></p>
<dd> Display verbose progress messages. Use more than once for greater effect: 1 &#8211; Show when each pass is completed and when packets with invalid cookies are received. 2 &#8211; Show each packet sent and received and when hosts are removed from the list. 3 &#8211; Display the host, Vendor ID and backoff lists before scanning starts.</p>
<dt><code>&#8211;quiet or -q</code></p>
<dd> Don&#8217;t decode the returned packet. This prints less protocol information so the output lines are shorter.</p>
<dt><code>&#8211;multiline or -M</code></p>
<dd> Split the payload decode across multiple lines. With this option, the decode for each payload is printed on a separate line starting with a TAB. This option makes the output easier to read, especially when there are many payloads.</p>
<dt><code>&#8211;lifetime=&lt;s&gt; or -l &lt;s&gt;</code></p>
<dd> Set IKE lifetime to &lt;s&gt; seconds, default=28800. RFC 2407 specifies 28800 as the default, but some implementations may require different values. If you specify this as a a decimal integer, e.g. 86400, then the attribute will use a 4-byte value. If you specify it as a hex number, e.g. 0xFF, then the attribute will use the appropriate size value (one byte for this example). If you specify the string &quot;none&quot; then no lifetime attribute will be added at all. You can use this option more than once in conjunction with the &#8211;trans options to produce multiple transform payloads with different lifetimes. Each &#8211;trans option will use the previously specified lifetime value.</p>
<dt><code>&#8211;lifesize=&lt;s&gt; or -z &lt;s&gt;</code></p>
<dd> Set IKE lifesize to &lt;s&gt; Kilobytes, default=0. If you specify this as a a decimal integer, e.g. 86400, then the attribute will use a 4-byte value. If you specify it as a hex number, e.g. 0xFF, then the attribute will use the appropriate size value (one byte for this example). You can use this option more than once in conjunction with the &#8211;trans options to produce multiple transform payloads with different lifesizes. Each &#8211;trans option will use the previously specified lifesize value.</p>
<dt><code>&#8211;auth=&lt;n&gt; or -m &lt;n&gt;</code></p>
<dd> Set auth. method to &lt;n&gt;, default=1 (PSK). RFC defined values are 1 to 5. See RFC 2409 Appendix A. Checkpoint hybrid mode is 64221. GSS (Windows &quot;Kerberos&quot;) is 65001. XAUTH uses 65001 to 65010. This is not applicable to IKEv2.</p>
<dt><code>&#8211;version or -V</code></p>
<dd> Display program version and exit.</p>
<dt><code>&#8211;vendor=&lt;v&gt; or -e &lt;v&gt;</code></p>
<dd> Set vendor id string to hex value &lt;v&gt;. You can use this option more than once to send multiple vendor ID payloads.</p>
<dt><code>&#8211;trans=&lt;t&gt; or -a &lt;t&gt;</code></p>
<dd> Use custom transform &lt;t&gt; instead of default set. You can use this option more than once to send an arbitrary number of custom transforms. There are two ways to specify the transform: The new way, where you specify the attribute/value pairs, and the old way where you specify the values for a fixed list of attributes. For the new method, the transform &lt;t&gt; is specified as (attr=value, attr=value, &#8230;) Where &quot;attr&quot; is the attribute number, and &quot;value&quot; is the value to assign to that attribute. You can specify an arbitary number of attribute/value pairs. See RFC 2409 Appendix A for details of the attributes and values. Note that brackets are special to some shells, so you may need to quote them, e.g. &#8211;trans=&quot;(1=1,2=2,3=3,4=4)&quot;. For example, &#8211;trans=(1=1,2=2,3=1,4=2) specifies Enc=3DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2; and &#8211;trans=(1=7,14=128,2=1,3=3,4=5) specifies Enc=AES/128, Hash=MD5, Auth=RSA sig, DH Group=5. For the old method, the transform &lt;t&gt; is specified as enc[/len],hash,auth,group. Where enc is the encryption algorithm, len is the key length for variable length ciphers, hash is the hash algorithm, and group is the DH Group. For example, &#8211;trans=5,2,1,2 specifies Enc=3DES-CBC, Hash=SHA1, Auth=shared key, DH Group=2; and &#8211;trans=7/256,1,1,5 specifies Enc=AES-256, Hash=MD5, Auth=shared key, DH Group=5. This option is not yet supported for IKEv2.</p>
<dt><code>&#8211;showbackoff[=&lt;n&gt;] or -o[&lt;n&gt;]</code></p>
<dd> Display the backoff fingerprint table. Display the backoff table to fingerprint the IKE implementation on the remote hosts. The optional argument specifies time to wait in seconds after receiving the last packet, default=60. If you are using the short form of the option (-o) then the value must immediately follow the option letter with no spaces, e.g. -o25 not -o 25.</p>
<dt><code>&#8211;fuzz=&lt;n&gt; or -u &lt;n&gt;</code></p>
<dd> Set pattern matching fuzz to &lt;n&gt; ms, default=500. This sets the maximum acceptable difference between the observed backoff times and the reference times in the backoff patterns file. Larger values allow for higher variance but also increase the risk of false positive identifications. Any per-pattern-entry fuzz specifications in the patterns file will override the value set here.</p>
<dt><code>&#8211;patterns=&lt;f&gt; or -p &lt;f&gt;</code></p>
<dd> Use IKE backoff patterns file &lt;f&gt;, default=/usr/local/share/ike-scan/ike-backoff-patterns. This specifies the name of the file containing IKE backoff patterns. This file is only used when &#8211;showbackoff is specified.</p>
<dt><code>&#8211;vidpatterns=&lt;f&gt; or -I &lt;f&gt;</code></p>
<dd> Use Vendor ID patterns file &lt;f&gt;, default=/usr/local/share/ike-scan/ike-vendor-ids. This specifies the name of the file containing Vendor ID patterns. These patterns are used for Vendor ID fingerprinting.</p>
<dt><code>&#8211;aggressive or -A</code></p>
<dd> Use IKE Aggressive Mode (The default is Main Mode) If you specify &#8211;aggressive, then you may also specify &#8211;dhgroup, &#8211;id and &#8211;idtype. If you use custom transforms with aggressive mode with the &#8211;trans option, note that all transforms should have the same DH Group and this should match the group specified with &#8211;dhgroup or the default if &#8211;dhgroup is not used.</p>
<dt><code>&#8211;id=&lt;id&gt; or -n &lt;id&gt;</code></p>
<dd> Use &lt;id&gt; as the identification value. This option is only applicable to Aggressive Mode. &lt;id&gt; can be specified as a string, e.g. &#8211;id=test or as a hex value with a leading &quot;0x&quot;, e.g. &#8211;id=0xdeadbeef.</p>
<dt><code>&#8211;idtype=&lt;n&gt; or -y &lt;n&gt;</code></p>
<dd> Use identification type &lt;n&gt;. Default 3 (ID_USER_FQDN). This option is only applicable to Aggressive Mode. See RFC 2407 4.6.2 for details of Identification types.</p>
<dt><code>&#8211;dhgroup=&lt;n&gt; or -g &lt;n&gt;</code></p>
<dd> Use Diffie Hellman Group &lt;n&gt;. Default 2. This option is only applicable to Aggressive Mode and IKEv2. For both of these, it is used to determine the size of the key exchange payload. If you use Aggressive Mode with custom transforms, then you will normally need to use the &#8211;dhgroup option unless you are using the default DH group. Acceptable values are 1,2,5,14,15,16,17,18 (MODP only).</p>
<dt><code>&#8211;gssid=&lt;n&gt; or -G &lt;n&gt;</code></p>
<dd> Use GSS ID &lt;n&gt; where &lt;n&gt; is a hex string. This uses transform attribute type 16384 as specified in draft-ietf-ipsec-isakmp-gss-auth-07.txt, although Windows-2000 has been observed to use 32001 as well. For Windows 2000, you&#8217;ll need to use &#8211;auth=65001 to specify Kerberos (GSS) authentication.</p>
<dt><code>&#8211;random or -R</code></p>
<dd> Randomise the host list. This option randomises the order of the hosts in the host list, so the IKE probes are sent to the hosts in a random order. It uses the Knuth shuffle algorithm.</p>
<dt><code>&#8211;tcp[=&lt;n&gt;] or -T[&lt;n&gt;]</code></p>
<dd> Use TCP transport instead of UDP. This allows you to test a host running IKE over TCP. You won&#8217;t normally need this option because the vast majority of IPsec systems only support IKE over UDP. The optional value &lt;n&gt; specifies the type of IKE over TCP. There are currently two possible values: 1 = RAW IKE over TCP as used by Checkpoint (default); 2 = Encapsulated IKE over TCP as used by Cisco. If you are using the short form of the option (-T) then the value must immediately follow the option letter with no spaces, e.g. -T2 not -T 2. You can only specify a single target host if you use this option.</p>
<dt><code>&#8211;tcptimeout=&lt;n&gt; or -O &lt;n&gt;</code></p>
<dd> Set TCP connect timeout to &lt;n&gt; seconds (default=10). This is only applicable to TCP transport mode.</p>
<dt><code>&#8211;pskcrack[=&lt;f&gt;] or -P[&lt;f&gt;]</code></p>
<dd> Crack aggressive mode pre-shared keys. This option outputs the aggressive mode pre-shared key (PSK) parameters for offline cracking using the &quot;psk-crack&quot; program that is supplied with ike-scan. You can optionally specify a filename, &lt;f&gt;, to write the PSK parameters to. If you do not specify a filename then the PSK parameters are written to standard output. If you are using the short form of the option (-P) then the value must immediately follow the option letter with no spaces, e.g. -Pfile not -P file. You can only specify a single target host if you use this option. This option is only applicable to IKE aggressive mode.</p>
<dt><code>&#8211;nodns or -N</code></p>
<dd> Do not use DNS to resolve names. If you use this option, then all hosts must be specified as IP addresses.</p>
<dt><code>&#8211;noncelen=&lt;n&gt; or -c &lt;n&gt;</code></p>
<dd> Set the nonce length to &lt;n&gt; bytes. Default=20 This option controls the length of the nonce payload that is sent in an aggressive mode or IKEv2 request. Normally there is no need to use this option unless you want to reduce the nonce size to speed up pre-shared key cracking, or if you want to see how a particular server handles different length nonce payloads. RFC 2409 states that the length of nonce payload must be between 8 and 256 bytes, but ike-scan does not enforce this. Specifying a large nonce length will increase the size of the packet sent by ike-scan. A very large nonce length may cause fragmentation, or exceed the maximum IP packet size. This option is only applicable to IKE aggressive mode.</p>
<dt><code>&#8211;headerlen=&lt;n&gt; or -L &lt;n&gt;</code></p>
<dd> Set the length in the ISAKMP header to &lt;n&gt; bytes. You can use this option to manually specify the value to be used for the ISAKMP header length. By default, ike-scan will fill in the correct value. Use this option to manually specify an incorrect length. &lt;n&gt; can be specified as &quot;+n&quot; which sets the length to n bytes more than it should be, &quot;-n&quot; which sets it to n bytes less, or &quot;n&quot; which sets it to exactly bytes. Changing the header length to an incorrect value can sometimes disrupt VPN servers.</p>
<dt><code>&#8211;mbz=&lt;n&gt; or -Z &lt;n&gt;</code></p>
<dd> Use the value &lt;n&gt; for reserved (MBZ) fields, default=0. Specifying this option makes the outgoing packet non-RFC compliant, and should only be used if you want to see how a VPN server will respond to invalid packets. The value of &lt;n&gt; should be in the range 0-255.</p>
<dt><code>&#8211;headerver=&lt;n&gt; or -E &lt;n&gt;</code></p>
<dd> Specify the ISAKMP header version. The default is 0x10 (16) which corresponds to v1.0. Specifying a non-default value will make the outgoing packet non-RFC compliant, and should only be used if you want to see how the VPN server reacts to strange versions. The value should be in the range 0-255.</p>
<dt><code>&#8211;certreq=&lt;c&gt; or -C &lt;c&gt;</code></p>
<dd> Add the CertificateRequest payload &lt;c&gt;. &lt;c&gt; should be specified as a hex value. The first byte of the hex value will be interpreted as the certificate type; the remaining bytes as the certificate authority as described in RFC 2408 3.10. The certificate types are listed in RFC 2408 sec 3.9. RFC 2048 states &quot;The Certificate Request payload MUST be accepted at any point during the exchange&quot;</p>
<dt><code>&#8211;doi=&lt;d&gt; or -D &lt;d&gt;</code></p>
<dd> Set the SA DOI to &lt;d&gt;, default 1 (IPsec). You will not normally want to change this unless you want to see how the VPN server responds to a non-standard DOI.</p>
<dt><code>&#8211;situation=&lt;s&gt; or -S &lt;s&gt;</code></p>
<dd> Set the SA Situation to &lt;d&gt;, default 1. The meaning of the situation depends on the DOI, and is detailed in the appropriate DOI document. For the IPsec DOI, the default Situation of 1 represents SIT_IDENTITY_ONLY. You will not normally want to change this unless you want to see how the VPN server responds to a non-standard situation.</p>
<dt><code>&#8211;protocol=&lt;p&gt; or -j &lt;p&gt;</code></p>
<dd> Set the Proposal protocol ID to &lt;p&gt;, default 1. The meaning of the proposal protocol ID depends on the DOI, and is detailed in the appropriate DOI document. For the IPsec DOI, the default proposal protocol id of 1 represents PROTO_ISAKMP. You will not normally want to change this unless you want to see how the VPN server responds to a non-standard protocol ID.</p>
<dt><code>&#8211;transid=&lt;t&gt; or -k &lt;t&gt;</code></p>
<dd> Set the Transform ID to &lt;t&gt;, default 1. The meaning of the transform ID depends on the DOI, and is detailed in the appropriate DOI document. For the IPsec DOI, the default transform id of 1 represents KEY_IKE. You will not normally want to change this unless you want to see how the VPN server responds to a non-standard transform ID.</p>
<dt><code>&#8211;spisize=&lt;n&gt;</code></p>
<dd> Set the proposal SPI size to &lt;n&gt;. Default=0 If this is non-zero, then a random SPI of the specified size will be added to the proposal payload. The default of zero means no SPI.</p>
<dt><code>&#8211;hdrflags=&lt;n&gt;</code></p>
<dd> Set the ISAKMP header flags to &lt;n&gt;. Default=0 The flags are detailed in RFC 2408 section 3.1</p>
<dt><code>&#8211;hdrmsgid=&lt;n&gt;</code></p>
<dd> Set the ISAKMP header message ID to &lt;n&gt;. Default=0 This should be zero for IKE Phase-1.</p>
<dt><code>&#8211;cookie=&lt;n&gt;</code></p>
<dd> Set the ISAKMP initiator cookie to &lt;n&gt; The cookie value should be specified in hex. By default, the cookies are automatically generated and have unique values. If you specify this option, then you can only specify a single target, because ike-scan requires unique cookie values to match up the response packets.</p>
<dt><code>&#8211;exchange=&lt;n&gt;</code></p>
<dd> Set the exchange type to &lt;n&gt; This option allows you to change the exchange type in the ISAKMP header to an arbitrary value. Note that ike-scan only supports Main and Aggressive modes (values 2 and 4 respectively). Specifying other values will change the exchange type value in the ISAKMP header, but will not adjust the other payloads. The exchange types are defined in RFC 2408 sec 3.1.</p>
<dt><code>&#8211;nextpayload=&lt;n&gt;</code></p>
<dd> Set the next payload in the ISAKMP header to &lt;n&gt; Normally, the next payload is automatically set to the correct value.</p>
<dt><code>&#8211;randomseed=&lt;n&gt;</code></p>
<dd> Use &lt;n&gt; to seed the pseudo random number generator. This option seeds the PRNG with the specified number, which can be useful if you want to ensure that the packet data is exactly repeatable when it includes payloads with random data such as key exchange or nonce. By default, the PRNG is seeded with an unpredictable value.</p>
<dt><code>&#8211;timestamp</code></p>
<dd> Display timestamps for received packets. This option causes a timestamp to be displayed for each received packet.</p>
<dt><code>&#8211;sourceip=&lt;s&gt;</code></p>
<dd> Set source IP address for outgoing packets to &lt;s&gt;. This option causes the outgoing IKE packets to have the specified source IP address. The address can either be an IP address in dotted quad format, or the string &quot;random&quot; which will use a different random source address for each packet that is sent. If this option is used, no packets will be received This option requires raw socket support, and you will need superuser privileges to use this option, even if you specify a high source port. This option does not work on all operating systems.</p>
<dt><code>&#8211;shownum</code></p>
<dd> Display the host number for received packets. This displays the ordinal host number of the responding host before the IP address. It can be useful when sending many packets to the same target IP, to see if any probes are being ignored.</p>
<dt><code>&#8211;nat-t</code></p>
<dd> Use RFC 3947 NAT-Traversal encapsulation. This option adds the non-ESP marker to the beginning of outgoing packets and strips it from received packets, as described in RFC 3947. It also changes the default source port to 4500 and the default destination port to 4500, which are the ports for NAT-T IKE. These port numbers can be changed with the &#8211;sport and &#8211;dport options, providing they are used after the &#8211;nat-t option.</p>
<dt><code>&#8211;rcookie=&lt;n&gt;</code></p>
<dd> Set the ISAKMP responder cookie to &lt;n&gt;. This sets the responder cookie to the specified hex value. By default, the responder cookie is set to zero.</p>
<dt><code>&#8211;ikev2 or -2</code></p>
<dd> Use IKE version 2 This causes the outgoing packets to use IKEv2 format as defined in RFC 4306 instead of the default IKEv1 format. Any packets returned are automatically decoded as IKE or IKEv2 depending on their payloads irrespective of this option. The &#8211;ikev2 option is currently experimental. It has not been extensively tested, and it only supports sending the default proposal.</dl>
<h2>FILES</h2>
<dl>
<dt><i>/usr/local/share/ike-scan/ike-backoff-patterns</i></p>
<dd> List of UDP backoff patterns. Used when the &#8211;showbackoff option is specified.</p>
<dt><i>/usr/local/share/ike-scan/ike-vendor-ids</i></p>
<dd> List of known Vendor ID patterns.</dl>
<h2>AUTHOR</h2>
<p> Roy Hills &lt;Roy.Hills [at] nta-monitor.com&gt;</p>
<h2>SEE ALSO</h2>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/wiki/">http://www.nta-monitor.com/wiki/</a></i> The ike-scan wiki page. </p>
<p> <i><a rel="nofollow" href="http://www.nta-monitor.com/tools/ike-scan/">http://www.nta-monitor.com/tools/ike-scan/</a></i> The ike-scan homepage. </p>
<h2>Index</h2>
