---
title: "dbgen-pl(1)"
name: "dbgen-pl"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbgen-pl/"
description: "dbgen.pl – Random LDIF database creator"
---

<p>dbgen.pl &#8211; Random LDIF database creator </p>
<h2>Synopsis</h2>
<p><code>dbgen.pl</code> [<i>OPTIONS</i>] -o output_file -n number</p>
<h2>Description</h2>
<p>Random LDIF database creator. Used to generate large LDIF files for use in testing the Directory Server. </p>
<h2>Options</h2>
<p>A summary of options is included below:</p>
<dl>
<dt><code>-v </code></p>
<dd>Verbose output</p>
<dt><code>-q</code></p>
<dd>Quiet output</p>
<dt><code>-s suffix </code></p>
<dd>LDAP suffix. Default is &#8216;dc=example,dc=com&#8217;</p>
<dt><code>-c CN naming style</code></p>
<dd>Naming style for RDN&#8217;s. Default is UID</p>
<dt><code>-O organizationalPersons</code></p>
<dd>Organizationalpersons objectClass. Default is inetOrgPerson.</p>
<dt><code>-p piranha style ACI</code></p>
<dd>Piranha style aci. Default is barracua</p>
<dt><code>-r seed</code></p>
<dd>Seed number for random number generator</p>
<dt><code>-g</code></p>
<dd>Print extra entries for orgchart</p>
<dt><code>-x</code></p>
<dd>Suppress printing of the preamble</p>
<dt><code>-y</code></p>
<dd>Suppress printing of Organizational Units</p>
<dt><code>-l</code></p>
<dd>Location of directory containing data files, default is /usr/share/dirsrv/data</p>
<dt><code>-n number</code></p>
<dd>Number of entries to be generated</p>
<dt><code>-b number</code></p>
<dd>Beginning number for RDN e.g. uid=1 (ending number is -n value + beginning number)</p>
<dt><code>-j number</code></p>
<dd>0 pad numbers used in RDN to this many digits e.g. with 4 1 becomes 0001 (ignored unless -b number is specified)</p>
<dt><code>-u</code></p>
<dd>Add groups containing uniquemembers; generate a group for every 100 user entries created that contains the 100 members
</dl>
<h2>Author</h2>
<p>dbgen.pl was written by the 389 Project.</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>Copyright</h2>
<p>Copyright &#169; 2001 Sun Microsystems, Inc. Used by permission.<br />
 Copyright &#169; 2008 Red Hat, Inc.<br />
 This manual page was written by Michele Baldessari &lt;michele [at] pupazzo.org&gt;, for the Debian project (but may be used by others).<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. This license is essentially the GNU General Public License version 2 with an exception for plug-in distribution.</p>
