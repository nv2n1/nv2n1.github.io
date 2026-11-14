---
title: "fluidsynth(1)"
name: "fluidsynth"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fluidsynth/"
description: "FluidSynth – a SoundFont synthesizer"
---

<h2 class="name">NAME</h2>
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
<dt><code>-a, &#8211;audio-driver=[label]</code></p>
<dd> The audio driver to use. &quot;-a help&quot; to list valid options</p>
<dt><code>-c, &#8211;audio-bufcount=[count]</code></p>
<dd> Number of audio buffers</p>
<dt><code>-C, &#8211;chorus</code></p>
<dd> Turn the chorus on or off [0|1|yes|no, default = on]</p>
<dt><code>-d, &#8211;dump</code></p>
<dd> Dump incoming and outgoing MIDI events to stdout</p>
<dt><code>-E, &#8211;audio-file-endian</code></p>
<dd> Audio file endian for fast rendering or aufile driver (&quot;-E help&quot; for list)</p>
<dt><code>-f, &#8211;load-config</code></p>
<dd> Load command configuration file (shell commands)</p>
<dt><code>-F, &#8211;fast-render=[file]</code></p>
<dd> Render MIDI file to raw audio data and store in [file]</p>
<dt><code>-g, &#8211;gain</code></p>
<dd> Set the master gain [0 &lt; gain &lt; 10, default = 0.2]</p>
<dt><code>-G, &#8211;audio-groups</code></p>
<dd> Defines the number of LADSPA audio nodes</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Print out this help summary</p>
<dt><code>-i, &#8211;no-shell</code></p>
<dd> Don&#8217;t read commands from the shell [default = yes]</p>
<dt><code>-j, &#8211;connect-jack-outputs</code></p>
<dd> Attempt to connect the jack outputs to the physical ports</p>
<dt><code>-K, &#8211;midi-channels=[num]</code></p>
<dd> The number of midi channels [default = 16]</p>
<dt><code>-l, &#8211;disable-lash</code></p>
<dd> Don&#8217;t connect to LASH server</p>
<dt><code>-L, &#8211;audio-channels=[num]</code></p>
<dd> The number of stereo audio channels [default = 1]</p>
<dt><code>-m, &#8211;midi-driver=[label]</code></p>
<dd> The name of the midi driver to use. &quot;-m help&quot; to list valid options.</p>
<dt><code>-n, &#8211;no-midi-in</code></p>
<dd> Don&#8217;t create a midi driver to read MIDI input events [default = yes]</p>
<dt><code>-o</code></p>
<dd> Define a setting, -o name=value (&quot;-o help&quot; to dump current values)</p>
<dt><code>-O, &#8211;audio-file-format</code></p>
<dd> Audio file format for fast rendering or aufile driver (&quot;-O help&quot; for list)</p>
<dt><code>-p, &#8211;portname=[label] </code></p>
<dd> Set MIDI port name (alsa_seq, coremidi drivers)</p>
<dt><code>-r, &#8211;sample-rate</code></p>
<dd> Set the sample rate</p>
<dt><code>-R, &#8211;reverb</code></p>
<dd> Turn the reverb on or off [0|1|yes|no, default = on]</p>
<dt><code>-s, &#8211;server</code></p>
<dd> Start FluidSynth as a server process</p>
<dt><code>-T, &#8211;audio-file-type</code></p>
<dd> Audio file type for fast rendering or aufile driver (&quot;T help&quot; for list)</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Print out verbose messages about midi events</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program</p>
<dt><code>-z, &#8211;audio-bufsize=[size]</code></p>
<dd> Size of each audio buffer </p>
</dl>
<h2>SETTINGS</h2>
<p> All settings are non-realtime (have no effect if set after startup), except for those indicated as realtime. </p>
<dl>
<dt><code>SYNTHESIZER</code></p>
<dd>
<dt><code>synth.audio-channels INT [min=1, max=128, def=1]</code></p>
<dd> Number of audio channels (DOCME!).</p>
<dt><code>synth.audio-groups INT [min=1, max=128, def=1]</code></p>
<dd> Number of audio groups (DOCME!).</p>
<dt><code>synth.chorus.active BOOL [def=True]</code></p>
<dd> Chorus effect enable toggle.</p>
<dt><code>synth.cpu-cores INT [min=1, max=256, def=1]</code></p>
<dd> Number of CPU cores to use for multi-core support.</p>
<dt><code>synth.device-id INT [min=0, max=126, def=0] REALTIME</code></p>
<dd> Device ID to use for accepting incoming SYSEX messages.</p>
<dt><code>synth.dump BOOL [def=False]</code></p>
<dd> No effect currently.</p>
<dt><code>synth.effects-channels INT [min=2, max=2, def=2]</code></p>
<dd> No effect currently.</p>
<dt><code>synth.gain FLOAT [min=0.000, max=10.000, def=0.200] REALTIME</code></p>
<dd> Master synthesizer gain.</p>
<dt><code>synth.ladspa.active BOOL [def=False]</code></p>
<dd> LADSPA subsystem enable toggle.</p>
<dt><code>synth.midi-channels INT [min=16, max=256, def=16]</code></p>
<dd> Total MIDI channel count (must be multiple of 16).</p>
<dt><code>synth.midi-bank-select STR [def=&#8217;gs&#8217; vals:&#8217;gm&#8217;, &#8216;gs&#8217;, &#8216;xg&#8217;, &#8216;mma&#8217;]</code></p>
<dd> MIDI Bank Select message style.</p>
<dt><code>synth.min-note-length INT [min=0, max=65535, def=10]</code></p>
<dd> Minimum duration for note events (work around for very short percussion notes).</p>
<dt><code>synth.overflow.age FLOAT [min=-10000, max=10000, def=1000]</code></p>
<dd> Weigthing (on overflow) for a voice&#8217;s duration.</p>
<dt><code>synth.overflow.percussion FLOAT [min=-10000, max=10000, def=4000]</code></p>
<dd> Weighting (on overflow) for a voice being on the drum channel.</p>
<dt><code>synth.overflow.released FLOAT [min=-10000, max=10000, def=-2000]</code></p>
<dd> Weighting (on overflow) for a voice that has been released, i e note off and no sustain pedal.</p>
<dt><code>synth.overflow.sustained FLOAT [min=-10000, max=10000, def=-1000]</code></p>
<dd> Weighting (on overflow) for a voice that has been sustained, i e note off, but sustain pedal held down.</p>
<dt><code>synth.overflow.volume FLOAT [min=-10000, max=10000, def=500]</code></p>
<dd> Weighting (on overflow) for a voice&#8217;s volume.</p>
<dt><code>synth.parallel-render BOOL [def=True]</code></p>
<dd> Enables low-latency audio rendering response, even if synth is otherwise busy. Should always to be true for usage by fluidsynth executable.</p>
<dt><code>synth.polyphony INT [min=1, max=65535, def=256] REALTIME</code></p>
<dd> Voice polyphony count (number of simultaneous voices allowed).</p>
<dt><code>synth.reverb.active BOOL [def=True]</code></p>
<dd> Reverb effect enable toggle.</p>
<dt><code>synth.sample-rate FLOAT [min=22050.000, max=96000.000, def=44100.000] </code></p>
<dd> Synthesizer sample rate.</p>
<dt><code>synth.threadsafe-api BOOL [def=True]</code></p>
<dd> Serializes access to the synth API. Must always to be true for usage by fluidsynth executable.</p>
<dt><code>synth.verbose BOOL [def=False]</code></p>
<dd> Print received MIDI events to stdout. </p>
<dt><code>GENERAL AUDIO</code></p>
<dd>
<dt><code>audio.driver STR</code></p>
<dd> Audio driver to use. Default and valid options depend on available drivers.</p>
<dt><code>audio.input-channels INT [min=0, max=2, def=0]</code></p>
<dd> Not used currently? (DOCME).</p>
<dt><code>audio.output-channels INT [min=2, max=32, def=2]</code></p>
<dd> DOCME</p>
<dt><code>audio.period-size INT [min=64, max=8192, def=64]</code></p>
<dd> Period size for audio buffers. Used by many audio drivers.</p>
<dt><code>audio.periods INT [min=2, max=64, def=16]</code></p>
<dd> Count of audio buffers. Used by many audio drivers.</p>
<dt><code>audio.realtime-prio INT [min=0, max=99, def=60]</code></p>
<dd> Realtime priority to assign to audio thread or 0 to disable high priority scheduling. Only used by some audio drivers (currently &#8216;alsa&#8217; and &#8216;oss&#8217;).</p>
<dt><code>audio.sample-format STR [def=&#8217;16bits&#8217; vals:&#8217;16bits&#8217;,&#8217;float&#8217;]</code></p>
<dd> Audio output format, to select format for those drivers which support 16 bit or floating point. </p>
<dt><code>AUDIO DRIVER SPECIFIC</code></p>
<dd>
<dt><code>audio.alsa.device STR [def=&#8217;default&#8217;]</code></p>
<dd> ALSA audio driver output device.</p>
<dt><code>audio.coreaudio.device STR [def=&#8217;default&#8217;]</code></p>
<dd> CoreAudio driver output device. Valid options depend on system.</p>
<dt><code>audio.dart.device STR [def=&#8217;default&#8217;]</code></p>
<dd> OS/2 Dart audio driver device.</p>
<dt><code>audio.dsound.device STR [def=&#8217;default&#8217;]</code></p>
<dd> Device to use for DirectSound driver. Valid options depend on system.</p>
<dt><code>audio.file.endian STR [def=&#8217;auto&#8217; vals:&#8217;auto&#8217;,&#8217;big&#8217;,&#8217;cpu&#8217;,&#8217;little&#8217;]</code></p>
<dd> File renderer or file driver byte order selection. &#8216;auto&#8217; selects the default for the selected file type. &#8216;cpu&#8217; uses the CPU byte order. Limited to &#8216;cpu&#8217; if no libsndfile support.</p>
<dt><code>audio.file.format STR [def=&#8217;s16&#8242; vals:&#8217;double&#8217;,&#8217;float&#8217;,&#8217;s16&#8242;,&#8217;s24&#8242;,&#8217;s32&#8242;,&#8217;s8&#8242;,&#8217;u8&#8242;]</code></p>
<dd> File renderer or file driver audio format. Limited to &#8216;s16&#8217; if no libsndfile support.</p>
<dt><code>audio.file.name STR [def=&#8217;fluidsynth.wav&#8217;]</code></p>
<dd> Output file name for file renderer or file driver.</p>
<dt><code>audio.file.type STR [def=&#8217;auto&#8217; vals:&#8217;aiff&#8217;,&#8217;au&#8217;,&#8217;auto&#8217;,&#8217;flac&#8217;,&#8217;oga&#8217;,&#8217;raw&#8217;,&#8217;wav&#8217;]</code></p>
<dd> Output file type for file renderer or file driver. &#8216;auto&#8217; attempts to determine type from file extension in audio.file.name. Limited to &#8216;raw&#8217; if no libsndfile support. Actual options will vary depending on libsndfile library.</p>
<dt><code>audio.jack.autoconnect BOOL [def=False]</code></p>
<dd> If enabled, then FluidSynth is automatically connected to Jack system audio output ports.</p>
<dt><code>audio.jack.id STR [def=&#8217;fluidsynth&#8217;]</code></p>
<dd> Client ID to use when connecting to Jack.</p>
<dt><code>audio.jack.multi BOOL [def=False]</code></p>
<dd> TRUE to enable multi-channel output.</p>
<dt><code>audio.jack.server STR [def=&#8221;]</code></p>
<dd> Jack server name. Blank for default.</p>
<dt><code>audio.oss.device STR [def=&#8217;/dev/dsp&#8217;]</code></p>
<dd> OSS driver output device.</p>
<dt><code>audio.portaudio.device STR [def=&#8217;PortAudio Default&#8217;]</code></p>
<dd> PortAudio driver output device. Available options depends on system.</p>
<dt><code>audio.pulseaudio.adjust-latency BOOL [def=True]</code></p>
<dd> Increases the latency dynamically if PulseAudio suggests so.</p>
<dt><code>audio.pulseaudio.device STR [def=&#8217;default&#8217;]</code></p>
<dd> PulseAudio driver output device.</p>
<dt><code>audio.pulseaudio.media-role STR [def=&#8217;music&#8217;]</code></p>
<dd> PulseAudio media role information.</p>
<dt><code>audio.pulseaudio.server STR [def=&#8217;default&#8217;]</code></p>
<dd> PulseAudio driver server. </p>
<dt><code>GENERAL MIDI</code></p>
<dd>
<dt><code>midi.driver STR</code></p>
<dd> MIDI driver to use. Default and valid options depend on available drivers.</p>
<dt><code>midi.realtime-prio INT [min=0, max=99, def=50]</code></p>
<dd> Realtime priority to assign to MIDI thread or 0 to disable high priority scheduling. Only used by some MIDI drivers (currently &#8216;alsa_seq&#8217;, &#8216;alsa_raw&#8217; and &#8216;oss&#8217;). </p>
<dt><code>MIDI DRIVER SPECIFIC</code></p>
<dd>
<dt><code>midi.alsa.device STR [def=&#8217;default&#8217;]</code></p>
<dd> ALSA raw MIDI driver device.</p>
<dt><code>midi.alsa_seq.device STR [def=&#8217;default&#8217;]</code></p>
<dd> ALSA sequencer MIDI driver device.</p>
<dt><code>midi.alsa_seq.id STR [def=&#8217;pid&#8217;]</code></p>
<dd> ALSA sequencer client ID. &#8216;pid&#8217; will use process ID as part of the client name.</p>
<dt><code>midi.coremidi.id STR [def=&#8217;pid&#8217;]</code></p>
<dd> Client ID to use for CoreMIDI driver. &#8216;pid&#8217; will use process ID as port of the client name.</p>
<dt><code>midi.jack.id STR [def=&#8217;fluidsynth-midi&#8217;]</code></p>
<dd> Jack MIDI driver client ID.</p>
<dt><code>midi.jack.server STR [def=&#8221;]</code></p>
<dd> Jack MIDI driver server. Blank to use default.</p>
<dt><code>midi.oss.device STR [def=&#8217;/dev/midi&#8217;]</code></p>
<dd> OSS MIDI driver device.</p>
<dt><code>midi.portname STR [def=&#8221;]</code></p>
<dd> Port name used for CoreAudio and ALSA sequencer drivers.</p>
<dt><code>midi.winmidi.device STR [def=&#8217;default&#8217;]</code></p>
<dd> Device for Windows MIDI driver. </p>
<dt><code>MISCELLANEOUS</code></p>
<dd>
<dt><code>player.reset-synth BOOL [def=True]</code></p>
<dd> TRUE to reset synthesizer MIDI state between MIDI songs.</p>
<dt><code>player.timing-source STR [def=&#8217;sample&#8217; vals:&#8217;sample&#8217;,&#8217;system&#8217;]</code></p>
<dd> Selects timing source for MIDI sequencer. &#8216;system&#8217; uses the system timer. &#8216;sample&#8217; uses the sample clock (amount of audio output, events synchronized with audio).</p>
<dt><code>shell.port INT [min=1, max=65535, def=9800]</code></p>
<dd> Shell command server TCP/IP port number to use.</p>
<dt><code>shell.prompt STR [def=&#8221;]</code></p>
<dd> Shell prompt string. </p>
</dl>
<h2>SHELL COMMANDS</h2>
<dl>
<dt><code>GENERAL</code></p>
<dd>
<dt><code>help</code></p>
<dd> Prints out list of help topics (type &quot;help &lt;topic&gt;&quot;)</p>
<dt><code>quit</code></p>
<dd> Quit the synthesizer</p>
<dt><code>SOUNDFONTS</code></p>
<dd>
<dt><code>load filename</code></p>
<dd> Load a SoundFont</p>
<dt><code>unload number</code></p>
<dd> Unload a SoundFont. The number is the index of the SoundFont on the stack.</p>
<dt><code>fonts</code></p>
<dd> Lists the current SoundFonts on the stack</p>
<dt><code>inst number</code></p>
<dd> Print out the available instruments for the SoundFont.</p>
<dt><code>MIDI MESSAGES</code></p>
<dd>
<dt><code>noteon channel key velocity </code></p>
<dd> Send a note-on event</p>
<dt><code>noteoff channel key</code></p>
<dd> Send a note-off event</p>
<dt><code>cc channel ctrl value</code></p>
<dd> Send a control change event</p>
<dt><code>prog chan num</code></p>
<dd> Send program-change message</p>
<dt><code>select chan sfont bank prog</code></p>
<dd> Combination of bank-select and program-change</p>
<dt><code>channels</code></p>
<dd> Print out the presets of all channels.</p>
<dt><code>AUDIO SYNTHESIS</code></p>
<dd>
<dt><code>gain value</code></p>
<dd> Set the master gain (0 &lt; gain &lt; 5)</p>
<dt><code>interp num</code></p>
<dd> Choose interpolation method for all channels</p>
<dt><code>interpc chan num</code></p>
<dd> Choose interpolation method for one channel</p>
<dt><code>REVERB</code></p>
<dd>
<dt><code>reverb [0|1|on|off]</code></p>
<dd> Turn the reverb on or off</p>
<dt><code>rev_preset num</code></p>
<dd> Load preset num into the reverb unit</p>
<dt><code>rev_setroomsize num</code></p>
<dd> Change reverb room size</p>
<dt><code>rev_setdamp num</code></p>
<dd> Change reverb damping</p>
<dt><code>rev_setwidth num</code></p>
<dd> Change reverb width</p>
<dt><code>rev_setlevel num</code></p>
<dd> Change reverb level</p>
<dt><code>CHORUS</code></p>
<dd>
<dt><code>chorus [0|1|on|off]</code></p>
<dd> Turn the chorus on or off</p>
<dt><code>cho_set_nr n</code></p>
<dd> Use n delay lines (default 3)</p>
<dt><code>cho_set_level num</code></p>
<dd> Set output level of each chorus line to num</p>
<dt><code>cho_set_speed num</code></p>
<dd> Set mod speed of chorus to num (Hz)</p>
<dt><code>cho_set_depth num</code></p>
<dd> Set chorus modulation depth to num (ms)</p>
<dt><code>MIDI ROUTER</code></p>
<dd>
<dt><code>router_default</code></p>
<dd> Reloads the default MIDI routing rules (input channels are mapped 1:1 to the synth)</p>
<dt><code>router_clear</code></p>
<dd> Deletes all MIDI routing rules.</p>
<dt><code>router_begin [note|cc|prog|pbend|cpress|kpress]</code></p>
<dd> Starts a new routing rule for events of the given type</p>
<dt><code>router_chan min max mul add</code></p>
<dd> Limits the rule for events on min &lt;= chan &lt;= max. If the channel falls into the window, it is multiplied by &#8216;mul&#8217;, then &#8216;add&#8217; is added.</p>
<dt><code>router_par1 min max mul add</code></p>
<dd> Limits parameter 1 (for example note number in a note events). Similar to router_chan.</p>
<dt><code>router_par2 min max mul add</code></p>
<dd> Limits parameter 2 (for example velocity in a note event). Similar to router_chan</p>
<dt><code>router_end</code></p>
<dd> Finishes the current rule and adds it to the router.</p>
<dt><code>Router examples</code></p>
<dd>
<dt>router_clear</p>
<dd>
<dt>router_begin note</p>
<dd>
<dt>router_chan 0 7 0 15</p>
<dd>
<dt>router_end</p>
<dd>
<dt>Will accept only note events from the lower 8 MIDI</p>
<dd> channels. Regardless of the channel, the synthesizer plays the note on ch 15 (synthchannel=midichannel*0+15)</p>
<dt>router_begin cc</p>
<dd>
<dt>router_chan 0 7 0 15</p>
<dd>
<dt>router_par1 1 1 0 64</p>
<dd>
<dt>router_add</p>
<dd> Configures the modulation wheel to act as sustain pedal (transforms CC 1 to CC 64 on the lower 8 MIDI channels, routes to ch 15) </p>
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
<h2>Index</h2>
