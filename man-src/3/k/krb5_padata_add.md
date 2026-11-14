---
title: "krb5_padata_add(3)"
name: "krb5_padata_add"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_padata_add/"
description: "krb5_find_padata krb5_padata_add – Kerberos 5 pre-authentication data handling functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_find_padata</code> <code>krb5_padata_add</code> &#8211; Kerberos 5 pre-authentication data handling functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> Ft PA_DATA * Fo krb5_find_padata Fa PA_DATA *val Fa unsigned len Fa int type Fa int *index Fc Ft int Fo krb5_padata_add Fa krb5_context context Fa METHOD_DATA *md Fa int type Fa void *buf Fa size_t len Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_find_padata tries to find the pre-authentication data entry of type Fa type in the array Fa val of length Fa len . The search is started at entry pointed out by Fa *index (zero based indexing). If the type isn&#8217;t found, <code>NULL</code> is returned. </p>
<p> Fn krb5_padata_add adds a pre-authentication data entry of type Fa type pointed out by Fa buf and Fa len to Fa md .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
