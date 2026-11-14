---
title: "libpowerman(3)"
name: "libpowerman"
section: "3"
letter: "l"
url: "/docs/linux/man/3-libpowerman/"
description: "libpowerman – PowerMan Client API"
---

<h2 class="name">NAME</h2>
<p> libpowerman &#8211; PowerMan Client API</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;libpowerman.h&gt;
pm_err_t pm_connect(char *server, void *arg, pm_handle_t *hp,
                    int flags);
void pm_disconnect(pm_handle_t h);
pm_err_t pm_node_on(pm_handle_t h, char *node);
pm_err_t pm_node_off(pm_handle_t h, char *node);
pm_err_t pm_node_cycle(pm_handle_t h, char *node);
pm_err_t pm_node_status(pm_handle_t h, char *node,
                        pm_node_state_t sp);
pm_err_t pm_node_iterator_create(pm_handle_t h,
                                 pm_node_iterator_t *ip);
void pm_node_iterator_destroy(pm_node_iterator_t i);
char *pm_node_next(pm_node_iterator_t i);
void pm_node_iterator_reset(pm_node_iterator_t i);
char *pm_strerror(pm_err_t err, char *str, int len);
cc... - lpowerman
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>pm_connect</code>() function establishes a connection with <i>server</i>, a string containing <i>host[:port]</i> or NULL for defaults; and returns a handle in <i>hp</i>. The <i>arg</i> parameter is currently unused. The <i>flags</i> parameter should be zero or one or more logically-OR&#8217;ed flags:</p>
<dl>
<dt><code>PM_CONN_INET6</code></p>
<dd> Establish connection to the powerman server using (only) IPv6 protocol. Without this flag, any available address family will be used.</dl>
<p> The <code>pm_disconnect</code>() function tears down the server connection and frees storage associated with handle <i>h</i>. </p>
<p> The <code>pm_node_on</code>(), <code>pm_node_off</code>(), and <code>pm_node_cycle</code>() functions issue on, off, and cycle commands acting on <i>node</i> to the server on handle <i>h</i>. </p>
<p> The <code>pm_node_status</code>() function issues a status query acting on <i>node</i> to the server on handle <i>h</i>. The result is resturned in <i>sp</i> which will be one of the values:</p>
<dl>
<dt><code>PM_ON</code></p>
<dd> Node is powered on.</p>
<dt><code>PM_OFF</code></p>
<dd> Node is powered off.</p>
<dt><code>PM_UNKNOWN</code></p>
<dd> Node state is unknown. Some devices may return this even when the query is successful, for example X10 devices controlled by <code>plmpower</code>.</dl>
<p> To use the above functions you must know the name of the node you wish to control. Calling <code>pm_node_iterator_create</code>() on handle <i>h</i> returns an iterator <i>ip</i> which can be used to walk the list of valid node names. <code>pm_node_next</code>() returns the next node in the list, or NULL when the end of the list is reached. <code>pm_node_iterator_reset</code>() rewinds iterator <i>i</i> to the beginning of the list. Finally, <code>pm_node_iterator_destroy</code>() destroys an iterator and reclaims its storage. </p>
<h2>RETURN VALUE</h2>
<p> Most functions have a return type of <i>pm_err_t</i>. <code>pm_strerror</code>() is available to convert an error code <i>err</i> to a human-readable string using storage <i>str</i> of length <i>len</i> passed in by the caller. </p>
<h2>ERRORS</h2>
<dl>
<dt><code>PM_ESUCCESS</code></p>
<dd> Success.</p>
<dt><code>PM_ERRNOVALID</code></p>
<dd> System call failed, see system errno.</p>
<dt><code>PM_ENOADDR</code></p>
<dd> Failed to get address info for server.</p>
<dt><code>PM_ECONNECT</code></p>
<dd> Connect failed.</p>
<dt><code>PM_ENOMEM</code></p>
<dd> Out of memory.</p>
<dt><code>PM_EBADHAND</code></p>
<dd> Bad server handle.</p>
<dt><code>PM_EBADARG</code></p>
<dd> Bad argument.</p>
<dt><code>PM_ESERVEREOF</code></p>
<dd> Received unexpected EOF from server.</p>
<dt><code>PM_ESERVERPARSE</code></p>
<dd> Received unexpected response from server.</p>
<dt><code>PM_EUNKNOWN</code></p>
<dd> Server responded with &#8220;unknown command&#8221;.</p>
<dt><code>PM_EPARSE</code></p>
<dd> Server responded with &#8220;parse error&#8221;.</p>
<dt><code>PM_ETOOLONG</code></p>
<dd> Server responded with &#8220;command too long&#8221;.</p>
<dt><code>PM_EINTERNAL</code></p>
<dd> Server responed with &#8220;internal error&#8221;.</p>
<dt><code>PM_EHOSTLIST</code></p>
<dd> Server responded with &#8220;hostlist error&#8221;.</p>
<dt><code>PM_EINPROGRESS</code></p>
<dd> Server responded with &#8220;command in progress&#8221;.</p>
<dt><code>PM_ENOSUCHNODES</code></p>
<dd> Server responded with &#8220;no such nodes&#8221;.</p>
<dt><code>PM_ECOMMAND</code></p>
<dd> Server responded with &#8220;command completed with errors&#8221;.</p>
<dt><code>PM_EQUERY</code></p>
<dd> Server responded with &#8220;query completed with errors&#8221;.</p>
<dt><code>PM_EUNIMPL</code></p>
<dd> Server responded with &#8220;not implemented by device&#8221;. </p>
</dl>
<h2>EXAMPLE</h2>
<p> This example program queries the list of valid nodes and turns them all on. </p>
<pre><code>
#include &lt;libpowerman.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(int argc, char *argv[])
{
    pm_err_t err;
    pm_node_state_t s;
    pm_handle_t h;
    pm_node_iterator_t i;
    char ebuf[64], *node;
    if ((err = pm_connect(NULL, NULL, &amp;h, 0)) != PM_ESUCCESS) {
        fprintf(stderr, "pm_connect: %s
",
                pm_strerror(err, ebuf, sizeof(ebuf)));
        exit(1);
    }
    if ((err = pm_node_iterator_create(h, &amp;i)) != PM_ESUCCESS) {
        fprintf(stderr, "pm_node_iterator_create: %s
",
                pm_strerror(err, ebuf, sizeof(ebuf)));
        exit(1);
    }
    while ((node = pm_node_next(i))) {
        if ((err = pm_node_on(h, node)) != PM_ESUCCESS) {
            fprintf(stderr, "pm_node_on: %s
",
                    pm_strerror(err, ebuf, sizeof(ebuf)));
            exit(1);
        }
    }
    pm_node_iterator_destroy(i);
    pm_disconnect(h);
    exit(0);
}
</code></pre>
<h2>FILES</h2>
<p> /usr/lib/libpowerman.*<br />
 /usr/lib64/libpowerman.*<br />
 /usr/include/libpowerman.h </p>
<h2>ORIGIN</h2>
<p> PowerMan was originally developed by Andrew Uselton on LLNL&#8217;s Linux clusters. This software is open source and distributed under the terms of the GNU GPL. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-powerman/">powerman</a></code>(1), <code><a href="/docs/linux/man/8-powermand/">powermand</a></code>(8), <code><a href="/docs/linux/man/8-httppower/">httppower</a></code>(8), <code><a href="/docs/linux/man/8-plmpower/">plmpower</a></code>(8), <code><a href="/docs/linux/man/8-vpcd/">vpcd</a></code>(8), <code><a href="/docs/linux/man/5-powerman-conf/">powerman.conf</a></code>(5), <code><a href="/docs/linux/man/5-powerman-dev/">powerman.dev</a></code>(5). </p>
<p> <code><a rel="nofollow" href="http://code.google.com/p/powerman">http://code.google.com/p/powerman</a></code> </p>
<h2>Index</h2>
