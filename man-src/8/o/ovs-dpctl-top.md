---
title: "ovs-dpctl-top(8)"
name: "ovs-dpctl-top"
section: "8"
letter: "o"
url: "/docs/linux/man/8-ovs-dpctl-top/"
description: "ovs-dpctl-top – Top like behavior for ovs-dpctl dump-flows"
---

<p><code>ovs-dpctl-top</code> &#8211; Top like behavior for ovs-dpctl dump-flows</p>
<h2>Synopsis</h2>
<p><code>ovs-dpctl-top</code> [-h] [-v] [-f FLOWFILES] [-V] [-s] [&#8211;host HOST] [-a | &#8211;accumulate] [&#8211;accumulate-decay ACCUMULATEDECAY] [-d DELAY]</p>
<h2>Description</h2>
<p>This program summarizes <code>ovs-dpctl</code> flow content by aggregating the number of packets, total bytes and occurrence of the following fields:</p>
<dl>
<dd>&#8211; Datapath in_port</dd>
<dd>&#8211; Ethernet type</dd>
<dd>&#8211; Source and destination MAC addresses</dd>
<dd>&#8211; IP protocol</dd>
<dd>&#8211; Source and destination IPv4 addresses</dd>
<dd>&#8211; Source and destination IPv6 addresses</dd>
<dd>&#8211; UDP and TCP destination port</dd>
<dd>&#8211; Tunnel source and destination addresses</dd></dl>
<h3>Output shows four values:</h3>
<dl>
<dd>&#8211; FIELDS: the flow fields for example in_port(1).</dd>
<dd>&#8211; COUNT: the number of lines in the dump-flow output contain the flow field.</dd>
<dd>&#8211; PACKETS: the total number of packets containing the flow field.</dd>
<dd>&#8211; BYTES: the total number of bytes containing the flow field. If units are not present then values are in bytes.</dd>
<dd>&#8211; AVERAGE: the average packets size (BYTES/PACKET).</dd></dl>
<h3>Top Behavior</h3>
<p>While in top mode, the default behavior, the following single character commands are supported:</p>
<dl>
<dd>a &#8211; toggles top in accumulate and live mode. Accumulate mode is described below.</dd>
<dd>s &#8211; toggles which column is used to sort content in decreasing order. A DESC title is placed over the column.</dd>
<dd>_ &#8211; a space indicating to collect dump-flow content again</dd>
<dd>h &#8211; halt output. Any character will restart sampling</dd>
<dd>f &#8211; cycle through flow fields</dd>
<dd>q &#8211; q for quit.</dd></dl>
<h3>Accumulate Mode</h3>
<p>There are two supported modes: live and accumulate. The default is live. The parameter <code>&#8211;accumulate</code> or the &#8216;a&#8217; character in top mode enables the latter. In live mode, recent dump-flow content is presented. Where as accumulate mode keeps track of the prior historical information until the flow is reset not when the flow is purged. Reset flows are determined when the packet count for a flow has decreased from its previous sample. There is one caveat, eventually the system will run out of memory if, after the accumulate-decay period any flows that have not been refreshed are purged. The goal here is to free memory of flows that are not active. Statistics are not decremented. Their purpose is to reflect the overall history of the flow fields.</p>
<h3>Debugging Errors</h3>
<p>Parsing errors are counted and displayed in the status line at the beginning of the output. Use the <code>&#8211;verbose</code> option with <code>&#8211;script to see what output was not parsed, like this: $ ovs-dpctl dump-flows | ovs-dpctl-top &#8211;script</code> <code>&#8211;verbose</code> Error messages will identify content that failed to parse.</p>
<h3>Access Remote Hosts</h3>
<p>The <code>&#8211;host</code> must follow the format user [at] hostname. This script simply calls &#8216;ssh user [at] Hostname&#8217; without checking for login credentials therefore public keys should be installed on the system identified by hostname, such as: $ ssh-copy-id user [at] hostname Consult ssh-copy-id man pages for more details.</p>
<h3>Expected usage</h3>
<p>$ ovs-dpctl-top or to run as a script: $ ovs-dpctl dump-flows &gt; dump-flows.log $ ovs-dpctl-top <code>&#8211;script</code> <code>&#8211;flow-file</code> dump-flows.log</p>
<h3>Options</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd>show this help message and exit.</dd>
<dt><code>-v</code>, <code>&#8211;version</code></dt>
<dd>show program&#8217;s version number and exit.</dd>
<dt><code>-f</code> FLOWFILES, <code>&#8211;flow-file</code> FLOWFILES</dt>
<dd>file containing flows from ovs-dpctl dump-flow.</dd>
<dt><code>-V</code>, <code>&#8211;verbose</code></dt>
<dd>enable debug level verbosity.</dd>
<dt><code>-s</code>, <code>&#8211;script</code></dt>
<dd>Run from a script (no user interface).</dd>
<dt><code>&#8211;host</code> HOST</dt>
<dd>Specify a user [at] host for retrieving flows see Accessing Remote Hosts for more information.</dd>
<dt><code>-a</code>, <code>&#8211;accumulate</code></dt>
<dd>Accumulate dump-flow content.</dd>
<dt><code>&#8211;accumulate-decay</code> ACCUMULATEDECAY</dt>
<dd>Decay old accumulated flows. The default is 5 minutes. A value of 0 disables decay.</dd>
<dt><code>-d</code> DELAY, <code>&#8211;delay</code> DELAY</dt>
<dd>Delay in milliseconds to collect dump-flow content (sample rate). </dd>
</dl>