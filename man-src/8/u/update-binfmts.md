---
title: "update-binfmts(8)"
name: "update-binfmts"
section: "8"
letter: "u"
url: "/docs/linux/man/8-update-binfmts/"
description: "update-binfmts – maintain registry of executable binary formats"
---

<p><code>update-binfmts</code> &#8211; maintain registry of executable binary formats</p>
<h2>Synopsis</h2>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-install</code> <i>name path spec</i> </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-remove</code> <i>name path</i> </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-import</code> [<i>name</i> ] </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-unimport</code> [<i>name</i> ] </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-display</code> [<i>name</i> ] </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-enable</code> [<i>name</i> ] </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-disable</code> [<i>name</i> ] </p>
<p><code>update\-binfmts</code> [<i>options</i> ] &#8211;<code>-find</code> [<i>path</i> ]</p>
<h2>Description</h2>
<p>Versions 2.1.43 and later of the Linux kernel have contained the binfmt_misc module. This enables a system administrator to register interpreters for various binary formats based on a magic number or their file extension, and cause the appropriate interpreter to be invoked whenever a matching file is executed. Think of it as a more flexible version of the #! executable interpreter mechanism, or as something which can behave a little like &quot;associations&quot; in certain other operating systems (though in GNU/Linux the tendency is to keep this sort of thing somewhere else, like your file manager). <code>update\-binfmts</code> manages a persistent database of these interpreters. </p>
<p> When each package providing a registered interpreter is installed, changed, or removed, <code>update\-binfmts</code> is called to update information about that interpreter. <code>update\-binfmts</code> is usually called from the postinst or prerm scripts in Debian packages.</p>
<h2>Options</h2>
<p>Exactly one action must be specified; this may be accompanied by any one of the common options.</p>
<h3>Common Options</h3>
<dl>
<dt><code>&#8211;package </code><i>package-name</i></p>
<dd>Specifies the name of the current package, to be used by package post-installation and pre-removal scripts. System administrators installing binary formats for local use should probably ignore this option. </p>
<p> When installing new formats, the &#8211;<code>-import</code> action should be used instead. Similarly, when removing old formats, the &#8211;<code>-unimport</code> action should be used instead.</p>
<dt><code>&#8211;admindir </code><i>directory</i></p>
<dd>Specifies the administrative directory, when this is to be different from the default of /var/lib/binfmts</p>
<dt><code>&#8211;importdir </code><i>directory</i></p>
<dd>Specifies the directory from which packaged binary formats are imported, when this is to be different from the default of /usr/share/binfmts</p>
<dt><code>&#8211;test</code></p>
<dd>Don&#8217;t do anything, just demonstrate what would be done.</p>
<dt><code>&#8211;help</code></p>
<dd>Display some usage information.</p>
<dt><code>&#8211;version</code></p>
<dd>Display version information.</dl>
<h3>Actions</h3>
<dl>
<dt><code>&#8211;install </code><i>name path spec</i></p>
<dd>Install a binary format identified by <i>name</i> with interpreter <i>path</i> into the database. After registration, this format will be used when the kernel tries to execute a file matching <i>spec</i> (see Sx BINARY FORMAT SPECIFICATIONS below). </p>
<p> &#8211;<code>-install</code> will attempt to enable this binary format in the kernel as well as adding it to its own database; see &#8211;<code>-enable</code> below. </p>
<p> You cannot install a format with any of the names &quot;.&quot;, &quot;..&quot;, &quot;register&quot;, or &quot;status&quot;, as these are used by the filesystem or the binfmt_misc module.</p>
<dt><code>&#8211;remove </code><i>name path</i></p>
<dd>Remove the binary format identified by <i>name</i> with interpreter <i>path</i> from the database. This will also attempt to disable the binary format in the kernel; see &#8211;<code>-disable</code> below.</p>
<dt><code>&#8211;import </code>[<i>name</i> ]</p>
<dd>Import a packaged format file called <i>name</i> or import all format files currently on the system if no <i>name</i> is given. If <i>name</i> is not a full path, it is assumed to be a file in the import directory ( /usr/share/binfmts by default). See Sx FORMAT FILES below for the required contents of these files. </p>
<p> For packages, this is preferable to using the &#8211;<code>-install</code> option, as a format file can be installed without <code>update\-binfmts</code> needing to be available.</p>
<dt><code>&#8211;unimport </code>[<i>name</i> ]</p>
<dd>Unimport a packaged format file called <i>name</i> or unimport all format files currently on the system if no <i>name</i> is given. If <i>name</i> is not a full path, it is assumed to be a file in the import directory ( /usr/share/binfmts by default). See Sx FORMAT FILES below for the required contents of these files. </p>
<p> For packages, this is preferable to using the &#8211;<code>-remove</code> option, for symmetry with &#8211;<code>-import</code></p>
<dt><code>&#8211;display </code>[<i>name</i> ]</p>
<dd>Display any information held in the database about the binary format identifier <i>name</i> or about all known binary formats if no <i>name</i> is given. Also show whether displayed binary formats are enabled or disabled.</p>
<dt><code>&#8211;enable </code>[<i>name</i> ]</p>
<dd>Enable binary format <i>name</i> or all known binary formats if no <i>name</i> is given, in the kernel, thus enabling direct execution of matching files. You must have binfmt_misc compiled into the kernel or loaded as a module for this to work.</p>
<dt><code>&#8211;disable </code>[<i>name</i> ]</p>
<dd>Disable binary format <i>name</i> or all known binary formats if no <i>name</i> is given, in the kernel, thus disabling direct execution of matching files. You must have binfmt_misc compiled into the kernel or loaded as a module for this to work.</p>
<dt><code>&#8211;find </code>[<i>path</i> ]</p>
<dd>Print the list of interpreters that will be tried in sequence when attempting to execute <i>path</i> one per line. The first one for which <a href="/docs/linux/man/3-execvp/">execvp</a>(3) succeeds will be used. </p>
<p> Note that if multiple formats match an executable, then the order is in general not defined, and may not be preserved between <code>update\-binfmts</code> operations, so you should generally try to ensure that this option prints at most one line for any given <i>path</i> The exception to this is that any format with a userspace detector will be run before any format without a userspace detector.</dl>
<h3>Binary Format Specifications</h3>
<dl>
<dt><code>&#8211;magic </code><i>byte-sequence</i></p>
<dd>This matches all files with the magic number <i>byte-sequence</i> Hexadecimal escapes may be included in the <i>byte-sequence</i> by preceding them with 
