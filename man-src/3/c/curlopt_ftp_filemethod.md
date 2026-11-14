---
title: "curlopt_ftp_filemethod(3)"
name: "curlopt_ftp_filemethod"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_filemethod/"
description: "CURLOPT_FTP_FILEMETHOD – select directory traversing method for FTP"
---

<p>CURLOPT_FTP_FILEMETHOD &#8211; select directory traversing method for FTP</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_FILEMETHOD,
 long method);</pre>
<h2>Description</h2>
<p>Pass a long telling libcurl which <i>method</i> to use to reach a file on a FTP(S) server. </p>
<p> This option exists because some server implementations aren&#8217;t compliant to what the standards say should work. </p>
<p> The argument should be one of the following alternatives:</p>
<dl COMPACT>
<dt>CURLFTPMETHOD_MULTICWD</p>
<dd>libcurl does a single CWD operation for each path part in the given URL. For deep hierarchies this means many commands. This is how RFC1738 says it should be done. This is the default but the slowest behavior.</p>
<dt>CURLFTPMETHOD_NOCWD</p>
<dd>libcurl does no CWD at all. libcurl will do SIZE, RETR, STOR etc and give a full path to the server for all these commands. This is the fastest behavior.</p>
<dt>CURLFTPMETHOD_SINGLECWD</p>
<dd>libcurl does one CWD with the full target directory and then operates on the file &quot;normally&quot; (like in the multicwd case). This is somewhat more standards compliant than &#8216;nocwd&#8217; but without the full penalty of &#8216;multicwd&#8217;.</dl>
<h2>Default</h2>
<p>CURLFTPMETHOD_MULTICWD</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.15.1</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftplistonly/">CURLOPT_FTPLISTONLY</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_skip_pasv_ip/">CURLOPT_FTP_SKIP_PASV_IP</a></code>(3),</p>
