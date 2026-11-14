---
title: "curlmopt_pipelining_site_bl(3)"
name: "curlmopt_pipelining_site_bl"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlmopt_pipelining_site_bl/"
description: "CURLMOPT_PIPELINING_SITE_BL – pipelining host blacklist"
---

<p>CURLMOPT_PIPELINING_SITE_BL &#8211; pipelining host blacklist</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLMcode curl_multi_setopt(CURLM *handle, CURLMOPT_PIPELINING_SITE_BL, char **hosts);</p>
<h2>Description</h2>
<p>Pass a <code>hosts</code> array of char *, ending with a NULL entry. This is a list of sites that are blacklisted from pipelining, i.e sites that are known to not support HTTP pipelining. The array is copied by libcurl. </p>
<p> Pass a NULL pointer to clear the blacklist.</p>
<h2>Default</h2>
<p>The default value is NULL, which means that there is no blacklist.</p>
<h2>Protocols</h2>
<p>HTTP(S)</p>
<h2>Example</h2>
<pre> site_blacklist[] =
 {
 &quot;<a rel="nofollow" href="http://www.haxx.se">www.haxx.se</a>&quot;,
 &quot;<a rel="nofollow" href="http://www.example.com">www.example.com</a>:1234&quot;,
 NULL
 };
 curl_multi_setopt(m, CURLMOPT_PIPELINE_SITE_BL, site_blacklist);</pre>
<h2>Availability</h2>
<p>Added in 7.30.0</p>
<h2>Return Value</h2>
<p>Returns CURLM_OK if the option is supported, and CURLM_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlmopt_pipelining/">CURLMOPT_PIPELINING</a></code>(3), <code><a href="/docs/linux/man/3-curlmopt_pipelining_server_bl/">CURLMOPT_PIPELINING_SERVER_BL</a></code>(3),</p>
