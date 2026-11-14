---
title: "dcb-maxrate(8)"
name: "dcb-maxrate"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-maxrate/"
description: "dcb-maxrate – show / manipulate port maxrate settings of the DCB (Data Center Bridging) subsystem"
---

<p>dcb-maxrate &#8211; show / manipulate port maxrate settings of the DCB (Data Center Bridging) subsystem</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

maxrate

{ COMMAND | help }
</code></pre>
<p> <code>dcb maxrate show dev</code> DEV [ <code>tc-maxrate</code> ]<br />
 <code>dcb maxrate set dev</code> DEV [ <code>tc-maxrate</code> <i>RATE-MAP</i> ] </p>
<pre><code>RATE-MAP := [ RATE-MAP ] RATE-MAPPING
RATE-MAPPING := { TC | all }:RATE
TC := { 0 .. 7 }
RATE := { INTEGER[bit] | INTEGERKbit |

    INTEGERMib | ... }
</code></pre>
<h2>Description</h2>
<p><code>dcb maxrate</code> is used to configure and inspect maximum rate at which traffic is allowed to egress from a given traffic class. </p>
<h2>Parameters</h2>
<p>The following describes only the write direction, i.e. as used with the <code>set</code> command. For the <code>show</code> command, the parameter name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters are given, the tool shows the complete maxrate configuration. </p>
<dl>
<dt><code>tc-maxrate </code><i>RATE-MAP</i></p>
<dd><i>RATE-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are TC indices, values are traffic rates in bits per second. The rates can use the notation documented in section PARAMETERS at <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8). Note that under that notation, &quot;bit&quot; stands for bits per second whereas &quot;b&quot; stands for bytes per second. When showing, the command line option <code>-i</code> toggles between using decadic and ISO/IEC prefixes. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Set rates of all traffic classes to 25Gbps, except for TC 6, which will have the rate of 100Gbps: </p>
<p> # dcb maxrate set dev eth0 tc-maxrate all:25Gbit 6:100Gbit </p>
<p> Show what was set: </p>
<p> # dcb maxrate show dev eth0<br />
 tc-maxrate 0:25Gbit 1:25Gbit 2:25Gbit 3:25Gbit 4:25Gbit 5:25Gbit 6:100Gbit 7:25Gbit</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
