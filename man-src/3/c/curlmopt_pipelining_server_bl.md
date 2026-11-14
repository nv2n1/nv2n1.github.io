---
title: "curlmopt_pipelining_server_bl(3)"
name: "curlmopt_pipelining_server_bl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_pipelining_server_bl/"
description: "CURLMOPT_PIPELINING_SERVER_BL – pipelining server blacklist"
---

<p>CURLMOPT_PIPELINING_SERVER_BL &#8211; pipelining server blacklist</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_PIPELINING_SERVER_BL, char **servers);</p>
<h2>Description</h2>
<p>Pass a <code>servers</code> array of char *, ending with a NULL entry. This is a list of server types prefixes (in the Server: HTTP header) that are blacklisted from pipelining, i.e server types that are known to not support HTTP pipelining. The array is copied by libcurl. </p>
<p> Note that the comparison matches if the Server: header begins with the string in the blacklist, i.e &quot;Server: Ninja 1.2.3&quot; and &quot;Server: Ninja 1.4.0&quot; can both be blacklisted by having &quot;Ninja&quot; in the backlist. </p>
<p> Pass a NULL pointer to clear the blacklist.</p>
<h2>Default</h2>
<p>The default value is NULL, which means that there is no blacklist.</p>
<h2>Protocols</h2>
<h2>Example</h2>
<pre> server_blacklist[] =
 {
 &quot;Microsoft-IIS/6.0&quot;,
 &quot;nginx/0.8.54&quot;,
 NULL
 };
 curl_multi_setopt(m, CURLMOPT_PIPELINE_SERVER_BL, server_blacklist);</pre>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_pipelining_site_bl/">CURLMOPT_PIPELINING_SITE_BL</a></code>(3),</p>
