---
title: "curlopt_userpwd(3)"
name: "curlopt_userpwd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_userpwd/"
description: "CURLOPT_USERPWD – user name and password to use in authentication"
---

<p>CURLOPT_USERPWD &#8211; user name and password to use in authentication</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_USERPWD, char *userpwd);</p>
<h2>Description</h2>
<p>Pass a char * as parameter, pointing to a zero terminated login details string for the connection. The format of which is: [user name]:[password]. </p>
<p> When using Kerberos V5 authentication with a Windows based server, you should specify the user name part with the domain name in order for the server to successfully obtain a Kerberos Ticket. If you don&#8217;t then the initial part of the authentication handshake may fail. </p>
<p> When using NTLM, the user name can be specified simply as the user name without the domain name should the server be part of a single domain and forest. </p>
<p> To specify the domain name use either Down-Level Logon Name or UPN (User Principal Name) formats. For example, EXAMPLE
