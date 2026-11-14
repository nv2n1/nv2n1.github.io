---
title: "flow-stat(1)"
name: "flow-stat"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-stat/"
description: "flow-stat – Generate reports with flow data."
---

<h2>NAME</h2>
<p> flow-stat &#8211; Generate reports with flow data.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-stat</code> [ <code>-hnpPw</code> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-f</code><i> format</i> ] [ <code>-S</code><i> sort_field</i> ] [ <code>-s</code><i> sort_field</i> ] [ <code>-t</code><i> tally_lines</i> ] [ <code>-T</code><i> title</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-stat</code> utility generates usage reports for flow data sets by IP address, IP address pairs, ports, packets, bytes, interfaces, next hops, autonomous systems, ToS bits, exporters, and tags.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-f</code><i> format</i></p>
<dd>
<pre>
Report format.  Choose from the following:
    0  Overall Summary
    1  Average packet size distribution
    2  Packets per flow distribution
    3  Octets per flow distribution
    4  Bandwidth per flow distribution
    5  UDP/TCP destination port
    6  UDP/TCP source port
    7  UDP/TCP port
    8  Destination IP
    9  Source IP
    10 Source/Destination IP
    11 Source or Destination IP
    12 IP protocol
    13 octets for flow duration plot data
    14 packets for flow duration plot data
    15 short summary
    16 IP Next Hop
    17 Input interface
    18 Output interface
    19 Source AS
    20 Destination AS
    21 Source/Destination AS
    22 IP ToS
    23 Input/Output Interface
    24 Source Prefix
    25 Destination Prefix
    26 Source/Destination Prefix
    27 Exporter IP
    28 Engine Id
    29 Engine Type
    30 Source Tag
    31 Destination Tag
    32 Source/Destination Tag
</pre>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-n</code></p>
<dd> Use symbolic names where appropriate.</p>
<dt><code>-p</code></p>
<dd> Display header information.</p>
<dt><code>-P</code></p>
<dd> Report as percent total.</p>
<dt><code>-s</code><i> sort_field</i></p>
<dd> Sort ascending on field <i>sort_field</i>.</p>
<dt><code>-S</code><i> sort_field</i></p>
<dd> Sort descending on field <i>sort_field</i>.</p>
<dt><code>-t</code><i> tally_lines</i></p>
<dd> Tally totals every <i>tally_lines</i>lines.</p>
<dt><code>-T</code><i> title</i></p>
<dd> Set report title to <i>title</i>.</p>
<dt><code>-w</code></p>
<dd> Wide output.</dl>
<h2>EXAMPLES</h2>
<p> Provide a report on top source/destination IP pairs sorted by octets, report in percent total form for the flows in <i>/flows/krc4</i>. Use the preload option to flow-cat to preserve meta information and display it with flow-stat. </p>
<p> <code>flow-cat -p /flows/krc4 | flow-stat -f10 -P -p -S4</code></p>
<h2>EXAMPLES</h2>
<p> Many times a campus network will have a single border router which has one interface pointing to the internal side and many interfaces pointing to other providers. These interfaces each have a unique numerical id known in SNMP terms as an ifIndex. The ifIndex to interface name mappings can be determined by using a tool such as <code>snmpwalk</code> or using show commands in recent versions of IOS with the &#8216;show snmp mib ifmib ifindex&#8217; or JunOS &#8216;show interfaces&#8217;. Once the ifIndex for each interface is known flow-filter can be combined with flow-stat to provide reports such as inbound vs outbound top src/destination IP addresses. Provide a top source IP address report by outbound traffic, ie the top senders of traffic on the campus network. Assume the ifIndex of the campus interface is 5. </p>
<p> flow-cat -p /flows/krc4 | flow-filter -i5 | flow-stat -f9 -P -p -S3</p>
<h2>EXAMPLES</h2>
<p> Provide a top destination IP address report by outbound traffic, ie the top sinks of traffic on the campus network. Assume the ifIndex of the campus interface is 5. </p>
<p> flow-cat -p /flows/krc4 | flow-filter -I5 | flow-stat -f8 -P -p -S3</p>
<h2>EXAMPLES</h2>
<p> Provide a top source/destination AS report. Use symbolic names. </p>
<p> flow-cat -p /flows/krc4 | flow-stat -f20 -n -P -p -S4</p>
<h2>BUGS</h2>
<p> None known.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
