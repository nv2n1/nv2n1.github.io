---

title: "sane-config(1)"
name: "sane-config"
section: "1"
letter: "s"
url: "/docs/linux/man/1-sane-config/"
description: "sane-config – get information about the installed version of libsane"
---

<p> sane-config &#8211; get information about the installed version of libsane </p>
<h2>SYNOPSIS</h2>
<p> <code>sane-config [&#8211;prefix] [&#8211;exec-prefix] [&#8211;libs] [&#8211;cflags] [&#8211;ldflags] [&#8211;version] [&#8211;help </code><i>[OPTION]</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>sane-config</code> is a tool that is used to determine the compiler and linker flags that should be used to compile and link <code>SANE</code> frontends to a <code>SANE</code> backend library (libsane).</p>
<h2>OPTIONS</h2>
<p> <code>sane-config</code> accepts the following options (you can&#8217;t use more than one option at the same time):</p>
<dl>
<dt><code>&#8211;version</code></dt>
<dd> Print the currently installed version of libsane on the standard output.</dd>
<dt><code>&#8211;help OPTION</code></dt>
<dd> Print a short usage message. If OPTION is specified, help for that option (e.g. &#8211;libs) is printed (if available).</dd>
<dt><code>&#8211;libs</code></dt>
<dd> Print the additional libraries that are necessary to link a <code>SANE</code> frontend to libsane.</dd>
<dt><code>&#8211;ldflags</code></dt>
<dd> Print the linker flags that are necessary to link a <code>SANE</code> frontend to libsane.</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> Print the compiler flags that are necessary to compile a <code>SANE</code> frontend.</dd>
<dt><code>&#8211;prefix</code></dt>
<dd> Print the prefix used during compilation of libsane.</dd>
<dt><code>&#8211;exec-prefix</code></dt>
<dd> Print the exec-prefix used during compilation of libsane.</dd></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/7-sane/">sane</a></code>(7)</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Julien BLACHE &lt;jblache [at] debian.org&gt;, for the Debian GNU/Linux system (but may be used by others). </p>
