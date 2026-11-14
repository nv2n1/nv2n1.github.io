---
title: "bpf_prog_create(9)"
name: "bpf_prog_create"
section: "9"
letter: "b"
url: "/docs/linux/man/9-bpf_prog_create/"
---

bpf_prog_create - create an unattached filter

<h2>Synopsis</h2>

<pre><code>int bpf_prog_create(struct bpf_prog **pfp, struct sock_fprog_kern *fprog);</code></pre>

<h2>Arguments</h2>

<i>pfp</i>
<dl><dd><dd>the unattached filter that is created</dl>
 

 <i>fprog</i>
<dl><dd>the filter program</dl>

<h2>Description</h2>

Create a filter independent of any socket. We first run some sanity checks on it to make sure it does not explode on us later. If an error occurs or there is insufficient memory for the filter a negative errno code is returned. On success the return is zero.

<h2>Copyright</h2>


