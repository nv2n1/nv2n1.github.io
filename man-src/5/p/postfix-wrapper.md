---
title: "postfix-wrapper(5)"
name: "postfix-wrapper"
section: "5"
letter: "p"
url: "/docs/linux/man/5-postfix-wrapper/"
description: "postfix-wrapper – Postfix multi-instance API"
---

<p>postfix-wrapper &#8211; Postfix multi-instance API</p>
<h2>Description</h2>
<p>Support for managing multiple Postfix instances is available as of version 2.6. Instances share executable files and documentation, but have their own directories for configuration, queue and data files. </p>
<p> This document describes how the familiar &quot;postfix start&quot; etc. user interface can be used to manage one or multiple Postfix instances, and gives details of an API to coordinate activities between the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command and a multi-instance manager program. </p>
<p> With multi-instance support, the default Postfix instance is always required. This instance is identified by the config_directory parameter&#8217;s default value.</p>
<h2>General Operation</h2>
<p>Multi-instance support is backwards compatible: when you run only one Postfix instance, commands such as &quot;postfix start&quot; will not change behavior at all. </p>
<p> Even with multiple Postfix instances, you can keep using the same postfix commands in boot scripts, upgrade procedures, and other places. The commands do more work, but humans are not forced to learn new tricks. </p>
<p> For example, to start all Postfix instances, use:</p>
<dl>
<dd># postfix start</dl>
<p> Other <a href="/docs/linux/man/1-postfix/">postfix</a>(1) commands also work as expected. For example, to find out what Postfix instances exist in a multi-instance configuration, use:</p>
<dl>
<dd># postfix status</dl>
<p> This enumerates the status of all Postfix instances within a multi-instance configuration.</p>
<h2>Managing An Individual Postfix Instance</h2>
<p>To manage a specific Postfix instance, specify its configuration directory on the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command line:</p>
<dl>
<dd># postfix -c <i>/path/to/config_directory command</i></dl>
<p> Alternatively, the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command accepts the instance&#8217;s configuration directory via the MAIL_CONFIG environment variable (the -c command-line option has higher precedence). </p>
<p> Otherwise, the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command will operate on all Postfix instances.</p>
<h2>ENABLING <a href="/docs/linux/man/1-postfix/">POSTFIX</a>(1) MULTI-INSTANCE MODE</h2>
<p>By default, the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command operates in single-instance mode. In this mode the command invokes the postfix-script file directly (currently installed in the daemon directory). This file contains the commands that start or stop one Postfix instance, that upgrade the configuration of one Postfix instance, and so on. </p>
<p> When the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command operates in multi-instance mode as discussed below, the command needs to execute start, stop, etc. commands for each Postfix instance. This multiplication of commands is handled by a multi-instance manager program. </p>
<p> Turning on <a href="/docs/linux/man/1-postfix/">postfix</a>(1) multi-instance mode goes as follows: in the default Postfix instance&#8217;s main.cf file, 1) specify the pathname of a multi-instance manager program with the multi_instance_wrapper parameter; 2) populate the multi_instance_directories parameter with the configuration directory pathnames of additional Postfix instances. For example:</p>
<dl>
<dd>
<pre>/etc/postfix/main.cf:
 multi_instance_wrapper = $daemon_directory/postfix-wrapper
 multi_instance_directories = /etc/postfix-test</pre>
</dl>
<p> The $daemon_directory/postfix-wrapper file implements a simple manager and contains instructions for creating Postfix instances by hand. The <a href="/docs/linux/man/1-postmulti/">postmulti</a>(1) command provides a more extensive implementation including support for life-cycle management. </p>
<p> The multi_instance_directories and other main.cf parameters are listed below in the CONFIGURATION PARAMETERS section. </p>
<p> In multi-instance mode, the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command invokes the $multi_instance_wrapper command instead of the postfix-script file. This multi-instance manager in turn executes the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command in single-instance mode for each Postfix instance. </p>
<p> To illustrate the main ideas behind multi-instance operation, below is an example of a simple but useful multi-instance manager implementation:</p>
<dl>
<dd>
<pre>#!/bin/sh
: ${command_directory?&quot;do not invoke this command directly&quot;}
POSTCONF=$command_directory/postconf
POSTFIX=$command_directory/postfix
instance_dirs=`$POSTCONF -h multi_instance_directories |
 sed 's/,/ /'` || exit 1
err=0
for dir in $config_directory $instance_dirs
do
 case &quot;$1&quot; in
 stop|abort|flush|reload|drain)
 test &quot;`$POSTCONF -c $dir -h multi_instance_enable`&quot; \
 = yes || continue;;
 start)
 test &quot;`$POSTCONF -c $dir -h multi_instance_enable`&quot; \
 = yes || {
 $POSTFIX -c $dir check || err=$?
 continue
 };;
 esac
 $POSTFIX -c $dir &quot;$@&quot; || err=$?
done
exit $err</pre>
</dl>
<h2>Per-Instance Multi-Instance Manager Controls</h2>
<p>Each Postfix instance has its own main.cf file with parameters that control how the multi-instance manager operates on that instance. This section discusses the most important settings. </p>
<p> The setting &quot;multi_instance_enable = yes&quot; allows the multi-instance manager to start (stop, etc.) the corresponding Postfix instance. For safety reasons, this setting is not the default. </p>
<p> The default setting &quot;multi_instance_enable = no&quot; is useful for manual testing with &quot;postfix -c <i>/path/name</i> start&quot; etc. The multi-instance manager will not start such an instance, and it will skip commands such as &quot;stop&quot; or &quot;flush&quot; that require a running Postfix instance. The multi-instance manager will execute commands such as &quot;check&quot;, &quot;set-permissions&quot; or &quot;upgrade-configuration&quot;, and it will replace &quot;start&quot; by &quot;check&quot; so that problems will be reported even when the instance is disabled.</p>
<h2>Maintaining Shared And Non-Shared Files</h2>
<p>Some files are shared between Postfix instances, such as executables and manpages, and some files are per-instance, such as configuration files, mail queue files, and data files. See the NON-SHARED FILES section below for a list of per-instance files. </p>
<p> Before Postfix multi-instance support was implemented, the executables, manpages, etc., have always been maintained as part of the default Postfix instance. </p>
<p> With multi-instance support, we simply continue to do this. Specifically, a Postfix instance will not check or update shared files when that instance&#8217;s config_directory value is listed with the default main.cf file&#8217;s multi_instance_directories parameter. </p>
<p> The consequence of this approach is that the default Postfix instance should be checked and updated before any other instances.</p>
<h2>Multi-Instance Api Summary</h2>
<p>Only the multi-instance manager implements support for the multi_instance_enable configuration parameter. The multi-instance manager will start only Postfix instances whose main.cf file has &quot;multi_instance_enable = yes&quot;. A setting of &quot;no&quot; allows a Postfix instance to be tested by hand. </p>
<p> The <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command operates on only one Postfix instance when the -c option is specified, or when MAIL_CONFIG is present in the process environment. This is necessary to terminate recursion. </p>
<p> Otherwise, when the multi_instance_directories parameter value is non-empty, the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command executes the command specified with the multi_instance_wrapper parameter, instead of executing the commands in postfix-script. </p>
<p> The multi-instance manager skips commands such as &quot;stop&quot; or &quot;reload&quot; that require a running Postfix instance, when an instance does not have &quot;multi_instance_enable = yes&quot;. This avoids false error messages. </p>
<p> The multi-instance manager replaces a &quot;start&quot; command by &quot;check&quot; when a Postfix instance&#8217;s main.cf file does not have &quot;multi_instance_enable = yes&quot;. This substitution ensures that problems will be reported even when the instance is disabled. </p>
<p> No Postfix command or script will update or check shared files when its config_directory value is listed in the default main.cf&#8217;s multi_instance_directories parameter value. Therefore, the default instance should be checked and updated before any Postfix instances that depend on it. </p>
<p> Set-gid commands such as <a href="/docs/linux/man/1-postdrop/">postdrop</a>(1) and <a href="/docs/linux/man/1-postqueue/">postqueue</a>(1) effectively append the multi_instance_directories parameter value to the legacy alternate_config_directories parameter value. The commands use this information to determine whether a -c option or MAIL_CONFIG environment setting specifies a legitimate value. </p>
<p> The legacy alternate_config_directories parameter remains necessary for non-default Postfix instances that are running different versions of Postfix, or that are not managed together with the default Postfix instance.</p>
<h2>Environment Variables</h2>
<dl>
<dt>MAIL_CONFIG</p>
<dd>When present, this forces the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) command to operate only on the specified Postfix instance. This environment variable is exported by the <a href="/docs/linux/man/1-postfix/">postfix</a>(1) -c option, so that <a href="/docs/linux/man/1-postfix/">postfix</a>(1) commands in descendant processes will work correctly.</dl>
<h2>Configuration Parameters</h2>
<p>The text below provides only a parameter summary. See <a href="/docs/linux/man/5-postconf/">postconf</a>(5) for more details.</p>
<dl>
<dt><code>multi_instance_directories (empty)</code></p>
<dd>An optional list of non-default Postfix configuration directories; these directories belong to additional Postfix instances that share the Postfix executable files and documentation with the default Postfix instance, and that are started, stopped, etc., together with the default Postfix instance.</p>
<dt><code>multi_instance_wrapper (empty)</code></p>
<dd>The pathname of a multi-instance manager command that the <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) command invokes when the multi_instance_directories parameter value is non-empty.</p>
<dt><code>multi_instance_name (empty)</code></p>
<dd>The optional instance name of this Postfix instance.</p>
<dt><code>multi_instance_group (empty)</code></p>
<dd>The optional instance group name of this Postfix instance.</p>
<dt><code>multi_instance_enable (no)</code></p>
<dd>Allow this Postfix instance to be started, stopped, etc., by a multi-instance manager.</dl>
<h2>Non-Shared Files</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>data_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory with Postfix-writable data files (for example: caches, pseudo-random numbers).</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/1-postfix/">postfix</a>(1) Postfix control program
<a href="//www.systutorials.com/docs/linux/man/1-postmulti/">postmulti</a>(1) full-blown multi-instance manager
$daemon_directory/postfix-wrapper simple multi-instance manager</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
