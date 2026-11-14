---
title: "smpdump(8)"
name: "smpdump"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smpdump/"
description: "SMPDUMP –"
---

<p>SMPDUMP &#8211;</p>
<h2>Dump Infiniband Subnet Management Attributes</h2>
<h3>Synopsis</h3>
<p>smpdump [options] &lt;dlid|dr_path&gt; &lt;attribute&gt; [attribute_modifier]</p>
<h3>Description</h3>
<p>smpdump is a general purpose SMP utility which gets SM attributes from a specified SMA. The result is dumped in hex by default.</p>
<h3>Options</h3>
<dl>
<dt><code>dlid|drpath</code></p>
<dd>LID or DR path to SMA</p>
<dt><code>attribute</code></p>
<dd>IBA attribute ID for SM attribute</p>
<dt><code>attribute_modifier</code></p>
<dd>IBA modifier for SM attribute</p>
<dt><code>-s, &#8211;string</code></p>
<dd>Print strings in packet if possible</dl>
<h3>Addressing Flags</h3>
<p><code>-D, &#8211;Direct</code> The address specified is a directed route </p>
<pre>Examples:
 [options] -D [options] &quot;0&quot; # self port
 [options] -D [options] &quot;0,1,2,1,4&quot; # out via port 1, then 2, ...
 (Note the second number in the path specified must match the port being
 used. This can be specified using the port selection flag '-P' or the
 port found through the automatic selection process.)</pre>
<p><code>-L, &#8211;Lid</code> The address specified is a LID</p>
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
<p><code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</p>
<h3>Files</h3>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>Examples</h3>
<p>Direct Routed Examples</p>
<dl>
<dt><code>::</code></p>
<dd>smpdump -D 0,1,2,3,5 16 # NODE DESC smpdump -D 0,1,2 0x15 2 # PORT INFO, port 2 </p>
<p> LID Routed Examples</p>
<dt><code>::</code></p>
<dd>smpdump 3 0x15 2 # PORT INFO, lid 3 port 2 smpdump 0xa0 0x11 # NODE INFO, lid 0xa0</dl>
<h3>See Also</h3>
<p>smpquery (8)</p>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>halr [at] voltaire.com</i> &gt; </p>
</dl>
