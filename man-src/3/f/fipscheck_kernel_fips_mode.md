---
title: "fipscheck_kernel_fips_mode(3)"
name: "fipscheck_kernel_fips_mode"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fipscheck_kernel_fips_mode/"
description: "FIPSCHECK_verify, FIPSCHECK_verify_ex, FIPSCHECK_verify_files, FIPSCHECK_verify_files_ex, FIPSCHECK_fips_module_installed, FIPSCHECK_get_binary_path, FIPSCHECK_get_library_path, FIPSCHECK_kernel_fi..."
---

<p>FIPSCHECK_verify, FIPSCHECK_verify_ex, FIPSCHECK_verify_files, FIPSCHECK_verify_files_ex, FIPSCHECK_fips_module_installed, FIPSCHECK_get_binary_path, FIPSCHECK_get_library_path, FIPSCHECK_kernel_fips_mode, fipscheck.h &#8211; Various functions relating to running in FIPS mode </p>
<h2>Synopsis</h2>
<pre>#include &lt;fipscheck.h&gt;</pre>
<dl COMPACT>
<dt> <code>int FIPSCHECK_verify(const char&nbsp;<wbr>*</code><i>libname</i><code>, const char&nbsp;<wbr>*</code><i>symbolname</i><code>);</code></p>
<dt> <code>int FIPSCHECK_verify_ex(const char&nbsp;<wbr>*</code><i>libname</i><code>, const char&nbsp;<wbr>*</code><i>symbolname</i><code>, const char&nbsp;<wbr>*</code><i>hmac_suffix</i><code>, int&nbsp;<wbr></code><i>fail_if_missing</i><code>);</code></p>
<dt> <code>int FIPSCHECK_verify_files(const char&nbsp;<wbr>*</code><i>files[]</i><code>);</code></p>
<dt> <code>int FIPSCHECK_verify_files_ex(const char&nbsp;<wbr>*</code><i>hmac_suffix</i><code>, int&nbsp;<wbr></code><i>fail_if_missing</i><code>, const char&nbsp;<wbr>*</code><i>files[]</i><code>);</code></p>
<dt> <code>int FIPSCHECK_fips_module_installed(const char&nbsp;<wbr>*</code><i>libname</i><code>, const char&nbsp;<wbr>*</code><i>symbolname</i><code>, const char&nbsp;<wbr>*</code><i>hmac_suffix</i><code>);</code></p>
<dt> <code>int FIPSCHECK_get_binary_path(char&nbsp;<wbr>*</code><i>path</i><code>, size_t&nbsp;<wbr></code><i>pathlen</i><code>);</code></p>
<dt> <code>int FIPSCHECK_get_library_path(const char&nbsp;<wbr>*</code><i>libname</i><code>, const char&nbsp;<wbr>*</code><i>symbolname</i><code>, char&nbsp;<wbr>*</code><i>path</i><code>, size_t&nbsp;<wbr></code><i>pathlen</i><code>);</code></p>
<dt> <code>int FIPSCHECK_kernel_fips_mode(void</code><i></i><code>);</code></dl>
<h2>Description</h2>
<dd>The function <code>FIPSCHECK_kernel_fips_mode()</code> tests for the FIPS-140-2 mode in kernel. </p>
<p> The function <code>FIPSCHECK_verify()</code> computes and compares HMAC-SHA256 checksum by spawning the <code>fipscheck</code> command. The parameters <i>libname</i> and <i>symbolname</i> determine which shared library file loaded into the process space will be checksummed. If these parameters are set to NULL, the executable of the calling process is checksummed. </p>
<p> The function <code>FIPSCHECK_verify_ex()</code> in addition to the functionality above also allows to specify the full <i>hmac_suffix</i> with the default value of .hmac. And will return success if the hmac file is missing and the <i>fail_if_missing</i> parameter is set to 0. </p>
<p> The function <code>FIPSCHECK_verify_files()</code> can be used to explicitly specify NULL terminated array of file names in the parameter <i>files</i> to check. </p>
<p> Similarly the function <code>FIPSCHECK_verify_files_ex()</code> in addition to the functionality above also allows to specify the full <i>hmac_suffix</i> with the default value of .hmac. And will return success if the first hmac file is missing and the <i>fail_if_missing</i> parameter is set to 0. </p>
<p> The checksum file contains the HMAC-SHA256 encoded in hexadecimal notation using lowercase letters with one EOL character appended at the end. </p>
<p> The function <code>FIPSCHECK_fips_module_installed()</code> returns 1 if the hmac checksum file is found and 0 otherwise. </p>
<p> The functions <code>FIPSCHECK_get_library_path()</code> and <code>FIPSCHECK_get_binary_path()</code> return the shared library and executable paths in the <i>path</i>. The buffer pointed to by the parameter must be large enough to hold the path otherwise the path is truncated. The size of the buffer is specified by the <i>pathlen</i>.</p>
<h2>Return Value</h2>
<p>The main functions <code>FIPSCHECK_verify()</code> and <code>FIPSCHECK_verify_files()</code> return 1 when the verification of the binaries succeeds and 0 otherwise. The function <code>FIPSCHECK_kernel_fips_mode()</code> returns 1 when the kernel is in fips mode and 0 otherwise. </p>
<p> The auxiliary functions <code>FIPSCHECK_get_binary_path()</code> and <code>FIPSCHECK_get_library_path()</code> return 0 on success and -1 if the path cannot be determined.</p>
<h2>Fips Mode</h2>
<p>A kernel compiled with CONFIG_CRYPTO_FIPS=y can be booted in fips mode by specifying fips=1 as kernel parameter. Please refer to the security policy of the Kernel FIPS module for further details.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-fipscheck/">fipscheck</a></code>(8), <code><a href="/docs/linux/man/8-fipshmac/">fipshmac</a></code>(8), m[blue]<code><a rel="nofollow" href="https://fedorahosted.org/fipscheck/">https://fedorahosted.org/fipscheck/</a></code>m[]</p>
<h2>Author</h2>
<p>Tomas Mraz &lt;tmraz [at] redhat.com&gt;. </p>
<p> Man page authors Paul Wouters &lt;pwouters [at] redhat.com&gt; and Tomas Mraz &lt;tmraz [at] redhat.com&gt;.</p>
<h2>Copyright</h2>
<p>Copyright 2008, 2012 Red Hat, Inc. All rights reserved. </p>
<p> Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: </p>
<p> 1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. </p>
<p> 2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.</p>
