---
title: "struct_snd_compr(9)"
name: "struct_snd_compr"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_compr/"
---

struct_snd_compr -

<h2>Synopsis</h2>

<pre><code>struct snd_compr {
    const char *name;
    struct device dev;
    struct snd_compr_ops *ops;
    void *private_data;
    struct snd_card *card;
    unsigned int direction;
    struct mutex lock;
    int device;
#ifdef CONFIG_SND_VERBOSE_PROCFS
#endif
};</code></pre>

<h2>Members</h2>

name
<dl><dd>DSP device name</dl>
 

 dev
<dl><dd>associated device instance</dl>
 

 ops
<dl><dd>pointer to DSP callbacks</dl>
 

 private_data
<dl><dd>pointer to DSP pvt data</dl>
 

 card
<dl><dd>sound card pointer</dl>
 

 direction
<dl><dd>Playback or capture direction</dl>
 

 lock
<dl><dd>device lock</dl>
 

 device
<dl><dd>device id</dl>

<h2>Copyright</h2>


