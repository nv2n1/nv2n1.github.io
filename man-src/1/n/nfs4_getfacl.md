---
title: "nfs4_getfacl(1)"
name: "nfs4_getfacl"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nfs4_getfacl/"
description: "nfs4_getfacl – get NFSv4 file/directory access control lists"
---

<h2>NAME</h2>
<p> nfs4_getfacl &#8211; get NFSv4 file/directory access control lists</p>
<h2>SYNOPSIS</h2>
<p> <code>nfs4_getfacl [-H]</code> <i>file</i></p>
<h2>DESCRIPTION</h2>
<p> <code>nfs4_getfacl </code> will display the NFSv4 Access Control List (ACL) for <i>file </i> (a file or directory), provided <i>file </i> is on a mounted NFSv4 filesystem which supports ACLs. </p>
<p> If the <code>-H</code>/<code>&#8211;more-help</code> flag is specified, <code>nfs4_getfacl</code> will print some information about NFSv4 ACLs and the fields used in ACEs. </p>
<p> The output format for an NFSv4 file ACL, e.g., is:</p>
<dl>
<dt>
<dd>
<pre><code>
A::OWNER @ : rwatTnNcCy
                 A::alice[at] nfsdomain.org : rxtncy
                                                  A::bob[at] nfsdomain.org : rwadtTnNcCy
                                                                                 A : g : GROUP @ : rtncy
                                                                                                       D : g : GROUP @ : waxTC
                                                                                                                             A::EVERYONE @ : rtncy
                                                                                                                                                 D::EVERYONE @ : waxTC
</code></pre>
</dl>
<p> In the example output above, the user `alice [at] nfsdomain.org&#8217; has the equivalent of &quot;read&quot; and &quot;execute&quot; permissions, `bob [at] nfsdomain.org&#8217; has &quot;read&quot; and &quot;write&quot;, and both `GROUP@&#8217; and `EVERYONE@&#8217; have &quot;read&quot;. </p>
<p> Refer to the <code><a href="/docs/linux/man/5-nfs4_acl/">nfs4_acl</a></code>(5) manpage for detailed information about NFSv4 ACL terminology and syntax.</p>
<h2>AUTHORS</h2>
<p> <code>nfs4_getfacl</code> was written by people at CITI, the Center for Information Technology Integration (<i><a rel="nofollow" href="http://www.citi.umich.edu">http://www.citi.umich.edu</a></i>). This manpage was written by David Richter.</p>
<h2>CONTACT</h2>
<p> Please send bug reports, feature requests, and comments to &lt;<i>nfsv4 [at] linux-nfs.org</i>&gt;.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nfs4_setfacl/">nfs4_setfacl</a></code>(1), <code><a href="/docs/linux/man/5-nfs4_acl/">nfs4_acl</a></code>(5), <i>RFC3530</i> (NFSv4.0), NFSv4.1 Minor Version Draft. </p>
<h2>Index</h2>
