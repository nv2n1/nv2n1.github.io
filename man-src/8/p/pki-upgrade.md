---
title: "pki-upgrade(8)"
name: "pki-upgrade"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pki-upgrade/"
description: "pki-upgrade – Tool for upgrading system-wide configuration for Certificate System."
---

<p>pki-upgrade &#8211; Tool for upgrading system-wide configuration for Certificate System.</p>
<h2>Synopsis</h2>
<p><code>pki-upgrade</code> [OPTIONS] </p>
<h2>Description</h2>
<p>There are two parts to upgrading Certificate System: upgrading the system configuration files used by both the client and the server processes and upgrading the server configuration files. When upgrading Certificate System, the existing system configuration files (e.g. <code>/etc/pki/pki.conf</code>) may need to be upgraded because the content may have changed from one version to another. The configuration upgrade is executed automatically during RPM upgrade. However, in case there is a problem, the process can also be run manually using <code>pki-upgrade</code>. The system upgrade process is done incrementally using upgrade scriptlets. The upgrade process and scriptlet execution is monitored in upgrade trackers. A counter shows the latest index number for the most recently executed scriptlet; when all scriptlets have run, the component tracker shows the updated version number. The scriptlets are stored in the upgrade directory:</p>
<dl>
<dd>/usr/share/pki/upgrade/&lt;version&gt;/&lt;index&gt;-&lt;name&gt;</dl>
<p> The <code>version</code> is the system version to be upgraded. The <code>index</code> is the script execution order. The <code>name</code> is the scriptlet name. During upgrade, the scriptlets will back up all changes to the filesystem into the following folder:</p>
<dl>
<dd>/var/log/pki/upgrade/&lt;version&gt;/&lt;index&gt;</dl>
<p> The <code>version</code> and <code>index</code> values indicate the scriptlet being executed. A copy of the files and folders that are being modified or removed will be stored in <code>oldfiles</code>. The names of the newly-added files and folders will be stored in <code>newfiles</code>. The system upgrade process is tracked using this file:</p>
<dl>
<dd>/etc/pki/pki.version</dl>
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
<p>By default, <code>pki-upgrade</code> will run interactively. It will ask for a confirmation before executing each scriptlet. </p>
<p> <code>% pki-upgrade</code> </p>
<p> If there is an error, it will stop and show the error.</p>
<h3>Silent mode</h3>
<p>The upgrade process can also be done silently without user interaction: </p>
<p> <code>% pki-upgrade &#8211;silent</code> </p>
<p> If there is an error, it will stop and show the error.</p>
<h3>Checking upgrade status</h3>
<p>It is possible to check the status of a running upgrade process. </p>
<p> <code>% pki-upgrade &#8211;status</code></p>
<h3>Troubleshooting</h3>
<p>If there is an error, rerun the upgrade in verbose mode: </p>
<p> <code>% pki-upgrade &#8211;verbose</code> </p>
<p> Check the scriptlet to see which operations are being executed. Once the error is identified and corrected, the upgrade can be resumed by re-running <code>pki-upgrade</code>. </p>
<p> It is possible to rerun a failed script by itself, specifying the instance and subsystem, version, and scriptlet index: </p>
<p> <code>% pki-upgrade &#8211;scriptlet-version 10.0.1 &#8211;scriptlet-index 1</code></p>
<h3>Reverting an upgrade</h3>
<p>If necessary, the upgrade can be reverted: </p>
<p> <code>% pki-upgrade &#8211;revert</code> </p>
<p> Files and folders that were created by the scriptlet will be removed. Files and folders that were modified or removed by the scriptlet will be restored.</p>
<h2>Files</h2>
<p><i>/usr/sbin/pki-upgrade</i></p>
<h2>Authors</h2>
<p>Ade Lee &lt;alee [at] redhat.com&gt;, Ella Deon Lackey &lt;dlackey [at] redhat.com&gt;, and Endi Dewata &lt;edewata [at] redhat.com&gt;. <code>pki-upgrade</code> was written by the Dogtag project.</p>
<h2>Copyright</h2>
<p>Copyright (c) 2013 Red Hat, Inc. This is licensed under the GNU General Public License, version 2 (GPLv2). A copy of this license is available at <a rel="nofollow" href="http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.">http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt.</a></p>
