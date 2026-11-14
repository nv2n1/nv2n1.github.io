---
title: "ocf_heartbeat_ids(7)"
name: "ocf_heartbeat_ids"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_ids/"
description: "ocf_heartbeat_ids – Manages an Informix Dynamic Server (IDS) instance"
---

<p>ocf_heartbeat_ids &#8211; Manages an Informix Dynamic Server (IDS) instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ids</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>OCF resource agent to manage an IBM Informix Dynamic Server (IDS) instance as an High-Availability resource.</p>
<h2>Supported Parameters</h2>
<p><code>informixdir</code></p>
<dl>
<dd>The value the environment variable INFORMIXDIR has after a typical installation of IDS. Or in other words: the path (without trailing &#8216;/&#8217;) where IDS was installed to. If this parameter is unspecified the script will try to get the value from the shell environment. (optional, string, no default)</dl>
<p> <code>informixserver</code></p>
<dl>
<dd>The value the environment variable INFORMIXSERVER has after a typical installation of IDS. Or in other words: the name of the IDS server instance to manage. If this parameter is unspecified the script will try to get the value from the shell environment. (optional, string, no default)</dl>
<p> <code>onconfig</code></p>
<dl>
<dd>The value the environment variable ONCONFIG has after a typical installation of IDS. Or in other words: the name of the configuration file for the IDS instance specified in INFORMIXSERVER. The specified configuration file will be searched at &#8216;/etc/&#8217;. If this parameter is unspecified the script will try to get the value from the shell environment. (optional, string, no default)</dl>
<p> <code>dbname</code></p>
<dl>
<dd>This parameter defines which database to use in order to monitor the IDS instance. If this parameter is unspecified the script will use the &#8216;sysmaster&#8217; database as a default. (optional, string, default sysmaster)</dl>
<p> <code>sqltestquery</code></p>
<dl>
<dd>SQL test query to run on the database specified by the parameter &#8216;dbname&#8217; in order to monitor the IDS instance and determine if it&#8217;s functional or not. If this parameter is unspecified the script will use &#8216;SELECT COUNT(*) FROM systables;&#8217; as a default. (optional, string, default SELECT COUNT(*) FROM systables;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 120.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<p> <code>usage</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a ids resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_ids ocf:heartbeat:ids \

op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/ids_(resource_agent)">http://www.linux-ha.org/wiki/ids_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
