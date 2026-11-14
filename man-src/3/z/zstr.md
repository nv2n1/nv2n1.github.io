---
title: "zstr(3)"
name: "zstr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zstr/"
description: "zstr – sending and receiving strings"
---

<p>zstr &#8211; sending and receiving strings</p>
<h2>Synopsis</h2>
<pre>// Receive C string from socket. Caller must free returned string using
// zstr_free(). Returns NULL if the context is being terminated or the
// process was interrupted.
CZMQ_EXPORT char *
 zstr_recv (void *source);
// Send a C string to a socket, as a frame. The string is sent without
// trailing null byte; to read this you can use zstr_recv, or a similar
// method that adds a null terminator on the received string. String
// may be NULL, which is sent as &quot;&quot;.
CZMQ_EXPORT int
 zstr_send (void *dest, const char *string);
// Send a C string to a socket, as zstr_send(), with a MORE flag, so that
// you can send further strings in the same multi-part message.
CZMQ_EXPORT int
 zstr_sendm (void *dest, const char *string);
// Send a formatted string to a socket. Note that you should NOT use
// user-supplied strings in the format (they may contain '%' which
// will create security holes).
CZMQ_EXPORT int
 zstr_sendf (void *dest, const char *format, ...);
// Send a formatted string to a socket, as for zstr_sendf(), with a
// MORE flag, so that you can send further strings in the same multi-part
// message.
CZMQ_EXPORT int
 zstr_sendfm (void *dest, const char *format, ...);
// Send a series of strings (until NULL) as multipart data
// Returns 0 if the strings could be sent OK, or -1 on error.
CZMQ_EXPORT int
 zstr_sendx (void *dest, const char *string, ...);
// Receive a series of strings (until NULL) from multipart data.
// Each string is allocated and filled with string data; if there
// are not enough frames, unallocated strings are set to NULL.
// Returns -1 if the message could not be read, else returns the
// number of strings filled, zero or more. Free each returned string
// using zstr_free(). If not enough strings are provided, remaining
// multipart frames in the message are dropped.
CZMQ_EXPORT int
 zstr_recvx (void *source, char **string_p, ...);
// Free a provided string, and nullify the parent pointer. Safe to call on
// a null pointer.
CZMQ_EXPORT void
 zstr_free (char **string_p);
// Self test of this class
CZMQ_EXPORT void
 zstr_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zstr class provides utility functions for sending and receiving C strings across 0MQ sockets. It sends strings without a terminating null, and appends a null byte on received strings. This class is for simple message sending. </p>
<dl>
<dd>
<pre> Memory Wire
 +-------------+---+ +---+-------------+
Send | S t r i n g | 0 | ----&gt; | 6 | S t r i n g |
 +-------------+---+ +---+-------------+</pre>
</dl>
<dl>
<dd>
<pre> Wire Heap
 +---+-------------+ +-------------+---+
Recv | 6 | S t r i n g | ----&gt; | S t r i n g | 0 |
 +---+-------------+ +-------------+---+</pre>
</dl>
<h2>Example</h2>
<p><code>From zstr_test method</code>. </p>
<pre><code>//  Create two PAIR sockets and connect over inproc
zsock_t *output = zsock_new_pair(&quot;@inproc://zstr.test&quot;);
assert(output);
zsock_t *input = zsock_new_pair(&quot;&gt;inproc://zstr.test&quot;);
assert(input);

//  Send ten strings, five strings with MORE flag and then END
int string_nbr;
for (string_nbr = 0; string_nbr &lt; 10; string_nbr++)
    zstr_sendf(output, &quot;this is string %d&quot;, string_nbr);
zstr_sendx(output, &quot;This&quot;, &quot;is&quot;, &quot;almost&quot;, &quot;the&quot;, &quot;very&quot;, &quot;END&quot;, NULL);

//  Read and count until we receive END
string_nbr = 0;
for (string_nbr = 0;; string_nbr++) {
    char *string = zstr_recv(input);
    assert(string);
    if (streq(string, &quot;END&quot;)) {
        zstr_free(&amp;string);
        break;
    }
    zstr_free(&amp;string);
}
assert(string_nbr == 15);

zsock_destroy(&amp;input);
zsock_destroy(&amp;output);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
