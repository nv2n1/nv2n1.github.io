---
title: "ocf_heartbeat_sapinstance(7)"
name: "ocf_heartbeat_sapinstance"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sapinstance/"
description: "ocf_heartbeat_SAPInstance – Manages a SAP instance"
---

<p>ocf_heartbeat_SAPInstance &#8211; Manages a SAP instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SAPInstance</code> [start | stop | status | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for SAP. It manages a SAP Instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>InstanceName</code></p>
<dl>
<dd>The full qualified SAP instance name. e.g. P01_DVEBMGS00_sapp01ci (required, string, no default)</dl>
<p> <code>DIR_EXECUTABLE</code></p>
<dl>
<dd>The full qualified path where to find sapstartsrv and sapcontrol. (optional, string, no default)</dl>
<p> <code>DIR_PROFILE</code></p>
<dl>
<dd>The full qualified path where to find the SAP START profile. (optional, string, no default)</dl>
<p> <code>START_PROFILE</code></p>
<dl>
<dd>The name of the SAP START profile. (optional, string, no default)</dl>
<p> <code>START_WAITTIME</code></p>
<dl>
<dd>After that time in seconds a monitor operation is executed by the resource agent. Does the monitor return SUCCESS, the start is handled as SUCCESS. This is useful to resolve timing problems with e.g. the J2EE-Addin instance. (optional, string, default 3600)</dl>
<p> <code>AUTOMATIC_RECOVER</code></p>
<dl>
<dd>The SAPInstance resource agent tries to recover a failed start attempt automaticaly one time. This is done by killing runing instance processes and executing cleanipc. (optional, boolean, default false)</dl>
<p> <code>MONITOR_SERVICES</code></p>
<dl>
<dd>(optional, string, default disp+work|msg_server|enserver|enrepserver|jcontrol|jstart)</dl>
<p> <code>ERS_InstanceName</code></p>
<dl>
<dd>(optional, string, no default)</dl>
<p> <code>ERS_START_PROFILE</code></p>
<dl>
<dd>(optional, string, no default)</dl>
<p> <code>PRE_START_USEREXIT</code></p>
<dl>
<dd>The full qualified path where to find a script or program which should be executed before this resource gets started. (optional, string, no default)</dl>
<p> <code>POST_START_USEREXIT</code></p>
<dl>
<dd>The full qualified path where to find a script or program which should be executed after this resource got started. (optional, string, no default)</dl>
<p> <code>PRE_STOP_USEREXIT</code></p>
<dl>
<dd>The full qualified path where to find a script or program which should be executed before this resource gets stopped. (optional, string, no default)</dl>
<p> <code>POST_STOP_USEREXIT</code></p>
<dl>
<dd>The full qualified path where to find a script or program which should be executed after this resource got stopped. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 180.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 240.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 120.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 320.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 320.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a SAPInstance resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_SAPInstance ocf:heartbeat:SAPInstance \
params \
InstanceName=string \
op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;120&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/SAPInstance_(resource_agent)">http://www.linux-ha.org/wiki/SAPInstance_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
