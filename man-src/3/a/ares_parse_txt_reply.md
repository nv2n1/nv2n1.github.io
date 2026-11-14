---
title: "ares_parse_txt_reply(3)"
name: "ares_parse_txt_reply"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_parse_txt_reply/"
description: "ares_parse_txt_reply – Parse a reply to a DNS query of type TXT"
---

<h2>NAME</h2>
<p> ares_parse_txt_reply &#8211; Parse a reply to a DNS query of type TXT</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
int ares_parse_txt_reply(const unsigned char *abuf, int alen,
                         struct ares_txt_reply **txt_out);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>ares_parse_txt_reply</code> function parses the response to a query of type TXT into a linked list (one element per sub-string) of <i>struct ares_txt_reply </i> The parameters <i>abuf</i> and <i>alen</i> give the contents of the response. The result is stored in allocated memory and a pointer to it stored into the variable pointed to by <i>txt_out</i>. It is the caller&#8217;s responsibility to free the resulting <i>txt_out</i> structure when it is no longer needed using the function <code>ares_free_data</code> </p>
<p> The structure <i>ares_txt_reply</i> contains the following fields: </p>
<pre><code>
struct ares_txt_reply {
    struct ares_txt_reply *next;
    unsigned int length;
    unsigned char *txt;
};
</code></pre>
<h2>RETURN VALUES</h2>
<p> <code>ares_parse_txt_reply</code> can return any of the following values:</p>
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
<p> This function was first introduced in c-ares version 1.7.0.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_query/">ares_query</a></code>(3) <code><a href="/docs/linux/man/3-ares_free_data/">ares_free_data</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Written by Jakub Hrozek &lt;jhrozek [at] redhat.com&gt;, on behalf of Red Hat, Inc <a rel="nofollow" href="http://www.redhat.com">http://www.redhat.com</a> </p>
<h2>Index</h2>
