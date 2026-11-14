---
title: "netdump-server(8)"
name: "netdump-server"
section: "8"
letter: "n"
url: "/docs/linux/man/8-netdump-server/"
description: "netdump-server – handle crash dumps over the network"
---

<p>netdump-server &#8211; handle crash dumps over the network</p>
<h2>Synopsis</h2>
<pre><code>netdump-server [--port </code><i>portnumber</i>]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--addr </code><i>address</i>]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--concurrent </code><i>number</i>]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--pidfile </code><i>path</i>]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--dumpdir </code><i>path</i>]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--daemon]</code>
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--secure &lt;</code><i>0|1</i>&gt;]
<code>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>[--help] [--usage]</code></pre>
<h2>Description</h2>
<p>Listens to the network for clients that crash and uses the netdump protocol to recieve a memory dump and a stack trace. The memory dump and oops message are stored in a timestamped directory in /var/crash. The server can also run scripts when some events happen.</p>
<h2>Options</h2>
<dl>
<dt>&#8211;port <i>portnumber</i></p>
<dd>Specifies the IP port number for the netdump server to listen to. The default is 6666.</p>
<dt>&#8211;addr <i>address</i></p>
<dd>Specifies the IP address for the netdump server to listen to. The default is any.</p>
<dt>&#8211;concurrent <i>number</i></p>
<dd>You can limit the amount of concurrent dumps being done at any one time. If more clients than the specified maximum connects at one time the last ones will just be logged and then rebooted.</p>
<dt>&#8211;dumpdir <i>path</i></p>
<dd>Specify the location where received vmcore files are saved. Defaults to /var/crash</p>
<dt>&#8211;pidfile <i>path</i></p>
<dd>Store a pidfile. The default service uses /var/run/netdump-server.pid. The default is not to write a pidfile.</p>
<dt>&#8211;daemon</p>
<dd>netdump-server should background itself and run as a daemon.</p>
<dt>&#8211;secure</p>
<dd>Specify a 0 here to disable the client authentication bits. This will enable any client to dump core to this server without any credentials. If using this option, you may specify the <code>NETDUMPKEYEXCHANGE=none</code> option in <i>/etc/sysconfig/netdump </i> on the client systems.</dl>
<h2>Examples</h2>
<pre><code>netdump-server --daemon</code></pre>
<p>This launches the netdump-server and puts it in the background, listening for crashed clients. </p>
<h2>Exit Status</h2>
<p>Exit status is 0 for a clean exit and non-0 for a non-clean exit.</p>
<h2>Files</h2>
<dl>
<dt>/etc/netdump.conf</p>
<dd>A configuration file read by netdump-server on startup. It is a &quot;key=value&quot; style file. Currently it supports the options: port, max_concurrent_dumps, daemon, pidfile and secure.</p>
<dt>/etc/init.d/netdump-server</p>
<dd>An init script to start a default system installation of netdump-server. This is normally turned off by default; use the command </p>
<pre>/sbin/chkconfig netdump-server on</pre>
<p>to enable the netdump-server service.</p>
<dt>/var/crash</p>
<dd>The main directory where the crash dump files are stored. Each dump is put in a subdirectory named with the ip of the crashed machine and the date and time of the crash.</p>
<dt>/var/crash/scripts</p>
<dd>This directory can contain scripts that are run at various times. The script files should be executable and owned by the netdump user. They all get passed the ip of the crashing machine as the first argument, and each one except netdump-start gets the directory that the dump is written into as the second argument. </p>
<p> netdump-start &#8211; This is called when a client connects to the server to tell it that it has just started the netdump client. This normally means that the machine just booted up. </p>
<p> netdump-crash &#8211; This is run when a client reports that it has crashed. If it returns a non-zero value the dump request will be ignored and the client will be told to reboot immediately </p>
<p> netdump-nospace &#8211; This is run when there is not enough diskspace for the dump of the crashed machine. If this script exits with a non-zero return value netdump-server will try once again (but only once) before giving up the dump. If this script exits with a zero return value, netdump-server will reboot the client without performing a dump. </p>
<p> netdump-reboot &#8211; This is run when netdump-server is finished with a client and is about to tell the client to reboot itself. </p>
<p> The four executable scripts are run in the foreground by the netdump-server, so any time-consuming task done by the scripts will block the netdump-server from servicing any crash or log requests from any other source. Therefore it may be advisable to run any time-consuming tasks in the background, allowing the script to return back to the netdump-server. </p>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-netdump/">netdump</a></code>(8) </p>
<h2>Bugs</h2>
<p>Report any bugs you find to <a rel="nofollow" href="http://bugzilla.redhat.com/bugzilla">http://bugzilla.redhat.com/bugzilla</a> </p>
<h2>Author</h2>
<p>Alexander Larsson &lt;alexl [at] redhat.com&gt;</p>
