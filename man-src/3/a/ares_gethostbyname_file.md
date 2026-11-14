---
title: "ares_gethostbyname_file(3)"
name: "ares_gethostbyname_file"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_gethostbyname_file/"
description: "ares_gethostbyname_file – Lookup a name in the system’s hosts file"
---

<h2>NAME</h2>
<p> ares_gethostbyname_file &#8211; Lookup a name in the system&#8217;s hosts file</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_gethostbyname_file(ares_channel channel, const char *name,
                            int family, struct hostent **host)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_gethostbyname_file</code> function performs a host lookup by name against the system&#8217;s hosts file (or equivalent local hostname database). The <i>channel</i> parameter is required, but no asynchronous queries are performed. Instead, the lookup is done via the same mechanism used to perform &#8216;f&#8217; lookups (see the <i>lookups</i> options field in <i><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a>(3)</i>). The parameter <i>name</i> gives the hostname as a NUL-terminated C string, and <i>family</i> gives the desired type of address for the resulting host entry. </p>
<p> The return value indicates whether the query succeeded and, if not, how it failed. It may have any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The host lookup completed successfully and <i>host</i> now points to the result (and must be freed with <i><a href="/docs/linux/man/3-ares_free_hostent/">ares_free_hostent</a>(3)</i>).</p>
<dt><code>ARES_ENOTFOUND</code></p>
<dd> The hostname <i>name</i> was not found.</p>
<dt><code>ARES_EFILE</code></p>
<dd> There was a file I/O error while performing the lookup.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<p> On successful completion of the query, the pointer pointed to by <i>host</i> points to a <code>struct hostent</code> containing the address of the host returned by the lookup. The user must free the memory pointed to by <i>host</i> when finished with it by calling <i><a href="/docs/linux/man/3-ares_free_hostent/">ares_free_hostent</a>(3)</i>. If the lookup did not complete successfully, <i>host</i> will be <code>NULL</code>.</p>
<h2>AVAILABILITY</h2>
<p> Added in c-ares 1.5.4</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_gethostbyname/">ares_gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-ares_free_hostent/">ares_free_hostent</a></code>(3), <code><a href="/docs/linux/man/3-ares_init_options/">ares_init_options</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Brad Spencer<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
