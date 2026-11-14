---
title: "yum-verify(1)"
name: "yum-verify"
section: "1"
letter: "y"
url: "/docs/linux/man/1-yum-verify/"
description: "yum verify plugin"
---

<h2>NAME</h2>
<p> yum verify plugin</p>
<h2>SYNOPSIS</h2>
<p> <code>yum</code> [options] verify [package &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> This plugin extends <code>yum</code> with some commands that give verification information on the installed system, much like rpm -V. You can change how the verification is done and which files it applies to. </p>
<p> added yum <i>command</i>s are:<br />
 <i></i> * verify<br />
 <i></i> * verify-rpm<br />
 <i></i> * verify-all </p>
<p> all of which take the same arguments as the list yum command, obviously you can only verify packages that are installed on the system. </p>
<dl>
<dt><code>verify</code></p>
<dd> Is the generic verification command, and is intended to give the most useful output. It removes all false matches due to multilib and ignores changes to configuration files by default.</p>
<dt>
<dd>
<dt><code>verify-rpm</code></p>
<dd> Is meant to be 100% compatible with rpm -V output, and any differences should be considered as bugs.</p>
<dt>
<dd>
<dt><code>verify-all</code></p>
<dd> Is used to list all the differences, including some that rpm itself will ignore.</p>
<dt>
<dd></dl>
<h2>GENERAL OPTIONS</h2>
<p> These are the options added to yum that are available in the verify commands. They are: </p>
<dl>
<dt><code>&#8211;verify-filenames</code></p>
<dd> This option is used to limit the filenames that the packages will perform verification.</p>
<dt><code>&#8211;verify-configuration-files</code></p>
<dd> This option is only useful in the generic verify command, and will enable/disable verification of files that are tagged as configuration files.</dl>
<h2>EXAMPLES</h2>
<p> To do the same as rpm -Va, use:</p>
<dl>
<dt>
<dd> yum verify-rpm</dl>
<p> To verify the packages starting with the name yum, use:</p>
<dl>
<dt>
<dd> yum verify &#8216;yum*&#8217;</dl>
<p> To verify the binaries that are in a bin directory, use:</p>
<dl>
<dt>
<dd> yum verify &#8211;verify-filenames=&#8217;*bin/*&#8217;</dl>
<p> To verify all include files, Eg. for multilib problems, use:</p>
<dl>
<dt>
<dd> yum verify-all &#8211;verify-filenames=&#8217;/usr/include/*&#8217; </p>
</dl>
<h2>SEE ALSO</h2>
<pre>
<i>yum (8)</i>
<i>yum.conf (5)</i>
<i>the verify.conf file in /etc/yum/plugins.d</i>
</pre>
<h2>AUTHORS</h2>
<pre>
James Antill &lt;james.antill [at] redhat.com&gt;.
</pre>
<h2>BUGS</h2>
<pre>
Currently yum-verify does not do verify-script checking or dependency checking,
only file checking.
Should you find any other bugs, you should first
consult the FAQ section on <a rel="nofollow" href="http://yum.baseurl.org/wiki/Faq">http://yum.baseurl.org/wiki/Faq</a> and if unsuccessful
in finding a resolution contact the mailing list: yum-devel [at] lists.baseurl.org.
To file a bug use <a rel="nofollow" href="http://bugzilla.redhat.com">http://bugzilla.redhat.com</a> for Fedora/RHEL/Centos
related bugs and <a rel="nofollow" href="http://yum.baseurl.org/report">http://yum.baseurl.org/report</a> for all other bugs.
</pre>
<h2>Index</h2>
