---
title: "gocr(1)"
name: "gocr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gocr/"
description: "gocr – command line text recognition tool"
---

<h2>NAME</h2>
<p> gocr &#8211; command line text recognition tool</p>
<h2>SYNOPSIS</h2>
<p> <code>gocr</code> [<i>OPTION</i>] [<code>-i</code>] <i>pnm-file</i></p>
<h2>DESCRIPTION</h2>
<p> gocr is an optical character recognition program that can be used from the command line. It takes input in PNM, PGM, PBM, PPM, or PCX format, and writes recognized text to <code>stdout</code>. If the <i>pnm file</i> is a single dash, PNM data is read from <code>stdin</code>. If gzip, bzip2 and netpbm-progs are installed and your system supports <a href="/docs/linux/man/3-popen/">popen</a>(3) also pnm.gz, pnm.bz2, png, jpg, jpeg, tiff, gif, bmp, ps (only single pages) and eps are supported as input files (not as input stream), where pnm can be replaced by one of ppm, pgm and pbm.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></p>
<dd> show usage information</p>
<dt><code>-i</code> <i>file</i></p>
<dd> read input from <i>file</i> (or <code>stdin</code> if <i>file</i> is a single dash)</p>
<dt><code>-o</code> <i>file</i></p>
<dd> send output to <i>file</i> instead of <code>stdout</code></p>
<dt><code>-e</code> <i>file</i></p>
<dd> send errors to <i>file</i> instead of <code>stderr</code> or to <code>stdout</code> if <i>file</i> is a dash</p>
<dt><code>-x</code> <i>file</i></p>
<dd> progress output to <i>file</i> (<i>file</i> can be a file name, a fifo name or a file descriptor 1&#8230;255), this is useful for GUI developpers to show the OCR progress, the file descriptor argument is only available, if compiled with __USE_POSIX defined</p>
<dt><code>-p</code> <i>path</i></p>
<dd> database path, a final slash must be included, default is ./db/, this path will be populated with images of learned characters</p>
<dt><code>-f</code> <i>format</i></p>
<dd> output <i>format</i> of the recognized text (ISO8859_1 TeX HTML XML UTF8 ASCII), XML will also output position and probability data</p>
<dt><code>-l</code> <i>level</i></p>
<dd> set grey level to <i>level</i> (0&lt;160&lt;=255, default: 0 for autodetect), darker pixels belong to characters, brighter pixels are interpreted as background of the input image</p>
<dt><code>-d</code> <i>size</i></p>
<dd> set dust size in pixels (clusters smaller than this are removed), 0 means no clusters are removed, the default is -1 for auto detection</p>
<dt><code>-s</code> <i>num</i></p>
<dd> set spacewidth between words in units of dots (default: 0 for autodetect), wider widths are interpreted as word spaces, smaller as character spaces</p>
<dt><code>-v</code> <i>verbosity</i></p>
<dd> be verbose to stderr; <i>verbosity</i> is a bitfield</p>
<dt><code>-c </code><i>string</i></p>
<dd> only verbose output of characters from <i>string</i> to stderr, more output is generated for all characters within the string, the underscore stands for unknown chars, this function is usefull to limit debug information to the necessary one</p>
<dt><code>-C </code><i>string</i></p>
<dd> only recognise characters from <i>string</i>, this is a filter function in cases where the interest is only to a part of the character alphabet, you can use 0-9 or a-z to specify ranges, use &#8212; to detect the minus sign</p>
<dt><code>-a</code> <i>certainty</i></p>
<dd> set value for certainty of recognition (0..100; default: 95), characters with a higher certainty are accepted, characters with a lower certainty are treated as unknown (not recognized); set higher values, if you want to have only more certain recognized characters</p>
<dt><code>-u </code><i>string</i></p>
<dd> output this string for every unrecognized character (default is &quot;_&quot;)</p>
<dt><code>-m</code> <i>mode</i></p>
<dd> set oprational mode; mode is a bitfield (default: 0)</p>
<dt><code>-n</code> <i>bool</i></p>
<dd> if <i>bool</i> is non-zero, only recognise numbers (this is now obsolete, use -C &quot;0123456789&quot;)</dl>
<p> The verbosity is specified as a bitfield:</p>
<dl>
<dt><code>1</code></p>
<dd> print more info</p>
<dt><code>2</code></p>
<dd> list shapes of boxes (see -c) to stderr</p>
<dt><code>4</code></p>
<dd> list pattern of boxes (see -c) to stderr</p>
<dt><code>8</code></p>
<dd> print pattern after recognition for debugging</p>
<dt><code>16</code></p>
<dd> print debug information about recognition of lines to stderr</p>
<dt><code>32</code></p>
<dd> create outXX.png with boxes and lines marked on each general OCR-step</dl>
<p> The operation modes are:</p>
<dl>
<dt><code>2</code></p>
<dd> use database to recognize characters which are not recognized by other algorithms, (early development)</p>
<dt><code>4</code></p>
<dd> switching on layout analysis or zoning (development)</p>
<dt><code>8</code></p>
<dd> don&#8217;t compare unrecognized characters to recognized one</p>
<dt><code>16</code></p>
<dd> don&#8217;t try to divide overlapping characters to two or three single characters</p>
<dt><code>32</code></p>
<dd> don&#8217;t do context correction</p>
<dt><code>64</code></p>
<dd> character packing, before recognition starts, similar characters are searched and only one of this characters will be send to the recognition engine (development)</p>
<dt><code>130</code></p>
<dd> extend database, prompts user for unidentified characters and extends the database with users answer (128+2, early development)</p>
<dt><code>256</code></p>
<dd> switch off the recognition engine (makes sense together with -m 2)</dl>
<h2>
<h2>AUTHOR</h2>
</h2>
<p> Joerg Schulenburg (see <a rel="nofollow" href="http://jocr.sourceforge.net/">http://jocr.sourceforge.net/</a> for EMAIL)<br />
 First version of man page by Tim Waugh &lt;twaugh [at] redhat.com&gt;</p>
<h2>VERSION INFORMATION</h2>
<p> This man page documents <code>gocr</code>, version 0.41.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to Joerg Schulenburg</p>
<h2>SEE ALSO</h2>
<p> More details can be found at /usr/share/doc/gocr-<code>X.XX</code>/gocr.html. Also read /usr/share/doc/gocr-<code>X.XX</code>/README to learn, how to improve results.</p>
<h2>EXAMPLES</h2>
<dl>
<dt><code>gocr -v 33 text1.pbm</code></p>
<dd> output verbose information, out30.png is created to see details of recognition process</p>
<dt><code>gocr -v 7 -c _YV text1.pbm</code></p>
<dd> verbose output for unknown chars and chars Y and V</p>
<dt><code>djpeg -pnm -gray text.jpg | gocr &#8211;</code></p>
<dd> convert a jpeg file to pnm format and input via pipe </p>
</dl>
<h2>Index</h2>
