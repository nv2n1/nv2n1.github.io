---
title: "ocf_heartbeat_nginx(7)"
name: "ocf_heartbeat_nginx"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_nginx/"
description: "ocf_heartbeat_nginx – Manages an Nginx web/proxy server instance"
---

<p>ocf_heartbeat_nginx &#8211; Manages an Nginx web/proxy server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nginx</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is the resource agent for the Nginx web/proxy server. This resource agent does not monitor POP or IMAP servers, as we don&#8217;t know how to determine meaningful status for them. The start operation ends with a loop in which monitor is repeatedly called to make sure that the server started and that it is operational. Hence, if the monitor operation does not succeed within the start operation timeout, the nginx resource will end with an error status. The default monitor operation will verify that nginx is running. The level 10 monitor operation by default will try and fetch the /nginx_status page &#8211; which is commented out in sample nginx configurations. Make sure that the /nginx_status page works and that the access is restricted to localhost (address 127.0.0.1) plus whatever places _outside the cluster_ you want to monitor the server from. See the status10url and status10regex attributes for more details. The level 20 monitor operation will perform a more complex set of tests from a configuration file. The level 30 monitor operation will run an external command to perform an arbitrary monitoring operation. </p>
<h2>Supported Parameters</h2>
<p><code>configfile</code></p>
<dl>
<dd>The full pathname of the Nginx configuration file. This file is parsed to provide defaults for various other resource agent parameters. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>httpd</code></p>
<dl>
<dd>The full pathname of the httpd binary (optional). </p>
<p> (optional, string, default &quot;/usr/sbin/httpd&quot;)</dl>
<p> <code>port</code></p>
<dl>
<dd>A port number that we can probe for status information using the statusurl. This will default to the port number found in the configuration file, or 80, if none can be found in the configuration file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>status10url</code></p>
<dl>
<dd>The URL to monitor (the nginx server status page by default) when given a level 10 monitor operation. If left unspecified, it will be inferred from the nginx configuration file, or defaulted to /nginx_status. </p>
<p> If you set this, make sure that it succeeds *only* from the localhost (127.0.0.1) and no other cluster nodes. Otherwise, the cluster software may complain about it being active on multiple nodes. </p>
<p> (optional, string, no default)</dl>
<p> <code>status10regex</code></p>
<dl>
<dd>Regular expression to match in the output of status10url. Case insensitive. </p>
<p> (optional, string, default &quot;Reading: [0-9]+ Writing: [0-9]+ Waiting: [0-9]+&quot;)</dl>
<p> <code>testclient</code></p>
<dl>
<dd>Client to use to query to Nginx for level 10 and level 20 tests. If not specified, the RA will try to find one on the system. Currently, wget and curl are supported, with curl being preferred. For example, you can set this paramter to &quot;wget&quot; if you prefer that to curl. </p>
<p> (optional, string, no default)</dl>
<p> <code>test20url</code></p>
<dl>
<dd>URL to test. If it does not start with &quot;http&quot;, then it&#8217;s considered to be relative to the document root address. </p>
<p> (optional, string, no default)</dl>
<p> <code>test20regex</code></p>
<dl>
<dd>Regular expression to match in the output of test20url. Case insensitive. </p>
<p> (optional, string, no default)</dl>
<p> <code>test20conffile</code></p>
<dl>
<dd>A file which contains a more complex test configuration. Could be useful if you have to check more than one web application or in case sensitive info should be passed as arguments (passwords). Furthermore, using a config file is the only way to specify certain parameters. </p>
<p> Please see README.webapps for examples and file description. </p>
<p> (optional, string, no default)</dl>
<p> <code>test20name</code></p>
<dl>
<dd>Name of the test within the test configuration file. </p>
<p> (optional, string, no default)</dl>
<p> <code>external_monitor30_cmd</code></p>
<dl>
<dd>Command string to run which implements level 30 monitoring. </p>
<p> (optional, string, no default)</dl>
<p> <code>options</code></p>
<dl>
<dd>Extra options to apply when starting nginx. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 40s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30s. Suggested interval: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a nginx resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_nginx ocf:heartbeat:nginx \
 op monitor timeout=&quot;30s&quot; depth=&quot;0&quot; interval=&quot;20s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a nginx resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_nginx ocf:heartbeat:nginx \
 op monitor timeout=&quot;30s&quot; depth=&quot;0&quot; interval=&quot;20s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/nginx_(resource_agent)">http://www.linux-ha.org/wiki/nginx_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
