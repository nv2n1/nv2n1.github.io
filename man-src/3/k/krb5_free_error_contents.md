---
title: "krb5_free_error_contents(3)"
name: "krb5_free_error_contents"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_free_error_contents/"
description: "krb5_rd_error krb5_free_error krb5_free_error_contents krb5_error_from_rd_error – parse, free and read error from KRB-ERROR message"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_rd_error</code> <code>krb5_free_error</code> <code>krb5_free_error_contents</code> <code>krb5_error_from_rd_error</code> &#8211; parse, free and read error from KRB-ERROR message </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_rd_error Fa krb5_context context Fa const krb5_data *msg Fa KRB_ERROR *result Fc Ft void Fo krb5_free_error Fa krb5_context context Fa krb5_error *error Fc Ft void Fo krb5_free_error_contents Fa krb5_context context Fa krb5_error *error Fc Ft krb5_error_code Fo krb5_error_from_rd_error Fa krb5_context context Fa const krb5_error *error Fa const krb5_creds *creds Fc</p>
<h2>DESCRIPTION</h2>
<p> Usually applications never needs to parse and understand Kerberos error messages since higher level functions will parse and push up the error in the krb5_context. These functions are described for completeness. </p>
<p> Fn krb5_rd_error parses and returns the kerboeros error message, the structure should be freed with Fn krb5_free_error_contents when the caller is done with the structure. </p>
<p> Fn krb5_free_error frees the content and the memory region holding the structure iself. </p>
<p> Fn krb5_free_error_contents free the content of the KRB-ERROR message. </p>
<p> Fn krb5_error_from_rd_error will parse the error message and set the error buffer in krb5_context to the error string passed back or the matching error code in the KRB-ERROR message. Caller should pick up the message with Fn krb5_get_error_string 3 (don&#8217;t forget to free the returned string with Fn krb5_free_error_string ) .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_set_error_string3, krb5_get_error_string3, krb5.conf5 </p>
<h2>Index</h2>
