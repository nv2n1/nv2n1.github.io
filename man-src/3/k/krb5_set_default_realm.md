---
title: "krb5_set_default_realm(3)"
name: "krb5_set_default_realm"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_set_default_realm/"
description: "krb5_copy_host_realm krb5_free_host_realm krb5_get_default_realm krb5_get_default_realms krb5_get_host_realm krb5_set_default_realm – default and host realm read and manipulation routines"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_copy_host_realm</code> <code>krb5_free_host_realm</code> <code>krb5_get_default_realm</code> <code>krb5_get_default_realms</code> <code>krb5_get_host_realm</code> <code>krb5_set_default_realm</code> &#8211; default and host realm read and manipulation routines </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fo krb5_copy_host_realm Fa krb5_context context Fa const krb5_realm *from Fa krb5_realm **to Fc Ft krb5_error_code Fo krb5_free_host_realm Fa krb5_context context Fa krb5_realm *realmlist Fc Ft krb5_error_code Fo krb5_get_default_realm Fa krb5_context context Fa krb5_realm *realm Fc Ft krb5_error_code Fo krb5_get_default_realms Fa krb5_context context Fa krb5_realm **realm Fc Ft krb5_error_code Fo krb5_get_host_realm Fa krb5_context context Fa const char *host Fa krb5_realm **realms Fc Ft krb5_error_code Fo krb5_set_default_realm Fa krb5_context context Fa const char *realm Fc</p>
<h2>DESCRIPTION</h2>
<p> Fn krb5_copy_host_realm copies the list of realms from Fa from to Fa to . Fa to should be freed by the caller using Fa krb5_free_host_realm . </p>
<p> Fn krb5_free_host_realm frees all memory allocated by Fa realmlist . </p>
<p> Fn krb5_get_default_realm returns the first default realm for this host. The realm returned should be freed with Fn krb5_xfree . </p>
<p> Fn krb5_get_default_realms returns a <code>NULL</code> terminated list of default realms for this context. Realms returned by Fn krb5_get_default_realms should be freed with Fn krb5_free_host_realm . </p>
<p> Fn krb5_get_host_realm returns a <code>NULL</code> terminated list of realms for Fa host by looking up the information in the <code>[domain_realm]</code> in krb5.conf or in <code>DNS</code> If the mapping in <code>[domain_realm]</code> results in the string <code>dns_locate</code> DNS is used to lookup the realm. </p>
<p> When using <code>DNS</code> to a resolve the domain for the host a.b.c, Fn krb5_get_host_realm looks for a <code>TXT</code> resource record named <code>_kerberos.a.b.c</code> and if not found, it strips off the first component and tries a again (_kerberos.b.c) until it reaches the root. </p>
<p> If there is no configuration or DNS information found, Fn krb5_get_host_realm assumes it can use the domain part of the Fa host to form a realm. Caller must free Fa realmlist with Fn krb5_free_host_realm . </p>
<p> Fn krb5_set_default_realm sets the default realm for the Fa context . If <code>NULL</code> is used as a Fa realm , the <code>[libdefaults]default_realm</code> stanza in krb5.conf is used. If there is no such stanza in the configuration file, the Fn krb5_get_host_realm function is used to form a default realm.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-free/">free</a>(3), krb5.conf5 </p>
<h2>Index</h2>
