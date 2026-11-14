---
title: "go-clean(1)"
name: "go-clean"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-clean/"
description: "go-clean – remove object files and cached files"
---

<h2 class="name">NAME</h2>
<p> go-clean &#8211; remove object files and cached files </p>
<h2>SYNOPSIS</h2>
<p> <code>go clean</code> [<code>-i</code>] [<code>-r</code>] [<code>-n</code>] [<code>-x</code>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Clean removes object files from package source directories. The go command builds most objects in a temporary directory, so go clean is mainly concerned with object files left by other tools or by manual invocations of go build. </p>
<p> If a package argument is given or the -i or -r flag is set, clean removes the following files from each of the source directories corresponding to the import paths:</p>
<dl>
<dt><code>_obj/</code></p>
<dd> old object directory, left from Makefiles</p>
<dt><code>_test/</code></p>
<dd> old test directory, left from Makefiles</p>
<dt><code>_testmain.go</code></p>
<dd> old gotest file, left from Makefiles</p>
<dt><code>test.out</code></p>
<dd> old test log, left from Makefiles</p>
<dt><code>build.out</code></p>
<dd> old test log, left from Makefiles</p>
<dt><code>*.[568ao]</code></p>
<dd> object files, left from Makefiles </p>
<dt><code>DIR(.exe)</code></p>
<dd> from go build</p>
<dt><code>DIR.test(.exe)</code></p>
<dd> from go test -c</p>
<dt><code>MAINFILE(.exe)</code></p>
<dd> from go build MAINFILE.go</p>
<dt><code>*.so</code></p>
<dd> from SWIG</dl>
<p> In the list, DIR represents the final path element of the directory, and MAINFILE is the base name of any Go source file in the directory that is not included when building the package.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-i</code></p>
<dd> The -i flag causes clean to remove the corresponding installed archive or binary (what &#8216;go install&#8217; would create).</p>
<dt><code>-n</code></p>
<dd> The -n flag causes clean to print the remove commands it would execute, but not run them.</p>
<dt><code>-r</code></p>
<dd> The -r flag causes clean to be applied recursively to all the dependencies of the packages named by the import paths.</p>
<dt><code>-x</code></p>
<dd> The -x flag causes clean to print remove commands as it executes them.</p>
<dt><code>-cache</code></p>
<dd> The -cache flag causes clean to remove the entire go build cache.</p>
<dt><code>-testcache</code></p>
<dd> The -testcache flag causes clean to expire all test results in the go build cache.</p>
<dt><code>-modcache</code></p>
<dd> The -modcache flag causes clean to remove the entire module download cache, including unpacked source code of versioned dependencies.</dl>
<p> For more about build flags, see <code><a href="/docs/linux/man/1-go-build/">go-build</a></code>(1). </p>
<p> For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help clean&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
