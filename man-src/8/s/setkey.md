---
title: "setkey(8)"
name: "setkey"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setkey/"
description: "setkey – manually manipulate the IPsec SA/SP database"
---

<p><code>setkey</code> &#8211; manually manipulate the IPsec SA/SP database</p>
<h2>Synopsis</h2>
<p><code>setkey</code> [-<code>knrv</code> ] <i>file &#8230;</i><br />
<code>setkey</code> [-<code>knrv</code> ] &#8211;<code>c</code><br />
<code>setkey</code> [-<code>krv</code> ] &#8211;<code>f </code><i>filename</i><br />
<code>setkey</code> [-<code>aklPrv</code> ] &#8211;<code>D</code><br />
<code>setkey</code> [-<code>Pvp</code> ] &#8211;<code>F</code><br />
<code>setkey</code> [-<code>H</code> ] &#8211;<code>x</code><br />
<code>setkey</code> [-<code>?V</code> ]</p>
<h2>Description</h2>
<p><code>setkey</code> adds, updates, dumps, or flushes Security Association Database (SAD) entries as well as Security Policy Database (SPD) entries in the kernel. <code>setkey</code> takes a series of operations from standard input Po if invoked with &#8211;<code>c</code> Pc or the file named <i>filename</i> Po if invoked with &#8211;<code>f </code><i>filename</i> Pc .</p>
<dl>
<dt><code>(no flag)</code></p>
<dd>Dump the SAD entries or SPD entries contained in the specified <i>file</i></p>
<dt><code>&#8211; </code></p>
<dd>Print short help.</p>
<dt><code>-a</code></p>
<dd><code>setkey</code> usually does not display dead SAD entries with &#8211;<code>D</code> If &#8211;<code>a</code> is also specified, the dead SAD entries will be displayed as well. A dead SAD entry is one that has expired but remains in the system because it is referenced by some SPD entries.</p>
<dt><code>-D</code></p>
<dd>Dump the SAD entries. If &#8211;<code>P</code> is also specified, the SPD entries are dumped. If &#8211;<code>p</code> is specified, the ports are displayed.</p>
<dt><code>-F</code></p>
<dd>Flush the SAD entries. If &#8211;<code>P</code> is also specified, the SPD entries are flushed.</p>
<dt><code>-H</code></p>
<dd>Add hexadecimal dump in &#8211;<code>x</code> mode.</p>
<dt><code>-h</code></p>
<dd>On Nx , synonym for &#8211;<code>H</code> On other systems, synonym for &#8211;<code>?</code></p>
<dt><code>-k</code></p>
<dd>Use semantics used in kernel. Available only in Linux. See also &#8211;<code>r</code></p>
<dt><code>-l</code></p>
<dd>Loop forever with short output on &#8211;<code>D</code></p>
<dt><code>-n</code></p>
<dd>No action. The program will check validity of the input, but no changes to the SPD will be made.</p>
<dt><code>-r</code></p>
<dd>Use semantics described in IPsec RFCs. This mode is default. For details see section Sx RFC vs Linux kernel semantics . Available only in Linux. See also &#8211;<code>k</code></p>
<dt><code>-x</code></p>
<dd>Loop forever and dump all the messages transmitted to the <code>PF_KEY</code> socket. &#8211;<code>xx</code> prints the unformatted timestamps.</p>
<dt><code>-V</code></p>
<dd>Print version string.</p>
<dt><code>-v</code></p>
<dd>Be verbose. The program will dump messages exchanged on the <code>PF_KEY</code> socket, including messages sent from other processes to the kernel.</dl>
<h3>Configuration syntax</h3>
<p>With &#8211;<code>c</code> or &#8211;<code>f</code> on the command line, <code>setkey</code> accepts the following configuration syntax. Lines starting with hash signs (`#&#8217; ) are treated as comment lines.</p>
<dl>
<dt><code>add </code>[-<code>46n </code><i>src dst protocol spi</i> ]</p>
<dd>Oo Ar extensions Oc Ar algorithm &#8230; Li ; Add an SAD entry. <code>add</code> can fail for multiple reasons, including when the key length does not match the specified algorithm.</p>
<dt><code>get </code>[-<code>46n </code><i>src dst protocol spi </i><code>;</code> ]</p>
<dd>Show an SAD entry.</p>
<dt><code>delete </code>[-<code>46n </code><i>src dst protocol spi </i><code>;</code> ]</p>
<dd>Remove an SAD entry.</p>
<dt><code>deleteall </code>[-<code>46n </code><i>src dst protocol </i><code>;</code> ]</p>
<dd>Remove all SAD entries that match the specification.</p>
<dt><code>flush </code>[<i>protocol </i><code>;</code> ]</p>
<dd>Clear all SAD entries matched by the options. &#8211;<code>F</code> on the command line achieves the same functionality.</p>
<dt><code>dump </code>[<i>protocol </i><code>;</code> ]</p>
<dd>Dumps all SAD entries matched by the options. &#8211;<code>D</code> on the command line achieves the same functionality.</p>
<dt><code>spdadd </code>[-<code>46n </code><i>src_range dst_range upperspec</i> ]</p>
<dd>Ar label Ar policy Li ; Add an SPD entry.</p>
<dt><code>spdadd tagged </code><i>tag policy </i><code>;</code></p>
<dd>Add an SPD entry based on a PF tag. <i>tag</i> must be a string surrounded by double quotes.</p>
<dt><code>spdupdate </code>[-<code>46n </code><i>src_range dst_range upperspec</i> ]</p>
<dd>Ar label Ar policy Li ; Updates an SPD entry.</p>
<dt><code>spdupdate tagged </code><i>tag policy </i><code>;</code></p>
<dd>Update an SPD entry based on a PF tag. <i>tag</i> must be a string surrounded by double quotes.</p>
<dt><code>spddelete </code>[-<code>46n </code><i>src_range dst_range upperspec</i> ]</p>
<dd>Fl P Ar direction Li ; Delete an SPD entry.</p>
<dt><code>spdflush ;</code></p>
<dd>Clear all SPD entries. &#8211;<code>FP</code> on the command line achieves the same functionality.</p>
<dt><code>spddump ;</code></p>
<dd>Dumps all SPD entries. &#8211;<code>DP</code> on the command line achieves the same functionality.</dl>
<p> Meta-arguments are as follows: </p>
<dt><i>src</i></p>
<dd>
<dt><i>dst</i></p>
<dd>Source/destination of the secure communication is specified as an IPv4/v6 address, and an optional port number between square brackets. <code>setkey</code> can resolve a FQDN into numeric addresses. If the FQDN resolves into multiple addresses, <code>setkey</code> will install multiple SAD/SPD entries into the kernel by trying all possible combinations. &#8211;<code>4</code> &#8211;<code>6</code> and &#8211;<code>n</code> restrict the address resolution of FQDN in certain ways. &#8211;<code>4</code> and &#8211;<code>6</code> restrict results into IPv4/v6 addresses only, respectively. &#8211;<code>n</code> avoids FQDN resolution and requires addresses to be numeric addresses.</p>
<dt><i>protocol</i></p>
<dd><i>protocol</i> is one of following:</p>
<dl>
<dt><code>esp</code></p>
<dd>ESP based on rfc2406</p>
<dt><code>esp-old</code></p>
<dd>ESP based on rfc1827</p>
<dt><code>ah</code></p>
<dd>AH based on rfc2402</p>
<dt><code>ah-old</code></p>
<dd>AH based on rfc1826</p>
<dt><code>ipcomp</code></p>
<dd>IPComp</p>
<dt><code>tcp</code></p>
<dd>TCP-MD5 based on rfc2385</dl>
<dt><i>spi</i></p>
<dd>Security Parameter Index (SPI) for the SAD and the SPD. <i>spi</i> must be a decimal number, or a hexadecimal number with a &#8220;<code>0x</code> &#8221; prefix. SPI values between 0 and 255 are reserved for future use by IANA and cannot be used. TCP-MD5 associations must use 0x1000 and therefore only have per-host granularity at this time.</p>
<dt><i>extensions</i></p>
<dd>take some of the following:</p>
<dl>
<dt><code>-m </code><i>mode</i></p>
<dd>Specify a security protocol mode for use. <i>mode</i> is one of following: <code>transport , tunnel</code> or <code>any</code> The default value is <code>any</code></p>
<dt><code>-r </code><i>size</i></p>
<dd>Specify window size of bytes for replay prevention. <i>size</i> must be decimal number in 32-bit word. If <i>size</i> is zero or not specified, replay checks don&#8217;t take place.</p>
<dt><code>-u </code><i>id</i></p>
<dd>Specify the identifier of the policy entry in the SPD. See <i>policy</i></p>
<dt><code>-f </code><i>pad_option</i></p>
<dd>defines the content of the ESP padding. <i>pad_option</i> is one of following:</p>
<dl>
<dt><code>zero-pad</code></p>
<dd>All the paddings are zero.</p>
<dt><code>random-pad</code></p>
<dd>A series of randomized values are used.</p>
<dt><code>seq-pad</code></p>
<dd>A series of sequential increasing numbers started from 1 are used.</dl>
<dt><code>-f nocyclic-seq</code></p>
<dd>Don&#8217;t allow cyclic sequence numbers.</p>
<dt><code>-lh </code><i>time</i></p>
<dd>
<dt><code>-ls </code><i>time</i></p>
<dd>Specify hard/soft life time duration of the SA measured in seconds.</p>
<dt><code>-bh </code><i>bytes</i></p>
<dd>
<dt><code>-bs </code><i>bytes</i></p>
<dd>Specify hard/soft life time duration of the SA measured in bytes transported.</p>
<dt><code>-ctx </code><i>doi algorithm context-name</i></p>
<dd>Specify an access control label. The access control label is interpreted by the LSM (e.g., SELinux). Ultimately, it enables MAC on network communications.</p>
<dl>
<dt><i>doi</i></p>
<dd>The domain of interpretation, which is used by the IKE daemon to identify the domain in which negotiation takes place.</p>
<dt><i>algorithm</i></p>
<dd>Indicates the LSM for which the label is generated (e.g., SELinux).</p>
<dt><i>context-name</i></p>
<dd>The string representation of the label that is interpreted by the LSM.</dl>
<dt><i>algorithm</i></p>
<dd>
<dl>
<dt><code>-E </code><i>ealgo key</i></p>
<dd>Specify an encryption algorithm <i>ealgo</i> for ESP.</p>
<dt><code>-E </code><i>ealgo key &#8211;</i><code>A </code><i>aalgo key</i></p>
<dd>Specify an encryption algorithm <i>ealgo</i> as well as a payload authentication algorithm <i>aalgo</i> for ESP.</p>
<dt><code>-A </code><i>aalgo key</i></p>
<dd>Specify an authentication algorithm for AH.</p>
<dt><code>-C </code><i>calgo </i>[-<code>R</code> ]</p>
<dd>Specify a compression algorithm for IPComp. If &#8211;<code>R</code> is specified, the <i>spi</i> field value will be used as the IPComp CPI (compression parameter index) on wire as-is. If &#8211;<code>R</code> is not specified, the kernel will use well-known CPI on wire, and <i>spi</i> field will be used only as an index for kernel internal usage.</dl>
<p> <i>key</i> must be a double-quoted character string, or a series of hexadecimal digits preceded by &#8220;<code>0x</code> &#8221; Possible values for <i>ealgo</i> <i>aalgo</i> and <i>calgo</i> are specified in the Sx Algorithms sections.</p>
<dt><i>src_range</i></p>
<dd>
<dt><i>dst_range</i></p>
<dd>These select the communications that should be secured by IPsec. They can be an IPv4/v6 address or an IPv4/v6 address range, and may be accompanied by a TCP/UDP port specification. This takes the following form: </p>
<pre><i>address</i>
<i>address/prefixlen</i>
<i>address[port]</i>
<i>address/prefixlen[port]</i></pre>
<p><i>prefixlen</i> and <i>port</i> must be decimal numbers. The square brackets around <i>port</i> are really necessary, they are not man page meta-characters. For FQDN resolution, the rules applicable to <i>src</i> and <i>dst</i> apply here as well.</p>
<dt><i>upperspec</i></p>
<dd>Upper-layer protocol to be used. You can use one of the words in /etc/protocols as <i>upperspec</i> or <code>icmp6</code> <code>ip4</code> <code>gre</code> or <code>any</code> <code>any</code> stands for &#8220;any protocol&#8221; You can also use the protocol number. Additional specification can be placed after the protocol name for some protocols. You can specify a type and/or a code of ICMP or ICMPv6. The type is separated from a code by single comma and the code must always be specified. GRE key can be specified in dotted-quad format or as plain number. When a zero is specified, the kernel deals with it as a wildcard. Note that the kernel can not distinguish a wildcard from an ICPMv6 type of zero. For example, the following means that the policy doesn&#8217;t require IPsec for any inbound Neighbor Solicitation. </p>
<blockquote><p><tt>spdadd ::/0 ::/0 icmp6 135,0 -P in none</tt></p></blockquote>
<p> A second example of requiring transport mode encryption of specific GRE tunnel: </p>
<blockquote><p><tt>spdadd 0.0.0.0 0.0.0.0 gre 1234 ipsec esp/transport//require</tt></p></blockquote>
<p> <i>Note</i> <i>upperspec</i> does not work against forwarding case at this moment, as it requires extra reassembly at the forwarding node (not implemented at this moment) There are many protocols in /etc/protocols but all protocols except of TCP, UDP, GRE, and ICMP may not be suitable to use with IPsec. You have to consider carefully what to use.</p>
<dt><i>label</i></p>
<dd><i>label</i> is the access control label for the policy. This label is interpreted by the LSM (e.g., SELinux). Ultimately, it enables MAC on network communications. When a policy contains an access control label, SAs negotiated with this policy will contain the label. Its format:</p>
<dl>
<dt><code>-ctx </code><i>doi algorithm context-name</i></p>
<dd>
<dl>
<dt><i>doi</i></p>
<dd>The domain of interpretation, which is used by the IKE daemon to identify the domain in which negotiation takes place.</p>
<dt><i>algorithm</i></p>
<dd>Indicates the LSM for which the label is generated (e.g., SELinux).</p>
<dt><i>context-name</i></p>
<dd>The string representation of the label that is interpreted by the LSM.</dl>
<dt><i>policy</i></p>
<dd><i>policy</i> is in one of the following three formats:</p>
<dl>
<dt><code>-P </code><i>direction [priority specification] </i><code>discard</code></p>
<dd>
<dt><code>-P </code><i>direction [priority specification] </i><code>none</code></p>
<dd>
<dt><code>-P </code><i>direction [priority specification] </i><code>ipsec</code></p>
<dd><i>protocol/mode/src-dst/level </i>[&#8230;]</dl>
<p> You must specify the direction of its policy as <i>direction</i> Either <i>out</i> <i>in</i> or <i>fwd</i> can be used. <i>priority specification</i> is used to control the placement of the policy within the SPD. Policy position is determined by a signed integer where higher priorities indicate the policy is placed closer to the beginning of the list and lower priorities indicate the policy is placed closer to the end of the list. Policies with equal priorities are added at the end of groups of such policies. Priority can only be specified when setkey has been compiled against kernel headers that support policy priorities (Linux &gt;= 2.6.6). If the kernel does not support priorities, a warning message will be printed the first time a priority specification is used. Policy priority takes one of the following formats:</p>
<dl>
<dt><i>{priority,prio} offset</i></p>
<dd><i>offset</i> is an integer in the range from -2147483647 to 214783648.</p>
<dt><i>{priority,prio} base {+,-} offset</i></p>
<dd><i>base</i> is either <code>low (-1073741824)</code> <code>def (0)</code> or <code>high (1073741824)</code> <i>offset</i> is an unsigned integer. It can be up to 1073741824 for positive offsets, and up to 1073741823 for negative offsets.</dl>
<p> <code>discard</code> means the packet matching indexes will be discarded. <code>none</code> means that IPsec operation will not take place onto the packet. <code>ipsec</code> means that IPsec operation will take place onto the packet. The <i>protocol/mode/src-dst/level</i> part specifies the rule how to process the packet. Either <code>ah</code> <code>esp</code> or <code>ipcomp</code> must be used as <i>protocol</i> <i>mode</i> is either <code>transport</code> or <code>tunnel</code> If <i>mode</i> is <code>tunnel</code> you must specify the end-point addresses of the SA as <i>src</i> and <i>dst</i> with `-&#8216; between these addresses, which is used to specify the SA to use. If <i>mode</i> is <code>transport</code> both <i>src</i> and <i>dst</i> can be omitted. <i>level</i> is to be one of the following: <code>default , use , require</code> or <code>unique</code> If the SA is not available in every level, the kernel will ask the key exchange daemon to establish a suitable SA. <code>default</code> means the kernel consults the system wide default for the protocol you specified, e.g. the <code>esp_trans_deflev</code> sysctl variable, when the kernel processes the packet. <code>use</code> means that the kernel uses an SA if it&#8217;s available, otherwise the kernel keeps normal operation. <code>require</code> means SA is required whenever the kernel sends a packet matched with the policy. <code>unique</code> is the same as <code>require</code> in addition, it allows the policy to match the unique out-bound SA. You just specify the policy level <code>unique</code> <a href="/docs/linux/man/8-racoon/">racoon</a>(8) will configure the SA for the policy. If you configure the SA by manual keying for that policy, you can put a decimal number as the policy identifier after <code>unique</code> separated by a colon `:&#8217; like: <code>unique:number</code> in order to bind this policy to the SA. <code>number</code> must be between 1 and 32767. It corresponds to <i>extensions &#8211;</i><code>u</code> of the manual SA configuration. When you want to use SA bundle, you can define multiple rules. For example, if an IP header was followed by an AH header followed by an ESP header followed by an upper layer protocol header, the rule would be: </p>
<blockquote><p><tt>esp/transport//require ah/transport//require</tt></p></blockquote>
<p> The rule order is very important. When NAT-T is enabled in the kernel, policy matching for ESP over UDP packets may be done on endpoint addresses and port (this depends on the system. System that do not perform the port check cannot support multiple endpoints behind the same NAT). When using ESP over UDP, you can specify port numbers in the endpoint addresses to get the correct matching. Here is an example: </p>
<pre>spdadd 10.0.11.0/24[any] 10.0.11.33/32[any] any -P out ipsec
 esp/tunnel/192.168.0.1[4500]-192.168.1.2[30000]/require ;</pre>
<p>These ports must be left unspecified (which defaults to 0) for anything other than ESP over UDP. They can be displayed in SPD dump using <code>setkey</code> &#8211;<code>D  Note that &#8220;<code>discard</code> &#8221; and &#8220;<code>none</code> &#8221; are not in the syntax described in ipsec_set_policy3. There are a few differences in the syntax. See ipsec_set_policy3 for detail.</dl>
<h3>Algorithms</h3>
<p>The following list shows the supported algorithms. <code>protocol</code> and <code>algorithm</code> are almost orthogonal. These authentication algorithms can be used as <i>aalgo</i> in &#8211;<code>A </code><i>aalgo</i> of the <i>protocol</i> parameter: </p>
<blockquote>
<pre>algorithm keylen (bits)
hmac-md5 128 ah: rfc2403
 128 ah-old: rfc2085
hmac-sha1 160 ah: rfc2404
 160 ah-old: 128bit ICV (no document)
keyed-md5 128 ah: 96bit ICV (no document)
 128 ah-old: rfc1828
keyed-sha1 160 ah: 96bit ICV (no document)
 160 ah-old: 128bit ICV (no document)
null 0 to 2048 for debugging
hmac-sha256 256 ah: 96bit ICV
 (draft-ietf-ipsec-ciph-sha-256-00)
 256 ah-old: 128bit ICV (no document)
hmac-sha384 384 ah: 96bit ICV (no document)
 384 ah-old: 128bit ICV (no document)
hmac-sha512 512 ah: 96bit ICV (no document)
 512 ah-old: 128bit ICV (no document)
hmac-ripemd160 160 ah: 96bit ICV (RFC2857)
 ah-old: 128bit ICV (no document)
aes-xcbc-mac 128 ah: 96bit ICV (RFC3566)
 128 ah-old: 128bit ICV (no document)
tcp-md5 8 to 640 tcp: rfc2385</pre>
</blockquote>
<p> These encryption algorithms can be used as <i>ealgo</i> in &#8211;<code>E </code><i>ealgo</i> of the <i>protocol</i> parameter: </p>
<blockquote>
<pre>algorithm keylen (bits)
des-cbc 64 esp-old: rfc1829, esp: rfc2405
3des-cbc 192 rfc2451
null 0 to 2048 rfc2410
blowfish-cbc 40 to 448 rfc2451
cast128-cbc 40 to 128 rfc2451
des-deriv 64 ipsec-ciph-des-derived-01
3des-deriv 192 no document
rijndael-cbc 128/192/256 rfc3602
twofish-cbc 0 to 256 draft-ietf-ipsec-ciph-aes-cbc-01
aes-ctr 160/224/288 draft-ietf-ipsec-ciph-aes-ctr-03
camellia-cbc 128/192/256 rfc4312</pre>
</blockquote>
<p> Note that the first 128 bits of a key for <code>aes-ctr</code> will be used as AES key, and the remaining 32 bits will be used as nonce. These compression algorithms can be used as <i>calgo</i> in &#8211;<code>C </code><i>calgo</i> of the <i>protocol</i> parameter: </p>
<blockquote>
<pre>algorithm
deflate rfc2394</pre>
</blockquote>
<h3>RFC vs Linux kernel semantics</h3>
<p>The Linux kernel uses the <i>fwd</i> policy instead of the <i>in</i> policy for packets what are forwarded through that particular box. In <i>kernel</i> mode, <code>setkey</code> manages and shows policies and SAs exactly as they are stored in the kernel. In <i>RFC</i> mode, <code>setkey</code></p>
<dl>
<dt><code>creates</code></p>
<dd><i>fwd</i> policies for every <i>in</i> policy inserted</p>
<dt><code>(not implemented yet) filters out all</code></p>
<dd><i>fwd</i> policies</dl>
<h2>Return Values</h2>
<p>The command exits with 0 on success, and non-zero on errors.</p>
<h2>Examples</h2>
<pre>add 3ffe:501:4819::1 3ffe:501:481d::1 esp 123457
 -E des-cbc 0x3ffe05014819ffff ;
add -6 myhost.example.com yourhost.example.com ah 123456
 -A hmac-sha1 &quot;AH SA configuration!&quot; ;
add 10.0.11.41 10.0.11.33 esp 0x10001
 -E des-cbc 0x3ffe05014819ffff
 -A hmac-md5 &quot;authentication!!&quot; ;
get 3ffe:501:4819::1 3ffe:501:481d::1 ah 123456 ;
flush ;
dump esp ;
spdadd 10.0.11.41/32[21] 10.0.11.33/32[any] any
 -P out ipsec esp/tunnel/192.168.0.1-192.168.1.2/require ;
add 10.1.10.34 10.1.10.36 tcp 0x1000 -A tcp-md5 &quot;TCP-MD5 BGP secret&quot; ;
add 10.0.11.41 10.0.11.33 esp 0x10001
 -ctx 1 1 &quot;system_u:system_r:unconfined_t:SystemLow-SystemHigh&quot;
 -E des-cbc 0x3ffe05014819ffff;
spdadd 10.0.11.41 10.0.11.33 any
 -ctx 1 1 &quot;system_u:system_r:unconfined_t:SystemLow-SystemHigh&quot;
 -P out ipsec esp/transport//require ;</pre>
<h2>See Also</h2>
<p>ipsec_set_policy3, <a href="/docs/linux/man/8-racoon/">racoon</a>(8), <a href="/docs/linux/man/8-sysctl/">sysctl</a>(8)</p>
<dl>
<dd><i>&quot;Changed manual key configuration for IPsec&quot;</i> &quot;October 1999&quot;</dl>
<h2>History</h2>
<p>The <code>setkey</code> command first appeared in the WIDE Hydrangea IPv6 protocol stack kit. The command was completely re-designed in June 1998.</p>
<h2>Bugs</h2>
<p><code>setkey</code> should report and handle syntax errors better. For IPsec gateway configuration, <i>src_range</i> and <i>dst_range</i> with TCP/UDP port numbers does not work, as the gateway does not reassemble packets (it cannot inspect upper-layer headers) </p>
