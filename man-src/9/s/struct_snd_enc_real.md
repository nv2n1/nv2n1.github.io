---
title: "struct_snd_enc_real(9)"
name: "struct_snd_enc_real"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_enc_real/"
---

struct_snd_enc_real -

<h2>Synopsis</h2>

<pre><code>struct snd_enc_real {
    __u32 quant_bits;
    __u32 start_region;
    __u32 num_regions;
};</code></pre>

<h2>Members</h2>

quant_bits
<dl><dd>number of coupling quantization bits in the stream</dl>
 

 start_region
<dl><dd>coupling start region in the stream</dl>
 

 num_regions
<dl><dd>number of regions value</dl>

<h2>Description</h2>

These options were extracted from the OpenMAX IL spec

<h2>Copyright</h2>


