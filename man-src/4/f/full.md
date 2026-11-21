---
title: "full(4)"
name: "full"
section: "4"
letter: "f"
url: "/docs/linux/man/4-full/"
description: "full – always full device"
---

<p>full &#8211; always full device</p>
<h2>Configuration</h2>
<p>If your system does not have <i>/dev/full</i> created already, it can be created with the following commands: </p>
<p> mknod -m 666 /dev/full c 1 7 chown root:root /dev/full</p>
<h2>Description</h2>
<p>The file <i>/dev/full</i> has major device number 1 and minor device number 7. </p>
<p> Writes to the <i>/dev/full</i> device fail with an <code>ENOSPC</code> error. This can be used to test how a program handles disk-full errors. </p>
<p> Reads from the <i>/dev/full</i> device will return \0 characters. </p>
<p> Seeks on <i>/dev/full</i> will always succeed.  </p>
<h2>FILES</h2>
<p> <i>/dev/full</i>  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/4-null/">null</a></code>(4), <code><a href="/docs/linux/man/4-zero/">zero</a></code>(4)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
