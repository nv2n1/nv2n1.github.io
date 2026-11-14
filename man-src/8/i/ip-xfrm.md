---
title: "ip-xfrm(8)"
name: "ip-xfrm"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ip-xfrm/"
description: "ip-xfrm – transform configuration"
---

<p>ip-xfrm &#8211; transform configuration</p>
<h2>Synopsis</h2>
<pre><code>ip

[ OPTIONS ]

xfrm

{ COMMAND |

    help }

ip xfrm

XFRM-OBJECT { COMMAND |

    help }

XFRM-OBJECT :=

state | policy | monitor
</code></pre>
<p> <code>ip xfrm state</code> { <code>add</code> | <code>update</code> } <i>ID</i> [ <i>ALGO-LIST</i> ] [ <code>mode</code> <i>MODE</i> ] [ <code>mark</code> <i>MARK</i> [ <code>mask</code> <i>MASK</i> ] ] [ <code>reqid</code> <i>REQID</i> ] [ <code>seq</code> <i>SEQ</i> ] [ <code>replay-window</code> <i>SIZE</i> ] [ <code>replay-seq</code> <i>SEQ</i> ] [ <code>replay-oseq</code> <i>SEQ</i> ] [ <code>replay-seq-hi</code> <i>SEQ</i> ] [ <code>replay-oseq-hi</code> <i>SEQ</i> ] [ <code>flag</code> <i>FLAG-LIST</i> ] [ <code>sel</code> <i>SELECTOR</i> ] [ <i>LIMIT-LIST</i> ] [ <code>encap</code> <i>ENCAP</i> ] [ <code>coa</code> <i>ADDR</i>[/<i>PLEN</i>] ] [ <code>ctx</code> <i>CTX</i> ] [ <code>extra-flag</code> <i>EXTRA-FLAG-LIST</i> ] [ <code>output-mark</code> <i>OUTPUT-MARK</i> [ <code>mask</code> <i>MASK</i> ] ] [ <code>if_id</code> <i>IF-ID</i> ] [ <code>tfcpad</code> <i>LENGTH</i> ]<br />
 <code>ip xfrm state allocspi</code> <i>ID</i> [ <code>mode</code> <i>MODE</i> ] [ <code>mark</code> <i>MARK</i> [ <code>mask</code> <i>MASK</i> ] ] [ <code>reqid</code> <i>REQID</i> ] [ <code>seq</code> <i>SEQ</i> ] [ <code>min</code> <i>SPI</i> <code>max</code> <i>SPI</i> ]<br />
 <code>ip xfrm state</code> { <code>delete</code> | <code>get</code> } <i>ID</i> [ <code>mark</code> <i>MARK</i> [ <code>mask</code> <i>MASK</i> ] ]<br />
 <code>ip</code> [ <code>-4</code> | <code>-6</code> ] <code>xfrm state deleteall</code> [ <i>ID</i> ] [ <code>mode</code> <i>MODE</i> ] [ <code>reqid</code> <i>REQID</i> ] [ <code>flag</code> <i>FLAG-LIST</i> ]<br />
 <code>ip</code> [ <code>-4</code> | <code>-6</code> ] <code>xfrm state list</code> [ <i>ID</i> ] [ <code>nokeys</code> ] [ <code>mode</code> <i>MODE</i> ] [ <code>reqid</code> <i>REQID</i> ] [ <code>flag</code> <i>FLAG-LIST</i> ]<br />
 <code>ip xfrm state flush</code> [ <code>proto</code> <i>XFRM-PROTO</i> ]<br />
 <code>ip xfrm state count</code> ID :=</p>
<p>[ src</p>
<p>ADDR ]</p>
<p>[ dst</p>
<p>ADDR ]</p>
<p>[ proto</p>
<p>XFRM-PROTO ]</p>
<p>[ spi</p>
<p>SPI ]<br />
XFRM-PROTO :=</p>
<p>esp | ah | comp | route2 | hao<br />
ALGO-LIST := [ ALGO-LIST ] ALGO<br />
ALGO :=</p>
<p>{ enc | auth }</p>
<p>ALGO-NAME ALGO-KEYMAT |</p>
<p>auth-trunc</p>
<p>ALGO-NAME ALGO-KEYMAT ALGO-TRUNC-LEN |</p>
<p>aead</p>
<p>ALGO-NAME ALGO-KEYMAT ALGO-ICV-LEN |</p>
<p>comp</p>
<p>ALGO-NAME<br />
MODE :=</p>
<p>transport | tunnel | beet | ro | in_trigger<br />
FLAG-LIST := [ FLAG-LIST ] FLAG<br />
FLAG :=</p>
<p>noecn | decap-dscp | nopmtudisc | wildrecv | icmp |</p>
<p>af-unspec | align4 | esn<br />
SELECTOR :=</p>
<p>[ src</p>
<p>ADDR[/PLEN] ]</p>
<p>[ dst</p>
<p>ADDR[/PLEN] ]</p>
<p>[ dev</p>
<p>DEV ]</p>
<p>[ UPSPEC ]<br />
UPSPEC :=</p>
<p>proto {</p>
<p>    PROTO |</p>
<p>    { tcp | udp | sctp | dccp } [ sport</p>
<p>    PORT ]</p>
<p>    [ dport</p>
<p>    PORT ] |</p>
<p>    { icmp | ipv6-icmp | mobility-header } [ type</p>
<p>    NUMBER ]</p>
<p>    [ code</p>
<p>    NUMBER ] |</p>
<p>    gre [ key</p>
<p>    { DOTTED-QUAD | NUMBER } ] }<br />
LIMIT-LIST := [ LIMIT-LIST ]</p>
<p>limit</p>
<p>LIMIT<br />
LIMIT :=</p>
<p>{ time-soft | time-hard | time-use-soft | time-use-hard }</p>
<p>SECONDS |</p>
<p>{ byte-soft | byte-hard }</p>
<p>SIZE |</p>
<p>{ packet-soft | packet-hard }</p>
<p>COUNT<br />
ENCAP :=</p>
<p>{ espinudp | espinudp-nonike | espintcp }</p>
<p>SPORT DPORT OADDR<br />
EXTRA-FLAG-LIST := [ EXTRA-FLAG-LIST ] EXTRA-FLAG<br />
EXTRA-FLAG :=</p>
<p>dont-encap-dscp | oseq-may-wrap<br />
 <code>ip xfrm policy</code> { <code>add</code> | <code>update</code> } <i>SELECTOR</i> <code>dir</code> <i>DIR</i> [ <code>ctx</code> <i>CTX</i> ] [ <code>mark</code> <i>MARK</i> [ <code>mask</code> <i>MASK</i> ] ] [ <code>index</code> <i>INDEX</i> ] [ <code>ptype</code> <i>PTYPE</i> ] [ <code>action</code> <i>ACTION</i> ] [ <code>priority</code> <i>PRIORITY</i> ] [ <code>flag</code> <i>FLAG-LIST</i> ] [ <code>if_id</code> <i>IF-ID</i> ] [ <i>LIMIT-LIST</i> ] [ <i>TMPL-LIST</i> ]<br />
 <code>ip xfrm policy</code> { <code>delete</code> | <code>get</code> } { <i>SELECTOR</i> | <code>index</code> <i>INDEX</i> } <code>dir</code> <i>DIR</i> [ <code>ctx</code> <i>CTX</i> ] [ <code>mark</code> <i>MARK</i> [ <code>mask</code> <i>MASK</i> ] ] [ <code>ptype</code> <i>PTYPE</i> ] [ <code>if_id</code> <i>IF-ID</i> ]<br />
 <code>ip</code> [ <code>-4</code> | <code>-6</code> ] <code>xfrm policy</code> { <code>deleteall</code> | <code>list</code> } [ <code>nosock</code> ] [ <i>SELECTOR</i> ] [ <code>dir</code> <i>DIR</i> ] [ <code>index</code> <i>INDEX</i> ] [ <code>ptype</code> <i>PTYPE</i> ] [ <code>action</code> <i>ACTION</i> ] [ <code>priority</code> <i>PRIORITY</i> ] [ <code>flag</code> <i>FLAG-LIST</i>]<br />
 <code>ip xfrm policy flush</code> [ <code>ptype</code> <i>PTYPE</i> ]<br />
 <code>ip xfrm policy count</code><br />
 <code>ip xfrm policy set</code> [ <code>hthresh4</code> <i>LBITS</i> <i>RBITS</i> ] [ <code>hthresh6</code> <i>LBITS</i> <i>RBITS</i> ] SELECTOR :=</p>
<p>[ src</p>
<p>ADDR[/PLEN] ]</p>
<p>[ dst</p>
<p>ADDR[/PLEN] ]</p>
<p>[ dev</p>
<p>DEV ]</p>
<p>[ UPSPEC ]<br />
UPSPEC :=</p>
<p>proto {</p>
<p>    PROTO |</p>
<p>    { tcp | udp | sctp | dccp } [ sport</p>
<p>    PORT ]</p>
<p>    [ dport</p>
<p>    PORT ] |</p>
<p>    { icmp | ipv6-icmp | mobility-header } [ type</p>
<p>    NUMBER ]</p>
<p>    [ code</p>
<p>    NUMBER ] |</p>
<p>    gre [ key</p>
<p>    { DOTTED-QUAD | NUMBER } ] }<br />
DIR :=</p>
<p>in | out | fwd<br />
PTYPE :=</p>
<p>main | sub<br />
ACTION :=</p>
<p>allow | block<br />
FLAG-LIST := [ FLAG-LIST ] FLAG<br />
FLAG :=</p>
<p>localok | icmp<br />
LIMIT-LIST := [ LIMIT-LIST ]</p>
<p>limit</p>
<p>LIMIT<br />
LIMIT :=</p>
<p>{ time-soft | time-hard | time-use-soft | time-use-hard }</p>
<p>SECONDS |</p>
<p>{ byte-soft | byte-hard }</p>
<p>SIZE |</p>
<p>{ packet-soft | packet-hard }</p>
<p>COUNT<br />
TMPL-LIST := [ TMPL-LIST ]</p>
<p>tmpl</p>
<p>TMPL<br />
TMPL := ID</p>
<p>[ mode</p>
<p>MODE ]</p>
<p>[ reqid</p>
<p>REQID ]</p>
<p>[ level</p>
<p>LEVEL ]<br />
ID :=</p>
<p>[ src</p>
<p>ADDR ]</p>
<p>[ dst</p>
<p>ADDR ]</p>
<p>[ proto</p>
<p>XFRM-PROTO ]</p>
<p>[ spi</p>
<p>SPI ]<br />
XFRM-PROTO :=</p>
<p>esp | ah | comp | route2 | hao<br />
MODE :=</p>
<p>transport | tunnel | beet | ro | in_trigger<br />
LEVEL :=</p>
<p>required | use<br />
 <code>ip xfrm monitor</code> [ <code>all-nsid</code> ] [ <code>nokeys</code> ] [ <code>all</code><br />
&nbsp;| <i>LISTofXFRM-OBJECTS</i> ] </p>
<pre><code>LISTofXFRM-OBJECTS := [ LISTofXFRM-OBJECTS ] XFRM-OBJECT
XFRM-OBJECT :=

acquire | expire | SA | policy | aevent | report

</code></pre>
<h2>Description</h2>
<p>xfrm is an IP framework for transforming packets (such as encrypting their payloads). This framework is used to implement the IPsec protocol suite (with the <code>state</code> object operating on the Security Association Database, and the <code>policy</code> object operating on the Security Policy Database). It is also used for the IP Payload Compression Protocol and features of Mobile IPv6. </p>
<table>
<tr VALIGN=top>
<td>ip xfrm state add</td>
<td>add new state into xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state update</td>
<td>update existing state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state allocspi</td>
<td>allocate an SPI value
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state delete</td>
<td>delete existing state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state get</td>
<td>get existing state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state deleteall</td>
<td>delete all existing state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state list</td>
<td>print out the list of existing state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state flush</td>
<td>flush all state in xfrm
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm state count</td>
<td>count all existing state in xfrm
</td>
</tr>
</table>
<dl>
<dt><i>ID</i></p>
<dd>is specified by a source address, destination address, transform protocol <i>XFRM-PROTO</i>, and/or Security Parameter Index <i>SPI</i>. (For IP Payload Compression, the Compression Parameter Index or CPI is used for <i>SPI</i>.)</p>
<dt><i>XFRM-PROTO</i></p>
<dd>specifies a transform protocol: IPsec Encapsulating Security Payload (<code>esp</code>), IPsec Authentication Header (<code>ah</code>), IP Payload Compression (<code>comp</code>), Mobile IPv6 Type 2 Routing Header (<code>route2</code>), or Mobile IPv6 Home Address Option (<code>hao</code>).</p>
<dt><i>ALGO-LIST</i></p>
<dd>contains one or more algorithms to use. Each algorithm <i>ALGO</i> is specified by:</p>
<dl>
<dd>
<dl>
<dt>&bull;</p>
<dd>the algorithm type: encryption (<code>enc</code>), authentication (<code>auth</code> or <code>auth-trunc</code>), authenticated encryption with associated data (<code>aead</code>), or compression (<code>comp</code>)</p>
<dt>&bull;</p>
<dd>the algorithm name <i>ALGO-NAME</i> (see below)</p>
<dt>&bull;</p>
<dd>(for all except <code>comp</code>) the keying material <i>ALGO-KEYMAT</i>, which may include both a key and a salt or nonce value; refer to the corresponding RFC</p>
<dt>&bull;</p>
<dd>(for <code>auth-trunc</code> only) the truncation length <i>ALGO-TRUNC-LEN</i> in bits</p>
<dt>&bull;</p>
<dd>(for <code>aead</code> only) the Integrity Check Value length <i>ALGO-ICV-LEN</i> in bits</dl>
</dl>
<dl>
<dd>Encryption algorithms include <code>ecb(cipher_null)</code>, <code>cbc(des)</code>, <code>cbc(des3_ede)</code>, <code>cbc(cast5)</code>, <code>cbc(blowfish)</code>, <code>cbc(aes)</code>, <code>cbc(serpent)</code>, <code>cbc(camellia)</code>, <code>cbc(twofish)</code>, and <code>rfc3686(ctr(aes))</code>. Authentication algorithms include <code>digest_null</code>, <code>hmac(md5)</code>, <code>hmac(sha1)</code>, <code>hmac(sha256)</code>, <code>hmac(sha384)</code>, <code>hmac(sha512)</code>, <code>hmac(rmd160)</code>, and <code>xcbc(aes)</code>. Authenticated encryption with associated data (AEAD) algorithms include <code>rfc4106(gcm(aes))</code>, <code>rfc4309(ccm(aes))</code>, and <code>rfc4543(gcm(aes))</code>. Compression algorithms include <code>deflate</code>, <code>lzs</code>, and <code>lzjh</code>.</dl>
<dt><i>MODE</i></p>
<dd>specifies a mode of operation for the transform protocol. IPsec and IP Payload Compression modes are <code>transport</code>, <code>tunnel</code>, and (for IPsec ESP only) Bound End-to-End Tunnel (<code>beet</code>). Mobile IPv6 modes are route optimization (<code>ro</code>) and inbound trigger (<code>in_trigger</code>).</p>
<dt><i>FLAG-LIST</i></p>
<dd>contains one or more of the following optional flags: <code>noecn</code>, <code>decap-dscp</code>, <code>nopmtudisc</code>, <code>wildrecv</code>, <code>icmp</code>, <code>af-unspec</code>, <code>align4</code>, or <code>esn</code>.</p>
<dt><i>SELECTOR</i></p>
<dd>selects the traffic that will be controlled by the policy, based on the source address, the destination address, the network device, and/or <i>UPSPEC</i>.</p>
<dt><i>UPSPEC</i></p>
<dd>selects traffic by protocol. For the <code>tcp</code>, <code>udp</code>, <code>sctp</code>, or <code>dccp</code> protocols, the source and destination port can optionally be specified. For the <code>icmp</code>, <code>ipv6-icmp</code>, or <code>mobility-header</code> protocols, the type and code numbers can optionally be specified. For the <code>gre</code> protocol, the key can optionally be specified as a dotted-quad or number. Other protocols can be selected by name or number <i>PROTO</i>.</p>
<dt><i>LIMIT-LIST</i></p>
<dd>sets limits in seconds, bytes, or numbers of packets.</p>
<dt><i>ENCAP</i></p>
<dd>encapsulates packets with protocol <code>espinudp</code>, <code>espinudp-nonike</code>, or <code>espintcp</code>, using source port <i>SPORT</i>, destination port <i>DPORT</i> , and original address <i>OADDR</i>.</p>
<dt><i>MARK</i></p>
<dd>used to match xfrm policies and states</p>
<dt><i>OUTPUT-MARK</i></p>
<dd>used to set the output mark to influence the routing of the packets emitted by the state</p>
<dt><i>IF-ID</i></p>
<dd>xfrm interface identifier used to in both xfrm policies and states  </p>
<table>
<tr VALIGN=top>
<td>ip xfrm policy add</td>
<td>add a new policy
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy update</td>
<td>update an existing policy
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy delete</td>
<td>delete an existing policy
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy get</td>
<td>get an existing policy
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy deleteall</td>
<td>delete all existing xfrm policies
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy list</td>
<td>print out the list of xfrm policies
</td>
</tr>
<tr VALIGN=top>
<td>ip xfrm policy flush</td>
<td>flush policies
</td>
</tr>
</table>
<dl>
<dt><code>nosock</code></p>
<dd>filter (remove) all socket policies from the output.</p>
<dt><i>SELECTOR</i></p>
<dd>selects the traffic that will be controlled by the policy, based on the source address, the destination address, the network device, and/or <i>UPSPEC</i>.</p>
<dt><i>UPSPEC</i></p>
<dd>selects traffic by protocol. For the <code>tcp</code>, <code>udp</code>, <code>sctp</code>, or <code>dccp</code> protocols, the source and destination port can optionally be specified. For the <code>icmp</code>, <code>ipv6-icmp</code>, or <code>mobility-header</code> protocols, the type and code numbers can optionally be specified. For the <code>gre</code> protocol, the key can optionally be specified as a dotted-quad or number. Other protocols can be selected by name or number <i>PROTO</i>.</p>
<dt><i>DIR</i></p>
<dd>selects the policy direction as <code>in</code>, <code>out</code>, or <code>fwd</code>.</p>
<dt><i>CTX</i></p>
<dd>sets the security context.</p>
<dt><i>PTYPE</i></p>
<dd>can be <code>main</code> (default) or <code>sub</code>.</p>
<dt><i>ACTION</i></p>
<dd>can be <code>allow</code> (default) or <code>block</code>.</p>
<dt><i>PRIORITY</i></p>
<dd>is a number that defaults to zero.</p>
<dt><i>FLAG-LIST</i></p>
<dd>contains one or both of the following optional flags: <code>local</code> or <code>icmp</code>.</p>
<dt><i>LIMIT-LIST</i></p>
<dd>sets limits in seconds, bytes, or numbers of packets.</p>
<dt><i>TMPL-LIST</i></p>
<dd>is a template list specified using <i>ID</i>, <i>MODE</i>, <i>REQID</i>, and/or <i>LEVEL</i>.</p>
<dt><i>ID</i></p>
<dd>is specified by a source address, destination address, transform protocol <i>XFRM-PROTO</i>, and/or Security Parameter Index <i>SPI</i>. (For IP Payload Compression, the Compression Parameter Index or CPI is used for <i>SPI</i>.)</p>
<dt><i>XFRM-PROTO</i></p>
<dd>specifies a transform protocol: IPsec Encapsulating Security Payload (<code>esp</code>), IPsec Authentication Header (<code>ah</code>), IP Payload Compression (<code>comp</code>), Mobile IPv6 Type 2 Routing Header (<code>route2</code>), or Mobile IPv6 Home Address Option (<code>hao</code>).</p>
<dt><i>MODE</i></p>
<dd>specifies a mode of operation for the transform protocol. IPsec and IP Payload Compression modes are <code>transport</code>, <code>tunnel</code>, and (for IPsec ESP only) Bound End-to-End Tunnel (<code>beet</code>). Mobile IPv6 modes are route optimization (<code>ro</code>) and inbound trigger (<code>in_trigger</code>).</p>
<dt><i>LEVEL</i></p>
<dd>can be <code>required</code> (default) or <code>use</code>.  </p>
<table>
<tr VALIGN=top>
<td>ip xfrm policy count</td>
<td>count existing policies
</td>
</tr>
</table>
<p> Use one or more -s options to display more details, including policy hash table information. </p>
<table>
<tr VALIGN=top>
<td>ip xfrm policy set</td>
<td>configure the policy hash table
</td>
</tr>
</table>
<p> Security policies whose address prefix lengths are greater than or equal policy hash table thresholds are hashed. Others are stored in the policy_inexact chained list.</p>
<dl>
<dt><i>LBITS</i></p>
<dd>specifies the minimum local address prefix length of policies that are stored in the Security Policy Database hash table.</p>
<dt><i>RBITS</i></p>
<dd>specifies the minimum remote address prefix length of policies that are stored in the Security Policy Database hash table.  </p>
<table>
<tr VALIGN=top>
<td>ip xfrm monitor </td>
<td>state monitoring for xfrm objects
</td>
</tr>
</table>
<p> The xfrm objects to monitor can be optionally specified. If the <code>all-nsid</code> option is set, the program listens to all network namespaces that have a nsid assigned into the network namespace were the program is running. A prefix is displayed to show the network namespace where the message originates. Example: [nsid 1]Flushed state proto 0 </p>
<h2>Author</h2>
<p>Manpage revised by David Ward &lt;david.ward [at] ll.mit.edu&gt;<br />
 Manpage revised by Christophe Gouault &lt;christophe.gouault [at] 6wind.com&gt;<br />
 Manpage revised by Nicolas Dichtel &lt;nicolas.dichtel [at] 6wind.com&gt;</p>
