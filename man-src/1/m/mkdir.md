---
title: "mkdir(1)"
name: "mkdir"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mkdir/"
description: "mkdir – make directories"
---

<h2 class="name">NAME</h2>
<p> mkdir &#8211; make directories </p>
<h2>SYNOPSIS</h2>
<p> <code>mkdir</code> [<i>,OPTION/</i>]&#8230; <i>,DIRECTORY/</i>&#8230;</p>
<h2>DESCRIPTION</h2>
<p> Create the DIRECTORY(ies), if they do not already exist. </p>
<p> Mandatory arguments to long options are mandatory for short options too.</p>
<dl>
<dt><code>-m</code>, <code>&#8211;mode</code>=<i>,MODE/</i></p>
<dd> set file mode (as in chmod), not a=rwx &#8211; umask</p>
<dt><code>-p</code>, <code>&#8211;parents</code></p>
<dd> no error if existing, make parent directories as needed</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd> print a message for each created directory</p>
<dt><code>-Z</code></p>
<dd> set SELinux security context of each created directory to the default type</p>
<dt><code>&#8211;context</code>[=<i>,CTX/</i>]</p>
<dd> like <code>-Z</code>, or if CTX is specified then set the SELinux or SMACK security context to CTX</p>
<dt><code>&#8211;help</code></p>
<dd> display this help and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version information and exit</dl>
<h2>AUTHOR</h2>
<p> Written by David MacKenzie.</p>
<h2>REPORTING BUGS</h2>
<p> GNU coreutils online help: &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/">https://www.gnu.org/software/coreutils/</a>&gt;<br />
 Report any translation bugs to &lt;<a rel="nofollow" href="https://translationproject.org/team/">https://translationproject.org/team/</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2020 Free Software Foundation, Inc. License GPLv3+: GNU GPL version 3 or later &lt;<a rel="nofollow" href="https://gnu.org/licenses/gpl.html">https://gnu.org/licenses/gpl.html</a>&gt;.<br />
 This is free software: you are free to change and redistribute it. There is NO WARRANTY, to the extent permitted by law.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-mkdir/">mkdir</a>(2) </p>
<p> Full documentation &lt;<a rel="nofollow" href="https://www.gnu.org/software/coreutils/mkdir">https://www.gnu.org/software/coreutils/mkdir</a>&gt;<br />
 or available locally via: info &#8216;(coreutils) mkdir invocation&#8217; </p>
<h2>Index</h2>
