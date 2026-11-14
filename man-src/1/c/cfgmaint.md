---
title: "cfgmaint(1)"
name: "cfgmaint"
section: "1"
letter: "c"
url: "/docs/linux/man/1-cfgmaint/"
---

<h2 class="name">NAME</h2>
 

 cfgmaint - configuration tool for Visual Builder 

<h2>SYNTAX</h2>

 cfgmaint [ -rbxop ] command object [ parameters ]

<h2>DESCRIPTION</h2>

 Maintains widget palette configuration for the Visual Builder. It can be stored in the system-wide and the local user config files. <tt>&quot;cfgmaint&quot;</tt> allows adding, renaming, moving, and deleting the classes and pages in the Visual Builder widget palette.

<h2>USAGE</h2>

 <tt>&quot;cfgmaint&quot;</tt> is invoked with <tt>&quot;command&quot;</tt> and <tt>&quot;object&quot;</tt> arguments, where <tt>&quot;command&quot;</tt> defines the action to be taken, and <tt>&quot;object&quot;</tt> - the object to be handled.

<h3>Options</h3>

<dl>
<dt>-r
<dd> Write configuration to the system-wide config file
<dt>-b
<dd> Read configuration from both system-wide and user config files
<dt>-x
<dd> Do not write backups
<dt>-o
<dd> Read-only mode
<dt>-p
<dd> Execute <tt>&quot;use Prima;&quot;</tt> code before start. This option might be necessary when adding a module that relies on the toolkit but does not invoke the code itself.</dl>

<h3>Objects</h3>

<dl>
<dt>m
<dd> Selects a module. Valid for add, list, and remove commands.
<dt>p
<dd> Selects a page. Valid for all commands.
<dt>w
<dd> Selects a widget. Valid for list, remove, rename, and move commands.</dl>

<h3>Commands</h3>

<dl>
<dt>a
<dd> Adds a new object to the configuration. Can be either a page or a module.
<dt>d
<dd> Removes an object.
<dt>l
<dd> Prints object name. In case object is a widget, prints all registered widgets. If the string is specified as an additional parameter, it is treated as a page name and only widgets from the page are printed.
<dt>r
<dd> Renames an object to a new name, which is passed as additional parameter. Can be either a widget or a page.
<dt>m
<dd> If <tt>&quot;object&quot;</tt> is a widget, relocates one or more widgets to a new page. If <tt>&quot;object&quot;</tt> is a page, moves the page before the page specified as an additional parameter, or to the end if no additional page specified.</dl>

<h2>EXAMPLE</h2>

 Add a new module to the system-wide configuration: 

 <pre>
        cfgmaint -r a m CPAN/Prima/VB/New/MyCtrls.pm
</pre> 

 List widgets, present in both config files: 

 <pre>
        cfgmaint -b l w
</pre> 

 Rename a page: 

 <pre>
        cfgmaint r p General Basic
</pre>

<h2>FILES</h2>

 <i>Prima/VB/Config.pm</i>, <i>~/.prima/vbconfig</i>

<h2>AUTHOR</h2>

 Dmitry Karasik, &lt;dmitry [at] karasik.eu.org&gt;.

<h2>SEE ALSO</h2>

 <font SIZE="-1">VB</font>, Prima::VB::CfgMaint 

<h2>Index</h2>


