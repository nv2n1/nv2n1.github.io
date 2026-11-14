---
title: "krb5_free_host_realm(3)"
name: "krb5_free_host_realm"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_free_host_realm/"
description: "Heimdal Kerberos 5 support functions –"
---

<h2 class="name">NAME</h2>
<p> Heimdal Kerberos 5 support functions &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>krb5plugin_an2ln_ftable_desc</code><br />
 <i>Description of the <a href="/docs/linux/man/3-krb5_aname_to_lname/">krb5_aname_to_lname</a>(3) plugin facility. </i><br />
 struct <code>krb5plugin_db_ftable_desc</code><br />
 <i>Description of the krb5 DB plugin facility. </i><br />
 struct <code>krb5plugin_kuserok_ftable_desc</code><br />
 <i>Description of the <a href="/docs/linux/man/3-krb5_kuserok/">krb5_kuserok</a>(3) plugin facility. </i></p>
<h3>Functions</h3>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_acl_match_string</code> (krb5_context context, const char *string, const char *format,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_acl_match_file</code> (krb5_context context, const char *file, const char *format,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_aname_to_localname</code> (krb5_context context, krb5_const_principal aname, size_t lnsize, char *lname)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_config_parse_file_multi</code> (krb5_context context, const char *fname, krb5_config_section **res)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_config_file_free</code> (krb5_context context, krb5_config_section *s)&quot; </p>
<p> KRB5_LIB_FUNCTION const<br />
 krb5_config_binding<br />
 *KRB5_LIB_CALL <code>krb5_config_get_list</code> (krb5_context context, const krb5_config_section *c,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION const<br />
 krb5_config_binding<br />
 *KRB5_LIB_CALL <code>krb5_config_vget_list</code> (krb5_context context, const krb5_config_section *c, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_config_get_string</code> (krb5_context context, const krb5_config_section *c,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_config_vget_string</code> (krb5_context context, const krb5_config_section *c, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_config_vget_string_default</code> (krb5_context context, const krb5_config_section *c, const char *def_value, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION const char<br />
 *KRB5_LIB_CALL <code>krb5_config_get_string_default</code> (krb5_context context, const krb5_config_section *c, const char *def_value,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION char<br />
 **KRB5_LIB_CALL <code>krb5_config_vget_strings</code> (krb5_context context, const krb5_config_section *c, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION char<br />
 **KRB5_LIB_CALL <code>krb5_config_get_strings</code> (krb5_context context, const krb5_config_section *c,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION void<br />
 KRB5_LIB_CALL <code>krb5_config_free_strings</code> (char **strings)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_config_vget_bool_default</code> (krb5_context context, const krb5_config_section *c, krb5_boolean def_value, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_config_vget_bool</code> (krb5_context context, const krb5_config_section *c, va_list args)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_config_get_bool_default</code> (krb5_context context, const krb5_config_section *c, krb5_boolean def_value,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_config_get_bool</code> (krb5_context context, const krb5_config_section *c,&#8230;)&quot; </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_config_vget_time_default</code> (krb5_context context, const krb5_config_section *c, int def_value, va_list args) </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_config_vget_time</code> (krb5_context context, const krb5_config_section *c, va_list args) </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_config_get_time_default</code> (krb5_context context, const krb5_config_section *c, int def_value,&#8230;) </p>
<p> KRB5_LIB_FUNCTION int KRB5_LIB_CALL <code>krb5_config_get_time</code> (krb5_context context, const krb5_config_section *c,&#8230;) </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_expand_hostname</code> (krb5_context context, const char *orig_hostname, char **new_hostname)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_expand_hostname_realms</code> (krb5_context context, const char *orig_hostname, char **new_hostname, char ***realms)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_free_host_realm</code> (krb5_context context, krb5_realm *realmlist)&quot; </p>
<p> KRB5_LIB_FUNCTION krb5_boolean<br />
 KRB5_LIB_CALL <code>krb5_kuserok</code> (krb5_context, krb5_principal, const char *)&quot; </p>
<p> KRB5_LIB_FUNCTION<br />
 krb5_error_code KRB5_LIB_CALL <code>krb5_plugin_register</code> (krb5_context, enum krb5_plugin_type, const char *, void *)&quot; </p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_acl_match_file (krb5_contextcontext, const char *file, const char *format, &#8230;)</h3>
<p> krb5_acl_match_file matches ACL format against each line in a file using <code>krb5_acl_match_string()</code>. Lines starting with # are treated like comments and ignored. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>file</i> file with acl listed in the file.<br />
 <i>format</i> format to match.<br />
 <i>&#8230;</i> parameter to format string.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_acl_match_string</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_acl_match_string (krb5_contextcontext, const char *string, const char *format, &#8230;)</h3>
<p> krb5_acl_match_string matches ACL format against a string. </p>
<p> The ACL format has three format specifiers: s, f, and r. Each specifier will retrieve one argument from the variable arguments for either matching or storing data. The input string is split up using &#8216; &#8216; (space) and &#8216;	&#8217; (tab) as a delimiter; multiple and &#8216;	&#8217; in a row are considered to be the same. </p>
<p> List of format specifiers:</p>
<dl>
<dt>&bull;</p>
<dd> s Matches a string using <a href="/docs/linux/man/3-strcmp/">strcmp</a>(3) (case sensitive).</p>
<dt>&bull;</p>
<dd> f Matches the string with <a href="/docs/linux/man/3-fnmatch/">fnmatch</a>(3). Theflags argument (the last argument) passed to the fnmatch function is 0.</p>
<dt>&bull;</p>
<dd> r Returns a copy of the string in the char ** passed in; the copy must be freed with <a href="/docs/linux/man/3-free/">free</a>(3). There is no need to <a href="/docs/linux/man/3-free/">free</a>(3) the string on error: the function will clean up and set the pointer to NULL.</dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context<br />
 <i>string</i> string to match with<br />
 <i>format</i> format to match<br />
 <i>&#8230;</i> parameter to format string</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0.</dl>
<pre><code>
*char *s;
**ret = krb5_acl_match_string(context, "foo", "s", "foo");
*if (ret) * krb5_errx(context, 1, "acl didn't match");
*ret = krb5_acl_match_string(context, "foo foo baz/kaka",
                             *"ss", "foo", &amp;s, "foo/\*");
*if (ret)
{
    * // no need to free(s) on error
        *assert(s == NULL);
    *krb5_errx(context, 1, "acl didn't match");
    *
}
*free(s);
*
</code></pre>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> <code>krb5_acl_match_file</code></dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_aname_to_localname (krb5_contextcontext, krb5_const_principalaname, size_tlnsize, char *lname)</h3>
<p> Map a principal name to a local username. </p>
<p> Returns 0 on success, KRB5_NO_LOCALNAME if no mapping was found, or some Kerberos or system error. </p>
<p> Inputs: </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A krb5_context<br />
 <i>aname</i> A principal name<br />
 <i>lnsize</i> The size of the buffer into which the username will be written<br />
 <i>lname</i> The buffer into which the username will be written</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_config_file_free (krb5_contextcontext, krb5_config_section *s)</h3>
<p> Free configuration file section, the result of krb5_config_parse_file() and <code>krb5_config_parse_file_multi()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context<br />
 <i>s</i> the configuration section to free</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns 0 on successes, otherwise an error code, see <code>krb5_get_error_message()</code></dl>
<h3>KRB5_LIB_FUNCTION void KRB5_LIB_CALL krb5_config_free_strings (char **strings)</h3>
<p> Free the resulting strings from krb5_config-get_strings() and <code>krb5_config_vget_strings()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>strings</i> strings to free</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_config_get_bool (krb5_contextcontext, const krb5_config_section *c, &#8230;)</h3>
<p> Like <code>krb5_config_get_bool()</code> but with a va_list list of configuration selection. </p>
<p> Configuration value to a boolean value, where yes/true and any non-zero number means TRUE and other value is FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_config_get_bool_default (krb5_contextcontext, const krb5_config_section *c, krb5_booleandef_value, &#8230;)</h3>
<p> <code>krb5_config_get_bool_default()</code> will convert the configuration option value to a boolean value, where yes/true and any non-zero number means TRUE and other value is FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION const krb5_config_binding *KRB5_LIB_CALL krb5_config_get_list (krb5_contextcontext, const krb5_config_section *c, &#8230;)</h3>
<p> Get a list of configuration binding list for more processing </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if configuration list is not found, a list otherwise</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_config_get_string (krb5_contextcontext, const krb5_config_section *c, &#8230;)</h3>
<p> Returns a &#8216;const char *&#8217; to a string in the configuration database. The string may not be valid after a reload of the configuration database so a caller should make a local copy if it needs to keep the string. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if configuration string not found, a string otherwise</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_config_get_string_default (krb5_contextcontext, const krb5_config_section *c, const char *def_value, &#8230;)</h3>
<p> Like <code>krb5_config_get_string()</code>, but instead of returning NULL, instead return a default value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a configuration string</dl>
<h3>KRB5_LIB_FUNCTION char **KRB5_LIB_CALL krb5_config_get_strings (krb5_contextcontext, const krb5_config_section *c, &#8230;)</h3>
<p> Get a list of configuration strings, free the result with <code>krb5_config_free_strings()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_config_get_time (krb5_contextcontext, const krb5_config_section *c, &#8230;)</h3>
<p> Get the time from the configuration file using a relative time, for example: 1h30s </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> parsed the time or -1 on error</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_config_get_time_default (krb5_contextcontext, const krb5_config_section *c, intdef_value, &#8230;)</h3>
<p> Get the time from the configuration file using a relative time, for example: 1h30s </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>&#8230;</i> a list of names, terminated with NULL.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> parsed the time (or def_value on parse error)</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_config_parse_file_multi (krb5_contextcontext, const char *fname, krb5_config_section **res)</h3>
<p> Parse a configuration file and add the result into res. This interface can be used to parse several configuration files into one resulting krb5_config_section by calling it repeatably. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Kerberos 5 context.<br />
 <i>fname</i> a file name to a Kerberos configuration file<br />
 <i>res</i> the returned result, must be free with <code>krb5_free_config_files()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<p> If the fname starts with &#8216;~/&#8217; parse configuration file in the current users home directory. The behavior can be disabled and enabled by calling <code>krb5_set_home_dir_access()</code>.</p>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_config_vget_bool (krb5_contextcontext, const krb5_config_section *c, va_listargs)</h3>
<p> <code>krb5_config_get_bool()</code> will convert the configuration option value to a boolean value, where yes/true and any non-zero number means TRUE and other value is FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_config_vget_bool_default (krb5_contextcontext, const krb5_config_section *c, krb5_booleandef_value, va_listargs)</h3>
<p> Like <code>krb5_config_get_bool_default()</code> but with a va_list list of configuration selection. </p>
<p> Configuration value to a boolean value, where yes/true and any non-zero number means TRUE and other value is FALSE. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION const krb5_config_binding *KRB5_LIB_CALL krb5_config_vget_list (krb5_contextcontext, const krb5_config_section *c, va_listargs)</h3>
<p> Get a list of configuration binding list for more processing </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if configuration list is not found, a list otherwise</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_config_vget_string (krb5_contextcontext, const krb5_config_section *c, va_listargs)</h3>
<p> Like <code>krb5_config_get_string()</code>, but uses a va_list instead of &#8230; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> NULL if configuration string not found, a string otherwise</dl>
<h3>KRB5_LIB_FUNCTION const char *KRB5_LIB_CALL krb5_config_vget_string_default (krb5_contextcontext, const krb5_config_section *c, const char *def_value, va_listargs)</h3>
<p> Like <code>krb5_config_vget_string()</code>, but instead of returning NULL, instead return a default value. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a configuration string</dl>
<h3>KRB5_LIB_FUNCTION char **KRB5_LIB_CALL krb5_config_vget_strings (krb5_contextcontext, const krb5_config_section *c, va_listargs)</h3>
<p> Get a list of configuration strings, free the result with <code>krb5_config_free_strings()</code>. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> TRUE or FALSE</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_config_vget_time (krb5_contextcontext, const krb5_config_section *c, va_listargs)</h3>
<p> Get the time from the configuration file using a relative time, for example: 1h30s </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> parsed the time or -1 on error</dl>
<h3>KRB5_LIB_FUNCTION int KRB5_LIB_CALL krb5_config_vget_time_default (krb5_contextcontext, const krb5_config_section *c, intdef_value, va_listargs)</h3>
<p> Get the time from the configuration file using a relative time. </p>
<p> Like <code>krb5_config_get_time_default()</code> but with a va_list list of configuration selection. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>c</i> a configuration section, or NULL to use the section from context<br />
 <i>def_value</i> the default value to return if no configuration found in the database.<br />
 <i>args</i> a va_list of arguments</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> parsed the time (or def_value on parse error)</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_expand_hostname (krb5_contextcontext, const char *orig_hostname, char **new_hostname)</h3>
<p> <code>krb5_expand_hostname()</code> tries to make orig_hostname into a more canonical one in the newly allocated space returned in new_hostname. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>orig_hostname</i> hostname to canonicalise.<br />
 <i>new_hostname</i> output hostname, caller must free hostname with krb5_xfree().</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_expand_hostname_realms (krb5_contextcontext, const char *orig_hostname, char **new_hostname, char ***realms)</h3>
<p> <code>krb5_expand_hostname_realms()</code> expands orig_hostname to a name we believe to be a hostname in newly allocated space in new_hostname and return the realms new_hostname is believed to belong to in realms. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>orig_hostname</i> hostname to canonicalise.<br />
 <i>new_hostname</i> output hostname, caller must free hostname with krb5_xfree().<br />
 <i>realms</i> output possible realms, is an array that is terminated with NULL. Caller must free with <code>krb5_free_host_realm()</code>.</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> Return an error code or 0, see <code>krb5_get_error_message()</code>.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_free_host_realm (krb5_contextcontext, krb5_realm *realmlist)</h3>
<p> Free all memory allocated by `realmlist&#8217; </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> A Kerberos 5 context.<br />
 <i>realmlist</i> realmlist to free, NULL is ok</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> a Kerberos error code, always 0.</dl>
<h3>KRB5_LIB_FUNCTION krb5_boolean KRB5_LIB_CALL krb5_kuserok (krb5_contextcontext, krb5_principalprincipal, const char *luser)</h3>
<p> This function takes the name of a local user and checks if principal is allowed to log in as that user. </p>
<p> The user may have a ~/.k5login file listing principals that are allowed to login as that user. If that file does not exist, all principals with a only one component that is identical to the username, and a realm considered local, are allowed access. </p>
<p> The .k5login file must contain one principal per line, be owned by user and not be writable by group or other (but must be readable by anyone). </p>
<p> Note that if the file exists, no implicit access rights are given to user [at] LOCALREALM. </p>
<p> Optionally, a set of files may be put in ~/.k5login.d (a directory), in which case they will all be checked in the same manner as .k5login. The files may be called anything, but files starting with a hash (#) , or ending with a tilde (~) are ignored. Subdirectories are not traversed. Note that this directory may not be checked by other Kerberos implementations. </p>
<p> If no configuration file exists, match user against local domains, ie luser [at] LOCAL-REALMS-IN-CONFIGURATION-FILES. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> Kerberos 5 context.<br />
 <i>principal</i> principal to check if allowed to login<br />
 <i>luser</i> local user id</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> returns TRUE if access should be granted, FALSE otherwise.</dl>
<h3>KRB5_LIB_FUNCTION krb5_error_code KRB5_LIB_CALL krb5_plugin_register (krb5_contextcontext, enum krb5_plugin_typetype, const char *name, void *symbol)</h3>
<p> Register a plugin symbol name of specific type. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>context</i> a Keberos context<br />
 <i>type</i> type of plugin symbol<br />
 <i>name</i> name of plugin symbol<br />
 <i>symbol</i> a pointer to the named symbol</dl>
<p> <code>Returns:</code></p>
<dl>
<dt>
<dd> In case of error a non zero error com_err error is returned and the Kerberos error string is set.</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for HeimdalKerberos5library from the source code. </p>
<h2>Index</h2>
