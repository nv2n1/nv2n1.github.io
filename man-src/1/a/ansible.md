---
title: "ansible(1)"
name: "ansible"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansible/"
description: "ansible – run a task on a target host(s)"
---

<h2 class="name">NAME</h2>
<p> ansible &#8211; run a task on a target host(s) </p>
<h2>SYNOPSIS</h2>
<p> ansible &lt;host-pattern&gt; [-m module_name] [-a args] [options]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ansible</code> is an extra-simple tool/framework/API for doing &#8216;remote things&#8217;. This is the adhoc command that allows for a &#8216;single task playbook&#8217; run.</p>
<h2>ARGUMENTS</h2>
<p> <code>host-pattern</code></p>
<dl>
<dt>
<dd> A name of a group in the inventory, a shell-like glob selecting hosts in inventory or any combination of the two separated by commas.</dl>
<h2>OPTIONS</h2>
<p> <code>-a</code> &#8216;<i>ARGUMENTS</i>&#8216;, <code>&#8211;args=</code>&#8216;<i>ARGUMENTS</i>&#8216;</p>
<dl>
<dt>
<dd> The <i>ARGUMENTS</i> to pass to the module.</dl>
<p> <code>-b</code>, <code>&#8211;become</code></p>
<dl>
<dt>
<dd> Use privilege escalation (specific one depends on become_method), this does not imply prompting for passwords.</dl>
<p> <code>-K</code>, <code>&#8211;ask-become-pass</code></p>
<dl>
<dt>
<dd> Ask for privilege escalation password.</dl>
<p> <code>-k</code>, <code>&#8211;ask-pass</code></p>
<dl>
<dt>
<dd> Prompt for the connection password, if it is needed for the transport used. For example, using ssh and not having a key-based authentication with ssh-agent.</dl>
<p> <code>&#8211;ask-su-pass</code></p>
<dl>
<dt>
<dd> Prompt for su password, used with &#8211;su (deprecated, use become).</dl>
<p> <code>&#8211;ask-sudo-pass</code></p>
<dl>
<dt>
<dd> Prompt for the password to use with &#8211;sudo, if any (deprecated, use become).</dl>
<p> <code>&#8211;ask-vault-pass</code></p>
<dl>
<dt>
<dd> Prompt for vault password.</dl>
<p> <code>-B</code> <i>NUM</i>, <code>&#8211;background=</code><i>NUM</i></p>
<dl>
<dt>
<dd> Run commands in the background, killing the task after <i>NUM</i> seconds.</dl>
<p> <code>&#8211;become-method=</code><i>BECOME_METHOD</i></p>
<dl>
<dt>
<dd> Privilege escalation method to use (default=sudo), valid choices: [ sudo | su | pbrun | pfexec | doas | dzdo | ksu ]</dl>
<p> <code>&#8211;become-user=</code><i>BECOME_USER</i></p>
<dl>
<dt>
<dd> Run operations as this user (default=root).</dl>
<p> <code>-C</code>, <code>&#8211;check</code></p>
<dl>
<dt>
<dd> Do not make any changes on the remote system, but test resources to see what might have changed. Note this can not scan all possible resource types and is only a simulation.</dl>
<p> <code>-c</code> <i>CONNECTION</i>, <code>&#8211;connection=</code><i>CONNECTION</i></p>
<dl>
<dt>
<dd> Connection type to use. Most common options are <i>paramiko</i> (SSH), <i>ssh</i>, <i>winrm</i> and <i>local</i>. <i>local</i> is mostly useful for crontab or kickstarts.</dl>
<p> <code>-e</code> <i>EXTRA_VARS, </i><i></i><code>&#8211;extra-vars=</code><i>&#8216;EXTRA_VARS</i></p>
<dl>
<dt>
<dd> Extra variables to inject into a playbook, in key=value key=value format or as quoted YAML/JSON (hashes and arrays). To load variables from a file, specify the file preceded by @ (e.g. @vars.yml).</dl>
<p> <code>-f</code> <i>NUM</i>, <code>&#8211;forks=</code><i>NUM</i></p>
<dl>
<dt>
<dd> Level of parallelism. <i>NUM</i> is specified as an integer, the default is 5.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show help message and exit.</dl>
<p> <code>-i</code> <i>PATH</i>, <code>&#8211;inventory=</code><i>PATH</i></p>
<dl>
<dt>
<dd> The <i>PATH</i> to the inventory, which defaults to <i>/etc/ansible/hosts</i>. Alternatively you can use a comma separated list of hosts or single host with trailing comma <i>host,</i>.</dl>
<p> <code>-l</code> <i>SUBSET</i>, <code>&#8211;limit=</code><i>SUBSET</i></p>
<dl>
<dt>
<dd> Further limits the selected host/group patterns. You can prefix it with <i>~</i> to indicate that the pattern is a regex.</dl>
<p> <code>&#8211;list-hosts</code></p>
<dl>
<dt>
<dd> Outputs a list of matching hosts; does not execute anything else.</dl>
<p> <code>-m</code> <i>NAME</i>, <code>&#8211;module-name=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Execute the module called <i>NAME</i>.</dl>
<p> <code>-M</code> <i>DIRECTORY</i>, <code>&#8211;module-path=</code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> The <i>DIRECTORY</i> search path to load modules from. The default is <i>/usr/share/ansible</i>. This can also be set with the ANSIBLE_LIBRARY environment variable.</dl>
<p> <code>-o</code>, <code>&#8211;one-line</code></p>
<dl>
<dt>
<dd> Try to output everything on one line.</dl>
<p> <code>-P</code> <i>NUM</i>, <code>&#8211;poll=</code><i>NUM</i></p>
<dl>
<dt>
<dd> Poll a background job every <i>NUM</i> seconds. Requires <code>-B</code>.</dl>
<p> <code>&#8211;private-key=</code><i>PRIVATE_KEY_FILE</i></p>
<dl>
<dt>
<dd> Use this file to authenticate the connection.</dl>
<p> <code>-S</code>, <code>&#8211;su</code></p>
<dl>
<dt>
<dd> Run operations with su (deprecated, use become).</dl>
<p> <code>-R</code> <i>SU_USER</i>, <code>&#8211;se-user=</code><i>SUDO_USER</i></p>
<dl>
<dt>
<dd> Run operations with su as this user (default=root) (deprecated, use become).</dl>
<p> <code>-s</code>, <code>&#8211;sudo</code></p>
<dl>
<dt>
<dd> Run the command as the user given by -u and sudo to root (deprecated, use become).</dl>
<p> <code>&#8211;ssh-common-args=</code><i>&#8216;-o ProxyCommand=&quot;ssh -W %h:%p &#8230;&quot; &#8230;</i>&#8216;</p>
<dl>
<dt>
<dd> Add the specified arguments to any sftp/scp/ssh command-line. Useful to set a ProxyCommand to use a jump host, but any arguments that are accepted by all three programs may be specified.</dl>
<p> <code>&#8211;sftp-extra-args=</code><i>&#8216;-f &#8230;</i>&#8216;</p>
<dl>
<dt>
<dd> Add the specified arguments to any sftp command-line.</dl>
<p> <code>&#8211;scp-extra-args=</code><i>&#8216;-l &#8230;</i>&#8216;</p>
<dl>
<dt>
<dd> Add the specified arguments to any scp command-line.</dl>
<p> <code>&#8211;ssh-extra-args=</code><i>&#8216;-R &#8230;</i>&#8216;</p>
<dl>
<dt>
<dd> Add the specified arguments to any ssh command-line.</dl>
<p> <code>-U</code> <i>SUDO_USERNAME</i>, <code>&#8211;sudo-user=</code><i>SUDO_USERNAME</i></p>
<dl>
<dt>
<dd> Sudo to <i>SUDO_USERNAME</i> default is root. (deprecated, use become).</dl>
<p> <code>-t</code> <i>DIRECTORY</i>, <code>&#8211;tree=</code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Save contents in this output <i>DIRECTORY</i>, with the results saved in a file named after each host.</dl>
<p> <code>-T</code> <i>SECONDS</i>, <code>&#8211;timeout=</code><i>SECONDS</i></p>
<dl>
<dt>
<dd> Connection timeout to use when trying to talk to hosts, in <i>SECONDS</i>.</dl>
<p> <code>-u</code> <i>USERNAME</i>, <code>&#8211;user=</code><i>USERNAME</i></p>
<dl>
<dt>
<dd> Use this <i>USERNAME</i> to login to the target host, instead of the current user.</dl>
<p> <code>&#8211;vault-password-file=</code><i>VAULT_PASSWORD_FILE</i></p>
<dl>
<dt>
<dd> A file containing the vault password to be used during the decryption of vault encrypted files. Be sure to keep this file secured if it is used. If the file is executable, it will be run and its standard output will be used as the password.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Verbose mode, more output from successful actions will be shown. Give up to three times for more output.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Show program version number and exit.</dl>
<h2>INVENTORY</h2>
<p> Ansible stores the hosts it can potentially operate on in an inventory. This can be an ini-like file, a script, directory or a list. The ini syntax is one host per line. Groups headers are allowed and are included on their own line, enclosed in square brackets that start the line. </p>
<p> Ranges of hosts are also supported. For more information and additional options, see the documentation on <a rel="nofollow" href="http://docs.ansible.com/.">http://docs.ansible.com/.</a></p>
<h2>ENVIRONMENT</h2>
<p> The following environment variables may be specified. </p>
<p> ANSIBLE_INVENTORY &#8212; Override the default ansible inventory file </p>
<p> ANSIBLE_LIBRARY &#8212; Override the default ansible module library path </p>
<p> ANSIBLE_CONFIG &#8212; Override the default ansible config file </p>
<p> Many more are available for most options in ansible.cfg</p>
<h2>FILES</h2>
<p> /etc/ansible/hosts &#8212; Default inventory file </p>
<p> /usr/share/ansible/ &#8212; Default module library </p>
<p> /etc/ansible/ansible.cfg &#8212; Config file, used if present </p>
<p> ~/.ansible.cfg &#8212; User config file, overrides the default config if present</p>
<h2>AUTHOR</h2>
<p> Ansible was originally written by Michael DeHaan. See the AUTHORS file for a complete list of contributors.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012, Michael DeHaan Ansible is released under the terms of the GPLv3 License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1), <code><a href="/docs/linux/man/1-ansible-pull/">ansible-pull</a></code>(1), <code><a href="/docs/linux/man/1-ansible-doc/">ansible-doc</a></code>(1), <code><a href="/docs/linux/man/1-ansible-vault/">ansible-vault</a></code>(1), <code><a href="/docs/linux/man/1-ansible-galaxy/">ansible-galaxy</a></code>(1) </p>
<p> Extensive documentation is available in the documentation site: <a rel="nofollow" href="http://docs.ansible.com.">http://docs.ansible.com.</a> IRC and mailing list info can be found in file CONTRIBUTING.md, available in: <a href="https://github.com/ansible/ansible">https://github.com/ansible/ansible</a> </p>
<h2>Index</h2>
