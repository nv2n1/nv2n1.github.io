---
title: "vdsm-tool(1)"
name: "vdsm-tool"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdsm-tool/"
description: "vdsm-tool – Virtual Desktops and Servers Manager Tool"
---

<h2>NAME</h2>
<p> vdsm-tool &#8211; Virtual Desktops and Servers Manager Tool</p>
<h2>SYNOPSIS</h2>
<p> vdsm-tool [options] &lt;action&gt; [arguments]</p>
<h2>DESCRIPTION</h2>
<p> <code>vdsm-tool</code> is a command line tool for configuring VDSM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>-l, &#8211;logfile &lt;path&gt;</code></p>
<dd> Specifies a path on the local file system to which any messages output by the operation being performed will be redirected.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> Specifies that additional information is to be included in logging.</p>
<dt><code>-a, &#8211;append</code></p>
<dd> Specifies that log files are to be appended to instead of truncated.</p>
<dt>Options for the <i>configurator</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>configure</code></p>
<dd> Configures external services for VDSM.</p>
<dl>
<dt>
<dd>
<p> Usage: <code>vdsm-tool [options] configure [-h|&#8230;]</code></p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>&#8211;module </code><i>STRING</i></p>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</p>
<dt><code>&#8211;force</code></p>
<dd> Forces configuration and triggers the restart of relevant services.</dl>
</dl>
<dt><code>is-configured</code></p>
<dd> Determines if a given module has been configured.</p>
<dl>
<dt>
<dd>
<p> Usage: <code>vdsm-tool is-configured [-h] [&#8211;module </code><i>STRING</i>]</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>&#8211;module </code><i>STRING</i></p>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</dl>
</dl>
<dt><code>validate-config</code></p>
<dd> Determines if the current configuration is valid.</p>
<dl>
<dt>
<dd>
<p> Usage: <code>vdsm-tool validate-config [-h] [&#8211;module </code><i>STRING</i>]</p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>&#8211;module </code><i>STRING</i></p>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</dl>
</dl>
</dl>
</dl>
<dt>Options for the <i>dummybr</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>dummybr</code></p>
<dd> Defines a dummy bridge on a libvirt network.</dl>
</dl>
<dt>Options for the <i>nwfilter</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>nwfilter</code></p>
<dd> Defines network filters on libvirt.</dl>
</dl>
<dt>Options for the <i>restore_nets</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>restore-nets</code></p>
<dd> Restores the networks to what was previously persisted via VDSM.</dl>
</dl>
<dt>Options for the <i>restore_nets_init</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>restore-nets-init</code></p>
<dd> Restore IP+link configuration of persisted networks.</dl>
</dl>
<dt>Options for the <i>service</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>service-disable</code></p>
<dd> Disables a system service.</p>
<dt><code>service-is-managed</code></p>
<dd> Checks whether a given system service exists.</p>
<dt><code>service-reload</code></p>
<dd> Notifies a system service to reload its configuration.</p>
<dt><code>service-restart</code></p>
<dd> Restarts a system service.</p>
<dt><code>service-start</code></p>
<dd> Starts a system service.</p>
<dt><code>service-status</code></p>
<dd> Gets the current status of a system service.</p>
<dt><code>service-stop</code></p>
<dd> Stops a system service.</dl>
</dl>
<dt>Options for the <i>transient</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>cleanup-transient-repository</code></p>
<dd> Cleans up the unused transient disks present in the repository. (NOTE: do NOT execute this command when the VDSM daemon is running.)</p>
<dt><code>setup-transient-repository</code></p>
<dd> Prepares the transient disks repository.</dl>
</dl>
<dt>Options for the <i>unified_persistence</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>upgrade-unified-persistence</code></p>
<dd> Upgrades host networking persistence from <code>ifcfg</code> to <code>unified</code> if the persistence model is set as <code>unified</code> in the <i>/usr/lib64/python2.X/site-packages/vdsm/config.py</i> file.</p>
<dl>
<dt>
<dd>
<p> Usage: <code>vdsm-tool upgrade-unified-persistence [-h] [&#8211;run-again]</code></p>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> Displays a list of options.</p>
<dt><code>&#8211;run-again</code></p>
<dd> Runs the upgrade operation again, even if this operation has been performed previously.</dl>
</dl>
</dl>
</dl>
<dt>Options for the <i>validate_ovirt_certs</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>validate-ovirt-certs</code></p>
<dd> Validates <i>vdsmcert.pem</i> against <i>cacert.pem</i>. If the current <i>cacert.pem</i> is invalid, the command will find a valid certificate file and replace the old <i>cacert.pem</i> with that certificate, and then persist that change.</dl>
</dl>
<dt>Options for the <i>vdsm-id</i> module:</p>
<dd>
<dl>
<dt>
<dd>
<dl>
<dt><code>vdsm-id</code></p>
<dd> Prints the host UUID.</dl>
</dl>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011-2014 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. </p>
<h2>Index</h2>
