---
title: "csbuild(1)"
name: "csbuild"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csbuild/"
description: "csbuild – tool for plugging static analyzers into the build process"
---

<h2>NAME</h2>
<p> csbuild &#8211; tool for plugging static analyzers into the build process</p>
<h2>DESCRIPTION</h2>
<p> usage: csbuild [-h] <code>-c</code> BUILD_CMD [-g GIT_COMMIT_RANGE] [&#8211;git-bisect]</p>
<dl>
<dt>
<dd> [&#8211;added-exit-code ADDED_EXIT_CODE] [&#8211;base-fail-exit-code BASE_FAIL_EXIT_CODE] [&#8211;print-current] [&#8211;no-print-current] [&#8211;print-added] [&#8211;no-print-added] [&#8211;print-fixed] [&#8211;no-print-fixed] [&#8211;clean] [&#8211;no-clean] [&#8211;cswrap-timeout CSWRAP_TIMEOUT] [&#8211;color] [&#8211;no-color] [&#8211;gen-travis-yml] [&#8211;install INSTALL] [&#8211;prep-cmd PREP_CMD] [-w GCC_WARNING_LEVEL] [-U EMBED_CONTEXT] [&#8211;version]</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-c</code> BUILD_CMD, <code>&#8211;build-cmd</code> BUILD_CMD</p>
<dd> shell command used to build the sources (runs in $PWD)</p>
<dt><code>-g</code> GIT_COMMIT_RANGE, <code>&#8211;git-commit-range</code> GIT_COMMIT_RANGE</p>
<dd> range of git revisions for a differential scan</p>
<dt><code>&#8211;git-bisect</code></p>
<dd> if a new defect is added, use git-bisect to identify the cause WARNING: The given command must (re)compile all sources for this option to work!</p>
<dt><code>&#8211;added-exit-code</code> ADDED_EXIT_CODE</p>
<dd> exit code to return if there is any defect added in the new version</p>
<dt><code>&#8211;base-fail-exit-code</code> BASE_FAIL_EXIT_CODE</p>
<dd> exit code to return if the base scan fails</p>
<dt><code>&#8211;print-current</code></p>
<dd> print all defects in the current version (default unless <code>-g</code> is given) WARNING: The given command must (re)compile all sources for this option to work!</p>
<dt><code>&#8211;no-print-current</code></p>
<dd> disables <code>&#8211;print-current</code></p>
<dt><code>&#8211;print-added</code></p>
<dd> print defects added in the new version (default if <code>-g</code> is given)</p>
<dt><code>&#8211;no-print-added</code></p>
<dd> disables <code>&#8211;print-added</code></p>
<dt><code>&#8211;print-fixed</code></p>
<dd> print defects fixed in the new version WARNING: The given command must (re)compile all sources for this option to work!</p>
<dt><code>&#8211;no-print-fixed</code></p>
<dd> disables <code>&#8211;print-fixed</code></p>
<dt><code>&#8211;clean</code></p>
<dd> clean the temporary directory with results on exit (default)</p>
<dt><code>&#8211;no-clean</code></p>
<dd> disables <code>&#8211;clean</code></p>
<dt><code>&#8211;cswrap-timeout</code> CSWRAP_TIMEOUT</p>
<dd> maximal amount of time taken by analysis of a single module [s]</p>
<dt><code>&#8211;color</code></p>
<dd> use colorized console output (default if connected to a tty)</p>
<dt><code>&#8211;no-color</code></p>
<dd> disables <code>&#8211;color</code></p>
<dt><code>&#8211;gen-travis-yml</code></p>
<dd> generate the .travis.yml file for Travis CI (requires <code>&#8211;install</code>)</p>
<dt><code>&#8211;install</code> INSTALL</p>
<dd> space-separated list of packages to install with <code>&#8211;gen-travis-yml</code></p>
<dt><code>&#8211;prep-cmd</code> PREP_CMD</p>
<dd> shell command to run before the build (runs in $PWD)</p>
<dt><code>-w</code> GCC_WARNING_LEVEL, <code>&#8211;gcc-warning-level</code> GCC_WARNING_LEVEL</p>
<dd> Adjust GCC warning level. <code>-w0</code> means no additional warnings, <code>-w1</code> appends <code>-Wall</code> and <code>-Wextra</code>, and <code>-w2</code> enables some other useful warnings (default).</p>
<dt><code>-U</code> EMBED_CONTEXT, <code>&#8211;embed-context</code> EMBED_CONTEXT</p>
<dd> embed a number of lines of context from the source file for the key event (defaults to 3).</p>
<dt><code>&#8211;version</code></p>
<dd> print the version of csbuild and exit </p>
</dl>
<h2>Index</h2>
