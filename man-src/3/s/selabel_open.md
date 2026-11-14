---
title: "selabel_open(3)"
name: "selabel_open"
section: "3"
letter: "s"
url: "/docs/linux/man/3-selabel_open/"
description: "selabel_open, selabel_close – userspace SELinux labeling interface"
---

<p>selabel_open, selabel_close &#8211; userspace SELinux labeling interface</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;selinux/selinux.h&gt;

#include &lt;selinux/label.h&gt;
struct selabel_handle *selabel_open(int backend,

                                    const struct selinux_opt *options,

                                    unsigned nopt);
void selabel_close(struct selabel_handle *hnd);</code></pre>
<h2>Description</h2>
<p><code>selabel_open</code>() is used to initialize a labeling handle to be used for lookup operations. The <i>backend</i> argument specifies which backend is to be opened; the list of current backends appears in <code>BACKENDS</code> below. The <i>options</i> argument should be NULL or a pointer to an array of <code>selinux_opt</code> structures of length <i>nopt</i>: </p>
<pre><code>struct selinux_opt {
    int type;
    const char *value;
};</code></pre>
<p> The available option types are described in <code>GLOBAL OPTIONS</code> below as well as in the documentation for each individual backend. The return value on success is a non-NULL value for use in subsequent label operations. <code>selabel_close</code>() terminates use of a handle, freeing any internal resources associated with it. After this call has been made, the handle must not be used again.</p>
<h2>Global Options</h2>
<p>Global options which may be passed to <code>selabel_open</code>() include the following:</p>
<dl>
<dt><code>SELABEL_OPT_UNUSED</code></p>
<dd>The option with a type code of zero is a no-op. Thus an array of options may be initizalized to zero and any untouched elements will not cause an error.</p>
<dt><code>SELABEL_OPT_VALIDATE</code></p>
<dd>A non-null value for this option enables context validation. By default, <code><a href="/docs/linux/man/3-security_check_context/">security_check_context</a></code>(3) is used; a custom validation function can be provided via <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3). Note that an invalid context may not be treated as an error unless it is actually encountered during a lookup operation.</p>
<dt><code>SELABEL_OPT_DIGEST</code></p>
<dd>A non-null value for this option enables the generation of an SHA1 digest of the spec files loaded as described in <code><a href="/docs/linux/man/3-selabel_digest/">selabel_digest</a></code>(3)</dl>
<h2>Backends</h2>
<dl>
<dt><code>SELABEL_CTX_FILE</code></p>
<dd>File contexts backend, described in <code><a href="/docs/linux/man/5-selabel_file/">selabel_file</a></code>(5).</p>
<dt><code>SELABEL_CTX_MEDIA</code></p>
<dd>Media contexts backend, described in <code><a href="/docs/linux/man/5-selabel_media/">selabel_media</a></code>(5).</p>
<dt><code>SELABEL_CTX_X</code></p>
<dd>X Windows contexts backend, described in <code><a href="/docs/linux/man/5-selabel_x/">selabel_x</a></code>(5).</p>
<dt><code>SELABEL_CTX_DB</code></p>
<dd>Database objects contexts backend, described in <code><a href="/docs/linux/man/5-selabel_db/">selabel_db</a></code>(5).</dl>
<h2>Return Value</h2>
<p>A non-NULL handle value is returned on success. On error, NULL is returned and <i>errno</i> is set appropriately.</p>
<h2>Author</h2>
<p>Eamon Walsh &lt;ewalsh [at] tycho.nsa.gov&gt;</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-selabel_lookup/">selabel_lookup</a></code>(3), <code><a href="/docs/linux/man/3-selabel_stats/">selabel_stats</a></code>(3), <code><a href="/docs/linux/man/3-selinux_set_callback/">selinux_set_callback</a></code>(3), <code><a href="/docs/linux/man/8-selinux/">selinux</a></code>(8) </p>
