---
title: "tc-police(8)"
name: "tc-police"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-police/"
description: "police – policing action"
---

<p>police &#8211; policing action</p>
<h2>Synopsis</h2>
<p><code>tc</code> &#8230; <code>action police [</code> <code>rate</code><i> RATE </i><code>burst</code> <i>BYTES</i>[<code>/</code><i>BYTES</i>] ] [ <code>pkts_rate</code><i> RATE </i><code>pkts_burst</code> <i>PACKETS</i>] [ <code>mtu</code> <i>BYTES</i>[<code>/</code><i>BYTES</i>] ] [ <code>peakrate</code><i> RATE</i> ] [ <code>overhead</code><i> BYTES</i> ] [ <code>linklayer</code><i> TYPE</i> ] [ <i>CONTROL</i> ]<br />
 <code>tc</code> &#8230; <code>filter</code> &#8230; [ <code>estimator</code> <i>SAMPLE AVERAGE </i>] <code>action police avrate</code> <i>RATE</i> [ <i>CONTROL</i> ] </p>
<pre><code>CONTROL :=

conform-exceed EXCEEDACT[/NOTEXCEEDACT
EXCEEDACT/NOTEXCEEDACT := {

    pipe | ok | reclassify | drop | continue | goto chain CHAIN_INDEX }</code></pre>
<h2>Description</h2>
<p>The <code>police</code> action allows limiting of the byte or packet rate of traffic matched by the filter it is attached to. </p>
<p> There are two different algorithms available to measure the byte rate: The first one uses an internal dual token bucket and is configured using the <code>rate</code>, <code>burst</code>, <code>mtu</code>, <code>peakrate</code>, <code>overhead</code> and <code>linklayer</code> parameters. The second one uses an in-kernel sampling mechanism. It can be fine-tuned using the <code>estimator</code> filter parameter. </p>
<p> There is one algorithm available to measure packet rate and it is similar to the first algorithm described for byte rate. It is configured using the <code>pkt_rate</code> and <code>pkt_burst</code> parameters. </p>
<p> At least one of the <code>rate</code> and <code>pkt_rate</code> parameters must be configured.</p>
<h2>Options</h2>
<dl>
<dt><code>rate</code><i> RATE</i></p>
<dd>The maximum byte rate of packets passing this action. Those exceeding it will be treated as defined by the <code>conform-exceed</code> option.</p>
<dt><code>burst</code><i> BYTES</i>[<code>/</code><i>BYTES</i>]</p>
<dd>Set the maximum allowed burst in bytes, optionally followed by a slash (&#8216;/&#8217;) sign and cell size which must be a power of 2.</p>
<dt><code>pkt_rate</code><i> RATE</i></p>
<dd>The maximum packet rate or packets passing this action. Those exceeding it will be treated as defined by the <code>conform-exceed</code> option.</p>
<dt><code>pkt_burst</code><i> PACKETS</i></p>
<dd>Set the maximum allowed burst in packets.</p>
<dt><code>mtu</code><i> BYTES</i>[<code>/</code><i>BYTES</i>]</p>
<dd>This is the maximum packet size handled by the policer (larger ones will be handled like they exceeded the configured rate). Setting this value correctly will improve the scheduler&#8217;s precision. Value formatting is identical to <code>burst</code> above. Defaults to unlimited.</p>
<dt><code>peakrate</code><i> RATE</i></p>
<dd>Set the maximum bucket depletion rate, exceeding <code>rate</code>.</p>
<dt><code>avrate</code><i> RATE</i></p>
<dd>Make use of an in-kernel bandwidth rate estimator and match the given <i>RATE</i> against it.</p>
<dt><code>overhead</code><i> BYTES</i></p>
<dd>Account for protocol overhead of encapsulating output devices when computing <code>rate</code> and <code>peakrate</code>.</p>
<dt><code>linklayer</code><i> TYPE</i></p>
<dd>Specify the link layer type. <i>TYPE</i> may be one of <code>ethernet</code> (the default), <code>atm</code> or <code>adsl</code> (which are synonyms). It is used to align the precomputed rate tables to ATM cell sizes, for <code>ethernet</code> no action is taken.</p>
<dt><code>estimator</code><i> SAMPLE AVERAGE</i></p>
<dd>Fine-tune the in-kernel packet rate estimator. <i>SAMPLE</i> and <i>AVERAGE</i> are time values and control the frequency in which samples are taken and over what timespan an average is built.</p>
<dt><code>conform-exceed</code><i> EXCEEDACT</i>[<code>/</code><i>NOTEXCEEDACT</i>]</p>
<dd>Define how to handle packets which exceed or conform the configured bandwidth limit. Possible values are:</p>
<dl>
<dd>
<dl>
<dt>continue</p>
<dd>Don&#8217;t do anything, just continue with the next action in line.</p>
<dt>drop</p>
<dd>Drop the packet immediately.</p>
<dt>shot</p>
<dd>This is a synonym to <code>drop</code>.</p>
<dt>ok</p>
<dd>Accept the packet. This is the default for conforming packets.</p>
<dt>pass</p>
<dd>This is a synonym to <code>ok</code>.</p>
<dt>reclassify</p>
<dd>Treat the packet as non-matching to the filter this action is attached to and continue with the next filter in line (if any). This is the default for exceeding packets.</p>
<dt>pipe</p>
<dd>Pass the packet to the next action in line.</dl>
</dl>
</dl>
<h2>Examples</h2>
<p>A typical application of the police action is to enforce ingress traffic rate by dropping exceeding packets. Although better done on the sender&#8217;s side, especially in scenarios with lack of peer control (e.g. with dial-up providers) this is often the best one can do in order to keep latencies low under high load. The following establishes input bandwidth policing to 1mbit/s using the <code>ingress</code> qdisc and <code>u32</code> filter:</p>
<dl>
<dd># tc qdisc add dev eth0 handle ffff: ingress # tc filter add dev eth0 parent ffff: u32 \ <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>match u32 0 0 \<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>police rate 1mbit burst 100k
</dl>
<p> As an action can not live on it&#8217;s own, there always has to be a filter involved as link between qdisc and action. The example above uses <code>u32</code> for that, which is configured to effectively match any packet (passing it to the <code>police</code> action thereby). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8) </p>
