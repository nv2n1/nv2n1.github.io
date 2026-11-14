---
title: "nginx(8)"
name: "nginx"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nginx/"
description: "nginx – HTTP and reverse proxy server, mail proxy server"
---

<p><code>nginx</code> &#8211; HTTP and reverse proxy server, mail proxy server</p>
<h2>Synopsis</h2>
<p>[-<code>?hqTtVv </code>[-<code>c </code><i>file</i> ] ] [-<code>g </code><i>directives</i> ] [-<code>p </code><i>prefix</i> ] [-<code>s </code><i>signal</i> ]</p>
<h2>Description</h2>
<p>(pronounced &#8220;engine x&#8221; is an HTTP and reverse proxy server, as well as a mail proxy server. It is known for its high performance, stability, rich feature set, simple configuration, and low resource consumption. The options are as follows:</p>
<dl>
<dt><code>-? , h</code></p>
<dd>Print help.</p>
<dt><code>-c </code><i>file</i></p>
<dd>Use an alternative configuration <i>file</i></p>
<dt><code>-g </code><i>directives</i></p>
<dd>Set global configuration directives. See Sx EXAMPLES for details.</p>
<dt><code>-p </code><i>prefix</i></p>
<dd>Set the prefix path. The default value is %%PREFIX%%</p>
<dt><code>-q</code></p>
<dd>Suppress non-error messages during configuration testing.</p>
<dt><code>-s </code><i>signal</i></p>
<dd>Send a signal to the master process. The argument <i>signal</i> can be one of: <code>stop , quit , reopen , reload</code> The following table shows the corresponding system signals: </p>
<dt><code>stop</code></p>
<dd><code>SIGTERM</code></p>
<dt><code>quit</code></p>
<dd><code>SIGQUIT</code></p>
<dt><code>reopen</code></p>
<dd><code>SIGUSR1</code></p>
<dt><code>reload</code></p>
<dd><code>SIGHUP</code></dl>
<dt><code>-t</code></p>
<dd>Do not run, just test the configuration file. checks the configuration file syntax and then tries to open files referenced in the configuration file.</p>
<dt><code>-T</code></p>
<dd>Same as &#8211;<code>t</code> but additionally dump configuration files to standard output.</p>
<dt><code>-V</code></p>
<dd>Print the version, compiler version, and configure script parameters.</p>
<dt><code>-v</code></p>
<dd>Print the version.</dl>
<h2>Signals</h2>
<p>The master process of can handle the following signals: </p>
<dl>
<dt><code>SIGINT , SIGTERM</code></p>
<dd>Shut down quickly.</p>
<dt><code>SIGHUP</code></p>
<dd>Reload configuration, start the new worker process with a new configuration, and gracefully shut down old worker processes.</p>
<dt><code>SIGQUIT</code></p>
<dd>Shut down gracefully.</p>
<dt><code>SIGUSR1</code></p>
<dd>Reopen log files.</p>
<dt><code>SIGUSR2</code></p>
<dd>Upgrade the executable on the fly.</p>
<dt><code>SIGWINCH</code></p>
<dd>Shut down worker processes gracefully.</dl>
<p> While there is no need to explicitly control worker processes normally, they support some signals too: </p>
<dl>
<dt><code>SIGTERM</code></p>
<dd>Shut down quickly.</p>
<dt><code>SIGQUIT</code></p>
<dd>Shut down gracefully.</p>
<dt><code>SIGUSR1</code></p>
<dd>Reopen log files.</dl>
<h2>Debugging Log</h2>
<p>To enable a debugging log, reconfigure to build with debugging: </p>
<blockquote><p><tt>&quot;./configure --with-debug ...&quot;</tt></p></blockquote>
<p> and then set the <code>debug</code> level of the <i>error_log</i> </p>
<blockquote><p><tt>&quot;error_log /path/to/log debug;&quot;</tt></p></blockquote>
<p> It is also possible to enable the debugging for a particular IP address: </p>
<blockquote>
<pre>events {
 debug_connection 127.0.0.1;
}</pre>
</blockquote>
<h2>Environment</h2>
<p>The <code>NGINX</code> environment variable is used internally by and should not be set directly by the user.</p>
<h2>Files</h2>
<dl>
<dt><code>%%PID_PATH%% </code></p>
<dd>Contains the process ID of <code>.</code> The contents of this file are not sensitive, so it can be world-readable.</p>
<dt><code>%%CONF_PATH%% </code></p>
<dd>The main configuration file.</p>
<dt><code>%%ERROR_LOG_PATH%% </code></p>
<dd>Error log file.</dl>
<h2>Exit Status</h2>
<p>Exit status is 0 on success, or 1 if the command fails.</p>
<h2>Examples</h2>
<p>Test configuration file ~/mynginx.conf with global directives for PID and quantity of worker processes: </p>
<blockquote>
<pre>nginx -t -c ~/mynginx.conf \
 -g &quot;pid /var/run/mynginx.pid; worker_processes 2;&quot;</pre>
</blockquote>
<h2>See Also</h2>
<p>Documentation at <a rel="nofollow" href="http://nginx.org/en/docs/">http://nginx.org/en/docs/</a> </p>
<p> For questions and technical support, please refer to <a rel="nofollow" href="http://nginx.org/en/support.html">http://nginx.org/en/support.html</a></p>
<h2>History</h2>
<p>Development of started in 2002, with the first public release on October 4, 2004.</p>
<h2>Authors</h2>
<p>An -nosplit An Igor Sysoev Aq igor [at] sysoev.ru . </p>
<p> This manual page was originally written by An Sergey A. Osokin Aq osa [at] FreeBSD.org.ru as a result of compiling many documents from all over the world.</p>
