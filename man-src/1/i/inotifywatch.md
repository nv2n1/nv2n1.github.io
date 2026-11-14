---
title: "inotifywatch(1)"
name: "inotifywatch"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inotifywatch/"
description: "inotifywatch – gather filesystem access statistics using inotify"
---

<h2 class="name">NAME</h2>
<p> inotifywatch &#8211; gather filesystem access statistics using inotify</p>
<h2>SYNOPSIS</h2>
<p> <code>inotifywatch</code> [<code>-hvzrqf</code>] [<code>-e</code> &lt;event&gt; ] [<code>-t</code> &lt;seconds&gt; ] [<code>-a</code> &lt;event&gt; ] [<code>-d</code> &lt;event&gt; ] &lt;file&gt; [ &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>inotifywatch</code> listens for filesystem events using Linux&#8217;s <code><a href="/docs/linux/man/7-inotify/">inotify</a>(7)</code> interface, then outputs a summary count of the events received on each file or directory. </p>
<h2>OUTPUT</h2>
<p> <code>inotifywatch</code> will output a table on standard out with one column for each type of event and one row for each watched file or directory. The table will show the amount of times each event occurred for each watched file or directory. Output can be sorted by a particular event using the <code>-a</code> or <code>-d</code> options. </p>
<p> Some diagnostic information will be output on standard error. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Output some helpful usage information. </p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Output some extra information on standard error during execution.</p>
<dt><code>@&lt;file&gt;</code></p>
<dd> When watching a directory tree recursively, exclude the specified file from being watched. The file must be specified with a relative or absolute path according to whether a relative or absolute path is given for watched directories. If a specific path is explicitly both included and excluded, it will always be watched. </p>
<p> <code>Note:</code> If you need to watch a directory or file whose name starts with @, give the absolute path.</p>
<dt><code>&#8211;fromfile &lt;file&gt;</code></p>
<dd> Read filenames to watch or exclude from a file, one filename per line. If filenames begin with @ they are excluded as described above. If &lt;file&gt; is `-&#8216;, filenames are read from standard input. Use this option if you need to watch too many files to pass in as command line arguments.</p>
<dt><code>-z, &#8211;zero</code></p>
<dd> Output table rows and columns even if all elements are zero. By default, rows and columns are only output if they contain non-zero elements. Using this option when watching for every event on a lot of files can result in a <i>lot</i> of output! </p>
<dt><code>&#8211;exclude &lt;pattern&gt;</code></p>
<dd> Do not process any events whose filename matches the specified POSIX extended regular expression, case sensitive. </p>
<dt><code>&#8211;excludei &lt;pattern&gt;</code></p>
<dd> Do not process any events whose filename matches the specified POSIX extended regular expression, case insensitive. </p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Watch all subdirectories of any directories passed as arguments. Watches will be set up recursively to an unlimited depth. Symbolic links are not traversed. If new directories are created within watched directories they will automatically be watched. </p>
<p> <code>Warning:</code> If you use this option while watching the root directory of a large tree, it may take quite a while until all inotify watches are established, and events will not be received in this time. Also, since one inotify watch will be established per subdirectory, it is possible that the maximum amount of inotify watches per user will be reached. The default maximum is 8192; it can be increased by writing to <code>/proc/sys/fs/inotify/max_user_watches</code>. </p>
<dt><code>-t &lt;seconds&gt;, &#8211;timeout &lt;seconds&gt;</code></p>
<dd> Listen only for the specified amount of seconds. If not specified, inotifywatch will gather statistics until receiving an interrupt signal by (for example) pressing CONTROL-C at the console. </p>
<dt><code>-e &lt;event&gt;, &#8211;event &lt;event&gt;</code></p>
<dd> Listen for specific event(s) only. The events which can be listened for are listed in the <code>EVENTS</code> section. This option can be specified more than once. If omitted, all events are listened for. </p>
<dt><code>-a &lt;event&gt;, &#8211;ascending &lt;event&gt;</code></p>
<dd> Sort output ascending by event counts for the specified event. Sortable events include `total&#8217; and all the events listed in the <code>EVENTS</code> section except `move&#8217; and `close&#8217; (you must use `moved_to&#8217;, `moved_from&#8217;, `close_write&#8217; or `close_nowrite&#8217; instead). The default is to sort descending by `total&#8217;. </p>
<dt><code>-d &lt;event&gt;, &#8211;descending &lt;event&gt;</code></p>
<dd> Sort output descending by event counts for the specified event. Sortable events include `total&#8217; and all the events listed in the <code>EVENTS</code> section except `move&#8217; and `close&#8217; (you must use `moved_to&#8217;, `moved_from&#8217;, `close_write&#8217; or `close_nowrite&#8217; instead). The default is to sort descending by `total&#8217;. </p>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The program executed successfully.</p>
<dt><code>1</code></p>
<dd> An error occurred in execution of the program. </p>
</dl>
<h2>EVENTS</h2>
<p> The following events are valid for use with the <code>-e</code> option: </p>
<dl>
<dt><code>access</code></p>
<dd> A watched file or a file within a watched directory was read from. </p>
<dt><code>modify</code></p>
<dd> A watched file or a file within a watched directory was written to. </p>
<dt><code>attrib</code></p>
<dd> The metadata of a watched file or a file within a watched directory was modified. This includes timestamps, file permissions, extended attributes etc. </p>
<dt><code>close_write</code></p>
<dd> A watched file or a file within a watched directory was closed, after being opened in writeable mode. This does not necessarily imply the file was written to. </p>
<dt><code>close_nowrite</code></p>
<dd> A watched file or a file within a watched directory was closed, after being opened in read-only mode. </p>
<dt><code>close</code></p>
<dd> A watched file or a file within a watched directory was closed, regardless of how it was opened. Note that this is actually implemented simply by listening for both <code>close_write</code> and <code>close_nowrite,</code> hence all close events received will be output as one of these, not <code>CLOSE.</code> </p>
<dt><code>open</code></p>
<dd> A watched file or a file within a watched directory was opened. </p>
<dt><code>moved_to</code></p>
<dd> A file or directory was moved into a watched directory. This event occurs even if the file is simply moved from and to the same directory. </p>
<dt><code>moved_from</code></p>
<dd> A file or directory was moved from a watched directory. This event occurs even if the file is simply moved from and to the same directory. </p>
<dt><code>move</code></p>
<dd> A file or directory was moved from or to a watched directory. Note that this is actually implemented simply by listening for both <code>moved_to</code> and <code>moved_from,</code> hence all close events received will be output as one or both of these, not <code>MOVE.</code> </p>
<dt><code>move_self</code></p>
<dd> A watched file or directory was moved. After this event, the file or directory is no longer being watched. </p>
<dt><code>create</code></p>
<dd> A file or directory was created within a watched directory. </p>
<dt><code>delete</code></p>
<dd> A file or directory within a watched directory was deleted. </p>
<dt><code>delete_self</code></p>
<dd> A watched file or directory was deleted. After this event the file or directory is no longer being watched. Note that this event can occur even if it is not explicitly being listened for. </p>
<dt><code>unmount</code></p>
<dd> The filesystem on which a watched file or directory resides was unmounted. After this event the file or directory is no longer being watched. Note that this event can occur even if it is not explicitly being listened to. </p>
</dl>
<h2>EXAMPLE</h2>
<p> Watching the `~/.beagle&#8217; directory for 60 seconds: </p>
<pre>
% inotifywatch -v -e access -e modify -t 60 -r ~/.beagle
Establishing watches...
Setting up watch(es) on /home/rohan/.beagle
OK, /home/rohan/.beagle is now being watched.
Total of 302 watches.
Finished establishing watches, now collecting statistics.
Will listen for events for 60 seconds.
total  access  modify  filename
1436   1074    362     /home/rohan/.beagle/Indexes/FileSystemIndex/PrimaryIndex/
1323   1053    270     /home/rohan/.beagle/Indexes/FileSystemIndex/SecondaryIndex/
303    116     187     /home/rohan/.beagle/Indexes/KMailIndex/PrimaryIndex/
261    74      187     /home/rohan/.beagle/TextCache/
206    0       206     /home/rohan/.beagle/Log/
42     0       42      /home/rohan/.beagle/Indexes/FileSystemIndex/Locks/
18     6       12      /home/rohan/.beagle/Indexes/FileSystemIndex/
12     0       12      /home/rohan/.beagle/Indexes/KMailIndex/Locks/
3      0       3       /home/rohan/.beagle/TextCache/54/
3      0       3       /home/rohan/.beagle/TextCache/bc/
3      0       3       /home/rohan/.beagle/TextCache/20/
3      0       3       /home/rohan/.beagle/TextCache/62/
2      2       0       /home/rohan/.beagle/Indexes/KMailIndex/SecondaryIndex/
</pre>
<h2>CAVEATS</h2>
<p> When using inotifywatch, the filename that is outputted is not guaranteed to be up to date after a move because it is the inode that is being monitored. Additionally, none of the observed operations are guaranteed to have been performed on the filename inotifywatch was instructed to monitor in cases when the file is known by several names in the filesystem. </p>
<h2>BUGS</h2>
<p> There are race conditions in the recursive directory watching code which can cause events to be missed if they occur in a directory immediately after that directory is created. This is probably not fixable. </p>
<p> It is assumed the inotify event queue will never overflow. </p>
<h2>AUTHORS</h2>
<p> inotifywatch is written by Rohan McGovern &lt;rohan [at] mcgovern.id.au&gt;. </p>
<p> inotifywatch is part of inotify-tools. The inotify-tools website is located at: <i><a rel="nofollow" href="http://inotify-tools.sourceforge.net/">http://inotify-tools.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-inotifywait/">inotifywait</a>(1), <a href="/docs/linux/man/7-inotify/">inotify</a>(7) </p>
<h2>Index</h2>
