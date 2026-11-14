---
title: "dcb-ets(8)"
name: "dcb-ets"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-ets/"
description: "dcb-ets – show / manipulate ETS (Enhanced Transmission Selection) settings of the DCB (Data Center Bridging) subsystem"
---

<p>dcb-ets &#8211; show / manipulate ETS (Enhanced Transmission Selection) settings of the DCB (Data Center Bridging) subsystem</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

ets

{ COMMAND | help }
</code></pre>
<p> <code>dcb ets show dev</code> DEV [ <code>willing</code> ] [ <code>ets-cap</code> ] [ <code>cbs</code> ] [ <code>tc-tsa</code> ] [ <code>reco-tc-tsa</code> ] [ <code>pg-bw</code> ] [ <code>tc-bw</code> ] [ <code>reco-tc-bw</code> ] [ <code>prio-tc</code> ] [ <code>reco-prio-tc</code> ]<br />
 <code>dcb ets set dev</code> DEV [ <code>willing</code> { <code>on</code> | <code>off</code> } ] [ { <code>tc-tsa</code> | <code>reco-tc-tsa</code> } <i>TSA-MAP</i> ] [ { <code>pg-bw</code> | <code>tc-bw</code> | <code>reco-tc-bw</code> } <i>BW-MAP</i> ] [ { <code>prio-tc</code> | <code>reco-prio-tc</code> } <i>PRIO-MAP</i> ] </p>
<pre><code>TSA-MAP := [ TSA-MAP ] TSA-MAPPING
TSA-MAPPING := { TC | all }:{ strict |

    cbs | ets | vendor }
BW-MAP := [ BW-MAP ] BW-MAPPING
BW-MAPPING := { TC | all }:INTEGER
PRIO-MAP := [ PRIO-MAP ] PRIO-MAPPING
PRIO-MAPPING := { PRIO | all }:TC
TC := { 0 .. 7 }
PRIO := { 0 .. 7 }
</code></pre>
<h2>Description</h2>
<p><code>dcb ets</code> is used to configure Enhanced Transmission Selection attributes through Linux DCB (Data Center Bridging) interface. ETS permits configuration of mapping of priorities to traffic classes, traffic selection algorithm to use per traffic class, bandwidth allocation, etc. Two DCB TLVs are related to the ETS feature: a configuration and recommendation values. Recommendation values are named with a prefix <code>reco-,</code> while the configuration ones have plain names. </p>
<h2>Parameters</h2>
<p>For read-write parameters, the following describes only the write direction, i.e. as used with the <code>set</code> command. For the <code>show</code> command, the parameter name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters are given, the tool shows the complete ETS configuration. </p>
<dl>
<dt><code>ets-cap</code></p>
<dd>A read-only property that shows the number of supported ETS traffic classes. </p>
<dt><code>cbs</code></p>
<dd>A read-only property that is enabled if the driver and the hardware support the CBS Transmission Selection Algorithm. </p>
<dt><code>willing </code>{ <code>on</code> | <code>off</code> }</p>
<dd>Whether local host should accept configuration from peer TLVs. </p>
<dt><code>prio-tc </code><i>PRIO-MAP</i></p>
<dd><code>reco-prio-tc </code><i>PRIO-MAP</i> <i>PRIO-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are priorities, values are traffic classes. For each priority sets a TC where traffic with that priority is directed to. </p>
<dt><code>tc-tsa </code><i>TSA-MAP</i></p>
<dd><code>reco-tc-tsa </code><i>TSA-MAP</i> <i>TSA-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are TCs, values are Transmission Selection Algorithm (TSA) keywords described below. For each TC sets an algorithm used for deciding how traffic queued up at this TC is scheduled for transmission. Supported TSAs are: </p>
<p> <code>strict</code> &#8211; for strict priority, where traffic in higher-numbered TCs always takes precedence over traffic in lower-numbered TCs.<br />
 <code>ets</code> &#8211; for Enhanced Traffic Selection, where available bandwidth is distributed among the ETS-enabled TCs according to the weights set by <code>tc-bw</code> and <code>reco-tc-bw</code>, respectively.<br />
 <code>cbs</code> &#8211; for Credit Based Shaper, where traffic is scheduled in a strict manner up to the limit set by a shaper.<br />
 <code>vendor</code> &#8211; for vendor-specific traffic selection algorithm. </p>
<dt><code>tc-bw </code><i>BW-MAP</i></p>
<dd><code>reco-tc-bw </code><i>BW-MAP</i> <i>BW-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are TCs, values are integers representing percent of available bandwidth given to the traffic class in question. The value should be 0 for TCs whose TSA is not <code>ets</code>, and the sum of all values shall be 100. As an exception to the standard wording, a configuration with no <code>ets</code> TCs is permitted to sum up to 0 instead. </p>
<dt><code>pg-bw </code><i>BW-MAP</i></p>
<dd>The precise meaning of <code>pg-bw</code> is not standardized, but the assumption seems to be that the same scheduling process as on the transmit side is applicable on receive side as well, and configures receive bandwidth allocation for <code>ets</code> ingress traffic classes (priority groups). </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Configure ETS priomap in a one-to-one fashion: </p>
<p> # dcb ets set dev eth0 prio-tc 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7 </p>
<p> Set TSA and transmit bandwidth configuration: </p>
<p> # dcb ets set dev eth0 tc-tsa all:strict 0:ets 1:ets 2:ets \ </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;tc-bw all:0 0:33 1:33 2:34 </p>
<p> Show what was set: </p>
<p> # dcb ets show dev eth0 prio-tc tc-tsa tc-bw<br />
 prio-tc 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7<br />
 tc-tsa 0:ets 1:ets 2:ets 3:strict 4:strict 5:strict 6:strict 7:strict<br />
 tc-bw 0:33 1:33 2:34 3:0 4:0 5:0 6:0 7:0</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
