---
title: "curlopt_unix_socket_path(3)"
name: "curlopt_unix_socket_path"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_unix_socket_path/"
description: "CURLOPT_UNIX_SOCKET_PATH – set Unix domain socket"
---

<p>CURLOPT_UNIX_SOCKET_PATH &#8211; set Unix domain socket</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_UNIX_SOCKET_PATH, char *path);</p>
<h2>Description</h2>
<p>Enables the use of Unix domain sockets as connection endpoint and sets the path to <i>path</i>. If <i>path</i> is NULL, then Unix domain sockets are disabled. An empty string will result in an error at some point, it will not disable use of Unix domain sockets. </p>
<p> When enabled, cURL will connect to the Unix domain socket instead of establishing a TCP connection to a host. Since no TCP connection is created, cURL does not need to resolve the DNS hostname in the URL. </p>
<p> The maximum path length on Cygwin, Linux and Solaris is 107. On other platforms it might be even less. </p>
<p> Proxy and TCP options such as <code><a href="/docs/linux/man/3-curlopt_tcp_nodelay/">CURLOPT_TCP_NODELAY</a></code>(3) are not supported. Proxy options such as <code><a href="/docs/linux/man/3-curlopt_proxy/">CURLOPT_PROXY</a></code>(3) have no effect either as these are TCP-oriented, and asking a proxy server to connect to a certain Unix domain socket is not possible.</p>
<h2>Default</h2>
<p>Default is NULL, meaning that no Unix domain sockets are used.</p>
<h2>Protocols</h2>
<p>All protocols except for file:// and FTP are supported in theory. HTTP, IMAP, POP3 and SMTP should in particular work (including their SSL/TLS variants).</p>
<h2>Example</h2>
<p>Given that you have an nginx server running, listening on /tmp/nginx.sock, you can request a HTTP resource with: </p>
<pre> curl_easy_setopt(curl_handle, CURLOPT_UNIX_SOCKET_PATH, &quot;/tmp/nginx.sock&quot;);
 curl_easy_setopt(curl_handle, CURLOPT_URL, &quot;<a rel="nofollow" href="http://localhost/">http://localhost/</a>&quot;);</pre>
<p>If you are on Linux and somehow have a need for paths larger than 107 bytes, you could use the proc filesystem to bypass the limitation: </p>
<pre> int dirfd = open(long_directory_path_to_socket, O_DIRECTORY | O_RDONLY);
 char path[108];
 snprintf(path, sizeof(path), &quot;/proc/self/fd/%d/nginx.sock&quot;, dirfd);
 curl_easy_setopt(curl_handle, CURLOPT_UNIX_SOCKET_PATH, path);
 /* Be sure to keep dirfd valid until you discard the handle */</pre>
<h2>Availability</h2>
<p>Since 7.40.0.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_opensocketfunction/">CURLOPT_OPENSOCKETFUNCTION</a></code>(3), <code><a href="/docs/linux/man/7-unix/">unix</a></code>(7),</p>
