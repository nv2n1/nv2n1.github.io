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
<p> usage: csbuild [-h] <code>-c</code> BUILD_CMD [-g GIT_COMMIT_RANGE] [&#8211;git-bisect]</p>
<dl>
<dt>
</dt><dd> [&#8211;added-exit-code ADDED_EXIT_CODE] [&#8211;base-fail-exit-code BASE_FAIL_EXIT_CODE] [&#8211;print-current] [&#8211;no-print-current] [&#8211;print-added] [&#8211;no-print-added] [&#8211;print-fixed] [&#8211;no-print-fixed] [&#8211;clean] [&#8211;no-clean] [&#8211;cswrap-timeout CSWRAP_TIMEOUT] [&#8211;color] [&#8211;no-color] [&#8211;gen-travis-yml] [&#8211;install INSTALL] [&#8211;prep-cmd PREP_CMD] [-w GCC_WARNING_LEVEL] [-U EMBED_CONTEXT] [&#8211;version]</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-c</code> BUILD_CMD, <code>&#8211;build-cmd</code> BUILD_CMD</dt>
<dd> shell command used to build the sources (runs in $PWD)</dd>
<dt><code>-g</code> GIT_COMMIT_RANGE, <code>&#8211;git-commit-range</code> GIT_COMMIT_RANGE</dt>
<dd> range of git revisions for a differential scan</dd>
<dt><code>&#8211;git-bisect</code></dt>
<dd> if a new defect is added, use git-bisect to identify the cause WARNING: The given command must (re)compile all sources for this option to work!</dd>
<dt><code>&#8211;added-exit-code</code> ADDED_EXIT_CODE</dt>
<dd> exit code to return if there is any defect added in the new version</dd>
<dt><code>&#8211;base-fail-exit-code</code> BASE_FAIL_EXIT_CODE</dt>
<dd> exit code to return if the base scan fails</dd>
<dt><code>&#8211;print-current</code></dt>
<dd> print all defects in the current version (default unless <code>-g</code> is given) WARNING: The given command must (re)compile all sources for this option to work!</dd>
<dt><code>&#8211;no-print-current</code></dt>
<dd> disables <code>&#8211;print-current</code></dd>
<dt><code>&#8211;print-added</code></dt>
<dd> print defects added in the new version (default if <code>-g</code> is given)</dd>
<dt><code>&#8211;no-print-added</code></dt>
<dd> disables <code>&#8211;print-added</code></dd>
<dt><code>&#8211;print-fixed</code></dt>
<dd> print defects fixed in the new version WARNING: The given command must (re)compile all sources for this option to work!</dd>
<dt><code>&#8211;no-print-fixed</code></dt>
<dd> disables <code>&#8211;print-fixed</code></dd>
<dt><code>&#8211;clean</code></dt>
<dd> clean the temporary directory with results on exit (default)</dd>
<dt><code>&#8211;no-clean</code></dt>
<dd> disables <code>&#8211;clean</code></dd>
<dt><code>&#8211;cswrap-timeout</code> CSWRAP_TIMEOUT</dt>
<dd> maximal amount of time taken by analysis of a single module [s]</dd>
<dt><code>&#8211;color</code></dt>
<dd> use colorized console output (default if connected to a tty)</dd>
<dt><code>&#8211;no-color</code></dt>
<dd> disables <code>&#8211;color</code></dd>
<dt><code>&#8211;gen-travis-yml</code></dt>
<dd> generate the .travis.yml file for Travis CI (requires <code>&#8211;install</code>)</dd>
<dt><code>&#8211;install</code> INSTALL</dt>
<dd> space-separated list of packages to install with <code>&#8211;gen-travis-yml</code></dd>
<dt><code>&#8211;prep-cmd</code> PREP_CMD</dt>
<dd> shell command to run before the build (runs in $PWD)</dd>
<dt><code>-w</code> GCC_WARNING_LEVEL, <code>&#8211;gcc-warning-level</code> GCC_WARNING_LEVEL</dt>
<dd> Adjust GCC warning level. <code>-w0</code> means no additional warnings, <code>-w1</code> appends <code>-Wall</code> and <code>-Wextra</code>, and <code>-w2</code> enables some other useful warnings (default).</dd>
<dt><code>-U</code> EMBED_CONTEXT, <code>&#8211;embed-context</code> EMBED_CONTEXT</dt>
<dd> embed a number of lines of context from the source file for the key event (defaults to 3).</dd>
<dt><code>&#8211;version</code></dt>
<dd> print the version of csbuild and exit </dd>
</dl>
