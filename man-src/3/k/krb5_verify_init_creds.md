---
title: "krb5_verify_init_creds(3)"
name: "krb5_verify_init_creds"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_verify_init_creds/"
description: "krb5_verify_init_creds_opt_init krb5_verify_init_creds_opt_set_ap_req_nofail krb5_verify_init_creds – verifies a credential cache is correct by using a local keytab"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_verify_init_creds_opt_init</code> <code>krb5_verify_init_creds_opt_set_ap_req_nofail</code> <code>krb5_verify_init_creds</code> &#8211; verifies a credential cache is correct by using a local keytab </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> <code>struct krb5_verify_init_creds_opt;</code> Ft void Fo krb5_verify_init_creds_opt_init Fa krb5_verify_init_creds_opt *options Fc Ft void Fo krb5_verify_init_creds_opt_set_ap_req_nofail Fa krb5_verify_init_creds_opt *options Fa int ap_req_nofail Fc Ft krb5_error_code Fo krb5_verify_init_creds Fa krb5_context context Fa krb5_creds *creds Fa krb5_principal ap_req_server Fa krb5_ccache *ccache Fa krb5_verify_init_creds_opt *options Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>krb5_verify_init_creds</code> function verifies the initial tickets with the local keytab to make sure the response of the KDC was spoof-ed. </p>
<p> <code>krb5_verify_init_creds</code> will use principal Fa ap_req_server from the local keytab, if <code>NULL</code> is passed in, the code will guess the local hostname and use that to form host/hostname/GUESSED-REALM-FOR-HOSTNAME. Fa creds is the credential that <code>krb5_verify_init_creds</code> should verify. If Fa ccache is given Fn krb5_verify_init_creds stores all credentials it fetched from the KDC there, otherwise it will use a memory credential cache that is destroyed when done. </p>
<p> Fn krb5_verify_init_creds_opt_init cleans the the structure, must be used before trying to pass it in to Fn krb5_verify_init_creds . </p>
<p> Fn krb5_verify_init_creds_opt_set_ap_req_nofail controls controls the behavior if Fa ap_req_server doesn&#8217;t exists in the local keytab or in the KDC&#8217;s database, if it&#8217;s true, the error will be ignored. Note that this use is possible insecure.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_get_init_creds3, krb5_verify_user3, krb5.conf5 </p>
<h2>Index</h2>
