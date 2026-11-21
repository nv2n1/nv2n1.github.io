---

title: "vdsm-tool(1)"
name: "vdsm-tool"
section: "1"
letter: "v"
url: "/docs/linux/man/1-vdsm-tool/"
description: "vdsm-tool – Virtual Desktops and Servers Manager Tool"
---

<p> vdsm-tool &#8211; Virtual Desktops and Servers Manager Tool</p>
<h2>SYNOPSIS</h2>
<p> vdsm-tool [options] &lt;action&gt; [arguments]</p>
<h2>DESCRIPTION</h2>
<p> <code>vdsm-tool</code> is a command line tool for configuring VDSM.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>-l, &#8211;logfile &lt;path&gt;</code></dt>
<dd> Specifies a path on the local file system to which any messages output by the operation being performed will be redirected.</dd>
<dt><code>-v, &#8211;verbose</code></dt>
<dd> Specifies that additional information is to be included in logging.</dd>
<dt><code>-a, &#8211;append</code></dt>
<dd> Specifies that log files are to be appended to instead of truncated.</dd>
<dt>Options for the <i>configurator</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>configure</code></dt>
<dd> Configures external services for VDSM.</dd>
<dl>
<dt>
</dt><dd>
<p> Usage: <code>vdsm-tool [options] configure [-h|&#8230;]</code></p>
</dd><dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>&#8211;module </code><i>STRING</i></dt>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</dd>
<dt><code>&#8211;force</code></dt>
<dd> Forces configuration and triggers the restart of relevant services.</dd></dl>
</dl>
<dt><code>is-configured</code></dt>
<dd> Determines if a given module has been configured.</dd>
<dl>
<dt>
</dt><dd>
<p> Usage: <code>vdsm-tool is-configured [-h] [&#8211;module </code><i>STRING</i>]</p>
</dd><dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>&#8211;module </code><i>STRING</i></dt>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</dd></dl>
</dl>
<dt><code>validate-config</code></dt>
<dd> Determines if the current configuration is valid.</dd>
<dl>
<dt>
</dt><dd>
<p> Usage: <code>vdsm-tool validate-config [-h] [&#8211;module </code><i>STRING</i>]</p>
</dd><dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>&#8211;module </code><i>STRING</i></dt>
<dd> Specifies the module on which the action is to be run, such as &#8216;libvirt&#8217; or &#8216;sanlock&#8217;. If no module is specified, the action will be performed on all relevant modules.</dd></dl>
</dl>
</dl>
</dl>
<dt>Options for the <i>dummybr</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>dummybr</code></dt>
<dd> Defines a dummy bridge on a libvirt network.</dd></dl>
</dl>
<dt>Options for the <i>nwfilter</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>nwfilter</code></dt>
<dd> Defines network filters on libvirt.</dd></dl>
</dl>
<dt>Options for the <i>restore_nets</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>restore-nets</code></dt>
<dd> Restores the networks to what was previously persisted via VDSM.</dd></dl>
</dl>
<dt>Options for the <i>restore_nets_init</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>restore-nets-init</code></dt>
<dd> Restore IP+link configuration of persisted networks.</dd></dl>
</dl>
<dt>Options for the <i>service</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>service-disable</code></dt>
<dd> Disables a system service.</dd>
<dt><code>service-is-managed</code></dt>
<dd> Checks whether a given system service exists.</dd>
<dt><code>service-reload</code></dt>
<dd> Notifies a system service to reload its configuration.</dd>
<dt><code>service-restart</code></dt>
<dd> Restarts a system service.</dd>
<dt><code>service-start</code></dt>
<dd> Starts a system service.</dd>
<dt><code>service-status</code></dt>
<dd> Gets the current status of a system service.</dd>
<dt><code>service-stop</code></dt>
<dd> Stops a system service.</dd></dl>
</dl>
<dt>Options for the <i>transient</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>cleanup-transient-repository</code></dt>
<dd> Cleans up the unused transient disks present in the repository. (NOTE: do NOT execute this command when the VDSM daemon is running.)</dd>
<dt><code>setup-transient-repository</code></dt>
<dd> Prepares the transient disks repository.</dd></dl>
</dl>
<dt>Options for the <i>unified_persistence</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>upgrade-unified-persistence</code></dt>
<dd> Upgrades host networking persistence from <code>ifcfg</code> to <code>unified</code> if the persistence model is set as <code>unified</code> in the <i>/usr/lib64/python2.X/site-packages/vdsm/config.py</i> file.</dd>
<dl>
<dt>
</dt><dd>
<p> Usage: <code>vdsm-tool upgrade-unified-persistence [-h] [&#8211;run-again]</code></p>
</dd><dl>
<dt><code>-h, &#8211;help</code></dt>
<dd> Displays a list of options.</dd>
<dt><code>&#8211;run-again</code></dt>
<dd> Runs the upgrade operation again, even if this operation has been performed previously.</dd></dl>
</dl>
</dl>
</dl>
<dt>Options for the <i>validate_ovirt_certs</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>validate-ovirt-certs</code></dt>
<dd> Validates <i>vdsmcert.pem</i> against <i>cacert.pem</i>. If the current <i>cacert.pem</i> is invalid, the command will find a valid certificate file and replace the old <i>cacert.pem</i> with that certificate, and then persist that change.</dd></dl>
</dl>
<dt>Options for the <i>vdsm-id</i> module:</dt>
<dd>
</dd><dl>
<dl>
<dt><code>vdsm-id</code></dt>
<dd> Prints the host UUID.</dd></dl>
</dl>
</dl>
<h2>BUGS</h2>
<p> Report bugs to &lt;<a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a>&gt;</p>
<h2>COPYRIGHT</h2>
<p> Copyright 2011-2014 Red Hat, Inc. License GPLv2: GNU GPL Version 2 &lt;<a rel="nofollow" href="http://gnu.org/licenses/gpl.html">http://gnu.org/licenses/gpl.html</a>&gt;. </p>
