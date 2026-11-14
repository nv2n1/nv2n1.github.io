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
<dt><code>-a, &#8211;amplify</code> <i>factor</i></p>
<dd> Amplification factor for the software mixer. Valid amplification factors range from 0 to 3. Default is 1. . Warning: higher amplification factors may cause distorted or noisy output.</p>
<dt><code>-b, &#8211;bits</code> <i>bits</i></p>
<dd> Set the software mixer resolution (8 or 16 bits). If ommited, The audio device will be opened at the highest resolution available.</p>
<dt><code>-c, &#8211;stdout</code></p>
<dd> Mix the module to stdout.</p>
<dt><code>-D</code> <i>device-specific parameter</i></p>
<dd> Pass a configuration parameter to the device driver. See the <code>DEVICE DRIVER PARAMETERS</code> section below for a list of known parameters.</p>
<dt><code>-d, &#8211;driver</code> <i>driver</i></p>
<dd> Select the output driver. If not specified, <code>xmp</code> will try to probe each available driver.</p>
<dt><code>-F, &#8211;nofilter</code></p>
<dd> Disable IT lowpass filter effect and envelopes.</p>
<dt><code>-f, &#8211;frequency</code> <i>rate</i></p>
<dd> Set the software mixer sampling rate in hertz.</p>
<dt><code>&#8211;fix-sample-loop</code></p>
<dd> Halve sample loop start values. Use it to work around bad conversions from 15-instrument modules and to correctly play NoisePacker v2 and certain UNIC files.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show a short summary of command-line options.</p>
<dt><code>-I, &#8211;instrument-path</code> <i>path</i></p>
<dd> Set the pathname to the directory containing external samples.</p>
<dt><code>-i, &#8211;interpolation</code> <i>type</i></p>
<dd> Select interpolation type. Available types are <i>nearest</i> for nearest-neighbor interpolation, <i>linear for linear interpolation, and spline for cubic spline interpolation. Default is cubic spline.</p>
<dt></i><code>&#8211;load-only</code></p>
<dd> Load module and exit.</p>
<dt><code>-L, &#8211;list-formats</code></p>
<dd> List supported module formats.</p>
<dt><code>-l, &#8211;loop</code></p>
<dd> Enable module looping.</p>
<dt><code>&#8211;loop-all</code></p>
<dd> Loop over the entire module list.</p>
<dt><code>-M, &#8211;mute</code> <i>channel-list</i></p>
<dd> Mute the specified channels. <i>channel-list</i> is a comma-separated list of decimal channel ranges. Example: 0,2-4,8-16.</p>
<dt><code>-m, &#8211;mono</code></p>
<dd> Force mono output (default is stereo in stereo-capable devices).</p>
<dt><code>-N, &#8211;null</code></p>
<dd> Load and mix module, but discard output data (same as &#8211;device=null).</p>
<dt><code>&#8211;nocmd</code></p>
<dd> Disable interactive commands.</p>
<dt><code>-o, &#8211;output-file</code> <i>filename</i></p>
<dd> Set the output file name when mixing to raw or WAV files. If &#8216;-&#8216; is given as the file name, the output will be sent to stdout.</p>
<dt><code>&#8211;offset-bug-emulation</code></p>
<dd> Emulate Protracker 2.x handling of effect 0x09 (set sample offset).</p>
<dt><code>-P, &#8211;pan</code> <i>num</i></p>
<dd> Set the percentual panning amplitude.</p>
<dt><code>&#8211;probe-only</code></p>
<dd> Exit after probing the audio device.</p>
<dt><code>-R, &#8211;random</code></p>
<dd> Play modules in random order.</p>
<dt><code>-r, &#8211;reverse</code></p>
<dd> Reverse left/right stereo channels.</p>
<dt><code>-S, &#8211;solo</code> <i>channel-list</i></p>
<dd> Play only the specified channels. <i>channel-list</i> is a comma-separated list of decimal channel ranges. Example: 0,2-4,8-16.</p>
<dt><code>-s, &#8211;start</code> <i>pos</i></p>
<dd> Start playing the module from the position <i>pos</i>.</p>
<dt><code>-t, &#8211;time</code> <i>time</i></p>
<dd> Specifies the maximum playing time to <i>time</i> seconds.</p>
<dt><code>-u, &#8211;unsigned</code></p>
<dd> Tell the software mixer to use unsigned samples when mixing to a file (default is signed).</p>
<dt><code>&#8211;vblank</code></p>
<dd> Force Amiga vblank-based timing (no CIA tempo setting).</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print version information.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Verbose mode (incremental). If specified more than once, the verbosity level will be increased (no messages will be displayed when the player runs in background).</p>
<dt><code>-Z, &#8211;all-sequences</code></p>
<dd> Play all hidden or alternative pattern sequences (subsongs) in module.</p>
<dt><code>-z, &#8211;sequence</code> <i>num</i></p>
<dd> Play hidden or alternative pattern sequence <i>num</i>&nbsp;<wbr>(0 is the main sequence).</dl>
<h2>DEVICE DRIVER PARAMETERS</h2>
<p> Use the option <code>-D</code> to send parameters directly to the device drivers. Multiple <code>-D</code> options can be specified in the command line. </p>
<p> File output options:</p>
<dl>
<dt><code>-D</code> <i>endian=big</i></p>
<dd> Generate big-endian 16-bit samples (default is the machine byte ordering).</p>
<dt><code>-D</code> <i>endian=little</i></p>
<dd> Generate little-endian 16-bit samples (default is the machine byte ordering).</dl>
<p> ALSA driver options:</p>
<dl>
<dt><code>-D</code> <i>buffer=value</i></p>
<dd> Set buffer size in ms. Default value is 250.</p>
<dt><code>-D</code> <i>period=value</i></p>
<dd> Set period time in ms. Default value is 50.</p>
<dt><code>-D</code> <i>card=name</i></p>
<dd> Choose the ALSA device to use. Default value is &quot;default&quot;.</dl>
<p> OSS driver options:</p>
<dl>
<dt><code>-D</code> <i>frag=num,size</i></p>
<dd> Set the maximum number of fragments to <i>num</i> and the size of each fragment to <i>size</i> bytes (must be a power of two). The number and size of fragments set a tradeoff between the buffering latency and sensibility to system load. To get better synchronization, reduce the values. To avoid gaps in the sound playback, increase the values.</p>
<dt><code>-D</code> <i>dev=device_name</i></p>
<dd> Set the audio device to open. Default is /dev/dsp.</p>
<dt><code>-D</code> <i>nosync</i></p>
<dd> Don&#8217;t sync the OSS audio device between modules.</dl>
<p> BSD driver options:</p>
<dl>
<dt><code>-D</code> <i>gain=value</i></p>
<dd> Set the audio gain. Valid values range from 0 to 255. The default is 128.</p>
<dt><code>-D</code> <i>buffer=size</i></p>
<dd> Set the size in bytes of the audio buffer. Default value is 32 Kb.</dl>
<p> HP-UX and Solaris driver options:</p>
<dl>
<dt><code>-D</code> <i>gain=value</i></p>
<dd> Set the audio gain. Valid values range from 0 to 255. The default is 128.</p>
<dt><code>-D</code> <i>port={s|h|l}</i></p>
<dd> Set the audio port. Valid arguments are <i>s</i> for the internal speaker, <i>h</i> for headphones and <i>l</i> for line out. The default is the internal speaker.</p>
<dt><code>-D</code> <i>buffer=size</i></p>
<dd> Set the size in bytes of the audio buffer. The default value is 32 Kb.</dl>
<h2>INTERACTIVE COMMANDS</h2>
<p> The following single key commands can be used when playing modules:</p>
<dl>
<dt><code>q, Esc</code></p>
<dd> Stop the currently playing module and quit the player.</p>
<dt><code>f, Right</code></p>
<dd> Jump to the next pattern.</p>
<dt><code>b, Left</code></p>
<dd> Jump to the previous pattern.</p>
<dt><code>n, Up</code></p>
<dd> Jump to the next module.</p>
<dt><code>p, Down</code></p>
<dd> Jump to the previous module.</p>
<dt><code>Space</code></p>
<dd> Pause or unpause module replay.</p>
<dt><code>1</code>, <code>2</code>, <code>3</code>, <code>4</code>, <code>5</code>, <code>6</code>, <code>7</code>, <code>8</code>, <code>9</code>, <code>0</code></p>
<dd> Mute/unmute channels 1 to 10.</p>
<dt><code>!</code></p>
<dd> Unmute all channels.</p>
<dt><code>?</code></p>
<dd> Display available commands.</p>
<dt><code>Z</code></p>
<dd> Display current sequence.</p>
<dt><code>z</code></p>
<dd> Toggle subsong explorer mode.</p>
<dt><code>l</code></p>
<dd> Toggle module/sequence looping.</p>
<dt><code>m</code></p>
<dd> Display module information.</p>
<dt><code>i</code></p>
<dd> Display combined instrument/sample list.</p>
<dt><code>I</code></p>
<dd> Display instrument list.</p>
<dt><code>S</code></p>
<dd> Display sample list.</p>
<dt><code>&lt;</code></p>
<dd> Change to previous sequence (subsong).</p>
<dt><code>&gt;</code></p>
<dd> Change to next sequence (subsong).</dl>
<p> Interactive mode can be disabled using the <code>&#8211;nocmd</code> command line option. </p>
<h2>EXAMPLES</h2>
<p> Play module and save output in a .wav file:</p>
<dl>
<dt>
<dd> <tt>xmp -ofilename.wav module.mod</tt></dl>
<p> Play module muting channels 0 to 3 and 6:</p>
<dl>
<dt>
<dd> <tt>xmp --mute=0-3,6 module.mod.gz</tt></dl>
<p> Play modules in /dev/dsp using the default device settings (unsigned 8bit, 8 kHz mono):</p>
<dl>
<dt>
<dd> <tt>xmp -o/dev/dsp -f8000 -m -b8 -u module.lha</tt></dl>
<p> Play all XM modules in the /mod directory and all subdirectories in random order, ignoring any configuration set in the xmp.conf file:</p>
<dl>
<dt>
<dd> <tt>xmp --norc -R `find /mod -name &quot;*.xm&quot; -print`</tt></dl>
<h2>FILES</h2>
<p> <tt>/etc/xmp/xmp.conf, $HOME/.xmp/xmp.conf, /etc/xmp/modules.conf, $HOME/.xmp/modules.conf</tt> </p>
<h2>AUTHORS</h2>
<p> Claudio Matsuoka and Hipolito Carraro Jr. </p>
<h2>Index</h2>
