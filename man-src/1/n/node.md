---

title: "node(1)"
name: "node"
section: "1"
letter: "n"
url: "/docs/linux/man/1-node/"
description: "node – server-side JavaScript runtime"
---

<p> <code>node</code> &#8211; server-side JavaScript runtime </p>
<h2>SYNOPSIS</h2>
<p> <code>node</code> [<i>options</i> ] [<i>v8-options</i> ] [-<code>e </code><i>string | script.js | &#8211; </i> ] [- ] [<i>arguments &#8230;</i> ]<br/>
<code>node</code> <code>inspect</code> [-<code>e </code><i>string | script.js | &#8211;</i><code>| </code><i>&lt;host&gt;:&lt;port&gt;</i> ] <i>&#8230;</i><br/>
<code>node</code> [-<code>-v8-options</code> ]</p>
<h2>DESCRIPTION</h2>
<p> Node.js is a set of libraries for JavaScript which allows it to be used outside of the browser. It is primarily focused on creating simple, easy-to-build network clients and servers. </p>
<p> Execute <code>node</code> without arguments to start a REPL.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;</code></dt>
<dd> Alias for stdin, analogous to the use of &#8211; in other command-line utilities. The executed script is read from stdin, and remaining arguments are passed to the script.</dd>
<dt><code>&#8211; </code></dt>
<dd> Indicate the end of command-line options. Pass the rest of the arguments to the script. </dd>
<p> If no script filename or eval/print script is supplied prior to this, then the next argument will be used as a script filename.</p>
<dt><code>&#8211;abort-on-uncaught-exception</code></dt>
<dd> Aborting instead of exiting causes a core file to be generated for analysis.</dd>
<dt><code>&#8211;completion-bash</code></dt>
<dd> Print source-able bash completion script for Node.js.</dd>
<dt><code>&#8211;enable-fips</code></dt>
<dd> Enable FIPS-compliant crypto at startup. Requires Node.js to be built with <code>./configure &#8211;openssl-fips</code></dd>
<dt><code>&#8211;experimental-modules</code></dt>
<dd> Enable experimental ES module support and caching modules.</dd>
<dt><code>&#8211;experimental-repl-await</code></dt>
<dd> Enable experimental top-level <code>await</code> keyword support in REPL.</dd>
<dt><code>&#8211;experimental-vm-modules</code></dt>
<dd> Enable experimental ES module support in VM module.</dd>
<dt><code>&#8211;experimental-worker</code></dt>
<dd> Enable experimental worker threads using worker_threads module.</dd>
<dt><code>&#8211;force-fips</code></dt>
<dd> Force FIPS-compliant crypto on startup (Cannot be disabled from script code). Same requirements as &#8211;<code>-enable-fips</code></dd>
<dt><code>&#8211;http-parser = </code><i>library</i></dt>
<dd> Chooses an HTTP parser library. Available values are <code>llhttp</code> or <code>legacy</code></dd>
<dt><code>&#8211;icu-data-dir = </code><i>file</i></dt>
<dd> Specify ICU data load path. Overrides <code>NODE_ICU_DATA</code></dd>
<dt><code>&#8211;inspect-brk = </code><i>[host:]port</i></dt>
<dd> Activate inspector on <i>host:port</i> and break at start of user script.</dd>
<dt><code>&#8211;inspect-port = </code><i>[host:]port</i></dt>
<dd> Set the <i>host:port</i> to be used when the inspector is activated.</dd>
<dt><code>&#8211;inspect = </code><i>[host:]port</i></dt>
<dd> Activate inspector on <i>host:port</i> Default is <code>127.0.0.1:9229</code> </dd>
<p> V8 Inspector integration allows attaching Chrome DevTools and IDEs to Node.js instances for debugging and profiling. It uses the Chrome DevTools Protocol.</p>
<dt><code>&#8211;loader = </code><i>file</i></dt>
<dd> Specify the <i>file</i> as a custom loader, to load &#8211;<code>-experimental-modules</code></dd>
<dt><code>&#8211;insecure-http-parser</code></dt>
<dd> Use an insecure HTTP parser that accepts invalid HTTP headers. This may allow interoperability with non-conformant HTTP implementations. It may also allow request smuggling and other HTTP attacks that rely on invalid headers being accepted. Avoid using this option.</dd>
<dt><code>&#8211;max-http-header-size = </code><i>size</i></dt>
<dd> Specify the maximum size of HTTP headers in bytes. Defaults to 8KB.</dd>
<dt><code>&#8211;napi-modules</code></dt>
<dd> This option is a no-op. It is kept for compatibility.</dd>
<dt><code>&#8211;no-deprecation</code></dt>
<dd> Silence deprecation warnings.</dd>
<dt><code>&#8211;no-force-async-hooks-checks</code></dt>
<dd> Disable runtime checks for `async_hooks`. These will still be enabled dynamically when `async_hooks` is enabled.</dd>
<dt><code>&#8211;no-warnings</code></dt>
<dd> Silence all process warnings (including deprecations).</dd>
<dt><code>&#8211;openssl-config = </code><i>file</i></dt>
<dd> Load an OpenSSL configuration file on startup. Among other uses, this can be used to enable FIPS-compliant crypto if Node.js is built with <code>./configure &#8211;openssl-fips</code></dd>
<dt><code>&#8211;pending-deprecation</code></dt>
<dd> Emit pending deprecation warnings.</dd>
<dt><code>&#8211;preserve-symlinks</code></dt>
<dd> Instructs the module loader to preserve symbolic links when resolving and caching modules other than the main module.</dd>
<dt><code>&#8211;preserve-symlinks-main</code></dt>
<dd> Instructs the module loader to preserve symbolic links when resolving and caching the main module.</dd>
<dt><code>&#8211;prof</code></dt>
<dd> Generate V8 profiler output.</dd>
<dt><code>&#8211;prof-process</code></dt>
<dd> Process V8 profiler output generated using the V8 option &#8211;<code>-prof</code></dd>
<dt><code>&#8211;redirect-warnings = </code><i>file</i></dt>
<dd> Write process warnings to the given <i>file</i> instead of printing to stderr.</dd>
<dt><code>&#8211;throw-deprecation</code></dt>
<dd> Throw errors for deprecations.</dd>
<dt><code>&#8211;title = </code><i>title</i></dt>
<dd> Specify process.title on startup.</dd>
<dt><code>&#8211;tls-cipher-list = </code><i>list</i></dt>
<dd> Specify an alternative default TLS cipher list. Requires Node.js to be built with crypto support. (Default)</dd>
<dt><code>&#8211;trace-deprecation</code></dt>
<dd> Print stack traces for deprecations.</dd>
<dt><code>&#8211;trace-event-categories </code><i>categories</i></dt>
<dd> A comma-separated list of categories that should be traced when trace event tracing is enabled using &#8211;<code>-trace-events-enabled</code></dd>
<dt><code>&#8211;trace-event-file-pattern </code><i>pattern</i></dt>
<dd> Template string specifying the filepath for the trace event data, it supports <code>${rotation}</code> and <code>${pid}</code></dd>
<dt><code>&#8211;trace-events-enabled</code></dt>
<dd> Enable the collection of trace event tracing information.</dd>
<dt><code>&#8211;trace-sync-io</code></dt>
<dd> Print a stack trace whenever synchronous I/O is detected after the first turn of the event loop.</dd>
<dt><code>&#8211;trace-warnings</code></dt>
<dd> Print stack traces for process warnings (including deprecations).</dd>
<dt><code>&#8211;track-heap-objects</code></dt>
<dd> Track heap object allocations for heap snapshots.</dd>
<dt><code>&#8212;unhandled-rejections=mode</code></dt>
<dd> Define the behavior for unhandled rejections. Can be one of `strict` (raise an error), `warn` (enforce warnings) or `none` (silence warnings).</dd>
<dt><code>&#8211;use-bundled-ca , &#8211;use-openssl-ca</code></dt>
<dd> Use bundled Mozilla CA store as supplied by current Node.js version or use OpenSSL&#8217;s default CA store. The default store is selectable at build-time. </dd>
<p> The bundled CA store, as supplied by Node.js, is a snapshot of Mozilla CA store that is fixed at release time. It is identical on all supported platforms. </p>
<p> Using OpenSSL store allows for external modifications of the store. For most Linux and BSD distributions, this store is maintained by the distribution maintainers and system administrators. OpenSSL CA store location is dependent on configuration of the OpenSSL library but this can be altered at runtime using environment variables. </p>
<p> See <code>SSL_CERT_DIR</code> and <code>SSL_CERT_FILE</code></p>
<dt><code>&#8211;v8-options</code></dt>
<dd> Print V8 command-line options.</dd>
<dt><code>&#8211;v8-pool-size = </code><i>num</i></dt>
<dd> Set V8&#8217;s thread pool size which will be used to allocate background jobs. If set to 0 then V8 will choose an appropriate size of the thread pool based on the number of online processors. If the value provided is larger than V8&#8217;s maximum, then the largest value will be chosen.</dd>
<dt><code>&#8211;zero-fill-buffers</code></dt>
<dd> Automatically zero-fills all newly allocated Buffer and SlowBuffer instances.</dd>
<dt><code>-c , &#8211;check</code></dt>
<dd> Check the script&#8217;s syntax without executing it. Exits with an error code if script is invalid.</dd>
<dt><code>-e , &#8211;eval </code><i>string</i></dt>
<dd> Evaluate <i>string</i> as JavaScript.</dd>
<dt><code>-h , &#8211;help</code></dt>
<dd> Print command-line options. The output of this option is less detailed than this document.</dd>
<dt><code>-i , &#8211;interactive</code></dt>
<dd> Open the REPL even if stdin does not appear to be a terminal.</dd>
<dt><code>-p , &#8211;print </code><i>string</i></dt>
<dd> Identical to &#8211;<code>e</code> but prints the result.</dd>
<dt><code>-r , &#8211;require </code><i>module</i></dt>
<dd> Preload the specified <i>module</i> at startup. Follows `require()`&#8217;s module resolution rules. <i>module</i> may be either a path to a file, or a Node.js module name.</dd>
<dt><code>-v , &#8211;version</code></dt>
<dd> Print node&#8217;s version.</dd></dl>
<h2>ENVIRONMENT</h2>
<dl>
<dt><code>NODE_DEBUG </code><i>modules&#8230;</i></dt>
<dd> Comma-separated list of core modules that should print debug information.</dd>
<dt><code>NODE_DEBUG_NATIVE </code><i>modules&#8230;</i></dt>
<dd> Comma-separated list of C++ core modules that should print debug information.</dd>
<dt><code>NODE_DISABLE_COLORS</code></dt>
<dd> When set to <i>1</i> colors will not be used in the REPL.</dd>
<dt><code>NODE_EXTRA_CA_CERTS </code><i>file</i></dt>
<dd> When set, the well-known &#8220;root&#8221; CAs (like VeriSign) will be extended with the extra certificates in <i>file</i> The file should consist of one or more trusted certificates in PEM format. </dd>
<p> If <i>file</i> is missing or misformatted, a message will be emitted once using <code>process.emitWarning()</code> but any errors are otherwise ignored. </p>
<p> This environment variable is ignored when `node` runs as setuid root or has Linux file capabilities set.</p>
<dt><code>NODE_ICU_DATA </code><i>file</i></dt>
<dd> Data path for ICU (Intl object) data. Will extend linked-in data when compiled with small-icu support.</dd>
<dt><code>NODE_NO_WARNINGS</code></dt>
<dd> When set to <i>1</i> process warnings are silenced.</dd>
<dt><code>NODE_OPTIONS </code><i>options&#8230;</i></dt>
<dd> A space-separated list of command-line <i>options</i> which are interpreted as if they had been specified on the command-line before the actual command (so they can be overridden). Node.js will exit with an error if an option that is not allowed in the environment is used, such as &#8211;<code>-print</code> or a script file.</dd>
<dt><code>NODE_PATH </code><i>directories&#8230;</i></dt>
<dd> A colon-separated list of <i>directories</i> prefixed to the module search path.</dd>
<dt><code>NODE_PENDING_DEPRECATION</code></dt>
<dd> When set to <i>1</i> emit pending deprecation warnings.</dd>
<dt><code>NODE_PRESERVE_SYMLINKS</code></dt>
<dd> When set to <i>1</i> the module loader preserves symbolic links when resolving and caching modules.</dd>
<dt><code>NODE_REDIRECT_WARNINGS </code><i>file</i></dt>
<dd> Write process warnings to the given <i>file</i> instead of printing to stderr. Equivalent to passing &#8211;<code>-redirect-warnings </code><i>file</i> on command-line.</dd>
<dt><code>NODE_REPL_HISTORY </code><i>file</i></dt>
<dd> Path to the <i>file</i> used to store persistent REPL history. The default path is <code>~/.node_repl_history</code> which is overridden by this variable. Setting the value to an empty string (&quot;&quot; or &quot; &quot;) will disable persistent REPL history.</dd>
<dt><code>NODE_TLS_REJECT_UNAUTHORIZED</code></dt>
<dd> When set to <i>0</i> TLS certificate validation is disabled.</dd>
<dt><code>NODE_V8_COVERAGE </code><i>dir</i></dt>
<dd> When set, Node.js writes JavaScript code coverage information to <i>dir</i></dd>
<dt><code>OPENSSL_CONF </code><i>file</i></dt>
<dd> Load an OpenSSL configuration file on startup. Among other uses, this can be used to enable FIPS-compliant crypto if Node.js is built with <code>./configure &#8211;openssl-fips</code> </dd>
<p> If the &#8211;<code>-openssl-config</code> command-line option is used, this environment variable is ignored.</p>
<dt><code>SSL_CERT_DIR </code><i>dir</i></dt>
<dd> If &#8211;<code>-use-openssl-ca</code> is enabled, this overrides and sets OpenSSL&#8217;s directory containing trusted certificates.</dd>
<dt><code>SSL_CERT_FILE </code><i>file</i></dt>
<dd> If &#8211;<code>-use-openssl-ca</code> is enabled, this overrides and sets OpenSSL&#8217;s file containing trusted certificates.</dd>
<dt><code>UV_THREADPOOL_SIZE </code><i>size</i></dt>
<dd> Sets the number of threads used in libuv&#8217;s threadpool to <i>size</i></dd></dl>
<h2>BUGS</h2>
<p> Bugs are tracked in GitHub Issues: <code><a rel="nofollow" href="https://github.com/nodejs/node/issues">https://github.com/nodejs/node/issues</a></code></p>
<h2>COPYRIGHT</h2>
<p> Copyright Node.js contributors. Node.js is available under the MIT license. </p>
<p> Node.js also includes external libraries that are available under a variety of licenses. See <code><a rel="nofollow" href="https://github.com/nodejs/node/blob/master/LICENSE">https://github.com/nodejs/node/blob/master/LICENSE</a></code> for the full license text.</p>
<h2>SEE ALSO</h2>
<p> Website: <code><a rel="nofollow" href="https://nodejs.org/">https://nodejs.org/</a></code> </p>
<p> Documentation: <code><a rel="nofollow" href="https://nodejs.org/api/">https://nodejs.org/api/</a></code> </p>
<p> GitHub repository &amp; Issue Tracker: <code><a rel="nofollow" href="https://github.com/nodejs/node">https://github.com/nodejs/node</a></code> </p>
<p> IRC (general questions): <code>chat.freenode.net #node.js</code> (unofficial) </p>
<p> IRC (Node.js core development): <code>chat.freenode.net #node-dev</code></p>
<h2>AUTHORS</h2>
<p> Written and maintained by 1000+ contributors: <code><a rel="nofollow" href="https://github.com/nodejs/node/blob/master/AUTHORS">https://github.com/nodejs/node/blob/master/AUTHORS</a></code> </p>
