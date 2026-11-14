---
title: "struct_snd_enc_vorbis(9)"
name: "struct_snd_enc_vorbis"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_enc_vorbis/"
---

struct_snd_enc_vorbis -

<h2>Synopsis</h2>

<pre><code>struct snd_enc_vorbis {
    __s32 quality;
    __u32 managed;
    __u32 max_bit_rate;
    __u32 min_bit_rate;
    __u32 downmix;
};</code></pre>

<h2>Members</h2>

quality
<dl><dd>Sets encoding quality to n, between -1 (low) and 10 (high). In the default mode of operation, the quality level is 3. Normal quality range is 0 - 10.</dl>
 

 managed
<dl><dd>Boolean. Set bitrate management mode. This turns off the normal VBR encoding, but allows hard or soft bitrate constraints to be enforced by the encoder. This mode can be slower, and may also be lower quality. It is primarily useful for streaming.</dl>
 

 max_bit_rate
<dl><dd>Enabled only if managed is TRUE</dl>
 

 min_bit_rate
<dl><dd>Enabled only if managed is TRUE</dl>
 

 downmix
<dl><dd>Boolean. Downmix input from stereo to mono (has no effect on non-stereo streams). Useful for lower-bitrate encoding.</dl>

<h2>Description</h2>

These options were extracted from the OpenMAX IL spec and Gstreamer vorbisenc properties 

 For best quality users should specify VBR mode and set quality levels.

<h2>Copyright</h2>


