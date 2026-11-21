---

title: "fluidsynth(1)"
name: "fluidsynth"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fluidsynth/"
description: "FluidSynth – a SoundFont synthesizer"
---

<p> FluidSynth &#8211; a SoundFont synthesizer </p>
<h2>SYNOPSIS</h2>
<p> <code>fluidsynth</code> [<i>options</i>] [ SoundFonts ] [ midifiles ]</p>
<h2>DESCRIPTION</h2>
<p> <code>FluidSynth</code> is a real-time MIDI synthesizer based on the SoundFont(R) 2 specifications. It can be used to render MIDI input or MIDI files to audio. The MIDI events are read from a MIDI device. The sound is rendered in real-time to the sound output device. </p>
<p> The easiest way to start the synthesizer is to give it a SoundFont on the command line: &#8216;fluidsynth soundfont.sf2&#8217;. fluidsynth will load the SoundFont and read MIDI events from the default MIDI device using the default MIDI driver. Once FluidSynth is running, it reads commands from the stdin. There are commands to send MIDI events manually, to load or unload SoundFonts, and so forth. All the available commands are discussed below. </p>
<p> FluidSynth can also be used to play a list of MIDI files. Simply run FluidSynth with the SoundFont and the list of MIDI files to play. In this case you might not want to open the MIDI device to read external events. Use the -n option to deactivate MIDI input. If you also want to deactivate the use of the shell, start FluidSynth with the -i option: &#8216;fluidsynth -ni soundfont.sf2 midifile1.mid midifile2.mid&#8217;. </p>
<p> Run fluidsynth with the &#8211;help option to check for changes in the list of options.</p>
<h2>OPTIONS</h2>
<p> <code>fluidsynth</code> accepts the following options: </p>
<dl>
<dt><code>-a, &#8211;audio-driver=[label]</code></dt>
<dd> The audio driver to use. &quot;-a help&quot; to list valid options</dd>
<dt><code>-c, &#8211;audio-bufcount=[count]</code></dt>
<dd> Number of audio buffers</dd>
<dt><code>-C, &#8211;chorus</code></dt>
<dd> Turn the chorus on or off [0|1|yes|no, default = on]</dd>
<dt><code>-d, &#8211;dump</code></dt>
<dd> Dump incoming and outgoing MIDI events to stdout</dd>
<dt><code>-E, &#8211;audio-file-endian</code></dt>
<dd> Audio file endian for fast rendering or aufile driver (&quot;-E help&quot; for list)</dd>
<dt><code>-f, &#8211;load-config</code></dt>
<dd> Load command configuration file (shell commands)</dd>
<dt><code>-F, &#8211;fast-render=[file]</code></dt>
<dd> Render MIDI file to raw audio data and store in [file]</dd>
<dt><code>-g, &#8211;gain</code></dt>
<dd> Set the master gain [0 &lt; gain &lt; 10, default = 0.2]</dd>
<dt><code>-G, &#8211;audio-groups</code></dt>
<dd> Defines the number of LADSPA audio nodes</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Print out this help summary</dd>
<dt><code>-i, &#8211;no-shell</code></dt>
<dd> Don&#8217;t read commands from the shell [default = yes]</dd>
<dt><code>-j, &#8211;connect-jack-outputs</code></dt>
<dd> Attempt to connect the jack outputs to the physical ports</dd>
<dt><code>-K, &#8211;midi-channels=[num]</code></dt>
<dd> The number of midi channels [default = 16]</dd>
<dt><code>-l, &#8211;disable-lash</code></dt>
<dd> Don&#8217;t connect to LASH server</dd>
<dt><code>-L, &#8211;audio-channels=[num]</code></dt>
<dd> The number of stereo audio channels [default = 1]</dd>
<dt><code>-m, &#8211;midi-driver=[label]</code></dt>
<dd> The name of the midi driver to use. &quot;-m help&quot; to list valid options.</dd>
<dt><code>-n, &#8211;no-midi-in</code></dt>
<dd> Don&#8217;t create a midi driver to read MIDI input events [default = yes]</dd>
<dt><code>-o</code></dt>
<dd> Define a setting, -o name=value (&quot;-o help&quot; to dump current values)</dd>
<dt><code>-O, &#8211;audio-file-format</code></dt>
<dd> Audio file format for fast rendering or aufile driver (&quot;-O help&quot; for list)</dd>
<dt><code>-p, &#8211;portname=[label] </code></dt>
<dd> Set MIDI port name (alsa_seq, coremidi drivers)</dd>
<dt><code>-r, &#8211;sample-rate</code></dt>
<dd> Set the sample rate</dd>
<dt><code>-R, &#8211;reverb</code></dt>
<dd> Turn the reverb on or off [0|1|yes|no, default = on]</dd>
<dt><code>-s, &#8211;server</code></dt>
<dd> Start FluidSynth as a server process</dd>
<dt><code>-T, &#8211;audio-file-type</code></dt>
<dd> Audio file type for fast rendering or aufile driver (&quot;T help&quot; for list)</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Print out verbose messages about midi events</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Show version of program</dd>
<dt><code>-z, &#8211;audio-bufsize=[size]</code></dt>
<dd> Size of each audio buffer </dd>
</dl>
<h2>SETTINGS</h2>
<p> All settings are non-realtime (have no effect if set after startup), except for those indicated as realtime. </p>
<dl>
<dt><code>SYNTHESIZER</code></dt>
<dd>
</dd><dt><code>synth.audio-channels INT [min=1, max=128, def=1]</code></dt>
<dd> Number of audio channels (DOCME!).</dd>
<dt><code>synth.audio-groups INT [min=1, max=128, def=1]</code></dt>
<dd> Number of audio groups (DOCME!).</dd>
<dt><code>synth.chorus.active BOOL [def=True]</code></dt>
<dd> Chorus effect enable toggle.</dd>
<dt><code>synth.cpu-cores INT [min=1, max=256, def=1]</code></dt>
<dd> Number of CPU cores to use for multi-core support.</dd>
<dt><code>synth.device-id INT [min=0, max=126, def=0] REALTIME</code></dt>
<dd> Device ID to use for accepting incoming SYSEX messages.</dd>
<dt><code>synth.dump BOOL [def=False]</code></dt>
<dd> No effect currently.</dd>
<dt><code>synth.effects-channels INT [min=2, max=2, def=2]</code></dt>
<dd> No effect currently.</dd>
<dt><code>synth.gain FLOAT [min=0.000, max=10.000, def=0.200] REALTIME</code></dt>
<dd> Master synthesizer gain.</dd>
<dt><code>synth.ladspa.active BOOL [def=False]</code></dt>
<dd> LADSPA subsystem enable toggle.</dd>
<dt><code>synth.midi-channels INT [min=16, max=256, def=16]</code></dt>
<dd> Total MIDI channel count (must be multiple of 16).</dd>
<dt><code>synth.midi-bank-select STR [def=&#8217;gs&#8217; vals:&#8217;gm&#8217;, &#8216;gs&#8217;, &#8216;xg&#8217;, &#8216;mma&#8217;]</code></dt>
<dd> MIDI Bank Select message style.</dd>
<dt><code>synth.min-note-length INT [min=0, max=65535, def=10]</code></dt>
<dd> Minimum duration for note events (work around for very short percussion notes).</dd>
<dt><code>synth.overflow.age FLOAT [min=-10000, max=10000, def=1000]</code></dt>
<dd> Weigthing (on overflow) for a voice&#8217;s duration.</dd>
<dt><code>synth.overflow.percussion FLOAT [min=-10000, max=10000, def=4000]</code></dt>
<dd> Weighting (on overflow) for a voice being on the drum channel.</dd>
<dt><code>synth.overflow.released FLOAT [min=-10000, max=10000, def=-2000]</code></dt>
<dd> Weighting (on overflow) for a voice that has been released, i e note off and no sustain pedal.</dd>
<dt><code>synth.overflow.sustained FLOAT [min=-10000, max=10000, def=-1000]</code></dt>
<dd> Weighting (on overflow) for a voice that has been sustained, i e note off, but sustain pedal held down.</dd>
<dt><code>synth.overflow.volume FLOAT [min=-10000, max=10000, def=500]</code></dt>
<dd> Weighting (on overflow) for a voice&#8217;s volume.</dd>
<dt><code>synth.parallel-render BOOL [def=True]</code></dt>
<dd> Enables low-latency audio rendering response, even if synth is otherwise busy. Should always to be true for usage by fluidsynth executable.</dd>
<dt><code>synth.polyphony INT [min=1, max=65535, def=256] REALTIME</code></dt>
<dd> Voice polyphony count (number of simultaneous voices allowed).</dd>
<dt><code>synth.reverb.active BOOL [def=True]</code></dt>
<dd> Reverb effect enable toggle.</dd>
<dt><code>synth.sample-rate FLOAT [min=22050.000, max=96000.000, def=44100.000] </code></dt>
<dd> Synthesizer sample rate.</dd>
<dt><code>synth.threadsafe-api BOOL [def=True]</code></dt>
<dd> Serializes access to the synth API. Must always to be true for usage by fluidsynth executable.</dd>
<dt><code>synth.verbose BOOL [def=False]</code></dt>
<dd> Print received MIDI events to stdout. </dd>
<dt><code>GENERAL AUDIO</code></dt>
<dd>
</dd><dt><code>audio.driver STR</code></dt>
<dd> Audio driver to use. Default and valid options depend on available drivers.</dd>
<dt><code>audio.input-channels INT [min=0, max=2, def=0]</code></dt>
<dd> Not used currently? (DOCME).</dd>
<dt><code>audio.output-channels INT [min=2, max=32, def=2]</code></dt>
<dd> DOCME</dd>
<dt><code>audio.period-size INT [min=64, max=8192, def=64]</code></dt>
<dd> Period size for audio buffers. Used by many audio drivers.</dd>
<dt><code>audio.periods INT [min=2, max=64, def=16]</code></dt>
<dd> Count of audio buffers. Used by many audio drivers.</dd>
<dt><code>audio.realtime-prio INT [min=0, max=99, def=60]</code></dt>
<dd> Realtime priority to assign to audio thread or 0 to disable high priority scheduling. Only used by some audio drivers (currently &#8216;alsa&#8217; and &#8216;oss&#8217;).</dd>
<dt><code>audio.sample-format STR [def=&#8217;16bits&#8217; vals:&#8217;16bits&#8217;,&#8217;float&#8217;]</code></dt>
<dd> Audio output format, to select format for those drivers which support 16 bit or floating point. </dd>
<dt><code>AUDIO DRIVER SPECIFIC</code></dt>
<dd>
</dd><dt><code>audio.alsa.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> ALSA audio driver output device.</dd>
<dt><code>audio.coreaudio.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> CoreAudio driver output device. Valid options depend on system.</dd>
<dt><code>audio.dart.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> OS/2 Dart audio driver device.</dd>
<dt><code>audio.dsound.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> Device to use for DirectSound driver. Valid options depend on system.</dd>
<dt><code>audio.file.endian STR [def=&#8217;auto&#8217; vals:&#8217;auto&#8217;,&#8217;big&#8217;,&#8217;cpu&#8217;,&#8217;little&#8217;]</code></dt>
<dd> File renderer or file driver byte order selection. &#8216;auto&#8217; selects the default for the selected file type. &#8216;cpu&#8217; uses the CPU byte order. Limited to &#8216;cpu&#8217; if no libsndfile support.</dd>
<dt><code>audio.file.format STR [def=&#8217;s16&#8242; vals:&#8217;double&#8217;,&#8217;float&#8217;,&#8217;s16&#8242;,&#8217;s24&#8242;,&#8217;s32&#8242;,&#8217;s8&#8242;,&#8217;u8&#8242;]</code></dt>
<dd> File renderer or file driver audio format. Limited to &#8216;s16&#8217; if no libsndfile support.</dd>
<dt><code>audio.file.name STR [def=&#8217;fluidsynth.wav&#8217;]</code></dt>
<dd> Output file name for file renderer or file driver.</dd>
<dt><code>audio.file.type STR [def=&#8217;auto&#8217; vals:&#8217;aiff&#8217;,&#8217;au&#8217;,&#8217;auto&#8217;,&#8217;flac&#8217;,&#8217;oga&#8217;,&#8217;raw&#8217;,&#8217;wav&#8217;]</code></dt>
<dd> Output file type for file renderer or file driver. &#8216;auto&#8217; attempts to determine type from file extension in audio.file.name. Limited to &#8216;raw&#8217; if no libsndfile support. Actual options will vary depending on libsndfile library.</dd>
<dt><code>audio.jack.autoconnect BOOL [def=False]</code></dt>
<dd> If enabled, then FluidSynth is automatically connected to Jack system audio output ports.</dd>
<dt><code>audio.jack.id STR [def=&#8217;fluidsynth&#8217;]</code></dt>
<dd> Client ID to use when connecting to Jack.</dd>
<dt><code>audio.jack.multi BOOL [def=False]</code></dt>
<dd> TRUE to enable multi-channel output.</dd>
<dt><code>audio.jack.server STR [def=&#8221;]</code></dt>
<dd> Jack server name. Blank for default.</dd>
<dt><code>audio.oss.device STR [def=&#8217;/dev/dsp&#8217;]</code></dt>
<dd> OSS driver output device.</dd>
<dt><code>audio.portaudio.device STR [def=&#8217;PortAudio Default&#8217;]</code></dt>
<dd> PortAudio driver output device. Available options depends on system.</dd>
<dt><code>audio.pulseaudio.adjust-latency BOOL [def=True]</code></dt>
<dd> Increases the latency dynamically if PulseAudio suggests so.</dd>
<dt><code>audio.pulseaudio.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> PulseAudio driver output device.</dd>
<dt><code>audio.pulseaudio.media-role STR [def=&#8217;music&#8217;]</code></dt>
<dd> PulseAudio media role information.</dd>
<dt><code>audio.pulseaudio.server STR [def=&#8217;default&#8217;]</code></dt>
<dd> PulseAudio driver server. </dd>
<dt><code>GENERAL MIDI</code></dt>
<dd>
</dd><dt><code>midi.driver STR</code></dt>
<dd> MIDI driver to use. Default and valid options depend on available drivers.</dd>
<dt><code>midi.realtime-prio INT [min=0, max=99, def=50]</code></dt>
<dd> Realtime priority to assign to MIDI thread or 0 to disable high priority scheduling. Only used by some MIDI drivers (currently &#8216;alsa_seq&#8217;, &#8216;alsa_raw&#8217; and &#8216;oss&#8217;). </dd>
<dt><code>MIDI DRIVER SPECIFIC</code></dt>
<dd>
</dd><dt><code>midi.alsa.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> ALSA raw MIDI driver device.</dd>
<dt><code>midi.alsa_seq.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> ALSA sequencer MIDI driver device.</dd>
<dt><code>midi.alsa_seq.id STR [def=&#8217;pid&#8217;]</code></dt>
<dd> ALSA sequencer client ID. &#8216;pid&#8217; will use process ID as part of the client name.</dd>
<dt><code>midi.coremidi.id STR [def=&#8217;pid&#8217;]</code></dt>
<dd> Client ID to use for CoreMIDI driver. &#8216;pid&#8217; will use process ID as port of the client name.</dd>
<dt><code>midi.jack.id STR [def=&#8217;fluidsynth-midi&#8217;]</code></dt>
<dd> Jack MIDI driver client ID.</dd>
<dt><code>midi.jack.server STR [def=&#8221;]</code></dt>
<dd> Jack MIDI driver server. Blank to use default.</dd>
<dt><code>midi.oss.device STR [def=&#8217;/dev/midi&#8217;]</code></dt>
<dd> OSS MIDI driver device.</dd>
<dt><code>midi.portname STR [def=&#8221;]</code></dt>
<dd> Port name used for CoreAudio and ALSA sequencer drivers.</dd>
<dt><code>midi.winmidi.device STR [def=&#8217;default&#8217;]</code></dt>
<dd> Device for Windows MIDI driver. </dd>
<dt><code>MISCELLANEOUS</code></dt>
<dd>
</dd><dt><code>player.reset-synth BOOL [def=True]</code></dt>
<dd> TRUE to reset synthesizer MIDI state between MIDI songs.</dd>
<dt><code>player.timing-source STR [def=&#8217;sample&#8217; vals:&#8217;sample&#8217;,&#8217;system&#8217;]</code></dt>
<dd> Selects timing source for MIDI sequencer. &#8216;system&#8217; uses the system timer. &#8216;sample&#8217; uses the sample clock (amount of audio output, events synchronized with audio).</dd>
<dt><code>shell.port INT [min=1, max=65535, def=9800]</code></dt>
<dd> Shell command server TCP/IP port number to use.</dd>
<dt><code>shell.prompt STR [def=&#8221;]</code></dt>
<dd> Shell prompt string. </dd>
</dl>
<h2>SHELL COMMANDS</h2>
<dl>
<dt><code>GENERAL</code></dt>
<dd>
</dd><dt><code>help</code></dt>
<dd> Prints out list of help topics (type &quot;help &lt;topic&gt;&quot;)</dd>
<dt><code>quit</code></dt>
<dd> Quit the synthesizer</dd>
<dt><code>SOUNDFONTS</code></dt>
<dd>
</dd><dt><code>load filename</code></dt>
<dd> Load a SoundFont</dd>
<dt><code>unload number</code></dt>
<dd> Unload a SoundFont. The number is the index of the SoundFont on the stack.</dd>
<dt><code>fonts</code></dt>
<dd> Lists the current SoundFonts on the stack</dd>
<dt><code>inst number</code></dt>
<dd> Print out the available instruments for the SoundFont.</dd>
<dt><code>MIDI MESSAGES</code></dt>
<dd>
</dd><dt><code>noteon channel key velocity </code></dt>
<dd> Send a note-on event</dd>
<dt><code>noteoff channel key</code></dt>
<dd> Send a note-off event</dd>
<dt><code>cc channel ctrl value</code></dt>
<dd> Send a control change event</dd>
<dt><code>prog chan num</code></dt>
<dd> Send program-change message</dd>
<dt><code>select chan sfont bank prog</code></dt>
<dd> Combination of bank-select and program-change</dd>
<dt><code>channels</code></dt>
<dd> Print out the presets of all channels.</dd>
<dt><code>AUDIO SYNTHESIS</code></dt>
<dd>
</dd><dt><code>gain value</code></dt>
<dd> Set the master gain (0 &lt; gain &lt; 5)</dd>
<dt><code>interp num</code></dt>
<dd> Choose interpolation method for all channels</dd>
<dt><code>interpc chan num</code></dt>
<dd> Choose interpolation method for one channel</dd>
<dt><code>REVERB</code></dt>
<dd>
</dd><dt><code>reverb [0|1|on|off]</code></dt>
<dd> Turn the reverb on or off</dd>
<dt><code>rev_preset num</code></dt>
<dd> Load preset num into the reverb unit</dd>
<dt><code>rev_setroomsize num</code></dt>
<dd> Change reverb room size</dd>
<dt><code>rev_setdamp num</code></dt>
<dd> Change reverb damping</dd>
<dt><code>rev_setwidth num</code></dt>
<dd> Change reverb width</dd>
<dt><code>rev_setlevel num</code></dt>
<dd> Change reverb level</dd>
<dt><code>CHORUS</code></dt>
<dd>
</dd><dt><code>chorus [0|1|on|off]</code></dt>
<dd> Turn the chorus on or off</dd>
<dt><code>cho_set_nr n</code></dt>
<dd> Use n delay lines (default 3)</dd>
<dt><code>cho_set_level num</code></dt>
<dd> Set output level of each chorus line to num</dd>
<dt><code>cho_set_speed num</code></dt>
<dd> Set mod speed of chorus to num (Hz)</dd>
<dt><code>cho_set_depth num</code></dt>
<dd> Set chorus modulation depth to num (ms)</dd>
<dt><code>MIDI ROUTER</code></dt>
<dd>
</dd><dt><code>router_default</code></dt>
<dd> Reloads the default MIDI routing rules (input channels are mapped 1:1 to the synth)</dd>
<dt><code>router_clear</code></dt>
<dd> Deletes all MIDI routing rules.</dd>
<dt><code>router_begin [note|cc|prog|pbend|cpress|kpress]</code></dt>
<dd> Starts a new routing rule for events of the given type</dd>
<dt><code>router_chan min max mul add</code></dt>
<dd> Limits the rule for events on min &lt;= chan &lt;= max. If the channel falls into the window, it is multiplied by &#8216;mul&#8217;, then &#8216;add&#8217; is added.</dd>
<dt><code>router_par1 min max mul add</code></dt>
<dd> Limits parameter 1 (for example note number in a note events). Similar to router_chan.</dd>
<dt><code>router_par2 min max mul add</code></dt>
<dd> Limits parameter 2 (for example velocity in a note event). Similar to router_chan</dd>
<dt><code>router_end</code></dt>
<dd> Finishes the current rule and adds it to the router.</dd>
<dt><code>Router examples</code></dt>
<dd>
</dd><dt>router_clear</dt>
<dd>
</dd><dt>router_begin note</dt>
<dd>
</dd><dt>router_chan 0 7 0 15</dt>
<dd>
</dd><dt>router_end</dt>
<dd>
</dd><dt>Will accept only note events from the lower 8 MIDI</dt>
<dd> channels. Regardless of the channel, the synthesizer plays the note on ch 15 (synthchannel=midichannel*0+15)</dd>
<dt>router_begin cc</dt>
<dd>
</dd><dt>router_chan 0 7 0 15</dt>
<dd>
</dd><dt>router_par1 1 1 0 64</dt>
<dd>
</dd><dt>router_add</dt>
<dd> Configures the modulation wheel to act as sustain pedal (transforms CC 1 to CC 64 on the lower 8 MIDI channels, routes to ch 15) </dd>
</dl>
<h2>AUTHORS</h2>
<p> Peter Hanappe &lt;hanappe [at] fluid-synth.org&gt;<br />
 Markus Nentwig &lt;nentwig [at] users.sourceforge.net&gt;<br />
 Antoine Schmitt &lt;as [at] gratin.org&gt;<br />
 Josh Green &lt;jgreen [at] users.sourceforge.net&gt;<br />
 Stephane Letz &lt;letz [at] grame.fr&gt; </p>
<p> Please check the AUTHORS and THANKS files for all credits</p>
<h2>DISCLAIMER</h2>
<p> SoundFont(R) is a registered trademark of E-mu Systems, Inc. </p>
