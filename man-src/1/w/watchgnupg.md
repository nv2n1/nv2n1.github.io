---
title: "watchgnupg(1)"
name: "watchgnupg"
section: "1"
letter: "w"
url: "/docs/linux/man/1-watchgnupg/"
description: "watchgnupg – Read and print logs from a socket"
---

<h2 class="name">NAME</h2>
<p> <code>watchgnupg</code> &#8211; Read and print logs from a socket </p>
<h2>SYNOPSIS</h2>
<p> <code>watchgnupg</code> [<code>&#8211;force</code>] [<code>&#8211;verbose</code>] <i>socketname</i> </p>
<h2>DESCRIPTION</h2>
<p> Most of the main utilities are able to write their log files to a Unix Domain socket if configured that way. <code>watchgnupg</code> is a simple listener for such a socket. It ameliorates the output with a time stamp and makes sure that long lines are not interspersed with log output from other utilities. This tool is not available for Windows. </p>
<p> <code>watchgnupg</code> is commonly invoked as </p>
<dl>
<dt>
<dd>
<pre>
watchgnupg --force $(gpgconf --list-dirs socketdir)/S.log
</dl>
</pre>
<h2>OPTIONS</h2>
<p> <code>watchgnupg</code> understands these options: </p>
<dl>
<dt><code>&#8211;force</code></p>
<dd> Delete an already existing socket file. </p>
<dt><code>&#8211;tcp </code><i>n</i></p>
<dd> Instead of reading from a local socket, listen for connects on TCP port <i>n</i>. </p>
<dt><code>&#8211;time-only</code></p>
<dd> Do not print the date part of the timestamp. </p>
<dt><code>&#8211;verbose</code></p>
<dd> Enable extra informational output. </p>
<dt><code>&#8211;version</code></p>
<dd> Print version of the program and exit. </p>
<dt><code>&#8211;help</code></p>
<dd> Display a brief help page and exit. </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>
<dd>
<pre>
$ watchgnupg --force --time-only $(gpgconf --list-dirs socketdir)/S.log
</pre>
</dl>
<p> This waits for connections on the local socket (e.g. &#8216;<i>/home/foo/.gnupg/S.log</i>&#8216;) and shows all log entries. To make this work the option <code>log-file</code> needs to be used with all modules which logs are to be shown. The suggested entry for the configuration files is: </p>
<dl>
<dt>
<dd>
<pre>
log-file socket://
</pre>
</dl>
<p> If the default socket as given above and returned by &quot;echo $(gpgconf &#8211;list-dirs socketdir)/S.log&quot; is not desired an arbitrary socket name can be specified, for example &#8216;<i><a href="socket:///home/foo/bar/mysocket">socket:///home/foo/bar/mysocket</a></i>&#8216;. For debugging purposes it is also possible to do remote logging. Take care if you use this feature because the information is send in the clear over the network. Use this syntax in the conf files: </p>
<dl>
<dt>
<dd>
<pre>
log-file <a href="tcp://192.168.1.1:4711">tcp://192.168.1.1:4711</a>
</pre>
</dl>
<p> You may use any port and not just 4711 as shown above; only IP addresses are supported (v4 and v6) and no host names. You need to start <code>watchgnupg</code> with the <code>tcp</code> option. Note that under Windows the registry entry <i>HKCU\Software\GNU\GnuPG:DefaultLogFile</i> can be used to change the default log output from <code>stderr</code> to whatever is given by that entry. However the only useful entry is a TCP name for remote debugging. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), <code><a href="/docs/linux/man/1-scdaemon/">scdaemon</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
