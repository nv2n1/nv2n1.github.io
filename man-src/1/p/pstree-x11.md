---
title: "pstree-x11(1)"
name: "pstree-x11"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pstree-x11/"
description: "pstree – display a tree of processes"
---

<p>pstree &#8211; display a tree of processes </p>
<h2>Synopsis</h2>
<p><code>pstree</code> [<code>-a</code>,<code>&nbsp;&#8211;arguments</code>] [<code>-c</code>,<code>&nbsp;&#8211;compact-not</code>] [<code>-C</code>,<code>&nbsp;&#8211;color&nbsp;</code><i>attr</i>] [<code>-g</code>,<code>&nbsp;&#8211;show-pgids</code>] [<code>-h</code>,<code>&nbsp;&#8211;highlight-all</code>,<code>&nbsp;-H</code><i>&nbsp;pid</i>,<code>&nbsp;&#8211;highlight-pid&nbsp;</code><i>pid</i>] [<code>-l</code>,<code>&nbsp;&#8211;long</code>] [<code>-n</code>,<code>&nbsp;&#8211;numeric-sort</code>] [<code>-N</code>,<code>&nbsp;&#8211;ns-sort&nbsp;</code><i>ns</i>] [<code>-p</code>,<code>&nbsp;&#8211;show-pids</code>] [<code>-s</code>,<code>&nbsp;&#8211;show-parents</code>] [<code>-S</code>,<code>&nbsp;&#8211;ns-changes</code>] [<code>-t</code>,<code>&nbsp;&#8211;thread-names</code>] [<code>-T</code>,<code>&nbsp;&#8211;hide-threads</code>] [<code>-u</code>,<code>&nbsp;&#8211;uid-changes</code>] [<code>-Z</code>,<code>&nbsp;&#8211;security-context</code>] [<code>-A</code>,<code>&nbsp;&#8211;ascii</code>,<code>&nbsp;-G</code>,<code>&nbsp;&#8211;vt100</code>,<code>&nbsp;-U</code>,<code>&nbsp;&#8211;unicode</code>] [<i>pid</i>,<code>&nbsp;</code><i>user</i>]<br />
 <code>pstree</code> <code>-V</code>,<code>&nbsp;&#8211;version</code></p>
<h2>Description</h2>
<p><code>pstree</code> shows running processes as a tree. The tree is rooted at either <i>pid</i> or <code>init</code> if <i>pid</i> is omitted. If a user name is specified, all process trees rooted at processes owned by that user are shown. </p>
<p> <code>pstree</code> visually merges identical branches by putting them in square brackets and prefixing them with the repetition count, e.g. </p>
<pre> init-+-getty
 |-getty
 |-getty
 `-getty</pre>
<p>becomes </p>
<pre> init---4*[getty]</pre>
<p>Child threads of a process are found under the parent process and are shown with the process name in curly braces, e.g. </p>
<pre> icecast2---13*[{icecast2}]</pre>
<p>If <code>pstree</code> is called as <code>pstree.x11</code> then it will prompt the user at the end of the line to press return and will not return until that has happened. This is useful for when <code>pstree</code> is run in a xterminal. </p>
<p> Certain kernel or mount parameters, such as the <i>hidepid</i> option for procfs, will hide information for some processes. In these situations <code>pstree</code> will attempt to build the tree without this information, showing process names as question marks. </p>
<h2>Options</h2>
<dl COMPACT>
<dt><code>-a</code></p>
<dd>Show command line arguments. If the command line of a process is swapped out, that process is shown in parentheses. <code>-a</code> implicitly disables compaction for processes but not threads.</p>
<dt><code>-A</code></p>
<dd>Use ASCII characters to draw the tree.</p>
<dt><code>-c</code></p>
<dd>Disable compaction of identical subtrees. By default, subtrees are compacted whenever possible.</p>
<dt><code>-C</code></p>
<dd>Color the process name by given attribute. Currently <code>pstree</code> only accepts the value <code>age</code> which colors by process age. Processes newer than 60 seconds are green, newer than an hour yellow and the remaining red.</p>
<dt><code>-g</code></p>
<dd>Show PGIDs. Process Group IDs are shown as decimal numbers in parentheses after each process name. <code>-g</code> implicitly disables compaction. If both PIDs and PGIDs are displayed then PIDs are shown first.</p>
<dt><code>-G</code></p>
<dd>Use VT100 line drawing characters.</p>
<dt><code>-h</code></p>
<dd>Highlight the current process and its ancestors. This is a no-op if the terminal doesn&#8217;t support highlighting or if neither the current process nor any of its ancestors are in the subtree being shown.</p>
<dt><code>-H</code></p>
<dd>Like <code>-h</code>, but highlight the specified process instead. Unlike with <code>-h</code>, <code>pstree</code> fails when using <code>-H</code> if highlighting is not available.</p>
<dt><code>-l</code></p>
<dd>Display long lines. By default, lines are truncated to either the COLUMNS environment variable or the display width. If neither of these methods work, the default of 132 columns is used.</p>
<dt><code>-n</code></p>
<dd>Sort processes with the same parent by PID instead of by name. (Numeric sort.)</p>
<dt><code>-N</code></p>
<dd>Show individual trees for each namespace of the type specified. The available types are: <i>ipc</i>, <i>mnt</i>, <i>net</i>, <i>pid</i>, <i>time</i>, <i>user</i>, <i>uts</i>. Regular users don&#8217;t have access to other users&#8217; processes information, so the output will be limited.</p>
<dt><code>-p</code></p>
<dd>Show PIDs. PIDs are shown as decimal numbers in parentheses after each process name. <code>-p</code> implicitly disables compaction.</p>
<dt><code>-s</code></p>
<dd>Show parent processes of the specified process.</p>
<dt><code>-S</code></p>
<dd>Show namespaces transitions. Like <code>-N</code>, the output is limited when running as a regular user.</p>
<dt><code>-t</code></p>
<dd>Show full names for threads when available.</p>
<dt><code>-T</code></p>
<dd>Hide threads and only show processes.</p>
<dt><code>-u</code></p>
<dd>Show uid transitions. Whenever the uid of a process differs from the uid of its parent, the new uid is shown in parentheses after the process name.</p>
<dt><code>-U</code></p>
<dd>Use UTF-8 (Unicode) line drawing characters. Under Linux 1.1-54 and above, UTF-8 mode is entered on the console with <code>echo -e &#8216;%8&#8217;</code> and left with <code>echo -e &#8216;%@&#8217;</code>.</p>
<dt><code>-V</code></p>
<dd>Display version information.</p>
<dt><code>-Z</code></p>
<dd>Show the current security attributes of the process. For SELinux systems this will be the security context.</dl>
<h2>Files</h2>
<dl COMPACT>
<dt>/proc</p>
<dd>location of the proc file system</dl>
<h2>Bugs</h2>
<p>Some character sets may be incompatible with the VT100 characters.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-ps/">ps</a></code>(1), <code><a href="/docs/linux/man/1-top/">top</a></code>(1), <code><a href="/docs/linux/man/5-proc/">proc</a></code>(5).</p>
