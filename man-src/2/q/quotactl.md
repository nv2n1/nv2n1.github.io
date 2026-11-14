---
title: "quotactl(2)"
name: "quotactl"
section: "2"
letter: "q"
url: "/docs/linux/man/2-quotactl/"
description: "quotactl – manipulate disk quotas"
---

<h2 class="name">NAME</h2>
<p> quotactl &#8211; manipulate disk quotas </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;sys/quota.h&gt;
#include &lt;xfs/xqm.h&gt; /* for XFS quotas */
int quotactl(int cmd, const char *special, int id, caddr_t addr);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The quota system can be used to set per-user, per-group, and per-project limits on the amount of disk space used on a filesystem. For each user and/or group, a soft limit and a hard limit can be set for each filesystem. The hard limit can&#8217;t be exceeded. The soft limit can be exceeded, but warnings will ensue. Moreover, the user can&#8217;t exceed the soft limit for more than grace period duration (one week by default) at a time; after this, the soft limit counts as a hard limit. </p>
<p> The <code>quotactl</code>() call manipulates disk quotas. The <i>cmd</i> argument indicates a command to be applied to the user or group ID specified in <i>id</i>. To initialize the <i>cmd</i> argument, use the <i>QCMD(subcmd, type)</i> macro. The <i>type</i> value is either <code>USRQUOTA</code>, for user quotas, <code>GRPQUOTA</code>, for group quotas, or (since Linux 4.1) <code>PRJQUOTA</code>, for project quotas. The <i>subcmd</i> value is described below. </p>
<p> The <i>special</i> argument is a pointer to a null-terminated string containing the pathname of the (mounted) block special device for the filesystem being manipulated. </p>
<p> The <i>addr</i> argument is the address of an optional, command-specific, data structure that is copied in or out of the system. The interpretation of <i>addr</i> is given with each operation below. </p>
<p> The <i>subcmd</i> value is one of the following operations:</p>
<dl>
<dt><code>Q_QUOTAON</code></p>
<dd> Turn on quotas for a filesystem. The <i>id</i> argument is the identification number of the quota format to be used. Currently, there are three supported quota formats:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>QFMT_VFS_OLD</code></p>
<dd> The original quota format.</p>
<dt><code>QFMT_VFS_V0</code></p>
<dd> The standard VFS v0 quota format, which can handle 32-bit UIDs and GIDs and quota limits up to 2^42 bytes and 2^32 inodes.</p>
<dt><code>QFMT_VFS_V1</code></p>
<dd> A quota format that can handle 32-bit UIDs and GIDs and quota limits of 2^64 bytes and 2^64 inodes.</dl>
</dl>
<dt>
<dd> The <i>addr</i> argument points to the pathname of a file containing the quotas for the filesystem. The quota file must exist; it is normally created with the <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8) program</p>
<dt>
<dd> Quota information can be also stored in hidden system inodes for ext4, XFS, and other filesystems if the filesystem is configured so. In this case, there are no visible quota files and there is no need to use <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8). Quota information is always kept consistent by the filesystem and the <code>Q_QUOTAON</code> operation serves only to enable enforcement of quota limits. The presence of hidden system inodes with quota information is indicated by the <code>DQF_SYS_FILE</code> flag in the <i>dqi_flags</i> field returned by the <code>Q_GETINFO</code> operation.</p>
<dt>
<dd> This operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<dt><code>Q_QUOTAOFF</code></p>
<dd> Turn off quotas for a filesystem. The <i>addr</i> and <i>id</i> arguments are ignored. This operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<dt><code>Q_GETQUOTA</code></p>
<dd> Get disk quota limits and current usage for user or group <i>id</i>. The <i>addr</i> argument is a pointer to a <i>dqblk</i> structure defined in <i>&lt;sys/quota.h&gt;</i> as follows:</p>
<dt>
<dd> /* uint64_t is an unsigned 64-bit integer;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t is an unsigned 32-bit integer&nbsp;*/ </p>
<p> struct dqblk { /* Definition since Linux 2.4.22 */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_bhardlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Absolute limit on disk<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;quota blocks alloc&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_bsoftlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Preferred limit on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk quota blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_curspace;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Current occupied space<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(in bytes)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_ihardlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Maximum number of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocated inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_isoftlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Preferred inode limit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_curinodes;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Current number of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;allocated inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_btime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Time limit for excessive<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk use&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_itime;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Time limit for excessive<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;files&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dqb_valid;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Bit mask of QIF_*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;constants&nbsp;*/ }; </p>
<p> /* Flags in dqb_valid that indicate which fields in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;dqblk structure are valid.&nbsp;*/ </p>
<p> #define QIF_BLIMITS 1 #define QIF_SPACE 2 #define QIF_ILIMITS 4 #define QIF_INODES 8 #define QIF_BTIME 16 #define QIF_ITIME 32 #define QIF_LIMITS (QIF_BLIMITS | QIF_ILIMITS) #define QIF_USAGE (QIF_SPACE | QIF_INODES) #define QIF_TIMES (QIF_BTIME | QIF_ITIME) #define QIF_ALL (QIF_LIMITS | QIF_USAGE | QIF_TIMES)</p>
<dt>
<dd> The <i>dqb_valid</i> field is a bit mask that is set to indicate the entries in the <i>dqblk</i> structure that are valid. Currently, the kernel fills in all entries of the <i>dqblk</i> structure and marks them as valid in the <i>dqb_valid</i> field. Unprivileged users may retrieve only their own quotas; a privileged user (<code>CAP_SYS_ADMIN</code>) can retrieve the quotas of any user.</p>
<dt><code>Q_GETNEXTQUOTA</code> (since Linux 4.6)</p>
<dd> This operation is the same as <code>Q_GETQUOTA</code>, but it returns quota information for the next ID greater than or equal to <i>id</i> that has a quota set.</p>
<dt>
<dd> The <i>addr</i> argument is a pointer to a <i>nextdqblk</i> structure whose fields are as for the <i>dqblk</i>, except for the addition of a <i>dqb_id</i> field that is used to return the ID for which quota information is being returned:</p>
<dt>
<dd> struct nextdqblk {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_bhardlimit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_bsoftlimit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_curspace;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_ihardlimit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_isoftlimit;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_curinodes;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_btime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqb_itime;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dqb_valid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dqb_id; };</p>
<dt><code>Q_SETQUOTA</code></p>
<dd> Set quota information for user or group <i>id</i>, using the information supplied in the <i>dqblk</i> structure pointed to by <i>addr</i>. The <i>dqb_valid</i> field of the <i>dqblk</i> structure indicates which entries in the structure have been set by the caller. This operation supersedes the <code>Q_SETQLIM</code> and <code>Q_SETUSE</code> operations in the previous quota interfaces. This operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<dt><code>Q_GETINFO</code> (since Linux 2.4.22)</p>
<dd> Get information (like grace times) about quotafile. The <i>addr</i> argument should be a pointer to a <i>dqinfo</i> structure. This structure is defined in <i>&lt;sys/quota.h&gt;</i> as follows:</p>
<dt>
<dd> /* uint64_t is an unsigned 64-bit integer;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t is an unsigned 32-bit integer&nbsp;*/ </p>
<p> struct dqinfo { /* Defined since kernel 2.4.22 */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqi_bgrace;&nbsp;<wbr>&nbsp;/*&nbsp;Time before block soft limit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;becomes hard limit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t dqi_igrace;&nbsp;<wbr>&nbsp;/*&nbsp;Time before inode soft limit<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;becomes hard limit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dqi_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Flags for quotafile<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(DQF_*)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t dqi_valid; }; </p>
<p> /* Bits for dqi_flags */ </p>
<p> /* Quota format QFMT_VFS_OLD */ </p>
<p> #define DQF_ROOT_SQUASH (1 &lt;&lt; 0) /* Root squash enabled */<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Before Linux v4.0, this had been defined<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;privately as V1_DQF_RSQUASH&nbsp;*/ </p>
<p> /* Quota format QFMT_VFS_V0 / QFMT_VFS_V1 */ </p>
<p> #define DQF_SYS_FILE (1 &lt;&lt; 16) /* Quota stored in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;a system file&nbsp;*/ </p>
<p> /* Flags in dqi_valid that indicate which fields in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;dqinfo structure are valid.&nbsp;*/ </p>
<p> #define IIF_BGRACE 1 #define IIF_IGRACE 2 #define IIF_FLAGS 4 #define IIF_ALL (IIF_BGRACE | IIF_IGRACE | IIF_FLAGS)</p>
<dt>
<dd> The <i>dqi_valid</i> field in the <i>dqinfo</i> structure indicates the entries in the structure that are valid. Currently, the kernel fills in all entries of the <i>dqinfo</i> structure and marks them all as valid in the <i>dqi_valid</i> field. The <i>id</i> argument is ignored.</p>
<dt><code>Q_SETINFO</code> (since Linux 2.4.22)</p>
<dd> Set information about quotafile. The <i>addr</i> argument should be a pointer to a <i>dqinfo</i> structure. The <i>dqi_valid</i> field of the <i>dqinfo</i> structure indicates the entries in the structure that have been set by the caller. This operation supersedes the <code>Q_SETGRACE</code> and <code>Q_SETFLAGS</code> operations in the previous quota interfaces. The <i>id</i> argument is ignored. This operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<dt><code>Q_GETFMT</code> (since Linux 2.4.22)</p>
<dd> Get quota format used on the specified filesystem. The <i>addr</i> argument should be a pointer to a 4-byte buffer where the format number will be stored.</p>
<dt><code>Q_SYNC</code></p>
<dd> Update the on-disk copy of quota usages for a filesystem. If <i>special</i> is NULL, then all filesystems with active quotas are sync&#8217;ed. The <i>addr</i> and <i>id</i> arguments are ignored.</p>
<dt><code>Q_GETSTATS</code> (supported up to Linux 2.4.21)</p>
<dd> Get statistics and other generic information about the quota subsystem. The <i>addr</i> argument should be a pointer to a <i>dqstats</i> structure in which data should be stored. This structure is defined in <i>&lt;sys/quota.h&gt;</i>. The <i>special</i> and <i>id</i> arguments are ignored.</p>
<dt>
<dd> This operation is obsolete and was removed in Linux 2.4.22. Files in <i>/proc/sys/fs/quota/</i> carry the information instead.</dl>
<p> For XFS filesystems making use of the XFS Quota Manager (XQM), the above operations are bypassed and the following operations are used:</p>
<dl>
<dt><code>Q_XQUOTAON</code></p>
<dd> Turn on quotas for an XFS filesystem. XFS provides the ability to turn on/off quota limit enforcement with quota accounting. Therefore, XFS expects <i>addr</i> to be a pointer to an <i>unsigned int</i> that contains a bitwise combination of the following flags (defined in <i>&lt;xfs/xqm.h&gt;</i>):</p>
<dt>
<dd> XFS_QUOTA_UDQ_ACCT /* User quota accounting */ XFS_QUOTA_UDQ_ENFD /* User quota limits enforcement */ XFS_QUOTA_GDQ_ACCT /* Group quota accounting */ XFS_QUOTA_GDQ_ENFD /* Group quota limits enforcement */ XFS_QUOTA_PDQ_ACCT /* Project quota accounting */ XFS_QUOTA_PDQ_ENFD /* Project quota limits enforcement */</p>
<dt>
<dd> This operation requires privilege (<code>CAP_SYS_ADMIN</code>). The <i>id</i> argument is ignored.</p>
<dt><code>Q_XQUOTAOFF</code></p>
<dd> Turn off quotas for an XFS filesystem. As with <code>Q_QUOTAON</code>, XFS filesystems expect a pointer to an <i>unsigned int</i> that specifies whether quota accounting and/or limit enforcement need to be turned off (using the same flags as for <code>Q_XQUOTAON</code> operation). This operation requires privilege (<code>CAP_SYS_ADMIN</code>). The <i>id</i> argument is ignored.</p>
<dt><code>Q_XGETQUOTA</code></p>
<dd> Get disk quota limits and current usage for user <i>id</i>. The <i>addr</i> argument is a pointer to an <i>fs_disk_quota</i> structure, which is defined in <i>&lt;xfs/xqm.h&gt;</i> as follows:</p>
<dt>
<dd> /* All the blk units are in BBs (Basic Blocks) of<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;512 bytes.&nbsp;*/ </p>
<p> #define FS_DQUOT_VERSION 1 /* fs_disk_quota.d_version */ </p>
<p> #define XFS_USER_QUOTA (1&lt;&lt;0) /* User quota type */ #define XFS_PROJ_QUOTA (1&lt;&lt;1) /* Project quota type */ #define XFS_GROUP_QUOTA (1&lt;&lt;2) /* Group quota type */ </p>
<p> struct fs_disk_quota {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int8_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_version;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Version of this structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int8_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;XFS_{USER,PROJ,GROUP}_QUOTA&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t d_fieldmask;&nbsp;/*&nbsp;Field specifier&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t d_id;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;User, project, or group ID&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_blk_hardlimit;&nbsp;/*&nbsp;Absolute limit on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_blk_softlimit;&nbsp;/*&nbsp;Preferred limit on<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_ino_hardlimit;&nbsp;/*&nbsp;Maximum&nbsp;#&nbsp;allocated<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_ino_softlimit;&nbsp;/*&nbsp;Preferred inode limit&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_bcount;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;disk blocks owned by<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;the user&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_icount;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;inodes owned by the user&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;d_itimer;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Zero if within inode limits&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;If not, we refuse service&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;d_btimer;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Similar to above;&nbsp;for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t d_iwarns;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;warnings issued with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;respect to&nbsp;#&nbsp;of inodes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t d_bwarns;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;warnings issued with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;respect to disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;d_padding2;&nbsp;<wbr>&nbsp;/*&nbsp;Padding &#8211; for future use&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_rtb_hardlimit;&nbsp;/*&nbsp;Absolute limit on realtime<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(RT)&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_rtb_softlimit;&nbsp;/*&nbsp;Preferred limit on RT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t d_rtbcount;&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;realtime blocks owned&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;d_rtbtimer;&nbsp;<wbr>&nbsp;/*&nbsp;Similar to above;&nbsp;for RT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t d_rtbwarns;&nbsp;<wbr>&nbsp;/*&nbsp;#&nbsp;warnings issued with<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;respect to RT disk blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int16_t&nbsp;<wbr>&nbsp;d_padding3;&nbsp;<wbr>&nbsp;/*&nbsp;Padding &#8211; for future use&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_padding4[8];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Yet more padding&nbsp;*/ };</p>
<dt>
<dd> Unprivileged users may retrieve only their own quotas; a privileged user (<code>CAP_SYS_ADMIN</code>) may retrieve the quotas of any user.</p>
<dt><code>Q_XGETNEXTQUOTA</code> (since Linux 4.6)</p>
<dd> This operation is the same as <code>Q_XGETQUOTA</code>, but it returns (in the <i>fs_disk_quota</i> structure pointed by <i>addr</i>) quota information for the next ID greater than or equal to <i>id</i> that has a quota set. Note that since <i>fs_disk_quota</i> already has <i>q_id</i> field, no separate structure type is needed (in contrast with <code>Q_GETQUOTA</code> and <code>Q_GETNEXTQUOTA</code> operations)</p>
<dt><code>Q_XSETQLIM</code></p>
<dd> Set disk quota limits for user <i>id</i>. The <i>addr</i> argument is a pointer to an <i>fs_disk_quota</i> structure. This operation requires privilege (<code>CAP_SYS_ADMIN</code>).</p>
<dt><code>Q_XGETQSTAT</code></p>
<dd> Returns XFS filesystem-specific quota information in the <i>fs_quota_stat</i> structure pointed by <i>addr</i>. This is useful for finding out how much space is used to store quota information, and also to get the quota on/off status of a given local XFS filesystem. The <i>fs_quota_stat</i> structure itself is defined as follows:</p>
<dt>
<dd> #define FS_QSTAT_VERSION 1 /* fs_quota_stat.qs_version */ </p>
<p> struct fs_qfilestat {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t qfs_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t qfs_nblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of BBs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;512-byte-blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t qfs_nextents;&nbsp;<wbr>&nbsp;/*&nbsp;Number of extents&nbsp;*/ }; </p>
<p> struct fs_quota_stat {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int8_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;qs_version;&nbsp;/*&nbsp;Version number for<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;future changes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_flags;&nbsp;/*&nbsp;XFS_QUOTA_{U,P,G}DQ_{ACCT,ENFD}&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int8_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;qs_pad;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Unused&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fs_qfilestat qs_uquota;&nbsp;<wbr>&nbsp;/*&nbsp;User quota storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fs_qfilestat qs_gquota;&nbsp;<wbr>&nbsp;/*&nbsp;Group quota storage<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t qs_incoredqs;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of dquots in core&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_btimelimit;&nbsp;<wbr>&nbsp;/*&nbsp;Limit for blocks timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_itimelimit;&nbsp;<wbr>&nbsp;/*&nbsp;Limit for inodes timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_rtbtimelimit;/*&nbsp;Limit for RT<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;blocks timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_bwarnlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Limit for&nbsp;#&nbsp;of warnings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_iwarnlimit;&nbsp;<wbr>&nbsp;/*&nbsp;Limit for&nbsp;#&nbsp;of warnings&nbsp;*/ };</p>
<dt>
<dd> The <i>id</i> argument is ignored.</p>
<dt><code>Q_XGETQSTATV</code></p>
<dd> Returns XFS filesystem-specific quota information in the <i>fs_quota_statv</i> pointed to by <i>addr</i>. This version of the operation uses a structure with proper versioning support, along with appropriate layout (all fields are naturally aligned) and padding to avoiding special compat handling; it also provides the ability to get statistics regarding the project quota file. The <i>fs_quota_statv</i> structure itself is defined as follows:</p>
<dt>
<dd> #define FS_QSTATV_VERSION1 1 /* fs_quota_statv.qs_version */ </p>
<p> struct fs_qfilestatv {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t qfs_ino;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Inode number&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t qfs_nblks;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Number of BBs<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;512-byte-blocks&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t qfs_nextents;&nbsp;<wbr>&nbsp;/*&nbsp;Number of extents&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t qfs_pad;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pad for 8-byte alignment&nbsp;*/ }; </p>
<p> struct fs_quota_statv {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int8_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;qs_version;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Version for future<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;changes&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint8_t&nbsp;<wbr>&nbsp;qs_pad1;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Pad for 16-bit alignment&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_flags;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;XFS_QUOTA_.*&nbsp;flags&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t qs_incoredqs;&nbsp;<wbr>&nbsp;/*&nbsp;Number of dquots incore&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fs_qfilestatv qs_uquota;&nbsp;<wbr>&nbsp;/*&nbsp;User quota<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fs_qfilestatv qs_gquota;&nbsp;<wbr>&nbsp;/*&nbsp;Group quota<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct fs_qfilestatv qs_pquota;&nbsp;<wbr>&nbsp;/*&nbsp;Project quota<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;information&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_btimelimit;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Limit for blocks timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_itimelimit;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Limit for inodes timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;qs_rtbtimelimit;&nbsp;/*&nbsp;Limit for RT blocks<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;timer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_bwarnlimit;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Limit for&nbsp;#&nbsp;of warnings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t qs_iwarnlimit;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Limit for&nbsp;#&nbsp;of warnings&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t qs_pad2[8];&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;For future proofing&nbsp;*/ };</p>
<dt>
<dd> The <i>qs_version</i> field of the structure should be filled with the version of the structure supported by the callee (for now, only <i>FS_QSTAT_VERSION1</i> is supported). The kernel will fill the structure in accordance with version provided. The <i>id</i> argument is ignored.</p>
<dt><code>Q_XQUOTARM (since Linux 3.16)</code></p>
<dd> Free the disk space taken by disk quotas. The <i>addr</i> argument should be a pointer to an <i>unsigned int</i> value containing flags (the same as in <i>d_flags</i> field of <i>fs_disk_quota</i> structure) which identify what types of quota should be removed. (Note that the quota type passed in the <i>cmd</i> argument is ignored, but should remain valid in order to pass preliminary quotactl syscall handler checks.)</p>
<dt>
<dd> Quotas must have already been turned off. The <i>id</i> argument is ignored.</p>
<dt><code>Q_XQUOTASYNC</code> (since Linux 2.6.15; no-op since Linux 3.4)</p>
<dd> This operation was an XFS quota equivalent to <code>Q_SYNC</code>, but it is no-op since Linux 3.4, as <code><a href="/docs/linux/man/1-sync/">sync</a></code>(1) writes quota information to disk now (in addition to the other filesystem metadata that it writes out). The <i>special</i>, <i>id</i> and <i>addr</i> arguments are ignored.</dl>
<h2>RETURN VALUE</h2>
<p> On success, <code>quotactl</code>() returns 0; on error -1 is returned, and <i>errno</i> is set to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> <i>cmd</i> is <code>Q_QUOTAON</code>, and the quota file pointed to by <i>addr</i> exists, but is not a regular file or is not on the filesystem pointed to by <i>special</i>.</p>
<dt><code>EBUSY</code></p>
<dd> <i>cmd</i> is <code>Q_QUOTAON</code>, but another <code>Q_QUOTAON</code> had already been performed.</p>
<dt><code>EFAULT</code></p>
<dd> <i>addr</i> or <i>special</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> or <i>type</i> is invalid.</p>
<dt><code>EINVAL</code></p>
<dd> <i>cmd</i> is <code>Q_QUOTAON</code>, but the specified quota file is corrupted.</p>
<dt><code>EINVAL</code> (since Linux 5.5)</p>
<dd> <i>cmd</i> is <code>Q_XQUOTARM</code>, but <i>addr</i> does not point to valid quota types.</p>
<dt><code>ENOENT</code></p>
<dd> The file specified by <i>special</i> or <i>addr</i> does not exist.</p>
<dt><code>ENOSYS</code></p>
<dd> The kernel has not been compiled with the <code>CONFIG_QUOTA</code> option.</p>
<dt><code>ENOTBLK</code></p>
<dd> <i>special</i> is not a block device.</p>
<dt><code>EPERM</code></p>
<dd> The caller lacked the required privilege (<code>CAP_SYS_ADMIN</code>) for the specified operation.</p>
<dt><code>ERANGE</code></p>
<dd> <i>cmd</i> is <code>Q_SETQUOTA</code>, but the specified limits are out of the range allowed by the quota format.</p>
<dt><code>ESRCH</code></p>
<dd> No disk quota is found for the indicated user. Quotas have not been turned on for this filesystem.</p>
<dt><code>ESRCH</code></p>
<dd> <i>cmd</i> is <code>Q_QUOTAON</code>, but the specified quota format was not found.</p>
<dt><code>ESRCH</code></p>
<dd> <i>cmd</i> is <code>Q_GETNEXTQUOTA</code> or <code>Q_XGETNEXTQUOTA</code>, but there is no ID greater than or equal to <i>id</i> that has an active quota.</dl>
<h2>NOTES</h2>
<p> Instead of <i>&lt;xfs/xqm.h&gt;</i> one can use <i>&lt;linux/dqblk_xfs.h&gt;</i>, taking into account that there are several naming discrepancies:</p>
<dl>
<dt>&bull;</p>
<dd> Quota enabling flags (of format <code>XFS_QUOTA_[UGP]DQ_{ACCT,ENFD}</code>) are defined without a leading &quot;X&quot;, as <code>FS_QUOTA_[UGP]DQ_{ACCT,ENFD}</code>.</p>
<dt>&bull;</p>
<dd> The same is true for <code>XFS_{USER,GROUP,PROJ}_QUOTA</code> quota type flags, which are defined as <code>FS_{USER,GROUP,PROJ}_QUOTA</code>.</p>
<dt>&bull;</p>
<dd> The <i>dqblk_xfs.h</i> header file defines its own <code>XQM_USRQUOTA</code>, <code>XQM_GRPQUOTA</code>, and <code>XQM_PRJQUOTA</code> constants for the available quota types, but their values are the same as for constants without the <code>XQM_</code> prefix.</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-quota/">quota</a></code>(1), <code><a href="/docs/linux/man/2-getrlimit/">getrlimit</a></code>(2), <code><a href="/docs/linux/man/8-quotacheck/">quotacheck</a></code>(8), <code><a href="/docs/linux/man/8-quotaon/">quotaon</a></code>(8)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
