---
title: "krb5_krbhst_reset(3)"
name: "krb5_krbhst_reset"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_krbhst_reset/"
description: "krb5_krbhst_init krb5_krbhst_init_flags krb5_krbhst_next krb5_krbhst_next_as_string krb5_krbhst_reset krb5_krbhst_free krb5_krbhst_format_string krb5_krbhst_get_addrinfo – lookup Kerberos KDC hosts"
---

<h2 class="name">NAME</h2>
<p> <code>krb5_krbhst_init</code> <code>krb5_krbhst_init_flags</code> <code>krb5_krbhst_next</code> <code>krb5_krbhst_next_as_string</code> <code>krb5_krbhst_reset</code> <code>krb5_krbhst_free</code> <code>krb5_krbhst_format_string</code> <code>krb5_krbhst_get_addrinfo</code> &#8211; lookup Kerberos KDC hosts </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h Ft krb5_error_code Fn krb5_krbhst_init krb5_context context const char *realm unsigned int type krb5_krbhst_handle *handle Ft krb5_error_code Fn krb5_krbhst_init_flags krb5_context context const char *realm unsigned int type int flags krb5_krbhst_handle *handle Ft krb5_error_code Fn krb5_krbhst_next krb5_context context krb5_krbhst_handle handle krb5_krbhst_info **host Ft krb5_error_code Fn krb5_krbhst_next_as_string krb5_context context krb5_krbhst_handle handle char *hostname size_t hostlen Ft void Fn krb5_krbhst_reset krb5_context context krb5_krbhst_handle handle Ft void Fn krb5_krbhst_free krb5_context context krb5_krbhst_handle handle Ft krb5_error_code Fn krb5_krbhst_format_string krb5_context context const krb5_krbhst_info *host char *hostname size_t hostlen Ft krb5_error_code Fn krb5_krbhst_get_addrinfo krb5_context context krb5_krbhst_info *host struct addrinfo **ai</p>
<h2>DESCRIPTION</h2>
<p> These functions are used to sequence through all Kerberos hosts of a particular realm and service. The service type can be the KDCs, the administrative servers, the password changing servers, or the servers for Kerberos 4 ticket conversion. </p>
<p> First a handle to a particular service is obtained by calling Fn krb5_krbhst_init (or Fn krb5_krbhst_init_flags ) with the Fa realm of interest and the type of service to lookup. The Fa type can be one of: </p>
<dl>
<dt><code>KRB5_KRBHST_KDC</code></p>
<dd>
<dt><code>KRB5_KRBHST_ADMIN</code></p>
<dd>
<dt><code>KRB5_KRBHST_CHANGEPW</code></p>
<dd>
<dt><code>KRB5_KRBHST_KRB524</code></p>
<dd></dl>
<p> The Fa handle is returned to the caller, and should be passed to the other functions. </p>
<p> The Fa flag argument to <code>krb5_krbhst_init_flags</code> is the same flags as Fn krb5_send_to_kdc_flags uses. Possible values are: </p>
<dl>
<dt><code>KRB5_KRBHST_FLAGS_MASTER</code></p>
<dd> only talk to master (readwrite) KDC</p>
<dt><code>KRB5_KRBHST_FLAGS_LARGE_MSG</code></p>
<dd> this is a large message, so use transport that can handle that.</dl>
<p> For each call to Fn krb5_krbhst_next information on a new host is returned. The former function returns in Fa host a pointer to a structure containing information about the host, such as protocol, hostname, and port: </p>
<blockquote>
<pre><code>
typedef struct krb5_krbhst_info {
    enum { KRB5_KRBHST_UDP,
           KRB5_KRBHST_TCP,
           KRB5_KRBHST_HTTP } proto;
    unsigned short port;
    struct addrinfo *ai;
    struct krb5_krbhst_info *next;
    char hostname[1];
} krb5_krbhst_info;
</code></pre>
</blockquote>
<p> The related function, Fn krb5_krbhst_next_as_string , return the same information as a URL-like string. </p>
<p> When there are no more hosts, these functions return <code>KRB5_KDC_UNREACH</code> </p>
<p> To re-iterate over all hosts, call Fn krb5_krbhst_reset and the next call to Fn krb5_krbhst_next will return the first host. </p>
<p> When done with the handle, Fn krb5_krbhst_free should be called. </p>
<p> To use a <i>krb5_krbhst_info</i> there are two functions: Fn krb5_krbhst_format_string that will return a printable representation of that struct and Fn krb5_krbhst_get_addrinfo that will return a <i>struct addrinfo</i> that can then be used for communicating with the server mentioned.</p>
<h2>EXAMPLES</h2>
<p> The following code will print the KDCs of the realm &#8220;MY.REALM&#8221; </p>
<blockquote>
<pre><code>
krb5_krbhst_handle handle;
char host[MAXHOSTNAMELEN];
krb5_krbhst_init(context, "MY.REALM", KRB5_KRBHST_KDC, &amp;handle);
while (krb5_krbhst_next_as_string(context, handle,
                                  host, sizeof(host)) == 0)
    printf("%s
", host);
krb5_krbhst_free(context, handle);
</code></pre>
</blockquote>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-getaddrinfo/">getaddrinfo</a>(3), krb5_get_krbhst3, krb5_send_to_kdc_flags3</p>
<h2>HISTORY</h2>
<p> These functions first appeared in Heimdal 0.3g. </p>
<h2>Index</h2>
