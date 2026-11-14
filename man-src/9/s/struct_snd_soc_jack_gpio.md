---
title: "struct_snd_soc_jack_gpio(9)"
name: "struct_snd_soc_jack_gpio"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_snd_soc_jack_gpio/"
---

struct_snd_soc_jack_gpio - Describes a gpio pin for jack detection

<h2>Synopsis</h2>

<pre><code>struct snd_soc_jack_gpio {
    unsigned int gpio;
    unsigned int idx;
    struct device *gpiod_dev;
    const char *name;
    int report;
    int invert;
    int debounce_time;
    bool wake;
    int (*jack_status_check)(void *data);
};</code></pre>

<h2>Members</h2>

gpio
<dl><dd>legacy gpio number</dl>
 

 idx
<dl><dd>gpio descriptor index within the function of the GPIO consumer device</dl>
 

 gpiod_dev
<dl><dd>GPIO consumer device</dl>
 

 name
<dl><dd>gpio name. Also as connection ID for the GPIO consumer device function name lookup</dl>
 

 report
<dl><dd>value to report when jack detected</dl>
 

 invert
<dl><dd>report presence in low state</dl>
 

 debounce_time
<dl><dd>debounce time in ms</dl>
 

 wake
<dl><dd>enable as wake source</dl>
 

 jack_status_check
<dl><dd>callback function which overrides the detection to provide more complex checks (eg, reading an ADC).</dl>

<h2>Copyright</h2>


