---
title: "curlopt_ftpport(3)"
name: "curlopt_ftpport"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftpport/"
description: "CURLOPT_FTPPORT – make FTP transfer active"
---

<p>CURLOPT_FTPPORT &#8211; make FTP transfer active</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTPPORT, char *spec);</p>
<h2>Description</h2>
<p>Pass a pointer to a zero terminated string as parameter. It specifies that the FTP transfer will be made actively and the given string will be used to get the IP address to use for the FTP PORT instruction. </p>
<p> The PORT instruction tells the remote server to connect to our specified IP address. The string may be a plain IP address, a host name, a network interface name (under Unix) or just a &#8216;-&#8216; symbol to let the library use your system&#8217;s default IP address. Default FTP operations are passive, and thus won&#8217;t use PORT. </p>
<p> The address can be followed by a &#8216;:&#8217; to specify a port, optionally followed by a &#8216;-&#8216; to specify a port range. If the port specified is 0, the operating system will pick a free port. If a range is provided and all ports in the range are not available, libcurl will report CURLE_FTP_PORT_FAILED for the handle. Invalid port/range settings are ignored. IPv6 addresses followed by a port or portrange have to be in brackets. IPv6 addresses without port/range specifier can be in brackets. </p>
<p> Examples with specified ports: </p>
<pre> eth0:0
 192.168.1.2:32000-33000
 curl.se:32123
 [::1]:1234-4567</pre>
<p>You disable PORT again and go back to using the passive version by setting this option to NULL.</p>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Port range support was added in 7.19.5</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, CURLE_UNKNOWN_OPTION if not, or CURLE_OUT_OF_MEMORY if there was insufficient heap space.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_use_eprt/">CURLOPT_FTP_USE_EPRT</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_use_epsv/">CURLOPT_FTP_USE_EPSV</a></code>(3),</p>
