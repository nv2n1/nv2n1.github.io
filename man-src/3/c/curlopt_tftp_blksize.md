---
title: "curlopt_tftp_blksize(3)"
name: "curlopt_tftp_blksize"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_tftp_blksize/"
description: "CURLOPT_TFTP_BLKSIZE – TFTP block size"
---

<p>CURLOPT_TFTP_BLKSIZE &#8211; TFTP block size</p>
<h2>Synopsis</h2>
<p>#include &lt;curl/curl.h&gt; </p>
<p> CURLcode curl_easy_setopt(CURL *handle, CURLOPT_TFTP_BLKSIZE, long blocksize);</p>
<h2>Description</h2>
<p>Specify <i>blocksize</i> to use for TFTP data transmission. Valid range as per RFC2348 is 8-65464 bytes. The default of 512 bytes will be used if this option is not specified. The specified block size will only be used pending support by the remote server. If the server does not return an option acknowledgement or returns an option acknowledgement with no blksize, the default of 512 bytes will be used.</p>
<h2>Default</h2>
<p>512</p>
<h2>Protocols</h2>
<p>TFTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.19.4</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_maxfilesize/">CURLOPT_MAXFILESIZE</a></code>(3),</p>
