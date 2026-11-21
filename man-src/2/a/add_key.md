---
title: "add_key(2)"
name: "add_key"
section: "2"
letter: "a"
url: "/docs/linux/man/2-add_key/"
description: "add_key – add a key to the kernel’s key management facility"
---

<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
#include &lt;sys/types.h&gt;
key_serial_t add_key(const char *type, const char *description,
                     const void *payload, size_t plen,
                     key_serial_t keyring);
</code></pre>
<p> No glibc wrapper is provided for this system call; see NOTES.</p>
<h2>DESCRIPTION</h2>
<p> <code>add_key</code>() creates or updates a key of the given <i>type</i> and <i>description</i>, instantiates it with the <i>payload</i> of length <i>plen</i>, attaches it to the nominated <i>keyring</i>, and returns the key&#8217;s serial number. </p>
<p> The key may be rejected if the provided data is in the wrong format or it is invalid in some other way. </p>
<p> If the destination <i>keyring</i> already contains a key that matches the specified <i>type</i> and <i>description</i>, then, if the key type supports it, that key will be updated rather than a new key being created; if not, a new key (with a different ID) will be created and it will displace the link to the extant key from the keyring. </p>
<p> The destination <i>keyring</i> serial number may be that of a valid keyring for which the caller has <i>write</i> permission. Alternatively, it may be one of the following special keyring IDs:</p>
<dl>
<dt><code>KEY_SPEC_THREAD_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s thread-specific keyring (<code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7)).</dd>
<dt><code>KEY_SPEC_PROCESS_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s process-specific keyring (<code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7)).</dd>
<dt><code>KEY_SPEC_SESSION_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s session-specific keyring (<code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7)).</dd>
<dt><code>KEY_SPEC_USER_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s UID-specific keyring (<code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7)).</dd>
<dt><code>KEY_SPEC_USER_SESSION_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s UID-session keyring (<code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7)).</dd></dl>
<h3>Key types</h3>
<p> The key <i>type</i> is a string that specifies the key&#8217;s type. Internally, the kernel defines a number of key types that are available in the core key management code. Among the types that are available for user-space use and can be specified as the <i>type</i> argument to <code>add_key</code>() are the following:</p>
<dl>
<dt><i>keyring</i></dt>
<dd> Keyrings are special key types that may contain links to sequences of other keys of any type. If this interface is used to create a keyring, then <i>payload</i> should be NULL and <i>plen</i> should be zero.</dd>
<dt><i>&quot;user&quot;</i></dt>
<dd> This is a general purpose key type whose payload may be read and updated by user-space applications. The key is kept entirely within kernel memory. The payload for keys of this type is a blob of arbitrary data of up to 32,767 bytes.</dd>
<dt><i>&quot;logon&quot;</i> (since Linux 3.3)</dt>
<dd> This key type is essentially the same as <i>&quot;user&quot;</i>, but it does not permit the key to read. This is suitable for storing payloads that you do not want to be readable from user space.</dd></dl>
<p> This key type vets the <i>description</i> to ensure that it is qualified by a &quot;service&quot; prefix, by checking to ensure that the <i>description</i> contains a &#8216;:&#8217; that is preceded by other characters.</p>
<dl>
<dt><i>&quot;big_key&quot;</i> (since Linux 3.13)</dt>
<dd> This key type is similar to <i>&quot;user&quot;</i>, but may hold a payload of up to 1 MiB. If the key payload is large enough, then it may be stored encrypted in tmpfs (which can be swapped out) rather than kernel memory.</dd></dl>
<p> For further details on these key types, see <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7).</p>
<h2>RETURN VALUE</h2>
<p> On success, <code>add_key</code>() returns the serial number of the key it created or updated. On error, -1 is returned and <i>errno</i> is set to indicate the cause of the error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>EACCES</code></dt>
<dd> The keyring wasn&#8217;t available for modification by the user.</dd>
<dt><code>EDQUOT</code></dt>
<dd> The key quota for this user would be exceeded by creating this key or linking it to the keyring.</dd>
<dt><code>EFAULT</code></dt>
<dd> One or more of <i>type</i>, <i>description</i>, and <i>payload</i> points outside process&#8217;s accessible address space.</dd>
<dt><code>EINVAL</code></dt>
<dd> The size of the string (including the terminating null byte) specified in <i>type</i> or <i>description</i> exceeded the limit (32 bytes and 4096 bytes respectively).</dd>
<dt><code>EINVAL</code></dt>
<dd> The payload data was invalid.</dd>
<dt><code>EINVAL</code></dt>
<dd> <i>type</i> was <i>&quot;logon&quot;</i> and the <i>description</i> was not qualified with a prefix string of the form <i>&quot;service:&quot;</i>.</dd>
<dt><code>EKEYEXPIRED</code></dt>
<dd> The keyring has expired.</dd>
<dt><code>EKEYREVOKED</code></dt>
<dd> The keyring has been revoked.</dd>
<dt><code>ENOKEY</code></dt>
<dd> The keyring doesn&#8217;t exist.</dd>
<dt><code>ENOMEM</code></dt>
<dd> Insufficient memory to create a key.</dd>
<dt><code>EPERM</code></dt>
<dd> The <i>type</i> started with a period (&#8216;.&#8217;). Key types that begin with a period are reserved to the implementation.</dd>
<dt><code>EPERM</code></dt>
<dd> <i>type</i> was <i>keyring</i> and the <i>description</i> started with a period (&#8216;.&#8217;). Keyrings with descriptions (names) that begin with a period are reserved to the implementation.</dd></dl>
<h2>VERSIONS</h2>
<p> This system call first appeared in Linux 2.6.10.</p>
<h2>CONFORMING TO</h2>
<p> This system call is a nonstandard Linux extension.</p>
<h2>NOTES</h2>
<p> No wrapper for this system call is provided in glibc. A wrapper is provided in the <i>libkeyutils</i> package. When employing the wrapper in that library, link with <i>-lkeyutils</i>.</p>
<h2>EXAMPLES</h2>
<p> The program below creates a key with the type, description, and payload specified in its command-line arguments, and links that key into the session keyring. The following shell session demonstrates the use of the program: </p>
<p> $ <code>./a.out user mykey &quot;Some payload&quot;</code> Key ID is 64a4dca $ <code>grep &#8217;64a4dca&#8217; /proc/keys</code> 064a4dca I&#8211;Q&#8212; 1 perm 3f010000 1000 1000 user mykey: 12</p>
<h3>Program source</h3>
<p> #include &lt;sys/types.h&gt; #include &lt;keyutils.h&gt; #include &lt;stdint.h&gt; #include &lt;stdio.h&gt; #include &lt;stdlib.h&gt; #include &lt;string.h&gt; </p>
<p> int main(int argc, char *argv[]) {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key_serial_t key; </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(argc&nbsp;!=&nbsp;4)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;fprintf(stderr,&nbsp;&quot;Usage:&nbsp;%s type description payload
&quot;,<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;argv[0]);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;key&nbsp;=&nbsp;add_key(argv[1], argv[2], argv[3], strlen(argv[3]),<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;KEY_SPEC_SESSION_KEYRING);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;if&nbsp;(key&nbsp;==&nbsp;-1)&nbsp;{<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;perror(&quot;add_key&quot;);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_FAILURE);<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;} </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;printf(&quot;Key ID is&nbsp;%jx
&quot;,&nbsp;(uintmax_t)&nbsp;key); </p>
<p>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;exit(EXIT_SUCCESS); }</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1), <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2), <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2), <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/7-keyrings/">keyrings</a></code>(7), <code><a href="/docs/linux/man/7-keyutils/">keyutils</a></code>(7), <code><a href="/docs/linux/man/7-persistent-keyring/">persistent-keyring</a></code>(7), <code><a href="/docs/linux/man/7-process-keyring/">process-keyring</a></code>(7), <code><a href="/docs/linux/man/7-session-keyring/">session-keyring</a></code>(7), <code><a href="/docs/linux/man/7-thread-keyring/">thread-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-keyring/">user-keyring</a></code>(7), <code><a href="/docs/linux/man/7-user-session-keyring/">user-session-keyring</a></code>(7) </p>
<p> The kernel source files <i>Documentation/security/keys/core.rst</i> and <i>Documentation/keys/request-key.rst</i> (or, before Linux 4.13, in the files <i>Documentation/security/keys.txt</i> and <i>Documentation/security/keys-request-key.txt</i>).</p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
