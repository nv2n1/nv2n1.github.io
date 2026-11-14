---
title: "tc-flow(8)"
name: "tc-flow"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-flow/"
description: "flow – flow based traffic control filter"
---

<p>flow &#8211; flow based traffic control filter</p>
<h2>Synopsis</h2>
<dl>
<dt>Mapping mode:</p>
<dd>
<dl>
<dd><code>tc</code> <code>filter</code> &#8230; <code>flow map key </code> <i>KEY</i> [ <i>OPS</i> ] [ <i>OPTIONS</i> ]</dl>
<dt>Hashing mode:</p>
<dd>
<dl>
<dd><code>tc</code> <code>filter</code> &#8230; <code>flow hash keys </code> <i>KEY_LIST</i> [ <code>perturb</code> <i>secs</i> ] [ <i>OPTIONS</i> ]</dl>
<pre><code>OPS := [ OPS ] OP
OPTIONS := [

divisor

NUM ] [

baseclass

ID ] [

match

EMATCH_TREE ] [

action

ACTION_SPEC ]
KEY_LIST := [ KEY_LIST ] KEY
OP := {

    or | and | xor | rshift | addend }

NUM
ID := X:Y
KEY := {

    src | dst | proto | proto-src | proto-dst | iif |

    priority | mark | nfct | nfct-src | nfct-dst |

    nfct-proto-src | nfct-proto-dst | rt-classid | sk-uid |

    sk-gid | vlan-tag | rxhash }</code></pre>
<h2>Description</h2>
<p>The <code>flow</code> classifier is meant to extend the <code>SFQ</code> hashing capabilities without hard-coding new hash functions. It also allows deterministic mappings of keys to classes.</p>
<h2>Options</h2>
<dl>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</p>
<dt><code>baseclass</code><i> ID</i></p>
<dd>An offset for the resulting class ID. <i>ID</i> may be <code>root</code>, <code>none</code> or a hexadecimal class ID in the form [<i>X</i><code>:</code>]<i>Y</i>. <i>X</i> must match qdisc&#8217;s/class&#8217;s major handle (if omitted, the correct value is chosen automatically). If the whole <code>baseclass</code> is omitted, <i>Y</i> defaults to 1.</p>
<dt><code>divisor</code><i> NUM</i></p>
<dd>Number of buckets to use for sorting into. Keys are calculated modulo <i>NUM</i>.</p>
<dt><code>hash keys </code><i>KEY-LIST</i></p>
<dd>Perform a <code>jhash2</code> operation over the keys in <i>KEY-LIST</i>, the result (modulo the <code>divisor</code> if given) is taken as class ID, optionally offset by the value of <code>baseclass</code>. It is possible to specify an interval (in seconds) after which <code>jhash2</code>&#8216;s entropy source is recreated using the <code>perturb</code> parameter.</p>
<dt><code>map key </code><i>KEY</i></p>
<dd>Packet data identified by <i>KEY</i> is translated into class IDs to push the packet into. The value may be mangled by <i>OPS</i> before using it for the mapping. They are applied in the order listed here:</p>
<dl>
<dd>
<dl>
<dt><code>and</code><i> NUM</i></p>
<dd>Perform bitwise <code>AND</code> operation with numeric value <i>NUM</i>.</p>
<dt><code>or</code><i> NUM</i></p>
<dd>Perform bitwise <code>OR</code> operation with numeric value <i>NUM</i>.</p>
<dt><code>xor</code><i> NUM</i></p>
<dd>Perform bitwise <code>XOR</code> operation with numeric value <i>NUM</i>.</p>
<dt><code>rshift</code><i> NUM</i></p>
<dd>Shift the value of <i>KEY</i> to the right by <i>NUM</i> bits.</p>
<dt><code>addend</code><i> NUM</i></p>
<dd>Add <i>NUM</i> to the value of <i>KEY</i>. </p>
</dl>
</dl>
<dl>
<dd>For the <code>or</code>, <code>and</code>, <code>xor</code> and <code>rshift</code> operations, <i>NUM</i> is assumed to be an unsigned, 32bit integer value. For the <code>addend</code> operation, <i>NUM</i> may be much more complex: It may be prefixed by a minus (&#8216;-&#8216;) sign to cause subtraction instead of addition and for keys of <code>src</code>, <code>dst</code>, <code>nfct-src</code> and <code>nfct-dst</code> it may be given in IP address notation. See below for an illustrating example.</dl>
<dt><code>match</code><i> EMATCH_TREE</i></p>
<dd>Match packets using the extended match infrastructure. See <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) for a detailed description of the allowed syntax in <i>EMATCH_TREE</i>.</dl>
<h2>Keys</h2>
<p>In mapping mode, a single key is used (after optional permutation) to build a class ID. The resulting ID is deducible in most cases. In hashing more, a number of keys may be specified which are then hashed and the output used as class ID. This ID is not deducible in beforehand, and may even change over time for a given flow if a <code>perturb</code> interval has been given. </p>
<p> The range of class IDs can be limited by the <code>divisor</code> option, which is used for a modulus.</p>
<dl>
<dt><code>src</code>, <code>dst</code></p>
<dd>Use source or destination address as key. In case of IPv4 and TIPC, this is the actual address value. For IPv6, the 128bit address is folded into a 32bit value by XOR&#8217;ing the four 32bit words. In all other cases, the kernel-internal socket address is used (after folding into 32bits on 64bit systems).</p>
<dt><code>proto</code></p>
<dd>Use the layer four protocol number as key.</p>
<dt><code>proto-src</code></p>
<dd>Use the layer four source port as key. If not available, the kernel-internal socket address is used instead.</p>
<dt><code>proto-dst</code></p>
<dd>Use the layer four destination port as key. If not available, the associated kernel-internal dst_entry address is used after XOR&#8217;ing with the packet&#8217;s layer three protocol number.</p>
<dt><code>iif</code></p>
<dd>Use the incoming interface index as key.</p>
<dt><code>priority</code></p>
<dd>Use the packet&#8217;s priority as key. Usually this is the IP header&#8217;s DSCP/ECN value.</p>
<dt><code>mark</code></p>
<dd>Use the netfilter <code>fwmark</code> as key.</p>
<dt><code>nfct</code></p>
<dd>Use the associated conntrack entry address as key.</p>
<dt><code>nfct-src</code>, <code>nfct-dst</code>, <code>nfct-proto-src</code>, <code>nfct-proto-dst</code></p>
<dd>These are conntrack-aware variants of <code>src</code>, <code>dst</code>, <code>proto-src</code> and <code>proto-dst</code>. In case of NAT, these are basically the packet header&#8217;s values before NAT was applied.</p>
<dt><code>rt-classid</code></p>
<dd>Use the packet&#8217;s destination routing table entry&#8217;s realm as key.</p>
<dt><code>sk-uid</code></p>
<dd><code>sk-gid</code> For locally generated packets, use the user or group ID the originating socket belongs to as key.</p>
<dt><code>vlan-tag</code></p>
<dd>Use the packet&#8217;s vlan ID as key.</p>
<dt><code>rxhash</code></p>
<dd>Use the flow hash as key. </p>
</dl>
<h2>Examples</h2>
<dl>
<dt>Classic SFQ hash:</p>
<dd>tc filter add &#8230; flow hash \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>keys src,dst,proto,proto-src,proto-dst divisor 1024</p>
<dt>Classic SFQ hash, but using information from conntrack to work properly in combination with NAT:</p>
<dd>tc filter add &#8230; flow hash \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>keys nfct-src,nfct-dst,proto,nfct-proto-src,nfct-proto-dst \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>divisor 1024</p>
<dt>Map destination IPs of 192.168.0.0/24 to classids 1-256:</p>
<dd>tc filter add &#8230; flow map \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>key dst addend -192.168.0.0 divisor 256</p>
<dt>Alternative to the above:</p>
<dd>tc filter add &#8230; flow map \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>key dst and 0xff</p>
<dt>The same, but in reverse order:</p>
<dd>tc filter add &#8230; flow map \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>key dst and 0xff xor 0xff
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8), <code><a href="/docs/linux/man/8-tc-sfq/">tc-sfq</a></code>(8) </p>
