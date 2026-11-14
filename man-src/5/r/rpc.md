---
title: "rpc(5)"
name: "rpc"
section: "5"
letter: "r"
url: "/docs/linux/man/5-rpc/"
description: "rpc – RPC program number data base"
---

<p>rpc &#8211; RPC program number data base</p>
<h2>Synopsis</h2>
<p><code>/etc/rpc</code></p>
<h2>Description</h2>
<p>The <i>rpc</i> file contains user readable names that can be used in place of RPC program numbers. Each line has the following information: </p>
<dl>
<dt>&bull;</p>
<dd>name of server for the RPC program</p>
<dt>&bull;</p>
<dd>RPC program number</p>
<dt>&bull;</p>
<dd>aliases</dl>
<p> Items are separated by any number of blanks and/or tab characters. A &#8216;#&#8217; indicates the beginning of a comment; characters from the &#8216;#&#8217; to the end of the line are not interpreted by routines which search the file. </p>
<p> Here is an example of the <i>/etc/rpc</i> file from the Sun RPC Source distribution. </p>
<p> # # rpc 88/08/01 4.0 RPCSRC; from 1.12 88/02/07 SMI # portmapper 100000 portmap sunrpc rstatd 100001 rstat rstat_svc rup perfmeter rusersd 100002 rusers nfs 100003 nfsprog ypserv 100004 ypprog mountd 100005 mount showmount ypbind 100007 walld 100008 rwall shutdown yppasswdd 100009 yppasswd etherstatd 100010 etherstat rquotad 100011 rquotaprog quota rquota sprayd 100012 spray 3270_mapper 100013 rje_mapper 100014 selection_svc 100015 selnsvc database_svc 100016 rexd 100017 rex alis 100018 sched 100019 llockmgr 100020 nlockmgr 100021 x25.inr 100022 statmon 100023 status 100024 bootparam 100026 ypupdated 100028 ypupdate keyserv 100029 keyserver tfsd 100037 nsed 100038 nsemntd 100039</p>
<h2>Files</h2>
<dl>
<dt><i>/etc/rpc</i></p>
<dd>RPC program number data base</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-getrpcent/">getrpcent</a></code>(3)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
