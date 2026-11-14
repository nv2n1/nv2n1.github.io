---
title: "flow-capture(1)"
name: "flow-capture"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flow-capture/"
description: "flow-capture – Manage storage of flow file archives by expiring old data."
---

<h2>NAME</h2>
<p> flow-capture &#8211; Manage storage of flow file archives by expiring old data.</p>
<h2>SYNOPSIS</h2>
<p> <code>flow-capture</code> [ <code>-hu</code> ] [ <code>-b</code><i> big|little</i> ] [ <code>-C</code><i> comment</i> ] [ <code>-c</code><i> flow_clients</i> ] [ <code>-d</code><i> debug_level</i> ] [ <code>-D</code><i> daemonize</i> ] [ <code>-e</code><i> expire_count</i> ] [ <code>-f</code><i> filter_fname</i> ] [ <code>-F</code><i> filter_definition</i> ] [ <code>-E</code><i> expire_size</i> ] [ <code>-n</code><i> rotations</i> ] [ <code>-N</code><i> nesting_level</i> ] [ <code>-p</code><i> pidfile</i> ] [ <code>-R</code><i> rotate_program</i> ] [ <code>-S</code><i> stat_interval</i> ] [ <code>-t</code><i> tag_fname</i> ] [ <code>-T</code><i> active_def</i><code>|</code><i>active_def,active_def</i><i>&#8230;</i> ] [ <code>-V</code><i> pdu_version</i> ] [ <code>-z</code><i> z_level</i> ] <code>-w</code><i> workdir</i> [ <code>-x</code><i> xlate_fname</i> ] [ <code>-X</code><i> xlate_definition</i> ] <i>localip/remoteip/port</i></p>
<h2>DESCRIPTION</h2>
<p> The <code>flow-capture</code> utility will receive and store NetFlow exports to disk. The flow files are rotated <i>rotations</i>times per day and expiration of old flow files can be configured by number of files or total space utilization. Files are stored in <i>workdir</i> and can optionally be stored in additional levels of directories. Active files created by <code>flow-capture</code> begin with &#8216;tmp&#8217;. Files that are complete begin with &#8216;ft&#8217;. </p>
<p> When the <i>remoteip</i> is configured only flows from that exporter will be processed, this is the most secure and recommended configuration. When the <i>localip</i> is configured <code>flow-capture</code> will only process flows sent to the <i> localip</i> IP address. If <i>remoteip</i> is 0 (not configured) flows from any source IP address are accepted. Multiple non aggregated PDU versions may be accepted at once to support Cisco&#8217;s Catalyst 6500 NetFlow implementation which exports from both the supervisor and MSFC with the same IP address and same port but different export versions. In this case the exports will be stored in the format specified by <i>pdu_version</i> or whichever export type is received first. </p>
<p> NetFlow exports are UDP and do not employ congestion control or a retransmission mechanism. If the server flow-capture is configured on is too busy, or the network is congested or lossy NetFlow exports will be lost. An estimate of lost flows is recorded in the flow files, and logged via syslog. Most servers will provide a count of dropped packets due to full socket buffers via the <code>netstat</code> utility. For example <code>netstat -s | grep full</code> will provide a count of UDP packets dropped due to full socket buffers. If this is a persistent occurrence either <code>flow-capture</code> will need a larger server or the compression level should be decreased with -z. </p>
<p> A SIGHUP signal will cause <code>flow-capture</code> to close the current file and create a new one. </p>
<p> A SIGQUIT or SIGTERM signal will cause <code>flow-capture</code> to close the current file and exit.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-b</code><i> big</i><code>|</code><i>little</i></p>
<dd> Byte order of output.</p>
<dt><code>-c</code><i> flow_clients</i></p>
<dd> Enable <i>flow_clients</i> TCP clients. When libwrap is available the client must be in a permit list for the service flow-capture-client.</p>
<dt><code>-C</code><i> Comment</i></p>
<dd> Add a comment.</p>
<dt><code>-d</code><i> debug_level</i></p>
<dd> Enable debugging.</p>
<dt><code>-e</code><i> expire_count</i></p>
<dd> Retain the maximum number of files so that the total file count is less than <i>expire_count</i>. Defaults to 0 (do not expire).</p>
<dt><code>-E</code><i> expire_size</i></p>
<dd> Retain the maximum number of files so that the total storage is less than <i>expire_size</i>. The letters b,K,M,G can be used as multipliers, ie 16 Megabytes is 16M. Default to 0 (do not expire).</p>
<dt><code>-f</code><i> filter_fname</i></p>
<dd> Filter list filename. Defaults to <i>/etc/flow-tools/cfg/filter</i>.</p>
<dt><code>-F</code><i> filter_definition</i></p>
<dd> Select the active definition. Defaults to default.</p>
<dt><code>-h</code></p>
<dd> Display help.</p>
<dt><code>-n</code><i> rotations</i></p>
<dd> Configure the number of times flow-capture will create a new file per day. The default is 95, or every 15 minutes.</p>
<dt><code>-N</code><i> nesting_level</i></p>
<dd> Configure the nesting level for storing flow files. The default is 0. -3 YYYY/YYYY-MM/YYYY-MM-DD/flow-file -2 YYYY-MM/YYYY-MM-DD/flow-file -1 YYYY-MM-DD/flow-file 0 flow-file 1 YYYY/flow-file 2 YYYY/YYYY-MM/flow-file 3 YYYY/YYYY-MM/YYYY-MM-DD/flow-file</p>
<dt><code>-p</code><i> pidfile</i></p>
<dd> Configure the process ID file. Use &#8211; to disable pid file creation.</p>
<dt><code>-R</code><i> rotate_program</i></p>
<dd> Execute <i>rotate_program</i> with the first argument as the flow file name after rotating it.</p>
<dt><code>-S</code><i> stat_interval</i></p>
<dd> When configured <code>flow-capture</code> will log a timestamped message every <i>stat_interval</i> minutes indicating counters such as the number of flows received, packets processed, and lost flows.</p>
<dt><code>-t</code><i> tag_fname</i></p>
<dd> Load tags from <i>tag_name</i></p>
<dt><code>-T</code><i> active_def</i><code>|</code><i>active_def,active_def&#8230;</i></p>
<dd> Use <i>active_def</i> as the active tag definition(s).</p>
<dt><code>-u</code></p>
<dd> Preserve inherited umask. By default the umask will be set to 0022.</p>
<dt><code>-V</code><i> pdu_version</i></p>
<dd> Use <i>pdu_version</i> format output. </p>
<pre>
    1    NetFlow version 1 (No sequence numbers, AS, or mask)
    5    NetFlow version 5
    6    NetFlow version 6 (5+ Encapsulation size)
    7    NetFlow version 7 (Catalyst switches)
    8.1  NetFlow AS Aggregation
    8.2  NetFlow Proto Port Aggregation
    8.3  NetFlow Source Prefix Aggregation
    8.4  NetFlow Destination Prefix Aggregation
    8.5  NetFlow Prefix Aggregation
    8.6  NetFlow Destination (Catalyst switches)
    8.7  NetFlow Source Destination (Catalyst switches)
    8.8  NetFlow Full Flow (Catalyst switches)
    8.9  NetFlow ToS AS Aggregation
    8.10 NetFlow ToS Proto Port Aggregation
    8.11 NetFlow ToS Source Prefix Aggregation
    8.12 NetFlow ToS Destination Prefix Aggregation
    8.13 NetFlow ToS Prefix Aggregation
    8.14 NetFlow ToS Prefix Port Aggregation
    1005 Flow-Tools tagged version 5
</pre>
<dt><code>-w</code><i> workdir</i></p>
<dd> Work in <i>workdir</i>.</p>
<dt><code>-x</code><i> xlate_fname</i></p>
<dd> Translation config file name. Defaults to <i>/etc/flow-tools/cfg/xlate.c fg</i></p>
<dt><code>-X</code><i> xlate_definition</i></p>
<dd> Translation definition. Defaults to default.</p>
<dt><code>-z</code><i> z_level</i></p>
<dd> Configure compression level to <i> z_level</i>. 0 is disabled (no compression), 9 is highest compression.</dl>
<h2>EXAMPLES</h2>
<p> Receive flows from the exporter at 10.0.0.1 port 9800. Maintain 5 Gigabytes of flow files in /flows/krc4. Mask the source and destination IP addresses contained in the flow exports with 255.255.248.0. </p>
<p> <code>flow-capture -w /flows/krc4 -m 255.255.248.0 -E5G 0/10.0.0.1/9800</code> </p>
<p> Receive flows from any exporter on port 9800. Do not perform any flow file space management. Store the exports in /flows/krc4. Emit a stat log message every 5 minutes. </p>
<p> <code>flow-capture -w /flows/krc4 0/0/9800 -S5</code></p>
<h2>BUGS</h2>
<p> Empty directories are not removed.</p>
<h2>FILES</h2>
<p> Configuration files: Tag &#8211; <i>/etc/flow-tools/cfg/tag.cfg</i>. Filter &#8211; <i>/etc/flow-tools/cfg/filter.cfg</i>. Xlate &#8211; <i>/etc/flow-tools/cfg/xlate.cfg</i>.</p>
<h2>AUTHOR</h2>
<p> Mark Fullmer &lt;maf [at] splintered.net&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-flow-tools/">flow-tools</a></code>(1) </p>
<h2>Index</h2>
