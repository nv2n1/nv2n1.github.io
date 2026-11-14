---
title: "madplay(1)"
name: "madplay"
section: "1"
letter: "m"
url: "/docs/linux/man/1-madplay/"
description: "madplay – decode and play MPEG audio stream(s)"
---

<h2>NAME</h2>
<p> madplay &#8211; decode and play MPEG audio stream(s)</p>
<h2>SYNOPSIS</h2>
<p> <code>madplay</code> [<i>options</i>] <i>file</i> &#8230;<br />
 <code>madplay</code> [<i>options</i>] <code>-o</code> [<i>type</i><code>:</code>]<i>path</i> <i>file</i> &#8230;</p>
<h2>DESCRIPTION</h2>
<p> <code>madplay</code> is a command-line MPEG audio decoder and player based on the MAD library (<i>libmad</i>). </p>
<p> MAD is a high-quality MPEG audio decoder. It currently supports MPEG-1 and the MPEG-2 extension to Lower Sampling Frequencies, as well as the so-called MPEG 2.5 format. All three audio layers (Layer I, Layer II, and Layer III a.k.a. MP3) are fully implemented. </p>
<p> Among the special features of MAD are 24-bit PCM resolution and 100% fixed-point (integer) computation. Since MAD is implemented entirely without the use of floating point arithmetic, it performs especially well on architectures without an FPU. </p>
<p> MAD does not yet support MPEG-2 multichannel audio (although it should be backward compatible with such streams) nor does it currently support AAC. </p>
<p> By default <code>madplay</code> reads and decodes one or more input <i>file</i>s containing MPEG audio data and plays them on the native audio device. If the input file is a single dash (-), data is read from standard input. </p>
<p> Decoded output may optionally be redirected to a file instead of being played on the audio device by using the <code>-o</code> (<code>&#8211;output</code>) option. </p>
<p> For each <i>file</i>, <code>madplay</code> will also attempt to read and display ID3 tag information. The supported tag versions are ID3v1, ID3v1.1, ID3v2.2, ID3v2.3, and ID3v2.4. If a tag contains relative volume adjustment information (RVA2), <code>madplay</code> will use the information to adjust the master volume for output. This behavior can be changed with the <code>-A</code> (<code>&#8211;adjust-volume</code>) and <code>-G</code> (<code>&#8211;replay-gain</code>) options. </p>
<p> If the <code>-T</code> (<code>&#8211;show-tags-only</code>) option is used, decoding is not performed but tag information is still displayed. When used in conjunction with <code>-v</code> (<code>&#8211;verbose</code>), encoder as well as ID3 tags are shown.</p>
<h2>OPTIONS</h2>
<h3>Verbosity</h3>
<dl>
<dt><code>-v</code> or <code>&#8211;verbose</code></p>
<dd> Generally show more information than the default. During decoding, show information about the stream including playing time, audio layer, bit rate, sampling frequency, and stereo mode.</p>
<dt><code>-q</code> or <code>&#8211;quiet</code></p>
<dd> Generally show less information than the default. Do not show any information during decoding except warnings.</p>
<dt><code>-Q</code> or <code>&#8211;very-quiet</code></p>
<dd> Generally show no information except severe errors. Do not show any information or warnings during decoding.</p>
<dt><code>&#8211;display-time=</code><i>mode</i></p>
<dd> Set the default verbose time display mode to <i>mode</i>, which must be one of <code>remaining</code>, <code>current</code>, or <code>overall</code>. This is only relevant with <code>-v</code> (<code>&#8211;verbose</code>). See <code>&#8211;tty-control</code> below for details on changing the time display mode during playback.</dl>
<h3>Decoding</h3>
<dl>
<dt><code>&#8211;downsample</code></p>
<dd> Reduce the decoded sampling frequency 2:1. This also reduces the computational overhead of the decoder.</p>
<dt><code>-i</code> or <code>&#8211;ignore-crc</code></p>
<dd> Ignore CRC information in the audio stream. This causes frames with CRC errors to be decoded and played anyway. This option is not recommended, but since some encoders have been known to generate bad CRC information, this option is a work-around to play streams from such encoders.</p>
<dt><code>&#8211;ancillary-output=</code><i>path</i></p>
<dd> Write ancillary data from the MPEG audio stream to <i>path</i>. If <i>path</i> is a single dash (-), the data will be written to standard output. Bits from the ancillary data stream are packed into octets; if any bits remain, the final octet will be padded with zero bits. See the <code>NOTES</code> section below for further information about this option.</dl>
<h3>Audio Output</h3>
<dl>
<dt><code>-o</code> or <code>&#8211;output=</code>[<i>type</i><code>:</code>]<i>path</i></p>
<dd> Direct output to <i>path</i>, rather than playing audio on the native audio device. The format of the output is specified by <i>type</i> which can be any of the supported output formats (see <code>Output Formats</code> below.) If a format is not specified, one will be inferred from <i>path</i>. If <i>path</i> is a single dash (-), the output will be written to standard output.</p>
<dt><code>-b</code> or <code>&#8211;bit-depth=</code><i>depth</i></p>
<dd> Request an output precision of <i>depth</i> bits per sample. Higher bit depths yield higher quality sound. Typical bit depths are 8, 16, 24, and 32, however other depths may also be possible. Whether the request can be honored depends on the capabilities of the audio device or output format. See the <code>NOTES</code> section below for further details about this option.</p>
<dt><code>-R</code> or <code>&#8211;sample-rate=</code><i>hertz</i></p>
<dd> Request an output sampling frequency of <i>hertz</i> samples per second (Hz). The sample rate must be in the range 1000 to 65535 Hz. Whether the request can be honored depends on the capabilities of the audio device or output format. If the effective rate is not the same as the rate of the decoded audio, output may be resampled, possibly resulting in lower quality sound.</p>
<dt><code>-d</code> or <code>&#8211;no-dither</code></p>
<dd> Do not dither output PCM samples. This may result in lower quality sound but is useful for analyzing output from the decoder.</p>
<dt><code>&#8211;fade-in</code>[<code>=</code><i>duration</i>]</p>
<dd> Gradually fade-in the audio from each file over <i>duration</i>. If not specified, the default duration is <code>0:05</code> (five seconds.)</p>
<dt><code>-a</code> or <code>&#8211;attenuate=</code><i>decibels</i> or <code>&#8211;amplify=</code><i>decibels</i></p>
<dd> Attenuate or amplify the signal by <i>decibels</i> (dB). The signal is attenuated if the decibel value is negative; it is amplified if the value is positive. The value must be in the range -175 to +18 dB. The value may be fractional, e.g. -1.5 dB. A value of 0 dB will leave the signal unchanged. Each step of 6 dB will approximately halve (in the negative direction) or double (in the positive direction) the strength of the signal.</p>
<dt><code>-A</code> or <code>&#8211;adjust-volume=</code><i>decibels</i></p>
<dd> Adjust the relative volume for all files. This option overrides any per-file volume adjustment settings. For example, <code>-A0</code> may be used to ignore relative volume adjustments given by ID3 tags. Relative volume adjustments specified by this option or by ID3 tags are used as the base volume against which the signal is further attenuated or amplified using the <code>-a</code> (<code>&#8211;attenuate</code>, <code>&#8211;amplify</code>) option or keyboard controls. This option cannot be used together with <code>-G</code> (<code>&#8211;replay-gain</code>).</p>
<dt><code>-G</code> or <code>&#8211;replay-gain</code>[<code>=</code><i>profile</i>]</p>
<dd> Enable Replay Gain volume adjustments. Replay Gain information contained in the decoded files (if any) is used to make volume adjustments for output. The <i>profile</i> may be one of <code>radio</code> (the default) or <code>audiophile</code>. See the <code>NOTES</code> section below for further details. When Replay Gain is enabled, a default pre-amp gain of +6 dB is also applied; this can be changed with the <code>-a</code> (<code>&#8211;attenuate</code>, <code>&#8211;amplify</code>) option.</dl>
<h3>Channel Selection</h3>
<p> For dual channel streams, an output channel should be selected. If one is not selected, the first (left) channel will be used. </p>
<p> For stereo streams, making a channel selection other than stereo will cause the output to become monaural.</p>
<dl>
<dt><code>-1</code> or <code>&#8211;left</code></p>
<dd> Output the first (left) channel only.</p>
<dt><code>-2</code> or <code>&#8211;right</code></p>
<dd> Output the second (right) channel only.</p>
<dt><code>-m</code> or <code>&#8211;mono</code></p>
<dd> Mix the left and right channels together.</p>
<dt><code>-S</code> or <code>&#8211;stereo</code></p>
<dd> Force stereo output, even if the stream is single or dual channel.</dl>
<h3>Playback</h3>
<dl>
<dt><code>-s</code> or <code>&#8211;start=</code><i>time</i></p>
<dd> Begin playing at <i>time</i>, given as an offset from the beginning of the first file (<code>0:00:00</code>), seeking as necessary.</p>
<dt><code>-t</code> or <code>&#8211;time=</code><i>duration</i></p>
<dd> Stop playback after the playing time of the output audio equals <i>duration</i>.</p>
<dt><code>-z</code> or <code>&#8211;shuffle</code></p>
<dd> Randomize the list of files given on the command line for playback.</p>
<dt><code>-r</code> or <code>&#8211;repeat</code>[<code>=</code><i>max</i>]</p>
<dd> Play the input files <i>max</i> times, or indefinitely. Playback can be stopped prematurely by giving a time limit with the <code>-t</code> (<code>&#8211;time</code>) option. If <code>-z</code> (<code>&#8211;shuffle</code>) is also used, the files will be continuously shuffled and repeated in such a way that the same file is not played again until at least half of the other files have played in the interim.</p>
<dt><code>&#8211;tty-control</code></p>
<dd> Enable keyboard controls during playback. This is the default unless standard input is not a terminal, output is redirected with <code>-o</code> (<code>&#8211;output</code>), or either of <code>-q</code> (<code>&#8211;quiet</code>) or <code>-Q</code> (<code>&#8211;very-quiet</code>) is given. The keyboard controls are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>P</code></p>
<dd> Pause; press any key to resume.</p>
<dt><code>S</code></p>
<dd> Stop; press any key to replay the current file from the beginning.</p>
<dt><code>F</code></p>
<dd> Forward; advance to the next file.</p>
<dt><code>B</code></p>
<dd> Back; replay the current file, unless it has been playing for less than 4 seconds, in which case replay the previous file.</p>
<dt><code>T</code></p>
<dd> Time display; change the time display mode. This only works with <code>-v</code> (<code>&#8211;verbose</code>). The display mode alternates among overall playing time, current time remaining, and current playing time.</p>
<dt><code>+</code></p>
<dd> Increase gain; increase the audio output gain by 0.5 dB.</p>
<dt><code>&#8211;</code></p>
<dd> Decrease gain; decrease the audio output gain by 0.5 dB.</p>
<dt><code>Q</code></p>
<dd> Quit; stop decoding and exit.</dl>
</dl>
<dt><code>&#8211;no-tty-control</code></p>
<dd> Disable keyboard controls during playback. This is the default when standard input is not a terminal, output is redirected with <code>-o</code> (<code>&#8211;output</code>), or either of <code>-q</code> (<code>&#8211;quiet</code>) or <code>-Q</code> (<code>&#8211;very-quiet</code>) is given.</dl>
<h3>Miscellaneous</h3>
<dl>
<dt><code>-T</code> or <code>&#8211;show-tags-only</code></p>
<dd> Show ID3 and/or encoder tags from the input <i>file</i>s but do not otherwise decode or play any audio. By default only ID3 tags are shown (if any). With <code>-v</code> (<code>&#8211;verbose</code>), all tags are shown. Encoder tags recognized by <code>madplay</code> include the Xing VBR header tag and the header tag format written by <code><a href="/docs/linux/man/1-lame/">lame</a></code>(1).</p>
<dt><code>-V</code> or <code>&#8211;version</code></p>
<dd> Display the effective version and build options for <code>madplay</code> and exit.</p>
<dt><code>&#8211;license</code></p>
<dd> Display copyright, license, and warranty information and exit.</p>
<dt><code>-h</code> or <code>&#8211;help</code></p>
<dd> Display usage information and exit.</dl>
<h2>Output Formats</h2>
<p> Other than playing on the native audio device, the following output formats are supported:</p>
<dl>
<dt><code>cdda</code></p>
<dd> CD audio, 16-bit big-endian 44100 Hz stereo PCM, padded to 2352-byte block boundary (<code>*.cdr</code>, <code>*.cda</code>)</p>
<dt><code>aiff</code></p>
<dd> Audio IFF, [16-bit] PCM (<code>*.aif</code>, <code>*.aiff</code>)</p>
<dt><code>wave</code></p>
<dd> Microsoft RIFF/WAVE, [16-bit] PCM (<code>*.wav</code>)</p>
<dt><code>snd</code></p>
<dd> Sun/NeXT audio, 8-bit ISDN &mu;-law (<code>*.au</code>, <code>*.snd</code>)</p>
<dt><code>raw</code></p>
<dd> binary [16-bit] host-endian linear PCM, stereo interleaved</p>
<dt><code>hex</code></p>
<dd> ASCII hexadecimal [24-bit] linear PCM, stereo interleaved, one sample per output line</p>
<dt><code>esd</code></p>
<dd> Enlightened Sound Daemon (EsounD) [16-bit] (give speaker host as <i>path</i>)</p>
<dt><code>null</code></p>
<dd> no output (usually for testing or timing the decoder)</dl>
<p> Default bit depths shown in square brackets can be changed with the <code>-b</code> (<code>&#8211;bit-depth</code>) option. </p>
<p> Note that EsounD support requires the <i>libesd</i> library.</p>
<h2>Time Specifications</h2>
<p> For options which accept a time or duration argument, the following time specifications are recognized:</p>
<dl>
<dt><i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i><code>.</code><i>ddd</i></p>
<dd> Hours, minutes, seconds, and decimal fractions of a second. This specification is flexible; <i>hh</i><code>:</code><i>mm</i><code>:</code><i>ss</i>, <i>mmm</i><code>:</code><i>ss</i>, <code>:</code><i>ss</i>, <i>sss</i><code>.</code><i>ddd</i>, <code>.</code><i>ddd</i>, and <i>ssss</i> are all acceptable. The component values are not constrained to any particular range or number of digits.</p>
<dt><i>frac</i><code>/</code><i>unit</i></p>
<dd> A length of time specified as a rational number, in seconds. This can be used for sample-granularity, for example <code>32/44100</code> for 32 samples, assuming a 44100 Hz sample frequency.</p>
<dt><i>time1</i><code>+</code><i>time2</i></p>
<dd> A composite time made by adding two time values together. This permits mixing the above specification forms.</dl>
<p> The resolution of any time value cannot exceed 1/352800000 seconds.</p>
<h2>DIAGNOSTICS</h2>
<dl>
<dt><code>error: frame #: lost synchronization</code></p>
<dd> If encountered at the beginning of a file, this means the file contains something other than an ID3v2 tag before the MPEG audio data. If encountered in the middle of a file, it may mean the file is corrupt. This message is most commonly encountered, however, at the end of a file if the file contains an ID3v1 tag that is not aligned to an MPEG audio frame boundary. In this case, the message is harmless and may be ignored.</dl>
<dl>
<dt><code>error: frame #: bad main_data_begin pointer</code></p>
<dd> This message can occur while decoding a Layer III stream that has been cut or spliced without preserving its bit reservoir. The affected frame cannot be properly decoded, but will be used to help restore the bit reservoir for following frames.</dl>
<p> Most other messages indicate a deficiency in the input stream. </p>
<p> When a frame cannot be properly decoded, a concealment strategy is used as follows:</p>
<dl>
<dt>&bull;</p>
<dd> If the previous frame was properly decoded, it is repeated in place of the current frame.</p>
<dt>&bull;</p>
<dd> If the previous frame was <i>not</i> properly decoded, the current frame is muted.</dl>
<h2>NOTES</h2>
<h3>Output Precision</h3>
<p> Because MAD produces samples with a precision greater than 24 bits, by default <code>madplay</code> will dither the samples to the precision of the output format. This produces high quality audio that generally sounds superior to the output of a simple rounding algorithm. However, dithering may unfavorably affect an analytic examination of the output, and therefore it may be disabled by using the <code>-d</code> (<code>&#8211;no-dither</code>) option. </p>
<p> The actual precision of output samples can be requested with the <code>-b</code> (<code>&#8211;bit-depth</code>) option. Whether the request can be honored depends on the capabilities of the audio device or output format. If this option is not specified, a typical default depth will be used (often 16) or in the case of output to an audio device, the highest bit depth determined to work reliably with the device will be used. </p>
<p> Note that bit depths greater than 24 are effectively the same as 24-bit precision samples padded to the requested depth.</p>
<h3>Ancillary Data</h3>
<p> MPEG audio streams contain an ancillary data stream in addition to audio data. Most often this does not contain any useful information and may simply consist of padding bits. The MPEG-2 extension to multichannel audio uses part of this ancillary stream to convey multichannel information; presently MAD does not interpret such data. </p>
<p> For applications which have uses for the stream, ancillary data can be extracted with the <code>&#8211;ancillary-output</code> option.</p>
<h3>Replay Gain</h3>
<p> <code>madplay</code> optionally supports the Replay Gain proposed standard with the <code>-G</code> (<code>&#8211;replay-gain</code>) option to make compensating volume adjustments when playing decoded audio from different sources. There are two Replay Gain profiles: <code>radio</code> strives to make gain adjustments that give all tracks equal loudness, while <code>audiophile</code> attempts to give ideal listening loudness. These adjustments are relative to a reference of 83 dB SPL. </p>
<p> A pre-amp gain is also used in conjunction with Replay Gain to achieve the overall desired loudness. When Replay Gain is enabled, this pre-amp gain defaults to +6 dB, however it can be changed with the <code>-a</code> (<code>&#8211;attenuate</code>, <code>&#8211;amplify</code>) option or keyboard controls. </p>
<p> Note that when enabled, Replay Gain overrides any relative volume adjustments specified by ID3 tags (RVA2). Replay Gain is also incompatible with the <code>-A</code> (<code>&#8211;adjust-volume</code>) option; any attempt to use it will be ignored. </p>
<p> Replay Gain information is read either from an ID3 tag (RGAD) or from an encoder tag written by <code><a href="/docs/linux/man/1-lame/">lame</a></code>(1). If both are present, the information in the ID3 tag takes precedence. In accordance with the proposed standard, if the requested Replay Gain profile is not available but the alternate is, the alternate is used instead. </p>
<p> Due to an unfortunate heresy, versions of <code><a href="/docs/linux/man/1-lame/">lame</a></code>(1) since 3.95.1 write Replay Gain information using a reference of 89 dB SPL instead of the 83 dB specified in the Replay Gain proposed standard. To compensate, <code>madplay</code> automatically subtracts 6 dB from the Replay Gain values read from such tags. </p>
<p> Note that <code>madplay</code> does not yet support hard limiting as suggested by the Replay Gain proposed standard; nor does it automatically reduce the pre-amp gain to avoid clipping.</p>
<h2>CONFORMING TO</h2>
<p> MAD conforms to Part 3 of the ISO/IEC 11172 (MPEG-1) international standard for decoding MPEG audio. In addition, MAD supports the extension to Lower Sampling Frequencies (LSF) as defined in Part 3 of ISO/IEC 13818 (MPEG-2). </p>
<p> The output from MAD has been tested and found to satisfy the ISO/IEC 11172-4 computational accuracy requirements for compliance. In most configurations, MAD is a <i>Full Layer III ISO/IEC 11172-3 audio decoder</i> as defined by the standard. </p>
<p> The ID3 tag parsing library used by <code>madplay</code> conforms to the ID3v2.4.0 informal standard. </p>
<p> With the exception of the clipping prevention provisions, Replay Gain support provided by <code>madplay</code> is in accordance with the Replay Gain proposed standard published on July 10, 2001 by David Robinson.</p>
<h2>BUGS</h2>
<p> The resampling algorithm used by <code>madplay</code> is one of a linear interpolation, and does not produce optimum quality sound. </p>
<p> The granularity of start and stop times (<code>&#8211;start</code> and <code>&#8211;time</code>) is not yet as fine as this document suggests.</p>
<h2>AUTHOR</h2>
<p> Robert Leslie &lt;rob [at] mars.org&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-lame/">lame</a></code>(1), <code><a href="/docs/linux/man/1-normalize/">normalize</a></code>(1), <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) </p>
<h2>Index</h2>
