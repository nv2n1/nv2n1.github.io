---
title: "dcb-pfc(8)"
name: "dcb-pfc"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-pfc/"
description: "dcb-pfc – show / manipulate PFC (Priority-based Flow Control) settings of the DCB (Data Center Bridging) subsystem"
---

<p>dcb-pfc &#8211; show / manipulate PFC (Priority-based Flow Control) settings of the DCB (Data Center Bridging) subsystem</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

pfc

{ COMMAND | help }
</code></pre>
<p> <code>dcb pfc show dev</code> DEV [ <code>pfc-cap</code> ] [ <code>prio-pfc</code> ] [ <code>macsec-bypass</code> ] [ <code>delay</code> ] [ <code>requests</code> ] [ <code>indications</code> ]<br />
 <code>dcb pfc set dev</code> DEV [ <code>prio-pfc</code> <i>PFC-MAP</i> ] [ <code>macsec-bypass</code> { <code>on</code> | <code>off</code> } ] [ <code>delay</code> <i>INTEGER</i> ] </p>
<pre><code>PFC-MAP := [ PFC-MAP ] PFC-MAPPING
PFC-MAPPING := { PRIO | all }:{

    on | off }
PRIO := { 0 .. 7 }
</code></pre>
<h2>Description</h2>
<p><code>dcb pfc</code> is used to configure Priority-based Flow Control attributes through Linux DCB (Data Center Bridging) interface. PFC permits marking flows with a certain priority as lossless, and holds related configuration, as well as PFC counters. </p>
<h2>Parameters</h2>
<p>For read-write parameters, the following describes only the write direction, i.e. as used with the <code>set</code> command. For the <code>show</code> command, the parameter name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters are given, the tool shows the complete PFC configuration. </p>
<dl>
<dt><code>pfc-cap</code></p>
<dd>A read-only property that shows the number of traffic classes that may simultaneously support PFC. </p>
<dt><code>requests</code></p>
<dd>A read-only count of the sent PFC frames per traffic class. Only shown when -s is given, or when requested explicitly. </p>
<dt><code>indications</code></p>
<dd>A read-only count of the received PFC frames per traffic class. Only shown when -s is given, or when requested explicitly. </p>
<dt><code>macsec-bypass </code>{ <code>on</code> | <code>off</code> }</p>
<dd>Whether the sending station is capable of bypassing MACsec processing when MACsec is disabled. </p>
<dt><code>prio-pfc </code><i>PFC-MAP</i></p>
<dd><i>PFC-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are priorities, values are on / off indicators of whether PFC is enabled for a given priority. </p>
<dt><code>delay </code><i>INTEGER</i></p>
<dd>The allowance made for round-trip propagation delay of the link in bits. The value shall be 0..65535. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Enable PFC on priorities 6 and 7, leaving the rest intact: </p>
<p> # dcb pfc set dev eth0 prio-pfc 6:on 7:on </p>
<p> Disable PFC of all priorities except 6 and 7, and configure delay to 4096 bits: </p>
<p> # dcb pfc set dev eth0 prio-pfc all:off 6:on 7:on delay 0x1000 </p>
<p> Show what was set: </p>
<p> # dcb pfc show dev eth0<br />
 pfc-cap 8 macsec-bypass off delay 4096<br />
 prio-pfc 0:off 1:off 2:off 3:off 4:off 5:off 6:on 7:on</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
