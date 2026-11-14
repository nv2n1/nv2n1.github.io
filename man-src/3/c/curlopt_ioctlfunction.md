---
title: "curlopt_ioctlfunction(3)"
name: "curlopt_ioctlfunction"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curlopt_ioctlfunction/"
description: "CURLOPT_IOCTLFUNCTION – callback for I/O operations"
---

<p>CURLOPT_IOCTLFUNCTION &#8211; callback for I/O operations</p>
<h2>Synopsis</h2>
<pre>#include &lt;curl/curl.h&gt;
typedef enum {
 CURLIOE_OK, /* I/O operation successful */
 CURLIOE_UNKNOWNCMD, /* command was unknown to callback */
 CURLIOE_FAILRESTART, /* failed to restart the read */
 CURLIOE_LAST /* never use */
} curlioerr;
typedef enum {
 CURLIOCMD_NOP, /* no operation */
 CURLIOCMD_RESTARTREAD, /* restart the read stream from start */
 CURLIOCMD_LAST /* never use */
} curliocmd;
curlioerr ioctl_callback(CURL *handle, int cmd, void *clientp);
CURLcode curl_easy_setopt(CURL *handle, CURLOPT_IOCTLFUNCTION, ioctl_callback);</pre>
<h2>Description</h2>
<p>Pass a pointer to your callback function, which should match the prototype shown above. </p>
<p> This callback function gets called by libcurl when something special I/O-related needs to be done that the library can&#8217;t do by itself. For now, rewinding the read data stream is the only action it can request. The rewinding of the read data stream may be necessary when doing a HTTP PUT or POST with a multi-pass authentication method. </p>
<p> The callback MUST return <i>CURLIOE_UNKNOWNCMD</i> if the input <i>cmd</i> is not <i>CURLIOCMD_RESTARTREAD</i>. </p>
<p> The <i>clientp</i> argument to the callback is set with the <i><a href="/docs/linux/man/3-curlopt_ioctldata/">CURLOPT_IOCTLDATA</a>(3)</i> option. </p>
<p> This option is deprecated! Do not use it. Use <i><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a>(3)</i> instead to provide seeking! If <i><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a>(3)</i> is set, this parameter will be ignored when seeking.</p>
<h2>Default</h2>
<p>By default, this parameter is set to NULL. Not used.</p>
<h2>Protocols</h2>
<p>Used with HTTP</p>
<h2>Example</h2>
<p>TODO</p>
<h2>Availability</h2>
<p>Added in 7.12.3</p>
<h2>Return Value</h2>
<p>Returns CURLE_OK if the option is supported, and CURLE_UNKNOWN_OPTION if not.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-curlopt_ioctldata/">CURLOPT_IOCTLDATA</a></code>(3), <code><a href="/docs/linux/man/3-curlopt_seekfunction/">CURLOPT_SEEKFUNCTION</a></code>(3),</p>
