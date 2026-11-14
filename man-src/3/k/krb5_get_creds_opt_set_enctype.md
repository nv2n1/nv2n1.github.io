---
title: "krb5_get_creds_opt_set_enctype(3)"
name: "krb5_get_creds_opt_set_enctype"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_get_creds_opt_set_enctype/"
description: "krb5_get_creds krb5_get_creds_opt_add_options krb5_get_creds_opt_alloc krb5_get_creds_opt_free krb5_get_creds_opt_set_enctype krb5_get_creds_opt_set_impersonate krb5_get_creds_opt_set_options krb5_..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_creds</code> <code>krb5_get_creds_opt_add_options</code> <code>krb5_get_creds_opt_alloc</code> <code>krb5_get_creds_opt_free</code> <code>krb5_get_creds_opt_set_enctype</code> <code>krb5_get_creds_opt_set_impersonate</code> <code>krb5_get_creds_opt_set_options</code> <code>krb5_get_creds_opt_set_ticket</code> &#8211; get credentials from the KDC </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_get_creds Fa krb5_context context Fa krb5_get_creds_opt opt Fa krb5_ccache ccache Fa krb5_const_principal inprinc Fa krb5_creds **out_creds Fc Ft void Fo krb5_get_creds_opt_add_options Fa krb5_context context Fa krb5_get_creds_opt opt Fa krb5_flags options Fc Ft krb5_error_code Fo krb5_get_creds_opt_alloc Fa krb5_context context Fa krb5_get_creds_opt *opt Fc Ft void Fo krb5_get_creds_opt_free Fa krb5_context context Fa krb5_get_creds_opt opt Fc Ft void Fo krb5_get_creds_opt_set_enctype Fa krb5_context context Fa krb5_get_creds_opt opt Fa krb5_enctype enctype Fc Ft krb5_error_code Fo krb5_get_creds_opt_set_impersonate Fa krb5_context context Fa krb5_get_creds_opt opt Fa krb5_const_principal self Fc Ft void Fo krb5_get_creds_opt_set_options Fa krb5_context context Fa krb5_get_creds_opt opt Fa krb5_flags options Fc Ft krb5_error_code Fo krb5_get_creds_opt_set_ticket Fa krb5_context context Fa krb5_get_creds_opt opt Fa const Ticket *ticket Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_get_creds fetches credentials specified by Fa opt by first looking in the Fa ccache , and then it doesn&#8217;t exists, fetch the credential from the KDC using the krbtgts in Fa ccache . The credential is returned in Fa out_creds and should be freed using the function Fn krb5_free_creds . </p>
<p> The structure <code>krb5_get_creds_opt</code> controls the behavior of Fn krb5_get_creds . The structure is opaque to consumers that can set the content of the structure with accessors functions. All accessor functions make copies of the data that is passed into accessor functions, so external consumers free the memory before calling Fn krb5_get_creds . </p>
<p> The structure <code>krb5_get_creds_opt</code> is allocated with Fn krb5_get_creds_opt_alloc and freed with Fn krb5_get_creds_opt_free . The free function also frees the content of the structure set by the accessor functions. </p>
<p> Fn krb5_get_creds_opt_add_options and Fn krb5_get_creds_opt_set_options adds and sets options to the Fi krb5_get_creds_opt structure . The possible options to set are</p>
<dl>
<dt><code>KRB5_GC_CACHED</code></p>
<dd> Only check the Fa ccache , don&#8217;t got out on network to fetch credential.</p>
<dt><code>KRB5_GC_USER_USER</code></p>
<dd> request a user to user ticket. This options doesn&#8217;t store the resulting user to user credential in the Fa ccache .</p>
<dt><code>KRB5_GC_EXPIRED_OK</code></p>
<dd> returns the credential even if it is expired, default behavior is trying to refetch the credential from the KDC.</p>
<dt><code>KRB5_GC_NO_STORE</code></p>
<dd> Do not store the resulting credentials in the Fa ccache .</dl>
<p> Fn krb5_get_creds_opt_set_enctype sets the preferred encryption type of the application. Don&#8217;t set this unless you have to since if there is no match in the KDC, the function call will fail. </p>
<p> Fn krb5_get_creds_opt_set_impersonate sets the principal to impersonate., Returns a ticket that have the impersonation principal as a client and the requestor as the service. Note that the requested principal have to be the same as the client principal in the krbtgt. </p>
<p> Fn krb5_get_creds_opt_set_ticket sets the extra ticket used in user-to-user or contrained delegation use case.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_get_credentials3, krb5.conf5 </p>
<h2>Index</h2>
