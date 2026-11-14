---
title: "metalink_parser_context_new(3)"
name: "metalink_parser_context_new"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_parser_context_new/"
description: "metalink_parse_update, metalink_parse_final, metalink_parser_context_new, metalink_parse_context_delete – Parse Metalink file and create metalink_t object."
---

<h2>NAME</h2>
<p> metalink_parse_update, metalink_parse_final, metalink_parser_context_new, metalink_parse_context_delete &#8211; Parse Metalink file and create metalink_t object. </p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_parser.h">metalink/metalink_parser.h</a>&gt;</code> </p>
<p> <code>metalink_error_t metalink_parse_update(metalink_parser_context_t *</code><i>ctx</i><code>,</code> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const char *</code><i>buf</i><code>, size_t </code><i>len</i><code>);</code><br />
 <code>metalink_error_t metalink_parse_final(metalink_parser_context_t *</code><i>ctx</i><code>,</code> <code><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>const char *</code><i>buf</i><code>, size_t </code><i>len</i><code>,</code> <code>metalink_t **</code><i>res</i><code>);</code> </p>
<p> <code>metalink_parser_context_t* metalink_parser_context_new();</code><br />
 <code>void metalink_parser_context_delete(metalink_parser_context_t *</code><i>ctx</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> These functions privide a push interface for parsing Metalink XML files. </p>
<p> Before calling <code>metalink_parse_update</code>() and <code>metalink_parse_final</code>(), <code>metalink_parse_context_t</code> has to be created by <code>metalink_parser_context_new</code>(). </p>
<p> In each call of <code>metalink_parse_update</code>(), <i>len</i> bytes of <i>buf</i> are processed. At the last piece of data, call <code>metalink_parse_final</code>() to get <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) structure as a result. Giving 0 as <i>len</i> is permitted. </p>
<p> <code>metalink_parse_final</code>() calls <code>metalink_parser_context_delete</code>() internally to deallocate the memory for passed <code>metalink_parser_context_t</code>. Therefore you don&#8217;t have to call metlaink_parser_context_delete() if you call <code>metalink_parse_final</code>(). Otherwise call metalink_parser_context_delete() to free the allocated resource. </p>
<p> You don&#8217;t have to allocate memory for <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) structure. <code>metalink_parse_final</code>() take the pointer of <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) pointer and allocate memory for that pointer. </p>
<p> The caller must free the memory allocated for <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) structure using <code><a href="/docs/linux/man/3-metalink_delete/">metalink_delete</a></code>(3) if it is no longer used. </p>
<h2>RETURN VALUE</h2>
<p> <code>metalink_parse_update</code>(), <code>metalink_parse_final</code>() return 0 for success. When error occurred, non-zero value error code is returned. If error occurred, <code>metalink_parse_final</code>() does not allocate memory for <code>metalink_t</code>. The error codes are described in metalink_error.h. </p>
<p> In case of success, <code>metalink_parser_context_new</code>() allocates memory for <code>metalink_parser_context_t</code>() and returns the pointer to it. In case of failure, <code>metalink_parser_context_new</code>() returns NULL. </p>
<p> <code>metalink_parser_context_delete</code>() returns no value. </p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;errno.h&gt;
#include &lt;fcntl.h&gt;
#include &lt;metalink/metalink_parser.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
#include &lt;string.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;sys/types.h&gt;
#include &lt;unistd.h&gt;
int main(int argc, char **argv)
{
    metalink_error_t r;
    metalink_t *metalink;
    metalink_file_t *file;
    metalink_checksum_t **checksums;
    metalink_parser_context_t *context;
    int fd;
    char buf[BUFSIZ];
    ssize_t length;
    context = metalink_parser_context_new();
    if (context == NULL) {
        fprintf(stderr,
                "ERROR: failed to create metalink_parser_context_t
");
        exit(EXIT_FAILURE);
    }
    fd = open("sample.metalink", O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "ERROR: open():%s
", strerror(errno));
        exit(EXIT_FAILURE);
    }
    while ((length = TEMP_FAILURE_RETRY(read(fd, buf, sizeof(buf)))) != 0) {
        r = metalink_parse_update(context, buf, length);
        if (r != 0) {
            fprintf(stderr, "ERROR: code=%d
", r);
            metalink_parser_context_delete(context);
            exit(EXIT_FAILURE);
        }
    }
    if (length == -1) {
        fprintf(stderr, "ERROR: read():%s
", strerror(errno));
        metalink_parser_context_delete(context);
        exit(EXIT_FAILURE);
    }

    r = metalink_parse_final(context, NULL, 0, &amp;metalink);
    if (r != 0) {
        fprintf(stderr, "ERROR: code=%d
", r);
        exit(EXIT_FAILURE);
    }
    TEMP_FAILURE_RETRY(close(fd));

    file = metalink-&gt;files[0];
    printf("name: %s
", file-&gt;name);
    printf("size: %lld
", file-&gt;size);
    printf("os  : %s
", file-&gt;os);
    if (file-&gt;checksums) {
        checksums = file-&gt;checksums;
        while (*checksums) {
            printf("hash: %s %s
", (*checksums)-&gt;type, (*checksums)-&gt;hash);
            ++checksums;
        }
    }
    if (file-&gt;chunk_checksum) {
        size_t count = 0;
        metalink_piece_hash_t **piece_hashes;
        printf("chunk checksum: size=%d, type=%s
",
               file-&gt;chunk_checksum-&gt;length,
               file-&gt;chunk_checksum-&gt;type);
        printf("first 5 piece hashes...
");
        piece_hashes = file-&gt;chunk_checksum-&gt;piece_hashes;
        while (*piece_hashes &amp;&amp; count &lt; 5) {
            printf("piece=%d, hash=%s
", (*piece_hashes)-&gt;piece,
                   (*piece_hashes)-&gt;hash);
            ++piece_hashes;
            ++count;
        }
        printf("...
");
    }
    if (file-&gt;resources) {
        size_t count = 0;
        metalink_resource_t **resources;
        printf("first 5 resources...
");
        resources = file-&gt;resources;
        while (*resources &amp;&amp; count &lt; 5) {
            printf("type=%s, location=%s, preference=%d, url=%s
",
                   (*resources)-&gt;type, (*resources)-&gt;location,
                   (*resources)-&gt;preference, (*resources)-&gt;url);
            ++resources;
            ++count;
        }
        printf("...
");
    }
    /* delete metalink_t */
    metalink_delete(metalink);
    return EXIT_SUCCESS;
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-metalink_delete/">metalink_delete</a></code>(3), <code><a href="/docs/linux/man/3-metalink_parse_file/">metalink_parse_file</a></code>(3), <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) </p>
<h2>Index</h2>
