---
title: "clangd-14(1)"
name: "clangd-14"
section: "1"
letter: "c"
url: "/docs/linux/man/1-clangd-14/"
description: "clangd – manual page for clangd 14"
---

<h2 class="name">NAME</h2>
<p> clangd &#8211; manual page for clangd 14 </p>
<h2>DESCRIPTION</h2>
<p> OVERVIEW: clangd is a language server that provides IDE-like features to editors.</p>
<h3>It should be used via an editor plugin rather than invoked directly. For more information, see:</h3>
<dl>
<dt>
</dt><dd> <a rel="nofollow" href="https://clangd.llvm.org/">https://clangd.llvm.org/</a> <a rel="nofollow" href="https://microsoft.github.io/language-server-protocol/">https://microsoft.github.io/language-server-protocol/</a></dd></dl>
<p> clangd accepts flags on the commandline, and in the CLANGD_FLAGS environment variable. </p>
<p> USAGE: clangd [options] </p>
<p> OPTIONS: </p>
<p> Generic Options:</p>
<dl>
<dt> <code>&#8211;help</code> &#8211; Display available options (<code>&#8211;help-hidden</code> for more)</dt>
<dt> <code>&#8211;help-list</code> &#8211; Display list of available options (<code>&#8211;help-list-hidden</code> for more)</dt>
<dt> <code>&#8211;version</code> &#8211; Display the version of this program</dt></dl>
<dd>clangd compilation flags options:</dd>
<dl>
<dt> <code>&#8211;compile-commands-dir=</code>&lt;string&gt; &#8211; Specify a path to look for compile_commands.json. If path is invalid, clangd will look in the current directory and parent paths of each source file</dt>
<dt> <code>&#8211;query-driver=</code>&lt;string&gt; &#8211; Comma separated list of globs for white-listing gcc-compatible drivers that are safe to execute. Drivers matching any of these globs will be used to extract system includes. e.g. /usr/bin/**/clang-*,/path/to/repo/**/g++-*</dt></dl>
<dd>clangd feature options:</dd>
<dl>
<dt> <code>&#8211;all-scopes-completion</code> &#8211; If set to true, code completion will include index symbols that are not defined in the scopes (e.g. namespaces) visible from the code completion point. Such completions can insert scope qualifiers</dt>
<dt> <code>&#8211;background-index</code> &#8211; Index project code in the background and persist index on disk.</dt>
<dt> <code>&#8211;clang-tidy</code> &#8211; Enable clang-tidy diagnostics</dt>
<dt> <code>&#8211;completion-style=</code>&lt;value&gt; &#8211; Granularity of code completion suggestions</dt>
<dt>=detailed</dt>
<dd> &#8211; One completion item for each semantically distinct completion, with full type information</dd>
<dt>=bundled</dt>
<dd> &#8211; Similar completion items (e.g. function overloads) are combined. Type information shown where possible</dd>
<dt> <code>&#8211;fallback-style=</code>&lt;string&gt; &#8211; clang-format style to apply by default when no .clang-format file is found</dt>
<dt> <code>&#8211;function-arg-placeholders</code> &#8211; When disabled, completions contain only parentheses for function calls. When enabled, completions also contain placeholders for method parameters</dt>
<dt> <code>&#8211;header-insertion=</code>&lt;value&gt; &#8211; Add #include directives when accepting code completions</dt>
<dt>=iwyu</dt>
<dd> &#8211; Include what you use. Insert the owning header for top-level symbols, unless the header is already directly included or the symbol is forward-declared</dd>
<dt>=never</dt>
<dd> &#8211; Never insert #include directives as part of code completion</dd>
<dt> <code>&#8211;header-insertion-decorators</code> &#8211; Prepend a circular dot or space before the completion label, depending on whether an include line will be inserted or not</dt>
<dt> <code>&#8211;limit-references=</code>&lt;int&gt; &#8211; Limit the number of references returned by clangd. 0 means no limit (default=1000)</dt>
<dt> <code>&#8211;limit-results=</code>&lt;int&gt; &#8211; Limit the number of results returned by clangd. 0 means no limit (default=100)</dt>
<dt> <code>&#8211;project-root=</code>&lt;string&gt; &#8211; Path to the project root. Requires remote-index-address to be set.</dt>
<dt> <code>&#8211;remote-index-address=</code>&lt;string&gt; &#8211; Address of the remote index server</dt></dl>
<dd>clangd miscellaneous options:</dd>
<dl>
<dt> <code>&#8211;check[=</code>&lt;string&gt;] &#8211; Parse one file in isolation instead of acting as a language server. Useful to investigate/reproduce crashes or configuration problems. With <code>&#8211;check=</code>&lt;filename&gt;, attempts to parse a particular file.</dt>
<dt> <code>&#8211;check-lines[=</code>&lt;string&gt;] &#8211; If specified, limits the range of tokens in <code>-check</code> file on which various features are tested. Example <code>&#8211;check-lines</code>=<i>,3-7/</i> restricts testing to lines 3 to 7 (inclusive) or <code>&#8211;check-lines</code>=<i>,5/</i> to restrict to one line. Default is testing entire file.</dt>
<dt><code>&#8211;enable-config</code> &#8211; Read user and project configuration from YAML files.</dt>
<dd>
</dd><dd>Project config is from a .clangd file in the project directory. User config is from clangd/config.yaml in the following directories:</dd>
<dt>Windows: %USERPROFILE%\AppData\Local</dt>
<dd> Mac OS: ~/Library/Preferences/ Others: $XDG_CONFIG_HOME, usually ~/.config</dd>
<dt>
</dt><dd> Configuration is documented at <a rel="nofollow" href="https://clangd.llvm.org/config.html">https://clangd.llvm.org/config.html</a></dd>
<dt> <code>-j=</code>&lt;uint&gt; &#8211; Number of async workers used by clangd. Background index also uses this many workers.</dt>
<dt> <code>&#8211;malloc-trim</code> &#8211; Release memory periodically via <a href="/docs/linux/man/3-malloc_trim/">malloc_trim</a>(3).</dt>
<dt> <code>&#8211;pch-storage=</code>&lt;value&gt; &#8211; Storing PCHs in memory increases memory usages, but may improve performance</dt>
<dt>=disk</dt>
<dd> &#8211; store PCHs on disk</dd>
<dt>=memory</dt>
<dd> &#8211; store PCHs in memory</dd></dl>
<dd>clangd protocol and logging options:</dd>
<dl>
<dt> <code>&#8211;log=</code>&lt;value&gt; &#8211; Verbosity of log messages written to stderr</dt>
<dt>=error</dt>
<dd> &#8211; Error messages only</dd>
<dt>=info</dt>
<dd> &#8211; High level execution tracing</dd>
<dt>=verbose</dt>
<dd> &#8211; Low level details</dd>
<dt> <code>&#8211;offset-encoding=</code>&lt;value&gt; &#8211; Force the offsetEncoding used for character positions. This bypasses negotiation via client capabilities</dt>
<dt>=utf-8</dt>
<dd> &#8211; Offsets are in UTF-8 bytes</dd>
<dt>=utf-16</dt>
<dd> &#8211; Offsets are in UTF-16 code units</dd>
<dt>=utf-32</dt>
<dd> &#8211; Offsets are in unicode codepoints</dd>
<dt> <code>&#8211;path-mappings=</code>&lt;string&gt; &#8211; Translates between client paths (as seen by a remote editor) and server paths (where clangd sees files on disk). Comma separated list of &#8216;&lt;client_path&gt;=&lt;server_path&gt;&#8217; pairs, the first entry matching a given path is used. e.g. /home/project/incl=/opt/include,/home/project=/workarea/project</dt>
<dt> <code>&#8211;pretty</code> &#8211; Pretty-print JSON output </dt>
</dl>
<h2>Index</h2>
