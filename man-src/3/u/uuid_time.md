---
title: "uuid_time(3)"
name: "uuid_time"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uuid_time/"
description: "uuid_time – extract the time at which the UUID was created"
---

<p>uuid_time &#8211; extract the time at which the UUID was created</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;uuid.h&gt;

time_t uuid_time(uuid_t uu, struct timeval *ret_tv)</code></pre>
<h2>Description</h2>
<p>The <code>uuid_time</code> function extracts the time at which the supplied time-based UUID <i>uu</i> was created. Note that the UUID creation time is only encoded within certain types of UUIDs. This function can only reasonably expect to extract the creation time for UUIDs created with the <code><a href="/docs/linux/man/3-uuid_generate_time/">uuid_generate_time</a></code>(3) and <code><a href="/docs/linux/man/3-uuid_generate_time_safe/">uuid_generate_time_safe</a></code>(3) functions. It may or may not work with UUIDs created by other mechanisms.</p>
<h2>Return Values</h2>
<p>The time at which the UUID was created, in seconds since January 1, 1970 GMT (the epoch), is returned (see <code><a href="/docs/linux/man/2-time/">time</a></code>(2)). The time at which the UUID was created, in seconds and microseconds since the epoch, is also stored in the location pointed to by <i>ret_tv</i> (see <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2)).</p>
<h2>Author</h2>
<p>Theodore Y. Ts&#8217;o</p>
<h2>Availability</h2>
<p><code>libuuid</code> is part of the util-linux package since version 2.15.1 and is available from <a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/.">https://www.kernel.org/pub/linux/utils/util-linux/.</a></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uuid/">uuid</a></code>(3), <code><a href="/docs/linux/man/3-uuid_clear/">uuid_clear</a></code>(3), <code><a href="/docs/linux/man/3-uuid_compare/">uuid_compare</a></code>(3), <code><a href="/docs/linux/man/3-uuid_copy/">uuid_copy</a></code>(3), <code><a href="/docs/linux/man/3-uuid_generate/">uuid_generate</a></code>(3), <code><a href="/docs/linux/man/3-uuid_is_null/">uuid_is_null</a></code>(3), <code><a href="/docs/linux/man/3-uuid_parse/">uuid_parse</a></code>(3), <code><a href="/docs/linux/man/3-uuid_unparse/">uuid_unparse</a></code>(3) </p>
