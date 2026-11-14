---
title: "slapd-relay(5)"
name: "slapd-relay"
section: "5"
letter: "s"
url: "/docs/linux/man/5-slapd-relay/"
description: "slapd-relay – relay backend to slapd"
---

<p>slapd-relay &#8211; relay backend to slapd</p>
<h2>Synopsis</h2>
<p>/etc/openldap/slapd.conf</p>
<h2>Description</h2>
<p>The primary purpose of this <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) backend is to map a naming context defined in a database running in the same <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8) instance into a virtual naming context, with attributeType and objectClass manipulation, if required. It requires the <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) overlay. </p>
<p> This backend and the above mentioned overlay are experimental.</p>
<h2>Configuration</h2>
<p>The following <code>slapd.conf</code> directives apply to the relay backend database. That is, they must follow a &quot;database relay&quot; line and come before any subsequent &quot;backend&quot; or &quot;database&quot; lines. Other database options are described in the <code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5) manual page; only the <code>suffix</code> directive is allowed by the <i>relay</i> backend.</p>
<dl>
<dt><code>relay &lt;real naming context&gt;</code></p>
<dd>The naming context of the database that is presented under a virtual naming context. The presence of this directive implies that one specific database, i.e. the one serving the <code>real naming context</code>, will be presented under a virtual naming context. </p>
</dl>
<h2>Massaging</h2>
<p>The <code>relay</code> database does not automatically rewrite the naming context of requests and responses. For this purpose, the <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) overlay must be explicitly instantiated, and configured as appropriate. Usually, the <code>rwm-suffixmassage</code> directive suffices if only naming context rewriting is required.</p>
<h2>Access Rules</h2>
<p>One important issue is that access rules are based on the identity that issued the operation. After massaging from the virtual to the real naming context, the frontend sees the operation as performed by the identity in the real naming context. Moreover, since <code>back-relay</code> bypasses the real database frontend operations by short-circuiting operations through the internal backend API, the original database access rules do not apply but in selected cases, i.e. when the backend itself applies access control. As a consequence, the instances of the relay database must provide own access rules that are consistent with those of the original database, possibly adding further specific restrictions. So, access rules in the <code>relay</code> database must refer to identities in the real naming context. Examples are reported in the EXAMPLES section.</p>
<h2>Scenarios</h2>
<p>If no <code>relay</code> directive is given, the <i>relay</i> database does not refer to any specific database, but the most appropriate one is looked-up after rewriting the request DN for the operation that is being handled. </p>
<p> This allows to write carefully crafted rewrite rules that cause some of the requests to be directed to one database, and some to another; e.g., authentication can be mapped to one database, and searches to another, or different target databases can be selected based on the DN of the request, and so. </p>
<p> Another possibility is to map the same operation to different databases based on details of the virtual naming context, e.g. groups on one database and persons on another.</p>
<h2>Examples</h2>
<p>To implement a plain virtual naming context mapping that refers to a single database, use </p>
<pre><code>database                relay
suffix                  &quot;dc=virtual,dc=naming,dc=context&quot;
relay                   &quot;dc=real,dc=naming,dc=context&quot;
overlay                 rwm
rwm-suffixmassage       &quot;dc=real,dc=naming,dc=context&quot;</code></pre>
<p> To implement a plain virtual naming context mapping that looks up the real naming context for each operation, use </p>
<pre><code>database                relay
suffix                  &quot;dc=virtual,dc=naming,dc=context&quot;
overlay                 rwm
rwm-suffixmassage       &quot;dc=real,dc=naming,dc=context&quot;</code></pre>
<p> This is useful, for instance, to relay different databases that share the terminal portion of the naming context (the one that is rewritten). To implement the old-fashioned suffixalias, e.g. mapping the virtual to the real naming context, but not the results back from the real to the virtual naming context, use </p>
<pre> database relay
 suffix &quot;dc=virtual,dc=naming,dc=context&quot;
 relay &quot;dc=real,dc=naming,dc=context&quot;
 overlay rwm
 rwm-rewriteEngine on
 rwm-rewriteContext default
 rwm-rewriteRule &quot;dc=virtual,dc=naming,dc=context&quot;
 &quot;dc=real,dc=naming,dc=context&quot; &quot;:@&quot;
 rwm-rewriteContext searchFilter
 rwm-rewriteContext searchEntryDN
 rwm-rewriteContext searchAttrDN
 rwm-rewriteContext matchedDN</pre>
<p>Note that the <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5) overlay is instantiated, but the rewrite rules are written explicitly, rather than automatically as with the <code>rwm-suffixmassage</code> statement, to map all the virtual to real naming context data flow, but none of the real to virtual. Access rules: </p>
<pre> database bdb
 suffix &quot;dc=example,dc=com&quot;
 # skip...
 access to dn.subtree=&quot;dc=example,dc=com&quot;
 by dn.exact=&quot;cn=Supervisor,dc=example,dc=com&quot; write
 by * read
 database relay
 suffix &quot;o=Example,c=US&quot;
 relay &quot;dc=example,dc=com&quot;
 overlay rwm
 rwm-suffixmassage &quot;dc=example,dc=com&quot;
 # skip ...
 access to dn.subtree=&quot;o=Example,c=US&quot;
 by dn.exact=&quot;cn=Supervisor,dc=example,dc=com&quot; write
 by dn.exact=&quot;cn=Relay Supervisor,dc=example,dc=com&quot; write
 by * read</pre>
<p>Note that, in both databases, the identities (the <code>&lt;who&gt; </code> clause) are in the <code>real naming context</code>, i.e. <code>`dc=example,dc=com&#8217;</code>, while the targets (the <code>&lt;what&gt; </code> clause) are in the <code>real</code> and in the <code>virtual naming context</code>, respectively.</p>
<h2>Access Control</h2>
<p>The <code>relay</code> backend does not honor any of the access control semantics described in <code><a href="/docs/linux/man/5-slapd-access/">slapd.access</a></code>(5); all access control is delegated to the relayed database(s). Only <code>read (=r)</code> access to the <code>entry</code> pseudo-attribute and to the other attribute values of the entries returned by the <code>search</code> operation is honored, which is performed by the frontend.</p>
<h2>Files</h2>
<dl>
<dt>/etc/openldap/slapd.conf</p>
<dd>default slapd configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-slapd-conf/">slapd.conf</a></code>(5), <code><a href="/docs/linux/man/5-slapd-config/">slapd-config</a></code>(5), <code><a href="/docs/linux/man/5-slapo-rwm/">slapo-rwm</a></code>(5), <code><a href="/docs/linux/man/8-slapd/">slapd</a></code>(8). </p>
