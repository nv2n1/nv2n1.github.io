---
title: "copy(7)"
name: "copy"
section: "7"
letter: "c"
url: "/docs/linux/man/7-copy/"
description: "COPY – copy data between a file and a table"
---

<p>COPY &#8211; copy data between a file and a table </p>
<h2>Synopsis</h2>
<pre>COPY <i>tablename</i> [ ( <i>column</i> [, ...] ) ]
 FROM { '<i>filename</i>' | STDIN }
 [ [ WITH ] 
 [ BINARY ]
 [ OIDS ]
 [ DELIMITER [ AS ] '<i>delimiter</i>' ]
 [ NULL [ AS ] '<i>null string</i>' ]
 [ CSV [ HEADER ]
 [ QUOTE [ AS ] '<i>quote</i>' ] 
 [ ESCAPE [ AS ] '<i>escape</i>' ]
 [ FORCE NOT NULL <i>column</i> [, ...] ]
COPY { <i>tablename</i> [ ( <i>column</i> [, ...] ) ] | ( <i>query</i> ) }
 TO { '<i>filename</i>' | STDOUT }
 [ [ WITH ] 
 [ BINARY ]
 [ OIDS ]
 [ DELIMITER [ AS ] '<i>delimiter</i>' ]
 [ NULL [ AS ] '<i>null string</i>' ]
 [ CSV [ HEADER ]
 [ QUOTE [ AS ] '<i>quote</i>' ] 
 [ ESCAPE [ AS ] '<i>escape</i>' ]
 [ FORCE QUOTE <i>column</i> [, ...] ]</pre>
<h2>Description</h2>
<p><code>COPY</code> moves data between PostgreSQL tables and standard file-system files. <code>COPY TO</code> copies the contents of a table <code>to</code> a file, while <code>COPY FROM</code> copies data <code>from</code> a file to a table (appending the data to whatever is in the table already). <code>COPY TO</code> can also copy the results of a <code>SELECT</code> query. </p>
<p> If a list of columns is specified, <code>COPY</code> will only copy the data in the specified columns to or from the file. If there are any columns in the table that are not in the column list, <code>COPY FROM</code> will insert the default values for those columns. </p>
<p> <code>COPY</code> with a file name instructs the PostgreSQL server to directly read from or write to a file. The file must be accessible to the server and the name must be specified from the viewpoint of the server. When STDIN or STDOUT is specified, data is transmitted via the connection between the client and the server.</p>
<h2>Parameters</h2>
<dl>
<dt><i>tablename</i></dt>
<dd>The name (optionally schema-qualified) of an existing table.</dd>
<dt><i>column</i></dt>
<dd>An optional list of columns to be copied. If no column list is specified, all columns of the table will be copied.</dd>
<dt><i>query</i></dt>
<dd>A SELECT [<code><a href="/docs/linux/man/7-select/">select</a></code>(7)] or VALUES [<code><a href="/docs/linux/man/7-values/">values</a></code>(7)] command whose results are to be copied. Note that parentheses are required around the query.</dd>
<dt><i>filename</i></dt>
<dd>The absolute path name of the input or output file. Windows users might need to use an E&#8221; string and double backslashes used as path separators.</dd>
<dt><code>STDIN</code></dt>
<dd>Specifies that input comes from the client application.</dd>
<dt><code>STDOUT</code></dt>
<dd>Specifies that output goes to the client application.</dd>
<dt><code>BINARY</code></dt>
<dd>Causes all data to be stored or read in binary format rather than as text. You cannot specify the <code>DELIMITER</code>, <code>NULL</code>, or <code>CSV</code> options in binary mode.</dd>
<dt><code>OIDS</code></dt>
<dd>Specifies copying the OID for each row. (An error is raised if OIDS is specified for a table that does not have OIDs, or in the case of copying a <i>query</i>.)</dd>
<dt><i>delimiter</i></dt>
<dd>The single ASCII character that separates columns within each row (line) of the file. The default is a tab character in text mode, a comma in CSV mode.</dd>
<dt><i>null string</i></dt>
<dd>The string that represents a null value. The default is \N (backslash-N) in text mode, and an unquoted empty string in CSV mode. You might prefer an empty string even in text mode for cases where you don&#8217;t want to distinguish nulls from empty strings. </dd>
<dl>
<dd><code>Note:</code> When using <code>COPY FROM</code>, any data item that matches this string will be stored as a null value, so you should make sure that you use the same string as you used with <code>COPY TO</code>.</dd></dl>
<dt><code>CSV</code></dt>
<dd>Selects Comma Separated Value (CSV) mode.</dd>
<dt><code>HEADER</code></dt>
<dd>Specifies that the file contains a header line with the names of each column in the file. On output, the first line contains the column names from the table, and on input, the first line is ignored.</dd>
<dt><i>quote</i></dt>
<dd>Specifies the ASCII quotation character in CSV mode. The default is double-quote.</dd>
<dt><i>escape</i></dt>
<dd>Specifies the ASCII character that should appear before a QUOTE data character value in CSV mode. The default is the QUOTE value (usually double-quote).</dd>
<dt><code>FORCE QUOTE</code></dt>
<dd>In CSV <code>COPY TO</code> mode, forces quoting to be used for all non-NULL values in each specified column. NULL output is never quoted.</dd>
<dt><code>FORCE NOT NULL</code></dt>
<dd>In CSV <code>COPY FROM</code> mode, process each specified column as though it were quoted and hence not a NULL value. For the default null string in CSV mode (&#8221;), this causes missing values to be input as zero-length strings.</dd></dl>
<h2>Outputs</h2>
<p>On successful completion, a <code>COPY</code> command returns a command tag of the form </p>
<pre>COPY <i>count</i></pre>
<p>The <i>count</i> is the number of rows copied.</p>
<h2>Notes</h2>
<p><code>COPY</code> can only be used with plain tables, not with views. However, you can write COPY (SELECT * FROM <i>viewname</i>) TO &#8230;. </p>
<p> The BINARY key word causes all data to be stored/read as binary format rather than as text. It is somewhat faster than the normal text mode, but a binary-format file is less portable across machine architectures and PostgreSQL versions. Also, the binary format is very data type specific; for example it will not work to output binary data from a <code>smallint</code> column and read it into an <code>integer</code> column, even though that would work fine in text format. </p>
<p> You must have select privilege on the table whose values are read by <code>COPY TO</code>, and insert privilege on the table into which values are inserted by <code>COPY FROM</code>. It is sufficient to have column privileges on the column(s) listed in the command. </p>
<p> Files named in a <code>COPY</code> command are read or written directly by the server, not by the client application. Therefore, they must reside on or be accessible to the database server machine, not the client. They must be accessible to and readable or writable by the PostgreSQL user (the user ID the server runs as), not the client. <code>COPY</code> naming a file is only allowed to database superusers, since it allows reading or writing any file that the server has privileges to access. </p>
<p> Do not confuse <code>COPY</code> with the <code>psql</code> instruction <code></code> <code>\copy</code>. <code>\copy</code> invokes <code>COPY FROM STDIN</code> or <code>COPY TO STDOUT</code>, and then fetches/stores the data in a file accessible to the <code>psql</code> client. Thus, file accessibility and access rights depend on the client rather than the server when <code>\copy</code> is used. </p>
<p> It is recommended that the file name used in <code>COPY</code> always be specified as an absolute path. This is enforced by the server in the case of <code>COPY TO</code>, but for <code>COPY FROM</code> you do have the option of reading from a file specified by a relative path. The path will be interpreted relative to the working directory of the server process (normally the cluster&#8217;s data directory), not the client&#8217;s working directory. </p>
<p> <code>COPY FROM</code> will invoke any triggers and check constraints on the destination table. However, it will not invoke rules. </p>
<p> <code>COPY</code> input and output is affected by DateStyle. To ensure portability to other PostgreSQL installations that might use non-default DateStyle settings, DateStyle should be set to ISO before using <code>COPY TO</code>. It is also a good idea to avoid dumping data with IntervalStyle set to sql_standard, because negative interval values might be misinterpreted by a server that has a different setting for IntervalStyle. </p>
<p> Input data is interpreted according to the current client encoding, and output data is encoded in the the current client encoding, even if the data does not pass through the client but is read from or written to a file. </p>
<p> <code>COPY</code> stops operation at the first error. This should not lead to problems in the event of a <code>COPY TO</code>, but the target table will already have received earlier rows in a <code>COPY FROM</code>. These rows will not be visible or accessible, but they still occupy disk space. This might amount to a considerable amount of wasted disk space if the failure happened well into a large copy operation. You might wish to invoke <code>VACUUM</code> to recover the wasted space.  </p>
<h2>FILE FORMATS</h2>
<h3>TEXT FORMAT</h3>
<p> When <code>COPY</code> is used without the BINARY or CSV options, the data read or written is a text file with one line per table row. Columns in a row are separated by the delimiter character. The column values themselves are strings generated by the output function, or acceptable to the input function, of each attribute&#8217;s data type. The specified null string is used in place of columns that are null. <code>COPY FROM</code> will raise an error if any line of the input file contains more or fewer columns than are expected. If OIDS is specified, the OID is read or written as the first column, preceding the user data columns. </p>
<p> End of data can be represented by a single line containing just backslash-period (\.). An end-of-data marker is not necessary when reading from a file, since the end of file serves perfectly well; it is needed only when copying data to or from client applications using pre-3.0 client protocol. </p>
<p> Backslash characters (\) can be used in the <code>COPY</code> data to quote data characters that might otherwise be taken as row or column delimiters. In particular, the following characters <code>must</code> be preceded by a backslash if they appear as part of a column value: backslash itself, newline, carriage return, and the current delimiter character. </p>
<p> The specified null string is sent by <code>COPY TO</code> without adding any backslashes; conversely, <code>COPY FROM</code> matches the input against the null string before removing backslashes. Therefore, a null string such as \N cannot be confused with the actual data value \N (which would be represented as \\N). </p>
<p> The following special backslash sequences are recognized by <code>COPY FROM</code>: SequenceRepresents\bBackspace (ASCII 8)\fForm feed (ASCII 12)\nNewline (ASCII 10)\rCarriage return (ASCII 13)\tTab (ASCII 9)\vVertical tab (ASCII 11)\<i>digits</i>Backslash followed by one to three octal digits specifies the character with that numeric code\x <i>digits</i>Backslash x followed by one or two hex digits specifies the character with that numeric code Presently, <code>COPY TO</code> will never emit an octal or hex-digits backslash sequence, but it does use the other sequences listed above for those control characters. </p>
<p> Any other backslashed character that is not mentioned in the above table will be taken to represent itself. However, beware of adding backslashes unnecessarily, since that might accidentally produce a string matching the end-of-data marker (\.) or the null string (\N by default). These strings will be recognized before any other backslash processing is done. </p>
<p> It is strongly recommended that applications generating <code>COPY</code> data convert data newlines and carriage returns to the \n and \r sequences respectively. At present it is possible to represent a data carriage return by a backslash and carriage return, and to represent a data newline by a backslash and newline. However, these representations might not be accepted in future releases. They are also highly vulnerable to corruption if the <code>COPY</code> file is transferred across different machines (for example, from Unix to Windows or vice versa). </p>
<p> <code>COPY TO</code> will terminate each row with a Unix-style newline (``\n&#8217;&#8216;). Servers running on Microsoft Windows instead output carriage return/newline (``\r\n&#8217;&#8216;), but only for <code>COPY</code> to a server file; for consistency across platforms, <code>COPY TO STDOUT</code> always sends ``\n&#8217;&#8216; regardless of server platform. <code>COPY FROM</code> can handle lines ending with newlines, carriage returns, or carriage return/newlines. To reduce the risk of error due to un-backslashed newlines or carriage returns that were meant as data, <code>COPY FROM</code> will complain if the line endings in the input are not all alike.  </p>
<h3>CSV FORMAT</h3>
<p> This format is used for importing and exporting the Comma Separated Value (CSV) file format used by many other programs, such as spreadsheets. Instead of the escaping used by PostgreSQL&#8217;s standard text mode, it produces and recognizes the common CSV escaping mechanism. </p>
<p> The values in each record are separated by the DELIMITER character. If the value contains the delimiter character, the QUOTE character, the NULL string, a carriage return, or line feed character, then the whole value is prefixed and suffixed by the QUOTE character, and any occurrence within the value of a QUOTE character or the ESCAPE character is preceded by the escape character. You can also use FORCE QUOTE to force quotes when outputting non-NULL values in specific columns. </p>
<p> The CSV format has no standard way to distinguish a NULL value from an empty string. PostgreSQL&#8217;s <code>COPY</code> handles this by quoting. A NULL is output as the NULL parameter string and is not quoted, while a non-NULL value matching the NULL parameter string is quoted. For example, with the default settings, a NULL is written as an unquoted empty string, while an empty string data value is written with double quotes (&quot;&quot;). Reading values follows similar rules. You can use FORCE NOT NULL to prevent NULL input comparisons for specific columns. </p>
<p> Because backslash is not a special character in the CSV format, \., the end-of-data marker, could also appear as a data value. To avoid any misinterpretation, a \. data value appearing as a lone entry on a line is automatically quoted on output, and on input, if quoted, is not interpreted as the end-of-data marker. If you are loading a file created by another application that has a single unquoted column and might have a value of \., you might need to quote that value in the input file. </p>
<dl>
<dd> <p> <code>Note:</code> In CSV mode, all characters are significant. A quoted value surrounded by white space, or any characters other than DELIMITER, will include those characters. This can cause errors if you import data from a system that pads CSV lines with white space out to some fixed width. If such a situation arises you might need to preprocess the CSV file to remove the trailing white space, before importing the data into PostgreSQL. </p>
 </dd></dl>
<dl>
<dd> <p> <code>Note:</code> CSV mode will both recognize and produce CSV files with quoted values containing embedded carriage returns and line feeds. Thus the files are not strictly one line per table row like text-mode files. </p>
 </dd></dl>
<dl>
<dd> <p> <code>Note:</code> Many programs produce strange and occasionally perverse CSV files, so the file format is more a convention than a standard. Thus you might encounter some files that cannot be imported using this mechanism, and <code>COPY</code> might produce files that other programs cannot process. </p>
 </dd></dl>
<h3>BINARY FORMAT</h3>
<p> The file format used for <code>COPY BINARY</code> changed in PostgreSQL 7.4. The new format consists of a file header, zero or more tuples containing the row data, and a file trailer. Headers and data are now in network byte order.  </p>
<h3>FILE HEADER</h3>
<p> The file header consists of 15 bytes of fixed fields, followed by a variable-length header extension area. The fixed fields are: </p>
<dl>
<dt><code>Signature</code></dt>
<dd> <p> 11-byte sequence PGCOPY\n\377\r\n\0 --- note that the zero byte is a required part of the signature. (The signature is designed to allow easy identification of files that have been munged by a non-8-bit-clean transfer. This signature will be changed by end-of-line-translation filters, dropped zero bytes, dropped high bits, or parity changes.) </p>
 </dd>
<dt><code>Flags field</code></dt>
<dd> <p> 32-bit integer bit mask to denote important aspects of the file format. Bits are numbered from 0 (LSB) to 31 (MSB). Note that this field is stored in network byte order (most significant byte first), as are all the integer fields used in the file format. Bits 16-31 are reserved to denote critical file format issues; a reader should abort if it finds an unexpected bit set in this range. Bits 0-15 are reserved to signal backwards-compatible format issues; a reader should simply ignore any unexpected bits set in this range. Currently only one flag bit is defined, and the rest must be zero: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>Bit 16</code></dt>
<dd> <p> if 1, OIDs are included in the data; if 0, not </p>
 </dd></dl>
</dl>
</dl>
<dl>
<dt><code>Header extension area length</code></dt>
<dd> <p> 32-bit integer, length in bytes of remainder of header, not including self. Currently, this is zero, and the first tuple follows immediately. Future changes to the format might allow additional data to be present in the header. A reader should silently skip over any header extension data it does not know what to do with. </p>
 </dd></dl>
<p> The header extension area is envisioned to contain a sequence of self-identifying chunks. The flags field is not intended to tell readers what is in the extension area. Specific design of header extension contents is left for a later release. </p>
<p> This design allows for both backwards-compatible header additions (add header extension chunks, or set low-order flag bits) and non-backwards-compatible changes (set high-order flag bits to signal such changes, and add supporting data to the extension area if needed).  </p>
<h3>TUPLES</h3>
<p> Each tuple begins with a 16-bit integer count of the number of fields in the tuple. (Presently, all tuples in a table will have the same count, but that might not always be true.) Then, repeated for each field in the tuple, there is a 32-bit length word followed by that many bytes of field data. (The length word does not include itself, and can be zero.) As a special case, -1 indicates a NULL field value. No value bytes follow in the NULL case. </p>
<p> There is no alignment padding or any other extra data between fields. </p>
<p> Presently, all data values in a <code>COPY BINARY</code> file are assumed to be in binary format (format code one). It is anticipated that a future extension might add a header field that allows per-column format codes to be specified. </p>
<p> To determine the appropriate binary format for the actual tuple data you should consult the PostgreSQL source, in particular the <code>*send</code> and <code>*recv</code> functions for each column&#8217;s data type (typically these functions are found in the <i>src/backend/utils/adt/</i> directory of the source distribution). </p>
<p> If OIDs are included in the file, the OID field immediately follows the field-count word. It is a normal field except that it&#8217;s not included in the field-count. In particular it has a length word --- this will allow handling of 4-byte vs. 8-byte OIDs without too much pain, and will allow OIDs to be shown as null if that ever proves desirable.  </p>
<h3>FILE TRAILER</h3>
<p> The file trailer consists of a 16-bit integer word containing -1. This is easily distinguished from a tuple&#8217;s field-count word. </p>
<p> A reader should report an error if a field-count word is neither -1 nor the expected number of columns. This provides an extra check against somehow getting out of sync with the data.  </p>
<h2>EXAMPLES</h2>
<p> The following example copies a table to the client using the vertical bar (|) as the field delimiter: </p>
<pre><code>COPY country TO STDOUT WITH DELIMITER '|';
</code></pre>
<p> To copy data from a file into the country table: </p>
<pre><code>COPY country FROM '/usr1/proj/bray/sql/country_data';
</code></pre>
<p> To copy into a file just the countries whose names start with &#8216;A&#8217;: </p>
<pre><code>COPY (SELECT * FROM country WHERE country_name LIKE 'A%') TO '/usr1/proj/bray/sql/a_list_countries.copy';
</code></pre>
<p> Here is a sample of data suitable for copying into a table from STDIN: </p>
<pre><code>AF AFGHANISTAN
AL ALBANIA
DZ ALGERIA
ZM ZAMBIA
ZW ZIMBABWE
</code></pre>
<p> Note that the white space on each line is actually a tab character. </p>
<p> The following is the same data, output in binary format. The data is shown after filtering through the Unix utility <code>od -c</code>. The table has three columns; the first has type <code><a href="/docs/linux/man/2-char/">char</a>(2)</code>, the second has type <code>text</code>, and the third has type <code>integer</code>. All the rows have a null value in the third column. </p>
<pre><code>0000000 P G C O P Y \n 377 \r \n \0 \0 \0 \0 \0 \0
0000020 \0 \0 \0 \0 003 \0 \0 \0 002 A F \0 \0 \0 013 A
0000040 F G H A N I S T A N 377 377 377 377 \0 003
0000060 \0 \0 \0 002 A L \0 \0 \0 007 A L B A N I
0000100 A 377 377 377 377 \0 003 \0 \0 \0 002 D Z \0 \0 \0
0000120 007 A L G E R I A 377 377 377 377 \0 003 \0 \0
0000140 \0 002 Z M \0 \0 \0 006 Z A M B I A 377 377
0000160 377 377 \0 003 \0 \0 \0 002 Z W \0 \0 \0 \b Z I
0000200 M B A B W E 377 377 377 377 377 377
</code></pre>
<h2>COMPATIBILITY</h2>
<p> There is no <code>COPY</code> statement in the SQL standard. </p>
<p> The following syntax was used before PostgreSQL version 7.3 and is still supported: </p>
<pre><code>COPY [ BINARY ] tablename  [ WITH OIDS ]
    FROM { ' filename ' | STDIN }
    [ [USING] DELIMITERS ' delimiter ' ]
    [ WITH NULL AS ' null string ' ]
COPY [ BINARY ] tablename  [ WITH OIDS ]
    TO { ' filename ' | STDOUT }
    [ [USING] DELIMITERS ' delimiter ' ]
    [ WITH NULL AS ' null string ' ]
</code></pre>
<h2>Index</h2>
