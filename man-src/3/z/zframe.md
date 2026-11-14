---
title: "zframe(3)"
name: "zframe"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zframe/"
description: "zframe – working with single message frames"
---

<p>zframe &#8211; working with single message frames</p>
<h2>Synopsis</h2>
<pre><code>#define ZFRAME_MORE 1     //
#define ZFRAME_REUSE 2    //
#define ZFRAME_DONTWAIT 4 //

//  Create a new frame. If size is not null, allocates the frame data
//  to the specified size. If additionally, data is not null, copies
//  size octets from the specified data into the frame body.
CZMQ_EXPORT zframe_t *
zframe_new(const void *data, size_t size);

//  Destroy a frame
CZMQ_EXPORT void
zframe_destroy(zframe_t **self_p);

//  Create an empty (zero-sized) frame
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zframe_new_empty();

//  Create a frame with a specified string content.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zframe_from(const char *string);

//  Receive frame from socket, returns zframe_t object or NULL if the recv
//  was interrupted. Does a blocking recv, if you want to not block then use
//  zpoller or zloop.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zframe_recv(void *source);

//  Send a frame to a socket, destroy frame after sending.
//  Return -1 on error, 0 on success.
CZMQ_EXPORT int
zframe_send(zframe_t **self_p, void *dest, int flags);

//  Return number of bytes in frame data
CZMQ_EXPORT size_t
zframe_size(zframe_t *self);

//  Return address of frame data
CZMQ_EXPORT byte *
zframe_data(zframe_t *self);

//  Create a new frame that duplicates an existing frame. If frame is null,
//  or memory was exhausted, returns null.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zframe_dup(zframe_t *self);

//  Return frame data encoded as printable hex string, useful for 0MQ UUIDs.
//  Caller must free string when finished with it.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT char *
zframe_strhex(zframe_t *self);

//  Return frame data copied into freshly allocated string
//  Caller must free string when finished with it.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT char *
zframe_strdup(zframe_t *self);

//  Return TRUE if frame body is equal to string, excluding terminator
CZMQ_EXPORT bool
zframe_streq(zframe_t *self, const char *string);

//  Return frame MORE indicator (1 or 0), set when reading frame from socket
//  or by the zframe_set_more() method
CZMQ_EXPORT int
zframe_more(zframe_t *self);

//  Set frame MORE indicator (1 or 0). Note this is NOT used when sending
//  frame to socket, you have to specify flag explicitly.
CZMQ_EXPORT void
zframe_set_more(zframe_t *self, int more);

//  Return TRUE if two frames have identical size and data
//  If either frame is NULL, equality is always false.
CZMQ_EXPORT bool
zframe_eq(zframe_t *self, zframe_t *other);

//  Set new contents for frame
CZMQ_EXPORT void
zframe_reset(zframe_t *self, const void *data, size_t size);

//  Send message to zsys log sink (may be stdout, or system facility as
//  configured by zsys_set_logstream). Prefix shows before frame, if not null.
CZMQ_EXPORT void
zframe_print(zframe_t *self, const char *prefix);

//  Probe the supplied object, and report if it looks like a zframe_t.
CZMQ_EXPORT bool
zframe_is(void *self);

//  Self test of this class
CZMQ_EXPORT void
zframe_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zframe class provides methods to send and receive single message frames across 0MQ sockets. A <i>frame</i> corresponds to one zmq_msg_t. When you read a frame from a socket, the zframe_more() method indicates if the frame is part of an unfinished multipart message. The zframe_send method normally destroys the frame, but with the ZFRAME_REUSE flag, you can send the same frame many times. Frames are binary, and this class has no special support for text data. </p>
<p> Please add @discuss section in ../src/zframe.c.</p>
<h2>Example</h2>
<p><code>From zframe_test method</code>. </p>
<pre><code>//  Create two PAIR sockets and connect over inproc
zsock_t *output = zsock_new_pair(&quot;@inproc://zframe.test&quot;);
assert(output);
zsock_t *input = zsock_new_pair(&quot;&gt;inproc://zframe.test&quot;);
assert(input);

//  Send five different frames, test ZFRAME_MORE
int frame_nbr;
for (frame_nbr = 0; frame_nbr &lt; 5; frame_nbr++) {
    frame = zframe_new(&quot;Hello&quot;, 5);
    assert(frame);
    rc = zframe_send(&amp;frame, output, ZFRAME_MORE);
    assert(rc == 0);
}
//  Send same frame five times, test ZFRAME_REUSE
frame = zframe_new(&quot;Hello&quot;, 5);
assert(frame);
for (frame_nbr = 0; frame_nbr &lt; 5; frame_nbr++) {
    rc = zframe_send(&amp;frame, output, ZFRAME_MORE + ZFRAME_REUSE);
    assert(rc == 0);
}
assert(frame);
zframe_t *copy = zframe_dup(frame);
assert(zframe_eq(frame, copy));
zframe_destroy(&amp;frame);
assert(!zframe_eq(frame, copy));
assert(zframe_size(copy) == 5);
zframe_destroy(&amp;copy);
assert(!zframe_eq(frame, copy));

//  Test zframe_new_empty
frame = zframe_new_empty();
assert(frame);
assert(zframe_size(frame) == 0);
zframe_destroy(&amp;frame);

//  Send END frame
frame = zframe_new(&quot;NOT&quot;, 3);
assert(frame);
zframe_reset(frame, &quot;END&quot;, 3);
char *string = zframe_strhex(frame);
assert(streq(string, &quot;454E44&quot;));
free(string);
string = zframe_strdup(frame);
assert(streq(string, &quot;END&quot;));
free(string);
rc = zframe_send(&amp;frame, output, 0);
assert(rc == 0);

//  Read and count until we receive END
frame_nbr = 0;
for (frame_nbr = 0;; frame_nbr++) {
    zframe_t *frame = zframe_recv(input);
    if (zframe_streq(frame, &quot;END&quot;)) {
        zframe_destroy(&amp;frame);
        break;
    }
    assert(zframe_more(frame));
    zframe_set_more(frame, 0);
    assert(zframe_more(frame) == 0);
    zframe_destroy(&amp;frame);
}
assert(frame_nbr == 10);

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
