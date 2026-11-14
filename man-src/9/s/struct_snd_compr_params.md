---
title: "struct_snd_compr_params(9)"
name: "struct_snd_compr_params"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_params/"
---

struct_snd_compr_params - compressed stream params

<h2>Synopsis</h2>

<pre><code>struct snd_compr_params {
    struct snd_compressed_buffer buffer;
    struct snd_codec codec;
    __u8 no_wake_mode;
};</code></pre>

<h2>Members</h2>

buffer
<dl><dd>buffer description</dl>
 

 codec
<dl><dd>codec parameters</dl>
 

 no_wake_mode
<dl><dd>dont wake on fragment elapsed</dl>

<h2>Copyright</h2>


