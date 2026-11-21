---

title: "csmock(1)"
name: "csmock"
section: "1"
letter: "c"
url: "/docs/linux/man/1-csmock/"
description: "csmock – run static analysis of the given SRPM using mock"
---

<h2>NAME</h2>
<p> csmock &#8211; run static analysis of the given SRPM using mock</p>
<p> usage: csmock [-h] [-r MOCK_PROFILE] [-t TOOLS] [-a] [-l]</p>
<dl>
<dt>
</dt><dd> [&#8211;install LIST_OF_PKGS] [-o OUTPUT] [-f] [-j JOBS] [&#8211;cswrap-timeout CSWRAP_TIMEOUT] [-U EMBED_CONTEXT] [-k] [&#8211;no-clean] [&#8211;no-scan] [&#8211;print-defects] [&#8211;no-print-defects] [&#8211;base-srpm BASE_SRPM] [&#8211;base-root BASE_MOCK_PROFILE] [&#8211;skip-patches | <code>&#8211;diff-patches</code> | <code>-c</code> SHELL_CMD] [&#8211;version] [SRPM]</dd></dl>
<h3>positional arguments:</h3>
<dl>
<dt>SRPM</dt>
<dd> source RPM package to be scanned by static analyzers</dd></dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></dt>
<dd> show this help message and exit</dd>
<dt><code>-r</code> MOCK_PROFILE, <code>&#8211;root</code> MOCK_PROFILE</dt>
<dd> mock profile to use (defaults to mock&#8217;s default)</dd>
<dt><code>-t</code> TOOLS, <code>&#8211;tools</code> TOOLS</dt>
<dd> comma-spearated list of tools to enable (use <code>&#8211;listavailable-tools</code> to see the list of available tools)</dd>
<dt><code>-a</code>, <code>&#8211;all-tools</code></dt>
<dd> enable all available tools (use <code>&#8211;list-available-tools</code> to see the list of available tools)</dd>
<dt><code>-l</code>, <code>&#8211;list-available-tools</code></dt>
<dd> list available tools and exit</dd>
<dt><code>&#8211;install</code> LIST_OF_PKGS</dt>
<dd> space-separated list of packages to install into the chroot</dd>
<dt><code>-o</code> OUTPUT, <code>&#8211;output</code> OUTPUT</dt>
<dd> name of the tarball or directory to put the results to</dd>
<dt><code>-f</code>, <code>&#8211;force</code></dt>
<dd> overwrite the resulting file or directory if it exists already</dd>
<dt><code>-j</code> JOBS, <code>&#8211;jobs</code> JOBS</dt>
<dd> maximal number of jobs running in parallel (passed to &#8216;make&#8217;)</dd>
<dt><code>&#8211;cswrap-timeout</code> CSWRAP_TIMEOUT</dt>
<dd> maximal amount of time taken by analysis of a single module [s]</dd>
<dt><code>-U</code> EMBED_CONTEXT, <code>&#8211;embed-context</code> EMBED_CONTEXT</dt>
<dd> embed a number of lines of context from the source file for the key event (defaults to 3).</dd>
<dt><code>-k</code>, <code>&#8211;keep-going</code></dt>
<dd> continue as much as possible after an error</dd>
<dt><code>&#8211;no-clean</code></dt>
<dd> do not clean chroot when it becomes unused</dd>
<dt><code>&#8211;no-scan</code></dt>
<dd> do not analyze any package, just check versions of the analyzers</dd>
<dt><code>&#8211;print-defects</code></dt>
<dd> print the resulting list of defects (default if connected to a tty)</dd>
<dt><code>&#8211;no-print-defects</code></dt>
<dd> disables <code>&#8211;print-defects</code></dd>
<dt><code>&#8211;base-srpm</code> BASE_SRPM</dt>
<dd> perform a differential scan against the specified base pacakge</dd>
<dt><code>&#8211;base-root</code> BASE_MOCK_PROFILE</dt>
<dd> mock profile to use for the base scan (use only with <code>&#8211;base-srpm</code>)</dd>
<dt><code>&#8211;skip-patches</code></dt>
<dd> skip patches not annotated by %{?_rawbuild} (vanilla build)</dd>
<dt><code>&#8211;diff-patches</code></dt>
<dd> scan with/without patches and diff the lists of defects</dd>
<dt><code>-c</code> SHELL_CMD, <code>&#8211;shell-cmd</code> SHELL_CMD</dt>
<dd> use shell command to build the given tarball (instead of SRPM)</dd>
<dt><code>&#8211;version</code></dt>
<dd> print the version of csmock and exit</dd></dl>
<h2>OUTPUT FORMAT</h2>
<p> If not overridden by the &#8211;output option, csmock creates an archive <code>NVR.tar.xz</code> in the current directory for an SRPM named NVR.src.rpm (or NVR.tar.* if the &#8211;shell-cmd option is used). The archive contains a directory named NVR as the only top-level directory, containing the following items: </p>
<p> <code>scan-results.err</code> &#8211; scan results encoded as plain-text (for source code editors) </p>
<p> <code>scan-results.html</code> &#8211; scan results encoded as HTML (suitable for web browsers) </p>
<p> <code>scan-results.js</code> &#8211; scan results, including scan metadata, encoded using JSON </p>
<p> <code>scan-results-summary.txt</code> &#8211; total count of defects found by particular checkers </p>
<p> <code>scan.ini</code> &#8211; scan metadata encoded in the INI format </p>
<p> <code>scan.log</code> &#8211; scan log file (useful for debugging scan failures) </p>
<p> <code>debug</code> &#8211; a directory containing additional data (intended for csmock debugging) </p>
<p> Note that external plug-ins of csmock may create additional files (not covered by this man page) in the directory with results. </p>
