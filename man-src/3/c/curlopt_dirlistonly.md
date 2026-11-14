---
title: "curlopt_dirlistonly(3)"
name: "curlopt_dirlistonly"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_dirlistonly/"
description: "CURLOPT_DIRLISTONLY – ask for names only in a directory listing"
---

<p>CURLOPT_DIRLISTONLY &#8211; ask for names only in a directory listing</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_DIRLISTONLY, long listonly);</p>
<h2>Description</h2>
<p>For FTP and SFTP based URLs a parameter set to 1 tells the library to list the names of files in a directory, rather than performing a full directory listing that would normally include file sizes, dates etc. </p>
<p> For POP3 a parameter of 1 tells the library to list the email message or messages on the POP3 server. This can be used to change the default behaviour of libcurl, when combined with a URL that contains a message ID, to perform a &quot;scan listing&quot; which can then be used to determine the size of an email. </p>
<p> Note: For FTP this causes a NLST command to be sent to the FTP server. Beware that some FTP servers list only files in their response to NLST; they might not include subdirectories and symbolic links. </p>
<p> Setting this option to 1 also implies a directory listing even if the URL doesn&#8217;t end with a slash, which otherwise is necessary. </p>
<p> Do NOT use this option if you also use <i><a href="/docs/linux/man/3-curlopt_wildcardmatch/">CURLOPT_WILDCARDMATCH</a>(3)</i> as it will effectively break that feature then.</p>
<h2>Default</h2>
<p>0, disabled</p>
<h2>Protocols</h2>
<p>FTP, SFTP and POP3</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>This option was known as CURLOPT_FTPLISTONLY up to 7.16.4. POP3 is supported since 7.21.5.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_customrequest/">CURLOPT_CUSTOMREQUEST</a></code>(3),</p>
