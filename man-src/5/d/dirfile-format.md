---

title: "dirfile-format(5)"
name: "dirfile-format"
section: "5"
letter: "d"
url: "/docs/linux/man/5-dirfile-format/"
description: "dirfile-format — the dirfile database format specification file"
---

<p> dirfile-format --- the dirfile database format specification file  </p>

<p> The <i>dirfile format</i> file fully specifies the raw and derived time streams and auxiliary information for a <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5) database. </p>
<p>The format file is a case sensitive text file called <code>format</code> located in the dirfile directory. The explicit text encoding of the file is not specified by these standards, but must be 7-bit ASCII compatible. Examples of acceptable character encodings include all the ISO~8859 character sets (<i>i.e.</i> Latin-1 through Latin-10, among others), as well as the UTF-8 encoding of Unicode and UCS. </p>
<h2>SYNTAX</h2>
<p> The format file is composed of field specification lines and directive lines, optionally separated by blank lines or lines containing only whitespace. Lines are separated by the line-feed character (0x0A). Unless escaped (see below), the hash mark (<code>#</code>) is the comment delimiter; the comment delimiter, and any text following it to the end of the line, is ignored. </p>
<h3>Tokens</h3>
<p> Both field specification lines and directive lines consist of several tokens separated by whitespace. Whitespace consists of one or more whitespace characters. These are: space (0x20), horizontal tab (0x09), vertical tab (0x0B), form-feed (0x0C), and carriage return (0x0D). The first token of a directive line is always a <i>reserved word</i>. The first token of a field specification line is never a reserved word. Any amount of whitespace may precede the first token on a line. </p>
<p>Since tokens are separated by whitespace, to include a whitespace character in a token, it must either escaped by preceding it by a backslash character (<code>\</code>), or be replaced by a <i>character escape sequence</i> (see below), or else the token must be enclosed in quotation marks (). The quotation marks themselves will be stripped from the token. The <i>null-token</i> (that is, the token consisting of zero characters) may be specified by a pair of quotation marks with nothing between them (). To include a literal quotation mark in a token, it must be escaped (<code>\ ).</code> Similarly, a hash mark may be included in a token by including it in a quoted token or else by escaping it (<code>\#</code>), otherwise the hash mark will be understood as the comment delimiter. </p>
<p>It is a syntax error to have a line which contains unmatched quotation marks, or in which the last character is the backslash character. </p>
<p>Several characters when escaped by a preceding backslash character are interpreted as special characters in tokens. The character escape sequences are: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code>\a</code></dt>
<dd> <p> an alert (bell) character (ASCII 0x07 / U+0007) </p>
 </dd>
<dt><code>\b</code></dt>
<dd> <p> a backspace character (ASCII 0x08 / U+0008) </p>
 </dd>
<dt><code>\e</code></dt>
<dd> <p> an escape character (ASCII 0x1B / U+001B) </p>
 </dd>
<dt><code>\f</code></dt>
<dd> <p> a form-feed character (ASCII 0x0C / U+000C) </p>
 </dd>
<dt><code>\n</code></dt>
<dd> <p> a line-feed character (ASCII 0x0A / U+000A) </p>
 </dd>
<dt><code>\r</code></dt>
<dd> <p> a carriage return character (ASCII 0x0D / U+000D) </p>
 </dd>
<dt><code>\t</code></dt>
<dd> <p> a horizontal tab character (ASCII 0x09 / U+0009) </p>
 </dd>
<dt><code>\v</code></dt>
<dd> <p> a vertical tab character (ASCII 0x0B / U+000B) </p>
 </dd>
<dt><code>\\</code></dt>
<dd> <p> a backslash character (ASCII 0x5C / U+005C) </p>
 </dd>
<dt><code>\</code><i>ooo</i></dt>
<dd> <p> the single byte given by the octal number <i>ooo</i>. </p>
 </dd>
<dt><code>\x</code><i>hh</i></dt>
<dd> <p> the single byte given by the hexadecimal number <i>hh</i>. </p>
 </dd>
<dt><code>\u</code><i>hhhhhhh</i></dt>
<dd> <p> the UTF-8 byte sequence encoding the Unicode code point given by the hexadecimal number <i>hhhhhhh</i>. </p>
 </dd></dl>
</dl>
<p>Any other character which is escaped is interpreted as the character itself. (<i>i.e.</i> <code>\c</code> is interpreted as <code>c</code>). </p>
<p>No token may contain the NULL character (ASCII 0x00 / U+0000). Furthermore, although support is present to create UTF-8 byte sequences, tokens are not required to be valid UTF-8 sequences. Any byte sequence not containing the NULL character forms a valid token. However, there may be further restrictions on allowed characters for a token in a particular situation, (for example, when used as a field name). </p>
<h2>DIRECTIVES</h2>
<p>There are eight <i>reserved words</i>, which cannot be used as field names in the dirfile. Instead, these specify directives. Any reserved word may omit its initial forward slash (<code>/</code>), without change in meaning. Future versions of the Standards may require the slash to distinguish a reserved word from a field name. Like the rest of the format file, directives are case sensitive. </p>
<p>A number of the directives have <i>fragment scope</i>. A directive with fragment scope only applies to the fragment in which it is present, plus any sub-fragments indicated by the <code>/INCLUDE</code> directive, but only if those sub-fragments don&#8217;t have their own corresponding directive. Directives which have fragment scope are: <code>/ENCODING</code>,~<code>/ENDIAN</code>,~<code>/FRAMEOFFSET</code>, and <code>/PROTECT</code>. Because of these scoping rules, different portions of the dirfile may have different encodings, endiannesses, frame offsets, or protection levels. </p>
<p>If a directive with fragment scope appears more than once in a fragment, only the last such directive will be honoured, with the exception that the effect of a directive will not be propagated to sub-fragments if the directive line appears after the sub-fragment is included. The scoping rules of the remaining directives are discussed below. </p>
<dl>
<dt><code>/ENCODING</code></dt>
<dd> <p> The ENCODING directive specifies the encoding scheme used to encode binary files in the dirfile. The encoding scheme may be one of the predefined names listed below, which are described in more detail in <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5), or any other site-specific encoding scheme. The predefined scheme names are: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><i>none</i></dt>
<dd> <p> The dirfile is unencoded. </p>
 </dd>
<dt><i>bzip2</i></dt>
<dd> <p> The dirfile is compressed using the bzip2 compression scheme. </p>
 </dd>
<dt><i>gzip</i></dt>
<dd> <p> The dirfile is compressed using the gzip compression scheme. </p>
 </dd>
<dt><i>lzma</i></dt>
<dd> <p> The dirfile is compressed using the LZMA compression scheme. </p>
 </dd>
<dt><i>slim</i></dt>
<dd> <p> The dirfile is compressed using the slim compression scheme. </p>
 </dd>
<dt><i>text</i></dt>
<dd> <p> The dirfile is text encoded. </p>
 </dd></dl>
<p>Implementations should fail gracefully when encountering an unknown encoding scheme. If no encoding scheme is specified, behaviour is implementation dependent. Syntax is: </p>
<dl>
<dd> <p> <code>/ENCODING~</code><i>&lt;scheme&gt;</i> </p>
 </dd></dl>
<p>The ENCODING directive has <i>fragment scope</i>. </dl>
 </p>
<dt><code>/ENDIAN</code></dt>
<dd> <p> The ENDIAN directive specifies the endianness of the raw data in the database. In previous versions of the Dirfile Standard, raw data was always assumed to be little-endian. This assumption has been removed. The assumed endianness of raw data in dirfiles which omit this directive is implementation dependent. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/ENDIAN</code> <i>( </i>big <i> | </i>little <i> )</i> </p>
 </dd></dl>
<p>The ENDIAN directive has <i>fragment scope</i>. </dl>
 </p>
<dt><code>/FRAMEOFFSET</code></dt>
<dd> <p> The FRAMEOFFSET directive specifies the frame number of the first frame for which data exists in binary files associated with <code>RAW</code> fields. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/FRAMEOFFSET~</code><i>&lt;integer&gt;</i> </p>
 </dd></dl>
<p>The FRAMEOFFSET directive has <i>fragment scope</i>. </dl>
 </p>
<dt><code>/INCLUDE</code></dt>
<dd> <p> The INCLUDE directive specifies another file (called a <i>format file fragment</i>) to parse for additional format specification for the dirfile. The inclusion is treated as if the lines of the fragment were pasted verbatim in place of the INCLUDE directive line. The exception to this is that RAW fields specified in the fragment are located in the directory containing the fragment and not in the directory containing the parent format file, and the binary file encoding may be different for each fragment. The fragment may be specified either with an absolute path, or else a relative path from the current file. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/INCLUDE~</code><i>&lt;file&gt;</i> </p>
 </dd></dl>
<p>The INCLUDE directive has no scope: it is processed immediately and has no long-term effect. </dl>
 </p>
<dt><code>/META</code></dt>
<dd> <p> The META directive specifies a metafield attached to a particular parent field. The field metadata may be of any allowed type except <code>RAW</code>. Metafields are retrieved in exactly the same way as regular field data, but the <i>field code</i> specified consists of the parent and metafield names joined with a forward slash: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;parent-field&gt;</i><code>/</code><i>&lt;meta-field&gt;</i> </p>
 </dd></dl>
<p>META fields may not be specified before their parent field has been. Syntax is: </p>
<dl>
<dd> <p> <code>/META</code> <i>&lt;parent-field&gt;</i> {field specification line} </p>
 </dd></dl>
<p>As an illustration of this concept, </p>
<dl>
<dd> <p> <code>/META </code> pfield meta <code>CONST FLOAT64</code> 3.291882 </p>
 </dd></dl>
<p>provides a scalar metadatum called <i>meta</i> with value 3.291882 attached to the field <i>pfield</i>. This particular metafield may be referred to by the <i>field code</i> &quot;pfield/meta&quot;. Note that different parent fields may have metafields with the same name, since all references to metafields must include the parent field name. Metafields may not themselves have further sub-metafields. </p>
<p>As an alternative to the META directive, a metafield may be specified by a standard field specification line, using </p>
<dl>
<dd> <p> <i>&lt;parent-field&gt;</i><code>/</code><i>&lt;meta-field&gt;</i> </p>
 </dd></dl>
<p>as the field name. That is, the above example metafield could have also been specified as: </p>
<dl>
<dd> <p> pfield/meta <code>CONST FLOAT64</code> 3.291882 </p>
 </dd></dl>
<p>The META directive has no scope: it is processed immediately and has no long-term effect. </dl>
 </p>
<dt><code>/PROTECT</code></dt>
<dd> <p> The PROTECT directive specifies the advisory protection level of the current fragment and of the <code>RAW</code> fields defined therein. The protection level indicates whether writing to the format file fragment, or the binary data on disk is permitted. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/PROTECT~</code><i>&lt;level&gt;</i> </p>
 </dd></dl>
<p>Four advisory protection levels are defined: </p>
<dl>
<dt><i>none</i></dt>
<dd> <p> No protection at all: data and metadata may be freely changed. This is the default, if no PROTECT directive is present. </p>
 </dd>
<dt><i>format</i></dt>
<dd> <p> The dirfile metadata is protected from change, but <code>RAW</code> data on disk may be modified. </p>
 </dd>
<dt><i>data</i></dt>
<dd> <p> The <code>RAW</code> data on disk is protected from change, but metadata may be modified. </p>
 </dd>
<dt><i>all</i></dt>
<dd> <p> Both metadata and data on disk are protected from change. </p>
 </dd></dl>
<p>The PROTECT directive has <i>fragment scope</i>. </dl>
 </p>
<dt><code>/REFERENCE</code></dt>
<dd> <p> The REFERENCE directive specifies the name of the field to use as the dirfile&#8217;s reference field (see <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5)). If no REFERENCE directive is specified, the first <code>RAW</code> field encountered is used as the reference field. The REFERENCE directive must specify a <code>RAW</code> field. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/REFERENCE~</code><i>&lt;field-code&gt;</i> </p>
 </dd></dl>
<p>The REFERENCE directive has <i>global scope</i>: if multiple REFERENCE directives appear in the dirfile metadata, only the last such will be honoured. </dl>
 </p>
<dt><code>/VERSION</code></dt>
<dd> <p> The VERSION directive specifies the particular version of the Dirfile Standards to which the dirfile format file conforms. This directive should occur before any version dependent syntax is encountered. As of Standards Version 6, no such syntax exists, and this directive is provided primarily to ease forward compatibility. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <code>/VERSION~</code><i>&lt;integer&gt;</i> </p>
 </dd></dl>
<p>The VERSION directive has <i>immediate scope</i>: its effect is immediate, and it applies only to metadata below it, including and propagating downwards to sub-fragments after the directive. Its effect will also propagate upwards back to the parent fragment, and affect subsequent metadata. </dl>
 </p>
<h2>FIELD SPECIFICATION LINES</h2>
<p>Any line which does not start with a <i>reserved word</i> is assumed to be a field specification line. A field specification line consists of at least two tokens. The first token is the <i>field name</i>. The second token is the <i>field type</i>. Subsequent tokens are field parameters. The meaning and number these parameters depends on the field type specified. </p>
<h3>Field Names</h3>
<p> The first token in a field specification line is the field name. The field name consists of one or more characters, excluding both ASCII control characters (the bytes 0x01 through 0x1F), and the characters </p>
<dl>
<dd> <p> <code>&amp; / ; &lt; &gt; | .</code> </p>
 </dd></dl>
<p>which are reserved (but see below for the use of <code>/</code> to specify metafields). The field name may not be <i>INDEX</i>, which is a special, implicit field which contains the integer frame index. Field names are case sensitive. </p>
<p>If the field name beginning a field specifiction line does contain a <code>/</code> character, the line is assumed to specify a metafield. See the <code>META</code> directive above for further details. </p>
<h3>Field Types</h3>
<p> There are ten field types. Of these, eight are of vector type (<code>BIT</code>, <code>LINCOM</code>, <code>LINTERP</code>, <code>MULTIPLY</code>, <code>PHASE</code>, <code>POLYNOM</code>, <code>RAW</code>, and <code>SBIT</code>) and two are of scalar type (<code>CONST</code> and <code>STRING</code>). The possible fields types are: </p>
<dl>
<dt><code>BIT</code></dt>
<dd> <p> The BIT vector field type extracts one or more bits out of an input vector field as an unsigned number. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>BIT</code> <i>&lt;input&gt; &lt;first-bit&gt; [&lt;bits&gt;]</i> </p>
 </dd></dl>
<p>which specifies <i>field-name</i> to be the value of bits <i>first-bit</i> through <i>first-bit</i>+<i>bits</i>-1 of the input vector field <i>input</i>, when <i>input</i> is converted from its native type to an (endianness corrected) unsigned 64-bit integer. If <i>bits</i> is omitted, it is assumed to be 1. Both <i>first-bit</i> and <i>bits</i> may be either literal numbers, or else the field code of a <code>CONST</code> field type containing their values. The <code>SBIT</code> field type is a signed version of this field type. </dl>
 </p>
<dt><code>CONST</code></dt>
<dd> <p> The CONST scalar field type is a constant fully specified in the format file metadata. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>CONST</code> <i>&lt;type&gt; &lt;value&gt;</i> </p>
 </dd></dl>
<p>where <i>type</i> may be any supported native data type (see the description of the <code>RAW</code> field type below), and <i>value</i> is the numerical value of the constant interpreted as indicated by <i>type</i>. </dl>
 </p>
<dt><code>LINCOM</code></dt>
<dd> <p> The LINCOM vector field type is the linear combination of one, two or three input vector fields. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>LINCOM</code> [<i>&lt;n&gt;</i>] <i>&lt;field1&gt; &lt;a1&gt; &lt;b1&gt;~</i>[<i>&lt;field2&gt; &lt;a2&gt; &lt;b2&gt;~</i>[<i>&lt;field3&gt; &lt;a3&gt;</i> <i>&lt;b3&gt;</i>]] </p>
 </dd></dl>
<p>where <i>n</i>, if present, indicates the number of input vector fields (1, 2, or 3). The derived field will be computed as: </p>
<dl>
<dd> <p> field-name[n] = (a1 * field1[n] + b1) + (a2 * field2[n2] + b2) + (a3 * field3[n3] + b3) </p>
 </dd></dl>
<p>with the <i>field2</i> and <i>field3</i> terms included only if specified and the indices <i>n2</i> and <i>n3</i> computed appropriately for the (potentially differing) sample rates of the input fields. The resultant field will have the same sample rate as <i>field1</i>. Each supplied co-efficient (<i>a1</i>,~<i>b1</i>,~<i>a2</i>, &amp;c.) may be either a literal number, or else the field code of a <code>CONST</code> field type containing its value. </p>
<p>If <i>n</i> is not specified, the number of fields is determined by looking at the supplied parameters. Since it is possible to create a field code which is identical to a literal number, the third token on the line is assumed to be <i>n</i> if it the entire token can be parsed as a literal number using the rules outlined in <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3). That is, if the field code specifying <i>field1</i> could be mistaken for a literal number, <i>n</i> must be specified to prevent ambiguity. </dl>
 </p>
<dt><code>LINTERP</code></dt>
<dd> <p> The LINTERP vector field type specifies a table look up based on another vector field. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>LINTERP</code> <i>&lt;input&gt; &lt;table&gt;</i> </p>
 </dd></dl>
<p>where <i>input</i> is the input vector field for the table lookup, and <i>table</i> is the path to the lookup table file for the field. If this path is relative, it is assumed to be relative to the directory containing the format file fragment defining this field. The lookup table file is an ASCII text file with two whitespace separated columns of <i>x</i> and <i>y</i> values. Values are linearly interpolated between the points specified in the lookup table. </dl>
 </p>
<dt><code>MULTIPLY</code></dt>
<dd> <p> The MULTIPLY vector field type is the product of two vector fields. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>MULTIPLY</code> <i>&lt;field1&gt; &lt;field2&gt;</i> </p>
 </dd></dl>
<p>The derived field will be computed as: </p>
<dl>
<dd> <p> field-name[n] = field1[n] * field2[n2] </p>
 </dd></dl>
<p>with the index <i>n2</i> computed appropriately for the (potentially differing) sample rates of the input fields. The resultant field will have the same sample rate as <i>field1</i>. </dl>
 </p>
<dt><code>PHASE</code></dt>
<dd> <p> The PHASE vector field type shifts an input vector field by the specified number of samples. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>PHASE</code> <i>&lt;input&gt; &lt;shift&gt;</i> </p>
 </dd></dl>
<p>which specifies <i>field-name</i> to be the input vector field, <i>input</i>, shifted by <i>shift</i> samples. A positive <i>shift</i> indicates a shift forward in time. Results of shifting past the beginning- or end-of-file is implementation dependent. The <i>shift</i> parameter may be either a literal number, or else the field code of a <code>CONST</code> field type containing its values. </dl>
 </p>
<dt><code>POLYNOM</code></dt>
<dd> <p> The POLYNOM vector field type specifies a polynomial function of a single input vector field. Synax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field_name&gt;</i> <code>POLYNOM</code> <i>&lt;input&gt; &lt;a0&gt; &lt;a1&gt;</i> [<i>&lt;a2&gt;</i>~[<i>&lt;a3&gt;</i>~[<i>&lt;a4&gt;</i>~[<i>&lt;a5&gt;</i>]]]] </p>
 </dd></dl>
<p>where <i>&lt;input&gt;</i> is the input field code, and the order of the computed polynomial is determined by how many co-efficients are present in the specification. The derived field is computed as: </p>
<dl>
<dd> <p> field-name[n] = a0 + a1 * input[n] + a2 * input[n]**2 + a3 * input[n]**3 + a4 * input[n]**4 + a5 * input[n]**5 </p>
 </dd></dl>
<p>where <i>**</i> is the exponentiation operator, and the higher order terms are computed only if the corresponding co-efficients a <i>i</i> are specified. The coefficients, if specified, may be either literal numbers, or else the field code of a <code>CONST</code> field type containing the value. </dl>
 </p>
<dt><code>RAW</code></dt>
<dd> <p> The RAW vector field type specifies raw time streams on disk. In this case, the field name should correspond to the name of the file containing the time stream. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>RAW</code> <i>&lt;type&gt; &lt;sample-rate&gt;</i> </p>
 </dd></dl>
<p>where <i>sample-rate</i> is the number of samples per dirfile frame for the time stream and <i>type</i> is a token specifying the native data format type: </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>UINT8</i></dt>
<dd> <p> unsigned 8-bit integer </p>
 </dd>
<dt><i>INT8</i></dt>
<dd> <p> signed (two&#8217;s complement) 8-bit integer </p>
 </dd>
<dt><i>UINT16</i></dt>
<dd> <p> unsigned 16-bit integer </p>
 </dd>
<dt><i>INT16</i></dt>
<dd> <p> signed (two&#8217;s complement) 16-bit integer </p>
 </dd>
<dt><i>UINT32</i></dt>
<dd> <p> unsigned 32-bit integer </p>
 </dd>
<dt><i>INT32</i></dt>
<dd> <p> signed (two&#8217;s complement) 32-bit integer </p>
 </dd>
<dt><i>UINT64</i></dt>
<dd> <p> unsigned 64-bit integer </p>
 </dd>
<dt><i>INT64</i></dt>
<dd> <p> signed (two&#8217;s complement) 64-bit integer </p>
 </dd>
<dt><i>FLOAT32</i>~or~<i>FLOAT</i></dt>
<dd> <p> IEEE-754 standard 32-bit single precision floating point number </p>
 </dd>
<dt><i>FLOAT64</i>~or~<i>DOUBLE</i></dt>
<dd> <p> IEEE-754 standard 64-bit double precision floating point number </p>
 </dd>
<dt><i>COMPLEX64</i></dt>
<dd> <p> a 64-bit complex number consisting of two IEEE-754 standard 32-bit single precision floating point numbers representing the real and imaginary parts of the complex number. </p>
 </dd>
<dt><i>COMPLEX128</i></dt>
<dd> <p> a 128-bit complex number consisting of two IEEE-754 standard 64-bit double precision floating point numbers representing the real and imaginary parts of the complex number. </p>
 </dd></dl>
</dl>
<p>For more information on the storage of complex valued data, see <a href="/docs/linux/man/5-dirfile/">dirfile</a>(5). </p>
<p>For backwards compatibility, implementations should also recognise the following single character type aliases in use prior to Standards Version 5: </p>
<dl>
<dd>  </dd>
<dl>
<dt><i>c</i></dt>
<dd> <p> UINT8 </p>
 </dd>
<dt><i>u</i></dt>
<dd> <p> UINT16 </p>
 </dd>
<dt><i>s</i></dt>
<dd> <p> INT16 </p>
 </dd>
<dt><i>U</i></dt>
<dd> <p> UINT32 </p>
 </dd>
<dt><i>i</i>,~<i>S</i></dt>
<dd> <p> INT32 </p>
 </dd>
<dt><i>f</i></dt>
<dd> <p> FLOAT32 </p>
 </dd>
<dt><i>d</i></dt>
<dd> <p> FLOAT64 </p>
 </dd></dl>
</dl>
<p>Types <i>INT8</i>,~<i>UINT64</i>,~<i>INT64</i>,~<i>COMPLEX64</i>, and <i>COMPLEX128</i> are not supported before Standards Version 5, so no single character type aliases exist for these types. </p>
<p>The <i>sample-rate</i> parameter may be either a literal number, or else the name of a <code>CONST</code> field type containing its values. </dl>
 </p>
<dt><code>SBIT</code></dt>
<dd> <p> The SBIT vector field type extracts one or more bits out of an input vector field as a signed number. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>SBIT</code> <i>&lt;input&gt; &lt;first-bit&gt; [&lt;bits&gt;]</i> </p>
 </dd></dl>
<p>which specifies <i>field-name</i> to be the value of bits <i>first-bit</i> through <i>first-bit</i>+<i>bits</i>-1 of the input vector field <i>input</i>, when <i>input</i> is converted from its native type to a (endianness corrected) signed 64-bit integer. If <i>bits</i> is omitted, it is assumed to be 1. Both <i>first-bit</i> and <i>bits</i> may be either literal numbers, or else the field code of a <code>CONST</code> field type containing their values. The <code>BIT</code> field type is an unsigned version of this field type. </dl>
 </p>
<dt><code>STRING</code></dt>
<dd> <p> The STRING scalar field type is a character string fully specified in the format file metadata. Syntax is: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dd> <p> <i>&lt;field-name&gt;</i> <code>STRING</code> <i>&lt;value&gt;</i> </p>
 </dd></dl>
<p>where <i>value</i> is the string value of the field. Note that <i>value</i> is a single token. To include whitespace in the string, enclose <i>value</i> in quotation marks (), or else escape the whitespace with the backslash character (<code>\</code>). </dl>
 </p>
<h3>Field Parameters</h3>
<p> All input vector field parameters should be <i>field codes</i> (see below). Additionally, some of the numerical field parameters may be either literal numbers or else the <i>field code</i> of a <code>CONST</code> field containing the value. Parameters for which this is possible are indicated above. Since it is possible to create a field code which is identical to a literal number, a parameter is assumed to be the field code of a <code>CONST</code> field only if the entire token cannot be parsed as a literal number using the rules outlined in <code><a href="/docs/linux/man/3-strtod/">strtod</a></code>(3). (So, for example, a <code>CONST</code> field whose field code consists solely of digits can never be used as a parameter in a field specification line.) </p>
<p>A literal complex number is specified as two real (floating point) numbers separated by a semicolon (<code>;</code>) with no intervening whitespace. So, for example, the tokens </p>
<dl>
<dd> <p> 1;0 0;1 4;0 0;5 9.313e2;74.1 </p>
 </dd></dl>
<p>represent, respectively, the real unit, the imaginary unit, the real number four, the imaginary number 5 <i>i</i>, and the complex number 931.3 + 74.1 <i>i</i>. Because the semicolon character cannot be used in field names, a complex valued literal can never be mistaken for a field code. This allows, among other things, the composition of complex valued fields from purely real input fields. For example, a complex valued field, <i>z</i>, may be created from a real valued field <i>re</i>, representing the real part of the complex number, and the real valued field <i>im</i>, representing the imaginary part of the complex number, with the following <code>LINCOM</code> specification: </p>
<dl>
<dd> <p> <i>z</i> <code>LINCOM</code> <i>re</i> 1 0 <i>im</i> 0;1 0 </p>
 </dd></dl>
<h3>Field Codes</h3>
<p> When specifying the input to a field, either as a <code>CONST</code> scalar parameter, or as an input vector field to a non-<code>RAW</code> vector field, <i>field codes</i> are used. A <i>field code</i> is one of: </p>
<dl>
<dt>*</dt>
<dd> <p> a simple field name, indicating a vector or scalar field </p>
 </dd>
<dt>*</dt>
<dd> <p> a parent field name, followed by a forward slash, followed by a metafield name, indicating a metafield. See the description of the <code>META</code> directive above for further details. </p>
 </dd>
<dt>*</dt>
<dd> <p> either of the above, followed by a period, followed by a <i>representation suffix</i>, but only if the field or metafield specified is not a <code>STRING</code> type field. </p>
 </dd></dl>
<p>A <i>representation suffix</i> may be used used to extract a real number from a complex value. The available suffixes and their meanings are: </p>
<dl>
<dt><code>.a</code></dt>
<dd> <p> This representation indicates the angle (in radians) between the positive real axis and the value (ie. the complex argument). The argument is in the range [-pi, pi], and a branch cut exists along the negative real axis. At the branch cut, -pi is returned if the imaginary part is -0, and pi is returned if the branch cut is +0. If z=0, zero is returned. </p>
 </dd>
<dt><code>.i</code></dt>
<dd> <p> This representation indicates the projection of the value onto the imaginary axis (ie. the imaginary part of the number). </p>
 </dd>
<dt><code>.m</code></dt>
<dd> <p> This representation indicates the modulus of the value (ie. its absolute value). </p>
 </dd>
<dt><code>.r</code></dt>
<dd> <p> This representation indicates the projection of the value onto the real axis (ie. the real part of the number). </p>
 </dd></dl>
<p>If the specified field is purely real, the representations are calculated as if the imaginary part was equal to +0. For example, given a complex valued vector, <i>z</i>, a vector containing the real part of <i>z</i>,~<i>re_z</i>, could be produced with: </p>
<dl>
<dd> <p> <i>re_z</i> <code>PHASE</code> <i>z.r</i> 0 </p>
 </dd></dl>
<p>and similarly for the complex field&#8217;s imaginary part, argument, and absolute value. (Although it should be pointed out this simplistic an example isn&#8217;t strictly necessary, since <i>z.r</i> could be used wherever <i>re_z</i> would be.) </p>
<h2>STANDARDS VERSIONS</h2>
<p>This document describes Version 7 of the Dirfile Standards. </p>
<p>Version 7 of the Standards (October 2009) added the <code>SBIT</code> and <code>POLYNOM</code> field types, and the directive-less method of specifying metafields. It also introduced the data types <i>COMPLEX128</i> and <i>COMPLEX64</i>, along with the notion of <i>representations</i>. Finally, it made the number of fields parameter for <i>LINCOM</i> optional. </p>
<p>Version 6 of the Standards (October 2008) added the <code>/ENCODING</code>,~<code>/META</code>,~<code>/PROTECT</code>, and <code>/REFERENCE</code> directives, and the <code>CONST</code> and <code>STRING</code> field types. It permitted whitespace in tokens and introduced the character escape sequences. It allowed <code>CONST</code> fields to be used as parameters in field specification lines. It also removed <i>FILEFRAM</i> as an alias for <i>INDEX</i>, and allowed <code>#</code> and <code>\</code> in field names. </p>
<p>Version 5 of the Standards (August 2008) added <code>/VERSION</code> and <code>/ENDIAN</code>, slash demarcation of reserved words, and removed the restriction on field name length. It introduced the data types <i>INT8</i>,~<i>INT64</i>, and <i>UINT64</i>, the new-style type specifiers, and increased the range of the <code>BIT</code> field type from 32 to 64 bits. It also prohibited the characters <code>#&amp;/;&lt;&gt;\.|</code> in field names. </p>
<p>Version 4 of the Standards (October 2006) added the <code>PHASE</code> field type. </p>
<p>Version 3 of the Standards (January 2006) added <code>INCLUDE </code> and increased the allowed length of a field name from 16 to 50 characters. </p>
<p>Version 2 of the Standards (September 2005) added the <code>MULTIPLY</code> field type. </p>
<p>Version 1 of the Standards (November 2004) added <code>FRAMEOFFSET</code> and the optional fourth argument to the <code>BIT</code> field type. </p>
<p>Version 0 of the Standards (before March 2003) refers to the dirfile standards supported by the <code><a href="/docs/linux/man/3-getdata/">getdata</a></code>(3) library originally introduced into the <code><a href="/docs/linux/man/1-kst/">kst</a></code>(1) sources, which contained support for all other features covered by this document. </p>
<h2>AUTHORS</h2>
<p>The dirfile specification was developed by C. B. Netterfield &lt;netterfield [at] astro.utoronto.ca&gt; </p>
<p>Since Standards Version 3, the dirfile specification has been maintained by D. V. Wiebe &lt;dwiebe [at] physics.utoronto.ca&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/5-dirfile/">dirfile</a></code>(5), <code><a href="/docs/linux/man/5-dirfile-encoding/">dirfile-encoding</a></code>(5) </p>
