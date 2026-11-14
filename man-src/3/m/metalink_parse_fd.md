---
title: "metalink_parse_fd(3)"
name: "metalink_parse_fd"
section: "3"
letter: "m"
url: "/docs/linux/man/3-metalink_parse_fd/"
description: "metalink_parse_file, metalink_parse_fp, metalink_parse_fd, metalink_parse_memory – Parse Metalink file and create metalink_t object."
---

<h2>NAME</h2>
<p> metalink_parse_file, metalink_parse_fp, metalink_parse_fd, metalink_parse_memory &#8211; Parse Metalink file and create metalink_t object.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/metalink/metalink_parser.h">metalink/metalink_parser.h</a>&gt;</code> </p>
<p> <code>metalink_error_t metalink_parse_file(const char *</code><i>filename</i><code>, metalink_t **</code><i>res</i><code>);</code><br />
 <code>metalink_error_t metalink_parse_fp(FILE *</code><i>docfp</i><code>, metalink_t **</code><i>res</i><code>);</code><br />
 <code>metalink_error_t metalink_parse_fd(int </code><i>docfd</i><code>, metalink_t **</code><i>res</i><code>);</code><br />
 <code>metalink_error_t metalink_parse_memory(const char *</code><i>buf</i><code>, size_t </code><i>len</i><code>, metalink_t **</code><i>res</i><code>);</code> </p>
<h2>DESCRIPTION</h2>
<p> These functions parse Metalink file data and constructs metalink_t structure. You don&#8217;t have to allocate memory for metalink_t structure. They take the pointer of metalink_t pointer and allocate memory for that pointer. </p>
<p> <code>metalink_parse_file</code>() parses Metalink file denoted by <i>filename</i> and constructs metalink_t structure. </p>
<p> <code>metalink_parse_fp</code>() reads data from file stream <i>docfp</i> and construtcts metalink_t structure. </p>
<p> <code>metalink_parse_fd</code>() reads data from file descriptor <i>docfd</i> and constructs metalink_t structure. </p>
<p> <code>metalink_parse_memory</code>() parses <i>len</i> bytes of <i>buf</i> and constructs metalink_t structure. </p>
<p> The caller must free the memory allocated for metalink_t structure using <code><a href="/docs/linux/man/3-metalink_delete/">metalink_delete</a></code>(3) if it is no longer used. </p>
<h2>RETURN VALUE</h2>
<p> All functions return 0 for success. When error occurred, non-zero value error code is returned and metalink_t structure is not allocated. The error codes are described in metalink_error.h. </p>
<h2>EXAMPLE</h2>
<pre><code>
#include &lt;metalink/metalink_parser.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(int argc, char **argv)
{
    metalink_error_t r;
    metalink_t *metalink;
    metalink_file_t *file;
    metalink_checksum_t **checksums;

    r = metalink_parse_file("sample.metalink", &amp;metalink);
    if (r != 0) {
        fprintf(stderr, "ERROR: code=%d
", r);
        exit(EXIT_FAILURE);
    }

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
<p> <code><a href="/docs/linux/man/3-metalink_delete/">metalink_delete</a></code>(3), <code><a href="/docs/linux/man/3-metalink_parse_update/">metalink_parse_update</a></code>(3), <code><a href="/docs/linux/man/3-metalink_t/">metalink_t</a></code>(3) </p>
<h2>Index</h2>
