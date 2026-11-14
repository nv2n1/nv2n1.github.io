---
title: "fence_virsh(8)"
name: "fence_virsh"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_virsh/"
description: "fence_virsh – Fence agent for virsh"
---

<p>fence_virsh &#8211; Fence agent for virsh</p>
<h2>Description</h2>
<p>fence_virsh is an I/O Fencing agent which can be used with the virtual machines managed by libvirt. It logs via ssh to a dom0 and there run virsh command, which does all work. </p>
<p> By default, virsh needs root account to do properly work. So you must allow ssh login in your sshd_config. </p>
<p> fence_virsh accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_virsh can be run by itself with command line options. This is useful for testing and for turning outlets on or off from scripts. </p>
<p> Vendor URL: <a rel="nofollow" href="http://libvirt.org">http://libvirt.org</a></p>
<h2>Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>-u, &#8211;ipport=[port]</code></p>
<dd>TCP/UDP port to use for connection with device (Default Value: 22) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-a, &#8211;ip=[ip]</code></p>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-n, &#8211;plug=[id]</code></p>
<dd>Physical plug number, name of virtual machine or UUID This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-x, &#8211;ssh</code></p>
<dd>SSH connection (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-c, &#8211;command-prompt=[prompt]</code></p>
<dd>Force Python regex for command prompt (Default Value: [&#8216;\[EXPECT\]#\ &#8216;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-6, &#8211;inet6-only</code></p>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-k, &#8211;identity-file=[filename]</code></p>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-4, &#8211;inet4-only</code></p>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-S, &#8211;password-script=[script]</code></p>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-p, &#8211;password=[password]</code></p>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;ssh-options=[options]</code></p>
<dd>SSH options to use (Default Value: -t &#8216;/bin/bash -c &quot;PS1=T\#&nbsp;<wbr> /bin/bash &#8211;noprofile &#8211;norc&quot;&#8217;) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-o, &#8211;action=[action]</code></p>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-l, &#8211;username=[name]</code></p>
<dd>Login Name This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Verbose mode <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-D, &#8211;debug-file=[debugfile]</code></p>
<dd>Write debug information to given file <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-V, &#8211;version</code></p>
<dd>Display version information and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-h, &#8211;help</code></p>
<dd>Display help and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>-C, &#8211;separator=[char]</code></p>
<dd>Separator for CSV created by operation list (Default Value: ,) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;power-wait=[seconds]</code></p>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;login-timeout=[seconds]</code></p>
<dd>Wait X seconds for cmd prompt after login (Default Value: 5) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;power-timeout=[seconds]</code></p>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;delay=[seconds]</code></p>
<dd>Wait X seconds before fencing is started (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;shell-timeout=[seconds]</code></p>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;missing-as-off</code></p>
<dd>Missing port returns OFF instead of failure <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;retry-on=[attempts]</code></p>
<dd>Count of attempts to retry power on (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>&#8211;use-sudo</code></p>
<dd>Use sudo (without password) when calling 3rd party sotfware. </p>
</dl>
<h2>Actions</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>on </code></p>
<dd>Power on machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>off </code></p>
<dd>Power off machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>reboot </code></p>
<dd>Reboot machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>status </code></p>
<dd>This returns the status of the plug/virtual machine. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>list </code></p>
<dd>List available plugs with aliases/virtual machines if there is support for more then one device. Returns N/A otherwise. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>list-status </code></p>
<dd>List available plugs with aliases/virtual machines and their power state if it can be obtained without additional commands. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>monitor </code></p>
<dd>Check the health of fence device <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>metadata </code></p>
<dd>Display the XML metadata describing this resource. </p>
</dl>
<h2>Stdin Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>ipport</code></p>
<dd>TCP/UDP port to use for connection with device (Default Value: 22) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>ipaddr</code></p>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>port</code></p>
<dd>Physical plug number, name of virtual machine or UUID This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>secure</code></p>
<dd>SSH connection (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>cmd_prompt</code></p>
<dd>Force Python regex for command prompt (Default Value: [&#8216;\[EXPECT\]#\ &#8216;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>inet6_only</code></p>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>identity_file</code></p>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>inet4_only</code></p>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>passwd_script</code></p>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>passwd</code></p>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>ssh_options</code></p>
<dd>SSH options to use (Default Value: -t &#8216;/bin/bash -c &quot;PS1=T\#&nbsp;<wbr> /bin/bash &#8211;noprofile &#8211;norc&quot;&#8217;) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>action</code></p>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>login</code></p>
<dd>Login Name This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>verbose</code></p>
<dd>Verbose mode <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>debug</code></p>
<dd>Write debug information to given file <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>version</code></p>
<dd>Display version information and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>help</code></p>
<dd>Display help and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>separator</code></p>
<dd>Separator for CSV created by operation list (Default Value: ,) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>power_wait</code></p>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>login_timeout</code></p>
<dd>Wait X seconds for cmd prompt after login (Default Value: 5) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>power_timeout</code></p>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>delay</code></p>
<dd>Wait X seconds before fencing is started (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>shell_timeout</code></p>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>missing_as_off</code></p>
<dd>Missing port returns OFF instead of failure <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>retry_on</code></p>
<dd>Count of attempts to retry power on (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dt><code>sudo</code></p>
<dd>Use sudo (without password) when calling 3rd party sotfware. </p>
</dl>
