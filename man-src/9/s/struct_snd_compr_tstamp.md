---
title: "struct_snd_compr_tstamp(9)"
name: "struct_snd_compr_tstamp"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_tstamp/"
---

struct_snd_compr_tstamp - timestamp descriptor

<h2>Synopsis</h2>

<pre><code>struct snd_compr_tstamp {
    __u32 byte_offset;
    __u32 copied_total;
    __u32 pcm_frames;
    __u32 pcm_io_frames;
    __u32 sampling_rate;
};</code></pre>

<h2>Members</h2>

byte_offset
<dl><dd>Byte offset in ring buffer to DSP</dl>
 

 copied_total
<dl><dd>Total number of bytes copied from/to ring buffer to/by DSP</dl>
 

 pcm_frames
<dl><dd>Frames decoded or encoded by DSP. This field will evolve by large steps and should only be used to monitor encoding/decoding progress. It shall not be used for timing estimates.</dl>
 

 pcm_io_frames
<dl><dd>Frames rendered or received by DSP into a mixer or an audio output/input. This field should be used for A/V sync or time estimates.</dl>
 

 sampling_rate
<dl><dd>sampling rate of audio</dl>

<h2>Copyright</h2>


