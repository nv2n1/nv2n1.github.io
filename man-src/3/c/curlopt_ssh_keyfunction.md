---
title: "curlopt_ssh_keyfunction(3)"
name: "curlopt_ssh_keyfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ssh_keyfunction/"
description: "CURLOPT_SSH_KEYFUNCTION – callback for known host matching logic"
---

<p>CURLOPT_SSH_KEYFUNCTION &#8211; callback for known host matching logic</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
enum curl_khstat {
 CURLKHSTAT_FINE_ADD_TO_FILE,
 CURLKHSTAT_FINE,
 CURLKHSTAT_REJECT, /* reject the connection, return an error */
 CURLKHSTAT_DEFER, /* do not accept it, but we can't answer right
 now so this causes a CURLE_DEFER error but
 otherwise the connection will be left intact
 etc */
};
enum curl_khmatch {
 CURLKHMATCH_OK, /* match */
 CURLKHMATCH_MISMATCH, /* host found, key mismatch! */
 CURLKHMATCH_MISSING, /* no matching host/key found */
};
struct curl_khkey {
 const char *key; /* points to a zero-terminated string encoded with
 base64 if len is zero, otherwise to the &quot;raw&quot;
 data */
 size_t len;
 enum curl_khtype keytype;
};
int ssh_keycallback(CURL *easy,
 const struct curl_khkey *knownkey,
 const struct curl_khkey *foundkey,
 enum curl_khmatch,
 void *clientp);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_SSH_KEYFUNCTION,
 ssh_keycallback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> It gets called when the known_host matching has been done, to allow the application to act and decide for libcurl how to proceed. The callback will only be called if <i><a href="/docs/linux/man/3-curlopt_ssh_knownhosts/">CURLOPT_SSH_KNOWNHOSTS</a>(3)</i> is also set. </p>
<p> This callback function gets passed the CURL handle, the key from the known_hosts file <i>knownkey</i>, the key from the remote site <i>foundkey</i>, info from libcurl on the matching status and a custom pointer (set with <i><a href="/docs/linux/man/3-curlopt_ssh_keydata/">CURLOPT_SSH_KEYDATA</a>(3)</i>). It MUST return one of the following return codes to tell libcurl how to act: </p>
<dl COMPACT>
<dt>CURLKHSTAT_FINE_ADD_TO_FILE</p>
<dd>The host+key is accepted and libcurl will append it to the known_hosts file before continuing with the connection. This will also add the host+key combo to the known_host pool kept in memory if it wasn&#8217;t already present there. The adding of data to the file is done by completely replacing the file with a new copy, so the permissions of the file must allow this.</p>
<dt>CURLKHSTAT_FINE</p>
<dd>The host+key is accepted libcurl will continue with the connection. This will also add the host+key combo to the known_host pool kept in memory if it wasn&#8217;t already present there.</p>
<dt>CURLKHSTAT_REJECT</p>
<dd>The host+key is rejected. libcurl will deny the connection to continue and it will be closed.</p>
<dt>CURLKHSTAT_DEFER</p>
<dd>The host+key is rejected, but the SSH connection is asked to be kept alive. This feature could be used when the app wants to somehow return back and act on the host+key situation and then retry without needing the overhead of setting it up from scratch again.</dl>
<h2>Default</h2>
<p>NULL</p>
<h2>Protocols</h2>
<p>SFTP and SCP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.6</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ssh_keydata/">CURLOPT_SSH_KEYDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_ssh_knownhosts/">CURLOPT_SSH_KNOWNHOSTS</a></code>(3),</p>
