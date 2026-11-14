---
title: "curlopt_quote(3)"
name: "curlopt_quote"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_quote/"
description: "CURLOPT_QUOTE – (S)FTP commands to run before transfer"
---

<p>CURLOPT_QUOTE &#8211; (S)FTP commands to run before transfer</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_QUOTE, struct curl_slist *cmds);</p>
<h2>Description</h2>
<p>Pass a pointer to a linked list of FTP or SFTP commands to pass to the server prior to your request. This will be done before any other commands are issued (even before the CWD command for FTP). The linked list should be a fully valid list of &#8216;struct curl_slist&#8217; structs properly filled in with text strings. Use <i><a href="/docs/linux/man/3-curl_slist_append/">curl_slist_append</a>(3)</i> to append strings (commands) to the list, and clear the entire list afterwards with <i><a href="/docs/linux/man/3-curl_slist_free_all/">curl_slist_free_all</a>(3)</i>. Disable this operation again by setting a NULL to this option. When speaking to a FTP server, prefix the command with an asterisk (*) to make libcurl continue even if the command fails as by default libcurl will stop at first failure. </p>
<p> The set of valid FTP commands depends on the server (see RFC959 for a list of mandatory commands). </p>
<p> The valid SFTP commands are:</p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>chgrp group file</p>
<dd>The chgrp command sets the group ID of the file named by the file operand to the group ID specified by the group operand. The group operand is a decimal integer group ID.</p>
<dt>chmod mode file</p>
<dd>The chmod command modifies the file mode bits of the specified file. The mode operand is an octal integer mode number.</p>
<dt>chown user file</p>
<dd>The chown command sets the owner of the file named by the file operand to the user ID specified by the user operand. The user operand is a decimal integer user ID.</p>
<dt>ln source_file target_file</p>
<dd>The ln and symlink commands create a symbolic link at the target_file location pointing to the source_file location.</p>
<dt>mkdir directory_name</p>
<dd>The mkdir command creates the directory named by the directory_name operand.</p>
<dt>pwd</p>
<dd>The pwd command returns the absolute pathname of the current working directory.</p>
<dt>rename source target</p>
<dd>The rename command renames the file or directory named by the source operand to the destination path named by the target operand.</p>
<dt>rm file</p>
<dd>The rm command removes the file specified by the file operand.</p>
<dt>rmdir directory</p>
<dd>The rmdir command removes the directory entry specified by the directory operand, provided it is empty.</p>
<dt>symlink source_file target_file</p>
<dd>See ln.</dl>
</dl>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SFTP and FTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>SFTP support added in 7.16.3. *-prefix for SFTP added in 7.24.0</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_postquote/">CURLOPT_POSTQUOTE</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_prequote/">CURLOPT_PREQUOTE</a></code>(3),</p>
