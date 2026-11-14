---
title: "zproxy(3)"
name: "zproxy"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zproxy/"
description: "zproxy – run a steerable proxy in the background"
---

<p>zproxy &#8211; run a steerable proxy in the background</p>
<h2>Synopsis</h2>
<pre><code>//  Create new zproxy actor instance. The proxy switches messages between
//  a frontend socket and a backend socket; use the FRONTEND and BACKEND
//  commands to configure these:
//
//      zactor_t *proxy = zactor_new (zproxy, NULL);
//
//  Destroy zproxy instance. This destroys the two sockets and stops any
//  message flow between them:
//
//      zactor_destroy (&amp;proxy);
//
//  Note that all zproxy commands are synchronous, so your application always
//  waits for a signal from the actor after each command.
//
//  Enable verbose logging of commands and activity:
//
//      zstr_send (proxy, &quot;VERBOSE&quot;);
//      zsock_wait (proxy);
//
//  Specify frontend socket type -- see zsock_type_str () -- and attach to
//  endpoints, see zsock_attach (). Note that a proxy socket is always
//  serverish:
//
//      zstr_sendx (proxy, &quot;FRONTEND&quot;, &quot;XSUB&quot;, endpoints, NULL);
//      zsock_wait (proxy);
//
//  Specify backend socket type -- see zsock_type_str () -- and attach to
//  endpoints, see zsock_attach (). Note that a proxy socket is always
//  serverish:
//
//      zstr_sendx (proxy, &quot;BACKEND&quot;, &quot;XPUB&quot;, endpoints, NULL);
//      zsock_wait (proxy);
//
//  Capture all proxied messages; these are delivered to the application
//  via an inproc PULL socket that you have already bound to the specified
//  endpoint:
//
//      zstr_sendx (proxy, &quot;CAPTURE&quot;, endpoint, NULL);
//      zsock_wait (proxy);
//
//  Pause the proxy. A paused proxy will cease processing messages, causing
//  them to be queued up and potentially hit the high-water mark on the
//  frontend or backend socket, causing messages to be dropped, or writing
//  applications to block:
//
//      zstr_sendx (proxy, &quot;PAUSE&quot;, NULL);
//      zsock_wait (proxy);
//
//  Resume the proxy. Note that the proxy starts automatically as soon as it
//  has a properly attached frontend and backend socket:
//
//      zstr_sendx (proxy, &quot;RESUME&quot;, NULL);
//      zsock_wait (proxy);
//
//  This is the zproxy constructor as a zactor_fn; the argument is a
//  character string specifying frontend and backend socket types as two
//  uppercase strings separated by a hyphen:
CZMQ_EXPORT void
zproxy(zsock_t *pipe, void *unused);

//  Selftest
CZMQ_EXPORT void
zproxy_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>A zproxy actor switches messages between a frontend and a backend socket. It acts much like the zmq_proxy_steerable method, though it makes benefit of CZMQ&#8217;s facilities, to be somewhat simpler to set-up. </p>
<p> This class replaces zproxy_v2, and is meant for applications that use the CZMQ v3 API (meaning, zsock).</p>
<h2>Example</h2>
<p><code>From zproxy_test method</code>. </p>
<pre><code>//  Create and configure our proxy
zactor_t *proxy = zactor_new(zproxy, NULL);
assert(proxy);
if (verbose) {
    zstr_sendx(proxy, &quot;VERBOSE&quot;, NULL);
    zsock_wait(proxy);
}
zstr_sendx(proxy, &quot;FRONTEND&quot;, &quot;PULL&quot;, &quot;inproc://frontend&quot;, NULL);
zsock_wait(proxy);
zstr_sendx(proxy, &quot;BACKEND&quot;, &quot;PUSH&quot;, &quot;inproc://backend&quot;, NULL);
zsock_wait(proxy);

//  Connect application sockets to proxy
zsock_t *faucet = zsock_new_push(&quot;&gt;inproc://frontend&quot;);
assert(faucet);
zsock_t *sink = zsock_new_pull(&quot;&gt;inproc://backend&quot;);
assert(sink);

//  Send some messages and check they arrived
char *hello, *world;
zstr_sendx(faucet, &quot;Hello&quot;, &quot;World&quot;, NULL);
zstr_recvx(sink, &amp;hello, &amp;world, NULL);
assert(streq(hello, &quot;Hello&quot;));
assert(streq(world, &quot;World&quot;));
zstr_free(&amp;hello);
zstr_free(&amp;world);

//  Test pause/resume functionality
zstr_sendx(proxy, &quot;PAUSE&quot;, NULL);
zsock_wait(proxy);
zstr_sendx(faucet, &quot;Hello&quot;, &quot;World&quot;, NULL);
zsock_set_rcvtimeo(sink, 100);
zstr_recvx(sink, &amp;hello, &amp;world, NULL);
assert(!hello &amp;&amp; !world);

zstr_sendx(proxy, &quot;RESUME&quot;, NULL);
zsock_wait(proxy);
zstr_recvx(sink, &amp;hello, &amp;world, NULL);
assert(streq(hello, &quot;Hello&quot;));
assert(streq(world, &quot;World&quot;));
zstr_free(&amp;hello);
zstr_free(&amp;world);

//  Test capture functionality
zsock_t *capture = zsock_new_pull(&quot;inproc://capture&quot;);
assert(capture);

//  Switch on capturing, check that it works
zstr_sendx(proxy, &quot;CAPTURE&quot;, &quot;inproc://capture&quot;, NULL);
zsock_wait(proxy);
zstr_sendx(faucet, &quot;Hello&quot;, &quot;World&quot;, NULL);
zstr_recvx(sink, &amp;hello, &amp;world, NULL);
assert(streq(hello, &quot;Hello&quot;));
assert(streq(world, &quot;World&quot;));
zstr_free(&amp;hello);
zstr_free(&amp;world);

zstr_recvx(capture, &amp;hello, &amp;world, NULL);
assert(streq(hello, &quot;Hello&quot;));
assert(streq(world, &quot;World&quot;));
zstr_free(&amp;hello);
zstr_free(&amp;world);

zsock_destroy(&amp;faucet);
zsock_destroy(&amp;sink);
zsock_destroy(&amp;capture);
zactor_destroy(&amp;proxy);
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
