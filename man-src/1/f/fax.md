---
title: "fax(1)"
name: "fax"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fax/"
description: "fax – make, send, receive, view or print a fax"
---

<h2 class="name">NAME</h2>
<p> fax &#8211; make, send, receive, view or print a fax </p>
<h2>SYNOPSIS</h2>
<p> <code>fax</code> <code>help</code> </p>
<p> <code>fax</code> <code>make</code> [<code>-l</code>] <i>file</i> </p>
<p> <code>fax</code> <code>send</code> [<code>-l</code>] [<code>-v</code>] { <code>-m</code> | <i>number</i> } <i>filename</i>&#8230; </p>
<p> <code>fax</code> [ <code>receive</code> [<code>-v</code>] [ <i>filename-prefix</i> ] ] </p>
<p> <code>fax</code> { <code>print</code> | <code>view</code> | <code>rm</code> } <i>filename</i>&#8230; </p>
<p> <code>fax</code> {<code> queue </code>|<code> status </code>[<i>t</i>] | <code> start </code>|<code> stop </code>} </p>
<p> <code>fax</code> <code>answer</code> </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-l</code></p>
<dd> use low (96 line per inch) resolution</p>
<dt><code>-v</code></p>
<dd> display verbose messages for debugging</p>
<dt><code>-m</code></p>
<dd> the phone call has already been dialed manually </p>
</dl>
<p> The commands make, send, receive, view and queue may be abbreviated to their first characters (e.g. &#8220;fax q&#8221;). </p>
<p> Assignments of the form <i>VARIABLE</i><code>=</code><i>value</i> may appear before the command name to temporarily change the values of most fax script variables (e.g. &#8220;fax PAGE=A4 print letter.001&#8221;) </p>
<h2>DESCRIPTION</h2>
<p> <code>fax</code> provides a simple user interface to the <a href="/docs/linux/man/1-efax/">efax</a>(1) and <a href="/docs/linux/man/1-efix/">efix</a>(1) programs. It allows you to send text or Postscript files as faxes and receive, print or preview received faxes. The <code>fax help</code> command prints a summary of the possible commands. </p>
<p> To send a fax, the original files need to be converted from ASCII or Postscript into a particular bit-map format (TIFF with Group 3 encoding). This can be done automatically by the <code>fax send</code> command or you can use the <code>fax make</code> command to do the conversion before sending the fax. The conversion will create one file per page. These files will have the name of the original file with the page number as an additional suffix. For example, running <code>fax make doc.ps</code> on the two-page postscript file doc.ps would generate the files doc.ps.001 and doc.ps.002. </p>
<p> When sending a fax with the <code>fax send</code> command you may dial the number manually and use the <code>-m</code> option or you may give the phone number on the command line. The names of the files to be sent are given on the command line, usually by using wildcards. For example, to send a multi-page fax consisting of the files doc.ps.001, doc.ps.002, and so on, you could use the command <code>fax send 555-1212 doc.ps.0*</code> (if you had already run the <code>fax make</code> command) or simply <code>fax send 555-1212 doc.ps</code>. If the number is busy the script will wait and try again. </p>
<p> Use the <code>fax receive</code> command to answer the phone and receive a fax. If a file name is specified the received fax will be stored in files with the given file name plus an extension equal to the page number. If no options are given, the received fax will be stored in files having a name given by the date and time and an extension equal to the page number. For example, a fax received beginning on July 4 at 3:05:20 pm will generate files 0704150520.001, 0704150520.002, and so on. </p>
<p> The <code>fax print</code>, <code>fax view</code>, and <code>fax rm</code> commands are used to print, preview or remove received fax files. As with the send command the file names are usually given using wildcards. </p>
<p> If efax has been installed for automatic fax reception you can use the <code>fax queue</code> command to check for files in the incoming spool directory. The fax script can also be configured to print received faxes or e-mail them as MIME attachments with type image/tiff-f. For convenience the <code>fax print</code>, <code>view</code> and <code>rm</code> commands will first check for the named files in this spool directory. The <code>fax status</code> command shows the status of the automatic receive process once, or every <i>t</i> seconds. Privileged users can use the <code>fax stop</code> and <code>fax start</code> commands to stop and restart the fax reception daemon. </p>
<p> The <code>fax answer</code> command is used for unattended reception of faxes. It is normally placed in the <a href="/docs/linux/man/5-inittab/">inittab</a>(5) or <a href="/docs/linux/man/5-ttytab/">ttytab</a>(5) file and is run automatically by <a href="/docs/linux/man/8-init/">init</a>(8). </p>
<p> The <code>-v</code> option displays verbose messages. </p>
<p> Other features of the fax script are documented within the script: </p>
<dl>
<dt><code>&#8211;</code></p>
<dd> a directory that lets you specify recipients by name instead of number </p>
<dt><code>&#8211;</code></p>
<dd> the <code>fax new</code> command to create a simple cover page and start up a text editor </p>
<dt><code>&#8211;</code></p>
<dd> the <code>fax makefont</code> command converts a Postscript font to a bit-mapped font for use in headers or text </p>
</dl>
<h2>RESOLUTION</h2>
<p> Faxes can be created at low (98 lines per inch) or high (196 lpi) resolution. Almost all fax machines will operate at either resolution. By default files are created at high resolution but you can use the optional <code>-l</code> argument to create files at low resolution. </p>
<h2>SESSION LOGS</h2>
<p> The modem commands and responses together with status and error messages are written to file. If the fax is successfully sent or received the log file is removed. Otherwise a message is printed showing the log file name. Please send a copy of this file when reporting problems with efax. </p>
<h2>FILES</h2>
<p> The fax script will `source&#8217; the optional shell scripts <code>/etc/efax.rc</code>, <code>~/.efaxrc</code> and/or <code>./.efaxrc</code> before processing command-line arguments. These files can be used to set script variables to custom values for a particular system, user and/or directory. </p>
<p> The following files are created in the FAXDIR spool directory when automatic fax reception is enabled (see the fax script). DEV represents the name of the fax modem device file in /dev (e.g. cua1 for /dev/cua1). </p>
<dl>
<dt>DEV.<i>n</i></p>
<dd> the log file created by the fax answer daemon with process id <i>n</i></p>
<dt>DEV.log</p>
<dd> contains collected log files for device DEV. Log files showing a termination status of 1 (device busy) or 4 (no response from modem) are not added to this file.</p>
<dt>DEV.stop</p>
<dd> created by the fax stop command to prevent the fax daemon from starting up. </p>
</dl>
<h2>AUTHOR</h2>
<p> Fax was written by Ed Casas. Please send comments or bug reports to edc [at] cce.com. Please describe the type of modem used and include a copy of the log file. </p>
<h2>COPYRIGHT</h2>
<p> Fax is copyright 1993 &#8212; 1999 by Ed Casas. It may be used, copied and modified under the terms of the GNU Public License. </p>
<h2>DISCLAIMER</h2>
<p> Although <code>fax</code> has been tested, it may have errors that will prevent it from working correctly on your system. Some of these errors may cause serious problems including loss of data and interruptions to telephone service. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-efax/">efax</a>(1),</code> <code><a href="/docs/linux/man/1-efix/">efix</a>(1),</code> <code><a href="/docs/linux/man/1-ghostscript/">ghostscript</a>(1).</code> </p>
<h2>BUGS</h2>
<p> See <a href="/docs/linux/man/1-efax/">efax</a>(1). </p>
<h2>Index</h2>
