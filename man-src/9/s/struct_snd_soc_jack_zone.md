---
title: "struct_snd_soc_jack_zone(9)"
name: "struct_snd_soc_jack_zone"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_soc_jack_zone/"
---

struct_snd_soc_jack_zone - Describes voltage zones of jack detection

<h2>Synopsis</h2>

<pre><code>struct snd_soc_jack_zone {
    unsigned int min_mv;
    unsigned int max_mv;
    unsigned int jack_type;
    unsigned int debounce_time;
    struct list_head list;
};</code></pre>

<h2>Members</h2>

min_mv
<dl><dd>start voltage in mv</dl>
 

 max_mv
<dl><dd>end voltage in mv</dl>
 

 jack_type
<dl><dd>type of jack that is expected for this voltage</dl>
 

 debounce_time
<dl><dd>debounce_time for jack, codec driver should wait for this duration before reading the adc for voltages</dl>
 

 list
<dl><dd>internal list entry</dl>

<h2>Copyright</h2>


