---

title: "twintro(8)"
name: "twintro"
section: "8"
letter: "t"
url: "/docs/linux/man/8-twintro/"
---

<p> twintro &#8211; introduction to <i>Tripwire</i> software  </p>
<h2>DESCRIPTION</h2>
<p> <i>Tripwire 2.4</i> is a file integrity assessment product for Linux networks. Rather than preventing an intruder or virus from attacking system files, <i>Tripwire</i> detects intrusions when they do occur. By comparing system files and directories against a previously stored &quot;baseline&quot; database, <i>Tripwire</i> finds any additions, deletions, or changes to specified properties. This allows the system administrator to determine the extent of the problem and begin necessary damage control. </p>
<p> After <i>Tripwire</i> is installed on a system, the following four commands are used: </p>
<dl>
<dd>  </dd>
<dl>
<dt><code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8) </dt>
<dd> <p> is used for most of the basic operations of the software. This includes creation of the <i>Tripwire</i> database, and checking the integrity of the filesystem against that database. </p>
 </dd>
<dt><code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8) </dt>
<dd> <p> is used to create, encode, and sign <i>Tripwire</i> policy, configuration, and key files, and for various administrative functions. </p>
 </dd>
<dt><code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8) </dt>
<dd> <p> prints <i>Tripwire</i> database and report files in a plain text format. </p>
 </dd>
<dt><code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8) </dt>
<dd> <p> is a file utility that displays hash values for files. </p>
 </dd></dl>
</dl>
<p> In addition to the command references listed above, the following three man pages provide information on important components of the <i>Tripwire</i> package. </p>
<dl>
<dd>  </dd>
<dl>
<dt><code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </dt>
<dd> <p> provides an overview of the various files created and used by <i>Tripwire</i>, including default locations and settings. </p>
 </dd>
<dt><code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4) </dt>
<dd> <p> explains the configuration file, which is used to set system-specific information that affects <i>Tripwire</i> operation. </p>
 </dd>
<dt><code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4) </dt>
<dd> <p> explains the policy file, which specifies the files and directories <i>Tripwire</i> should check, and how they should be scanned. </p>
 </dd></dl>
</dl>
<p> Using the <code>--help</code> flag with any <i>Tripwire</i> command (e.g.&nbsp;<wbr><code>tripwire --help</code>) will print a short summary of the command modes for that command. If a mode selector is also specified (e.g.&nbsp;<wbr><code>tripwire --check --help</code>), a mode-specific usage message will be displayed. Using the <code>all</code> argument with the <code>--help</code> flag (e.g.&nbsp;<wbr><code>tripwire --help all</code>) will print detailed usage messages for all modes of the specified command.  </p>
<h2>VERSION INFORMATION</h2>
<p> This man page describes <i>Tripwire 2.4</i>.  </p>
<h2>AUTHORS</h2>
<p> Tripwire, Inc.  </p>
<h2>COPYING PERMISSIONS</h2>
<p> Permission is granted to make and distribute verbatim copies of this man page provided the copyright notice and this permission notice are preserved on all copies. </p>
<p> Permission is granted to copy and distribute modified versions of this man page under the conditions for verbatim copying, provided that the entire resulting derived work is distributed under the terms of a permission notice identical to this one. </p>
<p> Permission is granted to copy and distribute translations of this man page into another language, under the above conditions for modified versions, except that this permission notice may be stated in a translation approved by Tripwire, Inc. </p>
<p> Copyright 2000-2017 Tripwire, Inc. Tripwire is a registered trademark of Tripwire, Inc. in the United States and other countries. All rights reserved.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/8-tripwire/">tripwire</a></code>(8), <code><a href="/docs/linux/man/8-twadmin/">twadmin</a></code>(8), <code><a href="/docs/linux/man/8-twprint/">twprint</a></code>(8), <code><a href="/docs/linux/man/8-siggen/">siggen</a></code>(8), <code><a href="/docs/linux/man/4-twconfig/">twconfig</a></code>(4), <code><a href="/docs/linux/man/4-twpolicy/">twpolicy</a></code>(4), <code><a href="/docs/linux/man/5-twfiles/">twfiles</a></code>(5) </p>
<p> <i>The Design and Implementation of Tripwire: A </i><i>UNIX</i><i> File Integrity Checker</i>by <i>Gene</i>Kim <i>and</i>Eugene <i>Spafford.</i>Purdue <i>Technical</i>Report <i>CSD-TR-93-071.</i> </p>
