---
title: "cfagent(8)"
name: "cfagent"
section: "8"
letter: "c"
url: "/docs/linux/man/8-cfagent/"
description: "cfagent – system configuration agent"
---

<p>cfagent &#8211; system configuration agent</p>
<h2>Synopsis</h2>
<p>/usr/local/sbin/cfagent [options] </p>
<h2>Description</h2>
<p><code>cfengine</code> is a language based system specifically designed for testing and configuring unix-like systems attached to a TCP/IP network. You can think of <code>cfengine</code> as a very high level language &#8212; much higher level than Perl or shell. A single statement can result in many hundreds of links being created, or the permissions of many hundreds of files being set. The idea of <code>cfengine</code> is to create a single file or set of configuration files which will describe the setup of every host on your network. </p>
<p> <code>cfagent</code> runs on every host and parses one file (or file-set), the configuration of the host is checked against this file and, if desired, any deviations are fixed. <code>cfagent</code> reads a configuration file called cfengine.conf in a directory pointed to by the environment variable CFINPUTS. <code>cfagent</code> performs host integrity and security checks as well as installing and repairing system configuration.</p>
<h2>Command Line Options</h2>
<dl>
<dt>-a (&#8211;sysadm)</p>
<dd>Print only the name of the system administrator then quit.</p>
<dt>-b (&#8211;force-net-copy)</p>
<dd>Forces net copy even if remote server is localhost</p>
<dt>-c (&#8211;no-check-files)</p>
<dd>Do not check access rights on file systems</p>
<dt>-C (&#8211;no-check-mounts)</p>
<dd>Check mount points for consistency. If this option is set then directories which lie in the &#8221;mount point&#8220; area are checked to see whether there is anything mounted on them.</p>
<dt>-d (&#8211;debug)</p>
<dd>Enable debugging output. (parsing -d1,run, -d2, lite -d3)</p>
<dt>-D (&#8211;define)</p>
<dd>Define a compound class symbol of the form alpha.beta.gamma.</p>
<dt>-e (&#8211;no-edits)</p>
<dd>Suppress file editing.</p>
<dt>-E (&#8211;enforce-links)</p>
<dd>Globally force links to be created where plain files or links already exist. You have to use this in interactive mode and answer a yes/no query before <code>cfagent</code> will run like this.</p>
<dt>-f (&#8211;file)</p>
<dd>Parse filename after this switch. By default <code>cfagent</code> looks for a file called cfengine.conf in the current directory.</p>
<dt>-h (&#8211;help )</p>
<dd>Help information. Display version banner and options summary.</p>
<dt>-H (&#8211;no-hard-classes)</p>
<dd>Prevents <code>cfagent</code> from generating any internal class name information. Can be used for emulation purposes.</p>
<dt>-i (&#8211;no-ifconfig)</p>
<dd>Do not attempt to configure the local area network interface.</p>
<dt>-I (&#8211;inform)</p>
<dd>Switches on the inform output level, whereby <code>cfagent</code> reports everything it changes..</p>
<dt>-k (&#8211;no-copy)</p>
<dd>Do not copy/image any files.</p>
<dt>-K (&#8211;no-lock)</p>
<dd>Ignore locks when running.</p>
<dt>-l (&#8211;traverse-links)</p>
<dd>Normally <code>cfagent</code> does not follow symbolic links when recursively parsing directories. This option will force it to do so.</p>
<dt>-L (&#8211;delete-stale-links)</p>
<dd>Delete links which do not point to existing files (except in user home directories, which are not touched).</p>
<dt>-m (&#8211;no-mount)</p>
<dd>Do not attempt to mount file systems or edit the filesystem table.</p>
<dt>-M (&#8211;no-modules)</p>
<dd>Ignore modules in actionsequence.</p>
<dt>-n (&#8211;recon,&#8211;dry-run,&#8211;just-print)</p>
<dd>No action. Only print what has to be done without actually doing it.</p>
<dt>-N (&#8211;negate,&#8211;undefine)</p>
<dd>Cancel a set of classes, or undefine (set value to false) a compound class of the form alpha.beta.gamma.</p>
<dt>-p (&#8211;parse-only)</p>
<dd>Parse file and then stop. Used for checking the syntax of a program.</p>
<dt>-P (&#8211;no-processes)</p>
<dd>Do not test the existence of processes, signal processes or optionally restart them.</p>
<dt>-q (&#8211;no-splay)</p>
<dd>Switch off host splaying (sleeping).</p>
<dt>-s (&#8211;no-commands)</p>
<dd>Do not execute scripts or shell commands.</p>
<dt>-S (&#8211;silent)</p>
<dd>Silence run time warnings.</p>
<dt>-t (&#8211;no-tidy)</p>
<dd>Do not tidy file systems.</p>
<dt>-u (&#8211;use-env)</p>
<dd>Causes <code>cfagent</code> to generate an environment variable CFALLCLASSES which can be read by child processes (scripts). This variable contains a summary of all the currently defined classes at any given time. This option causes some system 5 systems to generate a Bus Error or segmentation fault.</p>
<dt>-U (&#8211;underscore-classes)</p>
<dd>When this option is set, <code>cfagent</code> adds an underscore to the beginning of all hard system classes (like _sun4, _linux etc.) This can be used to avoid naming conflicts if you are so injudicious as to name a host by the name of a hard class. Other classes are not affected.</p>
<dt>-v (&#8211;verbose)</p>
<dd>Verbose mode. Prints detailed information about actions and state.</p>
<dt>-V (&#8211;version)</p>
<dd>Print only the version string and then quit.</p>
<dt>-x (&#8211;no-preconf)</p>
<dd>Do not execute the cf.preconf net configuration file.</p>
<dt>-X (&#8211;no-links)</p>
<dd>Do not execute the links section of a program.</p>
<dt>-w (&#8211;no-warn,&#8211;quiet)</p>
<dd>Do not print warning messages.</dl>
<h2>Author</h2>
<p>Mark Burgess, Oslo University College</p>
<h2>Information</h2>
<p><a rel="nofollow" href="http://www.cfengine.org">http://www.cfengine.org</a></p>
