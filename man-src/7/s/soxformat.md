---
title: "soxformat(7)"
name: "soxformat"
section: "7"
letter: "s"
url: "/docs/linux/man/7-soxformat/"
description: "SoX – Sound eXchange, the Swiss Army knife of audio manipulation"
---

<p>SoX &#8211; Sound eXchange, the Swiss Army knife of audio manipulation</p>
<h2>Description</h2>
<p>This manual describes SoX supported file formats and audio device types; the SoX manual set starts with <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1). </p>
<p> Format types that can SoX can determine by a filename extension are listed with their names preceded by a dot. Format types that are optionally built into SoX are marked `(optional)&#8217;. </p>
<p> Format types that can be handled by an external library via an optional pseudo file type (currently <code>sndfile</code> or <code>ffmpeg</code>) are marked e.g. `(also with <code>-t sndfile</code>)&#8217;. This might be useful if you have a file that doesn&#8217;t work with SoX&#8217;s default format readers and writers, and there&#8217;s an external reader or writer for that format. </p>
<p> To see if SoX has support for an optional format or device, enter <code>sox -h</code> and look for its name under the list: `AUDIO FILE FORMATS&#8217; or `AUDIO DEVICE DRIVERS&#8217;.</p>
<h3>SOX FORMATS &amp; DEVICE DRIVERS</h3>
<p><code>.raw</code> (also with <code>-t sndfile</code>), <code>.f32</code>, <code>.f64</code>, <code>.s8</code>, <code>.s16</code>, <code>.s24</code>, <code>.s32</code>,<br />
 <code>.u8</code>, <code>.u16</code>, <code>.u24</code>, <code>.u32</code>, <code>.ul</code>, <code>.al</code>, <code>.lu</code>, <code>.la</code> </p>
<dl>
<dt>&nbsp;<wbr></p>
<dd>Raw (headerless) audio files. For <code>raw</code>, the sample rate and the data encoding must be given using command-line format options; for the other listed types, the sample rate defaults to 8kHz (but may be overridden), and the data encoding is defined by the given suffix. Thus <code>f32</code> and <code>f64</code> indicate files encoded as 32 and 64-bit (IEEE single and double precision) floating point PCM respectively; <code>s8</code>, <code>s16</code>, <code>s24</code>, and <code>s32</code> indicate 8, 16, 24, and 32-bit signed integer PCM respectively; <code>u8</code>, <code>u16</code>, <code>u24</code>, and <code>u32</code> indicate 8, 16, 24, and 32-bit unsigned integer PCM respectively; <code>ul</code> indicates `&mu;-law&#8217; (8-bit), <code>al</code> indicates `A-law&#8217; (8-bit), and <code>lu</code> and <code>la</code> are inverse bit order `&mu;-law&#8217; and inverse bit order `A-law&#8217; respectively. For all raw formats, the number of channels defaults to 1 (but may be overridden). </p>
<p> Headerless audio files on a SPARC computer are likely to be of format <code>ul</code>; on a Mac, they&#8217;re likely to be <code>u8</code> but with a sample rate of 11025 or 22050 Hz. </p>
<p> See <code>.ima</code> and <code>.vox</code> for raw ADPCM formats, and <code>.cdda</code> for raw CD digital audio.</dl>
<p> <code>.f4</code>, <code>.f8</code>, <code>.s1</code>, <code>.s2</code>, <code>.s3</code>, <code>.s4</code>,<br />
 <code>.u1</code>, <code>.u2</code>, <code>.u3</code>, <code>.u4</code>, <code>.sb</code>, <code>.sw</code>, <code>.sl</code>, <code>.ub</code>, <code>.uw</code> </p>
<dl>
<dt>&nbsp;<wbr></p>
<dd>Deprecated aliases for <code>f32</code>, <code>f64</code>, <code>s8</code>, <code>s16</code>, <code>s24</code>, <code>s32</code>,<br />
 <code>u8</code>, <code>u16</code>, <code>u24</code>, <code>u32</code>, <code>s8</code>, <code>s16</code>, <code>s32</code>, <code>u8</code>, and <code>u16</code> respectively.</p>
<dt><code>.8svx</code> (also with <code>-t sndfile</code>)</p>
<dd>Amiga 8SVX musical instrument description format.</p>
<dt><code>.aiff</code>, <code>.aif</code> (also with <code>-t sndfile</code>)</p>
<dd>AIFF files as used on old Apple Macs, Apple IIc/IIgs and SGI. SoX&#8217;s AIFF support does not include multiple audio chunks, or the 8SVX musical instrument description format. AIFF files are multimedia archives and can have multiple audio and picture chunks &#8211; you may need a separate archiver to work with them. With Mac OS X, AIFF has been superseded by CAF.</p>
<dt><code>.aiffc</code>, <code>.aifc</code> (also with <code>-t sndfile</code>)</p>
<dd>AIFF-C is a format based on AIFF that was created to allow handling compressed audio. It can also handle little endian uncompressed linear data that is often referred to as <code>sowt </code> encoding. This encoding has also become the defacto format produced by modern Macs as well as iTunes on any platform. AIFF-C files produced by other applications typically have the file extension .aif and require looking at its header to detect the true format. The <code>sowt</code> encoding is the only encoding that SoX can handle with this format. </p>
<p> AIFF-C is defined in DAVIC 1.4 Part 9 Annex B. This format is referred from ARIB STD-B24, which is specified for Japanese data broadcasting. Any private chunks are not supported.</p>
<dt><code>alsa</code> (optional)</p>
<dd>Advanced Linux Sound Architecture device driver; supports both playing and recording audio. ALSA is only used in Linux-based operating systems, though these often support OSS (see below) as well. Examples: </p>
<pre> sox infile -t alsa
 sox infile -t alsa default
 sox infile -t alsa plughw:0,0
 sox -2 -t alsa hw:1 outfile</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.amb</code></p>
<dd>Ambisonic B-Format: a specialisation of <code>.wav</code> with between 3 and 16 channels of audio for use with an Ambisonic decoder. See <a rel="nofollow" href="http://www.ambisonia.com/Members/mleese/file-format-for-b-format">http://www.ambisonia.com/Members/mleese/file-format-for-b-format</a> for details. It is up to the user to get the channels together in the right order and at the correct amplitude.</p>
<dt><code>.amr-nb</code> (optional)</p>
<dd>Adaptive Multi Rate &#8211; Narrow Band speech codec; a lossy format used in 3rd generation mobile telephony and defined in 3GPP TS 26.071 et al. </p>
<p> AMR-NB audio has a fixed sampling rate of 8 kHz and supports encoding to the following bit-rates (as selected by the <code>-C</code> option): 0 = 4.75 kbit/s, 1 = 5.15 kbit/s, 2 = 5.9 kbit/s, 3 = 6.7 kbit/s, 4 = 7.4 kbit/s 5 = 7.95 kbit/s, 6 = 10.2 kbit/s, 7 = 12.2 kbit/s.</p>
<dt><code>.amr-wb</code> (optional)</p>
<dd>Adaptive Multi Rate &#8211; Wide Band speech codec; a lossy format used in 3rd generation mobile telephony and defined in 3GPP TS 26.171 et al. </p>
<p> AMR-WB audio has a fixed sampling rate of 16 kHz and supports encoding to the following bit-rates (as selected by the <code>-C</code> option): 0 = 6.6 kbit/s, 1 = 8.85 kbit/s, 2 = 12.65 kbit/s, 3 = 14.25 kbit/s, 4 = 15.85 kbit/s 5 = 18.25 kbit/s, 6 = 19.85 kbit/s, 7 = 23.05 kbit/s, 8 = 23.85 kbit/s.</p>
<dt><code>ao</code> (optional)</p>
<dd>Xiph.org&#8217;s Audio Output device driver; works only for playing audio. It supports a wide range of devices and sound systems &#8211; see its documentation for the full range. For the most part, SoX&#8217;s use of libao cannot be configured directly; instead, libao configuration files must be used. </p>
<p> The filename specified is used to determine which libao plugin to use. Normally, you should specify `default&#8217; as the filename. If that doesn&#8217;t give the desired behavior then you can specify the short name for a given plugin (such as <code>pulse</code> for pulse audio plugin). Examples: </p>
<pre> sox infile -t ao
 sox infile -t ao default
 sox infile -t ao pulse</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1) and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.au</code>, <code>.snd</code> (also with <code>-t sndfile</code>)</p>
<dd>Sun Microsystems AU files. There are many types of AU file; DEC has invented its own with a different magic number and byte order. To write a DEC file, use the <code>-L</code> option with the output file options. </p>
<p> Some .au files are known to have invalid AU headers; these are probably original Sun &mu;-law 8000 Hz files and can be dealt with using the <code>.ul</code> format (see below). </p>
<p> It is possible to override AU file header information with the <code>-r</code> and <code>-c</code> options, in which case SoX will issue a warning to that effect.</p>
<dt><code>.avr</code></p>
<dd>Audio Visual Research format; used by a number of commercial packages on the Mac.</p>
<dt><code>.caf</code> (optional)</p>
<dd>Apple&#8217;s Core Audio File format.</p>
<dt><code>.cdda</code>, <code>.cdr</code></p>
<dd>`Red Book&#8217; Compact Disc Digital Audio (raw audio). CDDA has two audio channels formatted as 16-bit signed integers (big endian)at a sample rate of 44.1 kHz. The number of (stereo) samples in each CDDA track is always a multiple of 588.</p>
<dt><code>coreaudio</code> (optional)</p>
<dd>Mac OSX CoreAudio device driver: supports both playing and recording audio. If a filename is not specific or if the name is &quot;default&quot; then the default audio device is selected. Any other name will be used to select a specific device. The valid names can be seen in the System Preferences-&gt;Sound menu and then under the Output and Input tabs. </p>
<p> Examples: </p>
<pre> sox infile -t coreaudio
 sox infile -t coreaudio default
 sox infile -t coreaudio &quot;Internal Speakers&quot;</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.cvsd</code>, <code>.cvs</code></p>
<dd>Continuously Variable Slope Delta modulation. A headerless format used to compress speech audio for applications such as voice mail. This format is sometimes used with bit-reversed samples &#8211; the <code>-X</code> format option can be used to set the bit-order.</p>
<dt><code>.cvu</code></p>
<dd>Continuously Variable Slope Delta modulation (unfiltered). This is an alternative handler for CVSD that is unfiltered but can be used with any bit-rate. E.g. </p>
<pre> sox infile outfile.cvu rate 28k
 play -r 28k outfile.cvu sinc -3.4k</pre>
<dt><code>.dat</code></p>
<dd>Text Data files. These files contain a textual representation of the sample data. There is one line at the beginning that contains the sample rate, and one line that contains the number of channels. Subsequent lines contain two or more numeric data intems: the time since the beginning of the first sample and the sample value for each channel. </p>
<p> Values are normalized so that the maximum and minimum are 1 and -1. This file format can be used to create data files for external programs such as FFT analysers or graph routines. SoX can also convert a file in this format back into one of the other file formats. </p>
<p> Example containing only 2 stereo samples of silence: </p>
<pre> ; Sample Rate 8012
 ; Channels 2
 0 0 0
 0.00012481278 0 0</pre>
<dt><code>.dvms</code>, <code>.vms</code></p>
<dd>Used in Germany to compress speech audio for voice mail. A self-describing variant of <code>cvsd</code>.</p>
<dt><code>.fap</code> (optional)</p>
<dd>See <code>.paf</code>.</p>
<dt><code>ffmpeg</code> (optional)</p>
<dd>This is a pseudo-type that forces ffmpeg to be used. The actual file type is deduced from the file name (it cannot be used on stdio). It can read a wide range of audio files, not all of which are documented here, and also the audio track of many video files (including AVI, WMV and MPEG). At present only the first audio track of a file can be read.</p>
<dt><code>.flac</code> (optional; also with <code>-t sndfile</code>)</p>
<dd>Xiph.org&#8217;s Free Lossless Audio CODEC compressed audio. FLAC is an open, patent-free CODEC designed for compressing music. It is similar to MP3 and Ogg Vorbis, but lossless, meaning that audio is compressed in FLAC without any loss in quality. </p>
<p> SoX can read native FLAC files (.flac) but not Ogg FLAC files (.ogg). [But see <code>.ogg</code> below for information relating to support for Ogg Vorbis files.] </p>
<p> SoX can write native FLAC files according to a given or default compression level. 8 is the default compression level and gives the best (but slowest) compression; 0 gives the least (but fastest) compression. The compression level is selected using the <code>-C</code> option [see <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1)] with a whole number from 0 to 8.</p>
<dt><code>.fssd</code></p>
<dd>An alias for the <code>.u8</code> format.</p>
<dt><code>.gsrt</code></p>
<dd>Grandstream ring-tone files. Whilst this file format can contain A-Law, &mu;-law, GSM, G.722, G.723, G.726, G.728, or iLBC encoded audio, SoX supports reading and writing only A-Law and &mu;-law. E.g. </p>
<pre> sox music.wav -t gsrt ring.bin
 play ring.bin</pre>
<dt><code>.gsm</code> (optional; also with <code>-t sndfile</code>)</p>
<dd>GSM 06.10 Lossy Speech Compression. A lossy format for compressing speech which is used in the Global Standard for Mobile telecommunications (GSM). It&#8217;s good for its purpose, shrinking audio data size, but it will introduce lots of noise when a given audio signal is encoded and decoded multiple times. This format is used by some voice mail applications. It is rather CPU intensive.</p>
<dt><code>.hcom</code></p>
<dd>Macintosh HCOM files. These are Mac FSSD files with Huffman compression.</p>
<dt><code>.htk</code></p>
<dd>Single channel 16-bit PCM format used by HTK, a toolkit for building Hidden Markov Model speech processing tools.</p>
<dt><code>.ircam</code> (also with <code>-t sndfile</code>)</p>
<dd>Another name for <code>.sf</code>.</p>
<dt><code>.ima</code> (also with <code>-t sndfile</code>)</p>
<dd>A headerless file of IMA ADPCM audio data. IMA ADPCM claims 16-bit precision packed into only 4 bits, but in fact sounds no better than <code>.vox</code>.</p>
<dt><code>.lpc</code>, <code>.lpc10</code></p>
<dd>LPC-10 is a compression scheme for speech developed in the United States. See <a rel="nofollow" href="http://www.arl.wustl.edu/~jaf/lpc/">http://www.arl.wustl.edu/~jaf/lpc/</a> for details. There is no associated file format, so SoX&#8217;s implementation is headerless.</p>
<dt><code>.mat</code>, <code>.mat4</code>, <code>.mat5</code> (optional)</p>
<dd>Matlab 4.2/5.0 (respectively GNU Octave 2.0/2.1) format (.mat is the same as .mat4).</p>
<dt><code>.m3u</code></p>
<dd>A <i>playlist</i> format; contains a list of audio files. SoX can read, but not write this file format. See [1] for details of this format.</p>
<dt><code>.maud</code></p>
<dd>An IFF-conforming audio file type, registered by MS MacroSystem Computer GmbH, published along with the `Toccata&#8217; sound-card on the Amiga. Allows 8bit linear, 16bit linear, A-Law, &mu;-law in mono and stereo.</p>
<dt><code>.mp3</code>, <code>.mp2</code> (optional read, optional write)</p>
<dd>MP3 compressed audio; MP3 (MPEG Layer 3) is a part of the patent-encumbered MPEG standards for audio and video compression. It is a lossy compression format that achieves good compression rates with little quality loss. </p>
<p> Because MP3 is patented, SoX cannot be distributed with MP3 support without incurring the patent holder&#8217;s fees. Users who require SoX with MP3 support must currently compile and build SoX with the MP3 libraries (LAME &amp; MAD) from source code, or, in some cases, obtain pre-built dynamically loadable libraries. </p>
<p> When reading MP3 files, up to 28 bits of precision is stored although only 16 bits is reported to user. This is to allow default behavior of writing 16 bit output files. A user can specify a higher precision for the output file to prevent lossing this extra information. MP3 output files will use up to 24 bits of precision while encoding. </p>
<p> MP3 compression parameters can be selected using SoX&#8217;s <code>-C</code> option as follows (note that the current syntax is subject to change): </p>
<p> The primary parameter to the LAME encoder is the bit rate. If the value of the <code>-C</code> value is a positive integer, it&#8217;s taken as the bitrate in kbps (e.g. if you specify 128, it uses 128 kbps). </p>
<p> The second most important parameter is probably &quot;quality&quot; (really performance), which allows balancing encoding speed vs. quality. In LAME, 0 specifies highest quality but is very slow, while 9 selects poor quality, but is fast. (5 is the default and 2 is recommended as a good trade-off for high quality encodes.) </p>
<p> Because the <code>-C</code> value is a float, the fractional part is used to select quality. 128.2 selects 128 kbps encoding with a quality of 2. There is one problem with this approach. We need 128 to specify 128 kbps encoding with default quality, so 0 means use default. Instead of 0 you have to use .01 (or .99) to specify the highest quality (128.01 or 128.99). </p>
<p> LAME uses bitrate to specify a constant bitrate, but higher quality can be achieved using Variable Bit Rate (VBR). VBR quality (really size) is selected using a number from 0 to 9. Use a value of 0 for high quality, larger files, and 9 for smaller files of lower quality. 4 is the default. </p>
<p> In order to squeeze the selection of VBR into the the <code>-C</code> value float we use negative numbers to select VRR. -4.2 would select default VBR encoding (size) with high quality (speed). One special case is 0, which is a valid VBR encoding parameter but not a valid bitrate. Compression value of 0 is always treated as a high quality vbr, as a result both -0.2 and 0.2 are treated as highest quality VBR (size) and high quality (speed). </p>
<p> See also <code>Ogg Vorbis</code> for a similar format.</p>
<dt><code>.mp4</code>, <code>.m4a</code> (optional)</p>
<dd>MP4 compressed audio. MP3 (MPEG 4) is part of the MPEG standards for audio and video compression. See <code>mp3</code> for more information.</p>
<dt><code>.nist</code> (also with <code>-t sndfile</code>)</p>
<dd>See <code>.sph</code>.</p>
<dt><code>.ogg</code>, <code>.vorbis</code> (optional)</p>
<dd>Xiph.org&#8217;s Ogg Vorbis compressed audio; an open, patent-free CODEC designed for music and streaming audio. It is a lossy compression format (similar to MP3, VQF &amp; AAC) that achieves good compression rates with a minimum amount of quality loss. </p>
<p> SoX can decode all types of Ogg Vorbis files, and can encode at different compression levels/qualities given as a number from -1 (highest compression/lowest quality) to 10 (lowest compression, highest quality). By default the encoding quality level is 3 (which gives an encoded rate of approx. 112kbps), but this can be changed using the <code>-C</code> option (see above) with a number from -1 to 10; fractional numbers (e.g. 3.6) are also allowed. Decoding is somewhat CPU intensive and encoding is very CPU intensive. </p>
<p> See also <code>.mp3</code> for a similar format.</p>
<dt><code>oss</code> (optional)</p>
<dd>Open Sound System /dev/dsp device driver; supports both playing and recording audio. OSS support is available in Unix-like operating systems, sometimes together with alternative sound systems (such as ALSA). Examples: </p>
<pre> sox infile -t oss
 sox infile -t oss /dev/dsp
 sox -2 -t oss /dev/dsp outfile</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.paf</code>, <code>.fap</code> (optional)</p>
<dd>Ensoniq PARIS file format (big and little-endian respectively).</p>
<dt><code>.pls</code></p>
<dd>A <i>playlist</i> format; contains a list of audio files. SoX can read, but not write this file format. See [2] for details of this format. </p>
<p> Note: SoX support for SHOUTcast PLS relies on <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) and is only partially supported: it&#8217;s necessary to specify the audio type manually, e.g. </p>
<pre> play -t mp3 &quot;<a rel="nofollow" href="http://a.server/pls?rn=265">http://a.server/pls?rn=265</a>&amp;file=filename.pls&quot;</pre>
<p>and SoX does not know about alternative servers &#8211; hit Ctrl-C twice in quick succession to quit.</p>
<dt><code>.prc</code></p>
<dd>Psion Record. Used in Psion EPOC PDAs (Series 5, Revo and similar) for System alarms and recordings made by the built-in Record application. When writing, SoX defaults to A-law, which is recommended; if you must use ADPCM, then use the <code>-i</code> switch. The sound quality is poor because Psion Record seems to insist on frames of 800 samples or fewer, so that the ADPCM CODEC has to be reset at every 800 frames, which causes the sound to glitch every tenth of a second.</p>
<dt><code>pulseaudio</code> (optional)</p>
<dd>PulseAudio driver; supports both playing and recording of audio. PulseAudio is a cross platform networked sound server. If a file name is specified with this driver, it is ignored. Examples: </p>
<pre> sox infile -t pulseaudio
 sox infile -t pulseaudio default</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.pvf</code> (optional)</p>
<dd>Portable Voice Format.</p>
<dt><code>.sd2</code> (optional)</p>
<dd>Sound Designer 2 format.</p>
<dt><code>.sds</code> (optional)</p>
<dd>MIDI Sample Dump Standard.</p>
<dt><code>.sf</code> (also with <code>-t sndfile</code>)</p>
<dd>IRCAM SDIF (Institut de Recherche et Coordination Acoustique/Musique Sound Description Interchange Format). Used by academic music software such as the CSound package, and the MixView sound sample editor.</p>
<dt><code>.sln</code></p>
<dd>Asterisk PBX `signed linear&#8217; 8khz, 16-bit signed integer, little-endian raw format.</p>
<dt><code>.sph</code>, <code>.nist</code> (also with <code>-t sndfile</code>)</p>
<dd>SPHERE (SPeech HEader Resources) is a file format defined by NIST (National Institute of Standards and Technology) and is used with speech audio. SoX can read these files when they contain &mu;-law and PCM data. It will ignore any header information that says the data is compressed using <i>shorten</i> compression and will treat the data as either &mu;-law or PCM. This will allow SoX and the command line <i>shorten</i> program to be run together using pipes to encompasses the data and then pass the result to SoX for processing.</p>
<dt><code>.smp</code></p>
<dd>Turtle Beach SampleVision files. SMP files are for use with the PC-DOS package SampleVision by Turtle Beach Softworks. This package is for communication to several MIDI samplers. All sample rates are supported by the package, although not all are supported by the samplers themselves. Currently loop points are ignored.</p>
<dt><code>.snd</code></p>
<dd>See <code>.au</code>, <code>.sndr</code> and <code>.sndt</code>.</p>
<dt><code>sndfile</code> (optional)</p>
<dd>This is a pseudo-type that forces libsndfile to be used. For writing files, the actual file type is then taken from the output file name; for reading them, it is deduced from the file.</p>
<dt><code>sndio</code> (optional)</p>
<dd>OpenBSD audio device driver; supports both playing and recording audio. </p>
<pre> sox infile -t sndio</pre>
<p>See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.sndr</code></p>
<dd>Sounder files. An MS-DOS/Windows format from the early &#8217;90s. Sounder files usually have the extension `.SND&#8217;.</p>
<dt><code>.sndt</code></p>
<dd>SoundTool files. An MS-DOS/Windows format from the early &#8217;90s. SoundTool files usually have the extension `.SND&#8217;.</p>
<dt><code>.sou</code></p>
<dd>An alias for the <code>.u8</code> raw format.</p>
<dt><code>.sox</code></p>
<dd>SoX&#8217;s native uncompressed PCM format, intended for storing (or piping) audio at intermediate processing points (i.e. between SoX invocations). It has much in common with the popular WAV, AIFF, and AU uncompressed PCM formats, but has the following specific characteristics: the PCM samples are always stored as 32 bit signed integers, the samples are stored (by default) as `native endian&#8217;, and the number of samples in the file is recorded as a 64-bit integer. Comments are also supported. </p>
<p> See `Special Filenames&#8217; in <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) for examples of using the <code>.sox</code> format with `pipes&#8217;.</p>
<dt><code>sunau</code> (optional)</p>
<dd>Sun /dev/audio device driver; supports both playing and recording audio. For example: </p>
<pre> sox infile -t sunau /dev/audio</pre>
<p>or </p>
<pre> sox infile -t sunau -U -c 1 /dev/audio</pre>
<p>for older sun equipment. </p>
<p> See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.txw</code></p>
<dd>Yamaha TX-16W sampler. A file format from a Yamaha sampling keyboard which wrote IBM-PC format 3.5&quot; floppies. Handles reading of files which do not have the sample rate field set to one of the expected by looking at some other bytes in the attack/loop length fields, and defaulting to 33 kHz if the sample rate is still unknown.</p>
<dt><code>.vms</code></p>
<dd>See <code>.dvms</code>.</p>
<dt><code>.voc</code> (also with <code>-t sndfile</code>)</p>
<dd>Sound Blaster VOC files. VOC files are multi-part and contain silence parts, looping, and different sample rates for different chunks. On input, the silence parts are filled out, loops are rejected, and sample data with a new sample rate is rejected. Silence with a different sample rate is generated appropriately. On output, silence is not detected, nor are impossible sample rates. SoX supports reading (but not writing) VOC files with multiple blocks, and files containing &mu;-law, A-law, and 2/3/4-bit ADPCM samples.</p>
<dt><code>.vorbis</code></p>
<dd>See <code>.ogg</code>.</p>
<dt><code>.vox</code> (also with <code>-t sndfile</code>)</p>
<dd>A headerless file of Dialogic/OKI ADPCM audio data commonly comes with the extension .vox. This ADPCM data has 12-bit precision packed into only 4-bits. </p>
<p> Note: some early Dialogic hardware does not always reset the ADPCM encoder at the start of each vox file. This can result in clipping and/or DC offset problems when it comes to decoding the audio. Whilst little can be done about the clipping, a DC offset can be removed by passing the decoded audio through a high-pass filter, e.g.: </p>
<pre> sox input.vox output.wav highpass 10</pre>
<dt><code>.w64</code> (optional)</p>
<dd>Sonic Foundry&#8217;s 64-bit RIFF/WAV format.</p>
<dt><code>.wav</code> (also with <code>-t sndfile</code>)</p>
<dd>Microsoft .WAV RIFF files. This is the native audio file format of Windows, and widely used for uncompressed audio. </p>
<p> Normally <code>.wav</code> files have all formatting information in their headers, and so do not need any format options specified for an input file. If any are, they will override the file header, and you will be warned to this effect. You had better know what you are doing! Output format options will cause a format conversion, and the <code>.wav</code> will written appropriately. </p>
<p> SoX can read and write linear PCM, floating point, &mu;-law, A-law, MS ADPCM, and IMA (or DVI) ADPCM encoded samples. WAV files can also contain audio encoded in many other ways (not currently supported with SoX) e.g. MP3; in some cases such a file can still be read by SoX by overriding the file type, e.g. </p>
<pre> play -t mp3 mp3-encoded.wav</pre>
<p>Big endian versions of RIFF files, called RIFX, are also supported. To write a RIFX file, use the <code>-B</code> option with the output file options.</p>
<dt><code>waveaudio</code> (optional)</p>
<dd>MS-Windows native audio device driver. Examples: </p>
<pre> sox infile -t waveaudio
 sox infile -t waveaudio default
 sox infile -t waveaudio 1
 sox infile -t waveaudio &quot;High Definition Audio Device (&quot;</pre>
<p>If the device name is omitted, <code>-1</code>, or <code>default</code>, then you get the `Microsoft Wave Mapper&#8217; device. Wave Mapper means `use the system default audio devices&#8217;. You can control what `default&#8217; means via the OS Control Panel. </p>
<p> If the device name given is some other number, you get that audio device by index; so recording with device name <code>0</code> would get the first input device (perhaps the microphone), <code>1</code> would get the second (perhaps line in), etc. Playback using <code>0</code> will get the first output device (usually the only audio device). </p>
<p> If the device name given is something other than a number, SoX tries to match it (maximum 31 characters) against the names of the available devices. </p>
<p> See also <code><a href="/docs/linux/man/1-play/">play</a></code>(1), <code><a href="/docs/linux/man/1-rec/">rec</a></code>(1), and <code><a href="/docs/linux/man/1-sox/">sox</a></code>(1) <code>-d</code>.</p>
<dt><code>.wavpcm</code></p>
<dd>A non-standard, but widely used, variant of <code>.wav</code>. Some applications cannot read a standard WAV file header for PCM-encoded data with sample-size greater than 16-bits or with more than two channels, but can read a non-standard WAV header. It is likely that such applications will eventually be updated to support the standard header, but in the mean time, this SoX format can be used to create files with the non-standard header that should work with these applications. (Note that SoX will automatically detect and read WAV files with the non-standard header.) </p>
<p> The most common use of this file-type is likely to be along the following lines: </p>
<pre> sox infile.any -t wavpcm -s outfile.wav</pre>
<dt><code>.wv</code> (optional)</p>
<dd>WavPack lossless audio compression. Note that, when converting <code>.wav</code> to this format and back again, the RIFF header is not necessarily preserved losslessly (though the audio is).</p>
<dt><code>.wve</code> (also with <code>-t sndfile</code>)</p>
<dd>Psion 8-bit A-law. Used on Psion SIBO PDAs (Series 3 and similar). This format is deprecated in SoX, but will continue to be used in libsndfile.</p>
<dt><code>.xa</code></p>
<dd>Maxis XA files. These are 16-bit ADPCM audio files used by Maxis games. Writing .xa files is currently not supported, although adding write support should not be very difficult.</p>
<dt><code>.xi</code> (optional)</p>
<dd>Fasttracker 2 Extended Instrument format.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-sox/">sox</a></code>(1), <code><a href="/docs/linux/man/1-soxi/">soxi</a></code>(1), <code><a href="/docs/linux/man/3-libsox/">libsox</a></code>(3), <code><a href="/docs/linux/man/1-octave/">octave</a></code>(1), <code><a href="/docs/linux/man/1-wget/">wget</a></code>(1) </p>
<p> The SoX web page at <a rel="nofollow" href="http://sox.sourceforge.net">http://sox.sourceforge.net</a><br />
 SoX scripting examples at <a rel="nofollow" href="http://sox.sourceforge.net/Docs/Scripts">http://sox.sourceforge.net/Docs/Scripts</a></p>
<h3>References</h3>
<dl>
<dt>[1]</p>
<dd>Wikipedia, <i>M3U</i>, <a rel="nofollow" href="http://en.wikipedia.org/wiki/M3U">http://en.wikipedia.org/wiki/M3U</a></p>
<dt>[2]</p>
<dd>Wikipedia, <i>PLS</i>, <a rel="nofollow" href="http://en.wikipedia.org/wiki/PLS_(file_format)">http://en.wikipedia.org/wiki/PLS_(file_format)</a></dl>
<h2>License</h2>
<p>Copyright 1998-2013 Chris Bagwell and SoX Contributors.<br />
 Copyright 1991 Lance Norskog and Sundry Contributors.</p>
<h2>Authors</h2>
<p>Chris Bagwell (cbagwell [at] users.sourceforge.net). Other authors and contributors are listed in the ChangeLog file that is distributed with the source code.</p>
