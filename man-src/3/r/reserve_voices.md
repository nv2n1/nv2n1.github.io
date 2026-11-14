---
title: "reserve_voices(3)"
name: "reserve_voices"
section: "3"
letter: "r"
url: "/docs/linux/man/3-reserve_voices/"
description: "reserve_voices – Reserve a number of voices for the digital and MIDI drivers. Allegro game programming library."
---

<p>reserve_voices &#8211; Reserve a number of voices for the digital and MIDI drivers. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void reserve_voices(int digi_voices, int midi_voices);</code></pre>
<h2>Description</h2>
<p>Call this function to specify the number of voices that are to be used by the digital and MIDI sound drivers respectively. This must be done _before_ calling install_sound(). If you reserve too many voices, subsequent calls to install_sound() will fail. How many voices are available depends on the driver, and in some cases you will actually get more than you reserve (eg. the FM synth drivers will always provide 9 voices on an OPL2 and 18 on an OPL3, and the SB digital driver will round the number of voices up to the nearest power of two). Pass negative values to restore the default settings. You should be aware that the sound quality is usually inversely related to how many voices you use, so don&#8217;t reserve any more than you really need. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-set_volume_per_voice/">set_volume_per_voice</a></code>(3), <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-detect_digi_driver/">detect_digi_driver</a></code>(3), <code><a href="/docs/linux/man/3-detect_midi_driver/">detect_midi_driver</a></code>(3), <code><a href="/docs/linux/man/3-get_mixer_voices/">get_mixer_voices</a></code>(3) </p>
