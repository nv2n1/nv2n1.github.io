---
title: "dcb-buffer(8)"
name: "dcb-buffer"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dcb-buffer/"
description: "dcb-buffer – show / manipulate port buffer settings of the DCB (Data Center Bridging) subsystem"
---

<p>dcb-buffer &#8211; show / manipulate port buffer settings of the DCB (Data Center Bridging) subsystem</p>
<h2>Synopsis</h2>
<pre><code>dcb

[ OPTIONS ]

buffer

{ COMMAND | help }
</code></pre>
<p> <code>dcb buffer show dev</code> DEV [ <code>prio-buffer</code> ] [ <code>buffer-size</code> ] [ <code>total-size</code> ]<br />
 <code>dcb buffer set dev</code> DEV [ <code>prio-buffer</code> <i>PRIO-MAP</i> ] [ <code>buffer-size</code> <i>SIZE-MAP</i> ] </p>
<pre><code>PRIO-MAP := [ PRIO-MAP ] PRIO-MAPPING
PRIO-MAPPING := { PRIO | all }:BUFFER
SIZE-MAP := [ SIZE-MAP ] SIZE-MAPPING
SIZE-MAPPING := { BUFFER | all }:SIZE
PRIO := { 0 .. 7 }
BUFFER := { 0 .. 7 }
SIZE := { INTEGER | INTEGERK | INTEGERM | ... }
</code></pre>
<h2>Description</h2>
<p><code>dcb buffer</code> is used to configure assignment of traffic to port buffers based on traffic priority, and sizes of those buffers. It can be also used to inspect the current configuration, as well as total device memory that the port buffers take. </p>
<h2>Parameters</h2>
<p>For read-write parameters, the following describes only the write direction, i.e. as used with the <code>set</code> command. For the <code>show</code> command, the parameter name is to be used as a simple keyword without further arguments. This instructs the tool to show the value of a given parameter. When no parameters are given, the tool shows the complete buffer configuration. </p>
<dl>
<dt><code>total-size</code></p>
<dd>A read-only property that shows the total device memory taken up by port buffers. This might be more than a simple sum of individual buffer sizes if there are any hidden or internal buffers. </p>
<dt><code>prio-buffer </code><i>PRIO-MAP</i></p>
<dd><i>PRIO-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are priorities, values are buffer indices. For each priority sets a buffer where traffic with that priority is directed to. </p>
<dt><code>buffer-size </code><i>SIZE-MAP</i></p>
<dd><i>SIZE-MAP</i> uses the array parameter syntax, see <code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) for details. Keys are buffer indices, values are sizes of that buffer in bytes. The sizes can use the notation documented in section PARAMETERS at <code><a href="/docs/linux/man/8-tc/">tc</a></code>(8). Note that the size requested by the tool can be rounded or capped by the driver to satisfy the requirements of the device. </p>
</dl>
<h2>EXAMPLE &amp; USAGE</h2>
<p>Configure the priomap in a one-to-one fashion: </p>
<p> # dcb buffer set dev eth0 prio-buffer 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7 </p>
<p> Set sizes of all buffers to 10KB, except for buffer 6, which will have the size 1MB: </p>
<p> # dcb buffer set dev eth0 buffer-size all:10K 6:1M </p>
<p> Show what was set: </p>
<p> # dcb buffer show dev eth0<br />
 prio-buffer 0:0 1:1 2:2 3:3 4:4 5:5 6:6 7:7<br />
 buffer-size 0:10Kb 1:10Kb 2:10Kb 3:10Kb 4:10Kb 5:10Kb 6:1Mb 7:10Kb<br />
 total-size 1222Kb</p>
<h2>Exit Status</h2>
<p>Exit status is 0 if command was successful or a positive integer upon failure.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-dcb/">dcb</a></code>(8) </p>
<h2>Reporting Bugs</h2>
<p>Report any bugs to the Network Developers mailing list <code>&lt;netdev [at] vger.kernel.org&gt;</code> where the development and maintenance is primarily done. You do not have to be subscribed to the list to send a message there.</p>
<h2>Author</h2>
<p>Petr Machata &lt;me [at] pmachata.org&gt;</p>
