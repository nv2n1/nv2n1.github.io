---
title: "chgrp(1)"
name: "chgrp"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chgrp/"
description: "chgrp – change group ownership"
---

<h2 class="name">NAME</h2>
<p> chgrp &#8211; change group ownership </p>
<h2>SYNOPSIS</h2>
<p> <code>chgrp</code> [<i>,OPTION/</i>]&#8230; <i>,GROUP FILE/</i>&#8230;<br />
 <code>chgrp</code> [<i>,OPTION/</i>]&#8230; <i>,&#8211;reference=RFILE FILE/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Change the group of each FILE to GROUP. With <code>&#8211;reference</code>, change the group of each FILE to that of RFILE.</p>
<dl>
<dt><code>-c</code>, <code>&#8211;changes</code></p>
<dd> like verbose but report only when a change is made</p>
<dt><code>-f</code>, <code>&#8211;silent</code>, <code>&#8211;quiet</code></p>
<dd> suppress most error messages</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> output a diagnostic for every file processed</p>
<dt><code>&#8211;dereference</code></p>
<dd> affect the referent of each symbolic link (this is the default), rather than the symbolic link itself</p>
<dt><code>-h</code>, <code>&#8211;no-dereference</code></p>
<dd> affect symbolic links instead of any referenced file (useful only on systems that can change the ownership of a symlink)</p>
<dt><code>&#8211;no-preserve-root</code></p>
<dd> do not treat &#8216;/&#8217; specially (the default)</p>
<dt><code>&#8211;preserve-root</code></p>
<dd> fail to operate recursively on &#8216;/&#8217;</p>
<dt><code>&#8211;reference</code>=<i>,RFILE/</i></p>
<dd> use RFILE&#8217;s group rather than specifying a GROUP value</p>
<dt><code>-R</code>, <code>&#8211;recursive</code></p>
<dd> operate on files and directories recursively</dl>
<p> The following options modify how a hierarchy is traversed when the <code>-R</code> option is also specified. If more than one is specified, only the final one takes effect.</p>
<dl>
<dt><code>-H</code></p>
<dd> if a command line argument is a symbolic link to a directory, traverse it</p>
<dt><code>-L</code></p>
<dd> traverse every symbolic link to a directory encountered</p>
<dt><code>-P</code></p>
<dd> do not traverse any symbolic links (default)</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>chgrp staff /u</p>
<dd> Change the group of /u to &quot;staff&quot;.</p>
<dt>chgrp -hR staff /u</p>
<dd> Change the group of /u and subfiles to &quot;staff&quot;.</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie and Jim Meyering.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-chown/">chown</a>(1), <a href="/docs/linux/man/2-chown/">chown</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/chgrp">https://www.gnu.org/software/coreutils/chgrp</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) chgrp invocation&#8217; </p>
<h2>Index</h2>
