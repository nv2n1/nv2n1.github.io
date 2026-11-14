---
title: "krb5_appdefault(3)"
name: "krb5_appdefault"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_appdefault/"
description: "krb5_appdefault_boolean krb5_appdefault_string krb5_appdefault_time – get application configuration value"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_appdefault_boolean</code> <code>krb5_appdefault_string</code> <code>krb5_appdefault_time</code> &#8211; get application configuration value </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft void Fn krb5_appdefault_boolean krb5_context context const char *appname krb5_realm realm const char *option krb5_boolean def_val krb5_boolean *ret_val Ft void Fn krb5_appdefault_string krb5_context context const char *appname krb5_realm realm const char *option const char *def_val char **ret_val Ft void Fn krb5_appdefault_time krb5_context context const char *appname krb5_realm realm const char *option time_t def_val time_t *ret_val</p>
<h2>DESCRIPTION</h2>
<p> These functions get application defaults from the <code>appdefaults</code> section of the krb5.conf5 configuration file. These defaults can be specified per application, and/or per realm. </p>
<p> These values will be looked for in krb5.conf5, in order of descending importance. </p>
<blockquote>
<pre><code>
[appdefaults] appname = {
    realm = {
        option = value}} appname = {option = value} realm = {option = value} option = value
</code></pre>
</blockquote>
<p> Fa appname is the name of the application, and Fa realm is the realm name. If the realm is omitted it will not be used for resolving values. Fa def_val is the value to return if no value is found in krb5.conf5.</p>
<h2>SEE ALSO</h2>
<p> krb5_config3, krb5.conf5 </p>
<h2>Index</h2>
