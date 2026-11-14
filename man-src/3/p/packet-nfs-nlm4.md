---
title: "packet-nfs-nlm4(3)"
name: "packet-nfs-nlm4"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-nlm4/"
description: "packet.nfs.nlm4 – NLMv4 decoding module"
---

<p>packet.nfs.nlm4 &#8211; NLMv4 decoding module</p>
<h2>Classes</h2>
<h3>class FREE_ALL4args(baseobj.BaseObj)</h3>
<pre>struct FREE_ALL4args {
 string name&lt;MAXNAMELEN&gt;;
 int32 state;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class NLM4args(packet.utils.RPCload)</h3>
<pre>union switch NLM4args (nlm_proc4 procedure) {
 case const.NLMPROC4_NULL:
 void;
 case const.NLMPROC4_TEST:
 TEST4args optest;
 case const.NLMPROC4_LOCK:
 LOCK4args oplock;
 case const.NLMPROC4_CANCEL:
 CANCEL4args opcancel;
 case const.NLMPROC4_UNLOCK:
 UNLOCK4args opunlock;
 case const.NLMPROC4_GRANTED:
 GRANTED4args opgranted;
 case const.NLMPROC4_TEST_MSG:
 TEST_MSG4args optest_msg;
 case const.NLMPROC4_LOCK_MSG:
 LOCK_MSG4args oplock_msg;
 case const.NLMPROC4_CANCEL_MSG:
 CANCEL_MSG4args opcancel_msg;
 case const.NLMPROC4_UNLOCK_MSG:
 UNLOCK_MSG4args opunlock_msg;
 case const.NLMPROC4_GRANTED_MSG:
 GRANTED_MSG4args opgranted_msg;
 case const.NLMPROC4_TEST_RES:
 TEST_RES4args optest_res;
 case const.NLMPROC4_LOCK_RES:
 LOCK_RES4args oplock_res;
 case const.NLMPROC4_CANCEL_RES:
 CANCEL_RES4args opcancel_res;
 case const.NLMPROC4_UNLOCK_RES:
 UNLOCK_RES4args opunlock_res;
 case const.NLMPROC4_GRANTED_RES:
 GRANTED_RES4args opgranted_res;
 case const.NLMPROC4_SHARE:
 SHARE4args opshare;
 case const.NLMPROC4_UNSHARE:
 UNSHARE4args opunshare;
 case const.NLMPROC4_NM_LOCK:
 NM_LOCK4args opnm_lock;
 case const.NLMPROC4_FREE_ALL:
 FREE_ALL4args opfree_all;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class NLM4res(packet.utils.RPCload)</h3>
<pre>union switch NLM4res (nlm_proc4 procedure) {
 case const.NLMPROC4_NULL:
 void;
 case const.NLMPROC4_TEST:
 TEST4res optest;
 case const.NLMPROC4_LOCK:
 LOCK4res oplock;
 case const.NLMPROC4_CANCEL:
 CANCEL4res opcancel;
 case const.NLMPROC4_UNLOCK:
 UNLOCK4res opunlock;
 case const.NLMPROC4_GRANTED:
 GRANTED4res opgranted;
 case const.NLMPROC4_TEST_MSG:
 void;
 case const.NLMPROC4_LOCK_MSG:
 void;
 case const.NLMPROC4_CANCEL_MSG:
 void;
 case const.NLMPROC4_UNLOCK_MSG:
 void;
 case const.NLMPROC4_GRANTED_MSG:
 void;
 case const.NLMPROC4_TEST_RES:
 void;
 case const.NLMPROC4_LOCK_RES:
 void;
 case const.NLMPROC4_CANCEL_RES:
 void;
 case const.NLMPROC4_UNLOCK_RES:
 void;
 case const.NLMPROC4_GRANTED_RES:
 void;
 case const.NLMPROC4_SHARE:
 SHARE4res opshare;
 case const.NLMPROC4_UNSHARE:
 UNSHARE4res opunshare;
 case const.NLMPROC4_NM_LOCK:
 NM_LOCK4res opnm_lock;
 case const.NLMPROC4_FREE_ALL:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class fsh4_access(packet.utils.Enum)</h3>
<pre>enum fsh4_access</pre>
<h3>class fsh4_mode(packet.utils.Enum)</h3>
<pre>enum fsh4_mode</pre>
<h3>class nfs_bool(packet.utils.Enum)</h3>
<pre>enum nfs_bool</pre>
<h3>class nlm4_cancargs(baseobj.BaseObj)</h3>
<pre>struct nlm4_cancargs {
 netobj cookie;
 bool block;
 bool exclusive;
 nlm4_lock locker;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_holder(baseobj.BaseObj)</h3>
<pre>struct nlm4_holder {
 bool exclusive;
 int32 svid;
 strobj oh;
 uint64 offset;
 uint64 length;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_lock(baseobj.BaseObj)</h3>
<pre>struct nlm4_lock {
 string owner&lt;LM_MAXSTRLEN&gt;;
 nlm_fh fh;
 strobj oh;
 int32 svid;
 uint64 offset;
 uint64 length;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_lockargs(baseobj.BaseObj)</h3>
<pre>struct nlm4_lockargs {
 netobj cookie;
 bool block;
 bool exclusive;
 nlm4_lock locker;
 bool reclaim; /* used for recovering locks */
 int state; /* specify local status monitor state */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_res(baseobj.BaseObj)</h3>
<pre>struct nlm4_res {
 netobj cookie;
 nlm4_stats status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_share(baseobj.BaseObj)</h3>
<pre>struct nlm4_share {
 string owner&lt;LM_MAXSTRLEN&gt;;
 nlm_fh fh;
 strobj oh;
 fsh4_mode mode;
 fsh4_access access;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_shareargs(baseobj.BaseObj)</h3>
<pre>struct nlm4_shareargs {
 netobj cookie;
 nlm4_share share;
 bool reclaim;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_shareres(baseobj.BaseObj)</h3>
<pre>struct nlm4_shareres {
 netobj cookie;
 nlm4_stats status;
 int sequence;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_stats(packet.utils.Enum)</h3>
<pre>enum nlm4_stats</pre>
<h3>class nlm4_testargs(baseobj.BaseObj)</h3>
<pre>struct nlm4_testargs {
 netobj cookie;
 bool exclusive;
 nlm4_lock locker;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_testres(baseobj.BaseObj)</h3>
<pre>struct nlm4_testres {
 netobj cookie;
 nlm4_testrply stat;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_testrply(baseobj.BaseObj)</h3>
<pre>union switch nlm4_testrply (nlm4_stats status) {
 case const.NLM4_DENIED:
 nlm4_holder denied;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm4_unlockargs(baseobj.BaseObj)</h3>
<pre>struct nlm4_unlockargs {
 netobj cookie;
 nlm4_lock locker;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nlm_proc4(packet.utils.Enum)</h3>
<pre>enum nlm_proc4</pre>
<h2>Functions</h2>
<h3>netobj(unpack)</h3>
<h3>nlm_fh(unpack)</h3>
<h3>strobj(unpack)</h3>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
