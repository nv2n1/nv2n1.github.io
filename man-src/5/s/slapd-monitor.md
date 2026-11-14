---
title: "slapd-monitor(5)"
name: "slapd-monitor"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-monitor/"
description: "slapd-monitor – Monitor backend to slapd"
---

<p>slapd-monitor &#8211; Monitor backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>monitor </code> backend to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) is not an actual database; if enabled, it is automatically generated and dynamically maintained by <code>slapd </code> with information about the running status of the daemon. </p>
<p> To inspect all monitor information, issue a subtree search with base cn=Monitor, requesting that attributes &quot;+&quot; and &quot;*&quot; are returned. The monitor backend produces mostly operational attributes, and LDAP only returns operational attributes that are explicitly requested. Requesting attribute &quot;+&quot; is an extension which requests all operational attributes.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the <code>monitor </code> backend database. That is, they must follow a &quot;database monitor&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. </p>
<p> As opposed to most databases, the <code>monitor </code> database can be instantiated only once, i.e. only one occurrence of &quot;database monitor&quot; can occur in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file. Moreover, the suffix of the database cannot be explicitly set by means of the <code>suffix</code> directive. The suffix is automatically set to &quot;<i>cn=Monitor</i>&quot;. </p>
<p> The <code>monitor</code> database honors the <code>rootdn</code> and the <code>rootpw</code> directives, and the usual ACL directives, e.g. the <code>access</code> directive. </p>
<p> Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page.</p>
<h2>Usage</h2>
<p>The usage is:</p>
<dl>
<dt>1) enable the <code>monitor</code> backend at configure:</p>
<dd></dl>
<dl>
<dd>
<pre>configure --enable-monitor</pre>
</dl>
<dl>
<dt>2) activate the <code>monitor</code> database in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) file:</p>
<dd></dl>
<dl>
<dd>
<pre>database monitor</pre>
</dl>
<dl>
<dt>3) add ACLs as detailed in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5) to control access to the database, e.g.:</p>
<dd></dl>
<dl>
<dd>
<pre>access to dn.subtree=&quot;cn=Monitor&quot;
 by dn.exact=&quot;uid=Admin,dc=my,dc=org&quot; write
 by users read
 by * none</pre>
</dl>
<dl>
<dt>4) ensure that the <code>core.schema</code> file is loaded.</p>
<dd>The <code>monitor </code> backend relies on some standard track attributeTypes that must be already defined when the backend is started.</dl>
<h2>Access Control</h2>
<p>The <code>monitor</code> backend honors access control semantics as indicated in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5), including the <code>disclose</code> access privilege, on all currently implemented operations.</p>
<h2>Known Limitations</h2>
<p>The <code>monitor </code> backend does not honor size/time limits in search operations.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/openldap/slapd.conf</code></p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8), <code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3).</p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
