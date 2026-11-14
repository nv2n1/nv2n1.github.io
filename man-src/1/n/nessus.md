---
title: "nessus(1)"
name: "nessus"
section: "1"
letter: "n"
url: "/docs/linux/man/1-nessus/"
description: "nessus – The client part of the Nessus Security Scanner"
---

<h2>NAME</h2>
<p> nessus &#8211; The client part of the Nessus Security Scanner</p>
<h2>SYNOPSIS</h2>
<p> <code>nessus [-v] [-h] [-n] [-T</code> <i>&lt;type&gt;</i><code>]&nbsp;<wbr>[-q&nbsp;<wbr>[-pPS]&nbsp;<wbr></code><i>host port user password targets results</i><code>]</code> <code>nessus -i in.[nsr|nbe] -o out.[html|xml|nsr|nbe]</code> </p>
<h2>DESCRIPTION</h2>
<p> The <code>Nessus Security Scanner</code> is a security auditing tool made up of two parts: a server, and a client. The server, <code>nessusd</code> is in charge of the attacks, whereas the client <code>nessus</code> provides an interface to the user. </p>
<p> <code>nessus </code> is an X11 client based on the Gimp ToolKit (GTK). </p>
<p> This man page explains how to use the client. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c </code><i>&lt;config-file&gt;</i><code>, &#8211;config-file=</code><i>&lt;config-file&gt;</i></p>
<dd> use another configuration file. </p>
<dt><code>-n, &#8211;no-pixmaps</code></p>
<dd> no pixmaps. This is handy if you are running nessus on a remote computer. </p>
<dt><code>-q, &#8211;batch-mode</code></p>
<dd> quiet mode or batch mode. Setting this option makes the nessus client expect all of the following settings.</p>
<dl>
<dt>
<dd> -p</p>
<dl>
<dt>
<dd>
&nbsp;<wbr>obtain list of plugins installed on the server.</dl>
<p> -P</p>
<dl>
<dt>
<dd> obtain list of server and plugin preferences.</dl>
<p> -S</p>
<dl>
<dt>
<dd> issue SQL output for -p and -P (experimental).</dl>
<p> *&nbsp;<wbr><i>host</i></p>
<dl>
<dt>
<dd> is the <code>nessusd </code> host to whom you will connect.</dl>
<p> *&nbsp;<wbr><i>port</i></p>
<dl>
<dt>
<dd> is the port to which you will connect on the remote <code>nessusd</code> host.</dl>
<p> *&nbsp;<wbr><i>user</i></p>
<dl>
<dt>
<dd> is the user name to use to connect to <code>nessusd</code>.</dl>
<p> *&nbsp;<wbr><i>password</i></p>
<dl>
<dt>
<dd> is the password associated with this user name.</dl>
<p> *&nbsp;<wbr><i>targets</i></p>
<dl>
<dt>
<dd> is the name of a file containing the target machines.</dl>
<p> *&nbsp;<wbr><i>results</i></p>
<dl>
<dt>
<dd> is the name of the file where the results will be stored at the end of the test.</dl>
<dl>
<dt><code>-r </code><i>&lt;report-file&gt;</i><code>, &#8211;open-report=</code><i>&lt;report-file&gt;</i></p>
<dd> Using the GUI, <code>nessus</code> visualizes a report file from a previous session. Repeating this option, more files are displayed. </p>
<dt><code>-T </code><i>&lt;type&gt;</i><code>, &#8211;output-type=</code><i>&lt;type&gt;</i></p>
<dd> Save the data as &lt;type&gt;, where &lt;type&gt; can be &#8220;nbe&#8221;, &#8220;html&#8221;, &#8220;html_graph&#8221;, &#8220;text&#8221;, &#8220;xml&#8221;, &#8220;old-xml&#8221;, &#8220;tex&#8221; or &#8220;nsr&#8221; </p>
<dt><code>-V, &#8211;verbose</code></p>
<dd> make the batch mode display status messages to the screen. </p>
<dt><code>-x, &#8211;dont-check-ssl-cert</code></p>
<dd> do not check SSL certificates. </p>
<dt><code>-v, &#8211;version</code></p>
<dd> shows version number and quits </p>
<dt><code>-h, &#8211;help</code></p>
<dd> lists the available options </p>
</dl>
</dl>
</dl>
<h2>The X11 interface</h2>
<p> The nessus client interface is divided in several panels:</p>
<dl>
<dt>* The &#8220;Nessusd host&#8221; section:</p>
<dd> In this section, you must enter the <code>nessusd </code> host to whom you will connect, as well as the port. You must also enter your <code>nessusd </code> user name and your password (not the one of the system). Once you are done, you must click on the &#8220;Log in&#8221; button, which will establish the connection to the <code>nessusd </code> host.<br />
 Once the connection is established, <code>nessusd</code> sends to the client the list of attacks it will perform, as well as the default preferences to use. </p>
<dt>* The &#8220;Target Selection&#8221; section:</p>
<dd> * In this section, you are required to enter the primary target. A primary target may be a single host (e.g. prof.fr.nessus.org), an IP (e.g. 192.168.1.1), a subnet (e.g. 192.168.1.1/24 or prof.fr.nessus.org), or a list of hosts, separated by commas (e.g. 192.168.1.1, 192.168.2.1/24, prof.fr.nessus.org, joyeux.fr.nessus.org). </p>
<p> * You can restrict the maximum number of hosts to test using the &#8220;Max Hosts&#8221; entry. This is a feature that prevents you from scanning too many machines; or accidentally scanning other machines. (For instance, if you only plan to test prof.fr.nessus.org and <a rel="nofollow" href="http://www.fr.nessus.org">www.fr.nessus.org</a>, you can safely set this entry to &#8220;2&#8221;). </p>
<p> * This panel also allows you to enable the &#8220;Perform a DNS zone transfer&#8221; option. This option is dangerous and should be enabled with caution. For instance, if you want to test <a rel="nofollow" href="http://www.nessus.org">www.nessus.org</a>, then if this option is set, <code>nessusd </code> will attempt to get the list of the hosts in the &#8220;nessus.org&#8221; domain. </p>
<p> This option may be dangerous. For instance, if you enable it and you ask to test 192.168.1.1/24, then <code>nessusd </code> will do a reverse lookup on <i>every</i> IP, and will attempt a DNS zone transfer on every domain. That is, if 192.168.1.1 is <a rel="nofollow" href="http://www.foo.bar">www.foo.bar</a>, and 192.168.1.10 is mail.bar.foo, then a DNS zone transfer will be made on the domains &#8220;foo.bar&#8221; and &#8220;bar.foo&#8221;. </p>
<dt>* The &#8220;Plugins&#8221; section</p>
<dd> Once you have successfully logged into the remote <code>nessusd </code> server, this section is filed with the list of the attacks that the server will perform. This panel is divided in two parts: the plugins families, and the plugins themselves. If you click on the name of a plugin, then a dialog will appear, showing you which will be the error message sent by the plugin if the attack is successful. </p>
</dl>
<h2>Report conversion</h2>
<p> You can use <code>nessus</code> to do conversion between formats used for reports. Nessus can take any NSR or NBE reports and change them into HTML, XML, NSR or NBE reports. Please note that the XML report provides usually more information about the scan itself NSR or NBE formats do not include in the report. Basically, XML is a merge between the .nbe reports and the .nessusrc configuration file. You won&#8217;t get extra verbosity or diagnosis info in the XML report, but you&#8217;ll know which plugins (and which version of these plugins) have been enabled during the scan. For more information on the report formats please read the files <code>nsr_file_format.txt</code> and <code>nbe_file_format.txt</code> provided along with the documentation. </p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>HOME</code></p>
<dd> The path to the user&#8217;s home directory which will hold the client configuration cache <i>.nessusrc</i>. The path is refered to as <i>~/</i>, below. </p>
<dt><code>NESSUSHOME</code></p>
<dd> If this environment variable is set, this path is used instead of the path defined by the <code>HOME</code> variable. This path is referred to as <i>~/</i>, below. </p>
<p> % More examples should be included here (jfs)</dl>
<h2>EXAMPLES</h2>
<p> To run a batch scan from a cron job and publish it in a given web space ( <code>/var/www/html/nessus/</code> ) try the following: <code>nessus -c /root/nessus/nessus.rc -T html -qx localhost 1241 batch batch1</code> <code>/root/nessus/target /var/www/html/nessus/results.html</code> Make sure that paranoia level is <code>not</code> set in your <code>nessus.rc</code> configuration file, otherwise the scan will not work </p>
<h2>FILES</h2>
<dl>
<dt><i>~/.nessusrc</i></p>
<dd> is the client configuration file, which contains the options about which <code>nessusd</code> server to connect to, which plugins to activate, and so on. The file is created automatically if it does not exist. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-nessus-mkcert-client/">nessus-mkcert-client</a></code>(1) </p>
<h2>MORE INFORMATION ABOUT THE NESSUS PROJECT</h2>
<p> The canonical places where you will find more information about the Nessus project are: </p>
<dl>
<dt>
<dd> <a rel="nofollow" href="http://www.nessus.org/">http://www.nessus.org/</a> (Official site)<br />
 <a rel="nofollow" href="http://cvs.nessus.org/">http://cvs.nessus.org/</a> (Developers site)</dl>
<h2>AUTHORS</h2>
<p> The Nessus Project was started and is being maintained by Renaud Deraison &lt;deraison [at] cvs.nessus.org&gt;. The <code>nessusd</code> server is mainly Copyright (C) 1998-2001 Renaud Deraison, as well as the attack modules. </p>
<p> Several other people have been kind enough to send patches and bug reports. Thanks to them. </p>
<h2>Index</h2>
