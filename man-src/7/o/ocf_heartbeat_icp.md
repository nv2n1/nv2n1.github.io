---
title: "ocf_heartbeat_icp(7)"
name: "ocf_heartbeat_icp"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_icp/"
---


 </p>
<h2>SYNOPSIS</h2>
<dl>
<dt><code>ICP</code> [start | stop | status | monitor | meta-data | validate-all] </dt>
</dl>
<h2>DESCRIPTION</h2>
<dd> <p> Resource script for ICP. It Manages an ICP Vortex clustered host drive as an HA resource.  </p>
<h2>SUPPORTED PARAMETERS</h2>
<p> <code>driveid</code> </p>
 </dd>
<dl>
<dd> <p> The ICP cluster drive ID. (required, string, no default) </p>
 </dd></dl>
<p> <code>device</code> </p>
<dl>
<dd> <p> The device name. (required, string, no default) </p>
 </dd></dl>
<h2>SUPPORTED ACTIONS</h2>
<p> This resource agent supports the following actions (operations): </p>
<p> <code>start</code> </p>
<dl>
<dd> <p> Starts the resource. Suggested minimum timeout: 20. </p>
 </dd></dl>
<p> <code>stop</code> </p>
<dl>
<dd> <p> Stops the resource. Suggested minimum timeout: 20. </p>
 </dd></dl>
<p> <code>status</code> </p>
<dl>
<dd> <p> Performs a status check. Suggested minimum timeout: 20. Suggested interval: 10. </p>
 </dd></dl>
<p> <code>monitor</code> </p>
<dl>
<dd> <p> Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10. </p>
 </dd></dl>
<p> <code>validate-all</code> </p>
<dl>
<dd> <p> Performs a validation of the resource configuration. Suggested minimum timeout: 5. </p>
 </dd></dl>
<p> <code>meta-data</code> </p>
<dl>
<dd> <p> Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5. </p>
 </dd></dl>
<h2>EXAMPLE</h2>
<p> The following is an example configuration for a ICP resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd> <pre><code>primitive example_ICP ocf:heartbeat:ICP \
  params \
    driveid= string  \
    device= string  \
  op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot;
</code></pre>
 </dd></dl>
<h2>SEE ALSO</h2>
<p> m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ICP_(resource_agent)">http://www.linux-ha.org/wiki/ICP_(resource_agent)</a></code>m[]  </p>
<h2>AUTHOR</h2>
<p> <code>Linux-HA contributors (see the resource agent source for information about individual authors)</code> </p>
