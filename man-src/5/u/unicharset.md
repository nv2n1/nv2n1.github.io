---
title: "unicharset(5)"
name: "unicharset"
section: "5"
letter: "u"
url: "/docs/linux/man/5-unicharset/"
description: "unicharset – character properties file used by"
---

<p>unicharset &#8211; character properties file used by </p>
<p><a href="/docs/linux/man/1-tesseract/">tesseract</a>(1)</p>
<h2>Description</h2>
<p>Tesseract&#8217;s unicharset file contains information on each symbol (unichar) the Tesseract OCR engine is trained to recognize. </p>
<p> A unicharset file (i.e. <i>eng.unicharset</i>) is distributed as part of a Tesseract language pack (i.e. <i>eng.traineddata</i>). For information on extracting the unicharset file, see <a href="/docs/linux/man/1-combine_tessdata/">combine_tessdata</a>(1). </p>
<p> The first line of a unicharset file contains the number of unichars in the file. After this line, each subsequent line provides information for a single unichar. The first such line contains a placeholder reserved for the space character. Each unichar is referred to within Tesseract by its Unichar ID, which is the line number (minus 1) within the unicharset file. Therefore, space gets unichar 0. </p>
<p> Each unichar line in the unicharset file (v2+) may have four space-separated fields: </p>
<dl>
<dd>
<pre>'character' 'properties' 'script' 'id'</pre>
</dl>
<p> Starting with Tesseract v3.02, more information may be given for each unichar: </p>
<dl>
<dd>
<pre>'character' 'properties' 'glyph_metrics' 'script' 'other_case' 'direction' 'mirror' 'normed_form'</pre>
</dl>
<p> Entries: </p>
<p> <i>character</i></p>
<dl>
<dd>The UTF-8 encoded string to be produced for this unichar.</dl>
<p> <i>properties</i></p>
<dl>
<dd>An integer mask of character properties, one per bit. From least to most significant bit, these are: isalpha, islower, isupper, isdigit, ispunctuation.</dl>
<p> <i>glyph_metrics</i></p>
<dl>
<dd>Ten comma-separated integers representing various standards for where this glyph is to be found within a baseline-normalized coordinate system where 128 is normalized to x-height. </p>
<dl>
<dd>&bull; min_bottom, max_bottom: the ranges where the bottom of the character can be found.</dl>
<dl>
<dd>&bull; min_top, max_top: the ranges where the top of the character may be found.</dl>
<dl>
<dd>&bull; min_width, max_width: horizontal width of the character.</dl>
<dl>
<dd>&bull; min_bearing, max_bearing: how far from the usual start position does the leftmost part of the character begin.</dl>
<dl>
<dd>&bull; min_advance, max_advance: how far from the printer&#8217;s cell left do we advance to begin the next character.</dl>
</dl>
<p> <i>script</i></p>
<dl>
<dd>Name of the script (Latin, Common, Greek, Cyrillic, Han, null).</dl>
<p> <i>other_case</i></p>
<dl>
<dd>The Unichar ID of the other case version of this character (upper or lower).</dl>
<p> <i>direction</i></p>
<dl>
<dd>The Unicode BiDi direction of this character, as defined by ICU&#8217;s enum UCharDirection. (0 = Left to Right, 1 = Right to Left, 2 = European Number&#8230;)</dl>
<p> <i>mirror</i></p>
<dl>
<dd>The Unichar ID of the BiDirectional mirror of this character. For example the mirror of open paren is close paren, but Latin Capital C has no mirror, so it remains a Latin Capital C.</dl>
<p> <i>normed_form</i></p>
<dl>
<dd>The UTF-8 representation of a &quot;normalized form&quot; of this unichar for the purpose of blaming a module for errors given ground truth text. For instance, a left or right single quote may normalize to an ASCII quote.</dl>
<h2>Example (V2)</h2>
<dl>
<dd>
<pre>; 10 Common 46
b 3 Latin 59
W 5 Latin 40
7 8 Common 66
= 0 Common 93</pre>
</dl>
<p> &quot;;&quot; is a punctuation character. Its properties are thus represented by the binary number 10000 (10 in hexadecimal). </p>
<p> &quot;b&quot; is an alphabetic character and a lower case character. Its properties are thus represented by the binary number 00011 (3 in hexadecimal). </p>
<p> &quot;W&quot; is an alphabetic character and an upper case character. Its properties are thus represented by the binary number 00101 (5 in hexadecimal). </p>
<p> &quot;7&quot; is just a digit. Its properties are thus represented by the binary number 01000 (8 in hexadecimal). </p>
<p> &quot;=&quot; is not punctuation nor a digit nor an alphabetic character. Its properties are thus represented by the binary number 00000 (0 in hexadecimal). </p>
<p> Japanese or Chinese alphabetic character properties are represented by the binary number 00001 (1 in hexadecimal): they are alphabetic, but neither upper nor lower case.</p>
<h2>Example (V3.02)</h2>
<dl>
<dd>
<pre>110
NULL 0 NULL 0
N 5 59,68,216,255,87,236,0,27,104,227 Latin 11 0 1 N
Y 5 59,68,216,255,91,205,0,47,91,223 Latin 33 0 2 Y
1 8 59,69,203,255,45,128,0,66,74,173 Common 3 2 3 1
9 8 18,66,203,255,89,156,0,39,104,173 Common 4 2 4 9
a 3 58,65,186,198,85,164,0,26,97,185 Latin 56 0 5 a
. . .</pre>
</dl>
<h2>Caveats</h2>
<p>Although the unicharset reader maintains the ability to read unicharsets of older formats and will assign default values to missing fields, the accuracy will be degraded. </p>
<p> Further, most other data files are indexed by the unicharset file, so changing it without re-generating the others is likely to have dire consequences.</p>
<h2>History</h2>
<p>The unicharset format first appeared with Tesseract 2.00, which was the first version to support languages other than English. The unicharset file contained only the first two fields, and the &quot;ispunctuation&quot; property was absent (punctuation was regarded as &quot;0&quot;, as &quot;=&quot; is in the above example.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-tesseract/">tesseract</a>(1), <a href="/docs/linux/man/1-combine_tessdata/">combine_tessdata</a>(1), <a href="/docs/linux/man/1-unicharset_extractor/">unicharset_extractor</a>(1) </p>
<p> m[blue]<code><a rel="nofollow" href="https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract">https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract</a></code>m[]</p>
<h2>Author</h2>
<p>The Tesseract OCR engine was written by Ray Smith and his research groups at Hewlett Packard (1985-1995) and Google (2006-present).</p>
