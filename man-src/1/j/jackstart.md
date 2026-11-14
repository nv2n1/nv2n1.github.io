---
title: "jackstart(1)"
name: "jackstart"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jackstart/"
description: "jackd – JACK Audio Connection Kit sound server"
---

<h2>NAME</h2>
<p> jackd &#8211; JACK Audio Connection Kit sound server</p>
<h2>SYNOPSIS</h2>
<p> <code>jackd</code> [<i>options</i>] <code>-d</code><i> backend </i> [<i>backend-parameters</i>]<br />
 <code>jackd &#8211;help</code></p>
<h2>DESCRIPTION</h2>
<p> <code>jackd</code> is the JACK audio server daemon, a low-latency audio server. Originally written for the GNU/Linux operating system, it also supports Mac OS X and various Unix platforms. JACK can connect a number of different client applications to an audio device and also to each other. Most clients are external, running in their own processes as normal applications. JACK also supports internal clients, which run within the <code>jackd</code> process using a loadable &quot;plugin&quot; interface. </p>
<p> JACK differs from other audio servers in being designed from the ground up for professional audio work. It focuses on two key areas: synchronous execution of all clients, and low latency operation. </p>
<p> For the latest JACK information, please consult the web site, &lt;<code><a rel="nofollow" href="http://www.jackaudio.org">http://www.jackaudio.org</a></code>&gt;.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-d, &#8211;driver </code><i>backend</i> [<i>backend-parameters</i> ]</p>
<dd>
 Select the audio interface backend. The current list of supported backends is: <code>alsa</code>, <code>coreaudio</code>, <code>dummy</code>, <code>freebob</code>, <code>oss</code> <code>sun</code> and <code>portaudio</code>. They are not all available on all platforms. All <i>backend-parameters</i> are optional. </p>
<dt><code>-h, &#8211;help</code></p>
<dd>
 Print a brief usage message describing the main <code>jackd</code> options. These do not include <i>backend-parameters</i>, which are listed using the <code>&#8211;help</code> option for each specific backend. Examples below show how to list them.</p>
<dt><code>-m, &#8211;no-mlock</code></p>
<dd> Do not attempt to lock memory, even if <code>&#8211;realtime</code>.</p>
<dt><code>-n, &#8211;name</code> <i>server-name</i></p>
<dd> Name this <code>jackd</code> instance <i>server-name</i>. If unspecified, this name comes from the <code>$JACK_DEFAULT_SERVER</code> environment variable. It will be &quot;default&quot; if that is not defined.</p>
<dt><code>-p, &#8211;port-max </code><i> n</i></p>
<dd> Set the maximum number of ports the JACK server can manage. The default value is 256.</p>
<dt><code>&#8211;replace-registry</code></p>
<dd>
 Remove the shared memory registry used by all JACK server instances before startup. This should rarely be used, and is intended only for occasions when the structure of this registry changes in ways that are incompatible across JACK versions (which is rare).</p>
<dt><code>-R, &#8211;realtime</code></p>
<dd>
 Use realtime scheduling (default = true). This is needed for reliable low-latency performance. On many systems, it requires <code>jackd</code> to run with special scheduler and memory allocation privileges, which may be obtained in several ways.</p>
<dt><code>-r, &#8211;no-realtime</code></p>
<dd>
 Do not use realtime scheduling.</p>
<dt><code>-P, &#8211;realtime-priority </code><i>int</i></p>
<dd> When running <code>&#8211;realtime</code>, set the scheduler priority to <i>int</i>.</p>
<dt><code>&#8211;silent</code></p>
<dd> Silence any output during operation.</p>
<dt><code>-T, &#8211;temporary</code></p>
<dd> Exit once all clients have closed their connections.</p>
<dt><code>-t, &#8211;timeout </code><i>int</i></p>
<dd>
 Set client timeout limit in milliseconds. The default is 500 msec. In realtime mode the client timeout must be smaller than the watchdog timeout (5000 msec).</p>
<dt><code>-Z, &#8211;nozombies</code></p>
<dd>
 Prevent JACK from ever kicking out clients because they were too slow. This cancels the effect any specified timeout value, but JACK and its clients are still subject to the supervision of the watchdog thread or its equivalent.</p>
<dt><code>-u, &#8211;unlock</code></p>
<dd>
 Unlock libraries GTK+, QT, FLTK, Wine.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Give verbose output.</p>
<dt><code>-c, &#8211;clocksource</code> (<i> c(ycle)</i> | <i> h(pet) </i> | <i> s(ystem) </i>)</p>
<dd> Select a specific wall clock (Cycle Counter, HPET timer, System timer).</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Print the current JACK version number and exit.</dl>
<h3>ALSA BACKEND OPTIONS</h3>
<dl>
<dt><code>-C, &#8211;capture</code> [ <i>name</i> ]</p>
<dd> Provide only capture ports, unless combined with -D or -P. Parameterally set capture device name.</p>
<dt><code>-d, &#8211;device </code><i>name</i></p>
<dd>
 The ALSA pcm device <i>name</i> to use. If none is specified, JACK will use &quot;hw:0&quot;, the first hardware card defined in <code>/etc/modules.conf</code>.</p>
<dt><code>-z, &#8211;dither [rectangular,triangular,shaped,none]</p>
<dd> Set dithering mode. If none</code> or unspecified, dithering is off. Only the first letter of the mode name is required.</p>
<dt><code>-D, &#8211;duplex</code></p>
<dd> Provide both capture and playback ports. Defaults to on unless only one of -P or -C is specified.</p>
<dt><code>-h, &#8211;help</code> Print a brief usage message describing only the</p>
<dd> <code>alsa</code> backend parameters.</p>
<dt><code>-M, &#8211;hwmeter</code></p>
<dd>
 Enable hardware metering for devices that support it. Otherwise, use software metering.</p>
<dt><code>-H, &#8211;hwmon</code></p>
<dd>
 Enable hardware monitoring of capture ports. This is a method for obtaining &quot;zero latency&quot; monitoring of audio input. It requires support in hardware and from the underlying ALSA device driver. </p>
<p> When enabled, requests to monitor capture ports will be satisfied by creating a direct signal path between audio interface input and output connectors, with no processing by the host computer at all. This offers the lowest possible latency for the monitored signal. </p>
<p> Presently (March 2003), only the RME Hammerfall series and cards based on the ICE1712 chipset (M-Audio Delta series, Terratec, and others) support <code>&#8211;hwmon</code>. In the future, some consumer cards may also be supported by modifying their mixer settings. </p>
<p> Without <code>&#8211;hwmon</code>, port monitoring requires JACK to read audio into system memory, then copy it back out to the hardware again, imposing the basic JACK system latency determined by the <code>&#8211;period</code> and <code>&#8211;nperiods</code> parameters.</p>
<dt><code>-i, &#8211;inchannels </code><i>int</i></p>
<dd>
 Number of capture channels. Default is maximum supported by hardware.</p>
<dt><code>-n, &#8211;nperiods </code><i>int</i></p>
<dd>
 Specify the number of periods of playback latency. In seconds, this corresponds to <code>&#8211;nperiods</code> times <code>&#8211;period</code> divided by <code>&#8211;rate</code>. The default is 2, the minimum allowable. For most devices, there is no need for any other value with the <code>&#8211;realtime</code> option. Without realtime privileges or with boards providing unreliable interrupts (like ymfpci), a larger value may yield fewer xruns. This can also help if the system is not tuned for reliable realtime scheduling. </p>
<p> For most ALSA devices, the hardware buffer has exactly <code>&#8211;period</code> times <code>&#8211;nperiods</code> frames. Some devices demand a larger buffer. If so, JACK will use the smallest possible buffer containing at least <code>&#8211;nperiods</code>, but the playback latency does not increase. </p>
<p> For USB audio devices it is recommended to use <code>-n 3</code>. Firewire devices supported by FFADO (formerly Freebob) are configured with <code>-n 3</code> by default.</p>
<dt><code>-o, &#8211;outchannels </code><i>int</i></p>
<dd>
 Number of playback channels. Default is maximum supported by hardware.</p>
<dt><code>-P, &#8211;playback</code> [ <i>name</i> ]</p>
<dd> Provide only playback ports, unless combined with -D or -C. Optionally set playback device name.</p>
<dt><code>-p, &#8211;period </code><i>int</i></p>
<dd>
 Specify the number of frames between JACK <code>process()</code> calls. This value must be a power of 2, and the default is 1024. If you need low latency, set <code>-p</code> as low as you can go without seeing xruns. A larger period size yields higher latency, but makes xruns less likely. The JACK capture latency in seconds is <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-r, &#8211;rate </code><i>int</i></p>
<dd> Specify the sample rate. The default is 48000.</p>
<dt><code>-S, &#8211;shorts</p>
<dd>
 Try to configure card for 16-bit samples first, only trying 32-bits if unsuccessful. Default is to prefer 32-bit samples.</p>
<dt>-s, &#8211;softmode</code></p>
<dd>
 Ignore xruns reported by the ALSA driver. This makes JACK less likely to disconnect unresponsive ports when running without <code>&#8211;realtime</code>.</p>
<dt><code>-X, &#8211;midi </code>[<i>seq</i>|<i>raw</i>]</p>
<dd>
 Specify which ALSA MIDI system to provide access to. Using <code>raw</code> will provide a set of JACK MIDI ports that correspond to each raw ALSA device on the machine. Using <code>seq</code> will provide a set of JACK MIDI ports that correspond to each ALSA &quot;sequencer&quot; client (which includes each hardware MIDI port on the machine). <code>raw</code> provides slightly better performance but does not permit JACK MIDI communication with software written to use the ALSA &quot;sequencer&quot; API.</dl>
<h3>COREAUDIO BACKEND PARAMETERS</h3>
<dl>
<dt><code>-c &#8211;channel</code></p>
<dd> Maximum number of channels (default: 2)</p>
<dt><code>-i &#8211;channelin</code></p>
<dd> Maximum number of input channels (default: 2)</p>
<dt><code>-o &#8211;channelout</code></p>
<dd> Maximum number of output channels (default: 2)</p>
<dt><code>-C &#8211;capture</code></p>
<dd> Whether or not to capture (default: true)</p>
<dt><code>-P &#8211;playback</code></p>
<dd> Whether or not to playback (default: true)</p>
<dt><code>-D &#8211;duplex</code></p>
<dd> Capture and playback (default: true)</p>
<dt><code>-r &#8211;rate</code></p>
<dd> Sample rate (default: 44100)</p>
<dt><code>-p &#8211;period</code></p>
<dd> Frames per period (default: 128). Must be a power of 2.</p>
<dt><code>-n &#8211;name</code></p>
<dd> Driver name (default: none)</p>
<dt><code>-I &#8211;id</code></p>
<dd> Audio Device ID (default: 0)</dl>
<h3>DUMMY BACKEND PARAMETERS</h3>
<dl>
<dt><code>-C, &#8211;capture </code><i>int</i></p>
<dd> Specify number of capture ports. The default value is 2.</p>
<dt><code>-P, &#8211;playback </code><i>int</i></p>
<dd> Specify number of playback ports. The default value is 2.</p>
<dt><code>-r, &#8211;rate </code><i>int</i></p>
<dd> Specify sample rate. The default value is 48000.</p>
<dt><code>-p, &#8211;period </code><i>int</i></p>
<dd> Specify the number of frames between JACK <code>process()</code> calls. This value must be a power of 2, and the default is 1024. If you need low latency, set <code>-p</code> as low as you can go without seeing xruns. A larger period size yields higher latency, but makes xruns less likely. The JACK capture latency in seconds is <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-w, &#8211;wait </code><i>int</i></p>
<dd> Specify number of usecs to wait between engine processes. The default value is 21333. </p>
</dl>
<h3>NET BACKEND PARAMETERS</h3>
<dl>
<dt>
&nbsp;<wbr><code>-i, &#8211;audio-ins&nbsp;<wbr></code><i>int</i></p>
<dd> Number of capture channels (default: 2)</p>
<dt>
&nbsp;<wbr><code>-o, &#8211;audio-outs&nbsp;<wbr></code><i>int</i></p>
<dd> Number of playback channels (default: 2)</p>
<dt>
&nbsp;<wbr><code>-I, &#8211;midi-ins&nbsp;<wbr></code><i>int</i></p>
<dd> Number of midi capture channels (default: 1)</p>
<dt><code>-O, &#8211;midi-outs </code><i>int</i></p>
<dd> Number of midi playback channels (default: 1)</p>
<dt>
&nbsp;<wbr><code>-r, &#8211;rate&nbsp;<wbr></code><i>int</i></p>
<dd> Sample rate (default: 48000)</p>
<dt><code>-p, &#8211;period </code><i>int</i></p>
<dd> Frames per period (default: 1024)</p>
<dt><code>-n, &#8211;num-periods </code><i>int</i></p>
<dd> Network latency setting in no. of periods (default: 5)</p>
<dt><code>-l, &#8211;listen-port </code><i>int</i></p>
<dd> The socket port we are listening on for sync packets (default: 3000)</p>
<dt><code>-f, &#8211;factor </code><i>int</i></p>
<dd> Factor for sample rate reduction (default: 1)</p>
<dt><code>-u, &#8211;upstream-factor </code><i>int</i></p>
<dd> Factor for sample rate reduction on the upstream (default: 0)</p>
<dt><code>-c, &#8211;celt </code><i>int</i></p>
<dd> sets celt encoding and number of kbits per channel (default: 0)</p>
<dt><code>-b, &#8211;bit-depth </code><i>int</i></p>
<dd> Sample bit-depth (0 for float, 8 for 8bit and 16 for 16bit) (default: 0)</p>
<dt><code>-t, &#8211;transport-sync </code><i>int</i></p>
<dd> Whether to slave the transport to the master transport (default: true)</p>
<dt><code>-a, &#8211;autoconf </code><i>int</i></p>
<dd> Whether to use Autoconfig, or just start. (default: true)</p>
<dt><code>-R, &#8211;redundancy </code><i>int</i></p>
<dd> Send packets N times (default: 1)</p>
<dt><code>-e, &#8211;native-endian </code><i>int</i></p>
<dd> Dont convert samples to network byte order. (default: false)</p>
<dt><code>-J, &#8211;jitterval </code><i>int</i></p>
<dd> attempted jitterbuffer microseconds on master (default: 0)</p>
<dt><code>-D, &#8211;always-deadline </code><i>int</i></p>
<dd> always use deadline (default: false) </p>
</dl>
<h3>OSS BACKEND PARAMETERS</h3>
<dl>
<dt><code>-r, &#8211;rate </code><i>int</i></p>
<dd> Specify the sample rate. The default is 48000.</p>
<dt><code>-p, &#8211;period </code><i>int</i></p>
<dd> Specify the number of frames between JACK <code>process()</code> calls. This value must be a power of 2, and the default is 1024. If you need low latency, set <code>-p</code> as low as you can go without seeing xruns. A larger period size yields higher latency, but makes xruns less likely. The JACK capture latency in seconds is <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-n, &#8211;nperiods </code><i>int</i></p>
<dd> Specify the number of periods in the hardware buffer. The default is 2. The period size (<code>-p</code>) times <code>&#8211;nperiods</code> times four is the JACK buffer size in bytes. The JACK output latency in seconds is <code>&#8211;nperiods</code> times <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-w, &#8211;wordlength </code><i>int</i></p>
<dd> Specify the sample size in bits. The default is 16.</p>
<dt><code>-i, &#8211;inchannels </code><i>int</i></p>
<dd> Specify how many channels to capture (default: 2)</p>
<dt><code>-o, &#8211;outchannels </code><i>int</i></p>
<dd> Specify number of playback channels (default: 2)</p>
<dt><code>-C, &#8211;capture </code><i>device_file</i></p>
<dd> Specify input device for capture (default: /dev/dsp)</p>
<dt><code>-P, &#8211;playback </code><i>device_file</i></p>
<dd> Specify output device for playback (default: /dev/dsp)</p>
<dt><code>-b, &#8211;ignorehwbuf </code><i>boolean</i></p>
<dd> Specify, whether to ignore hardware period size (default: false)</dl>
<h3>SUN BACKEND PARAMETERS</h3>
<dl>
<dt><code>-r, &#8211;rate </code><i>int</i></p>
<dd> Specify the sample rate. The default is 48000.</p>
<dt><code>-p, &#8211;period </code><i>int</i></p>
<dd> Specify the number of frames between JACK <code>process()</code> calls. This value must be a power of 2, and the default is 1024. If you need low latency, set <code>-p</code> as low as you can go without seeing xruns. A larger period size yields higher latency, but makes xruns less likely. The JACK capture latency in seconds is <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-n, &#8211;nperiods </code><i>int</i></p>
<dd> Specify the number of periods in the hardware buffer. The default is 2. The period size (<code>-p</code>) times <code>&#8211;nperiods</code> times four (assuming 2 channels 16-bit samples) is the JACK buffer size in bytes. The JACK output latency in seconds is <code>&#8211;nperiods</code> times <code>&#8211;period</code> divided by <code>&#8211;rate</code>.</p>
<dt><code>-w, &#8211;wordlength </code><i>int</i></p>
<dd> Specify the sample size in bits. The default is 16.</p>
<dt><code>-i, &#8211;inchannels </code><i>int</i></p>
<dd> Specify how many channels to capture (default: 2)</p>
<dt><code>-o, &#8211;outchannels </code><i>int</i></p>
<dd> Specify number of playback channels (default: 2)</p>
<dt><code>-C, &#8211;capture </code><i>device_file</i></p>
<dd> Specify input device for capture (default: /dev/audio)</p>
<dt><code>-P, &#8211;playback </code><i>device_file</i></p>
<dd> Specify output device for playback (default: /dev/audio)</p>
<dt><code>-b, &#8211;ignorehwbuf </code><i>boolean</i></p>
<dd> Specify, whether to ignore hardware period size (default: false)</dl>
<h3>PORTAUDIO BACKEND PARAMETERS</h3>
<dl>
<dt><code>-c &#8211;channel</code></p>
<dd> Maximum number of channels (default: all available hardware channels)</p>
<dt><code>-i &#8211;channelin</code></p>
<dd> Maximum number of input channels (default: all available hardware channels)</p>
<dt><code>-o &#8211;channelout</code></p>
<dd> Maximum number of output channels (default: all available hardware channels)</p>
<dt><code>-C &#8211;capture</code></p>
<dd> Whether or not to capture (default: true)</p>
<dt><code>-P &#8211;playback</code></p>
<dd> Whether or not to playback (default: true)</p>
<dt><code>-D &#8211;duplex</code></p>
<dd> Capture and playback (default: true)</p>
<dt><code>-r &#8211;rate</code></p>
<dd> Sample rate (default: 48000)</p>
<dt><code>-p &#8211;period</code></p>
<dd> Frames per period (default: 1024). Must be a power of 2.</p>
<dt><code>-n &#8211;name</code></p>
<dd> Driver name (default: none)</p>
<dt><code>-z &#8211;dither</code></p>
<dd> Dithering mode (default: none)</dl>
<h2>EXAMPLES</h2>
<p> Print usage message for the parameters specific to each backend.</p>
<dl>
<dt>
<dd> <code>jackd -d alsa &#8211;help</code><br />
 <code>jackd -d coreaudio &#8211;help</code><br />
 <code>jackd -d net &#8211;help</code><br />
 <code>jackd -d dummy &#8211;help</code><br />
 <code>jackd -d firewire &#8211;help</code><br />
 <code>jackd -d freebob &#8211;help</code><br />
 <code>jackd -d oss &#8211;help</code><br />
 <code>jackd -d sun &#8211;help</code><br />
 <code>jackd -d portaudio &#8211;help</code></dl>
<p> Run the JACK daemon with realtime priority using the first ALSA hardware card defined in <code>/etc/modules.conf</code>.</p>
<dl>
<dt>
<dd> <code>jackstart &#8211;realtime &#8211;driver=alsa</code></dl>
<p> Run the JACK daemon with low latency giving verbose output, which can be helpful for trouble-shooting system latency problems. A reasonably well-tuned system with a good sound card and a low-latency kernel can handle these values reliably. Some can do better. If you get xrun messages, try a larger buffer. Tuning a system for low latency can be challenging. The JACK FAQ, <i><a rel="nofollow" href="http://jackit.sourceforge.net/docs/faq.php">http://jackit.sourceforge.net/docs/faq.php</a></i> has some useful suggestions.</p>
<dl>
<dt>
<dd> <code>jackstart -Rv -d alsa -p 128 -n 2 -r 44100</code></dl>
<p> Run <code>jackd</code> with realtime priority using the &quot;sblive&quot; ALSA device defined in ~/.asoundrc. Apply shaped dithering to playback audio.</p>
<dl>
<dt>
<dd> <code>jackd -R -d alsa -d sblive &#8211;dither=shaped</code></dl>
<p> Run <code>jackd</code> with no special privileges using the second ALSA hardware card defined in <code>/etc/modules.conf</code>. Any xruns reported by the ALSA backend will be ignored. The larger buffer helps reduce data loss. Rectangular dithering will be used for playback.</p>
<dl>
<dt>
<dd> <code>jackd -d alsa -d hw:1 -p2048 -n3 &#8211;softmode -zr</code></dl>
<p> Run <code>jackd</code> in full-duplex mode using the ALSA hw:0,0 device for playback and the hw:0,2 device for capture.</p>
<dl>
<dt>
<dd> <code>jackd -d alsa -P hw:0,0 -C hw:0,2</code></dl>
<p> Run <code>jackd</code> in playback-only mode using the ALSA hw:0,0 device.</p>
<dl>
<dt>
<dd> <code>jackd -d alsa -P hw:0,0</code></dl>
<h2>ENVIRONMENT</h2>
<p> JACK is evolving a mechanism for automatically starting the server when needed. Any client started without a running JACK server will attempt to start one itself using the command line found in the first line of <code>$HOME/.jackdrc</code> if it exists, or <code>/etc/jackdrc</code> if it does not. If neither file exists, a built-in default command will be used, including the <code>-T</code> flag, which causes the server to shut down when all clients have exited. </p>
<p> As a transition, this only happens when <code>$JACK_START_SERVER</code> is defined in the environment of the calling process. In the future this will become normal behavior. In either case, defining <code>$JACK_NO_START_SERVER</code> disables this feature. </p>
<p> To change where JACK looks for the backend drivers, set <code>$JACK_DRIVER_DIR</code>. </p>
<p> <code>$JACK_DEFAULT_SERVER</code> specifies the default server name. If not defined, the string &quot;default&quot; is used. If set in their respective environments, this affects <code>jackd</code> unless its <code>&#8211;name</code> parameter is set, and all JACK clients unless they pass an explicit name to <code>jack_client_open()</code>. </p>
<h2>SEE ALSO:</h2>
<p> <i><a rel="nofollow" href="http://www.jackaudio.org">http://www.jackaudio.org</a></i><br />
 The official JACK website with news, docs and a list of JACK clients. </p>
<p> <i><a rel="nofollow" href="http://jackaudio.org/email">http://jackaudio.org/email</a></i><br />
 The JACK developers&#8217; mailing list. Subscribe, to take part in development of JACK or JACK clients. User questions are also welcome, there is no user-specific mailing list. </p>
<p> <i><a rel="nofollow" href="http://www.jackosx.com/">http://www.jackosx.com/</a></i><br />
 Tools specific to the Mac OS X version of JACK. </p>
<p> <i><a rel="nofollow" href="http://www.alsa-project.org">http://www.alsa-project.org</a></i><br />
 The Advanced Linux Sound Architecture.</p>
<h2>BUGS</h2>
<p> Please report bugs to<br />
 <i><a rel="nofollow" href="http://trac.jackaudio.org/">http://trac.jackaudio.org/</a></i></p>
<h2>AUTHORS</h2>
<p> Architect and original implementor: Paul Davis </p>
<p> Original design Group: Paul Davis, David Olofson, Kai Vehmanen, Benno Sennoner, Richard Guenther, and other members of the Linux Audio Developers group. </p>
<p> Programming: Paul Davis, Jack O&#8217;Quin, Taybin Rutkin, Stephane Letz, Fernando Pablo Lopez-Lezcano, Steve Harris, Jeremy Hall, Andy Wingo, Kai Vehmanen, Melanie Thielker, Jussi Laako, Tilman Linneweh, Johnny Petrantoni, Torben Hohn. </p>
<p> Manpage written by Stefan Schwandter, Jack O&#8217;Quin and Alexandre Prokoudine. </p>
<h2>Index</h2>
