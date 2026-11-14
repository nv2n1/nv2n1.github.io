---
title: "slapo-sssvlv(5)"
name: "slapo-sssvlv"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-sssvlv/"
description: "slapo-sssvlv – Server Side Sorting and Virtual List View overlay to slapd"
---

<p>slapo-sssvlv &#8211; Server Side Sorting and Virtual List View overlay to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>This overlay implements the LDAP Server Side Sorting (RFC2891) control as well as the Virtual List View control. It also replaces the default implementation of the LDAP PagedResults (RFC2696) control, to ensure that it works with Sorting. The overlay can be used with any backend or globally for all backends. Since a complete result set must be generated in memory before sorting can be performed, processing sort requests can have a large impact on the server&#8217;s memory use. As such, any connection is limited to having only a limited number of sort requests active at a time. Additional limits may be configured as described below. </p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the SSSVLV overlay. They should appear after the <code>overlay</code> directive.</p>
<dl>
<dt><code>sssvlv-max &lt;num&gt;</code></p>
<dd>Set the maximum number of concurrent sort requests allowed across all connections. The default is one half of the number of server threads.</p>
<dt><code>sssvlv-maxkeys &lt;num&gt;</code></p>
<dd>Set the maximum number of keys allowed in a sort request. The default is 5.</p>
<dt><code>sssvlv-maxperconn &lt;num&gt;</code></p>
<dd>Set the maximum number of concurrent paged search requests per connection. The default is 5. The number of concurrent requests remains limited by <code>sssvlv-max.</code></dl>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</p>
<dt>/etc/openldap/slapd.d</p>
<dd>default slapd configuration directory</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5). </p>
<p> &quot;OpenLDAP Administrator&#8217;s Guide&quot; (<a rel="nofollow" href="http://www.OpenLDAP.org/doc/admin/)">http://www.OpenLDAP.org/doc/admin/)</a> </p>
<p> IETF LDAP Virtual List View proposal by D. Boreham, J. Sermersheim, and A. Kashi in IETF document &quot;draft-ietf-ldapext-ldapv3-vlv-09.txt&quot;.</p>
<h2>Author</h2>
<p>Howard Chu</p>
