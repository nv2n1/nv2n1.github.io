---
title: "gt(1)"
name: "gt"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gt/"
description: "gt – version of TiMidity MIDI to WAVE converter and player"
---

<h2>NAME</h2>
<p> gt &#8211; version of TiMidity MIDI to WAVE converter and player </p>
<h2>SYNOPSIS</h2>
<p> <code>gt</code> [-options] [directoryname | filenames &#8230;] [-options] </p>
<h2>DESCRIPTION</h2>
<p> <i>Gt</i>&nbsp;<wbr>is a MIDI to WAVE converter using Gravis Ultrasound-compatible patch files, extended GUS patch files, or AWE-compatible SoundFonts to generate digital audio data from General MIDI files. </p>
<p> The data can be stored in a file for processing, or played in real time through an audio device. <i>Gt</i>&nbsp;<wbr>will generate 6 and 4 channel sound output on systems with capable Alsa drivers and soundcards. Currently, there is only a single output driver, for Alsa. </p>
<p> It&#8217;s not necessary to give any filenames on the command line; if there are midi files in the current directory, <i>gt</i>&nbsp;<wbr>will find them and play them. You can also give a single directory name, and <i>gt</i>&nbsp;<wbr>will look in that directory for midi files. (This automatic construction of play lists will not work for compressed files.) </p>
<p> The default display interface uses the ncurses library to show the notes being played and give other information. The alternatives to this interface are described below under the <code>-i</code>&nbsp;<wbr>option (they are <code>-int</code>&nbsp;<wbr>for ncurses in non-tracing mode, and <code>-id</code>&nbsp;<wbr>or <code>-idt</code>&nbsp;<wbr>for the dumb interface). As songs are playing, a moderate amount of control can be exerted with keys and the mouse (if the mouse works for your display window). Key <code>q</code> or <code>end</code> or <code>F10</code> exits. Key <code>V</code> or <code>up-arrow</code> and <code>v</code> or <code>down-arrow</code> adjust the volume. The space bar pauses playing or resumes playing when paused. Key <code>n</code> or <code>page-down</code> or <code>F9</code> goes to the next midi song. Key <code>p</code> or <code>page-up</code> goes to the previous midi song. Key <code>r</code> or <code>home</code> restarts the current midi song at the beginning. Key <code>f</code> or <code>right-arrow</code> skips forward in the current song. Key <code>b</code> or <code>left-arrow</code> skips backward in the current song. Shifted kays <code>left-arrow</code> and <code>right-arrow</code> adjust the voices ceiling. Kays <code>F2</code>, <code>F3</code>, and <code>F4</code> change the interpolation algorithm. Kays <code>F5</code>, <code>F6</code>, <code>F7</code>, and <code>F8</code> change the patch set. Key <code>F11</code> toggles between wet and dry mode. </p>
<p> Here is what is shown on the ncurses display:</p>
<dl>
<dt><i>line 1</i></p>
<dd> Program title.</p>
<dt><i>line 2</i></p>
<dd> Current patchset, interpolation method, loading mode. A different patchset can be chosen with function keys F5-F8, as indicated on the bottom line of the display. A different interpolation method can be chosen with function keys F2-F4 &#8212; also as indicated on the bottom line of the display. An &quot;[F]&quot; after the interpolation method means that the low pass filter is being used. Loading mode is either fast or full. With fast loading, only the first velocity layer is loaded from extended GUS patches (for ordinary GUS patches, loading mode makes no difference). You can toggle the loading mode with the shifted <code>F</code> key.</p>
<dt><i>line 3</i></p>
<dd> Program status messages and karaoke lyrics or other midi text messages. Fatal error messages are red if your display does color, otherwise they are shown in bold. (And all the colors mentioned below come out in bold face on a non-color display.) Loading progress for patch files required for the next song is shown in cyan. If there is a limit on the amount of memory to use for patches (see the <code>-r</code> option), the loading line displays the proportion of available memory that has been used. (Patches used for previous songs are purged from memory when necessary.) Lyrics and other midi text messages are in yellow.</p>
<dt><i>line 4</i></p>
<dd> Midi file being played or about to be played. Just after the file name, <code>[GM]</code>, <code>[GS]</code>, or <code>[XG]</code> may be shown, which is the synthesizer type, if that was specified in the midi file. After that, as screen space permits, a title, copyright, and author may be shown.</p>
<dt><i>line 5</i></p>
<dd> Elapsed time for the current song and the total time it will take to play it. You can fast forward or rewind with the right or left arrow keys. Key signature, time signature, and tempo are shown in the middle of the line. At the right is the master volume, which will be adjusted by some midi songs, or you can adjust it yourself with the up and down arrow keys. You can use the clipping rate as a guide to how far you want to turn up the volume.</p>
<dt><i>line 7</i></p>
<dd> The <code>Ch</code>&nbsp;<wbr>means midi channel number and is a label for the 16 numbers below it, referring to the 16 midi channels. To the right is a voices bar indicating how many simultaneous notes are being played, i.e., the current polyphony. The very left part of the voices bar is shown with yellow <code>+</code>&nbsp;<wbr>marks and indicates how full the Alsa output buffer is. (If the buffer gets too low, that means <i>gt</i>&nbsp;<wbr>can&#8217;t produce output fast enough, and you may anticipate dropouts.) Sometimes the bar will have a green middle part &#8212; this shows the number of notes that were actually in the music. The blue part of the bar indicates notes added for reverberation, and the magenta part shows notes added for various other effects (chorus, stereo, or tutti).</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> A <code>&lt;</code> mark on the voices bar shows where the voices ceiling has been set. The ceiling is the target maximum polyphony, i.e., number of simultaneously sounding notes, that <i>gt</i>&nbsp;<wbr>tries to remain below. The number can be adjusted up or down with the shifted right and left arrow keys. Higher polyphony gives better sound quality but means more work for the cpu. The default ceiling is 128, and the default absolute maximum is 256.</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> To the right of the voices bar are labels for the columns below. The labels are <code>Bnk</code>&nbsp;<wbr>for midi bank number (&#8216;0&#8217; is not shown; percussion banks are shown below in yellow, XG variation bank numbers in cyan, and the XG sfx bank in magenta), <code>Prg</code>&nbsp;<wbr>for midi program number, <code>Vol</code>&nbsp;<wbr>for the midi volume controller, <code>Exp</code>&nbsp;<wbr>for the expression controller, <code>Pan</code>&nbsp;<wbr>for the left-right panning controller, <code>S</code>&nbsp;<wbr>for the sustain pedal (also shows portamento, sostenuto, legato, and soft pedal), <code>B</code>&nbsp;<wbr>for pitch bend (also shows modulation wheel with <code>*</code>). <code>b</code>&nbsp;<wbr>for brightness, <code>R</code>&nbsp;<wbr>for reverberation, <code>C</code>&nbsp;<wbr>for chorus depth, <code>c</code>&nbsp;<wbr>for celeste effect, and <code>X</code>&nbsp;<wbr>for miscellaneous controllers (some not implemented).</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> Though they are displayed, the legato and soft pedal controllers are not yet implemented. You can click with the mouse on the <code>R</code>, <code>C</code>, or <code>c</code> labels to toggle reverberation, chorus effect, or celeste effect on or off. (For XG songs, celeste effect is actually variation send, and the <code>c</code> column is shown with a <code>V</code> instead.)</p>
<dt><i>lines 9-24</i></p>
<dd> These 16 lines show events on the 16 basic midi channels. <code>Gt</code>&nbsp;<wbr>can play on up to 64 channels, for midi files that have port commands to play on several synthesizers, but there is only room to show the first 16 in full on the display. Notes from higher channels do show up, though, and are shown in cyan. After the number of the midi channel is the name of the patch chosen with the midi program command. The name given here is the name for the patch given in the configuration file, for non-percussion channels. For a percussion channel, it&#8217;s the drumset name. If there is no name, that means there was no program command given, and the default Grand Piano program is being used, or the default drumset 0, for a percussion channel. Or, for a drumset, the absence of any name may be because no name for the drumset was given in the configuration file. Drum kits are shown in yellow, and XG rhythm sfx kits are shown in magenta.</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> In the middle area of the midi channel display the notes are shown. Lower notes are to the left and higher to the right. There isn&#8217;t room to show very high or very low notes, so these are clipped. A digit from 1-9 indicates the note velocity. At the onset of the note, if it&#8217;s playing a stereo patch, it&#8217;s shown in magenta, otherwise it&#8217;s shown in red for a melodic note and yellow for a percussion note. The decay and release phases of a note are shown in green, and the sustain phase in blue.</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> After that is the midi bank number in use on the channel, from 000 to 127, which for percussion channels is shown in yellow. The 000 for melodic bank 0 is left implicit. Numbers in cyan are for XG variation banks. The XG sfx bank is shown as magenta <code>sfx</code> (if your configuration does not supply an sfx bank, but you do have a bank 120, bank 120 is used for the sfx bank). Numbers shown in blue are XG model exclusive or VL patches. After this come the midi program number and current values for some midi controllers.</p>
<dt><i>bottom line</i></p>
<dd> Shown here are labels for the function keys. Function keys <code>F2</code>, <code>F3</code>, and <code>F4</code> are toggles to switch interpolation and filtering mode. The choices are not independent. <code>F3</code> switches between c-spline and Lagrange interpolation methods, but either choice is non-linear (key <code>F2</code>), and choosing Lagrange interpolation switches the low pass filter off (key <code>F4</code>) (because a filter is not yet implemented for Lagrange interpolation).</p>
<dt><i>&nbsp;<wbr></i></p>
<dd> The <code>Help</code> and <code>Mixer</code> keys bring up subwindows. In the <code>Mixer</code> window, you can adjust speaker balance by mouse-clicking to the left or right of the speaker letters. Small letter <code>l</code> and <code>r</code> stand for the left and right rear speakers.</p>
<dt><i>lines 26 on</i></p>
<dd> If there is room in the display window, below the midi channel display, the current play list of midi files is shown. You can select a new song to play by clicking in the list. To the right of the playlist there may be some tracing messages concerning XG effects if verbose mode was requested with <code>-inv</code> or <code>-invv</code>.</dl>
<h2>OPTIONS</h2>
<p> The following command line options are accepted by version 0.1 of <i>gt</i>:</p>
<dl>
<dt><code>-h</code></p>
<dd> Help. This shows a one-page summary of the options being described here. The path name of the current default configuration file is also shown, and, if you have set up alternate patch sets with <code>if</code> statements in your configuration file, the names of these alternate patch sets are also shown (they can be chosen with the command line option <code>-#</code><i>number</i>).</p>
<dt><code>-v</code></p>
<dd> Copyright statement from Tuukko Toivonen.</p>
<dt><code>-o</code><i> filename</i></p>
<dd> Place output on <i>filename</i>. Assumes output mode &#8220;w&#8221; was selected with the <code>-Ow</code> option. The special filename &#8220;-&#8221; causes output to be placed on stdout.</p>
<dt><code>-O</code><i> mode</i></p>
<dd> Selects the output mode from the compiled-in alternatives. <i>mode</i> must begin with one of the supported output mode identifiers. Run <i>gt</i>&nbsp;<wbr>with the <code>-h</code> option to see a list. The following identifier should be available in all versions:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-Ow</code></p>
<dd> Generate RIFF WAVE format output. If output is directed to a non-seekable file, or if <i>gt</i>&nbsp;<wbr>is interrupted before closing the file, the file header will contain 0xFFFFFFFF in the RIFF and data block length fields. The popular sound conversion utility <i>sox</i> is able to read such malformed files, so you can pipe data directly to sox for on-the-fly conversion to other formats.</p>
<dt><code>Format options</code></p>
<dd> Option characters may be added immediately after the mode identifier to change the output format. The following options are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>8</code></p>
<dd> 8-bit sample width</p>
<dt><code>1</code></p>
<dd> 16-bit sample width</p>
<dt><code>l</code></p>
<dd> Linear encoding</p>
<dt><code>U</code></p>
<dd> uLaw (8-bit) encoding</p>
<dt><code>M</code></p>
<dd> Monophonic</p>
<dt><code>S</code></p>
<dd> Stereo</p>
<dt><code>q</code></p>
<dd> Quadraphonic</p>
<dt><code>s</code></p>
<dd> Signed output</p>
<dt><code>u</code></p>
<dd> Unsigned output</p>
<dt><code>x</code></p>
<dd> Byte-swapped output</dl>
</dl>
</dl>
<p> Note that some options have no effect on some modes. For example, you cannot generate a byte-swapped RIFF WAVE file, or force uLaw output on a Linux PCM device.</dl>
</dl>
<dl>
<dt><code>-s</code><i> frequency</i></p>
<dd> Sets the resampling frequency. Not all sound devices are capable of all frequencies &#8212; an approximate frequency may be selected, depending on the implementation.</p>
<dt><code>-a</code></p>
<dd> Turns on antialiasing. Samples are run through a lowpass filter before playing, which reduces aliasing noise at low resampling frequencies. (With the sampling rate set to the standard 44,100 samples per second, there&#8217;s no point to using this.)</p>
<dt><code>-k number</code></p>
<dd> Select interpolation algorithm for resampling: 0 for linear interpolation, 1 for cspline interpolation, 2 for LaGrange interpolation, 3 for cspline with filter.</p>
<dt><code>-b number</code></p>
<dd> Substitute bank <i>number</i> instruments for bank 0 instruments, provided that the substitute instruments exist. I use this for auditioning new patches. The <i>number</i> argument is the raw index, which will reference sfx, vl, or mu100 banks if the number is greater than 127.</p>
<dt><code>-r number</code></p>
<dd> Set maximum of ram in megabytes to use up keeping patches from previously played midi files. This should presumably be less than your total ram plus disk cache size. The default is 60 megabytes. It probably doesn&#8217;t matter unless you&#8217;re using big sf2 soundfont patchsets.</p>
<dt><code>-F</code></p>
<dd> Toggles fast loading mode. With fast loading, only the first velocity layer is loaded in extended GUS patches. It&#8217;s lots faster &#8212; quality suffers.</p>
<dt><code>-f</code></p>
<dd> Toggles fast envelopes. Some MIDI files sound better when notes decay slower &#8212; it gives the impression of reverb, which <i>gt</i>&nbsp;<wbr>doesn&#8217;t currently fully support.</p>
<dt><code>-d</code></p>
<dd> Sets &quot;dry&quot; mode. After notes are released, their decay is governed by the patch data rather than the volume envelope. This is economical of polyphony, but for some instruments, typically vibraphone, ocarina, and mandolin, notes may be terminated too suddenly. Non-dry, or &quot;wet&quot; mode is the default.</p>
<dt><code>-S</code><i> separation</i></p>
<dd> Tunes surround sound separation. Lower values give more separation. For 5.1 surround, the default is 64. For 4.0 surround, the default is 95.</p>
<dt><code>-p</code><i> voices</i></p>
<dd> Sets polyphony (maximum number of simultaneous voices) to <i>voices</i>.</p>
<dt><code>-A</code><i> amplification</i></p>
<dd> Multiplies the master volume by <i>amplification</i>%.</p>
<dt><code>-X</code><i> curve</i></p>
<dd> With the value 0, the midi expression controller affects the volume linearly. With 1 (the default) or 2, it affects volume exponentially. Values 3, 4, or 5 use tables specific to GM, GS, and XG.</p>
<dt><code>-V</code><i> curve</i></p>
<dd> With the value 0, the midi volume controller affects the volume linearly. With 1 (the default) or 2, it affects volume exponentially. Values 3, 4, or 5 use tables specific to GM, GS, and XG.</p>
<dt><code>-C</code><i> ratio</i></p>
<dd> Sets the ratio of sampling and control frequencies. This determines how often envelopes are recalculated &#8212; small ratios yield better quality but use more CPU time.</p>
<dt><code>-#</code><i> number</i></p>
<dd> Selects patchset when the configuration file has been set up appropriately. See the FILES section below under <code>if</code> and <code>else</code> for how to do this.</p>
<dt><code>-L</code><i> directory</i></p>
<dd> Adds <i>directory</i> to the library path. Patch, configuration, and MIDI files are searched along this path. Directories added last will be searched first. Note that the current directory is always searched first before the library path.</p>
<dt><code>-c</code><i> file</i></p>
<dd> Reads an extra configuration file.</p>
<dt><code>-I</code><i> number</i></p>
<dd> Uses the program <i>number</i> as the default instrument. Any Program Change events in MIDI files will override this option.</p>
<dt><code>-D</code><i> channel</i></p>
<dd> Marks <i>channel</i> as a drum channel. If <i>channel</i> is negative, channel &#8211;<i>channel</i> is marked as an instrumental channel. If <i>channel</i> is 0, all channels are marked as instrumental. (Sysex dumps in GS or XG midi files may mark channels as drums and will override this flag.)</p>
<dt><code>-Q</code><i> channel</i></p>
<dd> Causes <i>channel</i> to be quiet. If <i>channel</i> is negative, channel &#8211;<i>channel</i> is turned back on. If <i>channel</i> is 0, all channels are turned on.</p>
<dt><code>-U</code></p>
<dd> Instructs <i>gt</i>&nbsp;<wbr>to unload all instruments from memory between MIDI files. This can reduce memory requirements when playing many files in succession.</p>
<dt><code>-i</code><i> interface</i></p>
<dd> Selects the user interface from the compiled-in alternatives. <i>interface</i> must begin with one of the supported interface identifiers. Run <i>gt</i>&nbsp;<wbr>with the <code>-h</code> option to see a list. The following identifiers may be available:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-id</code></p>
<dd> The dumb interface &#8212; plays files in sequence, prints messages according to verbosity level. The trace mode shows the current and total playing time.</p>
<dt><code>-in</code></p>
<dd> The ncurses full-screen interface with interactive controls.</p>
<dt><code>Interface options</code></p>
<dd> Option characters may be added immediately after the interface identifier. The following options are recognized:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>v</code></p>
<dd> Increases verbosity. This option is cumulative.</p>
<dt><code>q</code></p>
<dd> Decreases verbosity. This option is cumulative.</p>
<dt><code>t</code></p>
<dd> Toggles trace mode. Trace mode is the default for the ncurses interface, so <code>t</code> turns it off. Trace mode is not very useful for the dumb interface. The ncurses display in trace mode displays events in midi time. That is, midi events, like note onsets, are displayed approximately at the time you hear them, though <i>gt</i> is working a second or so ahead in the song, calculating data to send to the output driver. So midi time is a little behind real time. However, the status of midi controllers is shown in real time, so in the display, the controllers will change slightly before you can hear their effects.</dl>
</dl>
</dl>
</dl>
</dl>
<dl>
<dt>
<dt><code>-B</code><i> fragments</i></p>
<dd>
<dd> For the Linux sound driver, selects the number of buffer fragments. Increasing the number of fragments may reduce choppiness when many processes are running. Specify a <i>fragments</i> of 0 to use the maximum number of fragments available. The maximum number available is the default, and it&#8217;s probably not useful to change that.</dl>
<h2>FILES</h2>
<p> <i>gt</i>&nbsp;<wbr>looks for the configuration file <i>timidity.cfg</i> at startup, before processing any options. If it can&#8217;t be accessed, and the library path is changed with a <code>-L</code> option on the command line, then the default file will be sought again along the new library path after processing all options, unless another configuration file was specified with the <code>-c</code> option. </p>
<p> Configuration files define the mapping of MIDI programs to instrument files. Multiple files may be specified, but statements in later ones will not override earlier ones. The following statements can be used in a configuration file:</p>
<dl>
<dt><code>-p</code><i> voices</i></p>
<dd> Sets polyphony (maximum number of simultaneous voices) to <i>voices</i>.</p>
<dt><code>-A</code><i> amplification</i></p>
<dd> Multiplies the master volume by <i>amplification</i>%.</p>
<dt><code>-X</code><i> curve</i></p>
<dd> With the value 0, the midi expression controller affects the volume linearly. With 1 (the default) or 2, it affects volume exponentially.</p>
<dt><code>-V</code><i> curve</i></p>
<dd> With the value 0, the midi volume controller affects the volume linearly. With 1 (the default) or 2, it affects volume exponentially.</p>
<dt><code>-C</code><i> ratio</i></p>
<dd> Sets the ratio of sampling and control frequencies. This determines how often envelopes are recalculated &#8212; small ratios yield better quality but use more CPU time.</p>
<dt><code>-s</code><i> frequency</i></p>
<dd> Sets the resampling frequency. Not all sound devices are capable of all frequencies &#8212; an approximate frequency may be selected, depending on the implementation.</p>
<dt><code>-k number</code></p>
<dd> Select interpolation algorithm for resampling: 0 for linear interpolation, 1 for cspline interpolation, 2 for LaGrange interpolation, 3 for cspline interpolation with low-pass filtering.</p>
<dt><code>-r number</code></p>
<dd> Set maximum of ram in megabytes to use up keeping patches from previously played midi files. This should presumably be less than your total ram plus disk cache size. The default is 60 megabytes. It probably doesn&#8217;t matter unless you&#8217;re using big sf2 soundfont patchsets.</p>
<dt><code>-O</code><i> mode</i></p>
<dd> Same as corresponding commandline option.</p>
<dt><code>dir</code><i> directory</i></p>
<dd> Adds <i>directory</i> to the search path in the same manner as the <code>-L</code> command line option.</p>
<dt><code>source</code><i> file</i></p>
<dd> Reads another configuration file, then continues processing the current one.</p>
<dt><code>soundfont</code><i> file</i></p>
<dd> Loads a soundfont. Unlike the following <i>sf2</i> command, this offers no way to modify banks or presets inside the soundfont. But it&#8217;s easy to use.</p>
<dt><code>sf2</code><i> file [option]</i></p>
<dd> Reads the parameters and waveforms in an AWE-compatible SoundFont file. Both &quot;.sbk&quot; and &quot;.sf2&quot; SoundFonts can be used. Preceding patch mappings must list all patches that are to be loaded from the file, and the preceding <code>bank</code>/<code>drumset</code> keywords must be followed by <code>sf2</code> or <code>sbk</code> (which are equivalent). The options allowed are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>banknumber</i></p>
<dd> The bank number given in the first preceding &quot;bank&quot;/&quot;drumset&quot; statement is to be used in place of the bank <i>banknumber</i> given in the SoundFont itself.</dl>
</dl>
<dt><code>if</code><i> number</i></p>
<dd> This makes the next <i>source</i> or <i>soundfont</i> command in the configure file conditional on the number being the same as a number supplied to <i>gt</i> as the patchset number, with, e.g., the &quot;-#n&quot; command line option. Also, if this appears in the main config file <code>timidity.cfg</code>, the name given with the following conditional command becomes the name of the patchset.</p>
<dt><code>bank</code><i> number [option] [[#N ]name]</i></p>
<dd> Selects the tone bank to modify. Patch mappings that follow will affect this tone bank. The options allowed are <code>sf2</code> and <code>sbk</code>, which were described above. The optional name is for the sake of the display interface, so the bank can be shown with a meaningful name instead of just a number. The name assigned can be preceded by &quot;#N &quot;, for compatibility with Timidity++, which otherwise complains about the extra name argument.</p>
<dt><code>drumset</code><i> number [option] [[#N ]name]</i></p>
<dd> Selects the drum set to modify. Patch mappings that follow will affect this drum set. The options allowed are <code>sf2</code> and <code>sbk</code>, which were described above. As for the bank statement described above, the name is for display.</p>
<dt><code>sfx</code></p>
<dd> Selects the XG non-rhythm SFX bank to modify. Patch mappings that follow will affect this tone bank.</p>
<dt><code>bankxg</code><i>number</i></p>
<dd> Selects XG banks 1-16. These have to be kept separate from the banks 1-16 used for GM/GS midis, because they don&#8217;t have the same types of instruments.</p>
<dt><code>drumsfx</code><i>number</i></p>
<dd> Selects any of the 128 XG rhythm SFX banks (numbered 0-127) to modify. Patch mappings that follow will affect these drum banks. (Older XG midis use only 0 and 1 banks, but now there are also banks 16 (Techno Kit K/S), 17 (Techno Kit Hi), 18 (Techno Kit Lo), 32 (Sakura Kit), and 33 (Small Latin Kit).</p>
<dt><code>mu100</code><i>number</i></p>
<dd> Selects an XG MU100 model specific bank, where <i>number</i> is a multiple of 8.</p>
<dt><code>vl</code><i>number</i></p>
<dd> Selects an XG VL bank, where <i>number</i> is 0 or 1. (This is not for the VL-XG banks 112-119, which are treated as ordinary banks.)</p>
<dt><i>number file [options]</i></p>
<dd> Specifies that the the MIDI program <i>number</i> in the current tone bank or drum set should be played using the patch <i>file</i>. <i>options</i> may be any of the following:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>amp=</code><i>amplification</i></p>
<dd> Amplifies the instrument&#8217;s volume by <i>amplification</i> percent.</p>
<dt><code>note=</code><i>note</i></p>
<dd> Specifies a fixed MIDI note to use when playing the instrument. If <i>note</i> is 0, the instrument will be played at whatever note the Note On event triggering it has. For percussion instruments, if no value is specified in the configuration file, the default in the patch file will be used.</p>
<dt><code>tuning=</code><i>cents</i></p>
<dd> Changes the pitch of the instrument. <i>cents</i> is a signed quantity in units of 1/100th of a semitone, so, e.g., specify &quot;+1200&quot; to go up an octave. The number must begin with a &quot;+&quot; or a &quot;-&quot;. (Not yet implemented for soundfonts.)</p>
<dt><code>pan=</code><i>panning</i></p>
<dd> Sets the instrument&#8217;s default panning. <i>panning</i> may be <code>left</code>, <code>right</code>, <code>center</code>, or an integer between -100 and 100, designating full left and full right respectively. If no value is specified, the default in the patch file will be used. Note that panning controls in MIDI files will override this value.</p>
<dt><code>cutoff=</code><i>Hz</i></p>
<dd> Sets the initial cutoff frequency for the low pass filter used in filter interpolation.</p>
<dt><code>keep=</code>{<code>loop</code>|<code>env</code>|<code>sustain</code>}</p>
<dd> Strangely shaped envelopes are removed automatically from melodic instruments in GUS patches. <code>keep</code> can be used to prevent stripping envelope or loop data. (Stripping envelopes was originally the default for <i>timidity</i>, but in this version it&#8217;s not, except for GUS percussion patches. So these options are seldom useful.)</p>
<dt><code>strip=</code>{<code>loop</code>|<code>env</code>|<code>tail</code>|<code>sustain</code>}</p>
<dd> Force removal of loop or envelope information from all patches in the instrument, or strip the tail, i.e. all data after the loop. Some third-party instruments have garbage after the loop, as evidenced by a clicking noise whenever the instrument is played, so adding the <code>strip=tail</code> option will markedly improve sound quality. The <code>strip=sustain</code> option prevents notes from being held until released.</dl>
</dl>
</dl>
<p> <code>NOTE:</code> Whenever any filename ends in one of the compiled-in compression identifiers, such as <i>.gz</i>, or <i>.sht</i>, <i>gt</i> will pipe the file through the appropriate decompressor. MIDI files often compress very well, so the ability to handle compressed files can be useful. </p>
<p> The special filename &#8220;-&#8221; can be used on the command line to indicate that a MIDI file should be read from stdin. </p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 1995 Tuukka Toivonen.<br />
 See AUTHORS below for additional copyrights. </p>
<p> gt/TiMidity is free software; you can redistribute it and/or modify it under the terms of the <i>GNU General Public License</i> as published by the Free Software Foundation; either version 2 of the License, or (at your option) any later version. </p>
<p> TiMidity is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the <i>GNU General Public License</i> for more details.</p>
<h2>AVAILABILITY</h2>
<p> The latest release of the original version is available on the TiMidity Home Page, URL <i><a rel="nofollow" href="http://www.clinet.fi/~toivonen/timidity/">http://www.clinet.fi/~toivonen/timidity/</a></i>. (But the original version is no longer being maintained &#8212; see URL <i><a rel="nofollow" href="http://http://www.cgs.fi/~tt/discontinued.html">http://http://www.cgs.fi/~tt/discontinued.html</a></i>.) The present modified version is available at URL <i><a href="ftp://ling.lll.hawaii.edu/pub/greg/gt-0.3.tar.gz">ftp://ling.lll.hawaii.edu/pub/greg/gt-0.3.tar.gz</a></i>.</p>
<h2>BUGS</h2>
<p> 8-bit and low-rate output sounds worse than it should. </p>
<p> Eats more CPU time than a small CPU-time-eating animal.</p>
<h2>AUTHORS</h2>
<p> Tuukka Toivonen &lt;toivonen [at] clinet.fi&gt;<br />
 Surround sound, reading extended GUS patches implemented by Greg Lee.<br />
 HP-UX audio code, X-Motif interface, icons and antialiasing filter by Vincent Pagel &lt;pagel [at] loria.fr&gt;<br />
 Tcl/Tk interface and AWE SoundFont support by Takashi Iwai &lt;iwai [at] dragon.mm.t.u-tokyo.ac.jp&gt;<br />
 Windows 95/NT audio code by Davide Moretti &lt;dmoretti [at] iper.net&gt;<br />
 DEC audio code by Chi Ming HUNG &lt;cmhung [at] insti.physics.sunysb.edu&gt;<br />
 S-Lang user interface by Riccardo Facchetti &lt;riccardo [at] cdc8g5.cdc.polimi.it&gt;<br />
 IW patchset support, karaoke, AWE/XG enhancements, much reworking of the code by Greg Lee &lt;lee [at] hawaii.edu&gt;, &lt;greg [at] ling.lll.hawaii.edu&gt;<br />
 KDE user interface &quot;KMidi&quot; Copyright (C) 1997 Bernd Johannes Wuebben &lt;wuebben [at] math.cornell.edu&gt;<br />
 Effects filter by Nicolas Witczak &lt;witczak [at] geocities.fr&gt;, see URL <i><a rel="nofollow" href="http://www.geocities.com/SiliconValley/Lab/6307/">http://www.geocities.com/SiliconValley/Lab/6307/</a></i>).<br />
 Portamento, mod wheel, and other enhancements from TiMidity++ Copyright (C) 1999 Masanao Izumo &lt;mo [at] goice.co.jp&gt;. See URL <i><a rel="nofollow" href="http://www.goice.co.jp/member/mo/hack-progs/timidity.html">http://www.goice.co.jp/member/mo/hack-progs/timidity.html</a></i>.<br />
 alsa driver Copyright (C) 1999 Masanao Izumo &lt;mo [at] goice.co.jp&gt;<br />
 bsd20 driver Written by Yamate Keiichiro &lt;keiich-y [at] is.aist-nara.ac.jp&gt;<br />
 esd driver by Avatar &lt;avatar [at] deva.net&gt;<br />
 hpux_d driver Copyright 1997 Lawrence T. Hoff<br />
 nas driver Copyright (C) 1999 Michael Haardt &lt;michael [at] moria.de&gt;<br />
 XAW Interface from Tomokazu Harada &lt;harada [at] prince.pe.u-tokyo.ac.jp&gt; and Yoshishige Arai &lt;ryo2 [at] on.rim.or.jp&gt;<br />
 GTK+ interface by Glenn Trigg 29 Oct 1998<br />
 The autoconf script is (C)Copyright 1998 by Hiroshi Takekawa &lt;t80679 [at] hongo.ecc.u-tokyo.ac.jp&gt;, modified for automake by Isaku Yamahata &lt;yamahata [at] kusm.kyoto-u.ac.jp&gt;, modified for automake by Masanao Izumo &lt;mo [at] goice.co.jp&gt; (1998.11).<br />
 The m4 autoconf definitions: Configure paths for ESD by Manish Singh 98-9-30, stolen back from Frank Belew, stolen from Manish Singh, Shamelessly stolen from Owen Taylor.<br />
 Configure Paths for Alsa by Christopher Lansdown (lansdoct [at] cs.alfred.edu), 29/10/1998, modified for TiMidity++ by Isaku Yamahata(yamahata [at] kusm.kyoto-u.ac.jp), 16/12/1998. </p>
<h2>Index</h2>
