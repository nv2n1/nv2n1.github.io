---
title: "setmode(3)"
name: "setmode"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setmode/"
description: "getmode setmode – modify mode bits"
---

<p><code>getmode</code> <code>setmode</code> &#8211; modify mode bits</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/unistd.h Ft void * Fn setmode const char *mode_str Ft mode_t Fn getmode const void *set mode_t mode</p>
<h2>Description</h2>
<p>The Fn setmode function accepts a string representation of a file mode change, compiles it to binary form, and returns an abstract representation that may be passed to Fn getmode . The string may be an numeric (octal) or symbolic string of the form accepted by <a href="/docs/linux/man/1-chmod/">chmod</a>(1), and may represent either an exact mode to set or a change to make to the existing mode. </p>
<p> The Fn getmode function adjusts the file permission bits given by Fa mode according to the compiled change representation Fa set , and returns the adjusted mode. While only the permission bits are altered, other parts of the file mode, particularly the type, may be examined. </p>
<p> Because some of the possible symbolic values are defined relative to the file creation mask, Fn setmode may call <a href="/docs/linux/man/2-umask/">umask</a>(2), temporarily changing the mask. If this occurs, the file creation mask will be restored before Fn setmode returns. If the calling program changes the value of its file creation mask after calling Fn setmode , Fn setmode must be called again to recompile the mode string if Fn getmode is to modify future file modes correctly. </p>
<p> If the mode passed to Fn setmode is invalid, Fn setmode returns <code>NULL</code> </p>
<p> The value returned from Fn setmode is obtained from Fn malloc and should be returned to the system with Fn free when the program is done with it, generally after a call to Fn getmode .</p>
<h2>Examples</h2>
<p>The effects of the shell command `chmod&#8217; a+x myscript.sh can be duplicated as follows: </p>
<blockquote>
<pre>const char *file = &quot;myscript.sh&quot;;
struct stat st;
mode_t newmode;
stat(file, &amp;st);
newmode = getmode(setmode(&quot;a+x&quot;), st.st_mode);
chmod(file, newmode);</pre>
</blockquote>
<h2>Errors</h2>
<p>The Fn setmode function may fail and set <i>errno</i> for any of the errors specified for the library routines <a href="/docs/linux/man/3-malloc/">malloc</a>(3) or <a href="/docs/linux/man/3-strtol/">strtol</a>(3). In addition, Fn setmode will fail and set <i>errno</i> to:</p>
<dl>
<dt><code>Bq </code>Er EINVAL</p>
<dd>The Fa mode argument does not represent a valid mode.</dl>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-chmod/">chmod</a>(1), <a href="/docs/linux/man/2-stat/">stat</a>(2), <a href="/docs/linux/man/2-umask/">umask</a>(2), <a href="/docs/linux/man/3-malloc/">malloc</a>(3)</p>
<h2>History</h2>
<p>The Fn getmode and Fn setmode functions first appeared in BSD 4.4</p>
<h2>Bugs</h2>
<p>The type of Fa set should really be some opaque struct type used only by these functions rather than Ft void * . </p>
