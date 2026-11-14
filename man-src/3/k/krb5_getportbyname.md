---
title: "krb5_getportbyname(3)"
name: "krb5_getportbyname"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_getportbyname/"
description: "krb5_getportbyname – get port number by name"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_getportbyname</code> &#8211; get port number by name </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft int Fo krb5_getportbyname Fa krb5_context context Fa const char *service Fa const char *proto Fa int default_port Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_getportbyname gets the port number for Fa service / Fa proto pair from the global service table for and returns it in network order. If it isn&#8217;t found in the global table, the Fa default_port (given in host order) is returned.</p>
<h2>EXAMPLE</h2>
<pre><code>
int port = krb5_getportbyname(context, "kerberos", "tcp", 88);
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3) </p>
<h2>Index</h2>
