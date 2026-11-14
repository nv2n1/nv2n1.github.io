---
title: "struct_snd_compr_caps(9)"
name: "struct_snd_compr_caps"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_caps/"
---

struct_snd_compr_caps - caps descriptor

<h2>Synopsis</h2>

<pre><code>struct snd_compr_caps {
    __u32 num_codecs;
    __u32 direction;
    __u32 min_fragment_size;
    __u32 max_fragment_size;
    __u32 min_fragments;
    __u32 max_fragments;
    __u32 codecs[MAX_NUM_CODECS];
    __u32 reserved[11];
};</code></pre>

<h2>Members</h2>

num_codecs
<dl><dd>number of codecs supported</dl>
 

 direction
<dl><dd>direction supported. Of type snd_compr_direction</dl>
 

 min_fragment_size
<dl><dd>minimum fragment supported by DSP</dl>
 

 max_fragment_size
<dl><dd>maximum fragment supported by DSP</dl>
 

 min_fragments
<dl><dd>min fragments supported by DSP</dl>
 

 max_fragments
<dl><dd>max fragments supported by DSP</dl>
 

 codecs[MAX_NUM_CODECS]
<dl><dd>pointer to array of codecs</dl>
 

 reserved[11]
<dl><dd>reserved field</dl>

<h2>Copyright</h2>


