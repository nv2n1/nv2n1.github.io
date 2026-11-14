---
title: "slapo-collect(5)"
name: "slapo-collect"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-collect/"
description: "slapo-collect – Collective attributes overlay to slapd"
---

<p>slapo-collect &#8211; Collective attributes overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The collect overlay is used to provide a relatively coarse implementation of RFC 3671 collective attributes. In X.500, a collective attribute is &quot;a user attribute whose values are the same for each member of an entry collection&quot;. Collective attributes are added to entries returned by a search operation when the entry is within the scope of the related ancestor. Collective attributes can only be modified when the modification affects the related ancestor. </p>
<h2>Configuration</h2>
<p>This <code>slapd.conf</code> option applies to the collect overlay. It should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>collectinfo &lt;DN&gt; &lt;attrlist&gt;</code></p>
<dd>Specify the <code>DN</code> of the ancestor entry and the set of related collective attributes, where <code>attrlist</code> is a comma-separated list of attributes. The <code>DN </code> should be within the naming context of the database. </p>
</dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), The <code><a href="/docs/linux/man/5-slapo-collect/">slapo-collect</a></code>(5) overlay supports dynamic configuration via <code>back-config</code>.</p>
<h2>Acknowledgements</h2>
<p>This module was written in 2003 by Howard Chu. This man page was written in 2008 by Pierangelo Masarati. <code>OpenLDAP Software</code> is developed and maintained by The OpenLDAP Project &lt;<a rel="nofollow" href="http://www.openldap.org/">http://www.openldap.org/</a>&gt;. <code>OpenLDAP Software</code> is derived from University of Michigan LDAP 3.3 Release.</p>
