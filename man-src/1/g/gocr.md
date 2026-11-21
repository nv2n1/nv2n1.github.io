---

title: "gocr(1)"
name: "gocr"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gocr/"
description: "gocr – command line text recognition tool"
---

<p> gocr &#8211; command line text recognition tool</p>
<h2>SYNOPSIS</h2>
<p> <code>gocr</code> [<i>OPTION</i>] [<code>-i</code>] <i>pnm-file</i></p>
<h2>DESCRIPTION</h2>
<p> gocr is an optical character recognition program that can be used from the command line. It takes input in PNM, PGM, PBM, PPM, or PCX format, and writes recognized text to <code>stdout</code>. If the <i>pnm file</i> is a single dash, PNM data is read from <code>stdin</code>. If gzip, bzip2 and netpbm-progs are installed and your system supports <a href="/docs/linux/man/3-popen/">popen</a>(3) also pnm.gz, pnm.bz2, png, jpg, jpeg, tiff, gif, bmp, ps (only single pages) and eps are supported as input files (not as input stream), where pnm can be replaced by one of ppm, pgm and pbm.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h</code></dt>
<dd> show usage information</dd>
<dt><code>-i</code> <i>file</i></dt>
<dd> read input from <i>file</i> (or <code>stdin</code> if <i>file</i> is a single dash)</dd>
<dt><code>-o</code> <i>file</i></dt>
<dd> send output to <i>file</i> instead of <code>stdout</code></dd>
<dt><code>-e</code> <i>file</i></dt>
<dd> send errors to <i>file</i> instead of <code>stderr</code> or to <code>stdout</code> if <i>file</i> is a dash</dd>
<dt><code>-x</code> <i>file</i></dt>
<dd> progress output to <i>file</i> (<i>file</i> can be a file name, a fifo name or a file descriptor 1&#8230;255), this is useful for GUI developpers to show the OCR progress, the file descriptor argument is only available, if compiled with __USE_POSIX defined</dd>
<dt><code>-p</code> <i>path</i></dt>
<dd> database path, a final slash must be included, default is ./db/, this path will be populated with images of learned characters</dd>
<dt><code>-f</code> <i>format</i></dt>
<dd> output <i>format</i> of the recognized text (ISO8859_1 TeX HTML XML UTF8 ASCII), XML will also output position and probability data</dd>
<dt><code>-l</code> <i>level</i></dt>
<dd> set grey level to <i>level</i> (0&lt;160&lt;=255, default: 0 for autodetect), darker pixels belong to characters, brighter pixels are interpreted as background of the input image</dd>
<dt><code>-d</code> <i>size</i></dt>
<dd> set dust size in pixels (clusters smaller than this are removed), 0 means no clusters are removed, the default is -1 for auto detection</dd>
<dt><code>-s</code> <i>num</i></dt>
<dd> set spacewidth between words in units of dots (default: 0 for autodetect), wider widths are interpreted as word spaces, smaller as character spaces</dd>
<dt><code>-v</code> <i>verbosity</i></dt>
<dd> be verbose to stderr; <i>verbosity</i> is a bitfield</dd>
<dt><code>-c </code><i>string</i></dt>
<dd> only verbose output of characters from <i>string</i> to stderr, more output is generated for all characters within the string, the underscore stands for unknown chars, this function is usefull to limit debug information to the necessary one</dd>
<dt><code>-C </code><i>string</i></dt>
<dd> only recognise characters from <i>string</i>, this is a filter function in cases where the interest is only to a part of the character alphabet, you can use 0-9 or a-z to specify ranges, use &#8212; to detect the minus sign</dd>
<dt><code>-a</code> <i>certainty</i></dt>
<dd> set value for certainty of recognition (0..100; default: 95), characters with a higher certainty are accepted, characters with a lower certainty are treated as unknown (not recognized); set higher values, if you want to have only more certain recognized characters</dd>
<dt><code>-u </code><i>string</i></dt>
<dd> output this string for every unrecognized character (default is &quot;_&quot;)</dd>
<dt><code>-m</code> <i>mode</i></dt>
<dd> set oprational mode; mode is a bitfield (default: 0)</dd>
<dt><code>-n</code> <i>bool</i></dt>
<dd> if <i>bool</i> is non-zero, only recognise numbers (this is now obsolete, use -C &quot;0123456789&quot;)</dd></dl>
<p> The verbosity is specified as a bitfield:</p>
<dl>
<dt><code>1</code></dt>
<dd> print more info</dd>
<dt><code>2</code></dt>
<dd> list shapes of boxes (see -c) to stderr</dd>
<dt><code>4</code></dt>
<dd> list pattern of boxes (see -c) to stderr</dd>
<dt><code>8</code></dt>
<dd> print pattern after recognition for debugging</dd>
<dt><code>16</code></dt>
<dd> print debug information about recognition of lines to stderr</dd>
<dt><code>32</code></dt>
<dd> create outXX.png with boxes and lines marked on each general OCR-step</dd></dl>
<p> The operation modes are:</p>
<dl>
<dt><code>2</code></dt>
<dd> use database to recognize characters which are not recognized by other algorithms, (early development)</dd>
<dt><code>4</code></dt>
<dd> switching on layout analysis or zoning (development)</dd>
<dt><code>8</code></dt>
<dd> don&#8217;t compare unrecognized characters to recognized one</dd>
<dt><code>16</code></dt>
<dd> don&#8217;t try to divide overlapping characters to two or three single characters</dd>
<dt><code>32</code></dt>
<dd> don&#8217;t do context correction</dd>
<dt><code>64</code></dt>
<dd> character packing, before recognition starts, similar characters are searched and only one of this characters will be send to the recognition engine (development)</dd>
<dt><code>130</code></dt>
<dd> extend database, prompts user for unidentified characters and extends the database with users answer (128+2, early development)</dd>
<dt><code>256</code></dt>
<dd> switch off the recognition engine (makes sense together with -m 2)</dd></dl>
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
<dt><code>gocr -v 33 text1.pbm</code></dt>
<dd> output verbose information, out30.png is created to see details of recognition process</dd>
<dt><code>gocr -v 7 -c _YV text1.pbm</code></dt>
<dd> verbose output for unknown chars and chars Y and V</dd>
<dt><code>djpeg -pnm -gray text.jpg | gocr &#8211;</code></dt>
<dd> convert a jpeg file to pnm format and input via pipe </dd>
</dl>
