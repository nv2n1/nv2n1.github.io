---
title: "perfquery(8)"
name: "perfquery"
section: "8"
letter: "p"
url: "/docs/linux/man/8-perfquery/"
description: "PERFQUERY –"
---

<p>PERFQUERY &#8211;</p>
<h2>Query Infiniband Port Counters On A Single Port</h2>
<h3>Synopsis</h3>
<p>perfquery [options] [&lt;lid|guid&gt; [[port(s)] [reset_mask]]]</p>
<h3>Description</h3>
<p>perfquery uses PerfMgt GMPs to obtain the PortCounters (basic performance and error counters), PortExtendedCounters, PortXmitDataSL, PortRcvDataSL, PortRcvErrorDetails, PortXmitDiscardDetails, PortExtendedSpeedsCounters, or PortSamplesControl from the PMA at the node/port specified. Optionally shows aggregated counters for all ports of node. Finally it can, reset after read, or just reset the counters. </p>
<p> Note: In PortCounters, PortCountersExtended, PortXmitDataSL, and PortRcvDataSL, components that represent Data (e.g. PortXmitData and PortRcvData) indicate octets divided by 4 rather than just octets. </p>
<p> Note: Inputting a port of 255 indicates an operation be performed on all ports. </p>
<p> Note: For PortCounters, ExtendedCounters, and resets, multiple ports can be specified by either a comma separated list or a port range. See examples below.</p>
<h3>Options</h3>
<dl>
<dt><code>-x, &#8211;extended</code></p>
<dd>show extended port counters rather than (basic) port counters. Note that extended port counters attribute is optional.</p>
<dt><code>-X, &#8211;xmtsl</code></p>
<dd>show transmit data SL counter. This is an optional counter for QoS.</p>
<dt><code>-S, &#8211;rcvsl</code></p>
<dd>show receive data SL counter. This is an optional counter for QoS.</p>
<dt><code>-D, &#8211;xmtdisc</code></p>
<dd>show transmit discard details. This is an optional counter.</p>
<dt><code>-E, &#8211;rcverr</code></p>
<dd>show receive error details. This is an optional counter.</p>
<dt><code>-D, &#8211;xmtdisc</code></p>
<dd>show transmit discard details. This is an optional counter.</p>
<dt><code>-T, &#8211;extended_speeds</code></p>
<dd>show extended speeds port counters. This is an optional counter.</p>
<dt><code>&#8211;oprcvcounters</code></p>
<dd>show Rcv Counters per Op code. This is an optional counter.</p>
<dt><code>&#8211;flowctlcounters</code></p>
<dd>show flow control counters. This is an optional counter.</p>
<dt><code>&#8211;vloppackets</code></p>
<dd>show packets received per Op code per VL. This is an optional counter.</p>
<dt><code>&#8211;vlopdata</code></p>
<dd>show data received per Op code per VL. This is an optional counter.</p>
<dt><code>&#8211;vlxmitflowctlerrors</code></p>
<dd>show flow control update errors per VL. This is an optional counter.</p>
<dt><code>&#8211;vlxmitcounters</code></p>
<dd>show ticks waiting to transmit counters per VL. This is an optional counter.</p>
<dt><code>&#8211;swportvlcong</code></p>
<dd>show sw port VL congestion. This is an optional counter.</p>
<dt><code>&#8211;rcvcc</code></p>
<dd>show Rcv congestion control counters. This is an optional counter.</p>
<dt><code>&#8211;slrcvfecn</code></p>
<dd>show SL Rcv FECN counters. This is an optional counter.</p>
<dt><code>&#8211;slrcvbecn</code></p>
<dd>show SL Rcv BECN counters. This is an optional counter.</p>
<dt><code>&#8211;xmitcc</code></p>
<dd>show Xmit congestion control counters. This is an optional counter.</p>
<dt><code>&#8211;vlxmittimecc</code></p>
<dd>show VL Xmit Time congestion control counters. This is an optional counter.</p>
<dt><code>-c, &#8211;smplctl</code></p>
<dd>show port samples control.</p>
<dt><code>-a, &#8211;all_ports</code></p>
<dd>show aggregated counters for all ports of the destination lid, reset all counters for all ports, or if multiple ports are specified, aggregate the counters of the specified ports. If the destination lid does not support the AllPortSelect flag, all ports will be iterated through to emulate AllPortSelect behavior.</p>
<dt><code>-l, &#8211;loop_ports</code></p>
<dd>If all ports are selected by the user (either through the <code>-a</code> option or port 255) or multiple ports are specified iterate through each port rather than doing than aggregate operation.</p>
<dt><code>-r, &#8211;reset_after_read</code></p>
<dd>reset counters after read</p>
<dt><code>-R, &#8211;Reset_only</code></p>
<dd>only reset counters</dl>
<h3>Addressing Flags</h3>
<p><code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
<p> <code>-L, &#8211;Lid</code> The address specified is a LID </p>
<p> <code>-s, &#8211;sm_port &lt;smlid&gt;</code> use &#8216;smlid&#8217; as the target lid for SA queries.</p>
<h3>Port Selection flags</h3>
<p><code>-C, &#8211;Ca &lt;ca_name&gt;</code> use the specified ca_name. </p>
<p> <code>-P, &#8211;Port &lt;ca_port&gt;</code> use the specified ca_port.</p>
<h3>Local port Selection</h3>
<p>Multiple port/Multiple CA support: when no IB device or port is specified (see the &quot;local umad parameters&quot; below), the libibumad library selects the port to use by the following criteria:</p>
<dl>
<dt>1.</p>
<dd>the first port that is ACTIVE.</p>
<dt>2.</p>
<dd>if not found, the first port that is UP (physical link up). </p>
<p> If a port and/or CA name is specified, the libibumad library attempts to fulfill the user request, and will fail if it is not possible. </p>
<p> For example: </p>
<pre>ibaddr # use the first port (criteria #1 above)
ibaddr -C mthca1 # pick the best port from &quot;mthca1&quot; only.
ibaddr -P 2 # use the second (active/up) port from the first available IB device.
ibaddr -C mthca0 -P 2 # use the specified port only.</pre>
</dl>
<h3>Debugging flags</h3>
<dl>
<dt><code>-d</code></p>
<dd>raise the IB debugging level. May be used several times (-ddd or -d -d -d).</p>
<dt><code>-e</code></p>
<dd>show send and receive errors (timeouts and others) </p>
<p> <code>-h, &#8211;help</code> show the usage message</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info.</dl>
<h3>Configuration flags</h3>
<p><code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads.</p>
<dl>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</dl>
<h3>Files</h3>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>Examples</h3>
<pre>perfquery # read local port performance counters
perfquery 32 1 # read performance counters from lid 32, port 1
perfquery -x 32 1 # read extended performance counters from lid 32, port 1
perfquery -a 32 # read perf counters from lid 32, all ports
perfquery -r 32 1 # read performance counters and reset
perfquery -x -r 32 1 # read extended performance counters and reset
perfquery -R 0x20 1 # reset performance counters of port 1 only
perfquery -x -R 0x20 1 # reset extended performance counters of port 1 only
perfquery -R -a 32 # reset performance counters of all ports
perfquery -R 32 2 0x0fff # reset only error counters of port 2
perfquery -R 32 2 0xf000 # reset only non-error counters of port 2
perfquery -a 32 1-10 # read performance counters from lid 32, port 1-10, aggregate output
perfquery -l 32 1-10 # read performance counters from lid 32, port 1-10, output each port
perfquery -a 32 1,4,8 # read performance counters from lid 32, port 1, 4, and 8, aggregate output
perfquery -l 32 1,4,8 # read performance counters from lid 32, port 1, 4, and 8, output each port</pre>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>hal.rosenstock [at] gmail.com</i> &gt; </p>
</dl>
