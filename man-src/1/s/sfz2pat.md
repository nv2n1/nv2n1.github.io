---
title: "sfz2pat(1)"
name: "sfz2pat"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sfz2pat/"
description: "sz2pat – convert sample files into extended GUS patches"
---

<h2>NAME</h2>
<p> sz2pat &#8211; convert sample files into extended GUS patches </p>
<h2>SYNOPSIS</h2>
<p> <code>sfz2pat</code> filename.sfz </p>
<h2>DESCRIPTION</h2>
<p> This documents both the conversion program <i>sfz2pat</i> and the <code>sfz</code> loader of the <i>gt</i> midi player. </p>
<p> The name of one or more .wav files containing samples and various parameters describing the desired patch structure and how to play the patch are given in a text file with the extension <code>.sfz</code>. Run the <i>sfz2pat</i> utility on <i>filename</i><code>.sfz</code>, and, if all goes well, the result will be a GUS patch file named <i>filename</i><code>.pat</code>. </p>
<p> The same <code>.sfz</code> file can be loaded and played directly by <i>gt</i>. Just put the name of the file into timidity.cfg or a file it sources, as you would the name of a GUS <code>.pat</code> file. Some features of <code>sfz</code> patches can only be used when the patch is loaded directly, because they don&#8217;t fit into the GUS format. </p>
<p> The format of <code>.sfz</code> files is described in <i><a rel="nofollow" href="http://www.rgcaudio.com/sfzformat.htm">http://www.rgcaudio.com/sfzformat.htm</a></i>. See also <i><a rel="nofollow" href="http://www.drealm.org.uk/sfz/plj-sfz.html">http://www.drealm.org.uk/sfz/plj-sfz.html</a></i> a more lucid, less authoritative, account (from PL Jones). An <code>.sfz</code> patch file is a text file describing a single instrument, as implemented here. (Though a whole set of drums can be characterized in a single <code>.sfz</code> file for RGC Audio&#8217;s player program, this implementation requires a separate patch file for each drum.) </p>
<p> Typically, an instrument will have a number of different samples, and which sample sounds when a note on that instrument is played will depend on various circumstances &#8212; the pitch of the note, how loud it is, and so on. A sample thought of in relation to whether it sounds when a note is played is referred to as a <code>layer</code> in the RGC documentation, but I usually call it a sample. Each individual sample (layer) of an instrument is described in a <code>region</code> of the <code>.sfz</code> patch file (see the <i>&lt;region&gt;</i> opcode below). </p>
<p> Only a very tiny, little, miniscule part of <code>SFZ</code> is currently interpreted. <code>SFZ</code> opcodes in the <code>.sfz</code> file that are not yet implemented are ignored. Those that are interpreted may or may not work exactly as specified in the RGC Audio documentation (or as described here). </p>
<p> The <code>.pat</code> files that are created are GUS extended patch files, so they can have velocity layers and can be in stereo. If the source <code>.wav</code> file is in stereo, the extended GUS patch derived from it will also be in stereo. In addition to <code>.wav</code> files, you can also use <code>.aiff</code> and <code>.ogg</code> files for samples. 24-bit <code>.wav</code> files are ok, but for GUS patches, they are down-converted to 16 bits, so the extra resolution is lost. When loading patches directly, all 24 bits are used.</p>
<h2>OPCODES</h2>
<p> Here are the opcodes currently intepreted.</p>
<dl>
<dt><code>&lt;group&gt;</code></p>
<dd> Beginning of global opcodes that apply thoughout following regions, until the next <code>&lt;group&gt;</code> or end of file.</p>
<dt><code>&lt;region&gt;</code></p>
<dd> Beginning of local opcodes that apply only until the next <code>&lt;region&gt;</code>, or <code>&lt;group&gt;</code> or end of file.</p>
<dt><code>sample=</code><i>filename</i></p>
<dd> Gives path of a file containing sample data.</p>
<dt><code>key=</code><i>k</i></p>
<dd> Note to play. <i>k</i> is a number 0-127 or an IPN note name (letter A-G, optional # or b, then octave from -1 to 9), and likewise below for all values referred to as <i>k</i>.</p>
<dt><code>hikey=</code><i>k</i></p>
<dd> Highest key of range. Default is 60.</p>
<dt><code>lokey=</code><i>k</i></p>
<dd> Lowest key of range. Default is 60.</p>
<dt><code>pitch_keycenter=</code><i>k</i></p>
<dd> Middle key of range. Default is 60.</p>
<dt><code>hivel=</code><i>v</i></p>
<dd> Highest velocity of range. <i>v</i> is a number 0-127. Default is 127.</p>
<dt><code>lovel=</code><i>v</i></p>
<dd> Highest velocity of range. <i>v</i> is a number 0-127. Default is 0.</p>
<dt><code>offset=</code><i>n</i></p>
<dd> Where patch starts in sample file, in samples from the beginning of the file. Default is 0.</p>
<dt><code>end=</code><i>n</i></p>
<dd> Where patch ends in sample file, in samples. Default is the end of the file.</p>
<dt><code>loop_start=</code><i>n</i></p>
<dd> Where the loop start point of patch is in sample file, in samples. Default is the <code>offset</code> of the sample.</p>
<dt><code>loop_end=</code><i>n</i></p>
<dd> Where the loop end point of patch is in sample file, in samples. Default is the <code>end</code> of the sample.</p>
<dt><code>loop_mode=loop_sustain</code></p>
<dd> Makes the sample loop while note is held. Default is no loop.</p>
<dt><code>volume=</code><i>f</i></p>
<dd> How loud to play the sample, in decibels. Default is 0 decibel change to what is found in the sample file.</p>
<dt><code>amp_random=</code><i>f</i></p>
<dd> The sample is amplified by a randomly selected amount from 0 to <i>f</i>, given in decibels. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>ampeg_release=</code><i>f</i></p>
<dd> Release time for the volume envelope, in seconds.</p>
<dt><code>group=</code><i>n</i></p>
<dd> Defines the group the sample belongs to.</p>
<dt><code>off_by=</code><i>n</i></p>
<dd> The sample will stop playing when a note from group <i>n</i> is started.</p>
<dt><code>trigger=first</code></p>
<dd> The sample will be played only if no other note in the same group (and on the same channel) is playing. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>trigger=legato</code></p>
<dd> The sample will be played only if another note in the same group (and on the same channel) is playing. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>hirand=</code><i>f</i></p>
<dd> The sample plays only when a randomly selected number between 0 and 1 is less than <i>f</i>. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>lorand=</code><i>f</i></p>
<dd> The sample plays only when a randomly selected number between 0 and 1 is greater or equal to <i>f</i>. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>sw_hikey=</code><i>k</i></p>
<dd> Highest key in switch range.</p>
<dt><code>sw_lokey=</code><i>k</i></p>
<dd> Lowest key in switch range.</p>
<dt><code>sw_down=</code><i>k</i></p>
<dd> The sample will play only if note <i>k</i> is playing (on the same channel), provided it falls within the switch range. (This has no effect when creating <code>.pat</code> files.)</p>
<dt><code>sw_up=</code><i>k</i></p>
<dd> The sample will not play if note <i>k</i> is playing (on the same channel), provided it falls within the switch range. (This has no effect when creating <code>.pat</code> files.)</dl>
<h2>BUGS</h2>
<p> Probably, there are lots of bugs. This is an experiment.</p>
<h2>AUTHOR</h2>
<p> Greg Lee &lt;greg [at] ling.lll.hawaii.edu&gt; </p>
<h2>Index</h2>
