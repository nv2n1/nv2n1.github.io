---

title: "update-binfmts(8)"
name: "update-binfmts"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-binfmts/"
description: "update-binfmts – maintain registry of executable binary formats"
---

<p> <code>update-binfmts</code> - maintain registry of executable binary formats </p>
<p> <code>update\-binfmts</code> [<i>options</i> ] -<code>-install</code> <i>name path spec</i> <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-remove</code> <i>name path</i> <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-import</code> [<i>name</i> ] <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-unimport</code> [<i>name</i> ] <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-display</code> [<i>name</i> ] <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-enable</code> [<i>name</i> ] <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-disable</code> [<i>name</i> ] <br />
 <br />
<code>update\-binfmts</code> [<i>options</i> ] -<code>-find</code> [<i>path</i> ]  </p>
<p> Versions 2.1.43 and later of the Linux kernel have contained the binfmt_misc module. This enables a system administrator to register interpreters for various binary formats based on a magic number or their file extension, and cause the appropriate interpreter to be invoked whenever a matching file is executed. Think of it as a more flexible version of the #! executable interpreter mechanism, or as something which can behave a little like &quot;associations&quot; in certain other operating systems (though in GNU/Linux the tendency is to keep this sort of thing somewhere else, like your file manager). <code>update\-binfmts</code> manages a persistent database of these interpreters. </p>
<p>When each package providing a registered interpreter is installed, changed, or removed, <code>update\-binfmts</code> is called to update information about that interpreter. <code>update\-binfmts</code> is usually called from the postinst or prerm scripts in Debian packages.  </p>
<h2>OPTIONS</h2>
<p> Exactly one action must be specified; this may be accompanied by any one of the common options.  </p>
<h3>COMMON OPTIONS</h3>
<dl>
<dt><code>--package </code><i>package-name</i></dt>
<dd> <p> Specifies the name of the current package, to be used by package post-installation and pre-removal scripts. System administrators installing binary formats for local use should probably ignore this option. </p>
<p>When installing new formats, the -<code>-import</code> action should be used instead. Similarly, when removing old formats, the -<code>-unimport</code> action should be used instead. </p>
 </dd>
<dt><code>--admindir </code><i>directory</i></dt>
<dd> <p> Specifies the administrative directory, when this is to be different from the default of /var/lib/binfmts </p>
 </dd>
<dt><code>--importdir </code><i>directory</i></dt>
<dd> <p> Specifies the directory from which packaged binary formats are imported, when this is to be different from the default of /usr/share/binfmts </p>
 </dd>
<dt><code>--test</code></dt>
<dd> <p> Don&#8217;t do anything, just demonstrate what would be done. </p>
 </dd>
<dt><code>--help</code></dt>
<dd> <p> Display some usage information. </p>
 </dd>
<dt><code>--version</code></dt>
<dd> <p> Display version information. </p>
 </dd></dl>
<h3>ACTIONS</h3>
<dl>
<dt><code>--install </code><i>name path spec</i></dt>
<dd> <p> Install a binary format identified by <i>name</i> with interpreter <i>path</i> into the database. After registration, this format will be used when the kernel tries to execute a file matching <i>spec</i> (see Sx BINARY FORMAT SPECIFICATIONS below). </p>
<p>-<code>-install</code> will attempt to enable this binary format in the kernel as well as adding it to its own database; see -<code>-enable</code> below. </p>
<p>You cannot install a format with any of the names &quot;.&quot;, &quot;..&quot;, &quot;register&quot;, or &quot;status&quot;, as these are used by the filesystem or the binfmt_misc module. </p>
 </dd>
<dt><code>--remove </code><i>name path</i></dt>
<dd> <p> Remove the binary format identified by <i>name</i> with interpreter <i>path</i> from the database. This will also attempt to disable the binary format in the kernel; see -<code>-disable</code> below. </p>
 </dd>
<dt><code>--import </code>[<i>name</i> ] </dt>
<dd> <p> Import a packaged format file called <i>name</i> or import all format files currently on the system if no <i>name</i> is given. If <i>name</i> is not a full path, it is assumed to be a file in the import directory ( /usr/share/binfmts by default). See Sx FORMAT FILES below for the required contents of these files. </p>
<p>For packages, this is preferable to using the -<code>-install</code> option, as a format file can be installed without <code>update\-binfmts</code> needing to be available. </p>
 </dd>
<dt><code>--unimport </code>[<i>name</i> ] </dt>
<dd> <p> Unimport a packaged format file called <i>name</i> or unimport all format files currently on the system if no <i>name</i> is given. If <i>name</i> is not a full path, it is assumed to be a file in the import directory ( /usr/share/binfmts by default). See Sx FORMAT FILES below for the required contents of these files. </p>
<p>For packages, this is preferable to using the -<code>-remove</code> option, for symmetry with -<code>-import</code> </p>
 </dd>
<dt><code>--display </code>[<i>name</i> ] </dt>
<dd> <p> Display any information held in the database about the binary format identifier <i>name</i> or about all known binary formats if no <i>name</i> is given. Also show whether displayed binary formats are enabled or disabled. </p>
 </dd>
<dt><code>--enable </code>[<i>name</i> ] </dt>
<dd> <p> Enable binary format <i>name</i> or all known binary formats if no <i>name</i> is given, in the kernel, thus enabling direct execution of matching files. You must have binfmt_misc compiled into the kernel or loaded as a module for this to work. </p>
 </dd>
<dt><code>--disable </code>[<i>name</i> ] </dt>
<dd> <p> Disable binary format <i>name</i> or all known binary formats if no <i>name</i> is given, in the kernel, thus disabling direct execution of matching files. You must have binfmt_misc compiled into the kernel or loaded as a module for this to work. </p>
 </dd>
<dt><code>--find </code>[<i>path</i> ] </dt>
<dd> <p> Print the list of interpreters that will be tried in sequence when attempting to execute <i>path</i> one per line. The first one for which <a href="/docs/linux/man/3-execvp/">execvp</a>(3) succeeds will be used. </p>
<p>Note that if multiple formats match an executable, then the order is in general not defined, and may not be preserved between <code>update\-binfmts</code> operations, so you should generally try to ensure that this option prints at most one line for any given <i>path</i> The exception to this is that any format with a userspace detector will be run before any format without a userspace detector. </p>
 </dd></dl>
<h3>BINARY FORMAT SPECIFICATIONS</h3>
<dl>
<dt><code>--magic </code><i>byte-sequence</i></dt>
<dd> <p> This matches all files with the magic number <i>byte-sequence</i> Hexadecimal escapes may be included in the <i>byte-sequence</i> by preceding them with \x, for example `\x0a&#8217; for a linefeed. Remember to protect such escapes with quotes or an additional backslash to prevent their interpretation by the shell. </p>
<p>Also see -<code>-offset</code> and -<code>-mask</code> </p>
 </dd>
<dt><code>--offset </code><i>offset</i></dt>
<dd> <p> This is the offset of the magic/mask in the file, counted in bytes. The default is 0. Only valid with -<code>-magic</code> </p>
 </dd>
<dt><code>--mask </code><i>byte-sequence</i></dt>
<dd> <p> This mask will be logically-ANDed with the string to be checked against the magic number given with -<code>-magic</code> The default is all 0xff, i.e. no effect. Only valid with -<code>-magic</code> </p>
 </dd>
<dt><code>--extension </code><i>extension</i></dt>
<dd> <p> This matches all files whose names end in Qq Pf . Ar extension . Hexadecimal escapes are not recognized here. Extension matching is case-sensitive. </p>
 </dd>
<dt><code>--detector </code><i>path</i></dt>
<dd> <p> If this option is used, a userspace detector program will be used to check whether the file is suitable for this interpreter. This may be used when the binary format is more complex than can be handled by the kernel&#8217;s format specifications alone. The program should return an exit code of zero if the file is appropriate and non-zero otherwise. This option cannot be used together with -<code>-fix-binary yes</code> </p>
 </dd>
<dt><code>--credentials yes , --credentials no</code></dt>
<dd> <p> Whether to keep the credentials of the original binary to run the interpreter; this is typically useful to run setuid binaries, but has security implications. </p>
 </dd>
<dt><code>--preserve yes , --preserve no</code></dt>
<dd> <p> Whether to preserve the original <code>argv[0]</code> when running the interpreter, rather than overwriting it with the full path to the binary. </p>
 </dd>
<dt><code>--fix-binary yes , --fix-binary no</code></dt>
<dd> <p> Whether to open the interpreter binary immediately and always use the opened image. This allows the interpreter from the host to be used regardless of usage in chroots or different mount namespaces. The default behaviour is <code>no</code> meaning that the kernel should open the interpreter binary lazily when needed. This option requires Linux 4.8 or newer. It cannot be used together with -<code>-detector</code> or with multiple binary formats that share the same magic number, since the kernel will only open a single interpreter binary which will then not be able to detect and execute the real interpreter from inside a chroot or from a different mount namespace. </p>
 </dd></dl>
<h3>FORMAT FILES</h3>
<p> A format file is a sequence of options, one per line, corresponding roughly to the options given to an -<code>-install</code> command. Each option consists of a key, followed by whitespace, followed by a value. </p>
<p>The <i>package</i> option should be set to the current package. The <i>interpreter</i> option should be set to the path to the interpreter that will handle this binary format. The <i>magic</i> <i>offset</i> <i>mask</i> <i>extension</i> <i>detector</i> <i>credentials</i> <i>preserve</i> and <i>fix_binary</i> options correspond to the command-line options of the same names.  </p>
<h2>EXIT STATUS</h2>
<dl>
<dt><code>0</code></dt>
<dd> <p> The requested action was successfully performed. </p>
 </dd>
<dt><code>2</code></dt>
<dd> <p> Problems were encountered whilst parsing the command line or performing the action. </p>
 </dd></dl>
<h2>EXAMPLES</h2>
<p> This format file can be used with an interpreter capable of handling Java .class files: </p>
<pre><code>    package javawrapper
    interpreter /usr/bin/javawrapper
    magic \xca\xfe\xba\xbe
</code></pre>
<p>This corresponds roughly to the following command: </p>
<pre><code>    update-binfmts --package javawrapper \
        --install javawrapper /usr/bin/javawrapper \
        --magic '\xca\xfe\xba\xbe'
</code></pre>
<h2>NOTES</h2>
<p> If you&#8217;re not careful, you can break your system with <code>update\-binfmts.</code> An easy way to do this is to register an ELF binary as a handler for ELF, which will almost certainly cause your system to hang immediately; even if it doesn&#8217;t, you won&#8217;t be able to run <code>update\-binfmts</code> to fix it. In the future <code>update\-binfmts</code> may have some checks to prevent this sort of thing happening accidentally, though of course you can still manipulate the binfmt_misc kernel module directly.  </p>
<h2>AUTHOR</h2>
<p> An -nosplit <code>update\-binfmts</code> is copyright (C) 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011 An Colin Watson Aq cjwatson [at] debian.org . See the GNU General Public License version 3 or later for copying conditions. </p>
<p>You can find the GNU GPL v3 in /usr/share/common-licenses/GPL-3 on any modern Debian system. </p>
<p>Richard Guenther wrote the binfmt_misc kernel module.  </p>
<h2>THANKS</h2>
<p> Ian Jackson wrote <code>update-alternatives</code> and <code>dpkg-divert</code> from which this program borrows heavily. </p>
