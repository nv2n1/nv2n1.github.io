---
title: "tc-u32(8)"
name: "tc-u32"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-u32/"
description: "u32 – universal 32bit traffic control filter"
---

<p>u32 &#8211; universal 32bit traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; [ <code>handle</code> <i>HANDLE</i> ] <code>u32</code> <i>OPTION_LIST</i> [ <code>offset</code> <i>OFFSET</i> ] [ <code>hashkey</code> <i>HASHKEY</i> ] [ <code>classid</code> <i>CLASSID</i> ] [ <code>divisor</code> <i>uint_value</i> ] [ <code>order</code> <i>u32_value</i> ] [ <code>ht</code> <i>HANDLE</i> ] [ <code>sample</code> <i>SELECTOR</i> [ <code>divisor</code> <i>uint_value</i> ] ] [ <code>link</code> <i>HANDLE</i> ] [ <code>indev</code> <i>ifname</i> ] [ <code>skip_hw</code> | <code>skip_sw</code> ] [ <code>help</code> ] </p>
<pre><code>HANDLE := {

    u12_hex_htid:[u8_hex_hash:[u12_hex_nodeid] | 0xu32_hex_value }
OPTION_LIST := [ OPTION_LIST ] OPTION
HASHKEY := [

mask

u32_hex_value ] [

at

4*int_value ]
CLASSID := {

    root |

    none |

    [u16_major]:u16_minor | u32_hex_value }
OFFSET := [

plus

int_value ] [

at

2*int_value ] [

mask

u16_hex_value ] [

shift

int_value ] [

eat ]
OPTION := {

    match

    SELECTOR |

    action

    ACTION }
SELECTOR := {

    u32

    VAL_MASK_32 |

    u16

    VAL_MASK_16 |

    u8

    VAL_MASK_8 |

    ip

    IP |

    ip6

    IP6 | {

        tcp | udp }

    TCPUDP |

    icmp

    ICMP |

    mark

    VAL_MASK_32 |

    ether

    ETHER }
IP := { {

    src | dst } { default | any | all |

    ip_address [

    / {

        prefixlen | netmask } ] } AT | {

            dsfield | ihl | protocol | precedence |

            icmp_type | icmp_code }

        VAL_MASK_8 | {

            sport | dport }

        VAL_MASK_16 |

        nofrag | firstfrag | df | mf }
    IP6 := { {

        src | dst } { default | any | all |

        ip6_address [/prefixlen ] } AT |

    priority

    VAL_MASK_8 | {

        protocol | icmp_type | icmp_code }

    VAL_MASK_8 |

    flowlabel

    VAL_MASK_32 | {

        sport | dport }

    VAL_MASK_16 }
TCPUDP := {

    src | dst }

VAL_MASK_16
ICMP := {

    type

    VAL_MASK_8 |

    code

    VAL_MASK_8 }
ETHER := {

    src | dst }

ether_address AT
VAL_MASK_32 := u32_value u32_hex_mask [ AT ]
VAL_MASK_16 := u16_value u16_hex_mask [ AT ]
VAL_MASK_8 := u8_value u8_hex_mask [ AT ]
AT := [

at [ nexthdr+ ]

int_value ]</code></pre>
<h2>Description</h2>
<p>The Universal/Ugly 32bit filter allows to match arbitrary bitfields in the packet. Due to breaking everything down to values, masks and offsets, It is equally powerful and hard to use. Luckily many abstracting directives are present which allow defining rules on a higher level and therefore free the user from having to fiddle with bits and masks in many cases. </p>
<p> There are two general modes of invocation: The first mode creates a new filter to delegate packets to different destinations. Apart from the obvious ones, namely classifying the packet by specifying a <i>CLASSID</i> or calling an <code>action</code>, one may <code>link</code> one filter to another one (or even a list of them), effectively organizing filters into a tree-like hierarchy. </p>
<p> Typically filter delegation is done by means of a hash table, which leads to the second mode of invocation: it merely serves to set up these hash tables. Filters can select a hash table and provide a key selector from which a hash is to be computed and used as key to lookup the table&#8217;s bucket which contains filters for further processing. This is useful if a high number of filters is in use, as the overhead of performing the hash operation and table lookup becomes negligible in that case. Using hashtables with <code>u32</code> basically involves the following pattern:</p>
<dl>
<dt>(1)</p>
<dd>Creating a new hash table, specifying it&#8217;s size using the <code>divisor</code> parameter and ideally a handle by which the table can be identified. If the latter is not given, the kernel chooses one on it&#8217;s own, which has to be guessed later.</p>
<dt>(2)</p>
<dd>Creating filters which link to the created table in <i>(1)</i> using the <code>link</code> parameter and defining the packet data which the kernel will use to calculate the <code>hashkey</code>.</p>
<dt>(3)</p>
<dd>Adding filters to buckets in the hash table from <i>(1)</i>. In order to avoid having to know how exactly the kernel creates the hash key, there is the <code>sample</code> parameter, which gives sample data to hash and thereby define the table bucket the filter should be added to. </p>
<p> In fact, even if not explicitly requested <code>u32</code> creates a hash table for every <code>priority</code> a filter is being added with. The table&#8217;s size is 1 though, so it is in fact merely a linked list.</dl>
<h2>Values</h2>
<p>Options and selectors require values to be specified in a specific format, which is often non-intuitive. Therefore the terminals in <i>SYNOPSIS</i> have been given descriptive names to indicate the required format and/or maximum allowed numeric value: Prefixes <i>u32</i>, <i>u16</i> and <i>u8</i> indicate four, two and single byte unsigned values. E.g. <i>u16</i> indicates a two byte-sized value in range between 0 and 65535 (0xFFFF) inclusive. A prefix of <i>int</i> indicates a four byte signed value. A middle part of <i>_hex_</i> indicates that the value is parsed in hexadecimal format. Otherwise, the value&#8217;s base is automatically detected, i.e. values prefixed with <i>0x</i> are considered hexadecimal, a leading <i>0</i> indicates octal format and decimal format otherwise. There are some values with special formatting as well: <i>ip_address</i> and <i>netmask</i> are in dotted-quad formatting as usual for IPv4 addresses. An <i>ip6_address</i> is specified in common, colon-separated hexadecimal format. Finally, <i>prefixlen</i> is an unsigned, decimal integer value in range from 0 to the address width in bits (32 for IPv4 and 128 for IPv6). </p>
<p> Sometimes values need to be dividable by a certain number. In that case a name of the form <i>N*val</i> was chosen, indicating that <i>val</i> must be dividable by <i>N</i>. Or the other way around: the resulting value must be a multiple of <i>N</i>.</p>
<h2>Options</h2>
<p><code>U32</code> recognizes the following options:</p>
<dl>
<dt><code>handle</code><i> HANDLE</i></p>
<dd>The handle is used to reference a filter and therefore must be unique. It consists of a hash table identifier <code>htid</code> and optional <code>hash</code> (which identifies the hash table&#8217;s bucket) and <code>nodeid</code>. All these values are parsed as unsigned, hexadecimal numbers with length 12bits ( <code>htid</code> and <code>nodeid</code>) or 8bits ( <code>hash</code>). Alternatively one may specify a single, 32bit long hex number which contains the three fields bits in concatenated form. Other than the fields themselves, it has to be prefixed by <code>0x</code>.</p>
<dt><code>offset</code><i> OFFSET</i></p>
<dd>Set an offset which defines where matches of subsequent filters are applied to. Therefore this option is useful only when combined with <code>link</code> or a combination of <code>ht</code> and <code>sample</code>. The offset may be given explicitly by using the <code>plus</code> keyword, or extracted from the packet data with <code>at</code>. It is possible to mangle the latter using <code>mask</code> and/or <code>shift</code> keywords. By default, this offset is recorded but not implicitly applied. It is used only to substitute the <code>nexthdr+</code> statement. Using the keyword <code>eat</code> though inverses this behaviour: the offset is applied always, and <code>nexthdr+</code> will fall back to zero.</p>
<dt><code>hashkey</code><i> HASHKEY</i></p>
<dd>Specify what packet data to use to calculate a hash key for bucket lookup. The kernel adjusts the value according to the hash table&#8217;s size. For this to work, the option <code>link</code> must be given.</p>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Classify matching packets into the given <i>CLASSID</i>, which consists of either 16bit <code>major</code> and <code>minor</code> numbers or a single 32bit value combining both.</p>
<dt><code>divisor</code><i> u32_value</i></p>
<dd>Specify a modulo value. Used when creating hash tables to define their size or for declaring a <code>sample</code> to calculate hash table keys from. Must be a power of two with exponent not exceeding eight.</p>
<dt><code>order</code><i> u32_value</i></p>
<dd>A value to order filters by, ascending. Conflicts with <code>handle</code> which serves the same purpose.</p>
<dt><code>sample</code><i> SELECTOR</i></p>
<dd>Used together with <code>ht</code> to specify which bucket to add this filter to. This allows one to avoid having to know how exactly the kernel calculates hashes. The additional <code>divisor</code> defaults to 256, so must be given for hash tables of different size.</p>
<dt><code>link</code><i> HANDLE</i></p>
<dd>Delegate matching packets to filters in a hash table. <i>HANDLE</i> is used to only specify the hash table, so only <code>htid</code> may be given, <code>hash</code> and <code>nodeid</code> have to be omitted. By default, bucket number 0 will be used and can be overridden by the <code>hashkey</code> option.</p>
<dt><code>indev</code><i> ifname</i></p>
<dd>Filter on the incoming interface of the packet. Obviously works only for forwarded traffic.</p>
<dt><code>skip_sw</code></p>
<dd>Do not process filter by software. If hardware has no offload support for this filter, or TC offload is not enabled for the interface, operation will fail.</p>
<dt><code>skip_hw</code></p>
<dd>Do not process filter by hardware.</p>
<dt><code>help</code></p>
<dd>Print a brief help text about possible options.</dl>
<h2>Selectors</h2>
<p>Basically the only real selector is <code>u32 .</code> All others merely provide a higher level syntax and are internally translated into <code>u32 .</code></p>
<dl>
<dt><code>u32</code><i> VAL_MASK_32</i></p>
<dd><code>u16</code><i> VAL_MASK_16</i> <code>u8</code><i> VAL_MASK_8</i> Match packet data to a given value. The selector name defines the sample length to extract (32bits for <code>u32</code>, 16bits for <code>u16</code> and 8bits for <code>u8</code>). Before comparing, the sample is binary AND&#8217;ed with the given mask. This way uninteresting bits can be cleared before comparison. The position of the sample is defined by the offset specified in <i>AT</i>.</p>
<dt><code>ip</code><i> IP</i></p>
<dd><code>ip6</code><i> IP6</i> Assume packet starts with an IPv4 ( <code>ip</code>) or IPv6 ( <code>ip6</code>) header. <i>IP</i>/<i>IP6</i> then allows to match various header fields:</p>
<dl>
<dd>
<dl>
<dt><code>src</code><i> ADDR</i></p>
<dd><code>dst</code><i> ADDR</i> Compare Source or Destination Address fields against the value of <i>ADDR</i>. The reserved words <code>default</code>, <code>any</code> and <code>all</code> effectively match any address. Otherwise an IP address of the particular protocol is expected, optionally suffixed by a prefix length to match whole subnets. In case of IPv4 a netmask may also be given.</p>
<dt><code>dsfield</code><i> VAL_MASK_8</i></p>
<dd>IPv4 only. Match the packet header&#8217;s DSCP/ECN field. Synonyms to this are <code>tos</code> and <code>precedence</code>.</p>
<dt><code>ihl</code><i> VAL_MASK_8</i></p>
<dd>IPv4 only. Match the Internet Header Length field. Note that the value&#8217;s unit is 32bits, so to match a packet with 24byte header length <i>u8_value</i> has to be 6.</p>
<dt><code>protocol</code><i> VAL_MASK_8</i></p>
<dd>Match the Protocol (IPv4) or Next Header (IPv6) field value, e.g. 6 for TCP.</p>
<dt><code>icmp_type</code><i> VAL_MASK_8</i></p>
<dd><code>icmp_code</code><i> VAL_MASK_8</i> Assume a next-header protocol of icmp or ipv6-icmp and match Type or Code field values. This is dangerous, as the code assumes minimal header size for IPv4 and lack of extension headers for IPv6.</p>
<dt><code>sport</code><i> VAL_MASK_16</i></p>
<dd><code>dport</code><i> VAL_MASK_16</i> Match layer four source or destination ports. This is dangerous as well, as it assumes a suitable layer four protocol is present (which has Source and Destination Port fields right at the start of the header and 16bit in size). Also minimal header size for IPv4 and lack of IPv6 extension headers is assumed.</p>
<dt><code>nofrag</code></p>
<dd><code>firstfrag</code> <code>df</code> <code>mf</code> IPv4 only, check certain flags and fragment offset values. Match if the packet is not a fragment (<code>nofrag</code>), the first fragment (<code>firstfrag</code>), if Don&#8217;t Fragment (<code>df</code>) or More Fragments (<code>mf</code>) bits are set.</p>
<dt><code>priority</code><i> VAL_MASK_8</i></p>
<dd>IPv6 only. Match the header&#8217;s Traffic Class field, which has the same purpose and semantics of IPv4&#8217;s ToS field since RFC 3168: upper six bits are DSCP, the lower two ECN.</p>
<dt><code>flowlabel</code><i> VAL_MASK_32</i></p>
<dd>IPv6 only. Match the Flow Label field&#8217;s value. Note that Flow Label itself is only 20bytes long, which are the least significant ones here. The remaining upper 12bytes match Version and Traffic Class fields.</dl>
</dl>
<dt><code>tcp</code><i> TCPUDP</i></p>
<dd><code>udp</code><i> TCPUDP</i> Match fields of next header of protocol TCP or UDP. The possible values for <i>TCPDUP</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>src</code><i> VAL_MASK_16</i></p>
<dd>Match on Source Port field value.</p>
<dt><code>dst</code><i> VALMASK_16</i></p>
<dd>Match on Destination Port field value.</dl>
</dl>
<dt><code>icmp</code><i> ICMP</i></p>
<dd>Match fields of next header of protocol ICMP. The possible values for <i>ICMP</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>type</code><i> VAL_MASK_8</i></p>
<dd>Match on ICMP Type field.</p>
<dt><code>code</code><i> VAL_MASK_8</i></p>
<dd>Match on ICMP Code field.</dl>
</dl>
<dt><code>mark</code><i> VAL_MASK_32</i></p>
<dd>Match on netfilter fwmark value.</p>
<dt><code>ether</code><i> ETHER</i></p>
<dd>Match on ethernet header fields. Possible values for <i>ETHER</i> are:</p>
<dl>
<dd>
<dl>
<dt><code>src</code><i> ether_address</i><i>AT</i></p>
<dd><code>dst</code><i> ether_address</i><i>AT</i> Match on source or destination ethernet address. This is dangerous: It assumes an ethernet header is present at the start of the packet. This will probably lead to unexpected things if used with layer three interfaces like e.g. tun or ppp.</dl>
</dl>
</dl>
<h2>Examples</h2>
<dl>
<dd>tc filter add dev eth0 parent 999:0 prio 99 protocol ip u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match ip src 192.168.8.0/24 classid 1:1</dl>
<p> This attaches a filter to the qdisc identified by <code>999:0.</code> It&#8217;s priority is <code>99</code>, which affects in which order multiple filters attached to the same <code>parent</code> are consulted (the lower the earlier). The filter handles packets of <code>protocol</code> type <code>ip</code>, and <code>match</code>es if the IP header&#8217;s source address is within the <code>192.168.8.0/24</code> subnet. Matching packets are classified into class <code>1.1</code>. The effect of this command might be surprising at first glance: </p>
<dl>
<dd>filter parent 1: protocol ip pref 99 u32 filter parent 1: protocol ip pref 99 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fh 800: ht divisor 1 filter parent 1: protocol ip pref 99 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match c0a80800/ffffff00 at 12</dl>
<p> So parent <code>1:</code> is assigned a new <code>u32</code> filter, which contains a hash table of size 1 (as the <code>divisor</code> indicates). The table ID is <code>800</code>. The third line then shows the actual filter which was added above: it sits in table <code>800</code> and bucket <code>0</code>, classifies packets into class ID <code>1:1</code> and matches the upper three bytes of the four byte value at offset <code>12</code> to be <code>0xc0a808</code>, which is 192, 168 and 8. </p>
<p> Now for something more complicated, namely creating a custom hash table: </p>
<dl>
<dd>tc filter add dev eth0 prio 99 handle 1: u32 divisor 256</dl>
<p> This creates a table of size 256 with handle <code>1:</code> in priority <code>99</code>. The effect is as follows: </p>
<dl>
<dd>filter parent 1: protocol all pref 99 u32 filter parent 1: protocol all pref 99 u32 fh 1: ht divisor 256 filter parent 1: protocol all pref 99 u32 fh 800: ht divisor 1</dl>
<p> So along with the requested hash table (handle <code>1:</code>), the kernel has created his own table of size 1 to hold other filters of the same priority. </p>
<p> The next step is to create a filter which links to the created hash table: </p>
<dl>
<dd>tc filter add dev eth0 parent 1: prio 1 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;link 1: hashkey mask 0x0000ff00 at 12&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match ip src 192.168.0.0/16</dl>
<p> The filter is given a lower priority than the hash table itself so <code>u32</code> consults it before manually traversing the hash table. The options <code>link</code> and <code>hashkey</code> determine which table and bucket to redirect to. In this case the hash key should be constructed out of the second byte at offset 12, which corresponds to an IP packet&#8217;s third byte of the source address field. Along with the <code>match</code> statement, this effectively maps all class C networks below 192.168.0.0/16 to different buckets of the hash table. </p>
<p> Filters for certain subnets can be created like so: </p>
<dl>
<dd>tc filter add dev eth0 parent 1: prio 99 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ht 1: sample u32 0x00000800 0x0000ff00 at 12&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match ip src 192.168.8.0/24 classid 1:1</dl>
<p> The bucket is defined using the <code>sample</code> option: In this case, the second byte at offset 12 must be 0x08, exactly. In this case, the resulting bucket ID is obviously 8, but as soon as <code>sample</code> selects an amount of data which could exceed the <code>divisor</code>, one would have to know the kernel-internal algorithm to deduce the destination bucket. This filter&#8217;s <code>match</code> statement is redundant in this case, as the entropy for the hash key does not exceed the table size and therefore no collisions can occur. Otherwise it&#8217;s necessary to prevent matching unwanted packets. </p>
<p> Matching upper layer fields is problematic since IPv4 header length is variable and IPv6 supports extension headers which affect upper layer header offset. To overcome this, there is the possibility to specify <code>nexthdr+</code> when giving an offset, and to make things easier there are the <code>tcp</code> and <code>udp</code> matches which use <code>nexthdr+</code> implicitly. This offset has to be calculated in beforehand though, and the only way to achieve that is by doing it in a separate filter which then links to the filter which wants to use it. Here is an example of doing so: </p>
<dl>
<dd>tc filter add dev eth0 parent 1:0 protocol ip handle 1: \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 divisor 1 tc filter add dev eth0 parent 1:0 protocol ip \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 ht 1:&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match tcp src 22 FFFF&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;classid 1:2 tc filter add dev eth0 parent 1:0 protocol ip \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;u32 ht 800:&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match ip protocol 6 FF&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match ip firstfrag&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;offset at 0 mask 0f00 shift 6&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;link 1:</dl>
<p> This is what is being done: In the first call, a single element sized hash table is created so there is a place to hold the linked to filter and a known handle (<code>1:</code>) to reference to it. The second call then adds the actual filter, which pushes packets with TCP source port 22 into class <code>1:2</code>. Using <code>ht</code>, it is moved into the hash table created by the first call. The third call then does the actual magic: It matches IPv4 packets with next layer protocol 6 (TCP), only if it&#8217;s the first fragment (usually TCP sets DF bit, but if it doesn&#8217;t and the packet is fragmented, only the first one contains the TCP header), and then sets the offset based on the IP header&#8217;s IHL field (right-shifting by 6 eliminates the offset of the field and at the same time converts the value into byte unit). Finally, using <code>link</code>, the hash table from first call is referenced which holds the filter from second call.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8),<br />
 <code>cls_u32.txt</code> at <code><a rel="nofollow" href="http://linux-tc-notes.sourceforge.net/">http://linux-tc-notes.sourceforge.net/</a></code> </p>
