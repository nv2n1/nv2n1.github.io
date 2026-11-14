---
title: "go-build(1)"
name: "go-build"
section: "1"
letter: "g"
url: "/docs/linux/man/1-go-build/"
description: "go-build – compile the packages named by the import paths"
---

<h2 class="name">NAME</h2>
<p> go-build &#8211; compile the packages named by the import paths </p>
<h2>SYNOPSIS</h2>
<p> <code>go build</code> [<code>-o</code> <i>output</i>] [<i>build flags</i>] [<i>packages</i>]</p>
<h2>DESCRIPTION</h2>
<p> Build compiles the packages named by the import paths, along with their dependencies, but it does not install the results. </p>
<p> If the arguments to build are a list of .go files from a single directory, build treats them as a list of source files specifying a single package. </p>
<p> When compiling packages, build ignores files that end in &#8216;_test.go&#8217;. </p>
<p> When compiling a single main package, build writes the resulting executable to an output file named after the first source file (&#8216;go build ed.go rx.go&#8217; writes &#8216;ed&#8217; or &#8216;ed.exe&#8217;) or the source code directory (&#8216;go build unix/sam&#8217; writes &#8216;sam&#8217; or &#8216;sam.exe&#8217;). The &#8216;.exe&#8217; suffix is added when writing a Windows executable. </p>
<p> When compiling multiple packages or a single non-main package, build compiles the packages but discards the resulting object, serving only as a check that the packages can be built. </p>
<p> The -o flag forces build to write the resulting executable or object to the named output file or directory, instead of the default behavior described in the last two paragraphs. If the named output is an existing directory or ends with a slash or backslash, then any resulting executables will be written to that directory. </p>
<p> The -i flag installs the packages that are dependencies of the target.<br />
 The -i flag is deprecated. Compiled packages are cached automatically.</p>
<h2>OPTIONS</h2>
<p> The build flags are shared by the build, clean, get, install, list, run, and test commands:</p>
<dl>
<dt><code>-a</code></p>
<dd> force rebuilding of packages that are already up-to-date.</p>
<dt><code>-n</code></p>
<dd> print the commands but do not run them.</p>
<dt><code>-p </code><i>n</i></p>
<dd> the number of programs, such as build commands or test binaries, that can be run in parallel.<br />
 The default is GOMAXPROCS, normally the number of CPUs available.</p>
<dt><code>-race</code></p>
<dd> enable data race detection.<br />
 Supported only on linux/amd64, freebsd/amd64, darwin/amd64, windows/amd64, linux/ppc64le and linux/arm64 (only for 48-bit VMA).</p>
<dt><code>-msan</code></p>
<dd> enable interoperation with memory sanitizer. Supported only on linux/amd64, linux/arm64 and only with Clang/LLVM as the host C compiler. On linux/arm64, pie build mode will be used.</p>
<dt><code>-v</code></p>
<dd> print the names of packages as they are compiled.</p>
<dt><code>-work</code></p>
<dd> print the name of the temporary work directory and do not delete it when exiting.</p>
<dt><code>-x</code></p>
<dd> print the commands. </p>
<dt><code>-asmflags &#8216;[pattern=]</code><i>arg list</i><code>&#8216;</code></p>
<dd> arguments to pass on each go tool asm invocation.</p>
<dt><code>-buildmode</code><i> mode</i></p>
<dd> build mode to use. See &#8216;go help buildmode&#8217; for more.</p>
<dt><code>-compiler</code><i> name</i></p>
<dd> name of compiler to use, as in runtime.Compiler (gccgo or gc)</p>
<dt><code>-gccgoflags &#8216;</code><i>arg list</i><code>&#8216;</code></p>
<dd> arguments to pass on each gccgo compiler/linker invocation</p>
<dt><code>-gcflags &#8216;</code><i>arg list</i><code>&#8216;</code></p>
<dd> arguments to pass on each go tool compile invocation.</p>
<dt><code>-installsuffix </code><i>suffix</i></p>
<dd> a suffix to use in the name of the package installation directory, in order to keep output separate from default builds. If using the -race flag, the install suffix is automatically set to race or, if set explicitly, has _race appended to it. Likewise for the -msan flag. Using a -buildmode option that requires non-default compile flags has a similar effect.</p>
<dt><code>-ldflags &#8216;</code><i>flag list</i><code>&#8216;</code></p>
<dd> arguments to pass on each go tool link invocation.</p>
<dt><code>-linkshared</code></p>
<dd> build code that will be linked against shared libraries previously created with -buildmode=shared.</p>
<dt><code>-mod </code><i>mode</i></p>
<dd> module download mode to use: readonly, vendor, or mod. By default, if a vendor directory is present and the go version in go.mod is 1.14 or higher, the go command acts as if -mod=vendor were set. Otherwise, the go command acts as if -mod=readonly were set. See <a rel="nofollow" href="https://golang.org/ref/mod#build-commands">https://golang.org/ref/mod#build-commands</a> for details.</p>
<dt><code>-modcacherw</code></p>
<dd> leave newly-created directories in the module cache read-write instead of making them read-only.</p>
<dt><code>-modfile </code><i>file</i></p>
<dd> in module aware mode, read (and possibly write) an alternate go.mod file instead of the one in the module root directory. A file named &quot;go.mod&quot; must still be present in order to determine the module root directory, but it is not accessed. When -modfile is specified, an alternate go.sum file is also used: its path is derived from the -modfile flag by trimming the &quot;.mod&quot; extension and appending &quot;.sum&quot;.</p>
<dt><code>-overlay </code><i>file</i></p>
<dd> read a JSON config file that provides an overlay for build operations. The file is a JSON struct with a single field, named &#8216;Replace&#8217;, that maps each disk file path (a string) to its backing file path, so that a build will run as if the disk file path exists with the contents given by the backing file paths, or as if the disk file path does not exist if its backing file path is empty. Support for the -overlay flag has some limitations: importantly, cgo files included from outside the include path must be in the same directory as the Go package they are included from, and overlays will not appear when binaries and tests are run through go run and go test respectively.</p>
<dt><code>-pkgdir </code><i>dir</i></p>
<dd> install and load all packages from dir instead of the usual locations. For example, when building with a non-standard configuration, use -pkgdir to keep generated packages in a separate location.</p>
<dt><code>-tags </code>tag,list</p>
<dd> a comma-separated list of build tags to consider satisfied during the build. For more information about build tags, see the description of build constraints in the documentation for the go/build package. (Earlier versions of Go used a space-separated list, and that form is deprecated but still recognized.)</p>
<dt><code>-trimpath</code></p>
<dd> remove all file system paths from the resulting executable. Instead of absolute file system paths, the recorded file names will begin with either &quot;go&quot; (for the standard library), or a module path [at] version (when using modules), or a plain import path (when using GOPATH).</p>
<dt><code>-toolexec &#8216;</code><i>cmd args</i><code>&#8216;</code></p>
<dd> a program to use to invoke toolchain programs like vet and asm. For example, instead of running asm, the go command will run &#8216;cmd args /path/to/asm &lt;arguments for asm&gt;&#8217;.<br />
 The TOOLEXEC_IMPORTPATH environment variable will be set, matching &#8216;go list -f &#123;&#123;.ImportPath}}&#8217; for the package being built. </p>
</dl>
<p> The -asmflags, -gccgoflags, -gcflags, and -ldflags flags accept a space-separated list of arguments to pass to an underlying tool during the build. To embed spaces in an element in the list, surround it with either single or double quotes. The argument list may be preceded by a package pattern and an equal sign, which restricts the use of that argument list to the building of packages matching that pattern (see &#8216;go help packages&#8217; for a description of package patterns). Without a pattern, the argument list applies only to the packages named on the command line. The flags may be repeated with different patterns in order to specify different arguments for different sets of packages. If a package matches patterns given in multiple flags, the latest match on the command line wins. For example, &#8216;go build -gcflags=-S fmt&#8217; prints the disassembly only for package fmt, while &#8216;go build -gcflags=all=-S fmt&#8217; prints the disassembly for fmt and all its dependencies. </p>
<p> For more about specifying packages, see <code><a href="/docs/linux/man/7-go-packages/">go-packages</a></code>(7).<br />
 For more about where packages and binaries are installed, see <code><a href="/docs/linux/man/1-go-gopath/">go-gopath</a></code>(1).<br />
 For more about calling between Go and C/C++, run &#8216;go help c&#8217;. </p>
<p> Note: Build adheres to certain conventions such as those described by &#8216;go help gopath&#8217;. Not all projects can follow these conventions, however. Installations that have their own conventions or that use a separate software build system may choose to use lower-level invocations such as &#8216;go tool compile&#8217; and &#8216;go tool link&#8217; to avoid some of the overheads and design decisions of the build tool.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-go-install/">go-install</a></code>(1), <code><a href="/docs/linux/man/1-go-get/">go-get</a></code>(1), <code><a href="/docs/linux/man/1-go-clean/">go-clean</a></code>(1).</p>
<h2>AUTHOR</h2>
<p> This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of &#8216;go help build&#8217; for the Debian project (and may be used by others). </p>
<h2>Index</h2>
