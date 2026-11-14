---
title: "request_key(2)"
name: "request_key"
section: "2"
letter: "r"
url: "/docs/linux/man/2-request_key/"
description: "request_key – request a key from the kernel’s key management facility"
---

<h2 class="name">NAME</h2>
<p> request_key &#8211; request a key from the kernel&#8217;s key management facility </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
#include &lt;sys/types.h&gt;
key_serial_t request_key(const char *type, const char *description,
                         const char *callout_info,
                         key_serial_t dest_keyring);
</code></pre>
<p> No glibc wrapper is provided for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>request_key</code>() attempts to find a key of the given <i>type</i> with a description (name) that matches the specified <i>description</i>. If such a key could not be found, then the key is optionally created. If the key is found or created, <code>request_key</code>() attaches it to the keyring whose ID is specified in <i>dest_keyring</i> and returns the key&#8217;s serial number. </p>
<p> <code>request_key</code>() first recursively searches for a matching key in all of the keyrings attached to the calling process. The keyrings are searched in the order: thread-specific keyring, process-specific keyring, and then session keyring. </p>
<p> If <code>request_key</code>() is called from a program invoked by <code>request_key</code>() on behalf of some other process to generate a key, then the keyrings of that other process will be searched next, using that other process&#8217;s user ID, group ID, supplementary group IDs, and security context to determine access. </p>
<p> The search of the keyring tree is breadth-first: the keys in each keyring searched are checked for a match before any child keyrings are recursed into. Only keys for which the caller has <i>search</i> permission be found, and only keyrings for which the caller has <i>search</i> permission may be searched. </p>
<p> If the key is not found and <i>callout</i> is NULL, then the call fails with the error <code>ENOKEY</code>. </p>
<p> If the key is not found and <i>callout</i> is not NULL, then the kernel attempts to invoke a user-space program to instantiate the key. The details are given below. </p>
<p> The <i>dest_keyring</i> serial number may be that of a valid keyring for which the caller has <i>write</i> permission, or it may be one of the following special keyring IDs:</p>
<dl>
<dt><code>KEY_SPEC_THREAD_KEYRING</code></p>
<dd> This specifies the caller&#8217;s thread-specific keyring (see <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7)).</p>
<dt><code>KEY_SPEC_PROCESS_KEYRING</code></p>
<dd> This specifies the caller&#8217;s process-specific keyring (see <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7)).</p>
<dt><code>KEY_SPEC_SESSION_KEYRING</code></p>
<dd> This specifies the caller&#8217;s session-specific keyring (see <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7)).</p>
<dt><code>KEY_SPEC_USER_KEYRING</code></p>
<dd> This specifies the caller&#8217;s UID-specific keyring (see <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7)).</p>
<dt><code>KEY_SPEC_USER_SESSION_KEYRING</code></p>
<dd> This specifies the caller&#8217;s UID-session keyring (see <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)).</dl>
<p> When the <i>dest_keyring</i> is specified as 0 and no key construction has been performed, then no additional linking is done. </p>
<p> Otherwise, if <i>dest_keyring</i> is 0 and a new key is constructed, the new key will be linked to the &quot;default&quot; keyring. More precisely, when the kernel tries to determine to which keyring the newly constructed key should be linked, it tries the following keyrings, beginning with the keyring set via the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_SET_REQKEY_KEYRING</code> operation and continuing in the order shown below until it finds the first keyring that exists:</p>
<dl>
<dt>&bull;</p>
<dd> The requestor keyring (<code>KEY_REQKEY_DEFL_REQUESTOR_KEYRING</code>, since Linux 2.6.29).</p>
<dt>&bull;</p>
<dd> The thread-specific keyring (<code>KEY_REQKEY_DEFL_THREAD_KEYRING</code>; see <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7)).</p>
<dt>&bull;</p>
<dd> The process-specific keyring (<code>KEY_REQKEY_DEFL_PROCESS_KEYRING</code>; see <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7)).</p>
<dt>&bull;</p>
<dd> The session-specific keyring (<code>KEY_REQKEY_DEFL_SESSION_KEYRING</code>; see <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7)).</p>
<dt>&bull;</p>
<dd> The session keyring for the process&#8217;s user ID (<code>KEY_REQKEY_DEFL_USER_SESSION_KEYRING</code>; see <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)). This keyring is expected to always exist.</p>
<dt>&bull;</p>
<dd> The UID-specific keyring (<code>KEY_REQKEY_DEFL_USER_KEYRING</code>; see <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7)). This keyring is also expected to always exist.</dl>
<p> If the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_SET_REQKEY_KEYRING</code> operation specifies <code>KEY_REQKEY_DEFL_DEFAULT</code> (or no <code>KEYCTL_SET_REQKEY_KEYRING</code> operation is performed), then the kernel looks for a keyring starting from the beginning of the list.</p>
<h3>Requesting user-space instantiation of a key</h3>
<p> If the kernel cannot find a key matching <i>type</i> and <i>description</i>, and <i>callout</i> is not NULL, then the kernel attempts to invoke a user-space program to instantiate a key with the given <i>type</i> and <i>description</i>. In this case, the following steps are performed:</p>
<dl>
<dt>a)</p>
<dd> The kernel creates an uninstantiated key, U, with the requested <i>type</i> and <i>description</i>.</p>
<dt>b)</p>
<dd> The kernel creates an authorization key, V, that refers to the key U and records the facts that the caller of <code>request_key</code>() is:</p>
<dl>
<dt>
<dd>
<dl>
<dt>(1)</p>
<dd> the context in which the key U should be instantiated and secured, and</p>
<dt>(2)</p>
<dd> the context from which associated key requests may be satisfied.</dl>
</dl>
<dt>
<dd> The authorization key is constructed as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> The key type is <i>&quot;.request_key_auth&quot;</i>.</p>
<dt>*</p>
<dd> The key&#8217;s UID and GID are the same as the corresponding filesystem IDs of the requesting process.</p>
<dt>*</p>
<dd> The key grants <i>view</i>, <i>read</i>, and <i>search</i> permissions to the key possessor as well as <i>view</i> permission for the key user.</p>
<dt>*</p>
<dd> The description (name) of the key is the hexadecimal string representing the ID of the key that is to be instantiated in the requesting program.</p>
<dt>*</p>
<dd> The payload of the key is taken from the data specified in <i>callout_info</i>.</p>
<dt>*</p>
<dd> Internally, the kernel also records the PID of the process that called <code>request_key</code>().</dl>
</dl>
<dt>c)</p>
<dd> The kernel creates a process that executes a user-space service such as <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) with a new session keyring that contains a link to the authorization key, V.</p>
<dt>
<dd> This program is supplied with the following command-line arguments:</p>
<dl>
<dt>
<dd>
<dl>
<dt>[0]</p>
<dd> The string <i>&quot;/sbin/request-key&quot;</i>.</p>
<dt>[1]</p>
<dd> The string <i>create</i> (indicating that a key is to be created).</p>
<dt>[2]</p>
<dd> The ID of the key that is to be instantiated.</p>
<dt>[3]</p>
<dd> The filesystem UID of the caller of <code>request_key</code>().</p>
<dt>[4]</p>
<dd> The filesystem GID of the caller of <code>request_key</code>().</p>
<dt>[5]</p>
<dd> The ID of the thread keyring of the caller of <code>request_key</code>(). This may be zero if that keyring hasn&#8217;t been created.</p>
<dt>[6]</p>
<dd> The ID of the process keyring of the caller of <code>request_key</code>(). This may be zero if that keyring hasn&#8217;t been created.</p>
<dt>[7]</p>
<dd> The ID of the session keyring of the caller of <code>request_key</code>().</dl>
</dl>
<dt>
<dd> <i>Note</i>: each of the command-line arguments that is a key ID is encoded in <i>decimal</i> (unlike the key IDs shown in <i>/proc/keys</i>, which are shown as hexadecimal values).</p>
<dt>d)</p>
<dd> The program spawned in the previous step:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*</p>
<dd> Assumes the authority to instantiate the key U using the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_ASSUME_AUTHORITY</code> operation (typically via the <code><a href="/docs/linux/man/3-keyctl_assume_authority/">keyctl_assume_authority</a></code>(3) function).</p>
<dt>*</p>
<dd> Obtains the callout data from the payload of the authorization key V (using the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_READ</code> operation (or, more commonly, the <code><a href="/docs/linux/man/3-keyctl_read/">keyctl_read</a></code>(3) function) with a key ID value of <code>KEY_SPEC_REQKEY_AUTH_KEY</code>).</p>
<dt>*</p>
<dd> Instantiates the key (or execs another program that performs that task), specifying the payload and destination keyring. (The destination keyring that the requestor specified when calling <code>request_key</code>() can be accessed using the special key ID <code>KEY_SPEC_REQUESTOR_KEYRING</code>.) Instantiation is performed using the <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2) <code>KEYCTL_INSTANTIATE</code> operation (or, more commonly, the <code><a href="/docs/linux/man/3-keyctl_instantiate/">keyctl_instantiate</a></code>(3) function). At this point, the <code>request_key</code>() call completes, and the requesting program can continue execution.</dl>
</dl>
</dl>
<p> If these steps are unsuccessful, then an <code>ENOKEY</code> error will be returned to the caller of <code>request_key</code>() and a temporary, negatively instantiated key will be installed in the keyring specified by <i>dest_keyring</i>. This will expire after a few seconds, but will cause subsequent calls to <code>request_key</code>() to fail until it does. The purpose of this negatively instantiated key is to prevent (possibly different) processes making repeated requests (that require expensive <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) upcalls) for a key that can&#8217;t (at the moment) be positively instantiated. </p>
<p> Once the key has been instantiated, the authorization key (<code>KEY_SPEC_REQKEY_AUTH_KEY</code>) is revoked, and the destination keyring (<code>KEY_SPEC_REQUESTOR_KEYRING</code>) is no longer accessible from the <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) program. </p>
<p> If a key is created, then&#8212;regardless of whether it is a valid key or a negatively instantiated key&#8212;it will displace any other key with the same type and description from the keyring specified in <i>dest_keyring</i>.</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>request_key</code>() returns the serial number of the key it found or caused to be created. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></p>
<dd> The keyring wasn&#8217;t available for modification by the user.</p>
<dt><code>EDQUOT</code></p>
<dd> The key quota for this user would be exceeded by creating this key or linking it to the keyring.</p>
<dt><code>EFAULT</code></p>
<dd> One of <i>type</i>, <i>description</i>, or <i>callout_info</i> points outside the process&#8217;s accessible address space.</p>
<dt><code>EINTR</code></p>
<dd> The request was interrupted by a signal; see <code><a href="/docs/linux/man/7-signal/">signal</a></code>(7).</p>
<dt><code>EINVAL</code></p>
<dd> The size of the string (including the terminating null byte) specified in <i>type</i> or <i>description</i> exceeded the limit (32 bytes and 4096 bytes respectively).</p>
<dt><code>EINVAL</code></p>
<dd> The size of the string (including the terminating null byte) specified in <i>callout_info</i> exceeded the system page size.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> An expired key was found, but no replacement could be obtained.</p>
<dt><code>EKEYREJECTED</code></p>
<dd> The attempt to generate a new key was rejected.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> A revoked key was found, but no replacement could be obtained.</p>
<dt><code>ENOKEY</code></p>
<dd> No matching key was found.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to create a key.</p>
<dt><code>EPERM</code></p>
<dd> The <i>type</i> argument started with a period (&#8216;.&#8217;).</dl>
<h2>VERSIONS</h2>
<p> This system call first appeared in Linux 2.6.10. The ability to instantiate keys upon request was added in Linux 2.6.13.</p>
<h2>CONFORMING TO</h2>
<p> This system call is a nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> No wrapper for this system call is provided in glibc. A wrapper is provided in the <i>libkeyutils</i> package. When employing the wrapper in that library, link with <i>-lkeyutils</i>.</p>
<h2>EXAMPLES</h2>
<p> The program below demonstrates the use of <code>request_key</code>(). The <i>type</i>, <i>description</i>, and <i>callout_info</i> arguments for the system call are taken from the values supplied in the command-line arguments. The call specifies the session keyring as the target keyring. </p>
<p> In order to demonstrate this program, we first create a suitable entry in the file <i>/etc/request-key.conf</i>. </p>
<p> $ sudo sh # <code>echo &#8216;create user mtk:* * /bin/keyctl instantiate %k %c %S&#8217; \</code><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<code>&gt;&nbsp;/etc/request-key.conf</code> # <code>exit</code> </p>
<p> This entry specifies that when a new &quot;user&quot; key with the prefix &quot;mtk:&quot; must be instantiated, that task should be performed via the <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1) command&#8217;s <code>instantiate</code> operation. The arguments supplied to the <code>instantiate</code> operation are: the ID of the uninstantiated key (<i>%k</i>); the callout data supplied to the <code>request_key</code>() call (<i>%c</i>); and the session keyring (<i>%S</i>) of the requestor (i.e., the caller of <code>request_key</code>()). See <code><a href="/docs/linux/man/5-request-key-conf/">request-key.conf</a></code>(5) for details of these <i>%</i> specifiers. </p>
<p> Then we run the program and check the contents of <i>/proc/keys</i> to verify that the requested key has been instantiated: </p>
<p> $ <code>./t_request_key user mtk:key1 &quot;Payload data&quot;</code> $ <code>grep &#8216;2dddaf50&#8217; /proc/keys</code> 2dddaf50 I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 user mtk:key1: 12 </p>
<p> For another example of the use of this program, see <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2).</p>
<h3>Program source</h3>
<p> /* t_request_key.c */ </p>
<p> #include &lt;sys/types.h&gt; #include &lt;keyutils.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_serial_t key; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s type description callout-data
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key&nbsp;=&nbsp;request_key(argv[1], argv[2], argv[3],<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;KEY_SPEC_SESSION_KEYRING);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(key&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;request_key&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Key ID is&nbsp;%jx
&quot;,&nbsp;(uintmax_t)&nbsp;key); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-capabilities/">capabilities</a></code>(7), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-keyutils/">keyutils</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7), <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<p> The kernel source files <i>Documentation/security/keys/core.rst</i> and <i>Documentation/keys/request-key.rst</i> (or, before Linux 4.13, in the files <i>Documentation/security/keys.txt</i> and <i>Documentation/security/keys-request-key.txt</i>).</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
