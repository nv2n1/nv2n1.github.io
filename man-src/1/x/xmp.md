---
title: "xmp(1)"
name: "xmp"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xmp/"
description: "xmp – Extended Module Player"
---

<h2>NAME</h2>
<p> xmp &#8211; Extended Module Player </p>
<h2>SYNOPSIS</h2>
<p> <code>xmp</code> [<code>-a, &#8211;amplify</code> <i>factor</i>] [<code>-b, &#8211;bits</code> <i>bits</i>] [<code>-c, &#8211;stdout</code>] [<code>-D</code> <i>device-specific parameters</i>] [<code>-d, &#8211;driver</code> <i>driver</i>] [<code>-F, &#8211;nofilter</code>] [<code>-f, &#8211;frequency</code> <i>rate</i>] [<code>&#8211;fix-sample-loop</code>] [<code>-h, &#8211;help</code>] [<code>-I, &#8211;instrument-path</code>] [<code>-i, &#8211;interpolation </code><i>type</i>] [<code>&#8211;load-only</code>] [<code>-L, &#8211;list-formats</code>] [<code>-l, &#8211;loop</code>] [<code>&#8211;loop-all</code>] [<code>-M, &#8211;mute</code> <i>channel-list</i>] [<code>-m, &#8211;mono</code>] [<code>-N, &#8211;null</code>] [<code>&#8211;nocmd</code>] [<code>-o, &#8211;output-file</code> <i>filename</i>] [<code>&#8211;offset-bug-emulation</code>] [<code>-P, &#8211;pan</code> <i>pan</i>] [<code>&#8211;probe-only</code>] [<code>-q, &#8211;quiet</code>] [<code>-R, &#8211;random</code>] [<code>-S, &#8211;solo</code> <i>channel-list</i>] [<code>-s, &#8211;start</code> <i>pos</i>] [<code>-t, &#8211;time</code> <i>time</i>] [<code>-u, &#8211;unsigned</code>] [<code>&#8211;vblank</code>] [<code>-V, &#8211;version</code>] [<code>-v, &#8211;verbose</code>] [<code>-Z, &#8211;all-sequences</code>] [<code>-z, &#8211;sequence</code>] <i>modules</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>xmp</code> is a tracked music module player. It plays many module formats including Fasttracker II (XM), Noise/Fast/Protracker (MOD), Scream Tracker 3 (S3M) and Impulse Tracker (IT). Run <tt>xmp --list-formats</tt> for a complete list of supported formats. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a, &#8211;amplify</code> <i>factor</i></dt>
<dd> Amplification factor for the software mixer. Valid amplification factors range from 0 to 3. Default is 1. . Warning: higher amplification factors may cause distorted or noisy output.</dd>
<dt><code>-b, &#8211;bits</code> <i>bits</i></dt>
<dd> Set the software mixer resolution (8 or 16 bits). If ommited, The audio device will be opened at the highest resolution available.</dd>
<dt><code>-c, &#8211;stdout</code></dt>
<dd> Mix the module to stdout.</dd>
<dt><code>-D</code> <i>device-specific parameter</i></dt>
<dd> Pass a configuration parameter to the device driver. See the <code>DEVICE DRIVER PARAMETERS</code> section below for a list of known parameters.</dd>
<dt><code>-d, &#8211;driver</code> <i>driver</i></dt>
<dd> Select the output driver. If not specified, <code>xmp</code> will try to probe each available driver.</dd>
<dt><code>-F, &#8211;nofilter</code></dt>
<dd> Disable IT lowpass filter effect and envelopes.</dd>
<dt><code>-f, &#8211;frequency</code> <i>rate</i></dt>
<dd> Set the software mixer sampling rate in hertz.</dd>
<dt><code>&#8211;fix-sample-loop</code></dt>
<dd> Halve sample loop start values. Use it to work around bad conversions from 15-instrument modules and to correctly play NoisePacker v2 and certain UNIC files.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Show a short summary of command-line options.</dd>
<dt><code>-I, &#8211;instrument-path</code> <i>path</i></dt>
<dd> Set the pathname to the directory containing external samples.</dd>
<dt><code>-i, &#8211;interpolation</code> <i>type</i></dt>
<dd> Select interpolation type. Available types are <i>nearest</i> for nearest-neighbor interpolation, <i>linear for linear interpolation, and spline for cubic spline interpolation. Default is cubic spline.</dd>
<dt></i><code>&#8211;load-only</code></dt>
<dd> Load module and exit.</dd>
<dt><code>-L, &#8211;list-formats</code></dt>
<dd> List supported module formats.</dd>
<dt><code>-l, &#8211;loop</code></dt>
<dd> Enable module looping.</dd>
<dt><code>&#8211;loop-all</code></dt>
<dd> Loop over the entire module list.</dd>
<dt><code>-M, &#8211;mute</code> <i>channel-list</i></dt>
<dd> Mute the specified channels. <i>channel-list</i> is a comma-separated list of decimal channel ranges. Example: 0,2-4,8-16.</dd>
<dt><code>-m, &#8211;mono</code></dt>
<dd> Force mono output (default is stereo in stereo-capable devices).</dd>
<dt><code>-N, &#8211;null</code></dt>
<dd> Load and mix module, but discard output data (same as &#8211;device=null).</dd>
<dt><code>&#8211;nocmd</code></dt>
<dd> Disable interactive commands.</dd>
<dt><code>-o, &#8211;output-file</code> <i>filename</i></dt>
<dd> Set the output file name when mixing to raw or WAV files. If &#8216;-&#8216; is given as the file name, the output will be sent to stdout.</dd>
<dt><code>&#8211;offset-bug-emulation</code></dt>
<dd> Emulate Protracker 2.x handling of effect 0x09 (set sample offset).</dd>
<dt><code>-P, &#8211;pan</code> <i>num</i></dt>
<dd> Set the percentual panning amplitude.</dd>
<dt><code>&#8211;probe-only</code></dt>
<dd> Exit after probing the audio device.</dd>
<dt><code>-R, &#8211;random</code></dt>
<dd> Play modules in random order.</dd>
<dt><code>-r, &#8211;reverse</code></dt>
<dd> Reverse left/right stereo channels.</dd>
<dt><code>-S, &#8211;solo</code> <i>channel-list</i></dt>
<dd> Play only the specified channels. <i>channel-list</i> is a comma-separated list of decimal channel ranges. Example: 0,2-4,8-16.</dd>
<dt><code>-s, &#8211;start</code> <i>pos</i></dt>
<dd> Start playing the module from the position <i>pos</i>.</dd>
<dt><code>-t, &#8211;time</code> <i>time</i></dt>
<dd> Specifies the maximum playing time to <i>time</i> seconds.</dd>
<dt><code>-u, &#8211;unsigned</code></dt>
<dd> Tell the software mixer to use unsigned samples when mixing to a file (default is signed).</dd>
<dt><code>&#8211;vblank</code></dt>
<dd> Force Amiga vblank-based timing (no CIA tempo setting).</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Print version information.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Verbose mode (incremental). If specified more than once, the verbosity level will be increased (no messages will be displayed when the player runs in background).</dd>
<dt><code>-Z, &#8211;all-sequences</code></dt>
<dd> Play all hidden or alternative pattern sequences (subsongs) in module.</dd>
<dt><code>-z, &#8211;sequence</code> <i>num</i></dt>
<dd> Play hidden or alternative pattern sequence <i>num</i>&nbsp;<wbr>(0 is the main sequence).</dd></dl>
<h2>DEVICE DRIVER PARAMETERS</h2>
<p> Use the option <code>-D</code> to send parameters directly to the device drivers. Multiple <code>-D</code> options can be specified in the command line. </p>
<p> File output options:</p>
<dl>
<dt><code>-D</code> <i>endian=big</i></dt>
<dd> Generate big-endian 16-bit samples (default is the machine byte ordering).</dd>
<dt><code>-D</code> <i>endian=little</i></dt>
<dd> Generate little-endian 16-bit samples (default is the machine byte ordering).</dd></dl>
<p> ALSA driver options:</p>
<dl>
<dt><code>-D</code> <i>buffer=value</i></dt>
<dd> Set buffer size in ms. Default value is 250.</dd>
<dt><code>-D</code> <i>period=value</i></dt>
<dd> Set period time in ms. Default value is 50.</dd>
<dt><code>-D</code> <i>card=name</i></dt>
<dd> Choose the ALSA device to use. Default value is &quot;default&quot;.</dd></dl>
<p> OSS driver options:</p>
<dl>
<dt><code>-D</code> <i>frag=num,size</i></dt>
<dd> Set the maximum number of fragments to <i>num</i> and the size of each fragment to <i>size</i> bytes (must be a power of two). The number and size of fragments set a tradeoff between the buffering latency and sensibility to system load. To get better synchronization, reduce the values. To avoid gaps in the sound playback, increase the values.</dd>
<dt><code>-D</code> <i>dev=device_name</i></dt>
<dd> Set the audio device to open. Default is /dev/dsp.</dd>
<dt><code>-D</code> <i>nosync</i></dt>
<dd> Don&#8217;t sync the OSS audio device between modules.</dd></dl>
<p> BSD driver options:</p>
<dl>
<dt><code>-D</code> <i>gain=value</i></dt>
<dd> Set the audio gain. Valid values range from 0 to 255. The default is 128.</dd>
<dt><code>-D</code> <i>buffer=size</i></dt>
<dd> Set the size in bytes of the audio buffer. Default value is 32 Kb.</dd></dl>
<p> HP-UX and Solaris driver options:</p>
<dl>
<dt><code>-D</code> <i>gain=value</i></dt>
<dd> Set the audio gain. Valid values range from 0 to 255. The default is 128.</dd>
<dt><code>-D</code> <i>port={s|h|l}</i></dt>
<dd> Set the audio port. Valid arguments are <i>s</i> for the internal speaker, <i>h</i> for headphones and <i>l</i> for line out. The default is the internal speaker.</dd>
<dt><code>-D</code> <i>buffer=size</i></dt>
<dd> Set the size in bytes of the audio buffer. The default value is 32 Kb.</dd></dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> The following single key commands can be used when playing modules:</p>
<dl>
<dt><code>q, Esc</code></dt>
<dd> Stop the currently playing module and quit the player.</dd>
<dt><code>f, Right</code></dt>
<dd> Jump to the next pattern.</dd>
<dt><code>b, Left</code></dt>
<dd> Jump to the previous pattern.</dd>
<dt><code>n, Up</code></dt>
<dd> Jump to the next module.</dd>
<dt><code>p, Down</code></dt>
<dd> Jump to the previous module.</dd>
<dt><code>Space</code></dt>
<dd> Pause or unpause module replay.</dd>
<dt><code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, <code>6</code>, <code>7</code>, <code>8</code>, <code>9</code>, <code>0</code></dt>
<dd> Mute/unmute channels 1 to 10.</dd>
<dt><code>!</code></dt>
<dd> Unmute all channels.</dd>
<dt><code>?</code></dt>
<dd> Display available commands.</dd>
<dt><code>Z</code></dt>
<dd> Display current sequence.</dd>
<dt><code>z</code></dt>
<dd> Toggle subsong explorer mode.</dd>
<dt><code>l</code></dt>
<dd> Toggle module/sequence looping.</dd>
<dt><code>m</code></dt>
<dd> Display module information.</dd>
<dt><code>i</code></dt>
<dd> Display combined instrument/sample list.</dd>
<dt><code>I</code></dt>
<dd> Display instrument list.</dd>
<dt><code>S</code></dt>
<dd> Display sample list.</dd>
<dt><code>&lt;</code></dt>
<dd> Change to previous sequence (subsong).</dd>
<dt><code>&gt;</code></dt>
<dd> Change to next sequence (subsong).</dd></dl>
<p> Interactive mode can be disabled using the <code>&#8211;nocmd</code> command line option. </p>
<h2>EXAMPLES</h2>
<p> Play module and save output in a .wav file:</p>
<dl>
<dt>
</dt><dd> <tt>xmp -ofilename.wav module.mod</tt></dd></dl>
<p> Play module muting channels 0 to 3 and 6:</p>
<dl>
<dt>
</dt><dd> <tt>xmp --mute=0-3,6 module.mod.gz</tt></dd></dl>
<p> Play modules in /dev/dsp using the default device settings (unsigned 8bit, 8 kHz mono):</p>
<dl>
<dt>
</dt><dd> <tt>xmp -o/dev/dsp -f8000 -m -b8 -u module.lha</tt></dd></dl>
<p> Play all XM modules in the /mod directory and all subdirectories in random order, ignoring any configuration set in the xmp.conf file:</p>
<dl>
<dt>
</dt><dd> <tt>xmp --norc -R `find /mod -name &quot;*.xm&quot; -print`</tt></dd></dl>
<h2>FILES</h2>
<p> <tt>/etc/xmp/xmp.conf, $HOME/.xmp/xmp.conf, /etc/xmp/modules.conf, $HOME/.xmp/modules.conf</tt> </p>
<h2>AUTHORS</h2>
<p> Claudio Matsuoka and Hipolito Carraro Jr. </p>
