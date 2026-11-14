---
title: "slapo-translucent(5)"
name: "slapo-translucent"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-translucent/"
description: "slapo-translucent – Translucent Proxy overlay to slapd"
---

<p>slapo-translucent &#8211; Translucent Proxy overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Translucent Proxy overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to create a &quot;translucent proxy&quot;. Entries retrieved from a remote LDAP server may have some or all attributes overridden, or new attributes added, by entries in the local database before being presented to the client. </p>
<p> A <code>search</code> operation is first populated with entries from the remote LDAP server, the attributes of which are then overridden with any attributes defined in the local database. Local overrides may be populated with the <code>add</code>, <code>modify ,</code> and <code>modrdn</code> operations, the use of which is restricted to the root user. </p>
<p> A <code>compare</code> operation will perform a comparison with attributes defined in the local database record (if any) before any comparison is made with data in the remote database.</p>
<h2>Configuration</h2>
<p>The Translucent Proxy overlay uses a proxied database, typically a (set of) remote LDAP server(s), which is configured with the options shown in <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5), <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5) or similar. These <code>slapd.conf</code> options are specific to the Translucent Proxy overlay; they must appear after the <code>overlay</code> directive that instantiates the <code>translucent</code> overlay.</p>
<dl>
<dt><code>translucent_strict</code></p>
<dd>By default, attempts to delete attributes in either the local or remote databases will be silently ignored. The <code>translucent_strict</code> directive causes these modifications to fail with a Constraint Violation.</p>
<dt><code>translucent_no_glue</code></p>
<dd>This configuration option disables the automatic creation of &quot;glue&quot; records for an <code>add</code> or <code>modrdn</code> operation, such that all parents of an entry added to the local database must be created by hand. Glue records are always created for a <code>modify</code> operation.</p>
<dt><code>translucent_local &lt;attr[,attr&#8230;]&gt;</code></p>
<dd>Specify a list of attributes that should be searched for in the local database when used in a search filter. By default, search filters are only handled by the remote database. With this directive, search filters will be split into a local and remote portion, and local attributes will be searched locally.</p>
<dt><code>translucent_remote &lt;attr[,attr&#8230;]&gt;</code></p>
<dd>Specify a list of attributes that should be searched for in the remote database when used in a search filter. This directive complements the <code>translucent_local</code> directive. Attributes may be specified as both local and remote if desired.</dl>
<p> If neither <code>translucent_local</code> nor <code>translucent_remote</code> are specified, the default behavior is to search the remote database with the complete search filter. If only <code>translucent_local</code> is specified, searches will only be run on the local database. Likewise, if only <code>translucent_remote</code> is specified, searches will only be run on the remote database. In any case, both the local and remote entries corresponding to a search result will be merged before being returned to the client. </p>
<dl>
<dt><code>translucent_bind_local </code></p>
<dd>Enable looking for locally stored credentials for simple bind when binding to the remote database fails. Disabled by default. </p>
<dt><code>translucent_pwmod_local</code></p>
<dd>Enable RFC 3062 Password Modification extended operation on locally stored credentials. The operation only applies to entries that exist in the remote database. Disabled by default. </p>
</dl>
<h2>Access Control</h2>
<p>Access control is delegated to either the remote DSA(s) or to the local database backend for <code>auth</code> and <code>write</code> operations. It is delegated to the remote DSA(s) and to the frontend for <code>read</code> operations. Local access rules involving data returned by the remote DSA(s) should be designed with care. In fact, entries are returned by the remote DSA(s) only based on the remote fraction of the data, based on the identity the operation is performed as. As a consequence, local rules might only be allowed to see a portion of the remote data.</p>
<h2>Caveats</h2>
<p>The Translucent Proxy overlay will disable schema checking in the local database, so that an entry consisting of overlay attributes need not adhere to the complete schema. </p>
<p> Because the translucent overlay does not perform any DN rewrites, the local and remote database instances must have the same suffix. Other configurations will probably fail with No Such Object and other errors.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5). </p>
