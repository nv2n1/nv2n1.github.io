---
title: "file(1)"
name: "file"
section: "1"
letter: "f"
url: "/docs/linux/man/1-file/"
description: "file – determine file type"
---

<h2 class="name">NAME</h2>
<p> <code>file</code> &#8211; determine file type </p>
<h2>SYNOPSIS</h2>
<p> <code>file</code> [-<code>bcdEhiklLNnprsSvzZ0</code> ] [-<code>-apple</code> ] [-<code>-exclude-quiet</code> ] [-<code>-extension</code> ] [-<code>-mime-encoding</code> ] [-<code>-mime-type</code> ] [-<code>e </code><i>testname</i> ] [-<code>F </code><i>separator</i> ] [-<code>f </code><i>namefile</i> ] [-<code>m </code><i>magicfiles</i> ] [-<code>P </code><i>name=value</i> ] <i>file &#8230;</i><br />
<code>file</code> &#8211;<code>C</code> [-<code>m </code><i>magicfiles</i> ]<br />
<code>file</code> [-<code>-help</code> ]</p>
<h2>DESCRIPTION</h2>
<p> This manual page documents version 5.41 of the <code>file</code> command. </p>
<p> <code>file</code> tests each argument in an attempt to classify it. There are three sets of tests, performed in this order: filesystem tests, magic tests, and language tests. The <i>first</i> test that succeeds causes the file type to be printed. </p>
<p> The type printed will usually contain one of the words <i>text</i> (the file contains only printing characters and a few common control characters and is probably safe to read on an <code>ASCII</code> terminal), <i>executable</i> (the file contains the result of compiling a program in a form understandable to some <code>UNIX</code> kernel or another), or <i>data</i> meaning anything else (data is usually &#8220;binary&#8221; or non-printable). Exceptions are well-known file formats (core files, tar archives) that are known to contain binary data. When modifying magic files or the program itself, make sure to <i>preserve these keywords</i> Users depend on knowing that all the readable files in a directory have the word &#8220;text&#8221; printed. Don&#8217;t do as Berkeley did and change &#8220;shell commands text&#8221; to &#8220;shell script&#8221; </p>
<p> The filesystem tests are based on examining the return from a <a href="/docs/linux/man/2-stat/">stat</a>(2) system call. The program checks to see if the file is empty, or if it&#8217;s some sort of special file. Any known file types appropriate to the system you are running on (sockets, symbolic links, or named pipes (FIFOs) on those systems that implement them) are intuited if they are defined in the system header file In sys/stat.h . </p>
<p> The magic tests are used to check for files with data in particular fixed formats. The canonical example of this is a binary executable (compiled program) <code>a.out</code> file, whose format is defined in In elf.h , In a.out.h and possibly In exec.h in the standard include directory. These files have a &#8220;magic number&#8221; stored in a particular place near the beginning of the file that tells the <code>UNIX</code> operating system that the file is a binary executable, and which of several types thereof. The concept of a &#8220;magic number&#8221; has been applied by extension to data files. Any file with some invariant identifier at a small fixed offset into the file can usually be described in this way. The information identifying these files is read from /etc/magic and the compiled magic file /usr/share/misc/magic.mgc or the files in the directory /usr/share/misc/magic if the compiled file does not exist. In addition, if $HOME/.magic.mgc or $HOME/.magic exists, it will be used in preference to the system magic files. </p>
<p> If a file does not match any of the entries in the magic file, it is examined to see if it seems to be a text file. ASCII, ISO-8859-x, non-ISO 8-bit extended-ASCII character sets (such as those used on Macintosh and IBM PC systems), UTF-8-encoded Unicode, UTF-16-encoded Unicode, and EBCDIC character sets can be distinguished by the different ranges and sequences of bytes that constitute printable text in each set. If a file passes any of these tests, its character set is reported. ASCII, ISO-8859-x, UTF-8, and extended-ASCII files are identified as &#8220;text&#8221; because they will be mostly readable on nearly any terminal; UTF-16 and EBCDIC are only &#8220;character data&#8221; because, while they contain text, it is text that will require translation before it can be read. In addition, <code>file</code> will attempt to determine other characteristics of text-type files. If the lines of a file are terminated by CR, CRLF, or NEL, instead of the Unix-standard LF, this will be reported. Files that contain embedded escape sequences or overstriking will also be identified. </p>
<p> Once <code>file</code> has determined the character set used in a text-type file, it will attempt to determine in what language the file is written. The language tests look for particular strings (cf. In names.h ) that can appear anywhere in the first few blocks of a file. For example, the keyword <i>.br</i> indicates that the file is most likely a <a href="/docs/linux/man/1-troff/">troff</a>(1) input file, just as the keyword <i>struct</i> indicates a C program. These tests are less reliable than the previous two groups, so they are performed last. The language test routines also test for some miscellany (such as <a href="/docs/linux/man/1-tar/">tar</a>(1) archives, JSON files). </p>
<p> Any file that cannot be identified as having been written in any of the character sets listed above is simply said to be &#8220;data&#8221;</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;apple</code></dt>
<dd> Causes the <code>file</code> command to output the file type and creator code as used by older MacOS versions. The code consists of eight letters, the first describing the file type, the latter the creator. This option works properly only for file formats that have the apple-style output defined.</dd>
<dt><code>-b , &#8211;brief</code></dt>
<dd> Do not prepend filenames to output lines (brief mode).</dd>
<dt><code>-C , &#8211;compile</code></dt>
<dd> Write a magic.mgc output file that contains a pre-parsed version of the magic file or directory.</dd>
<dt><code>-c , &#8211;checking-printout</code></dt>
<dd> Cause a checking printout of the parsed form of the magic file. This is usually used in conjunction with the &#8211;<code>m</code> option to debug a new magic file before installing it.</dd>
<dt><code>-d</code></dt>
<dd> Prints internal debugging information to stderr.</dd>
<dt><code>-E</code></dt>
<dd> On filesystem errors (file not found etc), instead of handling the error as regular output as POSIX mandates and keep going, issue an error message and exit.</dd>
<dt><code>-e , &#8211;exclude </code><i>testname</i></dt>
<dd> Exclude the test named in <i>testname</i> from the list of tests made to determine the file type. Valid test names are:</dd>
<dl>
<dt><code>apptype</code></dt>
<dd> <code>EMX</code> application type (only on EMX).</dd>
<dt><code>ascii</code></dt>
<dd> Various types of text files (this test will try to guess the text encoding, irrespective of the setting of the `encoding&#8217; option).</dd>
<dt><code>encoding</code></dt>
<dd> Different text encodings for soft magic tests.</dd>
<dt><code>tokens</code></dt>
<dd> Ignored for backwards compatibility.</dd>
<dt><code>cdf</code></dt>
<dd> Prints details of Compound Document Files.</dd>
<dt><code>compress</code></dt>
<dd> Checks for, and looks inside, compressed files.</dd>
<dt><code>csv</code></dt>
<dd> Checks Comma Separated Value files.</dd>
<dt><code>elf</code></dt>
<dd> Prints ELF file details, provided soft magic tests are enabled and the elf magic is found.</dd>
<dt><code>json</code></dt>
<dd> Examines JSON (RFC-7159) files by parsing them for compliance.</dd>
<dt><code>soft</code></dt>
<dd> Consults magic files.</dd>
<dt><code>tar</code></dt>
<dd> Examines tar files by verifying the checksum of the 512 byte tar header. Excluding this test can provide more detailed content description by using the soft magic method.</dd>
<dt><code>text</code></dt>
<dd> A synonym for `ascii&#8217;</dd></dl>
<dt><code>&#8211;exclude-quiet</code></dt>
<dd> Like &#8211;<code>-exclude</code> but ignore tests that <code>file</code> does not know about. This is intended for compatibility with older versions of <code>file.</code></dd>
<dt><code>&#8211;extension</code></dt>
<dd> Print a slash-separated list of valid extensions for the file type found.</dd>
<dt><code>-F , &#8211;separator </code><i>separator</i></dt>
<dd> Use the specified string as the separator between the filename and the file result returned. Defaults to `:&#8217;</dd>
<dt><code>-f , &#8211;files-from </code><i>namefile</i></dt>
<dd> Read the names of the files to be examined from <i>namefile</i> (one per line) before the argument list. Either <i>namefile</i> or at least one filename argument must be present; to test the standard input, use `-&#8216; as a filename argument. Please note that <i>namefile</i> is unwrapped and the enclosed filenames are processed when this option is encountered and before any further options processing is done. This allows one to process multiple lists of files with different command line arguments on the same <code>file</code> invocation. Thus if you want to set the delimiter, you need to do it before you specify the list of files, like: &#8220;-<code>F </code><i>@ &#8211;</i><code>f </code><i>namefile</i> &#8221; instead of: &#8220;-<code>f </code><i>namefile &#8211;</i><code>F </code><i>file &#8230;</i> &#8221;</dd>
<dt><code>-h , &#8211;no-dereference</code></dt>
<dd> This option causes symlinks not to be followed (on systems that support symbolic links). This is the default if the environment variable <code>POSIXLY_CORRECT</code> is not defined.</dd>
<dt><code>-i , &#8211;mime</code></dt>
<dd> Causes the <code>file</code> command to output mime type strings rather than the more traditional human readable ones. Thus it may say `text/plain; charset=us-ascii&#8217; rather than &#8220;ASCII text&#8221;</dd>
<dt><code>&#8211;mime-type , &#8211;mime-encoding</code></dt>
<dd> Like &#8211;<code>i</code> but print only the specified element(s).</dd>
<dt><code>-k , &#8211;keep-going</code></dt>
<dd> Don&#8217;t stop at the first match, keep going. Subsequent matches will be have the string `
- &#8216; prepended. (If you want a newline, see the &#8211;<code>r</code> option.) The magic pattern with the highest strength (see the &#8211;<code>l</code> option) comes first.</dd>
<dt><code>-l , &#8211;list</code></dt>
<dd> Shows a list of patterns and their strength sorted descending by <a href="/docs/linux/man/5-magic/">magic</a>(5) strength which is used for the matching (see also the &#8211;<code>k</code> option).</dd>
<dt><code>-L , &#8211;dereference</code></dt>
<dd> This option causes symlinks to be followed, as the like-named option in <a href="/docs/linux/man/1-ls/">ls</a>(1) (on systems that support symbolic links). This is the default if the environment variable <code>POSIXLY_CORRECT</code> is defined.</dd>
<dt><code>-m , &#8211;magic-file </code><i>magicfiles</i></dt>
<dd> Specify an alternate list of files and directories containing magic. This can be a single item, or a colon-separated list. If a compiled magic file is found alongside a file or directory, it will be used instead.</dd>
<dt><code>-N , &#8211;no-pad</code></dt>
<dd> Don&#8217;t pad filenames so that they align in the output.</dd>
<dt><code>-n , &#8211;no-buffer</code></dt>
<dd> Force stdout to be flushed after checking each file. This is only useful if checking a list of files. It is intended to be used by programs that want filetype output from a pipe.</dd>
<dt><code>-p , &#8211;preserve-date</code></dt>
<dd> On systems that support utime(3) or <a href="/docs/linux/man/2-utimes/">utimes</a>(2), attempt to preserve the access time of files analyzed, to pretend that <code>file</code> never read them.</dd>
<dt><code>-P , &#8211;parameter </code><i>name=value</i></dt>
<dd> Set various parameter limits.</dd>
<dl>
<dt><code>Name Ta </code><code>Default Ta </code><code>Explanation</code></dt>
<dd>
</dd><dt><code>bytes Ta </code>1048576 Ta max number of bytes to read from file</dt>
<dd>
</dd><dt><code>elf_notes Ta </code>256 Ta max ELF notes processed</dt>
<dd>
</dd><dt><code>elf_phnum Ta </code>2048 Ta max ELF program sections processed</dt>
<dd>
</dd><dt><code>elf_shnum Ta </code>32768 Ta max ELF sections processed</dt>
<dd>
</dd><dt><code>encoding Ta </code>65536 Ta max number of bytes to scan for encoding evaluation</dt>
<dd>
</dd><dt><code>indir Ta </code>50 Ta recursion limit for indirect magic</dt>
<dd>
</dd><dt><code>name Ta </code>50 Ta use count limit for name/use magic</dt>
<dd>
</dd><dt><code>regex Ta </code>8192 Ta length limit for regex searches</dt>
<dd></dd></dl>
<dt><code>-r , &#8211;raw</code></dt>
<dd> Don&#8217;t translate unprintable characters to \ooo. Normally <code>file</code> translates unprintable characters to their octal representation.</dd>
<dt><code>-s , &#8211;special-files</code></dt>
<dd> Normally, <code>file</code> only attempts to read and determine the type of argument files which <a href="/docs/linux/man/2-stat/">stat</a>(2) reports are ordinary files. This prevents problems, because reading special files may have peculiar consequences. Specifying the &#8211;<code>s</code> option causes <code>file</code> to also read argument files which are block or character special files. This is useful for determining the filesystem types of the data in raw disk partitions, which are block special files. This option also causes <code>file</code> to disregard the file size as reported by <a href="/docs/linux/man/2-stat/">stat</a>(2) since on some systems it reports a zero size for raw disk partitions.</dd>
<dt><code>-S , &#8211;no-sandbox</code></dt>
<dd> On systems where libseccomp ( <a rel="nofollow" href="https://github.com/seccomp/libseccomp">https://github.com/seccomp/libseccomp</a> is available, the &#8211;<code>S</code> option disables sandboxing which is enabled by default. This option is needed for <code>file</code> to execute external decompressing programs, i.e. when the &#8211;<code>z</code> option is specified and the built-in decompressors are not available. On systems where sandboxing is not available, this option has no effect. </dd>
<p> <i>Note:</i> This Debian version of file was built without seccomp support, so this option has no effect.</p>
<dt><code>-v , &#8211;version</code></dt>
<dd> Print the version of the program and exit.</dd>
<dt><code>-z , &#8211;uncompress</code></dt>
<dd> Try to look inside compressed files.</dd>
<dt><code>-Z , &#8211;uncompress-noreport</code></dt>
<dd> Try to look inside compressed files, but report information about the contents only not the compression.</dd>
<dt><code>-0 , &#8211;print0</code></dt>
<dd> Output a null character `
</dd></dl>