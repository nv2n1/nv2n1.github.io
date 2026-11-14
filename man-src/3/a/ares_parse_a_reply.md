---
title: "ares_parse_a_reply(3)"
name: "ares_parse_a_reply"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_parse_a_reply/"
description: "ares_parse_a_reply – Parse a reply to a DNS query of type A"
---

<h2>NAME</h2>
<p> ares_parse_a_reply &#8211; Parse a reply to a DNS query of type A</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_parse_a_reply(const unsigned char *abuf, int alen,
                       struct hostent **host,
                       struct ares_addrttl *addrttls, int *naddrttls);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_parse_a_reply</code> function parses the response to a query of type A into a <code>struct hostent</code> and/or an array of <code>struct ares_addrttls</code>. The parameters <i>abuf</i> and <i>alen</i> give the contents of the response. The result is stored in allocated memory and a pointer to it stored into the variable pointed to by <i>host</i>, if host is nonnull. It is the caller&#8217;s responsibility to free the resulting host structure using <code><a href="/docs/linux/man/3-ares_free_hostent/">ares_free_hostent</a></code>(3) when it is no longer needed. </p>
<p> If <i>addrttls</i> and <i>naddrttls</i> are both nonnull, then up to *naddrttls <code>struct ares_addrttl</code> records are stored in the array pointed to by addrttls, and then *naddrttls is set to the number of records so stored. Note that the memory for these records is supplied by the caller.</p>
<h2>RETURN VALUES</h2>
<p> <code>ares_parse_a_reply</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The response was successfully parsed.</p>
<dt><code>ARES_EBADRESP</code></p>
<dd> The response was malformatted.</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The response did not contain an answer to the query.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_gethostbyname/">ares_gethostbyname</a></code>(3), <code><a href="/docs/linux/man/3-ares_free_hostent/">ares_free_hostent</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
