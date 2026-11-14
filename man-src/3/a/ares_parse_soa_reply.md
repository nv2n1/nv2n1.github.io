---
title: "ares_parse_soa_reply(3)"
name: "ares_parse_soa_reply"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_parse_soa_reply/"
description: "ares_parse_soa_reply – Parse a reply to a DNS query of type SOA"
---

<h2>NAME</h2>
<p> ares_parse_soa_reply &#8211; Parse a reply to a DNS query of type SOA</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_parse_soa_reply(const unsigned char* abuf, int alen,
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_parse_soa_reply</code> function parses the response to a query of type SOA into a <i>struct ares_soa_reply</i>. The parameters <i>abuf</i> and <i>alen</i> give the contents of the response. The result is stored in allocated memory and a pointer to it stored into the variable pointed to by <i>soa_out</i>. It is the caller&#8217;s responsibility to free the resulting <i>soa_out</i> structure when it is no longer needed using the function <code>ares_free_data</code> </p>
<p> The structure <i>ares_soa_reply</i> contains the following fields: </p>
<pre><code>
struct ares_soa_reply {
    char *nsname;
    char *hostmaster;
    unsigned int serial;
    unsigned int refresh;
    unsigned int retry;
    unsigned int expire;
    unsigned int minttl;
};
</code></pre>
<h2>RETURN VALUES</h2>
<p> <code>ares_parse_soa_reply</code> can return any of the following values:</p>
<dl>
<dt><code>ARES_SUCCESS</code></p>
<dd> The response was successfully parsed.</p>
<dt><code>ARES_EBADRESP</code></p>
<dd> The response was malformatted.</p>
<dt><code>ARES_ENODATA</code></p>
<dd> The response did not contain an answer to the query.</p>
<dt><code>ARES_ENOMEM</code></p>
<dd> Memory was exhausted.</dl>
<h2>AVAILABILITY</h2>
<p> This function was first introduced in c-ares version 1.9.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_query/">ares_query</a></code>(3) <code><a href="/docs/linux/man/3-ares_free_data/">ares_free_data</a></code>(3) </p>
<h2>Index</h2>
