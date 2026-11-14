---
title: "slapd-overlays(5)"
name: "slapd-overlays"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-overlays/"
description: "slapd.overlays – overlays for slapd, the stand-alone LDAP daemon"
---

<p>slapd.overlays &#8211; overlays for slapd, the stand-alone LDAP daemon</p>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) daemon can use a variety of different overlays to alter or extend the normal behavior of a database backend. Overlays may be compiled statically into slapd, or when module support is enabled, they may be dynamically loaded. Most of the overlays are only allowed to be configured on individual databases, but some may also be configured globally. </p>
<p> Configuration options for each overlay are documented separately in the corresponding <code>slapo-&lt;overlay&gt;</code>(5) manual pages.</p>
<dl>
<dt><code>accesslog</code></p>
<dd>Access Logging. This overlay can record accesses to a given backend database on another database.</p>
<dt><code>auditlog</code></p>
<dd>Audit Logging. This overlay records changes on a given backend database to an LDIF log file. By default it is not built.</p>
<dt><code>chain</code></p>
<dd>Chaining. This overlay allows automatic referral chasing when a referral would have been returned, either when configured by the server or when requested by the client.</p>
<dt><code>collect</code></p>
<dd>Collective Attributes. This overlay implements RFC 3671 collective attributes; these attributes share common values over all the members of the collection as inherited from an ancestor entry.</p>
<dt><code>constraint</code></p>
<dd>Constraint. This overlay enforces a regular expression constraint on all values of specified attributes. It is used to enforce a more rigorous syntax when the underlying attribute syntax is too general.</p>
<dt><code>dds</code></p>
<dd>Dynamic Directory Services. This overlay supports dynamic objects, which have a limited life after which they expire and are automatically deleted.</p>
<dt><code>dyngroup</code></p>
<dd>Dynamic Group. This is a demo overlay which extends the Compare operation to detect members of a dynamic group. It has no effect on any other operations.</p>
<dt><code>dynlist</code></p>
<dd>Dynamic List. This overlay allows expansion of dynamic groups and more.</p>
<dt><code>memberof</code></p>
<dd>MemberOf. This overlay maintains automatic reverse group membership values, typically stored in an attribute called memberOf.</p>
<dt><code>pbind</code></p>
<dd>Proxybind. This overlay forwards simple bind requests on a local database to a remote LDAP server.</p>
<dt><code>pcache</code></p>
<dd>Proxycache. This overlay allows caching of LDAP search requests in a local database. It is most often used with the <code><a href="/docs/linux/man/5-slapd-ldap/">slapd-ldap</a></code>(5) or <code><a href="/docs/linux/man/5-slapd-meta/">slapd-meta</a></code>(5) backends.</p>
<dt><code>ppolicy</code></p>
<dd>Password Policy. This overlay provides a variety of password control mechanisms, e.g. password aging, password reuse and duplication control, mandatory password resets, etc.</p>
<dt><code>refint</code></p>
<dd>Referential Integrity. This overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to maintain the cohesiveness of a schema which utilizes reference attributes.</p>
<dt><code>retcode</code></p>
<dd>Return Code. This overlay is useful to test the behavior of clients when server-generated erroneous and/or unusual responses occur.</p>
<dt><code>rwm</code></p>
<dd>Rewrite/remap. This overlay is experimental. It performs basic DN/data rewrite and objectClass/attributeType mapping.</p>
<dt><code>sssvlv</code></p>
<dd>Server Side Sorting and Virtual List Views. This overlay implements the RFC2891 server-side sorting control and virtual list view controls, and replaces the RFC2696 paged-results implementation to ensure it works with the sorting technique.</p>
<dt><code>syncprov</code></p>
<dd>Syncrepl Provider. This overlay implements the provider-side support for <code>syncrepl</code> replication, including persistent search functionality.</p>
<dt><code>translucent</code></p>
<dd>Translucent Proxy. This overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to create a &quot;translucent proxy&quot;. Content of entries retrieved from a remote LDAP server can be partially overridden by the database.</p>
<dt><code>unique</code></p>
<dd>Attribute Uniqueness. This overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to enforce the uniqueness of some or all attributes within a subtree.</p>
<dt><code>valsort</code></p>
<dd>Value Sorting. This overlay can be used to enforce a specific order for the values of an attribute when it is returned in a search.</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/openldap/slapd.d</p>
<dd>default slapd configuration directory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-ldap/">ldap</a></code>(3), <code><a href="/docs/linux/man/5-slapo-accesslog/">slapo-accesslog</a></code>(5), <code><a href="/docs/linux/man/5-slapo-auditlog/">slapo-auditlog</a></code>(5), <code><a href="/docs/linux/man/5-slapo-chain/">slapo-chain</a></code>(5), <code><a href="/docs/linux/man/5-slapo-collect/">slapo-collect</a></code>(5), <code><a href="/docs/linux/man/5-slapo-constraint/">slapo-constraint</a></code>(5), <code><a href="/docs/linux/man/5-slapo-dds/">slapo-dds</a></code>(5), <code><a href="/docs/linux/man/5-slapo-dyngroup/">slapo-dyngroup</a></code>(5), <code><a href="/docs/linux/man/5-slapo-dynlist/">slapo-dynlist</a></code>(5), <code><a href="/docs/linux/man/5-slapo-memberof/">slapo-memberof</a></code>(5), <code><a href="/docs/linux/man/5-slapo-pbind/">slapo-pbind</a></code>(5), <code><a href="/docs/linux/man/5-slapo-pcache/">slapo-pcache</a></code>(5), <code><a href="/docs/linux/man/5-slapo-ppolicy/">slapo-ppolicy</a></code>(5), <code><a href="/docs/linux/man/5-slapo-refint/">slapo-refint</a></code>(5), <code><a href="/docs/linux/man/5-slapo-retcode/">slapo-retcode</a></code>(5), <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5), <code><a href="/docs/linux/man/5-slapo-sssvlv/">slapo-sssvlv</a></code>(5), <code><a href="/docs/linux/man/5-slapo-syncprov/">slapo-syncprov</a></code>(5), <code><a href="/docs/linux/man/5-slapo-translucent/">slapo-translucent</a></code>(5), <code><a href="/docs/linux/man/5-slapo-unique/">slapo-unique</a></code>(5). <code><a href="/docs/linux/man/5-slapo-valsort/">slapo-valsort</a></code>(5). <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-backends/">slapd.backends</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a></p>
<h2>Acknowledgements</h2>
<p><code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
