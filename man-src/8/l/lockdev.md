---
title: "lockdev(8)"
name: "lockdev"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lockdev/"
description: "Lockdev is a setgid binary, which provides a reliable way to put an exclusive lock in /var/lock to devices (e.g. ttyS0) using both FSSTND and SVr4 methods, so regular users don’t need write access ..."
---

<p><code>Lockdev</code> is a setgid binary, which provides a reliable way to put an exclusive lock in /var/lock to devices (e.g. ttyS0) using both FSSTND and SVr4 methods, so regular users don&#8217;t need write access there. This task is achieved through calls to the </p>
<p><a href="/docs/linux/man/3-liblockdev/">liblockdev</a>(3) API. </p>
<h2>Synopsis</h2>
<p><code>/usr/sbin/lockdev</code> [&lt;<code>operation</code>&gt;] &lt;<code>device</code>&gt; </p>
<h2>Description</h2>
<p>The <code>lockdev</code> command can perform one of the following operations (calls to <a href="/docs/linux/man/3-liblockdev/">liblockdev</a>(3) API): <code>-l</code> &#8211; lock device with <code>dev_lock()</code> function <code>-u</code> &#8211; unlock device with <code>dev_unlock()</code> function <code>no operation</code> &#8211; test lock with <code>dev_testlock()</code> function </p>
<h2>Return Values</h2>
<p>Value&nbsp;<wbr>&nbsp;<wbr>dev_lock&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dev_unlock&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>dev_testlock<br />
0&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>OK&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>not locked<br />
1&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>locked other&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>locked other&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>locked<br />
2&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EACCES<br />
3&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EROFS<br />
4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EFAULT<br />
5&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EINVAL<br />
6&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ENAMETOOLONG<br />
7&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ENOENT<br />
8&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ENOTDIR<br />
9&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ENOMEM<br />
&nbsp;<wbr>&nbsp;<wbr>10&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ELOOP<br />
&nbsp;<wbr>&nbsp;<wbr>11&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EIO<br />
&nbsp;<wbr>&nbsp;<wbr>12&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>EPERM<br />
&nbsp;<wbr>255&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>error</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-lockdev/">lockdev</a></code>(3). </p>
