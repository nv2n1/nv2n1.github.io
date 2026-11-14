---
title: "ziflist(3)"
name: "ziflist"
section: "3"
letter: "z"
url: "/docs/linux/man/3-ziflist/"
description: "ziflist – List of network interfaces available on system"
---

<p>ziflist &#8211; List of network interfaces available on system</p>
<h2>Synopsis</h2>
<pre><code>//  Get a list of network interfaces currently defined on the system
CZMQ_EXPORT ziflist_t *
ziflist_new();

//  Destroy a ziflist instance
CZMQ_EXPORT void
ziflist_destroy(ziflist_t **self_p);

//  Print properties of the ziflist object.
CZMQ_EXPORT void
ziflist_print(ziflist_t *self);

//  Reload network interfaces from system
CZMQ_EXPORT void
ziflist_reload(ziflist_t *self);

//  Return the number of network interfaces on system
CZMQ_EXPORT size_t
ziflist_size(ziflist_t *self);

//  Get first network interface, return NULL if there are none
CZMQ_EXPORT const char *
ziflist_first(ziflist_t *self);

//  Get next network interface, return NULL if we hit the last one
CZMQ_EXPORT const char *
ziflist_next(ziflist_t *self);

//  Return the current interface IP address as a printable string
CZMQ_EXPORT const char *
ziflist_address(ziflist_t *self);

//  Return the current interface broadcast address as a printable string
CZMQ_EXPORT const char *
ziflist_broadcast(ziflist_t *self);

//  Return the current interface network mask as a printable string
CZMQ_EXPORT const char *
ziflist_netmask(ziflist_t *self);

//  Self test of this class.
CZMQ_EXPORT void
ziflist_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The ziflist class takes a snapshot of the network interfaces that the system currently supports (this can change arbitrarily, especially on mobile devices). The caller can then access the network interface information using an iterator that works like zlistx. Only stores those interfaces with broadcast capability, and ignores the loopback interface. </p>
<p> Please add @discuss section in ../src/ziflist.c.</p>
<h2>Example</h2>
<p><code>From ziflist_test method</code>. </p>
<pre><code>ziflist_t *iflist = ziflist_new();
assert(iflist);

size_t items = ziflist_size(iflist);

if (verbose) {
    //        printf (&quot;ziflist: interfaces=%zu
&quot;, ziflist_size (iflist));
    const char *name = ziflist_first(iflist);
    while (name) {
        printf(&quot; - name=%s address=%s netmask=%s broadcast=%s
&quot;,
               name, ziflist_address(iflist), ziflist_netmask(iflist), ziflist_broadcast(iflist));
        name = ziflist_next(iflist);
    }
}
ziflist_reload(iflist);
assert(items == ziflist_size(iflist));
ziflist_destroy(&amp;iflist);
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
