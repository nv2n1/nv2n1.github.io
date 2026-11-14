---
title: "ocf_heartbeat_apache(7)"
name: "ocf_heartbeat_apache"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_apache/"
description: "ocf_heartbeat_apache – Manages an Apache Web server instance"
---

<p>ocf_heartbeat_apache &#8211; Manages an Apache Web server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>apache</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is the resource agent for the Apache Web server. This resource agent operates both version 1.x and version 2.x Apache servers. </p>
<p> The start operation ends with a loop in which monitor is repeatedly called to make sure that the server started and that it is operational. Hence, if the monitor operation does not succeed within the start operation timeout, the apache resource will end with an error status. </p>
<p> The monitor operation by default loads the server status page which depends on the mod_status module and the corresponding configuration file (usually /etc/apache2/mod_status.conf). Make sure that the server status page works and that the access is allowed *only* from localhost (address 127.0.0.1). See the statusurl and testregex attributes for more details. </p>
<p> See also <a rel="nofollow" href="http://httpd.apache.org/">http://httpd.apache.org/</a></p>
<h2>Supported Parameters</h2>
<p><code>configfile</code></p>
<dl>
<dd>The full pathname of the Apache configuration file. This file is parsed to provide defaults for various other resource agent parameters. </p>
<p> (unique, optional, string, default &quot;/etc/httpd/conf/httpd.conf&quot;)</dl>
<p> <code>httpd</code></p>
<dl>
<dd>The full pathname of the httpd binary (optional). </p>
<p> (optional, string, default &quot;/usr/sbin/httpd&quot;)</dl>
<p> <code>port</code></p>
<dl>
<dd>A port number that we can probe for status information using the statusurl. This will default to the port number found in the configuration file, or 80, if none can be found in the configuration file. </p>
<p> (optional, integer, no default)</dl>
<p> <code>statusurl</code></p>
<dl>
<dd>The URL to monitor (the apache server status page by default). If left unspecified, it will be inferred from the apache configuration file. </p>
<p> If you set this, make sure that it succeeds *only* from the localhost (127.0.0.1). Otherwise, it may happen that the cluster complains about the resource being active on multiple nodes. </p>
<p> (optional, string, no default)</dl>
<p> <code>testregex</code></p>
<dl>
<dd>Regular expression to match in the output of statusurl. Case insensitive. </p>
<p> (optional, string, default &quot;exists, but impossible to show in a human readable format (try grep testregex)&quot;)</dl>
<p> <code>client</code></p>
<dl>
<dd>Client to use to query to Apache. If not specified, the RA will try to find one on the system. Currently, wget and curl are supported. For example, you can set this parameter to &quot;curl&quot; if you prefer that to wget. </p>
<p> (optional, string, no default)</dl>
<p> <code>testurl</code></p>
<dl>
<dd>URL to test. If it does not start with &quot;http&quot;, then it&#8217;s considered to be relative to the Listen address. </p>
<p> (optional, string, no default)</dl>
<p> <code>testregex10</code></p>
<dl>
<dd>Regular expression to match in the output of testurl. Case insensitive. </p>
<p> (optional, string, no default)</dl>
<p> <code>testconffile</code></p>
<dl>
<dd>A file which contains test configuration. Could be useful if you have to check more than one web application or in case sensitive info should be passed as arguments (passwords). Furthermore, using a config file is the only way to specify certain parameters. </p>
<p> Please see README.webapps for examples and file description. </p>
<p> (optional, string, no default)</dl>
<p> <code>testname</code></p>
<dl>
<dd>Name of the test within the test configuration file. </p>
<p> (optional, string, no default)</dl>
<p> <code>options</code></p>
<dl>
<dd>Extra options to apply when starting apache. See man <a href="/docs/linux/man/8-httpd/">httpd</a>(8). </p>
<p> (optional, string, no default)</dl>
<p> <code>envfiles</code></p>
<dl>
<dd>Files (one or more) which contain extra environment variables. If you want to prevent script from reading the default file, set this parameter to empty string. </p>
<p> (optional, string, default &quot;/etc/apache2/envvars&quot;)</dl>
<p> <code>use_ipv6</code></p>
<dl>
<dd>We will try to detect if the URL (for monitor) is IPv6, but if that doesn&#8217;t work set this to true to enforce IPv6. </p>
<p> (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 40s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a apache resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_apache ocf:heartbeat:apache \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a apache resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_apache ocf:heartbeat:apache \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/apache_(resource_agent)">http://www.linux-ha.org/wiki/apache_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
