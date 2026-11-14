---
title: "upscli_splitaddr(3)"
name: "upscli_splitaddr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-upscli_splitaddr/"
description: "upscli_splitaddr – split a listening address into its components"
---

<p>upscli_splitaddr &#8211; split a listening address into its components</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;upsclient.h&gt;</code></pre>
<pre>int upscli_splitaddr(const char *buf, char **hostname,
 int *port)</pre>
<h2>Description</h2>
<p>The <code>upscli_splitaddr()</code> function takes a pointer to the raw UPS definition <i>buf</i> and returns pointers to dynamically allocated memory in <i>upsname</i> and <i>hostname</i>. It also copies the port number into <i>port</i>.</p>
<h2>Formatting</h2>
<p>A listening address definition is specified according to this format: </p>
<dl>
<dd>
<pre>&lt;hostname&gt;[:&lt;port&gt;]</pre>
</dl>
<p> Definitions without an explicit port value receive the default value of 3493.</p>
<h2>Memory Usage</h2>
<p>You must <code><a href="/docs/linux/man/3-free/">free</a></code>(3) the pointer <i>hostname</i> when you are done with it to avoid memory leaks.</p>
<h2>Return Value</h2>
<p>The <code>upscli_splitaddr()</code> function returns 0 on success, or -1 if an error occurs.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-upscli_fd/">upscli_fd</a></code>(3), <code><a href="/docs/linux/man/3-upscli_get/">upscli_get</a></code>(3), <code><a href="/docs/linux/man/3-upscli_readline/">upscli_readline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_sendline/">upscli_sendline</a></code>(3), <code><a href="/docs/linux/man/3-upscli_splitname/">upscli_splitname</a></code>(3), <code><a href="/docs/linux/man/3-upscli_ssl/">upscli_ssl</a></code>(3), <code><a href="/docs/linux/man/3-upscli_strerror/">upscli_strerror</a></code>(3), <code><a href="/docs/linux/man/3-upscli_upserror/">upscli_upserror</a></code>(3) </p>
