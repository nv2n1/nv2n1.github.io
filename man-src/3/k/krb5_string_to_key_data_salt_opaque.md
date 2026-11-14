---
title: "krb5_string_to_key_data_salt_opaque(3)"
name: "krb5_string_to_key_data_salt_opaque"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_string_to_key_data_salt_opaque/"
description: "krb5_string_to_key krb5_string_to_key_data krb5_string_to_key_data_salt krb5_string_to_key_data_salt_opaque krb5_string_to_key_salt krb5_string_to_key_salt_opaque krb5_get_pw_salt krb5_free_salt – ..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_string_to_key</code> <code>krb5_string_to_key_data</code> <code>krb5_string_to_key_data_salt</code> <code>krb5_string_to_key_data_salt_opaque</code> <code>krb5_string_to_key_salt</code> <code>krb5_string_to_key_salt_opaque</code> <code>krb5_get_pw_salt</code> <code>krb5_free_salt</code> &#8211; turns a string to a Kerberos key </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_string_to_key Fa krb5_context context Fa krb5_enctype enctype Fa const char *password Fa krb5_principal principal Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_string_to_key_data Fa krb5_context context Fa krb5_enctype enctype Fa krb5_data password Fa krb5_principal principal Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_string_to_key_data_salt Fa krb5_context context Fa krb5_enctype enctype Fa krb5_data password Fa krb5_salt salt Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_string_to_key_data_salt_opaque Fa krb5_context context Fa krb5_enctype enctype Fa krb5_data password Fa krb5_salt salt Fa krb5_data opaque Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_string_to_key_salt Fa krb5_context context Fa krb5_enctype enctype Fa const char *password Fa krb5_salt salt Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_string_to_key_salt_opaque Fa krb5_context context Fa krb5_enctype enctype Fa const char *password Fa krb5_salt salt Fa krb5_data opaque Fa krb5_keyblock *key Fc Ft krb5_error_code Fo krb5_get_pw_salt Fa krb5_context context Fa krb5_const_principal principal Fa krb5_salt *salt Fc Ft krb5_error_code Fo krb5_free_salt Fa krb5_context context Fa krb5_salt salt Fc</p>
<h2>DESCRIPTION</h2>
<p> The string to key functions convert a string to a kerberos key. </p>
<p> Fn krb5_string_to_key_data_salt_opaque is the function that does all the work, the rest of the functions are just wrappers around Fn krb5_string_to_key_data_salt_opaque that calls it with default values. </p>
<p> Fn krb5_string_to_key_data_salt_opaque transforms the Fa password with the given salt-string Fa salt and the opaque, encryption type specific parameter Fa opaque to a encryption key Fa key according to the string to key function associated with Fa enctype . </p>
<p> The Fa key should be freed with Fn krb5_free_keyblock_contents . </p>
<p> If one of the functions that doesn&#8217;t take a <code>krb5_salt</code> as it argument Fn krb5_get_pw_salt is used to get the salt value. </p>
<p> Fn krb5_get_pw_salt get the default password salt for a principal, use Fn krb5_free_salt to free the salt when done. </p>
<p> Fn krb5_free_salt frees the content of Fa salt .</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_data3, krb5_keyblock3, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
