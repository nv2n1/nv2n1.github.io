---
title: "espeak(1)"
name: "espeak"
section: "1"
letter: "e"
url: "/docs/linux/man/1-espeak/"
description: "espeak – A multi-lingual software speech synthesizer."
---

<h2 class="name">NAME</h2>
<p> espeak &#8211; A multi-lingual software speech synthesizer. </p>
<h2>SYNOPSIS</h2>
<p> <code>espeak</code> [<i>options</i>]&nbsp;<wbr>[<i>words</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>espeak</code> is a software speech synthesizer for English, and some other languages.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f</code><i>file</i></p>
<dd> Text file to speak.</p>
<dt><code>&#8211;stdin</code></p>
<dd> Read text input from stdin instead of a file</p>
<dt>If neither <code>-f</code> nor <code>&#8211;stdin</code>, <i>words</i> are spoken, or if none then text is spoken from stdin, each line separately.</p>
<dd>
<dt><code>-a</code><i>integer</i></p>
<dd> Amplitude, 0 to 20, default is 10.</p>
<dt><code>-g</code><i>integer</i></p>
<dd> Word gap. Pause between words, units of 10 ms at the default speed.</p>
<dt><code>-k</code><i>integer</i></p>
<dd> Indicate capital letters with: 1=sound, 2=the word &quot;capitals&quot;, higher values = a pitch increase (try -k20).</p>
<dt><code>-l</code><i>integer</i></p>
<dd> Line length. If not zero (which is the default), consider lines less than this length as and-of-clause.</p>
<dt><code>-p</code><i>integer</i></p>
<dd> Pitch adjustment, 0 to 99, default is 50.</p>
<dt><code>-s</code><i>integer</i></p>
<dd> Speed in words per minute, default is 160.</p>
<dt><code>-v</code><i>voicename</i></p>
<dd> Use voice file of this name from espeak-data/voices.</p>
<dt><code>-w</code><i>file</i></p>
<dd> Write output to this WAV file, rather than speaking it directly.</p>
<dt><code>-b</code></p>
<dd> Input text is 8-bit encoding.</p>
<dt><code>-m</code></p>
<dd> Indicates that the text contains SSML (Speech Synthesis Markup Language) tags or other XML tags. Those SSML tags which are supported are interpreted. Other tags, including HTML, are ignored, except that some HTML tags such as &lt;hr&gt; &lt;h2&gt; and &lt;li&gt; ensure a break in the speech.</p>
<dt><code>-q</code></p>
<dd> Quiet, don&#8217;t produce any speech (may be useful with <code>-x</code>).</p>
<dt><code>-x</code></p>
<dd> Write phoneme mnemonics to stdout.</p>
<dt><code>-X</code></p>
<dd> Write phonemes mnemonics and translation trace to stdout.</p>
<dt><code>-z</code></p>
<dd> No final sentence pause at the end of the text.</p>
<dt><code>&#8211;compile</code><i></i>[<code>=</code>voicename]</p>
<dd> Compile the pronunciation rules and dictionary in the current directory. The <i>voicename</i> is optional and specifies which language to use.</p>
<dt><code>&#8211;ipa</code><i></i>[<code>=</code>ipa]</p>
<dd> Write phonemes to stdout using International Phonetic Alphabet. If <i>ipa</i> is 1 use ties, if 2 use ZWJ, if 3 separate with &quot;_&quot;.</p>
<dt><code>&#8211;path=</code><i>path</i></p>
<dd> Specifies the directory containing the espeak-data directory.</p>
<dt><code>&#8211;pho</code></p>
<dd> Write mbrola phoneme data (.pho) to stdout or to the file in <code>&#8211;phonout</code>.</p>
<dt><code>&#8211;phonout=</code><i>filename</i></p>
<dd> Write output from <code>-x</code>, <code>-X</code> commands and mbrola phoneme data to this file.</p>
<dt><code>&#8211;punct</code><i></i>[<code>=</code>characters]</p>
<dd> Speak the names of punctuation characters during speaking. If <i>characters</i> is omitted, all punctuation is spoken.</p>
<dt><code>&#8211;split=</code><i>minutes</i></p>
<dd> Starts a new WAV file every <i>minutes</i>. Used with <code>-w</code>.</p>
<dt><code>&#8211;stdout</code></p>
<dd> Write speech output to stdout.</p>
<dt><code>&#8211;voices</code><i></i>[<code>=</code>language]</p>
<dd> Lists the available voices. If <i>language</i> is present then only those voices which are suitable for that language are listed.</p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> Show summary of options.</p>
<dt><code>&#8211;version</code></p>
<dd> Show version information.</dl>
<h2>AUTHOR</h2>
<p> eSpeak was written by Jonathan Duddington &lt;jonsd [at] jsd.clara.co.uk&gt;. The webpage for this package can be found at <a rel="nofollow" href="http://espeak.sourceforge.net/.">http://espeak.sourceforge.net/.</a> </p>
<p> This manual page was written by Luke Yelavich &lt;themuso [at] ubuntu.com&gt;, for the Ubuntu project (but may be used by others). Several updates by Jaroslav Škarvada &lt;jskarvad [at] redhat.com&gt;. </p>
<h2>Index</h2>
