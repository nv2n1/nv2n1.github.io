---
title: "mh-mkstemp(1)"
name: "mh-mkstemp"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mh-mkstemp/"
description: "mkstemp – create a temporary file"
---

<h2 class="name">NAME</h2>
<p> mkstemp &#8211; create a temporary file </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>/usr/libexec/nmh/mkstemp</code> [<code>-directory</code> <i>directory</i>] [<code>-prefix</code> <i>prefix</i>] [<code>-suffix</code> <i>suffix</i>] [<code>-version</code>] [<code>-help</code>]</dl>
<h2>DESCRIPTION</h2>
<p> <code>mkstemp</code></p>
<dd>creates a temporary file using <i><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></i>(3), or if the <code>-suffix</code> switch is available and used, <i><a href="/docs/linux/man/3-mkstemps/">mkstemps</a></i>(3). The file name identifies a unique, newly created file, and always contains 6 characters that appear to be random. </p>
<p> The <code>-directory</code> switch specifies a <i>directory</i> in which to create the file. </p>
<p> The <code>-prefix</code> switch specifies an initial part, before the 6 characters, of the file name. </p>
<p> The <code>-suffix</code> switch is only supported on platforms that provide the <i><a href="/docs/linux/man/3-mkstemps/">mkstemps</a></i>(3) library function. It specifies a <i>suffix</i> to appear after the 6 characters; if it should begin with a special character such as a period, that must be explicit in <i>suffix</i>. </p>
<p> Unlike arguments to most switches of other <code>nmh</code> commands, the arguments to <code>mkstemp</code> switches can begin with a dash.</p>
<h2>EXIT STATUS</h2>
<p> If <code>mkstemp</code> successfully creates the temporary file, it prints the file name on standard output and exits with status 0. On failure, it prints a diagnostic message on standard error and exits with status -1.</p>
<h2>PROFILE COMPONENTS</h2>
<p> None</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/3-mkstemp/">mkstemp</a></i>(3), <i><a href="/docs/linux/man/3-mkstemps/">mkstemps</a></i>(3)</p>
<h2>DEFAULTS</h2>
<dl>
<dt>-directory</p>
<dd> current directory</p>
<dt>-prefix</p>
<dd> none</p>
<dt>-suffix</p>
<dd> none </p>
</dl>
<h2>Index</h2>
