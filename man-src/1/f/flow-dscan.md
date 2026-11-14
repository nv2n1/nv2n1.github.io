---
title: "flow-dscan(1)"
name: "flow-dscan"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-dscan/"
description: "flow-dscan – Detect scanning and other suspicious network activity."
---

<h2>NAME</h2>
<p> flow-dscan &#8211; Detect scanning and other suspicious network activity.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-dscan</code> [ <code>-bBhlmpwW</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-D</code><i> iplist_depth</i> ] [ <code>-s</code><i> state_file</i> ] [ <code>-i</code><i> input_filter</i> ] [ <code>-L</code><i> suppress_list</i> ] [ <code>-o</code><i> output_filter</i> ] [ <code>-O</code><i> excessive_octets</i> ] [ <code>-P</code><i> excessive_flows</i> ] [ <code>-S</code><i> port_scan_trigger</i> ] [ <code>-t</code><i> ager_timeout</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-dscan</code> utility is used to detect suspicious activity such as port scanning, host scanning, and flows with unusually high octets or packets. A source and destination suppress list is supported to help prevent false alarms due to hosts such as nameservers or popular web servers that exchange traffic with a large number of hosts. Alarms are logged to syslog or stderr. The internal state of flow-dscan can be saved and loaded to allow for interrupted operation. </p>
<p> <code>flow-dscan</code> will work best if configured to only watch only inbound or outbound traffic by using the input or output interface filter option. </p>
<p> The host scanner works by counting the length of the destination IP hash chain. If it goes above 64, then the src is considered to be scanning. </p>
<p> The port scanner works by keeping a bitmap of the destination port number &lt; 1024 per destination IP. If it goes above 64, the src is considered to be port scanning the destination. </p>
<p> When a src has been flagged as scanning it will not be reported again until the record is aged out and enough flows trigger it again. </p>
<p> A SIGHUP signal will instruct flow-dscan to reload the suppress list. </p>
<p> A SIGUSR1 signal will instruct flow-dscan to dump its internal state.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code></p>
<dd> Do not detach and run in the background. Alerts go to stderr.</p>
<dt><code>-B</code></p>
<dd> Do not detach and run in the background. Alerts go to syslog.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-D</code><i> iplist_depth</i></p>
<dd> Depth of IP host list for detecting host scanning.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-i</code><i> input_filter</i></p>
<dd> Input interface filter list.</p>
<dt><code>-I</code><i> output_filter</i></p>
<dd> Output interface filter list.</p>
<dt><code>-l</code></p>
<dd> Load state from <i>/var/tmp/dscan.state</i> or the filename specified with -s.</p>
<dt><code>-L</code><i> suppress_list</i></p>
<dd> Basename of suppress files. There are two suppress files for input and output traffic. The suppress file syntax is </p>
<p> IP_address protocol source_port destination_port </p>
<p> A &#8216;-&#8216; can be used as a wildcard in the protocol, source_port, and destination_port fields. Only a single protocol, source_port, and destination_port is supported per IP address.</p>
<dt><code>-m</code></p>
<dd> Multicast address filter. Use to ignore multicast addresses.</p>
<dt><code>-O</code><i> excessive_octets</i></p>
<dd> Trigger an alert if a flow is processed with the octets field exceeding <i>excessive_octets</i>.</p>
<dt><code>-p</code></p>
<dd> Dump state to <i>/var/tmp/dscan.state</i> or the filename specified with -s.</p>
<dt><code>-P</code><i> excessive_packets</i></p>
<dd> Trigger an alert if a flow is processed with the packets field exceeding <i>excessive_packets</i>.</p>
<dt><code>-s</code><i> statefile</i></p>
<dd> State filename. Defaults to <i>/var/tmp/dscan.state</i></p>
<dt><code>-S</code><i> port_scan_trigger</i></p>
<dd> Number of ports a IP address must have used to be considered scanning.</p>
<dt><code>-t</code><i> ager_timeout</i></p>
<dd> How long to keep flows around. Default to 90000. This is measured in flows processed.</p>
<dt><code>-T</code><i> excessive_time</i></p>
<dd> Trigger an alert if a flow is processed with the End-Start field exceeding <i>excessive_time</i>.</p>
<dt><code>-w</code></p>
<dd> Filter (ignore) candidate inbound www traffic, ie IP protocol 6, source port 80, and destination port &gt; 1023.</p>
<dt><code>-W</code></p>
<dd> Filter (ignore) candidate outbound www traffic, ie IP protocol 6, destination port 80, and source port &gt; 1023.</dl>
<h2>EXAMPLES</h2>
<p> In a topology where 25 is the only output interface run flow-dscan over the data in <i>/flows/krc4</i>. Ignore www and multicast traffic, store the internal state in <i>dscan.statefile</i> on exit. Use empty suppress list files <i>dscan.suppress.src</i> and <i>dscan.suppress.dst</i>. The output produced by flow-dscan typically must be manually inspected by using flow-filter and flow-print. Many of the alerts will be false until the suppress lists are populated for the local environment. </p>
<p> <code>flow-cat /flows/krc4 | flow-dscan -I25 -b -m -s dscan.statefile -p -W</code></p>
<h2>BUGS</h2>
<p> The ager should automatically become more aggressive when a low memory condition exists. There is no upper limit on the number of records that can be allocated. If the ager is not running often enough the host will be run out of memory.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
