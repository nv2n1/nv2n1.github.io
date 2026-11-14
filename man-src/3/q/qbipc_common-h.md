---
title: "qbipc_common-h(3)"
name: "qbipc_common-h"
section: "3"
letter: "q"
url: "/docs/linux/man/3-qbipc_common-h/"
description: "qbipc_common.h –"
---

<p>qbipc_common.h &#8211; </p>
<p> common types and definitions</p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;stdint.h&gt;</code></pre>
<h3>Data Structures</h3>
<p>struct qb_ipc_request_header</p>
<p>struct qb_ipc_response_header</p>
<p>Macros<br />
#define QB_IPC_MSG_NEW_MESSAGE   0</p>
<p>#define QB_IPC_MSG_USER_START   QB_IPC_MSG_NEW_MESSAGE</p>
<p>#define QB_IPC_MSG_AUTHENTICATE   -1</p>
<p>#define QB_IPC_MSG_NEW_EVENT_SOCK   -2</p>
<p>#define QB_IPC_MSG_DISCONNECT   -3</p>
<p>Enumerations<br />
 enum <code>qb_ipc_type</code> { <code>QB_IPC_SOCKET</code>, <code>QB_IPC_SHM</code>, <code>QB_IPC_POSIX_MQ</code>, <code>QB_IPC_SYSV_MQ</code>, <code>QB_IPC_NATIVE</code> }</p>
<h3>Functions</h3>
<pre><code>struct qb_ipc_request_header __attribute__ ((aligned(8)))



Variables</code></pre>
<p> enum <code>qb_ipc_type</code> <code>__attribute__</code></p>
<h2>Detailed Description</h2>
<p>common types and definitions</p>
<h2>Macro Definition Documentation</h2>
<h3>#define QB_IPC_MSG_AUTHENTICATE -1</h3>
<h3>#define QB_IPC_MSG_DISCONNECT -3</h3>
<h3>#define QB_IPC_MSG_NEW_EVENT_SOCK -2</h3>
<h3>#define QB_IPC_MSG_NEW_MESSAGE 0</h3>
<h3>#define QB_IPC_MSG_USER_START <code>QB_IPC_MSG_NEW_MESSAGE</code></h3>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>qb_ipc_type</code></h3>
<p><code>Enumerator</code></p>
<dl>
<dt><i>QB_IPC_SOCKET </i></p>
<dd>
<dt><i>QB_IPC_SHM </i></p>
<dd>
<dt><i>QB_IPC_POSIX_MQ </i></p>
<dd>
<dt><i>QB_IPC_SYSV_MQ </i></p>
<dd>
<dt><i>QB_IPC_NATIVE </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3>struct <code>qb_ipc_request_header</code> __attribute__ ((<a href="/docs/linux/man/8-aligned/">aligned</a>(8)))</h3>
<h2>Variable Documentation</h2>
<h3>int32_t error __attribute__</h3>
<h2>Author</h2>
<p>Generated automatically by Doxygen for libqb from the source code.</p>
