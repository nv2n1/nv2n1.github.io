---
title: "krb5_unparse_name_fixed_short(3)"
name: "krb5_unparse_name_fixed_short"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_unparse_name_fixed_short/"
description: "Heimdal Kerberos 5 principal functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 principal functions &#8211; </p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_build_principal</code> (krb5_context, krb5_principal *, int, krb5_const_realm,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_copy_principal</code> (krb5_context, krb5_const_principal, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_free_principal</code> (krb5_context, krb5_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_make_principal</code> (krb5_context, krb5_principal *, krb5_const_realm,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_parse_name</code> (krb5_context, const char *, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_parse_name_flags</code> (krb5_context, const char *, int, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_parse_nametype</code> (krb5_context, const char *, int32_t *)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_principal_compare</code> (krb5_context, krb5_const_principal, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_principal_compare_any_realm</code> (krb5_context, krb5_const_principal, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION unsigned int<br />
 KRB5_LIB_CALL <code>krb5_principal_get_num_comp</code> (krb5_context, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_principal_get_realm</code> (krb5_context, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_principal_get_type</code> (krb5_context, krb5_const_principal) </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_principal_is_gss_hostbased_service</code> (krb5_context, krb5_const_principal) </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_principal_is_krbtgt</code> (krb5_context, krb5_const_principal)&quot; </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_principal_is_lkdc</code> (krb5_context, krb5_const_principal) </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_principal_is_null</code> (krb5_context, krb5_const_principal) </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_principal_is_pku2u</code> (krb5_context, krb5_const_principal) </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_principal_is_root_krbtgt</code> (krb5_context, krb5_const_principal) </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_principal_match</code> (krb5_context, krb5_const_principal, krb5_const_principal)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_principal_set_realm</code> (krb5_context, krb5_principal, krb5_const_realm)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_principal_set_type</code> (krb5_context, krb5_principal, int)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_realm_compare</code> (krb5_context, krb5_const_principal, krb5_const_principal)&quot; </p>
<p> krb5_boolean KRB5_LIB_FUNCTION <code>krb5_realm_is_lkdc</code> (const char *) </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_sname_to_principal</code> (krb5_context, const char *, const char *, int32_t, krb5_principal *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name</code> (krb5_context, krb5_const_principal, char **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name_fixed</code> (krb5_context, krb5_const_principal, char *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name_fixed_flags</code> (krb5_context, krb5_const_principal, int, char *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name_fixed_short</code> (krb5_context, krb5_const_principal, char *, size_t)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name_flags</code> (krb5_context, krb5_const_principal, int, char **)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_unparse_name_short</code> (krb5_context, krb5_const_principal, char **)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_build_principal (krb5_contextcontext, krb5_principal *principal, intrlen, krb5_const_realmrealm, &#8230;)</h3>
<p> Build a principal using vararg style building </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> returned principal<br />
 <i>rlen</i> length of realm<br />
 <i>realm</i> realm name<br />
 <i>&#8230;</i> a list of components ended with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_copy_principal (krb5_contextcontext, krb5_const_principalinprinc, krb5_principal *outprinc)</h3>
<p> Copy a principal </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>inprinc</i> principal to copy<br />
 <i>outprinc</i> copied principal, free with <code>krb5_free_principal()</code></dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_free_principal (krb5_contextcontext, krb5_principalp)</h3>
<p> Frees a Kerberos principal allocated by the library with <code>krb5_parse_name()</code>, <code>krb5_make_principal()</code> or any other related principal functions. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>p</i> a principal to free.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_make_principal (krb5_contextcontext, krb5_principal *principal, krb5_const_realmrealm, &#8230;)</h3>
<p> Build a principal using vararg style building </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> returned principal<br />
 <i>realm</i> realm name<br />
 <i>&#8230;</i> a list of components ended with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_parse_name (krb5_contextcontext, const char *name, krb5_principal *principal)</h3>
<p> Parse a name into a krb5_principal structure </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>name</i> name to parse into a Kerberos principal<br />
 <i>principal</i> returned principal, free with <code>krb5_free_principal()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_parse_name_flags (krb5_contextcontext, const char *name, intflags, krb5_principal *principal)</h3>
<p> Parse a name into a krb5_principal structure, flags controls the behavior. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>name</i> name to parse into a Kerberos principal<br />
 <i>flags</i> flags to control the behavior<br />
 <i>principal</i> returned principal, free with <code>krb5_free_principal()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_parse_nametype (krb5_contextcontext, const char *str, int32_t *nametype)</h3>
<p> Parse nametype string and return a nametype integer</p>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_principal_compare (krb5_contextcontext, krb5_const_principalprinc1, krb5_const_principalprinc2)</h3>
<p> Compares the two principals, including realm of the principals and returns TRUE if they are the same and FALSE if not. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>princ1</i> first principal to compare<br />
 <i>princ2</i> second principal to compare</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_principal_compare_any_realm()</code> </p>
<p> <code>krb5_realm_compare()</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_principal_compare_any_realm (krb5_contextcontext, krb5_const_principalprinc1, krb5_const_principalprinc2)</h3>
<p> Return TRUE iff princ1 == princ2 (without considering the realm) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>princ1</i> first principal to compare<br />
 <i>princ2</i> second principal to compare</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> non zero if equal, 0 if not</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_principal_compare()</code> </p>
<p> <code>krb5_realm_compare()</code></dl>
<h3>KRB5_LIB_FUNCTION unsigned int KRB5_LIB_CALL krb5_principal_get_num_comp (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Get number of component is principal. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>principal</i> principal to query</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> number of components in string</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_principal_get_realm (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Get the realm of the principal </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to get the realm for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> realm of the principal, don&#8217;t free or use after krb5_principal is freed</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_principal_get_type (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Get the type of the principal </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to get the type for</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> the type of principal</dl>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_principal_is_gss_hostbased_service (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Returns true iff name is an WELLKNOWN:ORG.H5L.HOSTBASED-SERVICE</p>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_principal_is_krbtgt (krb5_contextcontext, krb5_const_principalp)</h3>
<p> Check if the cname part of the principal is a krbtgt principal</p>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_principal_is_lkdc (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Returns true if name is Kerberos an LKDC realm</p>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_principal_is_null (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Returns true if name is Kerberos NULL name</p>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_principal_is_pku2u (krb5_contextcontext, krb5_const_principalprincipal)</h3>
<p> Returns true if name is Kerberos an LKDC realm</p>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_principal_is_root_krbtgt (krb5_contextcontext, krb5_const_principalp)</h3>
<p> Check if the cname part of the principal is a initial or renewed krbtgt principal</p>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_principal_match (krb5_contextcontext, krb5_const_principalprinc, krb5_const_principalpattern)</h3>
<p> return TRUE iff princ matches pattern</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_principal_set_realm (krb5_contextcontext, krb5_principalprincipal, krb5_const_realmrealm)</h3>
<p> Set a new realm for a principal, and as a side-effect free the previous realm. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal set the realm for<br />
 <i>realm</i> the new realm to set</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_principal_set_type (krb5_contextcontext, krb5_principalprincipal, inttype)</h3>
<p> Set the type of the principal </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to set the type for<br />
 <i>type</i> the new type</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_realm_compare (krb5_contextcontext, krb5_const_principalprinc1, krb5_const_principalprinc2)</h3>
<p> return TRUE iff realm(princ1) == realm(princ2) </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>princ1</i> first principal to compare<br />
 <i>princ2</i> second principal to compare</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_principal_compare_any_realm()</code> </p>
<p> <code>krb5_principal_compare()</code></dl>
<h3>krb5_boolean KRB5_LIB_FUNCTION krb5_realm_is_lkdc (const char *realm)</h3>
<p> Returns true if name is Kerberos an LKDC realm</p>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_sname_to_principal (krb5_contextcontext, const char *hostname, const char *sname, int32_ttype, krb5_principal *ret_princ)</h3>
<p> Create a principal for the given service running on the given hostname. If KRB5_NT_SRV_HST is used, the hostname is canonicalized according the configured name canonicalization rules, with canonicalization delayed in some cases. One rule involves DNS, which is insecure unless DNSSEC is used, but we don&#8217;t use DNSSEC-capable resolver APIs here, so that if DNSSEC is used we wouldn&#8217;t know it. </p>
<p> Canonicalization is immediate (not delayed) only when there is only one canonicalization rule and that rule indicates that we should do a host lookup by name (i.e., DNS). </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>hostname</i> hostname to use<br />
 <i>sname</i> Service name to use<br />
 <i>type</i> name type of pricipal, use KRB5_NT_SRV_HST or KRB5_NT_UNKNOWN.<br />
 <i>ret_princ</i> return principal, free with <code>krb5_free_principal()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name (krb5_contextcontext, krb5_const_principalprincipal, char **name)</h3>
<p> Unparse the Kerberos name into a string </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>principal</i> principal to query<br />
 <i>name</i> resulting string, free with krb5_xfree()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name_fixed (krb5_contextcontext, krb5_const_principalprincipal, char *name, size_tlen)</h3>
<p> Unparse the principal name to a fixed buffer </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to unparse<br />
 <i>name</i> buffer to write name to<br />
 <i>len</i> length of buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name_fixed_flags (krb5_contextcontext, krb5_const_principalprincipal, intflags, char *name, size_tlen)</h3>
<p> Unparse the principal name with unparse flags to a fixed buffer. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to unparse<br />
 <i>flags</i> unparse flags<br />
 <i>name</i> buffer to write name to<br />
 <i>len</i> length of buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name_fixed_short (krb5_contextcontext, krb5_const_principalprincipal, char *name, size_tlen)</h3>
<p> Unparse the principal name to a fixed buffer. The realm is skipped if its a default realm. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to unparse<br />
 <i>name</i> buffer to write name to<br />
 <i>len</i> length of buffer</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name_flags (krb5_contextcontext, krb5_const_principalprincipal, intflags, char **name)</h3>
<p> Unparse the Kerberos name into a string </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>principal</i> principal to query<br />
 <i>flags</i> flag to determine the behavior<br />
 <i>name</i> resulting string, free with krb5_xfree()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_unparse_name_short (krb5_contextcontext, krb5_const_principalprincipal, char **name)</h3>
<p> Unparse the principal name to a allocated buffer. The realm is skipped if its a default realm. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos context.<br />
 <i>principal</i> principal to unparse<br />
 <i>name</i> returned buffer, free with krb5_xfree()</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> An krb5 error code, see <code>krb5_get_error_message()</code>.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
