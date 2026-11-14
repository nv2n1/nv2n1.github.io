---
title: "struct_snd_compressed_buffer(9)"
name: "struct_snd_compressed_buffer"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compressed_buffer/"
---

struct_snd_compressed_buffer - compressed buffer

<h2>Synopsis</h2>

<pre><code>struct snd_compressed_buffer {
    __u32 fragment_size;
    __u32 fragments;
};</code></pre>

<h2>Members</h2>

fragment_size
<dl><dd>size of buffer fragment in bytes</dl>
 

 fragments
<dl><dd>number of such fragments</dl>

<h2>Copyright</h2>


