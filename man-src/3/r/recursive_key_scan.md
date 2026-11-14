---
title: "recursive_key_scan(3)"
name: "recursive_key_scan"
section: "3"
letter: "r"
url: "/docs/linux/man/3-recursive_key_scan/"
description: "recursive_key_scan – Apply a function to all keys in a keyring tree recursive_session_key_scan – Apply a function to all keys in the session keyring tree"
---

<p>recursive_key_scan &#8211; Apply a function to all keys in a keyring tree<br />
 recursive_session_key_scan &#8211; Apply a function to all keys in the session keyring tree</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;keyutils.h&gt;

typedef int (*recursive_key_scanner_t)(key_serial_t parent,
                                       key_serial_t key, char *desc, int desc_len, void *data);

long recursive_key_scan(key_serial_t keyring,
                        recursive_key_scanner_t func, void *data);

long recursive_session_key_scan(recursive_key_scanner_t func,
                                void *data);</code></pre>
<h2>Description</h2>
<p><code>recursive_key_scan</code>() performs a depth-first recursive scan of the specified <i>keyring</i> tree and applies <i>func</i> to every link found in the accessible keyrings in that tree. <i>data</i> is passed to each invocation of func. </p>
<p> The return values of <i>func</i> are summed and returned as the overall return value. Errors are ignored. Inaccessible keyrings are not scanned, but links to them are still passed to func. </p>
<p> <code>recursive_session_key_scan</code>() works exactly like <i>recursive_key_scan</i>() with the caller&#8217;s session keyring specified as the starting keyring. </p>
<p> The callback function is called for each link found in all the keyrings in the nominated tree and so may be called multiple times for a particular key if that key has multiple links to it. </p>
<p> The callback function is passed the following parameters:</p>
<dl>
<dt><code>parent</code></p>
<dd>The keyring containing the link or 0 for the initial key.</p>
<dt><code>key</code></p>
<dd>The key to which the link points.</p>
<dt><code>desc</code> and <code>desc_len</code></p>
<dd>A pointer to the raw description and its length as retrieved with <i>keyctl_describe_alloc</i>(). These will be NULL and -1 respectively if the description couldn&#8217;t be retrieved and errno will retain the error from <i>keyctl_describe_alloc</i>().</p>
<dt><code>data</code></p>
<dd>The data passed to the scanner function.</dl>
<h2>Return Value</h2>
<p>These functions return the sum of the results of the callback functions they invoke.</p>
<h2>Errors</h2>
<p>Ignored.</p>
<h2>Linking</h2>
<p>When linking, <code>-lkeyutils</code> should be specified to the linker.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-keyctl/">keyctl</a></code>(3), <code><a href="/docs/linux/man/3-keyctl_describe_alloc/">keyctl_describe_alloc</a></code>(3) </p>
