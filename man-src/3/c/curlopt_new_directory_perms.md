---
title: "curlopt_new_directory_perms(3)"
name: "curlopt_new_directory_perms"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_new_directory_perms/"
description: "CURLOPT_NEW_DIRECTORY_PERMS – permissions for remotely created directories"
---

<p>CURLOPT_NEW_DIRECTORY_PERMS &#8211; permissions for remotely created directories</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_NEW_DIRECTORY_PERMS,
 long mode);</pre>
<h2>Description</h2>
<p>Pass a long as a parameter, containing the value of the permissions that will be assigned to newly created directories on the remote server. The default value is <i>0755</i>, but any valid value can be used. The only protocols that can use this are <i>sftp://</i>, <i>scp://</i>, and <i>file://</i>.</p>
<h2>Default</h2>
<p>0755</p>
<h2>Protocols</h2>
<p>SFTP, SCP and FILE</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.16.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_new_file_perms/">CURLOPT_NEW_FILE_PERMS</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_upload/">CURLOPT_UPLOAD</a></code>(3),</p>
