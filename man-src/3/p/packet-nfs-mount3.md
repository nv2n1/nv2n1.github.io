---
title: "packet-nfs-mount3(3)"
name: "packet-nfs-mount3"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-mount3/"
description: "packet.nfs.mount3 – MOUNTv3 decoding module"
---

<p>packet.nfs.mount3 &#8211; MOUNTv3 decoding module</p>
<h2>Classes</h2>
<h3>class DUMP3res(baseobj.BaseObj)</h3>
<pre>struct DUMP3res {
 mountentry *mountlist;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class EXPORT3res(baseobj.BaseObj)</h3>
<pre>struct EXPORT3res {
 exportnode3 *exports;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MNT3args(baseobj.BaseObj)</h3>
<pre>struct MNT3args {
 dirpath3 path;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MNT3res(baseobj.BaseObj)</h3>
<pre>union switch MNT3res (mountstat3 status) {
 case const.MNT3_OK:
 MNT3resok mountinfo;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MNT3resok(baseobj.BaseObj)</h3>
<pre>struct MNT3resok {
 fhandle3 fh;
 rpc_auth_flavors auth_flavors&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MOUNT3args(packet.utils.RPCload)</h3>
<pre>union switch MOUNT3args (mount_proc3 procedure) {
 case const.MOUNTPROC3_NULL:
 void;
 case const.MOUNTPROC3_MNT:
 MNT3args opmnt;
 case const.MOUNTPROC3_DUMP:
 void;
 case const.MOUNTPROC3_UMNT:
 UMNT3args opumnt;
 case const.MOUNTPROC3_UMNTALL:
 void;
 case const.MOUNTPROC3_EXPORT:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class MOUNT3res(packet.utils.RPCload)</h3>
<pre>union switch MOUNT3res (mount_proc3 procedure) {
 case const.MOUNTPROC3_NULL:
 void;
 case const.MOUNTPROC3_MNT:
 MNT3res opmnt;
 case const.MOUNTPROC3_DUMP:
 DUMP3res opdump;
 case const.MOUNTPROC3_UMNT:
 void;
 case const.MOUNTPROC3_UMNTALL:
 void;
 case const.MOUNTPROC3_EXPORT:
 EXPORT3res opexport;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class UMNT3args(baseobj.BaseObj)</h3>
<pre>struct UMNT3args {
 dirpath3 path;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class exportnode3(baseobj.BaseObj)</h3>
<pre>struct exportnode3 {
 dirpath3 dir;
 name3 *groups;
 exportnode3 *next;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class mount_proc3(packet.utils.Enum)</h3>
<pre>enum mount_proc3</pre>
<h3>class mountentry(baseobj.BaseObj)</h3>
<pre>struct mountentry {
 name3 hostname;
 dirpath3 directory;
 mountentry *next;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class mountstat3(packet.utils.Enum)</h3>
<pre>enum mountstat3</pre>
<h3>class rpc_auth_flavors(packet.utils.Enum)</h3>
<pre>enum rpc_auth_flavors</pre>
<h2>Functions</h2>
<h3>dirpath3(unpack)</h3>
<h3>fhandle3(unpack)</h3>
<p>&nbsp;<wbr>Basic Data Types</p>
<h3>name3(unpack)</h3>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
