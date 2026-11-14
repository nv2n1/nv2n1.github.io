---
title: "oggenc(1)"
name: "oggenc"
section: "1"
letter: "o"
url: "/docs/linux/man/1-oggenc/"
description: "oggenc – encode audio into the Ogg Vorbis format"
---

<h2 class="name">NAME</h2>
<p> oggenc &#8211; encode audio into the Ogg Vorbis format</p>
<h2>SYNOPSIS</h2>
<p> <code>oggenc</code> [ <code>-hrQ</code> ] [ <code>-B</code> <i>raw input sample size</i> ] [ <code>-C</code> <i>raw input number of channels</i> ] [ <code>-R</code> <i>raw input samplerate</i> ] [ <code>-b</code> <i>nominal bitrate</i> ] [ <code>-m</code> <i>minimum bitrate</i> ] [ <code>-M</code> <i>maximum bitrate</i> ] [ <code>-q</code> <i>quality</i> ] [ <code>&#8211;resample </code> <i>frequency</i> ] [ <code>&#8211;downmix </code> ] [ <code>&#8211;scale</code> ] [ <code>-s</code> <i>serial</i> ] [ <code>-o</code> <i>output_file</i> ] [ <code>-n</code> <i>pattern</i> ] [ <code>-c</code> <i>extra_comment</i> ] [ <code>-a</code> <i>artist</i> ] [ <code>-t</code> <i>title</i> ] [ <code>-l</code> <i>album</i> ] [ <code>-G</code> <i>genre</i> ] [ <code>-L</code> <i>lyrics file</i> ] [ <code>-Y</code> <i>language-string</i> ] <i>input_files </i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>oggenc</code> reads audio data in either raw, Wave, or AIFF format and encodes it into an Ogg Vorbis stream. <code>oggenc</code> may also read audio data from FLAC and Ogg FLAC files depending upon compile-time options. If the input file &quot;-&quot; is specified, audio data is read from <i>stdin</i> and the Vorbis stream is written to <i>stdout</i> unless the <code>-o</code> option is used to redirect the output. By default, disk files are output to Ogg Vorbis files of the same name, with the extension changed to &quot;.ogg&quot; or &quot;.oga&quot;. This naming convention can be overridden by the <code>-o</code> option (in the case of one file) or the <code>-n</code> option (in the case of several files). Finally, if none of these are available, the output filename will be the input filename with the extension (that part after the final dot) replaced with ogg, so file.wav will become file.ogg.<br />
 Optionally, lyrics may be embedded in the Ogg file, if Kate support was compiled in.<br />
 Note that some old players mail fail to play streams with more than a single Vorbis stream (the so called &quot;Vorbis I&quot; simple profile). </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Show command help.</p>
<dt>-V, &#8211;version</p>
<dd> Show the version number.</p>
<dt>-r, &#8211;raw</p>
<dd> Assume input data is raw little-endian audio data with no header information. If other options are not specified, defaults to 44.1kHz stereo 16 bit. See next three options for how to change this.</p>
<dt>-B n, &#8211;raw-bits=n</p>
<dd> Sets raw mode input sample size in bits. Default is 16.</p>
<dt>-C n, &#8211;raw-chan=n</p>
<dd> Sets raw mode input number of channels. Default is 2.</p>
<dt>-R n, &#8211;raw-rate=n</p>
<dd> Sets raw mode input samplerate. Default is 44100.</p>
<dt>&#8211;raw-endianness n</p>
<dd> Sets raw mode endianness to big endian (1) or little endian (0). Default is little endian.</p>
<dt>&#8211;utf8 &nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></p>
<dd> Informs oggenc that the Vorbis Comments are already encoded as UTF-8. Useful in situations where the shell is using some other encoding.</p>
<dt>-k, &#8211;skeleton</p>
<dd> Add a Skeleton bitstream. Important if the output Ogg is intended to carry multiplexed or chained streams. Output file uses .oga as file extension.</p>
<dt>&#8211;ignorelength</p>
<dd> Support for Wave files over 4 GB and stdin data streams.</p>
<dt>-Q, &#8211;quiet</p>
<dd> Quiet mode. No messages are displayed.</p>
<dt>-b n, &#8211;bitrate=n</p>
<dd> Sets target bitrate to n (in kb/s). The encoder will attempt to encode at approximately this bitrate. By default, this remains a VBR encoding. See the &#8211;managed option to force a managed bitrate encoding at the selected bitrate.</p>
<dt>-m n, &#8211;min-bitrate=n</p>
<dd> Sets minimum bitrate to n (in kb/s). Enables bitrate management mode (see &#8211;managed).</p>
<dt>-M n, &#8211;max-bitrate=n</p>
<dd> Sets maximum bitrate to n (in kb/s). Enables bitrate management mode (see &#8211;managed).</p>
<dt>&#8211;managed</p>
<dd> Set bitrate management mode. This turns off the normal VBR encoding, but allows hard or soft bitrate constraints to be enforced by the encoder. This mode is much slower, and may also be lower quality. It is primarily useful for creating files for streaming.</p>
<dt>-q n, &#8211;quality=n</p>
<dd> Sets encoding quality to n, between -1 (very low) and 10 (very high). This is the default mode of operation, with a default quality level of 3. Fractional quality levels such as 2.5 are permitted. Using this option allows the encoder to select an appropriate bitrate based on your desired quality level.</p>
<dt>&#8211;resample n</p>
<dd> Resample input to the given sample rate (in Hz) before encoding. Primarily useful for downsampling for lower-bitrate encoding.</p>
<dt>&#8211;downmix</p>
<dd> Downmix input from stereo to mono (has no effect on non-stereo streams). Useful for lower-bitrate encoding.</p>
<dt>&#8211;scale</p>
<dd> Input scaling factor (helps with clipping inputs).</p>
<dt>&#8211;advanced-encode-option optionname=value</p>
<dd> Sets an advanced option. See the Advanced Options section for details.</p>
<dt>-s, &#8211;serial</p>
<dd> Forces a specific serial number in the output stream. This is primarily useful for testing.</p>
<dt>&#8211;discard-comments</p>
<dd> Prevents comments in FLAC and Ogg FLAC files from being copied to the output Ogg Vorbis file.</p>
<dt>-o output_file, &#8211;output=output_file</p>
<dd> Write the Ogg Vorbis stream to <i>output_file</i> (only valid if a single input file is specified). </p>
<dt>-n pattern, &#8211;names=pattern</p>
<dd> Produce filenames as this string, with %g, %a, %l, %n, %t, %d replaced by genre, artist, album, track number, title, and date, respectively (see below for specifying these). Also, %% gives a literal %.</p>
<dt>-X, &#8211;name-remove=s</p>
<dd> Remove the specified characters from parameters to the -n format string. This is useful to ensure legal filenames are generated.</p>
<dt>-P, &#8211;name-replace=s</p>
<dd> Replace characters removed by &#8211;name-remove with the characters specified. If this string is shorter than the &#8211;name-remove list, or is not specified, the extra characters are just removed. The default settings for this option, and the -X option above, are platform specific (and chosen to ensure legal filenames are generated for each platform). </p>
<dt>-c comment, &#8211;comment comment</p>
<dd> Add the string <i>comment</i> as an extra comment. This may be used multiple times, and all instances will be added to each of the input files specified. The argument should be in the form &quot;tag=value&quot;. </p>
<dt>-a artist, &#8211;artist artist</p>
<dd> Set the artist comment field in the comments to <i>artist.</i> </p>
<dt>-G genre, &#8211;genre genre</p>
<dd> Set the genre comment field in the comments to <i>genre.</i> </p>
<dt>-d date, &#8211;date date</p>
<dd> Sets the date comment field to the given value. This should be the date of recording. </p>
<dt>-N n, &#8211;tracknum n</p>
<dd> Sets the track number comment field to the given value. </p>
<dt>-t title, &#8211;title title</p>
<dd> Set the track title comment field to <i>title.</i> </p>
<dt>-l album, &#8211;album album</p>
<dd> Set the album comment field to <i>album.</i> </p>
<dt>-L filename, &#8211;lyrics filename</p>
<dd> Loads lyrics from <i>filename</i> and encodes them into a Kate stream multiplexed with the Vorbis stream. Lyrics may be in LRC or SRT format, and should be encoded in UTF-8 or plain ASCII. Other encodings may be converted using tools such as iconv or recode. Alternatively, the same system as for comments will be used for conversion between encodings. So called &quot;enhanced LRC&quot; files are supported, and a simple karaoke style change will be saved with the lyrics. For more complex karaoke setups, <code><a href="/docs/linux/man/1-kateenc/">kateenc</a>(1)</code> should be used instead. When embedding lyrics, the default output file extention is &quot;.oga&quot;. Note that adding lyrics to a stream will automatically enable Skeleton (see the <code>-k</code> option for more information about Skeleton). </p>
<dt>-Y language-string, &#8211;lyrics-language language-string</p>
<dd> Sets the language for the corresponding lyrics file to <i>language-string.</i> This should be an ISO 639-1 language code (eg, &quot;en&quot;), or a RFC 3066 language tag (eg, &quot;en_US&quot;), <code>not</code> a free form language name. Players will typically recognize this standard tag and display the language name in your own language. Note that the maximum length of this tag is 15 characters.</dl>
<p> Note that the <code>-a</code>, <code>-t</code>, <code>-l</code>, <code>-L</code>, and <code>-Y</code> options can be given multiple times. They will be applied, one to each file, in the order given. If there are fewer album, title, or artist comments given than there are input files, <code>oggenc</code> will reuse the final one for the remaining files, and issue a warning in the case of repeated titles. </p>
<h2>ADVANCED ENCODER OPTIONS</h2>
<p> Oggenc allows you to set a number of advanced encoder options using the <code>&#8211;advanced-encode-option</code> option. These are intended for very advanced users only, and should be approached with caution. They may significantly degrade audio quality if misused. Not all these options are currently documented. </p>
<dl>
<dt>lowpass_frequency=N</p>
<dd> Set the lowpass frequency to N kHz. </p>
<dt>impulse_noisetune=N</p>
<dd> Set a noise floor bias N (range from -15. to 0.) for impulse blocks. A negative bias instructs the encoder to pay special attention to the crispness of transients in the encoded audio. The tradeoff for better transient response is a higher bitrate. </p>
<dt>bitrate_hard_max=N</p>
<dd> Set the allowed bitrate maximum for the encoded file to N kilobits per second. This bitrate may be exceeded only when there is spare bits in the bit reservoir; if the bit reservoir is exhausted, frames will be held under this value. This setting must be used with &#8211;managed to have any effect. </p>
<dt>bitrate_hard_min=N</p>
<dd> Set the allowed bitrate minimum for the encoded file to N kilobits per second. This bitrate may be underrun only when the bit reservoir is not full; if the bit reservoir is full, frames will be held over this value; if it impossible to add bits constructively, the frame will be padded with zeroes. This setting must be used with &#8211;managed to have any effect. </p>
<dt>bit_reservoir_bits=N</p>
<dd> Set the total size of the bit reservoir to N bits; the default size of the reservoir is equal to the nominal number of bits coded in one second (eg, a nominal 128kbps file will have a bit reservoir of 128000 bits by default). This option must be used with &#8211;managed to have any effect and affects only minimum and maximum bitrate management. Average bitrate encoding with no hard bitrate boundaries does not use a bit reservoir. </p>
<dt>bit_reservoir_bias=N</p>
<dd> Set the behavior bias of the bit reservoir (range: 0. to 1.). When set closer to 0, the bitrate manager attempts to hoard bits for future use in sudden bitrate increases (biasing toward better transient reproduction). When set closer to 1, the bitrate manager neglects transients in favor using bits for homogenous passages. In the middle, the manager uses a balanced approach. The default setting is .2, thus biasing slightly toward transient reproduction. </p>
<dt>bitrate_average=N</p>
<dd> Set the average bitrate for the file to N kilobits per second. When used without hard minimum or maximum limits, this option selects reservoirless Average Bit Rate encoding, where the encoder attempts to perfectly track a desired bitrate, but imposes no strict momentary fluctuation limits. When used along with a minimum or maximum limit, the average bitrate still sets the average overall bitrate of the file, but will work within the bounds set by the bit reservoir. When the min, max and average bitrates are identical, oggenc produces Constant Bit Rate Vorbis data. </p>
<dt>bitrate_average_damping=N</p>
<dd> Set the reaction time for the average bitrate tracker to N seconds. This number represents the fastest reaction the bitrate tracker is allowed to make to hold the bitrate to the selected average. The faster the reaction time, the less momentary fluctuation in the bitrate but (generally) the lower quality the audio output. The slower the reaction time, the larger the ABR fluctuations, but (generally) the better the audio. When used along with min or max bitrate limits, this option directly affects how deep and how quickly the encoder will dip into its bit reservoir; the higher the number, the more demand on the bit reservoir. </p>
<p> The setting must be greater than zero and the useful range is approximately .05 to 10. The default is .75 seconds. </p>
<dt>disable_coupling</p>
<dd> Disable use of channel coupling for multichannel encoding. At present, the encoder will normally use channel coupling to further increase compression with stereo and 5.1 inputs. This option forces the encoder to encode each channel fully independently using neither lossy nor lossless coupling. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Simplest version. Produces output as somefile.ogg:</p>
<dl>
<dt>
<dd> oggenc somefile.wav</dl>
<p> Specifying an output filename:</p>
<dl>
<dt>
<dd> oggenc somefile.wav -o out.ogg</dl>
<p> Specifying a high-quality encoding averaging 256 kbps (but still VBR):</p>
<dl>
<dt>
<dd> oggenc infile.wav -b 256 -o out.ogg</dl>
<p> Specifying a maximum and average bitrate, and enforcing these:</p>
<dl>
<dt>
<dd> oggenc infile.wav &#8211;managed -b 128 -M 160 -o out.ogg</dl>
<p> Specifying quality rather than bitrate (to a very high quality mode):</p>
<dl>
<dt>
<dd> oggenc infile.wav -q 6 -o out.ogg</dl>
<p> Downsampling and downmixing to 11 kHz mono before encoding:</p>
<dl>
<dt>
<dd> oggenc &#8211;resample 11025 &#8211;downmix infile.wav -q 1 -o out.ogg</dl>
<p> Adding some info about the track:</p>
<dl>
<dt>
<dd> oggenc somefile.wav -t &quot;The track title&quot; -a &quot;artist who performed this&quot; -l &quot;name of album&quot; -c &quot;OTHERFIELD=contents of some other field not explicitly supported&quot;</dl>
<p> Adding embedded lyrics:</p>
<dl>
<dt>
<dd> oggenc somefile.wav &#8211;lyrics lyrics.lrc &#8211;lyrics-language en -o out.oga</dl>
<p> This encodes the three files, each with the same artist/album tag, but with different title tags on each one. The string given as an argument to -n is used to generate filenames, as shown in the section above. This example gives filenames like &quot;The Tea Party &#8211; Touch.ogg&quot;:</p>
<dl>
<dt>
<dd> oggenc -b 192 -a &quot;The Tea Party&quot; -l &quot;Triptych&quot; -t &quot;Touch&quot; track01.wav -t &quot;Underground&quot; track02.wav -t &quot;Great Big Lie&quot; track03.wav -n &quot;%a &#8211; %t.ogg&quot;</dl>
<p> Encoding from stdin, to stdout (you can also use the various tagging options, like -t, -a, -l, etc.):</p>
<dl>
<dt>
<dd> oggenc &#8211;</dl>
<h2>AUTHORS</h2>
<dl>
<dt>Program Author:</p>
<dd>
 Michael Smith &lt;msmith [at] xiph.org&gt; </p>
<dt>Manpage Author:</p>
<dd>
 Stan Seibert &lt;indigo [at] aztec.asu.edu&gt; </p>
</dl>
<h2>BUGS</h2>
<p> Reading type 3 Wave files (floating point samples) probably doesn&#8217;t work other than on Intel (or other 32 bit, little endian machines). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-vorbiscomment/">vorbiscomment</a></code>(1), <code><a href="/docs/linux/man/1-ogg123/">ogg123</a></code>(1), <code><a href="/docs/linux/man/1-oggdec/">oggdec</a></code>(1), <code><a href="/docs/linux/man/1-flac/">flac</a></code>(1), <code><a href="/docs/linux/man/1-speexenc/">speexenc</a></code>(1), <code><a href="/docs/linux/man/1-ffmpeg2theora/">ffmpeg2theora</a></code>(1), <code><a href="/docs/linux/man/1-kateenc/">kateenc</a></code>(1) </p>
<h2>Index</h2>
