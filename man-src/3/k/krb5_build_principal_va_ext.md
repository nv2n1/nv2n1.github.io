---
title: "krb5_build_principal_va_ext(3)"
name: "krb5_build_principal_va_ext"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_build_principal_va_ext/"
description: "krb5_get_default_principal krb5_principal krb5_build_principal krb5_build_principal_ext krb5_build_principal_va krb5_build_principal_va_ext krb5_copy_principal krb5_free_principal krb5_make_princip..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_default_principal</code> <code>krb5_principal</code> <code>krb5_build_principal</code> <code>krb5_build_principal_ext</code> <code>krb5_build_principal_va</code> <code>krb5_build_principal_va_ext</code> <code>krb5_copy_principal</code> <code>krb5_free_principal</code> <code>krb5_make_principal</code> <code>krb5_parse_name</code> <code>krb5_parse_name_flags</code> <code>krb5_parse_nametype</code> <code>krb5_princ_set_realm</code> <code>krb5_principal_compare</code> <code>krb5_principal_compare_any_realm</code> <code>krb5_principal_get_comp_string</code> <code>krb5_principal_get_realm</code> <code>krb5_principal_get_type</code> <code>krb5_principal_match</code> <code>krb5_principal_set_type</code> <code>krb5_realm_compare</code> <code>krb5_sname_to_principal</code> <code>krb5_sock_to_principal</code> <code>krb5_unparse_name</code> <code>krb5_unparse_name_flags</code> <code>krb5_unparse_name_fixed</code> <code>krb5_unparse_name_fixed_flags</code> <code>krb5_unparse_name_fixed_short</code> <code>krb5_unparse_name_short</code> &#8211; Kerberos 5 principal handling functions </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> <code>krb5_principal</code> Ft void Fn krb5_free_principal krb5_context context krb5_principal principal Ft krb5_error_code Fn krb5_parse_name krb5_context context const char *name krb5_principal *principal Ft krb5_error_code Fn krb5_parse_name_flags krb5_context context const char *name int flags krb5_principal *principal Ft krb5_error_code Fn krb5_unparse_name krb5_context context krb5_const_principal principal char **name Ft krb5_error_code Fn krb5_unparse_name_flags krb5_context context krb5_const_principal principal int flags char **name Ft krb5_error_code Fn krb5_unparse_name_fixed krb5_context context krb5_const_principal principal char *name size_t len Ft krb5_error_code Fn krb5_unparse_name_fixed_flags krb5_context context krb5_const_principal principal int flags char *name size_t len Ft krb5_error_code Fn krb5_unparse_name_short krb5_context context krb5_const_principal principal char **name Ft krb5_error_code Fn krb5_unparse_name_fixed_short krb5_context context krb5_const_principal principal char *name size_t len Ft void Fn krb5_princ_set_realm krb5_context context krb5_principal principal krb5_realm *realm Ft krb5_error_code Fn krb5_build_principal krb5_context context krb5_principal *principal int rlen krb5_const_realm realm &#8230; Ft krb5_error_code Fn krb5_build_principal_va krb5_context context krb5_principal *principal int rlen krb5_const_realm realm va_list ap Ft krb5_error_code Fn krb5_build_principal_ext krb5_context context krb5_principal *principal int rlen krb5_const_realm realm &#8230; Ft krb5_error_code Fn krb5_build_principal_va_ext krb5_context context krb5_principal *principal int rlen krb5_const_realm realm va_list ap Ft krb5_error_code Fn krb5_make_principal krb5_context context krb5_principal *principal krb5_const_realm realm &#8230; Ft krb5_error_code Fn krb5_copy_principal krb5_context context krb5_const_principal inprinc krb5_principal *outprinc Ft krb5_boolean Fn krb5_principal_compare krb5_context context krb5_const_principal princ1 krb5_const_principal princ2 Ft krb5_boolean Fn krb5_principal_compare_any_realm krb5_context context krb5_const_principal princ1 krb5_const_principal princ2 Ft const char * Fn krb5_principal_get_comp_string krb5_context context krb5_const_principal principal unsigned int component Ft const char * Fn krb5_principal_get_realm krb5_context context krb5_const_principal principal Ft int Fn krb5_principal_get_type krb5_context context krb5_const_principal principal Ft krb5_boolean Fn krb5_principal_match krb5_context context krb5_const_principal principal krb5_const_principal pattern Ft void Fn krb5_principal_set_type krb5_context context krb5_principal principal int type Ft krb5_boolean Fn krb5_realm_compare krb5_context context krb5_const_principal princ1 krb5_const_principal princ2 Ft krb5_error_code Fn krb5_sname_to_principal krb5_context context const char *hostname const char *sname int32_t type krb5_principal *ret_princ Ft krb5_error_code Fn krb5_sock_to_principal krb5_context context int socket const char *sname int32_t type krb5_principal *principal Ft krb5_error_code Fn krb5_get_default_principal krb5_context context krb5_principal *princ Ft krb5_error_code Fn krb5_parse_nametype krb5_context context const char *str int32_t *type</p>
<h2>DESCRIPTION</h2>
<p> <code>krb5_principal</code> holds the name of a user or service in Kerberos. </p>
<p> A principal has two parts, a <code>PrincipalName</code> and a <code>realm</code> The PrincipalName consists of one or more components. In printed form, the components are separated by /. The PrincipalName also has a name-type. </p>
<p> Examples of a principal are <code>nisse/root [at] EXAMPLE.COM</code> and <code>host/datan.kth.se [at] KTH.SE</code> Fn krb5_parse_name and Fn krb5_parse_name_flags passes a principal name in Fa name to the kerberos principal structure. Fn krb5_parse_name_flags takes an extra Fa flags argument the following flags can be passed in</p>
<dl>
<dt><code>KRB5_PRINCIPAL_PARSE_NO_REALM</code></p>
<dd> requires the input string to be without a realm, and no realm is stored in the Fa principal return argument.</p>
<dt><code>KRB5_PRINCIPAL_PARSE_REQUIRE_REALM</code></p>
<dd> requires the input string to with a realm.</dl>
<p> Fn krb5_unparse_name and Fn krb5_unparse_name_flags prints the principal Fa princ to the string Fa name . Fa name should be freed with <a href="/docs/linux/man/3-free/">free</a>(3). To the Fa flags argument the following flags can be passed in</p>
<dl>
<dt><code>KRB5_PRINCIPAL_UNPARSE_SHORT</code></p>
<dd> no realm if the realm is one of the local realms.</p>
<dt><code>KRB5_PRINCIPAL_UNPARSE_NO_REALM</code></p>
<dd> never include any realm in the principal name.</p>
<dt><code>KRB5_PRINCIPAL_UNPARSE_DISPLAY</code></p>
<dd> don&#8217;t quote</dl>
<p> On failure Fa name is set to <code>NULL</code> Fn krb5_unparse_name_fixed and Fn krb5_unparse_name_fixed_flags behaves just like Fn krb5_unparse , but instead unparses the principal into a fixed size buffer. </p>
<p> Fn krb5_unparse_name_short just returns the principal without the realm if the principal is in the default realm. If the principal isn&#8217;t, the full name is returned. Fn krb5_unparse_name_fixed_short works just like Fn krb5_unparse_name_short but on a fixed size buffer. </p>
<p> Fn krb5_build_principal builds a principal from the realm Fa realm that has the length Fa rlen . The following arguments form the components of the principal. The list of components is terminated with <code>NULL</code> </p>
<p> Fn krb5_build_principal_va works like Fn krb5_build_principal using vargs. </p>
<p> Fn krb5_build_principal_ext and Fn krb5_build_principal_va_ext take a list of length-value pairs, the list is terminated with a zero length. </p>
<p> Fn krb5_make_principal works the same way as Fn krb5_build_principal , except it figures out the length of the realm itself. </p>
<p> Fn krb5_copy_principal makes a copy of a principal. The copy needs to be freed with Fn krb5_free_principal . </p>
<p> Fn krb5_principal_compare compares the two principals, including realm of the principals and returns <code>TRUE</code> if they are the same and <code>FALSE</code> if not. </p>
<p> Fn krb5_principal_compare_any_realm works the same way as Fn krb5_principal_compare but doesn&#8217;t compare the realm component of the principal. </p>
<p> Fn krb5_realm_compare compares the realms of the two principals and returns <code>TRUE</code> is they are the same, and <code>FALSE</code> if not. </p>
<p> Fn krb5_principal_match matches a Fa principal against a Fa pattern . The pattern is a globbing expression, where each component (separated by /) is matched against the corresponding component of the principal. </p>
<p> The Fn krb5_principal_get_realm and Fn krb5_principal_get_comp_string functions return parts of the Fa principal , either the realm or a specific component. Both functions return string pointers to data inside the principal, so they are valid only as long as the principal exists. </p>
<p> The Fa component argument to Fn krb5_principal_get_comp_string is the index of the component to return, from zero to the total number of components minus one. If the index is out of range <code>NULL</code> is returned. </p>
<p> Fn krb5_principal_get_realm and Fn krb5_principal_get_comp_string are replacements for Fn krb5_princ_component and related macros, described as internal in the MIT API specification. Unlike the macros, these functions return strings, not <code>krb5_data</code> A reason to return <code>krb5_data</code> was that it was believed that principal components could contain binary data, but this belief was unfounded, and it has been decided that principal components are infact UTF8, so it&#8217;s safe to use zero terminated strings. </p>
<p> It&#8217;s generally not necessary to look at the components of a principal. </p>
<p> Fn krb5_principal_get_type and Fn krb5_principal_set_type get and sets the name type for a principal. Name type handling is tricky and not often needed, don&#8217;t use this unless you know what you do. </p>
<p> Fn krb5_sname_to_principal and Fn krb5_sock_to_principal are for easy creation of &#8220;service&#8221; principals that can, for instance, be used to lookup a key in a keytab. For both functions the Fa sname parameter will be used for the first component of the created principal. If Fa sname is <code>NULL</code> &#8220;host&#8221; will be used instead. </p>
<p> Fn krb5_sname_to_principal will use the passed Fa hostname for the second component. If Fa type is <code>KRB5_NT_SRV_HST</code> this name will be looked up with Fn gethostbyname . If Fa hostname is <code>NULL</code> the local hostname will be used. </p>
<p> Fn krb5_sock_to_principal will use the &#8220;sockname&#8221; of the passed Fa socket , which should be a bound <code>AF_INET</code> or <code>AF_INET6</code> socket. There must be a mapping between the address and &#8220;sockname&#8221; The function may try to resolve the name in DNS. </p>
<p> Fn krb5_get_default_principal tries to find out what&#8217;s a reasonable default principal by looking at the environment it is running in. </p>
<p> Fn krb5_parse_nametype parses and returns the name type integer value in Fa type . On failure the function returns an error code and set the error string.</p>
<h2>SEE ALSO</h2>
<p> krb5_425_conv_principal3, krb5_config3, krb5.conf5</p>
<h2>BUGS</h2>
<p> You can not have a NUL in a component in some of the variable argument functions above. Until someone can give a good example of where it would be a good idea to have NUL&#8217;s in a component, this will not be fixed. </p>
<h2>Index</h2>
