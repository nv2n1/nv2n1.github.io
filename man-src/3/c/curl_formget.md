---
title: "curl_formget(3)"
name: "curl_formget"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_formget/"
description: "curl_formget – serialize a previously built multipart/formdata HTTP POST chain"
---

<h2>NAME</h2>
<p> curl_formget &#8211; serialize a previously built multipart/formdata HTTP POST chain</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;curl/curl.h&gt;
void curl_formget(struct curl_httppost *form, void *userp,
                  curl_formget_callback append);
</code></pre>
<h2>DESCRIPTION</h2>
<p> curl_formget() is used to serialize data previously built/appended with <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i>. Accepts a void pointer as second argument named <i>userp</i> which will be passed as the first argument to the curl_formget_callback function. </p>
<p> <code>typedef size_t (*curl_formget_callback)(void *</code><i>userp,</i><code> const char *</code><i>buf,</i> <code> size_t </code><i>len</i><code>);</code> </p>
<p> The curl_formget_callback will be executed for each part of the HTTP POST chain. The character buffer passed to the callback must not be freed. The callback should return the buffer length passed to it on success. </p>
<p> If the <code>CURLFORM_STREAM</code> option is used in the formpost, it will prevent <i><a href="/docs/linux/man/3-curl_formget/">curl_formget</a>(3)</i> from working until you&#8217;ve performed the actual HTTP request as only then will libcurl get the actual read callback to use!</p>
<h2>RETURN VALUE</h2>
<p> 0 means everything was ok, non-zero means an error occurred</p>
<h2>EXAMPLE</h2>
<pre><code>
size_t print_httppost_callback(void *arg, const char *buf, size_t len)
{
    fwrite(buf, len, 1, stdout);
    (*(size_t *)arg) += len;
    return len;
}
size_t print_httppost(struct curl_httppost *post)
{
    size_t total_size = 0;
    if (curl_formget(post, &amp;total_size, print_httppost_callback)) {
        return (size_t)-1;
    }
    return total_size;
}
</code></pre>
<h2>AVAILABILITY</h2>
<p> This function was added in libcurl 7.15.5</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a></code>(3) </p>
<h2>Index</h2>
