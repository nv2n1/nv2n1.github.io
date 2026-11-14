---
title: "shells(5)"
name: "shells"
section: "5"
letter: "s"
url: "/docs/linux/man/5-shells/"
description: "shells – pathnames of valid login shells"
---

<p>shells &#8211; pathnames of valid login shells</p>
<h2>Description</h2>
<p><i>/etc/shells</i> is a text file which contains the full pathnames of valid login shells. This file is consulted by <code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1) and available to be queried by other programs. </p>
<p> Be aware that there are programs which consult this file to find out if a user is a normal user; for example, FTP daemons traditionally disallow access to users with shells not included in this file.</p>
<h2>Files</h2>
<p><i>/etc/shells</i></p>
<h2>Examples</h2>
<p><i>/etc/shells</i> may contain the following paths: </p>
<p> <i>/bin/sh</i> <i>/bin/bash</i> <i>/bin/csh</i></p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-chsh/">chsh</a></code>(1), <code><a href="/docs/linux/man/3-getusershell/">getusershell</a></code>(3), <code><a href="/docs/linux/man/8-pam_shells/">pam_shells</a></code>(8)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
