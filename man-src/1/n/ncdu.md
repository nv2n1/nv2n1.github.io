---
title: "ncdu(1)"
name: "ncdu"
section: "1"
letter: "n"
url: "/docs/linux/man/1-ncdu/"
description: "ncdu – NCurses Disk Usage"
---

<h2 class="name">NAME</h2>
<p> ncdu &#8211; NCurses Disk Usage </p>
<h2>SYNOPSIS</h2>
<p> <code>ncdu</code> [<i>options</i>] <i>dir</i></p>
<h2>DESCRIPTION</h2>
<p> ncdu (NCurses Disk Usage) is a curses-based version of the well-known &#8216;du&#8217;, and provides a fast way to see what directories are using your disk space.</p>
<h2>OPTIONS</h2>
<h3>Mode Selection</h3>
<dl>
<dt>-h</p>
<dd> Print a short help message and quit.</p>
<dt>-v</p>
<dd> Print ncdu version and quit.</p>
<dt>-f <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Load the given file, which has earlier been created with the <tt>&quot;-o&quot;</tt> option. If <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is equivalent to <tt>&quot;-&quot;</tt>, the file is read from standard input. </p>
<p> For the sake of preventing a screw-up, the current version of ncdu will assume that the directory information in the imported file does not represent the filesystem on which the file is being imported. That is, the refresh and file deletion options in the browser will be disabled.</p>
<dt><i>dir</i></p>
<dd> Scan the given directory.</p>
<dt>-o <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Export all necessary information to <i></i><font SIZE="-1"><i>FILE</i></font><i></i> instead of opening the browser interface. If <i></i><font SIZE="-1"><i>FILE</i></font><i></i> is <tt>&quot;-&quot;</tt>, the data is written to standard output. See the examples section below for some handy use cases. </p>
<p> Be warned that the exported data may grow quite large when exporting a directory with many files. 10.000 files will get you an export in the order of 600 to 700 KiB uncompressed, or a little over 100 KiB when compressed with gzip. This scales linearly, so be prepared to handle a few tens of megabytes when dealing with millions of files.</dl>
<h3>Interface options</h3>
<dl>
<dt>-0</p>
<dd> Don&#8217;t give any feedback while scanning a directory or importing a file, other than when a fatal error occurs. Ncurses will not be initialized until the scan is complete. When exporting the data with <tt>&quot;-o&quot;</tt>, ncurses will not be initialized at all. This option is the default when exporting to standard output.</p>
<dt>-1</p>
<dd> Similar to <tt>&quot;-0&quot;</tt>, but does give feedback on the scanning progress with a single line of output. This option is the default when exporting to a file. </p>
<p> In some cases, the ncurses browser interface which you&#8217;ll see after the scan/import is complete may look garbled when using this option. If you&#8217;re not exporting to a file, <tt>&quot;-2&quot;</tt> is probably a better choice.</p>
<dt>-2</p>
<dd> Provide a full-screen ncurses interface while scanning a directory or importing a file. This is the only interface that provides feedback on any non-fatal errors while scanning.</p>
<dt>-q</p>
<dd> Quiet mode. While scanning or importing the directory, ncdu will update the screen 10 times a second by default, this will be decreased to once every 2 seconds in quiet mode. Use this feature to save bandwidth over remote connections. This option has no effect when <tt>&quot;-0&quot;</tt> is used.</p>
<dt>-r</p>
<dd> Read-only mode. This will disable the built-in file deletion feature. This option has no effect when <tt>&quot;-o&quot;</tt> is used, because there will not be a browser interface in that case. It has no effect when <tt>&quot;-f&quot;</tt> is used, either, because the deletion feature is disabled in that case anyway.</p>
<dt>&#8211;si</p>
<dd> List sizes using base 10 prefixes, that is, powers of 1000 (<font SIZE="-1">KB, MB,</font> etc), as defined in the International System of Units (<font SIZE="-1">SI</font>), instead of the usual base 2 prefixes, that is, powers of 1024 (KiB, MiB, etc).</p>
<dt>&#8211;confirm-quit</p>
<dd> Requires a confirmation before quitting ncdu. Very helpful when you accidentally press &#8216;q&#8217; during or after a very long scan.</dl>
<h3>Scan Options</h3>
<p> These options affect the scanning progress, and have no effect when importing directory information from a file.</p>
<dl>
<dt>-x</p>
<dd> Do not cross filesystem boundaries, i.e. only count files and directories on the same filesystem as the directory being scanned.</p>
<dt>&#8211;exclude <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i></p>
<dd> Exclude files that match <i></i><font SIZE="-1"><i>PATTERN</i></font><i></i>. The files will still be displayed by default, but are not counted towards the disk usage statistics. This argument can be added multiple times to add more patterns.</p>
<dt>-X <i></i><font SIZE="-1"><i>FILE</i></font><i></i>, &#8211;exclude-from <i></i><font SIZE="-1"><i>FILE</i></font><i></i></p>
<dd> Exclude files that match any pattern in <i></i><font SIZE="-1"><i>FILE</i></font><i></i>. Patterns should be separated by a newline.</p>
<dt>&#8211;exclude-caches</p>
<dd> Exclude directories containing <font SIZE="-1">CACHEDIR.TAG. </font> The directories will still be displayed, but not their content, and they are not counted towards the disk usage statistics. See <a rel="nofollow" href="http://www.brynosaurus.com/cachedir/">http://www.brynosaurus.com/cachedir/</a></dl>
<h2>KEYS</h2>
<dl>
<dt>?</p>
<dd> Show help + keys + about screen</p>
<dt>up, down j, k</p>
<dd> Cycle through the items</p>
<dt>right, enter, l</p>
<dd> Open selected directory</p>
<dt>left, &lt;, h</p>
<dd> Go to parent directory</p>
<dt>n</p>
<dd> Order by filename (press again for descending order)</p>
<dt>s</p>
<dd> Order by filesize (press again for descending order)</p>
<dt>C</p>
<dd> Order by number of items (press again for descending order)</p>
<dt>a</p>
<dd> Toggle between showing disk usage and showing apparent size.</p>
<dt>d</p>
<dd> Delete the selected file or directory. An error message will be shown when the contents of the directory do not match or do not exist anymore on the filesystem.</p>
<dt>t</p>
<dd> Toggle dirs before files when sorting.</p>
<dt>g</p>
<dd> Toggle between showing percentage, graph, both, or none. Percentage is relative to the size of the current directory, graph is relative to the largest item in the current directory.</p>
<dt>c</p>
<dd> Toggle display of child item counts.</p>
<dt>e</p>
<dd> Show/hide &#8216;hidden&#8217; or &#8216;excluded&#8217; files and directories. Please note that even though you can&#8217;t see the hidden files and directories, they are still there and they are still included in the directory sizes. If you suspect that the totals shown at the bottom of the screen are not correct, make sure you haven&#8217;t enabled this option.</p>
<dt>i</p>
<dd> Show information about the current selected item.</p>
<dt>r</p>
<dd> Refresh/recalculate the current directory.</p>
<dt>b</p>
<dd> Spawn shell in current directory. </p>
<p> Ncdu will determine your preferred shell from the <tt>&quot;NCDU_SHELL&quot;</tt> or <tt>&quot;SHELL&quot;</tt> variable (in that order), or will call <tt>&quot;/bin/sh&quot;</tt> if neither are set. This allows you to also configure another command to be run when he &#8216;b&#8217; key is pressed. For example, to spawn the <i><a href="/docs/linux/man/1-vifm/">vifm</a></i>(1) file manager instead of a shell, run ncdu as follows: </p>
<pre>
  export NCDU_SHELL=vifm
  ncdu
</pre>
<dt>q</p>
<dd> Quit</dl>
<h2>EXAMPLES</h2>
<p> To scan and browse the directory you&#8217;re currently in, all you need is a simple: </p>
<pre>
  ncdu
</pre>
<p> If you want to scan a full filesystem, your root filesystem, for example, then you&#8217;ll want to use <tt>&quot;-x&quot;</tt>: </p>
<pre>
  ncdu -x /
</pre>
<p> Since scanning a large directory may take a while, you can scan a directory and export the results for later viewing: </p>
<pre>
  ncdu -1xo- / | gzip &gt;export.gz
  # ...some time later:
  zcat export.gz | ncdu -f-
</pre>
<p> To export from a cron job, make sure to replace <tt>&quot;-1&quot;</tt> with <tt>&quot;-0&quot;</tt> to suppress any unnecessary output. </p>
<p> You can also export a directory and browse it once scanning is done: </p>
<pre>
  ncdu -o- | tee export.file | ./ncdu -f-
</pre>
<p> The same is possible with gzip compression, but is a bit kludgey: </p>
<pre>
  ncdu -o- | gzip | tee export.gz | gunzip | ./ncdu -f-
</pre>
<p> To scan a system remotely, but browse through the files locally: </p>
<pre>
  ssh -C user [at] system ncdu -o- / | ./ncdu -f-
</pre>
<p> The <tt>&quot;-C&quot;</tt> option to ssh enables compression, which will be very useful over slow links. Remote scanning and local viewing has two major advantages when compared to running ncdu directly on the remote system: You can browse through the scanned directory on the local system without any network latency, and ncdu does not keep the entire directory structure in memory when exporting, so you won&#8217;t consume much memory on the remote system.</p>
<h2>HARD LINKS</h2>
<p> Every disk usage analysis utility has its own way of (not) counting hard links. There does not seem to be any universally agreed method of handling hard links, and it is even inconsistent among different versions of ncdu. This section explains what each version of ncdu does. </p>
<p> ncdu 1.5 and below does not support any hard link detection at all: each link is considered a separate inode and its size is counted for every link. This means that the displayed directory sizes are incorrect when analyzing directories which contain hard links. </p>
<p> ncdu 1.6 has basic hard link detection: When a link to a previously encountered inode is detected, the link is considered to have a file size of zero bytes. Its size is not counted again, and the link is indicated in the browser interface with a &#8216;H&#8217; mark. The displayed directory sizes are only correct when all links to an inode reside within that directory. When this is not the case, the sizes may or may not be correct, depending on which links were considered as &#8220;duplicate&#8221; and which as &#8220;original&#8221;. The indicated size of the topmost directory (that is, the one specified on the command line upon starting ncdu) is always correct. </p>
<p> ncdu 1.7 and later has improved hard link detection. Each file that has more than two links has the &#8220;H&#8221; mark visible in the browser interface. Each hard link is counted exactly once for every directory it appears in. The indicated size of each directory is therefore, correctly, the sum of the sizes of all unique inodes that can be found in that directory. Note, however, that this may not always be same as the space that will be reclaimed after deleting the directory, as some inodes may still be accessible from hard links outside it.</p>
<h2>BUGS</h2>
<p> Directory hard links are not supported. They will not be detected as being hard links, and will thus be scanned and counted multiple times. </p>
<p> Some minor glitches may appear when displaying filenames that contain multibyte or multicolumn characters. </p>
<p> All sizes are internally represented as a signed 64bit integer. If you have a directory larger than 8 EiB minus one byte, ncdu will clip its size to 8 EiB minus one byte. When deleting items in a directory with a clipped size, the resulting sizes will be incorrect. </p>
<p> Item counts are stored in a signed 32-bit integer without overflow detection. If you have a directory with more than 2 billion files, quite literally anything can happen. </p>
<p> Please report any other bugs you may find at the bug tracker, which can be found on the web site at <a rel="nofollow" href="https://dev.yorhel.nl/ncdu">https://dev.yorhel.nl/ncdu</a></p>
<h2>AUTHOR</h2>
<p> Written by Yoran Heling &lt;projects [at] yorhel.nl&gt;.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-du/">du</a></i>(1) </p>
<h2>Index</h2>
