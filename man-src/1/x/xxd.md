---
title: "xxd(1)"
name: "xxd"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xxd/"
description: "xxd – make a hexdump or do the reverse."
---

<h2 class="name">NAME</h2>
<p> <i>xxd</i> &#8211; make a hexdump or do the reverse. </p>
<h2>SYNOPSIS</h2>
<p> <code>xxd</code> -h[elp]<br />
 <code>xxd</code> [options] [infile [outfile]]<br />
 <code>xxd</code> -r[evert] [options] [infile [outfile]]</p>
<h2>DESCRIPTION</h2>
<p> <i>xxd</i> creates a hex dump of a given file or standard input. It can also convert a hex dump back to its original binary form. Like <code><a href="/docs/linux/man/1-uuencode/">uuencode</a></code>(1) and <code><a href="/docs/linux/man/1-uudecode/">uudecode</a></code>(1) it allows the transmission of binary data in a `mail-safe&#8217; ASCII representation, but has the advantage of decoding to standard output. Moreover, it can be used to perform binary file patching.</p>
<h2>OPTIONS</h2>
<p> If no <i>infile</i> is given, standard input is read. If <i>infile</i> is specified as a `<code>&#8211;</code>&#8216; character, then input is taken from standard input. If no <i>outfile</i> is given (or a `<code>&#8211;</code>&#8216; character is in its place), results are sent to standard output. </p>
<p> Note that a &quot;lazy&quot; parser is used which does not check for more than the first option letter, unless the option is followed by a parameter. Spaces between a single option letter and its parameter are optional. Parameters to options can be specified in decimal, hexadecimal or octal notation. Thus <code>-c8</code>, <code>-c 8</code>, <code>-c 010</code> and <code>-cols 8</code> are all equivalent. </p>
<dl>
<dt><i>-a</i> | <i>-autoskip</i></p>
<dd> Toggle autoskip: A single &#8216;*&#8217; replaces nul-lines. Default off.</p>
<dt><i>-b</i> | <i>-bits</i></p>
<dd> Switch to bits (binary digits) dump, rather than hexdump. This option writes octets as eight digits &quot;1&quot;s and &quot;0&quot;s instead of a normal hexadecimal dump. Each line is preceded by a line number in hexadecimal and followed by an ascii (or ebcdic) representation. The command line switches -r, -p, -i do not work with this mode.</p>
<dt><i>-c cols </i>|<i> -cols cols</i></p>
<dd> Format &lt;<i>cols</i>&gt; octets per line. Default 16 (-i: 12, -ps: 30, -b: 6). Max 256.</p>
<dt><i>-C</i> | <i>-capitalize</i></p>
<dd> Capitalize variable names in C include file style, when using -i.</p>
<dt><i>-E</i> | <i>-EBCDIC</i></p>
<dd> Change the character encoding in the righthand column from ASCII to EBCDIC. This does not change the hexadecimal representation. The option is meaningless in combinations with -r, -p or -i.</p>
<dt><i>-e</i></p>
<dd> Switch to little-endian hexdump. This option treats byte groups as words in little-endian byte order. The default grouping of 4 bytes may be changed using <i>-g</i>. This option only applies to hexdump, leaving the ASCII (or EBCDIC) representation unchanged. The command line switches -r, -p, -i do not work with this mode.</p>
<dt><i>-g bytes </i>|<i> -groupsize bytes</i></p>
<dd> Separate the output of every &lt;<i>bytes</i>&gt; bytes (two hex characters or eight bit-digits each) by a whitespace. Specify <i>-g 0</i> to suppress grouping. &lt;<i>Bytes</i>&gt; defaults to <i>2</i> in normal mode, <i>4</i> in little-endian mode and <i>1</i> in bits mode. Grouping does not apply to postscript or include style.</p>
<dt><i>-h</i> | <i>-help</i></p>
<dd> Print a summary of available commands and exit. No hex dumping is performed.</p>
<dt><i>-i</i> | <i>-include</i></p>
<dd> Output in C include file style. A complete static array definition is written (named after the input file), unless xxd reads from stdin.</p>
<dt><i>-l len </i>|<i> -len len</i></p>
<dd> Stop after writing &lt;<i>len</i>&gt; octets.</p>
<dt><i>-o offset</i></p>
<dd> Add &lt;<i>offset</i>&gt; to the displayed file position.</p>
<dt><i>-p</i> | <i>-ps</i> | <i>-postscript</i> | <i>-plain</i></p>
<dd> Output in postscript continuous hexdump style. Also known as plain hexdump style.</p>
<dt><i>-r</i> | <i>-revert</i></p>
<dd> Reverse operation: convert (or patch) hexdump into binary. If not writing to stdout, xxd writes into its output file without truncating it. Use the combination <i>-r -p</i> to read plain hexadecimal dumps without line number information and without a particular column layout. Additional Whitespace and line-breaks are allowed anywhere.</p>
<dt><i>-seek offset</i></p>
<dd> When used after <i>-r</i>: revert with &lt;<i>offset</i>&gt; added to file positions found in hexdump.</p>
<dt><i>-s [+][-]seek</i></p>
<dd> Start at &lt;<i>seek</i>&gt; bytes abs. (or rel.) infile offset. <i>+ </i>indicates that the seek is relative to the current stdin file position (meaningless when not reading from stdin). <i>&#8211; </i>indicates that the seek should be that many characters from the end of the input (or if combined with <i>+</i>: before the current stdin file position). Without -s option, xxd starts at the current file position.</p>
<dt><i>-u</i></p>
<dd> Use upper case hex letters. Default is lower case.</p>
<dt><i>-v</i> | <i>-version</i></p>
<dd> Show version string.</dl>
<h2>CAVEATS</h2>
<p> <i>xxd -r</i> has some builtin magic while evaluating line number information. If the output file is seekable, then the linenumbers at the start of each hexdump line may be out of order, lines may be missing, or overlapping. In these cases xxd will <a href="/docs/linux/man/2-lseek/">lseek</a>(2) to the next position. If the output file is not seekable, only gaps are allowed, which will be filled by null-bytes. </p>
<p> <i>xxd -r</i> never generates parse errors. Garbage is silently skipped. </p>
<p> When editing hexdumps, please note that <i>xxd -r</i> skips everything on the input line after reading enough columns of hexadecimal data (see option -c). This also means, that changes to the printable ascii (or ebcdic) columns are always ignored. Reverting a plain (or postscript) style hexdump with xxd -r -p does not depend on the correct number of columns. Here anything that looks like a pair of hex-digits is interpreted. </p>
<p> Note the difference between<br />
 <i>% xxd -i file</i><br />
 and<br />
 <i>% xxd -i &lt; file</i> </p>
<p> <i>xxd -s +seek</i> may be different from <i>xxd -s seek</i>, as <a href="/docs/linux/man/2-lseek/">lseek</a>(2) is used to &quot;rewind&quot; input. A &#8216;+&#8217; makes a difference if the input source is stdin, and if stdin&#8217;s file position is not at the start of the file by the time xxd is started and given its input. The following examples may help to clarify (or further confuse!)&#8230; </p>
<p> Rewind stdin before reading; needed because the `cat&#8217; has already read to the end of stdin.<br />
 <i>% sh -c &quot;cat &gt; plain_copy; xxd -s 0 &gt; hex_copy&quot; &lt; file</i> </p>
<p> Hexdump from file position 0x480 (=1024+128) onwards. The `+&#8217; sign means &quot;relative to the current position&quot;, thus the `128&#8242; adds to the 1k where dd left off.<br />
 <i>% sh -c &quot;dd of=plain_snippet bs=1k count=1; xxd -s +128 &gt; hex_snippet&quot; &lt; file</i> </p>
<p> Hexdump from file position 0x100 ( = 1024-768) on.<br />
 <i>% sh -c &quot;dd of=plain_snippet bs=1k count=1; xxd -s +-768 &gt; hex_snippet&quot; &lt; file</i> </p>
<p> However, this is a rare situation and the use of `+&#8217; is rarely needed. The author prefers to monitor the effect of xxd with <a href="/docs/linux/man/1-strace/">strace</a>(1) or <a href="/docs/linux/man/1-truss/">truss</a>(1), whenever -s is used.</p>
<h2>EXAMPLES</h2>
<p> Print everything but the first three lines (hex 0x30 bytes) of <code>file</code>.<br />
 <i>% xxd -s 0x30 file</i> </p>
<p> Print 3 lines (hex 0x30 bytes) from the end of <code>file</code>.<br />
 <i>% xxd -s -0x30 file</i> </p>
<p> Print 120 bytes as continuous hexdump with 20 octets per line.<br />
 <i>% xxd -l 120 -ps -c 20 xxd.1</i><br />
 2e54482058584420312022417567757374203139<br />
 39362220224d616e75616c207061676520666f72<br />
 20787864220a2e5c220a2e5c222032317374204d<br />
 617920313939360a2e5c22204d616e2070616765<br />
 20617574686f723a0a2e5c2220202020546f6e79<br />
 204e7567656e74203c746f6e79407363746e7567 </p>
<p> Hexdump the first 120 bytes of this man page with 12 octets per line.<br />
 <i>% xxd -l 120 -c 12 xxd.1</i><br />
 0000000: 2e54 4820 5858 4420 3120 2241 .TH XXD 1 &quot;A<br />
 000000c: 7567 7573 7420 3139 3936 2220 ugust 1996&quot;<br />
 0000018: 224d 616e 7561 6c20 7061 6765 &quot;Manual page<br />
 0000024: 2066 6f72 2078 7864 220a 2e5c for xxd&quot;..\<br />
 0000030: 220a 2e5c 2220 3231 7374 204d &quot;..\&quot; 21st M<br />
 000003c: 6179 2031 3939 360a 2e5c 2220 ay 1996..\&quot;<br />
 0000048: 4d61 6e20 7061 6765 2061 7574 Man page aut<br />
 0000054: 686f 723a 0a2e 5c22 2020 2020 hor:..\&quot;<br />
 0000060: 546f 6e79 204e 7567 656e 7420 Tony Nugent<br />
 000006c: 3c74 6f6e 7940 7363 746e 7567 &lt;tony [at] sctnug </p>
<p> Display just the date from the file xxd.1<br />
 <i>% xxd -s 0x36 -l 13 -c 13 xxd.1</i><br />
 0000036: 3231 7374 204d 6179 2031 3939 36 21st May 1996 </p>
<p> Copy <code>input_file</code> to <code>output_file</code> and prepend 100 bytes of value 0x00.<br />
 <i>% xxd input_file | xxd -r -s 100 &gt; output_file</i> </p>
<p> Patch the date in the file xxd.1<br />
 <i>% echo &quot;0000037: 3574 68&quot; | xxd -r &#8211; xxd.1</i><br />
 <i>% xxd -s 0x36 -l 13 -c 13 xxd.1</i><br />
 0000036: 3235 7468 204d 6179 2031 3939 36 25th May 1996 </p>
<p> Create a 65537 byte file with all bytes 0x00, except for the last one which is &#8216;A&#8217; (hex 0x41).<br />
 <i>% echo &quot;010000: 41&quot; | xxd -r &gt; file</i> </p>
<p> Hexdump this file with autoskip.<br />
 <i>% xxd -a -c 12 file</i><br />
 0000000: 0000 0000 0000 0000 0000 0000 &#8230;&#8230;&#8230;&#8230;<br />
 *<br />
 000fffc: 0000 0000 40 &#8230;.A </p>
<p> Create a 1 byte file containing a single &#8216;A&#8217; character. The number after &#8216;-r -s&#8217; adds to the linenumbers found in the file; in effect, the leading bytes are suppressed.<br />
 <i>% echo &quot;010000: 41&quot; | xxd -r -s -0x10000 &gt; file</i> </p>
<p> Use xxd as a filter within an editor such as <code><a href="/docs/linux/man/1-vim/">vim</a>(1)</code> to hexdump a region marked between `a&#8217; and `z&#8217;.<br />
 <i>:&#8217;a,&#8217;z!xxd</i> </p>
<p> Use xxd as a filter within an editor such as <code><a href="/docs/linux/man/1-vim/">vim</a>(1)</code> to recover a binary hexdump marked between `a&#8217; and `z&#8217;.<br />
 <i>:&#8217;a,&#8217;z!xxd -r</i> </p>
<p> Use xxd as a filter within an editor such as <code><a href="/docs/linux/man/1-vim/">vim</a>(1)</code> to recover one line of a hexdump. Move the cursor over the line and type:<br />
 <i>!!xxd -r</i> </p>
<p> Read single characters from a serial line<br />
 <i>% xxd -c1 &lt; /dev/term/b &amp;</i><br />
 <i>% stty &lt; /dev/term/b -echo -opost -isig -icanon min 1</i><br />
 <i>% echo -n foo &gt; /dev/term/b</i> </p>
<h2>RETURN VALUES</h2>
<p> The following error values are returned:</p>
<dl>
<dt>0</p>
<dd> no errors encountered.</p>
<dt>-1</p>
<dd> operation not supported ( <i>xxd -r -i</i> still impossible).</p>
<dt>1</p>
<dd> error while parsing options.</p>
<dt>2</p>
<dd> problems with input file.</p>
<dt>3</p>
<dd> problems with output file.</p>
<dt>4,5</p>
<dd> desired seek position is unreachable.</dl>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-uuencode/">uuencode</a>(1), <a href="/docs/linux/man/1-uudecode/">uudecode</a>(1), <a href="/docs/linux/man/1-patch/">patch</a>(1) </p>
<h2>WARNINGS</h2>
<p> The tools weirdness matches its creators brain. Use entirely at your own risk. Copy files. Trace it. Become a wizard. </p>
<h2>VERSION</h2>
<p> This manual page documents xxd version 1.7</p>
<h2>AUTHOR</h2>
<p> (c) 1990-1997 by Juergen Weigert<br />
 &lt;jnweiger [at] informatik.uni-erlangen.de&gt; </p>
<p> Distribute freely and credit me,<br />
 make money and share with me,<br />
 lose money and don&#8217;t ask me. </p>
<p> Manual page started by Tony Nugent<br />
 &lt;tony [at] sctnugen.ppp.gu.edu.au&gt; &lt;T.Nugent [at] sct.gu.edu.au&gt;<br />
 Small changes by Bram Moolenaar. Edited by Juergen Weigert. </p>
<h2>Index</h2>
