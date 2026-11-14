---
title: "zmsg(3)"
name: "zmsg"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmsg/"
description: "zmsg – working with multipart messages"
---

<p>zmsg &#8211; working with multipart messages</p>
<h2>Synopsis</h2>
<pre><code>//  Create a new empty message object
CZMQ_EXPORT zmsg_t *
zmsg_new();

//  Destroy a message object and all frames it contains
CZMQ_EXPORT void
zmsg_destroy(zmsg_t **self_p);

//  Receive message from socket, returns zmsg_t object or NULL if the recv
//  was interrupted. Does a blocking recv. If you want to not block then use
//  the zloop class or zmsg_recv_nowait or zmq_poll to check for socket input
//  before receiving.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_recv(void *source);

//  Send message to destination socket, and destroy the message after sending
//  it successfully. If the message has no frames, sends nothing but destroys
//  the message anyhow. Nullifies the caller's reference to the message (as
//  it is a destructor).
CZMQ_EXPORT int
zmsg_send(zmsg_t **self_p, void *dest);

//  Return size of message, i.e. number of frames (0 or more).
CZMQ_EXPORT size_t
zmsg_size(zmsg_t *self);

//  Return total size of all frames in message.
CZMQ_EXPORT size_t
zmsg_content_size(zmsg_t *self);

//  Push frame to the front of the message, i.e. before all other frames.
//  Message takes ownership of frame, will destroy it when message is sent.
//  Returns 0 on success, -1 on error. Deprecates zmsg_push, which did not
//  nullify the caller's frame reference.
CZMQ_EXPORT int
zmsg_prepend(zmsg_t *self, zframe_t **frame_p);

//  Add frame to the end of the message, i.e. after all other frames.
//  Message takes ownership of frame, will destroy it when message is sent.
//  Returns 0 on success. Deprecates zmsg_add, which did not nullify the
//  caller's frame reference.
CZMQ_EXPORT int
zmsg_append(zmsg_t *self, zframe_t **frame_p);

//  Remove first frame from message, if any. Returns frame, or NULL.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zframe_t *
zmsg_pop(zmsg_t *self);

//  Push block of memory to front of message, as a new frame.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_pushmem(zmsg_t *self, const void *src, size_t size);

//  Add block of memory to the end of the message, as a new frame.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_addmem(zmsg_t *self, const void *src, size_t size);

//  Push string as new frame to front of message.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_pushstr(zmsg_t *self, const char *string);

//  Push string as new frame to end of message.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_addstr(zmsg_t *self, const char *string);

//  Push formatted string as new frame to front of message.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_pushstrf(zmsg_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Push formatted string as new frame to end of message.
//  Returns 0 on success, -1 on error.
CZMQ_EXPORT int
zmsg_addstrf(zmsg_t *self, const char *format, ...) CHECK_PRINTF(2);

//  Pop frame off front of message, return as fresh string. If there were
//  no more frames in the message, returns NULL.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT char *
zmsg_popstr(zmsg_t *self);

//  Push encoded message as a new frame. Message takes ownership of
//  submessage, so the original is destroyed in this call. Returns 0 on
//  success, -1 on error.
CZMQ_EXPORT int
zmsg_addmsg(zmsg_t *self, zmsg_t **msg_p);

//  Remove first submessage from message, if any. Returns zmsg_t, or NULL if
//  decoding was not succesfull.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_popmsg(zmsg_t *self);

//  Remove specified frame from list, if present. Does not destroy frame.
CZMQ_EXPORT void
zmsg_remove(zmsg_t *self, zframe_t *frame);

//  Set cursor to first frame in message. Returns frame, or NULL, if the
//  message is empty. Use this to navigate the frames as a list.
CZMQ_EXPORT zframe_t *
zmsg_first(zmsg_t *self);

//  Return the next frame. If there are no more frames, returns NULL. To move
//  to the first frame call zmsg_first(). Advances the cursor.
CZMQ_EXPORT zframe_t *
zmsg_next(zmsg_t *self);

//  Return the last frame. If there are no frames, returns NULL.
CZMQ_EXPORT zframe_t *
zmsg_last(zmsg_t *self);

//  Save message to an open file, return 0 if OK, else -1. The message is
//  saved as a series of frames, each with length and data. Note that the
//  file is NOT guaranteed to be portable between operating systems, not
//  versions of CZMQ. The file format is at present undocumented and liable
//  to arbitrary change.
CZMQ_EXPORT int
zmsg_save(zmsg_t *self, FILE *file);

//  Load/append an open file into message, create new message if
//  null message provided. Returns NULL if the message could not
//  be loaded.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_load(zmsg_t *self, FILE *file);

//  Serialize multipart message to a single buffer. Use this method to send
//  structured messages across transports that do not support multipart data.
//  Allocates and returns a new buffer containing the serialized message.
//  To decode a serialized message buffer, use zmsg_decode ().
CZMQ_EXPORT size_t
zmsg_encode(zmsg_t *self, byte **buffer);

//  Decodes a serialized message buffer created by zmsg_encode () and returns
//  a new zmsg_t object. Returns NULL if the buffer was badly formatted or
//  there was insufficient memory to work.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_decode(const byte *buffer, size_t buffer_size);

//  Create copy of message, as new message object. Returns a fresh zmsg_t
//  object. If message is null, or memory was exhausted, returns null.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_dup(zmsg_t *self);

//  Send message to zsys log sink (may be stdout, or system facility as
//  configured by zsys_set_logstream).
CZMQ_EXPORT void
zmsg_print(zmsg_t *self);

//  Return true if the two messages have the same number of frames and each
//  frame in the first message is identical to the corresponding frame in the
//  other message. As with zframe_eq, return false if either message is NULL.
CZMQ_EXPORT bool
zmsg_eq(zmsg_t *self, zmsg_t *other);

//  Generate a signal message encoding the given status. A signal is a short
//  message carrying a 1-byte success/failure code (by convention, 0 means
//  OK). Signals are encoded to be distinguishable from &quot;normal&quot; messages.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zmsg_new_signal(byte status);

//  Return signal value, 0 or greater, if message is a signal, -1 if not.
CZMQ_EXPORT int
zmsg_signal(zmsg_t *self);

//  Probe the supplied object, and report if it looks like a zmsg_t.
CZMQ_EXPORT bool
zmsg_is(void *self);

//  Self test of this class
CZMQ_EXPORT void
zmsg_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zmsg class provides methods to send and receive multipart messages across 0MQ sockets. This class provides a list-like container interface, with methods to work with the overall container. zmsg_t messages are composed of zero or more zframe_t frames. </p>
<p> Please add @discuss section in ../src/zmsg.c.</p>
<h2>Example</h2>
<p><code>From zmsg_test method</code>. </p>
<pre><code>//  Create two PAIR sockets and connect over inproc
zsock_t *output = zsock_new_pair(&quot;@inproc://zmsg.test&quot;);
assert(output);
zsock_t *input = zsock_new_pair(&quot;&gt;inproc://zmsg.test&quot;);
assert(input);

//  Test send and receive of single-frame message
zmsg_t *msg = zmsg_new();
assert(msg);
zframe_t *frame = zframe_new(&quot;Hello&quot;, 5);
assert(frame);
zmsg_prepend(msg, &amp;frame);
assert(zmsg_size(msg) == 1);
assert(zmsg_content_size(msg) == 5);
rc = zmsg_send(&amp;msg, output);
assert(msg == NULL);
assert(rc == 0);

msg = zmsg_recv(input);
assert(msg);
assert(zmsg_size(msg) == 1);
assert(zmsg_content_size(msg) == 5);
zmsg_destroy(&amp;msg);

//  Test send and receive of multi-frame message
msg = zmsg_new();
assert(msg);
rc = zmsg_addmem(msg, &quot;Frame0&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame1&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame2&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame3&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame4&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame5&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame6&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame7&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame8&quot;, 6);
assert(rc == 0);
rc = zmsg_addmem(msg, &quot;Frame9&quot;, 6);
assert(rc == 0);
zmsg_t *copy = zmsg_dup(msg);
assert(copy);
rc = zmsg_send(&amp;copy, output);
assert(rc == 0);
rc = zmsg_send(&amp;msg, output);
assert(rc == 0);

copy = zmsg_recv(input);
assert(copy);
assert(zmsg_size(copy) == 10);
assert(zmsg_content_size(copy) == 60);
zmsg_destroy(&amp;copy);

msg = zmsg_recv(input);
assert(msg);
assert(zmsg_size(msg) == 10);
assert(zmsg_content_size(msg) == 60);

// create empty file for null test
FILE *file = fopen(&quot;zmsg.test&quot;, &quot;w&quot;);
assert(file);
fclose(file);

file = fopen(&quot;zmsg.test&quot;, &quot;r&quot;);
zmsg_t *null_msg = zmsg_load(NULL, file);
assert(null_msg == NULL);
fclose(file);
remove(&quot;zmsg.test&quot;);

//  Save to a file, read back
file = fopen(&quot;zmsg.test&quot;, &quot;w&quot;);
assert(file);
rc = zmsg_save(msg, file);
assert(rc == 0);
fclose(file);

file = fopen(&quot;zmsg.test&quot;, &quot;r&quot;);
rc = zmsg_save(msg, file);
assert(rc == -1);
fclose(file);
zmsg_destroy(&amp;msg);

file = fopen(&quot;zmsg.test&quot;, &quot;r&quot;);
msg = zmsg_load(NULL, file);
assert(msg);
fclose(file);
remove(&quot;zmsg.test&quot;);
assert(zmsg_size(msg) == 10);
assert(zmsg_content_size(msg) == 60);

//  Remove all frames except first and last
int frame_nbr;
for (frame_nbr = 0; frame_nbr &lt; 8; frame_nbr++) {
    zmsg_first(msg);
    frame = zmsg_next(msg);
    zmsg_remove(msg, frame);
    zframe_destroy(&amp;frame);
}
//  Test message frame manipulation
assert(zmsg_size(msg) == 2);
frame = zmsg_last(msg);
assert(zframe_streq(frame, &quot;Frame9&quot;));
assert(zmsg_content_size(msg) == 12);
frame = zframe_new(&quot;Address&quot;, 7);
assert(frame);
zmsg_prepend(msg, &amp;frame);
assert(zmsg_size(msg) == 3);
rc = zmsg_addstr(msg, &quot;Body&quot;);
assert(rc == 0);
assert(zmsg_size(msg) == 4);
frame = zmsg_pop(msg);
zframe_destroy(&amp;frame);
assert(zmsg_size(msg) == 3);
char *body = zmsg_popstr(msg);
assert(streq(body, &quot;Frame0&quot;));
free(body);
zmsg_destroy(&amp;msg);

//  Test encoding/decoding
msg = zmsg_new();
assert(msg);
byte *blank = (byte *)zmalloc(100000);
assert(blank);
rc = zmsg_addmem(msg, blank, 0);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 1);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 253);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 254);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 255);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 256);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 65535);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 65536);
assert(rc == 0);
rc = zmsg_addmem(msg, blank, 65537);
assert(rc == 0);
free(blank);
assert(zmsg_size(msg) == 9);
byte *buffer;
size_t buffer_size = zmsg_encode(msg, &amp;buffer);
zmsg_destroy(&amp;msg);
msg = zmsg_decode(buffer, buffer_size);
assert(msg);
free(buffer);
zmsg_destroy(&amp;msg);

//  Test submessages
msg = zmsg_new();
assert(msg);
zmsg_t *submsg = zmsg_new();
zmsg_pushstr(msg, &quot;matr&quot;);
zmsg_pushstr(submsg, &quot;joska&quot;);
rc = zmsg_addmsg(msg, &amp;submsg);
assert(rc == 0);
assert(submsg == NULL);
submsg = zmsg_popmsg(msg);
assert(submsg == NULL); // string &quot;matr&quot; is not encoded zmsg_t, so was discarded
submsg = zmsg_popmsg(msg);
assert(submsg);
body = zmsg_popstr(submsg);
assert(streq(body, &quot;joska&quot;));
free(body);
zmsg_destroy(&amp;submsg);
frame = zmsg_pop(msg);
assert(frame == NULL);
zmsg_destroy(&amp;msg);

//  Test comparison of two messages
msg = zmsg_new();
zmsg_addstr(msg, &quot;One&quot;);
zmsg_addstr(msg, &quot;Two&quot;);
zmsg_addstr(msg, &quot;Three&quot;);
zmsg_t *msg_other = zmsg_new();
zmsg_addstr(msg_other, &quot;One&quot;);
zmsg_addstr(msg_other, &quot;Two&quot;);
zmsg_addstr(msg_other, &quot;One-Hundred&quot;);
zmsg_t *msg_dup = zmsg_dup(msg);
zmsg_t *empty_msg = zmsg_new();
zmsg_t *empty_msg_2 = zmsg_new();
assert(zmsg_eq(msg, msg_dup));
assert(!zmsg_eq(msg, msg_other));
assert(zmsg_eq(empty_msg, empty_msg_2));
assert(!zmsg_eq(msg, NULL));
assert(!zmsg_eq(NULL, empty_msg));
assert(!zmsg_eq(NULL, NULL));
zmsg_destroy(&amp;msg);
zmsg_destroy(&amp;msg_other);
zmsg_destroy(&amp;msg_dup);
zmsg_destroy(&amp;empty_msg);
zmsg_destroy(&amp;empty_msg_2);

//  Test signal messages
msg = zmsg_new_signal(0);
assert(zmsg_signal(msg) == 0);
zmsg_destroy(&amp;msg);
msg = zmsg_new_signal(-1);
assert(zmsg_signal(msg) == 255);
zmsg_destroy(&amp;msg);

//  Now try methods on an empty message
msg = zmsg_new();
assert(msg);
assert(zmsg_size(msg) == 0);
assert(zmsg_unwrap(msg) == NULL);
assert(zmsg_first(msg) == NULL);
assert(zmsg_last(msg) == NULL);
assert(zmsg_next(msg) == NULL);
assert(zmsg_pop(msg) == NULL);
//  Sending an empty message is valid and destroys the message
assert(zmsg_send(&amp;msg, output) == 0);
assert(!msg);

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
