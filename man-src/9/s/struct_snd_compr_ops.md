---
title: "struct_snd_compr_ops(9)"
name: "struct_snd_compr_ops"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_ops/"
---

struct_snd_compr_ops -

<h2>Synopsis</h2>

<pre><code>struct snd_compr_ops {
    int (*open)(struct snd_compr_stream *stream);
    int (*free)(struct snd_compr_stream *stream);
    int (*set_params)(struct snd_compr_stream *stream, struct snd_compr_params *params);
    int (*get_params)(struct snd_compr_stream *stream, struct snd_codec *params);
    int (*set_metadata)(struct snd_compr_stream *stream, struct snd_compr_metadata *metadata);
    int (*get_metadata)(struct snd_compr_stream *stream, struct snd_compr_metadata *metadata);
    int (*trigger)(struct snd_compr_stream *stream, int cmd);
    int (*pointer)(struct snd_compr_stream *stream, struct snd_compr_tstamp *tstamp);
    int (*copy)(struct snd_compr_stream *stream, char __user *buf, size_t count);
    int (*mmap)(struct snd_compr_stream *stream, struct vm_area_struct *vma);
    int (*ack)(struct snd_compr_stream *stream, size_t bytes);
    int (*get_caps)(struct snd_compr_stream *stream, struct snd_compr_caps *caps);
    int (*get_codec_caps)(struct snd_compr_stream *stream, struct snd_compr_codec_caps *codec);
};</code></pre>

<h2>Members</h2>

open
<dl><dd>Open the compressed stream This callback is mandatory and shall keep dsp ready to receive the stream parameter</dl>
 

 free
<dl><dd>Close the compressed stream, mandatory</dl>
 

 set_params
<dl><dd>Sets the compressed stream parameters, mandatory This can be called in during stream creation only to set codec params and the stream properties</dl>
 

 get_params
<dl><dd>retrieve the codec parameters, mandatory</dl>
 

 set_metadata
<dl><dd>Set the metadata values for a stream</dl>
 

 get_metadata
<dl><dd>retrieves the requested metadata values from stream</dl>
 

 trigger
<dl><dd>Trigger operations like start, pause, resume, drain, stop. This callback is mandatory</dl>
 

 pointer
<dl><dd>Retrieve current h/w pointer information. Mandatory</dl>
 

 copy
<dl><dd>Copy the compressed data to/from userspace, Optional Can't be implemented if DSP supports mmap</dl>
 

 mmap
<dl><dd>DSP mmap method to mmap DSP memory</dl>
 

 ack
<dl><dd>Ack for DSP when data is written to audio buffer, Optional Not valid if copy is implemented</dl>
 

 get_caps
<dl><dd>Retrieve DSP capabilities, mandatory</dl>
 

 get_codec_caps
<dl><dd>Retrieve capabilities for a specific codec, mandatory</dl>

<h2>Copyright</h2>


