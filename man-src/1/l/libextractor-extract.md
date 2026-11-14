---
title: "libextractor-extract(1)"
name: "libextractor-extract"
section: "1"
letter: "l"
url: "/docs/linux/man/1-libextractor-extract/"
description: "extract – determine meta-information about a file"
---

<h2 class="name">NAME</h2>
<p> extract &#8211; determine meta-information about a file </p>
<h2>SYNOPSIS</h2>
<p> <code>extract</code> [ <code>-abdfghLnrsvV</code> ] [ <code>-B</code> <i>language</i> ] [ <code>-H</code> <i>hash-algorithm</i> ] [ <code>-l</code> <i>library</i> ] [ <code>-p</code> <i>type</i> ] [ <code>-x</code> <i>type</i> ] <i>file</i> &#8230; </p>
<h2>DESCRIPTION</h2>
<p> This manual page documents version 0.5.17 of the <code>extract</code> command. </p>
<p> <code>extract</code> tests each file specified in the argument list in an attempt to infer meta-information from it. Each file is subjected to the meta-data extraction libraries from <i>libextractor.</i> </p>
<p> libextractor classifies meta-information (also referred to as keywords) into types. A list of all types can be obtained with the <code>-L</code> option. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-a</code></p>
<dd> Do not remove any duplicates, even if the keywords match exactly and have the same type (i.e. because the same keyword was found by different extractor libraries).</p>
<dt><code>-b</code></p>
<dd> Display the output in BiBTeX format. This implies the <code>-d</code> option</p>
<dt><code>-B LANG</code></p>
<dd> Use the generic plaintext extractor for the language with the 2-letter language code LANG. Supported languages are DA (Danish), DE (German), EN (English), ES (Spanish), FI (Finnish), FR (French), GA (Gaelic), IT (Italian), NO (Norwegian) and SV (Swedish).</p>
<dt><code>-d</code></p>
<dd> Remove duplicates only if the types match exactly. By default, duplicates are removed if the types match or if one of the types is I unknown (in this case, the duplicate of unknown type is removed).</p>
<dt><code>-f</code></p>
<dd> add the filename(s) (without directory) to the list of keywords.</p>
<dt><code>-g</code></p>
<dd> Use grep-friendly output (all keywords on a single line for each file). Use the verbose option to print the filename first, followed by the keywords. Use the verbose option twice to also display the keyword types. This option will not print keyword types or non-textual metadata.</p>
<dt><code>-h</code></p>
<dd> Print a brief summary of the options.</p>
<dt><code>-H ALGORITHM</code></p>
<dd> Use the ALGORITHM to compute a hash of each file (possible algorithms are sha1 and md5).</p>
<dt><code>-L</code></p>
<dd> Print a list of all known keyword types.</p>
<dt><code>-n</code></p>
<dd> Do not use the default set of extractors (typically all standard extractors, currently mp3, ogg, jpg, gif, png, tiff, real, html, pdf and mime-types), use only the extractors specified with the .B -l option.</p>
<dt><code>-r</code></p>
<dd> Remove all duplicates disregarding differences in the keyword type.</p>
<dt><code>-s</code></p>
<dd> Split keywords at delimiters (space, comma, colon, etc.) and list split keywords to be of .I unknown type. This can also be done by loading the split-library. Using this option guarantees that the splitting is performed after all other libraries have been run. It is always performed before duplicate elimination.</p>
<dt><code>-v</code></p>
<dd> Print the version number and exit.</p>
<dt><code>-V</code></p>
<dd> Be verbose.</p>
<dt><code>-B</code></p>
<dd> Run the printable extractor (costly, generic extractor for binaries)</p>
<dt><code>-l</code><i> libraries</i></p>
<dd> Use the specified libraries to extract keywords. The general format of libraries is .I [[-]LIBRARYNAME[:[-]LIBRARYNAME]*] where LIBRARYNAME is a libextractor compatible library and typically of the form .I libextractor_jpeg.so. The minus before the libraryname indicates that this library should be run after all the libraries that were specified so far. If the minus is missing, the library is run before all previously specified libraries.</p>
<dt><code>-p</code><i> type</i></p>
<dd> Print only the keywords matching the specified type. By default, all keywords that are found and not removed as duplicates are printed.</p>
<dt><code>-x</code><i> type</i></p>
<dd> Exclude keywords of the specified type from the output. By default, all keywords that are found and not removed as duplicates are printed.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-libextractor/">libextractor</a></code>(3) &#8211; description of the libextractor library </p>
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
<h2>Index</h2>
