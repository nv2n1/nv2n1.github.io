---
title: "fipscheck(8)"
name: "fipscheck"
section: "8"
letter: "f"
url: "/docs/linux/man/8-fipscheck/"
description: "fipscheck – perform a FIPS-140-2 validation check of one or more files"
---

<p>fipscheck &#8211; perform a FIPS-140-2 validation check of one or more files</p>
<h2>Syntax</h2>
<p>fipscheck [<code>-s</code> &lt;<i>hmac-suffix</i>&gt;] file1 [file2 &#8230;]</p>
<h2>Description</h2>
<p>fipscheck will perform a FIPS-140-2 validation of a file using a stored checksum of a file. The file containing the checksum value is first looked up in the /usr/lib{64,}/fipscheck directory and if not found there, it will be searched for in the same directory as the file which is being checksummed. </p>
<p> The checksum file must have &#8216;.&#8217; prepended and &#8216;.hmac&#8217; appended to the original file name. The &#8216;.&#8217; must not be prepended to the file names in the /usr/lib{64,}/fipscheck directory. </p>
<p> If invoked correctly the fipscheck command will not print anything to the standard output or error and set the return code based on the test result. A return code of 0 means the file passed the checksum test. A value of non-zero means the checksum failed. </p>
<p> The <code>-s</code> option allows to specify the suffix of the hmac file names. The default value <i>.hmac</i> is used when this option is not specified.</p>
<h2>Return Codes</h2>
<p>fipscheck can return the following return codes: </p>
<p> 0 Checksum OK </p>
<p> 1 Checksum mismatch </p>
<p> 2 Missing filename </p>
<p> 3 Cannot open the checksum file </p>
<p> 4 Cannot read the file to be checksummed, or the checksum computation failed </p>
<p> 5 Memory allocation error </p>
<p> 10 and higher &#8211; Failure during self-checking the libfipscheck.so shared library </p>
<p> 20 and higher &#8211; Failure during self-checking the fipscheck binary</p>
<h2>Environment Variables</h2>
<p>If you set the environment variable FIPSCHECK_DEBUG to &quot;error&quot;, all error messages are sent to stderr. Setting this variable to &quot;syslog&quot; will send all error messages to the syslog daemon.</p>
<h2>Fips Mode</h2>
<p>A kernel compiled with CONFIG_CRYPTO_FIPS=y can be booted in fips mode by specifying fips=1 as kernel parameter. If the /boot director resides on a different partition, this needs to be specfied, for example boot=/dev/sda2.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fipshmac/">fipshmac</a></code>(8), <code><a href="/docs/linux/man/3-fipscheck-h/">fipscheck.h</a></code>(3), m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/fipscheck/">https://fedorahosted.org/fipscheck/</a></code>m[]</p>
<h2>Author</h2>
<p>Tomas Mraz &lt;tmraz [at] redhat.com&gt;. </p>
<p> Man page by Paul Wouters &lt;pwouters [at] redhat.com&gt;</p>
<h2>Copyright</h2>
<p>Copyright 2008, 2012 Red Hat, Inc. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
