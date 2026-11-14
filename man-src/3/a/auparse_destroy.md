---
title: "auparse_destroy(3)"
name: "auparse_destroy"
section: "3"
letter: "a"
url: "/docs/linux/man/3-auparse_destroy/"
description: "auparse_destroy – release instance of parser"
---

<h2>NAME</h2>
<p> auparse_destroy &#8211; release instance of parser</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;auparse.h&gt;</code> </p>
<p> <code>void auparse_destroy (auparse_state_t *au);</code> </p>
<p> <code>void auparse_destroy_ext (auparse_state_t *au, auparse_destroy_what_t what);</code> </p>
<h2>DESCRIPTION</h2>
<p> <code>auparse_destroy</code> frees all data structures and closes file descriptors. </p>
<p> <code>auparse_destroy_ext</code> frees data structures based on what. What can be AUPARSE_DESTROY_ALL to release everything or AUPARSE_DESTROY_COMMON to release everything but the uid and gid lookup cache. </p>
<h2>RETURN VALUE</h2>
<p> None. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-auparse_init/">auparse_init</a></code>(3), <code><a href="/docs/linux/man/3-auparse_reset/">auparse_reset</a></code>(3). </p>
<h2>AUTHOR</h2>
<p> Steve Grubb </p>
<h2>Index</h2>
