---
title: "readpst(1)"
name: "readpst"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readpst/"
description: "readpst – convert PST (MS Outlook Personal Folders) files to mbox and other formats"
---

<h2 class="name">NAME</h2>
<p> readpst &#8211; convert PST (MS Outlook Personal Folders) files to mbox and other formats </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>readpst</code> [<code>-C&nbsp;<wbr></code><i>default-charset</i>] [<code>-D</code>] [<code>-M</code>] [<code>-S</code>] [<code>-V</code>] [<code>-b</code>] [<code>-c&nbsp;<wbr></code><i>format</i>] [<code>-d&nbsp;<wbr></code><i>debug-file</i>] [<code>-e</code>] [<code>-h</code>] [<code>-j&nbsp;<wbr></code><i>jobs</i>] [<code>-k</code>] [<code>-m</code>] [<code>-o&nbsp;<wbr></code><i>output-directory</i>] [<code>-q</code>] [<code>-r</code>] [<code>-t&nbsp;<wbr></code><i>output-type-codes</i>] [<code>-u</code>] [<code>-w</code>] pstfile</dl>
<h2>DESCRIPTION</h2>
<p> <code>readpst</code></p>
<dd>is a program that can read an Outlook PST (Personal Folders) file and convert it into an mbox file, a format suitable for KMail, a recursive mbox structure, or separate emails.</p>
<h2>OPTIONS</h2>
<p> -C <i>default-charset</i></p>
<dl>
<dt>
<dd> Set the character set to be used for items with an unspecified character set.</dl>
<p> -D</p>
<dl>
<dt>
<dd> Include deleted items in the output.</dl>
<p> -M</p>
<dl>
<dt>
<dd> Output messages in MH (rfc822) format as separate files. This will create folders as named in the PST file, and will put each email together with any attachments into its own file. These files will be numbered from 1 to n with no leading zeros. This format has no from quoting.</dl>
<p> -S</p>
<dl>
<dt>
<dd> Output messages into separate files. This will create folders as named in the PST file, and will put each email in its own file. These files will be numbered from 1 to n with no leading zeros. Attachments will also be saved in the same folder as the email message. The attachments for message $m are saved as $m-$name where $name is (the original name of the attachment, or &#8216;attach$n&#8217; if the attachment had no name), where $n is another sequential index with no leading zeros. This format has no from quoting.</dl>
<p> -V</p>
<dl>
<dt>
<dd> Show program version and exit.</dl>
<p> -b</p>
<dl>
<dt>
<dd> Do not save the attachments for the RTF format of the email body.</dl>
<p> -c <i>format</i></p>
<dl>
<dt>
<dd> Set the Contact output mode. Use -cv for vcard format or -cl for an email list.</dl>
<p> -d <i>debug-file</i></p>
<dl>
<dt>
<dd> Specify name of debug log file. The log file is now an ascii file, instead of the binary file used in previous versions.</dl>
<p> -e</p>
<dl>
<dt>
<dd> Same as the M option, but each output file will include an extension from (.eml, .ics, .vcf). This format has no from quoting.</dl>
<p> -h</p>
<dl>
<dt>
<dd> Show summary of options and exit.</dl>
<p> -j <i>jobs</i></p>
<dl>
<dt>
<dd> Specifies the maximum number of parallel jobs. Specify 0 to suppress running parallel jobs. Folders may be processed in parallel. Output formats that place each mail message in a separate file (-M, -S, -e) may process the contents of individual folders in parallel.</dl>
<p> -k</p>
<dl>
<dt>
<dd> Changes the output format to KMail. This format uses mboxrd from quoting.</dl>
<p> -m</p>
<dl>
<dt>
<dd> Same as the e option, but write .msg files also</dl>
<p> -o <i>output-directory</i></p>
<dl>
<dt>
<dd> Specifies the output directory. The directory must already exist, and is entered after the PST file is opened, but before any processing of files commences.</dl>
<p> -q</p>
<dl>
<dt>
<dd> Changes to silent mode. No feedback is printed to the screen, except for error messages.</dl>
<p> -r</p>
<dl>
<dt>
<dd> Changes the output format to Recursive. This will create folders as named in the PST file, and will put all emails in a file called &quot;mbox&quot; inside each folder. These files are then compatible with all mbox-compatible email clients. This format uses mboxrd from quoting.</dl>
<p> -t <i>output-type-codes</i></p>
<dl>
<dt>
<dd> Specifies the item types that are processed. The argument is a sequence of single letters from (e,a,j,c) for (email, appointment, journal, contact) types. The default is to process all item types.</dl>
<p> -u</p>
<dl>
<dt>
<dd> Sets Thunderbird mode, a submode of recursive mode. This causes two extra .type and .size meta files to be created. This format uses mboxrd from quoting.</dl>
<p> -w</p>
<dl>
<dt>
<dd> Overwrite any previous output files. Beware: When used with the -S switch, this will remove all files from the target folder before writing. This is to keep the count of emails and attachments correct.</dl>
<h2>FROM QUOTING</h2>
<p> Output formats that place each mail message in a separate file (-M, -S, -e, -m) don&#8217;t do any from quoting. Output formats that place multiple email messages in a single file (-k, -r, -u) now use mboxrd from quoting rules. If none of those switches are specified, the default output format uses mboxrd from quoting rules, since it produces multiple email messages in a single file. Earlier versions used mboxo from quoting rules for all output formats.</p>
<h2>AUTHOR</h2>
<p> This manual page was originally written by Dave Smith &lt;dave.s [at] earthcorp.com&gt;, and updated by Joe Nahmias &lt;joe [at] nahmias.net&gt; for the Debian GNU/Linux system (but may be used by others). It was subsequently updated by Brad Hards &lt;bradh [at] frogmouth.net&gt;, and converted to xml format by Carl Byington &lt;carl [at] five-ten-sg.com&gt;.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (C) 2002 by David Smith &lt;dave.s [at] earthcorp.com&gt;. XML version Copyright (C) 2008 by 510 Software Group &lt;carl [at] five-ten-sg.com&gt;. </p>
<p> This program is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 2, or (at your option) any later version. </p>
<p> You should have received a copy of the GNU General Public License along with this program; see the file COPYING. If not, please write to the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.</p>
<h2>VERSION</h2>
<p> 0.6.59 </p>
<h2>Index</h2>
