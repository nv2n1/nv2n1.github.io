---
title: "curlopt_httppost(3)"
name: "curlopt_httppost"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_httppost/"
description: "CURLOPT_HTTPPOST – specify the multipart formpost content"
---

<p>CURLOPT_HTTPPOST &#8211; specify the multipart formpost content</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_HTTPPOST,
 struct curl_httppost *formpost);</pre>
<h2>Description</h2>
<p>Tells libcurl you want a multipart/formdata HTTP POST to be made and you instruct what data to pass on to the server in the <i>formpost</i> argument. Pass a pointer to a linked list of curl_httppost structs as parameter. The easiest way to create such a list, is to use <i><a href="/docs/linux/man/3-curl_formadd/">curl_formadd</a>(3)</i> as documented. The data in this list must remain intact until you close this curl handle again with <i><a href="/docs/linux/man/3-curl_easy_cleanup/">curl_easy_cleanup</a>(3)</i>. </p>
<p> Using POST with HTTP 1.1 implies the use of a &quot;Expect: 100-continue&quot; header. You can disable this header with <i><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a>(3)</i>. </p>
<p> When setting <i><a href="/docs/linux/man/3-curlopt_httppost/">CURLOPT_HTTPPOST</a>(3)</i>, it will automatically set <i><a href="/docs/linux/man/3-curlopt_nobody/">CURLOPT_NOBODY</a>(3)</i> to 0.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>HTTP</p>
<h2>Example</h2>
<pre>/* Fill in the file upload field. This makes libcurl load data from
 the given file name when curl_easy_perform() is called. */
curl_formadd(&amp;formpost,
 &amp;lastptr,
 CURLFORM_COPYNAME, &quot;sendfile&quot;,
 CURLFORM_FILE, &quot;postit2.c&quot;,
 CURLFORM_END);
/* Fill in the filename field */
curl_formadd(&amp;formpost,
 &amp;lastptr,
 CURLFORM_COPYNAME, &quot;filename&quot;,
 CURLFORM_COPYCONTENTS, &quot;postit2.c&quot;,
 CURLFORM_END);
/* Fill in the submit field too, even if this is rarely needed */
curl_formadd(&amp;formpost,
 &amp;lastptr,
 CURLFORM_COPYNAME, &quot;submit&quot;,
 CURLFORM_COPYCONTENTS, &quot;send&quot;,
 CURLFORM_END);</pre>
<h2>Availability</h2>
<p>As long as HTTP is enabled</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if HTTP is enabled, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postfields/">CURLOPT_POSTFIELDS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_post/">CURLOPT_POST</a></code>(3),</p>
