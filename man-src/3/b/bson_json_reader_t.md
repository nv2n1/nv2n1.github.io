---
title: "bson_json_reader_t(3)"
name: "bson_json_reader_t"
section: "3"
letter: "b"
url: "/docs/linux/man/3-bson_json_reader_t/"
description: "bson_json_reader_t – Bulk JSON to BSON conversion"
---

<h2>NAME</h2>
<p> bson_json_reader_t &#8211; Bulk JSON to BSON conversion</p>
<h2>SYNOPSIS</h2>
<pre><code>
#include &lt;bson.h&gt;
typedef struct _bson_json_reader_t bson_json_reader_t;
typedef enum {
    BSON_JSON_ERROR_READ_CORRUPT_JS = 1,
    BSON_JSON_ERROR_READ_INVALID_PARAM,
    BSON_JSON_ERROR_READ_CB_FAILURE,
} bson_json_error_code_t;
</code></pre>
<h2>DESCRIPTION</h2>
<p> The <code>bson_json_reader_t</code> structure is used for reading a sequence of JSON documents and transforming them to <code>bson_t</code> documents. </p>
<p> This can often be useful if you want to perform bulk operations that are defined in a file containing JSON documents. </p>
<p> <code>NOTE</code></p>
<dl>
<dt>
<dd> <code>bson_json_reader_t</code> works upon JSON documents formatted in <code>MongoDB extended JSON</code> format.</dl>
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
 * This program will print each JSON document contained in the provided files
 * as a BSON string to STDOUT.
 */
#include &lt;bson.h&gt;
#include &lt;stdio.h&gt;
#include &lt;stdlib.h&gt;
int main(int argc,
         char *argv[])
{
    bson_json_reader_t *reader;
    bson_error_t error;
    const char *filename;
    bson_t doc = BSON_INITIALIZER;
    int i;
    int b;
    /*
     * Print program usage if no arguments are provided.
     */
    if (argc == 1) {
        fprintf(stderr, "usage: %s FILE...
", argv[0]);
        return 1;
    }
    /*
     * Process command line arguments expecting each to be a filename.
     */
    for (i = 1; i &lt; argc; i++) {
        filename = argv[i];
        /*
         * Open the filename provided in command line arguments.
         */
        if (0 == strcmp(filename, "-")) {
            reader = bson_json_reader_new_from_fd(STDIN_FILENO, false);
        } else {
            if (!(reader = bson_json_reader_new_from_file(filename, &amp;error))) {
                fprintf(stderr, "Failed to open \"%s\": %s
",
                        filename, error.message);
                continue;
            }
        }
        /*
         * Convert each incoming document to BSON and print to stdout.
         */
        while ((b = bson_json_reader_read(reader, &amp;doc, &amp;error))) {
            if (b &lt; 0) {
                fprintf(stderr, "Error in json parsing:
%s
", error.message);
                abort();
            }
            if (fwrite(bson_get_data(&amp;doc), 1, doc.len, stdout) != doc.len) {
                fprintf(stderr, "Failed to write to stdout, exiting.
");
                exit(1);
            }
            bson_reinit(&amp;doc);
        }
        bson_json_reader_destroy(reader);
        bson_destroy(&amp;doc);
    }
    return 0;
}
</code></pre>
<h2>COLOPHON</h2>
<p> This page is part of libbson. Please report any bugs at <a rel="nofollow" href="https://jira.mongodb.org/browse/CDRIVER.">https://jira.mongodb.org/browse/CDRIVER.</a> </p>
<h2>Index</h2>
