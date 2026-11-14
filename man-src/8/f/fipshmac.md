---
title: "fipshmac(8)"
name: "fipshmac"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fipshmac/"
description: "fipshmac – create FIPS-140-2 validation checksum files"
---

<p>fipshmac &#8211; create FIPS-140-2 validation checksum files</p>
<h2>Syntax</h2>
<p>fipshmac [<code>-d</code> &lt;<i>directory</i>&gt;] file1 [file2 &#8230;]</p>
<h2>Description</h2>
<p>fipshmac will create FIPS-140-2 checksum files for all the filenames specified. If the -d option is not specified, checksum files will be written in the same directory as the file being checksummed. It will prepend a &#8216;.&#8217; and append &#8216;.hmac&#8217; to the original file name. When a directory is specified with the <code>-d</code> option, the &#8216;.&#8217; will not be prepended and the files are stored into the directory. </p>
<p> If invoked correctly the fipshmac command will not print anything to the standard output or error. Otherwise it will print an error message to stderr. </p>
<p> The <code>-s</code> option allows to specify the suffix of the hmac file names. The default value <i>.hmac</i> is used when this option is not specified.</p>
<h2>Return Codes</h2>
<p>fipscheck can return the following return codes: </p>
<p> 0 OK </p>
<p> 2 Missing filename </p>
<p> 3 Cannot open the checksum file for writing </p>
<p> 4 Cannot read the file to be checksummed, or the checksum computation failed </p>
<p> 5 Memory allocation error </p>
<p> 6,7 Cannot write to the checksum file</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fipscheck/">fipscheck</a></code>(8), <code><a href="/docs/linux/man/3-fipscheck-h/">fipscheck.h</a></code>(3), m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/fipscheck/">https://fedorahosted.org/fipscheck/</a></code>m[]</p>
<h2>Author</h2>
<p>Tomas Mraz &lt;tmraz [at] redhat.com&gt;. </p>
<p> Man page by Paul Wouters &lt;pwouters [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright 2008, 2012 Red Hat, Inc. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
