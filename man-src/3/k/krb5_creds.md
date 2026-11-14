---
title: "krb5_creds(3)"
name: "krb5_creds"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_creds/"
description: "krb5_creds krb5_copy_creds krb5_copy_creds_contents krb5_free_creds krb5_free_cred_contents – Kerberos 5 credential handling functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_creds</code> <code>krb5_copy_creds</code> <code>krb5_copy_creds_contents</code> <code>krb5_free_creds</code> <code>krb5_free_cred_contents</code> &#8211; Kerberos 5 credential handling functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_copy_creds Fa krb5_context context Fa const krb5_creds *incred Fa krb5_creds **outcred Fc Ft krb5_error_code Fo krb5_copy_creds_contents Fa krb5_context context Fa const krb5_creds *incred Fa krb5_creds *outcred Fc Ft krb5_error_code Fo krb5_free_creds Fa krb5_context context Fa krb5_creds *outcred Fc Ft krb5_error_code Fo krb5_free_cred_contents Fa krb5_context context Fa krb5_creds *cred Fc</p>
<h2>DESCRIPTION</h2>
<p> Vt krb5_creds holds Kerberos credentials: </p>
<pre><code>
typedef struct krb5_creds {
    krb5_principal client;
    krb5_principal server;
    krb5_keyblock session;
    krb5_times times;
    krb5_data ticket;
    krb5_data second_ticket;
    krb5_authdata authdata;
    krb5_addresses addresses;
    krb5_ticket_flags flags;
} krb5_creds;
</code></pre>
<p> Fn krb5_copy_creds makes a copy of Fa incred to Fa outcred . Fa outcred should be freed with Fn krb5_free_creds by the caller. </p>
<p> Fn krb5_copy_creds_contents makes a copy of the content of Fa incred to Fa outcreds . Fa outcreds should be freed by the called with Fn krb5_free_creds_contents . </p>
<p> Fn krb5_free_creds frees the content of the Fa cred structure and the structure itself. </p>
<p> Fn krb5_free_cred_contents frees the content of the Fa cred structure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_compare_creds3, krb5_get_init_creds3, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
