---

title: "unix2mac(1)"
name: "unix2mac"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unix2mac/"
description: "dos2unix – DOS/Mac to Unix and vice versa text file format converter"
---

<p> dos2unix &#8211; DOS/Mac to Unix and vice versa text file format converter </p>
<h2>SYNOPSIS</h2>
<pre><code>
dos2unix[options][FILE...][-n INFILE OUTFILE...] unix2dos[options][FILE...][-n INFILE OUTFILE...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> The Dos2unix package includes utilities <tt>&quot;dos2unix&quot;</tt> and <tt>&quot;unix2dos&quot;</tt> to convert plain text files in DOS or Mac format to Unix format and vice versa. </p>
<p> In DOS/Windows text files a line break, also known as newline, is a combination of two characters: a Carriage Return (CR) followed by a Line Feed (LF). In Unix text files a line break is a single character: the Line Feed (LF). In Mac text files, prior to Mac OS X, a line break was single Carriage Return (CR) character. Nowadays Mac OS uses Unix style (LF) line breaks. </p>
<p> Besides line breaks Dos2unix can also convert the encoding of files. A few DOS code pages can be converted to Unix Latin-1. And Windows Unicode (UTF-16) files can be converted to Unix Unicode (UTF-8) files. </p>
<p> Binary files are automatically skipped, unless conversion is forced. </p>
<p> Non-regular files, such as directories and FIFOs, are automatically skipped. </p>
<p> Symbolic links and their targets are by default kept untouched. Symbolic links can optionally be replaced, or the output can be written to the symbolic link target. Writing to a symbolic link target is not supported on Windows. </p>
<p> Dos2unix was modelled after dos2unix under SunOS/Solaris. There is one important difference with the original SunOS/Solaris version. This version does by default in-place conversion (old file mode), while the original SunOS/Solaris version only supports paired conversion (new file mode). See also options <tt>&quot;-o&quot;</tt> and <tt>&quot;-n&quot;</tt>. Another difference is that the SunOS/Solaris version uses by default <i>iso</i> mode conversion while this version uses by default <i>ascii</i> mode conversion.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8212;</code></dt>
<dd> Treat all following options as file names. Use this option if you want to convert files whose names start with a dash. For instance to convert a file named &#8220;-foo&#8221;, you can use this command: </dd>
<pre>
    dos2unix -- -foo
</pre>
<p> Or in new file mode: </p>
<pre>
    dos2unix -n -- -foo out.txt
</pre>
<dt><code>&#8211;allow-chown</code></dt>
<dd> Allow file ownership change in old file mode. </dd>
<p> When this option is used, the conversion will not be aborted when the user and/or group ownership of the original file can&#8217;t be preserved in old file mode. Conversion will continue and the converted file will get the same new ownership as if it was converted in new file mode. See also options <tt>&quot;-o&quot;</tt> and <tt>&quot;-n&quot;</tt>. This option is only available if dos2unix has support for preserving the user and group ownership of files.</p>
<dt><code>-ascii</code></dt>
<dd> Convert only line breaks. This is the default conversion mode.</dd>
<dt><code>-iso</code></dt>
<dd> Conversion between DOS and ISO-8859-1 character set. See also section CONVERSION MODES.</dd>
<dt><code>-1252</code></dt>
<dd> Use Windows code page 1252 (Western European).</dd>
<dt><code>-437</code></dt>
<dd> Use DOS code page 437 (US). This is the default code page used for ISO conversion.</dd>
<dt><code>-850</code></dt>
<dd> Use DOS code page 850 (Western European).</dd>
<dt><code>-860</code></dt>
<dd> Use DOS code page 860 (Portuguese).</dd>
<dt><code>-863</code></dt>
<dd> Use DOS code page 863 (French Canadian).</dd>
<dt><code>-865</code></dt>
<dd> Use DOS code page 865 (Nordic).</dd>
<dt><code>-7</code></dt>
<dd> Convert 8 bit characters to 7 bit space.</dd>
<dt><code>-b, &#8211;keep-bom</code></dt>
<dd> Keep Byte Order Mark (BOM). When the input file has a BOM, write a BOM in the output file. This is the default behavior when converting to DOS line breaks. See also option <tt>&quot;-r&quot;</tt>.</dd>
<dt><code>-c, &#8211;convmode </code><code>CONVMODE</code></dt>
<dd> Set conversion mode. Where CONVMODE is one of: <i>ascii</i>, <i>7bit</i>, <i>iso</i>, <i>mac</i> with ascii being the default.</dd>
<dt><code>-D, &#8211;display-enc </code><code>ENCODING</code></dt>
<dd> Set encoding of displayed text. Where ENCODING is one of: <i>ansi</i>, <i>unicode</i>, <i>unicodebom</i>, <i>utf8</i>, <i>utf8bom</i> with ansi being the default. </dd>
<p> This option is only available in dos2unix for Windows with Unicode file name support. This option has no effect on the actual file names read and written, only on how they are displayed. </p>
<p> There are several methods for displaying text in a Windows console based on the encoding of the text. They all have their own advantages and disadvantages.</p>
<dl>
<dl>
<dt><code>ansi</code></dt>
<dd> Dos2unix&#8217;s default method is to use ANSI encoded text. The advantage is that it is backwards compatible. It works with raster and TrueType fonts. In some regions you may need to change the active DOS OEM code page to the Windows system ANSI code page using the <tt>&quot;chcp&quot;</tt> command, because dos2unix uses the Windows system code page. </dd>
<p> The disadvantage of ansi is that international file names with characters not inside the system default code page are not displayed properly. You will see a question mark, or a wrong symbol instead. When you don&#8217;t work with foreign file names this method is OK.</p>
<dt><code>unicode, unicodebom</code></dt>
<dd> The advantage of unicode (the Windows name for UTF-16) encoding is that text is usually properly displayed. There is no need to change the active code page. You may need to set the console&#8217;s font to a TrueType font to have international characters displayed properly. When a character is not included in the TrueType font you usually see a small square, sometimes with a question mark in it. </dd>
<p> When you use the ConEmu console all text is displayed properly, because ConEmu automatically selects a good font. </p>
<p> The disadvantage of unicode is that it is not compatible with ASCII. The output is not easy to handle when you redirect it to another program. </p>
<p> When method <tt>&quot;unicodebom&quot;</tt> is used the Unicode text will be preceded with a BOM (Byte Order Mark). A BOM is required for correct redirection or piping in PowerShell.</p>
<dt><code>utf8, utf8bom</code></dt>
<dd> The advantage of utf8 is that it is compatible with ASCII. You need to set the console&#8217;s font to a TrueType font. With a TrueType font the text is displayed similar as with the <tt>&quot;unicode&quot;</tt> encoding. </dd>
<p> The disadvantage is that when you use the default raster font all non-ASCII characters are displayed wrong. Not only unicode file names, but also translated messages become unreadable. On Windows configured for an East-Asian region you may see a lot of flickering of the console when the messages are displayed. </p>
<p> In a ConEmu console the utf8 encoding method works well. </p>
<p> When method <tt>&quot;utf8bom&quot;</tt> is used the UTF-8 text will be preceded with a BOM (Byte Order Mark). A BOM is required for correct redirection or piping in PowerShell.</dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> The default encoding can be changed with environment variable DOS2UNIX_DISPLAY_ENC by setting it to <tt>&quot;unicode&quot;</tt>, <tt>&quot;unicodebom&quot;</tt>, <tt>&quot;utf8&quot;</tt>, or <tt>&quot;utf8bom&quot;</tt>.</dd></dl>
<dt><code>-f, &#8211;force</code></dt>
<dd> Force conversion of binary files.</dd>
<dt><code>-gb, &#8211;gb18030</code></dt>
<dd> On Windows UTF-16 files are by default converted to UTF-8, regardless of the locale setting. Use this option to convert UTF-16 files to GB18030. This option is only available on Windows. See also section GB18030.</dd>
<dt><code>-h, &#8211;help</code></dt>
<dd> Display help and exit.</dd>
<dt><code>-i[</code><code>FLAGS</code><code>], &#8211;info[=FLAGS] </code><code>FILE &#8230;</code></dt>
<dd> Display file information. No conversion is done. </dd>
<p> The following information is printed, in this order: number of DOS line breaks, number of Unix line breaks, number of Mac line breaks, byte order mark, text or binary, file name. </p>
<p> Example output: </p>
<pre>
     6       0       0  no_bom    text    dos.txt
     0       6       0  no_bom    text    unix.txt
     0       0       6  no_bom    text    mac.txt
     6       6       6  no_bom    text    mixed.txt
    50       0       0  UTF-16LE  text    utf16le.txt
     0      50       0  no_bom    text    utf8unix.txt
    50       0       0  UTF-8     text    utf8dos.txt
     2     418     219  no_bom    binary  dos2unix.exe
</pre>
<p> Note that sometimes a binary file can be mistaken for a text file. See also option <tt>&quot;-s&quot;</tt>. </p>
<p> Optionally extra flags can be set to change the output. One or more flags can be added.</p>
<dl>
<dl>
<dt><code>0</code></dt>
<dd> Print the file information lines followed by a null character instead of a newline character. This enables correct interpretation of file names with spaces or quotes when flag c is used. Use this flag in combination with <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) option <tt>&quot;-0&quot;</tt> or <tt>&quot;--null&quot;</tt>.</dd>
<dt><code>d</code></dt>
<dd> Print number of DOS line breaks.</dd>
<dt><code>u</code></dt>
<dd> Print number of Unix line breaks.</dd>
<dt><code>m</code></dt>
<dd> Print number of Mac line breaks.</dd>
<dt><code>b</code></dt>
<dd> Print the byte order mark.</dd>
<dt><code>t</code></dt>
<dd> Print if file is text or binary.</dd>
<dt><code>c</code></dt>
<dd> Print only the files that would be converted. </dd>
<p> With the <tt>&quot;c&quot;</tt> flag dos2unix will print only the files that contain DOS line breaks, unix2dos will print only file names that have Unix line breaks.</p>
<dt><code>h</code></dt>
<dd> Print a header.</dd>
<dt><code>p</code></dt>
<dd> Show file names without path.</dd></dl>
</dl>
<dl>
<dt>
</dt><dd>
<p> Examples: </p>
<p> Show information for all *.txt files: </p>
<pre>
    dos2unix -i *.txt
</pre>
<p> Show only the number of DOS line breaks and Unix line breaks: </p>
<pre>
    dos2unix -idu *.txt
</pre>
<p> Show only the byte order mark: </p>
<pre>
    dos2unix --info=b *.txt
</pre>
<p> List the files that have DOS line breaks: </p>
<pre>
    dos2unix -ic *.txt
</pre>
<p> List the files that have Unix line breaks: </p>
<pre>
    unix2dos -ic *.txt
</pre>
<p> Convert only files that have DOS line breaks and leave the other files untouched: </p>
<pre>
    dos2unix -ic0 *.txt | xargs -0 dos2unix
</pre>
<p> Find text files that have DOS line breaks: </p>
<pre>
    find -name '*.txt' -print0 | xargs -0 dos2unix -ic
</pre>
</dd></dl>
<dt><code>-k, &#8211;keepdate</code></dt>
<dd> Keep the date stamp of output file same as input file.</dd>
<dt><code>-L, &#8211;license</code></dt>
<dd> Display program&#8217;s license.</dd>
<dt><code>-l, &#8211;newline</code></dt>
<dd> Add additional newline. </dd>
<p> <code>dos2unix</code>: Only DOS line breaks are changed to two Unix line breaks. In Mac mode only Mac line breaks are changed to two Unix line breaks. </p>
<p> <code>unix2dos</code>: Only Unix line breaks are changed to two DOS line breaks. In Mac mode Unix line breaks are changed to two Mac line breaks.</p>
<dt><code>-m, &#8211;add-bom</code></dt>
<dd> Write a Byte Order Mark (BOM) in the output file. By default an UTF-8 BOM is written. </dd>
<p> When the input file is UTF-16, and the option <tt>&quot;-u&quot;</tt> is used, an UTF-16 BOM will be written. </p>
<p> Never use this option when the output encoding is other than UTF-8, UTF-16, or GB18030. See also section UNICODE.</p>
<dt><code>-n, &#8211;newfile </code><code>INFILE OUTFILE &#8230;</code></dt>
<dd> New file mode. Convert file INFILE and write output to file OUTFILE. File names must be given in pairs and wildcard names should <i>not</i> be used or you <i>will</i> lose your files. </dd>
<p> The person who starts the conversion in new file (paired) mode will be the owner of the converted file. The read/write permissions of the new file will be the permissions of the original file minus the <code><a href="/docs/linux/man/1-umask/">umask</a></code>(1) of the person who runs the conversion.</p>
<dt><code>&#8211;no-allow-chown</code></dt>
<dd> Don&#8217;t allow file ownership change in old file mode (default). </dd>
<p> Abort conversion when the user and/or group ownership of the original file can&#8217;t be preserved in old file mode. See also options <tt>&quot;-o&quot;</tt> and <tt>&quot;-n&quot;</tt>. This option is only available if dos2unix has support for preserving the user and group ownership of files.</p>
<dt><code>-o, &#8211;oldfile </code><code>FILE &#8230;</code></dt>
<dd> Old file mode. Convert file FILE and overwrite output to it. The program defaults to run in this mode. Wildcard names may be used. </dd>
<p> In old file (in-place) mode the converted file gets the same owner, group, and read/write permissions as the original file. Also when the file is converted by another user who has write permissions on the file (e.g. user root). The conversion will be aborted when it is not possible to preserve the original values. Change of owner could mean that the original owner is not able to read the file any more. Change of group could be a security risk, the file could be made readable for persons for whom it is not intended. Preservation of owner, group, and read/write permissions is only supported on Unix. </p>
<p> To check if dos2unix has support for preserving the user and group ownership of files type <tt>&quot;dos2unix -V&quot;</tt>. </p>
<p> Conversion is always done via a temporary file. When an error occurs halfway the conversion, the temporary file is deleted and the original file stays intact. When the conversion is successful, the original file is replaced with the temporary file. You may have write permission on the original file, but no permission to put the same user and/or group ownership properties on the temporary file as the original file has. This means you are not able to preserve the user and/or group ownership of the original file. In this case you can use option <tt>&quot;--allow-chown&quot;</tt> to continue with the conversion: </p>
<pre>
    dos2unix --allow-chown foo.txt
</pre>
<p> Another option is to use new file mode: </p>
<pre>
    dos2unix -n foo.txt foo.txt
</pre>
<p> The advantage of the <tt>&quot;--allow-chown&quot;</tt> option is that you can use wildcards, and the ownership properties will be preserved when possible.</p>
<dt><code>-q, &#8211;quiet</code></dt>
<dd> Quiet mode. Suppress all warnings and messages. The return value is zero. Except when wrong command-line options are used.</dd>
<dt><code>-r, &#8211;remove-bom</code></dt>
<dd> Remove Byte Order Mark (BOM). Do not write a BOM in the output file. This is the default behavior when converting to Unix line breaks. See also option <tt>&quot;-b&quot;</tt>.</dd>
<dt><code>-s, &#8211;safe</code></dt>
<dd> Skip binary files (default). </dd>
<p> The skipping of binary files is done to avoid accidental mistakes. Be aware that the detection of binary files is not 100% foolproof. Input files are scanned for binary symbols which are typically not found in text files. It is possible that a binary file contains only normal text characters. Such a binary file will mistakenly be seen as a text file.</p>
<dt><code>-u, &#8211;keep-utf16</code></dt>
<dd> Keep the original UTF-16 encoding of the input file. The output file will be written in the same UTF-16 encoding, little or big endian, as the input file. This prevents transformation to UTF-8. An UTF-16 BOM will be written accordingly. This option can be disabled with the <tt>&quot;-ascii&quot;</tt> option.</dd>
<dt><code>-ul, &#8211;assume-utf16le</code></dt>
<dd> Assume that the input file format is UTF-16LE. </dd>
<p> When there is a Byte Order Mark in the input file the BOM has priority over this option. </p>
<p> When you made a wrong assumption (the input file was not in UTF-16LE format) and the conversion succeeded, you will get an UTF-8 output file with wrong text. You can undo the wrong conversion with <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) by converting the UTF-8 output file back to UTF-16LE. This will bring back the original file. </p>
<p> The assumption of UTF-16LE works as a <i>conversion mode</i>. By switching to the default <i>ascii</i> mode the UTF-16LE assumption is turned off.</p>
<dt><code>-ub, &#8211;assume-utf16be</code></dt>
<dd> Assume that the input file format is UTF-16BE. </dd>
<p> This option works the same as option <tt>&quot;-ul&quot;</tt>.</p>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Display verbose messages. Extra information is displayed about Byte Order Marks and the amount of converted line breaks.</dd>
<dt><code>-F, &#8211;follow-symlink</code></dt>
<dd> Follow symbolic links and convert the targets.</dd>
<dt><code>-R, &#8211;replace-symlink</code></dt>
<dd> Replace symbolic links with converted files (original target files remain unchanged).</dd>
<dt><code>-S, &#8211;skip-symlink</code></dt>
<dd> Keep symbolic links and targets unchanged (default).</dd>
<dt><code>-V, &#8211;version</code></dt>
<dd> Display version information and exit.</dd></dl>
<h2>MAC MODE</h2>
<p> In normal mode line breaks are converted from DOS to Unix and vice versa. Mac line breaks are not converted. </p>
<p> In Mac mode line breaks are converted from Mac to Unix and vice versa. DOS line breaks are not changed. </p>
<p> To run in Mac mode use the command-line option <tt>&quot;-c mac&quot;</tt> or use the commands <tt>&quot;mac2unix&quot;</tt> or <tt>&quot;unix2mac&quot;</tt>.</p>
<h2>CONVERSION MODES</h2>
<dl>
<dt><code>ascii</code></dt>
<dd> In mode <tt>&quot;ascii&quot;</tt> only line breaks are converted. This is the default conversion mode. </dd>
<p> Although the name of this mode is ASCII, which is a 7 bit standard, the actual mode is 8 bit. Use always this mode when converting Unicode UTF-8 files.</p>
<dt><code>7bit</code></dt>
<dd> In this mode all 8 bit non-ASCII characters (with values from 128 to 255) are converted to a 7 bit space.</dd>
<dt><code>iso</code></dt>
<dd> Characters are converted between a DOS character set (code page) and ISO character set ISO-8859-1 (Latin-1) on Unix. DOS characters without ISO-8859-1 equivalent, for which conversion is not possible, are converted to a dot. The same counts for ISO-8859-1 characters without DOS counterpart. </dd>
<p> When only option <tt>&quot;-iso&quot;</tt> is used dos2unix will try to determine the active code page. When this is not possible dos2unix will use default code page CP437, which is mainly used in the USA. To force a specific code page use options <tt>&quot;-437&quot;</tt> (US), <tt>&quot;-850&quot;</tt> (Western European), <tt>&quot;-860&quot;</tt> (Portuguese), <tt>&quot;-863&quot;</tt> (French Canadian), or <tt>&quot;-865&quot;</tt> (Nordic). Windows code page CP1252 (Western European) is also supported with option <tt>&quot;-1252&quot;</tt>. For other code pages use dos2unix in combination with <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1). Iconv can convert between a long list of character encodings. </p>
<p> Never use ISO conversion on Unicode text files. It will corrupt UTF-8 encoded files. </p>
<p> Some examples: </p>
<p> Convert from DOS default code page to Unix Latin-1: </p>
<pre>
    dos2unix -iso -n in.txt out.txt
</pre>
<p> Convert from DOS CP850 to Unix Latin-1: </p>
<pre>
    dos2unix -850 -n in.txt out.txt
</pre>
<p> Convert from Windows CP1252 to Unix Latin-1: </p>
<pre>
    dos2unix -1252 -n in.txt out.txt
</pre>
<p> Convert from Windows CP1252 to Unix UTF-8 (Unicode): </p>
<pre>
    iconv -f CP1252 -t UTF-8 in.txt | dos2unix &gt; out.txt
</pre>
<p> Convert from Unix Latin-1 to DOS default code page: </p>
<pre>
    unix2dos -iso -n in.txt out.txt
</pre>
<p> Convert from Unix Latin-1 to DOS CP850: </p>
<pre>
    unix2dos -850 -n in.txt out.txt
</pre>
<p> Convert from Unix Latin-1 to Windows CP1252: </p>
<pre>
    unix2dos -1252 -n in.txt out.txt
</pre>
<p> Convert from Unix UTF-8 (Unicode) to Windows CP1252: </p>
<pre>
    unix2dos &lt; in.txt | iconv -f UTF-8 -t CP1252 &gt; out.txt
</pre>
<p> See also &lt;<a rel="nofollow" href="http://czyborra.com/charsets/codepages.html">http://czyborra.com/charsets/codepages.html</a>&gt; and &lt;<a rel="nofollow" href="http://czyborra.com/charsets/iso8859.html">http://czyborra.com/charsets/iso8859.html</a>&gt;.</dl>
<h2>UNICODE</h2>
<h3>Encodings</h3>
<p> There exist different Unicode encodings. On Unix and Linux Unicode files are typically encoded in UTF-8 encoding. On Windows Unicode text files can be encoded in UTF-8, UTF-16, or UTF-16 big endian, but are mostly encoded in UTF-16 format.</p>
<h3>Conversion</h3>
<p> Unicode text files can have DOS, Unix or Mac line breaks, like regular text files. </p>
<p> All versions of dos2unix and unix2dos can convert UTF-8 encoded files, because UTF-8 was designed for backward compatibility with ASCII. </p>
<p> Dos2unix and unix2dos with Unicode UTF-16 support, can read little and big endian UTF-16 encoded text files. To see if dos2unix was built with UTF-16 support type <tt>&quot;dos2unix -V&quot;</tt>. </p>
<p> On Unix/Linux UTF-16 encoded files are converted to the locale character encoding. Use the <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1) command to find out what the locale character encoding is. When conversion is not possible a conversion error will occur and the file will be skipped. </p>
<p> On Windows UTF-16 files are by default converted to UTF-8. UTF-8 formatted text files are well supported on both Windows and Unix/Linux. </p>
<p> UTF-16 and UTF-8 encoding are fully compatible, there will no text be lost in the conversion. When an UTF-16 to UTF-8 conversion error occurs, for instance when the UTF-16 input file contains an error, the file will be skipped. </p>
<p> When option <tt>&quot;-u&quot;</tt> is used, the output file will be written in the same UTF-16 encoding as the input file. Option <tt>&quot;-u&quot;</tt> prevents conversion to UTF-8. </p>
<p> Dos2unix and unix2dos have no option to convert UTF-8 files to UTF-16. </p>
<p> ISO and 7-bit mode conversion do not work on UTF-16 files.</p>
<h3>Byte Order Mark</h3>
<p> On Windows Unicode text files typically have a Byte Order Mark (BOM), because many Windows programs (including Notepad) add BOMs by default. See also &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Byte_order_mark">http://en.wikipedia.org/wiki/Byte_order_mark</a>&gt;. </p>
<p> On Unix Unicode files typically don&#8217;t have a BOM. It is assumed that text files are encoded in the locale character encoding. </p>
<p> Dos2unix can only detect if a file is in UTF-16 format if the file has a BOM. When an UTF-16 file doesn&#8217;t have a BOM, dos2unix will see the file as a binary file. </p>
<p> Use option <tt>&quot;-ul&quot;</tt> or <tt>&quot;-ub&quot;</tt> to convert an UTF-16 file without BOM. </p>
<p> Dos2unix writes by default no BOM in the output file. With option <tt>&quot;-b&quot;</tt> Dos2unix writes a BOM when the input file has a BOM. </p>
<p> Unix2dos writes by default a BOM in the output file when the input file has a BOM. Use option <tt>&quot;-r&quot;</tt> to remove the BOM. </p>
<p> Dos2unix and unix2dos write always a BOM when option <tt>&quot;-m&quot;</tt> is used.</p>
<h3>Unicode file names on Windows</h3>
<p> Dos2unix has optional support for reading and writing Unicode file names in the Windows Command Prompt. That means that dos2unix can open files that have characters in the name that are not part of the default system ANSI code page. To see if dos2unix for Windows was built with Unicode file name support type <tt>&quot;dos2unix -V&quot;</tt>. </p>
<p> There are some issues with displaying Unicode file names in a Windows console. See option <tt>&quot;-D&quot;</tt>, <tt>&quot;--display-enc&quot;</tt>. The file names may be displayed wrongly in the console, but the files will be written with the correct name.</p>
<h3>Unicode examples</h3>
<p> Convert from Windows UTF-16 (with BOM) to Unix UTF-8: </p>
<pre>
    dos2unix -n in.txt out.txt
</pre>
<p> Convert from Windows UTF-16LE (without BOM) to Unix UTF-8: </p>
<pre>
    dos2unix -ul -n in.txt out.txt
</pre>
<p> Convert from Unix UTF-8 to Windows UTF-8 with BOM: </p>
<pre>
    unix2dos -m -n in.txt out.txt
</pre>
<p> Convert from Unix UTF-8 to Windows UTF-16: </p>
<pre>
    unix2dos &lt; in.txt | iconv -f UTF-8 -t UTF-16 &gt; out.txt
</pre>
<h2>GB18030</h2>
<p> GB18030 is a Chinese government standard. A mandatory subset of the GB18030 standard is officially required for all software products sold in China. See also &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/GB_18030">http://en.wikipedia.org/wiki/GB_18030</a>&gt;. </p>
<p> GB18030 is fully compatible with Unicode, and can be considered an unicode transformation format. Like UTF-8, GB18030 is compatible with ASCII. GB18030 is also compatible with Windows code page 936, also known as GBK. </p>
<p> On Unix/Linux UTF-16 files are converted to GB18030 when the locale encoding is set to GB18030. Note that this will only work if the locale is supported by the system. Use command <tt>&quot;locale -a&quot;</tt> to get the list of supported locales. </p>
<p> On Windows you need to use option <tt>&quot;-gb&quot;</tt> to convert UTF-16 files to GB18030. </p>
<p> GB18030 encoded files can have a Byte Order Mark, like Unicode files.</p>
<h2>EXAMPLES</h2>
<p> Read input from &#8216;stdin&#8217; and write output to &#8216;stdout&#8217;: </p>
<pre>
    dos2unix &lt; a.txt
    cat a.txt | dos2unix
</pre>
<p> Convert and replace a.txt. Convert and replace b.txt: </p>
<pre>
    dos2unix a.txt b.txt
    dos2unix -o a.txt b.txt
</pre>
<p> Convert and replace a.txt in ascii conversion mode: </p>
<pre>
    dos2unix a.txt
</pre>
<p> Convert and replace a.txt in ascii conversion mode, convert and replace b.txt in 7bit conversion mode: </p>
<pre>
    dos2unix a.txt -c 7bit b.txt
    dos2unix -c ascii a.txt -c 7bit b.txt
    dos2unix -ascii a.txt -7 b.txt
</pre>
<p> Convert a.txt from Mac to Unix format: </p>
<pre>
    dos2unix -c mac a.txt
    mac2unix a.txt
</pre>
<p> Convert a.txt from Unix to Mac format: </p>
<pre>
    unix2dos -c mac a.txt
    unix2mac a.txt
</pre>
<p> Convert and replace a.txt while keeping original date stamp: </p>
<pre>
    dos2unix -k a.txt
    dos2unix -k -o a.txt
</pre>
<p> Convert a.txt and write to e.txt: </p>
<pre>
    dos2unix -n a.txt e.txt
</pre>
<p> Convert a.txt and write to e.txt, keep date stamp of e.txt same as a.txt: </p>
<pre>
    dos2unix -k -n a.txt e.txt
</pre>
<p> Convert and replace a.txt, convert b.txt and write to e.txt: </p>
<pre>
    dos2unix a.txt -n b.txt e.txt
    dos2unix -o a.txt -n b.txt e.txt
</pre>
<p> Convert c.txt and write to e.txt, convert and replace a.txt, convert and replace b.txt, convert d.txt and write to f.txt: </p>
<pre>
    dos2unix -n c.txt e.txt -o a.txt b.txt -n d.txt f.txt
</pre>
<h2>RECURSIVE CONVERSION</h2>
<p> In a Unix shell the <code><a href="/docs/linux/man/1-find/">find</a></code>(1) and <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) commands can be used to run dos2unix recursively over all text files in a directory tree. For instance to convert all .txt files in the directory tree under the current directory type: </p>
<pre>
    find . -name '*.txt' -print0 |xargs -0 dos2unix
</pre>
<p> The <code><a href="/docs/linux/man/1-find/">find</a></code>(1) option <tt>&quot;-print0&quot;</tt> and corresponding <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) option <tt>&quot;-0&quot;</tt> are needed when there are files with spaces or quotes in the name. Otherwise these options can be omitted. Another option is to use <code><a href="/docs/linux/man/1-find/">find</a></code>(1) with the <tt>&quot;-exec&quot;</tt> option: </p>
<pre>
    find . -name '*.txt' -exec dos2unix {} \;
</pre>
<p> In a Windows Command Prompt the following command can be used: </p>
<pre>
    for /R %G in (*.txt) do dos2unix &quot;%G&quot;
</pre>
<p> PowerShell users can use the following command in Windows PowerShell: </p>
<pre>
    get-childitem -path . -filter '*.txt' -recurse | foreach-object {dos2unix $_.Fullname}
</pre>
<h2>LOCALIZATION</h2>
<dl>
<dt><code>LANG</code></dt>
<dd> The primary language is selected with the environment variable LANG. The LANG variable consists out of several parts. The first part is in small letters the language code. The second is optional and is the country code in capital letters, preceded with an underscore. There is also an optional third part: character encoding, preceded with a dot. A few examples for POSIX standard type shells: </dd>
<pre>
    export LANG=nl               Dutch
    export LANG=nl_NL            Dutch, The Netherlands
    export LANG=nl_BE            Dutch, Belgium
    export LANG=es_ES            Spanish, Spain
    export LANG=es_MX            Spanish, Mexico
    export LANG=en_US.iso88591   English, USA, Latin-1 encoding
    export LANG=en_GB.UTF-8      English, UK, UTF-8 encoding
</pre>
<p> For a complete list of language and country codes see the gettext manual: &lt;<a rel="nofollow" href="http://www.gnu.org/software/gettext/manual/html_node/Usual-Language-Codes.html">http://www.gnu.org/software/gettext/manual/html_node/Usual-Language-Codes.html</a>&gt; </p>
<p> On Unix systems you can use the command <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1) to get locale specific information.</p>
<dt><code>LANGUAGE</code></dt>
<dd> With the LANGUAGE environment variable you can specify a priority list of languages, separated by colons. Dos2unix gives preference to LANGUAGE over LANG. For instance, first Dutch and then German: <tt>&quot;LANGUAGE=nl:de&quot;</tt>. You have to first enable localization, by setting LANG (or LC_ALL) to a value other than &#8220;C&#8221;, before you can use a language priority list through the LANGUAGE variable. See also the gettext manual: &lt;<a rel="nofollow" href="http://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html">http://www.gnu.org/software/gettext/manual/html_node/The-LANGUAGE-variable.html</a>&gt; </dd>
<p> If you select a language which is not available you will get the standard English messages.</p>
<dt><code>DOS2UNIX_LOCALEDIR</code></dt>
<dd> With the environment variable DOS2UNIX_LOCALEDIR the LOCALEDIR set during compilation can be overruled. LOCALEDIR is used to find the language files. The GNU default value is <tt>&quot;/usr/local/share/locale&quot;</tt>. Option <code>&#8211;version</code> will display the LOCALEDIR that is used. </dd>
<p> Example (POSIX shell): </p>
<pre>
    export DOS2UNIX_LOCALEDIR=$HOME/share/locale
</pre>
</dl>
<h2>RETURN VALUE</h2>
<p> On success, zero is returned. When a system error occurs the last system error will be returned. For other errors 1 is returned. </p>
<p> The return value is always zero in quiet mode, except when wrong command-line options are used.</p>
<h2>STANDARDS</h2>
<p> &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Text_file">http://en.wikipedia.org/wiki/Text_file</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Carriage_return">http://en.wikipedia.org/wiki/Carriage_return</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Newline">http://en.wikipedia.org/wiki/Newline</a>&gt; </p>
<p> &lt;<a rel="nofollow" href="http://en.wikipedia.org/wiki/Unicode">http://en.wikipedia.org/wiki/Unicode</a>&gt;</p>
<h2>AUTHORS</h2>
<p> Benjamin Lin &#8211; &lt;blin [at] socs.uts.edu.au&gt;, Bernd Johannes Wuebben (mac2unix mode) &#8211; &lt;wuebben [at] kde.org&gt;, Christian Wurll (add extra newline) &#8211; &lt;wurll [at] ira.uka.de&gt;, Erwin Waterlander &#8211; &lt;waterlan [at] xs4all.nl&gt; (maintainer) </p>
<p> Project page: &lt;<a rel="nofollow" href="http://waterlan.home.xs4all.nl/dos2unix.html">http://waterlan.home.xs4all.nl/dos2unix.html</a>&gt; </p>
<p> SourceForge page: &lt;<a rel="nofollow" href="http://sourceforge.net/projects/dos2unix/">http://sourceforge.net/projects/dos2unix/</a>&gt;</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-file/">file</a></code>(1) <code><a href="/docs/linux/man/1-find/">find</a></code>(1) <code><a href="/docs/linux/man/1-iconv/">iconv</a></code>(1) <code><a href="/docs/linux/man/1-locale/">locale</a></code>(1) <code><a href="/docs/linux/man/1-xargs/">xargs</a></code>(1) </p>
