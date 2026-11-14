---
title: "keyrings(7)"
name: "keyrings"
section: "7"
letter: "k"
url: "/docs/linux/man/7-keyrings/"
description: "keyrings – in-kernel key management and retention facility"
---

<p>keyrings &#8211; in-kernel key management and retention facility</p>
<h2>Description</h2>
<p>The Linux key-management facility is primarily a way for various kernel components to retain or cache security data, authentication keys, encryption keys, and other data in the kernel. </p>
<p> System call interfaces are provided so that user-space programs can manage those objects and also use the facility for their own purposes; see <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), and <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2). </p>
<p> A library and some user-space utilities are provided to allow access to the facility. See <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), and <code><a href="/docs/linux/man/7-keyutils/">keyutils</a></code>(7) for more information.</p>
<h3>Keys</h3>
<p>A key has the following attributes:</p>
<dl>
<dt>Serial number (ID)</p>
<dd>This is a unique integer handle by which a key is referred to in system calls. The serial number is sometimes synonymously referred as the key ID. Programmatically, key serial numbers are represented using the type <i>key_serial_t</i>.</p>
<dt>Type</p>
<dd>A key&#8217;s type defines what sort of data can be held in the key, how the proposed content of the key will be parsed, and how the payload will be used.</p>
<dd>There are a number of general-purpose types available, plus some specialist types defined by specific kernel components.</p>
<dt>Description (name)</p>
<dd>The key description is a printable string that is used as the search term for the key (in conjunction with the key type) as well as a display name. During searches, the description may be partially matched or exactly matched.</p>
<dt>Payload (data)</p>
<dd>The payload is the actual content of a key. This is usually set when a key is created, but it is possible for the kernel to upcall to user space to finish the instantiation of a key if that key wasn&#8217;t already known to the kernel when it was requested. For further details, see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2).</p>
<dd>A key&#8217;s payload can be read and updated if the key type supports it and if suitable permission is granted to the caller.</p>
<dt>Access rights</p>
<dd>Much as files do, each key has an owning user ID, an owning group ID, and a security label. Each key also has a set of permissions, though there are more than for a normal UNIX file, and there is an additional category&#8212;possessor&#8212;beyond the usual user, group, and other (see <i>Possession</i>, below).</p>
<dd>Note that keys are quota controlled, since they require unswappable kernel memory. The owning user ID specifies whose quota is to be debited.</p>
<dt>Expiration time</p>
<dd>Each key can have an expiration time set. When that time is reached, the key is marked as being expired and accesses to it fail with the error <code>EKEYEXPIRED</code>. If not deleted, updated, or replaced, then, after a set amount of time, an expired key is automatically removed (garbage collected) along with all links to it, and attempts to access the key fail with the error <code>ENOKEY</code>.</p>
<dt>Reference count</p>
<dd>Each key has a reference count. Keys are referenced by keyrings, by currently active users, and by a process&#8217;s credentials. When the reference count reaches zero, the key is scheduled for garbage collection.</dl>
<h3>Key types</h3>
<p>The kernel provides several basic types of key:</p>
<dl>
<dt><i>keyring</i></p>
<dd>Keyrings are special keys which store a set of links to other keys (including other keyrings), analogous to a directory holding links to files. The main purpose of a keyring is to prevent other keys from being garbage collected because nothing refers to them.</p>
<dd>Keyrings with descriptions (names) that begin with a period (&#8216;.&#8217;) are reserved to the implementation.</p>
<dt><i>user</i></p>
<dd>This is a general-purpose key type. The key is kept entirely within kernel memory. The payload may be read and updated by user-space applications.</p>
<dd>The payload for keys of this type is a blob of arbitrary data of up to 32,767 bytes.</p>
<dd>The description may be any valid string, though it is preferred that it start with a colon-delimited prefix representing the service to which the key is of interest (for instance <i>&quot;afs:mykey&quot;</i>).</p>
<dt><i>&quot;logon&quot;</i> (since Linux 3.3)</p>
<dd>This key type is essentially the same as <i>&quot;user&quot;</i>, but it does not provide reading (i.e., the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_READ</code> operation), meaning that the key payload is never visible from user space. This is suitable for storing username-password pairs that should not be readable from user space.</p>
<dd>The description of a <i>&quot;logon&quot;</i> key <i>must</i> start with a non-empty colon-delimited prefix whose purpose is to identify the service to which the key belongs. (Note that this differs from keys of the <i>&quot;user&quot;</i> type, where the inclusion of a prefix is recommended but is not enforced.)</p>
<dt><i>&quot;big_key&quot;</i> (since Linux 3.13)</p>
<dd>This key type is similar to the <i>user</i> key type, but it may hold a payload of up to 1 MiB in size. This key type is useful for purposes such as holding Kerberos ticket caches.</p>
<dd>The payload data may be stored in a tmpfs filesystem, rather than in kernel memory, if the data size exceeds the overhead of storing the data in the filesystem. (Storing the data in a filesystem requires filesystem structures to be allocated in the kernel. The size of these structures determines the size threshold above which the tmpfs storage method is used.) Since Linux 4.8, the payload data is encrypted when stored in tmpfs, thereby preventing it from being written unencrypted into swap space.</dl>
<p> There are more specialized key types available also, but they aren&#8217;t discussed here because they aren&#8217;t intended for normal user-space use. </p>
<p> Key type names that begin with a period (&#8216;.&#8217;) are reserved to the implementation.</p>
<h3>Keyrings</h3>
<p>As previously mentioned, keyrings are a special type of key that contain links to other keys (which may include other keyrings). Keys may be linked to by multiple keyrings. Keyrings may be considered as analogous to UNIX directories where each directory contains a set of hard links to files. </p>
<p> Various operations (system calls) may be applied only to keyrings:</p>
<dl>
<dt>Adding</p>
<dd>A key may be added to a keyring by system calls that create keys. This prevents the new key from being immediately deleted when the system call releases its last reference to the key.</p>
<dt>Linking</p>
<dd>A link may be added to a keyring pointing to a key that is already known, provided this does not create a self-referential cycle.</p>
<dt>Unlinking</p>
<dd>A link may be removed from a keyring. When the last link to a key is removed, that key will be scheduled for deletion by the garbage collector.</p>
<dt>Clearing</p>
<dd>All the links may be removed from a keyring.</p>
<dt>Searching</p>
<dd>A keyring may be considered the root of a tree or subtree in which keyrings form the branches and non-keyrings the leaves. This tree may be searched for a key matching a particular type and description.</dl>
<p> See <code><a href="/docs/linux/man/3-keyctl_clear/">keyctl_clear</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_link/">keyctl_link</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_search/">keyctl_search</a></code>(3), and <code><a href="/docs/linux/man/3-keyctl_unlink/">keyctl_unlink</a></code>(3) for more information.</p>
<h3>Anchoring keys</h3>
<p>To prevent a key from being garbage collected, it must be anchored to keep its reference count elevated when it is not in active use by the kernel. </p>
<p> Keyrings are used to anchor other keys: each link is a reference on a key. Note that keyrings themselves are just keys and are also subject to the same anchoring requirement to prevent them being garbage collected. </p>
<p> The kernel makes available a number of anchor keyrings. Note that some of these keyrings will be created only when first accessed.</p>
<dl>
<dt>Process keyrings</p>
<dd>Process credentials themselves reference keyrings with specific semantics. These keyrings are pinned as long as the set of credentials exists, which is usually as long as the process exists.</p>
<dd>There are three keyrings with different inheritance/sharing rules: the <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) (inherited and shared by all child processes), the <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7) (shared by all threads in a process) and the <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7) (specific to a particular thread).</p>
<dd>As an alternative to using the actual keyring IDs, in calls to <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), and <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), the special keyring values <code>KEY_SPEC_SESSION_KEYRING</code>, <code>KEY_SPEC_PROCESS_KEYRING</code>, and <code>KEY_SPEC_THREAD_KEYRING</code> can be used to refer to the caller&#8217;s own instances of these keyrings.</p>
<dt>User keyrings</p>
<dd>Each UID known to the kernel has a record that contains two keyrings: the <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7) and the <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7). These exist for as long as the UID record in the kernel exists.</p>
<dd>As an alternative to using the actual keyring IDs, in calls to <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), and <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), the special keyring values <code>KEY_SPEC_USER_KEYRING</code> and <code>KEY_SPEC_USER_SESSION_KEYRING</code> can be used to refer to the caller&#8217;s own instances of these keyrings.</p>
<dd>A link to the user keyring is placed in a new session keyring by <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) when a new login session is initiated.</p>
<dt>Persistent keyrings</p>
<dd>There is a <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7) available to each UID known to the system. It may persist beyond the life of the UID record previously mentioned, but has an expiration time set such that it is automatically cleaned up after a set time. The persistent keyring permits, for example, <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) scripts to use credentials that are left in the persistent keyring after the user logs out.</p>
<dd>Note that the expiration time of the persistent keyring is reset every time the persistent key is requested.</p>
<dt>Special keyrings</p>
<dd>There are special keyrings owned by the kernel that can anchor keys for special purposes. An example of this is the <i>system keyring</i> used for holding encryption keys for module signature verification.</p>
<dd>These special keyrings are usually closed to direct alteration by user space.</dl>
<p> An originally planned &quot;group keyring&quot;, for storing keys associated with each GID known to the kernel, is not so far implemented, is unlikely to be implemented. Nevertheless, the constant <code>KEY_SPEC_GROUP_KEYRING</code> has been defined for this keyring.</p>
<h3>Possession</h3>
<p>The concept of possession is important to understanding the keyrings security model. Whether a thread possesses a key is determined by the following rules:</p>
<dl>
<dt>(1)</p>
<dd>Any key or keyring that does not grant <i>search</i> permission to the caller is ignored in all the following rules.</p>
<dt>(2)</p>
<dd>A thread possesses its <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), and <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7) directly because those keyrings are referred to by its credentials.</p>
<dt>(3)</p>
<dd>If a keyring is possessed, then any key it links to is also possessed.</p>
<dt>(4)</p>
<dd>If any key a keyring links to is itself a keyring, then rule (3) applies recursively.</p>
<dt>(5)</p>
<dd>If a process is upcalled from the kernel to instantiate a key (see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2)), then it also possesses the requester&#8217;s keyrings as in rule (1) as if it were the requester.</dl>
<p> Note that possession is not a fundamental property of a key, but must rather be calculated each time the key is needed. </p>
<p> Possession is designed to allow set-user-ID programs run from, say a user&#8217;s shell to access the user&#8217;s keys. Granting permissions to the key possessor while denying them to the key owner and group allows the prevention of access to keys on the basis of UID and GID matches. </p>
<p> When it creates the session keyring, <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8) adds a link to the <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), thus making the user keyring and anything it contains possessed by default.</p>
<h3>Access rights</h3>
<p>Each key has the following security-related attributes:</p>
<dl>
<dt>*</p>
<dd>The owning user ID</p>
<dt>*</p>
<dd>The ID of a group that is permitted to access the key</p>
<dt>*</p>
<dd>A security label</p>
<dt>*</p>
<dd>A permissions mask</dl>
<p> The permissions mask contains four sets of rights. The first three sets are mutually exclusive. One and only one will be in force for a particular access check. In order of descending priority, these three sets are:</p>
<dl>
<dt><i>user</i></p>
<dd>The set specifies the rights granted if the key&#8217;s user ID matches the caller&#8217;s filesystem user ID.</p>
<dt><i>group</i></p>
<dd>The set specifies the rights granted if the user ID didn&#8217;t match and the key&#8217;s group ID matches the caller&#8217;s filesystem GID or one of the caller&#8217;s supplementary group IDs.</p>
<dt><i>other</i></p>
<dd>The set specifies the rights granted if neither the key&#8217;s user ID nor group ID matched.</dl>
<p> The fourth set of rights is:</p>
<dl>
<dt><i>possessor</i></p>
<dd>The set specifies the rights granted if a key is determined to be possessed by the caller.</dl>
<p> The complete set of rights for a key is the union of whichever of the first three sets is applicable plus the fourth set if the key is possessed. </p>
<p> The set of rights that may be granted in each of the four masks is as follows:</p>
<dl>
<dt><i>view</i></p>
<dd>The attributes of the key may be read. This includes the type, description, and access rights (excluding the security label).</p>
<dt><i>read</i></p>
<dd>For a key: the payload of the key may be read. For a keyring: the list of serial numbers (keys) to which the keyring has links may be read.</p>
<dt><i>write</i></p>
<dd>The payload of the key may be updated and the key may be revoked. For a keyring, links may be added to or removed from the keyring, and the keyring may be cleared completely (all links are removed),</p>
<dt><i>search</i></p>
<dd>For a key (or a keyring): the key may be found by a search. For a keyring: keys and keyrings that are linked to by the keyring may be searched.</p>
<dt><i>link</i></p>
<dd>Links may be created from keyrings to the key. The initial link to a key that is established when the key is created doesn&#8217;t require this permission.</p>
<dt><i>setattr</i></p>
<dd>The ownership details and security label of the key may be changed, the key&#8217;s expiration time may be set, and the key may be revoked.</dl>
<p> In addition to access rights, any active Linux Security Module (LSM) may prevent access to a key if its policy so dictates. A key may be given a security label or other attribute by the LSM; this label is retrievable via <code><a href="/docs/linux/man/3-keyctl_get_security/">keyctl_get_security</a></code>(3). </p>
<p> See <code><a href="/docs/linux/man/3-keyctl_chown/">keyctl_chown</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_describe/">keyctl_describe</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_get_security/">keyctl_get_security</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_setperm/">keyctl_setperm</a></code>(3), and <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) for more information.</p>
<h3>Searching for keys</h3>
<p>One of the key features of the Linux key-management facility is the ability to find a key that a process is retaining. The <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) system call is the primary point of access for user-space applications to find a key. (Internally, the kernel has something similar available for use by internal components that make use of keys.) </p>
<p> The search algorithm works as follows:</p>
<dl>
<dt>(1)</p>
<dd>The process keyrings are searched in the following order: the thread <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7) if it exists, the <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7) if it exists, and then either the <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7) if it exists or the <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7) if that exists.</p>
<dt>(2)</p>
<dd>If the caller was a process that was invoked by the <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) upcall mechanism, then the keyrings of the original caller of <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) will be searched as well.</p>
<dt>(3)</p>
<dd>The search of a keyring tree is in breadth-first order: each keyring is searched first for a match, then the keyrings referred to by that keyring are searched.</p>
<dt>(4)</p>
<dd>If a matching key is found that is valid, then the search terminates and that key is returned.</p>
<dt>(5)</p>
<dd>If a matching key is found that has an error state attached, that error state is noted and the search continues.</p>
<dt>(6)</p>
<dd>If no valid matching key is found, then the first noted error state is returned; otherwise, an <code>ENOKEY</code> error is returned.</dl>
<p> It is also possible to search a specific keyring, in which case only steps (3) to (6) apply. </p>
<p> See <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) and <code><a href="/docs/linux/man/3-keyctl_search/">keyctl_search</a></code>(3) for more information.</p>
<h3>On-demand key creation</h3>
<p>If a key cannot be found, <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2) will, if given a <i>callout_info</i> argument, create a new key and then upcall to user space to instantiate the key. This allows keys to be created on an as-needed basis. </p>
<p> Typically, this will involve the kernel creating a new process that executes the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program, which will then execute the appropriate handler based on its configuration. </p>
<p> The handler is passed a special authorization key that allows it and only it to instantiate the new key. This is also used to permit searches performed by the handler program to also search the requester&#8217;s keyrings. </p>
<p> See <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), <code><a href="/docs/linux/man/3-keyctl_assume_authority/">keyctl_assume_authority</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_instantiate/">keyctl_instantiate</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_negate/">keyctl_negate</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_reject/">keyctl_reject</a></code>(3), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8), and <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) for more information.</p>
<h3>/proc files</h3>
<p>The kernel provides various <i>/proc</i> files that expose information about keys or define limits on key usage.</p>
<dl>
<dt><i>/proc/keys</i> (since Linux 2.6.10)</p>
<dd>This file exposes a list of the keys for which the reading thread has <i>view</i> permission, providing various information about each key. The thread need not possess the key for it to be visible in this file.</p>
<dd>The only keys included in the list are those that grant <i>view</i> permission to the reading process (regardless of whether or not it possesses them). LSM security checks are still performed, and may filter out further keys that the process is not authorized to view.</p>
<dd>An example of the data that one might see in this file (with the columns numbered for easy reference below) is the following:</p>
<dd>&nbsp;<wbr>&nbsp;(1)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(2)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(3)(4)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(5)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(6)&nbsp;<wbr>&nbsp;<wbr>&nbsp;(7)&nbsp;<wbr>&nbsp;<wbr>&nbsp;(8)&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;(9) 009a2028 I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 user krb_ccache:primary: 12 1806c4ba I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 keyring _pid: 2 25d3a08f I&#8211;Q&#8212; 1 perm 1f3f0000 1000 65534 keyring _uid_ses.1000: 1 28576bd8 I&#8211;Q&#8212; 3 perm 3f010000 1000 1000 keyring _krb: 1 2c546d21 I&#8211;Q&#8212; 190 perm 3f030000 1000 1000 keyring _ses: 2 30a4e0be I&#8212;&#8212; 4 2d 1f030000 1000 65534 keyring _persistent.1000: 1 32100fab I&#8211;Q&#8212; 4 perm 1f3f0000 1000 65534 keyring _uid.1000: 2 32a387ea I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 keyring _pid: 2 3ce56aea I&#8211;Q&#8212; 5 perm 3f030000 1000 1000 keyring _ses: 1</p>
<dd>The fields shown in each line of this file are as follows:</p>
<dl>
<dd>
<dl>
<dt>ID (1)</p>
<dd>The ID (serial number) of the key, expressed in hexadecimal.</p>
<dt>Flags (2)</p>
<dd>A set of flags describing the state of the key:</p>
<dl>
<dd>
<dl>
<dt>I</p>
<dd>The key has been instantiated.</p>
<dt>R</p>
<dd>The key has been revoked.</p>
<dt>D</p>
<dd>The key is dead (i.e., the key type has been unregistered). (A key may be briefly in this state during garbage collection.)</p>
<dt>Q</p>
<dd>The key contributes to the user&#8217;s quota.</p>
<dt>U</p>
<dd>The key is under construction via a callback to user space; see <code><a href="/docs/linux/man/2-request-key/">request-key</a></code>(2).</p>
<dt>N</p>
<dd>The key is negatively instantiated.</p>
<dt>i</p>
<dd>The key has been invalidated.</dl>
</dl>
<dt>Usage (3)</p>
<dd>This is a count of the number of kernel credential structures that are pinning the key (approximately: the number of threads and open file references that refer to this key).</p>
<dt>Timeout (4)</p>
<dd>The amount of time until the key will expire, expressed in human-readable form (weeks, days, hours, minutes, and seconds). The string <i>perm</i> here means that the key is permanent (no timeout). The string <i>expd</i> means that the key has already expired, but has not yet been garbage collected.</p>
<dt>Permissions (5)</p>
<dd>The key permissions, expressed as four hexadecimal bytes containing, from left to right, the possessor, user, group, and other permissions. Within each byte, the permission bits are as follows:</p>
<dd>
<dl>
<dd>
<dl>
<dt>0x01</p>
<dd><i>view</i></p>
<dt>Ox02</p>
<dd><i>read</i></p>
<dt>0x04</p>
<dd><i>write</i></p>
<dt>0x08</p>
<dd><i>search</i></p>
<dt>0x10</p>
<dd><i>link</i></p>
<dt>0x20</p>
<dd><i>setattr</i></dl>
</dl>
<dt>UID (6)</p>
<dd>The user ID of the key owner.</p>
<dt>GID (7)</p>
<dd>The group ID of the key. The value -1 here means that the key has no group ID; this can occur in certain circumstances for keys created by the kernel.</p>
<dt>Type (8)</p>
<dd>The key type (user, keyring, etc.)</p>
<dt>Description (9)</p>
<dd>The key description (name). This field contains descriptive information about the key. For most key types, it has the form</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;name[: extra-info]</p>
<dd>The <i>name</i> subfield is the key&#8217;s description (name). The optional <i>extra-info</i> field provides some further information about the key. The information that appears here depends on the key type, as follows:</p>
<dl>
<dd>
<dl>
<dt><i>&quot;user&quot;</i> and <i>&quot;logon&quot;</i></p>
<dd>The size in bytes of the key payload (expressed in decimal).</p>
<dt><i>&quot;keyring&quot;</i></p>
<dd>The number of keys linked to the keyring, or the string <i>empty</i> if there are no keys linked to the keyring.</p>
<dt><i>&quot;big_key&quot;</i></p>
<dd>The payload size in bytes, followed either by the string <i>[file]</i>, if the key payload exceeds the threshold that means that the payload is stored in a (swappable) <code><a href="/docs/linux/man/5-tmpfs/">tmpfs</a></code>(5) filesystem, or otherwise the string <i>[buff]</i>, indicating that the key is small enough to reside in kernel memory.</dl>
</dl>
<dd>For the <i>&quot;.request_key_auth&quot;</i> key type (authorization key; see <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2)), the description field has the form shown in the following example:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key:c9a9b19 pid:28880 ci:10</p>
<dd>The three subfields are as follows:</p>
<dl>
<dd>
<dl>
<dt><i>key</i></p>
<dd>The hexadecimal ID of the key being instantiated in the requesting program.</p>
<dt><i>pid</i></p>
<dd>The PID of the requesting program.</p>
<dt><i>ci</i></p>
<dd>The length of the callout data with which the requested key should be instantiated (i.e., the length of the payload associated with the authorization key).</dl>
</dl>
</dl>
</dl>
<dt><i>/proc/key-users</i> (since Linux 2.6.10)</p>
<dd>This file lists various information for each user ID that has at least one key on the system. An example of the data that one might see in this file is the following:</p>
<dd>&nbsp;<wbr>&nbsp;<wbr>&nbsp;0:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;10 9/9 2/1000000 22/25000000<br />
&nbsp;<wbr>&nbsp;42:&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;9 9/9 8/200 106/20000 1000: 11 11/11 10/200 271/20000</p>
<dd>The fields shown in each line are as follows:</p>
<dl>
<dd>
<dl>
<dt><i>uid</i></p>
<dd>The user ID.</p>
<dt><i>usage</i></p>
<dd>This is a kernel-internal usage count for the kernel structure used to record key users.</p>
<dt><i>nkeys</i>/<i>nikeys</i></p>
<dd>The total number of keys owned by the user, and the number of those keys that have been instantiated.</p>
<dt><i>qnkeys</i>/<i>maxkeys</i></p>
<dd>The number of keys owned by the user, and the maximum number of keys that the user may own.</p>
<dt><i>qnbytes</i>/<i>maxbytes</i></p>
<dd>The number of bytes consumed in payloads of the keys owned by this user, and the upper limit on the number of bytes in key payloads for that user.</dl>
</dl>
<dt><i>/proc/sys/kernel/keys/gc_delay</i> (since Linux 2.6.32)</p>
<dd>The value in this file specifies the interval, in seconds, after which revoked and expired keys will be garbage collected. The purpose of having such an interval is so that there is a window of time where user space can see an error (respectively <code>EKEYREVOKED</code> and <code>EKEYEXPIRED</code>) that indicates what happened to the key.</p>
<dd>The default value in this file is 300 (i.e., 5 minutes).</p>
<dt><i>/proc/sys/kernel/keys/persistent_keyring_expiry</i> (since Linux 3.13)</p>
<dd>This file defines an interval, in seconds, to which the persistent keyring&#8217;s expiration timer is reset each time the keyring is accessed (via <code><a href="/docs/linux/man/3-keyctl_get_persistent/">keyctl_get_persistent</a></code>(3) or the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_GET_PERSISTENT</code> operation.)</p>
<dd>The default value in this file is 259200 (i.e., 3 days).</dl>
<p> The following files (which are writable by privileged processes) are used to enforce quotas on the number of keys and number of bytes of data that can be stored in key payloads:</p>
<dl>
<dt><i>/proc/sys/kernel/keys/maxbytes</i> (since Linux 2.6.26)</p>
<dd>This is the maximum number of bytes of data that a nonroot user can hold in the payloads of the keys owned by the user.</p>
<dd>The default value in this file is 20,000.</p>
<dt><i>/proc/sys/kernel/keys/maxkeys</i> (since Linux 2.6.26)</p>
<dd>This is the maximum number of keys that a nonroot user may own.</p>
<dd>The default value in this file is 200.</p>
<dt><i>/proc/sys/kernel/keys/root_maxbytes</i> (since Linux 2.6.26)</p>
<dd>This is the maximum number of bytes of data that the root user (UID 0 in the root user namespace) can hold in the payloads of the keys owned by root.</p>
<dd>The default value in this file is 25,000,000 (20,000 before Linux 3.17).</p>
<dt><i>/proc/sys/kernel/keys/root_maxkeys</i> (since Linux 2.6.26)</p>
<dd>This is the maximum number of keys that the root user (UID 0 in the root user namespace) may own.</p>
<dd>The default value in this file is 1,000,000 (200 before Linux 3.17).</dl>
<p> With respect to keyrings, note that each link in a keyring consumes 4 bytes of the keyring payload.</p>
<h3>Users</h3>
<p>The Linux key-management facility has a number of users and usages, but is not limited to those that already exist. </p>
<p> In-kernel users of this facility include:</p>
<dl>
<dt>Network filesystems &#8211; DNS</p>
<dd>The kernel uses the upcall mechanism provided by the keys to upcall to user space to do DNS lookups and then to cache the results.</p>
<dt>AF_RXRPC and kAFS &#8211; Authentication</p>
<dd>The AF_RXRPC network protocol and the in-kernel AFS filesystem use keys to store the ticket needed to do secured or encrypted traffic. These are then looked up by network operations on AF_RXRPC and filesystem operations on kAFS.</p>
<dt>NFS &#8211; User ID mapping</p>
<dd>The NFS filesystem uses keys to store mappings of foreign user IDs to local user IDs.</p>
<dt>CIFS &#8211; Password</p>
<dd>The CIFS filesystem uses keys to store passwords for accessing remote shares.</p>
<dt>Module verification</p>
<dd>The kernel build process can be made to cryptographically sign modules. That signature is then checked when a module is loaded.</dl>
<p> User-space users of this facility include:</p>
<dl>
<dt>Kerberos key storage</p>
<dd>The MIT Kerberos 5 facility (libkrb5) can use keys to store authentication tokens which can be made to be automatically cleaned up a set time after the user last uses them, but until then permits them to hang around after the user has logged out so that <code><a href="/docs/linux/man/8-cron/">cron</a></code>(8) scripts can use them.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyutils/">keyutils</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), <code><a href="/docs/linux/man/8-pam_keyinit/">pam_keyinit</a></code>(8), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<p> The kernel source files <i>Documentation/crypto/asymmetric-keys.txt</i> and under <i>Documentation/security/keys</i> (or, before Linux 4.13, in the file <i>Documentation/security/keys.txt</i>).</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
