---
title: "twolame(1)"
name: "twolame"
section: "1"
letter: "t"
url: "/docs/linux/man/1-twolame/"
description: "twolame – an optimised MPEG Audio Layer 2 (MP2) encoder"
---

<h2 class="name">NAME</h2>
<p> twolame &#8211; an optimised MPEG Audio Layer 2 (MP2) encoder </p>
<h2>SYNOPSIS</h2>
<p> <i>twolame</i> [options] &lt;infile&gt; [outfile]</p>
<h2>DESCRIPTION</h2>
<p> TwoLAME is an optimised MPEG Audio Layer 2 (MP2) encoder based on tooLAME by Mike Cheng, which in turn is based upon the ISO dist10 code and portions of LAME. Encoding is performed by the libtwolame library backend.</p>
<h2>OPTIONS</h2>
<h3>Input File</h3>
<p> twolame uses libsndfile for reading the input sound file, so the input file can be in any format supported by libsndfile. To read raw PCM audio from STDIN, then use &#8211; as the input filename.</p>
<h3>Output File</h3>
<p> If no output filename is specified, then suffix of the input filename is automatically changed to .mp2. To write the encoded audio to STDOUT then use &#8211; as the output filename.</p>
<h3>Input Options</h3>
<p> -r, &#8211;raw-input</p>
<dl>
<dt>
<dd> Specifies that input is raw signed PCM audio. If audio is stereo, than audio samples are interleaved between the two channels.</dl>
<p> -x, &#8211;byte-swap</p>
<dl>
<dt>
<dd> Force byte-swapping of the input. Endian detection is performed automatically by libsndfile, so this option shouldn&#8217;t normally be needed.</dl>
<p> -s, &#8211;samplerate &lt;int&gt;</p>
<dl>
<dt>
<dd> If inputting raw PCM sound, you must specify the sample rate of the audio in Hz. Valid sample rates: 16000, 22050, 24000, 32000, 44100, 48000Hz. Default sample rate is 44100Hz.</dl>
<p> &#8211;samplesize &lt;int&gt;</p>
<dl>
<dt>
<dd> Specifies the sample size (in bits) of the raw PCM audio. Valid sample sizes: 8, 16, 24, 32. Default sample size is 16-bit.</dl>
<p> -N, &#8211;channels &lt;int&gt;</p>
<dl>
<dt>
<dd> If inputting raw PCM sound, you must specify the number of channels in the input audio. Default number of channels is 2.</dl>
<p> -g, &#8211;swap-channels</p>
<dl>
<dt>
<dd> Swap the Left and Right channels of a stereo input file.</dl>
<p> &#8211;scale &lt;float&gt;</p>
<dl>
<dt>
<dd> Scale the input audio prior to encoding. All of the input audio is multiplied by specified value. Value between 0 and 1 will reduce the audio gain, and a value above 1 will increase the gain of the audio.</dl>
<p> &#8211;scale-l &lt;float&gt;</p>
<dl>
<dt>
<dd> Same as &#8211;scale, but only affects the left channel.</dl>
<p> &#8211;scale-r &lt;float&gt;</p>
<dl>
<dt>
<dd> Same as &#8211;scale, but only affects the right channel.</dl>
<h3>Output Options</h3>
<p> -m, &#8211;mode &lt;char&gt;</p>
<dl>
<dt>
<dd> Choose the mode of the resulting audio. Default is auto. </p>
<dl>
<dt>
<dd> &bull; &quot;a&quot; auto &#8211; choose mode automatically based on the input</dl>
<dl>
<dt>
<dd> &bull; &quot;s&quot; stereo</dl>
<dl>
<dt>
<dd> &bull; &quot;d&quot; dual channel</dl>
<dl>
<dt>
<dd> &bull; &quot;j&quot; joint stereo</dl>
<dl>
<dt>
<dd> &bull; &quot;m&quot; mono</dl>
</dl>
<p> -a, &#8211;downmix</p>
<dl>
<dt>
<dd> If the input file is stereo then, downmix the left and right input channels into a single mono channel.</dl>
<p> -b, &#8211;bitrate &lt;int&gt;</p>
<dl>
<dt>
<dd> Sets the total bitrate (in kbps) for the output file. The default bitrate depends on the number of input channels and samplerate. </p>
<dl>
<dt>
<dd>
<pre><code>
-- -- -- -- -- -- -- -- -- -- -- -- -- -- --Sample Rate Mono Stereo-- -- -- -- -- -- -- -- -- -- -- -- -- -- --48000 96 192 44100 96 192 32000 80 160 24000 48 96 22050 48 96 16000 32 64 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
</code></pre>
</dl>
</dl>
<p> -P, &#8211;psyc-mode &lt;int&gt;</p>
<dl>
<dt>
<dd> Choose the psycho-acoustic model to use (-1 to 4). Model number -1 is turns off psycho-acoustic modelling and uses fixed default values instead. Please see the file <i>psycho</i> for a full description of each of the models available. Default model is 3.</dl>
<p> -v, &#8211;vbr</p>
<dl>
<dt>
<dd> Enable VBR mode. See <i>vbr</i> documentation file for details. Default VBR level is 5.0.</dl>
<p> -V, &#8211;vbr-level &lt;float&gt;</p>
<dl>
<dt>
<dd> Enable VBR mode and set quality level. The higher the number the better the quality. Maximum range is -50 to 50 but useful range is -10 to 10. See <i>vbr</i> documentation file for details.</dl>
<p> -l, &#8211;ath &lt;float&gt;</p>
<dl>
<dt>
<dd> Set the ATH level. Default level is 0.0.</dl>
<p> -q, &#8211;quick &lt;int&gt;</p>
<dl>
<dt>
<dd> Enable quick mode. Only re-calculate psycho-acoustic model every specified number of frames.</dl>
<p> -S, &#8211;single-frame</p>
<dl>
<dt>
<dd> Enables single frame mode: only a single frame of MPEG audio is output and then the program terminates.</dl>
<h3>Miscellaneous Options</h3>
<p> -c, &#8211;copyright</p>
<dl>
<dt>
<dd> Turn on Copyright flag in output bitstream.</dl>
<p> -o, &#8211;non-original</p>
<dl>
<dt>
<dd> Turn off Original flag in output bitstream.</dl>
<p> &#8211;original</p>
<dl>
<dt>
<dd> Turn on Original flag in output bitstream.</dl>
<p> -p, &#8211;protect</p>
<dl>
<dt>
<dd> Enable CRC error protection in output bitstream. An extra 16-bit checksum is added to frames.</dl>
<p> -d, &#8211;padding</p>
<dl>
<dt>
<dd> Turn on padding in output bitstream.</dl>
<p> -R, &#8211;reserve &lt;int&gt;</p>
<dl>
<dt>
<dd> Reserve specified number of bits in the each from of the output bitstream.</dl>
<p> -e, &#8211;deemphasis &lt;char&gt;</p>
<dl>
<dt>
<dd> Set the de-emphasis type (n/c/5). Default is none.</dl>
<p> -E, &#8211;energy</p>
<dl>
<dt>
<dd> Turn on energy level extensions.</dl>
<h3>Verbosity Options</h3>
<p> -t, &#8211;talkativity &lt;int&gt;</p>
<dl>
<dt>
<dd> Set the amount of information to be displayed on stderr (0 to 10). Default is 2.</dl>
<p> &#8211;quiet</p>
<dl>
<dt>
<dd> Don&#8217;t send any messages to stderr, unless there is an error. (Same as &#8211;talkativity=0)</dl>
<p> &#8211;brief</p>
<dl>
<dt>
<dd> Only display a minimal number of messages while encoding. This setting is quieter than the default talkativity setting. (Same as &#8211;talkativity=1)</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Display an increased number of messages on stderr. This setting is useful to diagnose problems. (Same as &#8211;talkativity=4)</dl>
<h2>RETURN CODES</h2>
<p> If encoding completes successfully, then twolame will return 0. However if encoding is not successful, then it will return one of the following codes. </p>
<dl>
<dt>
<dd> &bull; 1 (No encoding performed)</dl>
<dl>
<dt>
<dd> &bull; 2 (Error opening input file)</dl>
<dl>
<dt>
<dd> &bull; 4 (Error opening output file)</dl>
<dl>
<dt>
<dd> &bull; 6 (Error allocating memory)</dl>
<dl>
<dt>
<dd> &bull; 8 (Error in chosen encoding parameters)</dl>
<dl>
<dt>
<dd> &bull; 10 (Error reading input audio)</dl>
<dl>
<dt>
<dd> &bull; 12 (Error occured while encoding)</dl>
<dl>
<dt>
<dd> &bull; 14 (Error writing output audio)</dl>
<h2>EXAMPLES</h2>
<p> This will encode sound.wav to sound.mp2 using the default constant bitrate of 192 kbps and using the default psycho-acoustic model (model 3): </p>
<dl>
<dt>
<dd>
<pre>
twolame sound.wav
</pre>
</dl>
<p> Constant bitrate of 160kbps and joint stereo encoding, saved to file sound_160.mp2: </p>
<dl>
<dt>
<dd>
<pre>
twolame -b 160 -m j sound.aiff sound_160.mp2
</pre>
</dl>
<p> Encode sound.wav to newfile.mp2 using psycho-acoustic model 2 and encoding with variable bitrate: </p>
<dl>
<dt>
<dd>
<pre>
twolame -P 2 -v sound.wav newfile.mp2
</pre>
</dl>
<p> Same as example above, except that the negative value of the &quot;-V&quot; argument means that the lower bitrates will be favoured over the higher ones: </p>
<dl>
<dt>
<dd>
<pre>
twolame -P 2 -V -5 sound.wav newfile.mp2
</pre>
</dl>
<p> Resample audio file using sox and pipe straight through twolame: </p>
<dl>
<dt>
<dd>
<pre>
sox sound_11025.aiff -t raw -r 16000 | twolame -r -s 16000 - - &gt; out.mp2
</pre>
</dl>
<h2>AUTHORS</h2>
<p> The twolame frontend was (re)written by Nicholas J Humfrey. The libtwolame library is based on toolame by Mike Cheng. For a full list of authors, please see the AUTHORS file.</p>
<h2>RESOURCES</h2>
<p> TwoLAME web site: m[blue]<code><a rel="nofollow" href="http://www.twolame.org/">http://www.twolame.org/</a></code>m[]</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-lame/">lame</a>(1), <a href="/docs/linux/man/1-mpg123/">mpg123</a>(1), <a href="/docs/linux/man/1-madplay/">madplay</a>(1), <a href="/docs/linux/man/1-sox/">sox</a>(1)</p>
<h2>COPYING</h2>
<p> Copyright &#169; 2004-2006 The TwoLAME Project. Free use of this software is granted under the terms of the GNU Lesser General Public License (LGPL).</p>
<h2>AUTHOR</h2>
<p> <code>Nicholas J Humfrey</code> &lt;njh [at] aelius.com&gt;</p>
<dl>
<dt>
<dd> Author.</dl>
<h2>Index</h2>
