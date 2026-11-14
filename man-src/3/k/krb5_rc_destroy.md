---
title: "krb5_rc_destroy(3)"
name: "krb5_rc_destroy"
section: "3"
letter: "k"
url: "/docs/linux/man/3-krb5_rc_destroy/"
description: "krb5_rcache krb5_rc_close krb5_rc_default krb5_rc_default_name krb5_rc_default_type krb5_rc_destroy krb5_rc_expunge krb5_rc_get_lifespan krb5_rc_get_name krb5_rc_get_type krb5_rc_initialize krb5_rc..."
---

<h2 class="name">NAME</h2>
<p> <code>krb5_rcache</code> <code>krb5_rc_close</code> <code>krb5_rc_default</code> <code>krb5_rc_default_name</code> <code>krb5_rc_default_type</code> <code>krb5_rc_destroy</code> <code>krb5_rc_expunge</code> <code>krb5_rc_get_lifespan</code> <code>krb5_rc_get_name</code> <code>krb5_rc_get_type</code> <code>krb5_rc_initialize</code> <code>krb5_rc_recover</code> <code>krb5_rc_resolve</code> <code>krb5_rc_resolve_full</code> <code>krb5_rc_resolve_type</code> <code>krb5_rc_store</code> <code>krb5_get_server_rcache</code> &#8211; Kerberos 5 replay cache </p>
<h2>LIBRARY</h2>
<p> Kerberos 5 Library (libkrb5, -lkrb5)</p>
<h2>SYNOPSIS</h2>
<p> In krb5.h </p>
<p> <code>struct krb5_rcache;</code> </p>
<p> Ft krb5_error_code Fo krb5_rc_close Fa krb5_context context Fa krb5_rcache id Fc Ft krb5_error_code Fo krb5_rc_default Fa krb5_context context Fa krb5_rcache *id Fc Ft const char * Fo krb5_rc_default_name Fa krb5_context context Fc Ft const char * Fo krb5_rc_default_type Fa krb5_context context Fc Ft krb5_error_code Fo krb5_rc_destroy Fa krb5_context context Fa krb5_rcache id Fc Ft krb5_error_code Fo krb5_rc_expunge Fa krb5_context context Fa krb5_rcache id Fc Ft krb5_error_code Fo krb5_rc_get_lifespan Fa krb5_context context Fa krb5_rcache id Fa krb5_deltat *auth_lifespan Fc Ft const char* Fo krb5_rc_get_name Fa krb5_context context Fa krb5_rcache id Fc Ft const char* Fo krb5_rc_get_type Fa krb5_context context Fa krb5_rcache id Fc Ft krb5_error_code Fo krb5_rc_initialize Fa krb5_context context Fa krb5_rcache id Fa krb5_deltat auth_lifespan Fc Ft krb5_error_code Fo krb5_rc_recover Fa krb5_context context Fa krb5_rcache id Fc Ft krb5_error_code Fo krb5_rc_resolve Fa krb5_context context Fa krb5_rcache id Fa const char *name Fc Ft krb5_error_code Fo krb5_rc_resolve_full Fa krb5_context context Fa krb5_rcache *id Fa const char *string_name Fc Ft krb5_error_code Fo krb5_rc_resolve_type Fa krb5_context context Fa krb5_rcache *id Fa const char *type Fc Ft krb5_error_code Fo krb5_rc_store Fa krb5_context context Fa krb5_rcache id Fa krb5_donot_replay *rep Fc Ft krb5_error_code Fo krb5_get_server_rcache Fa krb5_context context Fa const krb5_data *piece Fa krb5_rcache *id Fc</p>
<h2>DESCRIPTION</h2>
<p> The <code>krb5_rcache</code> structure holds a storage element that is used for data manipulation. The structure contains no public accessible elements. </p>
<p> Fn krb5_rc_initialize Creates the reply cache Fa id and sets it lifespan to Fa auth_lifespan . If the cache already exists, the content is destroyed.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/3-krb5/">krb5</a>(3), krb5_data3, <a href="/docs/linux/man/8-kerberos/">kerberos</a>(8) </p>
<h2>Index</h2>
