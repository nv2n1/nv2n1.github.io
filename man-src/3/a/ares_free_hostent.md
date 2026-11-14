---
title: "ares_free_hostent(3)"
name: "ares_free_hostent"
section: "3"
letter: "a"
url: "/docs/linux/man/3-ares_free_hostent/"
description: "ares_free_hostent – Free host structure allocated by ares functions"
---

<h2>NAME</h2>
<p> ares_free_hostent &#8211; Free host structure allocated by ares functions</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;ares.h&gt;
void ares_free_hostent(struct hostent *host)
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <i>ares_free_hostent</i> function frees a <code>struct hostent</code> allocated by one of the functions <i><a href="/docs/linux/man/3-ares_parse_a_reply/">ares_parse_a_reply</a>(3)</i>, <i><a href="/docs/linux/man/3-ares_parse_aaaa_reply/">ares_parse_aaaa_reply</a>(3)</i>, or <i><a href="/docs/linux/man/3-ares_parse_ptr_reply/">ares_parse_ptr_reply</a>(3)</i>.</p>
<h2>NOTES</h2>
<p> It is not necessary (and is not correct) to free the host structure passed to the callback functions for <i><a href="/docs/linux/man/3-ares_gethostbyname/">ares_gethostbyname</a>(3)</i> or <i><a href="/docs/linux/man/3-ares_gethostbyaddr/">ares_gethostbyaddr</a>(3)</i>. c-ares will automatically free such host structures when the callback returns.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ares_parse_a_reply/">ares_parse_a_reply</a></code>(3), <code><a href="/docs/linux/man/3-ares_parse_aaaa_reply/">ares_parse_aaaa_reply</a></code>(3), <code><a href="/docs/linux/man/3-ares_parse_ptr_reply/">ares_parse_ptr_reply</a></code>(3), <code><a href="/docs/linux/man/3-ares_parse_ns_reply/">ares_parse_ns_reply</a></code>(3)</p>
<h2>AUTHOR</h2>
<p> Greg Hudson, MIT Information Systems<br />
 Copyright 1998 by the Massachusetts Institute of Technology. </p>
<h2>Index</h2>
