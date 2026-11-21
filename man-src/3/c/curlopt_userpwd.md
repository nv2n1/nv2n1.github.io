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
<p> To specify the domain name use either Down-Level Logon Name or UPN (User Principal Name) formats. For example, EXAMPLE\user and user [at] example.com respectively. </p>
<p> Some HTTP servers (on Windows) support inclusion of the domain for Basic authentication as well. </p>
<p> When using HTTP and <i><a href="/docs/linux/man/3-CURLOPT_FOLLOWLOCATION/">CURLOPT_FOLLOWLOCATION</a>(3)</i>, libcurl might perform several requests to possibly different hosts. libcurl will only send this user and password information to hosts using the initial host name (unless <i><a href="/docs/linux/man/3-CURLOPT_UNRESTRICTED_AUTH/">CURLOPT_UNRESTRICTED_AUTH</a>(3)</i> is set), so if libcurl follows locations to other hosts it will not send the user and password to those. This is enforced to prevent accidental information leakage. </p>
<p> Use <i><a href="/docs/linux/man/3-CURLOPT_HTTPAUTH/">CURLOPT_HTTPAUTH</a>(3)</i> to specify the authentication method for HTTP based connections or <i><a href="/docs/linux/man/3-CURLOPT_LOGIN_OPTIONS/">CURLOPT_LOGIN_OPTIONS</a>(3)</i> to control IMAP, POP3 and SMTP options. </p>
<p> The user and password strings are not URL decoded, so there&#8217;s no way to send in a user name containing a colon using this option. Use <i><a href="/docs/linux/man/3-CURLOPT_USERNAME/">CURLOPT_USERNAME</a>(3)</i> for that, or include it in the URL.  </p>
<h2>DEFAULT</h2>
<p> NULL  </p>
<h2>PROTOCOLS</h2>
<p> Most  </p>
<h2>EXAMPLE</h2>
<p> TODO  </p>
<h2>AVAILABILITY</h2>
<p> Always  </p>
<h2>RETURN VALUE</h2>
<p> Returns CURLE_OK on success or CURLE_OUT_OF_MEMORY if there was insufficient heap space.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-CURLOPT_USERNAME/">CURLOPT_USERNAME</a></code>(3), <code><a href="/docs/linux/man/3-CURLOPT_PASSWORD/">CURLOPT_PASSWORD</a></code>(3), </p>
<h2>Index</h2>
