---
title: "ksplice-create(8)"
name: "ksplice-create"
section: "8"
letter: "k"
url: "/docs/linux/man/8-ksplice-create/"
description: "ksplice-create – Create a set of kernel modules for a rebootless kernel update"
---

<p>ksplice-create &#8211; Create a set of kernel modules for a rebootless kernel update</p>
<h2>Synopsis</h2>
<p><code>ksplice-create</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>&#8211;patch=</code><i></i><font SIZE="-1"><i>PATCH_FILE</i></font><i></i> <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> </p>
<p> <code>ksplice-create</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>&#8211;diffext=</code><i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i> <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> </p>
<p> <code>ksplice-create</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>&#8211;git=</code><i></i><font SIZE="-1"><i>COMMIT</i></font><i></i> <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> </p>
<p> <code>ksplice-create</code> [<i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i>] <code>&#8211;prebuild</code> <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i></p>
<h2>Description</h2>
<p><code>ksplice-create</code> creates a set of Ksplice kernel modules that, when loaded, will apply a user-specified source code patch to the running binary kernel. </p>
<p> Before you use <code>ksplice-create</code> on a patch, you should confirm that the desired source code change does not make any semantic changes to kernel data structures&#8212;that is, changes that would require existing instances of kernel data structures to be transformed (e.g., a patch that adds a field to a global data structure would require the existing data structures to change). If you use Ksplice on a patch that changes data structure semantics, Ksplice will not detect the problem and you could experience kernel problems as a result. </p>
<p> The to-be-applied source code patch can be specified by providing a <i><a href="/docs/linux/man/1-patch/">patch</a></i>(1) file (<code>&#8211;patch=</code><i></i><font SIZE="-1"><i>PATCH_FILE</i></font><i></i>) or by providing a file extension (<code>&#8211;diffext=</code><i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>). </p>
<p> If a file extension is specified, then the desired source code patch will be determined by comparing all of the files in the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory tree whose names end with the extra extension <i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i> against the corresponding files without the extra extension. Only the new files containing the extra extension in their filenames should be modified. </p>
<p> Here is an example of using a file extension to specify a patch: </p>
<pre> $ cp KERNEL_SOURCE/kernel/sys.c KERNEL_SOURCE/kernel/sys.c.prctl_fixed
 [edit sys.c.prctl_fixed to include the desired changes]
 $ ksplice-create --diffext=.prctl_fixed KERNEL_SOURCE</pre>
<p><font SIZE="-1">KERNEL_SOURCE</font> must be a directory containing the to-be-updated kernel&#8217;s original source code. If your Linux distribution applies patches to the Linux kernel during the kernel build process, then those patches must be applied to the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory before invoking <code>ksplice-create</code> on that directory. <code>ksplice-create</code> will not modify the source code in the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory tree, but it will perform a kernel build in that directory tree. </p>
<p> <i></i><font SIZE="-1"><i>ORIG_CONFIG</i></font><i></i> can be used to specify the directory containing the to-be-updated kernel&#8217;s original <i>.config</i> file and original <i>System.map</i> file (the files should have exactly those names). <i></i><font SIZE="-1"><i>ORIG_CONFIG</i></font><i></i> defaults to <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i><code>/ksplice</code>. </p>
<p> The default <i><a href="/docs/linux/man/1-gcc/">gcc</a></i>(1) compiler and <i><a href="/docs/linux/man/1-as/">as</a></i>(1) assembler on the system should be as close to the compiler and assembler originally used to build the running kernel as possible. If the current compiler and linker are too different from the original compiler and linker, <code>ksplice-apply</code> will abort when applying the update. </p>
<p> <code>ksplice-create</code> outputs a <i><a href="/docs/linux/man/1-tar/">tar</a></i>(1) file, compressed with <i><a href="/docs/linux/man/1-gzip/">gzip</a></i>(1), containing the desired Ksplice update modules. This tarball will be created in the current directory, and it can be manipulated using the other Ksplice utilities, such as <code>ksplice-apply</code>. </p>
<p> The first time that <code>ksplice-create</code> is invoked on a <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory, it must build that kernel from scratch, which is much slower than the rest of the update-creation process. <code>&#8211;prebuild</code> can be used to perform this initial kernel build without providing a source code patch. </p>
<p> In order to patch a function that has previously been patched by Ksplice, the user needs to ensure that the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory provided to Ksplice contains the source for the currently running kernel, including any patches that have previously been applied by Ksplice.</p>
<h2>Options</h2>
<dl>
<dt><code>&#8211;patch=</code><i></i><font SIZE="-1"><i>PATCH_FILE</i></font><i></i></p>
<dd>Builds a Ksplice update out of the given <i><a href="/docs/linux/man/1-patch/">patch</a></i>(1) file <i></i><font SIZE="-1"><i>PATCH_FILE</i></font><i></i>.</p>
<dt><code>&#8211;diffext=</code><i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i></p>
<dd>Builds a Ksplice update using the modified source files with names ending in <i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i>. The patch will be determined by comparing all of the files in the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> directory tree whose names end with the extra extension <i></i><font SIZE="-1"><i>EXTENSION</i></font><i></i> against the corresponding files without the extra extension.</p>
<dt><code>&#8211;git</code>=<i></i><font SIZE="-1"><i>COMMIT</i></font><i></i></p>
<dd>Builds a Ksplice update using the commit <i></i><font SIZE="-1"><i>COMMIT</i></font><i></i> in the Git working tree <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i>. The original state corresponding to the running kernel is remembered in the Git ref <code>refs/ksplice/pre</code>, which will be created from the current <font SIZE="-1"><code>HEAD</code></font> if it does not yet exist (and can be changed using the <code>&#8211;series</code> option). Therefore, the source code change to be applied corresponds to the output of <code>git diff ksplice/pre</code> <i></i><font SIZE="-1"><i>COMMIT</i></font><i></i>.</p>
<dt><code>&#8211;prebuild</code></p>
<dd>Compiles the original source code that will be needed to build future Ksplice updates. If any Ksplice updates have previously been built in the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> tree, the source files in the tree are reverted to their original state.</p>
<dt><code>&#8211;series</code></p>
<dd>Specifies that the current state of the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> tree should be used as the original source that corresponds to the running kernel. If a Ksplice update has recently been built in the <i></i><font SIZE="-1"><i>KERNEL_SOURCE</i></font><i></i> tree, this option specifies that the Ksplice update being built should be applied after the previous update in series. This option can be used with <code>&#8211;prebuild</code> to forget the previous original state and perform no other action.</p>
<dt><code>&#8211;build-modules</code></p>
<dd>For a patch that includes changes to kernel modules, in addition to building a hot update that can be applied to the running kernel, this option will cause <code>ksplice-create</code> to generate a set of new modules based on the updated source code. These modules can be used to replace the kernel modules stored on disk, where they can later be loaded normally after part of the hot update has been applied using <i><a href="/docs/linux/man/1-ksplice-apply/">ksplice-apply</a></i>(1) <code>&#8211;partial</code>.</p>
<dt><code>-v</code>, <code>&#8211;verbose</code></p>
<dd>Causes <code>ksplice-create</code> to print debugging messages about its progress. Using multiple -v options increases the verbosity. The maximum is 2.</p>
<dt><code>-j</code> <i></i><font SIZE="-1"><i>JOBS</i></font><i></i>, <code>&#8211;jobs=</code><i></i><font SIZE="-1"><i>JOBS</i></font><i></i></p>
<dd>Specifies the number of jobs to run simultaneously while performing kernel builds. <code>ksplice-create</code> also honors the environment variable <font SIZE="-1">CONCURRENCY_LEVEL</font>.</p>
<dt><code>&#8211;patch-opt=</code><i></i><font SIZE="-1"><i>OPTIONS</i></font><i></i></p>
<dd>Can be used to pass options to <i><a href="/docs/linux/man/1-patch/">patch</a></i>(1). If this option is <font SIZE="-1">NOT</font> specified, then <code>-p1</code> is passed to <code>patch</code>. If this option is specified, then only the specified options will be passed to <code>patch</code>. This option can be repeated in order to pass multiple options to <code>patch</code>. This option is ignored when the to-be-applied source code patch is specified using <code>&#8211;diffext</code>.</p>
<dt><code>&#8211;id=</code><i></i><font SIZE="-1"><i>ID</i></font><i></i></p>
<dd>Specifies the unique value that will be used as the identifier of the Ksplice update. This identifier will, for example, appear in the name of the update tarball. By default, a random 8-character <font SIZE="-1">ID</font> will be generated.</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-ksplice-apply/">ksplice-apply</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-view/">ksplice-view</a></i>(8), <i><a href="/docs/linux/man/8-ksplice-undo/">ksplice-undo</a></i>(8)</p>
<h2>Bugs</h2>
<p>Please report bugs to &lt;devel [at] ksplice.com&gt;.</p>
<h2>Authors</h2>
<p>Jeff Arnold, Anders Kaseorg, and Tim Abbott</p>
<h2>Copyright</h2>
<p>Copyright (C) 2007-2009 Ksplice, Inc. </p>
<p> This is free software and documentation. You can redistribute and/or modify it under the terms of the <font SIZE="-1">GNU</font> General Public License, version 2.</p>
