---
title: "pva-addvo(1)"
name: "pva-addvo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pva-addvo/"
description: "pva-addvo – PHP VOMS-Admin(PVA) tool to add a new VO"
---

<h2 class="name">NAME</h2>
<p> pva-addvo &#8211; PHP VOMS-Admin(PVA) tool to add a new VO</p>
<h2>DESCRIPTION</h2>
<p> The <code>pva-addvo</code> command can be used to add new VO for serving by PHP VOMS-Admin. It also generates configuration files for voms-server for use in conjunction with PVA. </p>
<h2>SYNOPSIS</h2>
<p> <code>pva-addvo [vo config]</code> </p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>vo config</code></p>
<dd> VO provisioning configuration file</dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>pva-addvo</code> command creates configuration files for PVA and voms-server. New VO parameters can be provided via environment variables. Any subset of configuration variables can be specified in <code>vo config</code> file. </p>
<p> When &quot;Request VOMS resources for new VO&quot; form via PVA web-interface is filled and submitted by VO admin, PVA will automatically send an e-mail to server administrator formatted as configuration file to use with <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1). VOPORT is not included in mail body and must be set manually </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pva/addvo.conf</code></p>
<dd> Host-specific configuration file for <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1). You MUST review its contents and set your host parameters before adding the first VO. Settings include host name, voms-server certificate paths, MySQL access options and voms-server accout. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>VONAME</code></p>
<dd> The name for a new VO to add. According to EGI documentation, using FQDN is preferred way (required).</p>
<dt><code>ADMDN</code></p>
<dd> Initial VO administrator&#8217;s certificate distinguished name (required).</p>
<dt><code>ADMCA</code></p>
<dd> DN of a certification authority, which signed initial VO administrator&#8217;s certificate (required).</p>
<dt><code>ADMMAIL</code></p>
<dd> E-mail address of initital VO administrator (required).</p>
<dt><code>RULES_URL</code></p>
<dd> URL that points to VO usage rules. Every new user must agree and accept this rules to proceed (required).</p>
<dt><code>VOPORT</code></p>
<dd> voms-server listen port to issue VOMS ACs (required).</p>
<dt><code>HOMEPAGE</code></p>
<dd> URL to VO homepage (optional).</p>
<dt><code>DESCR</code></p>
<dd> Short human readable description of the VO (optional).</p>
<dt><code>DEFCA</code></p>
<dd> Default value for DN of certification authority, used when manually adding new users (optional). </p>
</dl>
<h2>EXAMPLE</h2>
<p> VOPORT=15110 pva-addvo /path/to/new_VO_request_file </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> Andrii Salnikov &lt;manf [at] grid.org.ua&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-addvo-conf/">addvo.conf</a></code>(5), <code><a href="/docs/linux/man/5-pva-config/">pva-config</a></code>(5), <code><a href="/docs/linux/man/8-voms/">voms</a></code>(8) </p>
<h2>Index</h2>
