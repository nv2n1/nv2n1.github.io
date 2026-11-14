---
title: "ibccquery(8)"
name: "ibccquery"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibccquery/"
description: "IBCCQUERY – query congestion control settings/info"
---

<p>IBCCQUERY &#8211; query congestion control settings/info</p>
<h2>Synopsis</h2>
<p>ibccquery [common_options] [-c cckey] &lt;op&gt; &lt;lid|guid&gt; [port]</p>
<h2>Description</h2>
<p>ibccquery support the querying of settings and other information related to congestion control.</p>
<h2>Options</h2>
<dl>
<dt><code>Current supported operations and their parameters:</code></p>
<dd>CongestionInfo (CI) &lt;addr&gt; CongestionKeyInfo (CK) &lt;addr&gt; CongestionLog (CL) &lt;addr&gt; SwitchCongestionSetting (SS) &lt;addr&gt; SwitchPortCongestionSetting (SP) &lt;addr&gt; [&lt;portnum&gt;] CACongestionSetting (CS) &lt;addr&gt; CongestionControlTable (CT) &lt;addr&gt; Timestamp (TI) &lt;addr&gt; </p>
<p> <code>&#8211;cckey, -c &lt;cckey&gt;</code> Specify a congestion control (CC) key. If none is specified, a key of 0 is used.</dl>
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
<h2>Files</h2>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h2>Examples</h2>
<pre>ibccquery CongestionInfo 3 # Congestion Info by lid
ibccquery SwitchPortCongestionSetting 3 # Query all Switch Port Congestion Settings
ibccquery SwitchPortCongestionSetting 3 1 # Query Switch Port Congestion Setting for port 1</pre>
<h2>Author</h2>
<dl>
<dt><code>Albert Chu</code></p>
<dd>&lt; <i>chu11 [at] llnl.gov</i> &gt; </p>
</dl>
