---
title: "packet-nfs-portmap2(3)"
name: "packet-nfs-portmap2"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-portmap2/"
description: "packet.nfs.portmap2 – PORTMAPv2 decoding module"
---

<p>packet.nfs.portmap2 &#8211; PORTMAPv2 decoding module</p>
<h2>Classes</h2>
<h3>class CALLIT2args(baseobj.BaseObj)</h3>
<pre>struct CALLIT2args {
 unsigned int prog;
 unsigned int vers;
 unsigned int proc;
 opaque args&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CALLIT2res(baseobj.BaseObj)</h3>
<pre>struct CALLIT2res {
 unsigned int port;
 opaque res&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DUMP2res(baseobj.BaseObj)</h3>
<pre>struct DUMP2res {
 entry2 *entries;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETPORT2res(baseobj.BaseObj)</h3>
<pre>struct GETPORT2res {
 unsigned int result;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PORTMAP2args(packet.utils.RPCload)</h3>
<pre>union switch PORTMAP2args (portmap_proc2 procedure) {
 case const.PMAPPROC_NULL:
 void;
 case const.PMAPPROC_SET:
 SET2args opset;
 case const.PMAPPROC_UNSET:
 UNSET2args opunset;
 case const.PMAPPROC_GETPORT:
 GETPORT2args opgetport;
 case const.PMAPPROC_DUMP:
 void;
 case const.PMAPPROC_CALLIT:
 CALLIT2args opcallit;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class PORTMAP2res(packet.utils.RPCload)</h3>
<pre>union switch PORTMAP2res (portmap_proc2 procedure) {
 case const.PMAPPROC_NULL:
 void;
 case const.PMAPPROC_SET:
 SET2res opset;
 case const.PMAPPROC_UNSET:
 UNSET2res opunset;
 case const.PMAPPROC_GETPORT:
 GETPORT2res opgetport;
 case const.PMAPPROC_DUMP:
 DUMP2res opdump;
 case const.PMAPPROC_CALLIT:
 CALLIT2res opcallit;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class bool_res(baseobj.BaseObj)</h3>
<pre>struct bool_res {
 bool result;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class entry2(baseobj.BaseObj)</h3>
<pre>struct entry2 {
 mapping map;
 entry2 *next;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class mapping(baseobj.BaseObj)</h3>
<pre>struct mapping {
 unsigned int prog;
 unsigned int vers;
 proto2 prot;
 unsigned int port;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class portmap_proc2(packet.utils.Enum)</h3>
<pre>enum portmap_proc2</pre>
<h3>class proto2(packet.utils.Enum)</h3>
<pre>enum proto2</pre>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
