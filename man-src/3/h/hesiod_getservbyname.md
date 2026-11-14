---
title: "hesiod_getservbyname(3)"
name: "hesiod_getservbyname"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hesiod_getservbyname/"
---

<h2>NAME</h2>

 hesiod_getservbyname, hesiod_free_servent - Hesiod functions for retrieving service information

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;hesiod.h&gt;
struct servent *hesiod_getservbyname(void *context,
                                     const char *name, const char *proto) void hesiod_free_servent(void *context, struct servent *serv)
        cc file.c
    - lhesiod
</code></pre>

<h2>DESCRIPTION</h2>

 This family of functions allows you to retrieve service to port mappings using Hesiod. To perform lookups, you need an initialized Hesiod context; see <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) for details. Information is returned in the same format as by <i>getservbyname</i>. It is the caller's responsibility to call <i>hesiod_free_servent</i> with the returned service entry to free the resources used by the service entry. 

 Hesiod queries for service information are made using the ``service'' Hesiod type, using the service name as the Hesiod name. The corresponding records should be space-separated lists of strings giving the service name, protocol, port number (in decimal), and zero or more aliases for the service. There may be multiple records per service name; <i>hesiod_getservbyname</i> will pick the first one whose protocol matches <i>proto</i>.

<h2>RETURN VALUES</h2>

 On failure, <i>hesiod_getservbyname</i> returns NULL and sets the global variable <i>errno</i> to indicate the error.

<h2>ERRORS</h2>

 <i>hesiod_getservbyname</i> may fail for any of the reasons the routine <i>hesiod_resolve</i> may fail.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) 

<h2>Index</h2>


