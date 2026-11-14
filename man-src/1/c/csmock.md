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
<h2>DESCRIPTION</h2>
<p> usage: csmock [-h] [-r MOCK_PROFILE] [-t TOOLS] [-a] [-l]</p>
<dl>
<dt>
<dd> [&#8211;install LIST_OF_PKGS] [-o OUTPUT] [-f] [-j JOBS] [&#8211;cswrap-timeout CSWRAP_TIMEOUT] [-U EMBED_CONTEXT] [-k] [&#8211;no-clean] [&#8211;no-scan] [&#8211;print-defects] [&#8211;no-print-defects] [&#8211;base-srpm BASE_SRPM] [&#8211;base-root BASE_MOCK_PROFILE] [&#8211;skip-patches | <code>&#8211;diff-patches</code> | <code>-c</code> SHELL_CMD] [&#8211;version] [SRPM]</dl>
<h3>positional arguments:</h3>
<dl>
<dt>SRPM</p>
<dd> source RPM package to be scanned by static analyzers</dl>
<h3>optional arguments:</h3>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-r</code> MOCK_PROFILE, <code>&#8211;root</code> MOCK_PROFILE</p>
<dd> mock profile to use (defaults to mock&#8217;s default)</p>
<dt><code>-t</code> TOOLS, <code>&#8211;tools</code> TOOLS</p>
<dd> comma-spearated list of tools to enable (use <code>&#8211;listavailable-tools</code> to see the list of available tools)</p>
<dt><code>-a</code>, <code>&#8211;all-tools</code></p>
<dd> enable all available tools (use <code>&#8211;list-available-tools</code> to see the list of available tools)</p>
<dt><code>-l</code>, <code>&#8211;list-available-tools</code></p>
<dd> list available tools and exit</p>
<dt><code>&#8211;install</code> LIST_OF_PKGS</p>
<dd> space-separated list of packages to install into the chroot</p>
<dt><code>-o</code> OUTPUT, <code>&#8211;output</code> OUTPUT</p>
<dd> name of the tarball or directory to put the results to</p>
<dt><code>-f</code>, <code>&#8211;force</code></p>
<dd> overwrite the resulting file or directory if it exists already</p>
<dt><code>-j</code> JOBS, <code>&#8211;jobs</code> JOBS</p>
<dd> maximal number of jobs running in parallel (passed to &#8216;make&#8217;)</p>
<dt><code>&#8211;cswrap-timeout</code> CSWRAP_TIMEOUT</p>
<dd> maximal amount of time taken by analysis of a single module [s]</p>
<dt><code>-U</code> EMBED_CONTEXT, <code>&#8211;embed-context</code> EMBED_CONTEXT</p>
<dd> embed a number of lines of context from the source file for the key event (defaults to 3).</p>
<dt><code>-k</code>, <code>&#8211;keep-going</code></p>
<dd> continue as much as possible after an error</p>
<dt><code>&#8211;no-clean</code></p>
<dd> do not clean chroot when it becomes unused</p>
<dt><code>&#8211;no-scan</code></p>
<dd> do not analyze any package, just check versions of the analyzers</p>
<dt><code>&#8211;print-defects</code></p>
<dd> print the resulting list of defects (default if connected to a tty)</p>
<dt><code>&#8211;no-print-defects</code></p>
<dd> disables <code>&#8211;print-defects</code></p>
<dt><code>&#8211;base-srpm</code> BASE_SRPM</p>
<dd> perform a differential scan against the specified base pacakge</p>
<dt><code>&#8211;base-root</code> BASE_MOCK_PROFILE</p>
<dd> mock profile to use for the base scan (use only with <code>&#8211;base-srpm</code>)</p>
<dt><code>&#8211;skip-patches</code></p>
<dd> skip patches not annotated by %{?_rawbuild} (vanilla build)</p>
<dt><code>&#8211;diff-patches</code></p>
<dd> scan with/without patches and diff the lists of defects</p>
<dt><code>-c</code> SHELL_CMD, <code>&#8211;shell-cmd</code> SHELL_CMD</p>
<dd> use shell command to build the given tarball (instead of SRPM)</p>
<dt><code>&#8211;version</code></p>
<dd> print the version of csmock and exit</dl>
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
<h2>Index</h2>
