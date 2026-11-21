---
title: "7za(1)"
name: "7za"
section: "1"
letter: "7"
url: "/docs/linux/man/1-7za/"
description: "7za – A file archiver with high compression ratio format"
---

<h2>SYNOPSIS</h2>
<p> <code>7za</code> <code>&lt;command&gt;</code> [<code>&lt;switches&gt;</code>&#8230; ] <code>&lt;archive_name&gt;</code> [<code>&lt;file_names&gt;</code>&#8230; ] [<code>&lt;@listfiles&gt;</code>&#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> 7-Zip is a file archiver supporting 7z (that implements LZMA compression algorithm featuring very high compression ratio), LZMA2, XZ, ZIP, Zip64, CAB, RAR (if the non-free p7zip-rar package is installed), ARJ, GZIP, BZIP2, TAR, CPIO, RPM, ISO, most filesystem images and DEB formats. Compression ratio in the new 7z format is 30-50% better than ratio in ZIP format. </p>
<p> <code>7za</code> is a stand-alone executable. <code>7za</code> handles fewer archive formats than <code><a href="/docs/linux/man/1-7z/">7z</a></code>(1).</p>
<h2>COMMANDS</h2>
<dl>
<dt><code>a</code></dt>
<dd> Add files to archive</dd>
<dt><code>b</code></dt>
<dd> Benchmark</dd>
<dt><code>d</code></dt>
<dd> Delete files from archive</dd>
<dt><code>e</code></dt>
<dd> Extract files from archive (without using directory names)</dd>
<dt><code>h</code></dt>
<dd> Calculate hash values for files</dd>
<dt><code>i</code></dt>
<dd> Show information about supported formats</dd>
<dt><code>l</code></dt>
<dd> List contents of archive</dd>
<dt><code>rn</code></dt>
<dd> Rename files in archive</dd>
<dt><code>t</code></dt>
<dd> Test integrity of archive</dd>
<dt><code>u</code></dt>
<dd> Update files to archive</dd>
<dt><code>x</code></dt>
<dd> eXtract files with full paths</dd></dl>
<h2>SWITCHES</h2>
<dl>
<dt><code>&#8212;</code></dt>
<dd> Stop switches parsing</dd>
<dt><code>-ai[r[-|0]]{@listfile|!wildcard}</code></dt>
<dd> Include archives</dd>
<dt><code>-ax[r[-|0]]{@listfile|!wildcard}</code></dt>
<dd> Exclude archives</dd>
<dt><code>-ao{a|s|t|u}</code></dt>
<dd> Set Overwrite mode</dd>
<dt><code>-an</code></dt>
<dd> Disable archive_name field</dd>
<dt><code>-bb[0-3]</code></dt>
<dd> Set output log level</dd>
<dt><code>-bd</code></dt>
<dd> Disable progress indicator</dd>
<dt><code>-bs{o|e|p}{0|1|2}</code></dt>
<dd> Set output stream for output/error/progress line</dd>
<dt><code>-bt</code></dt>
<dd> Show execution time statistics</dd>
<dt><code>-i[r[-|0]]{@listfile|!wildcard}</code></dt>
<dd> Include filenames</dd>
<dt><code>-m{Parameters}</code></dt>
<dd> Set Compression Method (see /usr/share/doc/p7zip/DOC/MANUAL/cmdline/switches/method.htm from the p7zip-full package for a list of methods)</dd>
<dt><code>-o{Directory}</code></dt>
<dd> Set Output directory</dd>
<dt><code>-p{Password}</code></dt>
<dd> Set Password (NOTE: this flag does not work with 7zr)</dd>
<dt><code>-r[-|0]</code></dt>
<dd> Recurse subdirectories (CAUTION: this flag does not do what you think, avoid using it)</dd>
<dt><code>-sa{a|e|s}</code></dt>
<dd> Set archive name mode</dd>
<dt><code>-scc{UTF-8|WIN|DOS}</code></dt>
<dd> Set charset for for console input/output</dd>
<dt><code>-scs{UTF-8|UTF-16LE|UTF-16BE|WIN|DOS|{id}}</code></dt>
<dd> Set charset for list files</dd>
<dt><code>-scrc[CRC32|CRC64|SHA1|SHA256|*]</code></dt>
<dd> Set hash function for x, e, h commands</dd>
<dt><code>-sdel</code></dt>
<dd> Delete files after compression</dd>
<dt><code>-seml[.]</code></dt>
<dd> Send archive by email</dd>
<dt><code>-sfx[{name}]</code></dt>
<dd> Create SFX archive</dd>
<dt><code>-si[{name}]</code></dt>
<dd> Read data from stdin (e.g. tar cf &#8211; directory | 7za a -si directory.tar.7z)</dd>
<dt><code>-slp</code></dt>
<dd> Set Large Pages mode</dd>
<dt><code>-slt</code></dt>
<dd> Show technical information for l (List) command</dd>
<dt><code>-snh</code></dt>
<dd> Store hard links as links</dd>
<dt><code>-snl</code></dt>
<dd> Store symbolic links as links</dd>
<dt><code>-sni</code></dt>
<dd> Store NT security information</dd>
<dt><code>-sns[-]</code></dt>
<dd> Store NTFS alternate streams</dd>
<dt><code>-sfx[{name}]</code></dt>
<dd> Create SFX archive</dd>
<dt><code>-so</code></dt>
<dd> Write data to stdout (e.g. 7za x -so directory.tar.7z | tar xf -)</dd>
<dt><code>-spd</code></dt>
<dd> Disable wildcard matching for file names</dd>
<dt><code>-spe</code></dt>
<dd> Eliminate duplication of root folder for extract command</dd>
<dt><code>-spf</code></dt>
<dd> Use fully qualified file paths</dd>
<dt><code>-ssc[-]</code></dt>
<dd> Set sensitive case mode</dd>
<dt><code>-ssw</code></dt>
<dd> Compress shared files</dd>
<dt><code>-stl</code></dt>
<dd> Set archive timestamp from the most recently modified file</dd>
<dt><code>-stm{HexMask}</code></dt>
<dd> Set CPU thread affinity mask (hexadecimal number)</dd>
<dt><code>-stx{Type}</code></dt>
<dd> Exclude archive type</dd>
<dt><code>-t{Type}</code></dt>
<dd> Set type of archive</dd>
<dt><code>-u[-][p#][q#][r#][x#][y#][z#][!newArchiveName]</code></dt>
<dd> Update options</dd>
<dt><code>-v{Size}[b|k|m|g]</code></dt>
<dd> Create volumes</dd>
<dt><code>-w[path]</code></dt>
<dd> Set working directory. Empty path means a temporary directory</dd>
<dt><code>-x[r[-|0]]]{@listfile|!wildcard}</code></dt>
<dd> Exclude filenames</dd>
<dt><code>-y</code></dt>
<dd> Assume Yes on all queries</dd></dl>
<h2>DIAGNOSTICS</h2>
<p> 7-Zip returns the following exit codes:</p>
<dl>
<dl>
<dt>0</dt>
<dd> Normal (no errors or warnings detected)</dd>
<dt>1</dt>
<dd> Warning (Non fatal error(s)). For example, some files cannot be read during compressing, so they were not compressed</dd>
<dt>2</dt>
<dd> Fatal error</dd>
<dt>7</dt>
<dd> Bad command line parameters</dd>
<dt>8</dt>
<dd> Not enough memory for operation</dd>
<dt>255</dt>
<dd> User stopped the process with control-C (or similar)</dd></dl>
</dl>
<h2>Backup and limitations</h2>
<p> DO NOT USE the 7-zip format for backup purpose on Linux/Unix because :<br />
&nbsp;&#8211; 7-zip does not store the owner/group of the file. </p>
<p> On Linux/Unix, in order to backup directories you must use tar :<br />
&nbsp;&#8211; to backup a directory&nbsp;<wbr>&nbsp;: tar cf &#8211; directory | 7za a -si directory.tar.7z<br />
&nbsp;&#8211; to restore your backup : 7za x -so directory.tar.7z | tar xf &#8211; </p>
<p> If you want to send files and directories (not the owner of file) to others Unix/MacOS/Windows users, you can use the 7-zip format. </p>
<p>&nbsp;<wbr>&nbsp;example : 7za a directory.7z&nbsp;<wbr>&nbsp;directory </p>
<p> Do not use &quot;-r&quot; because this flag does not do what you think. </p>
<p> Do not use directory/* because of &quot;.*&quot; files (example : &quot;directory/*&quot; does not match &quot;directory/.profile&quot;)</p>
<h2>EXAMPLE 1</h2>
<dl>
<dt><code>7za a -t7z -m0=lzma -mx=9 -mfb=64 -md=32m -ms=on archive.7z dir1</code></dt>
<dd> adds all files from directory &quot;dir1&quot; to archive archive.7z using &quot;ultra settings&quot;</dd>
<dt><code>-t7z</code></dt>
<dd> 7z archive</dd>
<dt><code>-m0=lzma</code></dt>
<dd> lzma method</dd>
<dt><code>-mx=9</code></dt>
<dd> level of compression = 9 (Ultra)</dd>
<dt><code>-mfb=64</code></dt>
<dd> number of fast bytes for LZMA = 64</dd>
<dt><code>-md=32m</code></dt>
<dd> dictionary size = 32 megabytes</dd>
<dt><code>-ms=on</code></dt>
<dd> solid archive = on</dd></dl>
<h2>EXAMPLE 2</h2>
<dl>
<dt><code>7za a -sfx archive.exe dir1</code></dt>
<dd> add all files from directory &quot;dir1&quot; to SFX archive archive.exe (Remark : SFX archive MUST end with &quot;.exe&quot;)</dd></dl>
<h2>EXAMPLE 3</h2>
<dl>
<dt><code>7za a -mhe=on -pmy_password archive.7z a_directory</code></dt>
<dd> add all files from directory &quot;a_directory&quot; to the archive &quot;archive.7z&quot; (with data and header archive encryption on)</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-7zr/">7zr</a></code>(1), <code><a href="/docs/linux/man/1-7z/">7z</a></code>(1), <code><a href="/docs/linux/man/1-p7zip/">p7zip</a></code>(1), <code><a href="/docs/linux/man/1-bzip2/">bzip2</a></code>(1), <code><a href="/docs/linux/man/1-gzip/">gzip</a></code>(1), <code><a href="/docs/linux/man/1-zip/">zip</a>(1),</code> </p>
<h2>HTML Documentation</h2>
<p> /usr/share/doc/p7zip-full/DOC/MANUAL/start.htm</p>
<h2>AUTHOR</h2>
<dl>
<dt>Written for Debian by Mohammed Adnene Trojette. Updated by Robert Luberda.</dt>
<dd>
</dd></dl>
