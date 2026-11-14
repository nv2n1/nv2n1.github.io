---
title: "sox(1)"
name: "sox"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sox/"
description: "SoX – Sound eXchange, the Swiss Army knife of audio manipulation"
---

<h2>NAME</h2>
<p> SoX &#8211; Sound eXchange, the Swiss Army knife of audio manipulation</p>
<h2>SYNOPSIS</h2>
<pre><code>
sox[global - options][format - options] infile1
    [[format - options] infile2]...[format - options] outfile
        [effect[effect - options]]... play[global - options][format - options] infile1
    [[format - options] infile2]...[format - options]
                                   [effect[effect - options]]... rec[global - options][format - options] outfile
                                       [effect[effect - options]]...
</code></pre>
<h2>DESCRIPTION</h2>
<h3>Introduction</h3>
<p> SoX reads and writes audio files in most popular formats and can optionally apply effects to them. It can combine multiple input sources, synthesise audio, and, on many systems, act as a general purpose audio player or a multi-track audio recorder. It also has limited ability to split the input into multiple output files. </p>
<p> All SoX functionality is available using just the <code>sox</code> command. To simplify playing and recording audio, if SoX is invoked as <code>play</code>, the output file is automatically set to be the default sound device, and if invoked as <code>rec</code>, the default sound device is used as an input source. Additionally, the <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1) command provides a convenient way to just query audio file header information. </p>
<p> The heart of SoX is a library called libSoX. Those interested in extending SoX or using it in other programs should refer to the libSoX manual page: <code><a href="/docs/linux/man/3-libsox/">libsox</a></code>(3). </p>
<p> SoX is a command-line audio processing tool, particularly suited to making quick, simple edits and to batch processing. If you need an interactive, graphical audio editor, use <code><a href="/docs/linux/man/1-audacity/">audacity</a></code>(1). <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> The overall SoX processing chain can be summarised as follows: <center></p>
<table>
<tr VALIGN=top>
<td>Input(s) &rarr; Combiner &rarr; Effects &rarr; Output(s)
</td>
</tr>
</table>
<p></center> </p>
<p> Note however, that on the SoX command line, the positions of the Output(s) and the Effects are swapped w.r.t. the logical flow just shown. Note also that whilst options pertaining to files are placed before their respective file name, the opposite is true for effects. To show how this works in practice, here is a selection of examples of how SoX might be used. The simple </p>
<pre>
   sox recital.au recital.wav
</pre>
<p> translates an audio file in Sun AU format to a Microsoft WAV file, whilst </p>
<pre>
   sox recital.au -b 16 recital.wav channels 1 rate 16k fade 3 norm
</pre>
<p> performs the same format translation, but also applies four effects (down-mix to one channel, sample rate change, fade-in, nomalize), and stores the result at a bit-depth of 16. </p>
<pre>
   sox -r 16k -e signed -b 8 -c 1 voice-memo.raw voice-memo.wav
</pre>
<p> converts `raw&#8217; (a.k.a. `headerless&#8217;) audio to a self-describing file format, </p>
<pre>
   sox slow.aiff fixed.aiff speed 1.027
</pre>
<p> adjusts audio speed, </p>
<pre>
   sox short.wav long.wav longer.wav
</pre>
<p> concatenates two audio files, and </p>
<pre>
   sox -m music.mp3 voice.wav mixed.flac
</pre>
<p> mixes together two audio files. </p>
<pre>
   play &quot;The Moonbeams/Greatest/*.ogg&quot; bass +3
</pre>
<p> plays a collection of audio files whilst applying a bass boosting effect, </p>
<pre>
   play -n -c1 synth sin %-12 sin %-9 sin %-5 sin %-2 fade h 0.1 1 0.1
</pre>
<p> plays a synthesised `A minor seventh&#8217; chord with a pipe-organ sound, </p>
<pre>
   rec -c 2 radio.aiff trim 0 30:00
</pre>
<p> records half an hour of stereo audio, and </p>
<pre>
   play -q take1.aiff &amp; rec -M take1.aiff take1-dub.aiff
</pre>
<p> (with POSIX shell and where supported by hardware) records a new track in a multi-track recording. Finally, </p>
<pre>
   rec -r 44100 -b 16 -s -p silence 1 0.50 0.1% 1 10:00 0.1% | \
        sox -p song.ogg silence 1 0.50 0.1% 1 2.0 0.1% : \
        newfile : restart
</pre>
<p> records a stream of audio such as LP/cassette and splits in to multiple audio files at points with 2 seconds of silence. Also, it does not start recording until it detects audio is playing and stops after it sees 10 minutes of silence. </p>
<p> N.B. The above is just an overview of SoX&#8217;s capabilities; detailed explanations of how to use <i>all</i> SoX parameters, file formats, and effects can be found below in this manual, in <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7), and in <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1).</p>
<h3>File Format Types</h3>
<p> SoX can work with `self-describing&#8217; and `raw&#8217; audio files. `self-describing&#8217; formats (e.g. WAV, FLAC, MP3) have a header that completely describes the signal and encoding attributes of the audio data that follows. `raw&#8217; or `headerless&#8217; formats do not contain this information, so the audio characteristics of these must be described on the SoX command line or inferred from those of the input file. </p>
<p> The following four characteristics are used to describe the format of audio data such that it can be processed with SoX:</p>
<dl>
<dt>sample rate</p>
<dd> The sample rate in samples per second (`Hertz&#8217; or `Hz&#8217;). Digital telephony traditionally uses a sample rate of 8000 Hz (8 kHz), though these days, 16 and even 32 kHz are becoming more common. Audio Compact Discs use 44100 Hz (44.1 kHz). Digital Audio Tape and many computer systems use 48 kHz. Professional audio systems often use 96 kHz.</p>
<dt>sample size</p>
<dd> The number of bits used to store each sample. Today, 16-bit is commonly used. 8-bit was popular in the early days of computer audio. 24-bit is used in the professional audio arena. Other sizes are also used.</p>
<dt>data encoding</p>
<dd> The way in which each audio sample is represented (or `encoded&#8217;). Some encodings have variants with different byte-orderings or bit-orderings. Some compress the audio data so that the stored audio data takes up less space (i.e. disk space or transmission bandwidth) than the other format parameters and the number of samples would imply. Commonly-used encoding types include floating-point, &mu;-law, ADPCM, signed-integer PCM, MP3, and FLAC.</p>
<dt>channels</p>
<dd> The number of audio channels contained in the file. One (`mono&#8217;) and two (`stereo&#8217;) are widely used. `Surround sound&#8217; audio typically contains six or more channels.</dl>
<p> The term `bit-rate&#8217; is a measure of the amount of storage occupied by an encoded audio signal over a unit of time. It can depend on all of the above and is typically denoted as a number of kilo-bits per second (kbps). An A-law telephony signal has a bit-rate of 64 kbps. MP3-encoded stereo music typically has a bit-rate of 128-196 kbps. FLAC-encoded stereo music typically has a bit-rate of 550-760 kbps. </p>
<p> Most self-describing formats also allow textual `comments&#8217; to be embedded in the file that can be used to describe the audio in some way, e.g. for music, the title, the author, etc. </p>
<p> One important use of audio file comments is to convey `Replay Gain&#8217; information. SoX supports applying Replay Gain information, but not generating it. Note that by default, SoX copies input file comments to output files that support comments, so output files may contain Replay Gain information if some was present in the input file. In this case, if anything other than a simple format conversion was performed then the output file Replay Gain information is likely to be incorrect and so should be recalculated using a tool that supports this (not SoX). </p>
<p> The <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1) command can be used to display information from audio file headers.</p>
<h3>Determining &amp; Setting The File Format</h3>
<p> There are several mechanisms available for SoX to use to determine or set the format characteristics of an audio file. Depending on the circumstances, individual characteristics may be determined or set using different mechanisms. </p>
<p> To determine the format of an input file, SoX will use, in order of precedence and as given or available:</p>
<dl>
<dt>1.</p>
<dd> Command-line format options.</p>
<dt>2.</p>
<dd> The contents of the file header.</p>
<dt>3.</p>
<dd> The filename extension.</dl>
<p> To set the output file format, SoX will use, in order of precedence and as given or available:</p>
<dl>
<dt>1.</p>
<dd> Command-line format options.</p>
<dt>2.</p>
<dd> The filename extension.</p>
<dt>3.</p>
<dd> The input file format characteristics, or the closest that is supported by the output file type.</dl>
<p> For all files, SoX will exit with an error if the file type cannot be determined. Command-line format options may need to be added or changed to resolve the problem.</p>
<h3>Playing &amp; Recording Audio</h3>
<p> The <code>play</code> and <code>rec</code> commands are provided so that basic playing and recording is as simple as </p>
<pre>
   play existing-file.wav
</pre>
<p> and </p>
<pre>
   rec new-file.wav
</pre>
<p> These two commands are functionally equivalent to </p>
<pre>
   sox existing-file.wav -d
</pre>
<p> and </p>
<pre>
   sox -d new-file.wav
</pre>
<p> Of course, further options and effects (as described below) can be added to the commands in either form. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> Some systems provide more than one type of (SoX-compatible) audio driver, e.g. ALSA &amp; OSS, or SUNAU &amp; AO. Systems can also have more than one audio device (a.k.a. `sound card&#8217;). If more than one audio driver has been built-in to SoX, and the default selected by SoX when recording or playing is not the one that is wanted, then the <code>AUDIODRIVER</code> environment variable can be used to override the default. For example (on many systems): </p>
<pre>
   set AUDIODRIVER=oss
   play ...
</pre>
<p> The <code>AUDIODEV</code> environment variable can be used to override the default audio device, e.g. </p>
<pre>
   set AUDIODEV=/dev/dsp2
   play ...
   sox ... -t oss
</pre>
<p> or </p>
<pre>
   set AUDIODEV=hw:soundwave,1,2
   play ...
   sox ... -t alsa
</pre>
<p> Note that the way of setting environment variables varies from system to system &#8211; for some specific examples, see `SOX_OPTS&#8217; below. </p>
<p> When playing a file with a sample rate that is not supported by the audio output device, SoX will automatically invoke the <code>rate</code> effect to perform the necessary sample rate conversion. For compatibility with old hardware, the default <code>rate</code> quality level is set to `low&#8217;. This can be changed by explicitly specifying the <code>rate</code> effect with a different quality level, e.g. </p>
<pre>
   play ... rate -m
</pre>
<p> or by using the <code>&#8211;play-rate-arg</code> option (see below). <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> On some systems, SoX allows audio playback volume to be adjusted whilst using <code>play</code>. Where supported, this is achieved by tapping the `v&#8217; &amp; `V&#8217; keys during playback. </p>
<p> To help with setting a suitable recording level, SoX includes a peak-level meter which can be invoked (before making the actual recording) as follows: </p>
<pre>
   rec -n
</pre>
<p> The recording level should be adjusted (using the system-provided mixer program, not SoX) so that the meter is <i>at most occasionally</i> full scale, and never `in the red&#8217; (an exclamation mark is shown). See also <code>-S</code> below.</p>
<h3>Accuracy</h3>
<p> Many file formats that compress audio discard some of the audio signal information whilst doing so. Converting to such a format and then converting back again will not produce an exact copy of the original audio. This is the case for many formats used in telephony (e.g. A-law, GSM) where low signal bandwidth is more important than high audio fidelity, and for many formats used in portable music players (e.g. MP3, Vorbis) where adequate fidelity can be retained even with the large compression ratios that are needed to make portable players practical. </p>
<p> Formats that discard audio signal information are called `lossy&#8217;. Formats that do not are called `lossless&#8217;. The term `quality&#8217; is used as a measure of how closely the original audio signal can be reproduced when using a lossy format. </p>
<p> Audio file conversion with SoX is lossless when it can be, i.e. when not using lossy compression, when not reducing the sampling rate or number of channels, and when the number of bits used in the destination format is not less than in the source format. E.g. converting from an 8-bit PCM format to a 16-bit PCM format is lossless but converting from an 8-bit PCM format to (8-bit) A-law isn&#8217;t. </p>
<p> <code>N.B.</code> SoX converts all audio files to an internal uncompressed format before performing any audio processing. This means that manipulating a file that is stored in a lossy format can cause further losses in audio fidelity. E.g. with </p>
<pre>
   sox long.mp3 short.mp3 trim 10
</pre>
<p> SoX first decompresses the input MP3 file, then applies the <code>trim</code> effect, and finally creates the output MP3 file by re-compressing the audio &#8211; with a possible reduction in fidelity above that which occurred when the input file was created. Hence, if what is ultimately desired is lossily compressed audio, it is highly recommended to perform all audio processing using lossless file formats and then convert to the lossy format only at the final stage. </p>
<p> <code>N.B.</code> Applying multiple effects with a single SoX invocation will, in general, produce more accurate results than those produced using multiple SoX invocations.</p>
<h3>Dithering</h3>
<p> Dithering is a technique used to maximise the dynamic range of audio stored at a particular bit-depth. Any distortion introduced by quantisation is decorrelated by adding a small amount of white noise to the signal. In most cases, SoX can determine whether the selected processing requires dither and will add it during output formatting if appropriate. </p>
<p> Specifically, by default, SoX automatically adds TPDF dither when the output bit-depth is less than 24 and any of the following are true:</p>
<dl>
<dt>&bull;</p>
<dd> bit-depth reduction has been specified explicitly using a command-line option</p>
<dt>&bull;</p>
<dd> the output file format supports only bit-depths lower than that of the input file format</p>
<dt>&bull;</p>
<dd> an effect has increased effective bit-depth within the internal processing chain</dl>
<p> For example, adjusting volume with <code>vol 0.25</code> requires two additional bits in which to losslessly store its results (since 0.25 decimal equals 0.01 binary). So if the input file bit-depth is 16, then SoX&#8217;s internal representation will utilise 18 bits after processing this volume change. In order to store the output at the same depth as the input, dithering is used to remove the additional bits. </p>
<p> Use the <code>-V</code> option to see what processing SoX has automatically added. The <code>-D</code> option may be given to override automatic dithering. To invoke dithering manually (e.g. to select a noise-shaping curve), see the <code>dither</code> effect.</p>
<h3>Clipping</h3>
<p> Clipping is distortion that occurs when an audio signal level (or `volume&#8217;) exceeds the range of the chosen representation. In most cases, clipping is undesirable and so should be corrected by adjusting the level prior to the point (in the processing chain) at which it occurs. </p>
<p> In SoX, clipping could occur, as you might expect, when using the <code>vol</code> or <code>gain</code> effects to increase the audio volume. Clipping could also occur with many other effects, when converting one format to another, and even when simply playing the audio. </p>
<p> Playing an audio file often involves resampling, and processing by analogue components can introduce a small DC offset and/or amplification, all of which can produce distortion if the audio signal level was initially too close to the clipping point. </p>
<p> For these reasons, it is usual to make sure that an audio file&#8217;s signal level has some `headroom&#8217;, i.e. it does not exceed a particular level below the maximum possible level for the given representation. Some standards bodies recommend as much as 9dB headroom, but in most cases, 3dB (~~ 70% linear) is enough. Note that this wisdom seems to have been lost in modern music production; in fact, many CDs, MP3s, etc. are now mastered at levels <i>above</i> 0dBFS i.e. the audio is clipped as delivered. </p>
<p> SoX&#8217;s <code>stat</code> and <code>stats</code> effects can assist in determining the signal level in an audio file. The <code>gain</code> or <code>vol</code> effect can be used to prevent clipping, e.g. </p>
<pre>
   sox dull.wav bright.wav gain -6 treble +6
</pre>
<p> guarantees that the treble boost will not clip. </p>
<p> If clipping occurs at any point during processing, SoX will display a warning message to that effect. </p>
<p> See also <code>-G</code> and the <code>gain</code> and <code>norm</code> effects.</p>
<h3>Input File Combining</h3>
<p> SoX&#8217;s input combiner can be configured (see OPTIONS below) to combine multiple files using any of the following methods: `concatenate&#8217;, `sequence&#8217;, `mix&#8217;, `mix-power&#8217;, `merge&#8217;, or `multiply&#8217;. The default method is `sequence&#8217; for <code>play</code>, and `concatenate&#8217; for <code>rec</code> and <code>sox</code>. </p>
<p> For all methods other than `sequence&#8217;, multiple input files must have the same sampling rate. If necessary, separate SoX invocations can be used to make sampling rate adjustments prior to combining. </p>
<p> If the `concatenate&#8217; combining method is selected (usually, this will be by default) then the input files must also have the same number of channels. The audio from each input will be concatenated in the order given to form the output file. </p>
<p> The `sequence&#8217; combining method is selected automatically for <code>play</code>. It is similar to `concatenate&#8217; in that the audio from each input file is sent serially to the output file. However, here the output file may be closed and reopened at the corresponding transition between input files. This may be just what is needed when sending different types of audio to an output device, but is not generally useful when the output is a normal file. </p>
<p> If either the `mix&#8217; or `mix-power&#8217; combining method is selected then two or more input files must be given and will be mixed together to form the output file. The number of channels in each input file need not be the same, but SoX will issue a warning if they are not and some channels in the output file will not contain audio from every input file. A mixed audio file cannot be un-mixed without reference to the original input files. </p>
<p> If the `merge&#8217; combining method is selected then two or more input files must be given and will be merged together to form the output file. The number of channels in each input file need not be the same. A merged audio file comprises all of the channels from all of the input files. Un-merging is possible using multiple invocations of SoX with the <code>remix</code> effect. For example, two mono files could be merged to form one stereo file. The first and second mono files would become the left and right channels of the stereo file. </p>
<p> The `multiply&#8217; combining method multiplies the sample values of corresponding channels (treated as numbers in the interval -1 to +1). If the number of channels in the input files is not the same, the missing channels are considered to contain all zero. </p>
<p> When combining input files, SoX applies any specified effects (including, for example, the <code>vol</code> volume adjustment effect) after the audio has been combined. However, it is often useful to be able to set the volume of (i.e. `balance&#8217;) the inputs individually, before combining takes place. </p>
<p> For all combining methods, input file volume adjustments can be made manually using the <code>-v</code> option (below) which can be given for one or more input files. If it is given for only some of the input files then the others receive no volume adjustment. In some circumstances, automatic volume adjustments may be applied (see below). </p>
<p> The <code>-V</code> option (below) can be used to show the input file volume adjustments that have been selected (either manually or automatically). </p>
<p> There are some special considerations that need to made when mixing input files: </p>
<p> Unlike the other methods, `mix&#8217; combining has the potential to cause clipping in the combiner if no balancing is performed. In this case, if manual volume adjustments are not given, SoX will try to ensure that clipping does not occur by automatically adjusting the volume (amplitude) of each input signal by a factor of &sup1;/<font SIZE="-2">n</font>, where n is the number of input files. If this results in audio that is too quiet or otherwise unbalanced then the input file volumes can be set manually as described above. Using the <code>norm</code> effect on the mix is another alternative. </p>
<p> If mixed audio seems loud enough at some points but too quiet in others then dynamic range compression should be applied to correct this &#8211; see the <code>compand</code> effect. </p>
<p> With the `mix-power&#8217; combine method, the mixed volume is approximately equal to that of one of the input signals. This is achieved by balancing using a factor of &sup1;/<font SIZE="-2">srn</font> instead of &sup1;/<font SIZE="-2">n</font>. Note that this balancing factor does not guarantee that clipping will not occur, but the number of clips will usually be low and the resultant distortion is generally imperceptible.</p>
<h3>Output Files</h3>
<p> SoX&#8217;s default behaviour is to take one or more input files and write them to a single output file. </p>
<p> This behaviour can be changed by specifying the pseudo-effect `newfile&#8217; within the effects list. SoX will then enter multiple output mode. </p>
<p> In multiple output mode, a new file is created when the effects prior to the `newfile&#8217; indicate they are done. The effects chain listed after `newfile&#8217; is then started up and its output is saved to the new file. </p>
<p> In multiple output mode, a unique number will automatically be appended to the end of all filenames. If the filename has an extension then the number is inserted before the extension. This behaviour can be customized by placing a %n anywhere in the filename where the number should be substituted. An optional number can be placed after the % to indicate a minimum fixed width for the number. </p>
<p> Multiple output mode is not very useful unless an effect that will stop the effects chain early is specified before the `newfile&#8217;. If end of file is reached before the effects chain stops itself then no new file will be created as it would be empty. </p>
<p> The following is an example of splitting the first 60 seconds of an input file into two 30 second files and ignoring the rest. </p>
<pre>
   sox song.wav ringtone%1n.wav trim 0 30 : newfile : trim 0 30
</pre>
<h3>Stopping SoX</h3>
<p> Usually SoX will complete its processing and exit automatically once it has read all available audio data from the input files. </p>
<p> If desired, it can be terminated earlier by sending an interrupt signal to the process (usually by pressing the keyboard interrupt key which is normally Ctrl-C). This is a natural requirement in some circumstances, e.g. when using SoX to make a recording. Note that when using SoX to play multiple files, Ctrl-C behaves slightly differently: pressing it once causes SoX to skip to the next file; pressing it twice in quick succession causes SoX to exit. </p>
<p> Another option to stop processing early is to use an effect that has a time period or sample count to determine the stopping point. The trim effect is an example of this. Once all effects chains have stopped then SoX will also stop.</p>
<h2>FILENAMES</h2>
<p> Filenames can be simple file names, absolute or relative path names, or URLs (input files only). Note that URL support requires that <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) is available. </p>
<p> Note: Giving SoX an input or output filename that is the same as a SoX effect-name will not work since SoX will treat it as an effect specification. The only work-around to this is to avoid such filenames. This is generally not difficult since most audio filenames have a filename `extension&#8217;, whilst effect-names do not.</p>
<h3>Special Filenames</h3>
<p> The following special filenames may be used in certain circumstances in place of a normal filename on the command line:</p>
<dl>
<dt><code>&#8211;</code></p>
<dd> SoX can be used in simple pipeline operations by using the special filename `-&#8216; which, if used as an input filename, will cause SoX will read audio data from `standard input&#8217; (stdin), and which, if used as the output filename, will cause SoX will send audio data to `standard output&#8217; (stdout). Note that when using this option for the output file, and sometimes when using it for an input file, the file-type (see <code>-t</code> below) must also be given.</p>
<dt><code>&quot;|</code><i>program </i>[<i>options</i>] &#8230;<code>&quot;</code></p>
<dd> This can be used in place of an input filename to specify the the given program&#8217;s standard output (stdout) be used as an input file. Unlike <code>&#8211;</code> (above), this can be used for several inputs to one SoX command. For example, if `genw&#8217; generates mono WAV formatted signals to its standard output, then the following command makes a stereo file from two generated signals: </p>
<pre>
   sox -M &quot;|genw --imd -&quot; &quot;|genw --thd -&quot; out.wav
</pre>
<p> For headerless (raw) audio, <code>-t</code> (and perhaps other format options) will need to be given, preceding the input command.</p>
<dt><code>&quot;</code><i>wildcard-filename</i><code>&quot;</code></p>
<dd> Specifies that filename `globbing&#8217; (wild-card matching) should be performed by SoX instead of by the shell. This allows a single set of file options to be applied to a group of files. For example, if the current directory contains three `vox&#8217; files, file1.vox, file2.vox, and file3.vox, then </p>
<pre>
   play --rate 6k *.vox
</pre>
<p> will be expanded by the `shell&#8217; (in most environments) to </p>
<pre>
   play --rate 6k file1.vox file2.vox file3.vox
</pre>
<p> which will treat only the first vox file as having a sample rate of 6k. With </p>
<pre>
   play --rate 6k &quot;*.vox&quot;
</pre>
<p> the given sample rate option will be applied to all three vox files.</p>
<dt><code>-p</code>, <code>&#8211;sox-pipe</code></p>
<dd> This can be used in place of an output filename to specify that the SoX command should be used as in input pipe to another SoX command. For example, the command: </p>
<pre>
   play &quot;|sox -n -p synth 2&quot; &quot;|sox -n -p synth 2 tremolo 10&quot; stat
</pre>
<p> plays two `files&#8217; in succession, each with different effects. </p>
<p> <code>-p</code> is in fact an alias for `<code>-t sox &#8211;</code>&#8216;.</p>
<dt><code>-d</code>, <code>&#8211;default-device</code></p>
<dd> This can be used in place of an input or output filename to specify that the default audio device (if one has been built into SoX) is to be used. This is akin to invoking <code>rec</code> or <code>play</code> (as described above).</p>
<dt><code>-n</code>, <code>&#8211;null</code></p>
<dd> This can be used in place of an input or output filename to specify that a `null file&#8217; is to be used. Note that here, `null file&#8217; refers to a SoX-specific mechanism and is not related to any operating-system mechanism with a similar name. </p>
<p> Using a null file to input audio is equivalent to using a normal audio file that contains an infinite amount of silence, and as such is not generally useful unless used with an effect that specifies a finite time length (such as <code>trim</code> or <code>synth</code>). </p>
<p> Using a null file to output audio amounts to discarding the audio and is useful mainly with effects that produce information about the audio instead of affecting it (such as <code>noiseprof</code> or <code>stat</code>). </p>
<p> The sampling rate associated with a null file is by default 48 kHz, but, as with a normal file, this can be overridden if desired using command-line format options (see below).</dl>
<h3>Supported File &amp; Audio Device Types</h3>
<p> See <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7) for a list and description of the supported file formats and audio device drivers.</p>
<h2>OPTIONS</h2>
<h3>Global Options</h3>
<p> These options can be specified on the command line at any point before the first effect name. </p>
<p> The <code>SOX_OPTS</code> environment variable can be used to provide alternative default values for SoX&#8217;s global options. For example: </p>
<pre>
   SOX_OPTS=&quot;--buffer 20000 --play-rate-arg -hs --temp /mnt/temp&quot;
</pre>
<p> Note that setting SOX_OPTS can potentially create unwanted changes in the behaviour of scripts or other programs that invoke SoX. SOX_OPTS might best be used for things (such as in the given example) that reflect the environment in which SoX is being run. Enabling options such as <code>&#8211;no-clobber</code> as default might be handled better using a shell alias since a shell alias will not affect operation in scripts etc. </p>
<p> One way to ensure that a script cannot be affected by SOX_OPTS is to clear SOX_OPTS at the start of the script, but this of course loses the benefit of SOX_OPTS carrying some system-wide default options. An alternative approach is to explicitly invoke SoX with default option values, e.g. </p>
<pre>
   SOX_OPTS=&quot;-V --no-clobber&quot;
   ...
   sox -V2 --clobber $input $output ...
</pre>
<p> Note that the way to set environment variables varies from system to system. Here are some examples: </p>
<p> Unix bash: </p>
<pre>
   export SOX_OPTS=&quot;-V --no-clobber&quot;
</pre>
<p> Unix csh: </p>
<pre>
   setenv SOX_OPTS &quot;-V --no-clobber&quot;
</pre>
<p> MS-DOS/MS-Windows: </p>
<pre>
   set SOX_OPTS=-V --no-clobber
</pre>
<p> MS-Windows GUI: via Control Panel : System : Advanced : Environment Variables </p>
<p> Mac OS X GUI: Refer to Apple&#8217;s Technical Q&amp;A QA1067 document.</p>
<dl>
<dt><code>&#8211;buffer</code> <code>BYTES</code>, <code>&#8211;input-buffer</code> <code>BYTES</code></p>
<dd> Set the size in bytes of the buffers used for processing audio (default 8192). <code>&#8211;buffer</code> applies to input, effects, and output processing; <code>&#8211;input-buffer</code> applies only to input processing (for which it overrides <code>&#8211;buffer</code> if both are given). </p>
<p> Be aware that large values for <code>&#8211;buffer</code> will cause SoX to be become slow to respond to requests to terminate or to skip the current input file.</p>
<dt><code>&#8211;clobber</code></p>
<dd> Don&#8217;t prompt before overwriting an existing file with the same name as that given for the output file. This is the default behaviour.</p>
<dt><code>&#8211;combine concatenate</code>|<code>merge</code>|<code>mix</code>|<code>mix-power</code>|<code>multiply</code>|<code>sequence</code></p>
<dd> Select the input file combining method; for some of these, short options are available: <code>-m</code> selects `mix&#8217;, <code>-M</code> selects `merge&#8217;, and <code>-T</code> selects `multiply&#8217;. </p>
<p> See <code>Input File Combining</code> above for a description of the different combining methods.</p>
<dt><code>-D</code>, <code>&#8211;no-dither</code></p>
<dd> Disable automatic dither &#8211; see `Dithering&#8217; above. An example of why this might occasionally be useful is if a file has been converted from 16 to 24 bit with the intention of doing some processing on it, but in fact no processing is needed after all and the original 16 bit file has been lost, then, strictly speaking, no dither is needed if converting the file back to 16 bit. See also the <code>stats</code> effect for how to determine the actual bit depth of the audio within a file.</p>
<dt><code>&#8211;effects-file </code><i>FILENAME</i></p>
<dd> Use FILENAME to obtain all effects and their arguments. The file is parsed as if the values were specified on the command line. A new line can be used in place of the special <code>:</code> marker to separate effect chains. For convenience, such markers at the end of the file are normally ignored; if you want to specify an empty last effects chain, use an explicit <code>:</code> by itself on the last line of the file. This option causes any effects specified on the command line to be discarded.</p>
<dt><code>-G</code>, <code>&#8211;guard</code></p>
<dd> Automatically invoke the <code>gain</code> effect to guard against clipping. E.g. </p>
<pre>
   sox -G infile -b 16 outfile rate 44100 dither -s
</pre>
<p> is shorthand for </p>
<pre>
   sox infile -b 16 outfile gain -h rate 44100 gain -rh dither -s
</pre>
<p> See also <code>-V,</code> <code>&#8211;norm,</code> and the <code>gain</code> effect.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show version number and usage information.</p>
<dt><code>&#8211;help-effect </code><i>NAME</i></p>
<dd> Show usage information on the specified effect. The name <code>all</code> can be used to show usage on all effects.</p>
<dt><code>&#8211;help-format </code><i>NAME</i></p>
<dd> Show information about the specified file format. The name <code>all</code> can be used to show information on all formats.</p>
<dt><code>&#8211;i</code>, <code>&#8211;info</code></p>
<dd> Only if given as the first parameter to <code>sox</code>, behave as <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1).</p>
<dt><code>-m</code>|<code>-M</code></p>
<dd> Equivalent to <code>&#8211;combine mix</code> and <code>&#8211;combine merge</code>, respectively.</p>
<dt><code>&#8211;magic</code></p>
<dd> If SoX has been built with the optional `libmagic&#8217; library then this option can be given to enable its use in helping to detect audio file types.</p>
<dt><code>&#8211;multi-threaded</code> | <code>&#8211;single-threaded</code></p>
<dd> By default, SoX is `single threaded&#8217;. If the <code>&#8211;multi-threaded</code> option is given however then SoX will process audio channels for most multi-channel effects in parallel on hyper-threading/multi-core architectures. This may reduce processing time, though sometimes it may be necessary to use this option in conjuction with a larger buffer size than is the default to gain any benefit from multi-threaded processing (e.g. 131072; see <code>&#8211;buffer</code> above).</p>
<dt><code>&#8211;no-clobber</code></p>
<dd> Prompt before overwriting an existing file with the same name as that given for the output file. </p>
<p> <code>N.B.</code> Unintentionally overwriting a file is easier than you might think, for example, if you accidentally enter </p>
<pre>
   sox file1 file2 effect1 effect2 ...
</pre>
<p> when what you really meant was </p>
<pre>
   play file1 file2 effect1 effect2 ...
</pre>
<p> then, without this option, file2 will be overwritten. Hence, using this option is recommended. SOX_OPTS (above), a `shell&#8217; alias, script, or batch file may be an appropriate way of permanently enabling it.</p>
<dt><code>&#8211;norm</code>[<code>=</code><i>dB-level</i>]</p>
<dd> Automatically invoke the <code>gain</code> effect to guard against clipping and to normalise the audio. E.g. </p>
<pre>
   sox --norm infile -b 16 outfile rate 44100 dither -s
</pre>
<p> is shorthand for </p>
<pre>
   sox infile -b 16 outfile gain -h rate 44100 gain -nh dither -s
</pre>
<p> Optionally, the audio can be normalized to a given level (usually) below 0 dBFS: </p>
<pre>
   sox --norm=-3 infile outfile
</pre>
<p> See also <code>-V,</code> <code>-G,</code> and the <code>gain</code> effect.</p>
<dt><code>&#8211;play-rate-arg ARG</code></p>
<dd> Selects a quality option to be used when the `rate&#8217; effect is automatically invoked whilst playing audio. This option is typically set via the <code>SOX_OPTS</code> environment variable (see above).</p>
<dt><code>&#8211;plot gnuplot</code>|<code>octave</code>|<code>off</code></p>
<dd> If not set to <code>off</code> (the default if <code>&#8211;plot</code> is not given), run in a mode that can be used, in conjunction with the gnuplot program or the GNU Octave program, to assist with the selection and configuration of many of the transfer-function based effects. For the first given effect that supports the selected plotting program, SoX will output commands to plot the effect&#8217;s transfer function, and then exit without actually processing any audio. E.g. </p>
<pre>
   sox --plot octave input-file -n highpass 1320 &gt; highpass.plt
   octave highpass.plt
</pre>
<dt><code>-q</code>, <code>&#8211;no-show-progress</code></p>
<dd> Run in quiet mode when SoX wouldn&#8217;t otherwise do so. This is the opposite of the <code>-S</code> option.</p>
<dt><code>-R</code></p>
<dd> Run in `repeatable&#8217; mode. When this option is given, where applicable, SoX will embed a fixed time-stamp in the output file (e.g. <code>AIFF</code>) and will `seed&#8217; pseudo random number generators (e.g. <code>dither</code>) with a fixed number, thus ensuring that successive SoX invocations with the same inputs and the same parameters yield the same output.</p>
<dt><code>&#8211;replay-gain track</code>|<code>album</code>|<code>off</code></p>
<dd> Select whether or not to apply replay-gain adjustment to input files. The default is <code>off</code> for <code>sox</code> and <code>rec</code>, <code>album</code> for <code>play</code> where (at least) the first two input files are tagged with the same Artist and Album names, and <code>track</code> for <code>play</code> otherwise.</p>
<dt><code>-S</code>, <code>&#8211;show-progress</code></p>
<dd> Display input file format/header information, and processing progress as input file(s) percentage complete, elapsed time, and remaining time (if known; shown in brackets), and the number of samples written to the output file. Also shown is a peak-level meter, and an indication if clipping has occurred. The peak-level meter shows up to two channels and is calibrated for digital audio as follows (right channel shown): <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>dB FSD</i></td>
<td><i>Display</i></td>
<td ALIGN=center><i>dB FSD</i></td>
<td><i>Display</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-25</td>
<td>&#8211;</td>
<td ALIGN=center>-11</td>
<td>====
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-23</td>
<td> = </td>
<td ALIGN=center>-9</td>
<td>====-
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-21</td>
<td>=-</td>
<td ALIGN=center>-7</td>
<td>=====
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-19</td>
<td>==</td>
<td ALIGN=center>-5</td>
<td>=====-
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-17</td>
<td>==-</td>
<td ALIGN=center>-3</td>
<td>======
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-15</td>
<td>===</td>
<td ALIGN=center>-1</td>
<td>=====!
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>-13</td>
<td>===-</td>
<td ALIGN=center></td>
<td>
</td>
</tr>
</table>
<p></center> </p>
<p> A three-second peak-held value of headroom in dBs will be shown to the right of the meter if this is below 6dB. </p>
<p> This option is enabled by default when using SoX to play or record audio.</p>
<dt><code>-T</code></p>
<dd> Equivalent to <code>&#8211;combine multiply</code>.</p>
<dt><code>&#8211;temp</code><i> DIRECTORY</i></p>
<dd> Specify that any temporary files should be created in the given <i>DIRECTORY</i>. This can be useful if there are permission or free-space problems with the default location. In this case, using `<code>&#8211;temp .</code>&#8216; (to use the current directory) is often a good solution.</p>
<dt><code>&#8211;version</code></p>
<dd> Show SoX&#8217;s version number and exit.</p>
<dt><code>-V</code>[<i>level</i>]</p>
<dd> Set verbosity. This is particularly useful for seeing how any automatic effects have been invoked by SoX. </p>
<p> SoX displays messages on the console (stderr) according to the following verbosity levels:</p>
<dt>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt>0</p>
<dd> No messages are shown at all; use the exit status to determine if an error has occurred.</p>
<dt>1</p>
<dd> Only error messages are shown. These are generated if SoX cannot complete the requested commands.</p>
<dt>2</p>
<dd> Warning messages are also shown. These are generated if SoX can complete the requested commands, but not exactly according to the requested command parameters, or if clipping occurs.</p>
<dt>3</p>
<dd> Descriptions of SoX&#8217;s processing phases are also shown. Useful for seeing exactly how SoX is processing your audio.</p>
<dt>4 and above</p>
<dd> Messages to help with debugging SoX are also shown.</dl>
</dl>
<dt>
<dd> By default, the verbosity level is set to 2 (shows errors and warnings). Each occurrence of the <code>-V</code> option increases the verbosity level by 1. Alternatively, the verbosity level can be set to an absolute number by specifying it immediately after the <code>-V</code>, e.g. <code>-V0</code> sets it to 0.</p>
<dt>
<dd></dl>
<h3>Input File Options</h3>
<p> These options apply only to input files and may precede only input filenames on the command line.</p>
<dl>
<dt><code>&#8211;ignore-length</code></p>
<dd> Override an (incorrect) audio length given in an audio file&#8217;s header. If this option is given then SoX will keep reading audio until it reaches the end of the input file.</p>
<dt><code>-v</code>, <code>&#8211;volume</code> <i>FACTOR</i></p>
<dd> Intended for use when combining multiple input files, this option adjusts the volume of the file that follows it on the command line by a factor of <i>FACTOR</i>. This allows it to be `balanced&#8217; w.r.t. the other input files. This is a linear (amplitude) adjustment, so a number less than 1 decreases the volume and a number greater than 1 increases it. If a negative number is given then in addition to the volume adjustment, the audio signal will be inverted. </p>
<p> See also the <code>norm</code>, <code>vol</code>, and <code>gain</code> effects, and see <code>Input File Balancing</code> above.</dl>
<h3>Input &amp; Output File Format Options</h3>
<p> These options apply to the input or output file whose name they immediately precede on the command line and are used mainly when working with headerless file formats or when specifying a format for the output file that is different to that of the input file.</p>
<dl>
<dt><code>-b</code> <i>BITS</i>, <code>&#8211;bits</code> <i>BITS</i></p>
<dd> The number of bits (a.k.a. bit-depth or sometimes word-length) in each encoded sample. Not applicable to complex encodings such as MP3 or GSM. Not necessary with encodings that have a fixed number of bits, e.g. A/&mu;-law, ADPCM. </p>
<p> For an input file, the most common use for this option is to inform SoX of the number of bits per sample in a `raw&#8217; (`headerless&#8217;) audio file. For example </p>
<pre>
   sox -r 16k -e signed -b 8 input.raw output.wav
</pre>
<p> converts a particular `raw&#8217; file to a self-describing `WAV&#8217; file. </p>
<p> For an output file, this option can be used (perhaps along with <code>-e</code>) to set the output encoding size. By default (i.e. if this option is not given), the output encoding size will (providing it is supported by the output file type) be set to the input encoding size. For example </p>
<pre>
   sox input.cdda -b 24 output.wav
</pre>
<p> converts raw CD digital audio (16-bit, signed-integer) to a 24-bit (signed-integer) `WAV&#8217; file.</p>
<dt><code>-1</code>/<code>-2</code>/<code>-3</code>/<code>-4</code>/<code>-8</code></p>
<dd> The number of bytes in each encoded sample. Deprecated aliases for <code>-b 8</code>, <code>-b 16</code>, <code>-b 24</code>, <code>-b 32</code>, <code>-b 64</code> respectively.</p>
<dt><code>-c</code> <i>CHANNELS</i>, <code>&#8211;channels</code> <i>CHANNELS</i></p>
<dd> The number of audio channels in the audio file. This can be any number greater than zero. </p>
<p> For an input file, the most common use for this option is to inform SoX of the number of channels in a `raw&#8217; (`headerless&#8217;) audio file. Occasionally, it may be useful to use this option with a `headered&#8217; file, in order to override the (presumably incorrect) value in the header &#8211; note that this is only supported with certain file types. Examples: </p>
<pre>
   sox -r 48k -e float -b 32 -c 2 input.raw output.wav
</pre>
<p> converts a particular `raw&#8217; file to a self-describing `WAV&#8217; file. </p>
<pre>
   play -c 1 music.wav
</pre>
<p> interprets the file data as belonging to a single channel regardless of what is indicated in the file header. Note that if the file does in fact have two channels, this will result in the file playing at half speed. </p>
<p> For an output file, this option provides a shorthand for specifying that the <code>channels</code> effect should be invoked in order to change (if necessary) the number of channels in the audio signal to the number given. For example, the following two commands are equivalent: </p>
<pre>
   sox input.wav -c 1 output.wav bass -b 24
   sox input.wav      output.wav bass -b 24 channels 1
</pre>
<p> though the second form is more flexible as it allows the effects to be ordered arbitrarily.</p>
<dt><code>-e </code><i>ENCODING</i>, <code>&#8211;encoding</code> <i>ENCODING</i></p>
<dd> The audio encoding type. Sometimes needed with file-types that support more than one encoding type. For example, with raw, WAV, or AU (but not, for example, with MP3 or FLAC). The available encoding types are as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>signed-integer</code></p>
<dd> PCM data stored as signed (`two&#8217;s complement&#8217;) integers. Commonly used with a 16 or 24 -bit encoding size. A value of 0 represents minimum signal power.</p>
<dt><code>unsigned-integer</code></p>
<dd> PCM data stored as unsigned integers. Commonly used with an 8-bit encoding size. A value of 0 represents maximum signal power.</p>
<dt><code>floating-point</code></p>
<dd> PCM data stored as IEEE 753 single precision (32-bit) or double precision (64-bit) floating-point (`real&#8217;) numbers. A value of 0 represents minimum signal power.</p>
<dt><code>a-law</code></p>
<dd> International telephony standard for logarithmic encoding to 8 bits per sample. It has a precision equivalent to roughly 13-bit PCM and is sometimes encoded with reversed bit-ordering (see the <code>-X</code> option).</p>
<dt><code>u-law, mu-law</code></p>
<dd> North American telephony standard for logarithmic encoding to 8 bits per sample. A.k.a. &mu;-law. It has a precision equivalent to roughly 14-bit PCM and is sometimes encoded with reversed bit-ordering (see the <code>-X</code> option).</p>
<dt><code>oki-adpcm</code></p>
<dd> OKI (a.k.a. VOX, Dialogic, or Intel) 4-bit ADPCM; it has a precision equivalent to roughly 12-bit PCM. ADPCM is a form of audio compression that has a good compromise between audio quality and encoding/decoding speed.</p>
<dt><code>ima-adpcm</code></p>
<dd> IMA (a.k.a. DVI) 4-bit ADPCM; it has a precision equivalent to roughly 13-bit PCM.</p>
<dt><code>ms-adpcm</code></p>
<dd> Microsoft 4-bit ADPCM; it has a precision equivalent to roughly 14-bit PCM.</p>
<dt><code>gsm-full-rate</code></p>
<dd> GSM is currently used for the vast majority of the world&#8217;s digital wireless telephone calls. It utilises several audio formats with different bit-rates and associated speech quality. SoX has support for GSM&#8217;s original 13kbps `Full Rate&#8217; audio format. It is usually CPU-intensive to work with GSM audio.</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> Encoding names can be abbreviated where this would not be ambiguous; e.g. `unsigned-integer&#8217; can be given as `un&#8217;, but not `u&#8217; (ambiguous with `u-law&#8217;). </p>
<p> For an input file, the most common use for this option is to inform SoX of the encoding of a `raw&#8217; (`headerless&#8217;) audio file (see the examples in <code>-b</code> and <code>-c</code> above). </p>
<p> For an output file, this option can be used (perhaps along with <code>-b</code>) to set the output encoding type For example </p>
<pre>
   sox input.cdda -e float output1.wav
   sox input.cdda -b 64 -e float output2.wav
</pre>
<p> convert raw CD digital audio (16-bit, signed-integer) to floating-point `WAV&#8217; files (single &amp; double precision respectively). </p>
<p> By default (i.e. if this option is not given), the output encoding type will (providing it is supported by the output file type) be set to the input encoding type.</p>
<dt><code>-s</code>/<code>-u</code>/<code>-f</code>/<code>-A</code>/<code>-U</code>/<code>-o</code>/<code>-i</code>/<code>-a</code>/<code>-g</code></p>
<dd> Deprecated aliases for specifying the encoding types <code>signed-integer</code>, <code>unsigned-integer</code>, <code>floating-point</code>, <code>a-law</code>, <code>mu-law</code>, <code>oki-adpcm</code>, <code>ima-adpcm</code>, <code>ms-adpcm</code>, <code>gsm-full-rate</code> respectively (see <code>-e</code> above).</p>
<dt><code>&#8211;no-glob</code></p>
<dd> Specifies that filename `globbing&#8217; (wild-card matching) should not be performed by SoX on the following filename. For example, if the current directory contains the two files `five-seconds.wav&#8217; and `five*.wav&#8217;, then </p>
<pre>
   play --no-glob &quot;five*.wav&quot;
</pre>
<p> can be used to play just the single file `five*.wav&#8217;.</p>
<dt><code>-r, &#8211;rate</code> <i>RATE</i>[<code>k</code>]</p>
<dd> Gives the sample rate in Hz (or kHz if appended with `k&#8217;) of the file. </p>
<p> For an input file, the most common use for this option is to inform SoX of the sample rate of a `raw&#8217; (`headerless&#8217;) audio file (see the examples in <code>-b</code> and <code>-c</code> above). Occasionally it may be useful to use this option with a `headered&#8217; file, in order to override the (presumably incorrect) value in the header &#8211; note that this is only supported with certain file types. For example, if audio was recorded with a sample-rate of say 48k from a source that played back a little, say 1.5%, too slowly, then </p>
<pre>
   sox -r 48720 input.wav output.wav
</pre>
<p> effectively corrects the speed by changing only the file header (but see also the <code>speed</code> effect for the more usual solution to this problem). </p>
<p> For an output file, this option provides a shorthand for specifying that the <code>rate</code> effect should be invoked in order to change (if necessary) the sample rate of the audio signal to the given value. For example, the following two commands are equivalent: </p>
<pre>
   sox input.wav -r 48k output.wav bass -b 24
   sox input.wav        output.wav bass -b 24 rate 48k
</pre>
<p> though the second form is more flexible as it allows <code>rate</code> options to be given, and allows the effects to be ordered arbitrarily.</p>
<dt><code>-t</code>, <code>&#8211;type</code> <i>FILE-TYPE</i></p>
<dd> Gives the type of the audio file. For both input and output files, this option is commonly used to inform SoX of the type a `headerless&#8217; audio file (e.g. raw, mp3) where the actual/desired type cannot be determined from a given filename extension. For example: </p>
<pre>
   another-command | sox -t mp3 - output.wav
   sox input.wav -t raw output.bin
</pre>
<p> It can also be used to override the type implied by an input filename extension, but if overriding with a type that has a header, SoX will exit with an appropriate error message if such a header is not actually present. </p>
<p> See <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7) for a list of supported file types.</dl>
<p> <code>-L</code>, <code>&#8211;endian little</code><br />
 <code>-B</code>, <code>&#8211;endian big</code><br />
 <code>-x</code>, <code>&#8211;endian swap</code> </p>
<dl>
<dt>&nbsp;<wbr></p>
<dd> These options specify whether the byte-order of the audio data is, respectively, `little endian&#8217;, `big endian&#8217;, or the opposite to that of the system on which SoX is being used. Endianness applies only to data encoded as floating-point, or as signed or unsigned integers of 16 or more bits. It is often necessary to specify one of these options for headerless files, and sometimes necessary for (otherwise) self-describing files. A given endian-setting option may be ignored for an input file whose header contains a specific endianness identifier, or for an output file that is actually an audio device. </p>
<p> <code>N.B.</code> Unlike other format characteristics, the endianness (byte, nibble, &amp; bit ordering) of the input file is not automatically used for the output file; so, for example, when the following is run on a little-endian system: </p>
<pre>
   sox -B audio.s16 trimmed.s16 trim 2
</pre>
<p> trimmed.s16 will be created as little-endian; </p>
<pre>
   sox -B audio.s16 -B trimmed.s16 trim 2
</pre>
<p> must be used to preserve big-endianness in the output file. </p>
<p> The <code>-V</code> option can be used to check the selected orderings.</p>
<dt><code>-N</code>, <code>&#8211;reverse-nibbles</code></p>
<dd> Specifies that the nibble ordering (i.e. the 2 halves of a byte) of the samples should be reversed; sometimes useful with ADPCM-based formats. </p>
<p> <code>N.B.</code> See also N.B. in section on <code>-x</code> above.</p>
<dt><code>-X</code>, <code>&#8211;reverse-bits</code></p>
<dd> Specifies that the bit ordering of the samples should be reversed; sometimes useful with a few (mostly headerless) formats. </p>
<p> <code>N.B.</code> See also N.B. in section on <code>-x</code> above.</dl>
<h3>Output File Format Options</h3>
<p> These options apply only to the output file and may precede only the output filename on the command line.</p>
<dl>
<dt><code>&#8211;add-comment </code><i>TEXT</i></p>
<dd> Append a comment in the output file header (where applicable).</p>
<dt><code>&#8211;comment </code><i>TEXT</i></p>
<dd> Specify the comment text to store in the output file header (where applicable). </p>
<p> SoX will provide a default comment if this option (or <code>&#8211;comment-file</code>) is not given. To specify that no comment should be stored in the output file, use <code>&#8211;comment &quot;&quot; .</code></p>
<dt><code>&#8211;comment-file </code><i>FILENAME</i></p>
<dd> Specify a file containing the comment text to store in the output file header (where applicable).</p>
<dt><code>-C</code>, <code>&#8211;compression</code> <i>FACTOR</i></p>
<dd> The compression factor for variably compressing output file formats. If this option is not given then a default compression factor will apply. The compression factor is interpreted differently for different compressing file formats. See the description of the file formats that use this option in <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7) for more information.</dl>
<h2>EFFECTS</h2>
<p> In addition to converting, playing and recording audio files, SoX can be used to invoke a number of audio `effects&#8217;. Multiple effects may be applied by specifying them one after another at the end of the SoX command line, forming an `effects chain&#8217;. Note that applying multiple effects in real-time (i.e. when playing audio) is likely to require a high performance computer. Stopping other applications may alleviate performance issues should they occur. </p>
<p> Some of the SoX effects are primarily intended to be applied to a single instrument or `voice&#8217;. To facilitate this, the <code>remix</code> effect and the global SoX option <code>-M</code> can be used to isolate then recombine tracks from a multi-track recording.</p>
<h3>Multiple Effects Chains</h3>
<p> A single effects chain is made up of one or more effects. Audio from the input runs through the chain until either the end of the input file is reached or an effect in the chain requests to terminate the chain. </p>
<p> SoX supports running multiple effects chains over the input audio. In this case, when one chain indicates it is done processing audio, the audio data is then sent through the next effects chain. This continues until either no more effects chains exist or the input has reached the end of the file. </p>
<p> An effects chain is terminated by placing a <code>:</code> (colon) after an effect. Any following effects are a part of a new effects chain. </p>
<p> It is important to place the effect that will stop the chain as the first effect in the chain. This is because any samples that are buffered by effects to the left of the terminating effect will be discarded. The amount of samples discarded is related to the <code>&#8211;buffer</code> option and it should be kept small, relative to the sample rate, if the terminating effect cannot be first. Further information on stopping effects can be found in the <code>Stopping SoX</code> section. </p>
<p> There are a few pseudo-effects that aid using multiple effects chains. These include <code>newfile</code> which will start writing to a new output file before moving to the next effects chain and <code>restart</code> which will move back to the first effects chain. Pseudo-effects must be specified as the first effect in a chain and as the only effect in a chain (they must have a <code>:</code> before and after they are specified). </p>
<p> The following is an example of multiple effects chains. It will split the input file into multiple files of 30 seconds in length. Each output filename will have unique number in its name as documented in the <code>Output Files</code> section. </p>
<pre>
   sox infile.wav output.wav trim 0 30 : newfile : restart
</pre>
<h3>Common Notation And Parameters</h3>
<p> In the descriptions that follow, brackets [ ] are used to denote parameters that are optional, braces { } to denote those that are both optional and repeatable, and angle brackets &lt; &gt; to denote those that are repeatable but not optional. Where applicable, default values for optional parameters are shown in parenthesis ( ). </p>
<p> The following parameters are used with, and have the same meaning for, several effects:</p>
<dl>
<dt><i>center</i>[<code>k</code>]</p>
<dd> See <i>frequency</i>.</p>
<dt><i>frequency</i>[<code>k</code>]</p>
<dd> A frequency in Hz, or, if appended with `k&#8217;, kHz.</p>
<dt><i>gain</i></p>
<dd> A power gain in dB. Zero gives no gain; less than zero gives an attenuation.</p>
<dt><i>width</i>[<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]</p>
<dd> Used to specify the band-width of a filter. A number of different methods to specify the width are available (though not all for every effect). One of the characters shown may be appended to select the desired method as follows: <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>&nbsp;<wbr></i></td>
<td ALIGN=center><i>Method</i></td>
<td><i>Notes</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>h</code></td>
<td ALIGN=center>Hz</td>
<td>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>k</code></td>
<td ALIGN=center>kHz</td>
<td>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>o</code></td>
<td ALIGN=center>Octaves</td>
<td>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>q</code></td>
<td ALIGN=center>Q-factor</td>
<td>See [2]
</td>
</tr>
</table>
<p></center> </p>
<p> For each effect that uses this parameter, the default method (i.e. if no character is appended) is the one that it listed first in the first line of the effect&#8217;s description.</dl>
<p> To see if SoX has support for an optional effect, enter <code>sox -h</code> and look for its name under the list: `EFFECTS&#8217;.</p>
<h3>Supported Effects</h3>
<p> Note: a categorised list of the effects can be found in the accompanying `README&#8217; file.</p>
<dl>
<dt><code>allpass</code> <i>frequency</i>[<code>k</code>]<i> width</i>[<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]</p>
<dd> Apply a two-pole all-pass filter with central frequency (in Hz) <i>frequency</i>, and filter-width <i>width</i>. An all-pass filter changes the audio&#8217;s frequency to phase relationship without changing its frequency to amplitude relationship. The filter is described in detail in [1]. </p>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>band</code> [<code>-n</code>] <i>center</i>[<code>k</code>] [<i>width</i>[<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]]</p>
<dd> Apply a band-pass filter. The frequency response drops logarithmically around the <i>center</i> frequency. The <i>width</i> parameter gives the slope of the drop. The frequencies at <i>center</i> + <i>width</i> and <i>center</i> &#8211; <i>width</i> will be half of their original amplitudes. <code>band</code> defaults to a mode oriented to pitched audio, i.e. voice, singing, or instrumental music. The <code>-n</code> (for noise) option uses the alternate mode for un-pitched audio (e.g. percussion). <code>Warning:</code> <code>-n</code> introduces a power-gain of about 11dB in the filter, so beware of output clipping. <code>band</code> introduces noise in the shape of the filter, i.e. peaking at the <i>center</i> frequency and settling around it. </p>
<p> This effect supports the <code>&#8211;plot</code> global option. </p>
<p> See also <code>sinc</code> for a bandpass filter with steeper shoulders.</p>
<dt><code>bandpass</code>|<code>bandreject</code> [<code>-c</code>] <i>frequency</i>[<code>k</code>]<i> width</i>[<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]</p>
<dd> Apply a two-pole Butterworth band-pass or band-reject filter with central frequency <i>frequency</i>, and (3dB-point) band-width <i>width</i>. The <code>-c</code> option applies only to <code>bandpass</code> and selects a constant skirt gain (peak gain = Q) instead of the default: constant 0dB peak gain. The filters roll off at 6dB per octave (20dB per decade) and are described in detail in [1]. </p>
<p> These effects support the <code>&#8211;plot</code> global option. </p>
<p> See also <code>sinc</code> for a bandpass filter with steeper shoulders.</p>
<dt><code>bandreject </code><i>frequency</i>[<code>k</code>]<i> width</i>[<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]</p>
<dd> Apply a band-reject filter. See the description of the <code>bandpass</code> effect for details.</p>
<dt><code>bass</code>|<code>treble </code><i>gain</i> [<i>frequency</i>[<code>k</code>] [<i>width</i>[<code>s</code>|<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]]]</p>
<dd> Boost or cut the bass (lower) or treble (upper) frequencies of the audio using a two-pole shelving filter with a response similar to that of a standard hi-fi&#8217;s tone-controls. This is also known as shelving equalisation (EQ). </p>
<p> <i>gain</i> gives the gain at 0 Hz (for <code>bass</code>), or whichever is the lower of &asymp;22 kHz and the Nyquist frequency (for <code>treble</code>). Its useful range is about -20 (for a large cut) to +20 (for a large boost). Beware of <code>Clipping</code> when using a positive <i>gain</i>. </p>
<p> If desired, the filter can be fine-tuned using the following optional parameters: </p>
<p> <i>frequency</i> sets the filter&#8217;s central frequency and so can be used to extend or reduce the frequency range to be boosted or cut. The default value is 100 Hz (for <code>bass</code>) or 3 kHz (for <code>treble</code>). </p>
<p> <i>width</i> determines how steep is the filter&#8217;s shelf transition. In addition to the common width specification methods described above, `slope&#8217; (the default, or if appended with `<code>s</code>&#8216;) may be used. The useful range of `slope&#8217; is about 0.3, for a gentle slope, to 1 (the maximum), for a steep slope; the default value is 0.5. </p>
<p> The filters are described in detail in [1]. </p>
<p> These effects support the <code>&#8211;plot</code> global option. </p>
<p> See also <code>equalizer</code> for a peaking equalisation effect.</p>
<dt><code>bend</code> [<code>-f </code><i>frame-rate</i>(25)] [<code>-o </code><i>over-sample</i>(16)] { <i>delay</i><code>,</code><i>cents</i><code>,</code><i>duration</i> }</p>
<dd> Changes pitch by specified amounts at specified times. Each given triple: <i>delay</i><code>,</code><i>cents</i><code>,</code><i>duration</i> specifies one bend. <i>delay</i> is the amount of time after the start of the audio stream, or the end of the previous bend, at which to start bending the pitch; <i>cents</i> is the number of cents (100 cents = 1 semitone) by which to bend the pitch, and <i>duration</i> the length of time over which the pitch will be bent. </p>
<p> The pitch-bending algorithm utilises the Discrete Fourier Transform (DFT) at a particular frame rate and over-sampling rate. The <code>-f</code> and <code>-o</code> parameters may be used to adjust these parameters and thus control the smoothness of the changes in pitch. </p>
<p> For example, an initial tone is generated, then bent three times, yielding four different notes in total: </p>
<pre>
   play -n synth 2.5 sin 667 gain 1 \
        bend .35,180,.25  .15,740,.53  0,-520,.3
</pre>
<p> Note that the clipping that is produced in this example is deliberate; to remove it, use <code>gain -5</code> in place of <code>gain 1</code>. </p>
<p> See also <code>pitch</code>.</p>
<dt><code>biquad </code><i>b0 b1 b2 a0 a1 a2</i></p>
<dd> Apply a biquad IIR filter with the given coefficients. Where b* and a* are the numerator and denominator coefficients respectively. </p>
<p> See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Digital_biquad_filter">http://en.wikipedia.org/wiki/Digital_biquad_filter</a> (where a0 = 1). </p>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>channels </code><i>CHANNELS</i></p>
<dd> Invoke a simple algorithm to change the number of channels in the audio signal to the given number <i>CHANNELS</i>: mixing if decreasing the number of channels or duplicating if increasing the number of channels. </p>
<p> The <code>channels</code> effect is invoked automatically if SoX&#8217;s <code>-c</code> option specifies a number of channels that is different to that of the input file(s). Alternatively, if this effect is given explicitly, then SoX&#8217;s <code>-c</code> option need not be given. For example, the following two commands are equivalent: </p>
<pre>
   sox input.wav -c 1 output.wav bass -b 24
   sox input.wav      output.wav bass -b 24 channels 1
</pre>
<p> though the second form is more flexible as it allows the effects to be ordered arbitrarily. </p>
<p> See also <code>remix</code> for an effect that allows channels to be mixed/selected arbitrarily.</p>
<dt><code>chorus </code><i>gain-in gain-out</i> &lt;<i>delay decay speed depth </i><code>-s</code>|<code>-t</code>&gt;</p>
<dd> Add a chorus effect to the audio. This can make a single vocal sound like a chorus, but can also be applied to instrumentation. </p>
<p> Chorus resembles an echo effect with a short delay, but whereas with echo the delay is constant, with chorus, it is varied using sinusoidal or triangular modulation. The modulation depth defines the range the modulated delay is played before or after the delay. Hence the delayed sound will sound slower or faster, that is the delayed sound tuned around the original one, like in a chorus where some vocals are slightly off key. See [3] for more discussion of the chorus effect. </p>
<p> Each four-tuple parameter delay/decay/speed/depth gives the delay in milliseconds and the decay (relative to gain-in) with a modulation speed in Hz using depth in milliseconds. The modulation is either sinusoidal (<code>-s</code>) or triangular (<code>-t</code>). Gain-out is the volume of the output. </p>
<p> A typical delay is around 40ms to 60ms; the modulation speed is best near 0.25Hz and the modulation depth around 2ms. For example, a single delay: </p>
<pre>
   play guitar1.wav chorus 0.7 0.9 55 0.4 0.25 2 -t
</pre>
<p> Two delays of the original samples: </p>
<pre>
   play guitar1.wav chorus 0.6 0.9 50 0.4 0.25 2 -t \
         60 0.32 0.4 1.3 -s
</pre>
<p> A fuller sounding chorus (with three additional delays): </p>
<pre>
   play guitar1.wav chorus 0.5 0.9 50 0.4 0.25 2 -t \
         60 0.32 0.4 2.3 -t 40 0.3 0.3 1.3 -s
</pre>
<dt><code>compand </code><i>attack1</i><code>,</code><i>decay1</i>{<code>,</code><i>attack2</i><code>,</code><i>decay2</i>}</p>
<dd> [<i>soft-knee-dB</i><code>:</code>]<i>in-dB1</i>[<code>,</code><i>out-dB1</i>]{<code>,</code><i>in-dB2</i><code>,</code><i>out-dB2</i>}<br />
 [<i>gain</i> [<i>initial-volume-dB</i> [<i>delay</i>]]] </p>
<p> Compand (compress or expand) the dynamic range of the audio. </p>
<p> The <i>attack</i> and <i>decay</i> parameters (in seconds) determine the time over which the instantaneous level of the input signal is averaged to determine its volume; attacks refer to increases in volume and decays refer to decreases. For most situations, the attack time (response to the music getting louder) should be shorter than the decay time because the human ear is more sensitive to sudden loud music than sudden soft music. Where more than one pair of attack/decay parameters are specified, each input channel is companded separately and the number of pairs must agree with the number of input channels. Typical values are <code>0.3,0.8</code> seconds. </p>
<p> The second parameter is a list of points on the compander&#8217;s transfer function specified in dB relative to the maximum possible signal amplitude. The input values must be in a strictly increasing order but the transfer function does not have to be monotonically rising. If omitted, the value of <i>out-dB1</i> defaults to the same value as <i>in-dB1</i>; levels below <i>in-dB1</i> are not companded (but may have gain applied to them). The point <code>0,0</code> is assumed but may be overridden (by <code>0,</code><i>out-dBn</i>). If the list is preceded by a <i>soft-knee-dB</i> value, then the points at where adjacent line segments on the transfer function meet will be rounded by the amount given. Typical values for the transfer function are <code>6:-70,-60,-20</code>. </p>
<p> The third (optional) parameter is an additional gain in dB to be applied at all points on the transfer function and allows easy adjustment of the overall gain. </p>
<p> The fourth (optional) parameter is an initial level to be assumed for each channel when companding starts. This permits the user to supply a nominal level initially, so that, for example, a very large gain is not applied to initial signal levels before the companding action has begun to operate: it is quite probable that in such an event, the output would be severely clipped while the compander gain properly adjusts itself. A typical value (for audio which is initially quiet) is <code>-90</code> dB. </p>
<p> The fifth (optional) parameter is a delay in seconds. The input signal is analysed immediately to control the compander, but it is delayed before being fed to the volume adjuster. Specifying a delay approximately equal to the attack/decay times allows the compander to effectively operate in a `predictive&#8217; rather than a reactive mode. A typical value is <code>0.2</code> seconds. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> The following example might be used to make a piece of music with both quiet and loud passages suitable for listening to in a noisy environment such as a moving vehicle: </p>
<pre>
   sox asz.wav asz-car.wav compand 0.3,1 6:-70,-60,-20 -5 -90 0.2
</pre>
<p> The transfer function (`6:-70,&#8230;&#8217;) says that very soft sounds (below -70dB) will remain unchanged. This will stop the compander from boosting the volume on `silent&#8217; passages such as between movements. However, sounds in the range -60dB to 0dB (maximum volume) will be boosted so that the 60dB dynamic range of the original music will be compressed 3-to-1 into a 20dB range, which is wide enough to enjoy the music but narrow enough to get around the road noise. The `6:&#8217; selects 6dB soft-knee companding. The -5 (dB) output gain is needed to avoid clipping (the number is inexact, and was derived by experimentation). The -90 (dB) for the initial volume will work fine for a clip that starts with near silence, and the delay of 0.2 (seconds) has the effect of causing the compander to react a bit more quickly to sudden volume changes. </p>
<p> In the next example, compand is being used as a noise-gate for when the noise is at a lower level than the signal: </p>
<pre>
   play infile compand .1,.2 -inf,-50.1,-inf,-50,-50 0 -90 .1
</pre>
<p> Here is another noise-gate, this time for when the noise is at a higher level than the signal (making it, in some ways, similar to squelch): </p>
<pre>
   play infile compand .1,.1 -45.1,-45,-inf,0,-inf 45 -90 .1
</pre>
<p> This effect supports the <code>&#8211;plot</code> global option (for the transfer function). </p>
<p> See also <code>mcompand</code> for a multiple-band companding effect.</p>
<dt><code>contrast </code>[<i>enhancement-amount</i>(75)]</p>
<dd> Comparable with compression, this effect modifies an audio signal to make it sound louder. <i>enhancement-amount</i> controls the amount of the enhancement and is a number in the range 0-100. Note that <i>enhancement-amount</i> = 0 still gives a significant contrast enhancement. </p>
<p> See also the <code>compand</code> and <code>mcompand</code> effects.</p>
<dt><code>dcshift </code><i>shift</i> [<i>limitergain</i>]</p>
<dd> Apply a DC shift to the audio. This can be useful to remove a DC offset (caused perhaps by a hardware problem in the recording chain) from the audio. The effect of a DC offset is reduced headroom and hence volume. The <code>stat</code> or <code>stats</code> effect can be used to determine if a signal has a DC offset. </p>
<p> The given <i>dcshift</i> value is a floating point number in the range of &plusmn;2 that indicates the amount to shift the audio (which is in the range of &plusmn;1). </p>
<p> An optional <i>limitergain</i> can be specified as well. It should have a value much less than 1 (e.g. 0.05 or 0.02) and is used only on peaks to prevent clipping. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> An alternative approach to removing a DC offset (albeit with a short delay) is to use the <code>highpass</code> filter effect at a frequency of say 10Hz, as illustrated in the following example: </p>
<pre>
   sox -n dc.wav synth 5 sin %0 50
   sox dc.wav fixed.wav highpass 10
</pre>
<dt><code>deemph</code></p>
<dd> Apply Compact Disc (IEC 60908) de-emphasis (a treble attenuation shelving filter). </p>
<p> Pre-emphasis was applied in the mastering of some CDs issued in the early 1980s. These included many classical music albums, as well as now sought-after issues of albums by The Beatles, Pink Floyd and others. Pre-emphasis should be removed at playback time by a de-emphasis filter in the playback device. However, not all modern CD players have this filter, and very few PC CD drives have it; playing pre-emphasised audio without the correct de-emphasis filter results in audio that sounds harsh and is far from what its creators intended. </p>
<p> With the <code>deemph</code> effect, it is possible to apply the necessary de-emphasis to audio that has been extracted from a pre-emphasised CD, and then either burn the de-emphasised audio to a new CD (which will then play correctly on any CD player), or simply play the correctly de-emphasised audio files on the PC. For example: </p>
<pre>
   sox track1.wav track1-deemph.wav deemph
</pre>
<p> and then burn track1-deemph.wav to CD, or </p>
<pre>
   play track1-deemph.wav
</pre>
<p> or simply </p>
<pre>
   play track1.wav deemph
</pre>
<p> The de-emphasis filter is implemented as a biquad; its maximum deviation from the ideal response is only 0.06dB (up to 20kHz). </p>
<p> This effect supports the <code>&#8211;plot</code> global option. </p>
<p> See also the <code>bass</code> and <code>treble</code> shelving equalisation effects.</p>
<dt><code>delay</code> {<i>length</i>}</p>
<dd> Delay one or more audio channels. <i>length</i> can specify a time or, if appended with an `s&#8217;, a number of samples. Do not specify both time and samples delays in the same command. For example, <code>delay 1.5 0 0.5</code> delays the first channel by 1.5 seconds, the third channel by 0.5 seconds, and leaves the second channel (and any other channels that may be present) un-delayed. The following (one long) command plays a chime sound: </p>
<pre>
   play -n synth -j 3 sin %3 sin %-2 sin %-5 sin %-9 \
        sin %-14 sin %-21 fade h .01 2 1.5 delay \
        1.3 1 .76 .54 .27 remix - fade h 0 2.7 2.5 norm -1
</pre>
<p> and this plays a guitar chord: </p>
<pre>
   play -n synth pl G2 pl B2 pl D3 pl G3 pl D4 pl G4 \
        delay 0 .05 .1 .15 .2 .25 remix - fade 0 4 .1 norm -1
</pre>
<dt><code>dither</code> [<code>-S</code>|<code>-s</code>|<code>-f </code><i>filter</i>] [<code>-a</code>] [<code>-p </code><i>precision</i>]</p>
<dd> Apply dithering to the audio. Dithering deliberately adds a small amount of noise to the signal in order to mask audible quantization effects that can occur if the output sample size is less than 24 bits. With no options, this effect will add triangular (TPDF) white noise. Noise-shaping (only for certain sample rates) can be selected with <code>-s</code>. With the <code>-f</code> option, it is possible to select a particular noise-shaping filter from the following list: lipshitz, f-weighted, modified-e-weighted, improved-e-weighted, gesemann, shibata, low-shibata, high-shibata. Note that most filter types are available only with 44100Hz sample rate. The filter types are distinguished by the following properties: audibility of noise, level of (inaudible, but in some circumstances, otherwise problematic) shaped high frequency noise, and processing speed.<br />
 See <a rel="nofollow" href="http://sox.sourceforge.net/SoX/NoiseShaping">http://sox.sourceforge.net/SoX/NoiseShaping</a> for graphs of the different noise-shaping curves. </p>
<p> The <code>-S</code> option selects a slightly `sloped&#8217; TPDF, biased towards higher frequencies. It can be used at any sampling rate but below ~~22k, plain TPDF is probably better, and above ~~ 37k, noise-shaped is probably better. </p>
<p> The <code>-a</code> option enables a mode where dithering (and noise-shaping if applicable) are automatically enabled only when needed. The most likely use for this is when applying fade in or out to an already dithered file, so that the redithering applies only to the faded portions. However, auto dithering is not fool-proof, so the fades should be carefully checked for any noise modulation; if this occurs, then either re-dither the whole file, or use <code>trim</code>, <code>fade</code>, and concatencate. </p>
<p> The <code>-p</code> option allows overriding the target precision. </p>
<p> If the SoX global option <code>-R</code> option is not given, then the pseudo-random number generator used to generate the white noise will be `reseeded&#8217;, i.e. the generated noise will be different between invocations. </p>
<p> This effect should not be followed by any other effect that affects the audio. </p>
<p> See also the `Dithering&#8217; section above.</p>
<dt><code>downsample</code> [<i><a href="/docs/linux/man/2-factor/">factor</a></i>(2)]</p>
<dd> Downsample the signal by an integer factor: Only the first out of each <i>factor</i> samples is retained, the others are discarded. </p>
<p> No decimation filter is applied. If the input is not a properly bandlimited baseband signal, aliasing will occur. This may be desirable, e.g., for frequency translation. </p>
<p> For a general resampling effect with anti-aliasing, see <code>rate</code>. See also <code>upsample</code>.</p>
<dt><code>earwax</code></p>
<dd> Makes audio easier to listen to on headphones. Adds `cues&#8217; to 44.1kHz stereo (i.e. audio CD format) audio so that when listened to on headphones the stereo image is moved from inside your head (standard for headphones) to outside and in front of the listener (standard for speakers).</p>
<dt><code>echo </code><i>gain-in gain-out</i> &lt;<i>delay decay</i>&gt;</p>
<dd> Add echoing to the audio. Echoes are reflected sound and can occur naturally amongst mountains (and sometimes large buildings) when talking or shouting; digital echo effects emulate this behaviour and are often used to help fill out the sound of a single instrument or vocal. The time difference between the original signal and the reflection is the `delay&#8217; (time), and the loudness of the reflected signal is the `decay&#8217;. Multiple echoes can have different delays and decays. </p>
<p> Each given <i>delay decay</i> pair gives the delay in milliseconds and the decay (relative to gain-in) of that echo. Gain-out is the volume of the output. For example: This will make it sound as if there are twice as many instruments as are actually playing: </p>
<pre>
   play lead.aiff echo 0.8 0.88 60 0.4
</pre>
<p> If the delay is very short, then it sound like a (metallic) robot playing music: </p>
<pre>
   play lead.aiff echo 0.8 0.88 6 0.4
</pre>
<p> A longer delay will sound like an open air concert in the mountains: </p>
<pre>
   play lead.aiff echo 0.8 0.9 1000 0.3
</pre>
<p> One mountain more, and: </p>
<pre>
   play lead.aiff echo 0.8 0.9 1000 0.3 1800 0.25
</pre>
<dt><code>echos </code><i>gain-in gain-out</i> &lt;<i>delay decay</i>&gt;</p>
<dd> Add a sequence of echoes to the audio. Each <i>delay decay</i> pair gives the delay in milliseconds and the decay (relative to gain-in) of that echo. Gain-out is the volume of the output. </p>
<p> Like the echo effect, echos stand for `ECHO in Sequel&#8217;, that is the first echos takes the input, the second the input and the first echos, the third the input and the first and the second echos, &#8230; and so on. Care should be taken using many echos; a single echos has the same effect as a single echo. </p>
<p> The sample will be bounced twice in symmetric echos: </p>
<pre>
   play lead.aiff echos 0.8 0.7 700 0.25 700 0.3
</pre>
<p> The sample will be bounced twice in asymmetric echos: </p>
<pre>
   play lead.aiff echos 0.8 0.7 700 0.25 900 0.3
</pre>
<p> The sample will sound as if played in a garage: </p>
<pre>
   play lead.aiff echos 0.8 0.7 40 0.25 63 0.3
</pre>
<dt><code>equalizer </code><i>frequency</i>[<code>k</code>]<i> width</i>[<code>q</code>|<code>o</code>|<code>h</code>|<code>k</code>] <i>gain</i></p>
<dd> Apply a two-pole peaking equalisation (EQ) filter. With this filter, the signal-level at and around a selected frequency can be increased or decreased, whilst (unlike band-pass and band-reject filters) that at all other frequencies is unchanged. </p>
<p> <i>frequency</i> gives the filter&#8217;s central frequency in Hz, <i>width</i>, the band-width, and <i>gain</i> the required gain or attenuation in dB. Beware of <code>Clipping</code> when using a positive <i>gain</i>. </p>
<p> In order to produce complex equalisation curves, this effect can be given several times, each with a different central frequency. </p>
<p> The filter is described in detail in [1]. </p>
<p> This effect supports the <code>&#8211;plot</code> global option. </p>
<p> See also <code>bass</code> and <code>treble</code> for shelving equalisation effects.</p>
<dt><code>fade</code> [<i>type</i>] <i>fade-in-length</i> [<i>stop-time</i> [<i>fade-out-length</i>]]</p>
<dd> Apply a fade effect to the beginning, end, or both of the audio. </p>
<p> An optional <i>type</i> can be specified to select the shape of the fade curve: <code>q</code> for quarter of a sine wave, <code>h</code> for half a sine wave, <code>t</code> for linear (`triangular&#8217;) slope, <code>l</code> for logarithmic, and <code>p</code> for inverted parabola. The default is logarithmic. </p>
<p> A fade-in starts from the first sample and ramps the signal level from 0 to full volume over <i>fade-in-length</i> seconds. Specify 0 seconds if no fade-in is wanted. </p>
<p> For fade-outs, the audio will be truncated at <i>stop-time</i> and the signal level will be ramped from full volume down to 0 starting at <i>fade-out-length</i> seconds before the <i>stop-time</i>. If <i>fade-out-length</i> is not specified, it defaults to the same value as <i>fade-in-length</i>. No fade-out is performed if <i>stop-time</i> is not specified. If the file length can be determined from the input file header and length-changing effects are not in effect, then <code>0</code> may be specified for <i>stop-time</i> to indicate the usual case of a fade-out that ends at the end of the input audio stream. </p>
<p> All times can be specified in either periods of time or sample counts. To specify time periods use the format hh:mm:ss.frac format. To specify using sample counts, specify the number of samples and append the letter `s&#8217; to the sample count (for example `8000s&#8217;). </p>
<p> See also the <code>splice</code> effect.</p>
<dt><code>fir</code> [<i>coefs-file</i>|<i>coefs</i>]</p>
<dd> Use SoX&#8217;s FFT convolution engine with given FIR filter coefficients. If a single argument is given then this is treated as the name of a file containing the filter coefficients (white-space separated; may contain `#&#8217; comments). If the given filename is `-&#8216;, or if no argument is given, then the coefficients are read from the `standard input&#8217; (stdin); otherwise, coefficients may be given on the command line. Examples: </p>
<pre>
   sox infile outfile fir 0.0195 -0.082 0.234 0.891 -0.145 0.043
</pre>
<pre>
   sox infile outfile fir coefs.txt
</pre>
<p> with coefs.txt containing </p>
<pre>
   # HP filter
   # freq=10000
     1.2311233052619888e-01
    -4.4777096106211783e-01
     5.1031563346705155e-01
    -6.6502926320995331e-02
   ...
</pre>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>flanger</code> [<i>delay depth regen width speed shape phase interp</i>]</p>
<dd> Apply a flanging effect to the audio. See [3] for a detailed description of flanging. </p>
<p> All parameters are optional (right to left). <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>&nbsp;<wbr></i></td>
<td ALIGN=center><i>Range</i></td>
<td ALIGN=center><i>Default</i></td>
<td><i>Description</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>delay</i></td>
<td ALIGN=center>0 &#8211; 30</td>
<td ALIGN=center>0</td>
<td>Base delay in milliseconds.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>depth</i></td>
<td ALIGN=center>0 &#8211; 10</td>
<td ALIGN=center>2</td>
<td>Added swept delay in milliseconds.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>regen</i></td>
<td ALIGN=center>-95 &#8211; 95</td>
<td ALIGN=center>0</td>
<td> Percentage regeneration (delayed signal feedback).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>width</i></td>
<td ALIGN=center>0 &#8211; 100</td>
<td ALIGN=center>71</td>
<td> Percentage of delayed signal mixed with original.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>speed</i></td>
<td ALIGN=center>0.1 &#8211; 10</td>
<td ALIGN=center>0.5</td>
<td>Sweeps per second (Hz).
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>shape</i></td>
<td ALIGN=center>&nbsp;<wbr></td>
<td ALIGN=center>sin</td>
<td>Swept wave shape: <code>sine</code>|<code>triangle</code>.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>phase</i></td>
<td ALIGN=center>0 &#8211; 100</td>
<td ALIGN=center>25</td>
<td> Swept wave percentage phase-shift for multi-channel (e.g. stereo) flange; 0 = 100 = same phase on each channel.
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><i>interp</i></td>
<td ALIGN=center>&nbsp;<wbr></td>
<td ALIGN=center>lin</td>
<td> Digital delay-line interpolation: <code>linear</code>|<code>quadratic</code>.
</td>
</tr>
</table>
<p></center></p>
<dt><code>gain </code>[<code>-e</code>|<code>-B</code>|<code>-b</code>|<code>-r</code>] [<code>-n</code>] [<code>-l</code>|<code>-h</code>] [<i>gain-dB</i>]</p>
<dd> Apply amplification or attenuation to the audio signal, or, in some cases, to some of its channels. Note that use of any of <code>-e</code>, <code>-B</code>, <code>-b</code>, <code>-r</code>, or <code>-n</code> requires temporary file space to store the audio to be processed, so may be unsuitable for use with `streamed&#8217; audio. </p>
<p> Without other options, <i>gain-dB</i> is used to adjust the signal power level by the given number of dB: positive amplifies (beware of Clipping), negative attenuates. With other options, the <i>gain-dB</i> amplification or attenuation is (logically) applied after the processing due to those options. </p>
<p> Given the <code>-e</code> option, the levels of the audio channels of a multi-channel file are `equalised&#8217;, i.e. gain is applied to all channels other than that with the highest peak level, such that all channels attain the same peak level (but, without also giving <code>-n</code>, the audio is not `normalised&#8217;). </p>
<p> The <code>-B</code> (balance) option is similar to <code>-e</code>, but with <code>-B,</code> the RMS level is used instead of the peak level. <code>-B</code> might be used to correct stereo imbalance caused by an imperfect record turntable cartridge. Note that unlike <code>-e</code>, <code>-B</code> might cause some clipping. </p>
<p> <code>-b</code> is similar to <code>-B</code> but has clipping protection, i.e. if necessary to prevent clipping whilst balancing, attenuation is applied to all channels. Note, however, that in conjunction with <code>-n</code>, <code>-B</code> and <code>-b</code> are synonymous. </p>
<p> The <code>-r</code> option is used in conjunction with a prior invocation of <code>gain</code> with the <code>-h</code> option &#8211; see below for details. </p>
<p> The <code>-n</code> option normalises the audio to 0dB FSD; it is often used in conjunction with a negative <i>gain-dB</i> to the effect that the audio is normalised to a given level below 0dB. For example, </p>
<pre>
   sox infile outfile gain -n
</pre>
<p> normalises to 0dB, and </p>
<pre>
   sox infile outfile gain -n -3
</pre>
<p> normalises to -3dB. </p>
<p> The <code>-l</code> option invokes a simple limiter, e.g. </p>
<pre>
   sox infile outfile gain -l 6
</pre>
<p> will apply 6dB of gain but never clip. Note that limiting more than a few dBs more than occasionally (in a piece of audio) is not recommended as it can cause audible distortion. See the <code>compand</code> effect for a more capable limiter. </p>
<p> The <code>-h</code> option is used to apply gain to provide head-room for subsequent processing. For example, with </p>
<pre>
   sox infile outfile gain -h bass +6
</pre>
<p> 6dB of attenuation will be applied prior to the bass boosting effect thus ensuring that it will not clip. Of course, with bass, it is obvious how much headroom will be needed, but with other effects (e.g. rate, dither) it is not always as clear. Another advantage of using <code>gain -h</code> rather than an explicit attenuation, is that if the headroom is not used by subsequent effects, it can be reclaimed with <code>gain -r</code>, for example: </p>
<pre>
   sox infile outfile gain -h bass +6 rate 44100 gain -r
</pre>
<p> The above effects chain guarantees never to clip nor amplify; it attenuates if necessary to prevent clipping, but by only as much as is needed to do so. </p>
<p> Output formatting (dithering and bit-depth reduction) also requires headroom (which cannot be `reclaimed&#8217;), e.g. </p>
<pre>
   sox infile outfile gain -h bass +6 rate 44100 gain -rh dither
</pre>
<p> Here, the second <code>gain</code> invocation, reclaims as much of the headroom as it can from the preceding effects, but retains as much headroom as is needed for subsequent processing. The SoX global option <code>-G</code> can be given to automatically invoke <code>gain -h</code> and <code>gain -r</code>. </p>
<p> See also the <code>norm</code> and <code>vol</code> effects.</p>
<dt><code>highpass</code>|<code>lowpass</code> [<code>-1</code>|<code>-2</code>] <i>frequency</i>[<code>k</code>] [width[<code>q</code>|<code>o</code>|<code>h</code>|<code>k</code>]]</p>
<dd> Apply a high-pass or low-pass filter with 3dB point <i>frequency</i>. The filter can be either single-pole (with <code>-1</code>), or double-pole (the default, or with <code>-2</code>). <i>width</i> applies only to double-pole filters; the default is Q = 0.707 and gives a Butterworth response. The filters roll off at 6dB per pole per octave (20dB per pole per decade). The double-pole filters are described in detail in [1]. </p>
<p> These effects support the <code>&#8211;plot</code> global option. </p>
<p> See also <code>sinc</code> for filters with a steeper roll-off.</p>
<dt><code>hilbert</code> [<code>-n </code><i>taps</i>]</p>
<dd> Apply an odd-tap Hilbert transform filter, phase-shifting the signal by 90 degrees. </p>
<p> This is used in many matrix coding schemes and for analytic signal generation. The process is often written as a multiplication by <i>i</i> (or <i>j</i>), the imaginary unit. </p>
<p> An odd-tap Hilbert transform filter has a bandpass characteristic, attenuating the lowest and highest frequencies. Its bandwidth can be controlled by the number of filter taps, which can be specified with <code>-n</code>. By default, the number of taps is chosen for a cutoff frequency of about 75 Hz. </p>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>ladspa</code> <code>module</code> [<code>plugin</code>] [<code>argument</code>&#8230;]</p>
<dd> Apply a LADSPA [5] (Linux Audio Developer&#8217;s Simple Plugin API) plugin. Despite the name, LADSPA is not Linux-specific, and a wide range of effects is available as LADSPA plugins, such as cmt [6] (the Computer Music Toolkit) and Steve Harris&#8217;s plugin collection [7]. The first argument is the plugin module, the second the name of the plugin (a module can contain more than one plugin) and any other arguments are for the control ports of the plugin. Missing arguments are supplied by default values if possible. Only plugins with at most one audio input and one audio output port can be used. If found, the environment variable LADSPA_PATH will be used as search path for plugins.</p>
<dt><code>loudness</code> [<i>gain</i> [<i>reference</i>]]</p>
<dd> Loudness control &#8211; similar to the <code>gain</code> effect, but provides equalisation for the human auditory system. See <a rel="nofollow" href="http://en.wikipedia.org/wiki/Loudness">http://en.wikipedia.org/wiki/Loudness</a> for a detailed description of loudness. The gain is adjusted by the given <i>gain</i> parameter (usually negative) and the signal equalised according to ISO 226 w.r.t. a reference level of 65dB, though an alternative <i>reference</i> level may be given if the original audio has been equalised for some other optimal level. A default gain of -10dB is used if a <i>gain</i> value is not given. </p>
<p> See also the <code>gain</code> effect.</p>
<dt><code>lowpass</code> [<code>-1</code>|<code>-2</code>] <i>frequency</i>[<code>k</code>] [width[<code>q</code>|<code>o</code>|<code>h</code>|<code>k</code>]]</p>
<dd> Apply a low-pass filter. See the description of the <code>highpass</code> effect for details.</p>
<dt><code>mcompand</code> &quot;<i>attack1</i><code>,</code><i>decay1</i>{<code>,</code><i>attack2</i><code>,</code><i>decay2</i>}</p>
<dd> [<i>soft-knee-dB</i><code>:</code>]<i>in-dB1</i>[<code>,</code><i>out-dB1</i>]{<code>,</code><i>in-dB2</i><code>,</code><i>out-dB2</i>}<br />
 [<i>gain</i> [<i>initial-volume-dB</i> [<i>delay</i>]]]&quot; {<i>crossover-freq</i>[<code>k</code>] &quot;attack1,&#8230;&quot;} </p>
<p> The multi-band compander is similar to the single-band compander but the audio is first divided into bands using Linkwitz-Riley cross-over filters and a separately specifiable compander run on each band. See the <code>compand</code> effect for the definition of its parameters. Compand parameters are specified between double quotes and the crossover frequency for that band is given by <i>crossover-freq</i>; these can be repeated to create multiple bands. </p>
<p> For example, the following (one long) command shows how multi-band companding is typically used in FM radio: </p>
<pre>
   play track1.wav gain -3 sinc 8000- 29 100 mcompand \
        &quot;0.005,0.1 -47,-40,-34,-34,-17,-33&quot; 100 \
        &quot;0.003,0.05 -47,-40,-34,-34,-17,-33&quot; 400 \
        &quot;0.000625,0.0125 -47,-40,-34,-34,-15,-33&quot; 1600 \
        &quot;0.0001,0.025 -47,-40,-34,-34,-31,-31,-0,-30&quot; 6400 \
        &quot;0,0.025 -38,-31,-28,-28,-0,-25&quot; \
        gain 15 highpass 22 highpass 22 sinc -n 255 -b 16 -17500 \
        gain 9 lowpass -1 17801
</pre>
<p> The audio file is played with a simulated FM radio sound (or broadcast signal condition if the lowpass filter at the end is skipped). Note that the pipeline is set up with US-style 75us pre-emphasis. </p>
<p> See also <code>compand</code> for a single-band companding effect.</p>
<dt><code>noiseprof</code> [<i>profile-file</i>]</p>
<dd> Calculate a profile of the audio for use in noise reduction. See the description of the <code>noisered</code> effect for details.</p>
<dt><code>noisered</code> [<i>profile-file</i> [<i>amount</i>]]</p>
<dd> Reduce noise in the audio signal by profiling and filtering. This effect is moderately effective at removing consistent background noise such as hiss or hum. To use it, first run SoX with the <code>noiseprof</code> effect on a section of audio that ideally would contain silence but in fact contains noise &#8211; such sections are typically found at the beginning or the end of a recording. <code>noiseprof</code> will write out a noise profile to <i>profile-file</i>, or to stdout if no <i>profile-file</i> or if `-&#8216; is given. E.g. </p>
<pre>
   sox speech.wav -n trim 0 1.5 noiseprof speech.noise-profile
</pre>
<p> To actually remove the noise, run SoX again, this time with the <code>noisered</code> effect; <code>noisered</code> will reduce noise according to a noise profile (which was generated by <code>noiseprof</code>), from <i>profile-file</i>, or from stdin if no <i>profile-file</i> or if `-&#8216; is given. E.g. </p>
<pre>
   sox speech.wav cleaned.wav noisered speech.noise-profile 0.3
</pre>
<p> How much noise should be removed is specified by <i>amount</i> &#8211; a number between 0 and 1 with a default of 0.5. Higher numbers will remove more noise but present a greater likelihood of removing wanted components of the audio signal. Before replacing an original recording with a noise-reduced version, experiment with different <i>amount</i> values to find the optimal one for your audio; use headphones to check that you are happy with the results, paying particular attention to quieter sections of the audio. </p>
<p> On most systems, the two stages &#8211; profiling and reduction &#8211; can be combined using a pipe, e.g. </p>
<pre>
   sox noisy.wav -n trim 0 1 noiseprof | play noisy.wav noisered
</pre>
<dt><code>norm</code> [<i>dB-level</i>]</p>
<dd> Normalise the audio. <code>norm</code> is just an alias for <code>gain -n</code>; see the <code>gain</code> effect for details.</p>
<dt><code>oops</code></p>
<dd> Out Of Phase Stereo effect. Mixes stereo to twin-mono where each mono channel contains the difference between the left and right stereo channels. This is sometimes known as the `karaoke&#8217; effect as it often has the effect of removing most or all of the vocals from a recording. It is equivalent to <code>remix 1,2i 1,2i</code>.</p>
<dt><code>overdrive</code> [<i>gain</i>(20) [<i>colour</i>(20)]]</p>
<dd> Non linear distortion. The <i>colour</i> parameter controls the amount of even harmonic content in the over-driven output.</p>
<dt><code>pad</code> { <i>length</i>[<code>@</code><i>position</i>] }</p>
<dd> Pad the audio with silence, at the beginning, the end, or any specified points through the audio. Both <i>length</i> and <i>position</i> can specify a time or, if appended with an `s&#8217;, a number of samples. <i>length</i> is the amount of silence to insert and <i>position</i> the position in the input audio stream at which to insert it. Any number of lengths and positions may be specified, provided that a specified position is not less that the previous one. <i>position</i> is optional for the first and last lengths specified and if omitted correspond to the beginning and the end of the audio respectively. For example, <code>pad 1.5 1.5</code> adds 1.5 seconds of silence padding at each end of the audio, whilst <code>pad 4000s@3:00</code> inserts 4000 samples of silence 3 minutes into the audio. If silence is wanted only at the end of the audio, specify either the end position or specify a zero-length pad at the start. </p>
<p> See also <code>delay</code> for an effect that can add silence at the beginning of the audio on a channel-by-channel basis.</p>
<dt><code>phaser </code><i>gain-in gain-out delay decay speed</i> [<code>-s</code>|<code>-t</code>]</p>
<dd> Add a phasing effect to the audio. See [3] for a detailed description of phasing. </p>
<p> delay/decay/speed gives the delay in milliseconds and the decay (relative to gain-in) with a modulation speed in Hz. The modulation is either sinusoidal (<code>-s</code>) &#8211; preferable for multiple instruments, or triangular (<code>-t</code>) &#8211; gives single instruments a sharper phasing effect. The decay should be less than 0.5 to avoid feedback, and usually no less than 0.1. Gain-out is the volume of the output. </p>
<p> For example: </p>
<pre>
   play snare.flac phaser 0.8 0.74 3 0.4 0.5 -t
</pre>
<p> Gentler: </p>
<pre>
   play snare.flac phaser 0.9 0.85 4 0.23 1.3 -s
</pre>
<p> A popular sound: </p>
<pre>
   play snare.flac phaser 0.89 0.85 1 0.24 2 -t
</pre>
<p> More severe: </p>
<pre>
   play snare.flac phaser 0.6 0.66 3 0.6 2 -t
</pre>
<dt><code>pitch </code>[<code>-q</code>] <i>shift</i> [<i>segment</i> [<i>search</i> [<i>overlap</i>]]]</p>
<dd> Change the audio pitch (but not tempo). </p>
<p> <i>shift</i> gives the pitch shift as positive or negative `cents&#8217; (i.e. 100ths of a semitone). See the <code>tempo</code> effect for a description of the other parameters. </p>
<p> See also the <code>bend</code>, <code>speed</code>, and <code>tempo</code> effects.</p>
<dt><code>rate</code> [<code>-q</code>|<code>-l</code>|<code>-m</code>|<code>-h</code>|<code>-v</code>] [override-options] <i>RATE</i>[<code>k</code>]</p>
<dd> Change the audio sampling rate (i.e. resample the audio) to any given <i>RATE</i> (even non-integer if this is supported by the output file format) using a quality level defined as follows: <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>&nbsp;<wbr></i></td>
<td ALIGN=center><i>Quality&nbsp;<wbr>&nbsp;<wbr></i></td>
<td ALIGN=center><i> Band-width &nbsp;<wbr>&nbsp;<wbr></i></td>
<td ALIGN=center><i>Rej dB</i></td>
<td><i> Typical Use </i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>-q</code></td>
<td ALIGN=center> quick </td>
<td ALIGN=center>n/a</td>
<td ALIGN=center> ~=30 @ &nbsp;<wbr>Fs/4 </td>
<td> playback on ancient hardware
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>-l</code></td>
<td ALIGN=center>low</td>
<td ALIGN=center>80%</td>
<td ALIGN=center>100</td>
<td> playback on old hardware
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>-m</code></td>
<td ALIGN=center>medium</td>
<td ALIGN=center>95%</td>
<td ALIGN=center>100</td>
<td> audio playback
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>-h</code></td>
<td ALIGN=center>high</td>
<td ALIGN=center>95%</td>
<td ALIGN=center>125</td>
<td> 16-bit mastering (use with dither)
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>-v</code></td>
<td ALIGN=center> very high </td>
<td ALIGN=center>95%</td>
<td ALIGN=center>175</td>
<td>24-bit mastering
</td>
</tr>
</table>
<p></center> </p>
<p> where <i>Band-width</i> is the percentage of the audio frequency band that is preserved and <i>Rej dB</i> is the level of noise rejection. Increasing levels of resampling quality come at the expense of increasing amounts of time to process the audio. If no quality option is given, the quality level used is `high&#8217; (but see `Playing &amp; Recording Audio&#8217; above regarding playback). </p>
<p> The `quick&#8217; algorithm uses cubic interpolation; all others use band-limited interpolation. By default, all algorithms have a `linear&#8217; phase response; for `medium&#8217;, `high&#8217; and `very high&#8217;, the phase response is configurable (see below). </p>
<p> The <code>rate</code> effect is invoked automatically if SoX&#8217;s <code>-r</code> option specifies a rate that is different to that of the input file(s). Alternatively, if this effect is given explicitly, then SoX&#8217;s <code>-r</code> option need not be given. For example, the following two commands are equivalent: </p>
<pre>
   sox input.wav -r 48k output.wav bass -b 24
   sox input.wav        output.wav bass -b 24 rate 48k
</pre>
<p> though the second command is more flexible as it allows <code>rate</code> options to be given, and allows the effects to be ordered arbitrarily. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> Warning: technically detailed discussion follows. </p>
<p> The simple quality selection described above provides settings that satisfy the needs of the vast majority of resampling tasks. Occasionally, however, it may be desirable to fine-tune the resampler&#8217;s filter response; this can be achieved using <i>override options</i>, as detailed in the following table: <center></p>
<table>
<tr VALIGN=top>
<td><code>-M/-I/-L</code></td>
<td>Phase response = minimum/intermediate/linear
</td>
</tr>
<tr VALIGN=top>
<td><code>-s</code></td>
<td>Steep filter (band-width = 99%)
</td>
</tr>
<tr VALIGN=top>
<td><code>-a</code></td>
<td>Allow aliasing/imaging above the pass-band
</td>
</tr>
<tr VALIGN=top>
<td><code>-b 74-99.7</code></td>
<td>Any band-width %
</td>
</tr>
<tr VALIGN=top>
<td><code>-p 0-100</code></td>
<td> Any phase response (0 = minimum, 25 = intermediate, 50 = linear, 100 = maximum)
</td>
</tr>
</table>
<p></center> </p>
<p> N.B. Override options cannot be used with the `quick&#8217; or `low&#8217; quality algorithms. </p>
<p> All resamplers use filters that can sometimes create `echo&#8217; (a.k.a. `ringing&#8217;) artefacts with transient signals such as those that occur with `finger snaps&#8217; or other highly percussive sounds. Such artefacts are much more noticeable to the human ear if they occur before the transient (`pre-echo&#8217;) than if they occur after it (`post-echo&#8217;). Note that frequency of any such artefacts is related to the smaller of the original and new sampling rates but that if this is at least 44.1kHz, then the artefacts will lie outside the range of human hearing. </p>
<p> A phase response setting may be used to control the distribution of any transient echo between `pre&#8217; and `post&#8217;: with minimum phase, there is no pre-echo but the longest post-echo; with linear phase, pre and post echo are in equal amounts (in signal terms, but not audibility terms); the intermediate phase setting attempts to find the best compromise by selecting a small length (and level) of pre-echo and a medium lengthed post-echo. </p>
<p> Minimum, intermediate, or linear phase response is selected using the <code>-M</code>, <code>-I</code>, or <code>-L</code> option; a custom phase response can be created with the <code>-p</code> option. Note that phase responses between `linear&#8217; and `maximum&#8217; (greater than 50) are rarely useful. </p>
<p> A resampler&#8217;s band-width setting determines how much of the frequency content of the original signal (w.r.t. the original sample rate when up-sampling, or the new sample rate when down-sampling) is preserved during conversion. The term `pass-band&#8217; is used to refer to all frequencies up to the band-width point (e.g. for 44.1kHz sampling rate, and a resampling band-width of 95%, the pass-band represents frequencies from 0Hz (D.C.) to circa 21kHz). Increasing the resampler&#8217;s band-width results in a slower conversion and can increase transient echo artefacts (and vice versa). </p>
<p> The <code>-s</code> `steep filter&#8217; option changes resampling band-width from the default 95% (based on the 3dB point), to 99%. The <code>-b</code> option allows the band-width to be set to any value in the range 74-99.7 %, but note that band-width values greater than 99% are not recommended for normal use as they can cause excessive transient echo. </p>
<p> If the <code>-a</code> option is given, then aliasing/imaging above the pass-band is allowed. For example, with 44.1kHz sampling rate, and a resampling band-width of 95%, this means that frequency content above 21kHz can be distorted; however, since this is above the pass-band (i.e. above the highest frequency of interest/audibility), this may not be a problem. The benefits of allowing aliasing/imaging are reduced processing time, and reduced (by almost half) transient echo artefacts. Note that if this option is given, then the minimum band-width allowable with <code>-b</code> increases to 85%. </p>
<p> Examples: </p>
<pre>
   sox input.wav -b 16 output.wav rate -s -a 44100 dither -s
</pre>
<p> default (high) quality resampling; overrides: steep filter, allow aliasing; to 44.1kHz sample rate; noise-shaped dither to 16-bit WAV file. </p>
<pre>
   sox input.wav -b 24 output.aiff rate -v -I -b 90 48k
</pre>
<p> very high quality resampling; overrides: intermediate phase, band-width 90%; to 48k sample rate; store output to 24-bit AIFF file. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> The <code>pitch</code> and <code>speed</code> effects use the <code>rate</code> effect at their core.</p>
<dt><code>remix</code> [<code>-a</code>|<code>-m</code>|<code>-p</code>] &lt;<i>out-spec</i>&gt;</p>
<dd> <i>out-spec</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>= <i>in-spec</i>{<code>,</code><i>in-spec</i>} | <code>0</code></p>
<p> <i>in-spec</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>= [<i>in-chan</i>][<code>&#8211;</code>[<i>in-chan2</i>]][<i>vol-spec</i>]</p>
<p> <i>vol-spec</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>= <code>p</code>|<code>i</code>|<code>v</code>[<i>volume</i>]</p>
<p> Select and mix input audio channels into output audio channels. Each output channel is specified, in turn, by a given <i>out-spec</i>: a list of contributing input channels and volume specifications. </p>
<p> Note that this effect operates on the audio <i>channels</i> within the SoX effects processing chain; it should not be confused with the <code>-m</code> global option (where multiple <i>files</i> are mix-combined before entering the effects chain). </p>
<p> An <i>out-spec</i> contains comma-separated input channel-numbers and hyphen-delimited channel-number ranges; alternatively, <code>0</code> may be given to create a silent output channel. For example, </p>
<pre>
   sox input.wav output.wav remix 6 7 8 0
</pre>
<p> creates an output file with four channels, where channels 1, 2, and 3 are copies of channels 6, 7, and 8 in the input file, and channel 4 is silent. Whereas </p>
<pre>
   sox input.wav output.wav remix 1-3,7 3
</pre>
<p> creates a (somewhat bizarre) stereo output file where the left channel is a mix-down of input channels 1, 2, 3, and 7, and the right channel is a copy of input channel 3. </p>
<p> Where a range of channels is specified, the channel numbers to the left and right of the hyphen are optional and default to 1 and to the number of input channels respectively. Thus </p>
<pre>
   sox input.wav output.wav remix -
</pre>
<p> performs a mix-down of all input channels to mono. </p>
<p> By default, where an output channel is mixed from multiple (n) input channels, each input channel will be scaled by a factor of &sup1;/<font SIZE="-2">n</font>. Custom mixing volumes can be set by following a given input channel or range of input channels with a <i>vol-spec</i> (volume specification). This is one of the letters <code>p</code>, <code>i</code>, or <code>v</code>, followed by a volume number, the meaning of which depends on the given letter and is defined as follows: <center></p>
<table>
<tr VALIGN=top>
<td><i>Letter</i></td>
<td><i>Volume number</i></td>
<td><i>Notes</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>p</td>
<td>power adjust in dB</td>
<td>0 = no change
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>i</td>
<td>power adjust in dB</td>
<td> As `p&#8217;, but invert the audio
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>v</td>
<td>voltage multiplier</td>
<td> 1 = no change, 0.5 ~= 6dB attenuation, 2 ~= 6dB gain, -1 = invert
</td>
</tr>
</table>
<p></center> </p>
<p> If an <i>out-spec</i> includes at least one <i>vol-spec</i> then, by default, &sup1;/<font SIZE="-2">n</font> scaling is not applied to any other channels in the same out-spec (though may be in other out-specs). The -a (automatic) option however, can be given to retain the automatic scaling in this case. For example, </p>
<pre>
   sox input.wav output.wav remix 1,2 3,4v0.8
</pre>
<p> results in channel level multipliers of 0.5,0.5 1,0.8, whereas </p>
<pre>
   sox input.wav output.wav remix -a 1,2 3,4v0.8
</pre>
<p> results in channel level multipliers of 0.5,0.5 0.5,0.8. </p>
<p> The -m (manual) option disables all automatic volume adjustments, so </p>
<pre>
   sox input.wav output.wav remix -m 1,2 3,4v0.8
</pre>
<p> results in channel level multipliers of 1,1 1,0.8. </p>
<p> The volume number is optional and omitting it corresponds to no volume change; however, the only case in which this is useful is in conjunction with <code>i</code>. For example, if <i>input.wav</i> is stereo, then </p>
<pre>
   sox input.wav output.wav remix 1,2i
</pre>
<p> is a mono equivalent of the <code>oops</code> effect. </p>
<p> If the <code>-p</code> option is given, then any automatic &sup1;/<font SIZE="-2">n</font> scaling is replaced by &sup1;/<font SIZE="-2">srn</font> (`power&#8217;) scaling; this gives a louder mix but one that might occasionally clip. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> One use of the <code>remix</code> effect is to split an audio file into a set of files, each containing one of the constituent channels (in order to perform subsequent processing on individual audio channels). Where more than a few channels are involved, a script such as the following (Bourne shell script) is useful: </p>
<p>#!/ bin / sh<br />
chans =`soxi &#8211; c &#8220;$1&#8243;` while[$chans &#8211; ge 1];<br />
do<br />
chans0 =`printf % 02i $chans` #2 digits hence up to 99 chans<br />
                      out =`echo &#8220;$1&#8221; | sed &#8220;s/\(.*\)\.\(.*\)/\1-$chans0.\2/&#8221;` sox &#8220;$1&#8221;<br />
                                                                                   &#8220;$out&#8221; remix $chans<br />
                                                                                       chans =`expr $chans &#8211; 1` done<br />
 If a file <i>input.wav</i> containing six audio channels were given, the script would produce six output files: <i>input-01.wav</i>, <i>input-02.wav</i>, &#8230;, <i>input-06.wav</i>. </p>
<p> See also the <code>swap</code> effect.</p>
<dt><code>repeat</code> [<i>count</i> (1)]</p>
<dd> Repeat the entire audio <i>count</i> times, or once if <i>count</i> is not given. Requires temporary file space to store the audio to be repeated. Note that repeating once yields two copies: the original audio and the repeated audio.</p>
<dt><code>reverb</code> [<code>-w</code>|<code>&#8211;wet-only</code>] [<i>reverberance</i> (50%) [<i>HF-damping</i> (50%)</p>
<dd> [<i>room-scale</i> (100%) [<i>stereo-depth</i> (100%)<br />
 [<i>pre-delay</i> (0ms) [<i>wet-gain</i> (0dB)]]]]]] </p>
<p> Add reverberation to the audio using the `freeverb&#8217; algorithm. A reverberation effect is sometimes desirable for concert halls that are too small or contain so many people that the hall&#8217;s natural reverberance is diminished. Applying a small amount of stereo reverb to a (dry) mono signal will usually make it sound more natural. See [3] for a detailed description of reverberation. </p>
<p> Note that this effect increases both the volume and the length of the audio, so to prevent clipping in these domains, a typical invocation might be: </p>
<pre>
   play dry.wav gain -3 pad 0 3 reverb
</pre>
<p> The <code>-w</code> option can be given to select only the `wet&#8217; signal, thus allowing it to be processed further, independently of the `dry&#8217; signal. E.g. </p>
<pre>
   play -m voice.wav &quot;|sox voice.wav -p reverse reverb -w reverse&quot;
</pre>
<p> for a reverse reverb effect.</p>
<dt><code>reverse</code></p>
<dd> Reverse the audio completely. Requires temporary file space to store the audio to be reversed.</p>
<dt><code>riaa</code></p>
<dd> Apply RIAA vinyl playback equalisation. The sampling rate must be one of: 44.1, 48, 88.2, 96 kHz. </p>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>silence </code>[<code>-l</code>] <i>above-periods</i> [<i>duration threshold</i>[<code>d</code>|<code>%</code>]</p>
<dd> [<i>below-periods duration threshold</i>[<code>d</code>|<code>%</code>]] </p>
<p> Removes silence from the beginning, middle, or end of the audio. `Silence&#8217; is determined by a specified threshold. </p>
<p> The <i>above-periods</i> value is used to indicate if audio should be trimmed at the beginning of the audio. A value of zero indicates no silence should be trimmed from the beginning. When specifying an non-zero <i>above-periods</i>, it trims audio up until it finds non-silence. Normally, when trimming silence from beginning of audio the <i>above-periods</i> will be 1 but it can be increased to higher values to trim all audio up to a specific count of non-silence periods. For example, if you had an audio file with two songs that each contained 2 seconds of silence before the song, you could specify an <i>above-period</i> of 2 to strip out both silence periods and the first song. </p>
<p> When <i>above-periods</i> is non-zero, you must also specify a <i>duration</i> and <i>threshold</i>. <i>Duration</i> indications the amount of time that non-silence must be detected before it stops trimming audio. By increasing the duration, burst of noise can be treated as silence and trimmed off. </p>
<p> <i>Threshold</i> is used to indicate what sample value you should treat as silence. For digital audio, a value of 0 may be fine but for audio recorded from analog, you may wish to increase the value to account for background noise. </p>
<p> When optionally trimming silence from the end of the audio, you specify a <i>below-periods</i> count. In this case, <i>below-period</i> means to remove all audio after silence is detected. Normally, this will be a value 1 of but it can be increased to skip over periods of silence that are wanted. For example, if you have a song with 2 seconds of silence in the middle and 2 second at the end, you could set below-period to a value of 2 to skip over the silence in the middle of the audio. </p>
<p> For <i>below-periods</i>, <i>duration</i> specifies a period of silence that must exist before audio is not copied any more. By specifying a higher duration, silence that is wanted can be left in the audio. For example, if you have a song with an expected 1 second of silence in the middle and 2 seconds of silence at the end, a duration of 2 seconds could be used to skip over the middle silence. </p>
<p> Unfortunately, you must know the length of the silence at the end of your audio file to trim off silence reliably. A work around is to use the <code>silence</code> effect in combination with the <code>reverse</code> effect. By first reversing the audio, you can use the <i>above-periods</i> to reliably trim all audio from what looks like the front of the file. Then reverse the file again to get back to normal. </p>
<p> To remove silence from the middle of a file, specify a <i>below-periods</i> that is negative. This value is then treated as a positive value and is also used to indicate the effect should restart processing as specified by the <i>above-periods</i>, making it suitable for removing periods of silence in the middle of the audio. </p>
<p> The option <code>-l</code> indicates that <i>below-periods</i> <i>duration</i> length of audio should be left intact at the beginning of each period of silence. For example, if you want to remove long pauses between words but do not want to remove the pauses completely. </p>
<p> The <i>period</i> counts are in units of samples. <i>Duration</i> counts may be in the format of hh:mm:ss.frac, or the exact count of samples. <i>Threshold</i> numbers may be suffixed with <code>d</code> to indicate the value is in decibels, or <code>%</code> to indicate a percentage of maximum value of the sample value (<code>0%</code> specifies pure digital silence). </p>
<p> The following example shows how this effect can be used to start a recording that does not contain the delay at the start which usually occurs between `pressing the record button&#8217; and the start of the performance: </p>
<pre>
   rec <i>parameters filename other-effects</i> silence 1 5 2%
</pre>
<dt><code>sinc</code> [<code>-a</code><i> att</i>|<code>-b</code><i> beta</i>] [<code>-p</code><i> phase</i>|<code>-M</code>|<code>-I</code>|<code>-L</code>] :[<code>-t</code><i> tbw</i>|<code>-n</code><i> taps</i>] [<i>freqHP</i>]:[<code>&#8211;</code><i>freqLP</i> [<code>-t</code> tbw|<code>-n</code> taps]]</p>
<dd> Apply a sinc kaiser-windowed low-pass, high-pass, band-pass, or band-reject filter to the signal. The <i>freqHP</i> and <i>freqLP</i> parameters give the frequencies of the 6dB points of a high-pass and low-pass filter that may be invoked individually, or together. If both are given, then <i>freqHP</i> less than <i>freqLP</i> creates a band-pass filter, <i>freqHP</i> greater than <i>freqLP</i> creates a band-reject filter. For example, the invocations </p>
<pre>
   sinc 3k
   sinc -4k
   sinc 3k-4k
   sinc 4k-3k
</pre>
<p> create a high-pass, low-pass, band-pass, and band-reject filter respectively. </p>
<p> The default stop-band attenuation of 120dB can be overridden with <code>-a</code>; alternatively, the kaiser-window `beta&#8217; parameter can be given directly with <code>-b</code>. </p>
<p> The default transition band-width of 5% of the total band can be overridden with <code>-t</code> (and <i>tbw</i> in Hertz); alternatively, the number of filter taps can be given directly with <code>-n</code>. </p>
<p> If both <i>freqHP</i> and <i>freqLP</i> are given, then a <code>-t</code> or <code>-n</code> option given to the left of the frequencies applies to both frequencies; one of these options given to the right of the frequencies applies only to <i>freqLP</i>. </p>
<p> The <code>-p</code>, <code>-M</code>, <code>-I</code>, and <code>-L</code> options control the filter&#8217;s phase response; see the <code>rate</code> effect for details. </p>
<p> This effect supports the <code>&#8211;plot</code> global option.</p>
<dt><code>spectrogram </code>[<i>options</i>]</p>
<dd> Create a spectrogram of the audio; the audio is passed unmodified through the SoX processing chain. This effect is optional &#8211; type <code>sox &#8211;help</code> and check the list of supported effects to see if it has been included. </p>
<p> The spectrogram is rendered in a Portable Network Graphic (PNG) file, and shows time in the X-axis, frequency in the Y-axis, and audio signal magnitude in the Z-axis. Z-axis values are represented by the colour (or optionally the intensity) of the pixels in the X-Y plane. If the audio signal contains multiple channels then these are shown from top to bottom starting from channel 1 (which is the left channel for stereo audio). </p>
<p> For example, if `my.wav&#8217; is a stereo file, then with </p>
<pre>
   sox my.wav -n spectrogram
</pre>
<p> a spectrogram of the entire file will be created in the file `spectrogram.png&#8217;. More often though, analysis of a smaller portion of the audio is required; e.g. with </p>
<pre>
   sox my.wav -n remix 2 trim 20 30 spectrogram
</pre>
<p> the spectrogram shows information only from the second (right) channel, and of thirty seconds of audio starting from twenty seconds in. To analyse a small portion of the frequency domain, the <code>rate</code> effect may be used, e.g. </p>
<pre>
   sox my.wav -n rate 6k spectrogram
</pre>
<p> allows detailed analysis of frequencies up to 3kHz (half the sampling rate) i.e. where the human auditory system is most sensitive. With </p>
<pre>
   sox my.wav -n trim 0 10 spectrogram -x 600 -y 200 -z 100
</pre>
<p> the given options control the size of the spectrogram&#8217;s X, Y &amp; Z axes (in this case, the spectrogram area of the produced image will be 600 by 200 pixels in size and the Z-axis range will be 100 dB). Note that the produced image includes axes legends etc. and so will be a little larger than the specified spectrogram size. In this example: </p>
<pre>
   sox -n -n synth 6 tri 10k:14k spectrogram -z 100 -w kaiser
</pre>
<p> an analysis `window&#8217; with high dynamic range is selected to best display the spectrogram of a swept triangular wave. For a smilar example, append the following to the `chime&#8217; command in the description of the <code>delay</code> effect (above): </p>
<pre>
   rate 2k spectrogram -X 200 -Z -10 -w kaiser
</pre>
<p> Options are also avaliable to control the appearance (colour-set, brightness, contrast, etc.) and filename of the spectrogram; e.g. with </p>
<pre>
   sox my.wav -n spectrogram -m -l -o print.png
</pre>
<p> a spectrogram is created suitable for printing on a `black and white&#8217; printer. </p>
<p> <i>Options:</i></p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-x&nbsp;<wbr></code><i>num</i></p>
<dd> Change the (maximum) width (X-axis) of the spectrogram from its default value of 800 pixels to a given number between 100 and 200000. See also <code>-X</code> and <code>-d</code>.</p>
<dt><code>-X&nbsp;<wbr></code><i>num</i></p>
<dd> X-axis pixels/second; the default is auto-calculated to fit the given or known audio duration to the X-axis size, or 100 otherwise. If given in conjunction with <code>-d</code>, this option affects the width of the spectrogram; otherwise, it affects the duration of the spectrogram. <i>num</i> can be from 1 (low time resolution) to 5000 (high time resolution) and need not be an integer. SoX may make a slight adjustment to the given number for processing quantisation reasons; if so, SoX will report the actual number used (viewable when the SoX global option <code>-V</code> is in effect). See also <code>-x</code> and <code>-d</code>.</p>
<dt><code>-y&nbsp;<wbr></code><i>num</i></p>
<dd> Sets the Y-axis size in pixels (per channel); this is the number of frequency `bins&#8217; used in the Fourier analysis that produces the spectrogram. N.B. it can be slow to produce the spectrogram if this number is not one more than a power of two (e.g. 129). By default the Y-axis size is chosen automatically (depending on the number of channels). See <code>-Y</code> for alternative way of setting spectrogram height.</p>
<dt><code>-Y&nbsp;<wbr></code><i>num</i></p>
<dd> Sets the target total height of the spectrogram(s). The default value is 550 pixels. Using this option (and by default), SoX will choose a height for individual spectrogram channels that is one more than a power of two, so the actual total height may fall short of the given number. However, there is also a minimum height per channel so if there are many channels, the number may be exceeded. See <code>-y</code> for alternative way of setting spectrogram height.</p>
<dt><code>-z&nbsp;<wbr></code><i>num</i></p>
<dd> Z-axis (colour) range in dB, default 120. This sets the dynamic-range of the spectrogram to be &#8211;<i>num</i>&nbsp;<wbr>dBFS to 0 dBFS. <i>Num</i> may range from 20 to 180. Decreasing dynamic-range effectively increases the `contrast&#8217; of the spectrogram display, and vice versa.</p>
<dt><code>-Z&nbsp;<wbr></code><i>num</i></p>
<dd> Sets the upper limit of the Z-axis in dBFS. A negative <i>num</i> effectively increases the `brightness&#8217; of the spectrogram display, and vice versa.</p>
<dt><code>-q&nbsp;<wbr></code><i>num</i></p>
<dd> Sets the Z-axis quantisation, i.e. the number of different colours (or intensities) in which to render Z-axis values. A small number (e.g. 4) will give a `poster&#8217;-like effect making it easier to discern magnitude bands of similar level. Small numbers also usually result in small PNG files. The number given specifies the number of colours to use inside the Z-axis range; two colours are reserved to represent out-of-range values.</p>
<dt><code>-w&nbsp;<wbr></code><i>name</i></p>
<dd> Window: Hann (default), Hamming, Bartlett, Rectangular or Kaiser. The spectrogram is produced using the Discrete Fourier Transform (DFT) algorithm. A significant parameter to this algorithm is the choice of `window function&#8217;. By default, SoX uses the Hann window which has good all-round frequency-resolution and dynamic-range properties. For better frequency resolution (but lower dynamic-range), select a Hamming window; for higher dynamic-range (but poorer frequency-resolution), select a Kaiser window. Bartlett and Rectangular windows are also available.</p>
<dt><code>-W&nbsp;<wbr></code><i>num</i></p>
<dd> Window adjustment parameter. This can be used to make small adjustments to the Kaiser window shape. A positive number (up to ten) increases its dynamic range, a negative number decreases it.</p>
<dt><code>-s</code></p>
<dd> Allow slack overlapping of DFT windows. This can, in some cases, increase image sharpness and give greater adherence to the <code>-x</code> value, but at the expense of a little spectral loss.</p>
<dt><code>-m</code></p>
<dd> Creates a monochrome spectrogram (the default is colour).</p>
<dt><code>-h</code></p>
<dd> Selects a high-colour palette &#8211; less visually pleasing than the default colour palette, but it may make it easier to differentiate different levels. If this option is used in conjunction with <code>-m</code>, the result will be a hybrid monochrome/colour palette.</p>
<dt><code>-p&nbsp;<wbr></code><i>num</i></p>
<dd> Permute the colours in a colour or hybrid palette. The <i>num</i> parameter, from 1 (the default) to 6, selects the permutation.</p>
<dt><code>-l</code></p>
<dd> Creates a `printer friendly&#8217; spectrogram with a light background (the default has a dark background).</p>
<dt><code>-a</code></p>
<dd> Suppress the display of the axis lines. This is sometimes useful in helping to discern artefacts at the spectrogram edges.</p>
<dt><code>-r</code></p>
<dd> Raw spectrogram: suppress the display of axes and legends.</p>
<dt><code>-A</code></p>
<dd> Selects an alternative, fixed colour-set. This is provided only for compatibility with spectrograms produced by another package. It should not normally be used as it has some problems, not least, a lack of differentiation at the bottom end which results in masking of low-level artefacts.</p>
<dt><code>-t&nbsp;<wbr></code><i>text</i></p>
<dd> Set the image title &#8211; text to display above the spectrogram.</p>
<dt><code>-c&nbsp;<wbr></code><i>text</i></p>
<dd> Set (or clear) the image comment &#8211; text to display below and to the left of the spectrogram.</p>
<dt><code>-o&nbsp;<wbr></code><i>text</i></p>
<dd> Name of the spectrogram output PNG file, default `spectrogram.png&#8217;.</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> <i>Advanced Options:</i><br />
 In order to process a smaller section of audio without affecting other effects or the output signal (unlike when the <code>trim</code> effect is used), the following options may be used.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-d&nbsp;<wbr></code><i>duration</i></p>
<dd> This option sets the X-axis resolution such that audio with the given <i>duration</i> ([[HH:]MM:]SS) fits the selected (or default) X-axis width. For example, </p>
<pre>
   sox input.mp3 output.wav -n spectrogram -d 1:00 stats
</pre>
<p> creates a spectrogram showing the first minute of the audio, whilst </p>
<p> the <code>stats</code> effect is applied to the entire audio signal. </p>
<p> See also <code>-X</code> for an alternative way of setting the X-axis resolution.</p>
<dt><code>-S&nbsp;<wbr></code><i>time</i></p>
<dd> Start the spectrogram at the given point in the audio stream. For example </p>
<pre>
   sox input.aiff output.wav spectrogram -S 1:00
</pre>
<p> creates a spectrogram showing all but the first minute of the audio (the output file however, receives the entire audio stream).</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> For the ability to perform off-line processing of spectral data, see the <code>stat</code> effect.</p>
<dt><code>speed </code><i>factor</i>[<code>c</code>]</p>
<dd> Adjust the audio speed (pitch and tempo together). <i>factor</i> is either the ratio of the new speed to the old speed: greater than 1 speeds up, less than 1 slows down, or, if appended with the letter `c&#8217;, the number of cents (i.e. 100ths of a semitone) by which the pitch (and tempo) should be adjusted: greater than 0 increases, less than 0 decreases. </p>
<p> Technically, the speed effect only changes the sample rate information, leaving the samples themselves untouched. The <code>rate</code> effect is invoked automatically to resample to the output sample rate, using its default quality/speed. For higher quality or higher speed resampling, in addition to the <code>speed</code> effect, specify the <code>rate</code> effect with the desired quality option. </p>
<p> See also the <code>bend</code>, <code>pitch</code>, and <code>tempo</code> effects.</p>
<dt><code>splice </code> [<code>-h</code>|<code>-t</code>|<code>-q</code>] { <i>position</i>[<code>,</code><i>excess</i>[<code>,</code><i>leeway</i>]] }</p>
<dd> Splice together audio sections. This effect provides two things over simple audio concatenation: a (usually short) cross-fade is applied at the join, and a wave similarity comparison is made to help determine the best place at which to make the join. </p>
<p> One of the options <code>-h</code>, <code>-t</code>, or <code>-q</code> may be given to select the fade envelope as half-cosine wave (the default), triangular (a.k.a. linear), or quarter-cosine wave respectively. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>Type</i></td>
<td><i>Audio</i></td>
<td><i>Fade level</i></td>
<td><i>Transitions</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>t</code></td>
<td>correlated</td>
<td>constant gain</td>
<td>abrupt
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>h</code></td>
<td>correlated</td>
<td>constant gain</td>
<td>smooth
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center><code>q</code></td>
<td>uncorrelated</td>
<td>constant power</td>
<td>smooth
</td>
</tr>
</table>
<p></center> </p>
<p> To perform a splice, first use the <code>trim</code> effect to select the audio sections to be joined together. As when performing a tape splice, the end of the section to be spliced onto should be trimmed with a small <i>excess</i> (default 0.005 seconds) of audio after the ideal joining point. The beginning of the audio section to splice on should be trimmed with the same <i>excess</i> (before the ideal joining point), plus an additional <i>leeway</i> (default 0.005 seconds). SoX should then be invoked with the two audio sections as input files and the <code>splice</code> effect given with the position at which to perform the splice &#8211; this is length of the first audio section (including the excess). </p>
<p> The following diagram uses the tape analogy to illustrate the splice operation. The effect simulates the diagonal cuts and joins the two pieces: </p>
<pre><code>
length1 excess-- -- -- -- ---&gt;&lt; ---&gt;_________ : : _________________
             \ : : :\     `         
              \ : : : \     `        
               \: : :  \     `
                         * : : *- -*      
                 \ : : :\     `     
                  \ : : : \     ` _______________\: : :  \_____`____
    : : : : &lt; ---&gt;&lt; -- ---&gt;excess leeway
</code></pre>
<p> where * indicates the joining points. </p>
<p> For example, a long song begins with two verses which start (as determined e.g. by using the <code>play</code> command with the <code>trim</code> (<i>start</i>) effect) at times 0:30.125 and 1:03.432. The following commands cut out the first verse: </p>
<pre>
   sox too-long.wav part1.wav trim 0 30.130
</pre>
<p> (5 ms excess, after the first verse starts) </p>
<pre>
   sox too-long.wav part2.wav trim 1:03.422
</pre>
<p> (5 ms excess plus 5 ms leeway, before the second verse starts) </p>
<pre>
   sox part1.wav part2.wav just-right.wav splice 30.130
</pre>
<p> For another example, the SoX command </p>
<pre>
   play &quot;|sox -n -p synth 1 sin %1&quot; &quot;|sox -n -p synth 1 sin %3&quot;
</pre>
<p> generates and plays two notes, but there is a nasty click at the transition; the click can be removed by splicing instead of concatenating the audio, i.e. by appending <code>splice 1</code> to the command. (Clicks at the beginning and end of the audio can be removed by <i>preceding</i> the splice effect with <code>fade q .01 2 .01</code>). </p>
<p> Provided your arithmetic is good enough, multiple splices can be performed with a single <code>splice</code> invocation. For example: </p>
<pre>
#!/bin/sh
# Audio Copy and Paste Over
# acpo infile copy-start copy-stop paste-over-start outfile
# All times measured in samples.
rate=`soxi -r &quot;$1&quot;`
e=`expr $rate '*' 5 / 1000`  # Using default excess
l=$e                         # and leeway.
sox &quot;$1&quot; piece.wav trim `expr $2 - $e - $l`s \
   `expr $3 - $2 + $e + $l + $e`s
sox &quot;$1&quot; part1.wav trim 0 `expr $4 + $e`s
sox &quot;$1&quot; part2.wav trim `expr $4 + $3 - $2 - $e - $l`s
sox part1.wav piece.wav part2.wav &quot;$5&quot; splice \
   `expr $4 + $e`s \
   `expr $4 + $e + $3 - $2 + $e + $l + $e`s
</pre>
<p> In the above Bourne shell script, two splices are used to `copy and paste&#8217; audio. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></td>
<td ALIGN=center>*
</td>
</tr>
</table>
<p></center> </p>
<p> It is also possible to use this effect to perform general cross-fades, e.g. to join two songs. In this case, <i>excess</i> would typically be an number of seconds, the <code>-q</code> option would typically be given (to select an `equal power&#8217; cross-fade), and <i>leeway</i> should be zero (which is the default if <code>-q</code> is given). For example, if f1.wav and f2.wav are audio files to be cross-faded, then </p>
<pre>
   sox f1.wav f2.wav out.wav splice -q $(soxi -D f1.wav),3
</pre>
<p> cross-fades the files where the point of equal loudness is 3 seconds before the end of f1.wav, i.e. the total length of the cross-fade is 2 &#215; 3 = 6 seconds (Note: the $(&#8230;) notation is POSIX shell).</p>
<dt><code>stat</code> [<code>-s </code><i>scale</i>] [<code>-rms</code>] [<code>-freq</code>] [<code>-v</code>] [<code>-d</code>]</p>
<dd> Display time and frequency domain statistical information about the audio. Audio is passed unmodified through the SoX processing chain. </p>
<p> The information is output to the `standard error&#8217; (stderr) stream and is calculated, where <i>n</i> is the duration of the audio in samples, <i>c</i> is the number of audio channels, <i>r</i> is the audio sample rate, and <i>x</i><font SIZE="-2"><i>k</i></font><i></i> represents the PCM value (in the range -1 to +1 by default) of each successive sample in the audio, as follows: <center></p>
<table>
<tr VALIGN=top>
<td><i>Samples read</i></td>
<td><i>n</i>&#215;<i>c</i></td>
<td>&nbsp;<wbr>
</td>
</tr>
<tr VALIGN=top>
<td><i>Length (seconds)</i></td>
<td><i>n</i>&#247;<i>r</i></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>Scaled by</i></td>
<td>&nbsp;<wbr></td>
<td>See -s below.
</td>
</tr>
<tr VALIGN=top>
<td><i>Maximum amplitude</i></td>
<td>max(<i>x</i><font SIZE="-2"><i>k</i></font><i></i>)</td>
<td> The maximum sample value in the audio; usually this will be a positive number.
</td>
</tr>
<tr VALIGN=top>
<td><i>Minimum amplitude</i></td>
<td>min(<i>x</i><font SIZE="-2"><i>k</i></font><i></i>)</td>
<td> The minimum sample value in the audio; usually this will be a negative number.
</td>
</tr>
<tr VALIGN=top>
<td><i>Midline amplitude</i></td>
<td>&#189;min(<i>x</i><font SIZE="-2"><i>k</i></font><i></i>)+&#189;max(<i>x</i><font SIZE="-2"><i>k</i></font><i></i>)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>Mean norm</i></td>
<td>&sup1;/<font SIZE="-2">n</font>&Sigma;|<i>x</i><font SIZE="-2"><i>k</i></font><i></i>|</td>
<td> The average of the absolute value of each sample in the audio.
</td>
</tr>
<tr VALIGN=top>
<td><i>Mean amplitude</i></td>
<td>&sup1;/<font SIZE="-2">n</font>&Sigma;<i>x</i><font SIZE="-2"><i>k</i></font><i></i></td>
<td> The average of each sample in the audio. If this figure is non-zero, then it indicates the presence of a D.C. offset (which could be removed using the <code>dcshift</code> effect).
</td>
</tr>
<tr VALIGN=top>
<td><i>RMS amplitude</i></td>
<td>sr(&sup1;/<font SIZE="-2">n</font>&Sigma;<i>x</i><font SIZE="-2"><i>k</i></font><i></i>&sup2;)</td>
<td> The level of a D.C. signal that would have the same power as the audio&#8217;s average power.
</td>
</tr>
<tr VALIGN=top>
<td><i>Maximum delta</i></td>
<td>max(|<i>x</i><font SIZE="-2"><i>k</i></font><i></i>&#8211;<i>x</i><font SIZE="-2"><i>k-1</i></font><i></i>|)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>Minimum delta</i></td>
<td>min(|<i>x</i><font SIZE="-2"><i>k</i></font><i></i>&#8211;<i>x</i><font SIZE="-2"><i>k-1</i></font><i></i>|)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>Mean delta</i></td>
<td>&sup1;/<font SIZE="-2">n-1</font>&Sigma;|<i>x</i><font SIZE="-2"><i>k</i></font><i></i>&#8211;<i>x</i><font SIZE="-2"><i>k-1</i></font><i></i>|</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>RMS delta</i></td>
<td>sr(&sup1;/<font SIZE="-2">n-1</font>&Sigma;(<i>x</i><font SIZE="-2"><i>k</i></font><i></i>&#8211;<i>x</i><font SIZE="-2"><i>k-1</i></font><i></i>)&sup2;)</td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><i>Rough frequency</i></td>
<td>&nbsp;<wbr></td>
<td>In Hz.
</td>
</tr>
<tr VALIGN=top>
<td><i>Volume Adjustment</i></td>
<td>&nbsp;<wbr></td>
<td> The parameter to the <code>vol</code> effect which would make the audio as loud as possible without clipping. Note: See the discussion on <code>Clipping</code> above for reasons why it is rarely a good idea actually to do this.
</td>
</tr>
</table>
<p></center> </p>
<p> Note that the delta measurements are not applicable for multi-channel audio. </p>
<p> The <code>-s</code> option can be used to scale the input data by a given factor. The default value of <i>scale</i> is 2147483647 (i.e. the maximum value of a 32-bit signed integer). Internal effects always work with signed long PCM data and so the value should relate to this fact. </p>
<p> The <code>-rms</code> option will convert all output average values to `root mean square&#8217; format. </p>
<p> The <code>-v</code> option displays only the `Volume Adjustment&#8217; value. </p>
<p> The <code>-freq</code> option calculates the input&#8217;s power spectrum (4096 point DFT) instead of the statistics listed above. This should only be used with a single channel audio file. </p>
<p> The <code>-d</code> option displays a hex dump of the 32-bit signed PCM data audio in SoX&#8217;s internal buffer. This is mainly used to help track down endian problems that sometimes occur in cross-platform versions of SoX. </p>
<p> See also the <code>stats</code> effect.</p>
<dt><code>stats</code> [<code>-b </code><i>bits</i>|<code>-x </code><i>bits</i>|<code>-s </code><i>scale</i>] [<code>-w </code><i>window-time</i>]</p>
<dd> Display time domain statistical information about the audio channels; audio is passed unmodified through the SoX processing chain. Statistics are calculated and displayed for each audio channel and, where applicable, an overall figure is also given. </p>
<p> For example, for a typical well-mastered stereo music file: <center></p>
<table>
<tr VALIGN=top>
<td>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Overall&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Left&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Right
</td>
</tr>
<tr VALIGN=top>
<td>DC offset 0.000803 -0.000391 0.000803
</td>
</tr>
<tr VALIGN=top>
<td>Min level -0.750977 -0.750977 -0.653412
</td>
</tr>
<tr VALIGN=top>
<td>Max level 0.708801 0.708801 0.653534
</td>
</tr>
<tr VALIGN=top>
<td>Pk lev dB -2.49 -2.49 -3.69
</td>
</tr>
<tr VALIGN=top>
<td>RMS lev dB -19.41 -19.13 -19.71
</td>
</tr>
<tr VALIGN=top>
<td>RMS Pk dB -13.82 -13.82 -14.38
</td>
</tr>
<tr VALIGN=top>
<td>RMS Tr dB -85.25 -85.25 -82.66
</td>
</tr>
<tr VALIGN=top>
<td>Crest factor &#8211; 6.79 6.32
</td>
</tr>
<tr VALIGN=top>
<td>Flat factor 0.00 0.00 0.00
</td>
</tr>
<tr VALIGN=top>
<td>Pk count 2 2 2
</td>
</tr>
<tr VALIGN=top>
<td>Bit-depth 16/16 16/16 16/16
</td>
</tr>
<tr VALIGN=top>
<td>Num samples 7.72M
</td>
</tr>
<tr VALIGN=top>
<td>Length s 174.973
</td>
</tr>
<tr VALIGN=top>
<td>Scale max 1.000000
</td>
</tr>
<tr VALIGN=top>
<td>Window s 0.050
</td>
</tr>
</table>
<p></center> </p>
<p> <i>DC offset</i>, <i>Min level</i>, and <i>Max level</i> are shown, by default, in the range &plusmn;1. If the <code>-b</code> (bits) options is given, then these three measurements will be scaled to a signed integer with the given number of bits; for example, for 16 bits, the scale would be -32768 to +32767. The <code>-x</code> option behaves the same way as <code>-b</code> except that the signed integer values are displayed in hexadecimal. The <code>-s</code> option scales the three measurements by a given floating-point number. </p>
<p> <i>Pk lev dB</i> and <i>RMS lev dB</i> are standard peak and RMS level measured in dBFS. <i>RMS Pk dB</i> and <i>RMS Tr dB</i> are peak and trough values for RMS level measured over a short window (default 50ms). </p>
<p> <i>Crest factor</i> is the standard ratio of peak to RMS level (note: not in dB). </p>
<p> <i>Flat factor</i> is a measure of the flatness (i.e. consecutive samples with the same value) of the signal at its peak levels (i.e. either <i>Min level</i>, or <i>Max level</i>). <i>Pk count</i> is the number of occasions (not the number of samples) that the signal attained either <i>Min level</i>, or <i>Max level</i>. </p>
<p> The right-hand <i>Bit-depth</i> figure is the standard definition of bit-depth i.e. bits less significant than the given number are fixed at zero. The left-hand figure is the number of most significant bits that are fixed at zero (or one for negative numbers) subtracted from the right-hand figure (the number subtracted is directly related to <i>Pk lev dB</i>). </p>
<p> For multi-channel audio, an overall figure for each of the above measurements is given and derived from the channel figures as follows: <i>DC offset</i>: maximum magnitude; <i>Max level</i>, <i>Pk lev dB</i>, <i>RMS Pk dB</i>, <i>Bit-depth</i>: maximum; <i>Min level</i>, <i>RMS Tr dB</i>: minimum; <i>RMS lev dB</i>, <i>Flat factor</i>, <i>Pk count</i>: average; <i>Crest factor</i>: not applicable. </p>
<p> <i>Length s</i> is the duration in seconds of the audio, and <i>Num samples</i> is equal to the sample-rate multiplied by <i>Length</i>. <i>Scale Max</i> is the scaling applied to the first three measurements; specifically, it is the maximum value that could apply to <i>Max level</i>. <i>Window s</i> is the length of the window used for the peak and trough RMS measurements. </p>
<p> See also the <code>stat</code> effect.</p>
<dt><code>swap</code></p>
<dd> Swap stereo channels. See also <code>remix</code> for an effect that allows arbitrary channel selection and ordering (and mixing).</p>
<dt><code>stretch </code><i>factor</i> [<i>window fade shift fading</i>]</p>
<dd> Change the audio duration (but not its pitch). This effect is broadly equivalent to the <code>tempo</code> effect with (<i>factor</i> inverted and) <i>search</i> set to zero, so in general, its results are comparatively poor; it is retained as it can sometimes out-perform <code>tempo</code> for small <i>factor</i>s. </p>
<p> <i>factor</i> of stretching: &gt;1 lengthen, &lt;1 shorten duration. <i>window</i> size is in ms. Default is 20ms. The <i>fade</i> option, can be `lin&#8217;. <i>shift</i> ratio, in [0 1]. Default depends on stretch factor. 1 to shorten, 0.8 to lengthen. The <i>fading</i> ratio, in [0 0.5]. The amount of a fade&#8217;s default depends on <i>factor</i> and <i>shift</i>. </p>
<p> See also the <code>tempo</code> effect.</p>
<dt><code>synth</code> [<code>-j </code><i>KEY</i>] [<code>-n</code>] [<i>len</i> [<i>off</i> [<i>ph</i> [<i>p1</i> [<i>p2</i> [<i>p3</i>]]]]]] {[<i>type</i>] [<i>combine</i>] :[[<code>%</code>]<i>freq</i>[<code>k</code>][<code>:</code>|<code>+</code>|<code>/</code>|<code>&#8211;</code>[<code>%</code>]<i>freq2</i>[<code>k</code>]]] [<i>off</i> [<i>ph</i> [<i>p1</i> [<i>p2</i> [<i>p3</i>]]]]]}</p>
<dd> This effect can be used to generate fixed or swept frequency audio tones with various wave shapes, or to generate wide-band noise of various `colours&#8217;. Multiple synth effects can be cascaded to produce more complex waveforms; at each stage it is possible to choose whether the generated waveform will be mixed with, or modulated onto the output from the previous stage. Audio for each channel in a multi-channel audio file can be synthesised independently. </p>
<p> Though this effect is used to generate audio, an input file must still be given, the characteristics of which will be used to set the synthesised audio length, the number of channels, and the sampling rate; however, since the input file&#8217;s audio is not normally needed, a `null file&#8217; (with the special name <code>-n</code>) is often given instead (and the length specified as a parameter to <code>synth</code> or by another given effect that can has an associated length). </p>
<p> For example, the following produces a 3 second, 48kHz, audio file containing a sine-wave swept from 300 to 3300 Hz: </p>
<pre>
   sox -n output.wav synth 3 sine 300-3300
</pre>
<p> and this produces an 8 kHz version: </p>
<pre>
   sox -r 8000 -n output.wav synth 3 sine 300-3300
</pre>
<p> Multiple channels can be synthesised by specifying the set of parameters shown between braces multiple times; the following puts the swept tone in the left channel and adds `brown&#8217; noise in the right: </p>
<pre>
   sox -n output.wav synth 3 sine 300-3300 brownnoise
</pre>
<p> The following example shows how two synth effects can be cascaded to create a more complex waveform: </p>
<pre>
   play -n synth 0.5 sine 200-500 synth 0.5 sine fmod 700-100
</pre>
<p> Frequencies can also be given in `scientific&#8217; note notation, or, by prefixing a `%&#8217; character, as a number of semitones relative to `middle A&#8217; (440 Hz). For example, the following could be used to help tune a guitar&#8217;s low `E&#8217; string: </p>
<pre>
   play -n synth 4 pluck %-29
</pre>
<p> or with a (Bourne shell) loop, the whole guitar: </p>
<pre>
   for n in E2 A2 D3 G3 B3 E4; do
        play -n synth 4 pluck $n repeat 2; done
</pre>
<p> See the <code>delay</code> effect (above) and the reference to `SoX scripting examples&#8217; (below) for more <code>synth</code> examples. </p>
<p> <code>N.B.</code> This effect generates audio at maximum volume (0dBFS), which means that there is a high chance of clipping when using the audio subsequently, so in many cases, you will want to follow this effect with the <code>gain</code> effect to prevent this from happening. (See also <code>Clipping</code> above.) Note that, by default, the <code>synth</code> effect incorporates the functionality of <code>gain -h</code> (see the <code>gain</code> effect for details); <code>synth</code>&#8216;s <code>-n</code> option may be given to disable this behaviour. </p>
<p> A detailed description of each <code>synth</code> parameter follows: </p>
<p> <i>len</i> is the length of audio to synthesise expressed as a time or as a number of samples; 0=inputlength, default=0. </p>
<p> The format for specifying lengths in time is hh:mm:ss.frac. The format for specifying sample counts is the number of samples with the letter `s&#8217; appended to it. </p>
<p> <i>type</i> is one of sine, square, triangle, sawtooth, trapezium, exp, [white]noise, tpdfnoise pinknoise, brownnoise, pluck; default=sine. </p>
<p> <i>combine</i> is one of create, mix, amod (amplitude modulation), fmod (frequency modulation); default=create. </p>
<p> <i>freq</i>/<i>freq2</i> are the frequencies at the beginning/end of synthesis in Hz or, if preceded with `%&#8217;, semitones relative to A (440 Hz); alternatively, `scientific&#8217; note notation (e.g. E2) may be used. The default frequency is 440Hz. By default, the tuning used with the note notations is `equal temperament&#8217;; the <code>-j</code> <i>KEY</i> option selects `just intonation&#8217;, where <i>KEY</i> is an integer number of semitones relative to A (so for example, -9 or 3 selects the key of C), or a note in scientific notation. </p>
<p> If <i>freq2</i> is given, then <i>len</i> must also have been given and the generated tone will be swept between the given frequencies. The two given frequencies must be separated by one of the characters `:&#8217;, `+&#8217;, `/&#8217;, or `-&#8216;. This character is used to specify the sweep function as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>:</code></p>
<dd> Linear: the tone will change by a fixed number of hertz per second.</p>
<dt><code>+</code></p>
<dd> Square: a second-order function is used to change the tone.</p>
<dt><code>/</code></p>
<dd> Exponential: the tone will change by a fixed number of semitones per second.</p>
<dt><code>&#8211;</code></p>
<dd> Exponential: as `/&#8217;, but initial phase always zero, and stepped (less smooth) frequency changes.</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> Not used for noise. </p>
<p> <i>off</i> is the bias (DC-offset) of the signal in percent; default=0. </p>
<p> <i>ph</i> is the phase shift in percentage of 1 cycle; default=0. Not used for noise. </p>
<p> <i>p1</i> is the percentage of each cycle that is `on&#8217; (square), or `rising&#8217; (triangle, exp, trapezium); default=50 (square, triangle, exp), default=10 (trapezium), or sustain (pluck); default=40. </p>
<p> <i>p2</i> (trapezium): the percentage through each cycle at which `falling&#8217; begins; default=50. exp: the amplitude in multiples of 2dB; default=50, or tone-1 (pluck); default=20. </p>
<p> <i>p3</i> (trapezium): the percentage through each cycle at which `falling&#8217; ends; default=60, or tone-2 (pluck); default=90.</p>
<dt><code>tempo </code>[<code>-q</code>] [<code>-m</code>|<code>-s</code>|<code>-l</code>] <i>factor</i> [<i>segment</i> [<i>search</i> [<i>overlap</i>]]]</p>
<dd> Change the audio playback speed but not its pitch. This effect uses the WSOLA algorithm. The audio is chopped up into segments which are then shifted in the time domain and overlapped (cross-faded) at points where their waveforms are most similar as determined by measurement of `least squares&#8217;. </p>
<p> By default, linear searches are used to find the best overlapping points. If the optional <code>-q</code> parameter is given, tree searches are used instead. This makes the effect work more quickly, but the result may not sound as good. However, if you must improve the processing speed, this generally reduces the sound quality less than reducing the search or overlap values. </p>
<p> The <code>-m</code> option is used to optimize default values of segment, search and overlap for music processing. </p>
<p> The <code>-s</code> option is used to optimize default values of segment, search and overlap for speech processing. </p>
<p> The <code>-l</code> option is used to optimize default values of segment, search and overlap for `linear&#8217; processing that tends to cause more noticeable distortion but may be useful when factor is close to 1. </p>
<p> If -m, -s, or -l is specified, the default value of segment will be calculated based on factor, while default search and overlap values are based on segment. Any values you provide still override these default values. </p>
<p> <i>factor</i> gives the ratio of new tempo to the old tempo, so e.g. 1.1 speeds up the tempo by 10%, and 0.9 slows it down by 10%. </p>
<p> The optional <i>segment</i> parameter selects the algorithm&#8217;s segment size in milliseconds. If no other flags are specified, the default value is 82 and is typically suited to making small changes to the tempo of music. For larger changes (e.g. a factor of 2), 41 ms may give a better result. The -m, -s, and -l flags will cause the segment default to be automatically adjusted based on factor. For example using -s (for speech) with a tempo of 1.25 will calculate a default segment value of 32. </p>
<p> The optional <i>search</i> parameter gives the audio length in milliseconds over which the algorithm will search for overlapping points. If no other flags are specified, the default value is 14.68. Larger values use more processing time and may or may not produce better results. A practical maximum is half the value of segment. Search can be reduced to cut processing time at the risk of degrading output quality. The -m, -s, and -l flags will cause the search default to be automatically adjusted based on segment. </p>
<p> The optional <i>overlap</i> parameter gives the segment overlap length in milliseconds. Default value is 12, but -m, -s, or -l flags automatically adjust overlap based on segment size. Increasing overlap increases processing time and may increase quality. A practical maximum for overlap is the value of search, with overlap typically being (at least) a little smaller then search. </p>
<p> See also <code>speed</code> for an effect that changes tempo and pitch together, <code>pitch</code> and <code>bend</code> for effects that change pitch only, and <code>stretch</code> for an effect that changes tempo using a different algorithm.</p>
<dt><code>treble </code><i>gain</i> [<i>frequency</i>[<code>k</code>] [<i>width</i>[<code>s</code>|<code>h</code>|<code>k</code>|<code>o</code>|<code>q</code>]]]</p>
<dd> Apply a treble tone-control effect. See the description of the <code>bass</code> effect for details.</p>
<dt><code>tremolo </code><i>speed</i> [<i>depth</i>]</p>
<dd> Apply a tremolo (low frequency amplitude modulation) effect to the audio. The tremolo frequency in Hz is given by <i>speed</i>, and the depth as a percentage by <i>depth</i> (default 40).</p>
<dt><code>trim</code> {[<code>=</code>|<code>&#8211;</code>]<i>position</i>}</p>
<dd> Cuts portions out of the audio. Any number of <i>position</i>s may be given; audio is not sent to the output until the first <i>position</i> is reached. The effect then alternates between copying and discarding audio at each <i>position</i>. </p>
<p> If a <i>position</i> is preceded by an equals or minus sign, it is interpreted relative to the beginning or the end of the audio, respectively. (The audio length must be known for end-relative locations to work.) Otherwise, it is considered an offset from the last <i>position</i>, or from the start of audio for the first parameter. Using a value of 0 for the first <i>position</i> parameter allows copying from the beginning of the audio. </p>
<p> All parameters can be specified using either an amount of time or an exact count of samples. The format for specifying lengths in time is hh:mm:ss.frac. A value of 1:30.5 for the first parameter will not start until 1 minute, thirty and &#189; seconds into the audio. The format for specifying sample counts is the number of samples with the letter `s&#8217; appended to it. A value of 8000s for the first parameter will wait until 8000 samples are read before starting to process audio. </p>
<p> For example, </p>
<pre>
   sox infile outfile trim 0 10
</pre>
<p> will copy the first ten seconds, while </p>
<pre>
   play infile trim 12:34 =15:00 -2:00
</pre>
<p> will play from 12 minutes 34 seconds into the audio up to 15 minutes into the audio (i.e. 2 minutes and 26 seconds long), then resume playing two minutes before the end of audio.</p>
<dt><code>upsample</code> [<i>factor</i>]</p>
<dd> Upsample the signal by an integer factor: <i>factor</i>-1 zero-value samples are inserted between each pair of input samples. As a result, the original spectrum is replicated into the new frequency space (aliasing) and attenuated. This attenuation can be compensated for by adding <code>vol </code><i>factor</i> after any further processing. The upsample effect is typically used in combination with filtering effects. </p>
<p> For a general resampling effect with anti-aliasing, see <code>rate</code>. See also <code>downsample</code>.</p>
<dt><code>vad </code>[<i>options</i>]</p>
<dd> Voice Activity Detector. Attempts to trim silence and quiet background sounds from the ends of (fairly high resolution i.e. 16-bit, 44-48kHz) recordings of speech. The algorithm currently uses a simple cepstral power measurement to detect voice, so may be fooled by other things, especially music. The effect can trim only from the front of the audio, so in order to trim from the back, the <code>reverse</code> effect must also be used. E.g. </p>
<pre>
   play speech.wav norm vad
</pre>
<p> to trim from the front, </p>
<pre>
   play speech.wav norm reverse vad reverse
</pre>
<p> to trim from the back, and </p>
<pre>
   play speech.wav norm vad reverse vad reverse
</pre>
<p> to trim from both ends. The use of the <code>norm</code> effect is recommended, but remember that neither <code>reverse</code> nor <code>norm</code> is suitable for use with streamed audio. </p>
<p> <i>Options:</i><br />
 Default values are shown in parenthesis.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-t&nbsp;<wbr></code><i>num</i>&nbsp;<wbr>(7)</p>
<dd> The measurement level used to trigger activity detection. This might need to be changed depending on the noise level, signal level and other charactistics of the input audio.</p>
<dt><code>-T&nbsp;<wbr></code><i>num</i>&nbsp;<wbr>(0.25)</p>
<dd> The time constant (in seconds) used to help ignore short bursts of sound.</p>
<dt><code>-s&nbsp;<wbr></code><i>num</i>&nbsp;<wbr>(1)</p>
<dd> The amount of audio (in seconds) to search for quieter/shorter bursts of audio to include prior to the detected trigger point.</p>
<dt><code>-g&nbsp;<wbr></code><i>num</i>&nbsp;<wbr>(0.25)</p>
<dd> Allowed gap (in seconds) between quieter/shorter bursts of audio to include prior to the detected trigger point.</p>
<dt><code>-p&nbsp;<wbr></code><i>num</i>&nbsp;<wbr>(0)</p>
<dd> The amount of audio (in seconds) to preserve before the trigger point and any found quieter/shorter bursts.</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> <i>Advanced Options:</i><br />
 These allow fine tuning of the algorithm&#8217;s internal parameters.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-b&nbsp;<wbr></code><i>num</i></p>
<dd> The algorithm (internally) uses adaptive noise estimation/reduction in order to detect the start of the wanted audio. This option sets the time for the initial noise estimate.</p>
<dt><code>-N&nbsp;<wbr></code><i>num</i></p>
<dd> Time constant used by the adaptive noise estimator for when the noise level is increasing.</p>
<dt><code>-n&nbsp;<wbr></code><i>num</i></p>
<dd> Time constant used by the adaptive noise estimator for when the noise level is decreasing.</p>
<dt><code>-r&nbsp;<wbr></code><i>num</i></p>
<dd> Amount of noise reduction to use in the detection algorithm (e.g. 0, 0.5, &#8230;).</p>
<dt><code>-f&nbsp;<wbr></code><i>num</i></p>
<dd> Frequency of the algorithm&#8217;s processing/measurements.</p>
<dt><code>-m&nbsp;<wbr></code><i>num</i></p>
<dd> Measurement duration; by default, twice the measurement period; i.e. with overlap.</p>
<dt><code>-M&nbsp;<wbr></code><i>num</i></p>
<dd> Time constant used to smooth spectral measurements.</p>
<dt><code>-h&nbsp;<wbr></code><i>num</i></p>
<dd> `Brick-wall&#8217; frequency of high-pass filter applied at the input to the detector algorithm.</p>
<dt><code>-l&nbsp;<wbr></code><i>num</i></p>
<dd> `Brick-wall&#8217; frequency of low-pass filter applied at the input to the detector algorithm.</p>
<dt><code>-H&nbsp;<wbr></code><i>num</i></p>
<dd> `Brick-wall&#8217; frequency of high-pass lifter used in the detector algorithm.</p>
<dt><code>-L&nbsp;<wbr></code><i>num</i></p>
<dd> `Brick-wall&#8217; frequency of low-pass lifter used in the detector algorithm.</dl>
</dl>
<dt>&nbsp;<wbr></p>
<dd> See also the <code>silence</code> effect.</p>
<dt><code>vol </code><i>gain</i> [<i>type</i> [<i>limitergain</i>]]</p>
<dd> Apply an amplification or an attenuation to the audio signal. Unlike the <code>-v</code> option (which is used for balancing multiple input files as they enter the SoX effects processing chain), <code>vol</code> is an effect like any other so can be applied anywhere, and several times if necessary, during the processing chain. </p>
<p> The amount to change the volume is given by <i>gain</i> which is interpreted, according to the given <i>type</i>, as follows: if <i>type</i> is <code>amplitude</code> (or is omitted), then <i>gain</i> is an amplitude (i.e. voltage or linear) ratio, if <code>power</code>, then a power (i.e. wattage or voltage-squared) ratio, and if <code>dB</code>, then a power change in dB. </p>
<p> When <i>type</i> is <code>amplitude</code> or <code>power</code>, a <i>gain</i> of 1 leaves the volume unchanged, less than 1 decreases it, and greater than 1 increases it; a negative <i>gain</i> inverts the audio signal in addition to adjusting its volume. </p>
<p> When <i>type</i> is <code>dB</code>, a <i>gain</i> of 0 leaves the volume unchanged, less than 0 decreases it, and greater than 0 increases it. </p>
<p> See [4] for a detailed discussion on electrical (and hence audio signal) voltage and power ratios. </p>
<p> Beware of <code>Clipping</code> when the increasing the volume. </p>
<p> The <i>gain</i> and the <i>type</i> parameters can be concatenated if desired, e.g. <code>vol 10dB</code>. </p>
<p> An optional <i>limitergain</i> value can be specified and should be a value much less than 1 (e.g. 0.05 or 0.02) and is used only on peaks to prevent clipping. Not specifying this parameter will cause no limiter to be used. In verbose mode, this effect will display the percentage of the audio that needed to be limited. </p>
<p> See also <code>gain</code> for a volume-changing effect with different capabilities, and <code>compand</code> for a dynamic-range compression/expansion/limiting effect.</dl>
<h3>Deprecated Effects</h3>
<p> The following effects have been renamed or have their functionality included in another effect; they continue to work in this version of SoX but may be removed in future.</p>
<dl>
<dt><code>mixer</code> [ <code>-l</code>|<code>-r</code>|<code>-f</code>|<code>-b</code>|<code>-1</code>|<code>-2</code>|<code>-3</code>|<code>-4</code>|<i>n</i>{<code>,</code><i>n</i>} ]</p>
<dd> Reduce the number of audio channels by mixing or selecting channels, or increase the number of channels by duplicating channels. Note: this effect operates on the audio <i>channels</i> within the SoX effects processing chain; it should not be confused with the <code>-m</code> global option (where multiple <i>files</i> are mix-combined before entering the effects chain). </p>
<p> When reducing the number of channels it is possible to use the <code>-l</code>, <code>-r</code>, <code>-f</code>, <code>-b</code>, <code>-1</code>, <code>-2</code>, <code>-3</code>, <code>-4</code>, options to select only the left, right, front, back channel(s) or specific channel for the output instead of averaging the channels. The <code>-l</code>, and <code>-r</code> options will do averaging in quad-channel files so select the exact channel to prevent this. </p>
<p> The <code>mixer</code> effect can also be invoked with up to 16 numbers, separated by commas, which specify the proportion (0 = 0% and 1 = 100%) of each input channel that is to be mixed into each output channel. In two-channel mode, 4 numbers are given: l &rarr; l, l &rarr; r, r &rarr; l, and r &rarr; r, respectively. In four-channel mode, the first 4 numbers give the proportions for the left-front output channel, as follows: lf &rarr; lf, rf &rarr; lf, lb &rarr; lf, and rb &rarr; rf. The next 4 give the right-front output in the same order, then left-back and right-back. </p>
<p> It is also possible to use the 16 numbers to expand or reduce the channel count; just specify 0 for unused channels. </p>
<p> Finally, certain reduced combination of numbers can be specified for certain input/output channel combinations. <center></p>
<table>
<tr VALIGN=top>
<td ALIGN=center><i>In Ch</i></td>
<td ALIGN=center><i>Out Ch</i></td>
<td ALIGN=center><i>Num</i></td>
<td><i>Mappings</i>
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2</td>
<td ALIGN=center>1</td>
<td ALIGN=center>2</td>
<td>l &rarr; l, r &rarr; l
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>2</td>
<td ALIGN=center>2</td>
<td ALIGN=center>1</td>
<td>adjust balance
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>1</td>
<td ALIGN=center>4</td>
<td>lf &rarr; l, rf &rarr; l, lb &rarr; l, rb &rarr; l
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>2</td>
<td ALIGN=center>2</td>
<td>lf &rarr; l&amp;rf &rarr; r, lb &rarr; l&amp;rb &rarr; r
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td ALIGN=center>1</td>
<td>adjust balance
</td>
</tr>
<tr VALIGN=top>
<td ALIGN=center>4</td>
<td ALIGN=center>4</td>
<td ALIGN=center>2</td>
<td>front balance, back balance
</td>
</tr>
</table>
<p></center> </p>
<p> This effect has been superseded by the <code>remix</code> effect that handles any number of channels.</dl>
<h2>DIAGNOSTICS</h2>
<p> Exit status is 0 for no error, 1 if there is a problem with the command-line parameters, or 2 if an error occurs during file processing.</p>
<h2>BUGS</h2>
<p> Please report any bugs found in this version of SoX to the mailing list (sox-users [at] lists.sourceforge.net).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1), <code><a href="/docs/linux/man/7-soxformat/">soxformat</a></code>(7), <code><a href="/docs/linux/man/3-libsox/">libsox</a></code>(3)<br />
 <code><a href="/docs/linux/man/1-audacity/">audacity</a></code>(1), <code><a href="/docs/linux/man/1-gnuplot/">gnuplot</a></code>(1), <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1)<br />
 The SoX web site at <a rel="nofollow" href="http://sox.sourceforge.net">http://sox.sourceforge.net</a><br />
 SoX scripting examples at <a rel="nofollow" href="http://sox.sourceforge.net/Docs/Scripts">http://sox.sourceforge.net/Docs/Scripts</a></p>
<h3>References</h3>
<dl>
<dt>[1]</p>
<dd> R. Bristow-Johnson, <i>Cookbook formulae for audio EQ biquad filter coefficients</i>, <a rel="nofollow" href="http://musicdsp.org/files/Audio-EQ-Cookbook.txt">http://musicdsp.org/files/Audio-EQ-Cookbook.txt</a></p>
<dt>[2]</p>
<dd> Wikipedia, <i>Q-factor</i>, <a rel="nofollow" href="http://en.wikipedia.org/wiki/Q_factor">http://en.wikipedia.org/wiki/Q_factor</a></p>
<dt>[3]</p>
<dd> Scott Lehman, <i>Effects Explained</i>, <a rel="nofollow" href="http://harmony-central.com/Effects/effects-explained.html">http://harmony-central.com/Effects/effects-explained.html</a></p>
<dt>[4]</p>
<dd> Wikipedia, <i>Decibel</i>, <a rel="nofollow" href="http://en.wikipedia.org/wiki/Decibel">http://en.wikipedia.org/wiki/Decibel</a></p>
<dt>[5]</p>
<dd> Richard Furse, <i>Linux Audio Developer&#8217;s Simple Plugin API</i>, <a rel="nofollow" href="http://www.ladspa.org">http://www.ladspa.org</a></p>
<dt>[6]</p>
<dd> Richard Furse, <i>Computer Music Toolkit</i>, <a rel="nofollow" href="http://www.ladspa.org/cmt">http://www.ladspa.org/cmt</a></p>
<dt>[7]</p>
<dd> Steve Harris, <i>LADSPA plugins</i>, <a rel="nofollow" href="http://plugin.org.uk">http://plugin.org.uk</a></dl>
<h2>LICENSE</h2>
<p> Copyright 1998-2013 Chris Bagwell and SoX Contributors.<br />
 Copyright 1991 Lance Norskog and Sundry Contributors. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.</p>
<h2>AUTHORS</h2>
<p> Chris Bagwell (cbagwell [at] users.sourceforge.net). Other authors and contributors are listed in the ChangeLog file that is distributed with the source code. </p>
<h2>Index</h2>
