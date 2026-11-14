---
title: "libauth(3)"
name: "libauth"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libauth/"
description: "libauth – routines for writing nnrpd resolvers and authenticators"
---

<h2 class="name">NAME</h2>
<p> libauth &#8211; routines for writing nnrpd resolvers and authenticators </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include "libauth.h"
struct res_info {
    struct sockaddr *client;
    struct sockaddr *local;
    char *clienthostname;
};
struct auth_info {
    char *username;
    char *password;
};
struct auth_info *get_auth_info(FILE *);
struct res_info *get_res_info(FILE *);
void free_auth_info(struct auth_info *);
void free_res_info(struct res_info *);
</code></pre>
<h2>DESCRIPTION</h2>
<p> These functions provide a convenient C frontend to the nnrpd external authentication interface documented in <i>doc/external-auth</i>. Use of this library is <code>not</code> required; in particular, external resolvers and authenticators written in languages other than C will need to implement the necessary functionality themselves. </p>
<p> The <i>get_auth_info()</i> and <i>get_res_info()</i> functions allocate sufficient memory for a <code>struct auth_info</code> or <code>struct res_info</code> and any necessary fields, and return a pointer to the struct with the fields filled in from information supplied by nnrpd (the <code>FILE*</code> parameter generally should be <tt>&quot;stdin&quot;</tt>). Both functions return <font SIZE="-1">NULL</font> on error. The caller is responsible for deallocating the memory by using the functions below. </p>
<p> The string fields of both structs are straightforward. The <code>client</code> and <code>local</code> fields of <code>struct res_info</code> actually point to instances of <code>struct sockaddr_in</code> (or <code>struct sockaddr_in6</code> if IPv6 support is compiled in). </p>
<p> The <i>free_auth_info()</i> and <i>free_res_info()</i> functions free the struct passed in as argument and all necessary fields.</p>
<h2>BUGS</h2>
<p> In many cases, nnrpd provides more information than is normally useful (for example, even when calling an authenticator, the resolver information is often provided.) On the other hand, in certain cases it provides less information than might be expected (for example, if nnrpd is reading from stdin rather than a socket). The implementation is capable of handling at least the first of these issues, but that functionality is not exposed in the interface. </p>
<p> At present, <i>libauth.h</i> and its implementation are located in <i>authprogs/</i>; perhaps they should be moved to <i>include/</i> and <i>lib/</i>, respectively?</p>
<h2>HISTORY</h2>
<p> Written by Jeffrey M. Vinocur &lt;jeff [at] litech.org&gt; for InterNetNews. </p>
<p> <tt>$Id:</tt> libauth.pod 8200 2008-11-30 13:31:30Z iulius $</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/8-nnrpd/">nnrpd</a></i>(8), <i><a href="/docs/linux/man/5-readers-conf/">readers.conf</a></i>(5), <i>doc/external-auth</i> </p>
<h2>Index</h2>
