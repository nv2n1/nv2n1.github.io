---
title: "ibaddr(8)"
name: "ibaddr"
section: "8"
letter: "i"
url: "/docs/linux/man/8-ibaddr/"
description: "IBADDR – query InfiniBand address(es)"
---

<p>IBADDR &#8211; query InfiniBand address(es)</p>
<h2>Synopsis</h2>
<p>ibaddr [options]</p>
<h2>Description</h2>
<p>Display the lid (and range) as well as the GID address of the port specified (by DR path, lid, or GUID) or the local port by default. </p>
<p> Note: this utility can be used as simple address resolver.</p>
<h2>Options</h2>
<p><code>&#8211;gid_show, -g</code> show gid address only </p>
<p> <code>&#8211;lid_show, -l</code> show lid range only </p>
<p> <code>&#8211;Lid_show, -L</code> show lid range (in decimal) only</p>
<h3>Addressing Flags</h3>
<p><code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-G, &#8211;Guid</code> The address specified is a Port GUID </p>
<p> <code>-s, &#8211;sm_port &lt;smlid&gt;</code> use &#8216;smlid&#8217; as the target lid for SA queries.</p>
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
<p> <code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</dl>
<h2>Files</h2>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h2>Examples</h2>
<pre>ibaddr # local port\'s address
ibaddr 32 # show lid range and gid of lid 32
ibaddr -G 0x8f1040023 # same but using guid address
ibaddr -l 32 # show lid range only
ibaddr -L 32 # show decimal lid range only
ibaddr -g 32 # show gid address only</pre>
<h2>See Also</h2>
<p><code>ibroute (8), ibtracert (8)</code></p>
<h2>Author</h2>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
