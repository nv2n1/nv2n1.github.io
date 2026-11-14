---
title: "mp3gain(1)"
name: "mp3gain"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mp3gain/"
description: "mp3gain — lossless mp3 normalizer"
---

<h2>NAME</h2>
<p> mp3gain &#8212; lossless mp3 normalizer</p>
<h2>SYNOPSIS</h2>
<p> <code>mp3gain</code> [<code>options</code>] [<i>infile</i>] [<i>infile 2</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents briefly the <code>mp3gain</code> command. </p>
<p> This manual page was written for the <code>Debian</code> distribution because the original program does not have a manual page.<br />
&nbsp;<wbr> </p>
<p> <code>mp3gain</code> can analyze and adjust mp3 files so that they have the same volume. </p>
<p> <code>mp3gain</code> does not just do peak normalization, as many normalizers do. Instead, it does some statistical analysis to determine how loud the file actually sounds to the human ear. Also, the changes <code>mp3gain</code> makes are completely lossless. There is no quality lost in the change because the program adjusts the mp3 file directly, without decoding and re-encoding. Also, this works with all mp3 players, i.e. no support for a special tag or something similar is required. </p>
<p> <code>mp3gain</code> actually changes your file&#8217;s gain only when you use one of the options <code>-r</code>, <code>-a</code>, <code>-g</code>, or <code>-l</code>. If none of these options is given, only a tag denoting the recommended gain change is written to the file. If you only want to print the recommended gain change (and not modify the file at all) you have to use the <code>-s s</code> (skip tag) option. </p>
<p> The method mp3gain uses to determine the desired volume is described at <i><a rel="nofollow" href="http://www.replaygain.org">www.replaygain.org</a> (link to URL <a href="http://www.replaygain.org/)">http://www.replaygain.org/)</a> </i>. See also <code>/usr/share/doc/mp3gain-1.4.6/README.method</code> .</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-?</code> <code>-h</code></p>
<dd> Show summary of options.</p>
<dt><code>-g </code><i>i</i></p>
<dd> apply gain <i>i</i> to mp3 without doing any analysis</p>
<dt><code>-l 0 </code><i>i</i></p>
<dd> apply gain <i>i</i> to channel 0 (left channel) of mp3 without doing any analysis (ONLY works for STEREO mp3s, not Joint Stereo mp3s)</p>
<dt><code>-l 1 </code><i>i</i></p>
<dd> apply gain <i>i</i> to channel 1 (right channel) of mp3 without doing any analysis (ONLY works for STEREO mp3s, not Joint Stereo mp3s)</p>
<dt><code>-r</code></p>
<dd> apply Track gain automatically (all files set to equal loudness)</p>
<dt><code>-k</code></p>
<dd> automatically lower Track gain to not clip audio</p>
<dt><code>-a</code></p>
<dd> apply Album gain automatically (files are all from the same album: a single gain change is applied to all files, so their loudness relative to each other remains unchanged, but the average album loudness is normalized)</p>
<dt><code>-m </code><i>i</i></p>
<dd> modify suggested MP3 gain by integer <i>i</i></p>
<dt><code>-d </code><i>n</i></p>
<dd> modify suggested dB gain by floating-point <i>n</i></p>
<dt><code>-c</code></p>
<dd> ignore clipping warning when applying gain</p>
<dt><code>-o</code></p>
<dd> output is a database-friendly tab-delimited list</p>
<dt><code>-t</code></p>
<dd> mp3gain writes modified mp3 to temp file, then deletes original instead of modifying bytes in original file (This is the default in Debian)</p>
<dt><code>-T</code></p>
<dd> mp3gain modifys bytes in original file instead of writing to temp file.</p>
<dt><code>-q</code></p>
<dd> Quiet mode: no status messages</p>
<dt><code>-p</code></p>
<dd> Preserve original file timestamp</p>
<dt><code>-x</code></p>
<dd> Only find max. amplitude of mp3</p>
<dt><code>-f</code></p>
<dd> Force <code>mp3gain</code> to assume input file is an MPEG 2 Layer III file (i.e. don&#8217;t check for mis-named Layer I or Layer II files)</p>
<dt><code>-s c</code></p>
<dd> only check stored tag info (no other processing)</p>
<dt><code>-s d</code></p>
<dd> delete stored tag info (no other processing)</p>
<dt><code>-s s</code></p>
<dd> skip (ignore) stored tag info (do not read or write tags)</p>
<dt><code>-s r</code></p>
<dd> force re-calculation (do not read tag info)</p>
<dt><code>-u</code></p>
<dd> undo changes made by mp3gain (based on stored tag info)</p>
<dt><code>-w</code></p>
<dd> &quot;wrap&quot; gain change if gain+change &gt; 255 or gain+change &lt; 0 (see below or use <code>-? wrap</code> switch for a complete explanation)</p>
<dt><code>-v</code></p>
<dd> Show version of program.</dl>
<p> If you specify <code>-r</code> and <code>-a</code>, only the second one will work. </p>
<p> If you do not specify <code>-c</code>, the program will stop and ask before applying gain change to a file that might clip</p>
<h3>The WRAP option</h3>
<p> Here&#8217;s the problem: The &quot;global gain&quot; field that mp3gain adjusts is an 8-bit unsigned integer, so the possible values are 0 to 255.<br />
&nbsp;<wbr> </p>
<p> MOST mp3 files (in fact, ALL the mp3 files I&#8217;ve examined so far) don&#8217;t go over 230. So there&#8217;s plenty of headroom on top&#8211; you can increase the gain by 37dB (multiplying the amplitude by 76) without a problem.<br />
&nbsp;<wbr> </p>
<p> The problem is at the bottom of the range. Some encoders create frames with 0 as the global gain for silent frames. What happens when you _lower_ the global gain by 1? Well, in the past, mp3gain always simply wrapped the result up to 255. That way, if you lowered the gain by any amount and then raised it by the same amount, the mp3 would always be _exactly_ the same.<br />
&nbsp;<wbr> </p>
<p> There are a few encoders out there, unfortunately, that create 0-gain frames with other audio data in the frame. As long as the global gain is 0, you&#8217;ll never hear the data. But if you lower the gain on such a file, the global gain is suddenly _huge_. If you play this modified file, there might be a brief, very loud blip.<br />
&nbsp;<wbr> </p>
<p> So now the default behavior of mp3gain is to _not_ wrap gain changes. In other words,<br />
&nbsp;<wbr></p>
<dl>
<dt> 1.</p>
<dd> If the gain change would make a frame&#8217;s global gain drop below 0, then the global gain is set to 0.<br />
&nbsp;<wbr></p>
<dt> 2.</p>
<dd> If the gain change would make a frame&#8217;s global gain grow above 255, then the global gain is set to 255.<br />
&nbsp;<wbr></p>
<dt> 3.</p>
<dd>
&nbsp;<wbr> If a frame&#8217;s global gain field is already 0, it is not changed, even if the gain change is a positive number.<br />
&nbsp;<wbr></dl>
<p> To use the original &quot;wrapping&quot; behavior, use the <code>-w</code> switch.<br />
&nbsp;<wbr></p>
<h2>SEE ALSO</h2>
<p> The homepage of mp3gain is located at <i><a rel="nofollow" href="http://mp3gain.sourceforge.net/">http://mp3gain.sourceforge.net/</a> (link to URL <a href="http://mp3gain.sourceforge.net/)">http://mp3gain.sourceforge.net/)</a> </i> .<br />
&nbsp;<wbr></p>
<h2>AUTHOR</h2>
<p> This manual page was written by Stefan Fritsch sf [at] sfritsch.de for the <code>Debian</code> system (but may be used by others). Permission is granted to copy, distribute and/or modify this document under the terms of the GNU Lesser General Public License, Version 2.1 or any later version published by the Free Software Foundation. </p>
<h2>Index</h2>
