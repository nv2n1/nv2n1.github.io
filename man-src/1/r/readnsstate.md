---
title: "readnsstate(1)"
name: "readnsstate"
section: "1"
letter: "r"
url: "/docs/linux/man/1-readnsstate/"
description: "readnsstate – interpret the contents of cn=replica’s nsState value readnsstate /etc/dirsrv/slapd-INSTANCE/dse.ldif"
---

<h2>NAME</h2>
<p> readnsstate &#8211; interpret the contents of cn=replica&#8217;s nsState value <code>readnsstate</code> /etc/dirsrv/slapd-INSTANCE/dse.ldif </p>
<h2>DESCRIPTION</h2>
<p> Decode and display the content of the nsState attribute from a directory servers cn=replicate object. </p>
<h2>EXAMPLES</h2>
<pre>
<dl><dt><dd>sudo /usr/bin/readnsstate /etc/dirsrv/slapd-localhost/dse.ldif
</dl>
</pre>
<pre>
<dl><dt><dd>For replica cn=replica,cn=dc3Dexample2Cdc3Dcom,cn=mapping tree,cn=config
  fmtstr=[H6x3QH6x]
  size=40
  len of nsstate is 40
  CSN generator state:
    Replica ID    : 5
    Sampled Time  : 1463100468
    Gen as csn    : 57352434000000050000
    Time as str   : Fri May 13 10:47:48 2016
    Local Offset  : 0
    Remote Offset : 276
    Seq. num      : 0
    System time   : Fri May 13 14:01:25 2016
    Diff in sec.  : 11617
    Day:sec diff  : 0:11617
</dl>
</pre>
<h2>AUTHOR</h2>
<p> readnsstate was written by the 389 Project by richm.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to <a rel="nofollow" href="https://fedorahosted.org/389/newticket.">https://fedorahosted.org/389/newticket.</a></p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2016 Red Hat, Inc.<br />
 This manual page was written by William Brown &lt;wibrown [at] redhat.com&gt;, for the 389 Directory Server Project.<br />
 This is free software. You may redistribute copies of it under the terms of the Directory Server license found in the LICENSE file of this software distribution. </p>
<h2>Index</h2>
