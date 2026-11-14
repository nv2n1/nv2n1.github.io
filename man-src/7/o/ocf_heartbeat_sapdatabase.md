---
title: "ocf_heartbeat_sapdatabase(7)"
name: "ocf_heartbeat_sapdatabase"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_sapdatabase/"
description: "ocf_heartbeat_SAPDatabase – Manages any SAP database (based on Oracle, MaxDB, or DB2)"
---

<p>ocf_heartbeat_SAPDatabase &#8211; Manages any SAP database (based on Oracle, MaxDB, or DB2)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>SAPDatabase</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for SAP databases. It manages a SAP database of any type as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>SID</code></p>
<dl>
<dd>The unique SAP system identifier. e.g. P01 (required, string, no default)</dl>
<p> <code>DIR_EXECUTABLE</code></p>
<dl>
<dd>The full qualified path where to find sapstartsrv and sapcontrol. (optional, string, no default)</dl>
<p> <code>DBTYPE</code></p>
<dl>
<dd>The name of the database vendor you use. Set either: ORA,DB6,ADA (required, string, no default)</dl>
<p> <code>NETSERVICENAME</code></p>
<dl>
<dd>The Oracle TNS listener name. (optional, string, no default)</dl>
<p> <code>DBJ2EE_ONLY</code></p>
<dl>
<dd>If you do not have a ABAP stack installed in the SAP database, set this to TRUE (optional, boolean, default false)</dl>
<p> <code>JAVA_HOME</code></p>
<dl>
<dd>This is only needed if the DBJ2EE_ONLY parameter is set to true. Enter the path to the Java SDK which is used by the SAP WebAS Java (optional, string, no default)</dl>
<p> <code>STRICT_MONITORING</code></p>
<dl>
<dd>This controls how the resource agent monitors the database. If set to true, it will use SAP tools to test the connect to the database. Do not use with Oracle, because it will result in unwanted failovers in case of an archiver stuck (optional, boolean, default false)</dl>
<p> <code>AUTOMATIC_RECOVER</code></p>
<dl>
<dd>The SAPDatabase resource agent tries to recover a failed start attempt automaticaly one time. This is done by running a forced abort of the RDBMS and/or executing recovery commands. (optional, boolean, default false)</dl>
<p> <code>DIR_BOOTSTRAP</code></p>
<dl>
<dd>The full qualified path where to find the J2EE instance bootstrap directory. e.g. /usr/sap/P01/J00/j2ee/cluster/bootstrap (optional, string, no default)</dl>
<p> <code>DIR_SECSTORE</code></p>
<dl>
<dd>The full qualified path where to find the J2EE security store directory. e.g. /usr/sap/P01/SYS/global/security/lib/tools (optional, string, no default)</dl>
<p> <code>DB_JARS</code></p>
<dl>
<dd>The full qualified filename of the jdbc driver for the database connection test. It will be automaticaly read from the bootstrap.properties file in Java engine 6.40 and 7.00. For Java engine 7.10 the parameter is mandatory. (optional, string, no default)</dl>
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
<dd>Starts the resource. Suggested minimum timeout: 1800.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 1800.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 120.</dl>
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
<p>The following is an example configuration for a SAPDatabase resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_SAPDatabase ocf:heartbeat:SAPDatabase \
params \
SID=string \
DBTYPE=string \
op monitor depth=&quot;0&quot; timeout=&quot;60&quot; interval=&quot;120&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/SAPDatabase_(resource_agent)">http://www.linux-ha.org/wiki/SAPDatabase_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
