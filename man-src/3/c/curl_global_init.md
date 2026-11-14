---
title: "curl_global_init(3)"
name: "curl_global_init"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_global_init/"
description: "curl_global_init – Global libcurl initialisation"
---

<h2>NAME</h2>
<p> curl_global_init &#8211; Global libcurl initialisation</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<p> <code>CURLcode curl_global_init(long </code><i>flags</i><code>);</code></p>
<h2>DESCRIPTION</h2>
<p> This function sets up the program environment that libcurl needs. Think of it as an extension of the library loader. </p>
<p> This function must be called at least once within a program (a program is all the code that shares a memory space) before the program calls any other function in libcurl. The environment it sets up is constant for the life of the program and is the same for every program, so multiple calls have the same effect as one call. </p>
<p> The flags option is a bit pattern that tells libcurl exactly what features to init, as described below. Set the desired bits by ORing the values together. In normal operation, you must specify CURL_GLOBAL_ALL. Don&#8217;t use any other value unless you are familiar with it and mean to control internal operations of libcurl. </p>
<p> <code>This function is not thread safe.</code> You must not call it when any other thread in the program (i.e. a thread sharing the same memory) is running. This doesn&#8217;t just mean no other thread that is using libcurl. Because <i>curl_global_init()</i> calls functions of other libraries that are similarly thread unsafe, it could conflict with any other thread that uses these other libraries. </p>
<p> See the description in <code><a href="/docs/linux/man/3-libcurl/">libcurl</a></code>(3) of global environment requirements for details of how to use this function. </p>
<h2>FLAGS</h2>
<dl>
<dt><code>CURL_GLOBAL_ALL</code></p>
<dd> Initialize everything possible. This sets all known bits.</p>
<dt><code>CURL_GLOBAL_SSL</code></p>
<dd> Initialize SSL</p>
<dt><code>CURL_GLOBAL_WIN32</code></p>
<dd> Initialize the Win32 socket libraries.</p>
<dt><code>CURL_GLOBAL_NOTHING</code></p>
<dd> Initialise nothing extra. This sets no bit.</p>
<dt><code>CURL_GLOBAL_DEFAULT</code></p>
<dd> A sensible default. It will init both SSL and Win32. Right now, this equals the functionality of the <code>CURL_GLOBAL_ALL</code> mask.</p>
<dt><code>CURL_GLOBAL_ACK_EINTR</code></p>
<dd> When this flag is set, curl will acknowledge EINTR condition when connecting or when waiting for data. Otherwise, curl waits until full timeout elapses.</dl>
<h2>RETURN VALUE</h2>
<p> If this function returns non-zero, something went wrong and you cannot use the other curl functions.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_global_init_mem/">curl_global_init_mem</a></code>(3), <code><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a></code>(3), <code><a href="/docs/linux/man/3-curl_easy_init/">curl_easy_init</a></code>(3) <code><a href="/docs/linux/man/3-libcurl/">libcurl</a></code>(3) </p>
<h2>Index</h2>
