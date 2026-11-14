---
title: "ibccconfig(8)"
name: "ibccconfig"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibccconfig/"
description: "IBCCCONFIG – configure congestion control settings"
---

<p>IBCCCONFIG &#8211; configure congestion control settings</p>
<h2>Synopsis</h2>
<p>ibccconfig [common_options] [-c cckey] &lt;op&gt; &lt;lid|guid&gt; [port]</p>
<h2>Description</h2>
<p><code>ibccconfig</code> supports the configuration of congestion control settings on switches and HCAs. </p>
<p> <code>WARNING &#8212; You should understand what you are doing before using this tool. Misuse of this tool could result in a broken fabric.</code></p>
<h2>Options</h2>
<dl>
<dt><code>Current supported operations and their parameters:</code></p>
<dd>CongestionKeyInfo (CK) &lt;lid|guid&gt; &lt;cckey&gt; &lt;cckeyprotectbit&gt; &lt;cckeyleaseperiod&gt; &lt;cckeyviolations&gt; SwitchCongestionSetting (SS) &lt;lid|guid&gt; &lt;controlmap&gt; &lt;victimmask&gt; &lt;creditmask&gt; &lt;threshold&gt; &lt;packetsize&gt; &lt;csthreshold&gt; &lt;csreturndelay&gt; &lt;markingrate&gt; SwitchPortCongestionSetting (SP) &lt;lid|guid&gt; &lt;portnum&gt; &lt;valid&gt; &lt;control_type&gt; &lt;threshold&gt; &lt;packet_size&gt; &lt;cong_parm_marking_rate&gt; CACongestionSetting (CS) &lt;lid|guid&gt; &lt;port_control&gt; &lt;control_map&gt; &lt;ccti_timer&gt; &lt;ccti_increase&gt; &lt;trigger_threshold&gt; &lt;ccti_min&gt; CongestionControlTable (CT) &lt;lid|guid&gt; &lt;cctilimit&gt; &lt;index&gt; &lt;cctentry&gt; &lt;cctentry&gt; &#8230; </p>
<p> <code>&#8211;cckey, -c, &lt;cckey&gt;</code> Specify a congestion control (CC) key. If none is specified, a key of 0 is used.</dl>
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
<h3>Configuration flags</h3>
<dl>
<dt><code>-y, &#8211;m_key &lt;key&gt;</code></p>
<dd>use the specified M_key for requests. If non-numeric value (like &#8216;x&#8217;) is specified then a value will be prompted for. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</dl>
<h2>Examples</h2>
<pre>ibccconfig SwitchCongestionSetting 2 0x1F 0x1FFFFFFFFF 0x0 0xF 8 0 0:0 1 # Configure Switch Congestion Settings
ibccconfig CACongestionSetting 1 0 0x3 150 1 0 0 # Configure CA Congestion Settings to SL 0 and SL 1
ibccconfig CACongestionSetting 1 0 0x4 200 1 0 0 # Configure CA Congestion Settings to SL 2
ibccconfig CongestionControlTable 1 63 0 0:0 0:1 ... # Configure first block of Congestion Control Table
ibccconfig CongestionControlTable 1 127 0 0:64 0:65 ... # Configure second block of Congestion Control Table</pre>
<h2>Files</h2>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h2>Author</h2>
<dl>
<dt><code>Albert Chu</code></p>
<dd>&lt; <i>chu11 [at] llnl.gov</i> &gt; </p>
</dl>
