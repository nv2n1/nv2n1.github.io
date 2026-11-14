---
title: "krb5_set_password_using_ccache(3)"
name: "krb5_set_password_using_ccache"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_set_password_using_ccache/"
description: "krb5_change_password krb5_set_password krb5_set_password_using_ccache krb5_passwd_result_to_string – change password functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_change_password</code> <code>krb5_set_password</code> <code>krb5_set_password_using_ccache</code> <code>krb5_passwd_result_to_string</code> &#8211; change password functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_change_password Fa krb5_context context Fa krb5_creds *creds Fa char *newpw Fa int *result_code Fa krb5_data *result_code_string Fa krb5_data *result_string Fc Ft krb5_error_code Fo krb5_set_password Fa krb5_context context Fa krb5_creds *creds Fa char *newpw Fa krb5_principal targprinc Fa int *result_code Fa krb5_data *result_code_string Fa krb5_data *result_string Fc Ft krb5_error_code Fo krb5_set_password_using_ccache Fa krb5_context context Fa krb5_ccache ccache Fa char *newpw Fa krb5_principal targprinc Fa int *result_code Fa krb5_data *result_code_string Fa krb5_data *result_string Fc Ft const char * Fo krb5_passwd_result_to_string Fa krb5_context context Fa int result Fc</p>
<h2>DESCRIPTION</h2>
<p> These functions change the password for a given principal. </p>
<p> Fn krb5_set_password and Fn krb5_set_password_using_ccache are the newer of the three functions, and use a newer version of the protocol (and also fall back to the older set-password protocol if the newer protocol doesn&#8217;t work). </p>
<p> Fn krb5_change_password sets the password Fa newpasswd for the client principal in Fa creds . The server principal of creds must be <code>kadmin/changepw</code> </p>
<p> Fn krb5_set_password and Fn krb5_set_password_using_ccache change the password for the principal Fa targprinc . </p>
<p> Fn krb5_set_password requires that the credential for <code>kadmin/changepw [at] REALM</code> is in Fa creds . If the user caller isn&#8217;t an administrator, this credential needs to be an initial credential, see krb5_get_init_creds3 how to get such credentials. </p>
<p> Fn krb5_set_password_using_ccache will get the credential from Fa ccache . </p>
<p> If Fa targprinc is <code>NULL</code> Fn krb5_set_password_using_ccache uses the the default principal in Fa ccache and Fn krb5_set_password uses the global the default principal. </p>
<p> All three functions return an error in Fa result_code and maybe an error string to print in Fa result_string . </p>
<p> Fn krb5_passwd_result_to_string returns an human readable string describing the error code in Fa result_code from the Fn krb5_set_password functions.</p>
<h2>SEE ALSO</h2>
<p> krb5_ccache3, krb5_init_context3 </p>
<h2>Index</h2>
