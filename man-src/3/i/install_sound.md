---
title: "install_sound(3)"
name: "install_sound"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_sound/"
description: "install_sound – Initialises the sound module. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_sound &#8211; Initialises the sound module. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_sound(int digi, int midi, const char *cfg_path);</code></p>
<h2>DESCRIPTION</h2>
<p> Initialises the sound module. You should normally pass DIGI_AUTODETECT and MIDI_AUTODETECT as the driver parameters to this function, in which case Allegro will read hardware settings from the current configuration file. This allows the user to select different values with the setup utility: see the config section for details. Alternatively, see the platform specific documentation for a list of the available drivers. The cfg_path parameter is only present for compatibility with previous versions of Allegro, and has no effect on anything.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero if the sound is successfully installed, and -1 on failure. If it fails it will store a description of the problem in allegro_error. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-remove_sound/">remove_sound</a></code>(3), <code><a href="/docs/linux/man/3-reserve_voices/">reserve_voices</a></code>(3), <code><a href="/docs/linux/man/3-detect_digi_driver/">detect_digi_driver</a></code>(3), <code><a href="/docs/linux/man/3-detect_midi_driver/">detect_midi_driver</a></code>(3), <code><a href="/docs/linux/man/3-set_volume/">set_volume</a></code>(3), <code><a href="/docs/linux/man/3-play_sample/">play_sample</a></code>(3), <code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3), <code><a href="/docs/linux/man/3-play_audio_stream/">play_audio_stream</a></code>(3), <code><a href="/docs/linux/man/3-install_sound_input/">install_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-allegro_error/">allegro_error</a></code>(3), <code><a href="/docs/linux/man/3-set_mixer_quality/">set_mixer_quality</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3), <code><a href="/docs/linux/man/3-exsample/">exsample</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exstream/">exstream</a></code>(3) </p>
<h2>Index</h2>
