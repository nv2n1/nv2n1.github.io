---

title: "jamin(1)"
name: "jamin"
section: "1"
letter: "j"
url: "/docs/linux/man/1-jamin/"
description: "jamin – JACK Audio Mastering interface"
---

<p> jamin &#8211; JACK Audio Mastering interface </p>
<h2>SYNOPSIS</h2>
<p> <code>jamin</code> [<i> options </i>] [<i> inport1 inport2</i> [<i> outport1 outport2</i> ]] </p>
<p> <code>jamin-scene</code> <i>&lt;scene-num&gt;</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>jamin</code> command invokes JAMin, the JACK Audio Mastering interface which is based on the JACK Audio Connection Kit, &lt;<code><a rel="nofollow" href="http://jackit.sourceforge.net">http://jackit.sourceforge.net</a></code>&gt;. </p>
<p> JAMin is designed for professional stereo audio mastering. It provides of a number of tools: a 1024-band hand-drawn EQ with parametric controls, a 31-band graphic EQ, 3-band compressor, 3-band stereo width control, lookahead limiter, boost, and other features. </p>
<p> For the latest JAMin information, see &lt;<code><a rel="nofollow" href="http://jamin.sourceforge.net">http://jamin.sourceforge.net</a></code>&gt;. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code> <i>filename</i></dt>
<dd>
 Load session file <i>filename</i> on startup. If no session file is specified, JAMin loads &quot;~/.jamin/default.jam&quot; if that exists, or else uses some system-provided default settings.</dd>
<dt><code>-h</code></dt>
<dd>
 Print a brief usage message describing the main <code>jamin</code> options, including some developer options not intended for normal users.</dd>
<dt><code>-j</code> <i>servername</i></dt>
<dd>
 Connect to JACK server <i>servername</i>. Otherwise, use the default server.</dd>
<dt><code>-n</code> <i>clientname</i></dt>
<dd>
 Set JACK <i>clientname</i> used to identify input and output ports. Otherwise, use &quot;jamin&quot;.</dd>
<dt><code>-s</code> <i>frequency</i></dt>
<dd>
 Set the spectrum update frequency (per second). The range is 1 to 10 with 10 as the default. Set to 0 to disable spectrum update.</dd>
<dt><code>-c</code> <i>time</i></dt>
<dd>
 Set the crossfade time in seconds. The range is 0.0 to 2.0 with 1.0 as the default. WARNING: fast crossfade times in combination with large jack buffer sizes may introduce zipper noise to some signals (especially sustained sounds in the bass range).</dd>
<dt><code>-p</code></dt>
<dd>
 Don&#8217;t automatically connect any JACK output ports. </dd>
<p> Without this option, JAMin will connect to <i>outport1</i> and <i>outport2</i> if they were explicitly listed on the command line. If not, it connects to the first two physical output ports with the string &quot;:playback&quot; in their names.</p>
<dt><code>-i</code></dt>
<dd>
 Use IIR type crossover instead of the default FFT type crossover. The IIR crossover is less CPU intensive but the FFT crossover will give better results (YMMV).</dd>
<dt><code>-l</code></dt>
<dd>
 Set to 0 to use Steve Harris&#8217; fast-lookahead-limiter or 1 for Sampo Savolainen&#8217;s foo-limiter. At this time there is a problem with the foo-limiter if you push the input too hard.</dd>
<dt><code>-r</code></dt>
<dd>
 Load GTK resource information from an example JAMin resource file. If the <code>-r</code> option is not specified, look for a user-defined resource file in <code>~/.jamin/jamin_ui</code>. Otherwise, use the system-wide GTK settings.</dd>
<dt><code>-v</code></dt>
<dd>
 Print verbose output. Use <code>-vv</code> or <code>-vvv</code> for more detail.</dd>
<dt><code>-V</code></dt>
<dd> Print version and copyright information, then quit. </dd>
</dl>
<h2>FILES</h2>
<dl>
<dt><code>~/.jamin</code></dt>
<dd> Directory containing per-user JAMin data. Created automatically if it does not already exist.</dd>
<dt><code>~/.jamin/jamin_ui</code></dt>
<dd> Default resource file for GTK user interface customization, used when the <code>-r</code> command option is not specified. JAMin provides a default resource file in ${prefix}/share/jamin/examples/jamin_ui. To customize that file, copy it to ~/.jamin/jamin_ui and make changes.</dd>
<dt><code>~/.jamin/*.jam</code></dt>
<dd> Normal location for user-defined session files. They can be stored elsewhere, if desired.</dd>
<dt><code>~/.jamin/default.jam</code></dt>
<dd> If this session file exists, it is loaded by default on startup, except when overridden by the <code>-f</code> option. </dd>
</dl>
<h2>IPC</h2>
<p> If JAMin has been built with OSC support enabled it responds to UDP OSC messages on port 4444. </p>
<p> Messages to /jamin/scene with a numerical argument cause the scene number to change. A commaind line tool (<code>jamin-scene</code>) and LADSPA Plugin (<code>jamin_cont</code>, ID:1912) are provided for remote scene changes. </p>
<h2>EXAMPLES</h2>
<p> Since <code>jamin</code> is not a standalone program we generally need other programs to provide input audio and receive the mastered output. This example uses <code>alsaplayer</code> with output going to the first two ALSA playback ports: </p>
<dl>
<dt>
</dt><dd> <code>jackd -R -d alsa -p 2048 -r 44100 &amp;</code><br/>
 <code>alsaplayer -o jack -s src -d noconnect song.wav &amp;</code><br/>
 <code>jamin src:out_1 src:out_2</code> </dd>
</dl>
<p> That was the brute force method. It is much easier to have <code>qjackctl</code> start the JACK server and handle its connections. After the server is running, start <code>jackplayer</code> and <code>jamin</code>. The &quot;transport&quot; option tells <code>jackplayer</code> (an <code>alsaplayer</code> alias) to start and stop under JACK transport control. </p>
<dl>
<dt>
</dt><dd> <code>qjackctl &amp;</code><br/>
 <code>jackplayer -d noconnect/transport song.wav &amp;</code><br/>
 <code>jamin</code></dd></dl>
<p> Any JACK-aware player such as <code>rezound</code>, <code>ecasound</code> or <code>ecamegapedal</code> can be used, instead. </p>
<p> A more advanced technique uses <code>ardour</code> for both the source and destination. In <code>ardour</code>, run all of your track outputs into a stereo bus, connect its output ports to JAMin, then run the JAMin outputs back into a record-enabled stereo track. This allows mixing and mastering at the same time. If JAMin is already running when <code>ardour</code> reopens the session, it will automatically reconnect all these ports. </p>
<dl>
<dt>
</dt><dd> <code>qjackctl &amp;</code><br/>
 <code>jamin &amp;</code><br/>
 <code>ardour</code> </dd>
</dl>
<h2>SEE ALSO:</h2>
<p> <code>&lt;<a rel="nofollow" href="http://jamin.sourceforge.net">http://jamin.sourceforge.net</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://www.alsa-project.org">http://www.alsa-project.org</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://jackaudio.org">http://jackaudio.org</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://qjackctl.sourceforge.net">http://qjackctl.sourceforge.net</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://www.suse.de/~mana/jack.html">http://www.suse.de/~mana/jack.html</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://alsaplayer.sourceforge.net">http://alsaplayer.sourceforge.net</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://www.ardour.org">http://www.ardour.org</a></code>&gt;<br/>
 <code>&lt;<a rel="nofollow" href="http://rezound.sourceforge.net">http://rezound.sourceforge.net</a></code>&gt;<br/>
 <code><a href="/docs/linux/man/1-jackd/">jackd</a>(1)</code><br/>
 <code>alsaplayer(1)</code><br/>
 <code><a href="/docs/linux/man/1-ardour/">ardour</a>(1)</code></p>
<h2>BUGS</h2>
<p> Please send bug reports to &lt;<code>jamin-devel [at] lists.sourceforge.net</code>&gt;.</p>
<h2>AUTHORS</h2>
<p> Steve Harris is the principal JAMin author and team leader. Other developers include: Jan Depner, Jack O&#8217;Quin, Ron Parker, Emmanuel Saracco, and Patrick Shirkey. Alexandre Prokoudine and Yuri N. Sedunov developed the translation infrastructure. Alexandre also translated JAMin into Russian and is our (really good) web engineer. </p>
