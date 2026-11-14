---
title: "domain(8)"
name: "domain"
section: "8"
letter: "d"
url: "/docs/linux/man/8-domain/"
description: "domain – nnrpd domain resolver"
---

<p>domain &#8211; nnrpd domain resolver</p>
<h2>Synopsis</h2>
<p><code>domain</code> <code>domainname</code></p>
<h2>Description</h2>
<p>This program can be used in <i>readers.conf</i> to grant access based on the subdomain part of the remote hostname. In particular, it only returns success if the remote hostname ends in <code>domainname</code>. (A leading dot on <code>domainname</code> is optional; even without it, the argument must match on dot-separated boundaries). The &#8220;username&#8221; returned is whatever initial part of the remote hostname remains after <code>domainname</code> is removed. It is an error if there is no initial part (that is, if the remote hostname is <i>exactly</i> the specified <code>domainname</code>).</p>
<h2>Example</h2>
<p>The following <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) fragment grants access to hosts with internal domain names: </p>
<pre> auth internal {
 res: &quot;domain .internal&quot;
 default-domain: &quot;example.com&quot;
 }
 access internal {
 users: &quot;*@example.com&quot;
 newsgroups: example.*
 }</pre>
<p>Access is granted to the example.* groups for all connections from hosts that resolve to hostnames ending in <tt>&quot;.internal&quot;</tt>; a connection from &#8220;foo.internal&#8221; would match access groups as &#8220;foo [at] example.com&#8221;.</p>
<h2>Bugs</h2>
<p>It seems the code does not confirm that the matching part is actually at the end of the remote hostname (e.g., &#8220;domain: example.com&#8221; would match the remote host &#8220;foo.example.com.org&#8221; by ignoring the trailing &#8220;.org&#8221; part). </p>
<p> Does this resolver actually provide any useful functionality not available by using wildcards in the <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) <i>hosts</i> parameter? If so, the example above should reflect this functionality.</p>
<h2>History</h2>
<p>This documentation was written by Jeffrey M. Vinocur &lt;jeff [at] litech.org&gt;. </p>
<p> <tt>$Id:</tt> domain.pod 8200 2008-11-30 13:31:30Z iulius $</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5) </p>
