---
title: "keyctl(2)"
name: "keyctl"
section: "2"
letter: "k"
url: "/docs/linux/man/2-keyctl/"
description: "keyctl – manipulate the kernel’s key management facility"
---

<h2 class="name">NAME</h2>
<p> keyctl &#8211; manipulate the kernel&#8217;s key management facility </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
#include &lt;sys/types.h&gt;
long keyctl(int operation, ...);
/* For direct call via syscall(2): */
#include &lt;asm/unistd.h&gt;
#include &lt;linux/keyctl.h&gt;
#include &lt;unistd.h&gt;
long syscall(__NR_keyctl, int operation, __kernel_ulong_t arg2,
             __kernel_ulong_t arg3, __kernel_ulong_t arg4,
             __kernel_ulong_t arg5);
</code></pre>
<p> No glibc wrapper is provided for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>keyctl</code>() allows user-space programs to perform key manipulation. </p>
<p> The operation performed by <code>keyctl</code>() is determined by the value of the <i>operation</i> argument. Each of these operations is wrapped by the <i>libkeyutils</i> library (provided by the <i>keyutils</i> package) into individual functions (noted below) to permit the compiler to check types. </p>
<p> The permitted values for <i>operation</i> are:</p>
<dl>
<dt><code>KEYCTL_GET_KEYRING_ID</code> (since Linux 2.6.10)</p>
<dd> Map a special key ID to a real key ID for this process.</p>
<dt>
<dd> This operation looks up the special key whose ID is provided in <i>arg2</i> (cast to <i>key_serial_t</i>). If the special key is found, the ID of the corresponding real key is returned as the function result. The following values may be specified in <i>arg2</i>:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>KEY_SPEC_THREAD_KEYRING</code></p>
<dd> This specifies the calling thread&#8217;s thread-specific keyring. See <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7).</p>
<dt><code>KEY_SPEC_PROCESS_KEYRING</code></p>
<dd> This specifies the caller&#8217;s process-specific keyring. See <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7).</p>
<dt><code>KEY_SPEC_SESSION_KEYRING</code></p>
<dd> This specifies the caller&#8217;s session-specific keyring. See <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7).</p>
<dt><code>KEY_SPEC_USER_KEYRING</code></p>
<dd> This specifies the caller&#8217;s UID-specific keyring. See <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7).</p>
<dt><code>KEY_SPEC_USER_SESSION_KEYRING</code></p>
<dd> This specifies the caller&#8217;s UID-session keyring. See <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7).</p>
<dt><code>KEY_SPEC_REQKEY_AUTH_KEY</code> (since Linux 2.6.16)</p>
<dd> This specifies the authorization key created by <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) and passed to the process it spawns to generate a key. This key is available only in a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program that was passed an authorization key by the kernel and ceases to be available once the requested key has been instantiated; see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2).</p>
<dt><code>KEY_SPEC_REQUESTOR_KEYRING</code> (since Linux 2.6.29)</p>
<dd> This specifies the key ID for the <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) destination keyring. This keyring is available only in a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program that was passed an authorization key by the kernel and ceases to be available once the requested key has been instantiated; see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2).</dl>
</dl>
<dt>
<dd> The behavior if the key specified in <i>arg2</i> does not exist depends on the value of <i>arg3</i> (cast to <i>int</i>). If <i>arg3</i> contains a nonzero value, then&#8212;if it is appropriate to do so (e.g., when looking up the user, user-session, or session key)&#8212;a new key is created and its real key ID returned as the function result. Otherwise, the operation fails with the error <code>ENOKEY</code>.</p>
<dt>
<dd> If a valid key ID is specified in <i>arg2</i>, and the key exists, then this operation simply returns the key ID. If the key does not exist, the call fails with error <code>ENOKEY</code>.</p>
<dt>
<dd> The caller must have <i>search</i> permission on a keyring in order for it to be found.</p>
<dt>
<dd> The arguments <i>arg4</i> and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_get_keyring_id/">keyctl_get_keyring_ID</a></code>(3).</p>
<dt><code>KEYCTL_JOIN_SESSION_KEYRING</code> (since Linux 2.6.10)</p>
<dd> Replace the session keyring this process subscribes to with a new session keyring.</p>
<dt>
<dd> If <i>arg2</i> is NULL, an anonymous keyring with the description &quot;_ses&quot; is created and the process is subscribed to that keyring as its session keyring, displacing the previous session keyring.</p>
<dt>
<dd> Otherwise, <i>arg2</i> (cast to <i>char&nbsp;*</i>) is treated as the description (name) of a keyring, and the behavior is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> If a keyring with a matching description exists, the process will attempt to subscribe to that keyring as its session keyring if possible; if that is not possible, an error is returned. In order to subscribe to the keyring, the caller must have <i>search</i> permission on the keyring.</p>
<dt>*</p>
<dd> If a keyring with a matching description does not exist, then a new keyring with the specified description is created, and the process is subscribed to that keyring as its session keyring.</dl>
</dl>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_join_session_keyring/">keyctl_join_session_keyring</a></code>(3).</p>
<dt><code>KEYCTL_UPDATE</code> (since Linux 2.6.10)</p>
<dd> Update a key&#8217;s data payload.</p>
<dt>
<dd> The <i>arg2</i> argument (cast to <i>key_serial_t</i>) specifies the ID of the key to be updated. The <i>arg3</i> argument (cast to <i>void&nbsp;*</i>) points to the new payload and <i>arg4</i> (cast to <i>size_t</i>) contains the new payload size in bytes.</p>
<dt>
<dd> The caller must have <i>write</i> permission on the key specified and the key type must support updating.</p>
<dt>
<dd> A negatively instantiated key (see the description of <code>KEYCTL_REJECT</code>) can be positively instantiated with this operation.</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_update/">keyctl_update</a></code>(3).</p>
<dt><code>KEYCTL_REVOKE</code> (since Linux 2.6.10)</p>
<dd> Revoke the key with the ID provided in <i>arg2</i> (cast to <i>key_serial_t</i>). The key is scheduled for garbage collection; it will no longer be findable, and will be unavailable for further operations. Further attempts to use the key will fail with the error <code>EKEYREVOKED</code>.</p>
<dt>
<dd> The caller must have <i>write</i> or <i>setattr</i> permission on the key.</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_revoke/">keyctl_revoke</a></code>(3).</p>
<dt><code>KEYCTL_CHOWN</code> (since Linux 2.6.10)</p>
<dd> Change the ownership (user and group ID) of a key.</p>
<dt>
<dd> The <i>arg2</i> argument (cast to <i>key_serial_t</i>) contains the key ID. The <i>arg3</i> argument (cast to <i>uid_t</i>) contains the new user ID (or -1 in case the user ID shouldn&#8217;t be changed). The <i>arg4</i> argument (cast to <i>gid_t</i>) contains the new group ID (or -1 in case the group ID shouldn&#8217;t be changed).</p>
<dt>
<dd> The key must grant the caller <i>setattr</i> permission.</p>
<dt>
<dd> For the UID to be changed, or for the GID to be changed to a group the caller is not a member of, the caller must have the <code>CAP_SYS_ADMIN</code> capability (see <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7)).</p>
<dt>
<dd> If the UID is to be changed, the new user must have sufficient quota to accept the key. The quota deduction will be removed from the old user to the new user should the UID be changed.</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_chown/">keyctl_chown</a></code>(3).</p>
<dt><code>KEYCTL_SETPERM</code> (since Linux 2.6.10)</p>
<dd> Change the permissions of the key with the ID provided in the <i>arg2</i> argument (cast to <i>key_serial_t</i>) to the permissions provided in the <i>arg3</i> argument (cast to <i>key_perm_t</i>).</p>
<dt>
<dd> If the caller doesn&#8217;t have the <code>CAP_SYS_ADMIN</code> capability, it can change permissions only for the keys it owns. (More precisely: the caller&#8217;s filesystem UID must match the UID of the key.)</p>
<dt>
<dd> The key must grant <i>setattr</i> permission to the caller <i>regardless</i> of the caller&#8217;s capabilities.</p>
<dt>
<dd> The permissions in <i>arg3</i> specify masks of available operations for each of the following user categories:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>possessor</i> (since Linux 2.6.14)</p>
<dd> This is the permission granted to a process that possesses the key (has it attached searchably to one of the process&#8217;s keyrings); see <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7).</p>
<dt><i>user</i></p>
<dd> This is the permission granted to a process whose filesystem UID matches the UID of the key.</p>
<dt><i>group</i></p>
<dd> This is the permission granted to a process whose filesystem GID or any of its supplementary GIDs matches the GID of the key.</p>
<dt><i>other</i></p>
<dd> This is the permission granted to other processes that do not match the <i>user</i> and <i>group</i> categories.</dl>
</dl>
<dt>
<dd> The <i>user</i>, <i>group</i>, and <i>other</i> categories are exclusive: if a process matches the <i>user</i> category, it will not receive permissions granted in the <i>group</i> category; if a process matches the <i>user</i> or <i>group</i> category, then it will not receive permissions granted in the <i>other</i> category.</p>
<dt>
<dd> The <i>possessor</i> category grants permissions that are cumulative with the grants from the <i>user</i>, <i>group</i>, or <i>other</i> category.</p>
<dt>
<dd> Each permission mask is eight bits in size, with only six bits currently used. The available permissions are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><i>view</i></p>
<dd> This permission allows reading attributes of a key.</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_DESCRIBE</code> operation.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_VIEW</code>, <code>KEY_USR_VIEW</code>, <code>KEY_GRP_VIEW</code>, and <code>KEY_OTH_VIEW</code>.</p>
<dt><i>read</i></p>
<dd> This permission allows reading a key&#8217;s payload.</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_READ</code> operation.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_READ</code>, <code>KEY_USR_READ</code>, <code>KEY_GRP_READ</code>, and <code>KEY_OTH_READ</code>.</p>
<dt><i>write</i></p>
<dd> This permission allows update or instantiation of a key&#8217;s payload. For a keyring, it allows keys to be linked and unlinked from the keyring,</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_UPDATE</code>, <code>KEYCTL_REVOKE</code>, <code>KEYCTL_CLEAR</code>, <code>KEYCTL_LINK</code>, and <code>KEYCTL_UNLINK</code> operations.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_WRITE</code>, <code>KEY_USR_WRITE</code>, <code>KEY_GRP_WRITE</code>, and <code>KEY_OTH_WRITE</code>.</p>
<dt><i>search</i></p>
<dd> This permission allows keyrings to be searched and keys to be found. Searches can recurse only into nested keyrings that have <i>search</i> permission set.</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_GET_KEYRING_ID</code>, <code>KEYCTL_JOIN_SESSION_KEYRING</code>, <code>KEYCTL_SEARCH</code>, and <code>KEYCTL_INVALIDATE</code> operations.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_SEARCH</code>, <code>KEY_USR_SEARCH</code>, <code>KEY_GRP_SEARCH</code>, and <code>KEY_OTH_SEARCH</code>.</p>
<dt><i>link</i></p>
<dd> This permission allows a key or keyring to be linked to.</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_LINK</code> and <code>KEYCTL_SESSION_TO_PARENT</code> operations.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_LINK</code>, <code>KEY_USR_LINK</code>, <code>KEY_GRP_LINK</code>, and <code>KEY_OTH_LINK</code>.</p>
<dt><i>setattr</i> (since Linux 2.6.15).</p>
<dd> This permission allows a key&#8217;s UID, GID, and permissions mask to be changed.</p>
<dt>
<dd> This permission is required for the <code>KEYCTL_REVOKE</code>, <code>KEYCTL_CHOWN</code>, and <code>KEYCTL_SETPERM</code> operations.</p>
<dt>
<dd> The permission bits for each category are <code>KEY_POS_SETATTR</code>, <code>KEY_USR_SETATTR</code>, <code>KEY_GRP_SETATTR</code>, and <code>KEY_OTH_SETATTR</code>.</dl>
</dl>
<dt>
<dd> As a convenience, the following macros are defined as masks for all of the permission bits in each of the user categories: <code>KEY_POS_ALL</code>, <code>KEY_USR_ALL</code>, <code>KEY_GRP_ALL</code>, and <code>KEY_OTH_ALL</code>.</p>
<dt>
<dd> The <i>arg4</i> and <i>arg5</i> arguments are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_setperm/">keyctl_setperm</a></code>(3).</p>
<dt><code>KEYCTL_DESCRIBE</code> (since Linux 2.6.10)</p>
<dd> Obtain a string describing the attributes of a specified key.</p>
<dt>
<dd> The ID of the key to be described is specified in <i>arg2</i> (cast to <i>key_serial_t</i>). The descriptive string is returned in the buffer pointed to by <i>arg3</i> (cast to <i>char&nbsp;*</i>); <i>arg4</i> (cast to <i>size_t</i>) specifies the size of that buffer in bytes.</p>
<dt>
<dd> The key must grant the caller <i>view</i> permission.</p>
<dt>
<dd> The returned string is null-terminated and contains the following information about the key:</p>
<dt>
<dd> <i>type</i>;<i>uid</i>;<i>gid</i>;<i>perm</i>;<i>description</i></p>
<dt>
<dd> In the above, <i>type</i> and <i>description</i> are strings, <i>uid</i> and <i>gid</i> are decimal strings, and <i>perm</i> is a hexadecimal permissions mask. The descriptive string is written with the following format:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s;%d;%d;%08x;%s</p>
<dt>
<dd> <code>Note: the intention is that the descriptive string should</code> <code>be extensible in future kernel versions.</code> In particular, the <i>description</i> field will not contain semicolons; it should be parsed by working backwards from the end of the string to find the last semicolon. This allows future semicolon-delimited fields to be inserted in the descriptive string in the future.</p>
<dt>
<dd> Writing to the buffer is attempted only when <i>arg3</i> is non-NULL and the specified buffer size is large enough to accept the descriptive string (including the terminating null byte). In order to determine whether the buffer size was too small, check to see if the return value of the operation is greater than <i>arg4</i>.</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_describe/">keyctl_describe</a></code>(3).</p>
<dt><code>KEYCTL_CLEAR</code></p>
<dd> Clear the contents of (i.e., unlink all keys from) a keyring.</p>
<dt>
<dd> The ID of the key (which must be of keyring type) is provided in <i>arg2</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> The caller must have <i>write</i> permission on the keyring.</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_clear/">keyctl_clear</a></code>(3).</p>
<dt><code>KEYCTL_LINK</code> (since Linux 2.6.10)</p>
<dd> Create a link from a keyring to a key.</p>
<dt>
<dd> The key to be linked is specified in <i>arg2</i> (cast to <i>key_serial_t</i>); the keyring is specified in <i>arg3</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> If a key with the same type and description is already linked in the keyring, then that key is displaced from the keyring.</p>
<dt>
<dd> Before creating the link, the kernel checks the nesting of the keyrings and returns appropriate errors if the link would produce a cycle or if the nesting of keyrings would be too deep (The limit on the nesting of keyrings is determined by the kernel constant <code>KEYRING_SEARCH_MAX_DEPTH</code>, defined with the value 6, and is necessary to prevent overflows on the kernel stack when recursively searching keyrings).</p>
<dt>
<dd> The caller must have <i>link</i> permission on the key being added and <i>write</i> permission on the keyring.</p>
<dt>
<dd> The arguments <i>arg4</i> and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_link/">keyctl_link</a></code>(3).</p>
<dt><code>KEYCTL_UNLINK</code> (since Linux 2.6.10)</p>
<dd> Unlink a key from a keyring.</p>
<dt>
<dd> The ID of the key to be unlinked is specified in <i>arg2</i> (cast to <i>key_serial_t</i>); the ID of the keyring from which it is to be unlinked is specified in <i>arg3</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> If the key is not currently linked into the keyring, an error results.</p>
<dt>
<dd> The caller must have <i>write</i> permission on the keyring from which the key is being removed.</p>
<dt>
<dd> If the last link to a key is removed, then that key will be scheduled for destruction.</p>
<dt>
<dd> The arguments <i>arg4</i> and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_unlink/">keyctl_unlink</a></code>(3).</p>
<dt><code>KEYCTL_SEARCH</code> (since Linux 2.6.10)</p>
<dd> Search for a key in a keyring tree, returning its ID and optionally linking it to a specified keyring.</p>
<dt>
<dd> The tree to be searched is specified by passing the ID of the head keyring in <i>arg2</i> (cast to <i>key_serial_t</i>). The search is performed breadth-first and recursively.</p>
<dt>
<dd> The <i>arg3</i> and <i>arg4</i> arguments specify the key to be searched for: <i>arg3</i> (cast as <i>char&nbsp;*</i>) contains the key type (a null-terminated character string up to 32 bytes in size, including the terminating null byte), and <i>arg4</i> (cast as <i>char&nbsp;*</i>) contains the description of the key (a null-terminated character string up to 4096 bytes in size, including the terminating null byte).</p>
<dt>
<dd> The source keyring must grant <i>search</i> permission to the caller. When performing the recursive search, only keyrings that grant the caller <i>search</i> permission will be searched. Only keys with for which the caller has <i>search</i> permission can be found.</p>
<dt>
<dd> If the key is found, its ID is returned as the function result.</p>
<dt>
<dd> If the key is found and <i>arg5</i> (cast to <i>key_serial_t</i>) is nonzero, then, subject to the same constraints and rules as <code>KEYCTL_LINK</code>, the key is linked into the keyring whose ID is specified in <i>arg5</i>. If the destination keyring specified in <i>arg5</i> already contains a link to a key that has the same type and description, then that link will be displaced by a link to the key found by this operation.</p>
<dt>
<dd> Instead of valid existing keyring IDs, the source (<i>arg2</i>) and destination (<i>arg5</i>) keyrings can be one of the special keyring IDs listed under <code>KEYCTL_GET_KEYRING_ID</code>.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_search/">keyctl_search</a></code>(3).</p>
<dt><code>KEYCTL_READ</code> (since Linux 2.6.10)</p>
<dd> Read the payload data of a key.</p>
<dt>
<dd> The ID of the key whose payload is to be read is specified in <i>arg2</i> (cast to <i>key_serial_t</i>). This can be the ID of an existing key, or any of the special key IDs listed for <code>KEYCTL_GET_KEYRING_ID</code>.</p>
<dt>
<dd> The payload is placed in the buffer pointed by <i>arg3</i> (cast to <i>char&nbsp;*</i>); the size of that buffer must be specified in <i>arg4</i> (cast to <i>size_t</i>).</p>
<dt>
<dd> The returned data will be processed for presentation according to the key type. For example, a keyring will return an array of <i>key_serial_t</i> entries representing the IDs of all the keys that are linked to it. The <i>user</i> key type will return its data as is. If a key type does not implement this function, the operation fails with the error <code>EOPNOTSUPP</code>.</p>
<dt>
<dd> If <i>arg3</i> is not NULL, as much of the payload data as will fit is copied into the buffer. On a successful return, the return value is always the total size of the payload data. To determine whether the buffer was of sufficient size, check to see that the return value is less than or equal to the value supplied in <i>arg4</i>.</p>
<dt>
<dd> The key must either grant the caller <i>read</i> permission, or grant the caller <i>search</i> permission when searched for from the process keyrings (i.e., the key is possessed).</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_read/">keyctl_read</a></code>(3).</p>
<dt><code>KEYCTL_INSTANTIATE</code> (since Linux 2.6.10)</p>
<dd> (Positively) instantiate an uninstantiated key with a specified payload.</p>
<dt>
<dd> The ID of the key to be instantiated is provided in <i>arg2</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> The key payload is specified in the buffer pointed to by <i>arg3</i> (cast to <i>void&nbsp;*);</i> the size of that buffer is specified in <i>arg4</i> (cast to <i>size_t</i>).</p>
<dt>
<dd> The payload may be a NULL pointer and the buffer size may be 0 if this is supported by the key type (e.g., it is a keyring).</p>
<dt>
<dd> The operation may be fail if the payload data is in the wrong format or is otherwise invalid.</p>
<dt>
<dd> If <i>arg5</i> (cast to <i>key_serial_t</i>) is nonzero, then, subject to the same constraints and rules as <code>KEYCTL_LINK</code>, the instantiated key is linked into the keyring whose ID specified in <i>arg5</i>.</p>
<dt>
<dd> The caller must have the appropriate authorization key, and once the uninstantiated key has been instantiated, the authorization key is revoked. In other words, this operation is available only from a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program. See <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) for an explanation of uninstantiated keys and key instantiation.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_instantiate/">keyctl_instantiate</a></code>(3).</p>
<dt><code>KEYCTL_NEGATE</code> (since Linux 2.6.10)</p>
<dd> Negatively instantiate an uninstantiated key.</p>
<dt>
<dd> This operation is equivalent to the call:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;keyctl(KEYCTL_REJECT, arg2, arg3, ENOKEY, arg4);</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_negate/">keyctl_negate</a></code>(3).</p>
<dt><code>KEYCTL_SET_REQKEY_KEYRING</code> (since Linux 2.6.13)</p>
<dd> Set the default keyring to which implicitly requested keys will be linked for this thread, and return the previous setting. Implicit key requests are those made by internal kernel components, such as can occur when, for example, opening files on an AFS or NFS filesystem. Setting the default keyring also has an effect when requesting a key from user space; see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) for details.</p>
<dt>
<dd> The <i>arg2</i> argument (cast to <i>int</i>) should contain one of the following values, to specify the new default keyring:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>KEY_REQKEY_DEFL_NO_CHANGE</code></p>
<dd> Don&#8217;t change the default keyring. This can be used to discover the current default keyring (without changing it).</p>
<dt><code>KEY_REQKEY_DEFL_DEFAULT</code></p>
<dd> This selects the default behaviour, which is to use the thread-specific keyring if there is one, otherwise the process-specific keyring if there is one, otherwise the session keyring if there is one, otherwise the UID-specific session keyring, otherwise the user-specific keyring.</p>
<dt><code>KEY_REQKEY_DEFL_THREAD_KEYRING</code></p>
<dd> Use the thread-specific keyring (<code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7)) as the new default keyring.</p>
<dt><code>KEY_REQKEY_DEFL_PROCESS_KEYRING</code></p>
<dd> Use the process-specific keyring (<code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7)) as the new default keyring.</p>
<dt><code>KEY_REQKEY_DEFL_SESSION_KEYRING</code></p>
<dd> Use the session-specific keyring (<code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7)) as the new default keyring.</p>
<dt><code>KEY_REQKEY_DEFL_USER_KEYRING</code></p>
<dd> Use the UID-specific keyring (<code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7)) as the new default keyring.</p>
<dt><code>KEY_REQKEY_DEFL_USER_SESSION_KEYRING</code></p>
<dd> Use the UID-specific session keyring (<code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)) as the new default keyring.</p>
<dt><code>KEY_REQKEY_DEFL_REQUESTOR_KEYRING</code> (since Linux 2.6.29)</p>
<dd> Use the requestor keyring.</dl>
</dl>
<dt>
<dd> All other values are invalid.</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> The setting controlled by this operation is inherited by the child of <code><a href="/docs/linux/man/2-fork/">fork</a></code>(2) and preserved across <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2).</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_set_reqkey_keyring/">keyctl_set_reqkey_keyring</a></code>(3).</p>
<dt><code>KEYCTL_SET_TIMEOUT</code> (since Linux 2.6.16)</p>
<dd> Set a timeout on a key.</p>
<dt>
<dd> The ID of the key is specified in <i>arg2</i> (cast to <i>key_serial_t</i>). The timeout value, in seconds from the current time, is specified in <i>arg3</i> (cast to <i>unsigned int</i>). The timeout is measured against the realtime clock.</p>
<dt>
<dd> Specifying the timeout value as 0 clears any existing timeout on the key.</p>
<dt>
<dd> The <i>/proc/keys</i> file displays the remaining time until each key will expire. (This is the only method of discovering the timeout on a key.)</p>
<dt>
<dd> The caller must either have the <i>setattr</i> permission on the key or hold an instantiation authorization token for the key (see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2)).</p>
<dt>
<dd> The key and any links to the key will be automatically garbage collected after the timeout expires. Subsequent attempts to access the key will then fail with the error <code>EKEYEXPIRED</code>.</p>
<dt>
<dd> This operation cannot be used to set timeouts on revoked, expired, or negatively instantiated keys.</p>
<dt>
<dd> The arguments <i>arg4</i> and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_set_timeout/">keyctl_set_timeout</a></code>(3).</p>
<dt><code>KEYCTL_ASSUME_AUTHORITY</code> (since Linux 2.6.16)</p>
<dd> Assume (or divest) the authority for the calling thread to instantiate a key.</p>
<dt>
<dd> The <i>arg2</i> argument (cast to <i>key_serial_t</i>) specifies either a nonzero key ID to assume authority, or the value 0 to divest authority.</p>
<dt>
<dd> If <i>arg2</i> is nonzero, then it specifies the ID of an uninstantiated key for which authority is to be assumed. That key can then be instantiated using one of <code>KEYCTL_INSTANTIATE</code>, <code>KEYCTL_INSTANTIATE_IOV</code>, <code>KEYCTL_REJECT</code>, or <code>KEYCTL_NEGATE</code>. Once the key has been instantiated, the thread is automatically divested of authority to instantiate the key.</p>
<dt>
<dd> Authority over a key can be assumed only if the calling thread has present in its keyrings the authorization key that is associated with the specified key. (In other words, the <code>KEYCTL_ASSUME_AUTHORITY</code> operation is available only from a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program; see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) for an explanation of how this operation is used.) The caller must have <i>search</i> permission on the authorization key.</p>
<dt>
<dd> If the specified key has a matching authorization key, then the ID of that key is returned. The authorization key can be read (<code>KEYCTL_READ</code>) to obtain the callout information passed to <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2).</p>
<dt>
<dd> If the ID given in <i>arg2</i> is 0, then the currently assumed authority is cleared (divested), and the value 0 is returned.</p>
<dt>
<dd> The <code>KEYCTL_ASSUME_AUTHORITY</code> mechanism allows a program such as <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) to assume the necessary authority to instantiate a new uninstantiated key that was created as a consequence of a call to <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2). For further information, see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) and the kernel source file <i>Documentation/security/keys-request-key.txt</i>.</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_assume_authority/">keyctl_assume_authority</a></code>(3).</p>
<dt><code>KEYCTL_GET_SECURITY</code> (since Linux 2.6.26)</p>
<dd> Get the LSM (Linux Security Module) security label of the specified key.</p>
<dt>
<dd> The ID of the key whose security label is to be fetched is specified in <i>arg2</i> (cast to <i>key_serial_t</i>). The security label (terminated by a null byte) will be placed in the buffer pointed to by <i>arg3</i> argument (cast to <i>char&nbsp;*</i>); the size of the buffer must be provided in <i>arg4</i> (cast to <i>size_t</i>).</p>
<dt>
<dd> If <i>arg3</i> is specified as NULL or the buffer size specified in <i>arg4</i> is too small, the full size of the security label string (including the terminating null byte) is returned as the function result, and nothing is copied to the buffer.</p>
<dt>
<dd> The caller must have <i>view</i> permission on the specified key.</p>
<dt>
<dd> The returned security label string will be rendered in a form appropriate to the LSM in force. For example, with SELinux, it may look like:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023</p>
<dt>
<dd> If no LSM is currently in force, then an empty string is placed in the buffer.</p>
<dt>
<dd> The <i>arg5</i> argument is ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the functions <code><a href="/docs/linux/man/3-keyctl_get_security/">keyctl_get_security</a></code>(3) and <code><a href="/docs/linux/man/3-keyctl_get_security_alloc/">keyctl_get_security_alloc</a></code>(3).</p>
<dt><code>KEYCTL_SESSION_TO_PARENT</code> (since Linux 2.6.32)</p>
<dd> Replace the session keyring to which the <i>parent</i> of the calling process subscribes with the session keyring of the calling process.</p>
<dt>
<dd> The keyring will be replaced in the parent process at the point where the parent next transitions from kernel space to user space.</p>
<dt>
<dd> The keyring must exist and must grant the caller <i>link</i> permission. The parent process must be single-threaded and have the same effective ownership as this process and must not be set-user-ID or set-group-ID. The UID of the parent process&#8217;s existing session keyring (f it has one), as well as the UID of the caller&#8217;s session keyring much match the caller&#8217;s effective UID.</p>
<dt>
<dd> The fact that it is the parent process that is affected by this operation allows a program such as the shell to start a child process that uses this operation to change the shell&#8217;s session keyring. (This is what the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) <code>new_session</code> command does.)</p>
<dt>
<dd> The arguments <i>arg2</i>, <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_session_to_parent/">keyctl_session_to_parent</a></code>(3).</p>
<dt><code>KEYCTL_REJECT</code> (since Linux 2.6.39)</p>
<dd> Mark a key as negatively instantiated and set an expiration timer on the key. This operation provides a superset of the functionality of the earlier <code>KEYCTL_NEGATE</code> operation.</p>
<dt>
<dd> The ID of the key that is to be negatively instantiated is specified in <i>arg2</i> (cast to <i>key_serial_t</i>). The <i>arg3</i> (cast to <i>unsigned int</i>) argument specifies the lifetime of the key, in seconds. The <i>arg4</i> argument (cast to <i>unsigned int</i>) specifies the error to be returned when a search hits this key; typically, this is one of <code>EKEYREJECTED</code>, <code>EKEYREVOKED</code>, or <code>EKEYEXPIRED</code>.</p>
<dt>
<dd> If <i>arg5</i> (cast to <i>key_serial_t</i>) is nonzero, then, subject to the same constraints and rules as <code>KEYCTL_LINK</code>, the negatively instantiated key is linked into the keyring whose ID is specified in <i>arg5</i>.</p>
<dt>
<dd> The caller must have the appropriate authorization key. In other words, this operation is available only from a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program. See <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2).</p>
<dt>
<dd> The caller must have the appropriate authorization key, and once the uninstantiated key has been instantiated, the authorization key is revoked. In other words, this operation is available only from a <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8)-style program. See <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) for an explanation of uninstantiated keys and key instantiation.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_reject/">keyctl_reject</a></code>(3).</p>
<dt><code>KEYCTL_INSTANTIATE_IOV</code> (since Linux 2.6.39)</p>
<dd> Instantiate an uninstantiated key with a payload specified via a vector of buffers.</p>
<dt>
<dd> This operation is the same as <code>KEYCTL_INSTANTIATE</code>, but the payload data is specified as an array of <i>iovec</i> structures:</p>
<dt>
<dd> struct iovec {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;void&nbsp;<wbr>&nbsp;*iov_base;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Starting address of buffer&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;size_t iov_len;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of buffer&nbsp;(in bytes)&nbsp;*/ };</p>
<dt>
<dd> The pointer to the payload vector is specified in <i>arg3</i> (cast as <i>const struct iovec&nbsp;*</i>). The number of items in the vector is specified in <i>arg4</i> (cast as <i>unsigned int</i>).</p>
<dt>
<dd> The <i>arg2</i> (key ID) and <i>arg5</i> (keyring ID) are interpreted as for <code>KEYCTL_INSTANTIATE</code>.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_instantiate_iov/">keyctl_instantiate_iov</a></code>(3).</p>
<dt><code>KEYCTL_INVALIDATE</code> (since Linux 3.5)</p>
<dd> Mark a key as invalid.</p>
<dt>
<dd> The ID of the key to be invalidated is specified in <i>arg2</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> To invalidate a key, the caller must have <i>search</i> permission on the key.</p>
<dt>
<dd> This operation marks the key as invalid and schedules immediate garbage collection. The garbage collector removes the invalidated key from all keyrings and deletes the key when its reference count reaches zero. After this operation, the key will be ignored by all searches, even if it is not yet deleted.</p>
<dt>
<dd> Keys that are marked invalid become invisible to normal key operations immediately, though they are still visible in <i>/proc/keys</i> (marked with an &#8216;i&#8217; flag) until they are actually removed.</p>
<dt>
<dd> The arguments <i>arg3</i>, <i>arg4</i>, and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_invalidate/">keyctl_invalidate</a></code>(3).</p>
<dt><code>KEYCTL_GET_PERSISTENT</code> (since Linux 3.13)</p>
<dd> Get the persistent keyring (<code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7)) for a specified user and link it to a specified keyring.</p>
<dt>
<dd> The user ID is specified in <i>arg2</i> (cast to <i>uid_t</i>). If the value -1 is specified, the caller&#8217;s real user ID is used. The ID of the destination keyring is specified in <i>arg3</i> (cast to <i>key_serial_t</i>).</p>
<dt>
<dd> The caller must have the <code>CAP_SETUID</code> capability in its user namespace in order to fetch the persistent keyring for a user ID that does not match either the real or effective user ID of the caller.</p>
<dt>
<dd> If the call is successful, a link to the persistent keyring is added to the keyring whose ID was specified in <i>arg3</i>.</p>
<dt>
<dd> The caller must have <i>write</i> permission on the keyring.</p>
<dt>
<dd> The persistent keyring will be created by the kernel if it does not yet exist.</p>
<dt>
<dd> Each time the <code>KEYCTL_GET_PERSISTENT</code> operation is performed, the persistent keyring will have its expiration timeout reset to the value in:</p>
<dt>
<dd> /proc/sys/kernel/keys/persistent_keyring_expiry</p>
<dt>
<dd> Should the timeout be reached, the persistent keyring will be removed and everything it pins can then be garbage collected.</p>
<dt>
<dd> Persistent keyrings were added to Linux in kernel version 3.13.</p>
<dt>
<dd> The arguments <i>arg4</i> and <i>arg5</i> are ignored.</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> via the function <code><a href="/docs/linux/man/3-keyctl_get_persistent/">keyctl_get_persistent</a></code>(3).</p>
<dt><code>KEYCTL_DH_COMPUTE</code> (since Linux 4.7)</p>
<dd> Compute a Diffie-Hellman shared secret or public key, optionally applying key derivation function (KDF) to the result.</p>
<dt>
<dd> The <i>arg2</i> argument is a pointer to a set of parameters containing serial numbers for three <i>&quot;user&quot;</i> keys used in the Diffie-Hellman calculation, packaged in a structure of the following form:</p>
<dt>
<dd> struct keyctl_dh_params {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t private;&nbsp;/*&nbsp;The local private key&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t prime;&nbsp;/*&nbsp;The prime, known to both parties&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t base;&nbsp;<wbr>&nbsp;/*&nbsp;The base integer: either a shared<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;generator or the remote public key&nbsp;*/ };</p>
<dt>
<dd> Each of the three keys specified in this structure must grant the caller <i>read</i> permission. The payloads of these keys are used to calculate the Diffie-Hellman result as:</p>
<dt>
<dd>
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;base ha private mod prime</p>
<dt>
<dd> If the base is the shared generator, the result is the local public key. If the base is the remote public key, the result is the shared secret.</p>
<dt>
<dd> The <i>arg3</i> argument (cast to <i>char&nbsp;*</i>) points to a buffer where the result of the calculation is placed. The size of that buffer is specified in <i>arg4</i> (cast to <i>size_t</i>).</p>
<dt>
<dd> The buffer must be large enough to accommodate the output data, otherwise an error is returned. If <i>arg4</i> is specified zero, in which case the buffer is not used and the operation returns the minimum required buffer size (i.e., the length of the prime).</p>
<dt>
<dd> Diffie-Hellman computations can be performed in user space, but require a multiple-precision integer (MPI) library. Moving the implementation into the kernel gives access to the kernel MPI implementation, and allows access to secure or acceleration hardware.</p>
<dt>
<dd> Adding support for DH computation to the <code>keyctl</code>() system call was considered a good fit due to the DH algorithm&#8217;s use for deriving shared keys; it also allows the type of the key to determine which DH implementation (software or hardware) is appropriate.</p>
<dt>
<dd> If the <i>arg5</i> argument is <code>NULL</code>, then the DH result itself is returned. Otherwise (since Linux 4.12), it is a pointer to a structure which specifies parameters of the KDF operation to be applied:</p>
<dt>
<dd> struct keyctl_kdf_params {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*hashname;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Hash algorithm name&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*otherinfo;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;SP800-56A OtherInfo&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32 otherinfolen;&nbsp;/*&nbsp;Length of otherinfo data&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;__u32&nbsp;__spare[8];&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Reserved&nbsp;*/ };</p>
<dt>
<dd> The <i>hashname</i> field is a null-terminated string which specifies a hash name (available in the kernel&#8217;s crypto API; the list of the hashes available is rather tricky to observe; please refer to the &quot;Kernel Crypto API Architecture&quot; documentation for the information regarding how hash names are constructed and your kernel&#8217;s source and configuration regarding what ciphers and templates with type <code>CRYPTO_ALG_TYPE_SHASH</code> are available) to be applied to DH result in KDF operation.</p>
<dt>
<dd> The <i>otherinfo</i> field is an <i>OtherInfo</i> data as described in SP800-56A section 5.8.1.2 and is algorithm-specific. This data is concatenated with the result of DH operation and is provided as an input to the KDF operation. Its size is provided in the <i>otherinfolen</i> field and is limited by <code>KEYCTL_KDF_MAX_OI_LEN</code> constant that defined in <i>security/keys/internal.h</i> to a value of 64.</p>
<dt>
<dd> The <code>__spare</code> field is currently unused. It was ignored until Linux 4.13 (but still should be user-addressable since it is copied to the kernel), and should contain zeros since Linux 4.13.</p>
<dt>
<dd> The KDF implementation complies with SP800-56A as well as with SP800-108 (the counter KDF).</p>
<dt>
<dd> This operation is exposed by <i>libkeyutils</i> (from version 1.5.10 onwards) via the functions <code><a href="/docs/linux/man/3-keyctl_dh_compute/">keyctl_dh_compute</a></code>(3) and <code><a href="/docs/linux/man/3-keyctl_dh_compute_alloc/">keyctl_dh_compute_alloc</a></code>(3).</p>
<dt><code>KEYCTL_RESTRICT_KEYRING</code> (since Linux 4.12)</p>
<dd> Apply a key-linking restriction to the keyring with the ID provided in <i>arg2</i> (cast to <i>key_serial_t</i>). The caller must have <i>setattr</i> permission on the key. If <i>arg3</i> is NULL, any attempt to add a key to the keyring is blocked; otherwise it contains a pointer to a string with a key type name and <i>arg4</i> contains a pointer to string that describes the type-specific restriction. As of Linux 4.12, only the type &quot;asymmetric&quot; has restrictions defined:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>builtin_trusted</code></p>
<dd> Allows only keys that are signed by a key linked to the built-in keyring (&quot;.builtin_trusted_keys&quot;).</p>
<dt><code>builtin_and_secondary_trusted</code></p>
<dd> Allows only keys that are signed by a key linked to the secondary keyring (&quot;.secondary_trusted_keys&quot;) or, by extension, a key in a built-in keyring, as the latter is linked to the former.</p>
<dt><code>key_or_keyring:</code><i>key</i></p>
<dd> <code>key_or_keyring:</code><i>key</i><code>:chain</code> If <i>key</i> specifies the ID of a key of type &quot;asymmetric&quot;, then only keys that are signed by this key are allowed.</p>
<dt>
<dd> If <i>key</i> specifies the ID of a keyring, then only keys that are signed by a key linked to this keyring are allowed.</p>
<dt>
<dd> If &quot;:chain&quot; is specified, keys that are signed by a keys linked to the destination keyring (that is, the keyring with the ID specified in the <i>arg2</i> argument) are also allowed.</dl>
</dl>
<dt>
<dd> Note that a restriction can be configured only once for the specified keyring; once a restriction is set, it can&#8217;t be overridden.</p>
<dt>
<dd> The argument <i>arg5</i> is ignored.</dl>
<h2>RETURN VALUE</h2>
<p> For a successful call, the return value depends on the operation:</p>
<dl>
<dt><code>KEYCTL_GET_KEYRING_ID</code></p>
<dd> The ID of the requested keyring.</p>
<dt><code>KEYCTL_JOIN_SESSION_KEYRING</code></p>
<dd> The ID of the joined session keyring.</p>
<dt><code>KEYCTL_DESCRIBE</code></p>
<dd> The size of the description (including the terminating null byte), irrespective of the provided buffer size.</p>
<dt><code>KEYCTL_SEARCH</code></p>
<dd> The ID of the key that was found.</p>
<dt><code>KEYCTL_READ</code></p>
<dd> The amount of data that is available in the key, irrespective of the provided buffer size.</p>
<dt><code>KEYCTL_SET_REQKEY_KEYRING</code></p>
<dd> The ID of the previous default keyring to which implicitly requested keys were linked (one of <code>KEY_REQKEY_DEFL_USER_*</code>).</p>
<dt><code>KEYCTL_ASSUME_AUTHORITY</code></p>
<dd> Either 0, if the ID given was 0, or the ID of the authorization key matching the specified key, if a nonzero key ID was provided.</p>
<dt><code>KEYCTL_GET_SECURITY</code></p>
<dd> The size of the LSM security label string (including the terminating null byte), irrespective of the provided buffer size.</p>
<dt><code>KEYCTL_GET_PERSISTENT</code></p>
<dd> The ID of the persistent keyring.</p>
<dt><code>KEYCTL_DH_COMPUTE</code></p>
<dd> The number of bytes copied to the buffer, or, if <i>arg4</i> is 0, the required buffer size.</p>
<dt>All other operations</p>
<dd> Zero.</dl>
<p> On error, -1 is returned, and <i>errno</i> is set appropriately to indicate the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The requested operation wasn&#8217;t permitted.</p>
<dt><code>EAGAIN</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and there was an error during crypto module initialization.</p>
<dt><code>EDEADLK</code></p>
<dd> <i>operation</i> was <code>KEYCTL_LINK</code> and the requested link would result in a cycle.</p>
<dt><code>EDEADLK</code></p>
<dd> <i>operation</i> was <code>KEYCTL_RESTRICT_KEYRING</code> and the requested keyring restriction would result in a cycle.</p>
<dt><code>EDQUOT</code></p>
<dd> The key quota for the caller&#8217;s user would be exceeded by creating a key or linking it to the keyring.</p>
<dt><code>EEXIST</code></p>
<dd> <i>operation</i> was <code>KEYCTL_RESTRICT_KEYRING</code> and keyring provided in <i>arg2</i> argument already has a restriction set.</p>
<dt><code>EFAULT</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and one of the following has failed:</p>
<dl>
<dt>
<dd>
<dl>
<dt>&bull;</p>
<dd> copying of the <i>struct keyctl_dh_params</i>, provided in the <i>arg2</i> argument, from user space;</p>
<dt>&bull;</p>
<dd> copying of the <i>struct keyctl_kdf_params</i>, provided in the non-NULL <i>arg5</i> argument, from user space (in case kernel supports performing KDF operation on DH operation result);</p>
<dt>&bull;</p>
<dd> copying of data pointed by the <i>hashname</i> field of the <i>struct keyctl_kdf_params</i> from user space;</p>
<dt>&bull;</p>
<dd> copying of data pointed by the <i>otherinfo</i> field of the <i>struct keyctl_kdf_params</i> from user space if the <i>otherinfolen</i> field was nonzero;</p>
<dt>&bull;</p>
<dd> copying of the result to user space.</dl>
</dl>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_SETPERM</code> and an invalid permission bit was specified in <i>arg3</i>.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_SEARCH</code> and the size of the description in <i>arg4</i> (including the terminating null byte) exceeded 4096 bytes. size of the string (including the terminating null byte) specified in <i>arg3</i> (the key type) or <i>arg4</i> (the key description) exceeded the limit (32 bytes and 4096 bytes respectively).</p>
<dt><code>EINVAL</code> (Linux kernels before 4.12)</p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code>, argument <i>arg5</i> was non-NULL.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> And the digest size of the hashing algorithm supplied is zero.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the buffer size provided is not enough to hold the result. Provide 0 as a buffer size in order to obtain the minimum buffer size.</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the hash name provided in the <i>hashname</i> field of the <i>struct keyctl_kdf_params</i> pointed by <i>arg5</i> argument is too big (the limit is implementation-specific and varies between kernel versions, but it is deemed big enough for all valid algorithm names).</p>
<dt><code>EINVAL</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the <i>__spare</i> field of the <i>struct keyctl_kdf_params</i> provided in the <i>arg5</i> argument contains nonzero values.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> An expired key was found or specified.</p>
<dt><code>EKEYREJECTED</code></p>
<dd> A rejected key was found or specified.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> A revoked key was found or specified.</p>
<dt><code>ELOOP</code></p>
<dd> <i>operation</i> was <code>KEYCTL_LINK</code> and the requested link would cause the maximum nesting depth for keyrings to be exceeded.</p>
<dt><code>EMSGSIZE</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the buffer length exceeds <code>KEYCTL_KDF_MAX_OUTPUT_LEN</code> (which is 1024 currently) or the <i>otherinfolen</i> field of the <i>struct keyctl_kdf_parms</i> passed in <i>arg5</i> exceeds <code>KEYCTL_KDF_MAX_OI_LEN</code> (which is 64 currently).</p>
<dt><code>ENFILE</code> (Linux kernels before 3.13)</p>
<dd> <i>operation</i> was <code>KEYCTL_LINK</code> and the keyring is full. (Before Linux 3.13, the available space for storing keyring links was limited to a single page of memory; since Linux 3.13, there is no fixed limit.)</p>
<dt><code>ENOENT</code></p>
<dd> <i>operation</i> was <code>KEYCTL_UNLINK</code> and the key to be unlinked isn&#8217;t linked to the keyring.</p>
<dt><code>ENOENT</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the hashing algorithm specified in the <i>hashname</i> field of the <i>struct keyctl_kdf_params</i> pointed by <i>arg5</i> argument hasn&#8217;t been found.</p>
<dt><code>ENOENT</code></p>
<dd> <i>operation</i> was <code>KEYCTL_RESTRICT_KEYRING</code> and the type provided in <i>arg3</i> argument doesn&#8217;t support setting key linking restrictions.</p>
<dt><code>ENOKEY</code></p>
<dd> No matching key was found or an invalid key was specified.</p>
<dt><code>ENOKEY</code></p>
<dd> The value <code>KEYCTL_GET_KEYRING_ID</code> was specified in <i>operation</i>, the key specified in <i>arg2</i> did not exist, and <i>arg3</i> was zero (meaning don&#8217;t create the key if it didn&#8217;t exist).</p>
<dt><code>ENOMEM</code></p>
<dd> One of kernel memory allocation routines failed during the execution of the syscall.</p>
<dt><code>ENOTDIR</code></p>
<dd> A key of keyring type was expected but the ID of a key with a different type was provided.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> <i>operation</i> was <code>KEYCTL_READ</code> and the key type does not support reading (e.g., the type is <i>&quot;login&quot;</i>).</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> <i>operation</i> was <code>KEYCTL_UPDATE</code> and the key type does not support updating.</p>
<dt><code>EOPNOTSUPP</code></p>
<dd> <i>operation</i> was <code>KEYCTL_RESTRICT_KEYRING</code>, the type provided in <i>arg3</i> argument was &quot;asymmetric&quot;, and the key specified in the restriction specification provided in <i>arg4</i> has type other than &quot;asymmetric&quot; or &quot;keyring&quot;.</p>
<dt><code>EPERM</code></p>
<dd> <i>operation</i> was <code>KEYCTL_GET_PERSISTENT</code>, <i>arg2</i> specified a UID other than the calling thread&#8217;s real or effective UID, and the caller did not have the <code>CAP_SETUID</code> capability.</p>
<dt><code>EPERM</code></p>
<dd> <i>operation</i> was <code>KEYCTL_SESSION_TO_PARENT</code> and either: all of the UIDs (GIDs) of the parent process do not match the effective UID (GID) of the calling process; the UID of the parent&#8217;s existing session keyring or the UID of the caller&#8217;s session keyring did not match the effective UID of the caller; the parent process is not single-thread; or the parent process is <code><a href="/docs/linux/man/1-init/">init</a></code>(1) or a kernel thread.</p>
<dt><code>ETIMEDOUT</code></p>
<dd> <i>operation</i> was <code>KEYCTL_DH_COMPUTE</code> and the initialization of crypto modules has timed out.</dl>
<h2>VERSIONS</h2>
<p> This system call first appeared in Linux 2.6.10.</p>
<h2>CONFORMING TO</h2>
<p> This system call is a nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> No wrapper for this system call is provided in glibc. A wrapper is provided in the <i>libkeyutils</i> library. When employing the wrapper in that library, link with <i>-lkeyutils</i>. However, rather than using this system call directly, you probably want to use the various library functions mentioned in the descriptions of individual operations above.</p>
<h2>EXAMPLES</h2>
<p> The program below provide subset of the functionality of the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program provided by the <i>keyutils</i> package. For informational purposes, the program records various information in a log file. </p>
<p> As described in <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program is invoked with command-line arguments that describe a key that is to be instantiated. The example program fetches and logs these arguments. The program assumes authority to instantiate the requested key, and then instantiates that key. </p>
<p> The following shell session demonstrates the use of this program. In the session, we compile the program and then use it to temporarily replace the standard <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program. (Note that temporarily disabling the standard <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program may not be safe on some systems.) While our example program is installed, we use the example program shown in <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) to request a key. </p>
<p> $ <code>cc -o key_instantiate key_instantiate.c -lkeyutils</code> $ <code>sudo mv /sbin/request-key /sbin/request-key.backup</code> $ <code>sudo cp key_instantiate /sbin/request-key</code> $ <code>./t_request_key user mykey somepayloaddata</code> Key ID is 20d035bf $ <code>sudo mv /sbin/request-key.backup /sbin/request-key</code> </p>
<p> Looking at the log file created by this program, we can see the command-line arguments supplied to our example program: </p>
<p> $ <code>cat /tmp/key_instantiate.log</code> Time: Mon Nov 7 13:06:47 2016 </p>
<p> Command line arguments:<br />
&nbsp;<wbr>&nbsp;argv[0]:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/sbin/request-key<br />
&nbsp;<wbr>&nbsp;operation:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;create<br />
&nbsp;<wbr>&nbsp;key_to_instantiate: 20d035bf<br />
&nbsp;<wbr>&nbsp;UID:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1000<br />
&nbsp;<wbr>&nbsp;GID:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;1000<br />
&nbsp;<wbr>&nbsp;thread_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;process_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0<br />
&nbsp;<wbr>&nbsp;session_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;256e6a6 </p>
<p> Key description: user;1000;1000;3f010000;mykey Auth key payload: somepayloaddata Destination keyring: 256e6a6 Auth key description: .request_key_auth;1000;1000;0b010000;20d035bf </p>
<p> The last few lines of the above output show that the example program was able to fetch:</p>
<dl>
<dt>*</p>
<dd> the description of the key to be instantiated, which included the name of the key (<i>mykey</i>);</p>
<dt>*</p>
<dd> the payload of the authorization key, which consisted of the data (<i>somepayloaddata</i>) passed to <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2);</p>
<dt>*</p>
<dd> the destination keyring that was specified in the call to <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2); and</p>
<dt>*</p>
<dd> the description of the authorization key, where we can see that the name of the authorization key matches the ID of the key that is to be instantiated (<i>20d035bf</i>).</dl>
<p> The example program in <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) specified the destination keyring as <code>KEY_SPEC_SESSION_KEYRING</code>. By examining the contents of <i>/proc/keys</i>, we can see that this was translated to the ID of the destination keyring (<i>0256e6a6</i>) shown in the log output above; we can also see the newly created key with the name <i>mykey</i> and ID <i>20d035bf</i>. </p>
<p> $ <code>cat /proc/keys | egrep &#8216;mykey|256e6a6&#8217;</code> 0256e6a6 I&#8211;Q&#8212; 194 perm 3f030000 1000 1000 keyring _ses: 3 20d035bf I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 user mykey: 16</p>
<h3>Program source</h3>
<p> /* key_instantiate.c */ </p>
<p> #include &lt;sys/types.h&gt; #include &lt;keyutils.h&gt; #include &lt;time.h&gt; #include &lt;fcntl.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;unistd.h&gt; #include &lt;string.h&gt; #include &lt;errno.h&gt; </p>
<p> #ifndef KEY_SPEC_REQUESTOR_KEYRING #define KEY_SPEC_REQUESTOR_KEYRING -8 #endif </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;FILE&nbsp;*fp;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;time_t t;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char&nbsp;*operation;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_serial_t key_to_instantiate, dest_keyring;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_serial_t thread_keyring, process_keyring, session_keyring;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid_t uid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid_t gid;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char dbuf[256];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;char auth_key_payload[256];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int akp_size;&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*&nbsp;Size of auth_key_payload&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int auth_key; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fp&nbsp;=&nbsp;fopen(&quot;/tmp/key_instantiate.log&quot;,&nbsp;&quot;w&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(fp&nbsp;==&nbsp;NULL)<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;setbuf(fp, NULL); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;t&nbsp;=&nbsp;time(NULL);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;Time:&nbsp;%s
&quot;, ctime(&amp;t)); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;The kernel passes a fixed set of arguments to the program<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;that it execs;&nbsp;fetch them.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;operation&nbsp;=&nbsp;argv[1];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_to_instantiate&nbsp;=&nbsp;atoi(argv[2]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uid&nbsp;=&nbsp;atoi(argv[3]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;gid&nbsp;=&nbsp;atoi(argv[4]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;thread_keyring&nbsp;=&nbsp;atoi(argv[5]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;process_keyring&nbsp;=&nbsp;atoi(argv[6]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;session_keyring&nbsp;=&nbsp;atoi(argv[7]); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;Command line arguments:
&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;argv[0]:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s
&quot;, argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;operation:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s
&quot;, operation);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;key_to_instantiate:&nbsp;%jx
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;key_to_instantiate);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;UID:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;uid);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;GID:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jd
&quot;,&nbsp;(intmax_t)&nbsp;gid);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;thread_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jx
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;thread_keyring);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;process_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jx
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;process_keyring);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;&nbsp;<wbr>&nbsp;session_keyring:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%jx
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(uintmax_t)&nbsp;session_keyring);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;
&quot;); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Assume the authority to instantiate the key named in argv[2]<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(keyctl(KEYCTL_ASSUME_AUTHORITY, key_to_instantiate)&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;KEYCTL_ASSUME_AUTHORITY failed:&nbsp;%s
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;strerror(errno));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Fetch the description of the key that is to be instantiated<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(keyctl(KEYCTL_DESCRIBE, key_to_instantiate,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;dbuf, sizeof(dbuf))&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;KEYCTL_DESCRIBE failed:&nbsp;%s
&quot;, strerror(errno));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;Key description:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;%s
&quot;, dbuf); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;/*<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;Fetch the payload of the authorization key, which is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*&nbsp;actually the callout data given to request_key()<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;*/<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;akp_size&nbsp;=&nbsp;keyctl(KEYCTL_READ, KEY_SPEC_REQKEY_AUTH_KEY,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auth_key_payload, sizeof(auth_key_payload));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(akp_size&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(fp,&nbsp;&quot;KEYCTL_READ failed:&nbsp;%s
&quot;, strerror(errno));<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;auth_key_payload[akp_size]&nbsp;=&nbsp;&#8216;
