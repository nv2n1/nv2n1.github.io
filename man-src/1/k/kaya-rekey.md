---
title: "kaya-rekey(1)"
name: "kaya-rekey"
section: "1"
letter: "k"
url: "/docs/linux/man/1-kaya-rekey/"
description: "kaya-rekey – Binary key regeneration for kaya web applications"
---

<h2>NAME</h2>
<p> kaya-rekey &#8211; Binary key regeneration for kaya web applications</p>
<h2>SYNOPSIS</h2>
<p> <code>kaya-rekey</code> <i>FILE1 [FILE2 [&#8230;]]</i></p>
<h2>DESCRIPTION</h2>
<p> <code>kaya-rekey</code> gives all Kaya binaries specified on the command line a new application secret key </p>
<p> The application secret key makes webapps and CGI programs secure, by encrypting the state transfers. If you receive a webapp or CGI binary from someone else, or you believe someone untrusted has had read access to your binary, you can use the kaya-rekey application to generate a new application secret key without needing a recompile. </p>
<p> Binary distributors of Kaya applications are strongly recommended to use &#8216;kaya-rekey&#8217; as part of the installation process. </p>
<p> Prior to Kaya 0.3.0 this utility was called rekey </p>
<h2>OBTAINING</h2>
<p> The latest release of Kaya can be obtained from &lt;<a rel="nofollow" href="http://kayalang.org/download">http://kayalang.org/download</a>&gt; </p>
<p> Development versions can be obtained using <code><a href="/docs/linux/man/1-darcs/">darcs</a>(1)</code> from &lt;<a rel="nofollow" href="http://kayalang.org/darcs/">http://kayalang.org/darcs/</a>&gt; </p>
<h2>SECURITY</h2>
<p> <code>kaya-rekey</code> will use /dev/random to generate the new key if possible. If /dev/random is unavailable (Windows without MinGW, for example), the new key will be generated pseudo-randomly. This may allow an attacker to easily guess the new key. In environments where security is a concern, therefore, we strongly recommend recompiling with <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code> rather than using <code>kaya-rekey</code> if /dev/random is unavailable. </p>
<p> <code>kaya-rekey</code> will give a warning when rekeying if /dev/random is unavailable. </p>
<h2>BUGS</h2>
<p> Please report bugs in kaya-rekey to &lt;kaya [at] kayalang.org&gt; </p>
<p> <code>kaya-rekey</code> cannot rekey Kaya binaries generated with a compiler older than the switch to AES256 encryption (i.e. older than 0.2.0 final version) </p>
<p> In rare cases, <code>kaya-rekey</code> may not be able to successfully rekey a file and will print an error instead. You must recompile in this case to get a new application key. </p>
<h2>LICENSE</h2>
<p> <code>kaya-rekey</code> is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License (version 2 or any later version) as published by the Free Software Foundation. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-kayac/">kayac</a>(1)</code> </p>
<h2>Index</h2>
