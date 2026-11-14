---
title: "motd(5)"
name: "motd"
section: "5"
letter: "m"
url: "/docs/linux/man/5-motd/"
description: "motd – message of the day"
---

<p>motd &#8211; message of the day</p>
<h2>Description</h2>
<p>The contents of <i>/etc/motd</i> are displayed by <code><a href="/docs/linux/man/8-pam_motd/">pam_motd</a></code>(8) after a successful login but just before it executes the login shell. </p>
<p> The abbreviation &quot;motd&quot; stands for &quot;message of the day&quot;, and this file has been traditionally used for exactly that (it requires much less disk space than mail to all users). </p>
<p> On Debian GNU/Linux, dynamic content configured at <i>/etc/pam.d/login</i> is also displayed by <i>pam_exec</i>.</p>
<h2>Files</h2>
<p><i>/etc/motd</i><br />
 <i>/etc/pam.d/login</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-login/">login</a></code>(1), <code><a href="/docs/linux/man/5-issue/">issue</a></code>(5), <code><a href="/docs/linux/man/8-pam_motd/">pam_motd</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
