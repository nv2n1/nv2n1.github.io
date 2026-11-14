---
title: "krb5_get_krb_admin_hst(3)"
name: "krb5_get_krb_admin_hst"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_get_krb_admin_hst/"
description: "krb5_get_krbhst krb5_get_krb_admin_hst krb5_get_krb_changepw_hst krb5_get_krb524hst krb5_free_krbhst – lookup Kerberos KDC hosts"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_krbhst</code> <code>krb5_get_krb_admin_hst</code> <code>krb5_get_krb_changepw_hst</code> <code>krb5_get_krb524hst</code> <code>krb5_free_krbhst</code> &#8211; lookup Kerberos KDC hosts </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fn krb5_get_krbhst krb5_context context const krb5_realm *realm char ***hostlist Ft krb5_error_code Fn krb5_get_krb_admin_hst krb5_context context const krb5_realm *realm char ***hostlist Ft krb5_error_code Fn krb5_get_krb_changepw_hst krb5_context context const krb5_realm *realm char ***hostlist Ft krb5_error_code Fn krb5_get_krb524hst krb5_context context const krb5_realm *realm char ***hostlist Ft krb5_error_code Fn krb5_free_krbhst krb5_context context char **hostlist</p>
<h2>DESCRIPTION</h2>
<p> These functions implement the old API to get a list of Kerberos hosts, and are thus similar to the Fn krb5_krbhst_init functions. However, since these functions returns <i>all</i> hosts in one go, they potentially have to do more lookups than necessary. These functions remain for compatibility reasons. </p>
<p> After a call to one of these functions, Fa hostlist is a <code>NULL</code> terminated list of strings, pointing to the requested Kerberos hosts. These should be freed with Fn krb5_free_krbhst when done with.</p>
<h2>EXAMPLES</h2>
<p> The following code will print the KDCs of the realm &#8220;MY.REALM&#8221; </p>
<blockquote>
<pre><code>
char **hosts, **p;
krb5_get_krbhst(context, "MY.REALM", &amp;hosts);
for (p = hosts; *p; p++)
    printf("%s
", *p);
krb5_free_krbhst(context, hosts);
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> krb5_krbhst_init3 </p>
<h2>Index</h2>
