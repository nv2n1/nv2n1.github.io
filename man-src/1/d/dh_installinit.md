---
title: "dh_installinit(1)"
name: "dh_installinit"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dh_installinit/"
description: "dh_installinit – install service init files into package build directories"
---

<h2 class="name">NAME</h2>
<p> dh_installinit &#8211; install service init files into package build directories </p>
<h2>SYNOPSIS</h2>
<p> <code>dh_installinit</code> [<i>debhelper options</i>] [<code>&#8211;name=</code><i>name</i>] [<code>-n</code>] [<code>-R</code>] [<code>-r</code>] [<code>-d</code>] [<code>&#8212;</code> <i>params</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>dh_installinit</code> is a debhelper program that is responsible for installing init scripts with associated defaults files. In compatibility levels up to 11, <code>dh_installinit</code> also handled upstart job files and systemd service files. </p>
<p> It also automatically generates the <i>postinst</i> and <i>postrm</i> and <i>prerm</i> commands needed to set up the symlinks in <i>/etc/rc*.d/</i> to start and stop the init scripts. </p>
<p> In compat 10 or earlier: If a package only ships a systemd service file and no sysvinit script is provided, you may want to exclude the call to dh_installinit for that package (e.g. via <code>-N</code>). Otherwise, you may get warnings from lintian about init.d scripts not being included in the package.</p>
<h2>FILES</h2>
<dl>
<dt>debian/<i>package</i>.init</p>
<dd> If this exists, it is installed into etc/init.d/<i>package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.default</p>
<dd> If this exists, it is installed into etc/default/<i>package</i> in the package build directory.</p>
<dt>debian/<i>package</i>.upstart</p>
<dd> In compatibility level 11, this file will trigger an error with a reminder about ensuring the proper removal of the upstart file in the previous package version. Please consider using the &#8220;rm_conffile&#8221; feature from <i><a href="/docs/linux/man/1-dh_installdeb/">dh_installdeb</a></i>(1) to ensure the proper removal of previous upstart files. </p>
<p> In compatibility level 10, if this file exists, it is installed into etc/init/<i>package</i>.conf in the package build directory.</p>
<dt>debian/<i>package</i>.service</p>
<dd> If this exists, it is installed into lib/systemd/system/<i>package</i>.service in the package build directory. Only used in compat levels 10 and below.</p>
<dt>debian/<i>package</i>.tmpfile</p>
<dd> If this exists, it is installed into usr/lib/tmpfiles.d/<i>package</i>.conf in the package build directory. (The tmpfiles.d mechanism is currently only used by systemd.) Only used in compat levels 10 and below.</dl>
<h2>OPTIONS</h2>
<dl>
<dt><code>-n</code>, <code>&#8211;no-scripts</code></p>
<dd> Do not modify <i>postinst</i>/<i>postrm</i>/<i>prerm</i> scripts.</p>
<dt><code>-o</code>, <code>&#8211;only-scripts</code></p>
<dd> Only modify <i>postinst</i>/<i>postrm</i>/<i>prerm</i> scripts, do not actually install any init script, default files, upstart job or systemd service file. May be useful if the file is shipped and/or installed by upstream in a way that doesn&#8217;t make it easy to let <code>dh_installinit</code> find it. </p>
<p> <code>Caveat</code>: This will bypass all the regular checks and <i>unconditionally</i> modify the scripts. You will almost certainly want to use this with <code>-p</code> to limit, which packages are affected by the call. Example: </p>
<pre>
 override_dh_installinit:
        dh_installinit -pfoo --only-scripts
        dh_installinit --remaining
</pre>
<dt><code>-R</code>, <code>&#8211;restart-after-upgrade</code></p>
<dd> Do not stop the init script until after the package upgrade has been completed. This is the default behaviour in compat 10. </p>
<p> In early compat levels, the default was to stop the script in the <i>prerm</i>, and starts it again in the <i>postinst</i>. </p>
<p> This can be useful for daemons that should not have a possibly long downtime during upgrade. But you should make sure that the daemon will not get confused by the package being upgraded while it&#8217;s running before using this option.</p>
<dt><code>&#8211;no-restart-after-upgrade</code></p>
<dd> Undo a previous <code>&#8211;restart-after-upgrade</code> (or the default of compat 10). If no other options are given, this will cause the service to be stopped in the <i>prerm</i> script and started again in the <i>postinst</i> script.</p>
<dt><code>-r</code>, <code>&#8211;no-stop-on-upgrade</code>, <code>&#8211;no-restart-on-upgrade</code></p>
<dd> Do not stop init script on upgrade. This has the side-effect of not restarting the service as a part of the upgrade. </p>
<p> If you want to restart the service with minimal downtime, please use <code>&#8211;restart-after-upgrade</code> (default in compat 10 or later). If you want the service to be restarted but be stopped during the upgrade, then please use <code>&#8211;no-restart-after-upgrade</code> (note the &#8220;after-upgrade&#8221;). </p>
<p> Note that the <code>&#8211;no-restart-on-upgrade</code> alias is deprecated and will be removed in compat 12. This is to avoid confusion with the <code>&#8211;no-restart-after-upgrade</code> option. The <code>&#8211;no-stop-on-upgrade</code> variant was introduced in debhelper 10.2 (included in Debian stretch).</p>
<dt><code>&#8211;no-start</code></p>
<dd> Do not start the init script on install or upgrade, or stop it on removal. Only call <code>update-rc.d</code>. Useful for rcS scripts.</p>
<dt><code>&#8211;no-enable</code></p>
<dd> Disable the init script on purge, but do not enable them on install. This implies a versioned dependency on <code>init-system-helpers (</code>= 1.51)&gt; as it is the first (functional) version that supports <code>&lt;update-rc.d &lt;script</code> defaults-disabled&gt;&gt;. </p>
<p> <code>Note</code> that this option does not affect whether the services are started. Please remember to also use <code>&#8211;no-start</code> if the service should not be started. </p>
<p> Cannot be combined with <code>-u</code><i>params</i>, <code>&#8211;update-rcd-params=</code><i>params</i>, or <code>&#8212;</code> <i>params</i>.</p>
<dt><code>-d</code>, <code>&#8211;remove-d</code></p>
<dd> Remove trailing <code>d</code> from the name of the package, and use the result for the filename the upstart job file is installed as in <i>etc/init/</i> , and for the filename the init script is installed as in etc/init.d and the default file is installed as in <i>etc/default/</i>. This may be useful for daemons with names ending in <code>d</code>. (Note: this takes precedence over the <code>&#8211;init-script</code> parameter described below.)</p>
<dt><code>-u</code><i>params</i> <code>&#8211;update-rcd-params=</code><i>params</i></p>
<dd>
<dt><code>&#8212;</code> <i>params</i></p>
<dd> Pass <i>params</i> to <i><a href="/docs/linux/man/8-update-rc-d/">update-rc.d</a></i>(8). If not specified, <code>defaults</code> (or <code>defaults-disabled</code> with <code>&#8211;no-enable</code>) will be passed to <i><a href="/docs/linux/man/8-update-rc-d/">update-rc.d</a></i>(8). </p>
<p> Cannot be combined with <code>&#8211;no-enable</code>.</p>
<dt><code>&#8211;name=</code><i>name</i></p>
<dd> Install the init script (and default file) as well as upstart job file using the filename <i>name</i> instead of the default filename, which is the package name. When this parameter is used, <code>dh_installinit</code> looks for and installs files named <i>debian/package.name.init</i>, <i>debian/package.name.default</i> and <i>debian/package.name.upstart</i> instead of the usual <i>debian/package.init</i>, <i>debian/package.default</i> and <i>debian/package.upstart</i>.</p>
<dt><code>&#8211;init-script=</code><i>scriptname</i></p>
<dd> Use <i>scriptname</i> as the filename the init script is installed as in <i>etc/init.d/</i> (and also use it as the filename for the defaults file, if it is installed). If you use this parameter, <code>dh_installinit</code> will look to see if a file in the <i>debian/</i> directory exists that looks like <i>package.scriptname</i> and if so will install it as the init script in preference to the files it normally installs. </p>
<p> This parameter is deprecated, use the <code>&#8211;name</code> parameter instead. This parameter is incompatible with the use of upstart jobs.</p>
<dt><code>&#8211;error-handler=</code><i>function</i></p>
<dd> Call the named shell <i>function</i> if running the init script fails. The function should be provided in the <i>prerm</i> and <i>postinst</i> scripts, before the <code>#DEBHELPER#</code> token.</dl>
<h2>NOTES</h2>
<p> Note that this command is not idempotent. <i><a href="/docs/linux/man/1-dh_prep/">dh_prep</a></i>(1) should be called between invocations of this command. Otherwise, it may cause multiple instances of the same text to be added to maintainer scripts.</p>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/7-debhelper/">debhelper</a></i>(7) </p>
<p> This program is a part of debhelper.</p>
<h2>AUTHORS</h2>
<p> Joey Hess &lt;joeyh [at] debian.org&gt; </p>
<p> Steve Langasek &lt;steve.langasek [at] canonical.com&gt; </p>
<p> Michael Stapelberg &lt;stapelberg [at] debian.org&gt; </p>
<h2>Index</h2>
