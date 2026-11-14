---
title: "slapo-dynlist(5)"
name: "slapo-dynlist"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-dynlist/"
description: "slapo-dynlist – Dynamic List overlay to slapd"
---

<p>slapo-dynlist &#8211; Dynamic List overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The <code>dynlist</code> overlay to <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) allows expansion of dynamic groups and more. Any time an entry with a specific objectClass (defined in the overlay configuration) is being returned, the LDAP URI-valued occurrences of a specific attribute (also defined in the overlay configuration) are expanded into the corresponding entries, and the values of the attributes listed in the URI are added to the original entry. No recursion is allowed, to avoid potential infinite loops. Since the resulting entry is dynamically constructed, it does not exist until it is constructed while being returned. As a consequence, dynamically added attributes do not participate in the filter matching phase of the search request handling. In other words, <i>filtering for dynamically added attributes always fails</i>. The resulting entry must comply with the LDAP data model, so constraints are enforced. For example, if a <i>SINGLE-VALUE</i> attribute is listed, only the first value found during the list expansion appears in the final entry. The above described behavior is disabled when the <i>manageDSAit</i> control (RFC 3296) is used. In that case, the contents of the dynamic group entry is returned; namely, the URLs are returned instead of being expanded. </p>
<h2>Configuration</h2>
<p>The config directives that are specific to the <code>dynlist</code> overlay must be prefixed by <code>dynlist-</code>, to avoid potential conflicts with directives specific to the underlying database or to other stacked overlays. </p>
<dl>
<dt><code>overlay dynlist</code></p>
<dd>This directive adds the dynlist overlay to the current database, or to the frontend, if used before any database instantiation; see <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) for details. </p>
</dl>
<p> This <code>slapd.conf</code> configuration option is defined for the dynlist overlay. It may have multiple occurrences, and it must appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>dynlist-attrset &lt;group-oc&gt; [&lt;URI&gt;] &lt;URL-ad&gt; [[&lt;mapped-ad&gt;:]&lt;member-ad&gt; &#8230;]</code></p>
<dd>The value <code>group-oc</code> is the name of the objectClass that triggers the dynamic expansion of the data. </p>
<p> The optional <code>URI</code> restricts expansion only to entries matching the <i>DN</i>, the <i>scope</i> and the <i>filter</i> portions of the URI. </p>
<p> The value <code>URL-ad</code> is the name of the attributeDescription that contains the URI that is expanded by the overlay; if none is present, no expansion occurs. If the intersection of the attributes requested by the search operation (or the asserted attribute for compares) and the attributes listed in the URI is empty, no expansion occurs for that specific URI. It must be a subtype of <i>labeledURI</i>. </p>
<p> The value <code>member-ad</code> is optional; if present, the overlay behaves as a dynamic group: this attribute will list the DN of the entries resulting from the internal search. In this case, the <i>attrs</i> portion of the URIs in the <code>URL-ad</code> attribute must be absent, and the <i>DN</i>s of all the entries resulting from the expansion of the URIs are listed as values of this attribute. Compares that assert the value of the <code>member-ad</code> attribute of entries with <code>group-oc</code> objectClass apply as if the DN of the entries resulting from the expansion of the URI were present in the <code>group-oc </code> entry as values of the <code>member-ad</code> attribute. </p>
<p> Alternatively, <code>mapped-ad</code> can be used to remap attributes obtained through expansion. <code>member-ad</code> attributes are not filled by expanded DN, but are remapped as <code>mapped-ad </code> attributes. Multiple mapping statements can be used. </p>
</dl>
<p> The dynlist overlay may be used with any backend, but it is mainly intended for use with local storage backends. In case the URI expansion is very resource-intensive and occurs frequently with well-defined patterns, one should consider adding a proxycache later on in the overlay stack.</p>
<h2>Authorization</h2>
<p>By default the expansions are performed using the identity of the current LDAP user. This identity may be overridden by setting the <code>dgIdentity</code> attribute in the group&#8217;s entry to the DN of another LDAP user. In that case the dgIdentity will be used when expanding the URIs in the object. Setting the dgIdentity to a zero-length string will cause the expansions to be performed anonymously. Note that the dgIdentity attribute is defined in the <code>dyngroup</code> schema, and this schema must be loaded before the dgIdentity authorization feature may be used. If the <code>dgAuthz</code> attribute is also present in the group&#8217;s entry, its values are used to determine what identities are authorized to use the <code>dgIdentity</code> to expand the group. Values of the <code>dgAuthz</code> attribute must conform to the (experimental) <i>OpenLDAP authz</i> syntax.</p>
<h2>Example</h2>
<p>This example collects all the email addresses of a database into a single entry; first of all, make sure that slapd.conf contains the directives: </p>
<pre> include /path/to/dyngroup.schema
 # ...
 database &lt;database&gt;
 # ...
 overlay dynlist
 dynlist-attrset groupOfURLs memberURL</pre>
<p>and that slapd loads dynlist.la, if compiled as a run-time module; then add to the database an entry like </p>
<pre> dn: cn=Dynamic List,ou=Groups,dc=example,dc=com
 objectClass: groupOfURLs
 cn: Dynamic List
 memberURL: <a href="ldap:///ou=People,dc=example,dc=com?mail?sub?(objectClass=person)">ldap:///ou=People,dc=example,dc=com?mail?sub?(objectClass=person)</a></pre>
<p>If no &lt;attrs&gt; are provided in the URI, all (non-operational) attributes are collected. This example implements the dynamic group feature on the <code>member</code> attribute: </p>
<pre> include /path/to/dyngroup.schema
 # ...
 database &lt;database&gt;
 # ...
 overlay dynlist
 dynlist-attrset groupOfURLs memberURL member</pre>
<p>A dynamic group with dgIdentity authorization could be created with an entry like </p>
<pre> dn: cn=Dynamic Group,ou=Groups,dc=example,dc=com
 objectClass: groupOfURLs
 objectClass: dgIdentityAux
 cn: Dynamic Group
 memberURL: <a href="ldap:///ou=People,dc=example,dc=com??sub?(objectClass=person)">ldap:///ou=People,dc=example,dc=com??sub?(objectClass=person)</a>
 dgIdentity: cn=Group Proxy,ou=Services,dc=example,dc=com</pre>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). The <code><a href="/docs/linux/man/5-slapo-dynlist/">slapo-dynlist</a></code>(5) overlay supports dynamic configuration via <code>back-config</code>.</p>
<h2>Acknowledgements</h2>
<p>This module was written in 2004 by Pierangelo Masarati for SysNet s.n.c. </p>
<p> Attribute remapping was contributed in 2008 by Emmanuel Dreyfus.</p>
