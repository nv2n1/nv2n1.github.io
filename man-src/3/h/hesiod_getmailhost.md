---
title: "hesiod_getmailhost(3)"
name: "hesiod_getmailhost"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hesiod_getmailhost/"
---

<h2>NAME</h2>

 hesiod_getmailhost, hesiod_free_postoffice - Hesiod functions for retrieving user to postoffice mappings

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;hesiod.h&gt;
struct hesiod_postoffice *hesiod_getmailhost(void *context,
                                             const char *user) void hesiod_free_postoffice(void *context,
                                                                                           struct hesiod_postoffice *po)
        cc file.c
    - lhesiod
</code></pre>

<h2>DESCRIPTION</h2>

 This family of functions allows you to retrieve user to postoffice mappings using Hesiod. To perform lookups, you need an initialized Hesiod context; see <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) for details. Information is returned in a <i>hesiod_postoffice</i> structure, which has the following fields:
<dl>
<dt>hesiod_po_type
<dd> The type of postoffice box, typically ``POP''.
<dt>hesiod_po_host
<dd> The hostname where the postoffice box resides.
<dt>hesiod_po_name
<dd> The account name on the given postoffice server.</dl>
 

 It is the caller's responsibility to call <i>hesiod_free_postoffice</i> with the returned postoffice entry to free the resources used by the postoffice entry. 

 Hesiod queries for postoffice information are made using the ``pobox'' Hesiod type, using the username as the Hesiod name. The corresponding entries should be space-separated lists of strings giving the type of postoffice box, the hostname, and the account name.

<h2>RETURN VALUES</h2>

 On failure, <i>hesiod_getservbyname</i> returns NULL and sets the global variable <i>errno</i> to indicate the error.

<h2>ERRORS</h2>

 <i>hesiod_getmailhost</i> may fail for any of the reasons the routine <i>hesiod_resolve</i> may fail.

<h2>SEE ALSO</h2>

 <a HREF="/docs/linux/man/3-hesiod/">hesiod</a>(3) 

<h2>Index</h2>


