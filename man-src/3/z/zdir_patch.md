---
title: "zdir_patch(3)"
name: "zdir_patch"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdir_patch/"
description: "zdir_patch – work with directory patches"
---

<p>zdir_patch &#8211; work with directory patches</p>
<h2>Synopsis</h2>
<pre><code>typedef enum {
    ZDIR_PATCH_CREATE = 1,
    ZDIR_PATCH_DELETE = 2
} zdir_patch_op_t;

//  Create new patch
CZMQ_EXPORT zdir_patch_t *
zdir_patch_new(const char *path, zfile_t *file, zdir_patch_op_t op, const char *alias);

//  Destroy a patch
CZMQ_EXPORT void
zdir_patch_destroy(zdir_patch_t **self_p);

//  Create copy of a patch. If the patch is null, or memory was exhausted,
//  returns null.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zdir_patch_t *
zdir_patch_dup(zdir_patch_t *self);

//  Return patch file directory path
CZMQ_EXPORT const char *
zdir_patch_path(zdir_patch_t *self);

//  Return patch file item
CZMQ_EXPORT zfile_t *
zdir_patch_file(zdir_patch_t *self);

//  Return operation
CZMQ_EXPORT zdir_patch_op_t
zdir_patch_op(zdir_patch_t *self);

//  Return patch virtual file path
CZMQ_EXPORT const char *
zdir_patch_vpath(zdir_patch_t *self);

//  Calculate hash digest for file (create only)
CZMQ_EXPORT void
zdir_patch_digest_set(zdir_patch_t *self);

//  Return hash digest for patch file
CZMQ_EXPORT const char *
zdir_patch_digest(zdir_patch_t *self);

//  Self test of this class.
CZMQ_EXPORT void
zdir_patch_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zdir_patch class works with one patch, which says &quot;create this file&quot; or &quot;delete this file&quot; (referring to a zfile item each time). </p>
<p> Please add @discuss section in ../src/zdir_patch.c.</p>
<h2>Example</h2>
<p><code>From zdir_patch_test method</code>. </p>
<pre><code>zfile_t *file = zfile_new (&quot;.&quot;, &quot;bilbo&quot;);
assert (file);
zdir_patch_t *patch = zdir_patch_new (&quot;.&quot;, file, patch_create, &quot;/&quot;);
assert (patch);
zfile_destroy (&amp;file);

file = zdir_patch_file (patch);
assert (file);
assert (streq (zfile_filename (file, &quot;.&quot;), &quot;bilbo&quot;));
assert (streq (zdir_patch_vpath (patch), &quot;/bilbo&quot;));
zdir_patch_destroy (&amp;patch);
</code></pre>
<h2>Authors</h2>
<p>The czmq manual was written by the authors in the AUTHORS file.</p>
<h2>Resources</h2>
<p>Main web site: m[blue]m[] </p>
<p> Report bugs to the email &lt;m[blue]<code>zeromq-dev [at] lists.zeromq.org</code>m[]<font SIZE="-2">[1]</font>&gt;</p>
<h2>Copyright</h2>
<p>Copyright (c) 1991-2012 iMatix Corporation &#8212; <a rel="nofollow" href="http://www.imatix.com">http://www.imatix.com</a> Copyright other contributors as noted in the AUTHORS file. This file is part of CZMQ, the high-level C binding for 0MQ: <a href="http://czmq.zeromq.org">http://czmq.zeromq.org</a> This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at <a href="http://mozilla.org/MPL/2.0/.">http://mozilla.org/MPL/2.0/.</a> LICENSE included with the czmq distribution.</p>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd>zeromq-dev [at] lists.zeromq.org</p>
<dl>
<dd>mailto:zeromq-dev [at] lists.zeromq.org</dl>
