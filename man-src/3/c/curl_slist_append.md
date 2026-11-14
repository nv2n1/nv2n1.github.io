---
title: "curl_slist_append(3)"
name: "curl_slist_append"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_slist_append/"
description: "curl_slist_append – add a string to an slist"
---

<h2>NAME</h2>
<p> curl_slist_append &#8211; add a string to an slist</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>struct curl_slist *curl_slist_append(struct curl_slist *</code><i>list,</i> <code>const char * string</code><i>);</i></p>
<h2>DESCRIPTION</h2>
<p> curl_slist_append() appends a specified string to a linked list of strings. The existing <i>list</i> should be passed as the first argument while the new list is returned from this function. The specified <i>string</i> has been appended when this function returns. curl_slist_append() copies the string. </p>
<p> The list should be freed again (after usage) with <code><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</code>.</p>
<h2>RETURN VALUE</h2>
<p> A null pointer is returned if anything went wrong, otherwise the new list pointer is returned.</p>
<h2>EXAMPLE</h2>
<pre><code>
CURL handle;
struct curl_slist *slist = NULL;
slist = curl_slist_append(slist, "pragma:");
curl_easy_setopt(handle, CURLOPT_HTTPHEADER, slist);
curl_easy_perform(handle);
curl_slist_free_all(slist); /* free the list again */
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a></code>(3), </p>
<h2>Index</h2>
