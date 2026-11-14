---
title: "envy24control(1)"
name: "envy24control"
section: "1"
letter: "e"
url: "/docs/linux/man/1-envy24control/"
description: "envy24control – GUI control tool for Envy24 (ice1712) based soundcards, under ALSA."
---

<h2>NAME</h2>
<p> envy24control &#8211; GUI control tool for Envy24 (ice1712) based soundcards, under ALSA. </p>
<h2>SYNOPSIS</h2>
<p> <code>envy24control</code> [<i>-c</i> card-number] [<i>-D</i> control-name] [<i>-o</i> 0-num DACs max 8] [<i>-i</i> 0-num ADCs max 8] [<i>-p</i> 0-8] [<i>-s</i> 0-2] [<i>-f</i> &lt;profiles file name&gt;] [<i>-v</i>] [&lt;profile number&gt;|&lt;profile name&gt;] [<i>-m</i> midi-channel] [<i>-M</i>] [<i>-w</i> window-width] [<i>-t</i> 0-9] </p>
<h2>DESCRIPTION</h2>
<p> <code>envy24control</code> allows control of the digital mixer, channel gains and other hardware settings for sound cards based on the ice1712 chipset (Midiman Delta series, Terratec EWS and EWX series). It also displays a level meter for each input and output channel. </p>
<h2>INVOKING</h2>
<p> <code>envy24control</code> [<i>-c</i> card-number] [<i>-D</i> control-name] [<i>-o</i> 0-num DACs max 8] [<i>-i</i> 0-num ADCs max 8] [<i>-p</i> 0-8] [<i>-s</i> 0-2] [<i>-f</i> &lt;profiles file name&gt;] [<i>-v</i>] [&lt;profile number&gt;|&lt;profile name&gt;] [<i>-m</i> midi-channel] [<i>-M</i>] [<i>-w</i> window-width] [<i>-t</i> 0-9]</p>
<dl>
<dt>If no control-name is given, then the first sound card is used.</p>
<dd>
</dl>
<h3>Options</h3>
<dl>
<dt><i>-c</i> card-number</p>
<dd> Use the card specified by card-number rather than the first card. This is equivalent with <i>-Dhw:n</i> option where <i>n</i> is the card number.</p>
<dt><i>-D</i> control-name</p>
<dd> Use the card specified by control-name rather than the first card, normally this will be of the form hw:<i>n</i> where <i>n</i> is the sound card number (zero-based). This is only needed if you have more than one Envy24-based card or if your Envy24 card is not configured as the first card in your ALSA driver setup.</p>
<dt><i>-o</i> outputs</p>
<dd> Limit number of analog line outputs to display. Default is the number of DACs in the driver specification. Maximum is 8. The number of analog output lines can only be reduced from the available number of output lines.</p>
<dt><i>-i</i> inputs</p>
<dd> Limit number of analog line inputs to display. Default is the number of ADCs in the driver specification. Maximum is 8. The number of analog input lines can only be reduced from the available number of input lines.</p>
<dt><i>-p</i> pcm outputs</p>
<dd> Limit number of PCM outputs to display. Default is 8.</p>
<dt><i>-s</i> spdif inputs/outputs</p>
<dd> Limit number of SPDIF inputs/outputs to display. Default is 2.</p>
<dt><i>-f</i> name and path of the profiles file name.</p>
<dd> From/to this file will envy24control read/write the alsactl settings. If is not given DEFAULT_PROFILERC or for restore if DEFAULT_PROFILERC doesn&#8217;t exists SYS_PROFILERC will be used.</p>
<dt><i>-v</i> view spdif playback channels in the mixer.</p>
<dd> It is not possible to manage something (muting, volume levels). It is only to view the levelmeters. Default is no view of spdif playback channels in the mixer.</p>
<dt><i>-m</i> midi-channel</p>
<dd> Use MIDI controller values to control the Faders in the mixer view. The application will react to controllers on channel midi-channel and send controllers on this channel when the user moves the GUI sliders.</p>
<dt><i>-M</i></p>
<dd> Use an enhanced mapping from midi controller values to db sliders.</p>
<dt><i>-w</i> window-width</p>
<dd> Specify the initial width of the envy24control window. Using window-width in the range 0-20 specifies approx number of mixer channels visible. Values &gt;20 are interpreted as screen pixels.</p>
<dt><i>-t</i> tall-equal mixer heights</p>
<dd> Using <i>-t</i> 1 enlarges the channel mixers to the same height as the digital mixer. With values &gt;1 the height of all mixers is increased in stages. <i>-t</i> 0 is the default, set for minimum window height.</dl>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1), <a href="/docs/linux/man/1-amixer/">amixer</a>(1), <a href="/docs/linux/man/1-gamix/">gamix</a>(1) </code> </p>
<h2>AUTHOR</h2>
<p> <code>envy24control</code> is by Jaroslav Kysela &lt;perex [at] perex.cz&gt; This document is by James Tappin &lt;james [at] xena.uklinux.net&gt;. Updated by Dirk Kalis &lt;dirk.kalis [at] t-online.de&gt;. Options<i>-w and -t</i> added Alan Horstmann &lt;gineera [at] aspect135.co.uk&gt; </p>
<h2>Index</h2>
