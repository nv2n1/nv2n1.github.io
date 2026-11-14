---
title: "tc-pedit(8)"
name: "tc-pedit"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-pedit/"
description: "pedit – generic packet editor action"
---

<p>pedit &#8211; generic packet editor action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action pedit [ex] munge </code>{ <i>RAW_OP</i> | <i>LAYERED_OP</i> | <i>EXTENDED_LAYERED_OP</i> } [ <i>CONTROL</i> ] </p>
<pre><code>RAW_OP :=

offset OFFSET

{ u8 | u16 | u32 } [

AT_SPEC ] CMD_SPEC
AT_SPEC :=

at AT offmask MASK shift SHIFT
LAYERED_OP := {

    ip IPHDR_FIELD

    |
    ip BEYOND_IPHDR_FIELD

} CMD_SPEC
EXTENDED_LAYERED_OP := {

    eth ETHHDR_FIELD

    |
    ip IPHDR_FIELD

    |
    ip EX_IPHDR_FIELD

    |
    ip6 IP6HDR_FIELD

    |
    tcp TCPHDR_FIELD

    |
    udp UDPHDR_FIELD

} CMD_SPEC
ETHHDR_FIELD := {

    src | dst | type }
IPHDR_FIELD := {

    src | dst | tos | dsfield | ihl | protocol |

    precedence | nofrag | firstfrag | ce | df }
BEYOND_IPHDR_FIELD := {

    dport | sport | icmp_type | icmp_code }
EX_IPHDR_FIELD := {

    ttl }

IP6HDR_FIELD := {

    src | dst | traffic_class | flow_lbl | payload_len |

    nexthdr | hoplimit }
TCPHDR_FIELD := {

    sport | dport | flags }
UDPHDR_FIELD := {

    sport | dport }
CMD_SPEC := {

    clear | invert | set

    VAL |

    add

    VAL |

    decrement |

    preserve } [ retain

RVAL ]
CONTROL := {

    reclassify | pipe | drop | shot | continue | pass | goto chain CHAIN_INDEX }</code></pre>
<h2>Description</h2>
<p>The <code>pedit</code> action can be used to change arbitrary packet data. The location of data to change can either be specified by giving an offset and size as in <i>RAW_OP</i>, or for header values by naming the header and field to edit the size is then chosen automatically based on the header field size.</p>
<h2>Options</h2>
<dl>
<dt><code>ex</code></p>
<dd>Use extended pedit. <i>EXTENDED_LAYERED_OP</i> and the add/decrement <i>CMD_SPEC</i> are allowed only in this mode.</p>
<dt><code>offset</code><i> OFFSET </i>{ <code>u32 </code>| <code>u16 </code>| <code>u8 </code>}</p>
<dd>Specify the offset at which to change data. <i>OFFSET</i> is a signed integer, it&#8217;s base is automatically chosen (e.g. hex if prefixed by <code>0x</code> or octal if prefixed by <code>0</code>). The second argument specifies the length of data to change, that is four bytes (<code>u32</code>), two bytes (<code>u16</code>) or a single byte (<code>u8</code>).</p>
<dt><code>at</code><i> AT </i><code>offmask</code><i> MASK </i><code>shift</code><i> SHIFT</i></p>
<dd>This is an optional part of <i>RAW_OP</i> which allows to have a variable <i>OFFSET</i> depending on packet data at offset <i>AT</i>, which is binary ANDed with <i>MASK</i> and right-shifted by <i>SHIFT</i> before adding it to <i>OFFSET</i>.</p>
<dt><code>eth</code><i> ETHHDR_FIELD</i></p>
<dd>Change an ETH header field. The supported keywords for <i>ETHHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>src</code></p>
<dd><code>dst</code> Source or destination MAC address in the standard format: XX:XX:XX:XX:XX:XX</p>
<dt><code>type</code></p>
<dd>Ether-type in numeric value</dl>
</dl>
<dt><code>ip</code><i> IPHDR_FIELD</i></p>
<dd>Change an IPv4 header field. The supported keywords for <i>IPHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>src</code></p>
<dd><code>dst</code> Source or destination IP address, a four-byte value.</p>
<dt><code>tos</code></p>
<dd><code>dsfield</code> <code>precedence</code> Type Of Service field, an eight-bit value.</p>
<dt><code>ihl</code></p>
<dd>Change the IP Header Length field, a four-bit value.</p>
<dt><code>protocol</code></p>
<dd>Next-layer Protocol field, an eight-bit value.</p>
<dt><code>nofrag</code></p>
<dd><code>firstfrag</code> <code>ce</code> <code>df</code> <code>mf</code> Change IP header flags. Note that the value to pass to the <code>set</code> command is not just a bit value, but the full byte including the flags field. Though only the relevant bits of that value are respected, the rest ignored.</dl>
</dl>
<dt><code>ip</code><i> BEYOND_IPHDR_FIELD</i></p>
<dd>Supported only for non-extended layered op. It is passed to the kernel as offsets relative to the beginning of the IP header and assumes the IP header is of minimum size (20 bytes). The supported keywords for <i>BEYOND_IPHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>dport</code></p>
<dd><code>sport</code> Destination or source port numbers, a 16-bit value. Indeed, IPv4 headers don&#8217;t contain this information. Instead, this will set an offset which suits at least TCP and UDP if the IP header is of minimum size (20 bytes). If not, this will do unexpected things.</p>
<dt><code>icmp_type</code></p>
<dd><code>icmp_code</code> Again, this allows to change data past the actual IP header itself. It assumes an ICMP header is present immediately following the (minimal sized) IP header. If it is not or the latter is bigger than the minimum of 20 bytes, this will do unexpected things. These fields are eight-bit values.</dl>
</dl>
<dt><code>ip</code><i> EX_IPHDR_FIELD</i></p>
<dd>Supported only when <i>ex</i> is used. The supported keywords for <i>EX_IPHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>ttl</code></p>
<dd></dl>
</dl>
<dt><code>ip6</code><i> IP6HDR_FIELD</i></p>
<dd>The supported keywords for <i>IP6HDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>src</code></p>
<dd><code>dst</code> <code>traffic_class</code> <code>flow_lbl</code> <code>payload_len</code> <code>nexthdr</code> <code>hoplimit</code></dl>
</dl>
<dt><code>tcp</code><i> TCPHDR_FIELD</i></p>
<dd>The supported keywords for <i>TCPHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>sport</code></p>
<dd><code>dport</code> Source or destination TCP port number, a 16-bit value.</p>
<dt><code>flags</code></p>
<dd></dl>
</dl>
<dt><code>udp</code><i> UDPHDR_FIELD</i></p>
<dd>The supported keywords for <i>UDPHDR_FIELD</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>sport</code></p>
<dd><code>dport</code> Source or destination TCP port number, a 16-bit value.</dl>
</dl>
<dt><code>clear</code></p>
<dd>Clear the addressed data (i.e., set it to zero).</p>
<dt><code>invert</code></p>
<dd>Swap every bit in the addressed data.</p>
<dt><code>set</code><i> VAL</i></p>
<dd>Set the addressed data to a specific value. The size of <i>VAL</i> is defined by either one of the <code>u32</code>, <code>u16</code> or <code>u8</code> keywords in <i>RAW_OP</i>, or the size of the addressed header field in <i>LAYERED_OP</i>.</p>
<dt><code>add</code><i> VAL</i></p>
<dd>Add the addressed data by a specific value. The size of <i>VAL</i> is defined by the size of the addressed header field in <i>EXTENDED_LAYERED_OP</i>. This operation is supported only for extended layered op.</p>
<dt><code>decrement</code></p>
<dd>Decrease the addressed data by one. This operation is supported only for <code>ip</code> <code>ttl</code> and <code>ip6</code> <code>hoplimit</code>.</p>
<dt><code>preserve</code></p>
<dd>Keep the addressed data as is.</p>
<dt><code>retain</code><i> RVAL</i></p>
<dd>This optional extra part of <i>CMD_SPEC</i> allows to exclude bits from being changed. Supported only for 32 bits fields or smaller.</p>
<dt><i>CONTROL</i></p>
<dd>The following keywords allow to control how the tree of qdisc, classes, filters and actions is further traversed after this action.</p>
<dl>
<dd>
<dl>
<dt><code>reclassify</code></p>
<dd>Restart with the first filter in the current list.</p>
<dt><code>pipe</code></p>
<dd>Continue with the next action attached to the same filter.</p>
<dt><code>drop</code></p>
<dd><code>shot</code> Drop the packet.</p>
<dt><code>continue</code></p>
<dd>Continue classification with the next filter in line.</p>
<dt><code>pass</code></p>
<dd>Finish classification process and return to calling qdisc for further packet processing. This is the default.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>Being able to edit packet data, one could do all kinds of things, such as e.g. implementing port redirection. Certainly not the most useful application, but as an example it should do: First, qdiscs need to be set up to attach filters to. For the receive path, a simple <code>ingress</code> qdisc will do, for transmit path a classful qdisc (<code>HTB</code> in this case) is necessary:</p>
<dl>
<dd>tc qdisc replace dev eth0 root handle 1: htb tc qdisc add dev eth0 ingress handle ffff:</dl>
<p> Finally, a filter with <code>pedit</code> action can be added for each direction. In this case, <code>u32</code> is used matching on the port number to redirect from, while <code>pedit</code> then does the actual rewriting:</p>
<dl>
<dd>tc filter add dev eth0 parent 1: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip dport 23 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit pedit munge ip dport set 22<br />
 tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip sport 22 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit pedit munge ip sport set 23<br />
 tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip sport 22 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge ip dst set 192.168.1.199<br />
 tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip sport 22 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge ip6 dst set fe80::dacb:8aff:fec7:320e<br />
 tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip sport 22 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge eth dst set 11:22:33:44:55:66<br />
 tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip dport 23 0xffff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge tcp dport set 22
</dl>
<p> To rewrite just part of a field, use the <code>retain</code> directive. E.g. to overwrite the DSCP part of a dsfield with $DSCP, without touching ECN:</p>
<dl>
<dd>tc filter add dev eth0 ingress flower &#8230; \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge ip dsfield set $((DSCP &lt;&lt; 2)) retain 0xfc
</dl>
<p> And vice versa, to set ECN to e.g. 1 without impacting DSCP:</p>
<dl>
<dd>tc filter add dev eth0 ingress flower &#8230; \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit ex munge ip dsfield set 1 retain 0x3
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-htb/">tc-htb</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8) </p>
