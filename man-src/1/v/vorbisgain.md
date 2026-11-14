---
title: "vorbisgain(1)"
name: "vorbisgain"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vorbisgain/"
description: "vorbisgain – calculate the replay gain for Ogg Vorbis files"
---

<h2 class="name">NAME</h2>
<p> vorbisgain &#8211; calculate the replay gain for Ogg Vorbis files</p>
<h2>SYNOPSIS</h2>
<p> <code>vorbisgain</code> [ <code>-acCdfhqrsv</code> ] [ <code>-g</code> <i>album gain</i> ] <i>input_files </i>&#8230; </p>
<h2>DESCRIPTION</h2>
<p> <code>vorbisgain</code> calculates the ReplayGain values for the named Ogg Vorbis input files and writes back the result in the form of tags (comments) in the file. These values can be used by a playback program to maintain a uniform sound level during play. (See <a rel="nofollow" href="http://www.replaygain.org/">http://www.replaygain.org/</a> for more information.) <code>vorbisgain</code> uses a default target level of 89 dB, rather than the 83 dB recommended by the ReplayGain standard, when calculating the gain to apply. (Some players include a pre-amplification setting with which the target level can be changed.) </p>
<p> <code>vorbisgain</code> input files must be Ogg Vorbis I files with 1 or 2 channels and a sample rate of 48 kHz, 44.1 kHz, 32 kHz, 24 kHz, 22050 Hz, 16 kHz, 12 kHz, 11025 Hz or 8 kHz. If an input file contains multiple streams (i.e., it is chained), the streams must all have the same format, in terms of sampling frequency and number of channels. </p>
<p> All streams in a chained file are processed, but the ReplayGain tags are only written to (or removed from) the first stream. </p>
<h2>OPTIONS</h2>
<dl>
<dt>-h, &#8211;help</p>
<dd> Show command help. </p>
<dt>-a, &#8211;album</p>
<dd> Activates album mode, in which the album gain (sometimes called the audiophile gain) is calculated in addition to the track gain (sometimes called the radio gain). </p>
<dt>-g n, &#8211;album-gain=n</p>
<dd> Sets the album gain value to use. Default is to calculate it, if <i>-a</i> is specified. Implies <i>-a</i> in the sense that the album gain tag is written. This is a relative value, in dB, specifying the <code>change</code> in volume that should be applied. </p>
<dt>-c, &#8211;clean</p>
<dd> Remove any ReplayGain tags from the specified files. If a file does not contain any ReplayGain tags, the file is not modified. </p>
<dt>-C, &#8211;convert</p>
<dd> Convert old format ReplayGain tags to a new format (see section TAG FORMAT below for details). If a file does not contain all ReplayGain tags that are needed for a conversion, the file is not modified. The album peak tag is only created if <i>-a</i> is specified, and the album gain value is then checked for consistency. Otherwise any album gain is converted without any checks. </p>
<dt>-d, &#8211;display-only</p>
<dd> Display the result only; do not write anything to disk. This applies to all options. </p>
<dt>-f, &#8211;fast</p>
<dd> Only calculate the gain for files that do not contain all replay gain tags needed (the album gain and peak tags are only considered if <i>-a</i> has been specified). </p>
<dt>-n, &#8211;no-progress</p>
<dd> Only display results, but don&#8217;t show progress in percentages and times. This can be useful if the output is piped into other programs. </p>
<dt>-q, &#8211;quiet</p>
<dd> Do not display any output while processing. Only error and warning messages will be printed. </p>
<dt>-r, &#8211;recursive</p>
<dd> Enter directories (recursively) and search for files, if directories or file patterns are specified. <i>Note:</i> Only available if <code>vorbisgain</code> was configured with &#8211;enable-recursive. </p>
<dt>-s, &#8211;silent</p>
<dd> Silently skip any non-Vorbis files found. Vorbis files that can&#8217;t be processed for some reason are skipped as well, though not silently. Default is to stop when such files are encountered. </p>
<dt>-v, &#8211;version</p>
<dd> Display the version of the program. </p>
</dl>
<h2>EXAMPLES</h2>
<p> Simplest version. Calculate the track gain and peak only. </p>
<dl>
<dt>
<dd> vorbisgain somefile.ogg</dl>
<p> Note that the following examples are only possible if <code>vorbisgain</code> was configured with &#8211;enable-recursive. </p>
<p> Calculate the album gain and peak, in addition to the track gain and peak, for all .ogg files in the directory &quot;music&quot; (and all subdirectories). All files in one directory are treated as belonging to the same album. Files that already have ReplayGain tags are not re-calculated. Note the quotes, as they cause the shell to not do any filename globbing: </p>
<dl>
<dt>
<dd> vorbisgain -a -f -r &quot;music/*.ogg&quot;</dl>
<p> Calculate the album gain. The files specified before the directory &quot;album&quot; are treated as one album, the files in the directory &quot;album&quot; as another album and the remaining files as a third album: </p>
<dl>
<dt>
<dd> vorbisgain -a -r a.ogg b.ogg c.ogg album d.ogg e.ogg f.ogg</dl>
<p> Remove all replaygain tags from a collection of oggs: </p>
<dl>
<dt>
<dd> vorbisgain -c -r &quot;music/*.ogg&quot;</dl>
<h2>TAG FORMAT</h2>
<p> <code>vorbisgain</code> creates tags like these (when in <i>-a</i> mode): </p>
<dl>
<dt>
<dd> REPLAYGAIN_TRACK_GAIN=-7.03 dB</dl>
<dl>
<dt>
<dd> REPLAYGAIN_TRACK_PEAK=1.21822226</dl>
<dl>
<dt>
<dd> REPLAYGAIN_ALBUM_GAIN=-6.37 dB</dl>
<dl>
<dt>
<dd> REPLAYGAIN_ALBUM_PEAK=1.21822226</dl>
<p> Gain specifies how much the volume should be changed before playback, in dB. Peak is the maximum sample value of the file before any gain has been applied, where 1.0 means &quot;full sample value&quot; (32,767 when decoding to signed 16 bit samples). </p>
<p> Earlier versions of <code>vorbisgain</code> (before 0.30) created the following tags: </p>
<dl>
<dt>
<dd> RG_RADIO</dl>
<dl>
<dt>
<dd> RG_PEAK</dl>
<dl>
<dt>
<dd> RG_AUDIOPHILE</dl>
<p> When <i>-c</i> is used, RG_RADIO is converted to REPLAYGAIN_TRACK_GAIN, RG_PEAK to REPLAYGAIN_TRACK_PEAK, RG_AUDIOPHILE to REPLAYGAIN_ALBUM_GAIN and REPLAYGAIN_ALBUM_PEAK is calculated as the maximum of all RG_PEAK tags in the album. </p>
<h2>AUTHORS</h2>
<dl>
<dt>Program Code:</p>
<dd>
 Gian-Carlo Pascutto &lt;gcp [at] sjeng.org&gt;<br />
 Magnus Holmgren &lt;lear [at] algonet.se&gt; </p>
<dt>ReplayGain Analysis Code:</p>
<dd>
 Glen Sawyer &lt;glensawyer [at] hotmail.com&gt;<br />
 Frank Klemm (<a rel="nofollow" href="http://www.uni-jena.de/~pfk/)">http://www.uni-jena.de/~pfk/)</a> </p>
<dt>Man Page:</p>
<dd>
 Magnus Holmgren &lt;lear [at] algonet.se&gt; </p>
</dl>
<h2>BUGS</h2>
<p> None known. </p>
<h2>SEE ALSO</h2>
<dl>
<dt><a rel="nofollow" href="http://sjeng.org/vorbisgain.html">http://sjeng.org/vorbisgain.html</a></p>
<dd> Home page for VorbisGain. The latest version, and a Windows executable, can be found here. </p>
<dt><a rel="nofollow" href="http://www.replaygain.org/">http://www.replaygain.org/</a></p>
<dd> Contains detailed information about ReplayGain and how it is calculated. </p>
<dt><a rel="nofollow" href="http://www.hydrogenaudio.org/">http://www.hydrogenaudio.org/</a></p>
<dd> Discussion forum for audio compression and related issues, including Ogg Vorbis and VorbisGain. </p>
</dl>
<h2>Index</h2>
