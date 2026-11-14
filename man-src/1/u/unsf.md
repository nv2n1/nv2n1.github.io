---
title: "unsf(1)"
name: "unsf"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unsf/"
description: "unsf – break up SoundFont .sf2 files into GUS-type instrument patches."
---

<h2>NAME</h2>
<p> unsf &#8211; break up SoundFont .sf2 files into GUS-type instrument patches. </p>
<h2>SYNOPSIS</h2>
<p> <code>unsf</code> [<i>-v|-s|-m|-d|-n|-V</i>] [<i>-M &lt;bank&gt;:&lt;instrument&gt;=&lt;layer&gt;</i>] [<i>-D &lt;bank&gt;:&lt;instrument&gt;=&lt;layer&gt;</i>] <code>soundfont-file</code> </p>
<h2>DESCRIPTION</h2>
<p> Unsf is a tool to convert SoundFont files into GUS patches. Some reasons you might want to do such a thing are: (1) Your midi player can use GUS patches but doesn&#8217;t know how to read soundfonts, (2) You want a convenient way of substituting patches or reassigning banks of instruments by editing GUS config files, or (3) You need to modify patches by changing amplitude, stripping envelopes, or make other changes that can easily be done by attaching options in config files. Or (4), my own reason, you might need to use a version of timidity covered under the Lessor GNU Public License and find that the versions of timidity that can read soundfonts are protected by the more restrictive GNU Public License (e.g., Timidity++ or kmidi, or the Alsaplayer midi plugin). </p>
<p> Instrument samples embedded in soundfonts have a more complicated structure, and have more features, than GUS patches. So breaking a soundfont up into GUS patches loses information and quality, unless the GUS patch format is extended. The patch files produced by unsf do contain most of the information and structure they had as part of the original soundfont, but the extensions to GUS format are tucked away in hidden places, as they must be, to be compatible with programs expecting to see ordinary GUS patches. I&#8217;ll describe the extensions below. </p>
<p> Unsf is easy to use. If you&#8217;re using a version of timidity, just put a soundfont into the directory where you keep patches &#8212; perhaps /usr/local/lib/timidity &#8212; then cd to that directory and say &quot;unsf filename.sf2&quot;. Unsf will create directories for each bank of instruments in the soundfont and put the patch files for all the instruments into the appropriate bank directories. The names of the directories and patch files are derived from the names they were given inside the soundfont. Unsf also creates a GUS type configuration file, which will be called &quot;&lt;filename&gt;.cfg&quot;, the &lt;filename&gt; part coming from the name of the original soundfont. Edit timidity.cfg by adding the line &quot;source &lt;filename&gt;.cfg&quot; and you&#8217;re ready to use the new patches. </p>
<p> However, you won&#8217;t hear any of the enhancements of sf2 instruments, unless you use my reference version of timidity, because no other midi players as yet know how to find the special information in the extended GUS patch files. How could there be any? I just made up this extension to GUS patch structure. What you will hear is only the keyrange set of samples for the left channel of the first velocity layer. Sf2 instruments can have several velocity layers, meaning sets of samples tuned for the different timbres produced by different note loudness, and they can also be in stereo, with different sets of samples for the left and right channels. </p>
<p> This diagram describes the overall structure of sf2 instruments and extended GUS patches: </p>
<pre>
                                                key range 1   sample |GUS
                                left channel    key range 2   sample |compatible
             velocity range 1                   ...                  |part
                                                key range 1   sample
                                right channel   key range 2   sample
                                                        ...
                                left channel    ...
Instrument   velocity range 2
                                right channel   ...
             velocity range 3   ...
             ...
             velocity range 19  ...
</pre>
<p> In addition to the extra sets of samples for various velocity (loudness) ranges and for left and right channels, sf2 instruments have parameters for controlling an extra low frequency modulator and a bandpass filter. These parameters are also carried over into the extended GUS patches produced by unsf. My reference version of timidity does not interpret and use all this extra information, by any means, but it does understand velocity ranges, stereo instruments, and a couple of the extra sf2 parameters: volume-envelope-delay and exclusive-class. The first delays the beginning of note volume envelopes by a variable amount, and the second causes notes of certain instruments to be terminated when a new note of that instrument or an instrument in the same class is begun. </p>
<p> My reference version of timidity is the one contained the the SDL_mixer library of the gaming program library SDL (Simple Direct Layer), <a rel="nofollow" href="http://www.libsdl.org.">http://www.libsdl.org.</a> As of now (Sept 2004) only the CVS version of SDL_mixer has my version of timidity. My patches for the latest released version are in the archive:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr><a href="ftp://ling.lll.hawaii.edu/pub/greg/Surround-SDL.tgz">ftp://ling.lll.hawaii.edu/pub/greg/Surround-SDL.tgz</a></dl>
<p> I have also made a free standing demo version of timidity, which is in:</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr><a href="ftp://ling.lll.hawaii.edu/pub/greg/gt-0.3.tar.gz">ftp://ling.lll.hawaii.edu/pub/greg/gt-0.3.tar.gz</a></dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-s</code></p>
<dd> Small. Extract only a single velocity layer.</p>
<dt><code>-m</code></p>
<dd> Mono. Extract only the left channel of stereo patches.</p>
<dt><code>-d</code></p>
<dd> Drum. Assume the sf2 file is a drum kit, even though it is not marked as such in the soundfont, so that individual notes are broken out into separate drum patches.</p>
<dt><code>-n</code></p>
<dd> No write. Don&#8217;t write out patches or directories.</p>
<dt><code>-V</code></p>
<dd> Do not normalize sample volumes (it&#8217;s time-consuming).</p>
<dt><code>-F</code></p>
<dd> Adjust sustain by guessing which looping patches should be continued until note is released.</p>
<dt><code>-v</code></p>
<dd> Verbose.</p>
<dt><code>-M </code><i>&lt;bank&gt;:&lt;instrument&gt;=&lt;layer&gt;</i></p>
<dd> Make the given velocity <i>layer</i> the default for <i>bank:instrument</i>, this affects programs which do not know howto handle the extended GUS patch format, as they will always play the default layer, and this determines which layer gets written when using <code>-s</code>.</p>
<dt><code>-D </code><i>&lt;bank&gt;:&lt;instrument&gt;=&lt;layer&gt;</i></p>
<dd> Same as <code>-M</code> but then for drum banks. </p>
</dl>
<h2>AUTHORS</h2>
<p> Greg Lee &lt;greg [at] ling.lll.hawaii.edu&gt;<br />
 SoundFont loader based on code provided by George Foot.<br />
 SoundFont file extension written by Takashi Iwai &lt;iwai [at] dragon.mm.t.u-tokyo.ac.jp&gt; </p>
<h2>Index</h2>
