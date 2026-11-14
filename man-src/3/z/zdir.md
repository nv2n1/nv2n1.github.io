---
title: "zdir(3)"
name: "zdir"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zdir/"
description: "zdir – work with file-system directories"
---

<p>zdir &#8211; work with file-system directories</p>
<h2>Synopsis</h2>
<pre><code>//  Create a new directory item that loads in the full tree of the specified
//  path, optionally located under some parent path. If parent is &quot;-&quot;, then
//  loads only the top-level directory, and does not use parent as a path.
CZMQ_EXPORT zdir_t *
zdir_new(const char *path, const char *parent);

//  Destroy a directory tree and all children it contains.
CZMQ_EXPORT void
zdir_destroy(zdir_t **self_p);

//  Return directory path
CZMQ_EXPORT const char *
zdir_path(zdir_t *self);

//  Return last modification time for directory.
CZMQ_EXPORT time_t
zdir_modified(zdir_t *self);

//  Return total hierarchy size, in bytes of data contained in all files
//  in the directory tree.
CZMQ_EXPORT off_t
zdir_cursize(zdir_t *self);

//  Return directory count
CZMQ_EXPORT size_t
zdir_count(zdir_t *self);

//  Returns a sorted list of zfile objects; Each entry in the list is a pointer
//  to a zfile_t item already allocated in the zdir tree. Do not destroy the
//  original zdir tree until you are done with this list.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlist_t *
zdir_list(zdir_t *self);

//  Remove directory, optionally including all files that it contains, at
//  all levels. If force is false, will only remove the directory if empty.
//  If force is true, will remove all files and all subdirectories.
CZMQ_EXPORT void
zdir_remove(zdir_t *self, bool force);

//  Calculate differences between two versions of a directory tree.
//  Returns a list of zdir_patch_t patches. Either older or newer may
//  be null, indicating the directory is empty/absent. If alias is set,
//  generates virtual filename (minus path, plus alias).
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlist_t *
zdir_diff(zdir_t *older, zdir_t *newer, const char *alias);

//  Return full contents of directory as a zdir_patch list.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zlist_t *
zdir_resync(zdir_t *self, const char *alias);

//  Load directory cache; returns a hash table containing the SHA-1 digests
//  of every file in the tree. The cache is saved between runs in .cache.
//  The caller is responsible for destroying the return value when finished with it.
CZMQ_EXPORT zhash_t *
zdir_cache(zdir_t *self);

//  Print contents of directory to open stream
CZMQ_EXPORT void
zdir_fprint(zdir_t *self, FILE *file, int indent);

//  Print contents of directory to stdout
CZMQ_EXPORT void
zdir_print(zdir_t *self, int indent);

//  Create a new zdir_watch actor instance:
//
//      zactor_t *watch = zactor_new (zdir_watch, NULL);
//
//  Destroy zdir_watch instance:
//
//      zactor_destroy (&amp;watch);
//
//  Enable verbose logging of commands and activity:
//
//      zstr_send (watch, &quot;VERBOSE&quot;);
//
//  Subscribe to changes to a directory path:
//
//      zsock_send (watch, &quot;ss&quot;, &quot;SUBSCRIBE&quot;, &quot;directory_path&quot;);
//
//  Unsubscribe from changes to a directory path:
//
//      zsock_send (watch, &quot;ss&quot;, &quot;UNSUBSCRIBE&quot;, &quot;directory_path&quot;);
//
//  Receive directory changes:
//      zsock_recv (watch, &quot;sp&quot;, &amp;path, &amp;patches);
//
//      // Delete the received data.
//      free (path);
//      zlist_destroy (&amp;patches);
CZMQ_EXPORT void
zdir_watch(zsock_t *pipe, void *unused);

//  Self test of this class.
CZMQ_EXPORT void
zdir_test(bool verbose);</code></pre>
<h2>Description</h2>
<p>The zdir class gives access to the file system index. It will load a directory tree (a directory plus all child directories) into a zdir structure and then let you navigate that structure. It exists mainly to wrap non-portable OS functions to do this. </p>
<p> Please add @discuss section in ../src/zdir.c.</p>
<h2>Example</h2>
<p><code>From zdir_test method</code>. </p>
<pre><code>zdir_t *older = zdir_new(&quot;.&quot;, NULL);
assert(older);
if (verbose) {
    printf(&quot;
&quot;);
    zdir_dump(older, 0);
}
zdir_t *newer = zdir_new(&quot;..&quot;, NULL);
assert(newer);
zlist_t *patches = zdir_diff(older, newer, &quot;/&quot;);
assert(patches);
while (zlist_size(patches)) {
    zdir_patch_t *patch = (zdir_patch_t *)zlist_pop(patches);
    zdir_patch_destroy(&amp;patch);
}
zlist_destroy(&amp;patches);
zdir_destroy(&amp;older);
zdir_destroy(&amp;newer);

zdir_t *nosuch = zdir_new(&quot;does-not-exist&quot;, NULL);
assert(nosuch == NULL);

// zdir_watch test:
zactor_t *watch = zactor_new(zdir_watch, NULL);
assert(watch);

if (verbose) {
    zsock_send(watch, &quot;s&quot;, &quot;VERBOSE&quot;);
    assert(zsock_wait(watch) == 0);
}

// need to create a file in the test directory we're watching
// in order to ensure the directory exists
zfile_t *initfile = zfile_new(&quot;./zdir-test-dir&quot;, &quot;initial_file&quot;);
assert(initfile);
zfile_output(initfile);
fprintf(zfile_handle(initfile), &quot;initial file
&quot;);
zfile_close(initfile);
zfile_destroy(&amp;initfile);

zclock_sleep(1001); // wait for initial file to become 'stable'

zsock_send(watch, &quot;si&quot;, &quot;TIMEOUT&quot;, 100);
assert(zsock_wait(watch) == 0);

zsock_send(watch, &quot;ss&quot;, &quot;SUBSCRIBE&quot;, &quot;zdir-test-dir&quot;);
assert(zsock_wait(watch) == 0);

zsock_send(watch, &quot;ss&quot;, &quot;UNSUBSCRIBE&quot;, &quot;zdir-test-dir&quot;);
assert(zsock_wait(watch) == 0);

zsock_send(watch, &quot;ss&quot;, &quot;SUBSCRIBE&quot;, &quot;zdir-test-dir&quot;);
assert(zsock_wait(watch) == 0);

zfile_t *newfile = zfile_new(&quot;zdir-test-dir&quot;, &quot;test_abc&quot;);
zfile_output(newfile);
fprintf(zfile_handle(newfile), &quot;test file
&quot;);
zfile_close(newfile);

zpoller_t *watch_poll = zpoller_new(watch, NULL);

// poll for a certain timeout before giving up and failing the test.
assert(zpoller_wait(watch_poll, 1001) == watch);

// wait for notification of the file being added
char *path;
int rc = zsock_recv(watch, &quot;sp&quot;, &amp;path, &amp;patches);
assert(rc == 0);

assert(streq(path, &quot;zdir-test-dir&quot;));
free(path);

assert(zlist_size(patches) == 1);

zdir_patch_t *patch = (zdir_patch_t *)zlist_pop(patches);
assert(streq(zdir_patch_path(patch), &quot;zdir-test-dir&quot;));

zfile_t *patch_file = zdir_patch_file(patch);
assert(streq(zfile_filename(patch_file, &quot;&quot;), &quot;zdir-test-dir/test_abc&quot;));

zdir_patch_destroy(&amp;patch);
zlist_destroy(&amp;patches);

// remove the file
zfile_remove(newfile);
zfile_destroy(&amp;newfile);

// poll for a certain timeout before giving up and failing the test.
assert(zpoller_wait(watch_poll, 1001) == watch);

// wait for notification of the file being removed
rc = zsock_recv(watch, &quot;sp&quot;, &amp;path, &amp;patches);
assert(rc == 0);

assert(streq(path, &quot;zdir-test-dir&quot;));
free(path);

assert(zlist_size(patches) == 1);

patch = (zdir_patch_t *)zlist_pop(patches);
assert(streq(zdir_patch_path(patch), &quot;zdir-test-dir&quot;));

patch_file = zdir_patch_file(patch);
assert(streq(zfile_filename(patch_file, &quot;&quot;), &quot;zdir-test-dir/test_abc&quot;));

zdir_patch_destroy(&amp;patch);
zlist_destroy(&amp;patches);

zpoller_destroy(&amp;watch_poll);
zactor_destroy(&amp;watch);

// clean up by removing the test directory.
zdir_t *testdir = zdir_new(&quot;zdir-test-dir&quot;, NULL);
zdir_remove(testdir, true);
zdir_destroy(&amp;testdir);
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
