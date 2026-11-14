---
title: "krb5_get_all_client_addrs(3)"
name: "krb5_get_all_client_addrs"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_get_all_client_addrs/"
description: "krb5_get_all_client_addrs krb5_get_all_server_addrs – return local addresses"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_get_all_client_addrs</code> <code>krb5_get_all_server_addrs</code> &#8211; return local addresses </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fn krb5_get_all_client_addrs krb5_context context krb5_addresses *addrs Ft krb5_error_code Fn krb5_get_all_server_addrs krb5_context context krb5_addresses *addrs</p>
<h2>DESCRIPTION</h2>
<p> These functions return in Fa addrs a list of addresses associated with the local host. </p>
<p> The server variant returns all configured interface addresses (if possible), including loop-back addresses. This is useful if you want to create sockets to listen to. </p>
<p> The client version will also scan local interfaces (can be turned off by setting <code>libdefaults/scan_interfaces</code> to false in krb5.conf ) but will not include loop-back addresses, unless there are no other addresses found. It will remove all addresses included in <code>libdefaults/ignore_addresses</code> but will unconditionally include addresses in <code>libdefaults/extra_addresses</code> </p>
<p> The returned addresses should be freed by calling Fn krb5_free_addresses .</p>
<h2>SEE ALSO</h2>
<p> krb5_free_addresses3 </p>
<h2>Index</h2>
