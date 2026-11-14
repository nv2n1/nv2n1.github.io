---
title: "ipcmk(1)"
name: "ipcmk"
section: "1"
letter: "i"
url: "/docs/linux/man/1-ipcmk/"
description: "ipcmk – make various IPC resources"
---

<h2 class="name">NAME</h2>
<p> ipcmk &#8211; make various IPC resources </p>
<h2>SYNOPSIS</h2>
<p> <code>ipcmk</code> [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>ipcmk</code> allows you to create System V inter-process communication (IPC) objects: shared memory segments, message queues, and semaphore arrays.</p>
<h2>OPTIONS</h2>
<p> Resources can be specified with these options: </p>
<p> <code>-M</code>, <code>&#8211;shmem</code> <i>size</i></p>
<dl>
<dt>
<dd> Create a shared memory segment of <i>size</i> bytes. The <i>size</i> argument may be followed by the multiplicative suffixes KiB (=1024), MiB (=1024*1024), and so on for GiB, etc. (the &quot;iB&quot; is optional, e.g., &quot;K&quot; has the same meaning as &quot;KiB&quot;) or the suffixes KB (=1000), MB (=1000*1000), and so on for GB, etc.</dl>
<p> <code>-Q</code>, <code>&#8211;queue</code></p>
<dl>
<dt>
<dd> Create a message queue.</dl>
<p> <code>-S</code>, <code>&#8211;semaphore</code> <i>number</i></p>
<dl>
<dt>
<dd> Create a semaphore array with <i>number</i> of elements.</dl>
<p> Other options are: </p>
<p> <code>-p</code>, <code>&#8211;mode</code> <i>mode</i></p>
<dl>
<dt>
<dd> Access permissions for the resource. Default is 0644.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Display help text and exit.</dl>
<h2>AUTHORS</h2>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/1-ipcs/">ipcs</a></code>(1), <code><a href="/docs/linux/man/7-sysvipc/">sysvipc</a></code>(7)</p>
<h2>REPORTING BUGS</h2>
<p> For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>AVAILABILITY</h2>
<p> The <code>ipcmk</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;. </p>
<h2>Index</h2>
