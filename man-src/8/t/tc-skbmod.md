---
title: "tc-skbmod(8)"
name: "tc-skbmod"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-skbmod/"
description: "skbmod – user-friendly packet editor action"
---

<p>skbmod &#8211; user-friendly packet editor action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action skbmod </code>{ <code>set </code> <i>SETTABLE</i> | <code>swap</code><i> SWAPPABLE</i> | <code>ecn</code> } [ <i>CONTROL</i> ] [ <code>index</code><i> INDEX </i> ] </p>
<pre><code>SETTABLE :=

[ dmac

DMAC ]

[ smac

SMAC ]

[ etype

ETYPE ]
SWAPPABLE :=

mac
CONTROL := {

    reclassify | pipe | drop | shot | continue | pass }</code></pre>
<h2>Description</h2>
<p>The <code>skbmod</code> action is intended as a usability upgrade to the existing <code>pedit</code> action. Instead of having to manually edit 8-, 16-, or 32-bit chunks of an ethernet header, <code>skbmod</code> allows complete substitution of supported elements. Action must be one of <code>set</code>, <code>swap</code> and <code>ecn</code>. <code>set</code> and <code>swap</code> only affect Ethernet packets, while <code>ecn</code> only affects IP packets.</p>
<h2>Options</h2>
<dl>
<dt><code>dmac</code><i> DMAC</i></p>
<dd>Change the destination mac to the specified address.</p>
<dt><code>smac</code><i> SMAC</i></p>
<dd>Change the source mac to the specified address.</p>
<dt><code>etype</code><i> ETYPE</i></p>
<dd>Change the ethertype to the specified value.</p>
<dt><code>mac</code></p>
<dd>Used to swap mac addresses.</p>
<dt><code>ecn</code></p>
<dd>Used to mark ECN Capable Transport (ECT) IP packets as Congestion Encountered (CE). Does not affect Non ECN-Capable Transport (Non-ECT) packets.</p>
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
<p>To start, observe the following filter with a pedit action:</p>
<dl>
<dd>tc filter add dev eth1 parent 1: protocol ip prio 10 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action pedit munge offset -14 u8 set 0x02 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>munge offset -13 u8 set 0x15 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>munge offset -12 u8 set 0x15 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>munge offset -11 u8 set 0x15 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>munge offset -10 u16 set 0x1515 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pipe
</dl>
<p> Using the skbmod action, this command can be simplified to:</p>
<dl>
<dd>tc filter add dev eth1 parent 1: protocol ip prio 10 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action skbmod set dmac 02:15:15:15:15:15 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>pipe
</dl>
<p> Complexity will increase if source mac and ethertype are also being edited as part of the action. If all three fields are to be changed with skbmod:</p>
<dl>
<dd>tc filter add dev eth5 parent 1: protocol ip prio 10 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action skbmod \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set etype 0xBEEF \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set dmac 02:12:13:14:15:16 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>set smac 02:22:23:24:25:26
</dl>
<p> To swap the destination and source mac addresses in the Ethernet header:</p>
<dl>
<dd>tc filter add dev eth3 parent 1: protocol ip prio 10 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action skbmod \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>swap mac
</dl>
<p> Finally, to mark the CE codepoint in the IP header for ECN Capable Transport (ECT) packets:</p>
<dl>
<dd>tc filter add dev eth0 parent 1: protocol ip prio 10 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>u32 match ip protocol 1 0xff flowid 1:2 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>action skbmod \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>ecn
</dl>
<p> Only one of <code>set</code>, <code>swap</code> and <code>ecn</code> shall be used in a single command. Trying to use more than one of them in a single command is considered undefined behavior; pipe multiple commands together instead. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-u32/">tc-u32</a></code>(8), <code><a href="/docs/linux/man/8-tc-pedit/">tc-pedit</a></code>(8) </p>
