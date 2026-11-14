---
title: "flagpoll(1)"
name: "flagpoll"
section: "1"
letter: "f"
url: "/docs/linux/man/1-flagpoll/"
description: "flagpoll – manual page for flagpoll 0.9.1"
---

<h2>NAME</h2>
<p> flagpoll &#8211; manual page for flagpoll 0.9.1</p>
<h2>DESCRIPTION</h2>
<p> usage: flagpoll pkg options [pkg options] [generic options]</p>
<h3>generic options:</h3>
<dl>
<dt><code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>&#8211;version</code></p>
<dd> output version of flagpoll</p>
<dt><code>&#8211;list-all</code></p>
<dd> list all known packages</p>
<dt><code>&#8211;debug</code></p>
<dd> show debug information</p>
<dt><code>&#8211;verbose-debug</code></p>
<dd> show verbose debug information</p>
<dt><code>&#8211;extra-paths</code>=<i>EXTRA_PATHS</i></p>
<dd> extra paths for flagpoll to search for meta-data files</p>
<dt><code>&#8211;concat</code></p>
<dd> concatenate all output and output as one line</p>
<dt><code>&#8211;keep-dups</code></p>
<dd> do not strip out all duplicate info from options</p>
<dt><code>&#8211;info</code></p>
<dd> show information for packages</p>
<dt><code>&#8211;print-pkg-options</code></p>
<dd> show pkg specific options</dl>
<h3>options:</h3>
<dl>
<dt><code>&#8211;modversion</code></p>
<dd> output version for package</p>
<dt><code>&#8211;require</code>=<i>REQUIRE</i></p>
<dd> adds additional requirements for packages ex. 32/64</p>
<dt><code>&#8211;libs</code></p>
<dd> output all linker flags</p>
<dt><code>&#8211;static</code></p>
<dd> output linker flags for static linking</p>
<dt><code>&#8211;libs-only-l</code></p>
<dd> output <code>-l</code> flags</p>
<dt><code>&#8211;libs-only-other</code></p>
<dd> output other libs (e.g. <code>-pthread</code>)</p>
<dt><code>&#8211;libs-only-L</code></p>
<dd> output <code>-L</code> flags</p>
<dt><code>&#8211;cflags</code></p>
<dd> output all pre-processor and compiler flags</p>
<dt><code>&#8211;cflags-only-I</code></p>
<dd> output <code>-I</code> flags</p>
<dt><code>&#8211;cflags-only-other</code></p>
<dd> output cflags not covered by the cflags-only-I option</p>
<dt><code>&#8211;exists</code></p>
<dd> return 0 if the module(s) exist</p>
<dt><code>&#8211;from-file</code>=<i>FILE</i></p>
<dd> use the specified FILE for the package</p>
<dt><code>&#8211;no-deps</code></p>
<dd> do not lookup dependencies for the package</p>
<dt><code>&#8211;atleast-version</code>=<i>ATLEAST_VERSION</i></p>
<dd> return 0 if the module is at least version ATLEAST_VERSION</p>
<dt><code>&#8211;exact-version</code>=<i>EXACT_VERSION</i></p>
<dd> return 0 if the module is exactly version EXACT_VERSION</p>
<dt><code>&#8211;max-release</code>=<i>MAX_RELEASE</i></p>
<dd> return 0 if the module has a release that has a version of MAX_RELEASE and will return the max</p>
<dt><code>&#8211;variable</code>=<i>VARIABLE</i></p>
<dd> get the value of a variable</dl>
<p> dynamic options(replace VAR with a variable you want to get/filter on)</p>
<dl>
<dt>
<dd> NOTE: replace underscores with dashes in VAR NOTE: quotes are needed around &lt;,&gt;,= combinations</p>
<dt><code>&#8211;get-VAR</code></p>
<dd> get VAR from package</p>
<dt><code>&#8211;get-all-VAR</code></p>
<dd> get VAR from package and its deps</p>
<dt><code>&#8211;require-VAR[</code>&lt;,&gt;,=VAL]</p>
<dd> require that a var is defined for a package or optionally use equality operators against VAL</p>
<dt><code>&#8211;require-all-VAR[</code>&lt;,&gt;,=VAL]</p>
<dd> require that a var is defined for all packages or optionally use equality operators against VAL</dl>
<p> extending search path</p>
<dl>
<dt>FLAGPOLL_PATH</p>
<dd> environment variable that can be set to extend the search path for .fpc/.pc files</dl>
<p> Send bug reports and/or feedback to flagpoll-users [at] vrsource.org</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>flagpoll</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>flagpoll</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
<dd> <code>info flagpoll</code></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
