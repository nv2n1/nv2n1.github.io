---
title: "postmulti(1)"
name: "postmulti"
section: "1"
letter: "p"
url: "/docs/linux/man/1-postmulti/"
description: "postmulti – Postfix multi-instance manager"
---

<h2 class="name">NAME</h2>
<p> postmulti &#8211; Postfix multi-instance manager </p>
<h2>SYNOPSIS</h2>
<p> <code>Enabling multi-instance management:</code> </p>
<p> <code>postmulti</code> <code>-e init</code> [<code>-v</code>] </p>
<p> <code>Iterator mode:</code> </p>
<p> <code>postmulti</code> <code>-l</code> [<code>-aRv</code>] [<code>-g </code><i>group</i>] [<code>-i </code><i>name</i>] </p>
<p> <code>postmulti</code> <code>-p</code> [<code>-av</code>] [<code>-g </code><i>group</i>] [<code>-i </code><i>name</i>] <i>postfix-command&#8230;</i> </p>
<p> <code>postmulti</code> <code>-x</code> [<code>-aRv</code>] [<code>-g </code><i>group</i>] [<code>-i </code><i>name</i>] <i>unix-command&#8230;</i> </p>
<p> <code>Life-cycle management:</code> </p>
<p> <code>postmulti</code> <code>-e create</code> [<code>-av</code>] [<code>-g </code><i>group</i>] [<code>-i </code><i>name</i>] [<code>-G </code><i>group</i>] [<code>-I </code><i>name</i>] [<i>param=value</i> &#8230;] </p>
<p> <code>postmulti</code> <code>-e import</code> [<code>-av</code>] [<code>-g </code><i>group</i>] [<code>-i </code><i>name</i>] [<code>-G </code><i>group</i>] [<code>-I </code><i>name</i>] [<code>config_directory=</code><i>/path</i>] </p>
<p> <code>postmulti</code> <code>-e destroy</code> [<code>-v</code>] <code>-i </code><i>name</i> </p>
<p> <code>postmulti</code> <code>-e deport</code> [<code>-v</code>] <code>-i </code><i>name</i> </p>
<p> <code>postmulti</code> <code>-e enable</code> [<code>-v</code>] <code>-i </code><i>name</i> </p>
<p> <code>postmulti</code> <code>-e disable</code> [<code>-v</code>] <code>-i </code><i>name</i> </p>
<p> <code>postmulti</code> <code>-e assign</code> [<code>-v</code>] <code>-i </code><i>name</i> [<code>-I </code><i>name</i>] [-G <i>group</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) command allows a Postfix administrator to manage multiple Postfix instances on a single host. </p>
<p> <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) implements two fundamental modes of operation. In <code>iterator</code> mode, it executes the same command for multiple Postfix instances. In <code>life-cycle management</code> mode, it adds or deletes one instance, or changes the multi-instance status of one instance. </p>
<p> Each mode of operation has its own command syntax. For this reason, each mode is documented in separate sections below.</p>
<h2>BACKGROUND</h2>
<p> A multi-instance configuration consists of one primary Postfix instance, and one or more secondary instances whose configuration directory pathnames are recorded in the primary instance&#8217;s main.cf file. Postfix instances share program files and documentation, but have their own configuration, queue and data directories. </p>
<p> Currently, only the default Postfix instance can be used as primary instance in a multi-instance configuration. The <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) command does not currently support a <code>-c</code> option to select an alternative primary instance, and exits with a fatal error if the <code>MAIL_CONFIG</code> environment variable is set to a non-default configuration directory. </p>
<p> See the MULTI_INSTANCE_README tutorial for a more detailed discussion of multi-instance management with <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1).</p>
<h2>ITERATOR MODE</h2>
<p> In iterator mode, <code>postmulti</code> performs the same operation on all Postfix instances in turn. </p>
<p> If multi-instance support is not enabled, the requested command is performed just for the primary instance. </p>
<p> Iterator mode implements the following command options:</p>
<h2>Instance selection</h2>
<dl>
<dt><code>-a</code></p>
<dd> Perform the operation on all instances. This is the default.</p>
<dt><code>-g </code><i>group</i></p>
<dd> Perform the operation only for members of the named <i>group</i>.</p>
<dt><code>-i </code><i>name</i></p>
<dd> Perform the operation only for the instance with the specified <i>name</i>. You can specify either the instance name or the absolute pathname of the instance&#8217;s configuration directory. Specify &quot;-&quot; to select the primary Postfix instance.</p>
<dt><code>-R</code></p>
<dd> Reverse the iteration order. This may be appropriate when updating a multi-instance system, where &quot;sink&quot; instances are started before &quot;source&quot; instances. </p>
<p> This option cannot be used with <code>-p</code>.</dl>
<h2>List mode</h2>
<dl>
<dt><code>-l</code></p>
<dd> List Postfix instances with their instance name, instance group name, enable/disable status and configuration directory.</dl>
<h2>Postfix-wrapper mode</h2>
<dl>
<dt><code>-p </code><i>postfix-command</i></p>
<dd> Invoke <code><a href="/docs/linux/man/1-postfix/">postfix</a>(1)</code> to execute <i>postfix-command</i>. This option implements the <code><a href="/docs/linux/man/5-postfix-wrapper/">postfix-wrapper</a></code>(5) interface.</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> With &quot;start&quot;-like commands, &quot;postfix check&quot; is executed for instances that are not enabled. The full list of commands is specified with the postmulti_start_commands parameter.</p>
<dt>&bull;</p>
<dd> With &quot;stop&quot;-like commands, the iteration order is reversed, and disabled instances are skipped. The full list of commands is specified with the postmulti_stop_commands parameter.</p>
<dt>&bull;</p>
<dd> With &quot;reload&quot; and other commands that require a started instance, disabled instances are skipped. The full list of commands is specified with the postmulti_control_commands parameter.</p>
<dt>&bull;</p>
<dd> With &quot;status&quot; and other commands that don&#8217;t require a started instance, the command is executed for all instances.</dl>
</dl>
<dt>
<dd> The <code>-p</code> option can also be used interactively to start/stop/etc. a named instance or instance group. For example, to start just the instances in the group &quot;msa&quot;, invoke <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> # postmulti -g msa -p start</dl>
</dl>
</dl>
<h2>Command mode</h2>
<dl>
<dt><code>-x </code><i>unix-command</i></p>
<dd> Execute the specified <i>unix-command</i> for all Postfix instances. The command runs with appropriate environment settings for MAIL_CONFIG, command_directory, daemon_directory, config_directory, queue_directory, data_directory, multi_instance_name, multi_instance_group and multi_instance_enable.</dl>
<h2>Other options</h2>
<dl>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>LIFE-CYCLE MANAGEMENT MODE</h2>
<p> With the <code>-e</code> option <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) can be used to add or delete a Postfix instance, and to manage the multi-instance status of an existing instance. </p>
<p> The following options are implemented:</p>
<h2>Existing instance selection</h2>
<dl>
<dt><code>-a</code></p>
<dd> When creating or importing an instance, place the new instance at the front of the secondary instance list.</p>
<dt><code>-g </code><i>group</i></p>
<dd> When creating or importing an instance, place the new instance before the first secondary instance that is a member of the specified group.</p>
<dt><code>-i </code><i>name</i></p>
<dd> When creating or importing an instance, place the new instance before the matching secondary instance. </p>
<p> With other life-cycle operations, apply the operation to the named existing instance. Specify &quot;-&quot; to select the primary Postfix instance.</dl>
<h2>New or existing instance name assignment</h2>
<dl>
<dt><code>-I </code><i>name</i></p>
<dd> Assign the specified instance <i>name</i> to an existing instance, newly-created instance, or imported instance. Instance names other than &quot;-&quot; (which makes the instance &quot;nameless&quot;) must start with &quot;postfix-&quot;. This restriction reduces the likelihood of name collisions with system files.</p>
<dt><code>-G </code><i>group</i></p>
<dd> Assign the specified <i>group</i> name to an existing instance or to a newly created or imported instance.</dl>
<h2>Instance creation/deletion/status change</h2>
<dl>
<dt><code>-e </code><i>action</i></p>
<dd> &quot;Edit&quot; managed instances. The following actions are supported:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>init</code></p>
<dd> This command is required before <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) can be used to manage Postfix instances. The &quot;postmulti -e init&quot; command updates the primary instance&#8217;s main.cf file by setting:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
multi_instance_wrapper =
        ${command_directory}/postmulti -p --
multi_instance_enable = yes
</pre>
</dl>
</dl>
<dt>
<dd> You can set these by other means if you prefer.</p>
<dt><code>create</code></p>
<dd> Create a new Postfix instance and add it to the multi_instance_directories parameter of the primary instance. The &quot;<code>-I </code><i>name</i>&quot; option is recommended to give the instance a short name that is used to construct default values for the private directories of the new instance. The &quot;<code>-G </code><i>group</i>&quot; option may be specified to assign the instance to a group, otherwise, the new instance is not a member of any groups. </p>
<p> The new instance main.cf is the stock main.cf with the parameters that specify the locations of shared files cloned from the primary instance. For &quot;nameless&quot; instances, you should manually adjust &quot;syslog_name&quot; to yield a unique &quot;logtag&quot; starting with &quot;postfix-&quot; that will uniquely identify the instance in the mail logs. It is simpler to assign the instance a short name with the &quot;<code>-I </code><i>name</i>&quot; option. </p>
<p> Optional &quot;name=value&quot; arguments specify the instance config_directory, queue_directory and data_directory. For example:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd>
<pre>
# postmulti -I postfix-mumble \
        -G mygroup -e create \
        config_directory=/my/config/dir \
        queue_directory=/my/queue/dir \
        data_directory=/my/data/dir
</pre>
</dl>
</dl>
<dt>
<dd> If any of these pathnames is not supplied, the program attempts to generate the pathname by taking the corresponding primary instance pathname, and by replacing the last pathname component by the value of the <code>-I</code> option. </p>
<p> If the instance configuration directory already exists, and contains both a main.cf and master.cf file, <code>create</code> will &quot;import&quot; the instance as-is. For existing instances, <code>create</code> and <code>import</code> are identical.</p>
<dt><code>import</code></p>
<dd> Import an existing instance into the list of instances managed by the <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) multi-instance manager. This adds the instance to the multi_instance_directories list of the primary instance. If the &quot;<code>-I </code><i>name</i>&quot; option is provided it specifies the new name for the instance and is used to define a default location for the instance configuration directory (as with <code>create</code> above). The &quot;<code>-G </code><i>group</i>&quot; option may be used to assign the instance to a group. Add a &quot;<code>config_directory=</code><i>/path</i>&quot; argument to override a default pathname based on &quot;<code>-I </code><i>name</i>&quot;.</p>
<dt><code>destroy</code></p>
<dd> Destroy a secondary Postfix instance. To be a candidate for destruction an instance must be disabled, stopped and its queue must not contain any messages. Attempts to destroy the primary Postfix instance trigger a fatal error, without destroying the instance. </p>
<p> The instance is removed from the primary instance main.cf file&#8217;s alternate_config_directories parameter and its data, queue and configuration directories are cleaned of files and directories created by the Postfix system. The main.cf and master.cf files are removed from the configuration directory even if they have been modified since initial creation. Finally, the instance is &quot;deported&quot; from the list of managed instances. </p>
<p> If other files are present in instance private directories, the directories may not be fully removed, a warning is logged to alert the administrator. It is expected that an instance built using &quot;fresh&quot; directories via the <code>create</code> action will be fully removed by the <code>destroy</code> action (if first disabled). If the instance configuration and queue directories are populated with additional files (access and rewriting tables, chroot jail content, etc.) the instance directories will not be fully removed. </p>
<p> The <code>destroy</code> action triggers potentially dangerous file removal operations. Make sure the instance&#8217;s data, queue and configuration directories are set correctly and do not contain any valuable files.</p>
<dt><code>deport</code></p>
<dd> Deport a secondary instance from the list of managed instances. This deletes the instance configuration directory from the primary instance&#8217;s multi_instance_directories list, but does not remove any files or directories.</p>
<dt><code>assign</code></p>
<dd> Assign a new instance name or a new group name to the selected instance. Use &quot;<code>-G &#8211;</code>&quot; to specify &quot;no group&quot; and &quot;<code>-I &#8211;</code>&quot; to specify &quot;no name&quot;. If you choose to make an instance &quot;nameless&quot;, set a suitable syslog_name in the corresponding main.cf file.</p>
<dt><code>enable</code></p>
<dd> Mark the selected instance as enabled. This just sets the multi_instance_enable parameter to &quot;yes&quot; in the instance&#8217;s main.cf file.</p>
<dt><code>disable</code></p>
<dd> Mark the selected instance as disabled. This means that the instance will not be started etc. with &quot;postfix start&quot;, &quot;postmulti -p start&quot; and so on. The instance can still be started etc. with &quot;postfix -c config-directory start&quot;.</dl>
</dl>
</dl>
<h2>Other options</h2>
<dl>
<dt><code>-v</code></p>
<dd> Enable verbose logging for debugging purposes. Multiple <code>-v</code> options make the software increasingly verbose.</dl>
<h2>ENVIRONMENT</h2>
<p> The <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) command exports the following environment variables before executing the requested <i>command</i> for a given instance:</p>
<dl>
<dt><code>MAIL_VERBOSE</code></p>
<dd> This is set when the -v command-line option is present.</p>
<dt><code>MAIL_CONFIG</code></p>
<dd> The location of the configuration directory of the instance.</dl>
<h2>CONFIGURATION PARAMETERS</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The directory with Postfix support programs and daemon programs.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The list of environment parameters that a privileged Postfix process will import from a non-Postfix parent process, or name=value environment overrides.</p>
<dt><code>multi_instance_directories (empty)</code></p>
<dd> An optional list of non-default Postfix configuration directories; these directories belong to additional Postfix instances that share the Postfix executable files and documentation with the default Postfix instance, and that are started, stopped, etc., together with the default Postfix instance.</p>
<dt><code>multi_instance_group (empty)</code></p>
<dd> The optional instance group name of this Postfix instance.</p>
<dt><code>multi_instance_name (empty)</code></p>
<dd> The optional instance name of this Postfix instance.</p>
<dt><code>multi_instance_enable (no)</code></p>
<dd> Allow this Postfix instance to be started, stopped, etc., by a multi-instance manager.</p>
<dt><code>postmulti_start_commands (start)</code></p>
<dd> The <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) commands that the <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) instance manager treats as &quot;start&quot; commands.</p>
<dt><code>postmulti_stop_commands (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) commands that the <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) instance manager treats as &quot;stop&quot; commands.</p>
<dt><code>postmulti_control_commands (reload flush)</code></p>
<dd> The <code><a href="/docs/linux/man/1-postfix/">postfix</a></code>(1) commands that the <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) instance manager treats as &quot;control&quot; commands, that operate on running instances.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd> The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd> A prefix that is prepended to the process name in syslog records, so that, for example, &quot;smtpd&quot; becomes &quot;prefix/smtpd&quot;.</dl>
<p> Available in Postfix 3.0 and later:</p>
<dl>
<dt><code>meta_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of non-executable files that are shared among multiple Postfix instances, such as postfix-files, dynamicmaps.cf, and the multi-instance template files main.cf.proto and master.cf.proto.</p>
<dt><code>shlib_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd> The location of Postfix dynamically-linked libraries (libpostfix-*.so), and the default location of Postfix database plugins (postfix-*.so) that have a relative pathname in the dynamicmaps.cf file.</dl>
<h2>FILES</h2>
<pre>
$meta_directory/main.cf.proto, stock configuration file
$meta_directory/master.cf.proto, stock configuration file
$daemon_directory/postmulti-script, life-cycle helper program
</pre>
<h2>SEE ALSO</h2>
<pre>
<a href="//www.systutorials.com/docs/linux/man/1-postfix/">postfix</a>(1), Postfix control program
<a href="//www.systutorials.com/docs/linux/man/5-postfix-wrapper/">postfix-wrapper</a>(5), Postfix multi-instance API
</pre>
<h2>README FILES</h2>
<p> Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>
MULTI_INSTANCE_README, Postfix multi-instance management
</pre>
<h2>HISTORY</h2>
<p> The <code><a href="/docs/linux/man/1-postmulti/">postmulti</a></code>(1) command was introduced with Postfix version 2.6.</p>
<h2>LICENSE</h2>
<p> The Secure Mailer license must be distributed with this software.</p>
<h2>AUTHOR(S)</h2>
<pre>
Victor Duchovni
Morgan Stanley
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA
</pre>
<h2>Index</h2>
