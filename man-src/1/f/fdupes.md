---
title: "fdupes(1)"
name: "fdupes"
section: "1"
letter: "f"
url: "/docs/linux/man/1-fdupes/"
---

<h2 class="name">NAME</h2>
 

 fdupes - finds duplicate files in a given set of directories 

<h2>SYNOPSIS</h2>

 <b>fdupes</b> [ <i>options</i> ] <i>DIRECTORY</i> ... 

<h2>DESCRIPTION</h2>

 Searches the given path for duplicate files. Such files are found by comparing file sizes and MD5 signatures, followed by a byte-by-byte comparison. 

<h2>OPTIONS</h2>

<dl>
<dt><b>-r --recurse</b>
</dt><dd> for every directory given follow subdirectories encountered within
</dd><dt><b>-R --recurse:</b>
</dt><dd> for each directory given after this option follow subdirectories encountered within
</dd><dt><b>-s --symlinks</b>
</dt><dd> follow symlinked directories
</dd><dt><b>-H --hardlinks</b>
</dt><dd> normally, when two or more files point to the same disk area they are treated as non-duplicates; this option will change this behavior
</dd><dt><b>-n --noempty</b>
</dt><dd> exclude zero-length files from consideration
</dd><dt><b>-f --omitfirst</b>
</dt><dd> omit the first file in each set of matches
</dd><dt><b>-1 --sameline</b>
</dt><dd> list each set of matches on a single line
</dd><dt><b>-S --size</b>
</dt><dd> show size of duplicate files
</dd><dt><b>-q --quiet</b>
</dt><dd> hide progress indicator
</dd><dt><b>-d --delete</b>
</dt><dd> prompt user for files to preserve, deleting all others (see <b>CAVEATS</b> below)
</dd><dt><b>-N --noprompt</b>
</dt><dd> when used together with --delete, preserve the first file in each set of duplicates and delete the others without prompting the user
</dd><dt><b>-p --permissions</b>
</dt><dd> don't consider files with different owner/group or permission bits as duplicates
</dd><dt><b>-v --version</b>
</dt><dd> display fdupes version
</dd><dt><b>-h --help</b>
</dt><dd> displays help</dd></dl>

<h2>SEE ALSO</h2>

 <b><a HREF="/docs/linux/man/1-md5sum/">md5sum</a></b>(1)

<h2>NOTES</h2>

 Unless <b>-1</b> or <b>--sameline</b> is specified, duplicate files are listed together in groups, each file displayed on a separate line. The groups are then separated from each other by blank lines. 

 When <b>-1</b> or <b>--sameline</b> is specified, spaces and backslash characters (<b>\</b>) appearing in a filename are preceded by a backslash character.

<h2>CAVEATS</h2>

 If fdupes returns with an error message such as <b>fdupes: error invoking md5sum</b> it means the program has been compiled to use an external program to calculate MD5 signatures (otherwise, fdupes uses internal routines for this purpose), and an error has occurred while attempting to execute it. If this is the case, the specified program should be properly installed prior to running fdupes. 

 When using <b>-d</b> or <b>--delete</b>, care should be taken to insure against accidental data loss. 

 When used together with options <b>-s</b> or <b>--symlink</b>, a user could accidentally preserve a symlink while deleting the file it points to. 

 Furthermore, when specifying a particular directory more than once, all files within that directory will be listed as their own duplicates, leading to data loss should a user preserve a file without its &quot;duplicate&quot; (the file itself!). 

<h2>AUTHOR</h2>

 Adrian Lopez &lt;adrian2 [at] caribe.net&gt;
