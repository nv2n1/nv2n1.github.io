---
title: "fence_wti(8)"
name: "fence_wti"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_wti/"
description: "fence_wti – Fence agent for WTI"
---

<p>fence_wti &#8211; Fence agent for WTI</p>
<h2>Description</h2>
<p>fence_wti is an I/O Fencing agent which can be used with the WTI Network Power Switch (NPS). It logs into an NPS via telnet or ssh and boots a specified plug. Lengthy telnet connections to the NPS should be avoided while a GFS cluster is running because the connection will block any necessary fencing actions. </p>
<p> fence_wti accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_wti can be run by itself with command line options. This is useful for testing and for turning outlets on or off from scripts. </p>
<p> Vendor URL: <a rel="nofollow" href="http://www.wti.com">http://www.wti.com</a></p>
<h2>Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>-u, &#8211;ipport=[port]</code></dt>
<dd>TCP/UDP port to use for connection with device (Default Value: 23) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-a, &#8211;ip=[ip]</code></dt>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-n, &#8211;plug=[id]</code></dt>
<dd>Physical plug number, name of virtual machine or UUID This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-x, &#8211;ssh</code></dt>
<dd>SSH connection <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-c, &#8211;command-prompt=[prompt]</code></dt>
<dd>Force Python regex for command prompt (Default Value: [&#8216;RSM&gt;&#8217;, &#8216;MPC&gt;&#8217;, &#8216;IPS&gt;&#8217;, &#8216;TPS&gt;&#8217;, &#8216;NBB&gt;&#8217;, &#8216;NPS&gt;&#8217;, &#8216;VMR&gt;&#8217;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-6, &#8211;inet6-only</code></dt>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-k, &#8211;identity-file=[filename]</code></dt>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-4, &#8211;inet4-only</code></dt>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-S, &#8211;password-script=[script]</code></dt>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-p, &#8211;password=[password]</code></dt>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;ssh-options=[options]</code></dt>
<dd>SSH options to use <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-o, &#8211;action=[action]</code></dt>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-l, &#8211;username=[name]</code></dt>
<dd>Login Name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Verbose mode <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-D, &#8211;debug-file=[debugfile]</code></dt>
<dd>Write debug information to given file <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Display version information and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display help and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-C, &#8211;separator=[char]</code></dt>
<dd>Separator for CSV created by operation list (Default Value: ,) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;power-wait=[seconds]</code></dt>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;login-timeout=[seconds]</code></dt>
<dd>Wait X seconds for cmd prompt after login (Default Value: 5) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;power-timeout=[seconds]</code></dt>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;delay=[seconds]</code></dt>
<dd>Wait X seconds before fencing is started (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;shell-timeout=[seconds]</code></dt>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;retry-on=[attempts]</code></dt>
<dd>Count of attempts to retry power on (Default Value: 1) </dd>
</dl>
<h2>Actions</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>on </code></dt>
<dd>Power on machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>off </code></dt>
<dd>Power off machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>reboot </code></dt>
<dd>Reboot machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>status </code></dt>
<dd>This returns the status of the plug/virtual machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>list </code></dt>
<dd>List available plugs with aliases/virtual machines if there is support for more then one device. Returns N/A otherwise. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>list-status </code></dt>
<dd>List available plugs with aliases/virtual machines and their power state if it can be obtained without additional commands. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>monitor </code></dt>
<dd>Check the health of fence device <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>metadata </code></dt>
<dd>Display the XML metadata describing this resource. </dd>
</dl>
<h2>Stdin Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>ipport</code></dt>
<dd>TCP/UDP port to use for connection with device (Default Value: 23) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>ipaddr</code></dt>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>port</code></dt>
<dd>Physical plug number, name of virtual machine or UUID This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>secure</code></dt>
<dd>SSH connection <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>cmd_prompt</code></dt>
<dd>Force Python regex for command prompt (Default Value: [&#8216;RSM&gt;&#8217;, &#8216;MPC&gt;&#8217;, &#8216;IPS&gt;&#8217;, &#8216;TPS&gt;&#8217;, &#8216;NBB&gt;&#8217;, &#8216;NPS&gt;&#8217;, &#8216;VMR&gt;&#8217;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>inet6_only</code></dt>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>identity_file</code></dt>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>inet4_only</code></dt>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>passwd_script</code></dt>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>passwd</code></dt>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>ssh_options</code></dt>
<dd>SSH options to use <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>action</code></dt>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>login</code></dt>
<dd>Login Name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>verbose</code></dt>
<dd>Verbose mode <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>debug</code></dt>
<dd>Write debug information to given file <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>version</code></dt>
<dd>Display version information and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>help</code></dt>
<dd>Display help and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>separator</code></dt>
<dd>Separator for CSV created by operation list (Default Value: ,) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>power_wait</code></dt>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>login_timeout</code></dt>
<dd>Wait X seconds for cmd prompt after login (Default Value: 5) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>power_timeout</code></dt>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>delay</code></dt>
<dd>Wait X seconds before fencing is started (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>shell_timeout</code></dt>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>retry_on</code></dt>
<dd>Count of attempts to retry power on (Default Value: 1) </dd>
</dl>
