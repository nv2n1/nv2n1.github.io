---
title: "curl_formfree(3)"
name: "curl_formfree"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_formfree/"
description: "curl_formfree – free a previously build multipart/formdata HTTP POST chain"
---

<h2>NAME</h2>
<p> curl_formfree &#8211; free a previously build multipart/formdata HTTP POST chain</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>void curl_formfree(struct curl_httppost *</code><i>form);</i></p>
<h2>DESCRIPTION</h2>
<p> curl_formfree() is used to clean up data previously built/appended with <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i>. This must be called when the data has been used, which typically means after <i><a href="/docs/linux/man/3-curl_easy_perform/">curl_easy_perform</a>(3)</i> has been called. </p>
<p> The pointer to free is the same pointer you passed to the <code>CURLOPT_HTTPPOST</code> option, which is the <i>firstitem</i> pointer from the <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i> invoke(s). </p>
<p> <code>form</code> is the pointer as returned from a previous call to <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i> and may be NULL.</p>
<h2>RETURN VALUE</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a></code>(3) </p>
<h2>Index</h2>
