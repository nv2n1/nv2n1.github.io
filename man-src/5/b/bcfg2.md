---
title: "bcfg2(5)"
name: "bcfg2"
section: "5"
letter: "b"
url: "/docs/linux/man/5-bcfg2/"
description: "bcfg2.conf – configuration parameters for bcfg2"
---

<p>bcfg2.conf &#8211; configuration parameters for bcfg2</p>
<h2>Description</h2>
<dl>
<dt>bcfg2.conf includes configuration parameters for the bcfg2 server and client.</p>
<dd>
<h2>File Format</h2>
<p>The file is INI-style and consists of sections and options. A section begins with the name of the sections in square brackets and continues until the next section begins. </p>
<p> Options are specified in the form &#8216;name = value&#8217;. </p>
<p> The file is line-based each newline-terminated line represents either a comment, a section name or an option. </p>
<p> Any line beginning with a hash (#) is ignored, as are lines containing only whitespace.</p>
<h2>Server Options</h2>
<p>These options are only necessary on the Bcfg2 server. They are specified in the [server] section of the configuration file. </p>
<dl>
<dt><code>repository</code></p>
<dd>Specifies the path to the Bcfg2 repository containing all of the configuration specifications. The repository should be created using the bcfg2-init command. </p>
<dt><code>svn</code></p>
<dd>Set this to yes if the repository is SVN managed. </p>
<dt><code>structures</code></p>
<dd>A comma-delimited list of all the enabled structures plugins. Currently available plugins are Base, Bundler, and SGenshi. Defaults to Bundler and Base. </p>
<dt><code>generators</code></p>
<dd>A comma-delimited list of all enabled generator plugins. Currently available plugins are Actions, Cfg, Deps, Hostbase, Pkgmgr, Rules, SSHbase, TCheetah, and TGenshi. Defaults to SSHbase, Cfg, Pkgmgr, and Rules. </p>
<dt><code>plugins</code></p>
<dd>A comma-delimited list of enabled server plugins. Currently available plugins are DBStats. </p>
<dt><code>bundles</code></p>
<dd>A list of enabled bundles </p>
<dt><code>filemonitor</code></p>
<dd>The file monitor used to watch for changes in the repository. Values of &#8216;gamin&#8217;, &#8216;fam&#8217;, or &#8216;pseudo&#8217; are valid. </p>
</dl>
<h2>Statistics Options</h2>
<p>Server-only, specified in the [statistics] section. These options control the statistics collection functionality of the server. </p>
<dl>
<dt><code>database_engine</code></p>
<dd>The database engine used by the statistics module. One of either &#8216;postgresql&#8217;, &#8216;mysql&#8217;, &#8216;sqlite3&#8217;, or &#8216;ado_mssql&#8217;. </p>
<dt><code>database_name</code></p>
<dd>The name of the database to use for statistics data. If &#8216;database_engine&#8217; is set to &#8216;sqlite3&#8217; this is a file path to sqlite file and defaults to $REPOSITORY_DIR/etc/brpt.sqlite </p>
<dt><code>database_user</code></p>
<dd>User for database connections. Not used for sqlite3. </p>
<dt><code>database_password</code></p>
<dd>Password for database connections. Not used for sqlite3. </p>
<dt><code>database_host</code></p>
<dd>Host for database connections. Not used for sqlite3. </p>
<dt><code>database_port</code></p>
<dd>Port for database connections. Not used for sqlite3. </p>
</dl>
<h2>Communication Options</h2>
<p>Specified in the [communication] section. These options define settings used for client-server communication. </p>
<dl>
<dt><code>password</code></p>
<dd>Required on both the server and clients. On the server, sets the password clients need to use to communicate. On a client, sets the password to use to connect to the server. </p>
<dt><code>key</code></p>
<dd>A server-only option. The file system path to the server&#8217;s SSL key. Required if using xmlrpc/ssl for communication. </p>
<dt><code>protocol</code></p>
<dd>Communication protocol to use. Defaults to xmlrpc/ssl. </p>
<dt><code>retries</code></p>
<dd>A client-only option. Number of times to retry network communication. </p>
<dt><code>agent-port</code></p>
<dd>The TCP port on which to bind for agent mode. </p>
<dt><code>user</code></p>
<dd>A client-only option. The UUID of the client. </p>
<dt><code>fingerprint</code></p>
<dd>A client-only option. The fingerprint of the server&#8217;s SSL certificate. Obtainable by running &#8216;bcfg2-admin fingerprint&#8217;. </p>
</dl>
<h2>Component Options</h2>
<p>Specified in the [components] section. </p>
<dl>
<dt><code>bcfg2</code></p>
<dd>URL of the server. On the server this specifies which interface and port the server listens on. On the client, this specifies where the client will attempt to contact the server. eg: bcfg2 = <a rel="nofollow" href="https://10.3.1.6:6789">https://10.3.1.6:6789</a> </p>
<dt><code>encoding</code></p>
<dd>Text encoding of configuration files. Defaults to the system default encoding. </p>
</dl>
<h2>Logging Options</h2>
<p>Specified in the [logging] section. These options control the server logging functionality. </p>
<p> <code>path</code> Server log file path.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-bcfg2/">bcfg2</a>(1),</code> <code><a href="/docs/linux/man/8-bcfg2-server/">bcfg2-server</a>(8)</code> </p>
