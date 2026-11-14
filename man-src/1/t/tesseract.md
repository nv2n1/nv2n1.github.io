---
title: "tesseract(1)"
name: "tesseract"
section: "1"
letter: "t"
url: "/docs/linux/man/1-tesseract/"
description: "tesseract – command-line OCR engine"
---

<h2 class="name">NAME</h2>
<p> tesseract &#8211; command-line OCR engine </p>
<h2>SYNOPSIS</h2>
<p> <code>tesseract</code> <i>imagename</i>|<i>stdin</i> <i>outputbase</i>|<i>stdout</i> [options&#8230;] [configfile&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <a href="/docs/linux/man/1-tesseract/">tesseract</a>(1) is a commercial quality OCR engine originally developed at HP between 1985 and 1995. In 1995, this engine was among the top 3 evaluated by UNLV. It was open-sourced by HP and UNLV in 2005, and has been developed at Google since then.</p>
<h2>IN/OUT ARGUMENTS</h2>
<p> <i>imagename</i></p>
<dl>
<dt>
<dd> The name of the input image. Most image file formats (anything readable by Leptonica) are supported.</dl>
<p> <i>stdin</i></p>
<dl>
<dt>
<dd> Instruction to read data from standard input</dl>
<p> <i>outputbase</i></p>
<dl>
<dt>
<dd> The basename of the output file (to which the appropriate extension will be appended). By default the output will be named <i>outbase.txt</i>.</dl>
<p> <i>stdout</i></p>
<dl>
<dt>
<dd> Instruction to sent output data to standard output</dl>
<h2>OPTIONS</h2>
<p> <i>&#8211;tessdata-dir /path</i></p>
<dl>
<dt>
<dd> Specify the location of tessdata path</dl>
<p> <i>&#8211;user-words /path/to/file</i></p>
<dl>
<dt>
<dd> Specify the location of user words file</dl>
<p> <i>&#8211;user-patterns /path/to/file specify</i></p>
<dl>
<dt>
<dd> The location of user patterns file</dl>
<p> <i>-c configvar=value</i></p>
<dl>
<dt>
<dd> Set value for control parameter. Multiple -c arguments are allowed.</dl>
<p> <i>-l lang</i></p>
<dl>
<dt>
<dd> The language to use. If none is specified, English is assumed. Multiple languages may be specified, separated by plus characters. Tesseract uses 3-character ISO 639-2 language codes. (See LANGUAGES)</dl>
<p> <i>-psm N</i></p>
<dl>
<dt>
<dd> Set Tesseract to only run a subset of layout analysis and assume a certain form of image. The options for <code>N</code> are: </p>
<dl>
<dt>
<dd>
<pre>
0 = Orientation and script detection (OSD) only.
1 = Automatic page segmentation with OSD.
2 = Automatic page segmentation, but no OSD, or OCR.
3 = Fully automatic page segmentation, but no OSD. (Default)
4 = Assume a single column of text of variable sizes.
5 = Assume a single uniform block of vertically aligned text.
6 = Assume a single uniform block of text.
7 = Treat the image as a single text line.
8 = Treat the image as a single word.
9 = Treat the image as a single word in a circle.
10 = Treat the image as a single character.
</pre>
</dl>
</dl>
<p> <i>configfile</i></p>
<dl>
<dt>
<dd> The name of a config to use. A config is a plaintext file which contains a list of variables and their values, one per line, with a space separating variable from value. Interesting config files include: </p>
<dl>
<dt>
<dd> &bull; hocr &#8211; Output in hOCR format instead of as a text file.</dl>
<dl>
<dt>
<dd> &bull; pdf &#8211; Output in pdf instead of a text file.</dl>
</dl>
<p> <code>Nota Bene:</code> The options <i>-l lang</i> and <i>-psm N</i> must occur before any <i>configfile</i>.</p>
<h2>SINGLE OPTIONS</h2>
<p> <i>-v</i></p>
<dl>
<dt>
<dd> Returns the current version of the <a href="/docs/linux/man/1-tesseract/">tesseract</a>(1) executable.</dl>
<p> <i>&#8211;list-langs</i></p>
<dl>
<dt>
<dd> list available languages for tesseract engine. Can be used with &#8211;tessdata-dir.</dl>
<p> <i>&#8211;print-parameters</i></p>
<dl>
<dt>
<dd> print tesseract parameters to the stdout.</dl>
<h2>LANGUAGES</h2>
<p> There are currently language packs available for the following languages (in m[blue]<code><a rel="nofollow" href="https://github.com/tesseract-ocr/tessdata">https://github.com/tesseract-ocr/tessdata</a></code>m[]): </p>
<p> <code>afr</code> (Afrikaans) <code>amh</code> (Amharic) <code>ara</code> (Arabic) <code>asm</code> (Assamese) <code>aze</code> (Azerbaijani) <code>aze_cyrl</code> (Azerbaijani &#8211; Cyrilic) <code>bel</code> (Belarusian) <code>ben</code> (Bengali) <code>bod</code> (Tibetan) <code>bos</code> (Bosnian) <code>bul</code> (Bulgarian) <code>cat</code> (Catalan; Valencian) <code>ceb</code> (Cebuano) <code>ces</code> (Czech) <code>chi_sim</code> (Chinese &#8211; Simplified) <code>chi_tra</code> (Chinese &#8211; Traditional) <code>chr</code> (Cherokee) <code>cym</code> (Welsh) <code>dan</code> (Danish) <code>dan_frak</code> (Danish &#8211; Fraktur) <code>deu</code> (German) <code>deu_frak</code> (German &#8211; Fraktur) <code>dzo</code> (Dzongkha) <code>ell</code> (Greek, Modern (1453-)) <code>eng</code> (English) <code>enm</code> (English, Middle (1100-1500)) <code>epo</code> (Esperanto) <code>equ</code> (Math / equation detection module) <code>est</code> (Estonian) <code>eus</code> (Basque) <code>fas</code> (Persian) <code>fin</code> (Finnish) <code>fra</code> (French) <code>frk</code> (Frankish) <code>frm</code> (French, Middle (ca.1400-1600)) <code>gle</code> (Irish) <code>glg</code> (Galician) <code>grc</code> (Greek, Ancient (to 1453)) <code>guj</code> (Gujarati) <code>hat</code> (Haitian; Haitian Creole) <code>heb</code> (Hebrew) <code>hin</code> (Hindi) <code>hrv</code> (Croatian) <code>hun</code> (Hungarian) <code>iku</code> (Inuktitut) <code>ind</code> (Indonesian) <code>isl</code> (Icelandic) <code>ita</code> (Italian) <code>ita_old</code> (Italian &#8211; Old) <code>jav</code> (Javanese) <code>jpn</code> (Japanese) <code>kan</code> (Kannada) <code>kat</code> (Georgian) <code>kat_old</code> (Georgian &#8211; Old) <code>kaz</code> (Kazakh) <code>khm</code> (Central Khmer) <code>kir</code> (Kirghiz; Kyrgyz) <code>kor</code> (Korean) <code>kur</code> (Kurdish) <code>lao</code> (Lao) <code>lat</code> (Latin) <code>lav</code> (Latvian) <code>lit</code> (Lithuanian) <code>mal</code> (Malayalam) <code>mar</code> (Marathi) <code>mkd</code> (Macedonian) <code>mlt</code> (Maltese) <code>msa</code> (Malay) <code>mya</code> (Burmese) <code>nep</code> (Nepali) <code>nld</code> (Dutch; Flemish) <code>nor</code> (Norwegian) <code>ori</code> (Oriya) <code>osd</code> (Orientation and script detection module) <code>pan</code> (Panjabi; Punjabi) <code>pol</code> (Polish) <code>por</code> (Portuguese) <code>pus</code> (Pushto; Pashto) <code>ron</code> (Romanian; Moldavian; Moldovan) <code>rus</code> (Russian) <code>san</code> (Sanskrit) <code>sin</code> (Sinhala; Sinhalese) <code>slk</code> (Slovak) <code>slk_frak</code> (Slovak &#8211; Fraktur) <code>slv</code> (Slovenian) <code>spa</code> (Spanish; Castilian) <code>spa_old</code> (Spanish; Castilian &#8211; Old) <code>sqi</code> (Albanian) <code>srp</code> (Serbian) <code>srp_latn</code> (Serbian &#8211; Latin) <code>swa</code> (Swahili) <code>swe</code> (Swedish) <code>syr</code> (Syriac) <code>tam</code> (Tamil) <code>tel</code> (Telugu) <code>tgk</code> (Tajik) <code>tgl</code> (Tagalog) <code>tha</code> (Thai) <code>tir</code> (Tigrinya) <code>tur</code> (Turkish) <code>uig</code> (Uighur; Uyghur) <code>ukr</code> (Ukrainian) <code>urd</code> (Urdu) <code>uzb</code> (Uzbek) <code>uzb_cyrl</code> (Uzbek &#8211; Cyrilic) <code>vie</code> (Vietnamese) <code>yid</code> (Yiddish) </p>
<p> To use a non-standard language pack named <code>foo.traineddata</code>, set the <code>TESSDATA_PREFIX</code> environment variable so the file can be found at <code>TESSDATA_PREFIX</code>/tessdata/<code>foo</code>.traineddata and give Tesseract the argument <i>-l foo</i>.</p>
<h2>CONFIG FILES AND AUGMENTING WITH USER DATA</h2>
<p> Tesseract config files consist of lines with variable-value pairs (space separated). The variables are documented as flags in the source code like the following one in tesseractclass.h: </p>
<p> STRING_VAR_H(tessedit_char_blacklist, &quot;&quot;, &quot;Blacklist of chars not to recognize&quot;); </p>
<p> These variables may enable or disable various features of the engine, and may cause it to load (or not load) various data. For instance, let&#8217;s suppose you want to OCR in English, but suppress the normal dictionary and load an alternative word list and an alternative list of patterns &#8212; these two files are the most commonly used extra data files. </p>
<p> If your language pack is in /path/to/eng.traineddata and the hocr config is in /path/to/configs/hocr then create three new files: </p>
<p> /path/to/eng.user-words: </p>
<dl>
<dt>
<dd>
<pre>
the
quick
brown
fox
jumped
</pre>
</dl>
<p> /path/to/eng.user-patterns: </p>
<dl>
<dt>
<dd>
<pre>
1-\d\d\d-GOOG-411
www.
\\*.com
</pre>
</dl>
<p> /path/to/configs/bazaar: </p>
<dl>
<dt>
<dd>
<pre>
load_system_dawg     F
load_freq_dawg       F
user_words_suffix    user-words
user_patterns_suffix user-patterns
</pre>
</dl>
<p> Now, if you pass the word <i>bazaar</i> as a trailing command line parameter to Tesseract, Tesseract will not bother loading the system dictionary nor the dictionary of frequent words and will load and use the eng.user-words and eng.user-patterns files you provided. The former is a simple word list, one per line. The format of the latter is documented in dict/trie.h on read_pattern_list().</p>
<h2>HISTORY</h2>
<p> The engine was developed at Hewlett Packard Laboratories Bristol and at Hewlett Packard Co, Greeley Colorado between 1985 and 1994, with some more changes made in 1996 to port to Windows, and some C++izing in 1998. A lot of the code was written in C, and then some more was written in C++. The C\++ code makes heavy use of a list system using macros. This predates stl, was portable before stl, and is more efficient than stl lists, but has the big negative that if you do get a segmentation violation, it is hard to debug. </p>
<p> Version 2.00 brought Unicode (UTF-8) support, six languages, and the ability to train Tesseract. </p>
<p> Tesseract was included in UNLV&#8217;s Fourth Annual Test of OCR Accuracy. See m[blue]<code><a rel="nofollow" href="https://github.com/tesseract-ocr/docs/blob/master/AT-1995.pdf">https://github.com/tesseract-ocr/docs/blob/master/AT-1995.pdf</a></code>m[]. With Tesseract 2.00, scripts are now included to allow anyone to reproduce some of these tests. See m[blue]<code><a href="https://github.com/tesseract-ocr/tesseract/wiki/TestingTesseract">https://github.com/tesseract-ocr/tesseract/wiki/TestingTesseract</a></code>m[] for more details. </p>
<p> Tesseract 3.00 adds a number of new languages, including Chinese, Japanese, and Korean. It also introduces a new, single-file based system of managing language data. </p>
<p> Tesseract 3.02 adds BiDirectional text support, the ability to recognize multiple languages in a single image, and improved layout analysis. </p>
<p> For further details, see the file ReleaseNotes included with the distribution.</p>
<h2>RESOURCES</h2>
<p> Main web site: m[blue]<code><a rel="nofollow" href="https://github.com/tesseract-ocr">https://github.com/tesseract-ocr</a></code>m[] Information on training: m[blue]<code><a href="https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract">https://github.com/tesseract-ocr/tesseract/wiki/TrainingTesseract</a></code>m[]</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-ambiguous_words/">ambiguous_words</a>(1), <a href="/docs/linux/man/1-cntraining/">cntraining</a>(1), <a href="/docs/linux/man/1-combine_tessdata/">combine_tessdata</a>(1), <a href="/docs/linux/man/1-dawg2wordlist/">dawg2wordlist</a>(1), <a href="/docs/linux/man/1-shape_training/">shape_training</a>(1), <a href="/docs/linux/man/1-mftraining/">mftraining</a>(1), <a href="/docs/linux/man/5-unicharambigs/">unicharambigs</a>(5), <a href="/docs/linux/man/5-unicharset/">unicharset</a>(5), <a href="/docs/linux/man/1-unicharset_extractor/">unicharset_extractor</a>(1), <a href="/docs/linux/man/1-wordlist2dawg/">wordlist2dawg</a>(1)</p>
<h2>AUTHOR</h2>
<p> Tesseract development was led at Hewlett-Packard and Google by Ray Smith. The development team has included: </p>
<p> Ahmad Abdulkader, Chris Newton, Dan Johnson, Dar-Shyang Lee, David Eger, Eric Wiseblatt, Faisal Shafait, Hiroshi Takenaka, Joe Liu, Joern Wanke, Mark Seaman, Mickey Namiki, Nicholas Beato, Oded Fuhrmann, Phil Cheatle, Pingping Xiu, Pong Eksombatchai (Chantat), Ranjith Unnikrishnan, Raquel Romano, Ray Smith, Rika Antonova, Robert Moss, Samuel Charron, Sheelagh Lloyd, Shobhit Saxena, and Thomas Kielbus.</p>
<h2>COPYING</h2>
<p> Licensed under the Apache License, Version 2.0 </p>
<h2>Index</h2>
