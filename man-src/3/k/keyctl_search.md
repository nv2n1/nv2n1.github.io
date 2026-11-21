---

title: "keyctl_search(3)"
name: "keyctl_search"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_search/"
description: "keyctl_search – Search a keyring for a key"
---

<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_search(key_serial_t keyring, const char *type,
                   const char *description, key_serial_t destination);
</code></pre>
<p> <code>keyctl_search</code>() recursively searches the <i>keyring</i> for a key of the specified <i>type</i> and <i>description</i>. </p>
<p> If found, the key will be attached to the <i>destination</i> keyring (if given), and its serial number will be returned. </p>
<p> The source keyring must grant <code>search</code> permission to the caller, and for a key to be found, it must also grant <code>search</code> permission to the caller. Child keyrings will be only be recursively searched if they grant <code>search</code> permission to the caller as well. </p>
<p> If the destination keyring is <code>zero</code>, no attempt will be made to forge a link to the key, and just the serial number will be returned. </p>
<p> If the destination keyring is given, then the link may only be formed if the found key grants the caller <code>link</code> permission and the destination keyring grants the caller <code>write</code> permission. </p>
<p> If the search is successful, and if the destination keyring already contains a link to a key that matches the specified <i>type</i> and <i>description</i>, then that link will be replaced by a link to the found key. </p>
<p> The source keyring and destination keyring serial numbers may be those of valid keyrings to which the caller has appropriate permission, or they may be special keyring IDs:</p>
<dl>
<dt><code>KEY_SPEC_THREAD_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s thread-specific keyring.</dd>
<dt><code>KEY_SPEC_PROCESS_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s process-specific keyring.</dd>
<dt><code>KEY_SPEC_SESSION_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s session-specific keyring.</dd>
<dt><code>KEY_SPEC_USER_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s UID-specific keyring.</dd>
<dt><code>KEY_SPEC_USER_SESSION_KEYRING</code></dt>
<dd> This specifies the caller&#8217;s UID-session keyring.</dd></dl>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_search</code>() returns the serial number of the key it found. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></dt>
<dd> One of the keyrings doesn&#8217;t exist, no key was found by the search, or the only key found by the search was a negative key.</dd>
<dt><code>ENOTDIR</code></dt>
<dd> One of the keyrings is a valid key that isn&#8217;t a keyring.</dd>
<dt><code>EKEYEXPIRED</code></dt>
<dd> One of the keyrings has expired, or the only key found was expired.</dd>
<dt><code>EKEYREVOKED</code></dt>
<dd> One of the keyrings has been revoked, or the only key found was revoked.</dd>
<dt><code>ENOMEM</code></dt>
<dd> Insufficient memory to expand the destination keyring.</dd>
<dt><code>EDQUOT</code></dt>
<dd> The key quota for this user would be exceeded by creating a link to the found key in the destination keyring.</dd>
<dt><code>EACCES</code></dt>
<dd> The source keyring didn&#8217;t grant <code>search</code> permission, the destination keyring didn&#8217;t grant <code>write</code> permission or the found key didn&#8217;t grant <code>link</code> permission to the caller.</dd></dl>
<h2>LINKING</h2>
<p> Although this is a Linux system call, it is not present in <i>libc</i> but can be found rather in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
