---
title: "unzipsfx(1)"
name: "unzipsfx"
section: "1"
letter: "u"
url: "/docs/linux/man/1-unzipsfx/"
description: "unzipsfx – self-extracting stub for prepending to ZIP archives"
---

<h2 class="name">NAME</h2>
<p> unzipsfx &#8211; self-extracting stub for prepending to ZIP archives </p>
<h2>SYNOPSIS</h2>
<p> <code>&lt;name of unzipsfx+archive combo&gt;</code> [<code>-cfptuz</code>[<code>ajnoqsCLV$</code>]] [<i>file(s)</i>&nbsp;&#8230; [<code>-x</code>&nbsp;<i>xfile(s)</i>&nbsp;&#8230;]]</p>
<h2>DESCRIPTION</h2>
<p> <i>unzipsfx</i> is a modified version of <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) designed to be prepended to existing ZIP archives in order to form self-extracting archives. Instead of taking its first non-flag argument to be the zipfile(s) to be extracted, <i>unzipsfx</i> seeks itself under the name by which it was invoked and tests or extracts the contents of the appended archive. Because the executable stub adds bulk to the archive (the whole purpose of which is to be as small as possible), a number of the less-vital capabilities in regular <i>unzip</i> have been removed. Among these are the usage (or help) screen, the listing and diagnostic functions (<code>-l</code> and <code>-v</code>), the ability to decompress older compression formats (the &#8220;reduce,&#8221; &#8220;shrink&#8221; and &#8220;implode&#8221; methods). The ability to extract to a directory other than the current one can be selected as a compile-time option, which is now enabled by default since UnZipSFX version 5.5. Similarly, decryption is supported as a compile-time option but should be avoided unless the attached archive contains encrypted files. Starting with release 5.5, another compile-time option adds a simple &#8220;run command after extraction&#8221; feature. This feature is currently incompatible with the &#8220;extract to different directory&#8221; feature and remains disabled by default. </p>
<p> <code>Note that self-extracting archives made with</code> <i>unzipsfx</i> <code>are no more (or less) portable across different operating systems than is the</code> <i>unzip</i> <code>executable itself.</code> In general a self-extracting archive made on a particular Unix system, for example, will only self-extract under the same flavor of Unix. Regular <i>unzip</i> may still be used to extract the embedded archive as with any normal zipfile, although it will generate a harmless warning about extra bytes at the beginning of the zipfile. <i>Despite this</i>, however, the self-extracting archive is technically <i>not</i> a valid ZIP archive, and PKUNZIP may be unable to test or extract it. This limitation is due to the simplistic manner in which the archive is created; the internal directory structure is not updated to reflect the extra bytes prepended to the original zipfile.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt>[<i>file(s)</i>]</p>
<dd> An optional list of archive members to be processed. Regular expressions (wildcards) similar to those in Unix <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) may be used to match multiple members. These wildcards may contain:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> matches a sequence of 0 or more characters</p>
<dt>?</p>
<dd> matches exactly 1 character</p>
<dt>[&#8230;]</p>
<dd> matches any single character found inside the brackets; ranges are specified by a beginning character, a hyphen, and an ending character. If an exclamation point or a caret (`!&#8217; or `^&#8217;) follows the left bracket, then the range of characters within the brackets is complemented (that is, anything <i>except</i> the characters inside the brackets is considered a match).</dl>
</dl>
<dt>
<dd> (Be sure to quote any character that might otherwise be interpreted or modified by the operating system, particularly under Unix and VMS.)</p>
<dt>[<code>-x</code>&nbsp;<i>xfile(s)</i>]</p>
<dd> An optional list of archive members to be excluded from processing. Since wildcard characters match directory separators (`/&#8217;), this option may be used to exclude any files that are in subdirectories. For example, &#8220;foosfx *.[ch] -x */*&#8221; would extract all C source files in the main directory, but none in any subdirectories. Without the <code>-x</code> option, all C source files in all directories within the zipfile would be extracted.</dl>
<p> If <i>unzipsfx</i> is compiled with SFX_EXDIR defined, the following option is also enabled:</p>
<dl>
<dt>[<code>-d</code>&nbsp;<i>exdir</i>]</p>
<dd> An optional directory to which to extract files. By default, all files and subdirectories are recreated in the current directory; the <code>-d</code> option allows extraction in an arbitrary directory (always assuming one has permission to write to the directory). The option and directory may be concatenated without any white space between them, but note that this may cause normal shell behavior to be suppressed. In particular, &#8220;-d&nbsp;~&#8221; (tilde) is expanded by Unix C shells into the name of the user&#8217;s home directory, but &#8220;-d~&#8221; is treated as a literal subdirectory &#8220;<code>~</code>&#8221; of the current directory.</dl>
<h2>OPTIONS</h2>
<p> <i>unzipsfx</i> supports the following <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) options: <code>-c</code> and <code>-p</code> (extract to standard output/screen), <code>-f</code> and <code>-u</code> (freshen and update existing files upon extraction), <code>-t</code> (test archive) and <code>-z</code> (print archive comment). All normal listing options (<code>-l</code>, <code>-v</code> and <code>-Z</code>) have been removed, but the testing option (<code>-t</code>) may be used as a &#8220;poor man&#8217;s&#8221; listing. Alternatively, those creating self-extracting archives may wish to include a short listing in the zipfile comment. </p>
<p> See <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) for a more complete description of these options.</p>
<h2>MODIFIERS</h2>
<p> <i>unzipsfx</i> currently supports all <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) modifiers: <code>-a</code> (convert text files), <code>-n</code> (never overwrite), <code>-o</code> (overwrite without prompting), <code>-q</code> (operate quietly), <code>-C</code> (match names case-insensitively), <code>-L</code> (convert uppercase-OS names to lowercase), <code>-j</code> (junk paths) and <code>-V</code> (retain version numbers); plus the following operating-system specific options: <code>-X</code> (restore VMS owner/protection info), <code>-s</code> (convert spaces in filenames to underscores [DOS, OS/2, NT]) and <code>-$</code> (restore volume label [DOS, OS/2, NT, Amiga]). </p>
<p> (Support for regular ASCII text-conversion may be removed in future versions, since it is simple enough for the archive&#8217;s creator to ensure that text files have the appropriate format for the local OS. EBCDIC conversion will of course continue to be supported since the zipfile format implies ASCII storage of text files.) </p>
<p> See <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) for a more complete description of these modifiers.</p>
<h2>ENVIRONMENT OPTIONS</h2>
<p> <i>unzipsfx</i> uses the same environment variables as <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) does, although this is likely to be an issue only for the person creating and testing the self-extracting archive. See <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) for details.</p>
<h2>DECRYPTION</h2>
<p> Decryption is supported exactly as in <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1); that is, interactively with a non-echoing prompt for the password(s). See <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) for details. Once again, note that if the archive has no encrypted files there is no reason to use a version of <i>unzipsfx</i> with decryption support; that only adds to the size of the archive.</p>
<h2>AUTORUN COMMAND</h2>
<p> When <i>unzipsfx</i> was compiled with CHEAP_SFX_AUTORUN defined, a simple &#8220;command autorun&#8221; feature is supported. You may enter a command into the Zip archive comment, using the following format: </p>
<pre>
$AUTORUN$&gt;[command line string]
</pre>
<p> When <i>unzipsfx</i> recognizes the &#8220;$AUTORUN$&gt;&#8221; token at the beginning of the Zip archive comment, the remainder of the first line of the comment (until the first newline character) is passed as a shell command to the operating system using the C rtl &#8220;system&#8221; function. Before executing the command, <i>unzipsfx</i> displays the command on the console and prompts the user for confirmation. When the user has switched off prompting by specifying the <code>-q</code> option, autorun commands are never executed. </p>
<p> In case the archive comment contains additional lines of text, the remainder of the archive comment following the first line is displayed normally, unless quiet operation was requested by supplying a <code>-q</code> option.</p>
<h2>EXAMPLES</h2>
<p> To create a self-extracting archive <i>letters</i> from a regular zipfile <i>letters.zip</i> and change the new archive&#8217;s permissions to be world-executable under Unix: </p>
<pre>
cat unzipsfx letters.zip &gt; letters
chmod 755 letters
zip -A letters
</pre>
<p> To create the same archive under MS-DOS, OS/2 or NT (note the use of the <code>/b</code> [binary] option to the <i>copy</i> command): </p>
<pre>
copy /b unzipsfx.exe+letters.zip letters.exe
zip -A letters.exe
</pre>
<p> Under VMS: </p>
<pre>
copy unzipsfx.exe,letters.zip letters.exe
letters == &quot;$currentdisk:[currentdir]letters.exe&quot;
zip -A letters.exe
</pre>
<p> (The VMS <i>append</i> command may also be used. The second command installs the new program as a &#8220;foreign command&#8221; capable of taking arguments. The third line assumes that Zip is already installed as a foreign command.) Under AmigaDOS: </p>
<pre>
MakeSFX letters letters.zip UnZipSFX
</pre>
<p> (MakeSFX is included with the UnZip source distribution and with Amiga binary distributions. &#8220;zip -A&#8221; doesn&#8217;t work on Amiga self-extracting archives.) To test (or list) the newly created self-extracting archive: </p>
<pre>
letters -t
</pre>
<p> To test <i>letters</i> quietly, printing only a summary message indicating whether the archive is OK or not: </p>
<pre>
letters -tqq
</pre>
<p> To extract the complete contents into the current directory, recreating all files and subdirectories as necessary: </p>
<pre>
letters
</pre>
<p> To extract all *.txt files (in Unix quote the `*&#8217;): </p>
<pre>
letters *.txt
</pre>
<p> To extract everything <i>except</i> the *.txt files: </p>
<pre>
letters -x *.txt
</pre>
<p> To extract only the README file to standard output (the screen): </p>
<pre>
letters -c README
</pre>
<p> To print only the zipfile comment: </p>
<pre>
letters -z
</pre>
<h2>LIMITATIONS</h2>
<p> The principle and fundamental limitation of <i>unzipsfx</i> is that it is not portable across architectures or operating systems, and therefore neither are the resulting archives. For some architectures there is limited portability, however (e.g., between some flavors of Intel-based Unix). </p>
<p> Another problem with the current implementation is that any archive with &#8220;junk&#8221; prepended to the beginning technically is no longer a zipfile (unless <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1) is used to adjust the zipfile offsets appropriately, as noted above). <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) takes note of the prepended bytes and ignores them since some file-transfer protocols, notably MacBinary, are also known to prepend junk. But PKWARE&#8217;s archiver suite may not be able to deal with the modified archive unless its offsets have been adjusted. </p>
<p> <i>unzipsfx</i> has no knowledge of the user&#8217;s PATH, so in general an archive must either be in the current directory when it is invoked, or else a full or relative path must be given. If a user attempts to extract the archive from a directory in the PATH other than the current one, <i>unzipsfx</i> will print a warning to the effect, &#8220;can&#8217;t find myself.&#8221; This is always true under Unix and may be true in some cases under MS-DOS, depending on the compiler used (Microsoft C fully qualifies the program name, but other compilers may not). Under OS/2 and NT there are operating-system calls available that provide the full path name, so the archive may be invoked from anywhere in the user&#8217;s path. The situation is not known for AmigaDOS, Atari TOS, MacOS, etc. </p>
<p> As noted above, a number of the normal <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) functions have been removed in order to make <i>unzipsfx</i> smaller: usage and diagnostic info, listing functions and extraction to other directories. Also, only stored and deflated files are supported. The latter limitation is mainly relevant to those who create SFX archives, however. </p>
<p> VMS users must know how to set up self-extracting archives as foreign commands in order to use any of <i>unzipsfx</i>&#8216;s options. This is not necessary for simple extraction, but the command to do so then becomes, e.g., &#8220;run letters&#8221; (to continue the examples given above). </p>
<p> <i>unzipsfx</i> on the Amiga requires the use of a special program, MakeSFX, in order to create working self-extracting archives; simple concatenation does not work. (For technically oriented users, the attached archive is defined as a &#8220;debug hunk.&#8221;) There may be compatibility problems between the ROM levels of older Amigas and newer ones. </p>
<p> All current bugs in <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) exist in <i>unzipsfx</i> as well.</p>
<h2>DIAGNOSTICS</h2>
<p> <i>unzipsfx</i>&#8216;s exit status (error level) is identical to that of <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1); see the corresponding man page.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-funzip/">funzip</a></i>(1), <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1), <i><a href="/docs/linux/man/1-zipgrep/">zipgrep</a></i>(1), <i><a href="/docs/linux/man/1-zipinfo/">zipinfo</a></i>(1), <i><a href="/docs/linux/man/1-zipnote/">zipnote</a></i>(1), <i><a href="/docs/linux/man/1-zipsplit/">zipsplit</a></i>(1)</p>
<h2>URL</h2>
<p> The Info-ZIP home page is currently at </p>
<pre>
<a rel="nofollow" href="http://www.info-zip.org/pub/infozip/">http://www.info-zip.org/pub/infozip/</a>
</pre>
<p> or </p>
<pre>
<a href="ftp://ftp.info-zip.org/pub/infozip/">ftp://ftp.info-zip.org/pub/infozip/</a> .
</pre>
<h2>AUTHORS</h2>
<p> Greg Roelofs was responsible for the basic modifications to UnZip necessary to create UnZipSFX. See <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1) for the current list of Zip-Bugs authors, or the file CONTRIBS in the UnZip source distribution for the full list of Info-ZIP contributors. </p>
<h2>Index</h2>
