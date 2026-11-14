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
<dt>bs=BYTES</p>
<dd> force ibs=BYTES and obs=BYTES</p>
<dt>cbs=BYTES</p>
<dd> convert BYTES bytes at a time</p>
<dt>conv=KEYWORDS</p>
<dd> convert the file as per the comma separated keyword list</p>
<dt>count=BLOCKS</p>
<dd> copy only BLOCKS input blocks</p>
<dt>ibs=BYTES</p>
<dd> read BYTES bytes at a time</p>
<dt>if=FILE</p>
<dd> read from FILE instead of stdin</p>
<dt>obs=BYTES</p>
<dd> write BYTES bytes at a time</p>
<dt>of=FILE</p>
<dd> write to FILE instead of stdout</p>
<dt>
<dd> NOTE: of=FILE may be used several times to write</p>
<dt>
<dd> output to multiple files simultaneously</p>
<dt>of:=COMMAND</p>
<dd> exec and write output to process COMMAND</p>
<dt>seek=BLOCKS</p>
<dd> skip BLOCKS obs-sized blocks at start of output</p>
<dt>skip=BLOCKS</p>
<dd> skip BLOCKS ibs-sized blocks at start of input</p>
<dt>pattern=HEX</p>
<dd> use the specified binary pattern as input</p>
<dt>textpattern=TEXT</p>
<dd> use repeating TEXT as input</p>
<dt>errlog=FILE</p>
<dd> send error messages to FILE as well as stderr</p>
<dt>hashwindow=BYTES</p>
<dd> perform a hash on every BYTES amount of data</p>
<dt>hash=NAME</p>
<dd> either md5, sha1, sha256, sha384 or sha512</p>
<dt>
<dd> default algorithm is md5. To select multiple algorithms to run simultaneously enter the names in a comma separated list</p>
<dt>hashlog=FILE</p>
<dd> send MD5 hash output to FILE instead of stderr</p>
<dt>
<dd> if you are using multiple hash algorithms you can send each to a seperate file using the convention ALGORITHMlog=FILE, for example md5log=FILE1, sha1log=FILE2, etc.</p>
<dt>hashlog:=COMMAND</p>
<dd> exec and write hashlog to process COMMAND</p>
<dt>
<dd> ALGORITHMlog:=COMMAND also works in the same fashion</p>
<dt>hashconv=[before|after]</p>
<dd> perform the hashing before or after the conversions</p>
<dt>hashformat=FORMAT</p>
<dd> display each hashwindow according to FORMAT</p>
<dt>
<dd> the hash format mini-language is described below</p>
<dt>totalhashformat=FORMAT</p>
<dd> display the total hash value according to FORMAT</p>
<dt>status=[on|off]</p>
<dd> display a continual status message on stderr</p>
<dt>
<dd> default state is &quot;on&quot;</p>
<dt>statusinterval=N</p>
<dd> update the status message every N blocks</p>
<dt>
<dd> default value is 256</p>
<dt>sizeprobe=[if|of]</p>
<dd> determine the size of the input or output file</p>
<dt>
<dd> for use with status messages. (this option gives you a percentage indicator) WARNING: do not use this option against a</p>
<dt>
<dd> tape device.</p>
<dt>split=BYTES</p>
<dd> write every BYTES amount of data to a new file</p>
<dt>
<dd> This operation applies to any of=FILE that follows</p>
<dt>splitformat=TEXT</p>
<dd> the file extension format for split operation.</p>
<dt>
<dd> you may use any number of &#8216;a&#8217; or &#8216;n&#8217; in any combo the default format is &quot;nnn&quot; NOTE: The split and splitformat options take effect</p>
<dt>
<dd> only for output files specified AFTER these options appear in the command line. Likewise, you may specify these several times for for different output files within the same command line. you may use as many digits in any combination you would like. (e.g. &quot;anaannnaana&quot; would be valid, but quite insane)</p>
<dt>vf=FILE</p>
<dd> verify that FILE matches the specified input</p>
<dt>verifylog=FILE</p>
<dd> send verify results to FILE instead of stderr</p>
<dt>verifylog:=COMMAND</p>
<dd> exec and write verify results to process COMMAND</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<p> The structure of of FORMAT may contain any valid text and special variables. The built-in variables are used the following format: #variable_name# To pass FORMAT strings to the program from a command line, it may be necessary to surround your FORMAT strings with &quot;quotes.&quot; The built-in variables are listed below:</p>
<dl>
<dt>window_start</p>
<dd> The beginning byte offset of the hashwindow</p>
<dt>window_end</p>
<dd> The ending byte offset of the hashwindow</p>
<dt>block_start</p>
<dd> The beginning block (by input blocksize) of the window</p>
<dt>block_end</p>
<dd> The ending block (by input blocksize) of the hash window</p>
<dt>hash</p>
<dd> The hash value</p>
<dt>algorithm</p>
<dd> The name of the hash algorithm</dl>
<h3>For example, the default FORMAT for hashformat and totalhashformat are:</h3>
<dl>
<dt>
<dd> hashformat=&quot;#window_start# &#8211; #window_end#: #hash#&quot; totalhashformat=&quot;Total (#algorithm#): #hash#&quot;</dl>
<h3>The FORMAT structure accepts the following escape codes:</h3>
<dl>
<dt>
</p>
<dd> Newline</p>
<dt>	</p>
<dd> Tab</p>
<dt></p>
<dd> Carriage return</p>
<dt>\</p>
<dd> Insert the &#8216;\&#8217; character</p>
<dt>##</p>
<dd> Insert the &#8216;#&#8217; character as text, not a variable</dl>
<p> BLOCKS and BYTES may be followed by the following multiplicative suffixes: xM M, c 1, w 2, b 512, kD 1000, k 1024, MD 1,000,000, M 1,048,576, GD 1,000,000,000, G 1,073,741,824, and so on for T, P, E, Z, Y. Each KEYWORD may be:</p>
<dl>
<dt>ascii</p>
<dd> from EBCDIC to ASCII</p>
<dt>ebcdic</p>
<dd> from ASCII to EBCDIC</p>
<dt>ibm</p>
<dd> from ASCII to alternated EBCDIC</p>
<dt>block</p>
<dd> pad newline-terminated records with spaces to cbs-size</p>
<dt>unblock</p>
<dd> replace trailing spaces in cbs-size records with newline</p>
<dt>lcase</p>
<dd> change upper case to lower case</p>
<dt>notrunc</p>
<dd> do not truncate the output file</p>
<dt>ucase</p>
<dd> change lower case to upper case</p>
<dt>swab</p>
<dd> swap every pair of input bytes</p>
<dt>noerror</p>
<dd> continue after read errors</p>
<dt>sync</p>
<dd> pad every input block with NULs to ibs-size; when used with block or unblock, pad with spaces rather than NULs</dl>
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
<dd> <code>info dcfldd</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
