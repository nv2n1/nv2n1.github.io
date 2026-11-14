---
title: "zmq_poll(3)"
name: "zmq_poll"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zmq_poll/"
description: "zmq_poll – input/output multiplexing"
---

<p>zmq_poll &#8211; input/output multiplexing</p>
<h2>Synopsis</h2>
<pre><code>int zmq_poll(zmq_pollitem_t *items, int nitems, long timeout);</code></pre>
<h2>Description</h2>
<p>The <i>zmq_poll()</i> function provides a mechanism for applications to multiplex input/output events in a level-triggered fashion over a set of sockets. Each member of the array pointed to by the <i>items</i> argument is a <code>zmq_pollitem_t</code> structure. The <i>nitems</i> argument specifies the number of items in the <i>items</i> array. The <code>zmq_pollitem_t</code> structure is defined as follows:</p>
<dl>
<dd>
<pre>typedef struct
{
 void <i>*socket</i>;
 int <i>fd</i>;
 short <i>events</i>;
 short <i>revents</i>;
} zmq_pollitem_t;</pre>
</dl>
<p> For each <code>zmq_pollitem_t</code> item, <i>zmq_poll()</i> shall examine either the 0MQ socket referenced by <i>socket</i> <code>or</code> the standard socket specified by the file descriptor <i>fd</i>, for the event(s) specified in <i>events</i>. If both <i>socket</i> and <i>fd</i> are set in a single <code>zmq_pollitem_t</code>, the 0MQ socket referenced by <i>socket</i> shall take precedence and the value of <i>fd</i> shall be ignored. For each <code>zmq_pollitem_t</code> item, <i>zmq_poll()</i> shall first clear the <i>revents</i> member, and then indicate any requested events that have occurred by setting the bit corresponding to the event condition in the <i>revents</i> member. If none of the requested events have occurred on any <code>zmq_pollitem_t</code> item, <i>zmq_poll()</i> shall wait <i>timeout</i> milliseconds for an event to occur on any of the requested items. If the value of <i>timeout</i> is 0, <i>zmq_poll()</i> shall return immediately. If the value of <i>timeout</i> is -1, <i>zmq_poll()</i> shall block indefinitely until a requested event has occurred on at least one <code>zmq_pollitem_t</code>. The <i>events</i> and <i>revents</i> members of <code>zmq_pollitem_t</code> are bit masks constructed by OR&#8217;ing a combination of the following event flags: <code>ZMQ_POLLIN</code></p>
<dl>
<dd>For 0MQ sockets, at least one message may be received from the <i>socket</i> without blocking. For standard sockets this is equivalent to the <i>POLLIN</i> flag of the <i>poll()</i> system call and generally means that at least one byte of data may be read from <i>fd</i> without blocking.</dl>
<p> <code>ZMQ_POLLOUT</code></p>
<dl>
<dd>For 0MQ sockets, at least one message may be sent to the <i>socket</i> without blocking. For standard sockets this is equivalent to the <i>POLLOUT</i> flag of the <i>poll()</i> system call and generally means that at least one byte of data may be written to <i>fd</i> without blocking.</dl>
<p> <code>ZMQ_POLLERR</code></p>
<dl>
<dd>For standard sockets, this flag is passed through <i>zmq_poll()</i> to the underlying <i>poll()</i> system call and generally means that some sort of error condition is present on the socket specified by <i>fd</i>. For 0MQ sockets this flag has no effect if set in <i>events</i>, and shall never be returned in <i>revents</i> by <i>zmq_poll()</i>.</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 The <i>zmq_poll()</i> function may be implemented or emulated using operating system interfaces other than <i>poll()</i>, and as such may be subject to the limits of those interfaces in ways not defined in this documentation. </p>
<h2>Return Value</h2>
<p>Upon successful completion, the <i>zmq_poll()</i> function shall return the number of <code>zmq_pollitem_t</code> structures with events signaled in <i>revents</i> or 0 if no events have been signaled. Upon failure, <i>zmq_poll()</i> shall return -1 and set <i>errno</i> to one of the values defined below.</p>
<h2>Errors</h2>
<p><code>ETERM</code></p>
<dl>
<dd>At least one of the members of the <i>items</i> array refers to a <i>socket</i> whose associated 0MQ <i>context</i> was terminated.</dl>
<p> <code>EFAULT</code></p>
<dl>
<dd>The provided <i>items</i> was not valid (NULL).</dl>
<p> <code>EINTR</code></p>
<dl>
<dd>The operation was interrupted by delivery of a signal before any events were available.</dl>
<h2>Example</h2>
<p><code>Polling indefinitely for input events on both a 0MQ socket and a standard socket.</code>. </p>
<pre><code>zmq_pollitem_t items[2];
/* First item refers to 0MQ socket 'socket' */
items[0].socket = socket;
items[0].events = ZMQ_POLLIN;
/* Second item refers to standard socket 'fd' */
items[1].socket = NULL;
items[1].fd = fd;
items[1].events = ZMQ_POLLIN;
/* Poll for events indefinitely */
int rc = zmq_poll(items, 2, -1);
assert(rc &gt;= 0);
/* Returned events will be stored in items[].revents */
</code></pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-zmq_socket/">zmq_socket</a></code>(3) <code><a href="/docs/linux/man/3-zmq_send/">zmq_send</a></code>(3) <code><a href="/docs/linux/man/3-zmq_recv/">zmq_recv</a></code>(3) <code><a href="/docs/linux/man/7-zmq/">zmq</a></code>(7) </p>
<p> Your operating system documentation for the <i>poll()</i> system call.</p>
<h2>Authors</h2>
<p>This page was written by the 0MQ community. To make a change please read the 0MQ Contribution Policy at m[blue]<code><a rel="nofollow" href="http://www.zeromq.org/docs:contributing">http://www.zeromq.org/docs:contributing</a></code>m[].</p>
