---
title: "hesiod_getpwnam(3)"
name: "hesiod_getpwnam"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hesiod_getpwnam/"
---

<h2>NAME</h2>

 hesiod_getpwnam, hesiod_getpwuid, hesiod_free_passwd - Hesiod functions for retrieving passwd information

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;hesiod.h&gt;
struct passwd *hesiod_getpwnam(void *context, const char *name) struct passwd *hesiod_getpwuid(void *context, uid_t uid) void hesiod_free_passwd(void *context, struct passwd *pw)
        cc file.c
    - lhesiod
</code></pre>

<h2>DESCRIPTION</h2>

 This family of functions allows you to retrieve passwd database information using Hesiod. To perform lookups, you need an initialized Hesiod context; see <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) for details. You may look up passwd information by name or by uid; information is returned in the same format as by <i>getpwnam</i> or <i>getpwuid</i>. It is the caller's responsibility to call <i>hesiod_free_passwd</i> with the returned passwd entry to free the resources used by the passwd entry. 

 Hesiod queries for passwd information are made using the ``passwd'' or ``uid'' Hesiod type, using either the username or the decimal representation of the uid as the Hesiod name. The corresponding records should be a colon-separated list of fields giving the username, encrypted password, uid, gid, GECOS information, home directory, and shell of the user.

<h2>RETURN VALUES</h2>

 On failure, <i>hesiod_getpwnam</i> and <i>hesiod_getpwuid</i> return NULL and set the global variable <i>errno</i> to indicate the error.

<h2>ERRORS</h2>

 These calls may fail for any of the reasons the routine <i>hesiod_resolve</i> may fail.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) 

<h2>Index</h2>


