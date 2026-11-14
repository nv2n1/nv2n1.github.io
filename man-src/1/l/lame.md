---
title: "lame(1)"
name: "lame"
section: "1"
letter: "l"
url: "/docs/linux/man/1-lame/"
description: "lame – create mp3 audio files"
---

<h2>NAME</h2>
<p> lame &#8211; create mp3 audio files</p>
<h2>SYNOPSIS</h2>
<p> lame [options] &lt;infile&gt; &lt;outfile&gt;</p>
<h2>DESCRIPTION</h2>
<p> LAME is a program which can be used to create compressed audio files. (Lame ain&#8217;t an MP3 encoder). These audio files can be played back by popular MP3 players such as mpg123 or madplay. To read from stdin, use &quot;-&quot; for &lt;infile&gt;. To write to stdout, use &quot;-&quot; for &lt;outfile&gt;.</p>
<h2>OPTIONS</h2>
<p> Input options:</p>
<dl>
<dt><code>-r</code></p>
<dd> Assume the input file is raw pcm. Sampling rate and mono/stereo/jstereo must be specified on the command line. For each stereo sample, LAME expects the input data to be ordered left channel first, then right channel. By default, LAME expects them to be signed integers with a bitwidth of 16. Without <code>-r,</code> LAME will perform several <i>fseek()&#8217;s</i> on the input file looking for WAV and AIFF headers.<br />
 Might not be available on your release.</p>
<dt><code>-x</code></p>
<dd> Swap bytes in the input file or output file when using <code>&#8211;decode.</code><br />
 For sorting out little endian/big endian type problems. If your encodings sounds like static, try this first.<br />
 Without using <code>-x,</code> LAME will treat input file as native endian.</p>
<dt><code>-s</code><i> sfreq</i></p>
<dd> <i>sfreq</i> = 8/11.025/12/16/22.05/24/32/44.1/48 </p>
<p> Required only for raw PCM input files. Otherwise it will be determined from the header of the input file. </p>
<p> LAME will automatically resample the input file to one of the supported MP3 samplerates if necessary.</p>
<dt><code>&#8211;bitwidth</code><i> n</i></p>
<dd> Input bit width per sample.<br />
 <i>n</i> = 8, 16, 24, 32 (default 16) </p>
<p> Required only for raw PCM input files. Otherwise it will be determined from the header of the input file.</p>
<dt><code>&#8211;signed</code></p>
<dd> Instructs LAME that the samples from the input are signed (the default for 16, 24 and 32 bits raw pcm data). </p>
<p> Required only for raw PCM input files.</p>
<dt><code>&#8211;unsigned</code></p>
<dd> Instructs LAME that the samples from the input are unsigned (the default for 8 bits raw pcm data, where 0x80 is zero). </p>
<p> Required only for raw PCM input files and only available at bitwidth 8.</p>
<dt><code>&#8211;little-endian</code></p>
<dd> Instructs LAME that the samples from the input are in little-endian form. </p>
<p> Required only for raw PCM input files.</p>
<dt><code>&#8211;big-endian</code></p>
<dd> Instructs LAME that the samples from the input are in big-endian form. </p>
<p> Required only for raw PCM input files.</p>
<dt><code>&#8211;mp2input</code></p>
<dd> Assume the input file is a MPEG Layer II (ie MP2) file.<br />
 If the filename ends in &quot;.mp2&quot; LAME will assume it is a MPEG Layer II file. For stdin or Layer II files which do not end in .mp2 you need to use this switch.</p>
<dt><code>&#8211;mp3input</code></p>
<dd> Assume the input file is a MP3 file.<br />
 Useful for downsampling from one mp3 to another. As an example, it can be useful for streaming through an IceCast server.<br />
 If the filename ends in &quot;.mp3&quot; LAME will assume it is an MP3. For stdin or MP3 files which do not end in .mp3 you need to use this switch.</p>
<dt><code>&#8211;nogap</code><i> file1 file2 &#8230;</i></p>
<dd> gapless encoding for a set of contiguous files</p>
<dt><code>&#8211;nogapout</code><i> dir</i></p>
<dd> output dir for gapless encoding (must precede &#8211;nogap) </p>
</dl>
<p> Operational options:</p>
<dl>
<dt><code>-m</code><i> mode</i></p>
<dd> <i>mode</i> = s, j, f, d, m, l, r </p>
<p> Joint-stereo is the default mode for stereo files with VBR when <code>-V</code> is more than 4 or fixed bitrates of 160kbs or less. At higher fixed bitrates or higher VBR settings, the default is stereo. </p>
<p> <code>(s)imple stereo </code><br />
 In this mode, the encoder makes no use of potentially existing correlations between the two input channels. It can, however, negotiate the bit demand between both channel, i.e. give one channel more bits if the other contains silence or needs less bits because of a lower complexity. </p>
<p> <code>(j)oint stereo</code><br />
 In this mode, the encoder will make use of a correlation between both channels. The signal will be matrixed into a sum (&quot;mid&quot;), computed by L+R, and difference (&quot;side&quot;) signal, computed by L-R, and more bits are allocated to the mid channel. This will effectively increase the bandwidth if the signal does not have too much stereo separation, thus giving a significant gain in encoding quality. </p>
<p> Using mid/side stereo inappropriately can result in audible compression artifacts. To much switching between mid/side and regular stereo can also sound bad. To determine when to switch to mid/side stereo, LAME uses a much more sophisticated algorithm than that described in the ISO documentation, and thus is safe to use in joint stereo mode. </p>
<p> <code>(f)orced MS stereo </code><br />
 This mode will force MS stereo on all frames. It is slightly faster than joint stereo, but it should be used only if you are sure that every frame of the input file has very little stereo separation. </p>
<p> <code>(d)ual mono</code><br />
 In this mode, the 2 channels will be totally independently encoded. Each channel will have exactly half of the bitrate. This mode is designed for applications like dual languages encoding (for example: English in one channel and French in the other). Using this encoding mode for regular stereo files will result in a lower quality encoding. </p>
<p> <code>(m)ono</code><br />
 The input will be encoded as a mono signal. If it was a stereo signal, it will be downsampled to mono. The downmix is calculated as the sum of the left and right channel, attenuated by 6 dB. </p>
<p> <code>(l)eft channel only</code><br />
 The input will be encoded as a mono signal. If it was a stereo signal, the left channel will be encoded only. </p>
<p> <code>(r)ight channel only</code><br />
 The input will be encoded as a mono signal. If it was a stereo signal, the right channel will be encoded only. </p>
<dt><code>-a</code></p>
<dd> Mix the stereo input file to mono and encode as mono.<br />
 The downmix is calculated as the sum of the left and right channel, attenuated by 6 dB. </p>
<p> This option is only needed in the case of raw PCM stereo input (because LAME cannot determine the number of channels in the input file). To encode a stereo PCM input file as mono, use <code>lame -m</code> <i>s</i> <code>-a.</code> </p>
<p> For WAV and AIFF input files, using <code>-m</code> will always produce a mono .mp3 file from both mono and stereo input.</p>
<dt><code>-d</code></p>
<dd> Allows the left and right channels to use different block size types.</p>
<dt><code>&#8211;freeformat</code></p>
<dd> Produces a free format bitstream. With this option, you can use <code>-b</code> with any bitrate higher than 8 kbps. </p>
<p> However, even if an mp3 decoder is required to support free bitrates at least up to 320 kbps, many players are unable to deal with it. </p>
<p> Tests have shown that the following decoders support free format:<br />
 <code>FreeAmp</code> up to 440 kbps<br />
 <code>in_mpg123</code> up to 560 kbps<br />
 <code>l3dec</code> up to 310 kbps<br />
 <code>LAME</code> up to 560 kbps<br />
 <code>MAD</code> up to 640 kbps</p>
<dt><code>&#8211;decode</code></p>
<dd> Uses LAME for decoding to a wav file. The input file can be any input type supported by encoding, including layer II files. LAME uses a bugfixed version of mpglib for decoding. </p>
<p> If <code>-t</code> is used (disable wav header), LAME will output raw pcm in native endian format. You can use <code>-x</code> to swap bytes order. </p>
<p> This option is not usable if the MP3 decoder was <code>explicitly</code> disabled in the build of LAME.</p>
<dt><code>-t</code></p>
<dd> Disable writing of the INFO Tag on encoding.<br />
 This tag in embedded in frame 0 of the MP3 file. It includes some information about the encoding options of the file, and in VBR it lets VBR aware players correctly seek and compute playing times of VBR files. </p>
<p> When <code>&#8211;decode</code> is specified (decode to WAV), this flag will disable writing of the WAV header. The output will be raw pcm, native endian format. Use <code>-x</code> to swap bytes.</p>
<dt><code>&#8211;comp</code><i> arg</i></p>
<dd> Instead of choosing bitrate, using this option, user can choose compression ratio to achieve.</p>
<dt><code>&#8211;scale</code><i> n</i></p>
<dd>
<dt><code>&#8211;scale-l</code><i> n</i></p>
<dd>
<dt><code>&#8211;scale-r</code><i> n</i></p>
<dd> Scales input (every channel, only left channel or only right channel) by <i>n.</i> This just multiplies the PCM data (after it has been converted to floating point) by <i>n. </i> </p>
<p> <i>n</i> &gt; 1: increase volume<br />
 <i>n</i> = 1: no effect<br />
 <i>n</i> &lt; 1: reduce volume </p>
<p> Use with care, since most MP3 decoders will truncate data which decodes to values greater than 32768.</p>
<dt><code>&#8211;replaygain-fast</code></p>
<dd> Compute ReplayGain fast but slightly inaccurately. </p>
<p> This computes &quot;Radio&quot; ReplayGain on the input data stream after user-specified volume-scaling and/or resampling. </p>
<p> The ReplayGain analysis does <i>not</i> affect the content of a compressed data stream itself, it is a value stored in the header of a sound file. Information on the purpose of ReplayGain and the algorithms used is available from <code><a rel="nofollow" href="http://www.replaygain.org/.">http://www.replaygain.org/.</a></code> </p>
<p> Only the &quot;RadioGain&quot; Replaygain value is computed, it is stored in the LAME tag. The analysis is performed with the reference volume equal to 89dB. Note: the reference volume has been changed from 83dB on transition from version 3.95 to 3.95.1. </p>
<p> This switch is enabled by default. </p>
<p> See also: <code>&#8211;replaygain-accurate, &#8211;noreplaygain</code></p>
<dt><code>&#8211;replaygain-accurate</code></p>
<dd> Compute ReplayGain more accurately and find the peak sample. </p>
<p> This enables decoding on the fly, computes &quot;Radio&quot; ReplayGain on the decoded data stream, finds the peak sample of the decoded data stream and stores it in the file.<br />
&nbsp;<wbr> The ReplayGain analysis does <i>not</i> affect the content of a compressed data stream itself, it is a value stored in the header of a sound file. Information on the purpose of ReplayGain and the algorithms used is available from <code><a rel="nofollow" href="http://www.replaygain.org/.">http://www.replaygain.org/.</a></code> </p>
<p>&nbsp;<wbr> By default, LAME performs ReplayGain analysis on the input data (after the user-specified volume scaling). This behavior might give slightly inaccurate results because the data on the output of a lossy compression/decompression sequence differs from the initial input data. When <code>&#8211;replaygain-accurate</code> is specified the mp3 stream gets decoded on the fly and the analysis is performed on the decoded data stream. Although theoretically this method gives more accurate results, it has several disadvantages:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> tests have shown that the difference between the ReplayGain values computed on the input data and decoded data is usually not greater than 0.5dB, although the minimum volume difference the human ear can perceive is about 1.0dB</p>
<dt>*</p>
<dd> decoding on the fly significantly slows down the encoding process</dl>
</dl>
<dl>
<dt>
<dd>
<p> The apparent advantage is that:</dl>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> with <code>&#8211;replaygain-accurate</code> the real peak sample is determined and stored in the file. The knowledge of the peak sample can be useful to decoders (players) to prevent a negative effect called &#8216;clipping&#8217; that introduces distortion into the sound.</dl>
</dl>
<dl>
<dt>
<dd>
&nbsp;<wbr> Only the &quot;RadioGain&quot; ReplayGain value is computed, it is stored in the LAME tag. The analysis is performed with the reference volume equal to 89dB. Note: the reference volume has been changed from 83dB on transition from version 3.95 to 3.95.1.<br />
&nbsp;<wbr> This option is not usable if the MP3 decoder was <code>explicitly</code> disabled in the build of LAME. (Note: if LAME is compiled without the MP3 decoder, ReplayGain analysis is performed on the input data after user-specified volume scaling).<br />
&nbsp;<wbr> See also: <code>&#8211;replaygain-fast, &#8211;noreplaygain &#8211;clipdetect</code></dl>
<dt><code>&#8211;noreplaygain</code></p>
<dd> Disable ReplayGain analysis. </p>
<p> By default ReplayGain analysis is enabled. This switch disables it. </p>
<p> See also: <code>&#8211;replaygain-fast, &#8211;replaygain-accurate</code></p>
<dt><code>&#8211;clipdetect</code></p>
<dd> Clipping detection. </p>
<p> Enable <code>&#8211;replaygain-accurate</code> and print a message whether clipping occurs and how far in dB the waveform is from full scale.<br />
&nbsp;<wbr>&nbsp;<wbr> This option is not usable if the MP3 decoder was <code>explicitly</code> disabled in the build of LAME. </p>
<p> See also: <code>&#8211;replaygain-accurate</code></p>
<dt><code>&#8211;preset type | [cbr] kbps</code></p>
<dd> Use one of the built-in presets. </p>
<p> Have a look at the PRESETS section below. </p>
<p> <code>&#8211;preset help</code> gives more infos about the the used options in these presets.</p>
<dt><code>&#8211;preset type | [cbr] kbps</code></p>
<dd> Use one of the built-in presets.</p>
<dt><code>&#8211;noasm type</code></p>
<dd> Disable specific assembly optimizations ( <code>mmx</code> / <code>3dnow</code> / <code>sse</code> ). Quality will not increase, only speed will be reduced. If you have problems running Lame on a Cyrix/Via processor, disabling mmx optimizations might solve your problem. </p>
</dl>
<p> Verbosity:</p>
<dl>
<dt><code>&#8211;disptime</code><i> n</i></p>
<dd> Set the delay in seconds between two display updates.</p>
<dt><code>&#8211;nohist</code></p>
<dd> By default, LAME will display a bitrate histogram while producing VBR mp3 files. This will disable that feature.<br />
 Histogram display might not be available on your release.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;silent</code></p>
<dd>
<dt><code>&#8211;quiet</code></p>
<dd> Do not print anything on the screen.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Print a lot of information on the screen.</p>
<dt><code>&#8211;help</code></p>
<dd> Display a list of available options. </p>
</dl>
<p> Noise shaping &amp; psycho acoustic algorithms:</p>
<dl>
<dt><code>-q</code><i> qual</i></p>
<dd> 0 &lt;= <i>qual</i> &lt;= 9 </p>
<p> Bitrate is of course the main influence on quality. The higher the bitrate, the higher the quality. But for a given bitrate, we have a choice of algorithms to determine the best scalefactors and Huffman encoding (noise shaping). </p>
<p> <code>-q 0:</code><br />
 use slowest &amp; best possible version of all algorithms. <code>-q 0</code> and <code>-q 1</code> are slow and may not produce significantly higher quality. </p>
<p> <code>-q 2:</code><br />
 recommended. Same as <code>-h.</code> </p>
<p> <code>-q 5:</code><br />
 default value. Good speed, reasonable quality. </p>
<p> <code>-q 7:</code><br />
 same as <code>-f.</code> Very fast, ok quality. Psycho acoustics are used for pre-echo &amp; M/S, but no noise shaping is done. </p>
<p> <code>-q 9:</code><br />
 disables almost all algorithms including psy-model. Poor quality.</p>
<dt><code>-h</code></p>
<dd> Use some quality improvements. Encoding will be slower, but the result will be of higher quality. The behavior is the same as the <code>-q 2</code> switch.<br />
 This switch is always enabled when using VBR.</p>
<dt><code>-f</code></p>
<dd> This switch forces the encoder to use a faster encoding mode, but with a lower quality. The behavior is the same as the <code>-q 7</code> switch. </p>
<p> Noise shaping will be disabled, but psycho acoustics will still be computed for bit allocation and pre-echo detection. </p>
</dl>
<p> CBR (constant bitrate, the default) options:</p>
<dl>
<dt><code>-b</code><i> n</i></p>
<dd> For MPEG-1 (sampling frequencies of 32, 44.1 and 48 kHz)<br />
 <i>n</i> = 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 </p>
<p> For MPEG-2 (sampling frequencies of 16, 22.05 and 24 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160 </p>
<p> For MPEG-2.5 (sampling frequencies of 8, 11.025 and 12 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64 </p>
<p> Default is 128 for MPEG1 and 64 for MPEG2.</p>
<dt><code>&#8211;cbr</code></p>
<dd> enforce use of constant bitrate </p>
</dl>
<p> ABR (average bitrate) options:</p>
<dl>
<dt><code>&#8211;abr</code><i> n</i></p>
<dd> Turns on encoding with a targeted average bitrate of n kbits, allowing to use frames of different sizes. The allowed range of <i>n</i> is 8 &#8211; 310, you can use any integer value within that range. </p>
<p> It can be combined with the <code>-b</code> and <code>-B</code> switches like: <code>lame &#8211;abr</code> <i>123</i> <code>-b</code> <i>64</i> <code>-B</code> <i>192 a.wav a.mp3</i> which would limit the allowed frame sizes between 64 and 192 kbits. </p>
<p> The use of <code>-B</code> is NOT RECOMMENDED. A 128 kbps CBR bitstream, because of the bit reservoir, can actually have frames which use as many bits as a 320 kbps frame. VBR modes minimize the use of the bit reservoir, and thus need to allow 320 kbps frames to get the same flexibility as CBR streams. </p>
</dl>
<p> VBR (variable bitrate) options:</p>
<dl>
<dt><code>-v</code></p>
<dd> use variable bitrate <code>(&#8211;vbr-new)</code></p>
<dt><code>&#8211;vbr-old</code></p>
<dd> Invokes the oldest, most tested VBR algorithm. It produces very good quality files, though is not very fast. This has, up through v3.89, been considered the &quot;workhorse&quot; VBR algorithm.</p>
<dt><code>&#8211;vbr-new</code></p>
<dd> Invokes the newest VBR algorithm. During the development of version 3.90, considerable tuning was done on this algorithm, and it is now considered to be on par with the original <code>&#8211;vbr-old. </code> It has the added advantage of being very fast (over twice as fast as <code>&#8211;vbr-old).</code></p>
<dt><code>-V</code><i> n</i></p>
<dd> 0 &lt;= <i>n</i> &lt;= 9<br />
 Enable VBR (Variable BitRate) and specifies the value of VBR quality (default = 4). 0 = highest quality. </p>
</dl>
<p> ABR and VBR options:</p>
<dl>
<dt><code>-b</code><i> bitrate</i></p>
<dd> For MPEG-1 (sampling frequencies of 32, 44.1 and 48 kHz)<br />
 <i>n</i> = 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 </p>
<p> For MPEG-2 (sampling frequencies of 16, 22.05 and 24 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160 </p>
<p> For MPEG-2.5 (sampling frequencies of 8, 11.025 and 12 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64 </p>
<p> Specifies the minimum bitrate to be used. However, in order to avoid wasted space, the smallest frame size available will be used during silences.</p>
<dt><code>-B</code><i> bitrate</i></p>
<dd> For MPEG-1 (sampling frequencies of 32, 44.1 and 48 kHz)<br />
 <i>n</i> = 32, 40, 48, 56, 64, 80, 96, 112, 128, 160, 192, 224, 256, 320 </p>
<p> For MPEG-2 (sampling frequencies of 16, 22.05 and 24 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64, 80, 96, 112, 128, 144, 160 </p>
<p> For MPEG-2.5 (sampling frequencies of 8, 11.025 and 12 kHz)<br />
 <i>n</i> = 8, 16, 24, 32, 40, 48, 56, 64 </p>
<p> Specifies the maximum allowed bitrate. </p>
<p> Note: If you own an mp3 hardware player build upon a MAS 3503 chip, you must set maximum bitrate to no more than 224 kpbs.</p>
<dt><code>-F</code></p>
<dd> Strictly enforce the <code>-b</code> option.<br />
 This is mainly for use with hardware players that do not support low bitrate mp3. </p>
<p> Without this option, the minimum bitrate will be ignored for passages of analog silence, i.e. when the music level is below the absolute threshold of human hearing (ATH). </p>
</dl>
<p> Experimental options:</p>
<dl>
<dt><code>-X</code><i> n</i></p>
<dd> 0 &lt;= <i>n</i> &lt;= 7 </p>
<p> When LAME searches for a &quot;good&quot; quantization, it has to compare the actual one with the best one found so far. The comparison says which one is better, the best so far or the actual. The <code>-X</code> parameter selects between different approaches to make this decision, <code>-X0</code> being the default mode: </p>
<p> <code>-X0 </code><br />
 The criteria are (in order of importance):<br />
 * less distorted scalefactor bands<br />
 * the sum of noise over the thresholds is lower<br />
 * the total noise is lower </p>
<p> <code>-X1</code><br />
 The actual is better if the maximum noise over all scalefactor bands is less than the best so far. </p>
<p> <code>-X2</code><br />
 The actual is better if the total sum of noise is lower than the best so far. </p>
<p> <code>-X3</code><br />
 The actual is better if the total sum of noise is lower than the best so far and the maximum noise over all scalefactor bands is less than the best so far plus 2dB. </p>
<p> <code>-X4</code><br />
 Not yet documented. </p>
<p> <code>-X5</code><br />
 The criteria are (in order of importance):<br />
 * the sum of noise over the thresholds is lower<br />
 * the total sum of noise is lower </p>
<p> <code>-X6 </code><br />
 The criteria are (in order of importance):<br />
 * the sum of noise over the thresholds is lower<br />
 * the maximum noise over all scalefactor bands is lower<br />
 * the total sum of noise is lower </p>
<p> <code>-X7 </code><br />
 The criteria are:<br />
 * less distorted scalefactor bands<br />
 or<br />
 * the sum of noise over the thresholds is lower</p>
<dt><code>-Y</code></p>
<dd> lets LAME ignore noise in sfb21, like in CBR </p>
</dl>
<p> MP3 header/stream options:</p>
<dl>
<dt><code>-e</code><i> emp</i></p>
<dd> <i>emp</i> = n, 5, c </p>
<p> n = (none, default)<br />
 5 = 0/15 microseconds<br />
 c = citt j.17 </p>
<p> All this does is set a flag in the bitstream. If you have a PCM input file where one of the above types of (obsolete) emphasis has been applied, you can set this flag in LAME. Then the mp3 decoder should de-emphasize the output during playback, although most decoders ignore this flag. </p>
<p> A better solution would be to apply the de-emphasis with a standalone utility before encoding, and then encode without <code>-e. </code></p>
<dt><code>-c</code></p>
<dd> Mark the encoded file as being copyrighted.</p>
<dt><code>-o</code></p>
<dd> Mark the encoded file as being a copy.</p>
<dt><code>-p</code></p>
<dd> Turn on CRC error protection.<br />
 It will add a cyclic redundancy check (CRC) code in each frame, allowing to detect transmission errors that could occur on the MP3 stream. However, it takes 16 bits per frame that would otherwise be used for encoding, and then will slightly reduce the sound quality.</p>
<dt><code>&#8211;nores</code></p>
<dd> Disable the bit reservoir. Each frame will then become independent from previous ones, but the quality will be lower.</p>
<dt><code>&#8211;strictly-enforce-ISO</code></p>
<dd> With this option, LAME will enforce the 7680 bit limitation on total frame size.<br />
 This results in many wasted bits for high bitrate encodings but will ensure strict ISO compatibility. This compatibility might be important for hardware players. </p>
</dl>
<p> Filter options:</p>
<dl>
<dt><code>&#8211;lowpass</code><i> freq</i></p>
<dd> Set a lowpass filtering frequency in kHz. Frequencies above the specified one will be cutoff.</p>
<dt><code>&#8211;lowpass-width</code><i> freq</i></p>
<dd> Set the width of the lowpass filter. The default value is 15% of the lowpass frequency.</p>
<dt><code>&#8211;highpass</code><i> freq</i></p>
<dd> Set an highpass filtering frequency in kHz. Frequencies below the specified one will be cutoff.</p>
<dt><code>&#8211;highpass-width</code><i> freq</i></p>
<dd> Set the width of the highpass filter in kHz. The default value is 15% of the highpass frequency.</p>
<dt><code>&#8211;resample</code><i> sfreq</i></p>
<dd> <i>sfreq</i> = 8, 11.025, 12, 16, 22.05, 24, 32, 44.1, 48<br />
 Select output sampling frequency (only supported for encoding).<br />
 If not specified, LAME will automatically resample the input when using high compression ratios. </p>
</dl>
<p> ID3 tag options:</p>
<dl>
<dt><code>&#8211;tt</code><i> title</i></p>
<dd> audio/song title (max 30 chars for version 1 tag)</p>
<dt><code>&#8211;ta</code><i> artist</i></p>
<dd> audio/song artist (max 30 chars for version 1 tag)</p>
<dt><code>&#8211;tl</code><i> album</i></p>
<dd> audio/song album (max 30 chars for version 1 tag)</p>
<dt><code>&#8211;ty</code><i> year</i></p>
<dd> audio/song year of issue (1 to 9999)</p>
<dt><code>&#8211;tc</code><i> comment</i></p>
<dd> user-defined text (max 30 chars for v1 tag, 28 for v1.1)</p>
<dt><code>&#8211;tn</code><i> track[/total]</i></p>
<dd> audio/song track number and (optionally) the total number of tracks on the original recording. (track and total each 1 to 255. Providing just the track number creates v1.1 tag, providing a total forces v2.0).</p>
<dt><code>&#8211;tg</code><i> genre</i></p>
<dd> audio/song genre (name or number in list)</p>
<dt><code>&#8211;add-id3v2</code></p>
<dd> force addition of version 2 tag</p>
<dt><code>&#8211;id3v1-only</code></p>
<dd> add only a version 1 tag</p>
<dt><code>&#8211;id3v2-only</code></p>
<dd> add only a version 2 tag</p>
<dt><code>&#8211;id3v2-latin1</code></p>
<dd> add following options in ISO-8859-1 text encoding.</p>
<dt><code>&#8211;id3v2-utf16</code></p>
<dd> add following options in unicode text encoding.</p>
<dt><code>&#8211;space-id3v1</code></p>
<dd> pad version 1 tag with spaces instead of nulls</p>
<dt><code>&#8211;pad-id3v2</code></p>
<dd> same as &#8211;pad-id3v2-size 128</p>
<dt><code>&#8211;pad-id3v2-size num</code></p>
<dd> adds version 2 tag, pad with extra &quot;num&quot; bytes</p>
<dt><code>&#8211;genre-list</code></p>
<dd> print alphabetically sorted ID3 genre list and exit</p>
<dt><code>&#8211;ignore-tag-errors</code></p>
<dd> ignore errors in values passed for tags, use defaults in case an error occurs </p>
</dl>
<p> Analysis options:</p>
<dl>
<dt><code>-g</code></p>
<dd> run graphical analysis on &lt;infile&gt;. &lt;infile&gt; can also be a .mp3 file. (This feature is a compile time option. Your binary may for speed reasons be compiled without this.) </p>
</dl>
<h2>ID3 TAGS</h2>
<p> LAME is able to embed ID3 v1, v1.1 or v2 tags inside the encoded MP3 file. This allows to have some useful information about the music track included inside the file. Those data can be read by most MP3 players. </p>
<p> Lame will smartly choose which tags to use. It will add ID3 v2 tags only if the input comments won&#8217;t fit in v1 or v1.1 tags, i.e. if they are more than 30 characters. In this case, both v1 and v2 tags will be added, to ensure reading of tags by MP3 players which are unable to read ID3 v2 tags. </p>
<h2>ENCODING MODES</h2>
<p> LAME is able to encode your music using one of its 3 encoding modes: constant bitrate (CBR), average bitrate (ABR) and variable bitrate (VBR).</p>
<dl>
<dt><code>Constant Bitrate (CBR)</code></p>
<dd> This is the default encoding mode, and also the most basic. In this mode, the bitrate will be the same for the whole file. It means that each part of your mp3 file will be using the same number of bits. The musical passage being a difficult one to encode or an easy one, the encoder will use the same bitrate, so the quality of your mp3 is variable. Complex parts will be of a lower quality than the easiest ones. The main advantage is that the final files size won&#8217;t change and can be accurately predicted.</p>
<dt><code>Average Bitrate (ABR)</code></p>
<dd> In this mode, you choose the encoder will maintain an average bitrate while using higher bitrates for the parts of your music that need more bits. The result will be of higher quality than CBR encoding but the average file size will remain predictable, so this mode is highly recommended over CBR. This encoding mode is similar to what is referred as vbr in AAC or Liquid Audio (2 other compression technologies).</p>
<dt><code>Variable bitrate (VBR)</code></p>
<dd> In this mode, you choose the desired quality on a scale from 9 (lowest quality/biggest distortion) to 0 (highest quality/lowest distortion). Then encoder tries to maintain the given quality in the whole file by choosing the optimal number of bits to spend for each part of your music. The main advantage is that you are able to specify the quality level that you want to reach, but the inconvenient is that the final file size is totally unpredictable. </p>
</dl>
<h2>PRESETS</h2>
<p> The <code>&#8211;preset</code> switches are aliases over LAME settings. </p>
<p> To activate these presets: </p>
<p> For VBR modes (generally highest quality):</p>
<dl>
<dt><code>&#8211;preset medium</code></p>
<dd> This preset should provide near transparency to most people on most music.</p>
<dt><code>&#8211;preset standard</code></p>
<dd> This preset should generally be transparent to most people on most music and is already quite high in quality.</p>
<dt><code>&#8211;preset extreme</code></p>
<dd> If you have extremely good hearing and similar equipment, this preset will generally provide slightly higher quality than the <code>standard</code> mode.</dl>
<p> For CBR 320kbps (highest quality possible from the <code>&#8211;preset</code> switches):</p>
<dl>
<dt><code>&#8211;preset insane</code></p>
<dd> This preset will usually be overkill for most people and most situations, but if you must have the absolute highest quality with no regard to filesize, this is the way to go.</dl>
<p> For ABR modes (high quality per given bitrate but not as high as VBR):</p>
<dl>
<dt><code>&#8211;preset kbps</code></p>
<dd> Using this preset will usually give you good quality at a specified bitrate. Depending on the bitrate entered, this preset will determine the optimal settings for that particular situation. While this approach works, it is not nearly as flexible as VBR, and usually will not attain the same level of quality as VBR at higher bitrates.</dl>
<p> The following options are also available for the corresponding profiles: </p>
<p> <code>standard|extreme</code><br />
 <code>cbr kbps</code> </p>
<dl>
<dt><code>cbr</code></p>
<dd> If you use the ABR mode (read above) with a significant bitrate such as 80, 96, 112, 128, 160, 192, 224, 256, 320, you can use the <code>cbr</code> option to force CBR mode encoding instead of the standard ABR mode. ABR does provide higher quality but CBR may be useful in situations such as when streaming an MP3 over the Internet may be important. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Fixed bit rate jstereo 128kbs encoding:</p>
<dl>
<dt>
<dd> <code>lame</code> <i>sample.wav sample.mp3</i> </p>
</dl>
<p> Fixed bit rate jstereo 128 kbps encoding, highest quality (recommended):</p>
<dl>
<dt>
<dd> <code>lame -h</code> <i>sample.wav sample.mp3</i> </p>
</dl>
<p> Fixed bit rate jstereo 112 kbps encoding:</p>
<dl>
<dt>
<dd> <code>lame -b</code> <i>112 sample.wav sample.mp3</i> </p>
</dl>
<p> To disable joint stereo encoding (slightly faster, but less quality at bitrates &lt;= 128 kbps):</p>
<dl>
<dt>
<dd> <code>lame -m</code> <i>s sample.wav sample.mp3</i> </p>
</dl>
<p> Fast encode, low quality (no psycho-acoustics):</p>
<dl>
<dt>
<dd> <code>lame -f</code> <i>sample.wav sample.mp3</i> </p>
</dl>
<p> Variable bitrate (use -V n to adjust quality/filesize):</p>
<dl>
<dt>
<dd> <code>lame -h -V</code> <i>6 sample.wav sample.mp3</i> </p>
</dl>
<p> Streaming mono 22.05 kHz raw pcm, 24 kbps output:</p>
<dl>
<dt>
<dd> <code>cat</code> <i>inputfile</i> <code>| lame -r -m</code> <i>m</i> <code>-b</code> <i>24</i> <code>-s</code> <i>22.05 &#8211; &#8211;</i> <code>&gt;</code> <i>output</i> </p>
</dl>
<p> Streaming mono 44.1 kHz raw pcm, with downsampling to 22.05 kHz:</p>
<dl>
<dt>
<dd> <code>cat</code> <i>inputfile</i> <code>| lame -r -m</code> <i>m</i> <code>-b</code> <i>24</i> <code>&#8211;resample</code> <i>22.05 &#8211; &#8211;</i> <code>&gt;</code> <i>output</i> </p>
</dl>
<p> Encode with the <code>standard</code> preset:</p>
<dl>
<dt>
<dd> <code>lame &#8211;preset standard</code> <i>sample.wav sample.mp3</i> </p>
</dl>
<h2>BUGS</h2>
<p> Probably there are some.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mpg123/">mpg123</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-madplay/">madplay</a></code>(1)<code>,</code> <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1)</p>
<h2>AUTHORS</h2>
<pre>
LAME originally developed by Mike Cheng and now maintained by
Mark Taylor, and the LAME team.
GPSYCHO psycho-acoustic model by Mark Taylor.
(See <a rel="nofollow" href="http://www.mp3dev.org/">http://www.mp3dev.org/</a>).
mpglib by Michael Hipp
Manual page by William Schelter, Nils Faerber, Alexander Leidinger,
and Rog&eacute;rio Brito.
</pre>
<h2>Index</h2>
