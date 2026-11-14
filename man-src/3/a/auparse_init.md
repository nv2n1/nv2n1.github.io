---
title: "auparse_init(3)"
name: "auparse_init"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_init/"
description: "auparse_init – initialize an instance of the audit parsing library"
---

<h2>NAME</h2>
<p> auparse_init &#8211; initialize an instance of the audit parsing library</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> auparse_state_t *auparse_init(ausource_t source, const void *b); </p>
<h2>DESCRIPTION</h2>
<p> auparse_init initializes an instance of the audit parsing library. The function returns an opaque pointer to the parser&#8217;s internal state. It is used in subsequent calls to the library so. The source variable determines where the library looks for data. Legal values can be: </p>
<pre>
        AUSOURCE_LOGS - use audit logs
        AUSOURCE_FILE - use a file
        AUSOURCE_FILE_ARRAY - use several files
        AUSOURCE_BUFFER - use a buffer
        AUSOURCE_BUFFER_ARRAY - use an array of buffers
        AUSOURCE_DESCRIPTOR - use a particular descriptor
        AUSOURCE_FILE_POINTER - use a stdio FILE pointer
        AUSOURCE_FEED - feed data to parser with auparse_feed()
</pre>
<p> The pointer &#8216;b&#8217; is used to set the file name, array of filenames, the buffer address, or an array of pointers to buffers, or the descriptor number based on what source is given. When the data source is an array of files or buffers, you would create an array of pointers with the last one being a NULL pointer. Buffers should be NUL terminated. </p>
<h2>RETURN VALUE</h2>
<p> Returns a NULL pointer if an error occurs; otherwise, the return value is an opaque pointer to the parser&#8217;s internal state. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_reset/">auparse_reset</a></code>(3), <code><a href="/docs/linux/man/3-auparse_destroy/">auparse_destroy</a></code>(3). <code><a href="/docs/linux/man/3-auparse_feed/">auparse_feed</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
