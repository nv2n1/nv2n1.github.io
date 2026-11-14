---
title: "vendstat(8)"
name: "vendstat"
section: "8"
letter: "v"
url: "/docs/linux/man/8-vendstat/"
description: "VENDSTAT –"
---

<p>VENDSTAT &#8211;</p>
<h2>Query Infiniband Vendor Specific Functions</h2>
<h3>Synopsis</h3>
<p>vendstat [options] &lt;lid|guid&gt;</p>
<h3>Description</h3>
<p>vendstat uses vendor specific MADs to access beyond the IB spec vendor specific functionality. Currently, there is support for Mellanox InfiniSwitch-III (IS3) and InfiniSwitch-IV (IS4).</p>
<h3>Options</h3>
<dl>
<dt><code>-N</code></p>
<dd>show IS3 or IS4 general information.</p>
<dt><code>-w</code></p>
<dd>show IS3 port xmit wait counters.</p>
<dt><code>-i</code></p>
<dd>show IS4 counter group info.</p>
<dt><code>-c &lt;num,num&gt;</code></p>
<dd>configure IS4 counter groups. </p>
<p> Configure IS4 counter groups 0 and 1. Such configuration is not persistent across IS4 reboot. First number is for counter group 0 and second is for counter group 1. </p>
<p> Group 0 counter config values:</p>
<dt><code>::</code></p>
<dd>0 &#8211; PortXmitDataSL0-7 1 &#8211; PortXmitDataSL8-15 2 &#8211; PortRcvDataSL0-7 </p>
<p> Group 1 counter config values:</p>
<dt><code>::</code></p>
<dd>1 &#8211; PortXmitDataSL8-15 2 &#8211; PortRcvDataSL0-7 8 &#8211; PortRcvDataSL8-15</p>
<dt><code>-R, &#8211;Read &lt;addr,mask&gt;</code></p>
<dd>Read configuration space record at addr</p>
<dt><code>-W, &#8211;Write &lt;addr,val,mask&gt;</code></p>
<dd>Write configuration space record at addr</dl>
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
<p><code>-t, &#8211;timeout &lt;timeout_ms&gt;</code> override the default timeout for the solicited mads. </p>
<p> <code>&#8211;config, -z &lt;config_file&gt;</code> Specify alternate config file. Default: /etc/infiniband-diags/ibdiag.conf</p>
<h3>Files</h3>
<h3>Config File</h3>
<p>/etc/infiniband-diags/ibdiag.conf </p>
<p> A global config file is provided to set some of the common options for all tools. See supplied config file for details.</p>
<h3>Examples</h3>
<dl>
<dt><code>::</code></p>
<dd>vendstat -N 6 # read IS3 or IS4 general information vendstat -w 6 # read IS3 port xmit wait counters vendstat -i 6 12 # read IS4 port 12 counter group info vendstat -c 0,1 6 12 # configure IS4 port 12 counter groups for PortXmitDataSL vendstat -c 2,8 6 12 # configure IS4 port 12 counter groups for PortRcvDataSL</dl>
<h3>Author</h3>
<dl>
<dt><code>Hal Rosenstock</code></p>
<dd>&lt; <i>hal.rosenstock [at] gmail.com</i> &gt; </p>
</dl>
