---
title: "aplay(1)"
name: "aplay"
section: "1"
letter: "a"
url: "/docs/linux/man/1-aplay/"
description: "arecord, aplay – command-line sound recorder and player for ALSA soundcard driver"
---

<h2 class="name">NAME</h2>
<p> arecord, aplay &#8211; command-line sound recorder and player for ALSA soundcard driver </p>
<h2>SYNOPSIS</h2>
<p> <code>arecord</code> [<i>flags</i>] [filename]<br />
 <code>aplay</code> [<i>flags</i>] [filename [filename]] &#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>arecord</code> is a command-line soundfile recorder for the ALSA soundcard driver. It supports several file formats and multiple soundcards with multiple devices. If recording with interleaved mode samples the file is automatically split before the 2GB filesize. </p>
<p> <code>aplay</code> is much the same, only it plays instead of recording. For supported soundfile formats, the sampling rate, bit depth, and so forth can be automatically determined from the soundfile header. </p>
<p> If filename is not specified, the standard output or input is used. The <code>aplay</code> utility accepts multiple filenames. </p>
<h2>OPTIONS</h2>
<dl>
<dt><i>-h, &#8211;help</i></p>
<dd> Help: show syntax.</p>
<dt><i>&#8211;version</i></p>
<dd> Print current version.</p>
<dt><i>-l, &#8211;list-devices</i></p>
<dd> List all soundcards and digital audio devices</p>
<dt><i>-L, &#8211;list-pcms</i></p>
<dd> List all PCMs defined</p>
<dt><i>-D, &#8211;device=NAME</i></p>
<dd> Select PCM by name</p>
<dt><i>-q &#8211;quiet</i></p>
<dd> Quiet mode. Suppress messages (not sound :))</p>
<dt><i>-t, &#8211;file-type TYPE</i></p>
<dd> File type (voc, wav, raw or au). If this parameter is omitted the WAVE format is used.</p>
<dt><i>-c, &#8211;channels=#</i></p>
<dd> The number of channels. The default is one channel. Valid values are 1 through 32.</p>
<dt><i>-f &#8211;format=FORMAT</i></p>
<dd> Sample format<br />
 Recognized sample formats are: S8 U8 S16_LE S16_BE U16_LE U16_BE S24_LE S24_BE U24_LE U24_BE S32_LE S32_BE U32_LE U32_BE FLOAT_LE FLOAT_BE FLOAT64_LE FLOAT64_BE IEC958_SUBFRAME_LE IEC958_SUBFRAME_BE MU_LAW A_LAW IMA_ADPCM MPEG GSM SPECIAL S24_3LE S24_3BE U24_3LE U24_3BE S20_3LE S20_3BE U20_3LE U20_3BE S18_3LE S18_3BE U18_3LE<br />
 Some of these may not be available on selected hardware<br />
 The available format shortcuts are: </p>
<pre><code>
- f cd(16 bit little endian, 44100, stereo)[-f S16_LE - c2 - r44100] - f cdr(16 bit big endian, 44100, stereo)[-f S16_BE - c2 - r44100] - f dat(16 bit little endian, 48000, stereo)[-f S16_LE - c2 - r48000]
</code></pre>
<p> If no format is given U8 is used.</p>
<dt><i>-r, &#8211;rate=#&lt;Hz&gt;</i></p>
<dd> Sampling rate in Hertz. The default rate is 8000 Hertz. If the value specified is less than 300, it is taken as the rate in kilohertz. Valid values are 2000 through 192000 Hertz.</p>
<dt><i>-d, &#8211;duration=#</i></p>
<dd> Interrupt after # seconds. A value of zero means infinity. The default is zero, so if this option is omitted then the record/playback process will run until it is killed. Either &#8216;-d&#8217; or &#8216;-s&#8217; option is available exclusively.</p>
<dt><i>-s, &#8211;samples=#</i></p>
<dd> Interrupt after transmission of # PCM frames. A value of zero means infinity. The default is zero, so if this options is omitted then the record/playback process will run until it is killed. Either &#8216;-d&#8217; or &#8216;-s&#8217; option is available exclusively.</p>
<dt><i>-M, &#8211;mmap</i></p>
<dd> Use memory-mapped (mmap) I/O mode for the audio stream. If this option is not set, the read/write I/O mode will be used.</p>
<dt><i>-N, &#8211;nonblock</i></p>
<dd> Open the audio device in non-blocking mode. If the device is busy the program will exit immediately. If this option is not set the program will block until the audio device is available again.</p>
<dt><i>-F, &#8211;period-time=#</i></p>
<dd> Distance between interrupts is # microseconds. If no period time and no period size is given then a quarter of the buffer time is set.</p>
<dt><i>-B, &#8211;buffer-time=#</i></p>
<dd> Buffer duration is # microseconds If no buffer time and no buffer size is given then the maximal allowed buffer time but not more than 500ms is set.</p>
<dt><i>&#8211;period-size=#</i></p>
<dd> Distance between interrupts is # frames If no period size and no period time is given then a quarter of the buffer size is set.</p>
<dt><i>&#8211;buffer-size=#</i></p>
<dd> Buffer duration is # frames If no buffer time and no buffer size is given then the maximal allowed buffer time but not more than 500ms is set.</p>
<dt><i>-A, &#8211;avail-min=#</i></p>
<dd> Min available space for wakeup is # microseconds</p>
<dt><i>-R, &#8211;start-delay=#</i></p>
<dd> Delay for automatic PCM start is # microseconds (relative to buffer size if &lt;= 0)</p>
<dt><i>-T, &#8211;stop-delay=#</i></p>
<dd> Delay for automatic PCM stop is # microseconds from xrun</p>
<dt><i>-v, &#8211;verbose</i></p>
<dd> Show PCM structure and setup. This option is accumulative. The VU meter is displayed when this is given twice or three times.</p>
<dt><i>-V, &#8211;vumeter=TYPE</i></p>
<dd> Specifies the VU-meter type, either <i>stereo</i> or <i>mono</i>. The stereo VU-meter is available only for 2-channel stereo samples with interleaved format.</p>
<dt><i>-I, &#8211;separate-channels</i></p>
<dd> One file for each channel. This option disables max-file-time and use-strftime, and ignores SIGUSR1. The stereo VU meter is not available with separate channels.</p>
<dt><i>-P</i></p>
<dd> Playback. This is the default if the program is invoked by typing aplay.</p>
<dt><i>-C</i></p>
<dd> Record. This is the default if the program is invoked by typing arecord.</p>
<dt><i>-i, &#8211;interactive</i></p>
<dd> Allow interactive operation via stdin. Currently only pause/resume via space or enter key is implemented.</p>
<dt><i>-m, &#8211;chmap=ch1,ch2,&#8230;</i></p>
<dd> Give the channel map to override or follow. Pass channel position strings like <i>FL</i>, <i>FR</i>, etc. </p>
<p> If a device supports the override of the channel map, <code>aplay</code> tries to pass the given channel map. If it doesn&#8217;t support the channel map override but still it provides the channel map information, <code>aplay</code> tries to rearrange the channel order in the buffer to match with the returned channel map from the device.</p>
<dt><i>&#8211;disable-resample</i></p>
<dd> Disable automatic rate resample.</p>
<dt><i>&#8211;disable-channels</i></p>
<dd> Disable automatic channel conversions.</p>
<dt><i>&#8211;disable-format</i></p>
<dd> Disable automatic format conversions.</p>
<dt><i>&#8211;disable-softvol</i></p>
<dd> Disable software volume control (softvol).</p>
<dt><i>&#8211;test-position</i></p>
<dd> Test ring buffer position.</p>
<dt><i>&#8211;test-coef=&lt;coef&gt;</i></p>
<dd> Test coefficient for ring buffer position; default is 8. Expression for validation is: coef * (buffer_size / 2). Minimum value is 1.</p>
<dt><i>&#8211;test-nowait</i></p>
<dd> Do not wait for the ring buffer &#8211; eats the whole CPU.</p>
<dt><i>&#8211;max-file-time</i></p>
<dd> While recording, when the output file has been accumulating sound for this long, close it and open a new output file. Default is the maximum size supported by the file format: 2 GiB for WAV files. This option has no effect if &#8211;separate-channels is specified.</p>
<dt><i>&#8211;process-id-file &lt;file name&gt;</i></p>
<dd> aplay writes its process ID here, so other programs can send signals to it.</p>
<dt><i>&#8211;use-strftime</i></p>
<dd> When recording, interpret %-codes in the file name parameter using the strftime facility whenever the output file is opened. The important strftime codes are: %Y is the year, %m month, %d day of the month, %H hour, %M minute and %S second. In addition, %v is the file number, starting at 1. When this option is specified, intermediate directories for the output file are created automatically. This option has no effect if &#8211;separate-channels is specified.</p>
<dt><i>&#8211;dump-hw-params</i></p>
<dd> Dump hw_params of the device preconfigured status to stderr. The dump lists capabilities of the selected device such as supported formats, sampling rates, numbers of channels, period and buffer bytes/sizes/times. For raw device hw:X this option basically lists hardware capabilities of the soundcard.</p>
<dt><i>&#8211;fatal-errors</i></p>
<dd> Disables recovery attempts when errors (e.g. xrun) are encountered; the aplay process instead aborts immediately. </p>
</dl>
<h2>SIGNALS</h2>
<p> When recording, SIGINT, SIGTERM and SIGABRT will close the output file and exit. SIGUSR1 will close the output file, open a new one, and continue recording. However, SIGUSR1 does not work with &#8211;separate-channels. </p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>aplay -c 1 -t raw -r 22050 -f mu_law foobar</code></p>
<dd> will play the raw file &quot;foobar&quot; as a 22050-Hz, mono, 8-bit, Mu-Law .au file. </p>
<dt><code>arecord -d 10 -f cd -t wav -D copy foobar.wav</code></p>
<dd> will record foobar.wav as a 10-second, CD-quality wave file, using the PCM &quot;copy&quot; (which might be defined in the user&#8217;s .asoundrc file as: </p>
<pre><code>
pcm.copy
{
    type plug
        slave{
            pcm hw} route_policy copy
}
</code></pre>
<dt><code>arecord -t wav &#8211;max-file-time 30 mon.wav</code></p>
<dd> Record from the default audio source in monaural, 8,000 samples per second, 8 bits per sample. Start a new file every 30 seconds. File names are mon-nn.wav, where nn increases from 01. The file after mon-99.wav is mon-100.wav. </p>
<dt><code>arecord -f cd -t wav &#8211;max-file-time 3600 &#8211;use-strftime %Y/%m/%d/listen-%H-%M-%v.wav</code></p>
<dd> Record in stereo from the default audio source. Create a new file every hour. The files are placed in directories based on their start dates and have names which include their start times and file numbers. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code> <a href="/docs/linux/man/1-alsamixer/">alsamixer</a>(1), <a href="/docs/linux/man/1-amixer/">amixer</a>(1) </code> </p>
<h2>BUGS</h2>
<p> Note that .aiff files are not currently supported. </p>
<h2>AUTHOR</h2>
<p> <code>arecord</code> and <code>aplay</code> are by Jaroslav Kysela &lt;perex [at] perex.cz&gt; This document is by Paul Winkler &lt;zarmzarm [at] erols.com&gt;. Updated for Alsa 0.9 by James Tappin &lt;james [at] xena.uklinux.net&gt; </p>
<h2>Index</h2>
