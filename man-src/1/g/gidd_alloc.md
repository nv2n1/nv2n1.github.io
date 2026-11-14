---
title: "gidd_alloc(1)"
name: "gidd_alloc"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gidd_alloc/"
description: "gidd_alloc find a GID within the specified range which is not used by any process"
---

<h2>Name</h2>
<p> gidd_alloc find a GID within the specified range which is not used by any process </p>
<h2>Synopsis</h2>
<p> <code>gidd_alloc</code> <i>min-gid</i> <i>max-gid</i> </p>
<h2>Description</h2>
<p> This program will scan the alive PIDs, looking for which GID is unused in the supplied, inclusive range specified by the required arguments <i>min-gid</i> and <i>max-gid</i> . Upon finding one, it will add the GID to its own supplementary group list, and then scan the PIDs again expecting to find only itself using the GID. If no collision has occurred, the program exits, otherwise it retries. </p>
<h2>General Remarks</h2>
<p> This is a program only available for the Linux ports of HTCondor. </p>
<h2>Exit Status</h2>
<p> <i>gidd_alloc</i> will exit with a status value of 0 (zero) upon success, and it will exit with the value 1 (one) upon failure. </p>
<h2>Author</h2>
<p> Center for High Throughput Computing, University of Wisconsin-Madison</p>
<h2>Copyright</h2>
<p> Copyright (C) 1990-2015 Center for High Throughput Computing, Computer Sciences Department, University of Wisconsin-Madison, Madison, WI. All Rights Reserved. Licensed under the Apache License, Version 2.0. </p>
<h2>Index</h2>
