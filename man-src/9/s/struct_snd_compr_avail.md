---
title: "struct_snd_compr_avail(9)"
name: "struct_snd_compr_avail"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_avail/"
---

struct_snd_compr_avail - avail descriptor

<h2>Synopsis</h2>

<pre><code>struct snd_compr_avail {
    __u64 avail;
    struct snd_compr_tstamp tstamp;
};</code></pre>

<h2>Members</h2>

avail
<dl><dd>Number of bytes available in ring buffer for writing/reading</dl>
 

 tstamp
<dl><dd>timestamp information</dl>

<h2>Copyright</h2>


