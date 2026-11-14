---
title: "curlopt_ftp_create_missing_dirs(3)"
name: "curlopt_ftp_create_missing_dirs"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ftp_create_missing_dirs/"
description: "CURLOPT_FTP_CREATE_MISSING_DIRS – create missing dirs for FTP and SFTP"
---

<p>CURLOPT_FTP_CREATE_MISSING_DIRS &#8211; create missing dirs for FTP and SFTP</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
typedef enum {
 CURLFTP_CREATE_DIR_NONE,
 CURLFTP_CREATE_DIR,
 CURLFTP_CREATE_DIR_RETRY
} curl_ftpcreatedir;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_FTP_CREATE_MISSING_DIRS,
 long create);</pre>
<h2>Description</h2>
<p>Pass a long telling libcurl to <i>create</i> the dir. If the value is <i>CURLFTP_CREATE_DIR</i> (1), libcurl will attempt to create any remote directory that it fails to &quot;move&quot; into. </p>
<p> For FTP requests, that means a CWD command fails. CWD being the command that changes working directory. </p>
<p> For SFTP requests, libcurl will attempt to create the remote directory if it can&#8217;t obtain a handle to the target-location. The creation will fail if a file of the same name as the directory to create already exists or lack of permissions prevents creation. </p>
<p> Setting <i>create</i> to <i>CURLFTP_CREATE_DIR_RETRY</i> (2), tells libcurl to retry the CWD command again if the subsequent MKD command fails. This is especially useful if you&#8217;re doing many simultaneous connections against the same server and they all have this option enabled, as then CWD may first fail but then another connection does MKD before this connection and thus MKD fails but trying CWD works!</p>
<h2>Default</h2>
<p>CURLFTP_CREATE_DIR_NONE (0)</p>
<h2>Protocols</h2>
<p>FTP and SFTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.10.7. SFTP support added in 7.16.3. The retry option was added in 7.19.4.</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if the create value is not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ftp_filemethod/">CURLOPT_FTP_FILEMETHOD</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ftp_use_epsv/">CURLOPT_FTP_USE_EPSV</a></code>(3),</p>
