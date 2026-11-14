---
title: "incrontab(5)"
name: "incrontab"
section: "5"
letter: "i"
url: "/docs/linux/man/5-incrontab/"
description: "incrontab – tables for driving inotify cron (incron)"
---

<p>incrontab &#8211; tables for driving inotify cron (incron)</p>
<h2>Description</h2>
<p>An incrontab file contains instructions to the <i><a href="/docs/linux/man/8-incrond/">incrond</a></i>(8) daemon of the general form: &quot;run this command on these file events&quot;. There are two categories of tables: system tables (with root privileges) and user tables (with user privileges). System tables are (by default) located in /etc/incron.d and may have any names. Each system table exists separately inside incron and their watches never collide. Each user has their own table, and commands in any given incrontab will be executed as the user who owns the incrontab. System users (such as apache, postfix, nobody etc.) may have their own incrontab. incrontab files are read when the <i><a href="/docs/linux/man/8-incrond/">incrond</a></i>(8) daemon starts and after any change (incrontab file are being hooked when incrond is running). Blank lines are ignored. The general line format is the following: </p>
<pre><code>&lt;path&gt; &lt;mask&gt; &lt;command&gt;</code></pre>
<p> Where <i>path</i> is an absolute filesystem path, <i>mask</i> is an event mask (in symbolic or numeric form) and <i>command</i> is an executable file (or a script) with its arguments. See bellow for event mask symbols. The executable file may be noted as an absolute path or only as the name itself (PATH locations are examined). Please remember that the same path may occur only once per table (otherwise only the first occurrence takes effect and an error message is emitted to the system log).</p>
<h2>Event Symbols</h2>
<p>These basic event mask symbols are defined: </p>
<p> <code>IN_ACCESS</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File was accessed (read) (*)</p>
<p> <code>IN_ATTRIB</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Metadata changed (permissions, timestamps, extended attributes, etc.) (*)</p>
<p> <code>IN_CLOSE_WRITE</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File opened for writing was closed (*)</p>
<p> <code>IN_CLOSE_NOWRITE</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File not opened for writing was closed (*)</p>
<p> <code>IN_CREATE</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File/directory created in watched directory (*)</p>
<p> <code>IN_DELETE</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File/directory deleted from watched directory (*)</p>
<p> <code>IN_DELETE_SELF</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Watched file/directory was itself deleted</p>
<p> <code>IN_MODIFY</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File was modified (*)</p>
<p> <code>IN_MOVE_SELF</code> <tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Watched file/directory was itself moved</p>
<p> <code>IN_MOVED_FROM</code> <tt>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File moved out of watched directory (*)</p>
<p> <code>IN_MOVED_TO</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File moved into watched directory (*)</p>
<p> <code>IN_OPEN</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>File was opened (*)</p>
<p> When monitoring a directory, the events marked with an asterisk (*) above can occur for files in the directory, in which case the name field in the returned event data identifies the name of the file within the directory. </p>
<p> The <code>IN_ALL_EVENTS</code> symbol is defined as a bit mask of all of the above events. Two additional convenience symbols are <code>IN_MOVE</code>, which is a combination of <code>IN_MOVED_FROM</code> and <code>IN_MOVED_TO</code>, and <code>IN_CLOSE</code> which combines <code>IN_CLOSE_WRITE</code> and <code>IN_CLOSE_NOWRITE</code>. </p>
<p> The following further symbols can be specified in the mask:<br />
&nbsp;<wbr> <code>IN_DONT_FOLLOW</code> <tt>&nbsp;<wbr></tt>Don&#8217;t dereference pathname if it is a symbolic link</p>
<p> <code>IN_ONESHOT</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Monitor pathname for only one event</p>
<p> <code>IN_ONLYDIR</code> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>Only watch pathname if it is a directory</p>
<p> Additionaly, there is a symbol which doesn&#8217;t appear in the inotify symbol set. It it <code>IN_NO_LOOP</code>. This symbol disables monitoring events until the current one is completely handled (until its child process exits).</p>
<h2>Wildcards</h2>
<p>The following wildards may be used inside command specification: </p>
<p> <code>$$</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>dollar sign</p>
<p> <code>$@</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>watched filesystem path (see above)</p>
<p> <code>$#</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>event-related file name</p>
<p> <code>$%</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>event flags (textually)</p>
<p> <code>$&amp;</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>event flags (numerically)</p>
<h2>Example</h2>
<p>These are some example rules which can be used in an incrontab file: <code>/tmp IN_ALL_EVENTS abcd $@/$# $%</code> <code>/usr/bin IN_ACCESS,IN_NO_LOOP abcd $#</code> <code>/home IN_CREATE /usr/local/bin/abcd $#</code> <code>/var/log 12 abcd $@/$#</code> The first line monitors all events on the /tmp directory. When an event occurs it runs a application called &#8216;abcd&#8217; with the full path of the file as the first arguments and the event flags as the second one. The second line monitors accesses (readings) on the /usr/bin directory. The application &#8216;abcd&#8217; is run as a handler and the appropriate event watch is disabled until the program finishes. The file name (without the directory path) is passed in as an argument. The third example is used for monitoring the /home directory for newly create files or directories (it practically means an event is sent when a new user is added). This event is processed by a program specified by an absolute path. And the final line shows how to use numeric event mask instead of textual one. The value 12 is exactly the same as IN_ATTRIB,IN_CLOSE_WRITE. </p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-incrond/">incrond</a>(8), <a href="/docs/linux/man/1-incrontab/">incrontab</a>(1), <a href="/docs/linux/man/5-incron-conf/">incron.conf</a>(5)</p>
<h2>Author</h2>
<p>Lukas Jelinek &lt;lukas [at] aiken.cz&gt; (please report bugs to <a rel="nofollow" href="http://bts.aiken.cz">http://bts.aiken.cz</a> or &lt;bugs [at] aiken.cz&gt;).</p>
<h2>Copying</h2>
<p>This program is free software. It can be used, redistributed and/or modified under the terms of the GNU General Public License, version 2.</p>
