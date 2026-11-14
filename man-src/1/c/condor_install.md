---
title: "condor_install(1)"
name: "condor_install"
section: "1"
letter: "c"
url: "/docs/linux/man/1-condor_install/"
description: "condor_install Configure or install HTCondor"
---

<h2>Name</h2>
<p> <i>condor_install</i> Configure or install HTCondor </p>
<h2>Synopsis</h2>
<p> <i>condor_configure</i> or <i>condor_install</i> [ &#8212; <code>help</code> ] [ &#8212; <code>usage</code> ] </p>
<p> <i>condor_configure</i> or <i>condor_install</i> [ &#8212; <code>install[=&lt;path/to/release&gt;] </code> ] [ &#8212; <code>install-dir=&lt;path&gt;</code> ] [ &#8212; <code>prefix=&lt;path&gt;</code> ] [ &#8212; <code>local-dir=&lt;path&gt;</code> ] [ &#8212; <code>make-personal-condor</code> ] [ &#8212; <code>bosco</code> ] [ &#8212; <code>type = &lt;submit, execute, manager &gt;</code> ] [ &#8212; <code>central-manager = &lt;hostname&gt;</code> ] [ &#8212; <code>owner = &lt;ownername &gt;</code> ] [ &#8212; <code>maybe-daemon-owner</code> ] [ &#8212; <code>install-log = &lt;file &gt;</code> ] [ &#8212; <code>overwrite</code> ] [ &#8212; <code>ignore-missing-libs</code> ] [ &#8212; <code>force</code> ] [ &#8212; <code>no-env-scripts</code> ] [ &#8212; <code>env-scripts-dir = &lt;directory &gt;</code> ] [ &#8212; <code>backup</code> ] [ &#8212; <code>credd</code> ] [ &#8212; <code>verbose</code> ] </p>
<h2>Description</h2>
<p> <i>condor_configure</i> and <i>condor_install</i> refer to a single script that installs and/or configures HTCondor on Unix machines. As the names imply, <i>condor_install</i> is intended to perform a HTCondor installation, and <i>condor_configure</i> is intended to configure (or reconfigure) an existing installation. Both will run with Perl 5.6.0 or more recent versions. </p>
<p> <i>condor_configure</i> (and <i>condor_install</i> ) are designed to be run more than one time where required. It can install HTCondor when invoked with a correct configuration via </p>
<p> condor_install </p>
<p> or </p>
<p> condor_configure &#8211;install </p>
<p> or, it can change the configuration files when invoked via </p>
<p> condor_configure </p>
<p> Note that changes in the configuration files do not result in changes while HTCondor is running. To effect changes while HTCondor is running, it is necessary to further use the <i>condor_reconfig</i> or <i>condor_restart</i> command. <i>condor_reconfig</i> is required where the currently executing daemons need to be informed of configuration changes. <i>condor_restart</i> is required where the options &#8212; <code>make-personal-condor</code> or &#8212; <code>type</code> are used, since these affect which daemons are running. </p>
<p> Running <i>condor_configure</i> or <i>condor_install</i> with no options results in a usage screen being printed. The &#8212; <code>help</code> option can be used to display a full help screen. </p>
<p> Within the options given below, the phrase <i>release directories</i> is the list of directories that are released with HTCondor. This list includes: bin , etc , examples , include , lib , libexec , man , sbin , sql and src . </p>
<h2>Options</h2>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print help screen and exit</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;usage</code></p>
<dl>
<dt>
<dd> Print short usage and exit</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;install</code></p>
<dl>
<dt>
<dd> Perform installation, assuming that the current working directory contains the release directories. Without further options, the configuration is that of a Personal HTCondor, a complete one-machine pool. If used as an upgrade within an existing installation directory, existing configuration files and local directory are preserved. This is the default behavior of <i>condor_install</i> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;install-dir=&lt;path&gt;</code></p>
<dl>
<dt>
<dd> Specifies the path where HTCondor should be installed or the path where it already is installed. The default is the current working directory.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;prefix=&lt;path&gt;</code></p>
<dl>
<dt>
<dd> This is an alias for <code>-install-dir</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;local-dir=&lt;path&gt;</code></p>
<dl>
<dt>
<dd> Specifies the location of the local directory, which is the directory that generally contains the local (machine-specific) configuration file as well as the directories where HTCondor daemons write their run-time information ( spool , log , execute ). This location is indicated by the LOCAL_DIR variable in the configuration file. When installing (that is, if <code>-install</code> is specified), <i>condor_configure</i> will properly create the local directory in the location specified. If none is specified, the default value is given by the evaluation of $(RELEASE_DIR)/local.$(HOSTNAME) .</p>
<dt>
<dd> During subsequent invocations of <i>condor_configure</i> (that is, without the &#8211;install option), if the &#8211;local-dir option is specified, the new directory will be created and the log , spool and execute directories will be moved there from their current location.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;make-personal-condor</code></p>
<dl>
<dt>
<dd> Installs and configures for Personal HTCondor, a fully-functional, one-machine pool.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;bosco</code></p>
<dl>
<dt>
<dd> Installs and configures Bosco, a personal HTCondor that submits jobs to remote batch systems.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;type= &lt;submit, execute, manager &gt;</code></p>
<dl>
<dt>
<dd> One or more of the types may be listed. This determines the roles that a machine may play in a pool. In general, any machine can be a submit and/or execute machine, and there is one central manager per pool. In the case of a Personal HTCondor, the machine fulfills all three of these roles.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;central-manager=&lt;hostname&gt;</code></p>
<dl>
<dt>
<dd> Instructs the current HTCondor installation to use the specified machine as the central manager. This modifies the configuration variable COLLECTOR_HOST to point to the given host name. The central manager machine&#8217;s HTCondor configuration needs to be independently configured to act as a manager using the option <code>-type=manager</code> .</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;owner=&lt;ownername&gt;</code></p>
<dl>
<dt>
<dd> Set configuration such that HTCondor daemons will be executed as the given owner. This modifies the ownership on the log , spool and execute directories and sets the CONDOR_IDS value in the configuration file, to ensure that HTCondor daemons start up as the specified effective user. This is only applicable when <i>condor_configure</i> is run by root. If not run as root, the owner is the user running the <i>condor_configure</i> command.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;maybe-daemon-owner</code></p>
<dl>
<dt>
<dd> If <code>-owner</code> is not specified and no appropriate user can be found to run Condor, then this option will allow the daemon user to be selected. This option is rarely needed by users but can be useful for scripts that invoke condor_configure to install Condor.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;install-log=&lt;file&gt;</code></p>
<dl>
<dt>
<dd> Save information about the installation in the specified file. This is normally only needed when condor_configure is called by a higher-level script, not when invoked by a person.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;overwrite</code></p>
<dl>
<dt>
<dd> Always overwrite the contents of the sbin directory in the installation directory. By default, <i>condor_install</i> will not install if it finds an existing sbin directory with HTCondor programs in it. In this case, <i>condor_install</i> will exit with an error message. Specify <code>-overwrite</code> or <code>-backup</code> to tell <i>condor_install</i> what to do.</p>
<dt>
<dd> This prevents <i>condor_install</i> from moving an sbin directory out of the way that it should not move. This is particularly useful when trying to install HTCondor in a location used by other things ( /usr , /usr/local , etc.) For example: <i>condor_install</i> <code>-prefix=/usr</code> will not move /usr/sbin out of the way unless you specify the <code>-backup</code> option.</p>
<dt>
<dd> The <code>-backup</code> behavior is used to prevent <i>condor_install</i> from overwriting running daemons &#8211; Unix semantics will keep the existing binaries running, even if they have been moved to a new directory.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;backup</code></p>
<dl>
<dt>
<dd> Always backup the sbin directory in the installation directory. By default, <i>condor_install</i> will not install if it finds an existing sbin directory with HTCondor programs in it. In this case, <i>condor_install</i> with exit with an error message. You must specify <code>-overwrite</code> or <code>-backup</code> to tell <i>condor_install</i> what to do.</p>
<dt>
<dd> This prevents <i>condor_install</i> from moving an sbin directory out of the way that it should not move. This is particularly useful if you&#8217;re trying to install HTCondor in a location used by other things ( /usr , /usr/local , etc.) For example: <i>condor_install</i> <code>-prefix=/usr</code> will not move /usr/sbin out of the way unless you specify the <code>-backup</code> option.</p>
<dt>
<dd> The <code>-backup</code> behavior is used to prevent <i>condor_install</i> from overwriting running daemons &#8211; Unix semantics will keep the existing binaries running, even if they have been moved to a new directory.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;ignore-missing-libs</code></p>
<dl>
<dt>
<dd> Ignore missing shared libraries that are detected by <i>condor_install</i> . By default, <i>condor_install</i> will detect missing shared libraries such as libstdc++.so.5 on Linux; it will print messages and exit if missing libraries are detected. The <code>&#8211;ignore-missing-libs</code> will cause <i>condor_install</i> to not exit, and to proceed with the installation if missing libraries are detected.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;force</code></p>
<dl>
<dt>
<dd> This is equivalent to enabling both the <code>&#8211;overwrite</code> and <code>&#8211;ignore-missing-libs</code> command line options.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;no-env-scripts</code></p>
<dl>
<dt>
<dd> By default, <i>condor_configure</i> writes simple sh and csh shell scripts which can be sourced by their respective shells to set the user&#8217;s PATH and CONDOR_CONFIG environment variables. This option prevents <i>condor_configure</i> from generating these scripts.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;env-scripts-dir=&lt;directory&gt;</code></p>
<dl>
<dt>
<dd> By default, the simple <i>sh</i> and <i>csh</i> shell scripts (see <code>&#8211;no-env-scripts</code> for details) are created in the root directory of the HTCondor installation. This option causes <i>condor_configure</i> to generate these scripts in the specified directory.</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;credd</code></p>
<dl>
<dt>
<dd> Configure the the <i>condor_credd</i> daemon (credential manager daemon).</p>
<dt>
<dd>
<dt>
<dd></dl>
<p> <code>&#8211;verbose</code></p>
<dl>
<dt>
<dd> Print information about changes to configuration variables as they occur.</p>
<dt>
<dd></dl>
<h2>Exit Status</h2>
<p> <i>condor_configure</i> will exit with a status value of 0 (zero) upon success, and it will exit with a nonzero value upon failure. </p>
<h2>Examples</h2>
<p> Install HTCondor on the machine (machine1 [at] cs.wisc.edu) to be the pool&#8217;s central manager. On machine1, within the directory that contains the unzipped HTCondor distribution directories: </p>
<p> % condor_install &#8211;type=submit,execute,manager </p>
<p> This will allow the machine to submit and execute HTCondor jobs, in addition to being the central manager of the pool. </p>
<p> To change the configuration such that machine2 [at] cs.wisc.edu is an execute-only machine (that is, a dedicated computing node) within a pool with central manager on machine1 [at] cs.wisc.edu, issue the command on that machine2 [at] cs.wisc.edu from within the directory where HTCondor is installed: </p>
<p> % condor_configure &#8211;central-manager=machine1 [at] cs.wisc.edu &#8211;type=execute </p>
<p> To change the location of the LOCAL_DIR directory in the configuration file, do (from the directory where HTCondor is installed): </p>
<p> % condor_configure &#8211;local-dir=/path/to/new/local/directory </p>
<p> This will move the log , spool , execute directories to /path/to/new/local/directory from the current local directory. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
