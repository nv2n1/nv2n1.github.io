---
title: "git-daemon(1)"
name: "git-daemon"
section: "1"
letter: "g"
url: "/docs/linux/man/1-git-daemon/"
description: "git-daemon – A really simple server for Git repositories"
---

<h2 class="name">NAME</h2>
<p> git-daemon &#8211; A really simple server for Git repositories </p>
<h2>SYNOPSIS</h2>
<pre><code>
git daemon[--verbose][--syslog][--export - all]
          [--timeout = &lt;n&gt;][--init - timeout = &lt;n&gt;][--max - connections = &lt;n&gt;]
          [--strict - paths][--base - path = &lt;path&gt;][--base - path - relaxed]
          [--user - path | --user - path = &lt;path&gt;]
          [--interpolated - path = &lt;pathtemplate&gt;]
          [--reuseaddr][--detach][--pid - file = &lt;file&gt;]
          [--enable = &lt;service&gt;][--disable = &lt;service&gt;]
          [--allow - override = &lt;service&gt;][--forbid - override = &lt;service&gt;]
          [--access - hook = &lt;path&gt;][--[no - ] informative - errors]
          [--inetd |
           [--listen = &lt;host_or_ipaddr&gt;][--port = &lt;n&gt;]
                                        [--user = &lt;user&gt;[--group = &lt;group&gt;]]]
          [--log - destination = (stderr | syslog | none)]
          [&lt;directory&gt;...]
</code></pre>
<h2>DESCRIPTION</h2>
<p> A really simple TCP Git daemon that normally listens on port &quot;DEFAULT_GIT_PORT&quot; aka 9418. It waits for a connection asking for a service, and will serve that service if it is enabled. </p>
<p> It verifies that the directory has the magic file &quot;git-daemon-export-ok&quot;, and it will refuse to export any Git directory that hasn&#8217;t explicitly been marked for export this way (unless the <code>&#8211;export-all</code> parameter is specified). If you pass some directory paths as <i>git daemon</i> arguments, you can further restrict the offers to a whitelist comprising of those. </p>
<p> By default, only <code>upload-pack</code> service is enabled, which serves <i>git fetch-pack</i> and <i>git ls-remote</i> clients, which are invoked from <i>git fetch</i>, <i>git pull</i>, and <i>git clone</i>. </p>
<p> This is ideally suited for read-only updates, i.e., pulling from Git repositories. </p>
<p> An <code>upload-archive</code> also exists to serve <i>git archive</i>.</p>
<h2>OPTIONS</h2>
<p> &#8211;strict-paths</p>
<dl>
<dt>
<dd> Match paths exactly (i.e. don&#8217;t allow &quot;/foo/repo&quot; when the real path is &quot;/foo/repo.git&quot; or &quot;/foo/repo/.git&quot;) and don&#8217;t do user-relative paths. <i>git daemon</i> will refuse to start when this option is enabled and no whitelist is specified.</dl>
<p> &#8211;base-path=&lt;path&gt;</p>
<dl>
<dt>
<dd> Remap all the path requests as relative to the given path. This is sort of &quot;Git root&quot; &#8211; if you run <i>git daemon</i> with <i>&#8211;base-path=/srv/git</i> on example.com, then if you later try to pull <i><a href="git://example.com/hello.git">git://example.com/hello.git</a></i>, <i>git daemon</i> will interpret the path as <code>/srv/git/hello.git</code>.</dl>
<p> &#8211;base-path-relaxed</p>
<dl>
<dt>
<dd> If &#8211;base-path is enabled and repo lookup fails, with this option <i>git daemon</i> will attempt to lookup without prefixing the base path. This is useful for switching to &#8211;base-path usage, while still allowing the old paths.</dl>
<p> &#8211;interpolated-path=&lt;pathtemplate&gt;</p>
<dl>
<dt>
<dd> To support virtual hosting, an interpolated path template can be used to dynamically construct alternate paths. The template supports %H for the target hostname as supplied by the client but converted to all lowercase, %CH for the canonical hostname, %IP for the server&#8217;s IP address, %P for the port number, and %D for the absolute path of the named repository. After interpolation, the path is validated against the directory whitelist.</dl>
<p> &#8211;export-all</p>
<dl>
<dt>
<dd> Allow pulling from all directories that look like Git repositories (have the <i>objects</i> and <i>refs</i> subdirectories), even if they do not have the <i>git-daemon-export-ok</i> file.</dl>
<p> &#8211;inetd</p>
<dl>
<dt>
<dd> Have the server run as an inetd service. Implies &#8211;syslog (may be overridden with <code>&#8211;log-destination=</code>). Incompatible with &#8211;detach, &#8211;port, &#8211;listen, &#8211;user and &#8211;group options.</dl>
<p> &#8211;listen=&lt;host_or_ipaddr&gt;</p>
<dl>
<dt>
<dd> Listen on a specific IP address or hostname. IP addresses can be either an IPv4 address or an IPv6 address if supported. If IPv6 is not supported, then &#8211;listen=hostname is also not supported and &#8211;listen must be given an IPv4 address. Can be given more than once. Incompatible with <code>&#8211;inetd</code> option.</dl>
<p> &#8211;port=&lt;n&gt;</p>
<dl>
<dt>
<dd> Listen on an alternative port. Incompatible with <code>&#8211;inetd</code> option.</dl>
<p> &#8211;init-timeout=&lt;n&gt;</p>
<dl>
<dt>
<dd> Timeout (in seconds) between the moment the connection is established and the client request is received (typically a rather low value, since that should be basically immediate).</dl>
<p> &#8211;timeout=&lt;n&gt;</p>
<dl>
<dt>
<dd> Timeout (in seconds) for specific client sub-requests. This includes the time it takes for the server to process the sub-request and the time spent waiting for the next client&#8217;s request.</dl>
<p> &#8211;max-connections=&lt;n&gt;</p>
<dl>
<dt>
<dd> Maximum number of concurrent clients, defaults to 32. Set it to zero for no limit.</dl>
<p> &#8211;syslog</p>
<dl>
<dt>
<dd> Short for <code>&#8211;log-destination=syslog</code>.</dl>
<p> &#8211;log-destination=&lt;destination&gt;</p>
<dl>
<dt>
<dd> Send log messages to the specified destination. Note that this option does not imply &#8211;verbose, thus by default only error conditions will be logged. The &lt;destination&gt; must be one of: </p>
<p> stderr</p>
<dl>
<dt>
<dd> Write to standard error. Note that if <code>&#8211;detach</code> is specified, the process disconnects from the real standard error, making this destination effectively equivalent to <code>none</code>.</dl>
<p> syslog</p>
<dl>
<dt>
<dd> Write to syslog, using the <code>git-daemon</code> identifier.</dl>
<p> none</p>
<dl>
<dt>
<dd> Disable all logging.</dl>
<p> The default destination is <code>syslog</code> if <code>&#8211;inetd</code> or <code>&#8211;detach</code> is specified, otherwise <code>stderr</code>.</dl>
<p> &#8211;user-path, &#8211;user-path=&lt;path&gt;</p>
<dl>
<dt>
<dd> Allow ~user notation to be used in requests. When specified with no parameter, requests to <a href="git://host/~alice/foo">git://host/~alice/foo</a> is taken as a request to access <i>foo</i> repository in the home directory of user <code>alice</code>. If <code>&#8211;user-path=path</code> is specified, the same request is taken as a request to access <code>path/foo</code> repository in the home directory of user <code>alice</code>.</dl>
<p> &#8211;verbose</p>
<dl>
<dt>
<dd> Log details about the incoming connections and requested files.</dl>
<p> &#8211;reuseaddr</p>
<dl>
<dt>
<dd> Use SO_REUSEADDR when binding the listening socket. This allows the server to restart without waiting for old connections to time out.</dl>
<p> &#8211;detach</p>
<dl>
<dt>
<dd> Detach from the shell. Implies &#8211;syslog.</dl>
<p> &#8211;pid-file=&lt;file&gt;</p>
<dl>
<dt>
<dd> Save the process id in <i>file</i>. Ignored when the daemon is run under <code>&#8211;inetd</code>.</dl>
<p> &#8211;user=&lt;user&gt;, &#8211;group=&lt;group&gt;</p>
<dl>
<dt>
<dd> Change daemon&#8217;s uid and gid before entering the service loop. When only <code>&#8211;user</code> is given without <code>&#8211;group</code>, the primary group ID for the user is used. The values of the option are given to <code><a href="/docs/linux/man/3-getpwnam/">getpwnam</a>(3)</code> and <code><a href="/docs/linux/man/3-getgrnam/">getgrnam</a>(3)</code> and numeric IDs are not supported. </p>
<p> Giving these options is an error when used with <code>&#8211;inetd</code>; use the facility of inet daemon to achieve the same before spawning <i>git daemon</i> if needed. </p>
<p> Like many programs that switch user id, the daemon does not reset environment variables such as <code>$HOME</code> when it runs git programs, e.g. <code>upload-pack</code> and <code>receive-pack</code>. When using this option, you may also want to set and export <code>HOME</code> to point at the home directory of <code>&lt;user&gt;</code> before starting the daemon, and make sure any Git configuration files in that directory are readable by <code>&lt;user&gt;</code>.</dl>
<p> &#8211;enable=&lt;service&gt;, &#8211;disable=&lt;service&gt;</p>
<dl>
<dt>
<dd> Enable/disable the service site-wide per default. Note that a service disabled site-wide can still be enabled per repository if it is marked overridable and the repository enables the service with a configuration item.</dl>
<p> &#8211;allow-override=&lt;service&gt;, &#8211;forbid-override=&lt;service&gt;</p>
<dl>
<dt>
<dd> Allow/forbid overriding the site-wide default with per repository configuration. By default, all the services may be overridden.</dl>
<p> &#8211;[no-]informative-errors</p>
<dl>
<dt>
<dd> When informative errors are turned on, git-daemon will report more verbose errors to the client, differentiating conditions like &quot;no such repository&quot; from &quot;repository not exported&quot;. This is more convenient for clients, but may leak information about the existence of unexported repositories. When informative errors are not enabled, all errors report &quot;access denied&quot; to the client. The default is &#8211;no-informative-errors.</dl>
<p> &#8211;access-hook=&lt;path&gt;</p>
<dl>
<dt>
<dd> Every time a client connects, first run an external command specified by the &lt;path&gt; with service name (e.g. &quot;upload-pack&quot;), path to the repository, hostname (%H), canonical hostname (%CH), IP address (%IP), and TCP port (%P) as its command-line arguments. The external command can decide to decline the service by exiting with a non-zero status (or to allow it by exiting with a zero status). It can also look at the $REMOTE_ADDR and <code>$REMOTE_PORT</code> environment variables to learn about the requestor when making this decision. </p>
<p> The external command can optionally write a single line to its standard output to be sent to the requestor as an error message when it declines the service.</dl>
<p> &lt;directory&gt;</p>
<dl>
<dt>
<dd> A directory to add to the whitelist of allowed directories. Unless &#8211;strict-paths is specified this will also include subdirectories of each named directory.</dl>
<h2>SERVICES</h2>
<p> These services can be globally enabled/disabled using the command-line options of this command. If finer-grained control is desired (e.g. to allow <i>git archive</i> to be run against only in a few selected repositories the daemon serves), the per-repository configuration file can be used to enable or disable them. </p>
<p> upload-pack</p>
<dl>
<dt>
<dd> This serves <i>git fetch-pack</i> and <i>git ls-remote</i> clients. It is enabled by default, but a repository can disable it by setting <code>daemon.uploadpack</code> configuration item to <code>false</code>.</dl>
<p> upload-archive</p>
<dl>
<dt>
<dd> This serves <i>git archive &#8211;remote</i>. It is disabled by default, but a repository can enable it by setting <code>daemon.uploadarch</code> configuration item to <code>true</code>.</dl>
<p> receive-pack</p>
<dl>
<dt>
<dd> This serves <i>git send-pack</i> clients, allowing anonymous push. It is disabled by default, as there is <i>no</i> authentication in the protocol (in other words, anybody can push anything into the repository, including removal of refs). This is solely meant for a closed LAN setting where everybody is friendly. This service can be enabled by setting <code>daemon.receivepack</code> configuration item to <code>true</code>.</dl>
<h2>EXAMPLES</h2>
<p> We assume the following in /etc/services</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
$ grep 9418 /etc/services
git             9418/tcp                # Git Version Control System
</pre>
</dl>
</dl>
<p> <i>git daemon</i> as inetd server</p>
<dl>
<dt>
<dd> To set up <i>git daemon</i> as an inetd service that handles any repository under the whitelisted set of directories, /pub/foo and /pub/bar, place an entry like the following into /etc/inetd all on one line: </p>
<dl>
<dt>
<dd>
<pre>
        git stream tcp nowait nobody  /usr/bin/git
                git daemon --inetd --verbose --export-all
                /pub/foo /pub/bar
</pre>
</dl>
</dl>
<p> <i>git daemon</i> as inetd server for virtual hosts</p>
<dl>
<dt>
<dd> To set up <i>git daemon</i> as an inetd service that handles repositories for different virtual hosts, <code><a rel="nofollow" href="http://www.example.com">www.example.com</a></code> and <code><a rel="nofollow" href="http://www.example.org">www.example.org</a></code>, place an entry like the following into <code>/etc/inetd</code> all on one line: </p>
<dl>
<dt>
<dd>
<pre><code>
git stream tcp nowait nobody / usr / bin / git git daemon-- inetd-- verbose-- export - all-- interpolated - path = / pub / % H % D / pub / www.example.org / software / pub / www.example.com / software / software
</code></pre>
</dl>
<p> In this example, the root-level directory <code>/pub</code> will contain a subdirectory for each virtual host name supported. Further, both hosts advertise repositories simply as <code><a href="git://www.example.com/software/repo.git">git://www.example.com/software/repo.git</a></code>. For pre-1.4.0 clients, a symlink from <code>/software</code> into the appropriate default repository could be made as well.</dl>
<p> <i>git daemon</i> as regular daemon for virtual hosts</p>
<dl>
<dt>
<dd> To set up <i>git daemon</i> as a regular, non-inetd service that handles repositories for multiple virtual hosts based on their IP addresses, start the daemon like this: </p>
<dl>
<dt>
<dd>
<pre>
        git daemon --verbose --export-all
                --interpolated-path=/pub/%IP/%D
                /pub/192.168.1.200/software
                /pub/10.10.220.23/software
</pre>
</dl>
<p> In this example, the root-level directory <code>/pub</code> will contain a subdirectory for each virtual host IP address supported. Repositories can still be accessed by hostname though, assuming they correspond to these IP addresses.</dl>
<p> selectively enable/disable services per repository</p>
<dl>
<dt>
<dd> To enable <i>git archive &#8211;remote</i> and disable <i>git fetch</i> against a repository, have the following in the configuration file in the repository (that is the file <i>config</i> next to <code>HEAD</code>, <i>refs</i> and <i>objects</i>). </p>
<dl>
<dt>
<dd>
<pre>
        [daemon]
                uploadpack = false
                uploadarch = true
</pre>
</dl>
</dl>
<h2>ENVIRONMENT</h2>
<p> <i>git daemon</i> will set REMOTE_ADDR to the IP address of the client that connected to it, if the IP address is available. REMOTE_ADDR will be available in the environment of hooks called when services are performed.</p>
<h2>GIT</h2>
<p> Part of the <code><a href="/docs/linux/man/1-git/">git</a></code>(1) suite </p>
<h2>Index</h2>
