---
title: "upscli_splitname(3)"
name: "upscli_splitname"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_splitname/"
description: "upscli_splitname – split a UPS definition into its components"
---

<p>upscli_splitname &#8211; split a UPS definition into its components</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;</code></pre>
<pre>int upscli_splitname(const char *buf, char **upsname,
 char **hostname, int *port)</pre>
<h2>Description</h2>
<p>The <code>upscli_splitname()</code> function takes a pointer to the raw UPS definition <i>buf</i> and returns pointers to dynamically allocated memory in <i>upsname</i> and <i>hostname</i>. It also copies the port number into <i>port</i>.</p>
<h2>Formatting</h2>
<p>A UPS definition is specified according to this format: </p>
<dl>
<dd>
<pre>&lt;upsname&gt;[@&lt;hostname&gt;[:&lt;port&gt;]]</pre>
</dl>
<p> When the UPS name is not given, this function will print an error to stderr and return -1 without changing anything. </p>
<p> Definitions without an explicit port value receive the default value of 3493. The default hostname is &quot;localhost&quot;.</p>
<h2>Memory Usage</h2>
<p>You must <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the pointers to <i>upsname</i> and <i>hostname</i> when you are done with them to avoid memory leaks.</p>
<h2>Return Value</h2>
<p>The <code>upscli_splitname()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitaddr/">upscli_splitaddr</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
