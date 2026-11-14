---
title: "redhat-upgrade-tool(8)"
name: "redhat-upgrade-tool"
section: "8"
letter: "r"
url: "/docs/linux/man/8-redhat-upgrade-tool/"
description: "redhat-upgrade-tool – Red Hat Upgrade tool"
---

<p>redhat-upgrade-tool &#8211; Red Hat Upgrade tool</p>
<h2>Synopsis</h2>
<p>redhat-upgrade-tool [<i>OPTIONS</i>] <code>SOURCE</code></p>
<h2>Description</h2>
<p><code>redhat-upgrade-tool</code> is the Red Hat Upgrade tool. </p>
<p> The <code>redhat-upgrade-tool</code> client runs on the system to be upgraded. It determines what packages are needed for upgrade and gathers them from the source(s) given. It also fetches and sets up the boot images needed to run the upgrade and sets up the system to perform the upgrade at next boot. </p>
<p> The actual upgrade takes place when the system is rebooted, using the boot images set up by <code>redhat-upgrade-tool</code>. The upgrade initrd starts the existing system (mostly) as normal, lets it mount all the local filesystems, then starts the upgrade. </p>
<p> When the upgrade finishes, it reboots the system into the newly-upgraded OS.</p>
<h2>Options</h2>
<h3>Optional arguments</h3>
<p><code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Show a help message and exit.</dl>
<p> <code>-v</code>, <code>&#8211;verbose</code></p>
<dl>
<dd>Print more info.</dl>
<p> <code>-d</code>, <code>&#8211;debug</code></p>
<dl>
<dd>Print lots of debugging info.</dl>
<p> <code>&#8211;debuglog</code> <i>DEBUGLOG</i></p>
<dl>
<dd>Write debugging output to the given file. Defaults to <i>/var/log/redhat-upgrade-tool.log</i>.</dl>
<p> <code>&#8211;reboot</code></p>
<dl>
<dd>Automatically reboot to start the upgrade when ready.</dl>
<h3>Source</h3>
<p>These options tell <code>redhat-upgrade-tool</code> where to look for the packages and boot images needed to run the upgrade. At least one of these options is required. </p>
<p> <code>&#8211;device</code> [<i>DEV</i>]</p>
<dl>
<dd>Device or mountpoint of mounted install media. If <i>DEV</i> is omitted, <code>redhat-upgrade-tool</code> will scan all currently-mounted removable devices (USB disks, optical media, etc.)</dl>
<p> <code>&#8211;iso</code> <i>ISO</i></p>
<dl>
<dd>Installation image file.</dl>
<p> <code>&#8211;network</code> <i>VERSION</i></p>
<dl>
<dd>Online repos matching <i>VERSION</i> (a number or &quot;rawhide&quot;)</dl>
<p> Multiple sources may be used, if desired.</p>
<h3>Additional options for &#8211;network</h3>
<p><code>&#8211;enablerepo</code> <i>REPOID</i></p>
<dl>
<dd>Enable one or more repos (wildcards allowed).</dl>
<p> <code>&#8211;disablerepo</code> <i>REPOID</i></p>
<dl>
<dd>Disable one or more repos (wildcards allowed).</dl>
<p> <code>&#8211;addrepo</code> <i>REPOID=[@]URL</i></p>
<dl>
<dd>Add the repo at <i>URL</i>. Prefix URL with <i>@</i> to indicate that the URL is a mirrorlist.</dl>
<p> <code>&#8211;instrepo</code> <i>REPOID</i></p>
<dl>
<dd>Get upgrader boot images from the repo named <i>REPOID</i>. The repo must contain a valid <i>.treeinfo</i> file which points to the location of usable <i>kernel</i> and <i>upgrade</i> images.</dl>
<h3>Cleanup commands</h3>
<p><code>&#8211;resetbootloader</code></p>
<dl>
<dd>Remove any modifications made to bootloader configuration.</dl>
<p> <code>&#8211;clean</code></p>
<dl>
<dd>Clean up everything written by <code>redhat-upgrade-tool</code>.</dl>
<h2>Examples</h2>
<p><code>redhat-upgrade-tool &#8211;network 7.0 &#8211;instrepo &lt;repo URL&gt;</code> </p>
<p> Upgrade to RHEL 7.0 by downloading all needed packages and data from the specified repository. </p>
<p> <code>redhat-upgrade-tool &#8211;device &#8211;network 7.0</code> </p>
<p> Upgrade to RHEL 7.0 using install media mounted somewhere on the system, fetching updates from the network if needed.</p>
<h2>Exit Status</h2>
<p>0</p>
<dl>
<dd>Success.</dl>
<p> 1</p>
<dl>
<dd>Cancelled by user, failure writing files to disk, or other unknown error</dl>
<p> 2</p>
<dl>
<dd>Failed to download/copy files from the given <i>SOURCE</i></dl>
<p> 3</p>
<dl>
<dd>RPM upgrade transaction test failed</dl>
<h2>Bugs</h2>
<p>The <code>&#8211;iso</code> image must be on a filesystem listed in <i>/etc/fstab</i>.</p>
<h2>Authors</h2>
<p>Will Woods &lt;wwoods [at] redhat.com&gt;</p>
