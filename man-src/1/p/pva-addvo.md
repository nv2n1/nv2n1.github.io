---

title: "pva-addvo(1)"
name: "pva-addvo"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pva-addvo/"
description: "pva-addvo – PHP VOMS-Admin(PVA) tool to add a new VO"
---

<p> The <code>pva-addvo</code> command can be used to add new VO for serving by PHP VOMS-Admin. It also generates configuration files for voms-server for use in conjunction with PVA. </p>
<p> <code>pva-addvo [vo config]</code> </p>
<h2>ARGUMENTS</h2>
<dl>
<dt><code>vo config</code></dt>
<dd> VO provisioning configuration file</dd></dl>
<h2>EXTENDED DESCRIPTION</h2>
<p> The <code>pva-addvo</code> command creates configuration files for PVA and voms-server. New VO parameters can be provided via environment variables. Any subset of configuration variables can be specified in <code>vo config</code> file. </p>
<p> When &quot;Request VOMS resources for new VO&quot; form via PVA web-interface is filled and submitted by VO admin, PVA will automatically send an e-mail to server administrator formatted as configuration file to use with <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1). VOPORT is not included in mail body and must be set manually </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/pva/addvo.conf</code></dt>
<dd> Host-specific configuration file for <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1). You MUST review its contents and set your host parameters before adding the first VO. Settings include host name, voms-server certificate paths, MySQL access options and voms-server accout. </dd>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>VONAME</code></dt>
<dd> The name for a new VO to add. According to EGI documentation, using FQDN is preferred way (required).</dd>
<dt><code>ADMDN</code></dt>
<dd> Initial VO administrator&#8217;s certificate distinguished name (required).</dd>
<dt><code>ADMCA</code></dt>
<dd> DN of a certification authority, which signed initial VO administrator&#8217;s certificate (required).</dd>
<dt><code>ADMMAIL</code></dt>
<dd> E-mail address of initital VO administrator (required).</dd>
<dt><code>RULES_URL</code></dt>
<dd> URL that points to VO usage rules. Every new user must agree and accept this rules to proceed (required).</dd>
<dt><code>VOPORT</code></dt>
<dd> voms-server listen port to issue VOMS ACs (required).</dd>
<dt><code>HOMEPAGE</code></dt>
<dd> URL to VO homepage (optional).</dd>
<dt><code>DESCR</code></dt>
<dd> Short human readable description of the VO (optional).</dd>
<dt><code>DEFCA</code></dt>
<dd> Default value for DN of certification authority, used when manually adding new users (optional). </dd>
</dl>
<h2>EXAMPLE</h2>
<p> VOPORT=15110 pva-addvo /path/to/new_VO_request_file </p>
<h2>COPYRIGHT</h2>
<p> APACHE LICENSE Version 2.0 </p>
<h2>AUTHOR</h2>
<p> Andrii Salnikov &lt;manf [at] grid.org.ua&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-addvo-conf/">addvo.conf</a></code>(5), <code><a href="/docs/linux/man/5-pva-config/">pva-config</a></code>(5), <code><a href="/docs/linux/man/8-voms/">voms</a></code>(8) </p>
