---
title: "curlopt_username(3)"
name: "curlopt_username"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_username/"
description: "CURLOPT_USERNAME – user name to use in authentication"
---

<p>CURLOPT_USERNAME &#8211; user name to use in authentication</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_USERNAME,
 char *username);</pre>
<h2>Description</h2>
<p>Pass a char * as parameter, which should be pointing to the zero terminated user name to use for the transfer. </p>
<p> <code><a href="/docs/linux/man/3-curlopt_username/">CURLOPT_USERNAME</a>(3)</code> sets the user name to be used in protocol authentication. You should not use this option together with the (older) <i><a href="/docs/linux/man/3-curlopt_userpwd/">CURLOPT_USERPWD</a>(3)</i> option. </p>
<p> When using Kerberos V5 authentication with a Windows based server, you should include the domain name in order for the server to successfully obtain a Kerberos Ticket. If you don&#8217;t then the initial part of the authentication handshake may fail. </p>
<p> When using NTLM, the user name can be specified simply as the user name without the domain name should the server be part of a single domain and forest. </p>
<p> To include the domain name use either Down-Level Logon Name or UPN (User Principal Name) formats. For example, EXAMPLE
