---
title: "tc-nat(8)"
name: "tc-nat"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-nat/"
description: "nat – stateless native address translation action"
---

<p>nat &#8211; stateless native address translation action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action nat</code> <i>DIRECTION OLD NEW</i> </p>
<pre><code>DIRECTION := {

    ingress | egress }
OLD := IPV4_ADDR_SPEC
NEW := IPV4_ADDR_SPEC
IPV4_ADDR_SPEC := {

    default | any | all |

    in_addr[/{prefix|netmask}]</code></pre>
<h2>Description</h2>
<p>The <code>nat</code> action allows to perform NAT without the overhead of conntrack, which is desirable if the number of flows or addresses to perform NAT on is large. This action is best used in combination with the <code>u32</code> filter to allow for efficient lookups of a large number of stateless NAT rules in constant time.</p>
<h2>Options</h2>
<dl>
<dt><code>ingress</code></p>
<dd>Translate destination addresses, i.e. perform DNAT.</p>
<dt><code>egress</code></p>
<dd>Translate source addresses, i.e. perform SNAT.</p>
<dt><i>OLD</i></p>
<dd>Specifies addresses which should be translated.</p>
<dt><i>NEW</i></p>
<dd>Specifies addresses which <i>OLD</i> should be translated into.</dl>
<h2>Notes</h2>
<p>The accepted address format in <i>OLD</i> and <i>NEW</i> is quite flexible. It may either consist of one of the keywords <code>default</code>, <code>any</code> or <code>all</code>, representing the all-zero IP address or a combination of IP address and netmask or prefix length separated by a slash (<code>/</code>) sign. In any case, the mask (or prefix length) value of <i>OLD</i> is used for <i>NEW</i> as well so that a one-to-one mapping of addresses is assured. </p>
<p> Address translation is done using a combination of binary operations. First, the original (source or destination) address is matched against the value of <i>OLD</i>. If the original address fits, the new address is created by taking the leading bits from <i>NEW</i> (defined by the netmask of <i>OLD</i>) and taking the remaining bits from the original address. </p>
<p> There is rudimental support for upper layer protocols, namely TCP, UDP and ICMP. While for the first two only checksum recalculation is performed, the action also takes care of embedded IP headers in ICMP packets by translating the respective address therein, too.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
