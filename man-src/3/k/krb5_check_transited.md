---
title: "krb5_check_transited(3)"
name: "krb5_check_transited"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_check_transited/"
description: "krb5_check_transited krb5_check_transited_realms krb5_domain_x500_decode krb5_domain_x500_encode – realm transit verification and encoding/decoding functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_check_transited</code> <code>krb5_check_transited_realms</code> <code>krb5_domain_x500_decode</code> <code>krb5_domain_x500_encode</code> &#8211; realm transit verification and encoding/decoding functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_check_transited Fa krb5_context context Fa krb5_const_realm client_realm Fa krb5_const_realm server_realm Fa krb5_realm *realms Fa int num_realms Fa int *bad_realm Fc Ft krb5_error_code Fo krb5_check_transited_realms Fa krb5_context context Fa const char *const *realms Fa int num_realms Fa int *bad_realm Fc Ft krb5_error_code Fo krb5_domain_x500_decode Fa krb5_context context Fa krb5_data tr Fa char ***realms Fa int *num_realms Fa const char *client_realm Fa const char *server_realm Fc Ft krb5_error_code Fo krb5_domain_x500_encode Fa char **realms Fa int num_realms Fa krb5_data *encoding Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_check_transited checks the path from Fa client_realm to Fa server_realm where Fa realms and Fa num_realms is the realms between them. If the function returns an error value, Fa bad_realm will be set to the realm in the list causing the error. Fn krb5_check_transited is used internally by the KDC and libkrb5 and should not be called by client applications. </p>
<p> Fn krb5_check_transited_realms is deprecated. </p>
<p> Fn krb5_domain_x500_encode and Fn krb5_domain_x500_decode encodes and decodes the realm names in the X500 format that Kerberos uses to describe the transited realms in krbtgts.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5.conf5 </p>
<h2>Index</h2>
