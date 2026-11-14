---
title: "dbiproxy(1)"
name: "dbiproxy"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbiproxy/"
description: "dbiproxy – A proxy server for the DBD::Proxy driver"
---

<h2 class="name">NAME</h2>
<p> dbiproxy &#8211; A proxy server for the DBD::Proxy driver </p>
<h2>SYNOPSIS</h2>
<pre>
    dbiproxy &lt;options&gt; --localport=&lt;port&gt;
</pre>
<h2>DESCRIPTION</h2>
<p> This tool is just a front end for the DBI::ProxyServer package. All it does is picking options from the command line and calling <i>DBI::ProxyServer::main()</i>. See DBI::ProxyServer for details. </p>
<p> Available options include:</p>
<dl>
<dt><code>&#8211;chroot=dir</code></p>
<dd> (<font SIZE="-1">UNIX</font> only) After doing a <i>bind()</i>, change root directory to the given directory by doing a <i>chroot()</i>. This is useful for security, but it restricts the environment a lot. For example, you need to load <font SIZE="-1">DBI</font> drivers in the config file or you have to create hard links to Unix sockets, if your drivers are using them. For example, with MySQL, a config file might contain the following lines: </p>
<pre><code>
my $rootdir = '/var/dbiproxy';
my $unixsockdir = '/tmp';
my $unixsockfile = 'mysql.sock';
foreach
    $dir($rootdir, "$rootdir$unixsockdir")
    {
        mkdir 0755, $dir;
    }
link("$unixsockdir/$unixsockfile",
     "$rootdir$unixsockdir/$unixsockfile");
require DBD::mysql;
{
    'chroot' = &gt; $rootdir,
    ...
}
</code></pre>
<p> If you don&#8217;t know <i>chroot()</i>, think of an <font SIZE="-1">FTP</font> server where you can see a certain directory tree only after logging in. See also the &#8211;group and &#8211;user options.</p>
<dt><code>&#8211;configfile=file</code></p>
<dd> Config files are assumed to return a single hash ref that overrides the arguments of the new method. However, command line arguments in turn take precedence over the config file. See the &#8220;<font SIZE="-1">CONFIGURATION FILE&#8221;</font> section in the DBI::ProxyServer documentation for details on the config file.</p>
<dt><code>&#8211;debug</code></p>
<dd> Turn debugging mode on. Mainly this asserts that logging messages of level &#8220;debug&#8221; are created.</p>
<dt><code>&#8211;facility=mode</code></p>
<dd> (<font SIZE="-1">UNIX</font> only) Facility to use for Sys::Syslog. The default is <code>daemon</code>.</p>
<dt><code>&#8211;group=gid</code></p>
<dd> After doing a <i>bind()</i>, change the real and effective <font SIZE="-1">GID</font> to the given. This is useful, if you want your server to bind to a privileged port (&lt;1024), but don&#8217;t want the server to execute as root. See also the &#8211;user option. </p>
<p> <font SIZE="-1">GID</font>&#8216;s can be passed as group names or numeric values.</p>
<dt><code>&#8211;localaddr=ip</code></p>
<dd> By default a daemon is listening to any <font SIZE="-1">IP</font> number that a machine has. This attribute allows to restrict the server to the given <font SIZE="-1">IP</font> number.</p>
<dt><code>&#8211;localport=port</code></p>
<dd> This attribute sets the port on which the daemon is listening. It must be given somehow, as there&#8217;s no default.</p>
<dt><code>&#8211;logfile=file</code></p>
<dd> Be default logging messages will be written to the syslog (Unix) or to the event log (Windows <font SIZE="-1">NT</font>). On other operating systems you need to specify a log file. The special value &#8220;<font SIZE="-1">STDERR&#8221;</font> forces logging to stderr. See Net::Daemon::Log for details.</p>
<dt><code>&#8211;mode=modename</code></p>
<dd> The server can run in three different modes, depending on the environment. </p>
<p> If you are running Perl 5.005 and did compile it for threads, then the server will create a new thread for each connection. The thread will execute the server&#8217;s <i>Run()</i> method and then terminate. This mode is the default, you can force it with &#8220;&#8211;mode=threads&#8221;. </p>
<p> If threads are not available, but you have a working <i>fork()</i>, then the server will behave similar by creating a new process for each connection. This mode will be used automatically in the absence of threads or if you use the &#8220;&#8211;mode=fork&#8221; option. </p>
<p> Finally there&#8217;s a single-connection mode: If the server has accepted a connection, he will enter the <i>Run()</i> method. No other connections are accepted until the <i>Run()</i> method returns (if the client disconnects). This operation mode is useful if you have neither threads nor <i>fork()</i>, for example on the Macintosh. For debugging purposes you can force this mode with &#8220;&#8211;mode=single&#8221;.</p>
<dt><code>&#8211;pidfile=file</code></p>
<dd> (<font SIZE="-1">UNIX</font> only) If this option is present, a <font SIZE="-1">PID</font> file will be created at the given location. Default is to not create a pidfile.</p>
<dt><code>&#8211;user=uid</code></p>
<dd> After doing a <i>bind()</i>, change the real and effective <font SIZE="-1">UID</font> to the given. This is useful, if you want your server to bind to a privileged port (&lt;1024), but don&#8217;t want the server to execute as root. See also the &#8211;group and the &#8211;chroot options. </p>
<p> <font SIZE="-1">UID</font>&#8216;s can be passed as group names or numeric values.</p>
<dt><code>&#8211;version</code></p>
<dd> Supresses startup of the server; instead the version string will be printed and the program exits immediately.</dl>
<h2>AUTHOR</h2>
<pre>
    Copyright (c) 1997    Jochen Wiedmann
                          Am Eisteich 9
                          72555 Metzingen
                          Germany
                          Email: joe [at] ispsoft.de
                          Phone: +49 7123 14881
</pre>
<p> The DBI::ProxyServer module is free software; you can redistribute it and/or modify it under the same terms as Perl itself. In particular permission is granted to Tim Bunce for distributing this as a part of the <font SIZE="-1">DBI.</font></p>
<h2>SEE ALSO</h2>
<p> DBI::ProxyServer, DBD::Proxy, <font SIZE="-1">DBI</font> </p>
<h2>Index</h2>
