---
title: "eventfd_fget(9)"
name: "eventfd_fget"
section: "9"
letter: "e"
url: "/docs/linux/man/9-eventfd_fget/"
---

eventfd_fget - Acquire a reference of an eventfd file descriptor.

<h2>Synopsis</h2>

<pre><code>struct file *eventfd_fget(int fd);</code></pre>

<h2>Arguments</h2>

<i>fd</i>
<dl><dd>[in] Eventfd file descriptor.</dl>

<h2>Description</h2>

<dd>Returns a pointer to the eventfd file structure in case of success, or the following error pointer: 

 -EBADF : Invalid <i>fd</i> file descriptor. -EINVAL : The <i>fd</i> file descriptor is not an eventfd file.

<h2>Copyright</h2>


