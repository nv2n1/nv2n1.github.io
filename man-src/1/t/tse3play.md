---

title: "tse3play(1)"
name: "tse3play"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tse3play/"
description: "tse3play – play/convert music files (MIDI or TSE3MDL) using the TSE3 sequencer engine library"
---

<p> tse3play &#8211; play/convert music files (MIDI or TSE3MDL) using the TSE3 sequencer engine library</p>
<h2>SYNOPSIS</h2>
<p> <code>tse3play [-h] [-ver] [-v] [-list] [-nv] [-np] [-l] [-omidi</code> <i>output-midi-file</i> <code>] [-omidi0] [-omidicomp] [-otse3mdl</code> <i>output-tse3mdl-file</i> <code>] [-map</code> <i>from-midi-channel to-midi-channel</i> <code>] [-m] [-r] [-gmr] [-gsr] [-xgr] [-unix] [-oss] [-alsa] [-arts] [-stream] [-s</code> <i>start-time</i> <code>] [-solo</code> <i>track</i> <code>] [-sl</code> <i>usecs</i> <code>] [ -stop ] [ -e ] [ -mute</code> <i>channel</i> <code>] [ -pd</code> <i>dir</i> <code>]</code> <i>file</i> <code>] [ -port</code> <i>port</i> <code>] [ -fast ]</code></p>
<h2>DESCRIPTION</h2>
<p> <code>tse3play</code> plays TSE3MDL files and MIDI files using the TSE3 sequencer engine. It was originally developed as a test application for the TSE3 engine, but is now a fully featured playback application. </p>
<p> <code>tse3play</code> can also convert files between the two supported formats. Whilst playing it provides text based visual feedback, or can stream an English representation of the contents of the file to standard output. </p>
<p> <i>MIDI files</i> are a standard file format for the storage of musical (song) data that can be found in abundance on the internet. They don&#8217;t contain the actual sounds played, but instructions on how to recreate the song (i.e. start note/stop note commands). MIDI files are most often created by a <i>sequencer</i> application (akin to a word processor for music). MIDI files often have the extension .mid or .midi </p>
<p> <i>TSE3MDL</i> ( <i>TSE3 Music Description Langauge</i> ) files are a similar form of music file. They are created by sequencer applications based on the TSE3 sequencer engine library. The file format contains a great deal more information and harnesses the full power of the TSE3 library. TSE3MDL files often have the extension .tse3 </p>
<p> The type of the input file is automatically detected by <code>tse3play</code> . <code>tse3play</code> can also load legacy <i>TSE2MDL</i> files from sequencers based on the older TSE2 sequencer library.</p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</dt>
<dd> Provide help on the <code>tse3play</code> command line parameters.</dd>
<dt>-ver, &#8211;version</dt>
<dd> Print version number and exit.</dd>
<dt>-v, &#8211;verbose</dt>
<dd> Give verbose output on what <code>tse3play</code> is trying to do.</dd>
<dt>-list, &#8211;list-ports</dt>
<dd> Lists the port numbers available on your platform.</dd>
<dt>-nv, &#8211;novisual</dt>
<dd> Don&#8217;t produce visual feedback (text-based output-level indicator).</dd>
<dt>-np, &#8211;noplay</dt>
<dd> Don&#8217;t play the input file (only perform a conversion &#8211; if one is specified).</dd>
<dt>-l, &#8211;loop</dt>
<dd> Loop playback of the input file.</dd>
<dt>-omidi, &#8211;out-midi &lt;filename&gt;</dt>
<dd> Convert the loaded file to MIDI. File type will be MIDI type 1 unless <code>-omidi0</code> is specified. The filename of the output follows this option. You can specify &#8216;-&#8216; to output on stdandard out.</dd>
<dt>-omidi0, &#8211;out-midi-format-0</dt>
<dd> If performing a MIDI conversion, produce an output file in MIDI type 0 format. For most cases the default (type 1) is recommended.</dd>
<dt>-omidicomp, &#8211;out-midi-compact</dt>
<dd> Compact the converted MIDI file output. This removes any redundant information in the MIDI file that could be removed by using MIDI running status.</dd>
<dt>-otse3mdl, &#8211;out-tse3mdl FILENAME</dt>
<dd> Convert the file to tse3mdl format. The filename of the output follows this option. You can specify &#8216;-&#8216; to output on stdandard out.</dd>
<dt>-map, &#8211;map-channel F T</dt>
<dd> During playback, map MIDI channel F to MIDI channel T. Channel numbers start at zero.</dd>
<dt>-m, &#8211;metronome</dt>
<dd> During playback, produce a metronome tick.</dd>
<dt>-r, &#8211;reset</dt>
<dd> Send a basic MIDI reset message at playback start and end. This will send a reset message even if <code>-np</code> is specified.</dd>
<dt>-gmr, &#8211;gmreset</dt>
<dd> Send a General MIDI reset message at playback start and end. This will send a reset message even if <code>-np</code> is specified.</dd>
<dt>-gsr, &#8211;gsreset</dt>
<dd> Send a GS reset message at playback start and end. This will send a reset message even if <code>-np</code> is specified.</dd>
<dt>-xgr, &#8211;xgreset</dt>
<dd> Send an XG reset message at playback start and end. This will send a reset message even if <code>-np</code> is specified.</dd>
<dt>-unix, &#8211;unix-scheduler</dt>
<dd> Selects the best Unix scheduler device (either OSS or ALSA) as the MIDI output method. This is the default behaviour.</dd>
<dt>-oss, &#8211;oss-scheduler</dt>
<dd> Selects the Open Sound System interface as the MIDI output method.</dd>
<dt>-alsa, &#8211;alsa-scheduler</dt>
<dd> Selects the ALSA interface as the MIDI output method. This will only work if you have ALSA installed on your computer.</dd>
<dt>-arts, &#8211;arts-scheduler</dt>
<dd> Selects the aRts interface as the MIDI output method. This will only work if you have aRts installed on your computer.</dd>
<dt>-stream, &#8211;stream-scheduler</dt>
<dd> Selects the standard output stream as the MIDI output method. An English interpretation of each MIDI command generated will appear on standard out.</dd>
<dt>-s, &#8211;start</dt>
<dd> Begin playback at the specified clock pulse. The pulses are divisions of quarter notes. <code>tse3play</code> works to a resolution of 96 PPQN.</dd>
<dt>-solo, &#8211;solo-track</dt>
<dd> Play with the specified input track &#8216;soloed&#8217;. This will mute all the other tracks. Note that this option will mute the <code>input</code> track from the file, not the specified MIDI channel. Track numbers start at zero.</dd>
<dt>-sl, &#8211;sleep</dt>
<dd> Sets the time period that <code>tse3play</code> returns control back to the operating system between updates. The parameter is a number of u-seconds. The default value is 100. Specifying a shorter time will make the real time vu bars update more responsively. A value of 0 disables the sleep.</dd>
<dt>-stop, &#8211;no-stop</dt>
<dd> Prevents <code>tse3play</code> from exiting once playback has finished. This can be used in conjunction with &#8211;echo and no specified filename to make the computer act as a MIDI Thru box.</dd>
<dt>-e, &#8211;echo</dt>
<dd> Enable the MIDI echo facility, which is a soft MIDI Thru port. Anything received on the MIDI in connection will be immediately echoed on the MIDI out.</dd>
<dt>-mute, &#8211;mute-track</dt>
<dd> Mutes the specified track in the input file. The first track is track zero.</dd>
<dt>-pd, &#8211;patches-dir</dt>
<dd> Specifies the path to the directory in which FM or GUS patch files are to be found. This is used by the OSS driver to load sounds into the soundcard.</dd>
<dt>-port, &#8211;force-port</dt>
<dd> Forces all output to the specified port.</dd>
<dt>-fast, &#8211;fast-midi</dt>
<dd> Tells <code>tse3play</code> to use a faster MIDI file import routine. This will make the MIDI file playback start almost instantaneously (especially noticeable for very large MIDI files). You can only use this if you are not converting a file. </dd>
<p> It has a number of possible side effects; (i) The MIDI file&#8217;s last time stamp is trusted to be correct (it might not be) (ii) Stopping playback half way through <i>may</i> produce &#8216;hanging notes&#8217;</dl>
<h2>BUGS</h2>
<p> Naturally, <code>tse3play</code> is completely bug free. The TSE3 library upon which it is based is also completely bug free. However, if you do find something goes wrong then contact the author. The program can only be improved with your feedback.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 2000,2001 Pete Goodliffe. See the license file in the TSE3 doc diirectory for a complete license statement.</p>
<h2>AUTHOR</h2>
<p> Pete Goodliffe &lt;pete [at] cthree.org&gt; </p>
<p> Trax Software 2001</p>
<h2>SEE ALSO</h2>
<p> <code>playmidi</code>(1), <code>TSE3</code>(3) </p>
