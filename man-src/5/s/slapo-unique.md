---
title: "slapo-unique(5)"
name: "slapo-unique"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-unique/"
description: "slapo-unique – Attribute Uniqueness overlay to slapd"
---

<p>slapo-unique &#8211; Attribute Uniqueness overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The Attribute Uniqueness overlay can be used with a backend database such as <code><a href="/docs/linux/man/5-slapd-bdb/">slapd-bdb</a></code>(5) to enforce the uniqueness of some or all attributes within a scope. This subtree defaults to all objects within the subtree of the database for which the Uniqueness overlay is configured. </p>
<p> Uniqueness is enforced by searching the subtree to ensure that the values of all attributes presented with an <code>add</code>, <code>modify</code> or <code>modrdn</code> operation are unique within the scope. For example, if uniqueness were enforced for the <code>uid</code> attribute, the subtree would be searched for any other records which also have a <code>uid</code> attribute containing the same value. If any are found, the request is rejected. </p>
<p> The search is performed using the rootdn of the database, to avoid issues with ACLs preventing the overlay from seeing all of the relevant data. As such, the database must have a rootdn configured.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the Attribute Uniqueness overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>unique_uri &lt;[strict ][ignore ]URI[URI&#8230;]&#8230;&gt;</code></p>
<dd>Configure the base, attributes, scope, and filter for uniqueness checking. Multiple URIs may be specified within a domain, allowing complex selections of objects. Multiple <code>unique_uri</code> statements or <code>olcUniqueURI</code> attributes will create independent domains, each with their own independent lists of URIs and ignore/strict settings. </p>
<p> Keywords <code>strict</code> and <code>ignore</code> have to be enclosed in quotes (&quot;) together with the URI. </p>
<p> The LDAP URI syntax is a subset of <code>RFC-4516,</code> and takes the form: </p>
<p> <a href="ldap:///[base">ldap:///[base</a> dn]?[attributes&#8230;]?scope[?filter] </p>
<p> The <code>base dn</code> defaults to that of the back-end database. Specified base dns must be within the subtree of the back-end database. </p>
<p> If no <code>attributes</code> are specified, the URI applies to all non-operational attributes. </p>
<p> The <code>scope</code> component is effectively mandatory, because LDAP URIs default to <code>base</code> scope, which is not valid for uniqueness, because groups of one object are always unique. Scopes of <code>sub</code> (for subtree) and <code>one</code> for one-level are valid. </p>
<p> The <code>filter</code> component causes the domain to apply uniqueness constraints only to matching objects. e.g. <code><a href="ldap:///?cn?sub?(sn=e*)">ldap:///?cn?sub?(sn=e*)</a></code> would require unique <code>cn</code> attributes for all objects in the subtree of the back-end database whose <code>sn</code> starts with an e. </p>
<p> It is possible to assert uniqueness upon all non-operational attributes except those listed by prepending the keyword <code>ignore</code> If not configured, all non-operational (e.g., system) attributes must be unique. Note that the <code>attributes</code> list of an <code>ignore</code> URI should generally contain the <code>objectClass</code>, <code>dc</code>, <code>ou</code> and <code>o</code> attributes, as these will generally not be unique, nor are they operational attributes. </p>
<p> It is possible to set strict checking for the uniqueness domain by prepending the keyword <code>strict.</code> By default, uniqueness is not enforced for null values. Enabling <code>strict</code> mode extends the concept of uniqueness to include null values, such that only one attribute within a subtree will be allowed to have a null value. Strictness applies to all URIs within a uniqueness domain, but some domains may be strict while others are not.</dl>
<p> It is not possible to set both URIs and legacy slapo-unique configuration parameters simultaneously. In general, the legacy configuration options control pieces of a single unfiltered subtree domain.</p>
<dl>
<dt><code>unique_base &lt;basedn&gt;</code></p>
<dd>This legacy configuration parameter should be converted to the <code>base dn</code> component of the above <code>unique_uri</code> style of parameter.</p>
<dt><code>unique_ignore &lt;attribute&#8230;&gt;</code></p>
<dd>This legacy configuration parameter should be converted to a <code>unique_uri</code> parameter with <code>ignore</code> keyword as described above.</p>
<dt><code>unique_attributes &lt;attribute&#8230;&gt;</code></p>
<dd>This legacy configuration parameter should be converted to a <code>unique_uri</code> parameter, as described above.</p>
<dt><code>unique_strict &lt;attribute&#8230;&gt;</code></p>
<dd>This legacy configuration parameter should be converted to a <code>strict</code> keyword prepended to a <code>unique_uri</code> parameter, as described above.</dl>
<h2>Caveats</h2>
<p><code>unique_uri</code> cannot be used with the old-style of configuration, and vice versa. <code>unique_uri</code> can implement everything the older system can do, however. </p>
<p> Typical attributes for the <code>ignore <a href="ldap:///...">ldap:///&#8230;</a></code> URIs are intentionally not hardcoded into the overlay to allow for maximum flexibility in meeting site-specific requirements. </p>
<p> Replication and operations with <code>manageDsaIt</code> control are allowed to bypass this enforcement. It is therefore important that all servers accepting writes have this overlay configured in order to maintain uniqueness in a replicated DIT.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5). </p>
