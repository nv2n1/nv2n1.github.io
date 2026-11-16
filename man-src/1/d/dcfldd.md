---
title: "dcfldd(1)"
name: "dcfldd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dcfldd/"
description: "dcfldd – manual page for dcfldd (dcfldd) 1.3.4"
---

<h2>NAME</h2>
<p> dcfldd &#8211; manual page for dcfldd (dcfldd) 1.3.4</p>
<h2>SYNOPSIS</h2>
<p> <code>dcfldd</code> [<i>OPTION</i>]&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Copy a file, converting and formatting according to the options.</p>
<dl>
<dt>bs=BYTES</dt>
<dd> force ibs=BYTES and obs=BYTES</dd>
<dt>cbs=BYTES</dt>
<dd> convert BYTES bytes at a time</dd>
<dt>conv=KEYWORDS</dt>
<dd> convert the file as per the comma separated keyword list</dd>
<dt>count=BLOCKS</dt>
<dd> copy only BLOCKS input blocks</dd>
<dt>ibs=BYTES</dt>
<dd> read BYTES bytes at a time</dd>
<dt>if=FILE</dt>
<dd> read from FILE instead of stdin</dd>
<dt>obs=BYTES</dt>
<dd> write BYTES bytes at a time</dd>
<dt>of=FILE</dt>
<dd> write to FILE instead of stdout</dd>
<dt>
</dt><dd> NOTE: of=FILE may be used several times to write</dd>
<dt>
</dt><dd> output to multiple files simultaneously</dd>
<dt>of:=COMMAND</dt>
<dd> exec and write output to process COMMAND</dd>
<dt>seek=BLOCKS</dt>
<dd> skip BLOCKS obs-sized blocks at start of output</dd>
<dt>skip=BLOCKS</dt>
<dd> skip BLOCKS ibs-sized blocks at start of input</dd>
<dt>pattern=HEX</dt>
<dd> use the specified binary pattern as input</dd>
<dt>textpattern=TEXT</dt>
<dd> use repeating TEXT as input</dd>
<dt>errlog=FILE</dt>
<dd> send error messages to FILE as well as stderr</dd>
<dt>hashwindow=BYTES</dt>
<dd> perform a hash on every BYTES amount of data</dd>
<dt>hash=NAME</dt>
<dd> either md5, sha1, sha256, sha384 or sha512</dd>
<dt>
</dt><dd> default algorithm is md5. To select multiple algorithms to run simultaneously enter the names in a comma separated list</dd>
<dt>hashlog=FILE</dt>
<dd> send MD5 hash output to FILE instead of stderr</dd>
<dt>
</dt><dd> if you are using multiple hash algorithms you can send each to a seperate file using the convention ALGORITHMlog=FILE, for example md5log=FILE1, sha1log=FILE2, etc.</dd>
<dt>hashlog:=COMMAND</dt>
<dd> exec and write hashlog to process COMMAND</dd>
<dt>
</dt><dd> ALGORITHMlog:=COMMAND also works in the same fashion</dd>
<dt>hashconv=[before|after]</dt>
<dd> perform the hashing before or after the conversions</dd>
<dt>hashformat=FORMAT</dt>
<dd> display each hashwindow according to FORMAT</dd>
<dt>
</dt><dd> the hash format mini-language is described below</dd>
<dt>totalhashformat=FORMAT</dt>
<dd> display the total hash value according to FORMAT</dd>
<dt>status=[on|off]</dt>
<dd> display a continual status message on stderr</dd>
<dt>
</dt><dd> default state is &quot;on&quot;</dd>
<dt>statusinterval=N</dt>
<dd> update the status message every N blocks</dd>
<dt>
</dt><dd> default value is 256</dd>
<dt>sizeprobe=[if|of]</dt>
<dd> determine the size of the input or output file</dd>
<dt>
</dt><dd> for use with status messages. (this option gives you a percentage indicator) WARNING: do not use this option against a</dd>
<dt>
</dt><dd> tape device.</dd>
<dt>split=BYTES</dt>
<dd> write every BYTES amount of data to a new file</dd>
<dt>
</dt><dd> This operation applies to any of=FILE that follows</dd>
<dt>splitformat=TEXT</dt>
<dd> the file extension format for split operation.</dd>
<dt>
</dt><dd> you may use any number of &#8216;a&#8217; or &#8216;n&#8217; in any combo the default format is &quot;nnn&quot; NOTE: The split and splitformat options take effect</dd>
<dt>
</dt><dd> only for output files specified AFTER these options appear in the command line. Likewise, you may specify these several times for for different output files within the same command line. you may use as many digits in any combination you would like. (e.g. &quot;anaannnaana&quot; would be valid, but quite insane)</dd>
<dt>vf=FILE</dt>
<dd> verify that FILE matches the specified input</dd>
<dt>verifylog=FILE</dt>
<dd> send verify results to FILE instead of stderr</dd>
<dt>verifylog:=COMMAND</dt>
<dd> exec and write verify results to process COMMAND</dd>
<dt><code>&#8211;help</code></dt>
<dd> display this help and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version information and exit</dd></dl>
<p> The structure of of FORMAT may contain any valid text and special variables. The built-in variables are used the following format: #variable_name# To pass FORMAT strings to the program from a command line, it may be necessary to surround your FORMAT strings with &quot;quotes.&quot; The built-in variables are listed below:</p>
<dl>
<dt>window_start</dt>
<dd> The beginning byte offset of the hashwindow</dd>
<dt>window_end</dt>
<dd> The ending byte offset of the hashwindow</dd>
<dt>block_start</dt>
<dd> The beginning block (by input blocksize) of the window</dd>
<dt>block_end</dt>
<dd> The ending block (by input blocksize) of the hash window</dd>
<dt>hash</dt>
<dd> The hash value</dd>
<dt>algorithm</dt>
<dd> The name of the hash algorithm</dd></dl>
<h3>For example, the default FORMAT for hashformat and totalhashformat are:</h3>
<dl>
<dt>
</dt><dd> hashformat=&quot;#window_start# &#8211; #window_end#: #hash#&quot; totalhashformat=&quot;Total (#algorithm#): #hash#&quot;</dd></dl>
<h3>The FORMAT structure accepts the following escape codes:</h3>
<dl>
<dt>
</dt>
<dd> Newline</dd>
<dt>	</dt>
<dd> Tab</dd>
<dt>
</dt>
<dd> Carriage return</dd>
<dt>\</dt>
<dd> Insert the &#8216;\&#8217; character</dd>
<dt>##</dt>
<dd> Insert the &#8216;#&#8217; character as text, not a variable</dd></dl>
<p> BLOCKS and BYTES may be followed by the following multiplicative suffixes: xM M, c 1, w 2, b 512, kD 1000, k 1024, MD 1,000,000, M 1,048,576, GD 1,000,000,000, G 1,073,741,824, and so on for T, P, E, Z, Y. Each KEYWORD may be:</p>
<dl>
<dt>ascii</dt>
<dd> from EBCDIC to ASCII</dd>
<dt>ebcdic</dt>
<dd> from ASCII to EBCDIC</dd>
<dt>ibm</dt>
<dd> from ASCII to alternated EBCDIC</dd>
<dt>block</dt>
<dd> pad newline-terminated records with spaces to cbs-size</dd>
<dt>unblock</dt>
<dd> replace trailing spaces in cbs-size records with newline</dd>
<dt>lcase</dt>
<dd> change upper case to lower case</dd>
<dt>notrunc</dt>
<dd> do not truncate the output file</dd>
<dt>ucase</dt>
<dd> change lower case to upper case</dd>
<dt>swab</dt>
<dd> swap every pair of input bytes</dd>
<dt>noerror</dt>
<dd> continue after read errors</dd>
<dt>sync</dt>
<dd> pad every input block with NULs to ibs-size; when used with block or unblock, pad with spaces rather than NULs</dd></dl>
<h2>AUTHOR</h2>
<p> Written by: dcfldd by Nicholas Harbour, GNU dd by Paul Rubin, David MacKenzie and Stuart Kemp.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;nicholasharbour [at] yahoo.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 1985-2006 Free Software Foundation, Inc.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>dcfldd</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>dcfldd</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info dcfldd</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
