---
title: "tc-flower(8)"
name: "tc-flower"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-flower/"
description: "flower – flow based traffic control filter"
---

<p>flower &#8211; flow based traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>flower</code> [ <i>MATCH_LIST</i> ] [ <code>action</code> <i>ACTION_SPEC</i> ] [ <code>classid</code> <i>CLASSID</i> ] [ <code>hw_tc</code> <i>TCID</i> ] </p>
<pre><code>MATCH_LIST := [ MATCH_LIST ] MATCH
MATCH := {

    indev

    ifname |

    verbose

    |

    skip_sw | skip_hw

    | {

        dst_mac | src_mac }

    MASKED_LLADDR |

    vlan_id

    VID |

    vlan_prio

    PRIORITY |

    vlan_ethtype { ipv4 | ipv6 |

        ETH_TYPE } |

    cvlan_id

    VID |

    cvlan_prio

    PRIORITY |

    cvlan_ethtype { ipv4 | ipv6 |

        ETH_TYPE } |

    mpls

    LSE_LIST |

    mpls_label

    LABEL |

    mpls_tc

    TC |

    mpls_bos

    BOS |

    mpls_ttl

    TTL |

    ip_proto { tcp | udp | sctp | icmp | icmpv6 |

        IP_PROTO } |

    ip_tos

    MASKED_IP_TOS |

    ip_ttl

    MASKED_IP_TTL | {

        dst_ip | src_ip }

    PREFIX | {

        dst_port | src_port } {

            MASKED_NUMBER |

            min_port_number-max_port_number } |

        tcp_flags

        MASKED_TCP_FLAGS |

        type

        MASKED_TYPE |

        code

        MASKED_CODE | {

            arp_tip | arp_sip }

        IPV4_PREFIX |

        arp_op { request | reply |

            OP } | {

                arp_tha | arp_sha }

            MASKED_LLADDR |

            enc_key_id

            KEY-ID | {

                enc_dst_ip | enc_src_ip } {

                    ipv4_address | ipv6_address } |

                enc_dst_port

                port_number |

                enc_tos

                TOS |

                enc_ttl

                TTL |

                {
                    geneve_opts

                    |
                    vxlan_opts

                    |
                    erspan_opts

                }
                OPTIONS |

                ip_flags

                IP_FLAGS }
            LSE_LIST := [ LSE_LIST ] LSE
            LSE :=

            lse depth

            DEPTH {

                label

                LABEL |

                tc

                TC |

                bos

                BOS |

                ttl

                TTL }
</code></pre>
<h2>Description</h2>
<p>The <code>flower</code> filter matches flows to the set of keys specified and assigns an arbitrarily chosen class ID to packets belonging to them. Additionally (or alternatively) an action from the generic action framework may be called.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Specify a class to pass matching packets on to. <i>CLASSID</i> is in the form <code>X</code>:<code>Y</code>, while <code>X</code> and <code>Y</code> are interpreted as numbers in hexadecimal format.</p>
<dt><code>hw_tc</code><i> TCID</i></p>
<dd>Specify a hardware traffic class to pass matching packets on to. TCID is in the range 0 through 15.</p>
<dt><code>indev</code><i> ifname</i></p>
<dd>Match on incoming interface name. Obviously this makes sense only for forwarded flows. <i>ifname</i> is the name of an interface which must exist at the time of <code>tc</code> invocation.</p>
<dt><code>verbose</code></p>
<dd>Enable verbose logging, including offloading errors when not using <code>skip_sw</code> flag.</p>
<dt><code>skip_sw</code></p>
<dd>Do not process filter by software. If hardware has no offload support for this filter, or TC offload is not enabled for the interface, operation will fail.</p>
<dt><code>skip_hw</code></p>
<dd>Do not process filter by hardware.</p>
<dt><code>dst_mac</code><i> MASKED_LLADDR</i></p>
<dd><code>src_mac</code><i> MASKED_LLADDR</i> Match on source or destination MAC address. A mask may be optionally provided to limit the bits of the address which are matched. A mask is provided by following the address with a slash and then the mask. It may be provided in LLADDR format, in which case it is a bitwise mask, or as a number of high bits to match. If the mask is missing then a match on all bits is assumed.</p>
<dt><code>vlan_id</code><i> VID</i></p>
<dd>Match on vlan tag id. <i>VID</i> is an unsigned 12bit value in decimal format.</p>
<dt><code>vlan_prio</code><i> PRIORITY</i></p>
<dd>Match on vlan tag priority. <i>PRIORITY</i> is an unsigned 3bit value in decimal format.</p>
<dt><code>vlan_ethtype</code><i> VLAN_ETH_TYPE</i></p>
<dd>Match on layer three protocol. <i>VLAN_ETH_TYPE</i> may be either <code>ipv4</code>, <code>ipv6</code> or an unsigned 16bit value in hexadecimal format. To match on QinQ packet, it must be 802.1Q or 802.1AD.</p>
<dt><code>cvlan_id</code><i> VID</i></p>
<dd>Match on QinQ inner vlan tag id. <i>VID</i> is an unsigned 12bit value in decimal format.</p>
<dt><code>cvlan_prio</code><i> PRIORITY</i></p>
<dd>Match on QinQ inner vlan tag priority. <i>PRIORITY</i> is an unsigned 3bit value in decimal format.</p>
<dt><code>cvlan_ethtype</code><i> VLAN_ETH_TYPE</i></p>
<dd>Match on QinQ layer three protocol. <i>VLAN_ETH_TYPE</i> may be either <code>ipv4</code>, <code>ipv6</code> or an unsigned 16bit value in hexadecimal format. </p>
<dt><code>mpls</code><i> LSE_LIST</i></p>
<dd>Match on the MPLS label stack. <i>LSE_LIST</i> is a list of Label Stack Entries, each introduced by the <code>lse</code> keyword. This option can&#8217;t be used together with the standalone <code>mpls_label</code>, <code>mpls_tc</code>, <code>mpls_bos</code> and <code>mpls_ttl</code> options.</p>
<dl>
<dd>
<dl>
<dt><code>lse</code><i> LSE_OPTIONS</i></p>
<dd>Match on an MPLS Label Stack Entry. <i>LSE_OPTIONS</i> is a list of options that describe the properties of the LSE to match.</p>
<dl>
<dd>
<dl>
<dt><code>depth</code><i> DEPTH</i></p>
<dd>The depth of the Label Stack Entry to consider. Depth starts at 1 (the outermost Label Stack Entry). The maximum usable depth may be limited by the kernel. This option is mandatory. <i>DEPTH</i> is an unsigned 8 bit value in decimal format.</p>
<dt><code>label</code><i> LABEL</i></p>
<dd>Match on the MPLS Label field at the specified <code>depth</code>. <i>LABEL</i> is an unsigned 20 bit value in decimal format.</p>
<dt><code>tc</code><i> TC</i></p>
<dd>Match on the MPLS Traffic Class field at the specified <code>depth</code>. <i>TC</i> is an unsigned 3 bit value in decimal format.</p>
<dt><code>bos</code><i> BOS</i></p>
<dd>Match on the MPLS Bottom Of Stack field at the specified <code>depth</code>. <i>BOS</i> is a 1 bit value in decimal format.</p>
<dt><code>ttl</code><i> TTL</i></p>
<dd>Match on the MPLS Time To Live field at the specified <code>depth</code>. <i>TTL</i> is an unsigned 8 bit value in decimal format.</dl>
</dl>
</dl>
</dl>
<dt><code>mpls_label</code><i> LABEL</i></p>
<dd>Match the label id in the outermost MPLS label stack entry. <i>LABEL</i> is an unsigned 20 bit value in decimal format.</p>
<dt><code>mpls_tc</code><i> TC</i></p>
<dd>Match on the MPLS TC field, which is typically used for packet priority, in the outermost MPLS label stack entry. <i>TC</i> is an unsigned 3 bit value in decimal format.</p>
<dt><code>mpls_bos</code><i> BOS</i></p>
<dd>Match on the MPLS Bottom Of Stack field in the outermost MPLS label stack entry. <i>BOS</i> is a 1 bit value in decimal format.</p>
<dt><code>mpls_ttl</code><i> TTL</i></p>
<dd>Match on the MPLS Time To Live field in the outermost MPLS label stack entry. <i>TTL</i> is an unsigned 8 bit value in decimal format.</p>
<dt><code>ip_proto</code><i> IP_PROTO</i></p>
<dd>Match on layer four protocol. <i>IP_PROTO</i> may be <code>tcp</code>, <code>udp</code>, <code>sctp</code>, <code>icmp</code>, <code>icmpv6</code> or an unsigned 8bit value in hexadecimal format.</p>
<dt><code>ip_tos</code><i> MASKED_IP_TOS</i></p>
<dd>Match on ipv4 TOS or ipv6 traffic-class &#8211; eight bits in hexadecimal format. A mask may be optionally provided to limit the bits which are matched. A mask is provided by following the value with a slash and then the mask. If the mask is missing then a match on all bits is assumed.</p>
<dt><code>ip_ttl</code><i> MASKED_IP_TTL</i></p>
<dd>Match on ipv4 TTL or ipv6 hop-limit &#8211; eight bits value in decimal or hexadecimal format. A mask may be optionally provided to limit the bits which are matched. Same logic is used for the mask as with matching on ip_tos.</p>
<dt><code>dst_ip</code><i> PREFIX</i></p>
<dd><code>src_ip</code><i> PREFIX</i> Match on source or destination IP address. <i>PREFIX</i> must be a valid IPv4 or IPv6 address, depending on the <code>protocol</code> option to tc filter, optionally followed by a slash and the prefix length. If the prefix is missing, <code>tc</code> assumes a full-length host match.</p>
<dt><i></i><code>dst_port</code> { <i>MASKED_NUMBER</i> | <i> MIN_VALUE-MAX_VALUE </i>}</p>
<dd><i></i><code>src_port</code> { <i>MASKED_NUMBER</i> | <i> MIN_VALUE-MAX_VALUE </i>} Match on layer 4 protocol source or destination port number, with an optional mask. Alternatively, the minimum and maximum values can be specified to match on a range of layer 4 protocol source or destination port numbers. Only available for <code>ip_proto</code> values <code>udp</code>, <code>tcp</code> and <code>sctp</code> which have to be specified in beforehand.</p>
<dt><code>tcp_flags</code><i> MASKED_TCP_FLAGS</i></p>
<dd>Match on TCP flags represented as 12bit bitfield in in hexadecimal format. A mask may be optionally provided to limit the bits which are matched. A mask is provided by following the value with a slash and then the mask. If the mask is missing then a match on all bits is assumed.</p>
<dt><code>type</code><i> MASKED_TYPE</i></p>
<dd><code>code</code><i> MASKED_CODE</i> Match on ICMP type or code. A mask may be optionally provided to limit the bits of the address which are matched. A mask is provided by following the address with a slash and then the mask. The mask must be as a number which represents a bitwise mask If the mask is missing then a match on all bits is assumed. Only available for <code>ip_proto</code> values <code>icmp</code> and <code>icmpv6</code> which have to be specified in beforehand.</p>
<dt><code>arp_tip</code><i> IPV4_PREFIX</i></p>
<dd><code>arp_sip</code><i> IPV4_PREFIX</i> Match on ARP or RARP sender or target IP address. <i>IPV4_PREFIX</i> must be a valid IPv4 address optionally followed by a slash and the prefix length. If the prefix is missing, <code>tc</code> assumes a full-length host match.</p>
<dt><code>arp_op</code><i> ARP_OP</i></p>
<dd>Match on ARP or RARP operation. <i>ARP_OP</i> may be <code>request</code>, <code>reply</code> or an integer value 0, 1 or 2. A mask may be optionally provided to limit the bits of the operation which are matched. A mask is provided by following the address with a slash and then the mask. It may be provided as an unsigned 8 bit value representing a bitwise mask. If the mask is missing then a match on all bits is assumed.</p>
<dt><code>arp_sha</code><i> MASKED_LLADDR</i></p>
<dd><code>arp_tha</code><i> MASKED_LLADDR</i> Match on ARP or RARP sender or target MAC address. A mask may be optionally provided to limit the bits of the address which are matched. A mask is provided by following the address with a slash and then the mask. It may be provided in LLADDR format, in which case it is a bitwise mask, or as a number of high bits to match. If the mask is missing then a match on all bits is assumed.</p>
<dt><code>enc_key_id</code><i> NUMBER</i></p>
<dd><code>enc_dst_ip</code><i> PREFIX</i> <code>enc_src_ip</code><i> PREFIX</i> <code>enc_dst_port</code><i> NUMBER</i> <code>enc_tos</code><i> NUMBER</i> <code>enc_ttl</code><i> NUMBER</i></p>
<dt><code>ct_state</code><i> CT_STATE</i></p>
<dd><code>ct_zone</code><i> CT_MASKED_ZONE</i> <code>ct_mark</code><i> CT_MASKED_MARK</i> <code>ct_label</code><i> CT_MASKED_LABEL</i> Matches on connection tracking info</p>
<dl>
<dd>
<dl>
<dt><i>CT_STATE</i></p>
<dd>Match the connection state, and can be combination of [{+|-}flag] flags, where flag can be one of</p>
<dl>
<dd>
<dl>
<dt>trk &#8211; Tracked connection.</p>
<dd>
<dt>new &#8211; New connection.</p>
<dd>
<dt>est &#8211; Established connection.</p>
<dd>
<dt>rpl &#8211; The packet is in the reply direction, meaning that it is in the opposite direction from the packet that initiated the connection.</p>
<dd>
<dt>inv &#8211; The state is invalid. The packet couldn&#8217;t be associated to a connection.</p>
<dd>
<dt>rel &#8211; The packet is related to an existing connection.</p>
<dd>
<dt>Example: +trk+est</p>
<dd></dl>
</dl>
<dt><i>CT_MASKED_ZONE</i></p>
<dd>Match the connection zone, and can be masked.</p>
<dt><i>CT_MASKED_MARK</i></p>
<dd>32bit match on the connection mark, and can be masked.</p>
<dt><i>CT_MASKED_LABEL</i></p>
<dd>128bit match on the connection label, and can be masked.</dl>
</dl>
<dt><code>geneve_opts</code><i> OPTIONS</i></p>
<dd><code>vxlan_opts</code><i> OPTIONS</i> <code>erspan_opts</code><i> OPTIONS</i> Match on IP tunnel metadata. Key id <i>NUMBER</i> is a 32 bit tunnel key id (e.g. VNI for VXLAN tunnel). <i>PREFIX</i> must be a valid IPv4 or IPv6 address optionally followed by a slash and the prefix length. If the prefix is missing, <code>tc</code> assumes a full-length host match. Dst port <i>NUMBER</i> is a 16 bit UDP dst port. Tos <i>NUMBER</i> is an 8 bit tos (dscp+ecn) value, ttl <i>NUMBER</i> is an 8 bit time-to-live value. geneve_opts <i>OPTIONS</i> must be a valid list of comma-separated geneve options where each option consists of a key optionally followed by a slash and corresponding mask. If the masks is missing, <code>tc</code> assumes a full-length match. The options can be described in the form CLASS:TYPE:DATA/CLASS_MASK:TYPE_MASK:DATA_MASK, where CLASS is represented as a 16bit hexadecimal value, TYPE as an 8bit hexadecimal value and DATA as a variable length hexadecimal value. vxlan_opts <i>OPTIONS</i> doesn&#8217;t support multiple options, and it consists of a key followed by a slash and corresponding mask. If the mask is missing, <code>tc</code> assumes a full-length match. The option can be described in the form GBP/GBP_MASK, where GBP is represented as a 32bit number. erspan_opts <i>OPTIONS</i> doesn&#8217;t support multiple options, and it consists of a key followed by a slash and corresponding mask. If the mask is missing, <code>tc</code> assumes a full-length match. The option can be described in the form VERSION:INDEX:DIR:HWID/VERSION:INDEX_MASK:DIR_MASK:HWID_MASK, where VERSION is represented as a 8bit number, INDEX as an 32bit number, DIR and HWID as a 8bit number. Multiple options is not supported. Note INDEX/INDEX_MASK is used when VERSION is 1, and DIR/DIR_MASK and HWID/HWID_MASK are used when VERSION is 2.</p>
<dt><code>ip_flags</code><i> IP_FLAGS</i></p>
<dd><i>IP_FLAGS</i> may be either <code>frag</code>, <code>nofrag</code>, <code>firstfrag</code> or <code>nofirstfrag</code> where frag and nofrag could be used to match on fragmented packets or not, respectively. firstfrag and nofirstfrag can be used to further distinguish fragmented packet. firstfrag can be used to indicate the first fragmented packet. nofirstfrag can be used to indicates subsequent fragmented packets or non-fragmented packets.</dl>
<h2>Notes</h2>
<p>As stated above where applicable, matches of a certain layer implicitly depend on the matches of the next lower layer. Precisely, layer one and two matches (<code>indev</code>, <code>dst_mac</code> and <code>src_mac</code>) have no dependency, MPLS and layer three matches (<code>mpls</code>, <code>mpls_label</code>, <code>mpls_tc</code>, <code>mpls_bos</code>, <code>mpls_ttl</code>, <code>ip_proto</code>, <code>dst_ip</code>, <code>src_ip</code>, <code>arp_tip</code>, <code>arp_sip</code>, <code>arp_op</code>, <code>arp_tha</code>, <code>arp_sha</code> and <code>ip_flags</code>) depend on the <code>protocol</code> option of tc filter, layer four port matches (<code>dst_port</code> and <code>src_port</code>) depend on <code>ip_proto</code> being set to <code>tcp</code>, <code>udp</code> or <code>sctp,</code> and finally ICMP matches (<code>code</code> and <code>type</code>) depend on <code>ip_proto</code> being set to <code>icmp</code> or <code>icmpv6.</code> </p>
<p> There can be only used one mask per one prio. If user needs to specify different mask, he has to use different prio.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-flow/">tc-flow</a></code>(8) </p>
