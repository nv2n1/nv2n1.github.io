---
title: "keyctl_instantiate(3)"
name: "keyctl_instantiate"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl_instantiate/"
description: "keyctl_assume_authority – Assume the authority to instantiate a key keyctl_instantiate – Instantiate a key from flat data keyctl_instantiate_iov – Instantiate a key from segmented data keyctl_rejec..."
---

<h2 class="name">NAME</h2>
<p> keyctl_assume_authority &#8211; Assume the authority to instantiate a key<br />
 keyctl_instantiate &#8211; Instantiate a key from flat data<br />
 keyctl_instantiate_iov &#8211; Instantiate a key from segmented data<br />
 keyctl_reject &#8211; Negatively instantiate a key specifying search error<br />
 keyctl_negate &#8211; Negatively instantiate a key </p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;keyutils.h&gt;
long keyctl_assume_authority(key_serial_t key);
long keyctl_instantiate(key_serial_t key, const void *payload,
                        size_t plen, key_serial_t keyring);
long keyctl_instantiate_iov(key_serial_t key,
                            const struct iovec *payload_iov, unsigned ioc,
                            key_serial_t keyring);
long keyctl_negate(key_serial_t key, unsigned timeout,
                   key_serial_t keyring);
long keyctl_reject(key_serial_t key, unsigned timeout,
                   unsigned error, key_serial_t keyring);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>keyctl_assume_authority</code>() assumes the authority for the calling thread to deal with and instantiate the specified uninstantiated <i>key</i>. </p>
<p> The calling thread must have the appopriate authorisation key resident in one of its keyrings for this to succeed, and that authority must not have been revoked. </p>
<p> The authorising key is allocated by request_key() when it needs to invoke userspace to generate a key for the requesting process. This is then attached to one of the keyrings of the userspace process to which the task of instantiating the key is given:</p>
<dl>
<dt>
<dd> requester -&gt; request_key() -&gt; instantiator</dl>
<p> Calling this function modifies the way <code>request_key</code>() works when called thereafter by the calling (instantiator) thread; once the authority is assumed, the keyrings of the initial process are added to the search path, using the initial process&#8217;s UID, GID, groups and security context. </p>
<p> If a thread has multiple instantiations to deal with, it may call this function to change the authorisation key currently in effect. Supplying a <code>zero</code> <i>key</i> de-assumes the currently assumed authority. </p>
<p> <code>NOTE!</code> This is a per-thread setting and not a per-process setting so that a multithreaded process can be used to instantiate several keys at once. </p>
<p> <code>keyctl_instantiate</code>() instantiates the payload of an uninstantiated key from the data specified. <i>payload</i> and <i>plen</i> specify the data for the new payload. <i>payload</i> may be NULL and <i>plen</i> may be zero if the key type permits that. The key type may reject the data if it&#8217;s in the wrong format or in some other way invalid. </p>
<p> <code>keyctl_instantiate_iov</code>() is similar, but the data is passed in an array of iovec structs instead of in a flat buffer. <i>payload_iov</i> points to the base of the array and <i>ioc</i> indicates how many elements there are. <i>payload_iov</i> may be NULL or <i>ioc</i> may be zero to indicate that no data is being supplied. </p>
<p> <code>keyctl_reject</code>() marks a key as negatively instantiated and sets the expiration timer on it. <i>timeout</i> specifies the lifetime of the key in seconds. <i>error</i> specifies the error to be returned when a search hits the key (this is typically <i>EKEYREJECTED</i>, <i>EKEYREVOKED</i> or <i>EKEYEXPIRED</i>). Note that keyctl_reject() falls back to keyctl_negate() if the kernel does not support it. </p>
<p> <code>keyctl_negate</code>() as <i>keyctl_reject</i>() with an error code of <i>ENOKEY</i><code>.</code> </p>
<p> Only a key for which authority has been assumed may be instantiated or negatively instantiated, and once instantiated, the authorisation key will be revoked and the requesting process will be able to resume. </p>
<p> The destination <i>keyring</i>, if given, is assumed to belong to the initial requester, and not the instantiating process. Therefore, the special keyring IDs refer to the requesting process&#8217;s keyrings, not the caller&#8217;s, and the requester&#8217;s UID, etc. will be used to access them. </p>
<p> The destination keyring can be <code>zero</code> if no extra link is desired. </p>
<p> The requester, not the caller, must have <code>write</code> permission on the destination for a link to be made there.</p>
<h2>RETURN VALUE</h2>
<p> On success <code>keyctl_instantiate</code>() returns <code>0</code>. On error, the value <code>-1</code> will be returned and errno will have been set to an appropriate error.</p>
<h2>ERRORS</h2>
<dl>
<dt><code>ENOKEY</code></p>
<dd> The key or keyring specified is invalid.</p>
<dt><code>EKEYEXPIRED</code></p>
<dd> The keyring specified has expired.</p>
<dt><code>EKEYREVOKED</code></p>
<dd> The key or keyring specified had been revoked, or the authorisation has been revoked.</p>
<dt><code>EINVAL</code></p>
<dd> The payload data was invalid.</p>
<dt><code>ENOMEM</code></p>
<dd> Insufficient memory to store the new payload or to expand the destination keyring.</p>
<dt><code>EDQUOT</code></p>
<dd> The key quota for the key&#8217;s user would be exceeded by increasing the size of the key to accommodate the new payload or the key quota for the keyring&#8217;s user would be exceeded by expanding the destination keyring.</p>
<dt><code>EACCES</code></p>
<dd> The key exists, but is not <code>writable</code> by the requester.</dl>
<h2>LINKING</h2>
<p> This is a library function that can be found in <i>libkeyutils</i>. When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<h2>Index</h2>
