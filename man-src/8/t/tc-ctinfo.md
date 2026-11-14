---
title: "tc-ctinfo(8)"
name: "tc-ctinfo"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-ctinfo/"
description: "ctinfo – tc connmark processing action"
---

<p>ctinfo &#8211; tc connmark processing action</p>
<h2>Synopsis</h2>
<p><code>tc &#8230; action ctinfo</code> [ <code>dscp</code> MASK [STATEMASK] ] [ <code>cpmark</code> [MASK] ] [ <code>zone</code> ZONE ] [ <code>CONTROL</code> ] [ <code>index</code> &lt;INDEX&gt; ] </p>
<h2>Description</h2>
<p>CTINFO (Conntrack Information) is a tc action for retrieving data from conntrack marks into various fields. At present it has two independent processing modes which may be viewed as sub-functions. </p>
<p> DSCP mode copies a DSCP stored in conntrack&#8217;s connmark into the IPv4/v6 diffserv field. The copying may conditionally occur based on a flag also stored in the connmark. DSCP mode was designed to assist in restoring packet classifications on ingress, classifications which may then be used by qdiscs such as CAKE. It may be used in any circumstance where ingress classification needs to be maintained across links that otherwise bleach or remap according to their own policies. </p>
<p> CPMARK (copymark) mode copies the conntrack connmark into the packet&#8217;s mark field. Without additional parameters it is functionally completely equivalent to the existing connmark action. An optional mask may be specified to mask which bits of the connmark are restored. This may be useful when DSCP and CPMARK modes are combined. </p>
<p> Simple statistics (tc -s) on DSCP restores and CPMARK copies are maintained where values for set indicate a count of packets altered for that mode. DSCP includes an error count where the destination packet&#8217;s diffserv field was unwriteable.</p>
<h2>Parameters</h2>
<h3>DSCP mode parameters:</h3>
<dl>
<dt>mask</p>
<dd>A mask of 6 contiguous bits indicating where the DSCP value is located in the 32 bit conntrack mark field. A mask must be provided for this mode. mask is a 32 bit unsigned value.</p>
<dt>statemask</p>
<dd>A mask of at least 1 bit indicating where a conditional restore flag is located in the 32 bit conntrack mark field. The statemask bit/s must NOT overlap the mask bits. The DSCP will be restored if the conntrack mark logically ANDed with the statemask yields a non-zero result. statemask is an optional unsigned 32 bit value.</dl>
<h3>CPMARK mode parameters:</h3>
<dl>
<dt>mask</p>
<dd>Store the logically ANDed result of conntrack mark and mask into the packet&#8217;s mark field. Default is 0xffffffff i.e. the whole mark field. mask is an optional unsigned 32 bit value</dl>
<h3>Overall action parameters:</h3>
<dl>
<dt>zone</p>
<dd>Specify the conntrack zone when doing conntrack lookups for packets. zone is a 16bit unsigned decimal value. Default is 0.</p>
<dt>CONTROL</p>
<dd>The following keywords allow to control how the tree of qdisc, classes, filters and actions is further traversed after this action.</p>
<dl>
<dd>
<dl>
<dt><code>reclassify</code></p>
<dd>Restart with the first filter in the current list.</p>
<dt><code>pipe</code></p>
<dd>Continue with the next action attached to the same filter.</p>
<dt><code>drop</code></p>
<dd>Drop the packet.</p>
<dt><code>shot</code></p>
<dd>synonym for <code>drop</code></p>
<dt><code>continue</code></p>
<dd>Continue classification with the next filter in line.</p>
<dt><code>pass</code></p>
<dd>Finish classification process and return to calling qdisc for further packet processing. This is the default.</dl>
</dl>
<dt>index</p>
<dd>Specify an index for this action in order to being able to identify it in later commands. index is a 32bit unsigned decimal value.</dl>
<h2>Examples</h2>
<p>Example showing conditional restoration of DSCP on ingress via an IFB</p>
<dl>
<dd>#Set up the IFB interface<br />
 tc qdisc add dev ifb4eth0 handle ffff: ingress </p>
<p> #Put CAKE qdisc on it<br />
 tc qdisc add dev ifb4eth0 root cake bandwidth 40mbit </p>
<p> #Set interface UP<br />
 ip link set dev ifb4eth0 up </p>
<p> #Add 2 actions, ctinfo to restore dscp &amp; mirred to redirect the packets to IFB<br />
 tc filter add dev eth0 parent ffff: protocol all prio 10 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match u32 0 0 flowid 1:1 action&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ctinfo dscp 0xfc000000 0x01000000&nbsp;<wbr>&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;mirred egress redirect dev ifb4eth0 </p>
<p> tc -s qdisc show dev eth0 ingress </p>
<p>&nbsp;filter parent ffff: protocol all pref 10 u32 chain 0<br />
&nbsp;filter parent ffff: protocol all pref 10 u32 chain 0 fh 800: ht divisor 1<br />
&nbsp;filter parent ffff: protocol all pref 10 u32 chain 0 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1 not_in_hw<br />
&nbsp;<wbr>&nbsp;match 00000000/00000000 at 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action order 1: ctinfo zone 0 pipe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;index 2 ref 1 bind 1 dscp 0xfc000000 0x01000000 installed 72 sec used 0 sec DSCP set 1333 error 0 CPMARK set 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Action statistics:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 658484 bytes 1833 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 0 </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action order 2: mirred&nbsp;(Egress Redirect to device ifb4eth0)&nbsp;stolen<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;index 1 ref 1 bind 1 installed 72 sec used 0 sec<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Action statistics:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 658484 bytes 1833 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 0</dl>
<p> Example showing conditional restoration of DSCP on egress </p>
<p> This may appear nonsensical since iptables marking of egress packets is easy to achieve, however the iptables flow classification rules may be extensive and so some sort of set once and forget may be useful especially on cpu constrained devices.</p>
<dl>
<dd># Send unmarked connections to a marking chain which needs to store a DSCP and set statemask bit in the connmark<br />
 iptables -t mangle -A POSTROUTING -o eth0 -m connmark \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;&#8211;mark 0x00000000/0x01000000 -g CLASS_MARKING_CHAIN </p>
<p> # Apply marked DSCP to the packets<br />
 tc filter add dev eth0 protocol all prio 10 u32 \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;match u32 0 0 flowid 1:1 action&nbsp;\<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ctinfo dscp 0xfc000000 0x01000000 </p>
<p> tc -s filter show dev eth0<br />
&nbsp;filter parent 800e: protocol all pref 10 u32 chain 0<br />
&nbsp;filter parent 800e: protocol all pref 10 u32 chain 0 fh 800: ht divisor 1<br />
&nbsp;filter parent 800e: protocol all pref 10 u32 chain 0 fh 800::800 order 2048 key ht 800 bkt 0 flowid 1:1 not_in_hw<br />
&nbsp;<wbr>&nbsp;match 00000000/00000000 at 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action order 1: ctinfo zone 0 pipe<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;index 1 ref 1 bind 1 dscp 0xfc000000 0x01000000 installed 7414 sec used 0 sec DSCP set 53404 error 0 CPMARK set 0<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Action statistics:<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Sent 32890260 bytes 120441 pkt&nbsp;(dropped 0, overlimits 0 requeues 0)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;backlog 0b 0p requeues 0
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-cake/">tc-cake</a></code>(8) <code><a href="/docs/linux/man/8-tc-connmark/">tc-connmark</a></code>(8) <code><a href="/docs/linux/man/8-tc-mirred/">tc-mirred</a></code>(8)</p>
<h2>Authors</h2>
<p>ctinfo was written by Kevin Darbyshire-Bryant.</p>
