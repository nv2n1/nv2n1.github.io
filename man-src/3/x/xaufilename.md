---
title: "xaufilename(3)"
name: "xaufilename"
section: "3"
letter: "x"
url: "/docs/linux/man/3-xaufilename/"
description: "Xau library: XauFileName, XauReadAuth, XauLockAuth, XauUnlockAuth, XauWriteAuth, XauDisposeAuth, XauGetAuthByAddr, XauGetBestAuthByAddr – X authority database routines"
---

<p>Xau library: XauFileName, XauReadAuth, XauLockAuth, XauUnlockAuth, XauWriteAuth, XauDisposeAuth, XauGetAuthByAddr, XauGetBestAuthByAddr &#8211; X authority database routines </p>
<h2>Synopsis</h2>
<pre>#include &lt;X11/Xauth.h&gt;
typedef struct xauth {
 unsigned short family;
 unsigned short address_length;
 char *address;
 unsigned short number_length;
 char *number;
 unsigned short name_length;
 char *name;
 unsigned short data_length;
 char *data;
} Xauth;
<dl COMPACT><dt><dd>char *XauFileName (void);
<dt><dd>Xauth *XauReadAuth (FILE *<i>auth_file</i>);
<dt><dd>int XauWriteAuth (FILE *<i>auth_file</i>, Xauth *<i>auth</i>);
<dt><dd>Xauth *XauGetAuthByAddr (unsigned short <i>family</i>, unsigned short
<i>address_length</i>, const char *<i>address</i>, unsigned short
<i>number_length</i>, const char *<i>number</i>, unsigned short
<i>name_length</i>, const char *<i>name</i>);
<dt><dd>Xauth *XauGetBestAuthByAddr (unsigned short <i>family</i>, unsigned short
<i>address_length</i>, const char *<i>address</i>, unsigned short
<i>number_length</i>, const char *<i>number</i>, int <i>types_length</i>,
char **<i>types</i>, const int *<i>type_lengths</i>);
<dt><dd>int XauLockAuth (const char *<i>file_name</i>, int <i>retries</i>, int
<i>timeout</i>, long <i>dead</i>);
<dt><dd>int XauUnlockAuth (const char *<i>file_name</i>);
<dt><dd>int XauDisposeAuth (Xauth *<i>auth</i>);</pre>
</dl>
<h2>Description</h2>
<p><code>XauFileName</code> generates the default authorization file name by first checking the XAUTHORITY environment variable if set, else it returns $HOME/.Xauthority. This name is statically allocated and should not be freed. </p>
<p> <code>XauReadAuth</code> reads the next entry from <i>auth_file</i>. The entry is <code>not</code> statically allocated and should be freed by calling <i>XauDisposeAuth</i>. </p>
<p> <code>XauWriteAuth</code> writes an authorization entry to <i>auth_file</i>. It returns 1 on success, 0 on failure. </p>
<p> <code>XauGetAuthByAddr</code> searches for an entry which matches the given network address/display number pair. The entry is <code>not</code> statically allocated and should be freed by calling <i>XauDisposeAuth</i>. </p>
<p> <code>XauGetBestAuthByAddr</code> is similar to <code>XauGetAuthByAddr</code>, except that a list of acceptable authentication methods is specified. Xau will choose the file entry which matches the earliest entry in this list (e.g., the most secure authentication method). The <i>types</i> argument is an array of strings, one string for each authentication method. <i>types_length</i> specifies how many elements are in the <i>types</i> array. <i>types_lengths</i> is an array of integers representing the length of each string. </p>
<p> <code>XauLockAuth</code> does the work necessary to synchronously update an authorization file. First it makes two file names, one with &#8220;-c&#8221; appended to <i>file_name</i>, the other with &#8220;-l&#8221; appended. If the &#8220;-c&#8221; file already exists and is more than <i>dead</i> seconds old, <i>XauLockAuth</i> removes it and the associated &#8220;-l&#8221; file. To prevent possible synchronization troubles with NFS, a <i>dead</i> value of zero forces the files to be removed. <i>XauLockAuth</i> makes <i>retries</i> attempts to create and link the file names, pausing <i>timeout</i> seconds between each attempt. <i>XauLockAuth</i> returns a collection of values depending on the results:</p>
<dl COMPACT>
<dt>LOCK_ERROR</p>
<dd>A system error occurred, either a file_name which is too long, or an unexpected failure from a system call. errno may prove useful.</p>
<dt>LOCK_TIMEOUT</p>
<dd><i>retries</i> attempts failed</p>
<dt>LOCK_SUCCESS</p>
<dd>The lock succeeded.</dl>
<p> <code>XauUnlockAuth</code> undoes the work of <i>XauLockAuth</i> by unlinking both the &#8220;-c&#8221; and &#8220;-l&#8221; file names. </p>
<p> <code>XauDisposeAuth</code> frees storage allocated to hold an authorization entry.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-xauth/">xauth</a>(1), <a href="/docs/linux/man/1-xdm/">xdm</a>(1)</p>
<h2>Author</h2>
<p>Keith Packard, MIT X Consortium</p>
