---
title: "zconfig(3)"
name: "zconfig"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zconfig/"
description: "zconfig – work with config files written in rfc.zeromq.org/spec:4/ZPL."
---

<p>zconfig &#8211; work with config files written in rfc.zeromq.org/spec:4/ZPL.</p>
<h2>Synopsis</h2>
<pre>// Function that executes config
typedef int (zconfig_fct) (zconfig_t *self, void *arg, int level);
// Create new config item
CZMQ_EXPORT zconfig_t *
 zconfig_new (const char *name, zconfig_t *parent);
// Destroy a config item and all its children
CZMQ_EXPORT void
 zconfig_destroy (zconfig_t **self_p);
// Return name of config item
CZMQ_EXPORT char *
 zconfig_name (zconfig_t *self);
// Return value of config item
CZMQ_EXPORT char *
 zconfig_value (zconfig_t *self);
// Insert or update configuration key with value
CZMQ_EXPORT void
 zconfig_put (zconfig_t *self, const char *path, const char *value);
// Equivalent to zconfig_put, accepting a format specifier and variable
// argument list, instead of a single string value.
CZMQ_EXPORT void
 zconfig_putf (zconfig_t *self, const char *path, const char *format, ...);
// Get value for config item into a string value; leading slash is optional
// and ignored.
CZMQ_EXPORT char *
 zconfig_get (zconfig_t *self, const char *path, const char *default_value);
// Set config item name, name may be NULL
CZMQ_EXPORT void
 zconfig_set_name (zconfig_t *self, const char *name);
// Set new value for config item. The new value may be a string, a printf
// format, or NULL. Note that if string may possibly contain '%', or if it
// comes from an insecure source, you must use '%s' as the format, followed
// by the string.
CZMQ_EXPORT void
 zconfig_set_value (zconfig_t *self, const char *format, ...);
// Find our first child, if any
CZMQ_EXPORT zconfig_t *
 zconfig_child (zconfig_t *self);
// Find our first sibling, if any
CZMQ_EXPORT zconfig_t *
 zconfig_next (zconfig_t *self);
// Find a config item along a path; leading slash is optional and ignored.
CZMQ_EXPORT zconfig_t *
 zconfig_locate (zconfig_t *self, const char *path);
// Locate the last config item at a specified depth
CZMQ_EXPORT zconfig_t *
 zconfig_at_depth (zconfig_t *self, int level);
// Execute a callback for each config item in the tree; returns zero if
// successful, else -1.
CZMQ_EXPORT int
 zconfig_execute (zconfig_t *self, zconfig_fct handler, void *arg);
// Add comment to config item before saving to disk. You can add as many
// comment lines as you like. If you use a null format, all comments are
// deleted.
CZMQ_EXPORT void
 zconfig_set_comment (zconfig_t *self, const char *format, ...);
// Return comments of config item, as zlist.
CZMQ_EXPORT zlist_t *
 zconfig_comments (zconfig_t *self);
// Load a config tree from a specified ZPL text file; returns a zconfig_t
// reference for the root, if the file exists and is readable. Returns NULL
// if the file does not exist.
CZMQ_EXPORT zconfig_t *
 zconfig_load (const char *filename);
// Save a config tree to a specified ZPL text file, where a filename
// &quot;-&quot; means dump to standard output.
CZMQ_EXPORT int
 zconfig_save (zconfig_t *self, const char *filename);
// Equivalent to zconfig_load, taking a format string instead of a fixed
// filename.
CZMQ_EXPORT zconfig_t *
 zconfig_loadf (const char *format, ...);
// Equivalent to zconfig_save, taking a format string instead of a fixed
// filename.
CZMQ_EXPORT int
 zconfig_savef (zconfig_t *self, const char *format, ...);
// Report filename used during zconfig_load, or NULL if none
CZMQ_EXPORT const char *
 zconfig_filename (zconfig_t *self);
// Reload config tree from same file that it was previously loaded from.
// Returns 0 if OK, -1 if there was an error (and then does not change
// existing data).
CZMQ_EXPORT int
 zconfig_reload (zconfig_t **self_p);
// Load a config tree from a memory chunk
CZMQ_EXPORT zconfig_t *
 zconfig_chunk_load (zchunk_t *chunk);
// Save a config tree to a new memory chunk
CZMQ_EXPORT zchunk_t *
 zconfig_chunk_save (zconfig_t *self);
// Load a config tree from a null-terminated string
CZMQ_EXPORT zconfig_t *
 zconfig_str_load (const char *string);
// Save a config tree to a new null terminated string
CZMQ_EXPORT char *
 zconfig_str_save (zconfig_t *self);
// Return true if a configuration tree was loaded from a file and that
// file has changed in since the tree was loaded.
CZMQ_EXPORT bool
 zconfig_has_changed (zconfig_t *self);
// Print the config file to open stream
CZMQ_EXPORT void
 zconfig_fprint (zconfig_t *self, FILE *file);
// Print the config file to stdout
CZMQ_EXPORT void
 zconfig_print (zconfig_t *self);</pre>
<h2>Description</h2>
<p>Lets applications load, work with, and save configuration files. This implements rfc.zeromq.org/spec:4/ZPL, which is a simple structured text format for configuration files. </p>
<p> Here is an example ZPL stream and corresponding config structure: </p>
<dl>
<dd>
<pre>context
 iothreads = 1
 verbose = 1 # Ask for a trace
main
 type = zqueue # ZMQ_DEVICE type
 frontend
 option
 hwm = 1000
 swap = 25000000 # 25MB
 bind = '<a href="inproc://addr1'">inproc://addr1'</a>
 bind = '<a href="ipc://addr2'">ipc://addr2'</a>
 backend
 bind = <a href="inproc://addr3">inproc://addr3</a></pre>
</dl>
<dl>
<dd>
<pre>root Down = child
| Across = next
v
context--&gt;main
| |
| v
| type=queue--&gt;frontend--&gt;backend
| | |
| | v
| | bind=<a href="inproc://addr3">inproc://addr3</a>
| v
| option--&gt;bind=<a href="inproc://addr1--">inproc://addr1--</a>&gt;bind=<a href="ipc://addr2">ipc://addr2</a>
| |
| v
| hwm=1000--&gt;swap=25000000
v
iothreads=1--&gt;verbose=false</pre>
</dl>
<h2>Example</h2>
<p><code>From zconfig_test method</code>. </p>
<pre><code>//  Create temporary directory for test files
#define TESTDIR &quot;.test_zconfig&quot;
zsys_dir_create(TESTDIR);

zconfig_t *root = zconfig_new(&quot;root&quot;, NULL);
assert(root);
zconfig_t *section, *item;

section = zconfig_new(&quot;headers&quot;, root);
assert(section);
item = zconfig_new(&quot;email&quot;, section);
assert(item);
zconfig_set_value(item, &quot;some [at] random.com&quot;);
item = zconfig_new(&quot;name&quot;, section);
assert(item);
zconfig_set_value(item, &quot;Justin Kayce&quot;);
zconfig_putf(root, &quot;/curve/secret-key&quot;, &quot;%s&quot;, &quot;Top Secret&quot;);
zconfig_set_comment(root, &quot;   CURVE certificate&quot;);
zconfig_set_comment(root, &quot;   -----------------&quot;);
assert(zconfig_comments(root));
zconfig_save(root, TESTDIR &quot;/test.cfg&quot;);
zconfig_destroy(&amp;root);
root = zconfig_load(TESTDIR &quot;/test.cfg&quot;);
if (verbose)
    zconfig_save(root, &quot;-&quot;);
assert(streq(zconfig_filename(root), TESTDIR &quot;/test.cfg&quot;));

char *email = zconfig_get(root, &quot;/headers/email&quot;, NULL);
assert(email);
assert(streq(email, &quot;some [at] random.com&quot;));
char *passwd = zconfig_get(root, &quot;/curve/secret-key&quot;, NULL);
assert(passwd);
assert(streq(passwd, &quot;Top Secret&quot;));

zconfig_savef(root, &quot;%s/%s&quot;, TESTDIR, &quot;test.cfg&quot;);
assert(!zconfig_has_changed(root));
int rc = zconfig_reload(&amp;root);
assert(rc == 0);
assert(!zconfig_has_changed(root));
zconfig_destroy(&amp;root);

//  Test chunk load/save
root = zconfig_new(&quot;root&quot;, NULL);
assert(root);
section = zconfig_new(&quot;section&quot;, root);
assert(section);
item = zconfig_new(&quot;value&quot;, section);
assert(item);
zconfig_set_value(item, &quot;somevalue&quot;);
zconfig_t *search = zconfig_locate(root, &quot;section/value&quot;);
assert(search == item);
zchunk_t *chunk = zconfig_chunk_save(root);
assert(strlen((char *)zchunk_data(chunk)) == 32);
char *string = zconfig_str_save(root);
assert(string);
assert(streq(string, (char *)zchunk_data(chunk)));
free(string);
assert(chunk);
zconfig_destroy(&amp;root);

root = zconfig_chunk_load(chunk);
assert(root);
char *value = zconfig_get(root, &quot;/section/value&quot;, NULL);
assert(value);
assert(streq(value, &quot;somevalue&quot;));

//  Test config can't be saved to a file in a path that doesn't
//  exist or isn't writable
rc = zconfig_savef(root, &quot;%s/path/that/doesnt/exist/%s&quot;, TESTDIR, &quot;test.cfg&quot;);
assert(rc == -1);

zconfig_destroy(&amp;root);
zchunk_destroy(&amp;chunk);

//  Delete all test files
zdir_t *dir = zdir_new(TESTDIR, NULL);
assert(dir);
zdir_remove(dir, true);
zdir_destroy(&amp;dir);
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
