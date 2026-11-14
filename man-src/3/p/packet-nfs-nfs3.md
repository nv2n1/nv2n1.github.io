---
title: "packet-nfs-nfs3(3)"
name: "packet-nfs-nfs3"
section: "3"
letter: "p"
url: "/docs/linux/man/3-packet-nfs-nfs3/"
description: "packet.nfs.nfs3 – NFSv3 decoding module"
---

<p>packet.nfs.nfs3 &#8211; NFSv3 decoding module</p>
<h2>Classes</h2>
<h3>class ACCESS3args(baseobj.BaseObj)</h3>
<pre>struct ACCESS3args {
 nfs_fh3 fh;
 access3 access;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ACCESS3res(baseobj.BaseObj)</h3>
<pre>union switch ACCESS3res (nfsstat3 status) {
 case const.NFS3_OK:
 ACCESS3resok resok;
 default:
 ACCESS3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ACCESS3resfail(baseobj.BaseObj)</h3>
<pre>struct ACCESS3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ACCESS3resok(baseobj.BaseObj)</h3>
<pre>struct ACCESS3resok {
 post_op_attr attributes;
 access3 access;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT3args(baseobj.BaseObj)</h3>
<pre>struct COMMIT3args {
 nfs_fh3 fh;
 offset3 offset;
 count3 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT3res(baseobj.BaseObj)</h3>
<pre>union switch COMMIT3res (nfsstat3 status) {
 case const.NFS3_OK:
 COMMIT3resok resok;
 default:
 COMMIT3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT3resfail(baseobj.BaseObj)</h3>
<pre>struct COMMIT3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class COMMIT3resok(baseobj.BaseObj)</h3>
<pre>struct COMMIT3resok {
 wcc_data wcc;
 writeverf3 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE3args(baseobj.BaseObj)</h3>
<pre>struct CREATE3args {
 diropargs3 where;
 createhow3 how;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE3res(baseobj.BaseObj)</h3>
<pre>union switch CREATE3res (nfsstat3 status) {
 case const.NFS3_OK:
 CREATE3resok resok;
 default:
 CREATE3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE3resfail(baseobj.BaseObj)</h3>
<pre>struct CREATE3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class CREATE3resok(baseobj.BaseObj)</h3>
<pre>struct CREATE3resok {
 post_op_fh3 obj;
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSINFO3args(baseobj.BaseObj)</h3>
<pre>struct FSINFO3args {
 nfs_fh3 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSINFO3res(baseobj.BaseObj)</h3>
<pre>union switch FSINFO3res (nfsstat3 status) {
 case const.NFS3_OK:
 FSINFO3resok resok;
 default:
 FSINFO3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSINFO3resfail(baseobj.BaseObj)</h3>
<pre>struct FSINFO3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSINFO3resok(baseobj.BaseObj)</h3>
<pre>struct FSINFO3resok {
 post_op_attr attributes;
 uint32 rtmax;
 uint32 rtpref;
 uint32 rtmult;
 uint32 wtmax;
 uint32 wtpref;
 uint32 wtmult;
 uint32 dtpref;
 size3 maxfilesize;
 nfstime3 time_delta;
 uint32 properties;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSSTAT3args(baseobj.BaseObj)</h3>
<pre>struct FSSTAT3args {
 nfs_fh3 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSSTAT3res(baseobj.BaseObj)</h3>
<pre>union switch FSSTAT3res (nfsstat3 status) {
 case const.NFS3_OK:
 FSSTAT3resok resok;
 default:
 FSSTAT3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSSTAT3resfail(baseobj.BaseObj)</h3>
<pre>struct FSSTAT3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class FSSTAT3resok(baseobj.BaseObj)</h3>
<pre>struct FSSTAT3resok {
 post_op_attr attributes;
 size3 tbytes;
 size3 fbytes;
 size3 abytes;
 size3 tfiles;
 size3 ffiles;
 size3 afiles;
 uint32 invarsec;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR3args(baseobj.BaseObj)</h3>
<pre>struct GETATTR3args {
 nfs_fh3 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR3res(baseobj.BaseObj)</h3>
<pre>union switch GETATTR3res (nfsstat3 status) {
 case const.NFS3_OK:
 GETATTR3resok resok;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class GETATTR3resok(baseobj.BaseObj)</h3>
<pre>struct GETATTR3resok {
 fattr3 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK3args(baseobj.BaseObj)</h3>
<pre>struct LINK3args {
 nfs_fh3 fh;
 diropargs3 link;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK3res(baseobj.BaseObj)</h3>
<pre>union switch LINK3res (nfsstat3 status) {
 case const.NFS3_OK:
 LINK3resok resok;
 default:
 LINK3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK3resfail(baseobj.BaseObj)</h3>
<pre>struct LINK3resfail {
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LINK3resok(baseobj.BaseObj)</h3>
<pre>struct LINK3resok {
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP3args(baseobj.BaseObj)</h3>
<pre>struct LOOKUP3args {
 diropargs3 what;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP3res(baseobj.BaseObj)</h3>
<pre>union switch LOOKUP3res (nfsstat3 status) {
 case const.NFS3_OK:
 LOOKUP3resok resok;
 default:
 LOOKUP3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP3resfail(baseobj.BaseObj)</h3>
<pre>struct LOOKUP3resfail {
 post_op_attr dir_attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class LOOKUP3resok(baseobj.BaseObj)</h3>
<pre>struct LOOKUP3resok {
 nfs_fh3 fh;
 post_op_attr attributes;
 post_op_attr dir_attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKDIR3args(baseobj.BaseObj)</h3>
<pre>struct MKDIR3args {
 diropargs3 where;
 sattr3 attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKDIR3res(baseobj.BaseObj)</h3>
<pre>union switch MKDIR3res (nfsstat3 status) {
 case const.NFS3_OK:
 MKDIR3resok resok;
 default:
 MKDIR3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKDIR3resfail(baseobj.BaseObj)</h3>
<pre>struct MKDIR3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKDIR3resok(baseobj.BaseObj)</h3>
<pre>struct MKDIR3resok {
 post_op_fh3 obj;
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKNOD3args(baseobj.BaseObj)</h3>
<pre>struct MKNOD3args {
 diropargs3 where;
 mknoddata3 what;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKNOD3res(baseobj.BaseObj)</h3>
<pre>union switch MKNOD3res (nfsstat3 status) {
 case const.NFS3_OK:
 MKNOD3resok resok;
 default:
 MKNOD3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKNOD3resfail(baseobj.BaseObj)</h3>
<pre>struct MKNOD3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class MKNOD3resok(baseobj.BaseObj)</h3>
<pre>struct MKNOD3resok {
 post_op_fh3 obj;
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class NFS3args(packet.utils.RPCload)</h3>
<pre>union switch NFS3args (nfs_proc3 procedure) {
 case const.NFSPROC3_NULL:
 void;
 case const.NFSPROC3_GETATTR:
 GETATTR3args opgetattr;
 case const.NFSPROC3_SETATTR:
 SETATTR3args opsetattr;
 case const.NFSPROC3_LOOKUP:
 LOOKUP3args oplookup;
 case const.NFSPROC3_ACCESS:
 ACCESS3args opaccess;
 case const.NFSPROC3_READLINK:
 READLINK3args opreadlink;
 case const.NFSPROC3_READ:
 READ3args opread;
 case const.NFSPROC3_WRITE:
 WRITE3args opwrite;
 case const.NFSPROC3_CREATE:
 CREATE3args opcreate;
 case const.NFSPROC3_MKDIR:
 MKDIR3args opmkdir;
 case const.NFSPROC3_SYMLINK:
 SYMLINK3args opsymlink;
 case const.NFSPROC3_MKNOD:
 MKNOD3args opmknod;
 case const.NFSPROC3_REMOVE:
 REMOVE3args opremove;
 case const.NFSPROC3_RMDIR:
 RMDIR3args oprmdir;
 case const.NFSPROC3_RENAME:
 RENAME3args oprename;
 case const.NFSPROC3_LINK:
 LINK3args oplink;
 case const.NFSPROC3_READDIR:
 READDIR3args opreaddir;
 case const.NFSPROC3_READDIRPLUS:
 READDIRPLUS3args opreaddirplus;
 case const.NFSPROC3_FSSTAT:
 FSSTAT3args opfsstat;
 case const.NFSPROC3_FSINFO:
 FSINFO3args opfsinfo;
 case const.NFSPROC3_PATHCONF:
 PATHCONF3args oppathconf;
 case const.NFSPROC3_COMMIT:
 COMMIT3args opcommit;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class NFS3res(packet.utils.RPCload)</h3>
<pre>union switch NFS3res (nfs_proc3 procedure) {
 case const.NFSPROC3_NULL:
 void;
 case const.NFSPROC3_GETATTR:
 GETATTR3res opgetattr;
 case const.NFSPROC3_SETATTR:
 SETATTR3res opsetattr;
 case const.NFSPROC3_LOOKUP:
 LOOKUP3res oplookup;
 case const.NFSPROC3_ACCESS:
 ACCESS3res opaccess;
 case const.NFSPROC3_READLINK:
 READLINK3res opreadlink;
 case const.NFSPROC3_READ:
 READ3res opread;
 case const.NFSPROC3_WRITE:
 WRITE3res opwrite;
 case const.NFSPROC3_CREATE:
 CREATE3res opcreate;
 case const.NFSPROC3_MKDIR:
 MKDIR3res opmkdir;
 case const.NFSPROC3_SYMLINK:
 SYMLINK3res opsymlink;
 case const.NFSPROC3_MKNOD:
 MKNOD3res opmknod;
 case const.NFSPROC3_REMOVE:
 REMOVE3res opremove;
 case const.NFSPROC3_RMDIR:
 RMDIR3res oprmdir;
 case const.NFSPROC3_RENAME:
 RENAME3res oprename;
 case const.NFSPROC3_LINK:
 LINK3res oplink;
 case const.NFSPROC3_READDIR:
 READDIR3res opreaddir;
 case const.NFSPROC3_READDIRPLUS:
 READDIRPLUS3res opreaddirplus;
 case const.NFSPROC3_FSSTAT:
 FSSTAT3res opfsstat;
 case const.NFSPROC3_FSINFO:
 FSINFO3res opfsinfo;
 case const.NFSPROC3_PATHCONF:
 PATHCONF3res oppathconf;
 case const.NFSPROC3_COMMIT:
 COMMIT3res opcommit;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack, procedure)</code></pre>
<h3>class PATHCONF3args(baseobj.BaseObj)</h3>
<pre>struct PATHCONF3args {
 nfs_fh3 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PATHCONF3res(baseobj.BaseObj)</h3>
<pre>union switch PATHCONF3res (nfsstat3 status) {
 case const.NFS3_OK:
 PATHCONF3resok resok;
 default:
 PATHCONF3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PATHCONF3resfail(baseobj.BaseObj)</h3>
<pre>struct PATHCONF3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class PATHCONF3resok(baseobj.BaseObj)</h3>
<pre>struct PATHCONF3resok {
 post_op_attr attributes;
 uint32 linkmax;
 uint32 name_max;
 bool no_trunc;
 bool chown_restricted;
 bool case_insensitive;
 bool case_preserving;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ3args(baseobj.BaseObj)</h3>
<pre>struct READ3args {
 nfs_fh3 fh;
 offset3 offset;
 count3 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ3res(baseobj.BaseObj)</h3>
<pre>union switch READ3res (nfsstat3 status) {
 case const.NFS3_OK:
 READ3resok resok;
 default:
 READ3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ3resfail(baseobj.BaseObj)</h3>
<pre>struct READ3resfail {
 post_op_attr file_attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READ3resok(baseobj.BaseObj)</h3>
<pre>struct READ3resok {
 post_op_attr attributes;
 count3 count;
 bool eof;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR3args(baseobj.BaseObj)</h3>
<pre>struct READDIR3args {
 nfs_fh3 fh;
 cookie3 cookie;
 cookieverf3 verifier;
 count3 count;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR3res(baseobj.BaseObj)</h3>
<pre>union switch READDIR3res (nfsstat3 status) {
 case const.NFS3_OK:
 READDIR3resok resok;
 default:
 READDIR3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR3resfail(baseobj.BaseObj)</h3>
<pre>struct READDIR3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIR3resok(baseobj.BaseObj)</h3>
<pre>struct READDIR3resok {
 post_op_attr attributes;
 cookieverf3 verifier;
 dirlist3 reply;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIRPLUS3args(baseobj.BaseObj)</h3>
<pre>struct READDIRPLUS3args {
 nfs_fh3 fh;
 cookie3 cookie;
 cookieverf3 verifier;
 count3 dircount;
 count3 maxcount;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIRPLUS3res(baseobj.BaseObj)</h3>
<pre>union switch READDIRPLUS3res (nfsstat3 status) {
 case const.NFS3_OK:
 READDIRPLUS3resok resok;
 default:
 READDIRPLUS3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIRPLUS3resfail(baseobj.BaseObj)</h3>
<pre>struct READDIRPLUS3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READDIRPLUS3resok(baseobj.BaseObj)</h3>
<pre>struct READDIRPLUS3resok {
 post_op_attr attributes;
 cookieverf3 verifier;
 dirlistplus3 reply;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK3args(baseobj.BaseObj)</h3>
<pre>struct READLINK3args {
 nfs_fh3 fh;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK3res(baseobj.BaseObj)</h3>
<pre>union switch READLINK3res (nfsstat3 status) {
 case const.NFS3_OK:
 READLINK3resok resok;
 default:
 READLINK3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK3resfail(baseobj.BaseObj)</h3>
<pre>struct READLINK3resfail {
 post_op_attr attributes;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class READLINK3resok(baseobj.BaseObj)</h3>
<pre>struct READLINK3resok {
 post_op_attr attributes;
 nfspath3 link;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE3args(baseobj.BaseObj)</h3>
<pre>struct REMOVE3args {
 diropargs3 object;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE3res(baseobj.BaseObj)</h3>
<pre>union switch REMOVE3res (nfsstat3 status) {
 case const.NFS3_OK:
 REMOVE3resok resok;
 default:
 REMOVE3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE3resfail(baseobj.BaseObj)</h3>
<pre>struct REMOVE3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class REMOVE3resok(baseobj.BaseObj)</h3>
<pre>struct REMOVE3resok {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME3args(baseobj.BaseObj)</h3>
<pre>struct RENAME3args {
 diropargs3 nfrom;
 diropargs3 nto;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME3res(baseobj.BaseObj)</h3>
<pre>union switch RENAME3res (nfsstat3 status) {
 case const.NFS3_OK:
 RENAME3resok resok;
 default:
 RENAME3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME3resfail(baseobj.BaseObj)</h3>
<pre>struct RENAME3resfail {
 wcc_data fromdir_wcc;
 wcc_data todir_wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RENAME3resok(baseobj.BaseObj)</h3>
<pre>struct RENAME3resok {
 wcc_data fromdir_wcc;
 wcc_data todir_wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RMDIR3args(baseobj.BaseObj)</h3>
<pre>struct RMDIR3args {
 diropargs3 object;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RMDIR3res(baseobj.BaseObj)</h3>
<pre>union switch RMDIR3res (nfsstat3 status) {
 case const.NFS3_OK:
 RMDIR3resok resok;
 default:
 RMDIR3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RMDIR3resfail(baseobj.BaseObj)</h3>
<pre>struct RMDIR3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class RMDIR3resok(baseobj.BaseObj)</h3>
<pre>struct RMDIR3resok {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR3args(baseobj.BaseObj)</h3>
<pre>struct SETATTR3args {
 nfs_fh3 fh;
 sattr3 attributes;
 sattrguard3 guard;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR3res(baseobj.BaseObj)</h3>
<pre>union switch SETATTR3res (nfsstat3 status) {
 case const.NFS3_OK:
 SETATTR3resok resok;
 default:
 SETATTR3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR3resfail(baseobj.BaseObj)</h3>
<pre>struct SETATTR3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SETATTR3resok(baseobj.BaseObj)</h3>
<pre>struct SETATTR3resok {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SYMLINK3args(baseobj.BaseObj)</h3>
<pre>struct SYMLINK3args {
 diropargs3 where;
 symlinkdata3 symlink;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SYMLINK3res(baseobj.BaseObj)</h3>
<pre>union switch SYMLINK3res (nfsstat3 status) {
 case const.NFS3_OK:
 SYMLINK3resok resok;
 default:
 SYMLINK3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SYMLINK3resfail(baseobj.BaseObj)</h3>
<pre>struct SYMLINK3resfail {
 wcc_data dir_wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class SYMLINK3resok(baseobj.BaseObj)</h3>
<pre>struct SYMLINK3resok {
 post_op_fh3 obj;
 post_op_attr attributes;
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE3args(baseobj.BaseObj)</h3>
<pre>struct WRITE3args {
 nfs_fh3 fh;
 offset3 offset;
 count3 count;
 stable_how stable;
 opaque data&lt;&gt;;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE3res(baseobj.BaseObj)</h3>
<pre>union switch WRITE3res (nfsstat3 status) {
 case const.NFS3_OK:
 WRITE3resok resok;
 default:
 WRITE3resfail resfail;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE3resfail(baseobj.BaseObj)</h3>
<pre>struct WRITE3resfail {
 wcc_data wcc;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class WRITE3resok(baseobj.BaseObj)</h3>
<pre>struct WRITE3resok {
 wcc_data wcc;
 count3 count;
 stable_how committed;
 writeverf3 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class createhow3(baseobj.BaseObj)</h3>
<pre>union switch createhow3 (createmode3 mode) {
 case const.UNCHECKED:
 case const.GUARDED:
 sattr3 attributes;
 case const.EXCLUSIVE:
 createverf3 verifier;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class createmode3(packet.utils.Enum)</h3>
<pre>enum createmode3</pre>
<h3>class devicedata3(baseobj.BaseObj)</h3>
<pre>struct devicedata3 {
 sattr3 attributes;
 specdata3 spec;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class dirlist3(baseobj.BaseObj)</h3>
<pre>struct dirlist3 {
 entry3 *entries;
 bool eof;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class dirlistplus3(baseobj.BaseObj)</h3>
<pre>struct dirlistplus3 {
 entryplus3 *entries;
 bool eof;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class diropargs3(baseobj.BaseObj)</h3>
<pre>struct diropargs3 {
 nfs_fh3 fh;
 filename3 name;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class entry3(baseobj.BaseObj)</h3>
<pre>struct entry3 {
 fileid3 fileid;
 filename3 name;
 cookie3 cookie;
 entry3 *nextentry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class entryplus3(baseobj.BaseObj)</h3>
<pre>struct entryplus3 {
 fileid3 fileid;
 filename3 name;
 cookie3 cookie;
 post_op_attr attributes;
 post_op_fh3 obj;
 entryplus3 *nextentry;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class fattr3(baseobj.BaseObj)</h3>
<pre>struct fattr3 {
 ftype3 type;
 mode3 mode;
 uint32 nlink;
 uid3 uid;
 gid3 gid;
 size3 size;
 size3 used;
 specdata3 rdev;
 uint64 fsid;
 fileid3 fileid;
 nfstime3 atime;
 nfstime3 mtime;
 nfstime3 ctime;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class ftype3(packet.utils.Enum)</h3>
<pre>enum ftype3</pre>
<h3>class mknoddata3(baseobj.BaseObj)</h3>
<pre>union switch mknoddata3 (ftype3 type) {
 case const.NF3CHR:
 case const.NF3BLK:
 devicedata3 device;
 case const.NF3SOCK:
 case const.NF3FIFO:
 sattr3 attributes;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class nfs_bool(packet.utils.Enum)</h3>
<pre>enum nfs_bool</pre>
<h3>class nfs_proc3(packet.utils.Enum)</h3>
<pre>enum nfs_proc3</pre>
<h3>class nfsstat3(packet.utils.Enum)</h3>
<pre>enum nfsstat3</pre>
<h3>class nfstime3(baseobj.BaseObj)</h3>
<pre>struct nfstime3 {
 uint32 seconds;
 uint32 nseconds;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class post_op_attr(baseobj.BaseObj)</h3>
<pre>union switch post_op_attr (bool attributes_follow) {
 case const.TRUE:
 fattr3 attributes;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class post_op_fh3(baseobj.BaseObj)</h3>
<pre>union switch post_op_fh3 (bool handle_follows) {
 case const.TRUE:
 nfs_fh3 fh;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class pre_op_attr(baseobj.BaseObj)</h3>
<pre>union switch pre_op_attr (bool attributes_follow) {
 case const.TRUE:
 wcc_attr attributes;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class sattr3(baseobj.BaseObj)</h3>
<pre>struct sattr3 {
 set_mode3 mode;
 set_uid3 uid;
 set_gid3 gid;
 set_size3 size;
 set_atime atime;
 set_mtime mtime;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class sattrguard3(baseobj.BaseObj)</h3>
<pre>union switch sattrguard3 (bool check) {
 case const.TRUE:
 nfstime3 ctime;
 case const.FALSE:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_atime(baseobj.BaseObj)</h3>
<pre>union switch set_atime (time_how set_it) {
 case const.SET_TO_CLIENT_TIME:
 nfstime3 atime;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_gid3(baseobj.BaseObj)</h3>
<pre>union switch set_gid3 (bool set_it) {
 case const.TRUE:
 gid3 gid;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_mode3(baseobj.BaseObj)</h3>
<pre>union switch set_mode3 (bool set_it) {
 case const.TRUE:
 mode3 mode;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_mtime(baseobj.BaseObj)</h3>
<pre>union switch set_mtime (time_how set_it) {
 case const.SET_TO_CLIENT_TIME:
 nfstime3 mtime;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_size3(baseobj.BaseObj)</h3>
<pre>union switch set_size3 (bool set_it) {
 case const.TRUE:
 size3 size;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class set_uid3(baseobj.BaseObj)</h3>
<pre>union switch set_uid3 (bool set_it) {
 case const.TRUE:
 uid3 uid;
 default:
 void;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class specdata3(baseobj.BaseObj)</h3>
<pre>struct specdata3 {
 uint32 specdata1;
 uint32 specdata2;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class stable_how(packet.utils.Enum)</h3>
<pre>enum stable_how</pre>
<h3>class symlinkdata3(baseobj.BaseObj)</h3>
<pre>struct symlinkdata3 {
 sattr3 attributes;
 nfspath3 linkdata;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class time_how(packet.utils.Enum)</h3>
<pre>enum time_how</pre>
<h3>class wcc_attr(baseobj.BaseObj)</h3>
<pre>struct wcc_attr {
 size3 size;
 nfstime3 mtime;
 nfstime3 ctime;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h3>class wcc_data(baseobj.BaseObj)</h3>
<pre>struct wcc_data {
 pre_op_attr before;
 post_op_attr after;
};
<code>Methods defined here:</code>
---------------------
<code>__init__(self, unpack)</code></pre>
<h2>Functions</h2>
<h3>cookieverf3(unpack)</h3>
<h3>createverf3(unpack)</h3>
<h3>nfs_fh3(unpack)</h3>
<h3>writeverf3(unpack)</h3>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-baseobj/">baseobj</a>(3),</code> <code><a href="/docs/linux/man/3-packet-unpack/">packet.unpack</a>(3),</code> <code><a href="/docs/linux/man/3-packet-utils/">packet.utils</a>(3)</code> </p>
<h2>Bugs</h2>
<p>No known bugs.</p>
<h2>Author</h2>
<p>Jorge Mora (mora [at] netapp.com)</p>
