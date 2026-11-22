---

title: "firehol(1)"
name: "firehol"
section: "1"
letter: "f"
url: "/docs/linux/man/1-firehol/"
description: "firehol – An easy to use but powerful iptables stateful firewall"
---

<p> firehol &#8211; An easy to use but powerful iptables stateful firewall</p>
<h2>SYNOPSIS</h2>
<p> <code>firehol</code> start|try|stop|restart|condrestart|status|panic|save|debug|helpme </p>
<p> <code>firehol</code> <i>configfile</i> [start|debug|try] </p>
<p> <code>firehol</code> <i>nothing</i></p>
<h2>DESCRIPTION</h2>
<p> <code>firehol</code> is an <code>iptables</code> firewall generator producing stateful <code>iptables</code> packet filtering firewalls, on Linux hosts and routers with any number of network interfaces, any number of routes, any number of services served, any number of complexity between variations of the services (including positive and negative expressions). </p>
<p> <code>firehol</code> is a language to express firewalling rules, not just a script that produces some kind of a firewall. </p>
<p> The goals of <code>firehol</code> are:</p>
<dl>
<dt>* Being as easy as possible</dt>
<dd> Independently of the security skills he/she has, <code>firehol</code> allows to create and understand complex firewalls in just a few seconds. The configuration files are very easy to type and read.</dd>
<dt>* Being as secure as possible.</dt>
<dd> By allowing explicitly only the wanted traffic to flow <code>firehol</code> secures your system. <code>firehol</code> produces stateful rules for any service or protocol, in both directions of the firewall.</dd>
<dt>* Being as open as possible.</dt>
<dd> Althoug <code>firehol</code> is pre-configured for a large number of services, you can configure any service you like and <code>firehol</code> will turn it into a client, a server, or a router.</dd>
<dt>* Being as flexible as possible.</dt>
<dd> <code>firehol</code> can be used by end users and guru administrators requiring extremely complex firewalls. <code>firehol</code> configuration files are BASH scripts; you can write in them anything BASH accepts, including variables, pipes, loops, conditions, calls to external programs, run other BASH scripts with <code>firehol</code> directives in them, etc.</dd>
<dt>* Being as simple as possible.</dt>
<dd> <code>firehol</code> is easy to install on any modern Linux system; only one file is required, no compilations involved.</dd></dl>
<h2>Options</h2>
<dl>
<dt>start</dt>
<dd> Activates the firewall configuration. The configuration is expected to be found in <i>/etc/firehol/firehol.conf</i>.</dd>
<dt>try</dt>
<dd> Activates the firewall, but waits until the user types the word commit. If this word is not typed within 30 seconds, the previous firewall is restored.</dd>
<dt>stop</dt>
<dd> Stops a running <code>iptables</code> firewall by running <tt>/etc/init.d/iptables stop</tt>. This will allow all traffic to pass unchecked.</dd>
<dt>restart</dt>
<dd> This is an alias for start and is given for compatibility with <code>/etc/init.d/iptables</code>.</dd>
<dt>condrestart</dt>
<dd> Starts the <code>firehol</code> firewall only if it is not already active. It does not detect a modified configuration file, only verifies that <code>firehol</code> has been started in the past and not stopped yet.</dd>
<dt>status</dt>
<dd> Shows the running firewall, as in <tt>/sbin/iptables -nxvL | less</tt></dd>
<dt>panic</dt>
<dd> It removes all rules from the running firewall and then it DROPs all traffic on all <code>iptables</code> tables (mangle, nat, filter) and pre-defined chains (PREROUTING, INPUT, FORWARD, OUTPUT, POSTROUTING), thus blocking all IP communication. DROPing is not done by changing the default policy to DROP, but by adding just one rule per table/chain to drop all traffic, because the default iptables scripts supplied by many systems (including RedHat 8) do not reset all the chains to ACCEPT when starting (<code>firehol</code> resets them correctly). </dd>
<p> When activating panic mode, <code>firehol</code> checks for the existance of the <code>SSH_CLIENT</code> shell environment variable (set by SSH). If it find this, then panic mode will allow the established SSH connection specified in this variable to operate. Notice that in order for this to work, you should have su without the minus (-) sign, since su &#8211; overwrites the shell variables and therefore the SSH_CLIENT variable is lost. </p>
<p> Alternativelly, after the panic argument you can specify an IP address in which case all established connections between this IP address and the host in panic will be allowed.</p>
<dt>save</dt>
<dd> Start the firewall and then save it using <code>/sbin/iptables-save</code> to <i>/etc/sysconfig/iptables</i>. </dd>
<p> Since v1.64, this is not implemented using <tt>/etc/init.d/iptables save</tt> because there is a bug in some versions of iptables-save that save invalid commands (<tt>! --uid-owner A</tt> is saved as <tt>--uid-owner !A</tt>) which cannot be restored. <code>firehol</code> fixes this problem (by saving it, and then replacing <tt>--uid-owner !</tt> with <tt>! --uid-owner</tt>). </p>
<p> Note that not all <code>firehol</code> firewalls will work if restored with: <tt>/etc/init.d/iptables start</tt> because FireHOL handles kernel modules and might have queried RPC servers (used by the NFS service) before starting the firewall. Also, <code>firehol</code> automatically checks current kernel configuration for client ports range. If you restore a firewall using the iptables service your firewall may not work as expected.</p>
<dt>debug</dt>
<dd> Parses the configuration file but instead of activating it, it shows the generated iptables statements.</dd>
<dt>explain</dt>
<dd> Enters an interactive mode where it accepts normal configuration commands and presents the generated iptables commands for each of them, together with some reasoning for its purpose. Additionally, it automatically generates a configuration script based on the successfull commands given. </dd>
<p> When in directive mode, <code>firehol</code> has the following special commands:</p>
<dl>
<dl>
<dt>* help</dt>
<dd> Present some help</dd>
<dt>* show</dt>
<dd> Present the generated <code>firehol</code> configuration</dd>
<dt>* quit</dt>
<dd> Exit interactive mode and quit <code>firehol</code></dd></dl>
</dl>
<dt>helpme</dt>
<dd> Tries to guess the <code>firehol</code> configuration needed for the current machine. <code>firehol</code> will not stop or alter the running firewall. The configuration file is given in the standard output of <code>firehol</code>, thus </dd>
<p> /etc/init.d/firehol helpme &gt;/tmp/firehol.conf </p>
<p> will produce the output in <i>/tmp/firehol.conf</i>. </p>
<p> The generated <code>firehol</code> configuration should and must be edited before used on your systems. You are required to take many decisions and the comments of the generated file will instruct you for many of them.</p>
<dt><i>configfile</i></dt>
<dd> A different configuration file. If no other argument is given, the configuration file will be tried (default = try). Otherwise the argument next to the filename can be one of start, debug, try.</dd>
<dt><i>nothing</i></dt>
<dd> Presents help about <code>firehol</code> usage.</dd></dl>
<h2>FILES</h2>
<dl>
<dl>
<dt><i>/etc/firehol/firehol.conf</i></dt>
<dd></dd></dl>
</dl>
<h2>AUTHOR</h2>
<p> <code>firehol</code> written by Costa Tsaousis &lt;costa [at] tsaousis.gr&gt;. </p>
<p> Man page written by Marc Brockschmidt &lt;marc [at] marcbrockschmidt.de&gt;.</p>
<h2>SEE ALSO</h2>
<p> firehol.conf(5), <a href="/docs/linux/man/8-iptables/">iptables</a>(8), <a href="/docs/linux/man/1-bash/">bash</a>(1) </p>
