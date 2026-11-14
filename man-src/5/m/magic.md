---
title: "magic(5)"
name: "magic"
section: "5"
letter: "m"
url: "/docs/linux/man/5-magic/"
description: "magic – file command’s magic pattern file"
---

<p><code>magic</code> &#8211; file command&#8217;s magic pattern file</p>
<h2>Description</h2>
<p>This manual page documents the format of magic files as used by the <a href="/docs/linux/man/1-file/">file</a>(1) command, version 5.41. The <a href="/docs/linux/man/1-file/">file</a>(1) command identifies the type of a file using, among other tests, a test for whether the file contains certain &#8220;magic patterns&#8221; The database of these &#8220;magic patterns&#8221; is usually located in a binary file in /usr/share/misc/magic.mgc or a directory of source text magic pattern fragment files in /usr/share/misc/magic The database specifies what patterns are to be tested for, what message or MIME type to print if a particular pattern is found, and additional information to extract from the file. </p>
<p> The format of the source fragment files that are used to build this database is as follows: Each line of a fragment file specifies a test to be performed. A test compares the data starting at a particular offset in the file with a byte value, a string or a numeric value. If the test succeeds, a message is printed. The line consists of the following fields:</p>
<dl>
<dt><code>offset</code></p>
<dd>A number specifying the offset (in bytes) into the file of the data which is to be tested. This offset can be a negative number if it is: </p>
<ul>
<li> The first direct offset of the magic entry (at continuation level 0), in which case it is interpreted an offset from end end of the file going backwards. This works only when a file descriptor to the file is available and it is a regular file.
<li> A continuation offset relative to the end of the last up-level field <code>( &amp; )</code> </ul>
<dt><code>type</code></p>
<dd>The type of the data to be tested. The possible values are:</p>
<dl>
<dt><code>byte</code></p>
<dd>A one-byte value.</p>
<dt><code>short</code></p>
<dd>A two-byte value in this machine&#8217;s native byte order.</p>
<dt><code>long</code></p>
<dd>A four-byte value in this machine&#8217;s native byte order.</p>
<dt><code>quad</code></p>
<dd>An eight-byte value in this machine&#8217;s native byte order.</p>
<dt><code>float</code></p>
<dd>A 32-bit single precision IEEE floating point number in this machine&#8217;s native byte order.</p>
<dt><code>double</code></p>
<dd>A 64-bit double precision IEEE floating point number in this machine&#8217;s native byte order.</p>
<dt><code>string</code></p>
<dd>A string of bytes. The string type specification can be optionally followed by /[WwcCtbTf]*. The &#8220;W&#8221; flag compacts whitespace in the target, which must contain at least one whitespace character. If the magic has <code>n</code> consecutive blanks, the target needs at least <code>n</code> consecutive blanks to match. The &#8220;w&#8221; flag treats every blank in the magic as an optional blank. The &#8220;f&#8221; flags requires that the matched string is a full word, not a partial word match. The &#8220;c&#8221; flag specifies case insensitive matching: lower case characters in the magic match both lower and upper case characters in the target, whereas upper case characters in the magic only match upper case characters in the target. The &#8220;C&#8221; flag specifies case insensitive matching: upper case characters in the magic match both lower and upper case characters in the target, whereas lower case characters in the magic only match upper case characters in the target. To do a complete case insensitive match, specify both &#8220;c&#8221; and &#8220;C&#8221; The &#8220;t&#8221; flag forces the test to be done for text files, while the &#8220;b&#8221; flag forces the test to be done for binary files. The &#8220;T&#8221; flag causes the string to be trimmed, i.e. leading and trailing whitespace is deleted before the string is printed.</p>
<dt><code>pstring</code></p>
<dd>A Pascal-style string where the first byte/short/int is interpreted as the unsigned length. The length defaults to byte and can be specified as a modifier. The following modifiers are supported:</p>
<dl>
<dt><code>B</code></p>
<dd>A byte length (default).</p>
<dt><code>H</code></p>
<dd>A 2 byte big endian length.</p>
<dt><code>h</code></p>
<dd>A 2 byte little endian length.</p>
<dt><code>L</code></p>
<dd>A 4 byte big endian length.</p>
<dt><code>l</code></p>
<dd>A 4 byte little endian length.</p>
<dt><code>J</code></p>
<dd>The length includes itself in its count.</dl>
<p> The string is not NUL terminated. &#8220;J&#8221; is used rather than the more valuable &#8220;I&#8221; because this type of length is a feature of the JPEG format.</p>
<dt><code>date</code></p>
<dd>A four-byte value interpreted as a UNIX date.</p>
<dt><code>qdate</code></p>
<dd>An eight-byte value interpreted as a UNIX date.</p>
<dt><code>ldate</code></p>
<dd>A four-byte value interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>qldate</code></p>
<dd>An eight-byte value interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>qwdate</code></p>
<dd>An eight-byte value interpreted as a Windows-style date.</p>
<dt><code>beid3</code></p>
<dd>A 32-bit ID3 length in big-endian byte order.</p>
<dt><code>beshort</code></p>
<dd>A two-byte value in big-endian byte order.</p>
<dt><code>belong</code></p>
<dd>A four-byte value in big-endian byte order.</p>
<dt><code>bequad</code></p>
<dd>An eight-byte value in big-endian byte order.</p>
<dt><code>befloat</code></p>
<dd>A 32-bit single precision IEEE floating point number in big-endian byte order.</p>
<dt><code>bedouble</code></p>
<dd>A 64-bit double precision IEEE floating point number in big-endian byte order.</p>
<dt><code>bedate</code></p>
<dd>A four-byte value in big-endian byte order, interpreted as a Unix date.</p>
<dt><code>beqdate</code></p>
<dd>An eight-byte value in big-endian byte order, interpreted as a Unix date.</p>
<dt><code>beldate</code></p>
<dd>A four-byte value in big-endian byte order, interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>beqldate</code></p>
<dd>An eight-byte value in big-endian byte order, interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>beqwdate</code></p>
<dd>An eight-byte value in big-endian byte order, interpreted as a Windows-style date.</p>
<dt><code>bestring16</code></p>
<dd>A two-byte unicode (UCS16) string in big-endian byte order.</p>
<dt><code>leid3</code></p>
<dd>A 32-bit ID3 length in little-endian byte order.</p>
<dt><code>leshort</code></p>
<dd>A two-byte value in little-endian byte order.</p>
<dt><code>lelong</code></p>
<dd>A four-byte value in little-endian byte order.</p>
<dt><code>lequad</code></p>
<dd>An eight-byte value in little-endian byte order.</p>
<dt><code>lefloat</code></p>
<dd>A 32-bit single precision IEEE floating point number in little-endian byte order.</p>
<dt><code>ledouble</code></p>
<dd>A 64-bit double precision IEEE floating point number in little-endian byte order.</p>
<dt><code>ledate</code></p>
<dd>A four-byte value in little-endian byte order, interpreted as a UNIX date.</p>
<dt><code>leqdate</code></p>
<dd>An eight-byte value in little-endian byte order, interpreted as a UNIX date.</p>
<dt><code>leldate</code></p>
<dd>A four-byte value in little-endian byte order, interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>leqldate</code></p>
<dd>An eight-byte value in little-endian byte order, interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>leqwdate</code></p>
<dd>An eight-byte value in little-endian byte order, interpreted as a Windows-style date.</p>
<dt><code>lestring16</code></p>
<dd>A two-byte unicode (UCS16) string in little-endian byte order.</p>
<dt><code>melong</code></p>
<dd>A four-byte value in middle-endian (PDP-11) byte order.</p>
<dt><code>medate</code></p>
<dd>A four-byte value in middle-endian (PDP-11) byte order, interpreted as a UNIX date.</p>
<dt><code>meldate</code></p>
<dd>A four-byte value in middle-endian (PDP-11) byte order, interpreted as a UNIX-style date, but interpreted as local time rather than UTC.</p>
<dt><code>indirect</code></p>
<dd>Starting at the given offset, consult the magic database again. The offset of the <code>indirect</code> magic is by default absolute in the file, but one can specify <code>/r</code> to indicate that the offset is relative from the beginning of the entry.</p>
<dt><code>name</code></p>
<dd>Define a &#8220;named&#8221; magic instance that can be called from another <code>use</code> magic entry, like a subroutine call. Named instance direct magic offsets are relative to the offset of the previous matched entry, but indirect offsets are relative to the beginning of the file as usual. Named magic entries always match.</p>
<dt><code>use</code></p>
<dd>Recursively call the named magic starting from the current offset. If the name of the referenced begins with a <code>^</code> then the endianness of the magic is switched; if the magic mentioned <code>leshort</code> for example, it is treated as <code>beshort</code> and vice versa. This is useful to avoid duplicating the rules for different endianness.</p>
<dt><code>regex</code></p>
<dd>A regular expression match in extended POSIX regular expression syntax (like egrep). Regular expressions can take exponential time to process, and their performance is hard to predict, so their use is discouraged. When used in production environments, their performance should be carefully checked. The size of the string to search should also be limited by specifying <code>/&lt;length&gt;</code> to avoid performance issues scanning long files. The type specification can also be optionally followed by <code>/[c][s][l]</code> The &#8220;c&#8221; flag makes the match case insensitive, while the &#8220;s&#8221; flag update the offset to the start offset of the match, rather than the end. The &#8220;l&#8221; modifier, changes the limit of length to mean number of lines instead of a byte count. Lines are delimited by the platforms native line delimiter. When a line count is specified, an implicit byte count also computed assuming each line is 80 characters long. If neither a byte or line count is specified, the search is limited automatically to 8KiB. <code>^</code> and <code>$</code> match the beginning and end of individual lines, respectively, not beginning and end of file.</p>
<dt><code>search</code></p>
<dd>A literal string search starting at the given offset. The same modifier flags can be used as for string patterns. The search expression must contain the range in the form <code>/number,</code> that is the number of positions at which the match will be attempted, starting from the start offset. This is suitable for searching larger binary expressions with variable offsets, using <code>\</code> escapes for special characters. The order of modifier and number is not relevant.</p>
<dt><code>default</code></p>
<dd>This is intended to be used with the test <i>x</i> (which is always true) and it has no type. It matches when no other test at that continuation level has matched before. Clearing that matched tests for a continuation level, can be done using the <code>clear</code> test.</p>
<dt><code>clear</code></p>
<dd>This test is always true and clears the match flag for that continuation level. It is intended to be used with the <code>default</code> test.</p>
<dt><code>der</code></p>
<dd>Parse the file as a DER Certificate file. The test field is used as a der type that needs to be matched. The DER types are: <code>eoc</code> <code>bool</code> <code>int</code> <code>bit_str</code> <code>octet_str</code> <code>null</code> <code>obj_id</code> <code>obj_desc</code> <code>ext</code> <code>real</code> <code>enum</code> <code>embed</code> <code>utf8_str</code> <code>rel_oid</code> <code>time</code> <code>res2</code> <code>seq</code> <code>set</code> <code>num_str</code> <code>prt_str</code> <code>t61_str</code> <code>vid_str</code> <code>ia5_str</code> <code>utc_time</code> <code>gen_time</code> <code>gr_str</code> <code>vis_str</code> <code>gen_str</code> <code>univ_str</code> <code>char_str</code> <code>bmp_str</code> <code>date</code> <code>tod</code> <code>datetime</code> <code>duration</code> <code>oid-iri</code> <code>rel-oid-iri</code> These types can be followed by an optional numeric size, which indicates the field width in bytes.</p>
<dt><code>guid</code></p>
<dd>A Globally Unique Identifier, parsed and printed as XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX. It&#8217;s format is a string.</p>
<dt><code>offset</code></p>
<dd>This is a quad value indicating the current offset of the file. It can be used to determine the size of the file or the magic buffer. For example the magic entries: </p>
<blockquote>
<pre>-0 offset x this file is %lld bytes
-0 offset &lt;=100 must be more than 100 \
 bytes and is only %lld</pre>
</blockquote>
</dl>
<p> For compatibility with the Single UNIX Standard, the type specifiers <code>dC</code> and <code>d1</code> are equivalent to <code>byte</code> the type specifiers <code>uC</code> and <code>u1</code> are equivalent to <code>ubyte</code> the type specifiers <code>dS</code> and <code>d2</code> are equivalent to <code>short</code> the type specifiers <code>uS</code> and <code>u2</code> are equivalent to <code>ushort</code> the type specifiers <code>dI</code> <code>dL</code> and <code>d4</code> are equivalent to <code>long</code> the type specifiers <code>uI</code> <code>uL</code> and <code>u4</code> are equivalent to <code>ulong</code> the type specifier <code>d8</code> is equivalent to <code>quad</code> the type specifier <code>u8</code> is equivalent to <code>uquad</code> and the type specifier <code>s</code> is equivalent to <code>string</code> In addition, the type specifier <code>dQ</code> is equivalent to <code>quad</code> and the type specifier <code>uQ</code> is equivalent to <code>uquad</code> </p>
<p> Each top-level magic pattern (see below for an explanation of levels) is classified as text or binary according to the types used. Types &#8220;regex&#8221; and &#8220;search&#8221; are classified as text tests, unless non-printable characters are used in the pattern. All other tests are classified as binary. A top-level pattern is considered to be a test text when all its patterns are text patterns; otherwise, it is considered to be a binary pattern. When matching a file, binary patterns are tried first; if no match is found, and the file looks like text, then its encoding is determined and the text patterns are tried. </p>
<p> The numeric types may optionally be followed by <code>&amp;</code> and a numeric value, to specify that the value is to be AND&#8217;ed with the numeric value before any comparisons are done. Prepending a <code>u</code> to the type indicates that ordered comparisons should be unsigned.</p>
<dt><code>test</code></p>
<dd>The value to be compared with the value from the file. If the type is numeric, this value is specified in C form; if it is a string, it is specified as a C string with the usual escapes permitted (e.g. 
 for new-line). </p>
<p> Numeric values may be preceded by a character indicating the operation to be performed. It may be <code>=</code> to specify that the value from the file must equal the specified value, <code>&lt;</code> to specify that the value from the file must be less than the specified value, <code>&gt;</code> to specify that the value from the file must be greater than the specified value, <code>&amp;</code> to specify that the value from the file must have set all of the bits that are set in the specified value, <code>^</code> to specify that the value from the file must have clear any of the bits that are set in the specified value, or <code>~</code> the value specified after is negated before tested. <code>x</code> to specify that any value will match. If the character is omitted, it is assumed to be <code>=</code> Operators <code>&amp;</code> <code>^</code> and <code>~</code> don&#8217;t work with floats and doubles. The operator <code>!</code> specifies that the line matches if the test does <i>not</i> succeed. </p>
<p> Numeric values are specified in C form; e.g. <code>13</code> is decimal, <code>013</code> is octal, and <code>0x13</code> is hexadecimal. </p>
<p> Numeric operations are not performed on date types, instead the numeric value is interpreted as an offset. </p>
<p> For string values, the string from the file must match the specified string. The operators <code>=</code> <code>&lt;</code> and <code>&gt;</code> (but not <code>&amp;</code> can be applied to strings. The length used for matching is that of the string argument in the magic file. This means that a line can match any non-empty string (usually used to then print the string), with <i>&gt;
