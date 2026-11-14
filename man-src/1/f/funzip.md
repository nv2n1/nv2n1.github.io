---
title: "funzip(1)"
name: "funzip"
section: "1"
letter: "f"
url: "/docs/linux/man/1-funzip/"
description: "funzip – filter for extracting from a ZIP archive in a pipe"
---

<h2 class="name">NAME</h2>
<p> funzip &#8211; filter for extracting from a ZIP archive in a pipe </p>
<h2>SYNOPSIS</h2>
<p> <code>funzip</code> [<code>-password</code>] [<i>input[.zip|.gz]</i>]</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>[<i>-password</i>]</p>
<dd> Optional password to be used if ZIP archive is encrypted. Decryption may not be supported at some sites. See DESCRIPTION for more details.</p>
<dt>[<i>input[.zip|.gz]</i>]</p>
<dd> Optional input archive file specification. See DESCRIPTION for details.</dl>
<h2>DESCRIPTION</h2>
<p> <i>funzip</i> without a file argument acts as a filter; that is, it assumes that a ZIP archive (or a <i>gzip</i>&#8216;<a href="/docs/linux/man/1-d/">d</a>(1) file) is being piped into standard input, and it extracts the first member from the archive to stdout. When stdin comes from a tty device, <i>funzip</i> assumes that this cannot be a stream of (binary) compressed data and shows a short help text, instead. If there is a file argument, then input is read from the specified file instead of from stdin. </p>
<p> A password for encrypted zip files can be specified on the command line (preceding the file name, if any) by prefixing the password with a dash. Note that this constitutes a security risk on many systems; currently running processes are often visible via simple commands (e.g., <i><a href="/docs/linux/man/1-ps/">ps</a></i>(1) under Unix), and command-line histories can be read. If the first entry of the zip file is encrypted and no password is specified on the command line, then the user is prompted for a password and the password is not echoed on the console. </p>
<p> Given the limitation on single-member extraction, <i>funzip</i> is most useful in conjunction with a secondary archiver program such as <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1). The following section includes an example illustrating this usage in the case of disk backups to tape.</p>
<h2>EXAMPLES</h2>
<p> To use <i>funzip</i> to extract the first member file of the archive test.zip and to pipe it into <i><a href="/docs/linux/man/1-more/">more</a></i>(1): </p>
<pre>
funzip test.zip | more
</pre>
<p> To use <i>funzip</i> to test the first member file of test.zip (any errors will be reported on standard error): </p>
<pre>
funzip test.zip &gt; /dev/null
</pre>
<p> To use <i>zip</i> and <i>funzip</i> in place of <i><a href="/docs/linux/man/1-compress/">compress</a></i>(1) and <i><a href="/docs/linux/man/1-zcat/">zcat</a></i>(1) (or <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1) and <i><a href="/docs/linux/man/1-gzcat/">gzcat</a></i>(1)) for tape backups: </p>
<pre>
tar cf - . | zip -7 | dd of=/dev/nrst0 obs=8k
dd if=/dev/nrst0 ibs=8k | funzip | tar xf -
</pre>
<p> (where, for example, nrst0 is a SCSI tape drive).</p>
<h2>BUGS</h2>
<p> When piping an encrypted file into <i>more</i> and allowing <i>funzip</i> to prompt for password, the terminal may sometimes be reset to a non-echo mode. This is apparently due to a race condition between the two programs; <i>funzip</i> changes the terminal mode to non-echo before <i>more</i> reads its state, and <i>more</i> then &#8220;restores&#8221; the terminal to this mode before exiting. To recover, run <i>funzip</i> on the same file but redirect to /dev/null rather than piping into more; after prompting again for the password, <i>funzip</i> will reset the terminal properly. </p>
<p> There is presently no way to extract any member but the first from a ZIP archive. This would be useful in the case where a ZIP archive is included within another archive. In the case where the first member is a directory, <i>funzip</i> simply creates the directory and exits. </p>
<p> The functionality of <i>funzip</i> should be incorporated into <i>unzip</i> itself (future release).</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1), <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1), <i><a href="/docs/linux/man/1-unzipsfx/">unzipsfx</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1), <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1), <i><a href="/docs/linux/man/1-zipnote/">zipnote</a></i>(1), <i><a href="/docs/linux/man/1-zipsplit/">zipsplit</a></i>(1)</p>
<h2>URL</h2>
<p> The Info-ZIP home page is currently at </p>
<pre>
<a rel="nofollow" href="http://www.info-zip.org/pub/infozip/">http://www.info-zip.org/pub/infozip/</a>
</pre>
<p> or </p>
<pre>
<a href="ftp://ftp.info-zip.org/pub/infozip/">ftp://ftp.info-zip.org/pub/infozip/</a> .
</pre>
<h2>AUTHOR</h2>
<p> Mark Adler (Info-ZIP) </p>
<h2>Index</h2>
