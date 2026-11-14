---
title: "zactor(3)"
name: "zactor"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zactor/"
description: "zactor – simple actor framework"
---

<p>zactor &#8211; simple actor framework</p>
<h2>Synopsis</h2>
<pre><code>// Actors get a pipe and arguments from caller
typedef void(zactor_fn)(
    zsock_t *pipe, void *args);

//  Create a new actor passing arbitrary arguments reference.
CZMQ_EXPORT zactor_t *
zactor_new(zactor_fn task, void *args);

//  Destroy an actor.
CZMQ_EXPORT void
zactor_destroy(zactor_t **self_p);

//  Send a zmsg message to the actor, take ownership of the message
//  and destroy when it has been sent.
CZMQ_EXPORT int
zactor_send(zactor_t *self, zmsg_t **msg_p);

//  Receive a zmsg message from the actor. Returns NULL if the actor
//  was interrupted before the message could be received, or if there
//  was a timeout on the actor.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zmsg_t *
zactor_recv(zactor_t *self);

//  Probe the supplied object, and report if it looks like a zactor_t.
CZMQ_EXPORT bool
zactor_is(void *self);

//  Probe the supplied reference. If it looks like a zactor_t instance,
//  return the underlying libzmq actor handle; else if it looks like
//  a libzmq actor handle, return the supplied value.
CZMQ_EXPORT void *
zactor_resolve(void *self);

//  Return the actor's zsock handle. Use this when you absolutely need
//  to work with the zsock instance rather than the actor.
CZMQ_EXPORT zsock_t *
zactor_sock(zactor_t *self);

//  Self test of this class.
CZMQ_EXPORT void
zactor_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zactor class provides a simple actor framework. It replaces the CZMQ zthread class, which had a complex API that did not fit the CLASS standard. A CZMQ actor is implemented as a thread plus a PAIR-PAIR pipe. The constructor and destructor are always synchronized, so the caller can be sure all resources are created, and destroyed, when these calls complete. (This solves a major problem with zthread, that a caller could not be sure when a child thread had finished.) </p>
<p> A zactor_t instance acts like a zsock_t and you can pass it to any CZMQ method that would take a zsock_t argument, including methods in zframe, zmsg, zstr, and zpoller. (zloop somehow escaped and needs catching.) </p>
<p> An actor function MUST call zsock_signal (pipe) when initialized and MUST listen to pipe and exit on $TERM command. </p>
<p> Please add @discuss section in ../src/zactor.c.</p>
<h2>Example</h2>
<p><code>From zactor_test method</code>. </p>
<pre><code>zactor_t *actor = zactor_new(echo_actor, &quot;Hello, World&quot;);
assert(actor);
zstr_sendx(actor, &quot;ECHO&quot;, &quot;This is a string&quot;, NULL);
char *string = zstr_recv(actor);
assert(streq(string, &quot;This is a string&quot;));
free(string);
zactor_destroy(&amp;actor);
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
