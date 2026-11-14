---
title: "qconf(1)"
name: "qconf"
section: "1"
letter: "q"
url: "/docs/linux/man/1-qconf/"
description: "qconf – xxQS_NAMExx Queue Configuration"
---

<h2 class="name">NAME</h2>
<p> qconf &#8211; xxQS_NAMExx Queue Configuration </p>
<h2>SYNTAX</h2>
<p> <code>qconf options</code></p>
<h2>DESCRIPTION</h2>
<p> <i>Qconf</i> allows the system administrator to add, delete, and modify the current xxQS_NAMExx configuration, including queue management, host management, complex management and user management. <i>Qconf</i> also allows you to examine the current queue configuration for existing queues. </p>
<p> <i>Qconf</i> allows the use of the backslash, &#8216;\&#8217;, character at the end of a line to indicate that the next line is a continuation of the current line. When displaying settings, such as the output of one of the <code>-s</code><i>*</i> options, <i>qconf</i> will break up long lines (lines greater than 80 characters) into smaller lines using backslash line continuation where possible. Lines will only be broken up at commas or whitespace. This feature can be disabled by setting the SGE_SINGLE_LINE environment variable.</p>
<h2>OPTIONS</h2>
<p> Unless denoted otherwise, the following options and the corresponding operations are available to all users with a valid account. </p>
<dl>
<dt><code>-Aattr</code> <i>obj_spec</i> <i>fname</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add to object attributes&gt;</i></p>
<p> Similar to <code>-aattr</code> (see below) but takes specifications for the object attributes to be enhanced from file named <i>fname</i>. As opposed to <code>-aattr</code>, multiple attributes can be enhanced. Their specification has to be listed in <i>fname</i> following the file format of the corresponding object (see for the queue, for example).<br />
 Requires root or manager privileges.</p>
<dt><code>-Acal</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add calendar&gt;</i></p>
<dd> Adds a new calendar definition to the xxQS_NAMExx environment.<br />
 Calendars are used in xxQS_NAMExx for defining availability and unavailability schedules of queues. The format of a calendar definition is described in </p>
<p> The calendar definition is taken from the file <i>fname</i>. Requires root or manager privileges.</p>
<dt><code>-Ackpt</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add checkpointing environment&gt;</i></p>
<dd> Add the checkpointing environment as defined in <i>fname</i> (see<br />
 to the list of supported checkpointing environments. Requires root or manager privileges.</p>
<dt><code>-Aconf</code> <i>fname_list</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add configurations&gt;</i></p>
<dd> Add the configurations (see<br />
 specified in the files in the comma-separated <i>fname_list</i>. The configuration is added for the host that is identical to the file name.<br />
 Requires root or manager privileges.</p>
<dt><code>-Ae</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add execution host&gt;</i></p>
<dd> Add the execution host defined in <i>fname</i><br />
 to the xxQS_NAMExx cluster. The format of the execution host specification is described in Requires root or manager privileges.</p>
<dt><code>-Ahgrp</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add host group configuration&gt;</i></p>
<dd> Add the host group configuration defined in <i>file</i>.<br />
 The file format of <i>fname</i> must comply with the format specified in Requires root or manager privileges.</p>
<dt><code>-Arqs</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add RQS configuration&gt;</i></p>
<dd> Add the resource quota set (RQS) defined in the<br />
 file named <i>fname</i> to the xxQS_NAMExx cluster. Requires root or manager privileges.</p>
<dt><code>-Ap</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add PE configuration&gt;</i></p>
<dd> Add the parallel environment (PE) defined in <i>fname</i> to the xxQS_NAMExx<br />
 cluster. Requires root or manager privileges.</p>
<dt><code>-Aprj</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new project&gt;</i></p>
<dd> Adds the project description defined in<br />
 <code>fname</code> to the list of registered projects (see Requires root or manager privileges.</p>
<dt><code>-Aq</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new queue&gt;</i></p>
<dd> Add the queue defined in <i>fname</i> to the xxQS_NAMExx<br />
 cluster. Requires root or manager privileges.</p>
<dt><code>-Au</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add an ACL&gt;</i></p>
<dd> Add the user access list (ACL) defined in file<br />
 <code>fname</code> to xxQS_NAMExx. User lists are used for queue usage authentication. Requires root, manager, or operator privileges. The file format of <i>fname</i> must comply with the format specified in</p>
<dt><code>-Dattr</code> <i>obj_spec</i> <i>fname</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;del. from object attribs&gt;</i></p>
<p> Similar to <code>-dattr</code> (see below) but the definition of the list attributes from which entries are to be deleted is contained in the file named <i>fname</i>. As opposed to <code>-dattr</code>, multiple attributes can be modified. Their specification has to be listed in <i>fname</i> following the file format of the corresponding object (see for the queue, for example).<br />
 Requires root or manager privileges.</p>
<dt><code>-Mattr</code> <i>obj_spec fname obj_instance,&#8230;</i></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;mod. object attributes&gt;</i></p>
<p> Similar to <code>-mattr</code> (see below) but takes specifications for the object attributes to be modified from file named <i>fname</i>. As opposed to <code>-mattr</code>, multiple attributes can be modified. Their specification has to be listed in <i>fname</i> following the file format of the corresponding object (see for the queue, for example).<br />
 Requires root or manager privileges.</p>
<dt><code>-Mc</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify complex&gt;</i></p>
<dd> Overwrites the complex configuration with the contents of <i>fname</i>.<br />
 The argument file must comply with the format specified in Requires root or manager privileges.</p>
<dt><code>-Mcal</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify calendar&gt;</i></p>
<dd> Overwrites the calendar definition as specified in <i>fname</i>. The argument<br />
 file must comply with the format described in Requires root or manager privileges.</p>
<dt><code>-Mckpt</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify ckpt. environment&gt;</i></p>
<dd> Overwrite an existing checkpointing environment with the definitions in<br />
 <i>fname</i> (see The name attribute in <i>fname</i> has to match an existing checkpointing environment. Requires root or manager privileges.</p>
<dt><code>-Mconf</code> <i>fname_list</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify configurations&gt;</i></p>
<dd> Modify the configurations (see<br />
 specified in the files in the comma-separated <i>fname_list</i>. The configuration is modified for the host that is identical to the file name.<br />
 Requires root or manager privileges.</p>
<dt><code>-Me</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify execution host&gt;</i></p>
<dd> Overwrites the execution host configuration for the<br />
 specified host with the contents of <i>fname</i>, which must comply with the format defined in Requires root or manager privilege.</p>
<dt><code>-Mhgrp</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify host group configuration&gt;</i></p>
<dd> Allows changing the host group configuration with a single command.<br />
 All host group configuration entries contained in <code>fname</code> will be applied. Configuration entries not contained in <code>fname</code> will be deleted. The file format of <i>fname</i> must comply to the format specified in Requires root or manager privileges.</p>
<dt><code>-Mrqs</code> <i>fname [mrqs_name]</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify RQS configuration&gt;</i></p>
<dd> Same as <code>-mrqs</code> (see below) but<br />
 instead of invoking an editor to modify the RQS configuration, the file <i>fname</i> is considered to contain a changed configuration. The name of the rule set in <i>fname</i> must be the same as <code>rqs_name</code>. If <code>rqs_name</code> is not set, all rule sets are overwritten by the rule sets in <i>fname</i> Refer to for details on the RQS configuration format. Requires root or manager privileges.</p>
<dt><code>-Mp</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify PE configuration&gt;</i></p>
<dd> Same as <code>-mp</code> (see below) but<br />
 instead of invoking an editor to modify the PE configuration the file <i>fname</i> is considered to contain a changed configuration. Refer to for details on the PE configuration format. Requires root or manager privilege.</p>
<dt><code>-Mprj</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify project configuration&gt;</i></p>
<dd> Same as <code>-mprj</code> (see below) but<br />
 instead of invoking an editor to modify the project configuration the file <i>fname</i> is considered to contain a changed configuration. Refer to for details on the project configuration format. Requires root or manager privilege.</p>
<dt><code>-Mq</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify queue configuration&gt;</i></p>
<dd> Same as <code>-mq</code> (see below) but<br />
 instead of invoking an editor to modify the queue configuration the file <i>fname</i> is considered to contain a changed configuration. Refer to for details on the queue configuration format. Requires root or manager privilege.</p>
<dt><code>-Msconf</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify scheduler configuration from fname&gt;</i></p>
<dd> The current scheduler configuration (see<br />
 is overridden with the configuration specified in the file. Requires root or manager privilege.</p>
<dt><code>-Mstree </code><i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify share tree&gt;</i></p>
<dd> Modifies the definition of the share tree (see<br />
 The modified sharetree is read from file <i>fname</i>. Requires root or manager privileges.</p>
<dt><code>-Mu </code><i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify ACL&gt;</i></p>
<dd> Takes the user access list (ACL) defined in<br />
 <i>fname</i> to overwrite any existing ACL with the same name. See for information on the ACL configuration format. Requires root or manager privilege.</p>
<dt><code>-Muser </code><i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify user&gt;</i></p>
<dd> Modify the user defined in <i>fname</i><br />
 in the xxQS_NAMExx cluster. The format of the user specification is described in Requires root or manager privileges.</p>
<dt><code>-Rattr</code> <i>obj_spec</i> <i>fname</i> <i>obj_instance,&#8230;</i></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;replace object attribs&gt;</i></p>
<p> Similar to <code>-rattr</code> (see below) but the definition of the list attributes whose content is to be replaced is contained in the file named <i>fname</i>. As opposed to <code>-rattr</code>, multiple attributes can be modified. Their specification has to be listed in <i>fname</i> following the file format of the corresponding object (see for the queue, for example).<br />
 Requires root/manager privileges.</p>
<dt><code>-aattr</code> <i>obj_spec</i> <i>attr_name</i> <i>val</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add to object attributes&gt;</i></p>
<p> Allows adding specifications to a single configuration list attribute in multiple instances of an object with a single command. Currently supported object types are queues, hosts, host groups, parallel environments, resource quota sets, users, projects, calendars, and checkpointing interface configurations, specified respectively as <code>queue</code>, <code>exechost</code>, <code>hostgroup</code>, <code>pe</code>, <code>resource_quota</code>, <code>user</code>, <code>project</code>, <code>calender</code>, <code>userset</code>, or <code>ckpt</code> in <i>obj_spec</i>. For the <i>obj_spec</i> <code>queue</code> the <i>obj_instance</i> can be a cluster queue name, a queue domain name or a queue instance name. Find more information concerning different queue names in Depending on the type of the <i>obj_instance</i>, this adds to the cluster queues attribute sublist the cluster queue&#8217;s implicit default configuration value or the queue domain configuration value or queue instance configuration value. The queue <code>load_thresholds</code> parameter is an example of a list attribute. With the <code>-aattr</code> option, entries can be added to such lists, while they can be deleted with <code>-dattr</code>, modified with <code>-mattr</code>, and replaced with <code>-rattr</code>.<br />
 For the <i>obj_spec</i> <i>rqs</i> the <i>obj_instance</i> is a unique identifier for a specific rule. The identifier consists of a rule-set name and either the number of the rule in the list, or the name of the rule, separated by a &quot;/&quot;.<br />
 The name of the configuration attribute to be enhanced is specified with <i>attr_name</i> followed by <i>val</i> as a <i>name</i>=<i>value</i> pair. The space-separated list of object instances (e.g., the list of queues) to which the changes have to be applied are specified at the end of the command.<br />
 The following restriction applies: For the <i>exechost</i> object the <code>load_values</code> attribute cannot be modified (see<br />
 Requires root or manager privileges.</p>
<dt><code>-acal</code> <i>calendar_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add calendar&gt;</i></p>
<dd> Adds a new calendar definition to the xxQS_NAMExx environment.<br />
 Calendars are used in xxQS_NAMExx for defining availability and unavailability schedules of queues. The format of a calendar definition is described in </p>
<p> With the calendar name given in the option argument, <i>qconf</i> will open a temporary file and start up the text editor indicated by the environment variable EDITOR (default <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) if EDITOR is not set). After entering the calendar definition and closing the editor the new calendar is checked and registered with Requires root/manager privileges.</p>
<dt><code>-ackpt</code> <i>ckpt_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add checkpointing environment&gt;</i></p>
<dd> Adds a checkpointing environment under the name <code>ckpt_name</code> to the list<br />
 of checkpointing environments maintained by xxQS_NAMExx and to be usable to submit checkpointing jobs (see for details on the format of a checkpointing environment definition). <i>Qconf</i> retrieves a default checkpointing environment configuration and executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or $EDITOR if the EDITOR environment variable is set) to allow you to customize the checkpointing environment configuration. Upon exit from the editor, the checkpointing environment is registered with Requires root/manager privileges.</p>
<dt><code>-aconf</code> <i>host</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add configuration&gt;</i></p>
<dd> Successively adds configurations (see<br />
 For the hosts in the comma-separated host list. For each host, an editor ($EDITOR, if defined, or <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1)) is invoked and the configuration for the host can be entered. The configuration is registered with after saving the file and quitting the editor.<br />
 Requires root or manager privileges.</p>
<dt><code>-ae</code> [<i>host_template</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add execution host&gt;</i></p>
<dd> Adds a host to the list of xxQS_NAMExx execution<br />
 hosts. If a queue is configured on a host this host is automatically added to the xxQS_NAMExx execution host list. Adding execution hosts explicitly offers the advantage to be able to specify parameters like load scale values with the registration of the execution host. However, these parameters can be modified (from their defaults) at any later time via the <code>-me</code> option described below.<br />
 If the <i>host_template</i> argument is present, <i>qconf</i> retrieves the configuration of the specified execution host from or a generic template otherwise. The template is then stored in a file and <i>qconf</i> executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or the editor indicated by $EDITOR if the EDITOR environment variable is set) to change the entries in the file. The format of the execution host specification is described in When the changes are saved in the editor and the editor is quit the new execution host is registered with Requires root/manager privileges.</p>
<dt><code>-ah</code> <i>hostname,&#8230;</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add administrative host&gt;</i></p>
<dd> Adds hosts <i>hostname</i> to the xxQS_NAMExx trusted host list (a<br />
 host must be in this list to execute administrative xxQS_NAMExx commands, the sole exception to this being the execution of <i>qconf</i> on the node). The default xxQS_NAMExx installation procedures usually add all designated execution hosts (see the <code>-ae</code> option above) to the xxQS_NAMExx trusted host list automatically. Requires root or manager privileges.</p>
<dt><code>-ahgrp</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add host group configuration&gt;</i></p>
<dd> Adds a new host group with the name specified in<br />
 <i>group</i>. This command invokes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable). The new host group entry is registered after changing the entry and exiting the editor. Requires root or manager privileges.</p>
<dt><code>-arqs</code> [<i>rqs_name</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new RQS&gt;</i></p>
<dd> Adds one or more <i>Resource Quota Set</i> (RQS) description<br />
 under the names <i>rqs_name</i> to the list of RQSs maintained by xxQS_NAMExx. (See for details on the format of an RQS definition.) <i>Qconf</i> retrieves a default RQS configuration and executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or $EDITOR if the EDITOR environment variable is set) to allow you to customize the RQS configuration. Upon exit from the editor, the RQS is registered with Requires root or manager privileges.</p>
<dt><code>-am</code> <i>user</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add managers&gt;</i></p>
<dd> Adds the indicated users to the xxQS_NAMExx manager list. Requires<br />
 root or manager privileges.<br />
 Managers have full access to the xxQS_NAMExx configuration and operational features. Superusers on administration hosts have manager privileges by default.</p>
<dt><code>-ao</code> <i>user</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add operators&gt;</i></p>
<dd> Adds the indicated users to the xxQS_NAMExx operator list.<br />
 Requires root or manager privileges.<br />
 Operators have the same privileges as managers except that they cannot make configuration changes.</p>
<dt><code>-ap</code> <i>pe_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new PE&gt;</i></p>
<dd> Adds a <i>Parallel Environment</i> (PE) description<br />
 under the name <code>pe_name</code> to the list of PEs maintained by xxQS_NAMExx and to be usable to submit parallel jobs (see for details on the format of a PE definition). <i>Qconf</i> retrieves a default PE configuration and executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or $EDITOR if the EDITOR environment variable is set) to allow you to customize the PE configuration. Upon exit from the editor, the PE is registered with Requires root/manager privileges.</p>
<dt><code>-at</code> <i>thread_name</i> <i>&lt;activates thread in master&gt;</i></p>
<dd> Activates an additional thread in the master process. <i>thread_name</i> can be either &quot;scheduler&quot; or &quot;jvm&quot;. The corresponding thread is only started when it is not already running. There may be only one scheduler and only one JVM thread in the master process at the same time.</p>
<dt><code>-aprj</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new project&gt;</i></p>
<dd> Adds a project description to the list of registered projects (see<br />
 <i>Qconf</i> retrieves a template project configuration and executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or $EDITOR if the EDITOR environment variable is set) to allow you to customize the new project. Upon exit from the editor, the template is registered with Requires root or manager privileges.</p>
<dt><code>-aq</code> [<i>queue_name</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add new queue&gt;</i></p>
<dd> <i>Qconf</i> retrieves the default queue configuration (see<br />
 and executes <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) (or $EDITOR if the EDITOR environment variable is set) to allow you to customize the queue configuration. Upon exit from the editor, the queue is registered with A minimal configuration requires only that the queue name and queue hostlist be set. Requires root or manager privileges.</p>
<dt><code>-as</code> <i>hostname</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add submit hosts&gt;</i></p>
<dd> Add hosts <code>hostname</code> to the list of hosts allowed to<br />
 submit xxQS_NAMExx jobs and control their behavior only. Requires root or manager privileges.</p>
<dt><code>-astnode</code> <i>node_path</i><code>=</code><i>shares</i>,&#8230;<i>&lt;add share tree node&gt;</i></p>
<dd> Adds the specified share tree node(s) to the share tree (see<br />
 The <i>node_path</i> is a hierarchical path ([<code>/</code>]<i>node_name</i>[[<code>/.</code>]<i>node_name</i>&#8230;]) specifying the location of the new node in the share tree. The base name of the node_path is the name of the new node. The node is initialized to the number of specified shares. Requires root or manager privileges.</p>
<dt><code>-astree</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add share tree&gt;</i></p>
<dd> Adds the definition of a share tree to the system (see<br />
 A template share tree is retrieved and an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) is invoked for modifying the share tree definition. Upon exiting the editor, the modification is registered with Requires root or manager privileges.</p>
<dt><code>-Astree</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add share tree&gt;</i></p>
<dd> Adds the definition of a share tree to the system (see<br />
 from the file <i>fname</i>. Requires root or manager privileges.</p>
<dt><code>-au</code> <i>user</i>,&#8230; <i>acl_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add users to ACLs&gt;</i></p>
<dd> Adds users to xxQS_NAMExx user access lists (ACLs). User lists<br />
 are used for queue usage authentication. Requires root/manager/operator privileges.<br />
 Users can submit jobs and run them if they have access to a submit host and and execution host, but cannot affect the xxQS_NAMExx configuration or operation (other than altering or deleting their own jobs).</p>
<dt><code>-Auser</code> <i>fname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add user&gt;</i></p>
<dd> Add the user defined in <i>fname</i><br />
 to the xxQS_NAMExx cluster. The format of the user specification is described in Requires root or manager privileges.</p>
<dt><code>-auser</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;add user&gt;</i></p>
<dd> Adds a user to the list of registered users (see<br />
 This command invokes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) for a template user. The new user is registered after changing the entry and exiting the editor. Requires root or manager privileges.</p>
<dt><code>-bonsai</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;human-readable sharetree&gt;</i></p>
<dd> Shows a textual tree layout of the share tree analogous to the<br />
 graphical view in <code>-sstree</code> shows the same information in a less-readable (linearized) form.</p>
<dt><code>-clearusage</code> [<i>user_list</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;clear sharetree usage&gt;</i></p>
<dd> Clears usage from the sharetree, either just for <i>user_list</i> or for<br />
 all users and projects if <i>user_list</i> isn&#8217;t supplied. All specified usage will be set to zero.</p>
<dt><code>-cq</code> <i>wc_queue_list</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;clean queue&gt;</i></p>
<dd> Cleans queue of jobs which haven&#8217;t been reaped. (Actually purges jobs<br />
 remaining on the queue.) Primarily a development tool. Requires root/manager/operator privileges. Find a description of <i>wc_queue_list</i> in</p>
<dt><code>-dattr</code> <i>obj_spec</i> <i>attr_name</i> <i>val</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete in object attribs&gt;</i></p>
<p> Allows deleting specifications in a single configuration list attribute in multiple instances of an object with a single command. Find more information concerning <i>obj_spec</i> and <i>obj_instance</i> in the description of <code>-aattr</code>.</p>
<dt><code>-dcal</code> <i>calendar_name</i>,&#8230;<i>&lt;delete calendar&gt;</i></p>
<dd> Deletes the specified calendar definition from xxQS_NAMExx. Requires<br />
 root/manager privileges.</p>
<dt><code>-dckpt</code> <i>ckpt_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete checkpointing environment&gt;</i></p>
<dd> Deletes the specified checkpointing environment. Requires root/manager<br />
 privileges.</p>
<dt><code>-dconf</code> <i>host</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete local configuration&gt;</i></p>
<dd> The local configuration entries for the specified hosts are deleted<br />
 from the configuration list. Requires root or manager privilege.</p>
<dt><code>-de</code> <i>host_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete execution host&gt;</i></p>
<dd> Deletes hosts from the xxQS_NAMExx execution host list.<br />
 Requires root or manager privileges.</p>
<dt><code>-dh</code> <i>host_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete administrative host&gt;</i></p>
<dd> Deletes hosts from the xxQS_NAMExx trusted host list. The host on which<br />
 is currently running cannot be removed from the list of administrative hosts. Requires root or manager privileges.</p>
<dt><code>-dhgrp</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete host group configuration&gt;</i></p>
<dd> Deletes host group configuration with the name specified in<br />
 <code>group.</code> Requires root or manager privileges.</p>
<dt><code>-drqs</code> <i>rqs_name_list</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete RQS&gt;</i></p>
<dd> Deletes the specified resource quota sets (RQS).<br />
 Requires root or manager privileges.</p>
<dt><code>-dm</code> <i>user</i>[,<i>user</i>,&#8230;]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete managers&gt;</i></p>
<dd> Deletes managers from the manager list.<br />
 Requires root or manager privileges. It is not possible to delete the admin user or the user root from the manager list.</p>
<dt><code>-do</code> <i>user</i>[,<i>user</i>,&#8230;]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete operators&gt;</i></p>
<dd> Deletes operators from the operator list.<br />
 Requires root or manager privileges. It is not possible to delete the admin user or the user root from the operator list.</p>
<dt><code>-dp</code> <i>pe_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete parallel environment&gt;</i></p>
<dd> Deletes the specified parallel environment (PE).<br />
 Requires root or manager privileges.</p>
<dt><code>-dprj</code> <i>project</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete projects&gt;</i></p>
<dd> Deletes the specified project(s). Requires root/manager privileges.</p>
<dt><code>-dq</code> <i>queue_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete queue&gt;</i></p>
<dd> Removes the specified queue(s), which must be empty.<br />
 Requires root or manager privileges.</p>
<dt><code>-ds</code> <i>host_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete submit host&gt;</i></p>
<dd> Deletes hosts from the xxQS_NAMExx submit host list.<br />
 Requires root or manager privileges.</p>
<dt><code>-dstnode</code> <i>node_path</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete share tree node&gt;</i></p>
<dd> Deletes the specified share tree node(s).<br />
 The <i>node_path</i> is a hierarchical path ([<code>/</code><i>]node_name</i>[[<code>/.</code><i>]node_name</i>&#8230;]) specifying the location of the node to be deleted in the share tree. Requires root or manager privileges.</p>
<dt><code>-dstree</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete share tree&gt;</i></p>
<dd> Deletes the current share tree. Requires root or manager privileges.</p>
<dt><code>-du</code> <i>user</i>,&#8230; <i>acl_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete users from ACL&gt;</i></p>
<dd> Deletes one or more users from one or more xxQS_NAMExx user<br />
 access lists (ACLs). Requires root/manager/operator privileges.</p>
<dt><code>-dul</code> <i>acl_name</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete user lists&gt;</i></p>
<dd> Deletes one or more user lists from the system.<br />
 Requires root/manager/operator privileges.</p>
<dt><code>-duser</code> <i>user</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;delete users&gt;</i></p>
<dd> Deletes the specified user(s) from the list of registered users.<br />
 Requires root or manager privileges.</p>
<dt><code>-help</code></p>
<dd> Prints a listing of all options.</p>
<dt><code>-k</code>{<code>m</code>|<code>s</code>|<code>e</code>[<code>j</code>] {<i>host</i>,&#8230;|<code>all</code>}}<tt>&nbsp;</tt><i>&lt;shutdown xxQS_NAMExx&gt;</i></p>
<dd> <code>Note:</code> The <code>-ks</code> switch is deprecated and may be removed in future release.<br />
 Please use the <code>-kt</code> switch instead.<br />
 Used to shutdown xxQS_NAMExx components (daemons). In the form <code>-km</code> is forced to terminate in a controlled fashion. In the same way the <code>-ks</code> switch causes termination of the scheduler thread. Shutdown of running processes currently registered is initiated by the <code>-ke</code> option. If <code>-kej</code> is specified instead, all jobs running on the execution hosts are aborted prior to termination of the corresponding The comma-separated host list specifies the execution hosts to be addressed by the <code>-ke</code> and <code>-kej</code> option. If the keyword <code>all</code> is specified instead of a host list, all running processes are shutdown. Job abortion, initiated by the <code>-kej</code> option will result in <code>dr</code> state for all running jobs until is running again.<br />
 Requires root or manager privileges.</p>
<dt><code>-kt</code> <i>thread_name</i> <i>&lt;terminate master thread&gt;</i></p>
<dd> Terminates a thread in the master process. Currently it is only supported to shutdown the &quot;scheduler&quot; and the &quot;jvm&quot; thread. The command will only be successful if the corresponding thread is running.</p>
<dt><code>-kec</code> {<i>id</i>,&#8230;|<code>all</code>}<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;kill event client&gt;</i></p>
<dd> Used to shutdown event clients registered at<br />
 The comma-separated event client list specifies the event clients to be addressed by the <code>-kec</code> option. If the keyword <code>all</code> is specified instead of an event client list, all running event clients except special clients like the scheduler thread are terminated. Requires root or manager privilege.</p>
<dt><code>-mattr</code> <i>obj_spec</i> <i>attr_name</i> <i>val</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify object attributes&gt;</i></p>
<p> Allows changing a single configuration attribute in multiple instances of an object with a single command. Find more information concerning <i>obj_spec</i> and <i>obj_instance</i> in the description of <code>-aattr</code>.</p>
<dt><code>-mc</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify complex&gt;</i></p>
<dd> The complex configuration (see<br />
 is retrieved, an editor is executed (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) and the changed complex configuration is registered with upon exit of the editor. Requires root or manager privilege.</p>
<dt><code>-mcal</code> <i>calendar_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify calendar&gt;</i></p>
<dd> The specified calendar definition (see<br />
 is retrieved, an editor is executed (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) and the changed calendar definition is registered with upon exit of the editor. Requires root or manager privilege.</p>
<dt><code>-mckpt</code> <i>ckpt_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify checkpointing environment&gt;</i></p>
<dd> Retrieves the current configuration for the specified checkpointing<br />
 environment, executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the new configuration with the Refer to for details on the checkpointing environment configuration format. Requires root or manager privilege.</p>
<dt><code>-mconf</code> [<i>host</i>,&#8230;|<code>global</code>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify configuration&gt;</i></p>
<dd> The configuration for the specified host<br />
 is retrieved, an editor is executed (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) and the changed configuration is registered with upon exit of the editor. If the optional <i>host</i> argument is omitted, or if the special host name <code>global</code> is specified, the global configuration is modified. The format of the configuration is described in<br />
 Requires root or manager privilege.</p>
<dt><code>-me</code> <i>hostname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify execution host&gt;</i></p>
<dd> Retrieves the current configuration for the specified execution host,<br />
 executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the changed configuration with upon exit from the editor. The format of the execution host configuration is described in Requires root or manager privilege.</p>
<dt><code>-mhgrp</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify host group configuration&gt;</i></p>
<dd> The host group entries for the host group specified in<br />
 <code>group</code> are retrieved and an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) is invoked for modifying the host group configuration. By closing the editor, the modification is registered. The format of the host group configuration is described in Requires root or manager privileges.</p>
<dt><code>-mrqs</code> [<i>rqs_name</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify RQS configuration&gt;</i></p>
<dd> Retrieves the resource quota set (RQS)configuration defined in <i>rqs_name</i>,<br />
 or if <i>rqs_name</i> is not given, retrieves all resource quota sets, executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the new configuration with the Refer to for details on the RQS configuration format. Requires root or manager privilege.</p>
<dt><code>-mp</code> <i>pe_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify PE configuration&gt;</i></p>
<dd> Retrieves the current configuration for the specified<br />
 <i>parallel environment</i> (PE), executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the new configuration with the Refer to for details on the PE configuration format. Requires root or manager privilege.</p>
<dt><code>-mprj</code> <i>project</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify project&gt;</i></p>
<dd> Data for the specific project is retrieved (see<br />
 and an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) is invoked for modifying the project definition. Upon exiting the editor, the modification is registered. Requires root or manager privileges.</p>
<dt><code>-mq</code> <i>queuename</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify queue configuration&gt;</i></p>
<dd> Retrieves the current configuration for the specified queue,<br />
 executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the new configuration with the Refer to for details on the queue configuration format. Requires root or manager privilege.</p>
<dt><code>-msconf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify scheduler configuration&gt;</i></p>
<dd> The current scheduler configuration (see<br />
 is retrieved, an editor is executed (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) and the changed configuration is registered with upon exit of the editor. Requires root or manager privilege.</p>
<dt><code>-mstnode</code> <i>node_path</i><code>=</code><i>shares</i>,&#8230;<i>&lt;modify share tree node&gt;</i></p>
<dd> Modifies the specified share tree node(s) in the share tree (see<br />
 The <i>node_path</i> is a hierarchical path ([fB/]<i>node_name</i>[[<code>/.</code>]<i>node_name</i>&#8230;]) specifying the location of an existing node in the share tree. The node is set to the number of specified <i>shares</i>. Requires root or manager privileges.</p>
<dt><code>-mstree</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify share tree&gt;</i></p>
<dd> Modifies the definition of the share tree (see<br />
 The present share tree is retrieved and an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by $EDITOR) is invoked for modifying the share tree definition. Upon exiting the editor, the modification is registered with Requires root or manager privileges.</p>
<dt><code>-mu</code> <i>acl_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify user access lists&gt;</i></p>
<dd> Retrieves the current configuration for the specified user access list,<br />
 executes an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) and registers the new configuration with the The format of the configuration must comply with the format specified in Requires root or manager privilege.</p>
<dt><code>-muser</code> <i>user</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;modify user&gt;</i></p>
<dd> Data for the specific user is retrieved (see<br />
 and an editor (either <i><a href="/docs/linux/man/1-vi/">vi</a></i>(1) or the editor indicated by the EDITOR environment variable) is invoked for modifying the user definition. Upon exiting the editor, the modification is registered. Requires root or manager privileges.</p>
<dt><code>-purge</code> <i>queue</i> <i>attr_nm</i>,&#8230; <i>obj_spec</i></p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;purge divergent attribute settings&gt;</i></p>
<p> Delete the values of the attributes defined in <i>attr_nm</i> from the object defined in <i>obj_spec</i>. <i>obj_spec</i> can be &quot;queue_instance&quot; or &quot;queue_domain&quot;. The names of the attributes are described in<br />
 This operation only works on a single queue instance or domain. It cannot be used on a cluster queue. In the case where the <i>obj_spec</i> is &quot;queue@@hostgroup&quot;, the attribute values defined in <i>attr_nm</i> which are set for the indicated hostgroup are deleted, but not those which are set for the hosts contained by that hostgroup. If the <i>attr_nm</i> is &#8216;<code>*</code>&#8216;, all attribute values set for the given queue instance or domain are deleted.<br />
 The main difference between <code>-dattr</code> and <code>-purge</code> is that <code>-dattr</code> removes a value from a single list attribute, whereas <code>-purge</code> removes one or more overriding attribute settings from a cluster queue configuration. With <code>-purge</code>, the entire attribute is deleted for the given queue instance or queue domain.</p>
<dt><code>-rattr</code> <i>obj_spec</i> <i>attr_name</i> <i>val</i> <i>obj_instance</i>,&#8230;</p>
<dd> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;replace object attributes&gt;</i></p>
<p> Allows replacing a single configuration list attribute in multiple instances of an object with a single command. Find more information concerning <i>obj_spec</i> and <i>obj_instance</i> in the description of <code>-aattr</code>.<br />
 Requires root or manager privilege.</p>
<dt><code>-rsstnode</code> <i>node_path</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show share tree node&gt;</i></p>
<dd> Recursively shows the name and shares of the specified share tree node(s)<br />
 and the names and shares of its child nodes (not showing leaves). See The <i>node_path</i> is a hierarchical path ([<code>/</code>]<i>node_name</i>[{<code>/</code>|<code>.</code>}<i>node_name</i>&#8230;]) specifying the location of a node in the share tree.</p>
<dt><code>-sc</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show complexes&gt;</i></p>
<dd> Display the complex configuration.</p>
<dt><code>-scal</code> <i>calendar_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show calendar&gt;</i></p>
<dd> Display the configuration of the specified calendar. </p>
<dt><code>-scall</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show calendar list&gt;</i></p>
<dd> Show a list of all calendars currently defined. </p>
<dt><code>-sckpt</code> <i>ckpt_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show checkpointing environment&gt;</i></p>
<dd> Display the configuration of the specified checkpointing environment.</p>
<dt><code>-sckptl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show checkpointing environment list&gt;</i></p>
<dd> Show a list of the names of all checkpointing environments currently<br />
 configured.</p>
<dt><code>-sconf</code> [<i>host</i>,&#8230;|<code>global</code>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show configuration&gt;</i></p>
<dd> Print the global or local (host specific) configuration.<br />
 If the optional comma-separated host list argument is omitted, or the special string <code>global</code> is given, the global configuration is displayed. The configuration in effect on a certain host is the merger of the global configuration and the host specific local configuration. The format of the configuration is described in</p>
<dt><code>-sconfl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show configuration list&gt;</i></p>
<dd> Display a list of hosts for which configurations are<br />
 available. The special host name <code>global</code> refers to the global configuration.</p>
<dt><code>-sds</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show detached settings&gt;</i></p>
<dd> Displays detached settings in the cluster configuration (see</p>
<dt><code>-se</code> <i>hostname</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show execution host&gt;</i></p>
<dd> Displays the definition of the specified execution host.</p>
<dt><code>-sel</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show execution hosts&gt;</i></p>
<dd> Displays the xxQS_NAMExx execution host list.</p>
<dt><code>-secl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show event clients&gt;</i></p>
<dd> Displays the xxQS_NAMExx event client list.</p>
<dt><code>-sh</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show administrative hosts&gt;</i></p>
<dd> Displays the xxQS_NAMExx administrative host list.</p>
<dt><code>-shgrp</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show host group configuration&gt;</i></p>
<dd> Displays the host group entries for the group specified in<br />
 <i>group</i>.</p>
<dt><code>-shgrpl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show host group lists&gt;</i></p>
<dd> Displays a name list of all currently defined host groups<br />
 which have a valid host group configuration.</p>
<dt><code>-shgrp_tree</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show host group tree&gt;</i></p>
<dd> Shows a tree like structure of the host group.</p>
<dt><code>-shgrp_resolved</code> <i>group</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show host group hosts&gt;</i></p>
<dd> Shows a list of all hosts which are part of the definition of<br />
 host group. If the host group definition contains sub host groups than also these groups are resolved and the hostnames are printed.</p>
<dt><code>-srqs</code> [<i>rqs_name_list</i>]<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show RQS configuration&gt;</i></p>
<dd> Show the definition of the<br />
 resource quota sets (RQS) specified by the argument.</p>
<dt><code>-srqsl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show RQS-list&gt;</i></p>
<dd> Show a list of all currently defined<br />
 resource quota sets (RQSs).</p>
<dt><code>-sm</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show managers&gt;</i></p>
<dd> Displays the managers list.</p>
<dt><code>-so</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show operators&gt;</i></p>
<dd> Displays the operator list.</p>
<dt><code>-sobjl</code> <i>obj_spec</i> <i>attr_name</i> <i>val</i><i>&lt;show object list&gt;</i></p>
<dd> Shows a list of all configuration objects for which <i>val</i> matches at least<br />
 one configuration value of the attributes whose name matches <i>attr_name</i>. </p>
<p> <i>obj_spec</i> can be &quot;queue&quot; or &quot;queue_domain&quot; or &quot;queue_instance&quot; or &quot;exechost&quot;. Note: When &quot;queue_domain&quot; or &quot;queue_instance&quot; is specified as <i>obj_spec</i>, matching is only done with the attribute overridings concerning the host group or the execution host. In this case queue domain names resp. queue instances are returned. </p>
<p> <i>attr_name</i> can be any of the configuration file keywords listed in or Also wildcards can be used to match multiple attributes. </p>
<p> <i>val</i> can be an arbitrary string or a wildcard expression.</p>
<dt><code>-sp</code> <i>pe_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show PE configuration&gt;</i></p>
<dd> Show the definition of the<br />
 <i>parallel environment</i> (PE) specified by the argument.</p>
<dt><code>-spl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show PE-list&gt;</i></p>
<dd> Show a list of all currently defined<br />
 parallel environments (PEs).</p>
<dt><code>-sprj</code> <i>project</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show project&gt;</i></p>
<dd> Shows the definition of the specified project (see</p>
<dt><code>-sprjl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show project list&gt;</i></p>
<dd> Shows the list of all currently defined projects.</p>
<dt><code>-sq</code> <i>wc_queue_list</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt>&lt;show queues&gt;</p>
<dd> Displays one or multiple cluster queues or queue instances. A description<br />
 of <i>wc_queue_list</i> can be found in</p>
<dt><code>-sql</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show queue list&gt;</i></p>
<dd> Show a list of all currently defined cluster queues.</p>
<dt><code>-ss</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show submit hosts&gt;</i></p>
<dd> Displays the xxQS_NAMExx submit host list.</p>
<dt><code>-ssconf</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show scheduler configuration&gt;</i></p>
<dd> Displays the current scheduler configuration in the format explained in </p>
<dt><code>-sstnode</code> <i>node_path,&#8230;</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show share tree node&gt;</i></p>
<dd> Shows the name and shares of the specified share tree node(s) (see<br />
 The <i>node_path</i> is a hierarchical path ([<code>/</code>]<i>node_name</i>[{<code>/</code>|<code>.</code>}<i>node_name</i>&#8230;]) specifying the location of a node in the share tree.</p>
<dt><code>-sstree</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show share tree&gt;</i></p>
<dd> Shows the definition of the share tree (see<br />
 A different view is provided by <code>-bonsai</code>.</p>
<dt><code>-sst</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show formatted share tree&gt;</i></p>
<dd> Shows the definition of the share tree in a tree view (see</p>
<dt><code>-sss</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show scheduler status&gt;</i></p>
<dd> Currently displays the host on which the xxQS_NAMExx scheduler is<br />
 active or an error message if no scheduler is running.</p>
<dt><code>-su</code> <i>acl_name</i><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show user ACL&gt;</i></p>
<dd> Displays a xxQS_NAMExx user access list (ACL).</p>
<dt><code>-sul</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show user lists&gt;</i></p>
<dd> Displays a list of names of all currently defined<br />
 xxQS_NAMExx user access lists (ACLs).</p>
<dt><code>-suser</code> <i>user</i>,&#8230;<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show user&gt;</i></p>
<dd> Shows the definition of the specified user(s) (see</p>
<dt><code>-suserl</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;show users&gt;</i></p>
<dd> Shows the list of all currently defined users.</p>
<dt><code>-tsm</code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;</tt><i>&lt;trigger scheduler monitoring&gt;</i></p>
<dd> The xxQS_NAMExx scheduler is forced by this option to print<br />
 trace messages of its next scheduling run to the file <i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/schedd_runlog</i>. The messages indicate the reasons for jobs and queues not being selected in that run. Requires root or manager privileges. </p>
<p> Note, that the reasons for job requirements being invalid with respect to resource availability of queues are displayed using the format as described for the <code>-F</code> option (see description of <code>Full Format</code> in section <code>OUTPUT FORMATS</code> of the manual page.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>xxQS_NAME_Sxx_ROOT</code></p>
<dd> Specifies the location of the xxQS_NAMExx standard configuration files.</p>
<dt><code>xxQS_NAME_Sxx_CELL</code></p>
<dd> If set, specifies the default xxQS_NAMExx cell. To address a xxQS_NAMExx cell <i>qconf</i> uses (in the order of precedence): </p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> The name of the cell specified in the environment variable xxQS_NAME_Sxx_CELL, if it is set. </p>
<p> The name of the default cell, i.e. <code>default</code>. </p>
</dl>
</dl>
<dt><code>xxQS_NAME_Sxx_DEBUG_LEVEL</code></p>
<dd> If set, specifies that debug information should be written to stderr. In addition the level of detail in which debug information is generated is defined.</p>
<dt><code>xxQS_NAME_Sxx_QMASTER_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</p>
<dt><code>xxQS_NAME_Sxx_EXECD_PORT</code></p>
<dd> If set, specifies the tcp port on which is expected to listen for communication requests. Most installations will use a services map entry instead to define that port.</p>
<dt><code>SGE_SINGLE_LINE</code></p>
<dd> If set, indicates that long lines should not be broken up using backslashes. This setting is useful for scripts which expect one entry per line.</dl>
<h2>RESTRICTIONS</h2>
<p> Modifications to a queue configuration do not affect an active queue, taking effect on next invocation of the queue (i.e., the next job).</p>
<h2>FILES</h2>
<pre>
<i>&lt;xxqs_name_sxx_root&gt;/&lt;cell&gt;/common/act_qmaster</i>
                          xxQS_NAMExx master host file
</pre>
<h2>SEE ALSO</h2>
<h2>COPYRIGHT</h2>
<p> See for a full statement of rights and permissions. </p>
<h2>Index</h2>
