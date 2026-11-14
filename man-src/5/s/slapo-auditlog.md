---
title: "slapo-auditlog(5)"
name: "slapo-auditlog"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-auditlog/"
description: "slapo-auditlog – Audit Logging overlay to slapd"
---

<p>slapo-auditlog &#8211; Audit Logging overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<dl>
<dt>/etc/openldap/slapd.d</p>
<dd></dl>
<h2>Description</h2>
<p>The Audit Logging overlay can be used to record all changes on a given backend database to a specified log file. Changes are logged as standard LDIF, with an additional comment header giving the timestamp of the change and the identity of the user making the change. </p>
<p> For Add and Modify operations the identity comes from the modifiersName associated with the operation. This is usually the same as the requestor&#8217;s identity, but may be set by other overlays to reflect other values.</p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the Audit Logging overlay. It should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>auditlog &lt;filename&gt;</code></p>
<dd>Specify the fully qualified path for the log file.</p>
<dt><code>olcAuditlogFile &lt;filename&gt;</code></p>
<dd>For use with <code>cn=config</code></dl>
<h2>Example</h2>
<p>The following LDIF could be used to add this overlay to <code>cn=config </code> (adjust to suit)</p>
<dl>
<dd>
<pre>dn: olcOverlay=auditlog,olcDatabase={1}hdb,cn=config 
changetype: add
objectClass: olcOverlayConfig
objectClass: olcAuditLogConfig
olcOverlay: auditlog
olcAuditlogFile: /tmp/auditlog.ldif</pre>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/openldap/slapd.d</p>
<dd>default slapd configuration directory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a>(5).</code> </p>
