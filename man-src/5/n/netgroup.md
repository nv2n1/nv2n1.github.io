---
title: "netgroup(5)"
name: "netgroup"
section: "5"
letter: "n"
url: "/docs/linux/man/5-netgroup/"
description: "netgroup – specify network groups"
---

<p>netgroup &#8211; specify network groups</p>
<h2>Description</h2>
<p>The <i>netgroup</i> file defines &quot;netgroups&quot;, which are sets of (host, user, domain) tuples, used for permission checking when doing remote mounts,remote logins and remote shells. </p>
<p> Each line in the file consists of a netgroup name followed by a by a list of members, where a member is either another netgroup name, or a triple: </p>
<pre> (<i>host</i>, <i>user</i>, <i>domain</i>) </pre>
<p>where the <i>host</i>, <i>user</i>, and <i>domain</i> are character strings for the corresponding components. Any of the three fields can be empty, in which case it specifies a &quot;wildcard&quot;, or may consist of the string &quot;-&quot; to specify &quot;no valid value&quot;. The <i>domain</i> field must either be the local domain name or empty for the netgroup entry to be used. This field does not limit the netgroup or provide security. The domain field refers to the domain in which the triple is valid, not the domain containing the the trusted host. </p>
<p> A gateway machine should be listed under all possible hostnames by which it may be recognized: </p>
<pre> gateway (server, , ) (server-sn, , ) (server-bb, , )</pre>
<p>The <code><a href="/docs/linux/man/3-getnetgrent/">getnetgrent</a></code>(3), function should normally be used to access the netgroup database.</p>
<h2>Files</h2>
<p><i>/etc/netgroup</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getnetgrent/">getnetgrent</a></code>(3), <code><a href="/docs/linux/man/5-exports/">exports</a></code>(5), <code><a href="/docs/linux/man/8-makedbm/">makedbm</a></code>(8), <code><a href="/docs/linux/man/8-ypserv/">ypserv</a></code>(8)</p>
<h2>Warnings</h2>
<p>The triple (,,domain) allows all users and machines trusted access, and has the same effect as the triple (,,). Use the <i>host</i> and <i>user</i> fields of the triple to restrict the access correctly to a specific set of members.</p>
<h2>Author</h2>
<p>Thorsten Kukuk &lt;kukuk [at] thkukuk.de&gt;</p>
