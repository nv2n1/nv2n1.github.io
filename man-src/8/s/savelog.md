---
title: "savelog(8)"
name: "savelog"
section: "8"
letter: "s"
url: "/docs/linux/man/8-savelog/"
description: "savelog – save a log file"
---

<p>savelog &#8211; save a log file</p>
<h2>Synopsis</h2>
<p><code>savelog</code> [-m mode] [-u user] [-g group] [-t] [-p] [-c cycle] [-l] [-j] [-J] [-1 .. -9] [-C] [-d] [-l] [-r rolldir] [-n] [-q] [-D dateformat] file &#8230;</p>
<h2>Description</h2>
<p>The <code>savelog</code> command saves and optionally compresses old copies of files. Older versions of <i>file</i> are named:</p>
<dl>
<dd><i>file</i>.<i>&lt;number&gt;</i><i>&lt;compress_suffix&gt;</i> </p>
</dl>
<p> where <i>&lt;number&gt;</i> is the version number, 0 being the newest. Version numbers &gt; 0 are compressed unless <code>-l</code> prevents it. Version number 0 is not compressed because a process might still have <i>file</i> opened for I/O. Only <i>cycle</i> versions of the file are kept. </p>
<p> If the file does not exist and <code>-t</code> was given, it will be created. </p>
<p> For files that do exist and have lengths greater than zero, the following actions are performed: </p>
<dl>
<dt>1)</p>
<dd>Version numbered files are cycled. Version <i>file</i><code>.2</code> is moved to version <i>file</i><code>.3</code><i></i>, version <i>file</i><code>.1</code> is moved to version <i>file</i><code>.2</code><i></i>, and so on. Finally version <i>file</i><code>.0</code> is moved to version <i>file</i><code>.1</code><i></i>, and version <i>file</i> is deleted. Both compressed names and uncompressed names are cycled, regardless of <code>-l</code>. Missing version files are ignored.</p>
<dt>2)</p>
<dd>The new <i>file</i><code>.1</code> is compressed unless the <code>-l</code> flag was given. It is changed subject to the <code>-m</code>, <code>-u</code>, and <code>-g</code> flags.</p>
<dt>3)</p>
<dd>The main <i>file</i> is moved to <i>file</i><code>.0</code><i></i>.</p>
<dt>4)</p>
<dd>If the <code>-m</code>, <code>-u</code>, <code>-g</code>, <code>-t</code>, or <code>-p</code> flags are given, then an empty <i>file</i> is created subject to the given flags. With the <code>-p</code> flag, the file is created with the same owner, group, and permissions as before.</p>
<dt>5)</p>
<dd>The new <i>file</i><code>.0</code> is changed subject to the <code>-m</code>, <code>-u</code>, and <code>-g</code> flags.</dl>
<h2>Options</h2>
<dl>
<dt><code>-m mode</code></p>
<dd>chmod the log files to mode, implies <code>-t</code></p>
<dt><code>-u user</code></p>
<dd>chown log files to user, implies <code>-t</code></p>
<dt><code>-g group</code></p>
<dd>chgrp log files to group, implies <code>-t</code></p>
<dt><code>-c cycle</code></p>
<dd>Save cycle versions of the logfile (default: 7). The <i>cycle</i> count must be at least 2.</p>
<dt><code>-t</code></p>
<dd>touch new logfile into existence</p>
<dt><code>-l</code></p>
<dd>don&#8217;t compress any log files (default: do compress)</p>
<dt><code>-p</code></p>
<dd>preserve owner, group, and permissions of logfile</p>
<dt><code>-j</code></p>
<dd>compress with bzip2 instead of gzip</p>
<dt><code>-J</code></p>
<dd>compress with xz instead of gzip </p>
<p> For xz no strength option is set, and xz decides on the default based on the total amount of physical RAM. Note that xz can use a very large amount of memory for the higher compression levels.</p>
<dt><code>-1 .. -9</code></p>
<dd>compression strength or memory usage (default: 9, except for xz)</p>
<dt><code>-C</code></p>
<dd>force cleanup of cycled logfiles</p>
<dt><code>-d</code></p>
<dd>use standard date for rolling</p>
<dt><code>-D dateformat</code></p>
<dd>override date format, in the syntax understood by the <code><a href="/docs/linux/man/1-date/">date</a></code>(1) command</p>
<dt><code>-r</code></p>
<dd>use <i>rolldir</i> instead of . to roll files</p>
<dt><code>-n</code></p>
<dd>do not rotate empty files</p>
<dt><code>-q</code></p>
<dd>be quiet</dl>
<h2>Bugs</h2>
<p>If a process is still writing to <i>file</i><code>.0</code><i></i>, and savelog moves it to <i>file</i><code>.1</code> and compresses it, data could be lost.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-logrotate/">logrotate</a></code>(8) </p>
