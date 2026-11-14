---
title: "ibqueryerrors(8)"
name: "ibqueryerrors"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibqueryerrors/"
description: "IBQUERYERRORS – query and report IB port counters"
---

<p>IBQUERYERRORS &#8211; query and report IB port counters</p>
<h2>Synopsis</h2>
<p>ibqueryerrors [options]</p>
<h2>Description</h2>
<p>The default behavior is to report the port error counters which exceed a threshold for each port in the fabric. The default threshold is zero (0). Error fields can also be suppressed entirely. </p>
<p> In addition to reporting errors on every port. ibqueryerrors can report the port transmit and receive data as well as report full link information to the remote port if available.</p>
<h2>Options</h2>
<p><code>-s, &#8211;suppress &lt;err1,err2,&#8230;&gt;</code> Suppress the errors listed in the comma separated list provided. </p>
<p> <code>-c, &#8211;suppress-common</code> Suppress some of the common &quot;side effect&quot; counters. These counters usually do not indicate an error condition and can be usually be safely ignored. </p>
<p> <code>-r, &#8211;report-port</code> Report the port information. This includes LID, port, external port (if applicable), link speed setting, remote GUID, remote port, remote external port (if applicable), and remote node description information. </p>
<p> <code>&#8211;data</code> Include the optional transmit and receive data counters. </p>
<p> <code>&#8211;threshold-file &lt;filename&gt;</code> Specify an alternate threshold file. The default is /etc/infiniband-diags/error_thresholds </p>
<p> <code>&#8211;switch</code> print data for switch&#8217;s only </p>
<p> <code>&#8211;ca</code> print data for CA&#8217;s only </p>
<p> <code>&#8211;skip-sl</code> Use the default sl for queries. This is not recommended when using a QoS aware routing engine as it can cause a credit deadlock. </p>
<p> <code>&#8211;router</code> print data for routers only </p>
<p> <code>&#8211;clear-errors -k</code> Clear error counters after read. </p>
<p> <code>&#8211;clear-counts -K</code> Clear data counters after read. </p>
<p> <code>CAUTION</code> clearing data or error counters will occur regardless of if they are printed or not. See <code>&#8211;counters</code> and <code>&#8211;data</code> for details on controling which counters are printed. </p>
<p> <code>&#8211;details</code> include receive error and transmit discard details </p>
<p> <code>&#8211;counters</code> print data counters only</p>
<h3>Partial Scan flags</h3>
<p>The node to start a partial scan can be specified with the following addresses. </p>
<p> <code>&#8211;port-guid, -G &lt;port_guid&gt;</code> Specify a port_guid </p>
<p> <code>-D, &#8211;Direct &lt;dr_path&gt;</code> The address specified is a directed route </p>
<pre>Examples:
 -D &quot;0&quot; # self port
 -D &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>Note:</code> For switches results are printed for all ports not just switch port 0. </p>
<p> <code>-S &lt;port_guid&gt;</code> same as &quot;-G&quot;. (provided only for backward compatibility)</p>
<h3>Cache File flags</h3>
<p><code>&#8211;load-cache &lt;filename&gt;</code> Load and use the cached ibnetdiscover data stored in the specified filename. May be useful for outputting and learning about other fabrics or a previous state of a fabric.</p>
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
<h3>Configuration flags</h3>
<p><code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</p>
<dl>
<dt><code>&#8211;outstanding_smps, -o &lt;val&gt;</code></p>
<dd>Specify the number of outstanding SMP&#8217;s which should be issued during the scan </p>
<p> Default: 2 </p>
<p> <code>&#8211;node-name-map &lt;node-name-map&gt;</code> Specify a node name map. This file maps GUIDs to more user friendly names. See FILES section. </p>
<p> <code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads.</p>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for.</dl>
<h3>Debugging flags</h3>
<dl>
<dt><code>-d</code></p>
<dd>raise the IB debugging level. May be used several times (-ddd or -d -d -d).</p>
<dt><code>-e</code></p>
<dd>show send and receive errors (timeouts and others) </p>
<p> <code>-h, &#8211;help</code> show the usage message</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>increase the application verbosity level. May be used several times (-vv or -v -v -v) </p>
<p> <code>-V, &#8211;version</code> show the version info. </p>
<p> <code>-R</code> (This option is obsolete and does nothing)</dl>
<h2>Exit Status</h2>
<p><code>-1</code> if scan fails. </p>
<p> <code>0</code> if scan succeeds without errors beyond thresholds </p>
<p> <code>1</code> if errors are found beyond thresholds or inconsistencies are found in check mode.</p>
<h2>Files</h2>
<h3>Error Threshold</h3>
<p>/etc/infiniband-diags/error_thresholds </p>
<p> Define threshold values for errors. File format is simple &quot;name=val&quot;. Comments begin with &#8216;#&#8217; </p>
<p> <code>Example:</code> </p>
<pre># Define thresholds for error counters
SymbolErrorCounter=10
LinkErrorRecoveryCounter=10
VL15Dropped=100</pre>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>Node Name Map File Format</h3>
<p>The node name map is used to specify user friendly names for nodes in the output. GUIDs are used to perform the lookup. </p>
<p> This functionality is provided by the opensm-libs package. See <code><a href="/docs/linux/man/8-opensm/">opensm</a>(8)</code> for the file location for your installation. </p>
<p> <code>Generically:</code> </p>
<pre># comment
&lt;guid&gt; &quot;&lt;name&gt;&quot;</pre>
<p><code>Example:</code> </p>
<pre># IB1
# Line cards
0x0008f104003f125c &quot;IB1 (Rack 11 slot 1 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f125d &quot;IB1 (Rack 11 slot 1 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10d2 &quot;IB1 (Rack 11 slot 2 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10d3 &quot;IB1 (Rack 11 slot 2 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
0x0008f104003f10bf &quot;IB1 (Rack 11 slot 12 ) ISR9288/ISR9096 Voltaire sLB-24D&quot;
# Spines
0x0008f10400400e2d &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e2e &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e2f &quot;IB1 (Rack 11 spine 1 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e31 &quot;IB1 (Rack 11 spine 2 ) ISR9288 Voltaire sFB-12D&quot;
0x0008f10400400e32 &quot;IB1 (Rack 11 spine 2 ) ISR9288 Voltaire sFB-12D&quot;
# GUID Node Name
0x0008f10400411a08 &quot;SW1 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f10400411a28 &quot;SW2 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f10400411a34 &quot;SW3 (Rack 3) ISR9024 Voltaire 9024D&quot;
0x0008f104004119d0 &quot;SW4 (Rack 3) ISR9024 Voltaire 9024D&quot;</pre>
<h2>Author</h2>
<dl>
<dt><code>Ira Weiny</code></p>
<dd>&lt; <i>ira.weiny [at] intel.com</i> &gt; </p>
</dl>
