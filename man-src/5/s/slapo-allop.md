---
title: "slapo-allop(5)"
name: "slapo-allop"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapo-allop/"
description: "slapo-allop – All Operational Attributes overlay"
---

<p>slapo-allop &#8211; All Operational Attributes overlay</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The All Operational Attributes overlay is designed to allow slapd to interoperate with dumb clients that expect all attributes, including operational ones, to be returned when &quot;*&quot; or an empty attribute list is requested, as opposed to RFC2251 and RFC3673.</p>
<h2>Configuration</h2>
<p>These <code>slapd.conf</code> options apply to the All Operational overlay. They should appear after the <code>overlay</code> directive and before any subsequent <code>database</code> directive.</p>
<dl>
<dt><code>allop-URI &lt;ldapURI&gt;</code></p>
<dd>Specify the base and the scope of search operations that trigger the overlay. By default, it is &quot;<a href="ldap:///??base">ldap:///??base</a>&quot;, i.e. it only applies to the rootDSE. This requires the overlay to be instantited as global. </p>
</dl>
<h2>Examples</h2>
<p>default behavior: only affects requests to the rootDSE </p>
<pre> # global
 overlay allop</pre>
<p>affects all requests </p>
<pre> # global
 overlay allop
 allop-URI &quot;<a href="ldap:///??sub">ldap:///??sub</a>&quot;</pre>
<pre><code>affects only requests directed to the suffix of a database

# per database
database        bdb
suffix          &quot;dc=example,dc=com&quot;
# database specific directives ...
overlay         allop
allop-URI       &quot;ldap:///dc=example,dc=com??base&quot;
</code></pre>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5). </p>
<h2>Acknowledgements</h2>
<p>This module was written in 2005 by Pierangelo Masarati for SysNet s.n.c.</p>
