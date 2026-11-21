---

title: "echoping_ldap(1)"
name: "echoping_ldap"
section: "1"
letter: "e"
url: "/docs/linux/man/1-echoping_ldap/"
description: "echoping_ldap – echoping plugin which connects to a LDAP server"
---

<p> echoping_ldap &#8211; echoping plugin which connects to a LDAP server </p>
<h2>SYNOPSIS</h2>
<p> <code>echoping</code> [echoping options] -m ldap <code>hostname</code> [-b<i>base]</i> [-r<i>request]</i> [-s<i>scope]</i> [-p<i>port]</i></p>
<h2>DESCRIPTION</h2>
<p> ldap is an echoping plugin to connect to LDAP servers.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-r request</code></dt>
<dd> The request to the LDAP server, in LDAP filter language. By default (objectclass=*).</dd>
<dt><code>-b base</code></dt>
<dd> Base of the search, for instance &quot;dc=current,dc=bugs,dc=debian,dc=org&quot;</dd>
<dt><code>-s scope</code></dt>
<dd> Scope of the search, &quot;sub&quot;, &quot;one&quot; or &quot;base&quot;</dd>
<dt><code>-p port</code></dt>
<dd> TCP port to use</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-echoping/">echoping</a></code>(1),</p>
<h2>AUTHOR</h2>
<p> Stephane Bortzmeyer &lt;bortz [at] users.sourceforge.net&gt; </p>
