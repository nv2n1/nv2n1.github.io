---
title: "sminfo(8)"
name: "sminfo"
section: "8"
letter: "s"
url: "/docs/linux/man/8-sminfo/"
description: "SMINFO –"
---

<p>SMINFO &#8211;</p>
<h2>Query Infiniband Sminfo Attribute</h2>
<h3>Synopsis</h3>
<p>sminfo [options] sm_lid | sm_dr_path [modifier]</p>
<h3>Description</h3>
<p>Optionally set and display the output of a sminfo query in human readable format. The target SM is the one listed in the local port info, or the SM specified by the optional SM lid or by the SM direct routed path. </p>
<p> Note: using sminfo for any purposes other then simple query may be very dangerous, and may result in a malfunction of the target SM.</p>
<h3>Options</h3>
<dl>
<dt><code>-s, &#8211;state &lt;state&gt;</code> set SM state</p>
<dd>0 not active </p>
<p> 1 discovering </p>
<p> 2 standby </p>
<p> 3 master </p>
<p> <code>-p, &#8211;priority &lt;priority&gt;</code> set priority (0-15) </p>
<p> <code>-a, &#8211;activity &lt;val&gt;</code> set activity count</dl>
<h3>Addressing Flags</h3>
<p><code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
<p> <code>-L, &#8211;Lid</code> The address specified is a LID</p>
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
<dl>
<dt><code>::</code></p>
<dd>sminfo # local port&#8217;s sminfo sminfo 32 # show sminfo of lid 32 sminfo -G 0x8f1040023 # same but using guid address</dl>
<h3>See Also</h3>
<p>smpdump (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
