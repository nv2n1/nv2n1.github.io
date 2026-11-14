---
title: "atomic-openshift-installer(1)"
name: "atomic-openshift-installer"
section: "1"
letter: "a"
url: "/docs/linux/man/1-atomic-openshift-installer/"
description: "atomic-openshift-installer – Interactive OpenShift Container Platform (OCP) installer"
---

<h2 class="name">NAME</h2>
<p> atomic-openshift-installer &#8211; Interactive OpenShift Container Platform (OCP) installer </p>
<h2>SYNOPSIS</h2>
<p> atomic-openshift-installer [OPTIONS] COMMAND [OPTS]</p>
<h2>DESCRIPTION</h2>
<p> <code>atomic-openshift-installer</code> makes the process for installing OCP easier by interactively gathering the data needed to run on each host. It can also be run in unattended mode if provided with a configuration file.</p>
<h2>OPTIONS</h2>
<p> The following options are common to all commands. </p>
<p> <code>-u</code>, <code>&#8211;unattended</code></p>
<dl>
<dt>
<dd> Run installer in <code>unattended</code> mode. You will not be prompted to answer any questions.</dl>
<p> <code>-c</code>, <code>&#8211;configuration</code> <i>PATH</i></p>
<dl>
<dt>
<dd> Provide an alternate <i>PATH</i> to an <i>installer.cfg.yml</i> file.</dl>
<p> <code>-a</code> <i>DIRECTORY</i>, <code>&#8211;ansible-playbook-directory</code> <i>DIRECTORY</i></p>
<dl>
<dt>
<dd> Manually set the <i>DIRECTORY</i> in which to look for Ansible playbooks.</dl>
<p> <code>&#8211;ansible-log-path</code> <i>PATH</i></p>
<dl>
<dt>
<dd> Specify the <i>PATH</i> of the directory in which to save Ansible logs.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Run the installer with more verbosity.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dt>
<dd> Enable installer debugging. Logs are saved in <i>/tmp/installer.txt</i>.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Show the usage help and exit.</dl>
<h2>COMMANDS</h2>
<p> <code>atomic-openshift-installer</code> has three modes of operation: </p>
<dl>
<dt>
<dd> &bull; <code>install</code></dl>
<dl>
<dt>
<dd> &bull; <code>uninstall</code></dl>
<dl>
<dt>
<dd> &bull; <code>upgrade</code></dl>
<dl>
<dt>
<dd> &bull; <code>scaleup</code></dl>
<p> The options specific to each command are described in the following sections.</p>
<h2>INSTALL</h2>
<p> The <code>install</code> command will guide you through steps required to install an OCP cluster. After all of the required information has been collected (target hosts, storage options, high-availability), the installation will begin. </p>
<p> <code>-f</code>, <code>&#8211;force</code></p>
<dl>
<dt>
<dd> Forces an installation. This means that hosts with existing installations will be reinstalled if required.</dl>
<p> <code>&#8211;gen-inventory</code></p>
<dl>
<dt>
<dd> Generate an Ansible inventory file and exit. The default location for the inventory file is <i>~/.config/openshift/hosts</i>.</dl>
<h2>UNINSTALL</h2>
<p> The <code>uninstall</code> command will uninstall OCP from your target hosts. This command has no additional options.</p>
<h2>UPGRADE</h2>
<p> The <code>upgrade</code> command will upgrade a cluster of hosts to a newer version of OCP. </p>
<p> <code>-l</code>, <code>&#8211;latest-minor</code></p>
<dl>
<dt>
<dd> Upgrade to the latest minor version. For example, if you are running version <code>3.2.1</code> then this could upgrade you to <code>3.2.2</code>.</dl>
<p> <code>-n</code>, <code>&#8211;next-major</code></p>
<dl>
<dt>
<dd> Upgrade to the latest major version. For example, if you are running version <code>3.2</code> then this could upgrade you to <code>3.3</code>.</dl>
<h2>SCALEUP</h2>
<p> The <code>scaleup</code> command is used to add new nodes to an existing cluster. This command has no additional options.</p>
<h2>FILES</h2>
<p> <code>~/.config/openshift/installer.cfg.yml</code> &#8212; Installer configuration file. Can be used to generate an inventory later or start an unattended installation. </p>
<p> <code>~/.config/openshift/hosts</code> &#8212; Generated Ansible inventory file. Used to run the Ansible playbooks for install, uninstall, and upgrades. </p>
<p> <code>/tmp/ansible.log</code> &#8212; The default location of the ansible log file. </p>
<p> <code>/tmp/installer.txt</code> &#8212; The location of the log file for debugging the installer.</p>
<h2>AUTHOR</h2>
<p> Red Hat OpenShift Productization team </p>
<p> For a complete list of contributors, please visit the GitHub charts page.</p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Red Hat, Inc. </p>
<p> <code>atomic-openshift-installer</code> is released under the terms of the ASL 2.0 license.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-ansible/">ansible</a></code>(1), <code><a href="/docs/linux/man/1-ansible-playbook/">ansible-playbook</a></code>(1) </p>
<p> <code>The openshift-ansible GitHub Project</code> &#8212; <a rel="nofollow" href="https://github.com/openshift/openshift-ansible/">https://github.com/openshift/openshift-ansible/</a> </p>
<p> <code>The atomic-openshift-installer Documentation</code> &#8212; <a rel="nofollow" href="https://docs.openshift.com/container-platform/3.3/install_config/install/quick_install.html">https://docs.openshift.com/container-platform/3.3/install_config/install/quick_install.html</a> </p>
<h2>Index</h2>
