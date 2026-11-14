---
title: "struct_snd_compr_codec_caps(9)"
name: "struct_snd_compr_codec_caps"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_codec_caps/"
---

struct_snd_compr_codec_caps - query capability of codec

<h2>Synopsis</h2>

<pre><code>struct snd_compr_codec_caps {
    __u32 codec;
    __u32 num_descriptors;
    struct snd_codec_desc descriptor[MAX_NUM_CODEC_DESCRIPTORS];
};</code></pre>

<h2>Members</h2>

codec
<dl><dd>codec for which capability is queried</dl>
 

 num_descriptors
<dl><dd>number of codec descriptors</dl>
 

 descriptor[MAX_NUM_CODEC_DESCRIPTORS]
<dl><dd>array of codec capability descriptor</dl>

<h2>Copyright</h2>


