---
title: "struct_socket(9)"
name: "struct_socket"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_socket/"
description: "struct_socket – general BSD socket"
---

<p>struct_socket &#8211; general BSD socket</p>
<h2>Synopsis</h2>
<pre><code>struct socket {
    socket_state state;
    short type;
    unsigned long flags;
    struct socket_wq __rcu *wq;
    struct file *file;
    struct sock *sk;
    const struct proto_ops *ops;
};</code></pre>
<h2>Members</h2>
<p>state</p>
<dl>
<dd>socket state (<code>SS_CONNECTED</code>, etc)</dl>
<p> type</p>
<dl>
<dd>socket type (<code>SOCK_STREAM</code>, etc)</dl>
<p> flags</p>
<dl>
<dd>socket flags (<code>SOCK_NOSPACE</code>, etc)</dl>
<p> wq</p>
<dl>
<dd>wait queue for several uses</dl>
<p> file</p>
<dl>
<dd>File back pointer for gc</dl>
<p> sk</p>
<dl>
<dd>internal networking protocol agnostic socket representation</dl>
<p> ops</p>
<dl>
<dd>protocol specific socket operations</dl>
<h2>Copyright</h2>
