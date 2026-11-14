---
title: "tc-sample(8)"
name: "tc-sample"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-sample/"
description: "sample – packet sampling tc action"
---

<p>sample &#8211; packet sampling tc action</p>
<h2>Synopsis</h2>
<p> <code>tc</code> &#8230; <code>action sample rate</code> <i>RATE</i> <code>group</code> <i>GROUP</i> [ <code>trunc</code> <i>SIZE</i> ] [ <code>index</code> <i>INDEX</i> ]<br />
 <code>tc</code> &#8230; <code>action sample index </code> <i>INDEX</i> </p>
<h2>Description</h2>
<p>The <code>sample</code> action allows sampling packets matching classifier. The packets are chosen randomly according to the <code>rate</code> parameter, and are sampled using the <code>psample</code> generic netlink channel. The user can also specify packet truncation to save user-kernel traffic. Each sample includes some informative metadata about the original packet, which is sent using netlink attributes, alongside the original packet data. The user can either specify the sample action parameters as presented in the first form above, or use an existing sample action using its index, as presented in the second form. </p>
<h2>Sampled Packets Metadata Fields</h2>
<p>The metadata are delivered to userspace applications using the <code>psample</code> generic netlink channel, where each sample includes the following netlink attributes:</p>
<dl>
<dt><code>PSAMPLE_ATTR_IIFINDEX</code></p>
<dd>The input interface index of the packet, if there is one.</p>
<dt><code>PSAMPLE_ATTR_OIFINDEX</code></p>
<dd>The output interface index of the packet. This field is not relevant on ingress sampling</p>
<dt><code>PSAMPLE_ATTR_ORIGSIZE</code></p>
<dd>The size of the original packet (before truncation)</p>
<dt><code>PSAMPLE_ATTR_SAMPLE_GROUP</code></p>
<dd>The <code>psample</code> group the packet was sent to</p>
<dt><code>PSAMPLE_ATTR_GROUP_SEQ</code></p>
<dd>A sequence number of the sampled packet. This number is incremented with each sampled packet of the current <code>psample</code> group</p>
<dt><code>PSAMPLE_ATTR_SAMPLE_RATE</code></p>
<dd>The rate the packet was sampled with </p>
</dl>
<h2>Options</h2>
<dl>
<dt><code>rate</code><i> RATE</i></p>
<dd>The packet sample rate. <i>RATE</i> is the expected ratio between observed packets and sampled packets. For example, <i>RATE</i> of 100 will lead to an average of one sampled packet out of every 100 observed.</p>
<dt><code>trunc</code><i> SIZE</i></p>
<dd>Upon set, defines the maximum size of the sampled packets, and causes truncation if needed</p>
<dt><code>group</code><i> GROUP</i></p>
<dd>The <code>psample</code> group the packet will be sent to. The <code>psample</code> module defines the concept of groups, which allows the user to match specific sampled packets in the case of multiple sampling rules, thus identify only the packets that came from a specific rule.</p>
<dt><code>index</code><i> INDEX</i></p>
<dd>Is a unique ID for an action. When creating new action instance, this parameter allows to set the new action index. When using existing action, this parameter allows to specify the existing action index. The index must 32bit unsigned integer greater than zero.</dl>
<h2>Examples</h2>
<p>Sample one of every 100 packets flowing into interface eth0 to psample group 12:</p>
<dl>
<dd>tc qdisc add dev eth0 handle ffff: ingress tc filter add dev eth0 parent ffff: matchall \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action sample rate 100 group 12 index 19</dl>
<p> Use the same action instance to sample eth1 too:</p>
<dl>
<dd>tc qdisc add dev eth1 handle ffff: ingress tc filter add dev eth1 parent ffff: matchall \<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;action sample index 19</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-matchall/">tc-matchall</a></code>(8) <code><a href="/docs/linux/man/1-psample/">psample</a></code>(1) </p>
