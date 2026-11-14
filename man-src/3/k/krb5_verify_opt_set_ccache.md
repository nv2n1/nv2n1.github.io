---
title: "krb5_verify_opt_set_ccache(3)"
name: "krb5_verify_opt_set_ccache"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_verify_opt_set_ccache/"
description: "krb5_verify_user krb5_verify_user_lrealm krb5_verify_user_opt krb5_verify_opt_init krb5_verify_opt_alloc krb5_verify_opt_free krb5_verify_opt_set_ccache krb5_verify_opt_set_flags krb5_verify_opt_se..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_verify_user</code> <code>krb5_verify_user_lrealm</code> <code>krb5_verify_user_opt</code> <code>krb5_verify_opt_init</code> <code>krb5_verify_opt_alloc</code> <code>krb5_verify_opt_free</code> <code>krb5_verify_opt_set_ccache</code> <code>krb5_verify_opt_set_flags</code> <code>krb5_verify_opt_set_service</code> <code>krb5_verify_opt_set_secure</code> <code>krb5_verify_opt_set_keytab</code> &#8211; Heimdal password verifying functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fn krb5_verify_user krb5_context context krb5_principal principal krb5_ccache ccache const char *password krb5_boolean secure const char *service Ft krb5_error_code Fn krb5_verify_user_lrealm krb5_context context krb5_principal principal krb5_ccache ccache const char *password krb5_boolean secure const char *service Ft void Fn krb5_verify_opt_init krb5_verify_opt *opt Ft void Fn krb5_verify_opt_alloc krb5_verify_opt **opt Ft void Fn krb5_verify_opt_free krb5_verify_opt *opt Ft void Fn krb5_verify_opt_set_ccache krb5_verify_opt *opt krb5_ccache ccache Ft void Fn krb5_verify_opt_set_keytab krb5_verify_opt *opt krb5_keytab keytab Ft void Fn krb5_verify_opt_set_secure krb5_verify_opt *opt krb5_boolean secure Ft void Fn krb5_verify_opt_set_service krb5_verify_opt *opt const char *service Ft void Fn krb5_verify_opt_set_flags krb5_verify_opt *opt unsigned int flags Ft krb5_error_code Fo krb5_verify_user_opt Fa krb5_context context Fa krb5_principal principal Fa const char *password Fa krb5_verify_opt *opt Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>krb5_verify_user</code> function verifies the password supplied by a user. The principal whose password will be verified is specified in Fa principal . New tickets will be obtained as a side-effect and stored in Fa ccache (if <code>NULL</code> the default ccache is used). Fn krb5_verify_user will call Fn krb5_cc_initialize on the given Fa ccache , so Fa ccache must only initialized with Fn krb5_cc_resolve or Fn krb5_cc_gen_new . If the password is not supplied in Fa password (and is given as <code>NULL</code> the user will be prompted for it. If Fa secure the ticket will be verified against the locally stored service key Fa service (by default `host&#8217; if given as <code>NULL</code> ). </p>
<p> The Fn krb5_verify_user_lrealm function does the same, except that it ignores the realm in Fa principal and tries all the local realms (see krb5.conf5). After a successful return, the principal is set to the authenticated realm. If the call fails, the principal will not be meaningful, and should only be freed with krb5_free_principal3. </p>
<p> Fn krb5_verify_opt_alloc and Fn krb5_verify_opt_free allocates and frees a <code>krb5_verify_opt</code> You should use the the alloc and free function instead of allocation the structure yourself, this is because in a future release the structure wont be exported. </p>
<p> Fn krb5_verify_opt_init resets all opt to default values. </p>
<p> None of the krb5_verify_opt_set function makes a copy of the data structure that they are called with. It&#8217;s up the caller to free them after the Fn krb5_verify_user_opt is called. </p>
<p> Fn krb5_verify_opt_set_ccache sets the Fa ccache that user of Fa opt will use. If not set, the default credential cache will be used. </p>
<p> Fn krb5_verify_opt_set_keytab sets the Fa keytab that user of Fa opt will use. If not set, the default keytab will be used. </p>
<p> Fn krb5_verify_opt_set_secure if Fa secure if true, the password verification will require that the ticket will be verified against the locally stored service key. If not set, default value is true. </p>
<p> Fn krb5_verify_opt_set_service sets the Fa service principal that user of Fa opt will use. If not set, the `host&#8217; service will be used. </p>
<p> Fn krb5_verify_opt_set_flags sets Fa flags that user of Fa opt will use. If the flag <code>KRB5_VERIFY_LREALMS</code> is used, the Fa principal will be modified like Fn krb5_verify_user_lrealm modifies it. </p>
<p> Fn krb5_verify_user_opt function verifies the Fa password supplied by a user. The principal whose password will be verified is specified in Fa principal . Options the to the verification process is pass in in Fa opt .</p>
<h2>EXAMPLES</h2>
<p> Here is a example program that verifies a password. it uses the `host/`hostname`&#8217; service principal in krb5.keytab </p>
<pre><code>
#include &lt;krb5.h&gt;
int main(int argc, char **argv)
{
    char *user;
    krb5_error_code error;
    krb5_principal princ;
    krb5_context context;
    if (argc != 2)
        errx(1, "usage: verify_passwd &lt;principal-name&gt;");
    user = argv[1];
    if (krb5_init_context(&amp;context) &lt; 0)
        errx(1, "krb5_init_context");
    if ((error = krb5_parse_name(context, user, &amp;princ)) != 0)
        krb5_err(context, 1, error, "krb5_parse_name");
    error = krb5_verify_user(context, princ, NULL, NULL, TRUE, NULL);
    if (error)
        krb5_err(context, 1, error, "krb5_verify_user");
    return 0;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> krb5_cc_gen_new3, krb5_cc_initialize3, krb5_cc_resolve3, krb5_err3, krb5_free_principal3, krb5_init_context3, krb5_kt_default3, krb5.conf5 </p>
<h2>Index</h2>
