---
title: "debuginfod-client-config(7)"
name: "debuginfod-client-config"
section: "7"
letter: "d"
url: "/docs/linux/man/7-debuginfod-client-config/"
description: "debuginfod-client-config – debuginfod client environment variables, cache control files and etc."
---

<p>debuginfod-client-config &#8211; debuginfod client environment variables, cache control files and etc.</p>
<h2>Synopsis</h2>
<p>Several environment variables and control files control the behaviour of debuginfod client applications. </p>
<h2>Environment Variables</h2>
<dl>
<dt><code>$TMPDIR</code></p>
<dd>This environment variable points to a file system to be used for temporary files. The default is /tmp. </p>
<dt><code>$DEBUGINFOD_URLS</code></p>
<dd>This environment variable contains a list of URL prefixes for trusted debuginfod instances. Alternate URL prefixes are separated by space. Avoid referential loops that cause a server to contact itself, directly or indirectly &#8211; the results would be hilarious. </p>
<dt><code>$DEBUGINFOD_CACHE_PATH</code></p>
<dd>This environment variable governs the location of the cache where downloaded files and cache-control files are kept. The default directory is chosen based on other environment variables, see below. </p>
<dt><code>$DEBUGINFOD_PROGRESS</code></p>
<dd>This environment variable governs the default progress function. If set, and if a progressfn is not explicitly set, then the library will configure a default progressfn. This function will append a simple progress message periodically to stderr. The default is no progress function output. </p>
<dt><code>$DEBUGINFOD_VERBOSE</code></p>
<dd>This environment variable governs the default file descriptor for verbose output. If set, and if a verbose fd is not explicitly set, then the verbose output will be produced on STDERR_FILENO. </p>
<dt><code>$DEBUGINFOD_RETRY_LIMIT</code></p>
<dd>This environment variable governs the default limit of retry attempts. If a query failed with errno other than ENOENT, will initiate several attempts within the limit. </p>
<dt><code>$DEBUGINFOD_TIMEOUT</code></p>
<dd>This environment variable governs the download <i>commencing</i> timeout for each debuginfod HTTP connection. A server that fails to provide at least 100K of data within this many seconds is skipped. The default is 90 seconds. (Zero or negative means &quot;no timeout&quot;.) </p>
<dt><code>$DEBUGINFOD_MAXTIME</code></p>
<dd>This environment variable dictates how long the client will wait to <i>complete</i> the download a file found on a server in seconds. It is best used to ensure that a file is downloaded quickly or be rejected. The default is 0 (infinite time). </p>
<dt><code>$DEBUGINFOD_MAXSIZE</code></p>
<dd>This environment variable dictates the maximum size of a file to download in bytes. This is best used if the user would like to ensure only small files are downloaded. A value of 0 causes no consideration for size, and the client may attempt to download a file of any size. The default is 0 (infinite size). </p>
</dl>
<h2>Cache</h2>
<p>Before each query, the debuginfod client library checks for a need to clean the cache. If it&#8217;s time to clean, the library traverses the cache directory and removes downloaded debuginfo-related artifacts and newly empty directories, if they have not been accessed recently. </p>
<p> Control files are located directly under the cache directory. They contain simple decimal numbers to set cache-related configuration parameters. If the files do not exist, the client library creates the files with the default parameter values as content. </p>
<p> After each query, the debuginfod client library deposits newly received files into a directory &amp; file that is named based on the build-id. A failed query is also cached by a special file. The naming convention used for these artifacts is deliberately <code>undocumented</code>. </p>
<dl>
<dt><code>$XDG_CACHE_HOME/debuginfod_client/</code></p>
<dd>Default cache directory, if $XDG_CACHE_HOME is set. </p>
<dt><code>$HOME/.cache/debuginfod_client/</code></p>
<dd>Default cache directory, if $XDG_CACHE_HOME is not set. </p>
<dt><code>$HOME/.debuginfod_client_cache/</code></p>
<dd>Deprecated cache directory, used only if preexisting. </p>
<dt><code>cache_clean_interval_s</code></p>
<dd>This control file gives the interval between cache cleaning rounds, in seconds. The default is 86400, one day. 0 means &quot;immediately&quot;. </p>
<dt><code>max_unused_age_s</code></p>
<dd>This control file sets how long unaccessed debuginfo-related files are retained, in seconds. The default is 604800, one week. 0 means &quot;immediately&quot;. </p>
<dt><code>cache_miss_s</code></p>
<dd>This control file sets how long to remember a query failure, in seconds. New queries for the same artifacts within this time window are short-circuited (returning an immediate failure instead of sending a new query to servers). This accelerates queries that probably would still fail. The default is 600, 10 minutes. 0 means &quot;forget immediately&quot;. </p>
</dl>
