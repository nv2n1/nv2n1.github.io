---
title: "barcode(1)"
name: "barcode"
section: "1"
letter: "b"
url: "/docs/linux/man/1-barcode/"
description: "barcode – a stand alone program to run the barcode library"
---

<h2 class="name">NAME</h2>
<p> barcode &#8211; a stand alone program to run the barcode library </p>
<h2>SYNOPSIS</h2>
<p> <code>barcode</code> [-b &#8211; | string] [-e encoding] [-o &#8211; | outfile] [ <i>other-flags</i> ]</p>
<h2>DESCRIPTION</h2>
<p> The information below is extracted from the texinfo file, which is the preferred source of information. </p>
<p> The <code>barcode</code> program is a front-end to access some features of the library from the command line. It is able to read user supplied strings from the command line or a data file (standard input by default) and encode all of them. </p>
<h2>OPTIONS</h2>
<p> <code>barcode</code> accepts the following options:</p>
<dl>
<dt>&#8211;help or -h</p>
<dd> Print a usage summary and exit.</p>
<dt>-i filename</p>
<dd> Identify a file where strings to be encoded are read from. If missing (and if -b is not used) it defaults to standard input. Each data line of the input file will be used to create one barcode output.</p>
<dt>-o filename</p>
<dd> Output file. It defaults to standard output.</p>
<dt>-b string</p>
<dd> Specify a single &#8220;barcode&#8221; string to be encoded. The option can be used multiple times in order to encode multiple strings (this will result in multi-page postscript output or a table of barcodes if -t is specified). The strings must match the encoding chosen; if it doesn&#8217;t match the program will print a warning to stderr and generate &#8220;blank&#8221; output (although not zero-length). Please note that a string including spaces or other special characters must be properly quoted.</p>
<dt>-e encoding</p>
<dd> <code>encoding</code> is the name of the chosen encoding format being used. It defaults to the value of the environment variable BARCODE_ENCODING or to auto detection if the environment is also unset.</p>
<dt>-g geometry</p>
<dd> The geometry argument is of the form &#8220;[&lt;width&gt; x &lt;height&gt;] [+ &lt;xmargin&gt; + &lt;ymargin&gt;]&#8221; (with no intervening spaces). Unspecified margin values will result in no margin; unspecified size results in default size. The specified values represent print points by default, and can be inches, millimeters or other units according to the -u option or the BARCODE_UNIT environment variable. The argument is used to place the printout code on the page. Note that an additional white margin of 10 points is added to the printout. If the option is unspecified, BARCODE_GEOMETRY is looked up in the environment, if missing a default size and no margin (but the default 10 points) are used.</p>
<dt>-t table-geometry</p>
<dd> Used to print several barcodes to a single page, this option is meant to be used to print stickers. The argument is of the form &#8220;&lt;columns&gt; x &lt;lines&gt; [+ &lt;leftmargin&gt; + &lt;bottommargin&gt; [- &lt;rightmargin&gt; [- &lt;topmargin&gt;]]]&#8221; (with no intervening spaces); if missing, the top and right margin will default to be the same as the bottom and left margin. The margins are specified in print points or in the chosen unit (see -u below). If the option is not specified, BARCODE_TABLE is looked up in the environment, otherwise no table is printed and each barcode will get its own page. The size (but not the position) of a barcode item within a table can also be selected using -g (see &quot;geometry&quot; above), without struggling with external and internal margins. I still think management of geometries in a table is suboptimal, but I can&#8217;t make it better without introducing incompatibilities.</p>
<dt>-m margin(s)</p>
<dd> Specifies an internal margin for each sticker in the table. The argument is of the form &#8220;&lt;xmargin&gt;,&lt;ymargin&gt;&#8221; and the margin is applied symmetrically to the sticker. If unspecified, the environment variable BARCODE_MARGIN is used or a default internal margin of 10 points is used.</p>
<dt>-n</p>
<dd> &#8220;Numeric&#8221; output: don&#8217;t print the ASCII form of the code, only the bars.</p>
<dt>-c</p>
<dd> No checksum character (for encodings that allow it, like code 39, other codes, like UPC or EAN, ignore this option).</p>
<dt>-E</p>
<dd> Encapsulated postscript (default is normal postscript). When the output is generated as EPS only one barcode is encoded.</p>
<dt>-P</p>
<dd> PCL output. Please note that the Y direction goes from top to bottom for PCL, and the origin for an image is the top-left corner instead of the bottom-left</p>
<dt>-p pagesize</p>
<dd> Specify a non-default page size. The page size can be specified in millimeters, inches or plain numbers (for example: &quot;210x297mm&quot;, &quot;8.5x11in&quot;, &quot;595&#215;842&quot;). A page specification as numbers will be interpreted according to the current unit specification (see -u below). If libpaper is available, you can also specify the page size with its name, like &quot;A3&quot; or &quot;letter&quot; (libpaper is a standard component of Debian GNU/Linux, but may be missing elsewhere). The default page size is your system-wide default if libpaper is there, A4 otherwise.</p>
<dt>-u unit</p>
<dd> Choose the unit used in size specifications. Accepted values are &#8220;mm&#8221;, &#8220;cm&#8221;, &#8220;in&#8221; and &#8220;pt&#8221;. By default, the program will check BARCODE_UNIT in the environment, and assume points otherwise (this behaviour is compatible with 0.92 and previous versions. If -u appears more than once, each instance will modified the behaviour for the arguments at its right, as the command line is processes left to right. The program internally works with points, and any size is approximated to the nearest multiple of one point. The -u option affect -g (geometry), -t (table) and -p (page size). </p>
</dl>
<h2>ENCODING TYPES</h2>
<p> The program encodes text strings passed either on the command line (with -b) or retrieved from standard input. The text representation is interpreted according to the following rules. When auto-detection of the encoding is enabled (i.e, no explicit encoding type is specified), the encoding types are scanned to find one that can digest the text string. The following list of supported types is sorted in the same order the library uses when auto-detecting a suitable encoding for a string.</p>
<dl>
<dt>EAN</p>
<dd> The EAN frontend is similar to UPC; it accepts strings of digits, 12 or 7 characters long. Strings of 13 or 8 characters are accepted if the provided checksum digit is correct. I expect most users to feed input without a checksum, though. The add-2 and add-5 extension are accepted for both the EAN-13 and the EAN-8 encodings. The following are example of valid input strings: &#8220;123456789012&#8221; (EAN-13), &#8220;1234567890128&#8221; (EAN-13 wih checksum), &#8220;1234567&#8221; (EAN-8), &#8220;12345670 12345&#8221; (EAN-8 with checksum and add-5), &#8220;123456789012 12&#8221; (EAN-13 with add-2), &#8220;123456789012 12345&#8221; (EAN-13 with add-5).</p>
<dt>UPC</p>
<dd> The UPC frontend accepts only strings made up of digits (and, if a supplemental encoding is used, a blank to separate it). It accepts strings of 11 or 12 digits (UPC-A) and 6 or 7 or 8 digits (UPC-E). </p>
</dl>
<p> The 12th digit of UPC-A is the checksum and is added by the library if not specified in the input; if it is specified, it must be the right checksum or the code is rejected as invalid. For UPC-E, 6 digit are considered to be the middle part of the code, a leading 0 is assumed and the checksum is added; 7 digits are either considered the initial part (leading digit 0 or 1, checksum missing) or the final part (checksum specified, leading 0 assumed); 8 digits are considered to be the complete code, with leading 0 or 1 and checksum. For both UPC-A and UPC-E, a trailing string of 2 digits or 5 digits is accepted as well. Therefore, the following are examples of valid strings that can be encoded as UPC: &#8220;01234567890&#8221; (UPC-A) &#8220;012345678905&#8221; (UPC-A with checksum), &#8220;012345&#8221; (UPC-E), &#8220;01234567890 12&#8221; (UPC-A, add-2) and &#8220;01234567890 12345&#8221; (UPC-A, add-5), &#8220;0123456 12&#8221; (UPC-E, add-2). Please note that when setting BARCODE_ANY to auto-detect the encoding to be used, 12-digit strings and 7-digit strings will always be identified as EAN. This because I expect most user to provide input without a checksum. If you need to specify UPC-with-checksum as input you must explicitly set BARCODE_UPC as a flag or use -e upc on the command line.</p>
<dl>
<dt>ISBN</p>
<dd> ISBN numbers are encoded as EAN-13 symbols, with an optional add-5 trailer. The ISBN frontend of the library accepts real ISBN numbers and deals with any hyphen and, if present, the ISBN checksum character before encoding data. Valid representations for ISBN strings are for example: &#8220;1-56592-292-1&#8221;, &#8220;3-89721-122-X&#8221; and &#8220;3-89721-122-X 06900}&#8221;.</p>
<dt>code 128-B</p>
<dd> This encoding can represent all of the printing ASCII characters, from the space (32) to DEL (127). The checksum digit is mandatory in this encoding.</p>
<dt>code 128-C</p>
<dd> The &#8220;C&#8221; variation of Code-128 uses Code-128 symbols to represent two digits at a time (Code-128 is made up of 104 symbols whose interpretation is controlled by the start symbol being used). Code 128-C is thus the most compact way to represent any even number of digits. The encoder refuses to deal with an odd number of digits because the caller is expected to provide proper padding to an even number of digits. (Since Code-128 includes control symbols to switch charset, it is theoretically possible to represent the odd digit as a Code 128-A or 128-B symbol, but this tool doesn&#8217;t currently implement this option).</p>
<dt>code 128 raw</p>
<dd> Code-128 output represented symbol-by-symbol in the input string. To override part of the problems outlined below in specifying code128 symbols, this pseudo-encoding allows the used to specify a list of code128 symbols separated by spaces. Each symbol is represented by a number in the range 0-105. The list should include the leading character.The checksum and the stop character are automatically added by the library. Most likely this pseudo-encoding will be used with BARCODE_NO_ASCII and some external program to supply the printed text.</p>
<dt>code 39</p>
<dd> The code-39 standard can encode uppercase letters, digits, the blank space, plus, minus, dot, star, dollar, slash, percent. Any string that is only composed of such characters is accepted by the code-39 encoder. To avoid loosing information, the encoder refuses to encode mixed-case strings (a lowercase string is nonetheless accepted as a shortcut, but is encoded as uppercase).</p>
<dt>interleaved 2 of 5</p>
<dd> This encoding can only represent an even number of digits (odd digits are represented by bars, and even digits by the interleaving spaces). The name stresses the fact that two of the five items (bars or spaces) allocated to each symbol are wide, while the rest are narrow. The checksum digit is optional (can be disabled via BARCODE_NO_CHECKSUM). Since the number of digits, including the checksum, must be even, a leading zero is inserted in the string being encoded if needed (this is specifically stated in the specs I have access to).</p>
<dt>code 128</p>
<dd> Automatic selection between alphabet A, B and C of the Code-128 standard. This encoding can represent all ASCII symbols, from 0 (NUL) to 127 (DEL), as well as four special symbols, named F1, F2, F3, F4. The set of symbols available in this encoding is not easily represented as input to the barcode library, so the following convention is used. In the input string, which is a C-language null-terminated string, the NUL char is represented by the value 128 (0x80, 0200) and the F1-F4 characters are represented by the values 193-196 (0xc1-0xc4, 0301-0304). The values have been chosen to ease their representation as escape sequences. </p>
</dl>
<p> Since the shell doesn&#8217;t seem to interpret escape sequences on the command line, the &quot;-b&quot; option cannot be easily used to designate the strings to be encoded. As a workaround you can resort to the command echo, either within back-ticks or used separately to create a file that is then fed to the standard-input of barcode &#8212; assuming your echo command processes escape sequences. The newline character is especially though to encode (but not impossible unless you use a csh variant. </p>
<p> These problems only apply to the command-line tool; the use of library functions doesn&#8217;t give any problem. In needed, you can use the &#8220;code 128 raw&#8221; pseudo-encoding to represent code128 symbols by their numerical value. This encoding is used late in the auto-selection mechanism because (almost) any input string can be represented using code128.</p>
<dl>
<dt>Codabar</p>
<dd> Codabar can encode the ten digits and a few special symbols (minus, plus, dollar, colon, bar, dot). The characters &#8220;A&#8221;, &#8220;B&#8221;, &#8220;C&#8221; and &#8220;D&#8221; are used to represent four different start/stop characters. The input string to the barcode library can include the start and stop characters or not include them (in which case &#8220;A&#8221; is used as start and &#8220;B&#8221; as stop). Start and stop characters in the input string can be either all lowercase or all uppercase and are always printed as uppercase.</p>
<dt>Plessey</p>
<dd> Plessey barcodes can encode all the hexadecimal digits. Alphabetic digits in the input string must either be all lowercase or all uppercase. The output text is always uppercase.</p>
<dt>MSI</p>
<dd> MSI can only encode the decimal digits. While the standard specifies either one or two check digits, the current implementation in this library only generates one check digit.</p>
<dt>code 93</p>
<dd> The code-93 standard can natively encode 48 different characters, including uppercase letters, digits, the blank space, plus, minus, dot, star, dollar, slash, percent, as well as five special characters: a start/stop delimiter and four &quot;shift characters&quot; used for extended encoding. Using this &quot;extended encoding&quot; method, any standard 7-bit ASCII character can be encoded, but it takes up two symbol lengths in barcode if the character is not natively supported (one of the 48). The encoder here fully implements the code 93 encoding standard. Any characters natively supported (A-Z, 0-9, &quot;.+-/$ encoded as such &#8211; for any other characters (such as lower case letters, brackets, parentheses, etc.), the encoder will revert to extended encoding. As a note, the option to exclude the checksum will eliminate the two modulo-47 checksums (called C and K) from the barcode, but this probably will make it unreadable by 9 These checksums are specified to be used at the firmware level, and their absence will be interpreted as an invalid barcode. </p>
</dl>
<h2>PCL OUTPUT</h2>
<p> While the default output is Postscript (possibly EPS), and Postscript can be post-processed to almost anything, it is sometimes desirable to create output directly usable by the specific printer at hand. PCL is currently supported as an output format for this reason. Please note that the Y coordinate for PCL goes from top to bottom, while for Postscript it goes from bottom to top. Consistently, while in Postscript you specify the bottom-left corner as origin, for PCL you specify the top-left corner. </p>
<p> Barcode output for PCL Printers (HP LaserJet and compatibles), was developed using PCL5 Reference manuals from HP. that really refers to these printers:</p>
<dl>
<dt>
<dd> LaserJet III, III P, III D, III Si,</p>
<dt>
<dd> LaserJet 4 family</p>
<dt>
<dd> LaserJet 5 family</p>
<dt>
<dd> LaserJet 6 family</p>
<dt>
<dd> Color LaserJet</p>
<dt>
<dd> DeskJet 1200 and 1600. </p>
</dl>
<p> However, barcode printing uses a very small subset of PCL, probably also LaserJet II should print it without problem, but the resulting text may be horrible. </p>
<p> The only real difference from one printer to another really depends on which font are available in the printer, used in printing the label associated to the bars (if requested). </p>
<p> Earlier LaserJet supports only bitmaps fonts, so these are not &quot;scalable&quot;. (Ljet II ?), Also these fonts, when available, have a specified direction, and not all of them are available in both Portrait and Landscape mode. </p>
<p> From LaserJet 4 series, (except 4L/5L that are entry-level printers), Arial scalable font should be available, so it&#8217;s the &quot;default font&quot; used by this program. </p>
<p> LaserJet III series printers (and 4L, 5L), don&#8217;t feature &quot;Arial&quot; as a resident font, so you should use BARCODE_OUT_PCL_III instead of BARCODE_OUT_PCL., and font the font used will be &quot;Univers&quot; instead of &quot;Arial&quot;. </p>
<p> Results on compatible printers, may depend on consistency of PCL5 compatibility, in doubt, try BARCODE_OUT_PCL_III </p>
<p> PJL commands are not used here, as it&#8217;s not very compatible. </p>
<p> Tested Printers:</p>
<dl>
<dt>
<dd> Hp LaserJet 4050</p>
<dt>
<dd> Hp LaserJet 2100</p>
<dt>
<dd> Epson N-1200 emul PCL</p>
<dt>
<dd> Toshiba DP2570 (copier) + PCL option</p>
<dt>
<dd> Epson EPL-7100 emul. HP LaserJet II: bars print fine but text is bad. </p>
</dl>
<h2>BUGS</h2>
<p> The current management of borders/margins is far from optimal. The &#8220;default&#8221; margin applied by the library interferes with the external representation, but I feel it is mandatory to avoid creating barcode output with no surrounding white space (the problem is especially relevant for EPS output). </p>
<p> EAN-128 is not (yet) supported. I plan to implement it pretty soon and then bless the package as version 1.0. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-barcode/">barcode</a>(3)</code></p>
<h2>AUTHORS</h2>
<p> Alessandro Rubini &lt;rubini [at] gnu.org&gt; (maintainer) </p>
<p> Leonid A. Broukhis &lt;leob [at] mailcom.com&gt; (several encodings) </p>
<p> Andrea Scopece &lt;a.scopece [at] tin.it&gt; (PCL output) </p>
<h2>Index</h2>
