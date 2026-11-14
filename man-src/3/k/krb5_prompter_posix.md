---
title: "krb5_prompter_posix(3)"
name: "krb5_prompter_posix"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_prompter_posix/"
description: "krb5_get_init_creds krb5_get_init_creds_keytab krb5_get_init_creds_opt krb5_get_init_creds_opt_alloc krb5_get_init_creds_opt_free krb5_get_init_creds_opt_init krb5_get_init_creds_opt_set_address_li..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_init_creds</code> <code>krb5_get_init_creds_keytab</code> <code>krb5_get_init_creds_opt</code> <code>krb5_get_init_creds_opt_alloc</code> <code>krb5_get_init_creds_opt_free</code> <code>krb5_get_init_creds_opt_init</code> <code>krb5_get_init_creds_opt_set_address_list</code> <code>krb5_get_init_creds_opt_set_addressless</code> <code>krb5_get_init_creds_opt_set_anonymous</code> <code>krb5_get_init_creds_opt_set_default_flags</code> <code>krb5_get_init_creds_opt_set_etype_list</code> <code>krb5_get_init_creds_opt_set_forwardable</code> <code>krb5_get_init_creds_opt_set_pa_password</code> <code>krb5_get_init_creds_opt_set_paq_request</code> <code>krb5_get_init_creds_opt_set_preauth_list</code> <code>krb5_get_init_creds_opt_set_proxiable</code> <code>krb5_get_init_creds_opt_set_renew_life</code> <code>krb5_get_init_creds_opt_set_salt</code> <code>krb5_get_init_creds_opt_set_tkt_life</code> <code>krb5_get_init_creds_opt_set_canonicalize</code> <code>krb5_get_init_creds_opt_set_win2k</code> <code>krb5_get_init_creds_password</code> <code>krb5_prompt</code> <code>krb5_prompter_posix</code> &#8211; Kerberos 5 initial authentication functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> Ft krb5_get_init_creds_opt; </p>
<p> Ft krb5_error_code Fo krb5_get_init_creds_opt_alloc Fa krb5_context context Fa krb5_get_init_creds_opt **opt Fc Ft void Fo krb5_get_init_creds_opt_free Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fc Ft void Fo krb5_get_init_creds_opt_init Fa krb5_get_init_creds_opt *opt Fc Ft void Fo krb5_get_init_creds_opt_set_address_list Fa krb5_get_init_creds_opt *opt Fa krb5_addresses *addresses Fc Ft void Fo krb5_get_init_creds_opt_set_addressless Fa krb5_get_init_creds_opt *opt Fa krb5_boolean addressless Fc Ft void Fo krb5_get_init_creds_opt_set_anonymous Fa krb5_get_init_creds_opt *opt Fa int anonymous Fc Ft void Fo krb5_get_init_creds_opt_set_default_flags Fa krb5_context context Fa const char *appname Fa krb5_const_realm realm Fa krb5_get_init_creds_opt *opt Fc Ft void Fo krb5_get_init_creds_opt_set_etype_list Fa krb5_get_init_creds_opt *opt Fa krb5_enctype *etype_list Fa int etype_list_length Fc Ft void Fo krb5_get_init_creds_opt_set_forwardable Fa krb5_get_init_creds_opt *opt Fa int forwardable Fc Ft krb5_error_code Fo krb5_get_init_creds_opt_set_pa_password Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fa const char *password Fa krb5_s2k_proc key_proc Fc Ft krb5_error_code Fo krb5_get_init_creds_opt_set_paq_request Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fa krb5_boolean req_pac Fc Ft krb5_error_code Fo krb5_get_init_creds_opt_set_pkinit Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fa const char *cert_file Fa const char *key_file Fa const char *x509_anchors Fa int flags Fa char *password Fc Ft void Fo krb5_get_init_creds_opt_set_preauth_list Fa krb5_get_init_creds_opt *opt Fa krb5_preauthtype *preauth_list Fa int preauth_list_length Fc Ft void Fo krb5_get_init_creds_opt_set_proxiable Fa krb5_get_init_creds_opt *opt Fa int proxiable Fc Ft void Fo krb5_get_init_creds_opt_set_renew_life Fa krb5_get_init_creds_opt *opt Fa krb5_deltat renew_life Fc Ft void Fo krb5_get_init_creds_opt_set_salt Fa krb5_get_init_creds_opt *opt Fa krb5_data *salt Fc Ft void Fo krb5_get_init_creds_opt_set_tkt_life Fa krb5_get_init_creds_opt *opt Fa krb5_deltat tkt_life Fc Ft krb5_error_code Fo krb5_get_init_creds_opt_set_canonicalize Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fa krb5_boolean req Fc Ft krb5_error_code Fo krb5_get_init_creds_opt_set_win2k Fa krb5_context context Fa krb5_get_init_creds_opt *opt Fa krb5_boolean req Fc Ft krb5_error_code Fo krb5_get_init_creds Fa krb5_context context Fa krb5_creds *creds Fa krb5_principal client Fa krb5_prompter_fct prompter Fa void *prompter_data Fa krb5_deltat start_time Fa const char *in_tkt_service Fa krb5_get_init_creds_opt *options Fc Ft krb5_error_code Fo krb5_get_init_creds_password Fa krb5_context context Fa krb5_creds *creds Fa krb5_principal client Fa const char *password Fa krb5_prompter_fct prompter Fa void *prompter_data Fa krb5_deltat start_time Fa const char *in_tkt_service Fa krb5_get_init_creds_opt *in_options Fc Ft krb5_error_code Fo krb5_get_init_creds_keytab Fa krb5_context context Fa krb5_creds *creds Fa krb5_principal client Fa krb5_keytab keytab Fa krb5_deltat start_time Fa const char *in_tkt_service Fa krb5_get_init_creds_opt *options Fc Ft int Fo krb5_prompter_posix Fa krb5_context context Fa void *data Fa const char *name Fa const char *banner Fa int num_prompts Fa krb5_prompt prompts[] Fc</p>
<h2>DESCRIPTION</h2>
<p> Getting initial credential ticket for a principal. That may include changing an expired password, and doing preauthentication. This interface that replaces the deprecated Fa krb5_in_tkt and Fa krb5_in_cred functions. </p>
<p> If you only want to verify a username and password, consider using krb5_verify_user3 instead, since it also verifies that initial credentials with using a keytab to make sure the response was from the KDC. </p>
<p> First a <code>krb5_get_init_creds_opt</code> structure is initialized with Fn krb5_get_init_creds_opt_alloc or Fn krb5_get_init_creds_opt_init . Fn krb5_get_init_creds_opt_alloc allocates a extendible structures that needs to be freed with Fn krb5_get_init_creds_opt_free . The structure may be modified by any of the Fn krb5_get_init_creds_opt_set functions to change request parameters and authentication information. </p>
<p> If the caller want to use the default options, <code>NULL</code> can be passed instead. </p>
<p> The the actual request to the KDC is done by any of the Fn krb5_get_init_creds , Fn krb5_get_init_creds_password , or Fn krb5_get_init_creds_keytab functions. Fn krb5_get_init_creds is the least specialized function and can, with the right in data, behave like the latter two. The latter two are there for compatibility with older releases and they are slightly easier to use. </p>
<p> <code>krb5_prompt</code> is a structure containing the following elements: </p>
<pre><code>
typedef struct {
    const char *prompt;
    int hidden;
    krb5_data *reply;
    krb5_prompt_type type
} krb5_prompt;
</code></pre>
<p> Fa prompt is the prompt that should shown to the user If Fa hidden is set, the prompter function shouldn&#8217;t echo the output to the display device. Fa reply must be preallocated; it will not be allocated by the prompter function. Possible values for the Fa type element are: </p>
<dl>
<dt><code>KRB5_PROMPT_TYPE_PASSWORD</code></p>
<dd>
<dt><code>KRB5_PROMPT_TYPE_NEW_PASSWORD</code></p>
<dd>
<dt><code>KRB5_PROMPT_TYPE_NEW_PASSWORD_AGAIN</code></p>
<dd>
<dt><code>KRB5_PROMPT_TYPE_PREAUTH</code></p>
<dd>
<dt><code>KRB5_PROMPT_TYPE_INFO</code></p>
<dd></dl>
<p> Fn krb5_prompter_posix is the default prompter function in a POSIX environment. It matches the Fa krb5_prompter_fct and can be used in the Fa krb5_get_init_creds functions. Fn krb5_prompter_posix doesn&#8217;t require Fa prompter_data. </p>
<p> If the Fa start_time is zero, then the requested ticket will be valid beginning immediately. Otherwise, the Fa start_time indicates how far in the future the ticket should be postdated. </p>
<p> If the Fa in_tkt_service name is <code>non-NULL</code> that principal name will be used as the server name for the initial ticket request. The realm of the name specified will be ignored and will be set to the realm of the client name. If no in_tkt_service name is specified, krbtgt/CLIENT-REALM [at] CLIENT-REALM will be used. </p>
<p> For the rest of arguments, a configuration or library default will be used if no value is specified in the options structure. </p>
<p> Fn krb5_get_init_creds_opt_set_address_list sets the list of Fa addresses that is should be stored in the ticket. </p>
<p> Fn krb5_get_init_creds_opt_set_addressless controls if the ticket is requested with addresses or not, Fn krb5_get_init_creds_opt_set_address_list overrides this option. </p>
<p> Fn krb5_get_init_creds_opt_set_anonymous make the request anonymous if the Fa anonymous parameter is non-zero. </p>
<p> Fn krb5_get_init_creds_opt_set_default_flags sets the default flags using the configuration file. </p>
<p> Fn krb5_get_init_creds_opt_set_etype_list set a list of enctypes that the client is willing to support in the request. </p>
<p> Fn krb5_get_init_creds_opt_set_forwardable request a forwardable ticket. </p>
<p> Fn krb5_get_init_creds_opt_set_pa_password set the Fa password and Fa key_proc that is going to be used to get a new ticket. Fa password or Fa key_proc can be <code>NULL</code> if the caller wants to use the default values. If the Fa password is unset and needed, the user will be prompted for it. </p>
<p> Fn krb5_get_init_creds_opt_set_paq_request sets the password that is going to be used to get a new ticket. </p>
<p> Fn krb5_get_init_creds_opt_set_preauth_list sets the list of client-supported preauth types. </p>
<p> Fn krb5_get_init_creds_opt_set_proxiable makes the request proxiable. </p>
<p> Fn krb5_get_init_creds_opt_set_renew_life sets the requested renewable lifetime. </p>
<p> Fn krb5_get_init_creds_opt_set_salt sets the salt that is going to be used in the request. </p>
<p> Fn krb5_get_init_creds_opt_set_tkt_life sets requested ticket lifetime. </p>
<p> Fn krb5_get_init_creds_opt_set_canonicalize requests that the KDC canonicalize the client pricipal if possible. </p>
<p> Fn krb5_get_init_creds_opt_set_win2k turns on compatibility with Windows 2000.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_creds3, krb5_verify_user3, krb5.conf5, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
