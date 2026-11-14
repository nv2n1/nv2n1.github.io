---
title: "pgpool(8)"
name: "pgpool"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pgpool/"
description: "pgpool – PostgreSQL connection pool daemon"
---

<p>pgpool &#8211; PostgreSQL connection pool daemon</p>
<h2>Synopsis</h2>
<p><code>pgpool</code> [ <code>-c</code>] [ <code>-f config_file</code> ] [ <code>-F pcp_config_file</code> ] [ <code>-a hba_file</code> ] [ <code>-n</code> ] [ <code>-D</code> ] [ <code>-d</code> ] <code>pgpool</code> [ <code>-f config_file</code> ] [ <code>-F pcp_config_file</code> ] [ <code>-a hba_file</code> ] [ <code>-m</code> <i>{s[mart]|f[ast]|i[mmediate]}</i> ] <code>stop</code> <code>pgpool</code> [ <code>-f config_file</code> ] [ <code>-F pcp_config_file</code> ] [ <code>-a hba_file</code> ] <code>reload</code> </p>
<h2>Description</h2>
<p><code>pgpool</code> is a connection pool server for PostgreSQL. <code>pgpool</code> runs between PostgreSQL&#8217;s client and server. Any PostgreSQL client can connect to <code>pgpool</code> as if it&#8217;s a real PostgreSQL server. <code>pgpool</code> caches the connection to the PostgreSQL server to reduce the overhead involved in establishing the connection to it. <code>pgpool</code> can also be used with two PostgreSQL servers for fail over purposes. If the first server goes down, <code>pgpool</code> will automatically switch to the secondary server. <code>pgpool</code> is typically started and stopped via system initialization scripts. </p>
<h2>Invocation</h2>
<dl>
<dt><code>pgpool</code> [ <i>options&#8230;</i> ]</p>
<dd>Starts as a daemon in the background (unless <code>-n</code> is given).</p>
<dt><code>pgpool</code> [ <i>options&#8230;</i> ] <code>stop</code></p>
<dd>Shutdown.</p>
<dt><code>pgpool</code> [ <i>options&#8230;</i> ] <code>reload</code></p>
<dd>Reloads the configuration.</dl>
<h2>Options</h2>
<dl>
<dt><code>-a</code> <i>path</i></p>
<dd></dl>
<p> <code>&#8211;hba-file</code> <i>path</i> Sets the path to the <i>pool_hba.conf</i> configuration file (default: <i>/etc/pgpool-II/pgpool_hba.conf</i>).</p>
<dl>
<dt><code>-c</code></p>
<dd></dl>
<p> <code>&#8211;clear-cache</code> Clears the query cache.</p>
<dl>
<dt><code>-d</code></p>
<dd></dl>
<p> <code>&#8211;debug</code> Print lots of debug messages.</p>
<dl>
<dt><code>-f</code> <i>path</i></p>
<dd></dl>
<p> <code>&#8211;config-file</code> <i>path</i> Sets the path to the <i>pgpool.conf</i> configuration file (default: <i>/etc/pgpool-II/pgpool.conf</i>).</p>
<dl>
<dt><code>-F</code> <i>path</i></p>
<dd></dl>
<p> <code>&#8211;pcp-config-file</code> <i>path</i> Sets the path to the <i>pcp.conf</i> configuration file (default: <i>/etc/pgpool-II/pcp.conf</i>).</p>
<dl>
<dt><code>-h</code></p>
<dd></dl>
<p> <code>&#8211;help</code> Print a help message and exit.</p>
<dl>
<dt><code>-m</code> <i>mode</i></p>
<dd></dl>
<p> <code>&#8211;mode</code> <i>mode</i> Shutdown mode: <code>smart, fast, </code> or <code>immediate</code>.</p>
<dl>
<dt><code>-n</code></p>
<dd></dl>
<p> <code>&#8211;no-daemon</code> Foreground mode. Error messages go to stdout or stderr, which could be piped out to log processors such as <code><a href="/docs/linux/man/1-logger/">logger</a></code>(1) or <code><a href="/docs/linux/man/8-rotatelogs/">rotatelogs</a></code>(8). To daemonize, explicitly invoke <code>pgpool</code> in background.</p>
<dl>
<dt><code>-D</code></p>
<dd></dl>
<p> <code>&#8211;discard-status</code> Discard pgpool_status file and do not restore previous status.</p>
<dl>
<dt><code>-v</code></p>
<dd></dl>
<p> <code>&#8211;version</code> Print version and exit.</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/pgpool-II/pgpool.conf</i></p>
<dd>Default configuration file</p>
<dt><i>/etc/pgpool-II/pool_hba.conf</i></p>
<dd>Host Based Access configuration file</p>
<dt><i>/etc/pgpool-II/pcp.conf</i></p>
<dd>PCP commands configuration file</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-logger/">logger</a></code>(1), <code><a href="/docs/linux/man/1-postmaster/">postmaster</a></code>(1), <code><a href="/docs/linux/man/8-rotatelogs/">rotatelogs</a></code>(8) Additional information can be found in the <code>pgpool</code> <i>README</i> file. </p>
