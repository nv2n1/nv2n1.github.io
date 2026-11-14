---
title: "wimlib-imagex-extract(1)"
name: "wimlib-imagex-extract"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-extract/"
description: "wimlib-imagex-extract – Extract files or directories from a WIM image"
---

<h2>NAME</h2>
<p> wimlib-imagex-extract &#8211; Extract files or directories from a WIM image</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex extract</code> <i>WIMFILE</i> <i>IMAGE</i> [(<i>PATH</i> | @<i>LISTFILE</i>)&#8230;] [<i>OPTION</i>&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex extract</code> extracts one or more files or directory trees from the specified <i>IMAGE</i> contained in the Windows Imaging (WIM) file <i>WIMFILE</i>. This command is also available as simply <code>wimextract</code> if the appropriate hard link or batch file has been installed. </p>
<p> <code>wimlib-imagex extract</code> is intended for extracting only a subset of a WIM image. If you want to extract or &quot;apply&quot; a full WIM image to a directory or NTFS volume, use <code>wimlib-imagex apply</code> (1) instead. </p>
<p> <i>IMAGE</i> specifies the image in <i>WIMFILE</i> that contains the files or directory trees to extract. It may be a 1-based index of an image in the WIM or the name of an image in the WIM. Use the <code>wimlib-imagex info</code> (1) command to show what images a WIM file contains. </p>
<p> If no additional arguments are given, the entire WIM image is extracted. Otherwise, each additional argument is interpreted as a <i>PATH</i> if it does not begin with the &#8216;@&#8217; character, or a <i>LISTFILE</i> if it does. Each <i>PATH</i> specifies a file or directory tree within the WIM image to extract, whereas each <i>LISTFILE</i> specifies a file that itself contains a list of paths to extract. See <code>PATHS AND LISTFILES</code> for more details. </p>
<p> By default, files and directories are extracted to the current directory. Use <code>&#8211;dest-dir</code> to select a different destination directory. Alternatively, use <code>&#8211;to-stdout</code> to extract a file to standard output to pipe into another program. </p>
<p> A file or directory extracted from a <i>PATH</i> argument is by default extracted directly into the destination directory, whereas a file or directory extracted from a <i>LISTFILE</i> argument is by default extracted into the destination directory in such a way that the archive&#8217;s directory structure is preserved. Use <code>&#8211;preserve-dir-structure</code> to always get the latter behavior. </p>
<p> <code>wimlib-imagex extract</code> supports extracting files and directory trees from stand-alone WIMs as well as split WIMs. See <code>SPLIT WIMS</code>.</p>
<h2>PATHS AND LISTFILES</h2>
<p> Each path, including those on the command line and those in listfiles, must be specified as an absolute path starting from the root of the WIM image, like those output by the <code>wimlib-imagex dir</code> (1) command. However, path separators may be either forward or backward slashes, and the leading slash is optional. </p>
<p> On Windows, by default paths are treated case-insensitively, whereas on UNIX-like systems, by default paths are treated case-sensitively. In either case, the default behavior may be overridden through the <code>WIMLIB_IMAGEX_IGNORE_CASE</code> environmental variable, as documented in <code>wimlib-imagex</code> (1). </p>
<p> By default, each path may contain the wildcard characters &#8216;?&#8217; and &#8216;*&#8217;. The &#8216;?&#8217; character matches any non-path-separator character, whereas the &#8216;*&#8217; character matches zero or more non-path-separator characters. Consequently, a single wildcard path, or &quot;glob&quot;, may expand to multiple actual files or directories. Use the <code>&#8211;no-globs</code> option to disable wildcard matching and search for each path literally. </p>
<p> Each <i>LISTFILE</i> must be a text file (UTF-8 or UTF-16LE encoded; plain ASCII is also fine) that contains a list of paths to extract, one per line. Wildcard characters are allowed by default. The following demonstrates an example listfile: </p>
<dl>
<dt>
<dd>
<pre><code>
;
This is a comment(begins with semicolon)
#This is also a comment(begins with number sign)
        / Users
        / Windows / explorer.exe
        / Windows / System32 / en
    - US/*
; Both forward and backslashes are valid.
; It's not necessary to quote paths containing internal spaces.
\Program Files\A*
; Leading and trailing whitespace is ignored
    \Windows
otepad*

</code></pre>
<h2>SPLIT WIMS</h2>
<p> You may use <code>wimlib-imagex extract</code> to extract files or directory trees from a split WIM. This uses the <code>&#8211;refs</code>=&quot;<i>GLOB</i>&quot; option in the same way as in other commands such as <code>wimlib-imagex apply</code>. See <code>wimlib-imagex apply</code> (1) for more details.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if an integrity table is present.</p>
<dt><code>&#8211;ref</code>=&quot;<i>GLOB</i>&quot;</p>
<dd> File glob of additional WIMs or split WIM parts to reference resources from. See <code>SPLIT_WIMS</code>. Note: <i>GLOB</i> is listed in quotes because it is interpreted by <code>wimlib-imagex</code> and may need to be quoted to protect against shell expansion.</p>
<dt><code>&#8211;dest-dir</code>=<i>DIR</i></p>
<dd> Extract the files and directories to the directory <i>DIR</i> instead of to the current working directory.</p>
<dt><code>&#8211;to-stdout</code></p>
<dd> Extract the files to standard output instead of to the filesystem. This can only be provided if all the specified paths are to regular files (not directories or reparse points). If present, alternate data streams are not extracted.</p>
<dt><code>&#8211;unix-data</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;no-acls</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;strict-acls</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;no-attributes</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;include-invalid-names</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;no-globs</code></p>
<dd> Do not recognize wildcard characters in paths. Each path will be searched for literally. In addition, if case insensitivity is enabled, do not allow a single path to match multiple files with the same case-insensitive name but different case-sensitive names.</p>
<dt>
<dd> <code>&#8211;no-wildcards</code> is also accepted as an alias for this option.</p>
<dt><code>&#8211;nullglob</code></p>
<dd> If a glob does not match any files, ignore it and print a warning instead of failing with an error. In other words, this option allows a glob to successfully match zero files.</p>
<dt>
<dd> This option also affects paths that do not contain wildcard characters, since such paths are still considered globs unless <code>&#8211;no-globs</code> is enabled. If case-insensitivity is enabled, such a glob could match multiple files with the same case-insensitive name but different case-sensitive names, whereas a non-glob path (with <code>&#8211;no-globs</code>) can match at most one file.</p>
<dt><code>&#8211;preserve-dir-structure</code></p>
<dd> When extracting paths, preserve the archive directory structure instead of extracting the file or directory tree named by each path directly to the destination directory. Note: <code>&#8211;preserve-dir-structure</code> is already the default behavior for paths in listfiles, but not paths directly specified on the command line.</p>
<dt><code>&#8211;wimboot</code></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</p>
<dt><code>&#8211;compact</code>=<i>FORMAT</i></p>
<dd> See the documentation for this option in <code>wimlib-imagex-apply</code> (1).</dl>
<h2>NOTES</h2>
<p> See the documentation <code>wimlib-imagex apply</code> (1) for documentation about what data and metadata are extracted on UNIX-like systems versus on Windows. </p>
<p> On UNIX-like systems that support userspace filesystems with FUSE (e.g. Linux), one can alternatively mount the WIM image with <code>wimlib-imagex mount</code> (1) and then extract the desired files or directories using any standard command-line or graphical program. </p>
<p> Reparse-point fixups (a.k.a. changing absolute symbolic links and junctions to point within the extraction location) are never done by <code>wimlib-imagex extract</code>. Use <code>wimlib-imagex apply</code> if you want this behavior. </p>
<p> Unlike <code>wimlib-imagex apply</code>, <code>wimlib-imagex extract</code> does not support extracting files directly to an NTFS volume using libntfs-3g. </p>
<p> wimlib v1.6.0 and later can extract files from version 3584 WIMs, which usually contain LZMS-compressed solid resources and may carry the <i>.esd</i> file extension rather than <i>.wim</i>. However, <i>.esd</i> files downloaded directly by the Windows 8 web downloader have encrypted segments, and wimlib cannot extract such files until they are first decrypted. Furthermore, such files are not designed for random access, so extracting individual files from them may be slow.</p>
<h2>EXAMPLES</h2>
<p> Extract a file from the first image in &quot;boot.wim&quot; to the current directory:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract boot.wim 1 /Windows/System32/notepad.exe</dl>
<p> Extract a file from the first image in &quot;boot.wim&quot; to standard output:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract boot.wim 1 /Windows/System32/notepad.exe \ </p>
<dl>
<dt>
<dd> &#8211;to-stdout</dl>
</dl>
<p> Extract a file from the first image in &quot;boot.wim&quot; to the specified directory:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract boot.wim 1 /Windows/System32/notepad.exe \ </p>
<dl>
<dt>
<dd> &#8211;dest-dir=somedir</dl>
</dl>
<p> Extract the &quot;sources&quot; directory from the first image in &quot;boot.wim&quot; to the current directory:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract boot.wim 1 /sources</dl>
<p> Extract multiple files and directories in one command:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract boot.wim 1 /Windows/Fonts \ </p>
<dl>
<dt>
<dd> /sources /Windows/System32/cmd.exe</dl>
</dl>
<p> Extract many files to the current directory using a wildcard pattern:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract install.wim 1 &quot;/Windows/Fonts/*.ttf&quot;</dl>
<p> Extract files using a list file:</p>
<dl>
<dt>
<dd>
<p> wimlib-imagex extract install.wim 1 @files.txt</dl>
<p>&nbsp;<wbr>&#8230;&nbsp;<wbr>&nbsp;<wbr>where files.txt could be something like: </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
Windows\System32\*.*
Windows\System32\??-??\*.*
Windows\System32n-US\*.*
</dl>
</dl>
</pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-apply/">wimlib-imagex-apply</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-dir/">wimlib-imagex-dir</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-mount/">wimlib-imagex-mount</a></code>(1) </p>
<h2>Index</h2>
