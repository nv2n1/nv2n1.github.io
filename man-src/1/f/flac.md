---
title: "flac(1)"
name: "flac"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flac/"
description: "flac – Free Lossless Audio Codec"
---

<h2 class="name">NAME</h2>
<p> flac &#8211; Free Lossless Audio Codec </p>
<h2>SYNOPSIS</h2>
<p> <code>flac</code> [ <i>OPTIONS</i> ] [ <i>infile.wav</i> | <i>infile.rf64</i> | <i>infile.aiff</i> | <i>infile.raw</i> | <i>infile.flac</i> | <i>infile.oga</i> | <i>infile.ogg</i> | <code>&#8211;</code><i> &#8230;</i> ] </p>
<p> <code>flac</code> [ <code>-d</code> | <code>&#8211;decode</code> | <code>-t</code> | <code>&#8211;test</code> | <code>-a</code> | <code>&#8211;analyze</code> ] [ <i>OPTIONS</i> ] [ <i>infile.flac</i> | <i>infile.oga</i> | <i>infile.ogg</i> | <code>&#8211;</code><i> &#8230;</i> ] </p>
<h2>DESCRIPTION</h2>
<p> <code>flac</code> is a command-line tool for encoding, decoding, testing and analyzing FLAC streams.</p>
<h2>OPTIONS</h2>
<p> A summary of options is included below. For a complete description, see the HTML documentation.</p>
<h3>GENERAL OPTIONS</h3>
<dl>
<dt><code>-v, &#8211;version</code></p>
<dd> Show the flac version number</p>
<dt><code>-h, &#8211;help </code></p>
<dd> Show basic usage and a list of all options</p>
<dt><code>-H, &#8211;explain </code></p>
<dd> Show detailed explanation of usage and all options</p>
<dt><code>-d, &#8211;decode </code></p>
<dd> Decode (the default behavior is to encode)</p>
<dt><code>-t, &#8211;test </code></p>
<dd> Test a flac encoded file (same as -d except no decoded file is written)</p>
<dt><code>-a, &#8211;analyze </code></p>
<dd> Analyze a FLAC encoded file (same as -d except an analysis file is written)</p>
<dt><code>-c, &#8211;stdout </code></p>
<dd> Write output to stdout</p>
<dt><code>-s, &#8211;silent </code></p>
<dd> Silent mode (do not write runtime encode/decode statistics to stderr)</p>
<dt><code>&#8211;totally-silent </code></p>
<dd> Do not print anything of any kind, including warnings or errors. The exit code will be the only way to determine successful completion.</p>
<dt><code>&#8211;no-utf8-convert </code></p>
<dd> Do not convert tags from local charset to UTF-8. This is useful for scripts, and setting tags in situations where the locale is wrong. This option must appear before any tag options!</p>
<dt><code>-w, &#8211;warnings-as-errors </code></p>
<dd> Treat all warnings as errors (which cause flac to terminate with a non-zero exit code).</p>
<dt><code>-f, &#8211;force </code></p>
<dd> Force overwriting of output files. By default, flac warns that the output file already exists and continues to the next file.</p>
<dt><code>-o </code><i>filename</i><code>, &#8211;output-name=</code><i>filename</i></p>
<dd> Force the output file name (usually flac just changes the extension). May only be used when encoding a single file. May not be used in conjunction with &#8211;output-prefix.</p>
<dt><code>&#8211;output-prefix=</code><i>string</i></p>
<dd> Prefix each output file name with the given string. This can be useful for encoding or decoding files to a different directory. Make sure if your string is a path name that it ends with a trailing `/&#8217; (slash).</p>
<dt><code>&#8211;delete-input-file </code></p>
<dd> Automatically delete the input file after a successful encode or decode. If there was an error (including a verify error) the input file is left intact.</p>
<dt><code>&#8211;preserve-modtime </code></p>
<dd> Output files have their timestamps/permissions set to match those of their inputs (this is default). Use &#8211;no-preserve-modtime to make output files have the current time and default permissions.</p>
<dt><code>&#8211;keep-foreign-metadata </code></p>
<dd> If encoding, save WAVE, RF64, or AIFF non-audio chunks in FLAC metadata. If decoding, restore any saved non-audio chunks from FLAC metadata when writing the decoded file. Foreign metadata cannot be transcoded, e.g. WAVE chunks saved in a FLAC file cannot be restored when decoding to AIFF. Input and output must be regular files (not stdin or stdout).</p>
<dt><code>&#8211;skip={</code><i>#</i><code>|</code><i>mm:ss.ss</i><code>}</code></p>
<dd> Skip over the first number of samples of the input. This works for both encoding and decoding, but not testing. The alternative form mm:ss.ss can be used to specify minutes, seconds, and fractions of a second.</p>
<dt><code>&#8211;until={</code><i>#</i><code>|[</code><i>+</i><code>|</code><i>&#8211;</i><code>]</code><i>mm:ss.ss</i><code>}</code></p>
<dd> Stop at the given sample number for each input file. This works for both encoding and decoding, but not testing. The given sample number is not included in the decoded output. The alternative form mm:ss.ss can be used to specify minutes, seconds, and fractions of a second. If a `+&#8217; (plus) sign is at the beginning, the &#8211;until point is relative to the &#8211;skip point. If a `-&#8216; (minus) sign is at the beginning, the &#8211;until point is relative to end of the audio.</p>
<dt><code>&#8211;ogg</code></p>
<dd> When encoding, generate Ogg FLAC output instead of native FLAC. Ogg FLAC streams are FLAC streams wrapped in an Ogg transport layer. The resulting file should have an &#8216;.oga&#8217; extension and will still be decodable by flac. </p>
<p> When decoding, force the input to be treated as Ogg FLAC. This is useful when piping input from stdin or when the filename does not end in &#8216;.oga&#8217; or &#8216;.ogg&#8217;.</p>
<dt><code>&#8211;serial-number=</code><i>#</i></p>
<dd> When used with &#8211;ogg, specifies the serial number to use for the first Ogg FLAC stream, which is then incremented for each additional stream. When encoding and no serial number is given, flac uses a random number for the first stream, then increments it for each additional stream. When decoding and no number is given, flac uses the serial number of the first page.</dl>
<h3>ANALYSIS OPTIONS</h3>
<dl>
<dt><code>&#8211;residual-text </code></p>
<dd> Includes the residual signal in the analysis file. This will make the file very big, much larger than even the decoded file.</p>
<dt><code>&#8211;residual-gnuplot </code></p>
<dd> Generates a gnuplot file for every subframe; each file will contain the residual distribution of the subframe. This will create a lot of files.</dl>
<h3>DECODING OPTIONS</h3>
<dl>
<dt><code>&#8211;cue=[</code><i>#.#</i><code>][-[</code><i>#.#</i><code>]]</code></p>
<dd> Set the beginning and ending cuepoints to decode. The optional first #.# is the track and index point at which decoding will start; the default is the beginning of the stream. The optional second #.# is the track and index point at which decoding will end; the default is the end of the stream. If the cuepoint does not exist, the closest one before it (for the start point) or after it (for the end point) will be used. If those don&#8217;t exist, the start of the stream (for the start point) or end of the stream (for the end point) will be used. The cuepoints are merely translated into sample numbers then used as &#8211;skip and &#8211;until. A CD track can always be cued by, for example, &#8211;cue=9.1-10.1 for track 9, even if the CD has no 10th track.</p>
<dt><code>-F, &#8211;decode-through-errors </code></p>
<dd> By default flac stops decoding with an error and removes the partially decoded file if it encounters a bitstream error. With -F, errors are still printed but flac will continue decoding to completion. Note that errors may cause the decoded audio to be missing some samples or have silent sections.</p>
<dt><code>&#8211;apply-replaygain-which-is-not-lossless[=&lt;specification&gt;] </code></p>
<dd> Applies ReplayGain values while decoding. </p>
<p> WARNING: THIS IS NOT LOSSLESS. DECODED AUDIO WILL NOT BE IDENTICAL TO THE ORIGINAL WITH THIS OPTION. </p>
<p> The equals sign and &lt;specification&gt; is optional. If omitted, the default is 0aLn1. </p>
<p> The &lt;specification&gt; is a shorthand notation for describing how to apply ReplayGain. All components are optional but order is important. &#8216;[]&#8217; means &#8216;optional&#8217;. &#8216;|&#8217; means &#8216;or&#8217;. &#8216;{}&#8217; means required. The format is: </p>
<p> [&lt;preamp&gt;][a|t][l|L][n{0|1|2|3}]</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>preamp</code></p>
<dd> A floating point number in dB. This is added to the existing gain value.</p>
<dt><code>a|t</code></p>
<dd> Specify &#8216;a&#8217; to use the album gain, or &#8216;t&#8217; to use the track gain. If tags for the preferred kind (album/track) do not exist but tags for the other (track/album) do, those will be used instead.</p>
<dt><code>l|L</code></p>
<dd> Specify &#8216;l&#8217; to peak-limit the output, so that the ReplayGain peak value is full-scale. Specify &#8216;L&#8217; to use a 6dB hard limiter that kicks in when the signal approaches full-scale.</p>
<dt><code>n{0|1|2|3}</code></p>
<dd> Specify the amount of noise shaping. ReplayGain synthesis happens in floating point; the result is dithered before converting back to integer. This quantization adds noise. Noise shaping tries to move the noise where you won&#8217;t hear it as much. 0 means no noise shaping, 1 means &#8216;low&#8217;, 2 means &#8216;medium&#8217;, 3 means &#8216;high&#8217;.</dl>
</dl>
<p> For example, the default of 0aLn1 means 0dB preamp, use album gain, 6dB hard limit, low noise shaping. </p>
<p> &#8211;apply-replaygain-which-is-not-lossless=3 means 3dB preamp, use album gain, no limiting, no noise shaping. </p>
<p> flac uses the ReplayGain tags for the calculation. If a stream does not have the required tags or they can&#8217;t be parsed, decoding will continue with a warning, and no ReplayGain is applied to that stream.</dl>
<h3>ENCODING OPTIONS</h3>
<dl>
<dt><code>-V, &#8211;verify</code></p>
<dd> Verify a correct encoding by decoding the output in parallel and comparing to the original</p>
<dt><code>&#8211;lax</code></p>
<dd> Allow encoder to generate non-Subset files. The resulting FLAC file may not be streamable or might have trouble being played in all players (especially hardware devices), so you should only use this option in combination with custom encoding options meant for archival.</p>
<dt><code>&#8211;replay-gain</code></p>
<dd> Calculate ReplayGain values and store them as FLAC tags, similar to vorbisgain. Title gains/peaks will be computed for each input file, and an album gain/peak will be computed for all files. All input files must have the same resolution, sample rate, and number of channels. Only mono and stereo files are allowed, and the sample rate must be one of 8, 11.025, 12, 16, 22.05, 24, 32, 44.1, or 48 kHz. Also note that this option may leave a few extra bytes in a PADDING block as the exact size of the tags is not known until all files are processed. Note that this option cannot be used when encoding to standard output (stdout).</p>
<dt><code>&#8211;cuesheet=</code><i>filename</i></p>
<dd> Import the given cuesheet file and store it in a CUESHEET metadata block. This option may only be used when encoding a single file. A seekpoint will be added for each index point in the cuesheet to the SEEKTABLE unless &#8211;no-cued-seekpoints is specified.</p>
<dt><code>&#8211;picture={</code><i>FILENAME</i><code>|</code><i>SPECIFICATION</i><code>}</code></p>
<dd> Import a picture and store it in a PICTURE metadata block. More than one &#8211;picture command can be specified. Either a filename for the picture file or a more complete specification form can be used. The SPECIFICATION is a string whose parts are separated by | (pipe) characters. Some parts may be left empty to invoke default values. FILENAME is just shorthand for &quot;||||FILENAME&quot;. The format of SPECIFICATION is </p>
<p> [TYPE]|[MIME-TYPE]|[DESCRIPTION]|[WIDTHxHEIGHTxDEPTH[/COLORS]]|FILE </p>
<p> TYPE is optional; it is a number from one of: </p>
<p> 0: Other </p>
<p> 1: 32&#215;32 pixels &#8216;file icon&#8217; (PNG only) </p>
<p> 2: Other file icon </p>
<p> 3: Cover (front) </p>
<p> 4: Cover (back) </p>
<p> 5: Leaflet page </p>
<p> 6: Media (e.g. label side of CD) </p>
<p> 7: Lead artist/lead performer/soloist </p>
<p> 8: Artist/performer </p>
<p> 9: Conductor </p>
<p> 10: Band/Orchestra </p>
<p> 11: Composer </p>
<p> 12: Lyricist/text writer </p>
<p> 13: Recording Location </p>
<p> 14: During recording </p>
<p> 15: During performance </p>
<p> 16: Movie/video screen capture </p>
<p> 17: A bright coloured fish </p>
<p> 18: Illustration </p>
<p> 19: Band/artist logotype </p>
<p> 20: Publisher/Studio logotype </p>
<p> The default is 3 (front cover). There may only be one picture each of type 1 and 2 in a file. </p>
<p> MIME-TYPE is optional; if left blank, it will be detected from the file. For best compatibility with players, use pictures with MIME type image/jpeg or image/png. The MIME type can also be &#8211;&gt; to mean that FILE is actually a URL to an image, though this use is discouraged. </p>
<p> DESCRIPTION is optional; the default is an empty string. </p>
<p> The next part specfies the resolution and color information. If the MIME-TYPE is image/jpeg, image/png, or image/gif, you can usually leave this empty and they can be detected from the file. Otherwise, you must specify the width in pixels, height in pixels, and color depth in bits-per-pixel. If the image has indexed colors you should also specify the number of colors used. When manually specified, it is not checked against the file for accuracy. </p>
<p> FILE is the path to the picture file to be imported, or the URL if MIME type is &#8211;&gt; </p>
<p> For example, &quot;|image/jpeg|||../cover.jpg&quot; will embed the JPEG file at ../cover.jpg, defaulting to type 3 (front cover) and an empty description. The resolution and color info will be retrieved from the file itself. </p>
<p> The specification &quot;4|&#8211;&gt;|CD|320x300x24/173|<a rel="nofollow" href="http://blah.blah/backcover.tiff">http://blah.blah/backcover.tiff</a>&quot; will embed the given URL, with type 4 (back cover), description &quot;CD&quot;, and a manually specified resolution of 320&#215;300, 24 bits-per-pixel, and 173 colors. The file at the URL will not be fetched; the URL itself is stored in the PICTURE metadata block.</p>
<dt><code>&#8211;sector-align</code></p>
<dd> Align encoding of multiple CD format files on sector boundaries. See the HTML documentation for more information. This option is DEPRECATED and may not exist in future versions of flac.</p>
<dt><code>&#8211;ignore-chunk-sizes</code></p>
<dd> When encoding to flac, ignore the file size headers in WAV and AIFF files to attempt to work around problems with over-sized or malformed files. </p>
<p> WAV and AIFF files both have an unsigned 32 bit numbers in the file header which specifes the length of audio data. Since this number is unsigned 32 bits, that limits the size of a valid file to being just over 4 Gigabytes. Files larger than this are mal-formed, but should be read correctly using this option.</p>
<dt><code>-S {</code><i>#</i><code>|</code><i>X</i><code>|</code><i>#x</i><code>|</code><i>#s</i><code>}, &#8211;seekpoint={</code><i>#</i><code>|</code><i>X</i><code>|</code><i>#x</i><code>|</code><i>#s</i><code>}</code></p>
<dd> Include a point or points in a SEEKTABLE. Using #, a seek point at that sample number is added. Using X, a placeholder point is added at the end of a the table. Using #x, # evenly spaced seek points will be added, the first being at sample 0. Using #s, a seekpoint will be added every # seconds (# does not have to be a whole number; it can be, for example, 9.5, meaning a seekpoint every 9.5 seconds). You may use many -S options; the resulting SEEKTABLE will be the unique-ified union of all such values. With no -S options, flac defaults to &#8216;-S 10s&#8217;. Use &#8211;no-seektable for no SEEKTABLE. Note: &#8216;-S #x&#8217; and &#8216;-S #s&#8217; will not work if the encoder can&#8217;t determine the input size before starting. Note: if you use &#8216;-S #&#8217; and # is &gt;= samples in the input, there will be either no seek point entered (if the input size is determinable before encoding starts) or a placeholder point (if input size is not determinable).</p>
<dt><code>-P </code><i>#</i><code>, &#8211;padding=</code><i>#</i></p>
<dd> Tell the encoder to write a PADDING metadata block of the given length (in bytes) after the STREAMINFO block. This is useful if you plan to tag the file later with an APPLICATION block; instead of having to rewrite the entire file later just to insert your block, you can write directly over the PADDING block. Note that the total length of the PADDING block will be 4 bytes longer than the length given because of the 4 metadata block header bytes. You can force no PADDING block at all to be written with &#8211;no-padding. The encoder writes a PADDING block of 8192 bytes by default (or 65536 bytes if the input audio stream is more that 20 minutes long).</p>
<dt><code>-T </code><i>FIELD=VALUE</i><code>, &#8211;tag=</code><i>FIELD=VALUE</i></p>
<dd> Add a FLAC tag. The comment must adhere to the Vorbis comment spec; i.e. the FIELD must contain only legal characters, terminated by an &#8216;equals&#8217; sign. Make sure to quote the comment if necessary. This option may appear more than once to add several comments. NOTE: all tags will be added to all encoded files.</p>
<dt><code>&#8211;tag-from-file=</code><i>FIELD=FILENAME</i></p>
<dd> Like &#8211;tag, except FILENAME is a file whose contents will be read verbatim to set the tag value. The contents will be converted to UTF-8 from the local charset. This can be used to store a cuesheet in a tag (e.g. &#8211;tag-from-file=&quot;CUESHEET=image.cue&quot;). Do not try to store binary data in tag fields! Use APPLICATION blocks for that.</p>
<dt><code>-b </code><i>#</i><code>, &#8211;blocksize=</code><i>#</i></p>
<dd> Specify the block size in samples. Subset streams must use one of 192, 576, 1152, 2304, 4608, 256, 512, 1024, 2048, 4096 (and 8192 or 16384 if the sample rate is &gt;48kHz).</p>
<dt><code>-m, &#8211;mid-side</code></p>
<dd> Try mid-side coding for each frame (stereo input only)</p>
<dt><code>-M, &#8211;adaptive-mid-side</code></p>
<dd> Adaptive mid-side coding for all frames (stereo input only)</p>
<dt><code>-0..-8, &#8211;compression-level-0..&#8211;compression-level-8</code></p>
<dd> Fastest compression..highest compression (default is -5). These are synonyms for other options:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>-0, &#8211;compression-level-0</code></p>
<dd> Synonymous with -l 0 -b 1152 -r 3</p>
<dt><code>-1, &#8211;compression-level-1</code></p>
<dd> Synonymous with -l 0 -b 1152 -M -r 3</p>
<dt><code>-2, &#8211;compression-level-2</code></p>
<dd> Synonymous with -l 0 -b 1152 -m -r 3</p>
<dt><code>-3, &#8211;compression-level-3</code></p>
<dd> Synonymous with -l 6 -b 4096 -r 4</p>
<dt><code>-4, &#8211;compression-level-4</code></p>
<dd> Synonymous with -l 8 -b 4096 -M -r 4</p>
<dt><code>-5, &#8211;compression-level-5</code></p>
<dd> Synonymous with -l 8 -b 4096 -m -r 5</p>
<dt><code>-6, &#8211;compression-level-6</code></p>
<dd> Synonymous with -l 8 -b 4096 -m -r 6</p>
<dt><code>-7, &#8211;compression-level-7</code></p>
<dd> Synonymous with -l 8 -b 4096 -m -e -r 6</p>
<dt><code>-8, &#8211;compression-level-8</code></p>
<dd> Synonymous with -l 12 -b 4096 -m -e -r 6</dl>
</dl>
<dt><code>&#8211;fast</code></p>
<dd> Fastest compression. Currently synonymous with -0.</p>
<dt><code>&#8211;best</code></p>
<dd> Highest compression. Currently synonymous with -8.</p>
<dt><code>-e, &#8211;exhaustive-model-search</code></p>
<dd> Do exhaustive model search (expensive!)</p>
<dt><code>-A </code><i>function</i><code>, &#8211;apodization=</code><i>function</i></p>
<dd> Window audio data with given the apodization function. The functions are: bartlett, bartlett_hann, blackman, blackman_harris_4term_92db, connes, flattop, gauss(STDDEV), hamming, hann, kaiser_bessel, nuttall, rectangle, triangle, tukey(P), welch. </p>
<p> For gauss(STDDEV), STDDEV is the standard deviation (0&lt;STDDEV&lt;=0.5). </p>
<p> For tukey(P), P specifies the fraction of the window that is tapered (0&lt;=P&lt;=1; P=0 corresponds to &quot;rectangle&quot; and P=1 corresponds to &quot;hann&quot;). </p>
<p> More than one -A option (up to 32) may be used. Any function that is specified erroneously is silently dropped. The encoder chooses suitable defaults in the absence of any -A options; any -A option specified replaces the default(s). </p>
<p> When more than one function is specified, then for every subframe the encoder will try each of them separately and choose the window that results in the smallest compressed subframe. Multiple functions can greatly increase the encoding time.</p>
<dt><code>-l </code><i>#</i><code>, &#8211;max-lpc-order=</code><i>#</i></p>
<dd> Specifies the maximum LPC order. This number must be &lt;= 32. For Subset streams, it must be &lt;=12 if the sample rate is &lt;=48kHz. If 0, the encoder will not attempt generic linear prediction, and use only fixed predictors. Using fixed predictors is faster but usually results in files being 5-10% larger.</p>
<dt><code>-p, &#8211;qlp-coeff-precision-search</code></p>
<dd> Do exhaustive search of LP coefficient quantization (expensive!). Overrides -q; does nothing if using -l 0</p>
<dt><code>-q </code><i>#</i><code>, &#8211;qlp-coeff-precision=</code><i>#</i></p>
<dd> Precision of the quantized linear-predictor coefficients, 0 =&gt; let encoder decide (min is 5, default is 0)</p>
<dt><code>-r [</code><i>#</i><code>,]</code><i>#</i><code>, &#8211;rice-partition-order=[</code><i>#</i><code>,]</code><i>#</i></p>
<dd> Set the [min,]max residual partition order (0..16). min defaults to 0 if unspecified. Default is -r 5.</dl>
<h3>FORMAT OPTIONS</h3>
<dl>
<dt><code>&#8211;endian={</code><i>big</i><code>|</code><i>little</i><code>}</code></p>
<dd> Set the byte order for samples</p>
<dt><code>&#8211;channels=</code><i>#</i></p>
<dd> Set number of channels.</p>
<dt><code>&#8211;bps=</code><i>#</i></p>
<dd> Set bits per sample.</p>
<dt><code>&#8211;sample-rate=</code><i>#</i></p>
<dd> Set sample rate (in Hz).</p>
<dt><code>&#8211;sign={</code><i>signed</i><code>|</code><i>unsigned</i><code>}</code></p>
<dd> Set the sign of samples (the default is signed).</p>
<dt><code>&#8211;input-size=</code><i>#</i></p>
<dd> Specify the size of the raw input in bytes. If you are encoding raw samples from stdin, you must set this option in order to be able to use &#8211;skip, &#8211;until, &#8211;cuesheet, or other options that need to know the size of the input beforehand. If the size given is greater than what is found in the input stream, the encoder will complain about an unexpected end-of-file. If the size given is less, samples will be truncated.</p>
<dt><code>&#8211;force-raw-format</code></p>
<dd> Force input (when encoding) or output (when decoding) to be treated as raw samples (even if filename ends in <i>.wav</i>).</p>
<dt><code>&#8211;force-aiff-format</code></p>
<dd> Force the decoder to output AIFF format. This option is not needed if the output filename (as set by -o) ends with <i>.aif</i> or <i>.aiff</i>. Also, this option has no effect when encoding since input AIFF is auto-detected.</p>
<dt><code>&#8211;force-rf64-format</code></p>
<dd> Force the decoder to output RF64 format. This option is not needed if the output filename (as set by -o) ends with <i>.rf64</i>. Also, this option has no effect when encoding since input RF64 is auto-detected.</p>
<dt><code>&#8211;force-wave64-format</code></p>
<dd> Force the decoder to output Wave64 format. This option is not needed if the output filename (as set by -o) ends with <i>.w64</i>. Also, this option has no effect when encoding since input Wave64 is auto-detected.</dl>
<h3>NEGATIVE OPTIONS</h3>
<dl>
<dt><code>&#8211;no-adaptive-mid-side</code></p>
<dd>
<dt><code>&#8211;no-cued-seekpoints</code></p>
<dd>
<dt><code>&#8211;no-decode-through-errors</code></p>
<dd>
<dt><code>&#8211;no-delete-input-file</code></p>
<dd>
<dt><code>&#8211;no-preserve-modtime</code></p>
<dd>
<dt><code>&#8211;no-keep-foreign-metadata</code></p>
<dd>
<dt><code>&#8211;no-exhaustive-model-search</code></p>
<dd>
<dt><code>&#8211;no-force</code></p>
<dd>
<dt><code>&#8211;no-lax</code></p>
<dd>
<dt><code>&#8211;no-mid-side</code></p>
<dd>
<dt><code>&#8211;no-ogg</code></p>
<dd>
<dt><code>&#8211;no-padding</code></p>
<dd>
<dt><code>&#8211;no-qlp-coeff-prec-search</code></p>
<dd>
<dt><code>&#8211;no-replay-gain</code></p>
<dd>
<dt><code>&#8211;no-residual-gnuplot</code></p>
<dd>
<dt><code>&#8211;no-residual-text</code></p>
<dd>
<dt><code>&#8211;no-sector-align</code></p>
<dd>
<dt><code>&#8211;no-seektable</code></p>
<dd>
<dt><code>&#8211;no-silent</code></p>
<dd>
<dt><code>&#8211;no-verify</code></p>
<dd>
<dt><code>&#8211;no-warnings-as-errors</code></p>
<dd> These flags can be used to invert the sense of the corresponding normal option.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-metaflac/">metaflac</a>(1). </p>
<p> The programs are documented fully by HTML format documentation, available in <i>/usr/share/doc/libflac-doc/html</i> on Debian GNU/Linux systems.</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Matt Zimmerman &lt;mdz [at] debian.org&gt; for the Debian GNU/Linux system (but may be used by others). </p>
<h2>Index</h2>
