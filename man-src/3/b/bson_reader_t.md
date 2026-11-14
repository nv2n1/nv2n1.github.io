---
title: "bson_reader_t(3)"
name: "bson_reader_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_reader_t/"
description: "bson_reader_t – Streaming BSON Document Reader"
---

<h2>NAME</h2>
<p> bson_reader_t &#8211; Streaming BSON Document Reader</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct _bson_reader_t bson_reader_t;
bson_reader_t *bson_reader_new_from_handle(void *handle,
                                           bson_reader_read_func_t rf,
                                           bson_reader_destroy_func_t df);
bson_reader_t *bson_reader_new_from_fd(int fd,
                                       bool close_on_destroy);
bson_reader_t *bson_reader_new_from_file(const char *path,
                                         bson_error_t *error);
bson_reader_t *bson_reader_new_from_data(const uint8_t *data,
                                         size_t length);
void bson_reader_destroy(bson_reader_t *reader);
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>bson_reader_t</code> is a structure used for reading a sequence of BSON documents. The sequence can come from a file-descriptor, memory region, or custom callbacks. </p>
<h2>EXAMPLE</h2>
<pre><code>
/*
 * Copyright 2013 MongoDB, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
/*
 * This program will print each BSON document contained in the provided files
 * as a JSON string to STDOUT.
 */
#include &lt;bson.h&gt;
#include &lt;stdio.h&gt;
int main(int argc,
         char *argv[])
{
    bson_reader_t *reader;
    const bson_t *b;
    bson_error_t error;
    const char *filename;
    char *str;
    int i;
    /*
     * Print program usage if no arguments are provided.
     */
    if (argc == 1) {
        fprintf(stderr,
                "usage: %s [FILE | -]...
Use - for STDIN.
",
                argv[0]);
        return 1;
    }
    /*
     * Process command line arguments expecting each to be a filename.
     */
    for (i = 1; i &lt; argc; i++) {
        filename = argv[i];
        if (strcmp(filename, "-") == 0) {
            reader = bson_reader_new_from_fd(STDIN_FILENO, false);
        } else {
            if (!(reader = bson_reader_new_from_file(filename, &amp;error))) {
                fprintf(stderr, "Failed to open \"%s\": %s
",
                        filename, error.message);
                continue;
            }
        }
        /*
         * Convert each incoming document to JSON and print to stdout.
         */
        while ((b = bson_reader_read(reader, NULL))) {
            str = bson_as_json(b, NULL);
            fprintf(stdout, "%s
", str);
            bson_free(str);
        }
        /*
         * Cleanup after our reader, which closes the file descriptor.
         */
        bson_reader_destroy(reader);
    }
    return 0;
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
