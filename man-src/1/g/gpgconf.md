---
title: "gpgconf(1)"
name: "gpgconf"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gpgconf/"
description: "gpgconf – Modify .gnupg home directories"
---

<h2 class="name">NAME</h2>
<p> <code>gpgconf</code> &#8211; Modify .gnupg home directories </p>
<h2>SYNOPSIS</h2>
<p> <code>gpgconf</code> [<i>options</i>] <code>&#8211;list-components</code><br />
 <code>gpgconf</code> [<i>options</i>] <code>&#8211;list-options</code> <i>component</i><br />
 <code>gpgconf</code> [<i>options</i>] <code>&#8211;change-options</code> <i>component</i> </p>
<h2>DESCRIPTION</h2>
<p> The <code>gpgconf</code> is a utility to automatically and reasonable safely query and modify configuration files in the &#8216;<i>.gnupg</i>&#8216; home directory. It is designed not to be invoked manually by the user, but automatically by graphical user interfaces (GUI). ([Please note that currently no locking is done, so concurrent access should be avoided. There are some precautions to avoid corruption with concurrent usage, but results may be inconsistent and some changes may get lost. The stateless design makes it difficult to provide more guarantees.]) </p>
<p> <code>gpgconf</code> provides access to the configuration of one or more components of the GnuPG system. These components correspond more or less to the programs that exist in the GnuPG framework, like GPG, GPGSM, DirMngr, etc. But this is not a strict one-to-one relationship. Not all configuration options are available through <code>gpgconf</code>. <code>gpgconf</code> provides a generic and abstract method to access the most important configuration options that can feasibly be controlled via such a mechanism. </p>
<p> <code>gpgconf</code> can be used to gather and change the options available in each component, and can also provide their default values. <code>gpgconf</code> will give detailed type information that can be used to restrict the user&#8217;s input without making an attempt to commit the changes. </p>
<p> <code>gpgconf</code> provides the backend of a configuration editor. The configuration editor would usually be a graphical user interface program that displays the current options, their default values, and allows the user to make changes to the options. These changes can then be made active with <code>gpgconf</code> again. Such a program that uses <code>gpgconf</code> in this way will be called GUI throughout this section. </p>
<h2>COMMANDS</h2>
<p> One of the following commands must be given: </p>
<dl>
<dt><code>&#8211;list-components</code></p>
<dd> List all components. This is the default command used if none is specified. </p>
<dt><code>&#8211;check-programs</code></p>
<dd> List all available backend programs and test whether they are runnable. </p>
<dt><code>&#8211;list-options </code><i>component</i></p>
<dd> List all options of the component <i>component</i>. </p>
<dt><code>&#8211;change-options </code><i>component</i></p>
<dd> Change the options of the component <i>component</i>. </p>
<dt><code>&#8211;check-options </code><i>component</i></p>
<dd> Check the options for the component <i>component</i>. </p>
<dt><code>&#8211;apply-profile </code><i>file</i></p>
<dd> Apply the configuration settings listed in <i>file</i> to the configuration files. If <i>file</i> has no suffix and no slashes the command first tries to read a file with the suffix <code>.prf</code> from the data directory (<code>gpgconf &#8211;list-dirs datadir</code>) before it reads the file verbatim. A profile is divided into sections using the bracketed component name. Each section then lists the option which shall go into the respective configuration file. </p>
<dt><code>&#8211;apply-defaults</code></p>
<dd> Update all configuration files with values taken from the global configuration file (usually &#8216;<i>/etc/gnupg/gpgconf.conf</i>&#8216;). </p>
<dt><code>&#8211;list-dirs [</code><i>names</i>]</p>
<dd> Lists the directories used by <code>gpgconf</code>. One directory is listed per line, and each line consists of a colon-separated list where the first field names the directory type (for example <code>sysconfdir</code>) and the second field contains the percent-escaped directory. Although they are not directories, the socket file names used by <code>gpg-agent</code> and <code>dirmngr</code> are printed as well. Note that the socket file names and the <code>homedir</code> lines are the default names and they may be overridden by command line switches. If <i>names</i> are given only the directories or file names specified by the list names are printed without any escaping. </p>
<dt><code>&#8211;list-config [</code><i>filename</i>]</p>
<dd> List the global configuration file in a colon separated format. If <i>filename</i> is given, check that file instead. </p>
<dt><code>&#8211;check-config [</code><i>filename</i>]</p>
<dd> Run a syntax check on the global configuration file. If <i>filename</i> is given, check that file instead. </p>
<dt><code>&#8211;query-swdb </code><i>package_name</i> [<i>version_string</i>]</p>
<dd> Returns the current version for <i>package_name</i> and if <i>version_string</i> is given also an indicator on whether an update is available. The actual file with the software version is automatically downloaded and checked by <code>dirmngr</code>. <code>dirmngr</code> uses a thresholds to avoid download the file too often and it does this by default only if it can be done via Tor. To force an update of that file this command can be used: </p>
<dl>
<dt>
<dd>
<pre>
       gpg-connect-agent --dirmngr 'loadswdb --force' /bye
</pre>
</dl>
<dt><code>&#8211;reload [</code><i>component</i>]</p>
<dd> Reload all or the given component. This is basically the same as sending a SIGHUP to the component. Components which don&#8217;t support reloading are ignored. Without <i>component</i> or by using &quot;all&quot; for <i>component</i> all components which are daemons are reloaded. </p>
<dt><code>&#8211;launch [</code><i>component</i>]</p>
<dd> If the <i>component</i> is not already running, start it. <code>component</code> must be a daemon. This is in general not required because the system starts these daemons as needed. However, external software making direct use of <code>gpg-agent</code> or <code>dirmngr</code> may use this command to ensure that they are started. Using &quot;all&quot; for <i>component</i> launches all components which are daemons. </p>
<dt><code>&#8211;kill [</code><i>component</i>]</p>
<dd> Kill the given component that runs as a daemon, including <code>gpg-agent</code>, <code>dirmngr</code>, and <code>scdaemon</code>. A <code>component</code> which does not run as a daemon will be ignored. Using &quot;all&quot; for <i>component</i> kills all components running as daemons. Note that as of now reload and kill have the same effect for <code>scdaemon</code>. </p>
<dt><code>&#8211;create-socketdir</code></p>
<dd> Create a directory for sockets below /run/user or /var/run/user. This is command is only required if a non default home directory is used and the /run based sockets shall be used. For the default home directory GnUPG creates a directory on the fly. </p>
<dt><code>&#8211;remove-socketdir</code></p>
<dd> Remove a directory created with command <code>&#8211;create-socketdir</code>. </p>
</dl>
<h2>OPTIONS</h2>
<p> The following options may be used: </p>
<dl>
<dt><code>-o </code><i>file</i></p>
<dd> <code>&#8211;output </code><i>file</i> Write output to <i>file</i>. Default is to write to stdout. </p>
<dt><code>-v</code></p>
<dd> <code>&#8211;verbose</code> Outputs additional information while running. Specifically, this extends numerical field values by human-readable descriptions. </p>
<dt><code>-q</code></p>
<dd> <code>&#8211;quiet</code> Try to be as quiet as possible. </p>
<dt><code>&#8211;homedir </code><i>dir</i></p>
<dd> Set the name of the home directory to <i>dir</i>. If this option is not used, the home directory defaults to &#8216;<i>~/.gnupg</i>&#8216;. It is only recognized when given on the command line. It also overrides any home directory stated through the environment variable &#8216;<i>GNUPGHOME</i>&#8216; or (on Windows systems) by means of the Registry entry <i>HKCU\Software\GNU\GnuPG:HomeDir</i>. </p>
<p> On Windows systems it is possible to install GnuPG as a portable application. In this case only this command line option is considered, all other ways to set a home directory are ignored. </p>
<p> To install GnuPG as a portable application under Windows, create an empty file named &#8216;<i>gpgconf.ctl</i>&#8216; in the same directory as the tool &#8216;<i>gpgconf.exe</i>&#8216;. The root of the installation is then that directory; or, if &#8216;<i>gpgconf.exe</i>&#8216; has been installed directly below a directory named &#8216;<i>bin</i>&#8216;, its parent directory. You also need to make sure that the following directories exist and are writable: &#8216;<i>ROOT/home</i>&#8216; for the GnuPG home and &#8216;<i>ROOT/var/cache/gnupg</i>&#8216; for internal cache files. </p>
<dt><code>-n</code></p>
<dd> <code>&#8211;dry-run</code> Do not actually change anything. This is currently only implemented for <code>&#8211;change-options</code> and can be used for testing purposes. </p>
<dt><code>-r</code></p>
<dd> <code>&#8211;runtime</code> Only used together with <code>&#8211;change-options</code>. If one of the modified options can be changed in a running daemon process, signal the running daemon to ask it to reparse its configuration file after changing. </p>
<p> This means that the changes will take effect at run-time, as far as this is possible. Otherwise, they will take effect at the next start of the respective backend programs. </p>
<dt><code>&#8211;status-fd </code><i>n</i></p>
<dd> Write special status strings to the file descriptor <i>n</i>. This program returns the status messages SUCCESS or FAILURE which are helpful when the caller uses a double fork approach and can&#8217;t easily get the return code of the process. </p>
</dl>
<h2>USAGE</h2>
<p> The command <code>&#8211;list-components</code> will list all components that can be configured with <code>gpgconf</code>. Usually, one component will correspond to one GnuPG-related program and contain the options of that program&#8217;s configuration file that can be modified using <code>gpgconf</code>. However, this is not necessarily the case. A component might also be a group of selected options from several programs, or contain entirely virtual options that have a special effect rather than changing exactly one option in one configuration file. </p>
<p> A component is a set of configuration options that semantically belong together. Furthermore, several changes to a component can be made in an atomic way with a single operation. The GUI could for example provide a menu with one entry for each component, or a window with one tabulator sheet per component. </p>
<p> The command <code>&#8211;list-components</code> lists all available components, one per line. The format of each line is: </p>
<p> <i>name</i>:<i>description</i>:<i>pgmname</i>: </p>
<dl>
<dt><code>name</code></p>
<dd> This field contains a name tag of the component. The name tag is used to specify the component in all communication with <code>gpgconf</code>. The name tag is to be used <i>verbatim</i>. It is thus not in any escaped format. </p>
<dt><code>description</code></p>
<dd> The <i>string</i> in this field contains a human-readable description of the component. It can be displayed to the user of the GUI for informational purposes. It is <i>percent-escaped</i> and <i>localized</i>. </p>
<dt><code>pgmname</code></p>
<dd> The <i>string</i> in this field contains the absolute name of the program&#8217;s file. It can be used to unambiguously invoke that program. It is <i>percent-escaped</i>.</dl>
<p> Example:</p>
<dl>
<dt>
<dd>
<pre>
$ gpgconf --list-components
gpg:GPG for OpenPGP:/usr/local/bin/gpg2:
gpg-agent:GPG Agent:/usr/local/bin/gpg-agent:
scdaemon:Smartcard Daemon:/usr/local/bin/scdaemon:
gpgsm:GPG for S/MIME:/usr/local/bin/gpgsm:
dirmngr:Directory Manager:/usr/local/bin/dirmngr:
</pre>
</dl>
<h3>Checking programs</h3>
<p> &nbsp; </p>
<p> The command <code>&#8211;check-programs</code> is similar to <code>&#8211;list-components</code> but works on backend programs and not on components. It runs each program to test whether it is installed and runnable. This also includes a syntax check of all config file options of the program. </p>
<p> The command <code>&#8211;check-programs</code> lists all available programs, one per line. The format of each line is: </p>
<p> <i>name</i>:<i>description</i>:<i>pgmname</i>:<i>avail</i>:<i>okay</i>:<i>cfgfile</i>:<i>line</i>:<i>error</i>: </p>
<dl>
<dt><code>name</code></p>
<dd> This field contains a name tag of the program which is identical to the name of the component. The name tag is to be used <i>verbatim</i>. It is thus not in any escaped format. This field may be empty to indicate a continuation of error descriptions for the last name. The description and pgmname fields are then also empty. </p>
<dt><code>description</code></p>
<dd> The <i>string</i> in this field contains a human-readable description of the component. It can be displayed to the user of the GUI for informational purposes. It is <i>percent-escaped</i> and <i>localized</i>. </p>
<dt><code>pgmname</code></p>
<dd> The <i>string</i> in this field contains the absolute name of the program&#8217;s file. It can be used to unambiguously invoke that program. It is <i>percent-escaped</i>. </p>
<dt><code>avail</code></p>
<dd> The <i>boolean value</i> in this field indicates whether the program is installed and runnable. </p>
<dt><code>okay</code></p>
<dd> The <i>boolean value</i> in this field indicates whether the program&#8217;s config file is syntactically okay. </p>
<dt><code>cfgfile</code></p>
<dd> If an error occurred in the configuration file (as indicated by a false value in the field <code>okay</code>), this field has the name of the failing configuration file. It is <i>percent-escaped</i>. </p>
<dt><code>line</code></p>
<dd> If an error occurred in the configuration file, this field has the line number of the failing statement in the configuration file. It is an <i>unsigned number</i>. </p>
<dt><code>error</code></p>
<dd> If an error occurred in the configuration file, this field has the error text of the failing statement in the configuration file. It is <i>percent-escaped</i> and <i>localized</i>. </p>
</dl>
<p> In the following example the <code>dirmngr</code> is not runnable and the configuration file of <code>scdaemon</code> is not okay. </p>
<dl>
<dt>
<dd>
<pre>
$ gpgconf --check-programs
gpg:GPG for OpenPGP:/usr/local/bin/gpg2:1:1:
gpg-agent:GPG Agent:/usr/local/bin/gpg-agent:1:1:
scdaemon:Smartcard Daemon:/usr/local/bin/scdaemon:1:0:
gpgsm:GPG for S/MIME:/usr/local/bin/gpgsm:1:1:
dirmngr:Directory Manager:/usr/local/bin/dirmngr:0:0:
</pre>
</dl>
<p> The command configuration file in the same manner as <code>&#8211;check-programs</code>, but only for the component <i>component</i>. </p>
<h3>Listing options</h3>
<p> &nbsp; </p>
<p> Every component contains one or more options. Options may be gathered into option groups to allow the GUI to give visual hints to the user about which options are related. </p>
<p> The command lists all options (and the groups they belong to) in the component <i>component</i>, one per line. <i>component</i> must be the string in the field <i>name</i> in the output of the <code>&#8211;list-components</code> command. </p>
<p> There is one line for each option and each group. First come all options that are not in any group. Then comes a line describing a group. Then come all options that belong into each group. Then comes the next group and so on. There does not need to be any group (and in this case the output will stop after the last non-grouped option). </p>
<p> The format of each line is: </p>
<p> <i>name</i>:<i>flags</i>:<i>level</i>:<i>description</i>:<i>type</i>:<i>alt-type</i>:<i>argname</i>:<i>default</i>:<i>argdef</i>:<i>value</i> </p>
<dl>
<dt><code>name</code></p>
<dd> This field contains a name tag for the group or option. The name tag is used to specify the group or option in all communication with <code>gpgconf</code>. The name tag is to be used <i>verbatim</i>. It is thus not in any escaped format. </p>
<dt><code>flags</code></p>
<dd> The flags field contains an <i>unsigned number</i>. Its value is the OR-wise combination of the following flag values: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>group (1)</code></p>
<dd> If this flag is set, this is a line describing a group and not an option.</dl>
</dl>
<p> The following flag values are only defined for options (that is, if the <code>group</code> flag is not used). </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>optional arg (2)</code></p>
<dd> If this flag is set, the argument is optional. This is never set for <i>type</i> <code>0</code> (none) options. </p>
<dt><code>list (4)</code></p>
<dd> If this flag is set, the option can be given multiple times. </p>
<dt><code>runtime (8)</code></p>
<dd> If this flag is set, the option can be changed at runtime. </p>
<dt><code>default (16)</code></p>
<dd> If this flag is set, a default value is available. </p>
<dt><code>default desc (32)</code></p>
<dd> If this flag is set, a (runtime) default is available. This and the <code>default</code> flag are mutually exclusive. </p>
<dt><code>no arg desc (64)</code></p>
<dd> If this flag is set, and the <code>optional arg</code> flag is set, then the option has a special meaning if no argument is given. </p>
<dt><code>no change (128)</code></p>
<dd> If this flag is set, <code>gpgconf</code> ignores requests to change the value. GUI frontends should grey out this option. Note, that manual changes of the configuration files are still possible.</dl>
</dl>
<dt><code>level</code></p>
<dd> This field is defined for options and for groups. It contains an <i>unsigned number</i> that specifies the expert level under which this group or option should be displayed. The following expert levels are defined for options (they have analogous meaning for groups): </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>basic (0)</code></p>
<dd> This option should always be offered to the user. </p>
<dt><code>advanced (1)</code></p>
<dd> This option may be offered to advanced users. </p>
<dt><code>expert (2)</code></p>
<dd> This option should only be offered to expert users. </p>
<dt><code>invisible (3)</code></p>
<dd> This option should normally never be displayed, not even to expert users. </p>
<dt><code>internal (4)</code></p>
<dd> This option is for internal use only. Ignore it.</dl>
</dl>
<p> The level of a group will always be the lowest level of all options it contains. </p>
<dt><code>description</code></p>
<dd> This field is defined for options and groups. The <i>string</i> in this field contains a human-readable description of the option or group. It can be displayed to the user of the GUI for informational purposes. It is <i>percent-escaped</i> and <i>localized</i>. </p>
<dt><code>type</code></p>
<dd> This field is only defined for options. It contains an <i>unsigned number</i> that specifies the type of the option&#8217;s argument, if any. The following types are defined: </p>
<p> Basic types: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>none (0)</code></p>
<dd> No argument allowed. </p>
<dt><code>string (1)</code></p>
<dd> An <i>unformatted string</i>. </p>
<dt><code>int32 (2)</code></p>
<dd> A <i>signed number</i>. </p>
<dt><code>uint32 (3)</code></p>
<dd> An <i>unsigned number</i>.</dl>
</dl>
<p> Complex types: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>pathname (32)</code></p>
<dd> A <i>string</i> that describes the pathname of a file. The file does not necessarily need to exist. </p>
<dt><code>ldap server (33)</code></p>
<dd> A <i>string</i> that describes an LDAP server in the format: </p>
<p> <i>hostname</i>:<i>port</i>:<i>username</i>:<i>password</i>:<i>base_dn</i> </p>
<dt><code>key fingerprint (34)</code></p>
<dd> A <i>string</i> with a 40 digit fingerprint specifying a certificate. </p>
<dt><code>pub key (35)</code></p>
<dd> A <i>string</i> that describes a certificate by user ID, key ID or fingerprint. </p>
<dt><code>sec key (36)</code></p>
<dd> A <i>string</i> that describes a certificate with a key by user ID, key ID or fingerprint. </p>
<dt><code>alias list (37)</code></p>
<dd> A <i>string</i> that describes an alias list, like the one used with gpg&#8217;s group option. The list consists of a key, an equal sign and space separated values.</dl>
</dl>
<p> More types will be added in the future. Please see the <i>alt-type</i> field for information on how to cope with unknown types. </p>
<dt><code>alt-type</code></p>
<dd> This field is identical to <i>type</i>, except that only the types <code>0</code> to <code>31</code> are allowed. The GUI is expected to present the user the option in the format specified by <i>type</i>. But if the argument type <i>type</i> is not supported by the GUI, it can still display the option in the more generic basic type <i>alt-type</i>. The GUI must support all the defined basic types to be able to display all options. More basic types may be added in future versions. If the GUI encounters a basic type it doesn&#8217;t support, it should report an error and abort the operation. </p>
<dt><code>argname</code></p>
<dd> This field is only defined for options with an argument type <i>type</i> that is not <code>0</code>. In this case it may contain a <i>percent-escaped</i> and <i>localized string</i> that gives a short name for the argument. The field may also be empty, though, in which case a short name is not known. </p>
<dt><code>default</code></p>
<dd> This field is defined only for options for which the <code>default</code> or <code>default desc</code> flag is set. If the <code>default</code> flag is set, its format is that of an <i>option argument</i> (see: [Format conventions], for details). If the default value is empty, then no default is known. Otherwise, the value specifies the default value for this option. If the <code>default desc</code> flag is set, the field is either empty or contains a description of the effect if the option is not given. </p>
<dt><code>argdef</code></p>
<dd> This field is defined only for options for which the <code>optional arg</code> flag is set. If the <code>no arg desc</code> flag is not set, its format is that of an <i>option argument</i> (see: [Format conventions], for details). If the default value is empty, then no default is known. Otherwise, the value specifies the default argument for this option. If the <code>no arg desc</code> flag is set, the field is either empty or contains a description of the effect of this option if no argument is given. </p>
<dt><code>value</code></p>
<dd> This field is defined only for options. Its format is that of an <i>option argument</i>. If it is empty, then the option is not explicitly set in the current configuration, and the default applies (if any). Otherwise, it contains the current value of the option. Note that this field is also meaningful if the option itself does not take a real argument (in this case, it contains the number of times the option appears).</dl>
<h3>Changing options</h3>
<p> &nbsp; </p>
<p> The command to change the options of the component <i>component</i> to the specified values. <i>component</i> must be the string in the field <i>name</i> in the output of the <code>&#8211;list-components</code> command. You have to provide the options that shall be changed in the following format on standard input: </p>
<p> <i>name</i>:<i>flags</i>:<i>new-value</i> </p>
<dl>
<dt><code>name</code></p>
<dd> This is the name of the option to change. <i>name</i> must be the string in the field <i>name</i> in the output of the <code>&#8211;list-options</code> command. </p>
<dt><code>flags</code></p>
<dd> The flags field contains an <i>unsigned number</i>. Its value is the OR-wise combination of the following flag values: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>default (16)</code></p>
<dd> If this flag is set, the option is deleted and the default value is used instead (if applicable).</dl>
</dl>
<dt><code>new-value</code></p>
<dd> The new value for the option. This field is only defined if the <code>default</code> flag is not set. The format is that of an <i>option argument</i>. If it is empty (or the field is omitted), the default argument is used (only allowed if the argument is optional for this option). Otherwise, the option will be set to the specified value.</dl>
<p> The output of the command is the same as that of <code>&#8211;check-options</code> for the modified configuration file. </p>
<p> Examples: </p>
<p> To set the force option, which is of basic type <code>none (0)</code>: </p>
<dl>
<dt>
<dd>
<pre>
$ echo 'force:0:1' | gpgconf --change-options dirmngr
</pre>
</dl>
<p> To delete the force option: </p>
<dl>
<dt>
<dd>
<pre>
$ echo 'force:16:' | gpgconf --change-options dirmngr
</pre>
</dl>
<p> The <code>&#8211;runtime</code> option can influence when the changes take effect. </p>
<h3>Listing global options</h3>
<p> &nbsp; </p>
<p> Sometimes it is useful for applications to look at the global options file &#8216;<i>gpgconf.conf</i>&#8216;. The colon separated listing format is record oriented and uses the first field to identify the record type: </p>
<dl>
<dt><code>k</code></p>
<dd> This describes a key record to start the definition of a new ruleset for a user/group. The format of a key record is: </p>
<p>&nbsp;<wbr>&nbsp;<code>k:</code><i>user</i>:<i>group</i>: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>user</code></p>
<dd> This is the user field of the key. It is percent escaped. See the definition of the gpgconf.conf format for details. </p>
<dt><code>group</code></p>
<dd> This is the group field of the key. It is percent escaped.</dl>
</dl>
<dt><code>r</code></p>
<dd> This describes a rule record. All rule records up to the next key record make up a rule set for that key. The format of a rule record is: </p>
<p>&nbsp;<wbr>&nbsp;<code>r:::</code><i>component</i>:<i>option</i>:<i>flag</i>:<i>value</i>: </p>
<dl>
<dt>
<dd>
<dl>
<dt><code>component</code></p>
<dd> This is the component part of a rule. It is a plain string. </p>
<dt><code>option</code></p>
<dd> This is the option part of a rule. It is a plain string. </p>
<dt><code>flag</code></p>
<dd> This is the flags part of a rule. There may be only one flag per rule but by using the same component and option, several flags may be assigned to an option. It is a plain string. </p>
<dt><code>value</code></p>
<dd> This is the optional value for the option. It is a percent escaped string with a single quotation mark to indicate a string. The quotation mark is only required to distinguish between no value specified and an empty string.</dl>
</dl>
</dl>
<p> Unknown record types should be ignored. Note that there is intentionally no feature to change the global option file through <code>gpgconf</code>. </p>
<h3>Get and compare software versions.</h3>
<p> &nbsp; </p>
<p> The GnuPG Project operates a server to query the current versions of software packages related to GnuPG. <code>gpgconf</code> can be used to access this online database. To allow for offline operations, this feature works by having <code>dirmngr</code> download a file from <code><a rel="nofollow" href="https://versions.gnupg.org">https://versions.gnupg.org</a></code>, checking the signature of that file and storing the file in the GnuPG home directory. If <code>gpgconf</code> is used and <code>dirmngr</code> is running, it may ask <code>dirmngr</code> to refresh that file before itself uses the file. </p>
<p> The command <code>&#8211;query-swdb</code> returns information for the given package in a colon delimited format: </p>
<dl>
<dt><code>name</code></p>
<dd> This is the name of the package as requested. Note that &quot;gnupg&quot; is a special name which is replaced by the actual package implementing this version of GnuPG. For this name it is also not required to specify a version because <code>gpgconf</code> takes its own version in this case. </p>
<dt><code>iversion</code></p>
<dd> The currently installed version or an empty string. The value is taken from the command line argument but may be provided by gpg if not given. </p>
<dt><code>status</code></p>
<dd> The status of the software package according to this table:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>&#8211;</code></p>
<dd> No information available. This is either because no current version has been specified or due to an error.</p>
<dt><code>?</code></p>
<dd> The given name is not known in the online database.</p>
<dt><code>u</code></p>
<dd> An update of the software is available.</p>
<dt><code>c</code></p>
<dd> The installed version of the software is current.</p>
<dt><code>n</code></p>
<dd> The installed version is already newer than the released version.</dl>
</dl>
<dt><code>urgency</code></p>
<dd> If the value (the empty string should be considered as zero) is greater than zero an important update is available. </p>
<dt><code>error</code></p>
<dd> This returns an <code>gpg-error</code> error code to distinguish between various failure modes. </p>
<dt><code>filedate</code></p>
<dd> This gives the date of the file with the version numbers in standard ISO format (<code>yyyymmddThhmmss</code>). The date has been extracted by <code>dirmngr</code> from the signature of the file. </p>
<dt><code>verified</code></p>
<dd> This gives the date in ISO format the file was downloaded. This value can be used to evaluate the freshness of the information. </p>
<dt><code>version</code></p>
<dd> This returns the version string for the requested software from the file. </p>
<dt><code>reldate</code></p>
<dd> This returns the release date in ISO format. </p>
<dt><code>size</code></p>
<dd> This returns the size of the package as decimal number of bytes. </p>
<dt><code>hash</code></p>
<dd> This returns a hexified SHA-2 hash of the package. </p>
</dl>
<p> More fields may be added in future to the output. </p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/gnupg/gpgconf.conf</code></p>
<dd>
&nbsp;<wbr>&nbsp;If this file exists, it is processed as a global configuration file.<br />
&nbsp;<wbr>&nbsp;A commented example can be found in the&nbsp;&#8216;<i>examples</i>&#8216;&nbsp;directory of<br />
&nbsp;<wbr>&nbsp;the distribution. </p>
<dt><i>GNUPGHOME</i>/swdb.lst</p>
<dd>
&nbsp;<wbr>&nbsp;A file with current software versions.&nbsp;<wbr>&nbsp;<code>dirmngr</code>&nbsp;creates<br />
&nbsp;<wbr>&nbsp;this file on demand from an online resource. </p>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gpg/">gpg</a></code>(1), <code><a href="/docs/linux/man/1-gpgsm/">gpgsm</a></code>(1), <code><a href="/docs/linux/man/1-gpg-agent/">gpg-agent</a></code>(1), <code><a href="/docs/linux/man/1-scdaemon/">scdaemon</a></code>(1), <code><a href="/docs/linux/man/1-dirmngr/">dirmngr</a></code>(1) </p>
<p> The full documentation for this tool is maintained as a Texinfo manual. If GnuPG and the info program are properly installed at your site, the command </p>
<dl>
<dt>
<dd>
<pre>
info gnupg
</pre>
</dl>
<p> should give you access to the complete manual including a menu structure and an index. </p>
<h2>Index</h2>
