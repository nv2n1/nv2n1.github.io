---
title: "wimlib-imagex-update(1)"
name: "wimlib-imagex-update"
section: "1"
letter: "w"
url: "/docs/linux/man/1-wimlib-imagex-update/"
description: "wimlib-imagex-update – Update a WIM image"
---

<h2>NAME</h2>
<p> wimlib-imagex-update &#8211; Update a WIM image</p>
<h2>SYNOPSIS</h2>
<p> <code>wimlib-imagex update</code> <i>WIMFILE</i> [<i>IMAGE</i>] [<i>OPTION</i>&#8230;] [&lt; <i>CMDFILE</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>wimlib-imagex update</code> modifies the specified <i>IMAGE</i> in the Windows Imaging (WIM) file <i>WIMFILE</i> by adding, deleting, or renaming files or directories in it. This command is also available as simply <code>wimupdate</code> if the appropriate hard link or batch file has been installed. </p>
<p> <i>IMAGE</i> specifies the image in <i>WIMFILE</i> to update. It may be a 1-based index of an image in the WIM or the name of an image in the WIM. Use the <code>wimlib-imagex info</code> (1) command to list the images a WIM file contains. <i>IMAGE</i> may be omitted if <i>WIMFILE</i> contains only one image. </p>
<p> The modifications to perform on the WIM image are specified as a sequence of commands, one per line, read in a text file from standard input. It is recommended that standard input be redirected from a file (<i>CMDFILE</i>), as shown above, rather than typing in commands interactively. Alternatively, to specify a command directly on the command line, see the <code>&#8211;command</code> option.</p>
<h2>AVAILABLE COMMANDS</h2>
<p> This section documents the commands that may appear in the <i>CMDFILE</i> described above.</p>
<h3><code>add</code> [<i>OPTION</i>&#8230;] <i>SOURCE</i> <i>DESTINATION</i></h3>
<p> Add a file or directory tree to the WIM image. <i>SOURCE</i> must specify the path to a file or directory on your filesystem. <i>DESTINATION</i> must specify the path inside the WIM image at which to add the file or directory tree. </p>
<p> If <i>DESTINATION</i> names an existing directory in the WIM image, then <i>SOURCE</i> must also name a directory. This causes the contents of the <i>SOURCE</i> directory to be added to the <i>DESTINATION</i> directory. </p>
<p> If <i>DESTINATION</i> names an existing nondirectory file in the WIM image, then <i>SOURCE</i> must also name a nondirectory file. By default, this causes the <i>DESTINATION</i> file to be replaced with the <i>SOURCE</i> file. Or, with <code>&#8211;no-replace</code> specified, this generates an error. </p>
<p> If <i>DESTINATION</i> does not exist in the WIM image, then any prerequisite directories are created as needed to add the <i>SOURCE</i> at that location. </p>
<p> The <code>add</code> command supports a subset of the options accepted by <code>wimlib-imagex capture</code>; namely, <code>&#8211;dereference</code>, <code>&#8211;unix-data</code>, <code>&#8211;no-acls</code>, and <code>&#8211;strict-acls</code>. See <code>wimlib-imagex-capture</code> (1) for explanations of these options. </p>
<p> In addition, the <code>add</code> command supports the <code>&#8211;no-replace</code> option, which causes the <code>add</code> command to refuse to overwrite existing nondirectory files in the WIM image.</p>
<h3><code>delete</code> [<i>OPTION</i>&#8230;] <i>PATH</i></h3>
<p> Delete a file or directory tree from the WIM image. <i>PATH</i> must specify the path inside the WIM image of the file or directory tree to delete. </p>
<p> The available options for the <code>delete</code> command are:</p>
<dl>
<dt><code>&#8211;force</code></p>
<dd> Do not issue an error if the path to delete does not exist.</p>
<dt><code>&#8211;recursive</code></p>
<dd> Delete the file or directory tree recursively; if not specified, an error is issued if the path to delete is a directory.</dl>
<h3><code>rename</code> <i>OLD_PATH</i> <i>NEW_PATH</i></h3>
<p> Rename a file or directory tree inside the WIM image. <i>OLD_PATH</i> must specify the old path of the file or directory tree inside the WIM image, and <i>NEW_PATH</i> must specify the new path for the file or directory tree. This command follows the semantics of the POSIX <code>rename</code> (3) function; in particular, a pre-existing file at <i>NEW_PATH</i> will be deleted if present, except in certain cases such as attempting to rename a directory to a non-directory, which is not allowed. </p>
<p> There are no options available for the <code>rename</code> command.</p>
<h2>OPTIONS</h2>
<p> The following options are accepted on the command line by <code>wimlib-imagex update</code> itself:</p>
<dl>
<dt><code>&#8211;dereference</code></p>
<dd> Use <code>&#8211;dereference</code> for all <code>add</code> commands.</p>
<dt><code>&#8211;unix-data</code></p>
<dd> Use <code>&#8211;unix-data</code> for all <code>add</code> commands.</p>
<dt><code>&#8211;no-acls</code></p>
<dd> Use <code>&#8211;no-acls</code> for all <code>add</code> commands.</p>
<dt><code>&#8211;strict-acls</code></p>
<dd> Use <code>&#8211;strict-acls</code> for all <code>add</code> commands.</p>
<dt><code>&#8211;no-replace</code></p>
<dd> Use <code>&#8211;no-replace</code> for all <code>add</code> commands.</p>
<dt><code>&#8211;config</code>=<i>FILE</i></p>
<dd> Set the capture configuration file for all <code>add</code> commands. See the description of this option in <code>wimlib-imagex-capture</code> (1).</p>
<dt><code>&#8211;force</code></p>
<dd> Use <code>&#8211;force</code> for all <code>delete</code> commands.</p>
<dt><code>&#8211;recursive</code></p>
<dd> Use <code>&#8211;recursive</code> for all <code>delete</code> commands.</p>
<dt><code>&#8211;check</code></p>
<dd> When reading <i>WIMFILE</i>, verify its integrity if the integrity table is present; in addition, include an integrity table in the updated WIM. If this option is not specified, an integrity table will be included in the updated WIM if and only if one was present before.</p>
<dt><code>&#8211;threads</code>=<i>NUM_THREADS</i></p>
<dd> Number of threads to use for compressing newly added files. Default: autodetect (number of processors).</p>
<dt><code>&#8211;rebuild</code></p>
<dd> Rebuild the entire WIM rather than appending the updated data to the end of it. Rebuilding the WIM is slower, but will save a little bit of space that would otherwise be left as a hole in the WIM file.</p>
<dt>
<dd> See <code>wimlib-imagex-optimize</code> (1) for a more customizable way of rebuilding (and optionally recompressing) a WIM file. If running <code>wimlib-imagex optimize</code> after <code>wimlib-imagex update</code>, there is no need to specify <code>&#8211;rebuild</code> to <code>wimlib-imagex update</code>.</p>
<dt><code>&#8211;command</code>=<i>STRING</i></p>
<dd> Instead of reading update commands from standard input, read a single update command directly from the string <i>STRING</i> specified on the command line. This option cannot be provided more than one time and cannot be used to specify more than one update command. Note that the <i>STRING</i>, as well as any paths containing spaces within the <i>STRING</i> must be appropriately quoted. If running from cmd.exe on Windows, you should use double quotes for the outer quotes and single quotes for the inner quotes. Example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
wimlib-imagex update boot.wim 1 \
<br>
<dl><dt><dd>--command=&quot;add 'C:\My Dir' '\My Dir'&quot;
</dl>
</dl>
</dl>
</pre>
<dt>
<dd> This option is provided for convenience only. Do not execute <code>wimlib-imagex update</code> multiple consecutive times, each time passing the <code>&#8211;command</code> option! This is inefficient. Instead, generate an update command file and provide it (on standard input) to a single invocation of <code>wimlib-imagex update</code>, as explained in this document.</p>
<dt><code>&#8211;wimboot-config</code>=<i>FILE</i></p>
<dd> If this option is specified, no commands shall be read from standard input, and instead the following command shall be executed:</p>
<dt>
<dd>
<pre>
<dl><dt><dd><dl><dt><dd><code>add</code> <i>FILE</i> /Windows/System32/WimBootCompress.ini
</dl>
</dl>
</pre>
<dt>
<dd> This sets <i>FILE</i> as the WIMBoot configuration file for the image. The [PrepopulateList] section of this file specifies path globs that shall not be extracted as WIMBoot pointer files (perhaps due to being needed early in the boot process). See the documentation for the <code>&#8211;wimboot</code> option of <code>wimlib-imagex apply</code> (1) for more information.</p>
<dt><code>&#8211;unsafe-compact</code></p>
<dd> Compact the WIM archive in-place and append any new data, eliminating &quot;holes&quot;. In general, this option should <i>not</i> be used because a failed or interrupted compaction will corrupt the WIM archive. For more information, see the documentation for this option in <code>wimlib-imagex-optimize</code> (1).</dl>
<h2>NOTES</h2>
<p> <code>wimlib-imagex update</code> is partly redundant with <code>wimlib-imagex mountrw</code>, since if a WIM image can be mounted read-write, then there theoretically is no need for <code>wimlib-imagex update</code>. The main advantage of <code>wimlib-imagex update</code> is that it works on both UNIX-like systems and Windows, whereas <code>wimlib-imagex mountrw</code> is only available on UNIX-like systems, and even then it only works on those with a compatible FUSE implementation. </p>
<p> Symbolic links inside a WIM image are not dereferenced when being interpreted. So, for example, if you have a WIM image that contains a symbolic link &quot;/Documents and Settings&quot; -&gt; &quot;/Users&quot; where &quot;/Users&quot; is a directory, then a subdirectory named &quot;Public&quot; in this directory must be specified as &quot;/Users/Public&quot; rather than &quot;/Documents and Settings/Public&quot;. </p>
<p> All paths to files or directories within the WIM image must be specified relative to the root of the image. However, the leading slash is optional, and both forward slashes and backslashes are accepted. In addition, on Windows, the paths are by default treated case-insensitively, while on UNIX-like systems, the paths are by default treated case-sensitively. The default case sensitivity may be changed by setting the <code>WIMLIB_IMAGEX_IGNORE_CASE</code> environmental variable to 0 or 1. </p>
<p> The command file (<i>CMDFILE</i>) is parsed by <code>wimlib-imagex update</code> itself and not by the system shell. Therefore, its syntax is limited. However, comment lines beginning with &#8216;#&#8217; are allowed, and it is also possible to quote arguments with whitespace inside them. </p>
<p> On UNIX-like systems, you cannot use <code>wimlib-imagex update</code> to add files to an image directly from an NTFS volume using libntfs-3g, even though <code>wimlib-imagex capture</code> supports capturing a full image this way. </p>
<p> Except when using <code>&#8211;unsafe-compact</code>, it is safe to abort a <code>wimlib-imagex update</code> command partway through; however, after doing this, it is recommended to run <code>wimlib-imagex optimize</code> to remove any data that was appended to the physical WIM file but not yet incorporated into the structure of the WIM, unless <code>&#8211;rebuild</code> was specified, in which case you should delete the temporary file left over.</p>
<h2>EXAMPLES</h2>
<p> All the examples below show the update command file to be created as well as the <code>wimlib-imagex update</code> command to run to perform the updates. </p>
<p> Delete two files from a WIM image: </p>
<dl>
<dt>
<dd> <i>update_commands.txt</i>:</p>
<dl>
<dt>
<dd>
<pre>
delete /setup.exe
delete /sources/setup.exe
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> $ wimlib-imagex update boot.wim 2 &lt; update_commands.txt</dl>
<p> Add some files and directories to a WIM image. Note that the first path of each <code>add</code> command specifies the files to add, while the second path of each <code>add</code> command specify the locations at which to to add them inside the WIM image: </p>
<dl>
<dt>
<dd> <i>update_commands.txt</i>:</p>
<dl>
<dt>
<dd>
<pre>
add somedir     /dir
add somefile    /dir/file
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> $ wimlib-imagex update boot.wim 2 &lt; update_commands.txt</dl>
<p> Rename a file inside a WIM image. </p>
<dl>
<dt>
<dd> <i>update_commands.txt</i>:</p>
<dl>
<dt>
<dd>
<pre>
rename /dir_in_wim/oldfile.txt /dir_in_wim/newfile.txt
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> $ wimlib-imagex update boot.wim 2 &lt; update_commands.txt</dl>
<p> Using additional features, such as comments, options, and overlays, and including an integrity table in the updated WIM: </p>
<dl>
<dt>
<dd> <i>update_commands.txt</i>:</p>
<dl>
<dt>
<dd>
<pre>
#
# This file specifies some changes to make to a WIM image.
#
# Add a new directory containing files I want in the image.
# The quotes are necessary because the directory name
# contains a space.
add &quot;My Directory&quot; &quot;/My Directory&quot;
# Add the contents of &quot;Another Directory&quot; to the
# &quot;/My Directory&quot; we just created in the WIM image.  Since
# the destination path already exists, this performs an
# overlay.
add &quot;Another Directory&quot; &quot;/My Directory&quot;
# Rename some file for some reason.
rename /dir_in_wim/oldfile.txt /dir_in_wim/newfile.txt
# Delete an unwanted directory.
delete --recursive /Users/Me/Documents/Junk
</pre>
</dl>
</dl>
<dl>
<dt>
<dd> $ wimlib-imagex update boot.wim 2 &#8211;check &lt; update_commands.txt</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-wimlib-imagex/">wimlib-imagex</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-capture/">wimlib-imagex-capture</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-info/">wimlib-imagex-info</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-mountrw/">wimlib-imagex-mountrw</a></code>(1) <code><a href="/docs/linux/man/1-wimlib-imagex-optimize/">wimlib-imagex-optimize</a></code>(1) </p>
<h2>Index</h2>
<dt><a href="#lbAI">OPTIONS</a></p>
<dd>
<dt><a href="#lbAJ">NOTES</a></p>
<dd>
<dt><a href="#lbAK">EXAMPLES</a></p>
<dd>
<dt><a href="#lbAL">SEE ALSO</a></p>
<dd></dl>
