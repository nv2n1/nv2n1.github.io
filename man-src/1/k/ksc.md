---
title: "ksc(1)"
name: "ksc"
section: "1"
letter: "k"
url: "/docs/linux/man/1-ksc/"
description: "ksc – Linux kernel module source checker"
---

<h2>NAME</h2>
<p> ksc &#8211; Linux kernel module source checker</p>
<h2>SYNOPSIS</h2>
<p> <code>ksc</code> [<code> -d | &#8211;directory </code>] DIRECTORY</p>
<dl>
<dt><code>ksc [ -k | &#8211;ko </code>] FILE</p>
<dd></dl>
<h2>OPTIONS</h2>
<p> KSC accepts command-line arguments, and has both a long and short form usage. You can use either style or combine them to specify options. When the tool is run with kernel module sources it checks for all four architectures, and when run with binary kernel modules, it checks for the specific architecture for which the binary was built. </p>
<dl>
<dt><code>-h</code>, <code>&#8211;help</code></p>
<dd> show this help message and exit</p>
<dt><code>-c</code> CONFIG, <code>&#8211;config</code>=<i>CONFIG</i></p>
<dd> path to the local ksc.conf file. If not specified the tool tries to read from ~/ksc.conf and if that is also not found then from /etc/ksc.conf.</p>
<dt><code>-d</code> DIRECTORY, <code>&#8211;directory</code>=<i>DIRECTORY</i></p>
<dd> path to the directory with kernel module sources.</p>
<dt><code>-i</code>, <code>&#8211;internal</code></p>
<dd> to create text files to be used internally.</p>
<dt><code>-k</code> KO, <code>&#8211;ko</code>=<i>KO</i></p>
<dd> path to the ko file. You should either use -d or -k to run the KSC tool, but not both. If both -d and -k option is used at the same time then only -d is used and the -k option is discarded.<br />
 Option -k can be specified multiple times.</p>
<dt><code>-n</code> RELEASENAME, <code>&#8211;name</code>=RELEASENAME</p>
<dd> Red Hat release against which the bug is to be filed, e.g &#8216;6.5&#8217;. Default value is 6.5.</p>
<dt><code>-p</code> PREVIOUS, <code>&#8211;previous</code>=<i>PREVIOUS</i></p>
<dd> path to the previous resultset file and submit it as a bug to Red Hat Bugzilla.</p>
<dt><code>-r</code> RELEASE, <code>&#8211;release</code>=<i>RELEASE</i></p>
<dd> RHEL whitelist release used for comparison, e.g. &#8216;6.5&#8217;.</p>
<dt><code>-y</code> SYMVERS, <code>&#8211;symvers</code>=<i>SYMVERS</i></p>
<dd> Path to the Module.symvers file. The current kernel path is used if not specified.</p>
<dt><code>-s</code>, <code>&#8211;submit</code></p>
<dd> Submits the report to the Red Hat bugzilla (<a rel="nofollow" href="https://bugzilla.redhat.com">https://bugzilla.redhat.com</a>). The credentials need to be in the /etc/ksc.conf file. The tool will prompt for bugzilla password. </p>
<dt>
<dd> <code>The configuration file looks like below:</code></p>
<dt>
<dd>
 [bugzilla]<br />
 user=user [at] redhat.com<br />
 partner=partner-name<br />
 partnergroup=partner-group<br />
 server=<a rel="nofollow" href="https://bugzilla.redhat.com/xmlrpc.cgi">https://bugzilla.redhat.com/xmlrpc.cgi</a></p>
<dt><code>-v</code>, <code>&#8211;version</code></p>
<dd> Prints KSC version number </p>
</dl>
<h2>Index</h2>
