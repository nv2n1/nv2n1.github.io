---
title: "depmod-d(5)"
name: "depmod-d"
section: "5"
letter: "d"
url: "/docs/linux/man/5-depmod-d/"
description: "depmod.d – Configuration directory for depmod"
---

<p>depmod.d &#8211; Configuration directory for depmod</p>
<h2>Synopsis</h2>
<p>/usr/lib/depmod.d/*.conf </p>
<p> /usr/local/lib/depmod.d/*.conf </p>
<p> /run/depmod.d/*.conf </p>
<p> /etc/depmod.d/*.conf</p>
<h2>Description</h2>
<p>The order in which modules are processed by the <code>depmod</code> command can be altered on a global or per-module basis. This is typically useful in cases where built-in kernel modules are complemented by custom built versions of the same and the user wishes to affect the priority of processing in order to override the module version supplied by the kernel. </p>
<p> The format of files under depmod.d is simple: one command per line, with blank lines and lines starting with &#8216;#&#8217; ignored (useful for adding comments). A &#8216;\&#8217; at the end of a line causes it to continue on the next line, which makes the files a bit neater.</p>
<h2>Commands</h2>
<p>search <i>subdirectory&#8230;</i></p>
<dl>
<dd>This allows you to specify the order in which /lib/modules (or other configured module location) subdirectories will be processed by <code>depmod</code>. Directories are listed in order, with the highest priority given to the first listed directory and the lowest priority given to the last directory listed. The special keyword <code>built-in</code> refers to the standard module directories installed by the kernel. Another special keyword <code>external</code> refers to the list of external directories, defined by the <code>external</code> command. </p>
<p> By default, depmod will give a higher priority to a directory with the name <code>updates</code> using this built-in search string: &quot;updates built-in&quot; but more complex arrangements are possible and are used in several popular distributions.</dl>
<p> override <i>modulename</i> <i>kernelversion</i> <i>modulesubdirectory</i></p>
<dl>
<dd>This command allows you to override which version of a specific module will be used when more than one module sharing the same name is processed by the <code>depmod</code> command. It is possible to specify one kernel or all kernels using the * wildcard. <i>modulesubdirectory</i> is the name of the subdirectory under /lib/modules (or other module location) where the target module is installed. </p>
<p> For example, it is possible to override the priority of an updated test module called <code>kmod</code> by specifying the following command: &quot;override kmod * extra&quot;. This will ensure that any matching module name installed under the <code>extra</code> subdirectory within /lib/modules (or other module location) will take priority over any likenamed module already provided by the kernel.</dl>
<p> external <i>kernelversion</i> <i>absolutemodulesdirectory&#8230;</i></p>
<dl>
<dd>This specifies a list of directories, which will be checked according to the priorities in the <code>search</code> command. The order matters also, the first directory has the higher priority. </p>
<p> The <i>kernelversion</i> is a POSIX regular expression or * wildcard, like in the <code>override</code>.</dl>
<h2>Copyright</h2>
<p>This manual page Copyright 2006-2010, Jon Masters, Red Hat, Inc.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-depmod/">depmod</a></code>(8)</p>
<h2>Authors</h2>
<p><code>Jon Masters</code> &lt;jcm [at] jonmasters.org&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Robby Workman</code> &lt;rworkman [at] slackware.com&gt;</p>
<dl>
<dd>Developer</dl>
<p> <code>Lucas De Marchi</code> &lt;lucas.de.marchi [at] gmail.com&gt;</p>
<dl>
<dd>Developer</dl>
