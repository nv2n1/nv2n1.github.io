---
title: "alarm(2)"
name: "alarm"
section: "2"
letter: "a"
url: "/docs/linux/man/2-alarm/"
description: "alarm – set an alarm clock for delivery of a signal"
---

<h2 class="name">NAME</h2>
<p> alarm &#8211; set an alarm clock for delivery of a signal </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;unistd.h&gt;
unsigned int alarm(unsigned int seconds);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>alarm</code>() arranges for a <code>SIGALRM</code> signal to be delivered to the calling process in <i>seconds</i> seconds. </p>
<p> If <i>seconds</i> is zero, any pending alarm is canceled. </p>
<p> In any event any previously set <code>alarm</code>() is canceled.</p>
<h2>RETURN VALUE</h2>
<p> <code>alarm</code>() returns the number of seconds remaining until any previously scheduled alarm was due to be delivered, or zero if there was no previously scheduled alarm.</p>
<h2>CONFORMING TO</h2>
<p> POSIX.1-2001, POSIX.1-2008, SVr4, 4.3BSD.</p>
<h2>NOTES</h2>
<p> <code>alarm</code>() and <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2) share the same timer; calls to one will interfere with use of the other. </p>
<p> Alarms created by <code>alarm</code>() are preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2) and are not inherited by children created via <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2). </p>
<p> <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3) may be implemented using <code>SIGALRM</code>; mixing calls to <code>alarm</code>() and <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3) is a bad idea. </p>
<p> Scheduling delays can, as ever, cause the execution of the process to be delayed by an arbitrary amount of time.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-gettimeofday/">gettimeofday</a></code>(2), <code><a href="/docs/linux/man/2-pause/">pause</a></code>(2), <code><a href="/docs/linux/man/2-select/">select</a></code>(2), <code><a href="/docs/linux/man/2-setitimer/">setitimer</a></code>(2), <code><a href="/docs/linux/man/2-sigaction/">sigaction</a></code>(2), <code><a href="/docs/linux/man/2-signal/">signal</a></code>(2), <code><a href="/docs/linux/man/2-timer_create/">timer_create</a></code>(2), <code><a href="/docs/linux/man/2-timerfd_create/">timerfd_create</a></code>(2), <code><a href="/docs/linux/man/3-sleep/">sleep</a></code>(3), <code><a href="/docs/linux/man/7-time/">time</a></code>(7)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
