---
title: "l2tp-secrets(5)"
name: "l2tp-secrets"
section: "5"
letter: "l"
url: "/docs/linux/man/5-l2tp-secrets/"
---

l2tp-secrets - L2TPD secrets file

<h2>Description</h2>

The l2tp-secrets file contains challenge-response authentication information for xl2tpd, the implementation of l2tp protocol. The format of the file is derived from the pap and chap secrets file format used in pppd. The secrets file is composed of zero or more lines with 3 fields each. Each line represents an authentication secret. The 3 fields represent our hostname, the remote hostname and the secret used in the authentication process. The first field is for our hostname, a &quot;*&quot; may be used as a wildcard. The second field is for the remote system's hostname. Again, a &quot;*&quot; may be used as a wildcard. The third field is the secret used if the previous two fields match the hostnames of the systems involved. The secret should, ideally, be at 16 characters long (the length of an MD5 digest output), and should probably be longer to ensure sufficient security. There is no minimum length requirement, however. 

<h2>Files</h2>

/etc/xl2tpd/xl2tpd.conf /etc/xl2tpd/l2tp-secrets /var/run/xl2tpd/l2tp-control

<h2>Bugs</h2>

Please address bugs and comment to xl2tpd [at] lists.xelerance.com

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-xl2tpd/">xl2tpd</a>(8) <a HREF="/docs/linux/man/5-xl2tpd-conf/">xl2tpd.conf</a>(5)

<h2>Authors</h2>

Michael Richardson &lt;mcr [at] xelerance.com&gt; Paul Wouters &lt;paul [at] xelerance.com&gt; 

 Patched contributed by: 
&nbsp;<wbr>&nbsp;<wbr>Jacco de Leeuw&nbsp;<wbr>&lt;jacco2 [at] dds.nl&gt; 
&nbsp;<wbr>&nbsp;<wbr>Cedric Schieli&nbsp;<wbr>&lt;cschieli [at] gmail.com&gt; 

 Previous development was hosted at sourceforge (<a rel="nofollow" HREF="http://www.sourceforge.net/projects/l2tpd)">http://www.sourceforge.net/projects/l2tpd)</a> by: 

 Scott Balmos &lt;sbalmos [at] iglou.com&gt; 
 David Stipp &lt;dstipp [at] one.net&gt; 
 Jeff McAdams &lt;jeffm [at] iglou.com&gt; 

 

 Based off of l2tpd version 0.60 
 Copyright (C)1998 Adtran, Inc. 
 Mark Spencer &lt;markster [at] marko.net&gt;
