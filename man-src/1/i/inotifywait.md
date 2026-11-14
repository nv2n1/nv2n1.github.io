---
title: "inotifywait(1)"
name: "inotifywait"
section: "1"
letter: "i"
url: "/docs/linux/man/1-inotifywait/"
description: "inotifywait – wait for changes to files using inotify"
---

<h2 class="name">NAME</h2>
<p> inotifywait &#8211; wait for changes to files using inotify</p>
<h2>SYNOPSIS</h2>
<p> <code>inotifywait</code> [<code>-hcmrq</code>] [<code>-e</code> &lt;event&gt; ] [<code>-t</code> &lt;seconds&gt; ] [<code>&#8211;format</code> &lt;fmt&gt; ] [<code>&#8211;timefmt</code> &lt;fmt&gt; ] &lt;file&gt; [ &#8230; ] </p>
<h2>DESCRIPTION</h2>
<p> <code>inotifywait</code> efficiently waits for changes to files using Linux&#8217;s <code><a href="/docs/linux/man/7-inotify/">inotify</a>(7)</code> interface. It is suitable for waiting for changes to files from shell scripts. It can either exit once an event occurs, or continually execute and output events as they occur. </p>
<h2>OUTPUT</h2>
<p> <code>inotifywait</code> will output diagnostic information on standard error and event information on standard output. The event output can be configured, but by default it consists of lines of the following form: </p>
<p> <code>watched_filename EVENT_NAMES event_filename</code> </p>
<dl>
<dt><code>watched_filename</code></p>
<dd> is the name of the file on which the event occurred. If the file is a directory, a trailing slash is output.</p>
<dt><code>EVENT_NAMES</code></p>
<dd> are the names of the inotify events which occurred, separated by commas.</p>
<dt><code>event_filename</code></p>
<dd> is output only when the event occurred on a directory, and in this case the name of the file within the directory which caused this event is output. </p>
<p> By default, any special characters in filenames are not escaped in any way. This can make the output of inotifywait difficult to parse in awk scripts or similar. The <code>&#8211;csv</code> and <code>&#8211;format</code> options will be helpful in this case. </p>
</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Output some helpful usage information.</p>
<dt><code>@&lt;file&gt;</code></p>
<dd> When watching a directory tree recursively, exclude the specified file from being watched. The file must be specified with a relative or absolute path according to whether a relative or absolute path is given for watched directories. If a specific path is explicitly both included and excluded, it will always be watched. </p>
<p> <code>Note:</code> If you need to watch a directory or file whose name starts with @, give the absolute path.</p>
<dt><code>&#8211;fromfile &lt;file&gt;</code></p>
<dd> Read filenames to watch or exclude from a file, one filename per line. If filenames begin with @ they are excluded as described above. If &lt;file&gt; is `-&#8216;, filenames are read from standard input. Use this option if you need to watch too many files to pass in as command line arguments.</p>
<dt><code>-m, &#8211;monitor</code></p>
<dd> Instead of exiting after receiving a single event, execute indefinitely. The default behaviour is to exit after the first event occurs.</p>
<dt><code>-d, &#8211;daemon</code></p>
<dd> Same as &#8211;monitor, except run in the background logging events to a file that must be specified by &#8211;outfile. Implies &#8211;syslog.</p>
<dt><code>-o, &#8211;outfile &lt;file&gt;</code></p>
<dd> Output events to &lt;file&gt; rather than stdout.</p>
<dt><code>-s, &#8211;syslog</code></p>
<dd> Output errors to <code><a href="/docs/linux/man/3-syslog/">syslog</a>(3)</code> system log module rather than stderr.</p>
<dt><code>-r, &#8211;recursive</code></p>
<dd> Watch all subdirectories of any directories passed as arguments. Watches will be set up recursively to an unlimited depth. Symbolic links are not traversed. Newly created subdirectories will also be watched. </p>
<p> <code>Warning:</code> If you use this option while watching the root directory of a large tree, it may take quite a while until all inotify watches are established, and events will not be received in this time. Also, since one inotify watch will be established per subdirectory, it is possible that the maximum amount of inotify watches per user will be reached. The default maximum is 8192; it can be increased by writing to <code>/proc/sys/fs/inotify/max_user_watches</code>. </p>
<dt><code>-q, &#8211;quiet</code></p>
<dd> If specified once, the program will be less verbose. Specifically, it will not state when it has completed establishing all inotify watches. </p>
<p> If specified twice, the program will output nothing at all, except in the case of fatal errors. </p>
<dt><code>&#8211;exclude &lt;pattern&gt;</code></p>
<dd> Do not process any events whose filename matches the specified POSIX extended regular expression, case sensitive. </p>
<dt><code>&#8211;excludei &lt;pattern&gt;</code></p>
<dd> Do not process any events whose filename matches the specified POSIX extended regular expression, case insensitive. </p>
<dt><code>-t &lt;seconds&gt;, &#8211;timeout &lt;seconds&gt;</code></p>
<dd> Exit if an appropriate event has not occurred within &lt;seconds&gt; seconds. If &lt;seconds&gt; is zero (the default), wait indefinitely for an event. </p>
<dt><code>-e &lt;event&gt;, &#8211;event &lt;event&gt;</code></p>
<dd> Listen for specific event(s) only. The events which can be listened for are listed in the <code>EVENTS</code> section. This option can be specified more than once. If omitted, all events are listened for. </p>
<dt><code>-c, &#8211;csv</code></p>
<dd> Output in CSV (comma-separated values) format. This is useful when filenames may contain spaces, since in this case it is not safe to simply split the output at each space character. </p>
<dt><code>&#8211;timefmt &lt;fmt&gt;</code></p>
<dd> Set a time format string as accepted by <a href="/docs/linux/man/3-strftime/">strftime</a>(3) for use with the `%T&#8217; conversion in the &#8211;format option. </p>
<dt><code>&#8211;format &lt;fmt&gt;</code></p>
<dd> Output in a user-specified format, using printf-like syntax. The event strings output are limited to around 4000 characters and will be truncated to this length. The following conversions are supported: </p>
<dt>%w</p>
<dd> This will be replaced with the name of the Watched file on which an event occurred. </p>
<dt>%f</p>
<dd> When an event occurs within a directory, this will be replaced with the name of the File which caused the event to occur. Otherwise, this will be replaced with an empty string. </p>
<dt>%e</p>
<dd> Replaced with the Event(s) which occurred, comma-separated. </p>
<dt>%Xe</p>
<dd> Replaced with the Event(s) which occurred, separated by whichever character is in the place of `X&#8217;. </p>
<dt>%T</p>
<dd> Replaced with the current Time in the format specified by the &#8211;timefmt option, which should be a format string suitable for passing to <a href="/docs/linux/man/3-strftime/">strftime</a>(3). </p>
</dl>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></p>
<dd> The program executed successfully, and an event occurred which was being listened for.</p>
<dt><code>1</code></p>
<dd> An error occurred in execution of the program, or an event occurred which was not being listened for. The latter generally occurs if something happens which forcibly removes the inotify watch, such as a watched file being deleted or the filesystem containing a watched file being unmounted.</p>
<dt><code>2</code></p>
<dd> The <code>-t</code> option was used and an event did not occur in the specified interval of time. </p>
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
<h2>EXAMPLES</h2>
<h3>Example 1</h3>
<p> Running inotifywait at the command-line to wait for any file in the `test&#8217; directory to be accessed. After running inotifywait, `cat test/foo&#8217; is run in a separate console. </p>
<pre>
% inotifywait test
Setting up watches.
Watches established.
test/ ACCESS foo
</pre>
<h3>Example 2</h3>
<p> A short shell script to efficiently wait for httpd-related log messages and do something appropriate. </p>
<pre><code>
#!/ bin / sh
while
    inotifywait - e modify / var / log / messages;
do
    if tail
        - n1 / var / log / messages | grep httpd;
then
    kdialog-- msgbox "Apache needs love!" fi
        done
</code></pre>
<h3>Example 3</h3>
<p> A custom output format is used to watch `~/test&#8217;. Meanwhile, someone runs `touch ~/test/badfile; touch ~/test/goodfile; rm ~/test/badfile&#8217; in another console. </p>
<pre>
% inotifywait -m -r --format '%:e %f' ~/test
Setting up watches.  Beware: since -r was given, this may take a while!
Watches established.
CREATE badfile
OPEN badfile
ATTRIB badfile
CLOSE_WRITE:CLOSE badfile
CREATE goodfile
OPEN goodfile
ATTRIB goodfile
CLOSE_WRITE:CLOSE goodfile
DELETE badfile
</pre>
<h2>CAVEATS</h2>
<p> When using inotifywait, the filename that is outputted is not guaranteed to be up to date after a move because it is the inode that is being monitored. Additionally, none of the observed operations are guaranteed to have been performed on the filename inotifywait was instructed to monitor in cases when the file is known by several names in the filesystem. </p>
<h2>BUGS</h2>
<p> There are race conditions in the recursive directory watching code which can cause events to be missed if they occur in a directory immediately after that directory is created. This is probably not fixable. </p>
<p> It is assumed the inotify event queue will never overflow. </p>
<h2>AUTHORS</h2>
<p> inotifywait is written and maintained by Rohan McGovern &lt;rohan [at] mcgovern.id.au&gt;. </p>
<p> inotifywait is part of inotify-tools. The inotify-tools website is located at: <i><a rel="nofollow" href="http://inotify-tools.sourceforge.net/">http://inotify-tools.sourceforge.net/</a></i> </p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-inotifywatch/">inotifywatch</a>(1), <a href="/docs/linux/man/3-strftime/">strftime</a>(3), <a href="/docs/linux/man/7-inotify/">inotify</a>(7) </p>
<h2>Index</h2>
