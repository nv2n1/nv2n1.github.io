---
title: "slapo-constraint(5)"
name: "slapo-constraint"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-constraint/"
description: "slapo-constraint – Attribute Constraint Overlay to slapd"
---

<p>slapo-constraint &#8211; Attribute Constraint Overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The constraint overlay is used to ensure that attribute values match some constraints beyond basic LDAP syntax. Attributes can have multiple constraints placed upon them, and all must be satisfied when modifying an attribute value under constraint. </p>
<p> This overlay is intended to be used to force syntactic regularity upon certain string represented data which have well known canonical forms, like telephone numbers, post codes, FQDNs, etc. </p>
<p> It constrains only LDAP <i>add</i>, <i>modify</i> and <i>rename</i> commands and only seeks to control the <i>add</i> and <i>replace</i> values of <i>modify</i> and <i>rename</i> requests. </p>
<p> No constraints are applied for operations performed with the <i>relax</i> control set.</p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the constraint overlay. It should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>constraint_attribute &lt;attribute_name&gt;[,&#8230;] &lt;type&gt; &lt;value&gt; [&lt;extra&gt; [&#8230;]]</code></p>
<dd>Specifies the constraint which should apply to the comma-separated attribute list named as the first parameter. Five types of constraint are currently supported &#8211; <code>regex</code>, <code>size</code>, <code>count</code>, <code>uri</code>, and <code>set</code>. </p>
<p> The parameter following the <code>regex</code> type is a Unix style regular expression (See <code><a href="/docs/linux/man/7-regex/">regex</a></code>(7) ). The parameter following the <code>uri</code> type is an LDAP URI. The URI will be evaluated using an internal search. It must not include a hostname, and it must include a list of attributes to evaluate. </p>
<p> The parameter following the <code>set</code> type is a string that is interpreted according to the syntax in use for ACL sets. This allows to construct constraints based on the contents of the entry. </p>
<p> The <code>size</code> type can be used to enforce a limit on an attribute length, and the <code>count</code> type limits the number of values of an attribute. </p>
<p> Extra parameters can occur in any order after those described above.</p>
<dl>
<dd>
<dl>
<dt><code>&lt;extra&gt; : restrict=&lt;uri&gt;</code></p>
<dd></dl>
</dl>
<dl>
<dd>This extra parameter allows to restrict the application of the corresponding constraint only to entries that match the <i>base</i>, <i>scope</i> and <i>filter</i> portions of the LDAP URI. The <i>base</i>, if present, must be within the naming context of the database. The <i>scope</i> is only used when the <i>base</i> is present; it defaults to <code>base</code>. The other parameters of the URI are not allowed.</dl>
</dl>
<p> Any attempt to add or modify an attribute named as part of the constraint overlay specification which does not fit the constraint listed will fail with a LDAP_CONSTRAINT_VIOLATION error.</p>
<h2>Examples</h2>
<pre><code>overlay constraint
constraint_attribute jpegPhoto size 131072
constraint_attribute userPassword count 3
constraint_attribute mail regex ^[[:alnum:]]+@mydomain.com$
constraint_attribute title uri
ldap:///dc=catalog,dc=example,dc=com?title?sub?(objectClass=titleCatalog)
constraint_attribute cn,sn,givenName set
&quot;(this/givenName + [ ] + this/sn) &amp; this/cn&quot;
restrict=&quot;ldap:///ou=People,dc=example,dc=com??sub?(objectClass=inetOrgPerson)&quot;</code></pre>
</dl>
<p> A specification like the above would reject any <code>mail</code> attribute which did not look like <code>&lt;alpha-numeric string&gt;@mydomain.com</code>. It would also reject any <code>title</code> attribute whose values were not listed in the <code>title</code> attribute of any <code>titleCatalog</code> entries in the given scope. (Note that the &quot;dc=catalog,dc=example,dc=com&quot; subtree ought to reside in a separate database, otherwise the initial set of titleCatalog entries could not be populated while the constraint is in effect.) Finally, it requires the values of the attribute <code>cn</code> to be constructed by pairing values of the attributes <code>sn</code> and <code>givenName</code>, separated by a space, but only for entries derived from the objectClass <code>inetOrgPerson</code>.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5),</p>
<h2>Acknowledgements</h2>
<p>This module was written in 2005 by Neil Dunbar of Hewlett-Packard and subsequently extended by Howard Chu and Emmanuel Dreyfus. <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
