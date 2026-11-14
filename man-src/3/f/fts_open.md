---
title: "fts_open(3)"
name: "fts_open"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fts_open/"
description: "fts, fts_open, fts_read, fts_children, fts_set, fts_close – traverse a file hierarchy"
---

<h2 class="name">NAME</h2>
<p> fts, fts_open, fts_read, fts_children, fts_set, fts_close &#8211; traverse a file hierarchy </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;fts.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
FTS *fts_open(char *const *path_argv, int options,
              int (*compar)(const FTSENT **, const FTSENT **));
FTSENT *fts_read(FTS *ftsp);
FTSENT *fts_children(FTS *ftsp, int instr);
int fts_set(FTS *ftsp, FTSENT *f, int instr);
int fts_close(FTS *ftsp);
</code></pre>
<h2>DESCRIPTION</h2>
<p> The fts functions are provided for traversing file hierarchies. A simple overview is that the <code>fts_open</code>() function returns a &quot;handle&quot; (of type <i>FTS&nbsp;*</i>) that refers to a file hierarchy &quot;stream&quot;. This handle is then supplied to the other fts functions. The function <code>fts_read</code>() returns a pointer to a structure describing one of the files in the file hierarchy. The function <code>fts_children</code>() returns a pointer to a linked list of structures, each of which describes one of the files contained in a directory in the hierarchy. </p>
<p> In general, directories are visited two distinguishable times; in preorder (before any of their descendants are visited) and in postorder (after all of their descendants have been visited). Files are visited once. It is possible to walk the hierarchy &quot;logically&quot; (visiting the files that symbolic links point to) or physically (visiting the symbolic links themselves), order the walk of the hierarchy or prune and/or revisit portions of the hierarchy. </p>
<p> Two structures (and associated types) are defined in the include file <i>&lt;fts.h&gt;</i>. The first type is <i>FTS</i>, the structure that represents the file hierarchy itself. The second type is <i>FTSENT</i>, the structure that represents a file in the file hierarchy. Normally, an <i>FTSENT</i> structure is returned for every file in the file hierarchy. In this manual page, &quot;file&quot; and &quot;FTSENT structure&quot; are generally interchangeable. </p>
<p> The <i>FTSENT</i> structure contains fields describing a file. The structure contains at least the following fields (there are additional fields that should be considered private to the implementation): </p>
<p> typedef struct _ftsent {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned short&nbsp;<wbr>&nbsp;fts_info;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;flags for FTSENT structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*fts_accpath;&nbsp;<wbr>&nbsp;/*&nbsp;access path&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*fts_path;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;root path&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fts_pathlen;&nbsp;<wbr>&nbsp;/*&nbsp;strlen(fts_path)&nbsp;+<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strlen(fts_name)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*fts_name;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;filename&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fts_namelen;&nbsp;<wbr>&nbsp;/*&nbsp;strlen(fts_name)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;short&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fts_level;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;depth&nbsp;(-1 to N)&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fts_errno;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;file errno&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;long&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fts_number;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;local numeric value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*fts_pointer;&nbsp;<wbr>&nbsp;/*&nbsp;local address value&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;_ftsent&nbsp;*fts_parent;&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;parent directory&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;_ftsent&nbsp;*fts_link;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;next file structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct&nbsp;_ftsent&nbsp;*fts_cycle;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;cycle structure&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;struct stat&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*fts_statp;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;<a href="/docs/linux/man/2-stat/">stat</a>(2)&nbsp;information&nbsp;*/ } FTSENT; </p>
<p> These fields are defined as follows:</p>
<dl>
<dt><i>fts_info</i></p>
<dd> One of the following values describing the returned <i>FTSENT</i> structure and the file it represents. With the exception of directories without errors (<code>FTS_D</code>), all of these entries are terminal, that is, they will not be revisited, nor will any of their descendants be visited.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>FTS_D</code></p>
<dd> A directory being visited in preorder.</p>
<dt><code>FTS_DC</code></p>
<dd> A directory that causes a cycle in the tree. (The <i>fts_cycle</i> field of the <i>FTSENT</i> structure will be filled in as well.)</p>
<dt><code>FTS_DEFAULT</code></p>
<dd> Any <i>FTSENT</i> structure that represents a file type not explicitly described by one of the other <i>fts_info</i> values.</p>
<dt><code>FTS_DNR</code></p>
<dd> A directory which cannot be read. This is an error return, and the <i>fts_errno</i> field will be set to indicate what caused the error.</p>
<dt><code>FTS_DOT</code></p>
<dd> A file named &quot;.&quot; or &quot;..&quot; which was not specified as a filename to <code>fts_open</code>() (see <code>FTS_SEEDOT</code>).</p>
<dt><code>FTS_DP</code></p>
<dd> A directory being visited in postorder. The contents of the <i>FTSENT</i> structure will be unchanged from when it was returned in preorder, that is, with the <i>fts_info</i> field set to <code>FTS_D</code>.</p>
<dt><code>FTS_ERR</code></p>
<dd> This is an error return, and the <i>fts_errno</i> field will be set to indicate what caused the error.</p>
<dt><code>FTS_F</code></p>
<dd> A regular file.</p>
<dt><code>FTS_NS</code></p>
<dd> A file for which no <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) information was available. The contents of the <i>fts_statp</i> field are undefined. This is an error return, and the <i>fts_errno</i> field will be set to indicate what caused the error.</p>
<dt><code>FTS_NSOK</code></p>
<dd> A file for which no <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) information was requested. The contents of the <i>fts_statp</i> field are undefined.</p>
<dt><code>FTS_SL</code></p>
<dd> A symbolic link.</p>
<dt><code>FTS_SLNONE</code></p>
<dd> A symbolic link with a nonexistent target. The contents of the <i>fts_statp</i> field reference the file characteristic information for the symbolic link itself.</dl>
</dl>
<dt><i>fts_accpath</i></p>
<dd> A path for accessing the file from the current directory.</p>
<dt><i>fts_path</i></p>
<dd> The path for the file relative to the root of the traversal. This path contains the path specified to <code>fts_open</code>() as a prefix.</p>
<dt><i>fts_pathlen</i></p>
<dd> The sum of the lengths of the strings referenced by <i>fts_path</i> and <i>fts_name</i>.</p>
<dt><i>fts_name</i></p>
<dd> The name of the file.</p>
<dt><i>fts_namelen</i></p>
<dd> The length of the string referenced by <i>fts_name</i>.</p>
<dt><i>fts_level</i></p>
<dd> The depth of the traversal, numbered from -1 to N, where this file was found. The <i>FTSENT</i> structure representing the parent of the starting point (or root) of the traversal is numbered -1, and the <i>FTSENT</i> structure for the root itself is numbered 0.</p>
<dt><i>fts_errno</i></p>
<dd> If <code>fts_children</code>() or <code>fts_read</code>() returns an <i>FTSENT</i> structure whose <i>fts_info</i> field is set to <code>FTS_DNR</code>, <code>FTS_ERR</code>, or <code>FTS_NS</code>, the <i>fts_errno</i> field contains the error number (i.e., the <i>errno</i> value) specifying the cause of the error. Otherwise, the contents of the <i>fts_errno</i> field are undefined.</p>
<dt><i>fts_number</i></p>
<dd> This field is provided for the use of the application program and is not modified by the fts functions. It is initialized to 0.</p>
<dt><i>fts_pointer</i></p>
<dd> This field is provided for the use of the application program and is not modified by the fts functions. It is initialized to NULL.</p>
<dt><i>fts_parent</i></p>
<dd> A pointer to the <i>FTSENT</i> structure referencing the file in the hierarchy immediately above the current file, that is, the directory of which this file is a member. A parent structure for the initial entry point is provided as well, however, only the <i>fts_level</i>, <i>fts_number</i>, and <i>fts_pointer</i> fields are guaranteed to be initialized.</p>
<dt><i>fts_link</i></p>
<dd> Upon return from the <code>fts_children</code>() function, the <i>fts_link</i> field points to the next structure in the NULL-terminated linked list of directory members. Otherwise, the contents of the <i>fts_link</i> field are undefined.</p>
<dt><i>fts_cycle</i></p>
<dd> If a directory causes a cycle in the hierarchy (see <code>FTS_DC</code>), either because of a hard link between two directories, or a symbolic link pointing to a directory, the <i>fts_cycle</i> field of the structure will point to the <i>FTSENT</i> structure in the hierarchy that references the same file as the current <i>FTSENT</i> structure. Otherwise, the contents of the <i>fts_cycle</i> field are undefined.</p>
<dt><i>fts_statp</i></p>
<dd> A pointer to <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2) information for the file.</dl>
<p> A single buffer is used for all of the paths of all of the files in the file hierarchy. Therefore, the <i>fts_path</i> and <i>fts_accpath</i> fields are guaranteed to be null-terminated <i>only</i> for the file most recently returned by <code>fts_read</code>(). To use these fields to reference any files represented by other <i>FTSENT</i> structures will require that the path buffer be modified using the information contained in that <i>FTSENT</i> structure&#8217;s <i>fts_pathlen</i> field. Any such modifications should be undone before further calls to <code>fts_read</code>() are attempted. The <i>fts_name</i> field is always null-terminated.</p>
<h3>fts_open()</h3>
<p> The <code>fts_open</code>() function takes a pointer to an array of character pointers naming one or more paths which make up a logical file hierarchy to be traversed. The array must be terminated by a null pointer. </p>
<p> There are a number of options, at least one of which (either <code>FTS_LOGICAL</code> or <code>FTS_PHYSICAL</code>) must be specified. The options are selected by ORing the following values:</p>
<dl>
<dt><code>FTS_COMFOLLOW</code></p>
<dd> This option causes any symbolic link specified as a root path to be followed immediately whether or not <code>FTS_LOGICAL</code> is also specified.</p>
<dt><code>FTS_LOGICAL</code></p>
<dd> This option causes the fts routines to return <i>FTSENT</i> structures for the targets of symbolic links instead of the symbolic links themselves. If this option is set, the only symbolic links for which <i>FTSENT</i> structures are returned to the application are those referencing nonexistent files. Either <code>FTS_LOGICAL</code> or <code>FTS_PHYSICAL</code> <i>must</i> be provided to the <code>fts_open</code>() function.</p>
<dt><code>FTS_NOCHDIR</code></p>
<dd> As a performance optimization, the fts functions change directories as they walk the file hierarchy. This has the side-effect that an application cannot rely on being in any particular directory during the traversal. The <code>FTS_NOCHDIR</code> option turns off this optimization, and the fts functions will not change the current directory. Note that applications should not themselves change their current directory and try to access files unless <code>FTS_NOCHDIR</code> is specified and absolute pathnames were provided as arguments to <code>fts_open</code>().</p>
<dt><code>FTS_NOSTAT</code></p>
<dd> By default, returned <i>FTSENT</i> structures reference file characteristic information (the <i>statp</i> field) for each file visited. This option relaxes that requirement as a performance optimization, allowing the fts functions to set the <i>fts_info</i> field to <code>FTS_NSOK</code> and leave the contents of the <i>statp</i> field undefined.</p>
<dt><code>FTS_PHYSICAL</code></p>
<dd> This option causes the fts routines to return <i>FTSENT</i> structures for symbolic links themselves instead of the target files they point to. If this option is set, <i>FTSENT</i> structures for all symbolic links in the hierarchy are returned to the application. Either <code>FTS_LOGICAL</code> or <code>FTS_PHYSICAL</code> <i>must</i> be provided to the <code>fts_open</code>() function.</p>
<dt><code>FTS_SEEDOT</code></p>
<dd> By default, unless they are specified as path arguments to <code>fts_open</code>(), any files named &quot;.&quot; or &quot;..&quot; encountered in the file hierarchy are ignored. This option causes the fts routines to return <i>FTSENT</i> structures for them.</p>
<dt><code>FTS_XDEV</code></p>
<dd> This option prevents fts from descending into directories that have a different device number than the file from which the descent began.</dl>
<p> The argument <code>compar</code>() specifies a user-defined function which may be used to order the traversal of the hierarchy. It takes two pointers to pointers to <i>FTSENT</i> structures as arguments and should return a negative value, zero, or a positive value to indicate if the file referenced by its first argument comes before, in any order with respect to, or after, the file referenced by its second argument. The <i>fts_accpath</i>, <i>fts_path</i>, and <i>fts_pathlen</i> fields of the <i>FTSENT</i> structures may <i>never</i> be used in this comparison. If the <i>fts_info</i> field is set to <code>FTS_NS</code> or <code>FTS_NSOK</code>, the <i>fts_statp</i> field may not either. If the <code>compar</code>() argument is NULL, the directory traversal order is in the order listed in <i>path_argv</i> for the root paths, and in the order listed in the directory for everything else.</p>
<h3>fts_read()</h3>
<p> The <code>fts_read</code>() function returns a pointer to an <i>FTSENT</i> structure describing a file in the hierarchy. Directories (that are readable and do not cause cycles) are visited at least twice, once in preorder and once in postorder. All other files are visited at least once. (Hard links between directories that do not cause cycles or symbolic links to symbolic links may cause files to be visited more than once, or directories more than twice.) </p>
<p> If all the members of the hierarchy have been returned, <code>fts_read</code>() returns NULL and sets the external variable <i>errno</i> to 0. If an error unrelated to a file in the hierarchy occurs, <code>fts_read</code>() returns NULL and sets <i>errno</i> appropriately. If an error related to a returned file occurs, a pointer to an <i>FTSENT</i> structure is returned, and <i>errno</i> may or may not have been set (see <i>fts_info</i>). </p>
<p> The <i>FTSENT</i> structures returned by <code>fts_read</code>() may be overwritten after a call to <code>fts_close</code>() on the same file hierarchy stream, or, after a call to <code>fts_read</code>() on the same file hierarchy stream unless they represent a file of type directory, in which case they will not be overwritten until after a call to <code>fts_read</code>() after the <i>FTSENT</i> structure has been returned by the function <code>fts_read</code>() in postorder.</p>
<h3>fts_children()</h3>
<p> The <code>fts_children</code>() function returns a pointer to an <i>FTSENT</i> structure describing the first entry in a NULL-terminated linked list of the files in the directory represented by the <i>FTSENT</i> structure most recently returned by <code>fts_read</code>(). The list is linked through the <i>fts_link</i> field of the <i>FTSENT</i> structure, and is ordered by the user-specified comparison function, if any. Repeated calls to <code>fts_children</code>() will re-create this linked list. </p>
<p> As a special case, if <code>fts_read</code>() has not yet been called for a hierarchy, <code>fts_children</code>() will return a pointer to the files in the logical directory specified to <code>fts_open</code>(), that is, the arguments specified to <code>fts_open</code>(). Otherwise, if the <i>FTSENT</i> structure most recently returned by <code>fts_read</code>() is not a directory being visited in preorder, or the directory does not contain any files, <code>fts_children</code>() returns NULL and sets <i>errno</i> to zero. If an error occurs, <code>fts_children</code>() returns NULL and sets <i>errno</i> appropriately. </p>
<p> The <i>FTSENT</i> structures returned by <code>fts_children</code>() may be overwritten after a call to <code>fts_children</code>(), <code>fts_close</code>(), or <code>fts_read</code>() on the same file hierarchy stream. </p>
<p> The <i>instr</i> argument is either zero or the following value:</p>
<dl>
<dt><code>FTS_NAMEONLY</code></p>
<dd> Only the names of the files are needed. The contents of all the fields in the returned linked list of structures are undefined with the exception of the <i>fts_name</i> and <i>fts_namelen</i> fields.</dl>
<h3>fts_set()</h3>
<p> The function <code>fts_set</code>() allows the user application to determine further processing for the file <i>f</i> of the stream <i>ftsp</i>. The <code>fts_set</code>() function returns 0 on success, and -1 if an error occurs. </p>
<p> The <i>instr</i> argument is either 0 (meaning &quot;do nothing&quot;) or one of the following values:</p>
<dl>
<dt><code>FTS_AGAIN</code></p>
<dd> Revisit the file; any file type may be revisited. The next call to <code>fts_read</code>() will return the referenced file. The <i>fts_stat</i> and <i>fts_info</i> fields of the structure will be reinitialized at that time, but no other fields will have been changed. This option is meaningful only for the most recently returned file from <code>fts_read</code>(). Normal use is for postorder directory visits, where it causes the directory to be revisited (in both preorder and postorder) as well as all of its descendants.</p>
<dt><code>FTS_FOLLOW</code></p>
<dd> The referenced file must be a symbolic link. If the referenced file is the one most recently returned by <code>fts_read</code>(), the next call to <code>fts_read</code>() returns the file with the <i>fts_info</i> and <i>fts_statp</i> fields reinitialized to reflect the target of the symbolic link instead of the symbolic link itself. If the file is one of those most recently returned by <code>fts_children</code>(), the <i>fts_info</i> and <i>fts_statp</i> fields of the structure, when returned by <code>fts_read</code>(), will reflect the target of the symbolic link instead of the symbolic link itself. In either case, if the target of the symbolic link does not exist, the fields of the returned structure will be unchanged and the <i>fts_info</i> field will be set to <code>FTS_SLNONE</code>.</p>
<dt>
<dd> If the target of the link is a directory, the preorder return, followed by the return of all of its descendants, followed by a postorder return, is done.</p>
<dt><code>FTS_SKIP</code></p>
<dd> No descendants of this file are visited. The file may be one of those most recently returned by either <code>fts_children</code>() or <code>fts_read</code>().</dl>
<h3>fts_close()</h3>
<p> The <code>fts_close</code>() function closes the file hierarchy stream referred to by <i>ftsp</i> and restores the current directory to the directory from which <code>fts_open</code>() was called to open <i>ftsp</i>. The <code>fts_close</code>() function returns 0 on success, and -1 if an error occurs.</p>
<h2>ERRORS</h2>
<p> The function <code>fts_open</code>() may fail and set <i>errno</i> for any of the errors specified for <code><a href="/docs/linux/man/2-open/">open</a></code>(2) and <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3). </p>
<p> The function <code>fts_close</code>() may fail and set <i>errno</i> for any of the errors specified for <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2) and <code><a href="/docs/linux/man/2-close/">close</a></code>(2). </p>
<p> The functions <code>fts_read</code>() and <code>fts_children</code>() may fail and set <i>errno</i> for any of the errors specified for <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/3-malloc/">malloc</a></code>(3), <code><a href="/docs/linux/man/3-opendir/">opendir</a></code>(3), <code><a href="/docs/linux/man/3-readdir/">readdir</a></code>(3), and <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2). </p>
<p> In addition, <code>fts_children</code>(), <code>fts_open</code>(), and <code>fts_set</code>() may fail and set <i>errno</i> as follows:</p>
<dl>
<dt><code>EINVAL</code></p>
<dd> <i>options</i> or <i>instr</i> was invalid.</dl>
<h2>VERSIONS</h2>
<p> These functions are available in Linux since glibc2.</p>
<h2>ATTRIBUTES</h2>
<p> For an explanation of the terms used in this section, see <code><a href="/docs/linux/man/7-attributes/">attributes</a></code>(7). </p>
<table BORDER>
<tr VALIGN=top>
<td><code>Interface</code></td>
<td><code>Attribute</code></td>
<td><code>Value</code>
</td>
</tr>
<tr VALIGN=top>
<td> <code>fts_open</code>(), <code>fts_set</code>(), <code>fts_close</code>() </td>
<td>Thread safety</td>
<td>MT-Safe
</td>
</tr>
<tr VALIGN=top>
<td> <code>fts_read</code>(), <code>fts_children</code>() </td>
<td>Thread safety</td>
<td>MT-Unsafe
</td>
</tr>
</table>
<h2>CONFORMING TO</h2>
<p> 4.4BSD.</p>
<h2>BUGS</h2>
<p> In versions of glibc before 2.23, all of the APIs described in this man page are not safe when compiling a program using the LFS APIs (e.g., when compiling with <i>-D_FILE_OFFSET_BITS=64</i>).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-find/">find</a></code>(1), <code><a href="/docs/linux/man/2-chdir/">chdir</a></code>(2), <code><a href="/docs/linux/man/2-stat/">stat</a></code>(2), <code><a href="/docs/linux/man/3-ftw/">ftw</a></code>(3), <code><a href="/docs/linux/man/3-qsort/">qsort</a></code>(3)</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
