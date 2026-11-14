---
title: "pki-server-upgrade(8)"
name: "pki-server-upgrade"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-server-upgrade/"
description: "pki-server-upgrade – Tool for upgrading Certificate System server configuration."
---

<p>pki-server-upgrade &#8211; Tool for upgrading Certificate System server configuration.</p>
<h2>Synopsis</h2>
<p><code>pki-server-upgrade</code> [OPTIONS] </p>
<h2>Description</h2>
<p>There are two parts to upgrading Certificate System: upgrading the system configuration files used by both the client and the server processes and upgrading the server configuration files. When upgrading Certificate System, the existing server configuration files (e.g. <code>server.xml</code>, <code>web.xml</code>) may need to be upgraded because the content may have changed from one version to another. The configuration upgrade is executed automatically during RPM upgrade. However, in case there is a problem, the process can also be run manually using <code>pki-server-upgrade</code>. The server upgrade process is done incrementally using upgrade scriptlets. A server consists of the server instance itself and the subsystems running in that instance. The upgrade process executes one scriptlet at a time, running through each component (server instance and subsystem) in parallel and completing before executing the next scriptlet. If one component encounters an error, that component is skipped in the subsequent upgrade scriptlets. The upgrade process and scriptlet execution for each component is monitored in upgrade trackers. A counter shows the latest index number for the most recently executed scriptlet; when all scriptlets have run, the component tracker shows the updated version number. The scriptlets are stored in the upgrade directory:</p>
<dl>
<dd>/usr/share/pki/server/upgrade/&lt;version&gt;/&lt;index&gt;-&lt;name&gt;</dl>
<p> The <code>version</code> is the server version to be upgraded. The <code>index</code> is the script execution order. The <code>name</code> is the scriptlet name. During upgrade, the scriptlets will back up all changes to the file system into the following folder:</p>
<dl>
<dd>/var/log/pki/server/upgrade/&lt;version&gt;/&lt;index&gt;</dl>
<p> The <code>version</code> and <code>index</code> values indicate the scriptlet being executed. A copy of the files and folders that are being modified or removed will be stored in <code>oldfiles</code>. The names of the newly-added files and folders will be stored in <code>newfiles</code>. The instance upgrade process is tracked using this file:</p>
<dl>
<dd>/var/lib/pki/&lt;instance&gt;/conf/tomcat.conf</dl>
<p> The subsystem upgrade process is tracked using this file:</p>
<dl>
<dd>/var/lib/pki/&lt;instance&gt;/&lt;subsystem&gt;/conf/CS.cfg</dl>
<p> The file stores the current configuration version and the last successful scriptlet index. </p>
<h2>Options</h2>
<h3>General options</h3>
<dl>
<dt><code>&#8211;silent</code></p>
<dd>Upgrade in silent mode.</p>
<dt><code>&#8211;status</code></p>
<dd>Show upgrade status only <code>without</code> performing the upgrade.</p>
<dt><code>&#8211;revert</code></p>
<dd>Revert the last version.</p>
<dt><code>-i, &#8211;instance &lt;instance&gt;</code></p>
<dd>Upgrade a specific instance only.</p>
<dt><code>-s, &#8211;subsystem &lt;subsystem&gt;</code></p>
<dd>Upgrade a specific subsystem in an instance only.</p>
<dt><code>-t, &#8211;instance-type &lt;type&gt;</code></p>
<dd>Upgrade a specific instance type, by the major version number of the Dogtag instance. For example, use 9 for Dogtag 9 instances and 10 for Dogtag 10.</p>
<dt><code>-X</code></p>
<dd>Show advanced options.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd>Run in verbose mode.</p>
<dt><code>-h, &#8211;help</code></p>
<dd>Show this help message. </p>
</dl>
<h3>Advanced options</h3>
<p>The advanced options circumvent the normal component tracking process by changing the scriptlet order or changing the tracker information. </p>
<p> <code>WARNING:</code> These options may render the system unusable. </p>
<dl>
<dt><code>&#8211;scriptlet-version &lt;version&gt;</code></p>
<dd>Run scriptlets for a specific version only.</p>
<dt><code>&#8211;scriptlet-index &lt;index&gt;</code></p>
<dd>Run a specific scriptlet only.</p>
<dt><code>&#8211;remove-tracker</code></p>
<dd>Remove the tracker.</p>
<dt><code>&#8211;reset-tracker</code></p>
<dd>Reset the tracker to match the package version.</p>
<dt><code>&#8211;set-tracker &lt;version&gt;</code></p>
<dd>Set the tracker to a specific version. </p>
</dl>
<h2>Operations</h2>
<h3>Interactive mode</h3>
<p>By default, <code>pki-server-upgrade</code> will run interactively to upgrade all server instances and subsystems on the machine. It will ask for a confirmation before executing each scriptlet. </p>
<p> <code>% pki-server-upgrade</code> </p>
<p> If there is an error, it will stop and show the error.</p>
<h3>Silent mode</h3>
<p>The upgrade process can also be done silently without user interaction: </p>
<p> <code>% pki-server-upgrade &#8211;silent</code> </p>
<p> If there is an error, the upgrade process will stop for that particular instance/subsystem. Other instances/subsystems will continue to be upgraded.</p>
<h3>Checking upgrade status</h3>
<p>It is possible to check the status of a running upgrade process. </p>
<p> <code>% pki-server-upgrade &#8211;status</code></p>
<h3>Troubleshooting</h3>
<p>Check the scriptlet to see which operations are being executed. Once the error is identified and corrected, the upgrade can be resumed by re-running <code>pki-server-upgrade</code>. </p>
<p> If necessary, the upgrade can be run in verbose mode: </p>
<p> <code>% pki-server-upgrade &#8211;verbose</code> </p>
<p> It is possible to rerun a failed script by itself, specifying the instance and subsystem, version, and scriptlet index: </p>
<p> <code>% pki-server-upgrade &#8211;instance pki-tomcat &#8211;subsystem ca &#8211;scriptlet-version 10.0.1 &#8211;scriptlet-index 1</code></p>
<h3>Reverting an upgrade</h3>
<p>If necessary, the upgrade can be reverted: </p>
<p> <code>% pki-server-upgrade &#8211;revert</code> </p>
<p> Files and folders that were created by the scriptlet will be removed. Files and folders that were modified or removed by the scriptlet will be restored.</p>
<h2>Files</h2>
<p><i>/usr/sbin/pki-server-upgrade</i></p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;, Ella Deon Lackey &lt;dlackey [at] redhat.com&gt;, and Endi Dewata &lt;edewata [at] redhat.com&gt;. <code>pki-server-upgrade</code> was written by the Dogtag project.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2013 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
