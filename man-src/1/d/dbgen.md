---

title: "dbgen(1)"
name: "dbgen"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbgen/"
description: "dbgen.pl – Random LDIF database creator"
---

<p> dbgen.pl &#8211; Random LDIF database creator </p>
<h2>SYNOPSIS</h2>
<p> <code>dbgen.pl</code> [<i>OPTIONS</i>] -o output_file -n number</p>
<h2>DESCRIPTION</h2>
<p> Random LDIF database creator. Used to generate large LDIF files for use in testing the Directory Server. </p>
<h2>OPTIONS</h2>
<p> A summary of options is included below:</p>
<dl>
<dt><code>-v </code></dt>
<dd> Verbose output</dd>
<dt><code>-q</code></dt>
<dd> Quiet output</dd>
<dt><code>-s suffix </code></dt>
<dd> LDAP suffix. Default is &#8216;dc=example,dc=com&#8217;</dd>
<dt><code>-c CN naming style</code></dt>
<dd> Naming style for RDN&#8217;s. Default is UID</dd>
<dt><code>-O organizationalPersons</code></dt>
<dd> Organizationalpersons objectClass. Default is inetOrgPerson.</dd>
<dt><code>-p piranha style ACI</code></dt>
<dd> Piranha style aci. Default is barracua</dd>
<dt><code>-r seed</code></dt>
<dd> Seed number for random number generator</dd>
<dt><code>-g</code></dt>
<dd> Print extra entries for orgchart</dd>
<dt><code>-x</code></dt>
<dd> Suppress printing of the preamble</dd>
<dt><code>-y</code></dt>
<dd> Suppress printing of Organizational Units</dd>
<dt><code>-l</code></dt>
<dd> Location of directory containing data files, default is /usr/share/dirsrv/data</dd>
<dt><code>-n number</code></dt>
<dd> Number of entries to be generated
</dd></dl>
<h2>AUTHOR</h2>
<p> dbgen.pl was written by the 389 Project.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="http://bugzilla.redhat.com.">http://bugzilla.redhat.com.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution. </p>
