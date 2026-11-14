---
title: "mongoc_gridfs_t(3)"
name: "mongoc_gridfs_t"
section: "3"
letter: "m"
url: "/docs/linux/man/3-mongoc_gridfs_t/"
description: "mongoc_gridfs_t – mongoc_gridfs_t provides a MongoDB gridfs implementation. The system as a whole is made up of gridfs objects, which contain gridfs_files and gridfs_file_lists. Essentially, a basi..."
---

<p>mongoc_gridfs_t &#8211; mongoc_gridfs_t provides a MongoDB gridfs implementation. The system as a whole is made up of gridfs objects, which contain gridfs_files and gridfs_file_lists. Essentially, a basic file system API.</p>
<h2>Synopsis</h2>
<pre>#include &lt;mongoc.h&gt;
typedef struct _mongoc_gridfs_t mongoc_gridfs_t;</pre>
<h2>Description</h2>
<p><code>mongoc_gridfs_t</code> provides a MongoDB gridfs implementation. The system as a whole is made up of <code>gridfs</code> objects, which contain <code>gridfs_files</code> and <code>gridfs_file_lists</code> \&amp;. Essentially, a basic file system API. </p>
<p> There are extensive caveats about the kind of use cases gridfs is practical for. In particular, any writing after initial file creation is likely to both break any concurrent readers and be quite expensive. That said, this implementation does allow for arbitrary writes to existing gridfs object, just use them with caution. </p>
<p> mongoc_gridfs also integrates tightly with the <code>mongoc_stream_t</code> abstraction, which provides some convenient wrapping for file creation and reading/writing. It can be used without, but its worth looking to see if your problem can fit that model. </p>
<p> <code>NOTE</code></p>
<dl COMPACT>
<dd><code>mongoc_gridfs_t</code> does not support read preferences. In a replica set, GridFS queries are always routed to the primary. </p>
</dl>
<h2>Thread Safety</h2>
<p><code>mongoc_gridfs_t</code> is NOT thread-safe and should only be used in the same thread as the owning <code>mongoc_client_t</code> \&amp;. </p>
<h2>Lifecycle</h2>
<p>It is an error to free a <code>mongoc_gridfs_t</code> before freeing all related instances of <code>mongoc_gridfs_file_t</code> and <code>mongoc_gridfs_file_list_t</code> \&amp;. </p>
<h2>Example</h2>
<pre>#include &lt;mongoc.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;fcntl.h&gt;
int main (int argc, char *argv[])
{
 mongoc_gridfs_t *gridfs;
 mongoc_gridfs_file_t *file;
 mongoc_gridfs_file_list_t *list;
 mongoc_gridfs_file_opt_t opt = { 0 };
 mongoc_client_t *client;
 mongoc_stream_t *stream;
 bson_t query;
 bson_t child;
 bson_error_t error;
 ssize_t r;
 char buf[4096];
 mongoc_iovec_t iov;
 const char * filename;
 const char * command;
 if (argc &lt; 2) {
 fprintf(stderr, &quot;usage - %s command ...
&quot;, argv[0]);
 return 1;
 }
 mongoc_init();
 iov.iov_base = (void *)buf;
 iov.iov_len = sizeof buf;
 /* connect to localhost client */
 client = mongoc_client_new (&quot;mongodb://127.0.0.1:27017&quot;);
 assert(client);
 /* grab a gridfs handle in test prefixed by fs */
 gridfs = mongoc_client_get_gridfs (client, &quot;test&quot;, &quot;fs&quot;, &amp;error);
 assert(gridfs);
 command = argv[1];
 filename = argv[2];
 if (strcmp(command, &quot;read&quot;) == 0) {
 if (argc != 3) {
 fprintf(stderr, &quot;usage - %s read filename
&quot;, argv[0]);
 return 1;
 }
 file = mongoc_gridfs_find_one_by_filename(gridfs, filename, &amp;error);
 assert(file);
 stream = mongoc_stream_gridfs_new (file);
 assert(stream);
 for (;;) {
 r = mongoc_stream_readv (stream, &amp;iov, 1, -1, 0);
 assert (r &gt;= 0);
 if (r == 0) {
 break;
 }
 if (fwrite (iov.iov_base, 1, r, stdout) != r) {
 MONGOC_ERROR (&quot;Failed to write to stdout. Exiting.
&quot;);
 exit (1);
 }
 }
 mongoc_stream_destroy (stream);
 mongoc_gridfs_file_destroy (file);
 } else if (strcmp(command, &quot;list&quot;) == 0) {
 bson_init (&amp;query);
 bson_append_document_begin (&amp;query, &quot;$orderby&quot;, -1, &amp;child);
 bson_append_int32 (&amp;child, &quot;filename&quot;, -1, 1);
 bson_append_document_end (&amp;query, &amp;child);
 bson_append_document_begin (&amp;query, &quot;$query&quot;, -1, &amp;child);
 bson_append_document_end (&amp;query, &amp;child);
 list = mongoc_gridfs_find (gridfs, &amp;query);
 bson_destroy (&amp;query);
 while ((file = mongoc_gridfs_file_list_next (list))) {
 const char * name = mongoc_gridfs_file_get_filename(file);
 printf(&quot;%s
&quot;, name ? name : &quot;?&quot;);
 mongoc_gridfs_file_destroy (file);
 }
 mongoc_gridfs_file_list_destroy (list);
 } else if (strcmp(command, &quot;write&quot;) == 0) {
 if (argc != 4) {
 fprintf(stderr, &quot;usage - %s write filename input_file
&quot;, argv[0]);
 return 1;
 }
 stream = mongoc_stream_file_new_for_path (argv [3], O_RDONLY, 0);
 assert (stream);
 opt.filename = filename;
 file = mongoc_gridfs_create_file_from_stream (gridfs, stream, &amp;opt);
 assert(file);
 mongoc_gridfs_file_save(file);
 mongoc_gridfs_file_destroy(file);
 } else {
 fprintf(stderr, &quot;Unknown command&quot;);
 return 1;
 }
 mongoc_gridfs_destroy (gridfs);
 mongoc_client_destroy (client);
 mongoc_cleanup ();
 return 0;
}</pre>
<h2>Colophon</h2>
<p>This page is part of MongoDB C Driver. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a></p>
