---
title: "krb5-config(1)"
name: "krb5-config"
section: "1"
letter: "k"
url: "/docs/linux/man/1-krb5-config/"
description: "krb5-config – tool for linking against MIT Kerberos libraries"
---

<h2>NAME</h2>
<p> krb5-config &#8211; tool for linking against MIT Kerberos libraries</p>
<h2>SYNOPSIS</h2>
<p> <code>krb5-config</code> [<code>&#8211;</code><code>-help</code> | <code>&#8211;</code><code>-all</code> | <code>&#8211;</code><code>-version</code> | <code>&#8211;</code><code>-vendor</code> | <code>&#8211;</code><code>-prefix</code> | <code>&#8211;</code><code>-exec-prefix</code> | <code>&#8211;</code><code>-defccname</code> | <code>&#8211;</code><code>-defktname</code> | <code>&#8211;</code><code>-defcktname</code> | <code>&#8211;</code><code>-cflags</code> | <code>&#8211;</code><code>-libs</code> [<i>libraries</i>]]</p>
<h2>DESCRIPTION</h2>
<p> krb5-config tells the application programmer what flags to use to compile and link programs against the installed Kerberos libraries.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code><code>-help</code></p>
<dd> prints a usage message. This is the default behavior when no options are specified.</p>
<dt><code>&#8211;</code><code>-all</code></p>
<dd> prints the version, vendor, prefix, and exec-prefix.</p>
<dt><code>&#8211;</code><code>-version</code></p>
<dd> prints the version number of the Kerberos installation.</p>
<dt><code>&#8211;</code><code>-vendor</code></p>
<dd> prints the name of the vendor of the Kerberos installation.</p>
<dt><code>&#8211;</code><code>-prefix</code></p>
<dd> prints the prefix for which the Kerberos installation was built.</p>
<dt><code>&#8211;</code><code>-exec-prefix</code></p>
<dd> prints the prefix for executables for which the Kerberos installation was built.</p>
<dt><code>&#8211;</code><code>-defccname</code></p>
<dd> prints the built-in default credentials cache location.</p>
<dt><code>&#8211;</code><code>-defktname</code></p>
<dd> prints the built-in default keytab location.</p>
<dt><code>&#8211;</code><code>-defcktname</code></p>
<dd> prints the built-in default client (initiator) keytab location.</p>
<dt><code>&#8211;</code><code>-cflags</code></p>
<dd> prints the compilation flags used to build the Kerberos installation.</p>
<dt><code>&#8211;</code><code>-libs</code> [<i>library</i>]</p>
<dd> prints the compiler options needed to link against <i>library</i>. Allowed values for <i>library</i> are: <center></p>
<table>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> krb5 </td>
<td> Kerberos 5 applications (default)
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> gssapi </td>
<td> GSSAPI applications with Kerberos 5 bindings
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> kadm-client </td>
<td> Kadmin client
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> kadm-server </td>
<td> Kadmin server
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
<tr VALIGN=top>
<td> kdb </td>
<td> Applications that access the Kerberos database
</td>
</tr>
<tr VALIGN=top>
<td COLSPAN=2>
<hr>
</td>
</tr>
</table>
<p></center></dl>
<h2>EXAMPLES</h2>
<p> krb5-config is particularly useful for compiling against a Kerberos installation that was installed in a non-standard location. For example, a Kerberos installation that is installed in <code>/opt/krb5/</code> but uses libraries in <code>/usr/local/lib/</code> for text localization would produce the following output: </p>
<pre>
shell% krb5-config --libs krb5
-L/opt/krb5/lib -Wl,-rpath -Wl,/opt/krb5/lib -L/usr/local/lib -lkrb5 -lk5crypto -lcom_err
</pre>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-kerberos/">kerberos</a>(1), <a href="/docs/linux/man/1-cc/">cc</a>(1)</p>
<h2>AUTHOR</h2>
<p> MIT</p>
<h2>COPYRIGHT</h2>
<p> 1985-2017, MIT </p>
<h2>Index</h2>
