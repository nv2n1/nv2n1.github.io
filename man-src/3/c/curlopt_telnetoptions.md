---
title: "curlopt_telnetoptions(3)"
name: "curlopt_telnetoptions"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_telnetoptions/"
description: "CURLOPT_TELNETOPTIONS – custom telnet options"
---

<p>CURLOPT_TELNETOPTIONS &#8211; custom telnet options</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TELNETOPTIONS,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>struct curl_slist&nbsp;<wbr>*cmds);</p>
<h2>Description</h2>
<p>Provide a pointer to a curl_slist with variables to pass to the telnet negotiations. The variables should be in the format &lt;option=value&gt;. libcurl supports the options &#8216;TTYPE&#8217;, &#8216;XDISPLOC&#8217; and &#8216;NEW_ENV&#8217;. See the TELNET standard for details.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>TELNET</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Along with TELNET</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if TELNET is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_httpheader/">CURLOPT_HTTPHEADER</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_quote/">CURLOPT_QUOTE</a></code>(3),</p>
