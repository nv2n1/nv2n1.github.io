---
title: "auter(1)"
name: "auter"
section: "1"
letter: "a"
url: "/docs/linux/man/1-auter/"
description: "auter – manual page for auter 0.8"
---

<h2>NAME</h2>
<p> auter &#8211; manual page for auter 0.8</p>
<h2>SYNOPSIS</h2>
<p> <code>auter</code> [<i>&#8211;enable|&#8211;disable|&#8211;status</i>] [<i>&#8211;prep</i>] [<i>&#8211;apply</i>] [<i>&#8211;reboot</i>] [<i>&#8211;postreboot</i>] [<i>&#8211;config=&lt;configfile&gt;</i>] [<i>OPTION</i>]</p>
<h2>DESCRIPTION</h2>
<h3>Actions:</h3>
<dl>
<dt><code>&#8211;enable</code></p>
<dd> Enable auter</p>
<dt><code>&#8211;disable</code></p>
<dd> Disable auter</p>
<dt><code>&#8211;status</code></p>
<dd> Show whether enabled or disabled</p>
<dt><code>&#8211;prep</code></p>
<dd> Pre-download updates before applying</p>
<dt><code>&#8211;apply</code></p>
<dd> Apply updates, and reboot if AUTOREBOOT=yes</p>
<dt><code>&#8211;reboot</code></p>
<dd> Reboot system</p>
<dt><code>&#8211;postreboot</code></p>
<dd> Run post reboot script</dl>
<h2>OPTIONS</h2>
<dl>
<dt> <code>&#8211;config</code>=<i>FILE</i> Specify the full path to an auter config file. Defaults to <i>/etc/auter/auter.conf</i></p>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd>
<dd>Show this help text</p>
<dt> <code>-v</code>, <code>&#8211;version</code> Show the version</dl>
<h2>FILES</h2>
<p> //etc/auter/auter.conf<br />
&nbsp;<wbr>&nbsp;<wbr>Default config file location. Use the &#8211;config option to pass an alternative config file to use within&nbsp;<wbr>/etc/auter. </p>
<p> //usr/bin/auter<br />
&nbsp;<wbr>&nbsp;<wbr>The main auter script, which gets called to prepare and apply updates. </p>
<p> //var/lib/auter/enabled<br />
&nbsp;<wbr>&nbsp;<wbr>The lock file to determine if auter is enabled. If this file doesn&#8217;t exist, auter is disabled. </p>
<p> //etc/cron.d/auter<br />
&nbsp;<wbr>&nbsp;<wbr>The cron file defining the default schedule for auter. Commented out by default. </p>
<p> //etc/cron.d/auter-postreboot-CONFIGSET<br />
&nbsp;<wbr>&nbsp;<wbr>On reboot, auter will add a call to auter &#8211;postreboot via an&nbsp;<wbr>@reboot cron job. The CONFIGSET part of the filename is defined in the auter config file by setting a variable of the same name, and if not defined is set to&nbsp;<wbr>&quot;default&quot;. </p>
<p> //var/lib/auter/last-prep-CONFIGSET<br />
&nbsp;<wbr>&nbsp;<wbr>These files contain the list of packages to be updated according to the last time &#8211;prep was run. There may be multiple logs if different config files are used. This file will not be updated/created if there are no new updates to be applied. The CONFIGSET part of the filename is defined in the auter config file by setting a variable of the same name, and if not defined is set to&nbsp;<wbr>&quot;default&quot;. </p>
<p> //var/lib/auter/last-update-CONFIGSET<br />
&nbsp;<wbr>&nbsp;<wbr>This file contains the updates that were last applied by auter. The CONFIGSET part of the filename is defined in the auter config file by setting a variable of the same name, and if not defined is set to&nbsp;<wbr>&quot;default&quot;. </p>
<p> //etc/auter/pre-apply.d/ //etc/auter/post-apply.d/ //etc/auter/pre-reboot.d/ //etc/auter/post-reboot.d/<br />
&nbsp;<wbr>&nbsp;<wbr>Directories containing scripts to run before/after updates are applied, and before/after the server is rebooted&nbsp;<wbr>(if applicable). Default locations are above, but also customizable in the config file. If any scripts in the pre/post hook directories are not executable a warning will be logged with the filename but auter will continue. If any scripts in the pre-post hook directories exit with a non-zero exit code an error will be logged with the filename and exit code, and auter will abort. Post reboot, there is a delay of 5 mins before the post-reboot script is run to allow the system to become fully ready. </p>
<p> //var/cache/auter/<br />
&nbsp;<wbr>&nbsp;<wbr>Will be created during the during install but is also checked&nbsp;<wbr>(and created if it does not exist)&nbsp;<wbr>during the prep stage if ONLYINSTALLFROMPREP is set to&nbsp;<wbr>&#8216;yes&#8217;. A configset sub-directory will be created which will hold the updates that were downloaded from the most recent &#8211;prep execution. Any existing rpm files will be deleted as part of the following &#8211;prep execution. The directories for each profile must have owner and group set to root and must NOT be writable by other.</p>
<h2>ENABLE/DISABLE</h2>
<dd>To provide an easy way to switch on/off all auter jobs, use auter &#8211;enable or auter &#8211;disable to set the lockfile /var/lib/auter/enabled. Auter will check for the presence of this file before running.</p>
<h2>REBOOTING</h2>
<p> Rebooting is an essential part of applying updates, in order to ensure the updated packages are in use. An update to the kernel will always need a reboot. Some application updates, for example Apache, will restart the service. However often libraries are updated, such as openssl, which don&#8217;t force a reboot of services that use them. Rebooting guarantees that every update is in use by running services. You can either enable AUTOREBOOT=yes in the config file (the default is AUTOREBOOT=no), to reboot after &#8211;apply, or you can schedule a seperate schedule for &#8211;reboot via a second cronjob. A 2 minute warning is emitted before the server is rebooted, and this can be cancelled by a superuser with shutdown -c.</p>
<h2>CONFIG FILE OPTIONS</h2>
<p> Config options are set in /etc/auter/auter.conf, or in the file referenced by the &#8211;config option. </p>
<p>&nbsp;<wbr>CONFIGSET<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;default&quot;<br />
&nbsp;<wbr>Required: yes<br />
&nbsp;<wbr>Defines a name which auter will use to uniquely identify logs and postreboot hooks. This value must be unique amongst configs on a system, and is required when using a custom configuration file. </p>
<p>&nbsp;<wbr>AUTOREBOOT<br />
&nbsp;<wbr>Valid options:&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;no&quot;<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;no&quot;<br />
&nbsp;<wbr>If set to&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>the server will be rebooted 2 minutes after applying updates </p>
<p>&nbsp;<wbr>PACKAGEMANAGEROPTIONS<br />
&nbsp;<wbr>Valid options: Any valid yum or dnf options can be specified&nbsp;<wbr>(including dashes). This is passed directly to the package manager.<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;&quot;<br />
&nbsp;<wbr>See man pages for yum, or dnf as appropriate for more info. Example:&nbsp;<wbr>&quot;&#8211;disableexcludes=all&quot; </p>
<p>&nbsp;<wbr>PREDOWNLOADUPDATES<br />
&nbsp;<wbr>Valid options:&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;no&quot;<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;yes&quot;<br />
&nbsp;<wbr>This will only work if &#8211;downloadonly option is available in the package manager. </p>
<p>&nbsp;<wbr>ONLYINSTALLFROMPREP<br />
&nbsp;<wbr>Valid options:&nbsp;<wbr>&quot;yes&quot;&nbsp;<wbr>or&nbsp;<wbr>&quot;no&quot;<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;no&quot;<br />
&nbsp;<wbr>This will only work if PREDOWNLOADUPDATES is set to&nbsp;<wbr>&#8216;yes&#8217;&nbsp;<wbr>in the config file. This will only install the updates that were downloaded the last time auter &#8211;prep was called. This does work with multiple configsets. The latest updates will be saved in&nbsp;<wbr>/var/cache/auter/$CONFIGSET </p>
<p>&nbsp;<wbr>MAXDELAY<br />
&nbsp;<wbr>Valid options: Any positive number above 0<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;3600&quot;<br />
&nbsp;<wbr>This is the upper limit in seconds of a random time to wait before querying repositories. </p>
<p>&nbsp;<wbr>PREAPPLYSCRIPTDIR<br />
&nbsp;<wbr>Valid options: path to directory containing scripts<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;/etc/auter/pre-apply.d&quot;<br />
&nbsp;<wbr>Custom scripts to be run before applying updates </p>
<p>&nbsp;<wbr>POSTAPPLYSCRIPTDIR<br />
&nbsp;<wbr>Valid options: path to directory containing scripts<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;/etc/auter/post-apply.d&quot;<br />
&nbsp;<wbr>Custom scripts to be run after applying updates </p>
<p>&nbsp;<wbr>PREREBOOTSCRIPTDIR<br />
&nbsp;<wbr>Valid options: path to directory containing scripts<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;/etc/auter/pre-reboot.d&quot;<br />
&nbsp;<wbr>Custom scripts to be run before rebooting. These will only run if AUTOREBOOT=&quot;yes&quot;&nbsp;<wbr>or auter is run with the &#8211;reboot option </p>
<p>&nbsp;<wbr>POSTREBOOTSCRIPTDIR<br />
&nbsp;<wbr>Valid options: path to directory containing scripts<br />
&nbsp;<wbr>Default:&nbsp;<wbr>&quot;/etc/auter/post-reboot.d&quot;<br />
&nbsp;<wbr>Custom scripts to be run after rebooting. These will only run if AUTOREBOOT=&quot;yes&quot;&nbsp;<wbr>or auter is run with the &#8211;reboot option</p>
<h2>EXIT CODES</h2>
<p> 0 = updates successful / no updates available </p>
<p> 3 = issue related to yum / dnf command </p>
<p> 4 = auter disabled via lockfile </p>
<p> 5 = script not run as root / DATADIR does not exist / config file does not exist </p>
<p> 6 = auter is already running / PIDFILE exists </p>
<p> 7 = neither yum nor dnf is available </p>
<p> 8 = a pre/post hook exited with a non-zero error code </p>
<h2>Index</h2>
