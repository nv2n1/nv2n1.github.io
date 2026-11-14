---
title: "hivex(3)"
name: "hivex"
section: "3"
letter: "h"
url: "/docs/linux/man/3-hivex/"
---

<h2 class="name">NAME</h2>
 

 hivex - Windows Registry &quot;hive&quot; extraction library 

<h2>SYNOPSIS</h2>

 <pre><code>
#include &lt;hivex.h&gt;
hive_h *hivex_open(const char *filename, int flags);
int hivex_close(hive_h *h);
hive_node_h hivex_root(hive_h *h);
int64_t hivex_last_modified(hive_h *h);
char *hivex_node_name(hive_h *h, hive_node_h node);
size_t hivex_node_name_len(hive_h *h, hive_node_h node);
int64_t hivex_node_timestamp(hive_h *h, hive_node_h node);
hive_node_h *hivex_node_children(hive_h *h, hive_node_h node);
hive_node_h hivex_node_get_child(hive_h *h, hive_node_h node, const char *name);
hive_node_h hivex_node_parent(hive_h *h, hive_node_h node);
hive_value_h *hivex_node_values(hive_h *h, hive_node_h node);
hive_value_h hivex_node_get_value(hive_h *h, hive_node_h node, const char *key);
size_t hivex_value_key_len(hive_h *h, hive_value_h val);
char *hivex_value_key(hive_h *h, hive_value_h val);
int hivex_value_type(hive_h *h, hive_value_h val, hive_type *t, size_t *len);
size_t hivex_node_struct_length(hive_h *h, hive_node_h node);
size_t hivex_value_struct_length(hive_h *h, hive_value_h val);
hive_value_h hivex_value_data_cell_offset(hive_h *h, hive_value_h val, size_t *len);
char *hivex_value_value(hive_h *h, hive_value_h val, hive_type *t, size_t *len);
char *hivex_value_string(hive_h *h, hive_value_h val);
char **hivex_value_multiple_strings(hive_h *h, hive_value_h val);
int32_t hivex_value_dword(hive_h *h, hive_value_h val);
int64_t hivex_value_qword(hive_h *h, hive_value_h val);
int hivex_commit(hive_h *h, const char *filename, int flags);
hive_node_h hivex_node_add_child(hive_h *h, hive_node_h parent, const char *name);
int hivex_node_delete_child(hive_h *h, hive_node_h node);
int hivex_node_set_values(hive_h *h, hive_node_h node, size_t nr_values, const hive_set_value *values, int flags);
int hivex_node_set_value(hive_h *h, hive_node_h node, const hive_set_value *val, int flags);
</code></pre> 

 Link with <i>-lhivex</i>.

<h2>DESCRIPTION</h2>

 Hivex is a library for extracting the contents of Windows Registry ``hive'' files. It is designed to be secure against buggy or malicious registry files. 

 Unlike other tools in this area, it doesn't use the textual .REG format, because parsing that is as much trouble as parsing the original binary format. Instead it makes the file available through a C <font SIZE="-1">API,</font> and then wraps this <font SIZE="-1">API</font> in higher level scripting and <font SIZE="-1">GUI</font> tools. 

 There is a separate program to export the hive as <font SIZE="-1">XML </font>(see <i><a HREF="/docs/linux/man/1-hivexml/">hivexml</a></i>(1)), or to navigate the file (see <i><a HREF="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1)). There is also a Perl script to export and merge the file as a textual .REG (regedit) file, see <i><a HREF="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1). 

 If you just want to export or modify the Registry of a Windows virtual machine, you should look at <i><a HREF="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1). 

 Hivex is also comes with language bindings for OCaml, Perl, Python and Ruby.

<h2>TYPES</h2>

<h3>hive_h *</h3>

 This handle describes an open hive file.

<h3>hive_node_h</h3>

 This is a node handle, an integer but opaque outside the library. Valid node handles cannot be 0. The library returns 0 in some situations to indicate an error.

<h3>hive_type</h3>

 The enum below describes the possible types for the value(s) stored at each node. Note that you should not trust the type field in a Windows Registry, as it very often has no relationship to reality. Some applications use their own types. The encoding of strings is not specified. Some programs store everything (including strings) in binary blobs. 

 
enum hive_type {
    /* Just a key without a value */
    hive_t_REG_NONE = 0,
    /* A Windows string (encoding is unknown, but often UTF16-LE) */
    hive_t_REG_SZ = 1,
    /* A Windows string that contains %env% (environment variable expansion) */
    hive_t_REG_EXPAND_SZ = 2,
    /* A blob of binary */
    hive_t_REG_BINARY = 3,
    /* DWORD (32 bit integer), little endian */
    hive_t_REG_DWORD = 4,
    /* DWORD (32 bit integer), big endian */
    hive_t_REG_DWORD_BIG_ENDIAN = 5,
    /* Symbolic link to another part of the registry tree */
    hive_t_REG_LINK = 6,
    /* Multiple Windows strings.  See http://blogs.msdn.com/oldnewthing/archive/2009/10/08/9904646.aspx */
    hive_t_REG_MULTI_SZ = 7,
    /* Resource list */
    hive_t_REG_RESOURCE_LIST = 8,
    /* Resource descriptor */
    hive_t_REG_FULL_RESOURCE_DESCRIPTOR = 9,
    /* Resouce requirements list */
    hive_t_REG_RESOURCE_REQUIREMENTS_LIST = 10,
    /* QWORD (64 bit integer), unspecified endianness but usually little endian */
    hive_t_REG_QWORD = 11,
};


<h3>hive_value_h</h3>

 This is a value handle, an integer but opaque outside the library. Valid value handles cannot be 0. The library returns 0 in some situations to indicate an error.

<h3>hive_set_value</h3>

 The typedef <tt>&quot;hive_set_value&quot;</tt> is used in conjunction with the <tt>&quot;hivex_node_set_values&quot;</tt> call described below. 

 
struct hive_set_value {
    char *key;   /* key - a UTF-8 encoded ASCIIZ string */
    hive_type t; /* type of value field */
    size_t len;  /* length of value field in bytes */
    char *value; /* value field */
};
typedef struct hive_set_value hive_set_value;
 

 To set the default value for a node, you have to pass <tt>&quot;key = &quot;&quot;&quot;</tt>. 

 Note that the <tt>&quot;value&quot;</tt> field is just treated as a list of bytes, and is stored directly in the hive. The caller has to ensure correct encoding and endianness, for example converting dwords to little endian. 

 The correct type and encoding for values depends on the node and key in the registry, the version of Windows, and sometimes even changes between versions of Windows for the same key. We don't document it here. Often it's not documented at all.

<h2>FUNCTIONS</h2>

<h3>hivex_open</h3>

 
hive_h *hivex_open(const char *filename, int flags);
 

 Opens the hive named <tt>&quot;filename&quot;</tt> for reading. 

 Flags is an ORed list of the open flags (or <tt>0</tt> if you don't want to pass any flags). These flags are defined:
<dl>
<dt><font SIZE="-1">HIVEX_OPEN_VERBOSE</font>
<dd> Verbose messages.
<dt><font SIZE="-1">HIVEX_OPEN_DEBUG</font>
<dd> Very verbose messages, suitable for debugging problems in the library itself. 

 This is also selected if the <tt>&quot;HIVEX_DEBUG&quot;</tt> environment variable is set to 1.
<dt><font SIZE="-1">HIVEX_OPEN_WRITE</font>
<dd> Open the hive for writing. If omitted, the hive is read-only. 

 See ``<font SIZE="-1">WRITING TO HIVE FILES''</font> in <i><a HREF="/docs/linux/man/3-hivex/">hivex</a></i>(3).</dl>
 

 Returns a new hive handle. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_close</h3>

 
int hivex_close(hive_h *h);
 

 Close a hive handle and free all associated resources. 

 Note that any uncommitted writes are <i>not</i> committed by this call, but instead are lost. See ``<font SIZE="-1">WRITING TO HIVE FILES''</font> in <i><a HREF="/docs/linux/man/3-hivex/">hivex</a></i>(3). 

 Returns 0 on success. On error this returns -1 and sets errno. 

 This function frees the hive handle (even if it returns an error). The hive handle must not be used again after calling this function.

<h3>hivex_root</h3>

 <pre>
 hive_node_h hivex_root (hive_h *h);
</pre> 

 Return root node of the hive. All valid hives must contain a root node. 

 Returns a node handle. On error this returns 0 and sets errno.

<h3>hivex_last_modified</h3>

 <pre>
 int64_t hivex_last_modified (hive_h *h);
</pre> 

 Return the modification time from the header of the hive. 

 The returned value is a Windows filetime. To convert this to a Unix <tt>&quot;time_t&quot;</tt> see: &lt;<a rel="nofollow" HREF="http://stackoverflow.com/questions/6161776/convert-windows-filetime-to-second-in-unix-linux/6161842#6161842">http://stackoverflow.com/questions/6161776/convert-windows-filetime-to-second-in-unix-linux/6161842#6161842</a>&gt;

<h3>hivex_node_name</h3>

 
char *hivex_node_name(hive_h *h, hive_node_h node);
 

 Return the name of the node. 

 Note that the name of the root node is a dummy, such as <tt>&quot;$$$PROTO.HIV&quot;</tt> (other names are possible: it seems to depend on the tool or program that created the hive in the first place). You can only know the ``real'' name of the root node by knowing which registry file this hive originally comes from, which is knowledge that is outside the scope of this library. 

 The name is recoded to <font SIZE="-1">UTF-8</font> and may contain embedded <font SIZE="-1">NUL</font> characters. 

 Returns a string. The string must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_node_name_len</h3>

 <pre>
 size_t hivex_node_name_len (hive_h *h, hive_node_h node);
</pre> 

 Return the length of the node name as produced by <tt>&quot;hivex_node_name&quot;</tt>. 

 Returns a size. On error this returns 0 and sets errno.

<h3>hivex_node_timestamp</h3>

 <pre>
 int64_t hivex_node_timestamp (hive_h *h, hive_node_h node);
</pre> 

 Return the modification time of the node. 

 The returned value is a Windows filetime. To convert this to a Unix <tt>&quot;time_t&quot;</tt> see: &lt;<a rel="nofollow" HREF="http://stackoverflow.com/questions/6161776/convert-windows-filetime-to-second-in-unix-linux/6161842#6161842">http://stackoverflow.com/questions/6161776/convert-windows-filetime-to-second-in-unix-linux/6161842#6161842</a>&gt;

<h3>hivex_node_children</h3>

 <pre>
 hive_node_h *hivex_node_children (hive_h *h, hive_node_h node);
</pre> 

 Return an array of nodes which are the subkeys (children) of <tt>&quot;node&quot;</tt>. 

 Returns a 0-terminated array of nodes. The array must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_node_get_child</h3>

 
hive_node_h hivex_node_get_child(hive_h *h, hive_node_h node, const char *name);
 

 Return the child of node with the name <tt>&quot;name&quot;</tt>, if it exists. 

 The name is matched case insensitively. 

 Returns a node handle. If the node was not found, this returns 0 without setting errno. On error this returns 0 and sets errno.

<h3>hivex_node_parent</h3>

 <pre>
 hive_node_h hivex_node_parent (hive_h *h, hive_node_h node);
</pre> 

 Return the parent of <tt>&quot;node&quot;</tt>. 

 The parent pointer of the root node in registry files that we have examined seems to be invalid, and so this function will return an error if called on the root node. 

 Returns a node handle. On error this returns 0 and sets errno.

<h3>hivex_node_values</h3>

 <pre>
 hive_value_h *hivex_node_values (hive_h *h, hive_node_h node);
</pre> 

 Return the array of (key, value) pairs attached to this node. 

 Returns a 0-terminated array of values. The array must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_node_get_value</h3>

 
hive_value_h hivex_node_get_value(hive_h *h, hive_node_h node, const char *key);
 

 Return the value attached to this node which has the name <tt>&quot;key&quot;</tt>, if it exists. 

 The key name is matched case insensitively. 

 Note that to get the default key, you should pass the empty string <tt>&quot;&quot;</tt> here. The default key is often written <tt>&quot;@&quot;</tt>, but inside hives that has no meaning and won't give you the default key. 

 Returns a value handle. On error this returns 0 and sets errno.

<h3>hivex_value_key_len</h3>

 <pre>
 size_t hivex_value_key_len (hive_h *h, hive_value_h val);
</pre> 

 Return the length of the key (name) of a (key, value) pair as produced by <tt>&quot;hivex_value_key&quot;</tt>. The length can legitimately be 0, so errno is the necessary mechanism to check for errors. 

 In the context of Windows Registries, a zero-length name means that this value is the default key for this node in the tree. This is usually written as <tt>&quot;@&quot;</tt>. 

 The key is recoded to <font SIZE="-1">UTF-8</font> and may contain embedded <font SIZE="-1">NUL</font> characters. 

 Returns a size. On error this returns 0 and sets errno.

<h3>hivex_value_key</h3>

 
char *hivex_value_key(hive_h *h, hive_value_h val);
 

 Return the key (name) of a (key, value) pair. The name is reencoded as <font SIZE="-1">UTF-8</font> and returned as a string. 

 The string should be freed by the caller when it is no longer needed. 

 Note that this function can return a zero-length string. In the context of Windows Registries, this means that this value is the default key for this node in the tree. This is usually written as <tt>&quot;@&quot;</tt>. 

 Returns a string. The string must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_value_type</h3>

 
int hivex_value_type(hive_h *h, hive_value_h val, hive_type *t, size_t *len);
 

 Return the data length and data type of the value in this (key, value) pair. See also <tt>&quot;hivex_value_value&quot;</tt> which returns all this information, and the value itself. Also, <tt>&quot;hivex_value_*&quot;</tt> functions below which can be used to return the value in a more useful form when you know the type in advance. 

 Returns 0 on success. On error this returns -1 and sets errno.

<h3>hivex_node_struct_length</h3>

 <pre>
 size_t hivex_node_struct_length (hive_h *h, hive_node_h node);
</pre> 

 Return the length of the node data structure. 

 Returns a size. On error this returns 0 and sets errno.

<h3>hivex_value_struct_length</h3>

 <pre>
 size_t hivex_value_struct_length (hive_h *h, hive_value_h val);
</pre> 

 Return the length of the value data structure. 

 Returns a size. On error this returns 0 and sets errno.

<h3>hivex_value_data_cell_offset</h3>

 <pre>
 hive_value_h hivex_value_data_cell_offset (hive_h *h, hive_value_h val, size_t *len);
</pre> 

 Return the offset and length of the value's data cell. 

 The data cell is a registry structure that contains the length (a 4 byte, little endian integer) followed by the data. 

 If the length of the value is less than or equal to 4 bytes then the offset and length returned by this function is zero as the data is inlined in the value. 

 Returns 0 and sets errno on error. 

 Returns a value handle. On error this returns 0 and sets errno.

<h3>hivex_value_value</h3>

 
char *hivex_value_value(hive_h *h, hive_value_h val, hive_type *t, size_t *len);
 

 Return the value of this (key, value) pair. The value should be interpreted according to its type (see <tt>&quot;hive_type&quot;</tt>). 

 The value is returned as an array of bytes (of length <tt>&quot;len&quot;</tt>). The value must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_value_string</h3>

 
char *hivex_value_string(hive_h *h, hive_value_h val);
 

 If this value is a string, return the string reencoded as <font SIZE="-1">UTF-8 </font>(as a C string). This only works for values which have type <tt>&quot;hive_t_string&quot;</tt>, <tt>&quot;hive_t_expand_string&quot;</tt> or <tt>&quot;hive_t_link&quot;</tt>. 

 Returns a string. The string must be freed by the caller when it is no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_value_multiple_strings</h3>

 
char **hivex_value_multiple_strings(hive_h *h, hive_value_h val);
 

 If this value is a multiple-string, return the strings reencoded as <font SIZE="-1">UTF-8 </font>(in C, as a NULL-terminated array of C strings, in other language bindings, as a list of strings). This only works for values which have type <tt>&quot;hive_t_multiple_strings&quot;</tt>. 

 Returns a NULL-terminated array of C strings. The strings and the array must all be freed by the caller when they are no longer needed. On error this returns <font SIZE="-1">NULL</font> and sets errno.

<h3>hivex_value_dword</h3>

 <pre>
 int32_t hivex_value_dword (hive_h *h, hive_value_h val);
</pre> 

 If this value is a <font SIZE="-1">DWORD </font>(Windows int32), return it. This only works for values which have type <tt>&quot;hive_t_dword&quot;</tt> or <tt>&quot;hive_t_dword_be&quot;</tt>.

<h3>hivex_value_qword</h3>

 <pre>
 int64_t hivex_value_qword (hive_h *h, hive_value_h val);
</pre> 

 If this value is a <font SIZE="-1">QWORD </font>(Windows int64), return it. This only works for values which have type <tt>&quot;hive_t_qword&quot;</tt>.

<h3>hivex_commit</h3>

 
int hivex_commit(hive_h *h, const char *filename, int flags);
 

 Commit (write) any changes which have been made. 

 <tt>&quot;filename&quot;</tt> is the new file to write. If <tt>&quot;filename&quot;</tt> is null/undefined then we overwrite the original file (ie. the file name that was passed to <tt>&quot;hivex_open&quot;</tt>). 

 Note this does not close the hive handle. You can perform further operations on the hive after committing, including making more modifications. If you no longer wish to use the hive, then you should close the handle after committing. 

 The flags parameter is unused. Always pass 0. 

 Returns 0 on success. On error this returns -1 and sets errno.

<h3>hivex_node_add_child</h3>

 
hive_node_h hivex_node_add_child(hive_h *h, hive_node_h parent, const char *name);
 

 Add a new child node named <tt>&quot;name&quot;</tt> to the existing node <tt>&quot;parent&quot;</tt>. The new child initially has no subnodes and contains no keys or values. The sk-record (security descriptor) is inherited from the parent. 

 The parent must not have an existing child called <tt>&quot;name&quot;</tt>, so if you want to overwrite an existing child, call <tt>&quot;hivex_node_delete_child&quot;</tt> first. 

 Returns a node handle. On error this returns 0 and sets errno.

<h3>hivex_node_delete_child</h3>

 
int hivex_node_delete_child(hive_h *h, hive_node_h node);
 

 Delete the node <tt>&quot;node&quot;</tt>. All values at the node and all subnodes are deleted (recursively). The <tt>&quot;node&quot;</tt> handle and the handles of all subnodes become invalid. You cannot delete the root node. 

 Returns 0 on success. On error this returns -1 and sets errno.

<h3>hivex_node_set_values</h3>

 
int hivex_node_set_values(hive_h *h, hive_node_h node, size_t nr_values, const hive_set_value *values, int flags);
 

 This call can be used to set all the (key, value) pairs stored in <tt>&quot;node&quot;</tt>. 

 <tt>&quot;node&quot;</tt> is the node to modify. 

 The flags parameter is unused. Always pass 0. 

 <tt>&quot;values&quot;</tt> is an array of (key, value) pairs. There should be <tt>&quot;nr_values&quot;</tt> elements in this array. 

 Any existing values stored at the node are discarded, and their <tt>&quot;hive_value_h&quot;</tt> handles become invalid. Thus you can remove all values stored at <tt>&quot;node&quot;</tt> by passing <tt>&quot;nr_values = 0&quot;</tt>. 

 Returns 0 on success. On error this returns -1 and sets errno.

<h3>hivex_node_set_value</h3>

 
int hivex_node_set_value(hive_h *h, hive_node_h node, const hive_set_value *val, int flags);
 

 This call can be used to replace a single <tt>&quot;(key, value)&quot;</tt> pair stored in <tt>&quot;node&quot;</tt>. If the key does not already exist, then a new key is added. Key matching is case insensitive. 

 <tt>&quot;node&quot;</tt> is the node to modify. 

 The flags parameter is unused. Always pass 0. 

 <tt>&quot;value&quot;</tt> is a single (key, value) pair. 

 Existing <tt>&quot;hive_value_h&quot;</tt> handles become invalid. 

 Returns 0 on success. On error this returns -1 and sets errno.

<h2>WRITING TO HIVE FILES</h2>

 The hivex library supports making limited modifications to hive files. We have tried to implement this very conservatively in order to reduce the chance of corrupting your registry. However you should be careful and take back-ups, since Microsoft has never documented the hive format, and so it is possible there are nuances in the reverse-engineered format that we do not understand. 

 To be able to modify a hive, you must pass the <tt>&quot;HIVEX_OPEN_WRITE&quot;</tt> flag to <tt>&quot;hivex_open&quot;</tt>, otherwise any write operation will return with errno <tt>&quot;EROFS&quot;</tt>. 

 The write operations shown below do not modify the on-disk file immediately. You must call <tt>&quot;hivex_commit&quot;</tt> in order to write the changes to disk. If you call <tt>&quot;hivex_close&quot;</tt> without committing then any writes are discarded. 

 Hive files internally consist of a ``memory dump'' of binary blocks (like the C heap), and some of these blocks can be unused. The hivex library never reuses these unused blocks. Instead, to ensure robustness in the face of the partially understood on-disk format, hivex only allocates new blocks after the end of the file, and makes minimal modifications to existing structures in the file to point to these new blocks. This makes hivex slightly less disk-efficient than it could be, but disk is cheap, and registry modifications tend to be very small. 

 When deleting nodes, it is possible that this library may leave unreachable live blocks in the hive. This is because certain parts of the hive disk format such as security (sk) records and big data (db) records and classname fields are not well understood (and not documented at all) and we play it safe by not attempting to modify them. Apart from wasting a little bit of disk space, it is not thought that unreachable blocks are a problem.

<h3><font SIZE="-1">WRITE OPERATIONS WHICH ARE NOT SUPPORTED</font></h3>

<dl>
<dt>&bull;
<dd> Changing the root node.
<dt>&bull;
<dd> Creating a new hive file from scratch. This is impossible at present because not all fields in the header are understood. In the hivex source tree is a file called <tt>&quot;images/minimal&quot;</tt> which could be used as the basis for a new hive (but <i>caveat emptor</i>).
<dt>&bull;
<dd> Modifying or deleting single values at a node.
<dt>&bull;
<dd> Modifying security key (sk) records or classnames. Previously we did not understand these records. However now they are well-understood and we could add support if it was required (but nothing much really uses them).</dl>

<h2>VISITING ALL NODES</h2>

 The visitor pattern is useful if you want to visit all nodes in the tree or all nodes below a certain point in the tree. 

 First you set up your own <tt>&quot;struct hivex_visitor&quot;</tt> with your callback functions. 

 Each of these callback functions should return 0 on success or -1 on error. If any callback returns -1, then the entire visit terminates immediately. If you don't need a callback function at all, set the function pointer to <font SIZE="-1">NULL.</font> 

 
struct hivex_visitor {
    int (*node_start)(hive_h *, void *opaque, hive_node_h, const char *name);
    int (*node_end)(hive_h *, void *opaque, hive_node_h, const char *name);
    int (*value_string)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                        hive_type t, size_t len, const char *key, const char *str);
    int (*value_multiple_strings)(hive_h *, void *opaque, hive_node_h,
                                  hive_value_h, hive_type t, size_t len, const char *key, char **argv);
    int (*value_string_invalid_utf16)(hive_h *, void *opaque, hive_node_h,
                                      hive_value_h, hive_type t, size_t len, const char *key,
                                      const char *str);
    int (*value_dword)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                       hive_type t, size_t len, const char *key, int32_t);
    int (*value_qword)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                       hive_type t, size_t len, const char *key, int64_t);
    int (*value_binary)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                        hive_type t, size_t len, const char *key, const char *value);
    int (*value_none)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                      hive_type t, size_t len, const char *key, const char *value);
    int (*value_other)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                       hive_type t, size_t len, const char *key, const char *value);
    /* If value_any callback is not NULL, then the other value_*
     * callbacks are not used, and value_any is called on all values.
     */
    int (*value_any)(hive_h *, void *opaque, hive_node_h, hive_value_h,
                     hive_type t, size_t len, const char *key, const char *value);
};

<dl>
<dt>hivex_visit
<dd> 
int hivex_visit(hive_h *h, const struct hivex_visitor *visitor, size_t len, void *opaque, int flags);
 

 Visit all the nodes recursively in the hive <tt>&quot;h&quot;</tt>. 

 <tt>&quot;visitor&quot;</tt> should be a <tt>&quot;hivex_visitor&quot;</tt> structure with callback fields filled in as required (unwanted callbacks can be set to <font SIZE="-1">NULL</font>). <tt>&quot;len&quot;</tt> must be the length of the 'visitor' struct (you should pass <tt>&quot;sizeof (struct hivex_visitor)&quot;</tt> for this). 

 This returns 0 if the whole recursive visit was completed successfully. On error this returns -1. If one of the callback functions returned an error than we don't touch errno. If the error was generated internally then we set errno. 

 You can skip bad registry entries by setting <tt>&quot;flag&quot;</tt> to <tt>&quot;HIVEX_VISIT_SKIP_BAD&quot;</tt>. If this flag is not set, then a bad registry causes the function to return an error immediately. 

 This function is robust if the registry contains cycles or pointers which are invalid or outside the registry. It detects these cases and returns an error.
<dt>hivex_visit_node
<dd> <pre><code>
int hivex_visit_node(hive_h *h, hive_node_h node, const struct hivex_visitor *visitor, size_t len, void *opaque);
</code></pre> 

 Same as <tt>&quot;hivex_visit&quot;</tt> but instead of starting out at the root, this starts at <tt>&quot;node&quot;</tt>.</dl>

<h2>THE STRUCTURE OF THE WINDOWS REGISTRY</h2>

 Note: To understand the relationship between hives and the common Windows Registry keys (like <tt>&quot;HKEY_LOCAL_MACHINE&quot;</tt>) please see the Wikipedia page on the Windows Registry. 

 The Windows Registry is split across various binary files, each file being known as a ``hive''. This library only handles a single hive file at a time. 

 Hives are n-ary trees with a single root. Each node in the tree has a name. 

 Each node in the tree (including non-leaf nodes) may have an arbitrary list of (key, value) pairs attached to it. It may be the case that one of these pairs has an empty key. This is referred to as the default key for the node. 

 The (key, value) pairs are the place where the useful data is stored in the registry. The key is always a string (possibly the empty string for the default key). The value is a typed object (eg. string, int32, binary, etc.).

<h3><font SIZE="-1">RELATIONSHIP TO .REG FILES</font></h3>

 The hivex C library does not care about or deal with Windows .REG files. Instead we push this complexity up to the Perl <i><a HREF="/docs/linux/man/3-win--hivex/">Win::Hivex</a></i>(3) library and the Perl programs <i><a HREF="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1) and <i><a HREF="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1). Nevertheless it is useful to look at the relationship between the Registry and .REG files because they are so common. 

 A .REG file is a textual representation of the registry, or part of the registry. The actual registry hives that Windows uses are binary files. There are a number of Windows and Linux tools that let you generate .REG files, or merge .REG files back into the registry hives. Notable amongst them is Microsoft's <font SIZE="-1">REGEDIT</font> program (formerly known as <font SIZE="-1">REGEDT32</font>). 

 A typical .REG file will contain many sections looking like this: 

 <pre>
 [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Stack]
 &quot;@&quot;=&quot;Generic Stack&quot;
 &quot;TileInfo&quot;=&quot;prop:System.FileCount&quot;
 &quot;TilePath&quot;=<a HREF="//www.systutorials.com/docs/linux/man/2-str/">str</a>(2):&quot;%systemroot%\\system32&quot;
 &quot;ThumbnailCutoff&quot;=dword:00000000
 &quot;FriendlyTypeName&quot;=<a HREF="//www.systutorials.com/docs/linux/man/2-hex/">hex</a>(2):40,00,25,00,53,00,79,00,73,00,74,00,65,00,6d,00,52,00,6f,00,\
  6f,00,74,00,25,00,5c,00,53,00,79,00,73,00,74,00,65,00,6d,00,\
  33,00,32,00,5c,00,73,00,65,00,61,00,72,00,63,00,68,00,66,00,\
  6f,00,6c,00,64,00,65,00,72,00,2e,00,64,00,6c,00,6c,00,2c,00,\
  2d,00,39,00,30,00,32,00,38,00,00,00,d8
</pre> 

 Taking this one piece at a time: 

 <pre>
 [HKEY_LOCAL_MACHINE\SOFTWARE\Classes\Stack]
</pre> 

 This is the path to this node in the registry tree. The first part, <tt>&quot;HKEY_LOCAL_MACHINE\SOFTWARE&quot;</tt> means that this comes from a hive file called <tt>&quot;C:\WINDOWS\SYSTEM32\CONFIG\SOFTWARE&quot;</tt>. <tt>&quot;\Classes\Stack&quot;</tt> is the real path part, starting at the root node of the <tt>&quot;SOFTWARE&quot;</tt> hive. 

 Below the node name is a list of zero or more key-value pairs. Any interior or leaf node in the registry may have key-value pairs attached. 

 <pre>
 &quot;@&quot;=&quot;Generic Stack&quot;
</pre> 

 This is the ``default key''. In reality (ie. inside the binary hive) the key string is the empty string. In .REG files this is written as <tt>&quot;@&quot;</tt> but this has no meaning either in the hives themselves or in this library. The value is a string (type 1 - see <tt>&quot;enum hive_type&quot;</tt> above). 

 <pre>
 &quot;TileInfo&quot;=&quot;prop:System.FileCount&quot;
</pre> 

 This is a regular (key, value) pair, with the value being a type 1 string. Note that inside the binary file the string is likely to be <font SIZE="-1">UTF-16LE</font> encoded. This library converts to and from <font SIZE="-1">UTF-8</font> strings transparently in some cases. 

 <pre>
 &quot;TilePath&quot;=<a HREF="//www.systutorials.com/docs/linux/man/2-str/">str</a>(2):&quot;%systemroot%\\system32&quot;
</pre> 

 The value in this case has type 2 (expanded string) meaning that some %...% variables get expanded by Windows. (This library doesn't know or care about variable expansion). 

 <pre>
 &quot;ThumbnailCutoff&quot;=dword:00000000
</pre> 

 The value in this case is a dword (type 4). 

 <pre>
 &quot;FriendlyTypeName&quot;=<a HREF="//www.systutorials.com/docs/linux/man/2-hex/">hex</a>(2):40,00,....
</pre> 

 This value is an expanded string (type 2) represented in the .REG file as a series of hex bytes. In this case the string appears to be a <font SIZE="-1">UTF-16LE</font> string.

<h2>NOTE ON THE USE OF ERRNO</h2>

 Many functions in this library set errno to indicate errors. These are the values of errno you may encounter (this list is not exhaustive):
<dl>
<dt><font SIZE="-1">ENOTSUP</font>
<dd> Corrupt or unsupported Registry file format.
<dt><font SIZE="-1">HIVEX_NO_KEY</font>
<dd> Missing root key.
<dt><font SIZE="-1">EINVAL</font>
<dd> Passed an invalid argument to the function.
<dt><font SIZE="-1">EFAULT</font>
<dd> Followed a Registry pointer which goes outside the registry or outside a registry block.
<dt><font SIZE="-1">ELOOP</font>
<dd> Registry contains cycles.
<dt><font SIZE="-1">ERANGE</font>
<dd> Field in the registry out of range.
<dt><font SIZE="-1">EEXIST</font>
<dd> Registry key already exists.
<dt><font SIZE="-1">EROFS</font>
<dd> Tried to write to a registry which is not opened for writing.</dl>

<h2>ENVIRONMENT VARIABLES</h2>

<dl>
<dt><font SIZE="-1">HIVEX_DEBUG</font>
<dd> Setting HIVEX_DEBUG=1 will enable very verbose messages. This is useful for debugging problems with the library itself.</dl>

<h2>SEE ALSO</h2>

 <i><a HREF="/docs/linux/man/1-hivexget/">hivexget</a></i>(1), <i><a HREF="/docs/linux/man/1-hivexml/">hivexml</a></i>(1), <i><a HREF="/docs/linux/man/1-hivexsh/">hivexsh</a></i>(1), <i><a HREF="/docs/linux/man/1-hivexregedit/">hivexregedit</a></i>(1), <i><a HREF="/docs/linux/man/1-virt-win-reg/">virt-win-reg</a></i>(1), <i><a HREF="/docs/linux/man/3-win--hivex/">Win::Hivex</a></i>(3), <i><a HREF="/docs/linux/man/3-guestfs/">guestfs</a></i>(3), &lt;<a rel="nofollow" HREF="http://libguestfs.org/">http://libguestfs.org/</a>&gt;, <i><a HREF="/docs/linux/man/1-virt-cat/">virt-cat</a></i>(1), <i><a HREF="/docs/linux/man/1-virt-edit/">virt-edit</a></i>(1), &lt;<a rel="nofollow" HREF="http://en.wikipedia.org/wiki/Windows_Registry">http://en.wikipedia.org/wiki/Windows_Registry</a>&gt;.

<h2>AUTHORS</h2>

 Richard W.M. Jones (<tt>&quot;rjones at redhat dot com&quot;</tt>)

<h2>COPYRIGHT</h2>

 Copyright (C) 2009-2010 Red Hat Inc. 

 Derived from code by Petter Nordahl-Hagen under a compatible license: Copyright (C) 1997-2007 Petter Nordahl-Hagen. 

 Derived from code by Markus Stephany under a compatible license: Copyright (C) 2000-2004 Markus Stephany. 

 This library is free software; you can redistribute it and/or modify it under the terms of the <font SIZE="-1">GNU</font> Lesser General Public License as published by the Free Software Foundation; version 2.1 of the License only. 

 This library is distributed in the hope that it will be useful, but <font SIZE="-1">WITHOUT ANY WARRANTY</font>; without even the implied warranty of <font SIZE="-1">MERCHANTABILITY</font> or <font SIZE="-1">FITNESS FOR A PARTICULAR PURPOSE. </font> See the <font SIZE="-1">GNU</font> Lesser General Public License for more details. 

<h2>Index</h2>



<dt><a HREF="#lbBP">VISITING ALL NODES</a>
<dd>
<dt><a HREF="#lbBQ">THE STRUCTURE OF THE WINDOWS REGISTRY</a>
<dd>


<dt><a HREF="#lbBS">NOTE ON THE USE OF ERRNO</a>
<dd>
<dt><a HREF="#lbBT">ENVIRONMENT VARIABLES</a>
<dd>
<dt><a HREF="#lbBU">SEE ALSO</a>
<dd>
<dt><a HREF="#lbBV">AUTHORS</a>
<dd>
<dt><a HREF="#lbBW">COPYRIGHT</a>
<dd></dl>
