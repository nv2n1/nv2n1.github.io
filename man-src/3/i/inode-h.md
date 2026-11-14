---
title: "inode-h(3)"
name: "inode-h"
section: "3"
letter: "i"
url: "/docs/linux/man/3-inode-h/"
description: "inode.h –"
---

<p>inode.h &#8211; </p>
<p> C wrapper for DMLite INode API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;dmlite.h&#8217;<br />
 #include &#8216;any.h&#8217;<br />
 #include &#8216;utils.h&#8217;<br />
 #include &lt;stdint.h&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>dmlite_replica</code> </p>
<p> struct <code>dmlite_xstat</code> </p>
<h3>Typedefs</h3>
<p>typedef struct <code>dmlite_replica</code> <code>dmlite_replica</code> </p>
<p> typedef struct <code>dmlite_xstat</code> <code>dmlite_xstat</code> </p>
<p> typedef struct <code>dmlite_idir</code> <code>dmlite_idir</code> </p>
<h3>Enumerations</h3>
<p>enum <code>dmlite_replica_status</code> { <code>kAvailable</code> = &#8216;-&#8216;, <code>kBeingPopulated</code> = &#8216;P&#8217;, <code>kToBeDeleted</code> = &#8216;D&#8217; } </p>
<p> enum <code>dmlite_replica_type</code> { <code>kVolatile</code> = &#8216;V&#8217;, <code>kPermanent</code> = &#8216;P&#8217; } </p>
<p> enum <code>dmlite_file_status</code> { <code>kOnline</code> = &#8216;-&#8216;, <code>kMigrated</code> = &#8216;m&#8217; } </p>
<h3>Functions</h3>
<p>int <code>dmlite_ibegin</code> (<code>dmlite_context</code> *context)<br />
 <i>Starts a transaction. </i><br />
 int <code>dmlite_icommit</code> (<code>dmlite_context</code> *context)<br />
 <i>Commits the changes. </i><br />
 int <code>dmlite_irollback</code> (<code>dmlite_context</code> *context)<br />
 <i>Undo the changes. </i><br />
 int <code>dmlite_icreate</code> (<code>dmlite_context</code> *context, const <code>dmlite_xstat</code> *f)<br />
 <i>Creates a new file. </i><br />
 int <code>dmlite_isymlink</code> (<code>dmlite_context</code> *context, ino_t inode, const char *link)<br />
 <i>Associates a symlink with an existing file. </i><br />
 int <code>dmlite_iunlink</code> (<code>dmlite_context</code> *context, ino_t inode)<br />
 <i>Removes a file or directory from the database. </i><br />
 int <code>dmlite_imove</code> (<code>dmlite_context</code> *context, ino_t inode, ino_t dest)<br />
 <i>Moves a file to a different parent directory. </i><br />
 int <code>dmlite_irename</code> (<code>dmlite_context</code> *context, ino_t inode, const char *name)<br />
 <i>Changes the name of an entry. </i><br />
 int <code>dmlite_istat</code> (<code>dmlite_context</code> *context, ino_t inode, struct stat *buf)<br />
 <i>Does a stat of an entry using the inode instead of the path. </i><br />
 int <code>dmlite_istatx</code> (<code>dmlite_context</code> *context, ino_t inode, <code>dmlite_xstat</code> *buf)<br />
 <i>Does an extended stat of an entry using the inode instead of the path. </i><br />
 int <code>dmlite_istatx_by_name</code> (<code>dmlite_context</code> *context, ino_t parent, const char *name, <code>dmlite_xstat</code> *buf)<br />
 <i>Does an extended stat using the parent inode and the entry name. </i><br />
 int <code>dmlite_ireadlink</code> (<code>dmlite_context</code> *context, ino_t inode, char *path, size_t bufsize)<br />
 <i>Reads a symbolic link. </i><br />
 int <code>dmlite_iaddreplica</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Adds a new replica. </i><br />
 int <code>dmlite_ideletereplica</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Deletes a replica. </i><br />
 int <code>dmlite_igetreplica</code> (<code>dmlite_context</code> *context, int64_t rid, <code>dmlite_replica</code> *buf)<br />
 <i>Gets a specific replica using its replica id. </i><br />
 int <code>dmlite_igetreplicas</code> (<code>dmlite_context</code> *context, ino_t inode, unsigned *nreplicas, <code>dmlite_replica</code> **replicas)<br />
 <i>Gets all the replicas associated to a file. </i><br />
 int <code>dmlite_iutime</code> (<code>dmlite_context</code> *context, ino_t inode, const struct utimbuf *buf)<br />
 <i>Sets the access and modification time. </i><br />
 int <code>dmlite_isetmode</code> (<code>dmlite_context</code> *context, ino_t inode, uid_t uid, gid_t gid, mode_t mode, unsigned nentries, <code>dmlite_aclentry</code> *acl)<br />
 <i>Sets the mode and ACL of a file. </i><br />
 int <code>dmlite_isetsize</code> (<code>dmlite_context</code> *context, ino_t inode, size_t size)<br />
 <i>Sets the size of a file. </i><br />
 int <code>dmlite_isetchecksum</code> (<code>dmlite_context</code> *context, ino_t inode, const char *csumtype, const char *csumvalue)<br />
 <i>Sets the checksum of a file. </i><br />
 int <code>dmlite_igetcomment</code> (<code>dmlite_context</code> *context, ino_t inode, char *comment, size_t bufsize)<br />
 <i>Gets the comment associated with an entry. </i><br />
 int <code>dmlite_isetcomment</code> (<code>dmlite_context</code> *context, ino_t inode, const char *comment)<br />
 <i>Sets the comment associated with an entry. </i><br />
 int <code>dmlite_ideletecomment</code> (<code>dmlite_context</code> *context, ino_t inode)<br />
 <i>Deletes the comment associated with an entry. </i><br />
 int <code>dmlite_isetguid</code> (<code>dmlite_context</code> *context, ino_t inode, const char *guid)<br />
 <i>Sets the file Grid Unique Identifier. </i><br />
 int <code>dmlite_iupdate_xattr</code> (<code>dmlite_context</code> *context, ino_t inode, const <code>dmlite_any_dict</code> *xattr)<br />
 <i>Updates the file extended attributes. </i><br />
 <code>dmlite_idir</code> * <code>dmlite_iopendir</code> (<code>dmlite_context</code> *context, ino_t inode)<br />
 <i>Opens a directory. </i><br />
 int <code>dmlite_iclosedir</code> (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)<br />
 <i>Closes a directory, freeing any internally allocated memory. </i><br />
 <code>dmlite_xstat</code> * <code>dmlite_ireaddirx</code> (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)<br />
 <i>Reads a directory. Extended data. </i><br />
 struct dirent * <code>dmlite_ireaddir</code> (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)<br />
 <i>Reads a directory. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for DMLite INode API. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This is a low-level API, so security checks will NOT be done.</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_idir</code> <code>dmlite_idir</code></h3>
<p>Opaque directory handler</p>
<h3>typedef struct <code>dmlite_replica</code> <code>dmlite_replica</code></h3>
<p>A replica of a file</p>
<h3>typedef struct <code>dmlite_xstat</code> <code>dmlite_xstat</code></h3>
<p>File metadata</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>dmlite_file_status</code></h3>
<p>Posible file statuses </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>kOnline </i></p>
<dd>
<dt><i>kMigrated </i></p>
<dd></dl>
<h3>enum <code>dmlite_replica_status</code></h3>
<p>Possible replica statuses </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>kAvailable </i></p>
<dd>
<dt><i>kBeingPopulated </i></p>
<dd>
<dt><i>kToBeDeleted </i></p>
<dd></dl>
<h3>enum <code>dmlite_replica_type</code></h3>
<p>Possible replica types </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>kVolatile </i></p>
<dd>
<dt><i>kPermanent </i></p>
<dd></dl>
<h2>Function Documentation</h2>
<h3>int dmlite_iaddreplica (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)</h3>
<p>Adds a new replica. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>replica</i> The replica to add. replica-&gt;fileid must point to a valid file.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_ibegin (<code>dmlite_context</code> *context)</h3>
<p>Starts a transaction. Depending on the plugin stack, it can be possible to nest several calls. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_iclosedir (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)</h3>
<p>Closes a directory, freeing any internally allocated memory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The directory to close, as returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_icommit (<code>dmlite_context</code> *context)</h3>
<p>Commits the changes. Depending on the plugin stack, it can be possible to nest several calls, and there must be one icommit per ibegin for the changes to be permanent. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_icreate (<code>dmlite_context</code> *context, const <code>dmlite_xstat</code> *f)</h3>
<p>Creates a new file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>f</i> Only some fields from this struct will be used. That would depend on the plugin, but usually it will be: parent, name, mode, uid, gid, size, status, checksum and ACL.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>mode will probably be used raw (i.e. no cleanup or set of format bits)</dl>
<h3>int dmlite_ideletecomment (<code>dmlite_context</code> *context, ino_tinode)</h3>
<p>Deletes the comment associated with an entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_ideletereplica (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)</h3>
<p>Deletes a replica. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>replica</i> The replica to remove.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_igetcomment (<code>dmlite_context</code> *context, ino_tinode, char *comment, size_tbufsize)</h3>
<p>Gets the comment associated with an entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>comment</i> Where to put the comment.<br />
 <i>bufsize</i> The size of the memory pointed by comment.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_igetreplica (<code>dmlite_context</code> *context, int64_trid, <code>dmlite_replica</code> *buf)</h3>
<p>Gets a specific replica using its replica id. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>rid</i> The replica id.<br />
 <i>buf</i> Where to put the retrieved data.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_igetreplicas (<code>dmlite_context</code> *context, ino_tinode, unsigned *nreplicas, <code>dmlite_replica</code> **replicas)</h3>
<p>Gets all the replicas associated to a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>nreplicas</i> The number of replicas will be put here.<br />
 <i>replicas</i> It will be initialized to an array of nreplicas replicas. Free it with <code>dmlite_replicas_free</code>.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_imove (<code>dmlite_context</code> *context, ino_tinode, ino_tdest)</h3>
<p>Moves a file to a different parent directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>dest</i> The destination id.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_idir</code>* dmlite_iopendir (<code>dmlite_context</code> *context, ino_tinode)</h3>
<p>Opens a directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The directory ID.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>NULL on failure. A pointer to an internal struct to be used with dmlite_ireaddir*</dl>
<h3>struct dirent* dmlite_ireaddir (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)</h3>
<p>Reads a directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The directory to read, as returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a struct with the recovered data. NULL on failure, or end of dir. If an error occurred, dm_errno(context) will be different than 0.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The pointer is internally allocated. Do not free it.</dl>
<h3><code>dmlite_xstat</code>* dmlite_ireaddirx (<code>dmlite_context</code> *context, <code>dmlite_idir</code> *dir)</h3>
<p>Reads a directory. Extended data. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The directory to read, as returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a struct with the recovered data. NULL on failure, or end of dir. If an error occurred, dm_errno(context) will be different than 0.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The pointer is internally allocated. Do not free it.</dl>
<h3>int dmlite_ireadlink (<code>dmlite_context</code> *context, ino_tinode, char *path, size_tbufsize)</h3>
<p>Reads a symbolic link. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>path</i> The link will be put here.<br />
 <i>bufsize</i> The size of the memory area pointed by path.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_irename (<code>dmlite_context</code> *context, ino_tinode, const char *name)</h3>
<p>Changes the name of an entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>name</i> The new name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_irollback (<code>dmlite_context</code> *context)</h3>
<p>Undo the changes. If several ibegin were nested, all the transactions will be probable be undone, regardless on the nesting level. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_isetchecksum (<code>dmlite_context</code> *context, ino_tinode, const char *csumtype, const char *csumvalue)</h3>
<p>Sets the checksum of a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>csumtype</i> The new checksum type.<br />
 <i>csumvalue</i> The new checksum value.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_isetcomment (<code>dmlite_context</code> *context, ino_tinode, const char *comment)</h3>
<p>Sets the comment associated with an entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>comment</i> The new comment.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_isetguid (<code>dmlite_context</code> *context, ino_tinode, const char *guid)</h3>
<p>Sets the file Grid Unique Identifier. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The entry id.<br />
 <i>guid</i> The new GUID.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_isetmode (<code>dmlite_context</code> *context, ino_tinode, uid_tuid, gid_tgid, mode_tmode, unsignednentries, <code>dmlite_aclentry</code> *acl)</h3>
<p>Sets the mode and ACL of a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>uid</i> The new UID.<br />
 <i>gid</i> The new GID.<br />
 <i>mode</i> The new mode.<br />
 <i>nentries</i> The number of acl entries.<br />
 <i>acl</i> The new ACL.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This call may not validate that uid, gid, mode and acl are coherent.</dl>
<h3>int dmlite_isetsize (<code>dmlite_context</code> *context, ino_tinode, size_tsize)</h3>
<p>Sets the size of a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>size</i> The new size.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_istat (<code>dmlite_context</code> *context, ino_tinode, struct stat *buf)</h3>
<p>Does a stat of an entry using the inode instead of the path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The entry inode.<br />
 <i>buf</i> Where to put the retrieved information.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Security checks won&#8217;t be done if you use this function, so keep in mind doing it yourself.</dl>
<h3>int dmlite_istatx (<code>dmlite_context</code> *context, ino_tinode, <code>dmlite_xstat</code> *buf)</h3>
<p>Does an extended stat of an entry using the inode instead of the path. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The entry inode.<br />
 <i>buf</i> Where to put the retrieved information.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Security checks won&#8217;t be done if you use this function, so keep in mind doing it yourself.</dl>
<h3>int dmlite_istatx_by_name (<code>dmlite_context</code> *context, ino_tparent, const char *name, <code>dmlite_xstat</code> *buf)</h3>
<p>Does an extended stat using the parent inode and the entry name. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>parent</i> The parent id.<br />
 <i>name</i> The entry name.<br />
 <i>buf</i> Where to put the retrieved information.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_isymlink (<code>dmlite_context</code> *context, ino_tinode, const char *link)</h3>
<p>Associates a symlink with an existing file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file that will be a symlink.<br />
 <i>link</i> The destination link.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_iunlink (<code>dmlite_context</code> *context, ino_tinode)</h3>
<p>Removes a file or directory from the database. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The id of the entry to remove.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Not empty directories, or files will replicas may fail.</dl>
<h3>int dmlite_iupdate_xattr (<code>dmlite_context</code> *context, ino_tinode, const <code>dmlite_any_dict</code> *xattr)</h3>
<p>Updates the file extended attributes. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The entry id.<br />
 <i>xattr</i> The new set of extended attributes.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_iutime (<code>dmlite_context</code> *context, ino_tinode, const struct utimbuf *buf)</h3>
<p>Sets the access and modification time. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>inode</i> The file id.<br />
 <i>buf</i> The timestamps.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for dmlite from the source code.</p>
