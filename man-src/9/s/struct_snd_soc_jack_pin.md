---
title: "struct_snd_soc_jack_pin(9)"
name: "struct_snd_soc_jack_pin"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_soc_jack_pin/"
---

struct_snd_soc_jack_pin - Describes a pin to update based on jack detection

<h2>Synopsis</h2>

<pre><code>struct snd_soc_jack_pin {
    struct list_head list;
    const char *pin;
    int mask;
    bool invert;
};</code></pre>

<h2>Members</h2>

list
<dl><dd>internal list entry</dl>
 

 pin
<dl><dd>name of the pin to update</dl>
 

 mask
<dl><dd>bits to check for in reported jack status</dl>
 

 invert
<dl><dd>if non-zero then pin is enabled when status is not reported</dl>

<h2>Copyright</h2>


