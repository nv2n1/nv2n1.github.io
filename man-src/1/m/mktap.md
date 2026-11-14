---
title: "mktap(1)"
name: "mktap"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mktap/"
description: "mktap – create twisted.servers"
---

<h2>NAME</h2>
<p> mktap &#8211; create twisted.servers</p>
<h2>SYNOPSIS</h2>
<p> <code>mktap</code> [<i>options</i>] <i>apptype</i> [<i>application_option</i>]&#8230; </p>
<p> <code>mktap</code> <i>apptype</i> &#8211;help</p>
<h2>DESCRIPTION</h2>
<p> The <code>&#8211;help</code> prints out a usage message to standard output.</p>
<dl>
<dt><code>&#8211;debug</code>, <code>-d</code></p>
<dd> Show debug information for plugin loading.</p>
<dt><code>&#8211;progress</code>, <code>-p</code></p>
<dd> Show progress information for plugin loading.</p>
<dt><code>&#8211;encrypted</code>, <code>-e</code></p>
<dd> Encrypt file before writing (will make the extension of the resultant file begin with &#8216;e&#8217;).</p>
<dt><code>&#8211;uid</code>, <code>-u</code> <i>&lt;uid&gt;</i></p>
<dd> Application belongs to this uid, and should run with its permissions.</p>
<dt><code>&#8211;gid</code>, <code>-d</code> <i>&lt;gid&gt;</i></p>
<dd> Application belongs to this gid, and should run with its permissions.</p>
<dt><code>&#8211;append</code>, <code>-a</code> <i>&lt;file&gt;</i></p>
<dd> Append given servers to given file, instead of creating a new one. File should be be a tap file.</p>
<dt><code>&#8211;appname</code>, <code>-n</code> <i>&lt;name&gt;</i></p>
<dd> Use the specified name as the process name when the application is run with <i><a href="/docs/linux/man/1-twistd/">twistd</a>(1)</i>. This option also causes some initialization code to be duplicated when <i><a href="/docs/linux/man/1-twistd/">twistd</a>(1)</i> is run.</p>
<dt><code>&#8211;type</code>, <code>-t</code> <i>&lt;type&gt;</i></p>
<dd> Specify the output file type. Available types are:</p>
<dt>
<dd> pickle &#8211; (default) Output as a python pickle file.<br />
 xml &#8211; Output as a .tax XML file.<br />
 source &#8211; Output as a .tas (AOT Python source) file. <i>apptype</i> Can be &#8216;web&#8217;, &#8216;portforward&#8217;, &#8216;toc&#8217;, &#8216;coil&#8217;, &#8216;words&#8217;,</dl>
<h2><code>portforward</code> options</h2>
<dl>
<dt><code>-h</code>, <code>&#8211;host</code> <i>&lt;host&gt;</i></p>
<dd> Proxy connections to <i>&lt;host&gt;</i></p>
<dt><code>-d</code>, <code>&#8211;dest_port</code> <i>&lt;port&gt;</i></p>
<dd> Proxy connections to <i>&lt;port&gt;</i> on remote host.</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Listen locally on <i>&lt;port&gt;</i></dl>
<h2><code>web</code> options</h2>
<dl>
<dt><code>-u</code>, <code>&#8211;user</code></p>
<dd> Makes a server with ~/public_html and ~/.twistd-web-pb support for users.</p>
<dt><code>&#8211;personal</code></p>
<dd> Instead of generating a webserver, generate a ResourcePublisher which listens on ~/.twistd-web-pb</p>
<dt><code>&#8211;path</code> <i>&lt;path&gt;</i></p>
<dd> &lt;path&gt; is either a specific file or a directory to be set as the root of the web server. Use this if you have a directory full of HTML, cgi, php3, epy, or rpy files or any other files that you want to be served up raw.</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> &lt;port&gt; is a number representing which port you want to start the server on.</p>
<dt><code>-m</code>, <code>&#8211;mime_type</code> <i>&lt;mimetype&gt;</i></p>
<dd> &lt;mimetype&gt; is the default MIME type to use for files in a &#8211;path web server when none can be determined for a particular extension. The default is &#8216;text/html&#8217;.</p>
<dt><code>&#8211;allow_ignore_ext</code></p>
<dd> Specify whether or not a request for &#8216;foo&#8217; should return &#8216;foo.ext&#8217;. Default is off.</p>
<dt><code>&#8211;ignore-ext</code> <i>.&lt;extension&gt;</i></p>
<dd> Specify that a request for &#8216;foo&#8217; should return &#8216;foo.<i>&lt;extension&gt;</i>&#8216;.</p>
<dt><code>-t</code>, <code>&#8211;telnet</code> <i>&lt;port&gt;</i></p>
<dd> Run a telnet server on &lt;port&gt;, for additional configuration later.</p>
<dt><code>-i</code>, <code>&#8211;index</code> <i>&lt;name&gt;</i></p>
<dd> Use an index name other than &quot;index.html&quot;</p>
<dt><code>&#8211;https</code> <i>&lt;port&gt;</i></p>
<dd> Port to listen on for Secure HTTP.</p>
<dt><code>-c</code>, <code>&#8211;certificate</code> <i>&lt;filename&gt;</i></p>
<dd> SSL certificate to use for HTTPS. [default: server.pem]</p>
<dt><code>-k</code>, <code>&#8211;privkey</code> <i>&lt;filename&gt;</i></p>
<dd> SSL certificate to use for HTTPS. [default: server.pem]</p>
<dt><code>&#8211;processor</code> <i>&lt;ext&gt;=&lt;class name&gt;</i></p>
<dd> Adds a processor to those file names. (Only usable if after <code>&#8211;path)</code></p>
<dt><code>&#8211;resource-script</code> <i>&lt;script name&gt;</i></p>
<dd> Sets the root as a resource script. This script will be re-evaluated on every request.</dl>
<p> This creates a web.tap file that can be used by twistd. If you specify no arguments, it will be a demo webserver that has the Test class from twisted.web.test in it.</p>
<h2><code>toc</code> options</h2>
<dl>
<dt><code>-p</code> <i>&lt;port&gt;</i></p>
<dd> &lt;port&gt; is a number representing which port you want to start the server on.</dl>
<h2><code>mail</code> options</h2>
<dl>
<dt><code>-r</code>, <code>&#8211;relay</code> <i>&lt;ip&gt;,&lt;port&gt;=&lt;queue directory&gt;</i></p>
<dd> Relay mail to all unknown domains through given IP and port, using queue directory as temporary place to place files.</p>
<dt><code>-d</code>, <code>&#8211;domain</code> <i>&lt;domain&gt;</i>=<i>&lt;path&gt;</i></p>
<dd> generate an SMTP/POP3 virtual maildir domain named &quot;domain&quot; which saves to &quot;path&quot;</p>
<dt><code>-u</code>, <code>&#8211;username</code> <i>&lt;name&gt;</i>=<i>&lt;password&gt;</i></p>
<dd> add a user/password to the last specified domains</p>
<dt><code>-b</code>, <code>&#8211;bounce_to_postmaster</code></p>
<dd> undelivered mails are sent to the postmaster, instead of being rejected.</p>
<dt><code>-p</code>, <code>&#8211;pop</code> <i>&lt;port&gt;</i></p>
<dd> &lt;port&gt; is a number representing which port you want to start the pop3 server on.</p>
<dt><code>-s</code>, <code>&#8211;smtp</code> <i>&lt;port&gt;</i></p>
<dd> &lt;port&gt; is a number representing which port you want to start the smtp server on.</dl>
<p> This creates a mail.tap file that can be used by <a href="/docs/linux/man/1-twistd/">twistd</a>(1)</p>
<h2><code>telnet</code> options</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Run the telnet server on &lt;port&gt;</p>
<dt><code>-u</code>, <code>&#8211;username</code> <i>&lt;name&gt;</i></p>
<dd> set the username to &lt;name&gt;</p>
<dt><code>-w</code>, <code>&#8211;password</code> <i>&lt;password&gt;</i></p>
<dd> set the password to &lt;password&gt;</dl>
<h2><code>socks</code> options</h2>
<dl>
<dt><code>-i</code>, <code>&#8211;interface</code> <i>&lt;interface&gt;</i></p>
<dd> Listen on interface &lt;interface&gt;</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Run the SOCKSv4 server on &lt;port&gt;</p>
<dt><code>-l</code>, <code>&#8211;log</code> <i>&lt;filename&gt;</i></p>
<dd> log connection data to &lt;filename&gt;</dl>
<h2><code>ftp</code> options</h2>
<dl>
<dt><code>-a</code>, <code>&#8211;anonymous</code></p>
<dd> Allow anonymous logins</p>
<dt><code>-3</code>, <code>&#8211;thirdparty</code></p>
<dd> Allow third party connections</p>
<dt><code>&#8211;otp</code></p>
<dd> Use one time passwords (OTP)</p>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Run the FTP server on &lt;port&gt;</p>
<dt><code>-r</code>, <code>&#8211;root</code> <i>&lt;path&gt;</i></p>
<dd> Define the local root of the FTP server</p>
<dt><code>&#8211;anonymoususer</code> <i>&lt;username&gt;</i></p>
<dd> Define the the name of the anonymous user</dl>
<h2><code>manhole</code> options</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Run the manhole server on &lt;port&gt;</p>
<dt><code>-u</code>, <code>&#8211;user</code> <i>&lt;name&gt;</i></p>
<dd> set the username to &lt;name&gt;</p>
<dt><code>-w</code>, <code>&#8211;password</code> <i>&lt;password&gt;</i></p>
<dd> set the password to &lt;password&gt;</dl>
<h2><code>words</code> options</h2>
<dl>
<dt><code>-p</code>, <code>&#8211;port</code> <i>&lt;port&gt;</i></p>
<dd> Run the Words server on &lt;port&gt;</p>
<dt><code>-i</code>, <code>&#8211;irc</code> <i>&lt;port&gt;</i></p>
<dd> Run IRC server on port &lt;port&gt;</p>
<dt><code>-w</code>, <code>&#8211;web</code> <i>&lt;port&gt;</i></p>
<dd> Run web server on port &lt;port&gt;</dl>
<h2>AUTHOR</h2>
<p> Written by Moshe Zadka, based on mktap&#8217;s help messages</p>
<h2>REPORTING BUGS</h2>
<p> To report a bug, visit <i><a rel="nofollow" href="http://twistedmatrix.com/bugs/">http://twistedmatrix.com/bugs/</a></i></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2000-2008 Twisted Matrix Laboratories.<br />
 This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/1-twistd/">twistd</a>(1) </p>
<h2>Index</h2>
