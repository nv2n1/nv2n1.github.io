---
title: "pcp-ipcs(1)"
name: "pcp-ipcs"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pcp-ipcs/"
description: "pcp-ipcs – provide information on IPC facilities"
---

<h2>NAME</h2>
<p> pcp-ipcs &#8211; provide information on IPC facilities</p>
<h2>SYNOPSIS</h2>
<p> <code>pcp-ipcs</code> [<code>resource-option</code>] [<code>output-format</code>]<br />
 <code>pcp-ipcs</code> [<code>resource-option</code>] <code>-i</code><i> id</i></p>
<h2>DESCRIPTION</h2>
<p> <code>pcp-ipcs</code> provides information on the inter-process communication facilities for which the calling process has read access.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;id</code> <i>id</i></p>
<dd> Print details only on the resource identified by <i>id</i>.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Display a help text and exit.</p>
<dt><code>-V</code>, <code>&#8211;version</code></p>
<dd> Display version information and exit.</dl>
<h3>Resource options</h3>
<dl>
<dt><code>-q</code>, <code>&#8211;queues</code></p>
<dd> Write information about active message queues.</p>
<dt><code>-m</code>, <code>&#8211;shmems</code></p>
<dd> Write information about active shared memory segments.</p>
<dt><code>-s</code>, <code>&#8211;semaphores</code></p>
<dd> Write information about active semaphore sets.</p>
<dt><code>-a</code>, <code>&#8211;all</code></p>
<dd> Write information about all three resources (default).</dl>
<h3>Output formats</h3>
<p> Of these options only one takes effect: the last one specified.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;creator</code></p>
<dd> Show creator and owner.</p>
<dt><code>-l</code>, <code>&#8211;limits</code></p>
<dd> Show resource limits.</p>
<dt><code>-p</code>, <code>&#8211;pid</code></p>
<dd> Show PIDs of creator and last operator.</p>
<dt><code>-t</code>, <code>&#8211;time</code></p>
<dd> Write time information. The time of the last control operation that changed the access permissions for all facilities, the time of the last <i>msgsnd()</i> and <i>msgrcv()</i> operations on message queues, the time of the last <i>shmat()</i> and <i>shmdt()</i> operations on shared memory, and the time of the last <i>semop()</i> operation on semaphores.</p>
<dt><code>-u</code>, <code>&#8211;summary</code></p>
<dd> Show status summary.</dl>
<h3>Representation</h3>
<p> These affect only the <code>-l</code> (<code>&#8211;limits</code>) option.</p>
<dl>
<dt><code>-b</code>, <code>&#8211;bytes</code></p>
<dd> Print sizes in bytes.</p>
<dt><code>&#8211;human</code></p>
<dd> Print sizes in human-readable format.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ipcrm/">ipcrm</a></code>(1), <code><a href="/docs/linux/man/1-ipcmk/">ipcmk</a></code>(1), <code><a href="/docs/linux/man/2-msgrcv/">msgrcv</a></code>(2), <code><a href="/docs/linux/man/2-msgsnd/">msgsnd</a></code>(2), <code><a href="/docs/linux/man/2-semget/">semget</a></code>(2), <code><a href="/docs/linux/man/2-semop/">semop</a></code>(2), <code><a href="/docs/linux/man/2-shmat/">shmat</a></code>(2), <code><a href="/docs/linux/man/2-shmdt/">shmdt</a></code>(2), <code><a href="/docs/linux/man/2-shmget/">shmget</a></code>(2)</p>
<h2>CONFORMING TO</h2>
<p> The Linux pcp-ipcs utility is not fully compatible to the POSIX pcp-ipcs utility. The Linux version does not support the POSIX <code>-a</code>, <code>-b</code> and <code>-o</code> options, but does support the <code>-l</code> and <code>-u</code> options not defined by POSIX. A portable application shall not use the <code>-a</code>, <code>-b</code>, <code>-o</code>, <code>-l</code>, and <code>-u</code> options. </p>
<h2>Index</h2>
