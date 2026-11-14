---
title: "kadm5_pwcheck(3)"
name: "kadm5_pwcheck"
section: "3"
letter: "k"
url: "/docs/linux/man/3-kadm5_pwcheck/"
description: "krb5_pwcheck kadm5_setup_passwd_quality_check kadm5_add_passwd_quality_verifier kadm5_check_password_quality – Heimdal warning and error functions"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_pwcheck</code> <code>kadm5_setup_passwd_quality_check</code> <code>kadm5_add_passwd_quality_verifier</code> <code>kadm5_check_password_quality</code> &#8211; Heimdal warning and error functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkadm5srv, -lkadm5srv)</p>
<h2>SYNOPSIS</h2>
<p> In kadm5-protos.h In kadm5-pwcheck.h Ft void Fo kadm5_setup_passwd_quality_check Fa krb5_context context Fa const char *check_library Fa const char *check_function Fc Ft krb5_error_code Fo kadm5_add_passwd_quality_verifier Fa krb5_context context Fa const char *check_library Fc Ft const char * Fo kadm5_check_password_quality Fa krb5_context context Fa krb5_principal principal Fa krb5_data *pwd_data Fc Ft int Fo (*kadm5_passwd_quality_check_func) Fa krb5_context context Fa krb5_principal principal Fa krb5_data *password Fa const char *tuning Fa char *message Fa size_t length Fc</p>
<h2>DESCRIPTION</h2>
<p> These functions perform the quality check for the heimdal database library. </p>
<p> There are two versions of the shared object API; the old version (0) is deprecated, but still supported. The new version (1) supports multiple password quality checking policies in the same shared object. See below for details. </p>
<p> The password quality checker will run all policies that are configured by the user. If any policy rejects the password, the password will be rejected. </p>
<p> Policy names are of the form `module-name:policy-name&#8217; or, if the the policy name is unique enough, just `policy-name&#8217;</p>
<h2>IMPLEMENTING A PASSWORD QUALITY CHECKING SHARED OBJECT</h2>
<p> (This refers to the version 1 API only.) </p>
<p> Module shared objects may conveniently be compiled and linked with <a href="/docs/linux/man/1-libtool/">libtool</a>(1). An object needs to export a symbol called `kadm5_password_verifier&#8217; of the type Ft struct kadm5_pw_policy_verifier . </p>
<p> Its Ft name and Ft vendor fields should contain the obvious information. Ft name must match the `module-name&#8217; portion of the policy name (the part before the colon), if the policy name contains a colon, or the policy will not be run. Ft version should be <code>KADM5_PASSWD_VERSION_V1</code> </p>
<p> Ft funcs contains an array of Ft struct kadm5_pw_policy_check_func structures that is terminated with an entry whose Ft name component is <code>NULL</code> The Ft name field of the array must match the `policy-name&#8217; portion of a policy name (the part after the colon, or the complete policy name if there is no colon) specified by the user or the policy will not be run. The Ft func fields of the array elements are functions that are exported by the module to be called to check the password. They get the following arguments: the Kerberos context, principal, password, a tuning parameter, and a pointer to a message buffer and its length. The tuning parameter for the quality check function is currently always <code>NULL</code> If the password is acceptable, the function returns zero. Otherwise it returns non-zero and fills in the message buffer with an appropriate explanation.</p>
<h2>RUNNING THE CHECKS</h2>
<p> <code>kadm5_setup_passwd_quality_check</code> sets up type 0 checks. It sets up all type 0 checks defined in krb5.conf5 if called with the last two arguments null. </p>
<p> <code>kadm5_add_passwd_quality_verifier</code> sets up type 1 checks. It sets up all type 1 tests defined in krb5.conf5 if called with a null second argument. <code>kadm5_check_password_quality</code> runs the checks in the order in which they are defined in krb5.conf5 and the order in which they occur in a module&#8217;s Ft funcs array until one returns non-zero.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-libtool/">libtool</a>(1), <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5.conf5 </p>
<h2>Index</h2>
