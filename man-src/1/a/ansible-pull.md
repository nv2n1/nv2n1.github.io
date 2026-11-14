---
title: "ansible-pull(1)"
name: "ansible-pull"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansible-pull/"
description: "ansible-pull – pull playbooks from VCS server and run them using this machine as the target."
---

<h2 class="name">NAME</h2>
<p> ansible-pull &#8211; pull playbooks from VCS server and run them using this machine as the target. </p>
<h2>SYNOPSIS</h2>
<p> ansible-pull -U URL [options] [ &lt;filename.yml&gt; ]</p>
<h2>DESCRIPTION</h2>
<p> <code>Ansible</code> is an extra-simple tool/framework/API for doing &#8216;remote things&#8217;. </p>
<p> Use ansible-pull to set up a remote copy of ansible on each managed node, each set to run via cron and update playbook source via a source repository. This inverts the default <code>push</code> architecture of ansible into a <code>pull</code> architecture, which has near-limitless scaling potential. </p>
<p> The setup playbook can be tuned to change the cron frequency, logging locations, and parameters to ansible-pull. </p>
<p> This is useful both for extreme scale-out as well as periodic remediation. Usage of the <i>fetch</i> module to retrieve logs from ansible-pull runs would be an excellent way to gather and analyze remote logs from ansible-pull.</p>
<h2>OPTIONAL ARGUMENT</h2>
<p> <code>filename.yml</code></p>
<dl>
<dt>
<dd> The name of one the YAML format files to run as an ansible playbook. This can be a relative path within the checkout. If not provided, ansible-pull will look for a playbook based on the host&#8217;s fully-qualified domain name, on the host hostname and finally a playbook named <code>local.yml</code>.</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;accept-host-key</code></p>
<dl>
<dt>
<dd> Adds the hostkey for the repo URL if not already added.</dl>
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
<p> <code>-C</code> <i>CHECKOUT</i>, <code>&#8211;checkout=</code><i>CHECKOUT</i></p>
<dl>
<dt>
<dd> Branch/Tag/Commit to checkout. If not provided, uses default behavior of module used to check out playbook repository.</dl>
<p> <code>-d</code> <i>DEST</i>, <code>&#8211;directory=</code><i>DEST</i></p>
<dl>
<dt>
<dd> Directory to checkout repository into. If not provided, a subdirectory of ~/.ansible/pull/ will be used.</dl>
<p> <code>-e</code> <i>EXTRA_VARS</i>, <code>&#8211;extra-vars=</code>&#8216;EXTRA_VARS</p>
<dl>
<dt>
<dd> Extra variables to inject into a playbook, in key=value key=value format or as quoted YAML/JSON (hashes and arrays). To load variables from a file, specify the file preceded by @ (e.g. @vars.yml).</dl>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Force running of playbook even if unable to update playbook repository. This can be useful, for example, to enforce run-time state when a network connection may not always be up or possible.</dl>
<p> <code>&#8211;full</code></p>
<dl>
<dt>
<dd> Do a full clone of the repository. By default ansible-pull will do a shallow clone based on the last revision.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show the help message and exit.</dl>
<p> <code>-i</code> <i>PATH</i>, <code>&#8211;inventory=</code><i>PATH</i></p>
<dl>
<dt>
<dd> The <i>PATH</i> to the inventory, which defaults to <i>/etc/ansible/hosts</i>. Alternatively you can use a comma separated list of hosts or single host with traling comma <i>host,</i>.</dl>
<p> <code>&#8211;private-key=</code><i>PRIVATE_KEY_FILE</i></p>
<dl>
<dt>
<dd> Use this file to authenticate the connection.</dl>
<p> <code>-m</code> <i>NAME</i>, <code>&#8211;module-name=</code><i>NAME</i></p>
<dl>
<dt>
<dd> Module used to checkout playbook repository. Defaults to git.</dl>
<p> <code>-o</code>, <code>&#8211;only-if-changed</code></p>
<dl>
<dt>
<dd> Only run the playbook if the repository has been updated.</dl>
<p> <code>&#8211;purge</code></p>
<dl>
<dt>
<dd> Purge the checkout after the playbook is run.</dl>
<p> <code>-s</code> <i>SLEEP</i>, <code>&#8211;sleep=</code><i>SLEEP</i></p>
<dl>
<dt>
<dd> Sleep for random interval (between 0 and SLEEP number of seconds) before starting. This is a useful way ot disperse git requests.</dl>
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
<p> <code>-t</code> <i>TAGS</i>, <code>&#8211;tags=</code><i>TAGS</i></p>
<dl>
<dt>
<dd> Only run plays and tasks tagged with these values.</dl>
<p> <code>-U</code> <i>URL</i>, <code>&#8211;url=</code><i>URL</i></p>
<dl>
<dt>
<dd> URL of the playbook repository to checkout.</dl>
<p> <code>&#8211;vault-password-file=</code><i>VAULT_PASSWORD_FILE</i></p>
<dl>
<dt>
<dd> Vault password file.</dl>
<p> <code>&#8211;clean</code></p>
<dl>
<dt>
<dd> Modified files in the working repository will be discarded.</dl>
<p> <code>&#8211;track-subs</code></p>
<dl>
<dt>
<dd> Submodules will track the latest changes.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Pass -vvv to ansible-playbook.</dl>
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
<p> <code><a href="/docs/linux/man/1-ansible/">ansible</a></code>(1) <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1), <code><a href="/docs/linux/man/1-ansible-doc/">ansible-doc</a></code>(1), <code><a href="/docs/linux/man/1-ansible-vault/">ansible-vault</a></code>(1), <code><a href="/docs/linux/man/1-ansible-galaxy/">ansible-galaxy</a></code>(1) </p>
<p> Extensive documentation is available in the documentation site: <a rel="nofollow" href="http://docs.ansible.com.">http://docs.ansible.com.</a> IRC and mailing list info can be found in file CONTRIBUTING.md, available in: <a href="https://github.com/ansible/ansible">https://github.com/ansible/ansible</a> </p>
<h2>Index</h2>
