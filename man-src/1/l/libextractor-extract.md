---

title: "libextractor-extract(1)"
name: "libextractor-extract"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libextractor-extract/"
description: "extract – determine meta-information about a file"
---

<p> <code>extract</code> [ <code>-abdfghLnrsvV</code> ] [ <code>-B</code> <i>language</i> ] [ <code>-H</code> <i>hash-algorithm</i> ] [ <code>-l</code> <i>library</i> ] [ <code>-p</code> <i>type</i> ] [ <code>-x</code> <i>type</i> ] <i>file</i> &#8230; </p>
<p> This manual page documents version 0.5.17 of the <code>extract</code> command. </p>
<p> <code>extract</code> tests each file specified in the argument list in an attempt to infer meta-information from it. Each file is subjected to the meta-data extraction libraries from <i>libextractor.</i> </p>
<p> libextractor classifies meta-information (also referred to as keywords) into types. A list of all types can be obtained with the <code>-L</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></dt>
<dd> Do not remove any duplicates, even if the keywords match exactly and have the same type (i.e. because the same keyword was found by different extractor libraries).</dd>
<dt><code>-b</code></dt>
<dd> Display the output in BiBTeX format. This implies the <code>-d</code> option</dd>
<dt><code>-B LANG</code></dt>
<dd> Use the generic plaintext extractor for the language with the 2-letter language code LANG. Supported languages are DA (Danish), DE (German), EN (English), ES (Spanish), FI (Finnish), FR (French), GA (Gaelic), IT (Italian), NO (Norwegian) and SV (Swedish).</dd>
<dt><code>-d</code></dt>
<dd> Remove duplicates only if the types match exactly. By default, duplicates are removed if the types match or if one of the types is I unknown (in this case, the duplicate of unknown type is removed).</dd>
<dt><code>-f</code></dt>
<dd> add the filename(s) (without directory) to the list of keywords.</dd>
<dt><code>-g</code></dt>
<dd> Use grep-friendly output (all keywords on a single line for each file). Use the verbose option to print the filename first, followed by the keywords. Use the verbose option twice to also display the keyword types. This option will not print keyword types or non-textual metadata.</dd>
<dt><code>-h</code></dt>
<dd> Print a brief summary of the options.</dd>
<dt><code>-H ALGORITHM</code></dt>
<dd> Use the ALGORITHM to compute a hash of each file (possible algorithms are sha1 and md5).</dd>
<dt><code>-L</code></dt>
<dd> Print a list of all known keyword types.</dd>
<dt><code>-n</code></dt>
<dd> Do not use the default set of extractors (typically all standard extractors, currently mp3, ogg, jpg, gif, png, tiff, real, html, pdf and mime-types), use only the extractors specified with the .B -l option.</dd>
<dt><code>-r</code></dt>
<dd> Remove all duplicates disregarding differences in the keyword type.</dd>
<dt><code>-s</code></dt>
<dd> Split keywords at delimiters (space, comma, colon, etc.) and list split keywords to be of .I unknown type. This can also be done by loading the split-library. Using this option guarantees that the splitting is performed after all other libraries have been run. It is always performed before duplicate elimination.</dd>
<dt><code>-v</code></dt>
<dd> Print the version number and exit.</dd>
<dt><code>-V</code></dt>
<dd> Be verbose.</dd>
<dt><code>-B</code></dt>
<dd> Run the printable extractor (costly, generic extractor for binaries)</dd>
<dt><code>-l</code><i> libraries</i></dt>
<dd> Use the specified libraries to extract keywords. The general format of libraries is .I [[-]LIBRARYNAME[:[-]LIBRARYNAME]*] where LIBRARYNAME is a libextractor compatible library and typically of the form .I libextractor_jpeg.so. The minus before the libraryname indicates that this library should be run after all the libraries that were specified so far. If the minus is missing, the library is run before all previously specified libraries.</dd>
<dt><code>-p</code><i> type</i></dt>
<dd> Print only the keywords matching the specified type. By default, all keywords that are found and not removed as duplicates are printed.</dd>
<dt><code>-x</code><i> type</i></dt>
<dd> Exclude keywords of the specified type from the output. By default, all keywords that are found and not removed as duplicates are printed.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code>libextractor</code>(3) &#8211; description of the libextractor library </p>
<h2>EXAMPLES</h2>
<pre>
$ extract test/test.jpg
comment - (C) 2001 by Christian Grothoff, using gimp 1.2 1
mimetype - image/jpeg
$ extract -Vf -x comment test/test.jpg
Keywords for file test/test.jpg:
mimetype - image/jpeg
filename - test.jpg
$ extract -p comment test/test.jpg
comment - (C) 2001 by Christian Grothoff, using gimp 1.2 1
$ extract -nV -l libextractor_png.so -p comment test/test.jpg test/test.png
Keywords for file test/test.jpg:
Keywords for file test/test.png:
comment - Testing keyword extraction
</pre>
<h2>LEGAL NOTICE</h2>
<p> libextractor and the extract tool are released under the GPL. libextractor is a GNU project. </p>
<h2>BUGS</h2>
<p> A couple of file-formats (on the order of 10^3) are not recognized&#8230; </p>
<h2>AUTHORS</h2>
<p> <code>extract</code> was originally written by Christian Grothoff &lt;christian [at] grothoff.org&gt; and Vidyut Samanta &lt;vids [at] cs.ucla.edu&gt;. Use &lt;libextractor [at] gnu.org&gt; to contact the current maintainer(s). </p>
<h2>AVAILABILITY</h2>
<p> You can obtain the original author&#8217;s latest version from <a rel="nofollow" href="http://gnunet.org/libextractor/">http://gnunet.org/libextractor/</a> </p>
