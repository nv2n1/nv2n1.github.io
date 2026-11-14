---
title: "tc-fw(8)"
name: "tc-fw"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-fw/"
description: "fw – fwmark traffic control filter"
---

<p>fw &#8211; fwmark traffic control filter</p>
<h2>Synopsis</h2>
<p><code>tc</code> <code>filter</code> &#8230; <code>fw</code> [ <code>classid</code> <i>CLASSID</i> ] [ <code>action</code> <i>ACTION_SPEC</i> ]</p>
<h2>Description</h2>
<p>the <code>fw</code> filter allows to classify packets based on a previously set <code>fwmark</code> by <code>iptables</code>. If it is identical to the filter&#8217;s <code>handle</code>, the filter matches. <code>iptables</code> allows to mark single packets with the <code>MARK</code> target, or whole connections using <code>CONNMARK</code>. The benefit of using this filter instead of doing the heavy-lifting with <code>tc</code> itself is that on one hand it might be convenient to keep packet filtering and classification in one place, possibly having to match a packet just once, and on the other users familiar with <code>iptables</code> but not <code>tc</code> will have a less hard time adding QoS to their setups.</p>
<h2>Options</h2>
<dl>
<dt><code>classid</code><i> CLASSID</i></p>
<dd>Push matching packets to the class identified by <i>CLASSID</i>.</p>
<dt><code>action</code><i> ACTION_SPEC</i></p>
<dd>Apply an action from the generic actions framework on matching packets.</dl>
<h2>Examples</h2>
<p>Take e.g. the following tc filter statement: </p>
<dl>
<dd>tc filter add &#8230; handle 6 fw classid 1:1</dl>
<p> will match if the packet&#8217;s <code>fwmark</code> value is <code>6</code>. This is a sample <code>iptables</code> statement marking packets coming in on eth0: </p>
<dl>
<dd>iptables -t mangle -A PREROUTING -i eth0 -j MARK &#8211;set-mark 6</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-iptables/">iptables</a></code>(8), <code><a href="/docs/linux/man/8-iptables-extensions/">iptables-extensions</a></code>(8) </p>
