---
title: "struct_snd_compr_runtime(9)"
name: "struct_snd_compr_runtime"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr_runtime/"
---

struct_snd_compr_runtime -

<h2>Synopsis</h2>

<pre><code>struct snd_compr_runtime {
    snd_pcm_state_t state;
    struct snd_compr_ops *ops;
    void *buffer;
    u64 buffer_size;
    u32 fragment_size;
    u32 fragments;
    u64 total_bytes_available;
    u64 total_bytes_transferred;
    wait_queue_head_t sleep;
    void *private_data;
};</code></pre>

<h2>Members</h2>

state
<dl><dd>stream state</dd></dl>
 

 ops
<dl><dd>pointer to DSP callbacks</dd></dl>
 

 buffer
<dl><dd>pointer to kernel buffer, valid only when not in mmap mode or DSP doesn't implement copy</dd></dl>
 

 buffer_size
<dl><dd>size of the above buffer</dd></dl>
 

 fragment_size
<dl><dd>size of buffer fragment in bytes</dd></dl>
 

 fragments
<dl><dd>number of such fragments</dd></dl>
 

 total_bytes_available
<dl><dd>cumulative number of bytes made available in the ring buffer</dd></dl>
 

 total_bytes_transferred
<dl><dd>cumulative bytes transferred by offload DSP</dd></dl>
 

 sleep
<dl><dd>poll sleep</dd></dl>
 

 private_data
<dl><dd>driver private data pointer</dd></dl>

<h2>Copyright</h2>


