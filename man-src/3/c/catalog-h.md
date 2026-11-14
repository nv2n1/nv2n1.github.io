---
title: "catalog-h(3)"
name: "catalog-h"
section: "3"
letter: "c"
url: "/docs/linux/man/3-catalog-h/"
description: "catalog.h –"
---

<p>catalog.h &#8211; </p>
<p> C wrapper for DMLite Catalog API.</p>
<h2>Synopsis</h2>
<p>#include &#8216;dmlite.h&#8217;<br />
 #include &#8216;inode.h&#8217;<br />
 #include &#8216;utils.h&#8217; </p>
<h3>Typedefs</h3>
<p>typedef struct <code>dmlite_dir</code> <code>dmlite_dir</code> </p>
<h3>Functions</h3>
<p>int <code>dmlite_chdir</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Changes the working dir. </i><br />
 char * <code>dmlite_getcwd</code> (<code>dmlite_context</code> *context, char *buffer, size_t size)<br />
 <i>Gets the current working directory. </i><br />
 mode_t <code>dmlite_umask</code> (<code>dmlite_context</code> *context, mode_t mask)<br />
 <i>Sets the file mode creation mask. </i><br />
 int <code>dmlite_stat</code> (<code>dmlite_context</code> *context, const char *path, struct stat *buf)<br />
 <i>Does a stat of a file or directory. </i><br />
 int <code>dmlite_statl</code> (<code>dmlite_context</code> *context, const char *path, struct stat *buf)<br />
 <i>Does a stat of a file, directory, or symbolic link (does not follow). </i><br />
 int <code>dmlite_statx</code> (<code>dmlite_context</code> *context, const char *path, <code>dmlite_xstat</code> *buf)<br />
 <i>Does an extended stat of a file, directory or symbolic link. </i><br />
 int <code>dmlite_rstatx</code> (<code>dmlite_context</code> *context, const char *rfn, <code>dmlite_xstat</code> *buf)<br />
 <i>Does an extended stat of a logical file using an associated replica filename. </i><br />
 int <code>dmlite_access</code> (<code>dmlite_context</code> *context, const char *lfn, int mode)<br />
 <i>Checks wether the process would be allowed to read, write, or check existence. </i><br />
 int <code>dmlite_accessr</code> (<code>dmlite_context</code> *context, const char *rfn, int mode)<br />
 <i>Checks wether the process would be allowed to read, write, or check existence. </i><br />
 int <code>dmlite_addreplica</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Adds a new replica to an entry. </i><br />
 int <code>dmlite_delreplica</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Deletes a replica. </i><br />
 int <code>dmlite_getreplicas</code> (<code>dmlite_context</code> *context, const char *path, unsigned *nReplicas, <code>dmlite_replica</code> **fileReplicas)<br />
 <i>Gets the replicas of a file. </i><br />
 int <code>dmlite_replicas_free</code> (unsigned nReplicas, <code>dmlite_replica</code> *fileReplicas)<br />
 <i>Frees a replica list. </i><br />
 int <code>dmlite_symlink</code> (<code>dmlite_context</code> *context, const char *oldPath, const char *newPath)<br />
 <i>Creates a symlink. </i><br />
 int <code>dmlite_readlink</code> (<code>dmlite_context</code> *context, const char *path, char *buf, size_t bufsize)<br />
 <i>Reads a symlink. </i><br />
 int <code>dmlite_unlink</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Removes a file. </i><br />
 int <code>dmlite_create</code> (<code>dmlite_context</code> *context, const char *path, mode_t mode)<br />
 <i>Creates a file in the catalog (no replicas). </i><br />
 int <code>dmlite_chmod</code> (<code>dmlite_context</code> *context, const char *path, mode_t mode)<br />
 <i>Changes the mode of a file or directory. </i><br />
 int <code>dmlite_chown</code> (<code>dmlite_context</code> *context, const char *path, uid_t newUid, gid_t newGid)<br />
 <i>Changes the owner of a file or directory. </i><br />
 int <code>dmlite_lchown</code> (<code>dmlite_context</code> *context, const char *path, uid_t newUid, gid_t newGid)<br />
 <i>Changes the owner of a file, directory or symlink (does not follow). </i><br />
 int <code>dmlite_setfsize</code> (<code>dmlite_context</code> *context, const char *path, uint64_t filesize)<br />
 <i>Changes the size of a file in the catalog. </i><br />
 int <code>dmlite_setfsizec</code> (<code>dmlite_context</code> *context, const char *path, uint64_t filesize, const char *csumtype, const char *csumvalue)<br />
 <i>Changes the size and checksum of a file in the catalog. </i><br />
 int <code>dmlite_getchecksum</code> (<code>dmlite_context</code> *context, const char *path, const char *csumtype, char *csumvalue, const int maxcksumlen, const char *pfn, const int forcerecalc, const int waitsecs)<br />
 <i>Gets the checksum of a file in the catalog. </i><br />
 int <code>dmlite_setacl</code> (<code>dmlite_context</code> *context, const char *path, unsigned nEntries, <code>dmlite_aclentry</code> *acl)<br />
 <i>Changes the ACL of a file. </i><br />
 int <code>dmlite_utime</code> (<code>dmlite_context</code> *context, const char *path, const struct utimbuf *buf)<br />
 <i>Changes access and/or modification time. </i><br />
 int <code>dmlite_getcomment</code> (<code>dmlite_context</code> *context, const char *path, char *comment, size_t bufsize)<br />
 <i>Gets the comment associated with a file. </i><br />
 int <code>dmlite_setcomment</code> (<code>dmlite_context</code> *context, const char *path, const char *comment)<br />
 <i>Sets the comment associated with a file. </i><br />
 int <code>dmlite_setguid</code> (<code>dmlite_context</code> *context, const char *path, const char *guid)<br />
 <i>Sets the file Grid Unique Identifier. </i><br />
 int <code>dmlite_update_xattr</code> (<code>dmlite_context</code> *context, const char *path, const <code>dmlite_any_dict</code> *xattr)<br />
 <i>Updates the file extended attributes. </i><br />
 int <code>dmlite_getgrpbynam</code> (<code>dmlite_context</code> *context, const char *groupName, gid_t *gid)<br />
 <i>Gets the id of a group. </i><br />
 int <code>dmlite_getusrbynam</code> (<code>dmlite_context</code> *context, const char *userName, uid_t *uid)<br />
 <i>Get the user id. </i><br />
 <code>dmlite_dir</code> * <code>dmlite_opendir</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Opens a directory to read it later. </i><br />
 int <code>dmlite_closedir</code> (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)<br />
 <i>Closes a directory and free the internal structures. </i><br />
 struct dirent * <code>dmlite_readdir</code> (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)<br />
 <i>Reads an entry from a directory. </i><br />
 <code>dmlite_xstat</code> * <code>dmlite_readdirx</code> (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)<br />
 <i>Reads an entry from a directory (extended data). </i><br />
 int <code>dmlite_mkdir</code> (<code>dmlite_context</code> *context, const char *path, mode_t mode)<br />
 <i>Creates a new directory. </i><br />
 int <code>dmlite_rename</code> (<code>dmlite_context</code> *context, const char *oldPath, const char *newPath)<br />
 <i>Renames a file, directory or symlink. </i><br />
 int <code>dmlite_rmdir</code> (<code>dmlite_context</code> *context, const char *path)<br />
 <i>Deletes a directory. It must be empty. </i><br />
 int <code>dmlite_getreplica_by_rfn</code> (<code>dmlite_context</code> *context, const char *rfn, <code>dmlite_replica</code> *replica)<br />
 <i>Gets a specific replica. </i><br />
 int <code>dmlite_updatereplica</code> (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)<br />
 <i>Updates a replica. </i></p>
<h2>Detailed Description</h2>
<p>C wrapper for DMLite Catalog API. </p>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Alejandro Álvarez Ayllon aalvarez [at] cern.ch</dl>
<h2>Typedef Documentation</h2>
<h3>typedef struct <code>dmlite_dir</code> <code>dmlite_dir</code></h3>
<h2>Function Documentation</h2>
<h3>int dmlite_access (<code>dmlite_context</code> *context, const char *lfn, intmode)</h3>
<p>Checks wether the process would be allowed to read, write, or check existence. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>lfn</i> Logical filename.<br />
 <i>mode</i> A mask consisting of one or more of R_OK, W_OK, X_OK and F_OK.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_accessr (<code>dmlite_context</code> *context, const char *rfn, intmode)</h3>
<p>Checks wether the process would be allowed to read, write, or check existence. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>rfn</i> Replica filename.<br />
 <i>mode</i> A mask consisting of one or more of R_OK, W_OK, X_OK and F_OK.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_addreplica (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)</h3>
<p>Adds a new replica to an entry. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>replica</i> The replica to add.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_chdir (<code>dmlite_context</code> *context, const char *path)</h3>
<p>Changes the working dir. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The new working dir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_chmod (<code>dmlite_context</code> *context, const char *path, mode_tmode)</h3>
<p>Changes the mode of a file or directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>mode</i> The new mode.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_chown (<code>dmlite_context</code> *context, const char *path, uid_tnewUid, gid_tnewGid)</h3>
<p>Changes the owner of a file or directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>newUid</i> The new owner.<br />
 <i>newGid</i> The new group.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_closedir (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)</h3>
<p>Closes a directory and free the internal structures. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The pointer returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_create (<code>dmlite_context</code> *context, const char *path, mode_tmode)</h3>
<p>Creates a file in the catalog (no replicas). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical file name.<br />
 <i>mode</i> The creation mode.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_delreplica (<code>dmlite_context</code> *context, const <code>dmlite_replica</code> *replica)</h3>
<p>Deletes a replica. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>replica</i> The replica to delete.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_getchecksum (<code>dmlite_context</code> *context, const char *path, const char *csumtype, char *csumvalue, const intmaxcksumlen, const char *pfn, const intforcerecalc, const intwaitsecs)</h3>
<p>Gets the checksum of a file in the catalog. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>csumtype</i> The wanted checksum type (CS, AD or MD. We can also pass a long checksum name (e.g. checksum.adler32))<br />
 <i>csumvalue</i> The wanted checksum value will be written into this string. Make sure it has enough space.<br />
 <i>maxcksumlen</i> Max allowed length for a checksum, to avoid buffer overflows.<br />
 <i>pfn</i> Optional: the corresponding replica for which to calculate a checksum<br />
 <i>forcerecalc</i> True if nonzero. Force recalculation of the checksum (may take long and return EAGAIN)<br />
 <i>waitsecs</i> Seconds to wait for a checksum to be calculated. Returns EAGAIN if timeouts. Set to 0 for blocking behavior.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_getcomment (<code>dmlite_context</code> *context, const char *path, char *comment, size_tbufsize)</h3>
<p>Gets the comment associated with a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>comment</i> Where to put the retrieved comment. It must be at least of size COMMENT_MAX.<br />
 <i>bufsize</i> Size of the memory zone pointed by comment.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>char* dmlite_getcwd (<code>dmlite_context</code> *context, char *buffer, size_tsize)</h3>
<p>Gets the current working directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>buffer</i> If not NULL, the path will be stored here. <code>malloc</code> will be used otherwise.<br />
 <i>size</i> The buffer size.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a string with the current working dir.</dl>
<h3>int dmlite_getgrpbynam (<code>dmlite_context</code> *context, const char *groupName, gid_t *gid)</h3>
<p>Gets the id of a group. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>groupName</i> The group name.<br />
 <i>gid</i> Where to put the group ID.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_getreplica_by_rfn (<code>dmlite_context</code> *context, const char *rfn, <code>dmlite_replica</code> *replica)</h3>
<p>Gets a specific replica. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>rfn</i> The replica file name.<br />
 <i>replica</i> A buffer where the retrieved data will be put.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_getreplicas (<code>dmlite_context</code> *context, const char *path, unsigned *nReplicas, <code>dmlite_replica</code> **fileReplicas)</h3>
<p>Gets the replicas of a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical file name.<br />
 <i>nReplicas</i> The number of entries will be put here.<br />
 <i>fileReplicas</i> An array with nEntries elements will be stored here. <code>Use dmlite_replicas_free to free it.</code></dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_getusrbynam (<code>dmlite_context</code> *context, const char *userName, uid_t *uid)</h3>
<p>Get the user id. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>userName</i> The user name.<br />
 <i>uid</i> Where to put the user ID.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_lchown (<code>dmlite_context</code> *context, const char *path, uid_tnewUid, gid_tnewGid)</h3>
<p>Changes the owner of a file, directory or symlink (does not follow). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>newUid</i> The new owner.<br />
 <i>newGid</i> The new group.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_mkdir (<code>dmlite_context</code> *context, const char *path, mode_tmode)</h3>
<p>Creates a new directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The directory for the new path. All the precedent folders must exist.<br />
 <i>mode</i> Permissions to use for the creation.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3><code>dmlite_dir</code>* dmlite_opendir (<code>dmlite_context</code> *context, const char *path)</h3>
<p>Opens a directory to read it later. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The directory to open.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to an internal structure, or NULL on failure.</dl>
<h3>struct dirent* dmlite_readdir (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)</h3>
<p>Reads an entry from a directory. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The pointer returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a struct with the recovered data. NULL on failure, or end of dir. If an error occurred, dm_errno(context) will be different than 0.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The pointer is internally allocated. Do not free it.</dl>
<h3><code>dmlite_xstat</code>* dmlite_readdirx (<code>dmlite_context</code> *context, <code>dmlite_dir</code> *dir)</h3>
<p>Reads an entry from a directory (extended data). </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>dir</i> The pointer returned by dmlite_opendir.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>A pointer to a struct with the recovered data. NULL on failure, or end of dir. If an error occurred, dm_errno(context) will be different than 0.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>The pointer is internally allocated. Do not free it.</dl>
<h3>int dmlite_readlink (<code>dmlite_context</code> *context, const char *path, char *buf, size_tbufsize)</h3>
<p>Reads a symlink. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The symlink file.<br />
 <i>buf</i> Where to put the symlink target.<br />
 <i>bufsize</i> The size of the memory pointed by buf.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_rename (<code>dmlite_context</code> *context, const char *oldPath, const char *newPath)</h3>
<p>Renames a file, directory or symlink. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>oldPath</i> The old name.<br />
 <i>newPath</i> The new name.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_replicas_free (unsignednReplicas, <code>dmlite_replica</code> *fileReplicas)</h3>
<p>Frees a replica list. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>nReplicas</i> The number of replicas contained in the array.<br />
 <i>fileReplicas</i> The array to free.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_rmdir (<code>dmlite_context</code> *context, const char *path)</h3>
<p>Deletes a directory. It must be empty. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The directory to remove.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_rstatx (<code>dmlite_context</code> *context, const char *rfn, <code>dmlite_xstat</code> *buf)</h3>
<p>Does an extended stat of a logical file using an associated replica filename. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>rfn</i> Replica filename.<br />
 <i>buf</i> Where to put the retrieved information.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_setacl (<code>dmlite_context</code> *context, const char *path, unsignednEntries, <code>dmlite_aclentry</code> *acl)</h3>
<p>Changes the ACL of a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>nEntries</i> The number of entries in the acl array.<br />
 <i>acl</i> An ACL array.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>0 on success, error code otherwise.</dl>
<h3>int dmlite_setcomment (<code>dmlite_context</code> *context, const char *path, const char *comment)</h3>
<p>Sets the comment associated with a file. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>context</i> The DM context.<br />
 <i>path</i> The logical path.<br />
 <i>comment</i> The comment to associate. &#8216;
