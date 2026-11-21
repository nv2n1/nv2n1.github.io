---

title: "alsa_in(1)"
name: "alsa_in"
section: "1"
letter: "a"
url: "/docs/linux/man/1-alsa_in/"
description: "alsa_in, alsa_out – Jack clients that perform I/O with an alternate audio interface"
---

<h2>NAME</h2>
<p> <code>alsa_in</code>, <code>alsa_out</code> &#8211; Jack clients that perform I/O with an alternate audio interface</p>
<p> <code>alsa_in</code> [<i>options</i>]<br />
 <code>alsa_out</code> [<i>options</i>] </p>
<p> A JACK client that opens a specified audio interface (different to the one used by the JACK server, if any) and moves audio data between its JACK ports and the interface. alsa_in will provide data from the interface (potentially for capture); alsa_out will deliver data to it (for playback). </p>
<p> The audio interface used by alsa_in/alsa_out does not need to be synchronized with JACK backend (or the hardware it might be using). alsa_in/alsa_out tries to resample the output stream in an attempt to compensate for drift between the two clocks. </p>
<p> As of jack-0.116.3 this works almost perfectly. It takes some time, to reach absolute resample-rate stability. So give it some minutes (its intended to be running permanently anyways) </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-j </code><i> jack_client_name</i></dt>
<dd>
 Set Client Name.</dd>
<dt><code>-d </code><i> alsa_device</i></dt>
<dd>
 Use this Soundcard.</dd>
<dt><code>-v</code></dt>
<dd>
 Verbose, prints out resample coefficient and other parameters useful for debugging, every 500ms. also reports soft xruns.</dd>
<dt><code>-i</code></dt>
<dd>
 Instrumentation. This logs the 4 important parameters of the samplerate control algorithm every 1ms. You can pipe this into a file, and plot it. Should only be necessary, if it does not work as expected, and we need to adjust some of the obscure parameters, to make it work. Find me on irc.freenode.org #jack in order to set this up correctly.</dd>
<dt><code>-c </code><i> channels</i></dt>
<dd>
 Set Number of channels.</dd>
<dt><code>-r </code><i> sample_rate</i></dt>
<dd>
 Set sample_rate. The program resamples as necessary. So you can connect a 44k1 jackd to a soundcard only supporting 48k. (default is jack sample_rate)</dd>
<dt><code>-p </code><i> period_size</i></dt>
<dd>
 Set the period size. It is not related to the jackd period_size. Sometimes it affects the quality of the delay measurements. Setting this lower than the jackd period_size will only work, if you use a higher number of periods.</dd>
<dt><code>-n </code><i> num_period</i></dt>
<dd>
 Set number of periods. See note for period_size.</dd>
<dt><code>-q </code><i> quality</i></dt>
<dd>
 Set the quality of the resampler from 0 to 4. can significanly reduce cpu usage.</dd>
<dt><code>-m </code><i> max_diff</i></dt>
<dd>
 The value when a soft xrun occurs. Basically the window, in which the dma pointer may jitter. I don&#8217;t think its necessary to play with this anymore.</dd>
<dt><code>-t </code><i> target_delay</i></dt>
<dd>
 The delay alsa_io should try to approach. Same as for max_diff. It will be setup based on -p and -n which is generally sufficient.</dd>
<dt><code>-s </code><i> smooth_array_size</i></dt>
<dd>
 This parameter controls the size of the array used for smoothing the delay measurement. Its default is 256. If you use a pretty low period size, you can lower the CPU usage a bit by decreasing this parameter. However most CPU time is spent in the resampling so this will not be much.</dd>
<dt><code>-C </code><i> P Control Clamp</i></dt>
<dd>
 If you have a PCI card, then the default value (15) of this parameter is too high for -p64 -n2&#8230; Setting it to 5 should fix that. Be aware that setting this parameter too low, lets the hf noise on the delay measurement come through onto the resamplerate, so this might degrade the quality of the output. (but its a threshold value, and it has been chosen, to mask the noise of a USB card, which has an amplitude which is 50 times higher than that of a PCI card, so 5 wont loose you any quality on a PCI card) </dd>
</dl>
<h2>AUTHOR</h2>
<p> Torben Hohn </p>
