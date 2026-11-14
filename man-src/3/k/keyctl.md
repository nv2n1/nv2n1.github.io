---
title: "keyctl(3)"
name: "keyctl"
section: "3"
letter: "k"
url: "/docs/linux/man/3-keyctl/"
description: "keyctl_*() – Key management function wrappers"
---

<h2 class="name">NAME</h2>
<p> keyctl_*() &#8211; Key management function wrappers </p>
<h2>DESCRIPTION</h2>
<p> The <code>keyctl</code>() system call is a multiplexor for a number of key management functions. These should be called via the wrappers in the libkeyutils library. </p>
<p> The functions can be compiled in by including the keyutils header file: </p>
<dl>
<dt>
<dd>
<pre>
<code>#include &lt;keyutils.h&gt;</code>
</dl>
and then telling the linker it should link in the library:
<dl><dt><dd><code>-lkeyutils</code>
</dl>
</pre>
<h2>KEYCTL FUNCTIONS</h2>
<p> <code><a href="/docs/linux/man/3-keyctl_assume_authority/">keyctl_assume_authority</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_clear/">keyctl_clear</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_describe/">keyctl_describe</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_describe_alloc/">keyctl_describe_alloc</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_get_keyring_id/">keyctl_get_keyring_ID</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_instantiate/">keyctl_instantiate</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_instantiate_iov/">keyctl_instantiate_iov</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_invalidate/">keyctl_invalidate</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_join_session_keyring/">keyctl_join_session_keyring</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_link/">keyctl_link</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_negate/">keyctl_negate</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_read/">keyctl_read</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_read_alloc/">keyctl_read_alloc</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_reject/">keyctl_reject</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_revoke/">keyctl_revoke</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_search/">keyctl_search</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_security/">keyctl_security</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_security_alloc/">keyctl_security_alloc</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_session_to_parent/">keyctl_session_to_parent</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_set_reqkey_keyring/">keyctl_set_reqkey_keyring</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_set_timeout/">keyctl_set_timeout</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_setperm/">keyctl_setperm</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_unlink/">keyctl_unlink</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-keyctl_update/">keyctl_update</a></code>(3)</p>
<h2>UTILITY FUNCTIONS</h2>
<p> <code><a href="/docs/linux/man/3-find_key_by_type_and_name/">find_key_by_type_and_name</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-recursive_key_scan/">recursive_key_scan</a></code>(3)<br />
 <code><a href="/docs/linux/man/3-recursive_session_key_scan/">recursive_session_key_scan</a></code>(3)</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-keyctl/">keyctl</a></code>(1),<br />
 <code><a href="/docs/linux/man/2-add_key/">add_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-keyctl/">keyctl</a></code>(2),<br />
 <code><a href="/docs/linux/man/2-request_key/">request_key</a></code>(2),<br />
 <code><a href="/docs/linux/man/8-request-key/">request-key</a></code>(8) </p>
<h2>Index</h2>
