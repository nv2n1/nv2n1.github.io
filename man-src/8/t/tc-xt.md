---
title: "tc-xt(8)"
name: "tc-xt"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-xt/"
description: "xt – tc iptables action"
---

<p>xt &#8211; tc iptables action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action xt -j</code> <i>TARGET</i> [ <i>TARGET_OPTS</i> ]</p>
<h2>Description</h2>
<p>The <code>xt</code> action allows to call arbitrary iptables targets for packets matching the filter this action is attached to.</p>
<h2>Options</h2>
<dl>
<dt><code>-j</code><i> TARGET </i>[<i> TARGET_OPTS </i>]</p>
<dd>Perform a jump to the given iptables target, optionally passing any target specific options in <i>TARGET_OPTS</i>.</dl>
<h2>Examples</h2>
<p>The following will attach a <code>u32</code> filter to the <code>ingress</code> qdisc matching ICMP replies and using the <code>xt</code> action to make the kernel yell &#8216;PONG&#8217; each time: </p>
<dl>
<dd>tc qdisc add dev eth0 ingress tc filter add dev eth0 parent ffff: proto ip u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip protocol 1 0xff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match ip icmp_type 0 0xff \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action xt -j LOG &#8211;log-prefix PONG
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8), <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) </p>
