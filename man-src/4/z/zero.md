---
title: "zero(4)"
name: "zero"
section: "4"
letter: "z"
url: "/docs/linux/man/4-zero/"
description: "null, zero – data sink"
---

<p>null, zero &#8211; data sink</p>
<h2>Description</h2>
<p>Data written to the <i>/dev/null</i> and <i>/dev/zero</i> special files is discarded. </p>
<p> Reads from <i>/dev/null</i> always return end of file (i.e., <code><a href="/docs/linux/man/2-read/">read</a></code>(2) returns 0), whereas reads from <i>/dev/zero</i> always return bytes containing zero (&#8216;\0&#8217; characters). </p>
<p> These devices are typically created by: </p>
<p> mknod -m 666 /dev/null c 1 3 mknod -m 666 /dev/zero c 1 5 chown root:root /dev/null /dev/zero  </p>
<h2>FILES</h2>
<p> <i>/dev/null</i> <br/>
 <i>/dev/zero</i>  </p>
<h2>NOTES</h2>
<p> If these devices are not writable and readable for all users, many programs will act strangely. </p>
<p> Since Linux 2.6.31, reads from <i>/dev/zero</i> are interruptible by signals. (This change was made to help with bad latencies for large reads from <i>/dev/zero</i>.)  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-chown/">chown</a></code>(1), <code><a href="/docs/linux/man/1-mknod/">mknod</a></code>(1), <code><a href="/docs/linux/man/4-full/">full</a></code>(4)  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
