---
title: "adplay(1)"
name: "adplay"
section: "1"
letter: "a"
url: "/docs/linux/man/1-adplay/"
description: "adplay – AdPlay/UNIX console-based OPL2 audio player"
---

<h2>NAME</h2>
<p> adplay &#8211; AdPlay/UNIX console-based OPL2 audio player</p>
<h2>SYNOPSIS</h2>
<p> <code>adplay</code> [OPTION]&#8230; FILE&#8230;</p>
<h2>DESCRIPTION</h2>
<p> AdPlay/UNIX is AdPlug&#8217;s UNIX console-based frontend. It tries to play back all given FILEs, using one of many available output mechanisms. </p>
<p> AdPlay/UNIX plays endlessly, if only one file is given. With multiple files, it plays them in a sequence and exits after the last file. The same can also be accomplished with only one file, by using the <code>-o</code> option. When using the disk writer, <code>-o</code> is implied.</p>
<h2>EXIT STATUS</h2>
<p> <code>adplay</code> returns 0 on successful operation. 1 is returned otherwise.</p>
<h2>OUTPUT MECHANISMS</h2>
<p> AdPlay/UNIX can play back using many different output mechanisms, which can be selected with the <code>-O</code> argument. The availability of a method depends on compile-time settings. Available methods are printed out after the help text, displayed with <code>&#8211;help</code>. </p>
<p> Next is a brief description of all output mechanisms, following their abbreviations:</p>
<h3>oss &#8212; Open Sound System (OSS) driver</h3>
<p> This output method is available on most Linux and other UNIX systems.</p>
<h3>null &#8212; Total silence</h3>
<p> Discards anything sent to it. It can be useful for testing purposes.</p>
<h3>disk &#8212; Disk writer</h3>
<p> Writes its output to a file in Microsoft RIFF WAVE format.</p>
<h3>esound &#8212; EsounD output</h3>
<p> Creates a socket connection to an EsounD server and streams the audio to it.</p>
<h3>qsa &#8212; QNX Sound Architecture (QSA) driver</h3>
<p> Uses the QNX system&#8217;s standard output method.</p>
<h3>sdl &#8212; Simple Directmedia Layer (SDL) driver</h3>
<p> Uses the SDL library for sound output. The library has a broader platform support than any of the other output methods. Thus, it could be useful on some exotic systems.</p>
<h3>alsa &#8212; Advanced Linux Sound Architecture (ALSA) driver</h3>
<p> Uses the standard output method on newer Linux systems.</p>
<h3>ao &#8212; libao driver</h3>
<p> Libao is a cross-platform audio library with very broad platform support. Might be useful on systems, where SDL is not available, and generally to do tricky things.</p>
<h2>OPTIONS</h2>
<p> The order of the option commandline parameters is not important, except for the <code>-d</code> option, which always has to be specified after an <code>-O</code> option.</p>
<h3>Output selection:</h3>
<dl>
<dt><code>-O, &#8211;output=OUTPUT</code></p>
<dd> Specify output mechanism. Available mechanisms depend on compilation settings and are printed on <code>&#8211;help</code> output. A reasonable default is automatically selected, based on the availability of the output mechanisms.</dl>
<h3>OSS driver (oss) specific:</h3>
<dl>
<dt><code>-d &#8211;device=FILE</code></p>
<dd> Set sound output device file to FILE. This is <code>/dev/dsp</code> by default.</dl>
<h3>Disk writer (disk) specific:</h3>
<dl>
<dt><code>-d &#8211;device=FILE</code></p>
<dd> Write sound data to FILE. The data is written in Microsoft RIFF WAVE format (little-endian). You can specify a single &#8216;-&#8216; to write to stdout instead. This option has no default and must be specified when the disk writer is to be used!</dl>
<h3>EsounD output (esound) specific:</h3>
<dl>
<dt><code>-d &#8211;device=URL</code></p>
<dd> Connect to &quot;hostname:port&quot; combination in URL. Example: &quot;myhost.sound.net:1234&quot;. The default is &quot;localhost:16001&quot;.</dl>
<h3>ALSA driver (alsa) specific:</h3>
<dl>
<dt><code>-d &#8211;device=DEVICE</code></p>
<dd> Set sound output device to DEVICE. This is <code>plughw:0,0</code> by default.</dl>
<h3>Playback quality:</h3>
<dl>
<dt><code>-8, &#8211;8bit</code></p>
<dd> Use only 8-bit samples for playback.</p>
<dt><code>&#8211;16bit</code></p>
<dd> Use only 16-bit samples for playback (default).</p>
<dt><code>-f, &#8211;freq=FREQ</code></p>
<dd> Set playback frequency to FREQ, in Hz. This is 44100Hz by default.</p>
<dt><code>&#8211;stereo</code></p>
<dd> Use only stereo samples for playback. The sound stream is just doubled, no further audio processing is done. This option is pretty useless unless you have very obscure audio hardware that only accepts stereo streams. AdPlug only generates mono streams because the OPL2 only generates mono sound.</p>
<dt><code>&#8211;mono</code></p>
<dd> Use only mono samples for playback (default).</p>
<dt><code>-b &#8211;buffer=SIZE</code></p>
<dd> Set sound buffer size to SIZE samples. If you notice sound skipping with the default setting, try a greater buffer size. Note that this is measured in samples, not bytes! This is 2048 samples by default. Only the OSS, SDL, ALSA and libao output drivers support this option.</dl>
<h3>Informative output:</h3>
<dl>
<dt><code>-i &#8211;instruments</code></p>
<dd> Display instrument names (if available).</p>
<dt><code>-r &#8211;realtime</code></p>
<dd> Display realtime playback information, while playing. This will display a one-line status bar, containing essential playback information.</p>
<dt><code>-m &#8211;message</code></p>
<dd> Display the song message (if available).</p>
<dt></dl>
<h3>Playback:</h3>
<dd> <code>-s &#8211;subsong=N</code> Play subsong number N, instead of the first subsong. Only useful for file formats that support multiple subsongs.</p>
<dl>
<dt><code>-o &#8211;once</code></p>
<dd> Play just once, don&#8217;t loop. This will exit <code>adplay</code> after the song ended. This is the default when multiple <code>FILEs</code> are given.</dl>
<h3>Miscellaneous:</h3>
<dl>
<dt><code>-D, &#8211;database=FILE</code></p>
<dd> Additionally use database file FILE. This option may be specified multiple times. Each database file is additionally merged with the others, creating one large database on the fly.</p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> Be more quiet.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Be more verbose.</p>
<dt><code>-h, &#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> Show version of program.</dl>
<h2>AUTHOR</h2>
<p> Simon Peter &lt;dn.tlp [at] gmx.net&gt; </p>
<h2>Index</h2>
