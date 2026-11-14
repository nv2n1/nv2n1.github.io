---
title: "ansible-doc(1)"
name: "ansible-doc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-ansible-doc/"
description: "ansible-doc – show documentation on Ansible modules"
---

<h2 class="name">NAME</h2>
<p> ansible-doc &#8211; show documentation on Ansible modules </p>
<h2>SYNOPSIS</h2>
<p> ansible-doc [-M module_path] [-l] [-s] [module&#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>ansible-doc</code> displays information on modules installed in Ansible libraries. It displays a terse listing of modules and their short descriptions, provides a printout of their DOCUMENTATION strings, and it can create a short &quot;snippet&quot; which can be pasted into a playbook.</p>
<h2>OPTIONS</h2>
<p> <code>-M</code> <i>DIRECTORY</i>, <code>&#8211;module-path=</code><i>DIRECTORY</i></p>
<dl>
<dt>
<dd> the <i>DIRECTORY</i> search path to load modules from. The default is <i>/usr/share/ansible</i>. This can also be set with the ANSIBLE_LIBRARY environment variable.</dl>
<p> <code>-s</code>, <code>&#8211;snippet=</code></p>
<dl>
<dt>
<dd> Produce a snippet which can be copied into a playbook for modification, like a kind of task template.</dl>
<p> <code>-l</code>, <code>&#8211;list=</code></p>
<dl>
<dt>
<dd> Produce a terse listing of modules and a short description of each.</dl>
<h2>ENVIRONMENT</h2>
<p> ANSIBLE_LIBRARY &#8212; Override the default ansible module library path</p>
<h2>FILES</h2>
<p> /usr/share/ansible/ &#8212; Default module library </p>
<p> /etc/ansible/ansible.cfg &#8212; Config file, used if present </p>
<p> ~/.ansible.cfg &#8212; User config file, overrides the default config if present</p>
<h2>AUTHOR</h2>
<p> ansible-doc was originally written by Jan-Piet Mens. See the AUTHORS file for a complete list of contributors.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2012, Jan-Piet Mens </p>
<p> Ansible is released under the terms of the GPLv3 License.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1), <code><a href="/docs/linux/man/1-ansible/">ansible</a></code>(1), <code><a href="/docs/linux/man/1-ansible-pull/">ansible-pull</a></code>(1), <code><a href="/docs/linux/man/1-ansible-vault/">ansible-vault</a></code>(1), <code><a href="/docs/linux/man/1-ansible-galaxy/">ansible-galaxy</a></code>(1) </p>
<p> Extensive documentation is available in the documentation site: <a rel="nofollow" href="http://docs.ansible.com.">http://docs.ansible.com.</a> IRC and mailing list info can be found in file CONTRIBUTING.md, available in: <a href="https://github.com/ansible/ansible">https://github.com/ansible/ansible</a> </p>
<h2>Index</h2>
