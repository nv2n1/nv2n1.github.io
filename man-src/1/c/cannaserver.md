---
title: "cannaserver(1)"
name: "cannaserver"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cannaserver/"
description: "cannaserver – Kana-Kanji conversion server"
---

<h2>NAME</h2>
<p> cannaserver &#8211; Kana-Kanji conversion server</p>
<h2>SYNOPSIS</h2>
<p> <code>cannaserver [-d] [-u </code><i>userid</i>] [-inet] [-inet6] [-l <i>n</i>] [-syslog] [-p <i>num</i>] [<i>ddpath</i>]</p>
<h2>DESCRIPTION</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) provides the Kana-Kanji conversion service. Most commonly this daemon starts at daemon bootup framework like /etc/rc depending on your system, so you do not usually start it up manually. </p>
<p> By default, <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) only accepts connections from clients at the same host where the server is running (via UNIX domain socket). You can make it accessible from other hosts via TCP by using option -inet (or -inet6). Whether you use this option or not, you can get access control based on user and host using /etc/hosts.canna. </p>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) immediately forks and gets into the background after it starts. You do not need to use &#8216;&amp;&#8217; explicitly to make it run in the background. </p>
<p> When it starts, <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) creates the UNIX domain socket /var/run/.iroha_unix/IROHA[:num] to communicate clients. The socket is deleted automatically if <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) terminates normally. The socket may exist while <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) is not running (because, for example, <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) terminated abnormally). In this case, delete the file manually or you cannot start it. </p>
<p> /var/lib/canna/dic/*/dics.dir includes the list of dictionaries which are available to clients. Users (i.e. clients) can choose which to use and specify them in ~/.canna.</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>ddpath</i></p>
<dd> Specifies the directory that contains dictionaries.</p>
<dt>-inet</p>
<dd> This option lets <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) accept connections from remote hosts using inet domain socket (IPv4). By default, the <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) uses only UNIX domain socket, i.e. only clients in your local machine can connect to the server.</p>
<dt>-inet6</p>
<dd> Enable IPv6. If this option is used solely, IPv4 access is disabled. If you want to use IPv4 at the same time, use both -inet and -inet6.</p>
<dt>-l <i>n</i></p>
<dd> Outputs the <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) log to /tmp/canna.log. n (1 to 5) specifies the log level.</p>
<dt>-d</p>
<dd> Starts <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) in debug mode. It is executed as the foreground process. Log data at log level 5 is output to the standard output.</p>
<dt>-u <i>userid</i></p>
<dd> Specifies which user <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) runs as. By default, <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) runs as the user who started <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M).</p>
<dt>-syslog</p>
<dd> Outputs the <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) log to <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8). If you specify this option, logs are not output to /var/log/canna/CANNA?msgs.</p>
<dt>-p <i>num</i></p>
<dd> By this option <a href="//www.systutorials.com/docs/linux/man/1M-cannaserver/">cannaserver</a>(1M) uses the port number 5680 + num. The default port number is 5680. This option also has an effect on the filename of the socket and the log file. See below.</dl>
<h2>FILES</h2>
<dl>
<dt>/var/run/.iroha_unix/IROHA[:num]</p>
<dd> Socket. [:num] part is added only when you specify -p.</p>
<dt>/var/lib/canna/dic/*/dics.dir</p>
<dd> Dictionary directory</p>
<dt>/etc/hosts.canna</p>
<dd> Access control file</p>
<dt>/var/log/canna/CANNA?msgs</p>
<dd> Log file. &quot;?&quot; is replaced with <i>num</i> specified with -p, and defaults to 0 without -p <i>num</i>. Log messages are not output to this file when -syslog is specified.</dl>
<h2>SEE ALSO</h2>
<p> <a href="//www.systutorials.com/docs/linux/man/1M-cannakill/">cannakill</a>(1M), <a href="/docs/linux/man/1-cannastat/">cannastat</a>(1), <a href="/docs/linux/man/1-cannacheck/">cannacheck</a>(1), <a href="/docs/linux/man/1-cshost/">cshost</a>(1) </p>
<h2>Index</h2>
