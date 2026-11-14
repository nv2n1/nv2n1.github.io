---
title: "packet-nfs-nfs4(3)"
name: "packet-nfs-nfs4"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-nfs4/"
description: "packet.nfs.nfs4 – NFSv4 decoding module"
---

<p>packet.nfs.nfs4 &#8211; NFSv4 decoding module</p>
<h2>Classes</h2>
<h3>class ACCESS4args(baseobj.BaseObj)</h3>
<pre>struct ACCESS4args {
 /* CURRENT_FH: object */
 access4 access;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ACCESS4res(baseobj.BaseObj)</h3>
<pre>union switch ACCESS4res (nfsstat4 status) {
 case const.NFS4_OK:
 ACCESS4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ACCESS4resok(baseobj.BaseObj)</h3>
<pre>struct ACCESS4resok {
 access4 supported;
 access4 access;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ALLOCATE4args(baseobj.BaseObj)</h3>
<pre>struct ALLOCATE4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 length4 length;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ALLOCATE4res(baseobj.BaseObj)</h3>
<pre>struct ALLOCATE4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class BACKCHANNEL_CTL4args(baseobj.BaseObj)</h3>
<pre>struct BACKCHANNEL_CTL4args {
 uint32_t cb_program;
 callback_sec_parms4 sec_parms&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class BACKCHANNEL_CTL4res(baseobj.BaseObj)</h3>
<pre>struct BACKCHANNEL_CTL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class BIND_CONN_TO_SESSION4args(baseobj.BaseObj)</h3>
<pre>struct BIND_CONN_TO_SESSION4args {
 sessionid4 sessionid;
 channel_dir_from_client4 dir;
 bool rdma_mode;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class BIND_CONN_TO_SESSION4res(baseobj.BaseObj)</h3>
<pre>union switch BIND_CONN_TO_SESSION4res (nfsstat4 status) {
 case const.NFS4_OK:
 BIND_CONN_TO_SESSION4resok resok;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class BIND_CONN_TO_SESSION4resok(baseobj.BaseObj)</h3>
<pre>struct BIND_CONN_TO_SESSION4resok {
 sessionid4 sessionid;
 channel_dir_from_server4 dir;
 bool rdma_mode;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_COMPOUND4args(packet.nfs.nfsbase.NFSbase)</h3>
<pre>struct CB_COMPOUND4args {
 utf8str_cs tag;
 uint32_t minorversion;
 uint32_t callback_ident;
 nfs_cb_argop4 array&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_COMPOUND4res(packet.nfs.nfsbase.NFSbase)</h3>
<pre>struct CB_COMPOUND4res {
 nfsstat4 status;
 utf8str_cs tag;
 nfs_cb_resop4 array&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, minorversion)</code></pre>
<h3>class CB_GETATTR4args(baseobj.BaseObj)</h3>
<pre>struct CB_GETATTR4args {
 nfs_fh4 fh;
 bitmap4 request;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_GETATTR4res(baseobj.BaseObj)</h3>
<pre>union switch CB_GETATTR4res (nfsstat4 status) {
 case const.NFS4_OK:
 CB_GETATTR4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_GETATTR4resok(baseobj.BaseObj)</h3>
<pre>struct CB_GETATTR4resok {
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_ILLEGAL4res(baseobj.BaseObj)</h3>
<pre>struct CB_ILLEGAL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_LAYOUTRECALL4args(baseobj.BaseObj)</h3>
<pre>struct CB_LAYOUTRECALL4args {
 layouttype4 type;
 layoutiomode4 iomode;
 bool changed;
 layoutrecall4 recall;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_LAYOUTRECALL4res(baseobj.BaseObj)</h3>
<pre>struct CB_LAYOUTRECALL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY4args(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY4args {
 stateid4 stateid;
 nfs_fh4 fh;
 notify4 changes&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY4res(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY_DEVICEID4args(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY_DEVICEID4args {
 notify4 changes&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY_DEVICEID4res(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY_DEVICEID4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY_LOCK4args(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY_LOCK4args {
 nfs_fh4 fh;
 lock_owner4 lock_owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_NOTIFY_LOCK4res(baseobj.BaseObj)</h3>
<pre>struct CB_NOTIFY_LOCK4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_OFFLOAD4args(baseobj.BaseObj)</h3>
<pre>struct CB_OFFLOAD4args {
 nfs_fh4 fh;
 stateid4 stateid;
 offload_info4 info;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_OFFLOAD4res(baseobj.BaseObj)</h3>
<pre>struct CB_OFFLOAD4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_PUSH_DELEG4args(baseobj.BaseObj)</h3>
<pre>struct CB_PUSH_DELEG4args {
 nfs_fh4 fh;
 open_delegation4 delegation;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_PUSH_DELEG4res(baseobj.BaseObj)</h3>
<pre>struct CB_PUSH_DELEG4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL4args(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL4args {
 stateid4 stateid;
 bool truncate;
 nfs_fh4 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL4res(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALLABLE_OBJ_AVAIL4args(baseobj.BaseObj)</h3>
<pre>CB_RECALLABLE_OBJ_AVAIL4args = class CB_RECALL_ANY4args(baseobj.BaseObj)</pre>
<h3>class CB_RECALLABLE_OBJ_AVAIL4res(baseobj.BaseObj)</h3>
<pre>struct CB_RECALLABLE_OBJ_AVAIL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL_ANY4args(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL_ANY4args {
 uint32_t objects_to_keep;
 bitmap4 mask;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL_ANY4res(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL_ANY4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL_SLOT4args(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL_SLOT4args {
 slotid4 target_highest_slotid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_RECALL_SLOT4res(baseobj.BaseObj)</h3>
<pre>struct CB_RECALL_SLOT4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_SEQUENCE4args(baseobj.BaseObj)</h3>
<pre>struct CB_SEQUENCE4args {
 sessionid4 sessionid;
 sequenceid4 sequenceid;
 slotid4 slotid;
 slotid4 highest_slotid;
 bool cachethis;
 referring_call_list4 referring_call_lists&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_SEQUENCE4res(baseobj.BaseObj)</h3>
<pre>union switch CB_SEQUENCE4res (nfsstat4 status) {
 case const.NFS4_OK:
 CB_SEQUENCE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_SEQUENCE4resok(baseobj.BaseObj)</h3>
<pre>struct CB_SEQUENCE4resok {
 sessionid4 sessionid;
 sequenceid4 sequenceid;
 slotid4 slotid;
 slotid4 highest_slotid;
 slotid4 target_highest_slotid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_WANTS_CANCELLED4args(baseobj.BaseObj)</h3>
<pre>struct CB_WANTS_CANCELLED4args {
 bool contended;
 bool resourced;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CB_WANTS_CANCELLED4res(baseobj.BaseObj)</h3>
<pre>struct CB_WANTS_CANCELLED4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CLONE4args(baseobj.BaseObj)</h3>
<pre>struct CLONE4args {
 /*
 * SAVED_FH: source file
 * CURRENT_FH: destination file
 */
 stateid4 src_stateid;
 stateid4 dst_stateid;
 offset4 src_offset;
 offset4 dst_offset;
 length4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CLONE4res(baseobj.BaseObj)</h3>
<pre>struct CLONE4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CLOSE4args(baseobj.BaseObj)</h3>
<pre>struct CLOSE4args {
 /* CURRENT_FH: object */
 seqid4 seqid;
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CLOSE4res(baseobj.BaseObj)</h3>
<pre>union switch CLOSE4res (nfsstat4 status) {
 case const.NFS4_OK:
 stateid4 stateid;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT4args(baseobj.BaseObj)</h3>
<pre>struct COMMIT4args {
 /* CURRENT_FH: file */
 offset4 offset;
 count4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT4res(baseobj.BaseObj)</h3>
<pre>union switch COMMIT4res (nfsstat4 status) {
 case const.NFS4_OK:
 COMMIT4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT4resok(baseobj.BaseObj)</h3>
<pre>struct COMMIT4resok {
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMPOUND4args(packet.nfs.nfsbase.NFSbase)</h3>
<pre>struct COMPOUND4args {
 utf8str_cs tag;
 uint32_t minorversion;
 nfs_argop4 array&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMPOUND4res(packet.nfs.nfsbase.NFSbase)</h3>
<pre>struct COMPOUND4res {
 nfsstat4 status;
 utf8str_cs tag;
 nfs_resop4 array&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, minorversion)</code></pre>
<h3>class COPY4args(baseobj.BaseObj)</h3>
<pre>struct COPY4args {
 /*
 * SAVED_FH: source file
 * CURRENT_FH: destination file
 */
 stateid4 src_stateid;
 stateid4 dst_stateid;
 offset4 src_offset;
 offset4 dst_offset;
 length4 count;
 bool consecutive;
 bool synchronous;
 netloc4 src_servers&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COPY4res(baseobj.BaseObj)</h3>
<pre>union switch COPY4res (nfsstat4 status) {
 case const.NFS4_OK:
 COPY4resok resok;
 case const.NFS4ERR_OFFLOAD_NO_REQS:
 copy_requirements4 requirements;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COPY4resok(baseobj.BaseObj)</h3>
<pre>struct COPY4resok {
 write_response4 response;
 copy_requirements4 requirements;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COPY_NOTIFY4args(baseobj.BaseObj)</h3>
<pre>struct COPY_NOTIFY4args {
 /* CURRENT_FH: source file */
 stateid4 stateid;
 netloc4 dst_server;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COPY_NOTIFY4res(baseobj.BaseObj)</h3>
<pre>union switch COPY_NOTIFY4res (nfsstat4 status) {
 case const.NFS4_OK:
 COPY_NOTIFY4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COPY_NOTIFY4resok(baseobj.BaseObj)</h3>
<pre>struct COPY_NOTIFY4resok {
 nfstime4 lease_time;
 stateid4 stateid;
 netloc4 src_servers&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE4args(baseobj.BaseObj)</h3>
<pre>struct CREATE4args {
 /* CURRENT_FH: directory for creation */
 createtype4 type;
 component4 name;
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE4res(baseobj.BaseObj)</h3>
<pre>union switch CREATE4res (nfsstat4 status) {
 case const.NFS4_OK:
 /* new CURRENTFH: created object */
 CREATE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE4resok(baseobj.BaseObj)</h3>
<pre>struct CREATE4resok {
 change_info4 cinfo;
 bitmap4 attrset; /* attributes set */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE_SESSION4args(baseobj.BaseObj)</h3>
<pre>struct CREATE_SESSION4args {
 clientid4 clientid;
 sequenceid4 sequenceid;
 uint32_t flags;
 channel_attrs4 fore_chan_attrs;
 channel_attrs4 back_chan_attrs;
 uint32_t cb_program;
 callback_sec_parms4 sec_parms&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE_SESSION4res(baseobj.BaseObj)</h3>
<pre>union switch CREATE_SESSION4res (nfsstat4 status) {
 case const.NFS4_OK:
 CREATE_SESSION4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE_SESSION4resok(baseobj.BaseObj)</h3>
<pre>struct CREATE_SESSION4resok {
 sessionid4 sessionid;
 sequenceid4 sequenceid;
 uint32_t flags;
 channel_attrs4 fore_chan_attrs;
 channel_attrs4 back_chan_attrs;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DEALLOCATE4args(baseobj.BaseObj)</h3>
<pre>struct DEALLOCATE4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 length4 length;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DEALLOCATE4res(baseobj.BaseObj)</h3>
<pre>struct DEALLOCATE4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DELEGPURGE4args(baseobj.BaseObj)</h3>
<pre>struct DELEGPURGE4args {
 clientid4 clientid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DELEGPURGE4res(baseobj.BaseObj)</h3>
<pre>struct DELEGPURGE4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DELEGRETURN4args(baseobj.BaseObj)</h3>
<pre>struct DELEGRETURN4args {
 /* CURRENT_FH: delegated object */
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DELEGRETURN4res(baseobj.BaseObj)</h3>
<pre>struct DELEGRETURN4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DESTROY_CLIENTID4args(baseobj.BaseObj)</h3>
<pre>struct DESTROY_CLIENTID4args {
 clientid4 clientid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DESTROY_CLIENTID4res(baseobj.BaseObj)</h3>
<pre>struct DESTROY_CLIENTID4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DESTROY_SESSION4args(baseobj.BaseObj)</h3>
<pre>struct DESTROY_SESSION4args {
 sessionid4 sessionid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class DESTROY_SESSION4res(baseobj.BaseObj)</h3>
<pre>struct DESTROY_SESSION4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class EXCHANGE_ID4args(baseobj.BaseObj)</h3>
<pre>struct EXCHANGE_ID4args {
 client_owner4 clientowner;
 uint32_t flags;
 state_protect4_a state_protect;
 nfs_impl_id4 client_impl_id&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class EXCHANGE_ID4res(baseobj.BaseObj)</h3>
<pre>union switch EXCHANGE_ID4res (nfsstat4 status) {
 case const.NFS4_OK:
 EXCHANGE_ID4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class EXCHANGE_ID4resok(baseobj.BaseObj)</h3>
<pre>struct EXCHANGE_ID4resok {
 clientid4 clientid;
 sequenceid4 sequenceid;
 uint32_t flags;
 state_protect4_r state_protect;
 server_owner4 server_owner;
 opaque server_scope&lt;NFS4_OPAQUE_LIMIT&gt;;
 nfs_impl_id4 server_impl_id&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FREE_STATEID4args(baseobj.BaseObj)</h3>
<pre>struct FREE_STATEID4args {
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FREE_STATEID4res(baseobj.BaseObj)</h3>
<pre>struct FREE_STATEID4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR4args(baseobj.BaseObj)</h3>
<pre>struct GETATTR4args {
 /* CURRENT_FH: object */
 bitmap4 request;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR4res(baseobj.BaseObj)</h3>
<pre>union switch GETATTR4res (nfsstat4 status) {
 case const.NFS4_OK:
 GETATTR4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR4resok(baseobj.BaseObj)</h3>
<pre>struct GETATTR4resok {
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICEINFO4args(baseobj.BaseObj)</h3>
<pre>struct GETDEVICEINFO4args {
 deviceid4 deviceid;
 layouttype4 type;
 count4 maxcount;
 bitmap4 notification;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICEINFO4res(baseobj.BaseObj)</h3>
<pre>union switch GETDEVICEINFO4res (nfsstat4 status) {
 case const.NFS4_OK:
 GETDEVICEINFO4resok resok;
 case const.NFS4ERR_TOOSMALL:
 count4 mincount;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICEINFO4resok(baseobj.BaseObj)</h3>
<pre>struct GETDEVICEINFO4resok {
 device_addr4 device_addr;
 bitmap4 notification;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICELIST4args(baseobj.BaseObj)</h3>
<pre>struct GETDEVICELIST4args {
 /* CURRENT_FH: object belonging to the file system */
 layouttype4 type;
 /* number of deviceIDs to return */
 count4 maxdevices;
 nfs_cookie4 cookie;
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICELIST4res(baseobj.BaseObj)</h3>
<pre>union switch GETDEVICELIST4res (nfsstat4 status) {
 case const.NFS4_OK:
 GETDEVICELIST4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETDEVICELIST4resok(baseobj.BaseObj)</h3>
<pre>struct GETDEVICELIST4resok {
 nfs_cookie4 cookie;
 verifier4 verifier;
 deviceid4 deviceid_list&lt;&gt;;
 bool eof;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETFH4res(baseobj.BaseObj)</h3>
<pre>union switch GETFH4res (nfsstat4 status) {
 case const.NFS4_OK:
 GETFH4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETFH4resok(baseobj.BaseObj)</h3>
<pre>struct GETFH4resok {
 nfs_fh4 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GET_DIR_DELEGATION4args(baseobj.BaseObj)</h3>
<pre>struct GET_DIR_DELEGATION4args {
 /* CURRENT_FH: delegated directory */
 bool deleg_avail;
 bitmap4 notification;
 attr_notice4 child_attr_delay;
 attr_notice4 attr_delay;
 bitmap4 child_attributes;
 bitmap4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GET_DIR_DELEGATION4res(baseobj.BaseObj)</h3>
<pre>union switch GET_DIR_DELEGATION4res (nfsstat4 status) {
 case const.NFS4_OK:
 GET_DIR_DELEGATION4res_non_fatal resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GET_DIR_DELEGATION4res_non_fatal(baseobj.BaseObj)</h3>
<pre>union switch GET_DIR_DELEGATION4res_non_fatal (gddrnf4_status status) {
 case const.GDD4_OK:
 GET_DIR_DELEGATION4resok resok;
 case const.GDD4_UNAVAIL:
 bool signal;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GET_DIR_DELEGATION4resok(baseobj.BaseObj)</h3>
<pre>struct GET_DIR_DELEGATION4resok {
 verifier4 verifier;
 /* Stateid for get_dir_delegation */
 stateid4 stateid;
 /* Which notifications can the server support */
 bitmap4 notification;
 bitmap4 child_attributes;
 bitmap4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ILLEGAL4res(baseobj.BaseObj)</h3>
<pre>struct ILLEGAL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class IO_ADVISE4args(baseobj.BaseObj)</h3>
<pre>struct IO_ADVISE4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 length4 count;
 bitmap4 hints;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class IO_ADVISE4res(baseobj.BaseObj)</h3>
<pre>union switch IO_ADVISE4res (nfsstat4 status) {
 case const.NFS4_OK:
 IO_ADVISE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class IO_ADVISE4resok(baseobj.BaseObj)</h3>
<pre>struct IO_ADVISE4resok {
 bitmap4 hints;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class IO_ADVISE_type4(packet.utils.Enum)</h3>
<pre>enum IO_ADVISE_type4</pre>
<h3>class LAYOUTCOMMIT4args(baseobj.BaseObj)</h3>
<pre>struct LAYOUTCOMMIT4args {
 /* CURRENT_FH: file */
 offset4 offset;
 length4 length;
 bool reclaim;
 stateid4 stateid;
 newoffset4 last_write_offset;
 newtime4 time_modify;
 layoutupdate4 layoutupdate;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTCOMMIT4res(baseobj.BaseObj)</h3>
<pre>union switch LAYOUTCOMMIT4res (nfsstat4 status) {
 case const.NFS4_OK:
 LAYOUTCOMMIT4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTCOMMIT4resok(baseobj.BaseObj)</h3>
<pre>struct LAYOUTCOMMIT4resok {
 newsize4 newsize;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTERROR4args(baseobj.BaseObj)</h3>
<pre>struct LAYOUTERROR4args {
 /* CURRENT_FH: file */
 offset4 offset;
 length4 length;
 stateid4 stateid;
 device_error4 errors&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTERROR4res(baseobj.BaseObj)</h3>
<pre>struct LAYOUTERROR4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTGET4args(baseobj.BaseObj)</h3>
<pre>struct LAYOUTGET4args {
 /* CURRENT_FH: file */
 bool avail;
 layouttype4 type;
 layoutiomode4 iomode;
 offset4 offset;
 length4 length;
 length4 minlength;
 stateid4 stateid;
 count4 maxcount;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTGET4res(baseobj.BaseObj)</h3>
<pre>union switch LAYOUTGET4res (nfsstat4 status) {
 case const.NFS4_OK:
 LAYOUTGET4resok resok;
 case const.NFS4ERR_LAYOUTTRYLATER:
 /* Server will signal layout availability */
 bool signal;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTGET4resok(baseobj.BaseObj)</h3>
<pre>struct LAYOUTGET4resok {
 bool return_on_close;
 stateid4 stateid;
 layout4 layout&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTRETURN4args(baseobj.BaseObj)</h3>
<pre>struct LAYOUTRETURN4args {
 /* CURRENT_FH: file */
 bool reclaim;
 layouttype4 type;
 layoutiomode4 iomode;
 layoutreturn4 layoutreturn;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTRETURN4res(baseobj.BaseObj)</h3>
<pre>union switch LAYOUTRETURN4res (nfsstat4 status) {
 case const.NFS4_OK:
 layoutreturn_stateid stateid;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTSTATS4args(baseobj.BaseObj)</h3>
<pre>struct LAYOUTSTATS4args {
 /* CURRENT_FH: file */
 offset4 offset;
 length4 length;
 stateid4 stateid;
 io_info4 read;
 io_info4 write;
 deviceid4 deviceid;
 layoutupdate4 layoutupdate;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LAYOUTSTATS4res(baseobj.BaseObj)</h3>
<pre>struct LAYOUTSTATS4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK4args(baseobj.BaseObj)</h3>
<pre>struct LINK4args {
 /*
 * SAVED_FH: source object
 * CURRENT_FH: target directory
 */
 component4 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK4res(baseobj.BaseObj)</h3>
<pre>union switch LINK4res (nfsstat4 status) {
 case const.NFS4_OK:
 LINK4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK4resok(baseobj.BaseObj)</h3>
<pre>struct LINK4resok {
 change_info4 cinfo;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCK4args(baseobj.BaseObj)</h3>
<pre>struct LOCK4args {
 /* CURRENT_FH: file */
 nfs_lock_type4 locktype;
 bool reclaim;
 offset4 offset;
 length4 length;
 locker4 locker;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCK4denied(baseobj.BaseObj)</h3>
<pre>struct LOCK4denied {
 offset4 offset;
 length4 length;
 nfs_lock_type4 locktype;
 lock_owner4 owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCK4res(baseobj.BaseObj)</h3>
<pre>union switch LOCK4res (nfsstat4 status) {
 case const.NFS4_OK:
 LOCK4resok resok;
 case const.NFS4ERR_DENIED:
 LOCK4denied denied;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCK4resok(baseobj.BaseObj)</h3>
<pre>struct LOCK4resok {
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCKT4args(baseobj.BaseObj)</h3>
<pre>struct LOCKT4args {
 /* CURRENT_FH: file */
 nfs_lock_type4 locktype;
 offset4 offset;
 length4 length;
 lock_owner4 owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCKT4res(baseobj.BaseObj)</h3>
<pre>union switch LOCKT4res (nfsstat4 status) {
 case const.NFS4ERR_DENIED:
 LOCK4denied denied;
 case const.NFS4_OK:
 void;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCKU4args(baseobj.BaseObj)</h3>
<pre>struct LOCKU4args {
 /* CURRENT_FH: file */
 nfs_lock_type4 locktype;
 seqid4 seqid;
 stateid4 stateid;
 offset4 offset;
 length4 length;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOCKU4res(baseobj.BaseObj)</h3>
<pre>union switch LOCKU4res (nfsstat4 status) {
 case const.NFS4_OK:
 stateid4 stateid;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP4args(baseobj.BaseObj)</h3>
<pre>struct LOOKUP4args {
 /* CURRENT_FH: directory */
 component4 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP4res(baseobj.BaseObj)</h3>
<pre>struct LOOKUP4res {
 /* New CURRENT_FH: object */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUPP4res(baseobj.BaseObj)</h3>
<pre>struct LOOKUPP4res {
 /* new CURRENT_FH: parent directory */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class NVERIFY4args(baseobj.BaseObj)</h3>
<pre>struct NVERIFY4args {
 /* CURRENT_FH: object */
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class NVERIFY4res(baseobj.BaseObj)</h3>
<pre>struct NVERIFY4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OFFLOAD_CANCEL4args(baseobj.BaseObj)</h3>
<pre>struct OFFLOAD_CANCEL4args {
 /* CURRENT_FH: file to cancel */
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OFFLOAD_CANCEL4res(baseobj.BaseObj)</h3>
<pre>struct OFFLOAD_CANCEL4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OFFLOAD_STATUS4args(baseobj.BaseObj)</h3>
<pre>struct OFFLOAD_STATUS4args {
 /* CURRENT_FH: destination file */
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OFFLOAD_STATUS4res(baseobj.BaseObj)</h3>
<pre>union switch OFFLOAD_STATUS4res (nfsstat4 status) {
 case const.NFS4_OK:
 OFFLOAD_STATUS4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OFFLOAD_STATUS4resok(baseobj.BaseObj)</h3>
<pre>struct OFFLOAD_STATUS4resok {
 length4 count;
 nfsstat4 complete&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN4args(baseobj.BaseObj)</h3>
<pre>struct OPEN4args {
 seqid4 seqid;
 uint32_t access;
 uint32_t deny;
 open_owner4 owner;
 openflag4 openhow;
 open_claim4 claim;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN4res(baseobj.BaseObj)</h3>
<pre>union switch OPEN4res (nfsstat4 status) {
 case const.NFS4_OK:
 /* New CURRENT_FH: opened file */
 OPEN4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN4resok(baseobj.BaseObj)</h3>
<pre>struct OPEN4resok {
 stateid4 stateid; /* Stateid for open */
 change_info4 cinfo; /* Directory Change Info */
 uint32_t rflags; /* Result flags */
 bitmap4 attrset; /* attribute set for create */
 open_delegation4 delegation; /* Info on any open delegation */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPENATTR4args(baseobj.BaseObj)</h3>
<pre>struct OPENATTR4args {
 /* CURRENT_FH: object */
 bool createdir;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPENATTR4res(baseobj.BaseObj)</h3>
<pre>struct OPENATTR4res {
 /*
 * If status is NFS4_OK,
 * new CURRENT_FH: named attribute directory
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_CONFIRM4args(baseobj.BaseObj)</h3>
<pre>struct OPEN_CONFIRM4args {
 /* CURRENT_FH: opened file */
 stateid4 stateid;
 seqid4 seqid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_CONFIRM4res(baseobj.BaseObj)</h3>
<pre>union switch OPEN_CONFIRM4res (nfsstat4 status) {
 case const.NFS4_OK:
 OPEN_CONFIRM4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_CONFIRM4resok(baseobj.BaseObj)</h3>
<pre>struct OPEN_CONFIRM4resok {
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_DOWNGRADE4args(baseobj.BaseObj)</h3>
<pre>struct OPEN_DOWNGRADE4args {
 /* CURRENT_FH: opened file */
 stateid4 stateid;
 seqid4 seqid;
 uint32_t access;
 uint32_t deny;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_DOWNGRADE4res(baseobj.BaseObj)</h3>
<pre>union switch OPEN_DOWNGRADE4res (nfsstat4 status) {
 case const.NFS4_OK:
 OPEN_DOWNGRADE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class OPEN_DOWNGRADE4resok(baseobj.BaseObj)</h3>
<pre>struct OPEN_DOWNGRADE4resok {
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PUTFH4args(baseobj.BaseObj)</h3>
<pre>struct PUTFH4args {
 nfs_fh4 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PUTFH4res(baseobj.BaseObj)</h3>
<pre>struct PUTFH4res {
 /*
 * If status is NFS4_OK,
 * new CURRENT_FH: argument to PUTFH
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PUTPUBFH4res(baseobj.BaseObj)</h3>
<pre>struct PUTPUBFH4res {
 /*
 * If status is NFS4_OK,
 * new CURRENT_FH: public fh
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PUTROOTFH4res(baseobj.BaseObj)</h3>
<pre>struct PUTROOTFH4res {
 /*
 * If status is NFS4_OK,
 * new CURRENT_FH: root fh
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ4args(baseobj.BaseObj)</h3>
<pre>struct READ4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 count4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ4res(baseobj.BaseObj)</h3>
<pre>union switch READ4res (nfsstat4 status) {
 case const.NFS4_OK:
 READ4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ4resok(baseobj.BaseObj)</h3>
<pre>struct READ4resok {
 bool eof;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR4args(baseobj.BaseObj)</h3>
<pre>struct READDIR4args {
 /* CURRENT_FH: directory */
 nfs_cookie4 cookie;
 verifier4 verifier;
 count4 dircount;
 count4 maxcount;
 bitmap4 request;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR4res(baseobj.BaseObj)</h3>
<pre>union switch READDIR4res (nfsstat4 status) {
 case const.NFS4_OK:
 READDIR4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR4resok(baseobj.BaseObj)</h3>
<pre>struct READDIR4resok {
 verifier4 verifier;
 dirlist4 reply;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK4res(baseobj.BaseObj)</h3>
<pre>union switch READLINK4res (nfsstat4 status) {
 case const.NFS4_OK:
 READLINK4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK4resok(baseobj.BaseObj)</h3>
<pre>struct READLINK4resok {
 linktext4 link;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ_PLUS4args(baseobj.BaseObj)</h3>
<pre>struct READ_PLUS4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 count4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ_PLUS4res(baseobj.BaseObj)</h3>
<pre>union switch READ_PLUS4res (nfsstat4 status) {
 case const.NFS4_OK:
 read_plus_res4 resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RECLAIM_COMPLETE4args(baseobj.BaseObj)</h3>
<pre>union switch RECLAIM_COMPLETE4args (bool one_fs) {
 case const.TRUE:
 /*
 * If one_fs TRUE,
 * CURRENT_FH: object in filesystem reclaim is complete for.
 */
 void;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RECLAIM_COMPLETE4res(baseobj.BaseObj)</h3>
<pre>struct RECLAIM_COMPLETE4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RELEASE_LOCKOWNER4args(baseobj.BaseObj)</h3>
<pre>struct RELEASE_LOCKOWNER4args {
 lock_owner4 owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RELEASE_LOCKOWNER4res(baseobj.BaseObj)</h3>
<pre>struct RELEASE_LOCKOWNER4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE4args(baseobj.BaseObj)</h3>
<pre>struct REMOVE4args {
 /* CURRENT_FH: directory */
 component4 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE4res(baseobj.BaseObj)</h3>
<pre>union switch REMOVE4res (nfsstat4 status) {
 case const.NFS4_OK:
 REMOVE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE4resok(baseobj.BaseObj)</h3>
<pre>struct REMOVE4resok {
 change_info4 cinfo;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME4args(baseobj.BaseObj)</h3>
<pre>struct RENAME4args {
 /* SAVED_FH: source directory */
 component4 name;
 /* CURRENT_FH: target directory */
 component4 newname;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME4res(baseobj.BaseObj)</h3>
<pre>union switch RENAME4res (nfsstat4 status) {
 case const.NFS4_OK:
 RENAME4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME4resok(baseobj.BaseObj)</h3>
<pre>struct RENAME4resok {
 change_info4 source;
 change_info4 target;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENEW4args(baseobj.BaseObj)</h3>
<pre>struct RENEW4args {
 clientid4 clientid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENEW4res(baseobj.BaseObj)</h3>
<pre>struct RENEW4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RESTOREFH4res(baseobj.BaseObj)</h3>
<pre>struct RESTOREFH4res {
 /*
 * If status is NFS4_OK,
 * new CURRENT_FH: value of saved fh
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SAVEFH4res(baseobj.BaseObj)</h3>
<pre>struct SAVEFH4res {
 /*
 * If status is NFS4_OK,
 * new SAVED_FH: value of current fh
 */
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SECINFO4args(baseobj.BaseObj)</h3>
<pre>struct SECINFO4args {
 /* CURRENT_FH: directory */
 component4 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SECINFO4res(baseobj.BaseObj)</h3>
<pre>union switch SECINFO4res (nfsstat4 status) {
 case const.NFS4_OK:
 /* CURRENTFH: consumed */
 SECINFO4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SECINFO_NO_NAME4args(baseobj.BaseObj)</h3>
<pre>struct SECINFO_NO_NAME4args {
 /* CURRENT_FH: object or child directory */
 secinfo_style4 style;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SECINFO_NO_NAME4res(baseobj.BaseObj)</h3>
<pre>SECINFO_NO_NAME4res = class SECINFO4res(baseobj.BaseObj)</pre>
<h3>class SEEK4args(baseobj.BaseObj)</h3>
<pre>struct SEEK4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 data_content4 what;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SEEK4res(baseobj.BaseObj)</h3>
<pre>union switch SEEK4res (nfsstat4 status) {
 case const.NFS4_OK:
 seek_res4 resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SEQUENCE4args(baseobj.BaseObj)</h3>
<pre>struct SEQUENCE4args {
 sessionid4 sessionid;
 sequenceid4 sequenceid;
 slotid4 slotid;
 slotid4 highest_slotid;
 bool cachethis;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SEQUENCE4res(baseobj.BaseObj)</h3>
<pre>union switch SEQUENCE4res (nfsstat4 status) {
 case const.NFS4_OK:
 SEQUENCE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SEQUENCE4resok(baseobj.BaseObj)</h3>
<pre>struct SEQUENCE4resok {
 sessionid4 sessionid;
 sequenceid4 sequenceid;
 slotid4 slotid;
 slotid4 highest_slotid;
 slotid4 target_highest_slotid;
 uint32_t status_flags;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR4args(baseobj.BaseObj)</h3>
<pre>struct SETATTR4args {
 /* CURRENT_FH: target object */
 stateid4 stateid;
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR4res(baseobj.BaseObj)</h3>
<pre>struct SETATTR4res {
 nfsstat4 status;
 bitmap4 attrset;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETCLIENTID4args(baseobj.BaseObj)</h3>
<pre>struct SETCLIENTID4args {
 nfs_client_id4 client;
 cb_client4 callback;
 uint32_t callback_ident;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETCLIENTID4res(baseobj.BaseObj)</h3>
<pre>union switch SETCLIENTID4res (nfsstat4 status) {
 case const.NFS4_OK:
 SETCLIENTID4resok resok;
 case const.NFS4ERR_CLID_INUSE:
 clientaddr4 client;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETCLIENTID4resok(baseobj.BaseObj)</h3>
<pre>struct SETCLIENTID4resok {
 clientid4 clientid;
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETCLIENTID_CONFIRM4args(baseobj.BaseObj)</h3>
<pre>struct SETCLIENTID_CONFIRM4args {
 clientid4 clientid;
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETCLIENTID_CONFIRM4res(baseobj.BaseObj)</h3>
<pre>struct SETCLIENTID_CONFIRM4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SET_SSV4args(baseobj.BaseObj)</h3>
<pre>struct SET_SSV4args {
 opaque ssv&lt;&gt;;
 opaque digest&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SET_SSV4res(baseobj.BaseObj)</h3>
<pre>union switch SET_SSV4res (nfsstat4 status) {
 case const.NFS4_OK:
 SET_SSV4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SET_SSV4resok(baseobj.BaseObj)</h3>
<pre>struct SET_SSV4resok {
 opaque digest&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class TEST_STATEID4args(baseobj.BaseObj)</h3>
<pre>struct TEST_STATEID4args {
 stateid4 stateids&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class TEST_STATEID4res(baseobj.BaseObj)</h3>
<pre>union switch TEST_STATEID4res (nfsstat4 status) {
 case const.NFS4_OK:
 TEST_STATEID4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class TEST_STATEID4resok(baseobj.BaseObj)</h3>
<pre>struct TEST_STATEID4resok {
 nfsstat4 status_codes&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class VERIFY4args(baseobj.BaseObj)</h3>
<pre>struct VERIFY4args {
 /* CURRENT_FH: object */
 fattr4 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class VERIFY4res(baseobj.BaseObj)</h3>
<pre>struct VERIFY4res {
 nfsstat4 status;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WANT_DELEGATION4args(baseobj.BaseObj)</h3>
<pre>struct WANT_DELEGATION4args {
 uint32_t want;
 deleg_claim4 claim;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WANT_DELEGATION4res(baseobj.BaseObj)</h3>
<pre>union switch WANT_DELEGATION4res (nfsstat4 status) {
 case const.NFS4_OK:
 open_delegation4 resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE4args(baseobj.BaseObj)</h3>
<pre>struct WRITE4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 offset4 offset;
 stable_how4 stable;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE4res(baseobj.BaseObj)</h3>
<pre>union switch WRITE4res (nfsstat4 status) {
 case const.NFS4_OK:
 WRITE4resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE4resok(baseobj.BaseObj)</h3>
<pre>struct WRITE4resok {
 count4 count;
 stable_how4 committed;
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE_SAME4args(baseobj.BaseObj)</h3>
<pre>struct WRITE_SAME4args {
 /* CURRENT_FH: file */
 stateid4 stateid;
 stable_how4 stable;
 app_data_block4 adb;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE_SAME4res(baseobj.BaseObj)</h3>
<pre>union switch WRITE_SAME4res (nfsstat4 status) {
 case const.NFS4_OK:
 write_response4 resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class app_data_block4(baseobj.BaseObj)</h3>
<pre>struct app_data_block4 {
 offset4 offset;
 length4 block_size;
 length4 block_count;
 length4 reloff_blocknum;
 count4 block_num;
 length4 reloff_pattern;
 opaque pattern&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class attr_notice4(baseobj.BaseObj)</h3>
<pre>attr_notice4 = class nfstime4(baseobj.BaseObj)</pre>
<h3>class authsys_parms(baseobj.BaseObj)</h3>
<pre>struct authsys_parms {
 unsigned int stamp;
 string machinename&lt;255&gt;;
 unsigned int uid;
 unsigned int gid;
 unsigned int gids&lt;16&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class callback_sec_parms4(baseobj.BaseObj)</h3>
<pre>union switch callback_sec_parms4 (nfs_secflavor4 flavor) {
 case const.AUTH_NONE:
 void;
 case const.AUTH_SYS:
 authsys_parms sys_cred; /* RFC 1831 */
 case const.RPCSEC_GSS:
 gss_cb_handles4 gss_handles;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class cb_client4(baseobj.BaseObj)</h3>
<pre>struct cb_client4 {
 uint32_t cb_program;
 netaddr4 cb_location;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class change_attr_type4(packet.utils.Enum)</h3>
<pre>enum change_attr_type4</pre>
<h3>class change_info4(baseobj.BaseObj)</h3>
<pre>struct change_info4 {
 bool atomic;
 changeid4 before;
 changeid4 after;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class change_policy4(baseobj.BaseObj)</h3>
<pre>struct change_policy4 {
 uint64_t major;
 uint64_t minor;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class channel_attrs4(baseobj.BaseObj)</h3>
<pre>struct channel_attrs4 {
 count4 headerpadsize;
 count4 maxrequestsize;
 count4 maxresponsesize;
 count4 maxresponsesize_cached;
 count4 maxoperations;
 count4 maxrequests;
 uint32_t rdma_ird&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class channel_dir_from_client4(packet.utils.Enum)</h3>
<pre>enum channel_dir_from_client4</pre>
<h3>class channel_dir_from_server4(packet.utils.Enum)</h3>
<pre>enum channel_dir_from_server4</pre>
<h3>class client_owner4(baseobj.BaseObj)</h3>
<pre>struct client_owner4 {
 verifier4 verifier;
 opaque ownerid&lt;NFS4_OPAQUE_LIMIT&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class clientaddr4(baseobj.BaseObj)</h3>
<pre>struct clientaddr4 {
 /* See struct rpcb in RFC 1833 */
 string netid&lt;&gt;; /* network id */
 string addr&lt;&gt;; /* universal address */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class copy_confirm_auth_priv(baseobj.BaseObj)</h3>
<pre>struct copy_confirm_auth_priv {
 /* equal to GSS_GetMIC() of cfap_shared_secret */
 opaque secret&lt;&gt;;
 /* the NFSv4 user name that the user principal maps to */
 utf8str_mixed username;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class copy_from_auth_priv(baseobj.BaseObj)</h3>
<pre>struct copy_from_auth_priv {
 secret4 secret;
 netloc4 destination;
 /* the NFSv4 user name that the user principal maps to */
 utf8str_mixed username;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class copy_requirements4(baseobj.BaseObj)</h3>
<pre>struct copy_requirements4 {
 bool consecutive;
 bool synchronous;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class copy_to_auth_priv(baseobj.BaseObj)</h3>
<pre>struct copy_to_auth_priv {
 /* equal to cfap_shared_secret */
 secret4 secret;
 netloc4 source&lt;&gt;;
 /* the NFSv4 user name that the user principal maps to */
 utf8str_mixed username;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class createhow4(baseobj.BaseObj)</h3>
<pre>union switch createhow4 (createmode4 mode) {
 case const.UNCHECKED4:
 case const.GUARDED4:
 fattr4 attributes;
 case const.EXCLUSIVE4:
 verifier4 verifier;
 case const.EXCLUSIVE4_1:
 creatverfattr createboth;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class createmode4(packet.utils.Enum)</h3>
<pre>enum createmode4</pre>
<h3>class createtype4(baseobj.BaseObj)</h3>
<pre>union switch createtype4 (nfs_ftype4 type) {
 case const.NF4LNK:
 linktext4 linkdata;
 case const.NF4BLK:
 case const.NF4CHR:
 specdata4 devdata;
 case const.NF4SOCK:
 case const.NF4FIFO:
 case const.NF4DIR:
 void;
 default:
 void; /* server should return NFS4ERR_BADTYPE */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class creatverfattr(baseobj.BaseObj)</h3>
<pre>struct creatverfattr {
 verifier4 verifier;
 fattr4 attrs;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class data4(baseobj.BaseObj)</h3>
<pre>struct data4 {
 offset4 offset;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class data_content4(packet.utils.Enum)</h3>
<pre>enum data_content4</pre>
<h3>class data_info4(baseobj.BaseObj)</h3>
<pre>struct data_info4 {
 offset4 offset;
 length4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class deleg_claim4(baseobj.BaseObj)</h3>
<pre>union switch deleg_claim4 (open_claim_type4 claim) {
 /*
 * No special rights to object. Ordinary delegation
 * request of the specified object. Object identified
 * by filehandle.
 */
 case const.CLAIM_FH:
 void;
 /*
 * Right to file based on a delegation granted
 * to a previous boot instance of the client.
 * File is specified by filehandle.
 */
 case const.CLAIM_DELEG_PREV_FH:
 /* CURRENT_FH: object being delegated */
 void;
 /*
 * Right to the file established by an open previous
 * to server reboot. File identified by filehandle.
 * Used during server reclaim grace period.
 */
 case const.CLAIM_PREVIOUS:
 /* CURRENT_FH: object being reclaimed */
 open_delegation_type4 deleg_type;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class device_addr4(baseobj.BaseObj)</h3>
<pre>union switch device_addr4 (layouttype4 type) {
 case const.LAYOUT4_NFSV4_1_FILES:
 nfsv4_1_file_layout_ds_addr4 body;
 case const.LAYOUT4_FLEX_FILES:
 ff_device_addr4 body;
 default:
 /* All other types are not supported yet */
 opaque body&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class device_error4(baseobj.BaseObj)</h3>
<pre>struct device_error4 {
 deviceid4 deviceid;
 nfsstat4 status;
 nfs_opnum4 opnum;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class dirlist4(baseobj.BaseObj)</h3>
<pre>struct dirlist4 {
 entry4 *entries;
 bool eof;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class entry4(baseobj.BaseObj)</h3>
<pre>struct entry4 {
 nfs_cookie4 cookie;
 component4 name;
 fattr4 attrs;
 entry4 *nextentry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class exist_lock_owner4(baseobj.BaseObj)</h3>
<pre>struct exist_lock_owner4 {
 stateid4 stateid;
 seqid4 seqid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fattr4_archive(packet.utils.Enum)</h3>
<pre>fattr4_archive = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_cansettime(packet.utils.Enum)</h3>
<pre>fattr4_cansettime = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_case_insensitive(packet.utils.Enum)</h3>
<pre>fattr4_case_insensitive = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_case_preserving(packet.utils.Enum)</h3>
<pre>fattr4_case_preserving = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_change_attr_type(packet.utils.Enum)</h3>
<pre>fattr4_change_attr_type = class change_attr_type4(packet.utils.Enum)</pre>
<h3>class fattr4_change_policy(baseobj.BaseObj)</h3>
<pre>fattr4_change_policy = class change_policy4(baseobj.BaseObj)</pre>
<h3>class fattr4_chown_restricted(packet.utils.Enum)</h3>
<pre>fattr4_chown_restricted = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_dacl(baseobj.BaseObj)</h3>
<pre>fattr4_dacl = class nfsacl41(baseobj.BaseObj)</pre>
<h3>class fattr4_dir_notif_delay(baseobj.BaseObj)</h3>
<pre>fattr4_dir_notif_delay = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_dirent_notif_delay(baseobj.BaseObj)</h3>
<pre>fattr4_dirent_notif_delay = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_fs_locations(baseobj.BaseObj)</h3>
<pre>fattr4_fs_locations = class fs_locations4(baseobj.BaseObj)</pre>
<h3>class fattr4_fs_locations_info(baseobj.BaseObj)</h3>
<pre>fattr4_fs_locations_info = class fs_locations_info4(baseobj.BaseObj)</pre>
<h3>class fattr4_fs_status(baseobj.BaseObj)</h3>
<pre>fattr4_fs_status = class fs4_status(baseobj.BaseObj)</pre>
<h3>class fattr4_fsid(baseobj.BaseObj)</h3>
<pre>fattr4_fsid = class fsid4(baseobj.BaseObj)</pre>
<h3>class fattr4_hidden(packet.utils.Enum)</h3>
<pre>fattr4_hidden = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_homogeneous(packet.utils.Enum)</h3>
<pre>fattr4_homogeneous = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_layout_hint(baseobj.BaseObj)</h3>
<pre>fattr4_layout_hint = class layouthint4(baseobj.BaseObj)</pre>
<h3>class fattr4_link_support(packet.utils.Enum)</h3>
<pre>fattr4_link_support = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_mdsthreshold(baseobj.BaseObj)</h3>
<pre>fattr4_mdsthreshold = class mdsthreshold4(baseobj.BaseObj)</pre>
<h3>class fattr4_mode_set_masked(baseobj.BaseObj)</h3>
<pre>fattr4_mode_set_masked = class mode_masked4(baseobj.BaseObj)</pre>
<h3>class fattr4_named_attr(packet.utils.Enum)</h3>
<pre>fattr4_named_attr = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_no_trunc(packet.utils.Enum)</h3>
<pre>fattr4_no_trunc = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_rawdev(baseobj.BaseObj)</h3>
<pre>fattr4_rawdev = class specdata4(baseobj.BaseObj)</pre>
<h3>class fattr4_rdattr_error(packet.utils.Enum)</h3>
<pre>fattr4_rdattr_error = class nfsstat4(packet.utils.Enum)</pre>
<h3>class fattr4_retentevt_get(baseobj.BaseObj)</h3>
<pre>fattr4_retentevt_get = class retention_get4(baseobj.BaseObj)</pre>
<h3>class fattr4_retentevt_set(baseobj.BaseObj)</h3>
<pre>fattr4_retentevt_set = class retention_set4(baseobj.BaseObj)</pre>
<h3>class fattr4_retention_get(baseobj.BaseObj)</h3>
<pre>fattr4_retention_get = class retention_get4(baseobj.BaseObj)</pre>
<h3>class fattr4_retention_set(baseobj.BaseObj)</h3>
<pre>fattr4_retention_set = class retention_set4(baseobj.BaseObj)</pre>
<h3>class fattr4_sacl(baseobj.BaseObj)</h3>
<pre>fattr4_sacl = class nfsacl41(baseobj.BaseObj)</pre>
<h3>class fattr4_sec_label(baseobj.BaseObj)</h3>
<pre>fattr4_sec_label = class sec_label4(baseobj.BaseObj)</pre>
<h3>class fattr4_symlink_support(packet.utils.Enum)</h3>
<pre>fattr4_symlink_support = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_system(packet.utils.Enum)</h3>
<pre>fattr4_system = class nfs_bool(packet.utils.Enum)</pre>
<h3>class fattr4_time_access(baseobj.BaseObj)</h3>
<pre>fattr4_time_access = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_access_set(baseobj.BaseObj)</h3>
<pre>fattr4_time_access_set = class settime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_backup(baseobj.BaseObj)</h3>
<pre>fattr4_time_backup = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_create(baseobj.BaseObj)</h3>
<pre>fattr4_time_create = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_delta(baseobj.BaseObj)</h3>
<pre>fattr4_time_delta = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_metadata(baseobj.BaseObj)</h3>
<pre>fattr4_time_metadata = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_modify(baseobj.BaseObj)</h3>
<pre>fattr4_time_modify = class nfstime4(baseobj.BaseObj)</pre>
<h3>class fattr4_time_modify_set(baseobj.BaseObj)</h3>
<pre>fattr4_time_modify_set = class settime4(baseobj.BaseObj)</pre>
<h3>class fattr4_type(packet.utils.Enum)</h3>
<pre>fattr4_type = class nfs_ftype4(packet.utils.Enum)</pre>
<h3>class fattr4_unique_handles(packet.utils.Enum)</h3>
<pre>fattr4_unique_handles = class nfs_bool(packet.utils.Enum)</pre>
<h3>class ff_cb_recall_any_mask(packet.utils.Enum)</h3>
<pre>enum ff_cb_recall_any_mask</pre>
<h3>class ff_data_server4(baseobj.BaseObj)</h3>
<pre>struct ff_data_server4 {
 deviceid4 deviceid;
 uint32_t efficiency;
 stateid4 stateid;
 nfs_fh4 fh_list&lt;&gt;;
 fattr4_owner user;
 fattr4_owner_group group;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_device_addr4(baseobj.BaseObj)</h3>
<pre>struct ff_device_addr4 {
 uint32_t size; /* opaque size from device_addr4 */
 multipath_list4 netaddrs;
 ff_device_versions4 versions&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_device_versions4(baseobj.BaseObj)</h3>
<pre>struct ff_device_versions4 {
 uint32_t version;
 uint32_t minorversion;
 uint32_t rsize;
 uint32_t wsize;
 bool tightly_coupled;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_io_latency4(baseobj.BaseObj)</h3>
<pre>struct ff_io_latency4 {
 uint64_t ops_requested;
 uint64_t bytes_requested;
 uint64_t ops_completed;
 uint64_t bytes_completed;
 uint64_t bytes_not_delivered;
 nfstime4 total_busy_time;
 nfstime4 aggregate_completion_time;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_ioerr4(baseobj.BaseObj)</h3>
<pre>struct ff_ioerr4 {
 offset4 offset;
 length4 length;
 stateid4 stateid;
 device_error4 errors&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_iostats4(baseobj.BaseObj)</h3>
<pre>struct ff_iostats4 {
 offset4 offset;
 length4 length;
 stateid4 stateid;
 io_info4 read;
 io_info4 write;
 deviceid4 deviceid;
 ff_layoutupdate4 layoutupdate;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_layout4(baseobj.BaseObj)</h3>
<pre>struct ff_layout4 {
 uint32_t size; /* opaque size from layout_content4 */
 length4 stripe_unit;
 ff_mirror4 mirrors&lt;&gt;;
 ff_flags4 flags;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_layouthint4(baseobj.BaseObj)</h3>
<pre>struct ff_layouthint4 {
 ff_mirrors_hint mirrors_hint;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_layoutreturn4(baseobj.BaseObj)</h3>
<pre>struct ff_layoutreturn4 {
 uint32_t size; /* opaque size from layoutreturn_file4 */
 ff_ioerr4 ioerr_report&lt;&gt;;
 ff_iostats4 iostats_report&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_layoutupdate4(baseobj.BaseObj)</h3>
<pre>struct ff_layoutupdate4 {
 netaddr4 addr;
 nfs_fh4 fh;
 ff_io_latency4 read;
 ff_io_latency4 write;
 nfstime4 duration;
 bool local;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_mirror4(baseobj.BaseObj)</h3>
<pre>struct ff_mirror4 {
 ff_data_server4 data_servers&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ff_mirrors_hint(baseobj.BaseObj)</h3>
<pre>union switch ff_mirrors_hint (bool ffmc_valid) {
 case const.TRUE:
 uint32_t mirrors;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class filelayout_hint_care4(packet.utils.Enum)</h3>
<pre>enum filelayout_hint_care4</pre>
<h3>class fs4_status(baseobj.BaseObj)</h3>
<pre>struct fs4_status {
 bool absent;
 fs4_status_type type;
 utf8str_cs source;
 utf8str_cs current;
 int32_t age;
 nfstime4 version;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fs4_status_type(packet.utils.Enum)</h3>
<pre>enum fs4_status_type</pre>
<h3>class fs_location4(baseobj.BaseObj)</h3>
<pre>struct fs_location4 {
 utf8str_cis server&lt;&gt;;
 pathname4 root;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fs_locations4(baseobj.BaseObj)</h3>
<pre>struct fs_locations4 {
 pathname4 root;
 fs_location4 locations&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fs_locations_info4(baseobj.BaseObj)</h3>
<pre>struct fs_locations_info4 {
 uint32_t flags;
 int32_t valid_for;
 pathname4 root;
 fs_locations_item4 items&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fs_locations_item4(baseobj.BaseObj)</h3>
<pre>struct fs_locations_item4 {
 fs_locations_server4 entries&lt;&gt;;
 pathname4 root;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fs_locations_server4(baseobj.BaseObj)</h3>
<pre>struct fs_locations_server4 {
 int32_t currency;
 opaque info&lt;&gt;;
 utf8str_cis server;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fsid4(baseobj.BaseObj)</h3>
<pre>struct fsid4 {
 uint64_t major;
 uint64_t minor;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class gddrnf4_status(packet.utils.Enum)</h3>
<pre>enum gddrnf4_status</pre>
<h3>class gss_cb_handles4(baseobj.BaseObj)</h3>
<pre>struct gss_cb_handles4 {
 rpc_gss_svc_t service; /* RFC 2203 */
 gsshandle4_t server_handle;
 gsshandle4_t client_handle;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class io_info4(baseobj.BaseObj)</h3>
<pre>struct io_info4 {
 uint64_t count;
 uint64_t bytes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class labelformat_spec4(baseobj.BaseObj)</h3>
<pre>struct labelformat_spec4 {
 policy4 lfs;
 policy4 pi;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layout4(baseobj.BaseObj)</h3>
<pre>struct layout4 {
 offset4 offset;
 length4 length;
 layoutiomode4 iomode;
 layout_content4 content;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layout_content4(baseobj.BaseObj)</h3>
<pre>union switch layout_content4 (layouttype4 type) {
 case const.LAYOUT4_NFSV4_1_FILES:
 nfsv4_1_file_layout4 body;
 case const.LAYOUT4_FLEX_FILES:
 ff_layout4 body;
 default:
 /* All other types are not supported yet */
 opaque body&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layouthint4(baseobj.BaseObj)</h3>
<pre>union switch layouthint4 (layouttype4 type) {
 case const.LAYOUT4_NFSV4_1_FILES:
 nfsv4_1_file_layouthint4 body;
 case const.LAYOUT4_FLEX_FILES:
 ff_layouthint4 body;
 default:
 /* All other types are not supported yet */
 opaque body&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutiomode4(packet.utils.Enum)</h3>
<pre>enum layoutiomode4</pre>
<h3>class layoutrecall4(baseobj.BaseObj)</h3>
<pre>union switch layoutrecall4 (layoutrecall_type4 recalltype) {
 case const.LAYOUTRECALL4_FILE:
 layoutrecall_file4 layout;
 case const.LAYOUTRECALL4_FSID:
 fsid4 fsid;
 case const.LAYOUTRECALL4_ALL:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutrecall_file4(baseobj.BaseObj)</h3>
<pre>struct layoutrecall_file4 {
 nfs_fh4 fh;
 offset4 offset;
 length4 length;
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutrecall_type4(packet.utils.Enum)</h3>
<pre>enum layoutrecall_type4</pre>
<h3>class layoutreturn4(baseobj.BaseObj)</h3>
<pre>union switch layoutreturn4 (layoutreturn_type4 returntype) {
 case const.LAYOUTRETURN4_FILE:
 layoutreturn_file4 layout;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutreturn_file4(baseobj.BaseObj)</h3>
<pre>struct layoutreturn_file4 {
 offset4 offset;
 length4 length;
 stateid4 stateid;
 /* layouttype4 specific data */
 layoutreturn_file_body4 data;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutreturn_file_body4(baseobj.BaseObj)</h3>
<pre>union switch layoutreturn_file_body4 (layouttype4 nfs4_layouttype) {
 case const.LAYOUT4_FLEX_FILES:
 ff_layoutreturn4 body;
 default:
 /* All other types are not supported yet or not used */
 opaque body&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutreturn_stateid(baseobj.BaseObj)</h3>
<pre>union switch layoutreturn_stateid (bool present) {
 case const.TRUE:
 stateid4 stateid;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class layoutreturn_type4(packet.utils.Enum)</h3>
<pre>enum layoutreturn_type4</pre>
<h3>class layouttype4(packet.utils.Enum)</h3>
<pre>enum layouttype4</pre>
<h3>class layoutupdate4(baseobj.BaseObj)</h3>
<pre>struct layoutupdate4 {
 layouttype4 type;
 opaque body&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class limit_by4(packet.utils.Enum)</h3>
<pre>enum limit_by4</pre>
<h3>class lock_owner4(baseobj.BaseObj)</h3>
<pre>lock_owner4 = class state_owner4(baseobj.BaseObj)</pre>
<h3>class locker4(baseobj.BaseObj)</h3>
<pre>union switch locker4 (bool new_lock_owner) {
 case const.TRUE:
 open_to_lock_owner4 open_owner;
 case const.FALSE:
 exist_lock_owner4 lock_owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class mdsthreshold4(baseobj.BaseObj)</h3>
<pre>struct mdsthreshold4 {
 threshold_item4 hints&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class mode_masked4(baseobj.BaseObj)</h3>
<pre>struct mode_masked4 {
 mode4 values; /* Values of bits to set or reset in mode. */
 mode4 mask; /* Mask of bits to set or reset in mode. */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class netaddr4(baseobj.BaseObj)</h3>
<pre>netaddr4 = class clientaddr4(baseobj.BaseObj)</pre>
<h3>class netloc4(baseobj.BaseObj)</h3>
<pre>union switch netloc4 (netloc_type4 type) {
 case const.NL4_NAME:
 utf8str_cis name;
 case const.NL4_URL:
 utf8str_cis url;
 case const.NL4_NETADDR:
 netaddr4 addr;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class netloc_type4(packet.utils.Enum)</h3>
<pre>enum netloc_type4</pre>
<h3>class newoffset4(baseobj.BaseObj)</h3>
<pre>union switch newoffset4 (bool newoffset) {
 case const.TRUE:
 offset4 offset;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class newsize4(baseobj.BaseObj)</h3>
<pre>union switch newsize4 (bool sizechanged) {
 case const.TRUE:
 length4 size;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class newtime4(baseobj.BaseObj)</h3>
<pre>union switch newtime4 (bool timechanged) {
 case const.TRUE:
 nfstime4 time;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_argop4(baseobj.BaseObj)</h3>
<pre>union switch nfs_argop4 (nfs_opnum4 argop) {
 case const.OP_ACCESS:
 ACCESS4args opaccess;
 case const.OP_CLOSE:
 CLOSE4args opclose;
 case const.OP_COMMIT:
 COMMIT4args opcommit;
 case const.OP_CREATE:
 CREATE4args opcreate;
 case const.OP_DELEGPURGE:
 DELEGPURGE4args opdelegpurge;
 case const.OP_DELEGRETURN:
 DELEGRETURN4args opdelegreturn;
 case const.OP_GETATTR:
 GETATTR4args opgetattr;
 case const.OP_GETFH:
 void;
 case const.OP_LINK:
 LINK4args oplink;
 case const.OP_LOCK:
 LOCK4args oplock;
 case const.OP_LOCKT:
 LOCKT4args oplockt;
 case const.OP_LOCKU:
 LOCKU4args oplocku;
 case const.OP_LOOKUP:
 LOOKUP4args oplookup;
 case const.OP_LOOKUPP:
 void;
 case const.OP_NVERIFY:
 NVERIFY4args opnverify;
 case const.OP_OPEN:
 OPEN4args opopen;
 case const.OP_OPENATTR:
 OPENATTR4args opopenattr;
 case const.OP_OPEN_CONFIRM:
 /* Not used in NFSv4.1 */
 OPEN_CONFIRM4args opopen_confirm;
 case const.OP_OPEN_DOWNGRADE:
 OPEN_DOWNGRADE4args opopen_downgrade;
 case const.OP_PUTFH:
 PUTFH4args opputfh;
 case const.OP_PUTPUBFH:
 void;
 case const.OP_PUTROOTFH:
 void;
 case const.OP_READ:
 READ4args opread;
 case const.OP_READDIR:
 READDIR4args opreaddir;
 case const.OP_READLINK:
 void;
 case const.OP_REMOVE:
 REMOVE4args opremove;
 case const.OP_RENAME:
 RENAME4args oprename;
 case const.OP_RENEW:
 /* Not used in NFSv4.1 */
 RENEW4args oprenew;
 case const.OP_RESTOREFH:
 void;
 case const.OP_SAVEFH:
 void;
 case const.OP_SECINFO:
 SECINFO4args opsecinfo;
 case const.OP_SETATTR:
 SETATTR4args opsetattr;
 case const.OP_SETCLIENTID:
 /* Not used in NFSv4.1 */
 SETCLIENTID4args opsetclientid;
 case const.OP_SETCLIENTID_CONFIRM:
 /* Not used in NFSv4.1 */
 SETCLIENTID_CONFIRM4args opsetclientid_confirm;
 case const.OP_VERIFY:
 VERIFY4args opverify;
 case const.OP_WRITE:
 WRITE4args opwrite;
 case const.OP_RELEASE_LOCKOWNER:
 /* Not used in NFSv4.1 */
 RELEASE_LOCKOWNER4args oprelease_lockowner;
 /*
 * New to NFSv4.1
 */
 case const.OP_BACKCHANNEL_CTL:
 BACKCHANNEL_CTL4args opbackchannel_ctl;
 case const.OP_BIND_CONN_TO_SESSION:
 BIND_CONN_TO_SESSION4args opbind_conn_to_session;
 case const.OP_EXCHANGE_ID:
 EXCHANGE_ID4args opexchange_id;
 case const.OP_CREATE_SESSION:
 CREATE_SESSION4args opcreate_session;
 case const.OP_DESTROY_SESSION:
 DESTROY_SESSION4args opdestroy_session;
 case const.OP_FREE_STATEID:
 FREE_STATEID4args opfree_stateid;
 case const.OP_GET_DIR_DELEGATION:
 GET_DIR_DELEGATION4args opget_dir_delegation;
 case const.OP_GETDEVICEINFO:
 GETDEVICEINFO4args opgetdeviceinfo;
 case const.OP_GETDEVICELIST:
 /* Not used in NFSv4.2 */
 GETDEVICELIST4args opgetdevicelist;
 case const.OP_LAYOUTCOMMIT:
 LAYOUTCOMMIT4args oplayoutcommit;
 case const.OP_LAYOUTGET:
 LAYOUTGET4args oplayoutget;
 case const.OP_LAYOUTRETURN:
 LAYOUTRETURN4args oplayoutreturn;
 case const.OP_SECINFO_NO_NAME:
 SECINFO_NO_NAME4args opsecinfo_no_name;
 case const.OP_SEQUENCE:
 SEQUENCE4args opsequence;
 case const.OP_SET_SSV:
 SET_SSV4args opset_ssv;
 case const.OP_TEST_STATEID:
 TEST_STATEID4args optest_stateid;
 case const.OP_WANT_DELEGATION:
 WANT_DELEGATION4args opwant_delegation;
 case const.OP_DESTROY_CLIENTID:
 DESTROY_CLIENTID4args opdestroy_clientid;
 case const.OP_RECLAIM_COMPLETE:
 RECLAIM_COMPLETE4args opreclaim_complete;
 /*
 * New to NFSv4.2
 */
 case const.OP_ALLOCATE:
 ALLOCATE4args opallocate;
 case const.OP_COPY:
 COPY4args opcopy;
 case const.OP_COPY_NOTIFY:
 COPY_NOTIFY4args opcopy_notify;
 case const.OP_DEALLOCATE:
 DEALLOCATE4args opdeallocate;
 case const.OP_IO_ADVISE:
 IO_ADVISE4args opio_advise;
 case const.OP_LAYOUTERROR:
 LAYOUTERROR4args oplayouterror;
 case const.OP_LAYOUTSTATS:
 LAYOUTSTATS4args oplayoutstats;
 case const.OP_OFFLOAD_CANCEL:
 OFFLOAD_CANCEL4args opoffload_cancel;
 case const.OP_OFFLOAD_STATUS:
 OFFLOAD_STATUS4args opoffload_status;
 case const.OP_READ_PLUS:
 READ_PLUS4args opread_plus;
 case const.OP_SEEK:
 SEEK4args opseek;
 case const.OP_WRITE_SAME:
 WRITE_SAME4args opwrite_same;
 case const.OP_CLONE:
 CLONE4args opclone;
 case const.OP_ILLEGAL:
 /* Illegal operation */
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_bool(packet.utils.Enum)</h3>
<pre>enum nfs_bool</pre>
<h3>class nfs_cb_argop4(baseobj.BaseObj)</h3>
<pre>union switch nfs_cb_argop4 (nfs_cb_opnum4 argop) {
 case const.OP_CB_GETATTR:
 CB_GETATTR4args opcbgetattr;
 case const.OP_CB_RECALL:
 CB_RECALL4args opcbrecall;
 /*
 * New to NFSv4.1
 */
 case const.OP_CB_LAYOUTRECALL:
 CB_LAYOUTRECALL4args opcblayoutrecall;
 case const.OP_CB_NOTIFY:
 CB_NOTIFY4args opcbnotify;
 case const.OP_CB_PUSH_DELEG:
 CB_PUSH_DELEG4args opcbpush_deleg;
 case const.OP_CB_RECALL_ANY:
 CB_RECALL_ANY4args opcbrecall_any;
 case const.OP_CB_RECALLABLE_OBJ_AVAIL:
 CB_RECALLABLE_OBJ_AVAIL4args opcbrecallable_obj_avail;
 case const.OP_CB_RECALL_SLOT:
 CB_RECALL_SLOT4args opcbrecall_slot;
 case const.OP_CB_SEQUENCE:
 CB_SEQUENCE4args opcbsequence;
 case const.OP_CB_WANTS_CANCELLED:
 CB_WANTS_CANCELLED4args opcbwants_cancelled;
 case const.OP_CB_NOTIFY_LOCK:
 CB_NOTIFY_LOCK4args opcbnotify_lock;
 case const.OP_CB_NOTIFY_DEVICEID:
 CB_NOTIFY_DEVICEID4args opcbnotify_deviceid;
 /*
 * New to NFSv4.2
 */
 case const.OP_CB_OFFLOAD:
 CB_OFFLOAD4args opcboffload;
 case const.OP_CB_ILLEGAL:
 /* Illegal callback operation */
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_cb_opnum4(packet.utils.Enum)</h3>
<pre>enum nfs_cb_opnum4</pre>
<h3>class nfs_cb_resop4(baseobj.BaseObj)</h3>
<pre>union switch nfs_cb_resop4 (nfs_cb_opnum4 resop) {
 case const.OP_CB_GETATTR:
 CB_GETATTR4res opcbgetattr;
 case const.OP_CB_RECALL:
 CB_RECALL4res opcbrecall;
 /*
 * New to NFSv4.1
 */
 case const.OP_CB_LAYOUTRECALL:
 CB_LAYOUTRECALL4res opcblayoutrecall;
 case const.OP_CB_NOTIFY:
 CB_NOTIFY4res opcbnotify;
 case const.OP_CB_PUSH_DELEG:
 CB_PUSH_DELEG4res opcbpush_deleg;
 case const.OP_CB_RECALL_ANY:
 CB_RECALL_ANY4res opcbrecall_any;
 case const.OP_CB_RECALLABLE_OBJ_AVAIL:
 CB_RECALLABLE_OBJ_AVAIL4res opcbrecallable_obj_avail;
 case const.OP_CB_RECALL_SLOT:
 CB_RECALL_SLOT4res opcbrecall_slot;
 case const.OP_CB_SEQUENCE:
 CB_SEQUENCE4res opcbsequence;
 case const.OP_CB_WANTS_CANCELLED:
 CB_WANTS_CANCELLED4res opcbwants_cancelled;
 case const.OP_CB_NOTIFY_LOCK:
 CB_NOTIFY_LOCK4res opcbnotify_lock;
 case const.OP_CB_NOTIFY_DEVICEID:
 CB_NOTIFY_DEVICEID4res opcbnotify_deviceid;
 /*
 * New to NFSv4.2
 */
 case const.OP_CB_OFFLOAD:
 CB_OFFLOAD4res opcboffload;
 case const.OP_CB_ILLEGAL:
 /* Illegal callback operation */
 CB_ILLEGAL4res opcbillegal;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_client_id4(baseobj.BaseObj)</h3>
<pre>struct nfs_client_id4 {
 verifier4 verifier;
 opaque id&lt;NFS4_OPAQUE_LIMIT&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_fattr4(packet.utils.Enum)</h3>
<pre>enum nfs_fattr4</pre>
<h3>class nfs_ftype4(packet.utils.Enum)</h3>
<pre>enum nfs_ftype4</pre>
<h3>class nfs_impl_id4(baseobj.BaseObj)</h3>
<pre>struct nfs_impl_id4 {
 utf8str_cis domain;
 utf8str_cs name;
 nfstime4 date;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_lock_type4(packet.utils.Enum)</h3>
<pre>enum nfs_lock_type4</pre>
<h3>class nfs_modified_limit4(baseobj.BaseObj)</h3>
<pre>struct nfs_modified_limit4 {
 uint32_t num_blocks;
 uint32_t bytes_per_block;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_opnum4(packet.utils.Enum)</h3>
<pre>enum nfs_opnum4</pre>
<h3>class nfs_resop4(baseobj.BaseObj)</h3>
<pre>union switch nfs_resop4 (nfs_opnum4 resop) {
 case const.OP_ACCESS:
 ACCESS4res opaccess;
 case const.OP_CLOSE:
 CLOSE4res opclose;
 case const.OP_COMMIT:
 COMMIT4res opcommit;
 case const.OP_CREATE:
 CREATE4res opcreate;
 case const.OP_DELEGPURGE:
 DELEGPURGE4res opdelegpurge;
 case const.OP_DELEGRETURN:
 DELEGRETURN4res opdelegreturn;
 case const.OP_GETATTR:
 GETATTR4res opgetattr;
 case const.OP_GETFH:
 GETFH4res opgetfh;
 case const.OP_LINK:
 LINK4res oplink;
 case const.OP_LOCK:
 LOCK4res oplock;
 case const.OP_LOCKT:
 LOCKT4res oplockt;
 case const.OP_LOCKU:
 LOCKU4res oplocku;
 case const.OP_LOOKUP:
 LOOKUP4res oplookup;
 case const.OP_LOOKUPP:
 LOOKUPP4res oplookupp;
 case const.OP_NVERIFY:
 NVERIFY4res opnverify;
 case const.OP_OPEN:
 OPEN4res opopen;
 case const.OP_OPENATTR:
 OPENATTR4res opopenattr;
 case const.OP_OPEN_CONFIRM:
 /* Not used in NFSv4.1 */
 OPEN_CONFIRM4res opopen_confirm;
 case const.OP_OPEN_DOWNGRADE:
 OPEN_DOWNGRADE4res opopen_downgrade;
 case const.OP_PUTFH:
 PUTFH4res opputfh;
 case const.OP_PUTPUBFH:
 PUTPUBFH4res opputpubfh;
 case const.OP_PUTROOTFH:
 PUTROOTFH4res opputrootfh;
 case const.OP_READ:
 READ4res opread;
 case const.OP_READDIR:
 READDIR4res opreaddir;
 case const.OP_READLINK:
 READLINK4res opreadlink;
 case const.OP_REMOVE:
 REMOVE4res opremove;
 case const.OP_RENAME:
 RENAME4res oprename;
 case const.OP_RENEW:
 /* Not used in NFSv4.1 */
 RENEW4res oprenew;
 case const.OP_RESTOREFH:
 RESTOREFH4res oprestorefh;
 case const.OP_SAVEFH:
 SAVEFH4res opsavefh;
 case const.OP_SECINFO:
 SECINFO4res opsecinfo;
 case const.OP_SETATTR:
 SETATTR4res opsetattr;
 case const.OP_SETCLIENTID:
 /* Not used in NFSv4.1 */
 SETCLIENTID4res opsetclientid;
 case const.OP_SETCLIENTID_CONFIRM:
 /* Not used in NFSv4.1 */
 SETCLIENTID_CONFIRM4res opsetclientid_confirm;
 case const.OP_VERIFY:
 VERIFY4res opverify;
 case const.OP_WRITE:
 WRITE4res opwrite;
 case const.OP_RELEASE_LOCKOWNER:
 /* Not used in NFSv4.1 */
 RELEASE_LOCKOWNER4res oprelease_lockowner;
 /*
 * New to NFSv4.1
 */
 case const.OP_BACKCHANNEL_CTL:
 BACKCHANNEL_CTL4res opbackchannel_ctl;
 case const.OP_BIND_CONN_TO_SESSION:
 BIND_CONN_TO_SESSION4res opbind_conn_to_session;
 case const.OP_EXCHANGE_ID:
 EXCHANGE_ID4res opexchange_id;
 case const.OP_CREATE_SESSION:
 CREATE_SESSION4res opcreate_session;
 case const.OP_DESTROY_SESSION:
 DESTROY_SESSION4res opdestroy_session;
 case const.OP_FREE_STATEID:
 FREE_STATEID4res opfree_stateid;
 case const.OP_GET_DIR_DELEGATION:
 GET_DIR_DELEGATION4res opget_dir_delegation;
 case const.OP_GETDEVICEINFO:
 GETDEVICEINFO4res opgetdeviceinfo;
 case const.OP_GETDEVICELIST:
 /* Not used in NFSv4.2 */
 GETDEVICELIST4res opgetdevicelist;
 case const.OP_LAYOUTCOMMIT:
 LAYOUTCOMMIT4res oplayoutcommit;
 case const.OP_LAYOUTGET:
 LAYOUTGET4res oplayoutget;
 case const.OP_LAYOUTRETURN:
 LAYOUTRETURN4res oplayoutreturn;
 case const.OP_SECINFO_NO_NAME:
 SECINFO_NO_NAME4res opsecinfo_no_name;
 case const.OP_SEQUENCE:
 SEQUENCE4res opsequence;
 case const.OP_SET_SSV:
 SET_SSV4res opset_ssv;
 case const.OP_TEST_STATEID:
 TEST_STATEID4res optest_stateid;
 case const.OP_WANT_DELEGATION:
 WANT_DELEGATION4res opwant_delegation;
 case const.OP_DESTROY_CLIENTID:
 DESTROY_CLIENTID4res opdestroy_clientid;
 case const.OP_RECLAIM_COMPLETE:
 RECLAIM_COMPLETE4res opreclaim_complete;
 /*
 * New to NFSv4.2
 */
 case const.OP_ALLOCATE:
 ALLOCATE4res opallocate;
 case const.OP_COPY:
 COPY4res opcopy;
 case const.OP_COPY_NOTIFY:
 COPY_NOTIFY4res opcopy_notify;
 case const.OP_DEALLOCATE:
 DEALLOCATE4res opdeallocate;
 case const.OP_IO_ADVISE:
 IO_ADVISE4res opio_advise;
 case const.OP_LAYOUTERROR:
 LAYOUTERROR4res oplayouterror;
 case const.OP_LAYOUTSTATS:
 LAYOUTSTATS4res oplayoutstats;
 case const.OP_OFFLOAD_CANCEL:
 OFFLOAD_CANCEL4res opoffload_cancel;
 case const.OP_OFFLOAD_STATUS:
 OFFLOAD_STATUS4res opoffload_status;
 case const.OP_READ_PLUS:
 READ_PLUS4res opread_plus;
 case const.OP_SEEK:
 SEEK4res opseek;
 case const.OP_WRITE_SAME:
 WRITE_SAME4res opwrite_same;
 case const.OP_CLONE:
 CLONE4res opclone;
 case const.OP_ILLEGAL:
 /* Illegal operation */
 ILLEGAL4res opillegal;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_secflavor4(packet.utils.Enum)</h3>
<pre>enum nfs_secflavor4</pre>
<h3>class nfs_space_limit4(baseobj.BaseObj)</h3>
<pre>union switch nfs_space_limit4 (limit_by4 limitby) {
 /* limit specified as file size */
 case const.NFS_LIMIT_SIZE:
 uint64_t filesize;
 /* limit specified by number of blocks */
 case const.NFS_LIMIT_BLOCKS:
 nfs_modified_limit4 mod_blocks;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsace4(baseobj.BaseObj)</h3>
<pre>struct nfsace4 {
 acetype4 type;
 aceflag4 flag;
 acemask4 mask;
 utf8str_mixed who;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsacl41(baseobj.BaseObj)</h3>
<pre>struct nfsacl41 {
 aclflag4 flag;
 nfsace4 aces&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsstat4(packet.utils.Enum)</h3>
<pre>enum nfsstat4</pre>
<h3>class nfstime4(baseobj.BaseObj)</h3>
<pre>struct nfstime4 {
 int64_t seconds;
 uint32_t nseconds;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsv4_1_file_layout4(baseobj.BaseObj)</h3>
<pre>struct nfsv4_1_file_layout4 {
 uint32_t size; /* opaque size from layout_content4 */
 deviceid4 deviceid;
 nfl_util4 nfl_util;
 uint32_t first_stripe_index;
 offset4 pattern_offset;
 nfs_fh4 fh_list&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsv4_1_file_layout_ds_addr4(baseobj.BaseObj)</h3>
<pre>struct nfsv4_1_file_layout_ds_addr4 {
 uint32_t size; /* opaque size from device_addr4 */
 uint32_t stripe_indices&lt;&gt;;
 multipath_list4 multipath_ds_list&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfsv4_1_file_layouthint4(baseobj.BaseObj)</h3>
<pre>struct nfsv4_1_file_layouthint4 {
 uint32_t size; /* opaque size from layouthint4 */
 uint32_t care;
 nfl_util4 nfl_util;
 count4 stripe_count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify4(baseobj.BaseObj)</h3>
<pre>struct notify4 {
 /* composed from notify_type4 or notify_deviceid_type4 */
 bitmap4 mask;
 notifylist4 values;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_add4(baseobj.BaseObj)</h3>
<pre>struct notify_add4 {
 /*
 * Information on object
 * possibly renamed over.
 */
 notify_remove4 old_entry&lt;1&gt;;
 notify_entry4 new_entry;
 /* what READDIR would have returned for this entry */
 nfs_cookie4 new_cookie&lt;1&gt;;
 prev_entry4 prev_entry&lt;1&gt;;
 bool last_entry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_attr4(baseobj.BaseObj)</h3>
<pre>struct notify_attr4 {
 notify_entry4 entry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_deviceid_change4(baseobj.BaseObj)</h3>
<pre>struct notify_deviceid_change4 {
 layouttype4 type;
 deviceid4 deviceid;
 bool immediate;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_deviceid_delete4(baseobj.BaseObj)</h3>
<pre>struct notify_deviceid_delete4 {
 layouttype4 type;
 deviceid4 deviceid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_deviceid_type4(packet.utils.Enum)</h3>
<pre>enum notify_deviceid_type4</pre>
<h3>class notify_entry4(baseobj.BaseObj)</h3>
<pre>struct notify_entry4 {
 component4 name;
 fattr4 attrs;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_remove4(baseobj.BaseObj)</h3>
<pre>struct notify_remove4 {
 notify_entry4 entry;
 nfs_cookie4 cookie;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_rename4(baseobj.BaseObj)</h3>
<pre>struct notify_rename4 {
 notify_remove4 old_entry;
 notify_add4 new_entry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class notify_type4(packet.utils.Enum)</h3>
<pre>enum notify_type4</pre>
<h3>class notify_verifier4(baseobj.BaseObj)</h3>
<pre>struct notify_verifier4 {
 verifier4 old_verifier;
 verifier4 new_verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class offload_info4(baseobj.BaseObj)</h3>
<pre>union switch offload_info4 (nfsstat4 status) {
 case const.NFS4_OK:
 write_response4 resok;
 default:
 length4 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_claim4(baseobj.BaseObj)</h3>
<pre>union switch open_claim4 (open_claim_type4 claim) {
 /*
 * No special rights to file.
 * Ordinary OPEN of the specified file.
 */
 case const.CLAIM_NULL:
 /* CURRENT_FH: directory */
 component4 name;
 /*
 * Right to the file established by an
 * open previous to server reboot. File
 * identified by filehandle obtained at
 * that time rather than by name.
 */
 case const.CLAIM_PREVIOUS:
 /* CURRENT_FH: file being reclaimed */
 open_delegation_type4 deleg_type;
 /*
 * Right to file based on a delegation
 * granted by the server. File is
 * specified by name.
 */
 case const.CLAIM_DELEGATE_CUR:
 /* CURRENT_FH: directory */
 open_claim_delegate_cur4 deleg_info;
 /*
 * Right to file based on a delegation
 * granted to a previous boot instance
 * of the client. File is specified by name.
 */
 case const.CLAIM_DELEGATE_PREV:
 /* CURRENT_FH: directory */
 component4 name;
 /*
 * Like CLAIM_NULL. No special rights
 * to file. Ordinary OPEN of the
 * specified file by current filehandle.
 */
 case const.CLAIM_FH: /* New to NFSv4.1 */
 /* CURRENT_FH: regular file to open */
 void;
 /*
 * Like CLAIM_DELEGATE_PREV. Right to file based on a
 * delegation granted to a previous boot
 * instance of the client. File is identified by
 * by filehandle.
 */
 case const.CLAIM_DELEG_PREV_FH: /* New to NFSv4.1 */
 /* CURRENT_FH: file being opened */
 void;
 /*
 * Like CLAIM_DELEGATE_CUR. Right to file based on
 * a delegation granted by the server.
 * File is identified by filehandle.
 */
 case const.CLAIM_DELEG_CUR_FH: /* New to NFSv4.1 */
 /* CURRENT_FH: file being opened */
 stateid4 stateid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_claim_delegate_cur4(baseobj.BaseObj)</h3>
<pre>struct open_claim_delegate_cur4 {
 stateid4 stateid;
 component4 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_claim_type4(packet.utils.Enum)</h3>
<pre>enum open_claim_type4</pre>
<h3>class open_delegation4(baseobj.BaseObj)</h3>
<pre>union switch open_delegation4 (open_delegation_type4 deleg_type) {
 case const.OPEN_DELEGATE_NONE:
 void;
 case const.OPEN_DELEGATE_READ:
 open_read_delegation4 read;
 case const.OPEN_DELEGATE_WRITE:
 open_write_delegation4 write;
 case const.OPEN_DELEGATE_NONE_EXT: /* New to NFSv4.1 */
 open_none_delegation4 whynone;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_delegation_type4(packet.utils.Enum)</h3>
<pre>enum open_delegation_type4</pre>
<h3>class open_none_delegation4(baseobj.BaseObj)</h3>
<pre>union switch open_none_delegation4 (why_no_delegation4 why) {
 case const.WND4_CONTENTION:
 /* Server will push delegation */
 bool push;
 case const.WND4_RESOURCE:
 /* Server will signal availability */
 bool signal;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_owner4(baseobj.BaseObj)</h3>
<pre>open_owner4 = class state_owner4(baseobj.BaseObj)</pre>
<h3>class open_read_delegation4(baseobj.BaseObj)</h3>
<pre>struct open_read_delegation4 {
 stateid4 stateid; /* Stateid for delegation */
 bool recall; /* Pre-recalled flag for delegations obtained by reclaim (CLAIM_PREVIOUS) */
 nfsace4 permissions; /* Defines users who don't need an ACCESS call to open for read */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_to_lock_owner4(baseobj.BaseObj)</h3>
<pre>struct open_to_lock_owner4 {
 seqid4 seqid;
 stateid4 stateid;
 seqid4 lock_seqid;
 lock_owner4 lock_owner;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class open_write_delegation4(baseobj.BaseObj)</h3>
<pre>struct open_write_delegation4 {
 stateid4 stateid; /* Stateid for delegation */
 bool recall; /* Pre-recalled flag for delegations obtained by reclaim (CLAIM_PREVIOUS) */
 nfs_space_limit4 space_limit; /* Defines condition that the client must check to determine whether the file needs to be flushed to the server on close. */
 nfsace4 permissions; /* Defines users who don't need an ACCESS call as part of a delegated open. */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class openflag4(baseobj.BaseObj)</h3>
<pre>union switch openflag4 (opentype4 opentype) {
 case const.OPEN4_CREATE:
 createhow4 how;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class opentype4(packet.utils.Enum)</h3>
<pre>enum opentype4</pre>
<h3>class prev_entry4(baseobj.BaseObj)</h3>
<pre>struct prev_entry4 {
 notify_entry4 entry;
 /* what READDIR returned for this entry */
 nfs_cookie4 cookie;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class read_plus_content(baseobj.BaseObj)</h3>
<pre>union switch read_plus_content (data_content4 content) {
 case const.NFS4_CONTENT_DATA:
 data4 data;
 case const.NFS4_CONTENT_HOLE:
 data_info4 hole;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class read_plus_res4(baseobj.BaseObj)</h3>
<pre>struct read_plus_res4 {
 bool eof;
 read_plus_content contents&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class referring_call4(baseobj.BaseObj)</h3>
<pre>struct referring_call4 {
 sequenceid4 sequenceid;
 slotid4 slotid;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class referring_call_list4(baseobj.BaseObj)</h3>
<pre>struct referring_call_list4 {
 sessionid4 sessionid;
 referring_call4 referring_calls&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class retention_get4(baseobj.BaseObj)</h3>
<pre>struct retention_get4 {
 uint64_t duration;
 nfstime4 begin_time&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class retention_set4(baseobj.BaseObj)</h3>
<pre>struct retention_set4 {
 bool enable;
 uint64_t duration&lt;1&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class rpc_gss_svc_t(packet.utils.Enum)</h3>
<pre>enum rpc_gss_svc_t</pre>
<h3>class rpcsec_gss_info(baseobj.BaseObj)</h3>
<pre>struct rpcsec_gss_info {
 sec_oid4 oid;
 qop4 qop;
 rpc_gss_svc_t service;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class sec_label4(baseobj.BaseObj)</h3>
<pre>struct sec_label4 {
 labelformat_spec4 lfs;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class secinfo4(baseobj.BaseObj)</h3>
<pre>union switch secinfo4 (nfs_secflavor4 flavor) {
 case const.RPCSEC_GSS:
 rpcsec_gss_info info;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class secinfo_style4(packet.utils.Enum)</h3>
<pre>enum secinfo_style4</pre>
<h3>class seek_res4(baseobj.BaseObj)</h3>
<pre>struct seek_res4 {
 bool eof;
 offset4 offset;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class server_owner4(baseobj.BaseObj)</h3>
<pre>struct server_owner4 {
 uint64_t minor_id;
 opaque major_id&lt;NFS4_OPAQUE_LIMIT&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class settime4(baseobj.BaseObj)</h3>
<pre>union switch settime4 (time_how4 set_it) {
 case const.SET_TO_CLIENT_TIME4:
 nfstime4 time;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class specdata4(baseobj.BaseObj)</h3>
<pre>struct specdata4 {
 uint32_t specdata1; /* major device number */
 uint32_t specdata2; /* minor device number */
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssa_digest_input4(baseobj.BaseObj)</h3>
<pre>struct ssa_digest_input4 {
 SEQUENCE4args seqargs;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssr_digest_input4(baseobj.BaseObj)</h3>
<pre>struct ssr_digest_input4 {
 SEQUENCE4res seqres;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_mic_plain_tkn4(baseobj.BaseObj)</h3>
<pre>struct ssv_mic_plain_tkn4 {
 uint32_t ssv_seq;
 opaque orig_plain&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_mic_tkn4(baseobj.BaseObj)</h3>
<pre>struct ssv_mic_tkn4 {
 uint32_t ssv_seq;
 opaque hmac&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_prot_info4(baseobj.BaseObj)</h3>
<pre>struct ssv_prot_info4 {
 state_protect_ops4 ops;
 uint32_t hash_alg;
 uint32_t encr_alg;
 uint32_t ssv_len;
 uint32_t window;
 gsshandle4_t handles&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_seal_cipher_tkn4(baseobj.BaseObj)</h3>
<pre>struct ssv_seal_cipher_tkn4 {
 uint32_t ssv_seq;
 opaque iv&lt;&gt;;
 opaque encr_data&lt;&gt;;
 opaque hmac&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_seal_plain_tkn4(baseobj.BaseObj)</h3>
<pre>struct ssv_seal_plain_tkn4 {
 opaque confounder&lt;&gt;;
 uint32_t ssv_seq;
 opaque orig_plain&lt;&gt;;
 opaque pad&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_sp_parms4(baseobj.BaseObj)</h3>
<pre>struct ssv_sp_parms4 {
 state_protect_ops4 ops;
 sec_oid4 hash_algs&lt;&gt;;
 sec_oid4 encr_algs&lt;&gt;;
 uint32_t window;
 uint32_t num_gss_handles;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ssv_subkey4(packet.utils.Enum)</h3>
<pre>enum ssv_subkey4</pre>
<h3>class stable_how4(packet.utils.Enum)</h3>
<pre>enum stable_how4</pre>
<h3>class state_owner4(baseobj.BaseObj)</h3>
<pre>struct state_owner4 {
 clientid4 clientid;
 opaque owner&lt;NFS4_OPAQUE_LIMIT&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class state_protect4_a(baseobj.BaseObj)</h3>
<pre>union switch state_protect4_a (state_protect_how4 how) {
 case const.SP4_NONE:
 void;
 case const.SP4_MACH_CRED:
 state_protect_ops4 mach_ops;
 case const.SP4_SSV:
 ssv_sp_parms4 ssv_parms;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class state_protect4_r(baseobj.BaseObj)</h3>
<pre>union switch state_protect4_r (state_protect_how4 how) {
 case const.SP4_NONE:
 void;
 case const.SP4_MACH_CRED:
 state_protect_ops4 mach_ops;
 case const.SP4_SSV:
 ssv_prot_info4 ssv_info;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class state_protect_how4(packet.utils.Enum)</h3>
<pre>enum state_protect_how4</pre>
<h3>class state_protect_ops4(baseobj.BaseObj)</h3>
<pre>struct state_protect_ops4 {
 bitmap4 enforce;
 bitmap4 allow;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class stateid4(baseobj.BaseObj)</h3>
<pre>struct stateid4 {
 uint32_t seqid;
 opaque other[NFS4_OTHER_SIZE];
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class threshold_item4(baseobj.BaseObj)</h3>
<pre>struct threshold_item4 {
 layouttype4 type;
 bitmap4 mask;
 opaque values&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class time_how4(packet.utils.Enum)</h3>
<pre>enum time_how4</pre>
<h3>class why_no_delegation4(packet.utils.Enum)</h3>
<pre>enum why_no_delegation4</pre>
<h3>class write_response4(baseobj.BaseObj)</h3>
<pre>struct write_response4 {
 stateid4 callback_id&lt;1&gt;;
 length4 count;
 stable_how4 committed;
 verifier4 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h2>Functions</h2>
<h3>SECINFO4resok(unpack)</h3>
<h3>aceflag4(unpack)</h3>
<h3>acemask4(unpack)</h3>
<h3>acetype4(unpack)</h3>
<h3>aclflag4(unpack)</h3>
<h3>bitmap4(unpack)</h3>
<h3>changeid4(unpack)</h3>
<h3>clientid4(unpack)</h3>
<h3>deviceid4(unpack)</h3>
<h3>fattr4(unpack)</h3>
<p>struct fattr4 {<br />
&nbsp;<wbr>bitmap4&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>mask;<br />
&nbsp;<wbr>attrlist4 values; };</p>
<h3>fattr4_acl(unpack)</h3>
<h3>fattr4_change(unpack)</h3>
<h3>fattr4_filehandle(unpack)</h3>
<h3>fattr4_fs_layout_types(unpack)</h3>
<h3>fattr4_layout_types(unpack)</h3>
<h3>fattr4_suppattr_exclcreat(unpack)</h3>
<h3>fattr4_supported_attrs(unpack)</h3>
<h3>gsshandle4_t(unpack)</h3>
<h3>multipath_list4(unpack)</h3>
<h3>nfl_util4(unpack)</h3>
<h3>nfs_fh4(unpack)</h3>
<h3>notifylist4(unpack)</h3>
<p>&nbsp;<wbr>Objects of type notify_&lt;&gt;4 and<br />
&nbsp;<wbr>notify_device_&lt;&gt;4 are encoded in this.</p>
<h3>pathname4(unpack)</h3>
<h3>sec_oid4(unpack)</h3>
<h3>sessionid4(unpack)</h3>
<h3>verifier4(unpack)</h3>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-nfs-nfsbase/">packet.nfs.nfsbase</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
