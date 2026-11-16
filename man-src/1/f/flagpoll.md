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
<dt><code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>&#8211;version</code></dt>
<dd> output version of flagpoll</dd>
<dt><code>&#8211;list-all</code></dt>
<dd> list all known packages</dd>
<dt><code>&#8211;debug</code></dt>
<dd> show debug information</dd>
<dt><code>&#8211;verbose-debug</code></dt>
<dd> show verbose debug information</dd>
<dt><code>&#8211;extra-paths</code>=<i>EXTRA_PATHS</i></dt>
<dd> extra paths for flagpoll to search for meta-data files</dd>
<dt><code>&#8211;concat</code></dt>
<dd> concatenate all output and output as one line</dd>
<dt><code>&#8211;keep-dups</code></dt>
<dd> do not strip out all duplicate info from options</dd>
<dt><code>&#8211;info</code></dt>
<dd> show information for packages</dd>
<dt><code>&#8211;print-pkg-options</code></dt>
<dd> show pkg specific options</dd></dl>
<h3>options:</h3>
<dl>
<dt><code>&#8211;modversion</code></dt>
<dd> output version for package</dd>
<dt><code>&#8211;require</code>=<i>REQUIRE</i></dt>
<dd> adds additional requirements for packages ex. 32/64</dd>
<dt><code>&#8211;libs</code></dt>
<dd> output all linker flags</dd>
<dt><code>&#8211;static</code></dt>
<dd> output linker flags for static linking</dd>
<dt><code>&#8211;libs-only-l</code></dt>
<dd> output <code>-l</code> flags</dd>
<dt><code>&#8211;libs-only-other</code></dt>
<dd> output other libs (e.g. <code>-pthread</code>)</dd>
<dt><code>&#8211;libs-only-L</code></dt>
<dd> output <code>-L</code> flags</dd>
<dt><code>&#8211;cflags</code></dt>
<dd> output all pre-processor and compiler flags</dd>
<dt><code>&#8211;cflags-only-I</code></dt>
<dd> output <code>-I</code> flags</dd>
<dt><code>&#8211;cflags-only-other</code></dt>
<dd> output cflags not covered by the cflags-only-I option</dd>
<dt><code>&#8211;exists</code></dt>
<dd> return 0 if the module(s) exist</dd>
<dt><code>&#8211;from-file</code>=<i>FILE</i></dt>
<dd> use the specified FILE for the package</dd>
<dt><code>&#8211;no-deps</code></dt>
<dd> do not lookup dependencies for the package</dd>
<dt><code>&#8211;atleast-version</code>=<i>ATLEAST_VERSION</i></dt>
<dd> return 0 if the module is at least version ATLEAST_VERSION</dd>
<dt><code>&#8211;exact-version</code>=<i>EXACT_VERSION</i></dt>
<dd> return 0 if the module is exactly version EXACT_VERSION</dd>
<dt><code>&#8211;max-release</code>=<i>MAX_RELEASE</i></dt>
<dd> return 0 if the module has a release that has a version of MAX_RELEASE and will return the max</dd>
<dt><code>&#8211;variable</code>=<i>VARIABLE</i></dt>
<dd> get the value of a variable</dd></dl>
<p> dynamic options(replace VAR with a variable you want to get/filter on)</p>
<dl>
<dt>
</dt><dd> NOTE: replace underscores with dashes in VAR NOTE: quotes are needed around &lt;,&gt;,= combinations</dd>
<dt><code>&#8211;get-VAR</code></dt>
<dd> get VAR from package</dd>
<dt><code>&#8211;get-all-VAR</code></dt>
<dd> get VAR from package and its deps</dd>
<dt><code>&#8211;require-VAR[</code>&lt;,&gt;,=VAL]</dt>
<dd> require that a var is defined for a package or optionally use equality operators against VAL</dd>
<dt><code>&#8211;require-all-VAR[</code>&lt;,&gt;,=VAL]</dt>
<dd> require that a var is defined for all packages or optionally use equality operators against VAL</dd></dl>
<p> extending search path</p>
<dl>
<dt>FLAGPOLL_PATH</dt>
<dd> environment variable that can be set to extend the search path for .fpc/.pc files</dd></dl>
<p> Send bug reports and/or feedback to flagpoll-users [at] vrsource.org</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>flagpoll</code> is maintained as a Texinfo manual. If the <code>info</code> and <code>flagpoll</code> programs are properly installed at your site, the command</p>
<dl>
<dt>
</dt><dd> <code>info flagpoll</code></dd></dl>
<p> should give you access to the complete manual. </p>
<h2>Index</h2>
