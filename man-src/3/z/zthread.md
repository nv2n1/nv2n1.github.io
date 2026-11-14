---
title: "zthread(3)"
name: "zthread"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zthread/"
description: "zthread – working with system threads (deprecated)"
---

<p>zthread &#8211; working with system threads (deprecated)</p>
<h2>Synopsis</h2>
<pre>// Detached threads follow POSIX pthreads API
typedef void *(zthread_detached_fn) (void *args);
// Attached threads get context and pipe from parent
typedef void (zthread_attached_fn) (void *args, zctx_t *ctx, void *pipe);
// Create a detached thread. A detached thread operates autonomously
// and is used to simulate a separate process. It gets no ctx, and no
// pipe.
CZMQ_EXPORT int
 zthread_new (zthread_detached_fn *thread_fn, void *args);
// Create an attached thread. An attached thread gets a ctx and a PAIR
// pipe back to its parent. It must monitor its pipe, and exit if the
// pipe becomes unreadable. Do not destroy the ctx, the thread does this
// automatically when it ends.
CZMQ_EXPORT void *
 zthread_fork (zctx_t *ctx, zthread_attached_fn *thread_fn, void *args);
// Self test of this class
CZMQ_EXPORT void
 zthread_test (bool verbose);</pre>
<h2>Description</h2>
<p>The zthread class wraps OS thread creation. It creates detached threads that look like normal OS threads, or attached threads that share the caller&#8217;s 0MQ context, and get an inproc pipe to talk back to the parent thread. Detached threads create their own 0MQ contexts as needed. NOTE: this class is deprecated in favor of zactor. </p>
<p> We have several use cases for multiple threads. One is to simulate many processes, so we can test 0MQ designs and flows more easily. Another is to create APIs that can send and receive 0MQ messages in the background. </p>
<p> zthread solves these two use cases separately, using the zthread_new and zthead_fork methods respectively. These methods wrap the native system calls needed to start threads, so your code can remain fully portable. </p>
<p> Detached threads follow the POSIX pthreads API; they accept a void * argument and return a void * result (always NULL in our case). </p>
<p> Attached thread receive a void * argument, a zctx_t context, and a pipe socket. The pipe socket is a PAIR socket that is connected back to the caller. When you call zthread_fork, it returns you a PAIR socket that is the other end of this pipe. Thus attached threads can talk back to their parent threads over the pipe. We use this very heavily when making so-called &quot;asynchronous&quot; APIs, which you can see in the Guide examples like <i>clone</i>. </p>
<p> To recap some rules about threading: do not share sockets between threads or your code will crash. You can migrate a socket from one thread to a child thread, if you stop using it in the parent thread immediately after creating the child thread. If you want to connect sockets over inproc:// they must share the same 0MQ context, i.e. be attached threads. You should always use zthread_fork to create an attached thread; it is not sufficient to pass a zctx_t structure to a detached thread (this will crash). </p>
<p> If you want to communicate over ipc:// or tcp:// you may be sharing the same context, or use separate contexts. Thus, every detached thread usually starts by creating its own zctx_t instance.</p>
<h2>Example</h2>
<p><code>From zthread_test method</code>. </p>
<pre><code>static void *
s_test_detached(void *args)
{
    //  Create a socket to check it'll be automatically deleted
    zctx_t *ctx = zctx_new();
    assert(ctx);

    void *push = zsocket_new(ctx, ZMQ_PUSH);
    assert(push);
    zctx_destroy(&amp;ctx);
    return NULL;
}

static void
s_test_attached(void *args, zctx_t *ctx, void *pipe)
{
    //  Create a socket to check it'll be automatically deleted
    zsocket_new(ctx, ZMQ_PUSH);
    assert(ctx);
    //  Wait for our parent to ping us, and pong back
    char *ping = zstr_recv(pipe);
    assert(ping);
    zstr_free(&amp;ping);
    zstr_send(pipe, &quot;pong&quot;);
}

zctx_t *ctx = zctx_new();
assert(ctx);
int rc = 0;

//  Create a detached thread, let it run
rc = zthread_new(s_test_detached, NULL);
assert(rc == 0);
zclock_sleep(100);

//  Create an attached thread, check it's safely alive
void *pipe = zthread_fork(ctx, s_test_attached, NULL);
assert(pipe);
zstr_send(pipe, &quot;ping&quot;);
char *pong = zstr_recv(pipe);
assert(pong);
assert(streq(pong, &quot;pong&quot;));
zstr_free(&amp;pong);

//  Everything should be cleanly closed now
zctx_destroy(&amp;ctx);
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
