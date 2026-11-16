---
title: "fence_lpar(8)"
name: "fence_lpar"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fence_lpar/"
description: "fence_lpar – Fence agent for IBM LPAR"
---

<p>fence_lpar &#8211; Fence agent for IBM LPAR</p>
<h2>Description</h2>
<p>fence_lpar accepts options on the command line as well as from stdin. Fenced sends parameters through stdin when it execs the agent. fence_lpar can be run by itself with command line options. This is useful for testing and for turning outlets on or off from scripts. </p>
<h2>Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>-o, &#8211;action=&lt;action&gt;</code></dt>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-a, &#8211;ip=&lt;ip&gt;</code></dt>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-l, &#8211;username=&lt;name&gt;</code></dt>
<dd>Login Name This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-p, &#8211;password=&lt;password&gt;</code></dt>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-S, &#8211;password-script=&lt;script&gt;</code></dt>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-x, &#8211;ssh</code></dt>
<dd>SSH connection (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-k, &#8211;identity-file=&lt;filename&gt;</code></dt>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-n &lt;id&gt; Name of the partition</code></dt>
<dd>Partition name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-s &lt;id&gt; Name of the managed system</code></dt>
<dd>Managed system name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-H, &#8211;hmc-version=&lt;version&gt;</code></dt>
<dd>Force HMC version to use (3 or 4) (Default Value: 4) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-c, &#8211;command-prompt=&lt;prompt&gt;</code></dt>
<dd>Force command prompt (Default Value: [&#8216;:~&gt;&#8217;, &#8216;]\$&#8217;, &#8216;\$ &#8216;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-4, &#8211;inet4-only</code></dt>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-6, &#8211;inet6-only</code></dt>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-u, &#8211;ipport=&lt;port&gt;</code></dt>
<dd>TCP port to use for connection with device <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd>Verbose mode <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-D, &#8211;debug-file=&lt;debugfile&gt;</code></dt>
<dd>Write debug information to given file <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-V, &#8211;version</code></dt>
<dd>Display version information and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-h, &#8211;help</code></dt>
<dd>Display help and exit <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>-C, &#8211;separator=&lt;char&gt;</code></dt>
<dd>Separator for CSV created by operation list (Default Value: ,) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;power-timeout</code></dt>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;shell-timeout</code></dt>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;login-timeout</code></dt>
<dd>Wait X seconds for cmd prompt after login (Default Value: 15) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;power-wait</code></dt>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;retry-on</code></dt>
<dd>Count of attempts to retry power on (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>&#8211;delay</code></dt>
<dd>Wait X seconds before fencing is started (Default Value: 0) </dd>
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
<dt><code>monitor </code></dt>
<dd>Check if fencing device is running. List available plugs/virtual machines or get status of machine (if it does not support more). <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>metadata </code></dt>
<dd>&nbsp;<wbr>The operational behavior of this is not known. </dd>
</dl>
<h2>Stdin Parameters</h2>
<p><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></p>
<dl>
<dt><code>action</code></dt>
<dd>Fencing Action (Default Value: reboot) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>ipaddr</code></dt>
<dd>IP Address or Hostname This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>login</code></dt>
<dd>Login Name This parameter is always required. <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>passwd</code></dt>
<dd>Login password or passphrase <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>passwd_script</code></dt>
<dd>Script to retrieve password <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>secure</code></dt>
<dd>SSH connection (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>identity_file</code></dt>
<dd>Identity file for ssh <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>partition</code></dt>
<dd>Partition name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>managed</code></dt>
<dd>Managed system name <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>hmc_version</code></dt>
<dd>Force HMC version to use (3 or 4) (Default Value: 4) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>cmd_prompt</code></dt>
<dd>Force command prompt (Default Value: [&#8216;:~&gt;&#8217;, &#8216;]\$&#8217;, &#8216;\$ &#8216;]) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>inet4_only</code></dt>
<dd>Forces agent to use IPv4 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>inet6_only</code></dt>
<dd>Forces agent to use IPv6 addresses only <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>ipport</code></dt>
<dd>TCP port to use for connection with device <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
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
<dt><code>power_timeout</code></dt>
<dd>Test X seconds for status change after ON/OFF (Default Value: 20) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>shell_timeout</code></dt>
<dd>Wait X seconds for cmd prompt after issuing command (Default Value: 3) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>login_timeout</code></dt>
<dd>Wait X seconds for cmd prompt after login (Default Value: 15) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>power_wait</code></dt>
<dd>Wait X seconds after issuing ON/OFF (Default Value: 0) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>retry_on</code></dt>
<dd>Count of attempts to retry power on (Default Value: 1) <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt></dd>
<dt><code>delay</code></dt>
<dd>Wait X seconds before fencing is started (Default Value: 0) </dd>
</dl>
