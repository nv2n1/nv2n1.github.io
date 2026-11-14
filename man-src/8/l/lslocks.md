---
title: "lslocks(8)"
name: "lslocks"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lslocks/"
description: "lslocks – list local system locks"
---

<p>lslocks &#8211; list local system locks</p>
<h2>Synopsis</h2>
<p><code>lslocks</code> [options]</p>
<h2>Description</h2>
<p><code>lslocks</code> lists information about all the currently held file locks in a Linux system. </p>
<p> Note that lslocks also lists OFD (Open File Description) locks, these locks are not associated with any process (PID is -1). OFD locks are associated with the open file description on which they are acquired. This lock type is available since Linux 3.15, see <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) for more details.</p>
<h2>Options</h2>
<p><code>-b</code>, <code>&#8211;bytes</code></p>
<dl>
<dd>Print the SIZE column in bytes rather than in a human-readable format.</dl>
<p> <code>-i</code>, <code>&#8211;noinaccessible</code></p>
<dl>
<dd>Ignore lock files which are inaccessible for the current user.</dl>
<p> <code>-J</code>, <code>&#8211;json</code></p>
<dl>
<dd>Use JSON output format.</dl>
<p> <code>-n</code>, <code>&#8211;noheadings</code></p>
<dl>
<dd>Do not print a header line.</dl>
<p> <code>-o</code>, <code>&#8211;output</code> <i>list</i></p>
<dl>
<dd>Specify which output columns to print. Use <code>&#8211;help</code> to get a list of all supported columns. </p>
<p> The default list of columns may be extended if <i>list</i> is specified in the format <i>+list</i> (e.g., <code>lslocks -o +BLOCKER</code>).</dl>
<p> <code>&#8211;output-all</code></p>
<dl>
<dd>Output all available columns.</dl>
<p> <code>-p</code>, <code>&#8211;pid</code> <i>pid</i></p>
<dl>
<dd>Display only the locks held by the process with this <i>pid</i>.</dl>
<p> <code>-r</code>, <code>&#8211;raw</code></p>
<dl>
<dd>Use the raw output format.</dl>
<p> <code>-u</code>, <code>&#8211;notruncate</code></p>
<dl>
<dd>Do not truncate text in columns.</dl>
<p> <code>-V</code>, <code>&#8211;version</code></p>
<dl>
<dd>Display version information and exit.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Display help text and exit.</dl>
<h2>Output</h2>
<p>COMMAND</p>
<dl>
<dd>The command name of the process holding the lock.</dl>
<p> PID</p>
<dl>
<dd>The process ID of the process which holds the lock or -1 for OFDLCK.</dl>
<p> TYPE</p>
<dl>
<dd>The type of lock; can be FLOCK (created with <code><a href="/docs/linux/man/2-flock/">flock</a></code>(2)), POSIX (created with <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2) and <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3)) or OFDLCK (created with <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2)).</dl>
<p> SIZE</p>
<dl>
<dd>Size of the locked file.</dl>
<p> MODE</p>
<dl>
<dd>The lock&#8217;s access permissions (read, write). If the process is blocked and waiting for the lock, then the mode is postfixed with an &#8216;*&#8217; (asterisk).</dl>
<p> M</p>
<dl>
<dd>Whether the lock is mandatory; 0 means no (meaning the lock is only advisory), 1 means yes. (See <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2).)</dl>
<p> START</p>
<dl>
<dd>Relative byte offset of the lock.</dl>
<p> END</p>
<dl>
<dd>Ending offset of the lock.</dl>
<p> PATH</p>
<dl>
<dd>Full path of the lock. If none is found, or there are no permissions to read the path, it will fall back to the device&#8217;s mountpoint and &quot;&#8230;&quot; is appended to the path. The path might be truncated; use <code>&#8211;notruncate</code> to get the full path.</dl>
<p> BLOCKER</p>
<dl>
<dd>The PID of the process which blocks the lock.</dl>
<h2>Notes</h2>
<p>The <code>lslocks</code> command is meant to replace the <code><a href="/docs/linux/man/8-lslk/">lslk</a></code>(8) command, originally written by and unmaintained since 2001.</p>
<h2>Authors</h2>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-flock/">flock</a></code>(1), <code><a href="/docs/linux/man/2-fcntl/">fcntl</a></code>(2), <code><a href="/docs/linux/man/3-lockf/">lockf</a></code>(3)</p>
<h2>Reporting Bugs</h2>
<p>For bug reports, use the issue tracker at <i></i> &lt;<a rel="nofollow" href="https://github.com/karelzak/util-linux/issues">https://github.com/karelzak/util-linux/issues</a>&gt;.</p>
<h2>Availability</h2>
<p>The <code>lslocks</code> command is part of the util-linux package which can be downloaded from <i>Linux Kernel Archive</i> &lt;<a rel="nofollow" href="https://www.kernel.org/pub/linux/utils/util-linux/">https://www.kernel.org/pub/linux/utils/util-linux/</a>&gt;.</p>
