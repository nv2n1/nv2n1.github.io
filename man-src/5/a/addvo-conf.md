---
title: "addvo-conf(5)"
name: "addvo-conf"
section: "5"
letter: "a"
url: "/docs/linux/man/5-addvo-conf/"
description: "addvo.conf – pva-addvo host-specific configuration"
---

<p>addvo.conf &#8211; pva-addvo host-specific configuration</p>
<h2>Description</h2>
<p>Configauration file for <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1) command used to add new VO for serving by PHP VOMS-Admin. </p>
<h2>Synopsis</h2>
<p><code>/etc/pva/addvo.conf</code> </p>
<h2>Extended Description</h2>
<p>Configuration file set host-specific parameters for <code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1) script operation. Out of box installation from pacakge set most of variables accordinly to default settings that will works without modifications.</p>
<dl>
<dt>The configuration file has the following format:</p>
<dd>
<dt>Lines starting with # are comments. Otherwise a line is of the format</p>
<dd><code>keyword=argument</code></p>
<dt>Several configuration variables might be reviewed:</p>
<dd>
<dt><code>LIBDIR</code></p>
<dd>specify where to find voms-server shared libraries </p>
<p> <i>Example:</i> LIBDIR=&quot;/usr/lib64&quot;</p>
<dt><code>CONFDIR</code></p>
<dd>specify where to find configuration files </p>
<p> <i>Example: </i> CONFDIR=&quot;/etc&quot;</p>
<dt><code>PVACONFDIR</code></p>
<dd>path to PHP VOMS-Admin virtual organizations configuration files </p>
<p> <i>Example: </i> CONFDIR=&quot;${CONFDIR}/pva/vomses&quot;</p>
<dt><code>PVACONF_OWNER</code></p>
<dd>PHP VOMS-Admin virtual organizations configuration files owner </p>
<p> <i>Example:</i> PVACONF_OWNER=&quot;apache:apache&quot;</p>
<dt><code>MYSQL_USER</code></p>
<dd>MySQL user used for PHP VOMS-Admin VO databases creation </p>
<p> <i>Example:</i> MYSQL_USER=&quot;root&quot;</p>
<dt><code>VODBUSER</code></p>
<dd>VO database access username; &quot;voms_VONAME&quot; value will be used if not specified; useful to use common user name for all server VOs </p>
<p> <i>Example:</i> VODBUSER=&quot;voms&quot;</p>
<dt><code>VODBPASS</code></p>
<dd>VO database access password; dynamically generated password will be used if not specified </p>
<p> <i>Example:</i> VODBPASS=&quot;commonpassword&quot;</p>
<dt><code>VODBHOST</code></p>
<dd>VO database host running MySQL service; &quot;localhost&quot; value will be used if not specified </p>
<p> <i>Example:</i> VODBHOST=&quot;db.example.com&quot;</p>
<dt><code>VOHOST</code></p>
<dd>hostname of the server running credentials signing daemon (voms-server); <code><a href="/docs/linux/man/1-hostname/">hostname</a></code>(1)<code>value</code>will<code>be</code>used<code>if</code>not<code>specified</code> </p>
<p> <i>Example:</i> VOHOST=&quot;myvomds.host.org&quot;</p>
<dt><code>VOMSDDIR</code></p>
<dd>voms-server configuration files location </p>
<p> <i>Example:</i> VOMSDDIR=&quot;${CONFDIR}/voms&quot;</p>
<dt><code>VOMSDCERT</code></p>
<dd>voms-server certificate file path (on the server where vomsd is running) </p>
<p> <i>Example:</i> VOMSDCERT=&quot;${CONFDIR}/grid-security/hostcert.pem&quot;</p>
<dt><code>VOMSDKEY</code></p>
<dd>voms-server key file path (on the server where vomsd is running) </p>
<p> <i>Example:</i> VOMSDKEY=&quot;${CONFDIR}/grid-security/hostkey.pem&quot;</p>
<dt><code>VOMSDCONF_OWNER</code></p>
<dd>voms-server configuration files owner </p>
<p> <i>Example:</i> VOMSDCONF_OWNER=&quot;voms:voms&quot; </p>
</dl>
<h2>Author</h2>
<p>Andrii Salnikov &lt;manf [at] grid.org.ua&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-pva-addvo/">pva-addvo</a></code>(1), <code><a href="/docs/linux/man/5-pva-config/">pva-config</a></code>(5), <code><a href="/docs/linux/man/8-voms/">voms</a></code>(8) </p>
