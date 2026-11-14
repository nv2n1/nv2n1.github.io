---
title: "zipinfo(1)"
name: "zipinfo"
section: "1"
letter: "z"
url: "/docs/linux/man/1-zipinfo/"
description: "zipinfo – list detailed information about a ZIP archive"
---

<h2 class="name">NAME</h2>
<p> zipinfo &#8211; list detailed information about a ZIP archive </p>
<h2>SYNOPSIS</h2>
<p> <code>zipinfo</code> [<code>-12smlvhMtTz</code>] <i>file</i>[<i>.zip</i>] [<i>file(s)</i>&nbsp;&#8230;] [<code>-x</code>&nbsp;<i>xfile(s)</i>&nbsp;&#8230;] </p>
<p> <code>unzip</code> <code>-Z</code> [<code>-12smlvhMtTz</code>] <i>file</i>[<i>.zip</i>] [<i>file(s)</i>&nbsp;&#8230;] [<code>-x</code>&nbsp;<i>xfile(s)</i>&nbsp;&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <i>zipinfo</i> lists technical information about files in a ZIP archive, most commonly found on MS-DOS systems. Such information includes file access permissions, encryption status, type of compression, version and operating system or file system of compressing program, and the like. The default behavior (with no options) is to list single-line entries for each file in the archive, with header and trailer lines providing summary information for the entire archive. The format is a cross between Unix &#8220;ls -l&#8221; and &#8220;unzip -v&#8221; output. See <code>DETAILED DESCRIPTION</code> below. Note that <i>zipinfo</i> is the same program as <i>unzip</i> (under Unix, a link to it); on some systems, however, <i>zipinfo</i> support may have been omitted when <i>unzip</i> was compiled.</p>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>file</i>[<i>.zip</i>]</p>
<dd> Path of the ZIP archive(s). If the file specification is a wildcard, each matching file is processed in an order determined by the operating system (or file system). Only the filename can be a wildcard; the path itself cannot. Wildcard expressions are similar to Unix <i><a href="/docs/linux/man/1-egrep/">egrep</a></i>(1) (regular) expressions and may contain:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> matches a sequence of 0 or more characters</p>
<dt>?</p>
<dd> matches exactly 1 character</p>
<dt>[&#8230;]</p>
<dd> matches any single character found inside the brackets; ranges are specified by a beginning character, a hyphen, and an ending character. If an exclamation point or a caret (`!&#8217; or `^&#8217;) follows the left bracket, then the range of characters within the brackets is complemented (that is, anything <i>except</i> the characters inside the brackets is considered a match). To specify a verbatim left bracket, the three-character sequence &#8220;[[]&#8221; has to be used.</dl>
</dl>
<dt>
<dd> (Be sure to quote any character that might otherwise be interpreted or modified by the operating system, particularly under Unix and VMS.) If no matches are found, the specification is assumed to be a literal filename; and if that also fails, the suffix .zip is appended. Note that self-extracting ZIP files are supported, as with any other ZIP archive; just specify the .exe suffix (if any) explicitly.</p>
<dt>[<i>file(s)</i>]</p>
<dd> An optional list of archive members to be processed, separated by spaces. (VMS versions compiled with VMSCLI defined must delimit files with commas instead.) Regular expressions (wildcards) may be used to match multiple members; see above. Again, be sure to quote expressions that would otherwise be expanded or modified by the operating system.</p>
<dt>[<code>-x</code>&nbsp;<i>xfile(s)</i>]</p>
<dd> An optional list of archive members to be excluded from processing.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-1</code></p>
<dd> list filenames only, one per line. This option excludes all others; headers, trailers and zipfile comments are never printed. It is intended for use in Unix shell scripts.</p>
<dt><code>-2</code></p>
<dd> list filenames only, one per line, but allow headers (<code>-h</code>), trailers (<code>-t</code>) and zipfile comments (<code>-z</code>), as well. This option may be useful in cases where the stored filenames are particularly long.</p>
<dt><code>-s</code></p>
<dd> list zipfile info in short Unix &#8220;ls -l&#8221; format. This is the default behavior; see below.</p>
<dt><code>-m</code></p>
<dd> list zipfile info in medium Unix &#8220;ls -l&#8221; format. Identical to the <code>-s</code> output, except that the compression factor, expressed as a percentage, is also listed.</p>
<dt><code>-l</code></p>
<dd> list zipfile info in long Unix &#8220;ls -l&#8221; format. As with <code>-m</code> except that the compressed size (in bytes) is printed instead of the compression ratio.</p>
<dt><code>-v</code></p>
<dd> list zipfile information in verbose, multi-page format.</p>
<dt><code>-h</code></p>
<dd> list header line. The archive name, actual size (in bytes) and total number of files is printed.</p>
<dt><code>-M</code></p>
<dd> pipe all output through an internal pager similar to the Unix <i><a href="/docs/linux/man/1-more/">more</a></i>(1) command. At the end of a screenful of output, <i>zipinfo</i> pauses with a &#8220;&#8211;More&#8211;&#8221; prompt; the next screenful may be viewed by pressing the Enter (Return) key or the space bar. <i>zipinfo</i> can be terminated by pressing the &#8220;q&#8221; key and, on some systems, the Enter/Return key. Unlike Unix <i><a href="/docs/linux/man/1-more/">more</a></i>(1), there is no forward-searching or editing capability. Also, <i>zipinfo</i> doesn&#8217;t notice if long lines wrap at the edge of the screen, effectively resulting in the printing of two or more lines and the likelihood that some text will scroll off the top of the screen before being viewed. On some systems the number of available lines on the screen is not detected, in which case <i>zipinfo</i> assumes the height is 24 lines.</p>
<dt><code>-t</code></p>
<dd> list totals for files listed or for all files. The number of files listed, their uncompressed and compressed total sizes , and their overall compression factor is printed; or, if only the totals line is being printed, the values for the entire archive are given. The compressed total size does not include the 12 additional header bytes of each encrypted entry. Note that the total compressed (data) size will never match the actual zipfile size, since the latter includes all of the internal zipfile headers in addition to the compressed data.</p>
<dt><code>-T</code></p>
<dd> print the file dates and times in a sortable decimal format (yymmdd.hhmmss). The default date format is a more standard, human-readable version with abbreviated month names (see examples below).</p>
<dt><code>-U</code></p>
<dd> [UNICODE_SUPPORT only] modify or disable UTF-8 handling. When UNICODE_SUPPORT is available, the option <code>-U</code> forces <i>unzip</i> to escape all non-ASCII characters from UTF-8 coded filenames as &#8220;#Uxxxx&#8221;. This option is mainly provided for debugging purpose when the fairly new UTF-8 support is suspected to mangle up extracted filenames.</p>
<dt>
<dd> The option <code>-UU</code> allows to entirely disable the recognition of UTF-8 encoded filenames. The handling of filename codings within <i>unzip</i> falls back to the behaviour of previous versions.</p>
<dt><code>-z</code></p>
<dd> include the archive comment (if any) in the listing.</dl>
<h2>DETAILED DESCRIPTION</h2>
<p> <i>zipinfo</i> has a number of modes, and its behavior can be rather difficult to fathom if one isn&#8217;t familiar with Unix <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1) (or even if one is). The default behavior is to list files in the following format: </p>
<p> The last three fields are the modification date and time of the file, and its name. The case of the filename is respected; thus files that come from MS-DOS PKZIP are always capitalized. If the file was zipped with a stored directory name, that is also displayed as part of the filename. </p>
<p> The second and third fields indicate that the file was zipped under Unix with version 1.9 of <i>zip</i>. Since it comes from Unix, the file permissions at the beginning of the line are printed in Unix format. The uncompressed file-size (2802 in this example) is the fourth field. </p>
<p> The fifth field consists of two characters, either of which may take on several values. The first character may be either `t&#8217; or `b&#8217;, indicating that <i>zip</i> believes the file to be text or binary, respectively; but if the file is encrypted, <i>zipinfo</i> notes this fact by capitalizing the character (`T&#8217; or `B&#8217;). The second character may also take on four values, depending on whether there is an extended local header and/or an &#8220;extra field&#8221; associated with the file (fully explained in PKWare&#8217;s APPNOTE.TXT, but basically analogous to pragmas in ANSI C&#8211;i.e., they provide a standard way to include non-standard information in the archive). If neither exists, the character will be a hyphen (`-&#8216;); if there is an extended local header but no extra field, `l&#8217;; if the reverse, `x&#8217;; and if both exist, `X&#8217;. Thus the file in this example is (probably) a text file, is not encrypted, and has neither an extra field nor an extended local header associated with it. The example below, on the other hand, is an encrypted binary file with an extra field: </p>
<p> Extra fields are used for various purposes (see discussion of the <code>-v</code> option below) including the storage of VMS file attributes, which is presumably the case here. Note that the file attributes are listed in VMS format. Some other possibilities for the host operating system (which is actually a misnomer&#8211;host file system is more correct) include OS/2 or NT with High Performance File System (HPFS), MS-DOS, OS/2 or NT with File Allocation Table (FAT) file system, and Macintosh. These are denoted as follows: </p>
<p> File attributes in the first two cases are indicated in a Unix-like format, where the seven subfields indicate whether the file: (1) is a directory, (2) is readable (always true), (3) is writable, (4) is executable (guessed on the basis of the extension&#8211;<i>.exe</i>, <i>.com</i>, <i>.bat</i>, <i>.cmd</i> and <i>.btm</i> files are assumed to be so), (5) has its archive bit set, (6) is hidden, and (7) is a system file. Interpretation of Macintosh file attributes is unreliable because some Macintosh archivers don&#8217;t store any attributes in the archive. </p>
<p> Finally, the sixth field indicates the compression method and possible sub-method used. There are six methods known at present: storing (no compression), reducing, shrinking, imploding, tokenizing (never publicly released), and deflating. In addition, there are four levels of reducing (1 through 4); four types of imploding (4K or 8K sliding dictionary, and 2 or 3 Shannon-Fano trees); and four levels of deflating (superfast, fast, normal, maximum compression). <i>zipinfo</i> represents these methods and their sub-methods as follows: <i>stor</i>; <i>re:1</i>, <i>re:2</i>, etc.; <i>shrk</i>; <i>i4:2</i>, <i>i8:3</i>, etc.; <i>tokn</i>; and <i>defS</i>, <i>defF</i>, <i>defN</i>, and <i>defX</i>. </p>
<p> The medium and long listings are almost identical to the short format except that they add information on the file&#8217;s compression. The medium format lists the file&#8217;s compression factor as a percentage indicating the amount of space that has been &#8220;removed&#8221;: </p>
<p> In this example, the file has been compressed by more than a factor of five; the compressed data are only 19% of the original size. The long format gives the compressed file&#8217;s size in bytes, instead: </p>
<p> In contrast to the <i>unzip</i> listings, the compressed size figures in this listing format denote the complete size of compressed data, including the 12 extra header bytes in case of encrypted entries. </p>
<p> Adding the <code>-T</code> option changes the file date and time to decimal format: </p>
<p> Note that because of limitations in the MS-DOS format used to store file times, the seconds field is always rounded to the nearest even second. For Unix files this is expected to change in the next major releases of <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1) and <i>unzip</i>. </p>
<p> In addition to individual file information, a default zipfile listing also includes header and trailer lines: </p>
<p> The header line gives the name of the archive, its total size, and the total number of files; the trailer gives the number of files listed, their total uncompressed size, and their total compressed size (not including any of <i>zip</i>&#8216;s internal overhead). If, however, one or more <i>file(s)</i> are provided, the header and trailer lines are not listed. This behavior is also similar to that of Unix&#8217;s &#8220;ls -l&#8221;; it may be overridden by specifying the <code>-h</code> and <code>-t</code> options explicitly. In such a case the listing format must also be specified explicitly, since <code>-h</code> or <code>-t</code> (or both) in the absence of other options implies that ONLY the header or trailer line (or both) is listed. See the <code>EXAMPLES</code> section below for a semi-intelligible translation of this nonsense. </p>
<p> The verbose listing is mostly self-explanatory. It also lists file comments and the zipfile comment, if any, and the type and number of bytes in any stored extra fields. Currently known types of extra fields include PKWARE&#8217;s authentication (&#8220;AV&#8221;) info; OS/2 extended attributes; VMS filesystem info, both PKWARE and Info-ZIP versions; Macintosh resource forks; Acorn/Archimedes SparkFS info; and so on. (Note that in the case of OS/2 extended attributes&#8211;perhaps the most common use of zipfile extra fields&#8211;the size of the stored EAs as reported by <i>zipinfo</i> may not match the number given by OS/2&#8217;s <i>dir</i> command: OS/2 always reports the number of bytes required in 16-bit format, whereas <i>zipinfo</i> always reports the 32-bit storage.) </p>
<p> Again, the compressed size figures of the individual entries include the 12 extra header bytes for encrypted entries. In contrast, the archive total compressed size and the average compression ratio shown in the summary bottom line are calculated <code>without</code> the extra 12 header bytes of encrypted entries.</p>
<h2>ENVIRONMENT OPTIONS</h2>
<p> Modifying <i>zipinfo</i>&#8216;s default behavior via options placed in an environment variable can be a bit complicated to explain, due to <i>zipinfo</i>&#8216;s attempts to handle various defaults in an intuitive, yet Unix-like, manner. (Try not to laugh.) Nevertheless, there is some underlying logic. In brief, there are three &#8220;priority levels&#8221; of options: the default options; environment options, which can override or add to the defaults; and explicit options given by the user, which can override or add to either of the above. </p>
<p> The default listing format, as noted above, corresponds roughly to the &quot;zipinfo -hst&quot; command (except when individual zipfile members are specified). A user who prefers the long-listing format (<code>-l</code>) can make use of the <i>zipinfo</i>&#8216;s environment variable to change this default:</p>
<dl>
<dt>Unix Bourne shell:</p>
<dd> <tt>ZIPINFO=-l; export ZIPINFO</tt></p>
<dt>Unix C shell:</p>
<dd> <tt>setenv ZIPINFO -l</tt></p>
<dt>OS/2 or MS-DOS:</p>
<dd> <tt>set ZIPINFO=-l</tt></p>
<dt>VMS (quotes for <i>lowercase</i>):</p>
<dd> <tt>define ZIPINFO_OPTS &quot;-l&quot;</tt></dl>
<p> If, in addition, the user dislikes the trailer line, <i>zipinfo</i>&#8216;s concept of &#8220;negative options&#8221; may be used to override the default inclusion of the line. This is accomplished by preceding the undesired option with one or more minuses: e.g., &#8220;-l-t&#8221; or &#8220;&#8211;tl&#8221;, in this example. The first hyphen is the regular switch character, but the one before the `t&#8217; is a minus sign. The dual use of hyphens may seem a little awkward, but it&#8217;s reasonably intuitive nonetheless: simply ignore the first hyphen and go from there. It is also consistent with the behavior of the Unix command <i><a href="/docs/linux/man/1-nice/">nice</a></i>(1). </p>
<p> As suggested above, the default variable names are ZIPINFO_OPTS for VMS (where the symbol used to install <i>zipinfo</i> as a foreign command would otherwise be confused with the environment variable), and ZIPINFO for all other operating systems. For compatibility with <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), ZIPINFOOPT is also accepted (don&#8217;t ask). If both ZIPINFO and ZIPINFOOPT are defined, however, ZIPINFO takes precedence. <i>unzip</i>&#8216;s diagnostic option (<code>-v</code> with no zipfile name) can be used to check the values of all four possible <i>unzip</i> and <i>zipinfo</i> environment variables.</p>
<h2>EXAMPLES</h2>
<p> To get a basic, short-format listing of the complete contents of a ZIP archive <i>storage.zip</i>, with both header and totals lines, use only the archive name as an argument to zipinfo: </p>
<pre>
zipinfo storage
</pre>
<p> To produce a basic, long-format listing (not verbose), including header and totals lines, use <code>-l</code>: </p>
<pre>
zipinfo -l storage
</pre>
<p> To list the complete contents of the archive without header and totals lines, either negate the <code>-h</code> and <code>-t</code> options or else specify the contents explicitly: </p>
<pre>
zipinfo --h-t storage
zipinfo storage \*
</pre>
<p> (where the backslash is required only if the shell would otherwise expand the `*&#8217; wildcard, as in Unix when globbing is turned on&#8211;double quotes around the asterisk would have worked as well). To turn off the totals line by default, use the environment variable (C shell is assumed here): </p>
<pre>
setenv ZIPINFO --t
zipinfo storage
</pre>
<p> To get the full, short-format listing of the first example again, given that the environment variable is set as in the previous example, it is necessary to specify the <code>-s</code> option explicitly, since the <code>-t</code> option by itself implies that ONLY the footer line is to be printed: </p>
<pre><code>
setenv ZIPINFO-- t
        zipinfo -
    t storage[only totals line] zipinfo - st storage[full listing]
</code></pre>
<p> The <code>-s</code> option, like <code>-m</code> and <code>-l</code>, includes headers and footers by default, unless otherwise specified. Since the environment variable specified no footers and that has a higher precedence than the default behavior of <code>-s</code>, an explicit <code>-t</code> option was necessary to produce the full listing. Nothing was indicated about the header, however, so the <code>-s</code> option was sufficient. Note that both the <code>-h</code> and <code>-t</code> options, when used by themselves or with each other, override any default listing of member files; only the header and/or footer are printed. This behavior is useful when <i>zipinfo</i> is used with a wildcard zipfile specification; the contents of all zipfiles are then summarized with a single command. </p>
<p> To list information on a single file within the archive, in medium format, specify the filename explicitly: </p>
<pre>
zipinfo -m storage unshrink.c
</pre>
<p> The specification of any member file, as in this example, will override the default header and totals lines; only the single line of information about the requested file will be printed. This is intuitively what one would expect when requesting information about a single file. For multiple files, it is often useful to know the total compressed and uncompressed size; in such cases <code>-t</code> may be specified explicitly: </p>
<pre>
zipinfo -mt storage &quot;*.[ch]&quot; Mak\*
</pre>
<p> To get maximal information about the ZIP archive, use the verbose option. It is usually wise to pipe the output into a filter such as Unix <i><a href="/docs/linux/man/1-more/">more</a></i>(1) if the operating system allows it: </p>
<pre>
zipinfo -v storage | more
</pre>
<p> Finally, to see the most recently modified files in the archive, use the <code>-T</code> option in conjunction with an external sorting utility such as Unix <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) (and <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) as well, in this example): </p>
<pre>
zipinfo -T storage | sort -nr -k 7 | sed 15q
</pre>
<p> The <code>-nr</code> option to <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) tells it to sort numerically in reverse order rather than in textual order, and the <code>-k 7</code> option tells it to sort on the seventh field. This assumes the default short-listing format; if <code>-m</code> or <code>-l</code> is used, the proper <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) option would be <code>-k 8</code>. Older versions of <i><a href="/docs/linux/man/1-sort/">sort</a></i>(1) do not support the <code>-k</code> option, but you can use the traditional <code>+</code> option instead, e.g., <code>+6</code> instead of <code>-k 7</code>. The <i><a href="/docs/linux/man/1-sed/">sed</a></i>(1) command filters out all but the first 15 lines of the listing. Future releases of <i>zipinfo</i> may incorporate date/time and filename sorting as built-in options.</p>
<h2>TIPS</h2>
<p> The author finds it convenient to define an alias <i>ii</i> for <i>zipinfo</i> on systems that allow aliases (or, on other systems, copy/rename the executable, create a link or create a command file with the name <i>ii</i>). The <i>ii</i> usage parallels the common <i>ll</i> alias for long listings in Unix, and the similarity between the outputs of the two commands was intentional.</p>
<h2>BUGS</h2>
<p> As with <i>unzip</i>, <i>zipinfo</i>&#8216;s <code>-M</code> (&#8220;more&#8221;) option is overly simplistic in its handling of screen output; as noted above, it fails to detect the wrapping of long lines and may thereby cause lines at the top of the screen to be scrolled off before being read. <i>zipinfo</i> should detect and treat each occurrence of line-wrap as one additional line printed. This requires knowledge of the screen&#8217;s width as well as its height. In addition, <i>zipinfo</i> should detect the true screen geometry on all systems. </p>
<p> <i>zipinfo</i>&#8216;s listing-format behavior is unnecessarily complex and should be simplified. (This is not to say that it will be.) </p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ls/">ls</a></i>(1), <i><a href="/docs/linux/man/1-funzip/">funzip</a></i>(1), <i><a href="/docs/linux/man/1-unzip/">unzip</a></i>(1), <i><a href="/docs/linux/man/1-unzipsfx/">unzipsfx</a></i>(1), <i><a href="/docs/linux/man/1-zip/">zip</a></i>(1), <i><a href="/docs/linux/man/1-zipcloak/">zipcloak</a></i>(1), <i><a href="/docs/linux/man/1-zipnote/">zipnote</a></i>(1), <i><a href="/docs/linux/man/1-zipsplit/">zipsplit</a></i>(1)</p>
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
<p> Greg &#8220;Cave Newt&#8221; Roelofs. ZipInfo contains pattern-matching code by Mark Adler and fixes/improvements by many others. Please refer to the CONTRIBS file in the UnZip source distribution for a more complete list. </p>
<h2>Index</h2>
