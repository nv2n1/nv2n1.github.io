---
title: "tpmunsealshred(3)"
name: "tpmunsealshred"
section: "3"
letter: "t"
url: "/docs/linux/man/3-tpmunsealshred/"
description: "tpmUnsealFile, tpmUnsealShred, tpmUnsealStrerror – unseal routines"
---

<p>TPM Management &#8211; tpmUnsealFile, tpmUnsealShred, tpmUnsealStrerror<br />
 </center></p>
<h2>Name</h2>
<p>tpmUnsealFile, tpmUnsealShred, tpmUnsealStrerror &#8211; unseal routines</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;tpm_unseal/tpm_unseal.h&gt;
int tpmUnsealFile(char *file, char **data, int *size);

void tpmUnsealShred(char *data, int size);

char *tpmUnsealStrerror(int rc);
</code></pre>
<h2>Description</h2>
<p>The functions in the tpmUnseal family allow access to a piece of sensitive data that has been sealed to the TPM configuration of a given system if the conditions are right, that is the SRK has not changed and the PCRS (if any) specified at seal time are of the appropriate value. The tpmUnsealFile function returns the contents of the file unsealed in the data buffer. The memory at *data must be freed by the caller. The tpmUnsealShred function will zero and free the memory. The tpmUnsealStrerror function will convert the return code from tpmUnsealFile into a human comprehensible string using and internal errno variable. </p>
<h2>Return Value</h2>
<p>The tpmUnsealFile function returns 0 on success and a negative number on error. The tpmUnsealStrerror function returns the error string on success and the empty string on an error. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-tpm_sealdata/">tpm_sealdata</a></code>(1) </p>
<h2>Reporting Bugs</h2>
<p>Report bugs to &lt;trousers-users [at] lists.sourceforge.net&gt;</p>
