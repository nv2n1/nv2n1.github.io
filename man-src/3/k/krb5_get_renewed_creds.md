---
title: "krb5_get_renewed_creds(3)"
name: "krb5_get_renewed_creds"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_get_renewed_creds/"
description: "krb5_get_credentials krb5_get_credentials_with_flags krb5_get_kdc_cred krb5_get_renewed_creds – get credentials from the KDC using krbtgt"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_credentials</code> <code>krb5_get_credentials_with_flags</code> <code>krb5_get_kdc_cred</code> <code>krb5_get_renewed_creds</code> &#8211; get credentials from the KDC using krbtgt </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_get_credentials Fa krb5_context context Fa krb5_flags options Fa krb5_ccache ccache Fa krb5_creds *in_creds Fa krb5_creds **out_creds Fc Ft krb5_error_code Fo krb5_get_credentials_with_flags Fa krb5_context context Fa krb5_flags options Fa krb5_kdc_flags flags Fa krb5_ccache ccache Fa krb5_creds *in_creds Fa krb5_creds **out_creds Fc Ft krb5_error_code Fo krb5_get_kdc_cred Fa krb5_context context Fa krb5_ccache id Fa krb5_kdc_flags flags Fa krb5_addresses *addresses Fa Ticket *second_ticket Fa krb5_creds *in_creds Fa krb5_creds **out_creds Fc Ft krb5_error_code Fo krb5_get_renewed_creds Fa krb5_context context Fa krb5_creds *creds Fa krb5_const_principal client Fa krb5_ccache ccache Fa const char *in_tkt_service Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_get_credentials_with_flags get credentials specified by Fa in_creds-&gt;server and Fa in_creds-&gt;client (the rest of the Fa in_creds structure is ignored) by first looking in the Fa ccache and if doesn&#8217;t exists or is expired, fetch the credential from the KDC using the krbtgt in Fa ccache . The credential is returned in Fa out_creds and should be freed using the function Fn krb5_free_creds . </p>
<p> Valid flags to pass into Fa options argument are: </p>
<dl>
<dt><code>KRB5_GC_CACHED</code></p>
<dd> Only check the Fa ccache , don&#8217;t got out on network to fetch credential.</p>
<dt><code>KRB5_GC_USER_USER</code></p>
<dd> Request a user to user ticket. This option doesn&#8217;t store the resulting user to user credential in the Fa ccache .</p>
<dt><code>KRB5_GC_EXPIRED_OK</code></p>
<dd> returns the credential even if it is expired, default behavior is trying to refetch the credential from the KDC.</dl>
<p> Fa Flags are KDCOptions, note the caller must fill in the bit-field and not use the integer associated structure. </p>
<p> Fn krb5_get_credentials works the same way as Fn krb5_get_credentials_with_flags except that the Fa flags field is missing. </p>
<p> Fn krb5_get_kdc_cred does the same as the functions above, but the caller must fill in all the information andits closer to the wire protocol. </p>
<p> Fn krb5_get_renewed_creds renews a credential given by Fa in_tkt_service (if <code>NULL</code> the default <code>krbtgt</code> using the credential cache Fa ccache . The result is stored in Fa creds and should be freed using Fa krb5_free_creds .</p>
<h2>EXAMPLES</h2>
<p> Here is a example function that get a credential from a credential cache Fa id or the KDC and returns it to the caller. </p>
<pre><code>
#include &lt;krb5.h&gt;
int getcred(krb5_context context, krb5_ccache id, krb5_creds **creds)
{
    krb5_error_code ret;
    krb5_creds in;
    ret = krb5_parse_name(context, "client [at] EXAMPLE.COM",
                          &amp;in.client);
    if (ret)
        krb5_err(context, 1, ret, "krb5_parse_name");
    ret = krb5_parse_name(context, "host/server.example.com [at] EXAMPLE.COM",
                          &amp;in.server);
    if (ret)
        krb5_err(context, 1, ret, "krb5_parse_name");
    ret = krb5_get_credentials(context, 0, id, &amp;in, creds);
    if (ret)
        krb5_err(context, 1, ret, "krb5_get_credentials");
    return 0;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_get_forwarded_creds3, krb5.conf5 </p>
<h2>Index</h2>
