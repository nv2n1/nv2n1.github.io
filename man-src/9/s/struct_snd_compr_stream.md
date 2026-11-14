---
title: "struct_snd_compr_stream(9)"
name: "struct_snd_compr_stream"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_stream/"
---

struct_snd_compr_stream -

<h2>Synopsis</h2>

<pre><code>struct snd_compr_stream {
    const char *name;
    struct snd_compr_ops *ops;
    struct snd_compr_runtime *runtime;
    struct snd_compr *device;
    struct delayed_work error_work;
    enum snd_compr_direction direction;
    bool metadata_set;
    bool next_track;
    void *private_data;
};</code></pre>

<h2>Members</h2>

name
<dl><dd>device name</dl>
 

 ops
<dl><dd>pointer to DSP callbacks</dl>
 

 runtime
<dl><dd>pointer to runtime structure</dl>
 

 device
<dl><dd>device pointer</dl>
 

 error_work
<dl><dd>delayed work used when closing the stream due to an error</dl>
 

 direction
<dl><dd>stream direction, playback/recording</dl>
 

 metadata_set
<dl><dd>metadata set flag, true when set</dl>
 

 next_track
<dl><dd>has userspace signal next track transition, true when set</dl>
 

 private_data
<dl><dd>pointer to DSP private data</dl>

<h2>Copyright</h2>


