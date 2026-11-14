---
title: "group_member(3)"
name: "group_member"
section: "3"
letter: "g"
url: "/docs/linux/man/3-group_member/"
description: "group_member – test whether a process is in a group"
---

<h2 class="name">NAME</h2>
<p> group_member &#8211; test whether a process is in a group </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;unistd.h&gt;</code> </p>
<p> <code>int group_member(gid_t </code><i>gid</i><code>);</code> </p>
<p> Feature Test Macro Requirements for glibc (see <code><a href="/docs/linux/man/7-feature_test_macros/">feature_test_macros</a></code>(7)): </p>
<p> <code>group_member</code>(): _GNU_SOURCE</p>
<h2>DESCRIPTION</h2>
<p> The <code>group_member</code>() function tests whether any of the caller&#8217;s supplementary group IDs (as returned by <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2)) matches <i>gid</i>.</p>
<h2>RETURN VALUE</h2>
<p> The <code>group_member</code>() function returns nonzero if any of the caller&#8217;s supplementary group IDs matches <i>gid</i>, and zero otherwise.</p>
<h2>CONFORMING TO</h2>
<p> This function is a nonstandard GNU extension.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/2-getgid/">getgid</a></code>(2), <code><a href="/docs/linux/man/2-getgroups/">getgroups</a></code>(2), <code><a href="/docs/linux/man/3-getgrouplist/">getgrouplist</a></code>(3), <code><a href="/docs/linux/man/5-group/">group</a></code>(5)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
