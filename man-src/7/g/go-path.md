---
title: "go-path(7)"
name: "go-path"
section: "7"
letter: "g"
url: "/docs/linux/man/7-go-path/"
---

go - tool for managing Go source code

<h2>Description</h2>

The Go path is used to resolve import statements. It is implemented by and documented in the go/build package. 

 The GOPATH environment variable lists places to look for Go code. On Unix, the value is a colon-separated string. On Windows, the value is a semicolon-separated string. On Plan 9, the value is a list. 

 If the environment variable is unset, GOPATH defaults to a subdirectory named &quot;go&quot; in the user's home directory ($HOME/go on Unix, %USERPROFILE%go on Windows), unless that directory holds a Go distribution. Run &quot;go env GOPATH&quot; to see the current GOPATH. 

 See <a rel="nofollow" HREF="https://golang.org/wiki/SettingGOPATH">https://golang.org/wiki/SettingGOPATH</a> to set a custom GOPATH. 

 Each directory listed in GOPATH must have a prescribed structure: 

 The src directory holds source code. The path below src determines the import path or executable name. 

 The pkg directory holds installed package objects. As in the Go tree, each target operating system and architecture pair has its own subdirectory of pkg (pkg/GOOS_GOARCH). 

 If DIR is a directory listed in the GOPATH, a package with source in DIR/src/foo/bar can be imported as &quot;foo/bar&quot; and has its compiled form installed to &quot;DIR/pkg/GOOS_GOARCH/foo/bar.a&quot;. 

 The bin directory holds compiled commands. Each command is named for its source directory, but only the final element, not the entire path. That is, the command with source in DIR/src/foo/quux is installed into DIR/bin/quux, not DIR/bin/foo/quux. The &quot;foo/&quot; prefix is stripped so that you can add DIR/bin to your PATH to get at the installed commands. If the GOBIN environment variable is set, commands are installed to the directory it names instead of DIR/bin. GOBIN must be an absolute path. 

 Here's an example directory layout: 

 <pre> GOPATH=/home/user/gocode
 /home/user/gocode/
 src/
 foo/
 bar/ (go code in package bar)
 x.go
 quux/ (go code in package main)
 y.go
 bin/
 quux (installed command)
 pkg/
 linux_amd64/
 foo/
 bar.a (installed package object)</pre>Go searches each directory listed in GOPATH to find source code, but new packages are always downloaded into the first directory in the list. 

 See <a rel="nofollow" HREF="https://golang.org/doc/code.html">https://golang.org/doc/code.html</a> for an example.

<h3>GOPATH and Modules</h3>

When using modules, GOPATH is no longer used for resolving imports. However, it is still used to store downloaded source code (in GOPATH/pkg/mod) and compiled commands (in GOPATH/bin).

<h3>Internal Directories</h3>

Code in or below a directory named &quot;internal&quot; is importable only by code in the directory tree rooted at the parent of &quot;internal&quot;. Here's an extended version of the directory layout above: 

 <pre> /home/user/go/
 src/
 crash/
 bang/ (go code in package bang)
 b.go
 foo/ (go code in package foo)
 f.go
 bar/ (go code in package bar)
 x.go
 internal/
 baz/ (go code in package baz)
 z.go
 quux/ (go code in package main)
 y.go</pre>The code in z.go is imported as &quot;foo/internal/baz&quot;, but that import statement can only appear in source files in the subtree rooted at foo. The source files foo/f.go, foo/bar/x.go, and foo/quux/y.go can all import &quot;foo/internal/baz&quot;, but the source file crash/bang/b.go cannot. 

 See <a rel="nofollow" HREF="https://golang.org/s/go14internal">https://golang.org/s/go14internal</a> for details.

<h3>Vendor Directories</h3>

Go 1.6 includes support for using local copies of external dependencies to satisfy imports of those dependencies, often referred to as vendoring. 

 Code below a directory named &quot;vendor&quot; is importable only by code in the directory tree rooted at the parent of &quot;vendor&quot;, and only using an import path that omits the prefix up to and including the vendor element. 

 Here's the example from the previous section, but with the &quot;internal&quot; directory renamed to &quot;vendor&quot; and a new foo/vendor/crash/bang directory added: 

 <pre> /home/user/go/
 src/
 crash/
 bang/ (go code in package bang)
 b.go
 foo/ (go code in package foo)
 f.go
 bar/ (go code in package bar)
 x.go
 vendor/
 crash/
 bang/ (go code in package bang)
 b.go
 baz/ (go code in package baz)
 z.go
 quux/ (go code in package main)
 y.go</pre>The same visibility rules apply as for internal, but the code in z.go is imported as &quot;baz&quot;, not as &quot;foo/vendor/baz&quot;. 

 Code in vendor directories deeper in the source tree shadows code in higher directories. Within the subtree rooted at foo, an import of &quot;crash/bang&quot; resolves to &quot;foo/vendor/crash/bang&quot;, not the top-level &quot;crash/bang&quot;. 

 Code in vendor directories is not subject to import path checking (see 'go help importpath'). 

 When 'go get' checks out or updates a git repository, it now also updates submodules. 

 Vendor directories do not affect the placement of new repositories being checked out for the first time by 'go get': those are always placed in the main GOPATH, never in a vendor subtree. 

 See <a rel="nofollow" HREF="https://golang.org/s/go15vendor">https://golang.org/s/go15vendor</a> for details.

<h2>Author</h2>

This manual page was written by Michael Stapelberg &lt;stapelberg [at] debian.org&gt; and is maintained by the Debian Go Compiler Team &lt;team+go-compiler [at] tracker.debian.org&gt; based on the output of 'go help gopath' for the Debian project (and may be used by others).
