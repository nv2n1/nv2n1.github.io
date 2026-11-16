---
title: "ipsilon-conf(5)"
name: "ipsilon-conf"
section: "5"
letter: "i"
url: "/docs/linux/man/5-ipsilon-conf/"
description: "ipsilon.conf – Ipsilon IdP configuration file"
---

<p>ipsilon.conf &#8211; Ipsilon IdP configuration file</p>
<h2>Synopsis</h2>
<p>/etc/ipsilon/&lt;instancename&gt;/ipsilon.conf</p>
<h2>Description</h2>
<p><i>ipsilon.conf</i> is used to set instance-specific configuration options for an Ipsilon instance. It should be stored in a subdirectory representing the instance under the the system configuration directory, normally /etc/ipsilon. For example <i>/etc/ipsilon/idp/ispilon.conf</i>. </p>
<h2>Syntax</h2>
<p>The configuration options are not case sensitive. The values may be case sensitive, depending on the option. </p>
<p> Blank lines are ignored. Lines beginning with # are comments and are ignored. </p>
<p> Valid lines consist of an option name, an equals sign and a value. Spaces surrounding equals sign are ignored. An option terminates at the end of a line. </p>
<p> Non-string values should not be quoted, the quotes will not be stripped. </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Wrong &#8211; don&#8217;t include quotes with boolean options<br />
&nbsp;<wbr>verbose&nbsp;<wbr>=&nbsp;<wbr>&quot;True&quot; </p>
<p>&nbsp;<wbr>#&nbsp;<wbr>Right &#8211; Properly formatted options<br />
&nbsp;<wbr>verbose&nbsp;<wbr>=&nbsp;<wbr>True<br />
&nbsp;<wbr>verbose=True </p>
<p> Options must appear in the section named [global]. There are no other sections defined or used currently.</p>
<h2>Options</h2>
<p>The following options are defined:</p>
<dl>
<dt><code>debug</code></dt>
<dd>Enables additional debugging output. log.screen must also be True for this to be written.</dd>
<dt><code>tools.log_request_response.on</code></dt>
<dd>Logs the full SAML 2 request and response information.</dd>
<dt><code>db.conn.log</code></dt>
<dd>Enable verbose database connection tracing logs. debug and log.screen both need to be True for this to be written.</dd>
<dt><code>template_dir</code></dt>
<dd>Location of the template directory used for buidling the UI. This can be relative to <i>base.dir</i>.</dd>
<dt><code>log.screen</code></dt>
<dd>Send logs to the console, which Apache grabs and adds to its own error log.</dd>
<dt><code>base.mount</code></dt>
<dd>The base mount mount for UI pages. This should match the name of the IdP.</dd>
<dt><code>base.dir</code></dt>
<dd>The Ipsilon UI base directory, e.g. <i>/usr/share/ipsilon</i>.</dd>
<dt><code>admin.config.db</code></dt>
<dd>Database URL for storing Ipsilon administrative settings.</dd>
<dt><code>user.prefs.db</code></dt>
<dd>Database URL for storing persistent user information. This is where users are marked as administrators by setting is_admin to 1.</dd>
<dt><code>transactions.db</code></dt>
<dd>Database URL for storing login transactions.</dd>
<dt><code>tools.sessions.on</code></dt>
<dd>Enable sessions in CherryPy. This should always be True.</dd>
<dt><code>tools.sessions.name</code></dt>
<dd>The session name to be used in session cookies.</dd>
<dt><code>tools.sessions.storage_type</code></dt>
<dd>Type of storage for the sessions. See CherryPy documentation for more details. Ipsilon defaults to using file. Ipsilon adds a session storage type &quot;Sql&quot; for storing the sesions in an SQL database for load-balanced servers.</dd>
<dt><code>tools.sessions.storage_path</code></dt>
<dd>The directory where the CherryPy sessions are stored.</dd>
<dt><code>tools.sessions.storage_dburi</code></dt>
<dd>The database URL used for session storage if storage_type is set to &quot;Sql&quot;.</dd>
<dt><code>tools.sessions.path</code></dt>
<dd>The URI for where the session is valid, this should conform to the instance name, e.g. /idp.</dd>
<dt><code>tools.sessions.timeout</code></dt>
<dd>The time in minutes the session is valid for. Default is 60.</dd>
<dt><code>tools.sessions.httponly</code></dt>
<dd>If False (the default) the cookie <i>httponly</i> value will not be set. If True, the cookie <i>httponly</i> value will be set (to 1). Of this is set to True, browsers are instructed to only send cookies with http requests, resulting in them not being available for Javascript-based requests.</dd>
<dt><code>tools.sessions.secure</code></dt>
<dd>If False the cookie <i>secure</i> value will not be set. If True (the default), the cookie <i>secure</i> value will be set (to 1). If this is set to True, browsers are instructed to only send cookies to secure (TLS-protected) URLs.</dd></dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ipsilon-server-install/">ipsilon-server-install</a>(1)</code> </p>
