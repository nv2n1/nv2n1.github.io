---
title: "func-inventory(1)"
name: "func-inventory"
section: "1"
letter: "f"
url: "/docs/linux/man/1-func-inventory/"
---

<h2>NAME</h2>

 func-inventory -- Takes inventory of data from func minions, and stores them in git.

<h2>SYNOPSIS</h2>

 func-inventory [--verbose] [--server-spec glob] [--methods list] [--modules list] [--tree path] [--no-git]

<h2>DESCRIPTION</h2>

 func-inventory runs against func-minions to gather information, and stores this information on the filesystem, in a tree arranged by hostname, module name, and method name. 

 After each update, differences are commited to version control (using git), where they can be examined with tools such as ``git log'' and ``gitk''.

<h2>--verbose</h2>

 Provides extra output about what func-inventory is doing.

<h2>--server-spec</h2>

 A glob, as can be given to ``func'', that describes what machines the inventory program should run against. The default is ``*''.

<h2>--modules list</h2>

 A comma-seperated list of modules that should be included in the inventory, for instance ``hardware,packages''. The default is ``all''.

<h2>--methods list</h2>

 A comma-seperated list of methods that should be included in the inventory, for each module being queried. The default is ``info'', which saves the data for any module that has an ``info'' method.

<h2>--tree-path</h2>

 Selects the location where func-inventory will output data. The default is /var/lib/func/inventory. This directory will contain a tree structure based on the hostnames, modules, and methods included in the inventory.

<h2>--no-git</h2>

 Disables git integration, meaning changes will not be tracked using version control. This option is present for those that do not have the ``git-core'' package installed, though installing it is highly recommended to get the full degree of power out of func-inventory.

<h2>VIEWING CHANGES</h2>

 Since func-inventory integrates with git, all changes to the remote systems (including additions of new systems) can be tracked using standard git-tools such as ``git log'' and ``gitk'', when run on the directory specified for --tree. 

 Additional built in hooks to notify changes can be written using git's own trigger mechanism, though something more specific to func will likely be developed in the future --- also eliminating the need to grok git internals.

<h2>ALTERNATIVE OUTPUT FORMATS</h2>

 func-inventory can be passed a --json or --xmlrpc parameter to override the default output format. These output formats are much less readable in the git-produced diffs, but are more easily loaded by other programs that may want to ``mine'' the output of a func-inventory tree. Using --json requires that the python-simplejson <font SIZE="-1">RPM</font> be installed.

<h2>ADDITONAL RESOURCES</h2>

 See <a rel="nofollow" HREF="https://fedorahosted.org/func/">https://fedorahosted.org/func/</a> for more information. 

 See also the manpages for ``func'', ``funcd'', ``certmaster'', ``certmaster-ca'', and ``func-transmit''.

<h2>AUTHOR</h2>

 Michael DeHaan &lt;mdehaan [at] redhat.com&gt; 

<h2>Index</h2>


