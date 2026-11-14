---
title: "rdiffdir(1)"
name: "rdiffdir"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rdiffdir/"
description: "rdiffdir – compute and apply signatures and diffs to directories"
---

<h2 class="name">NAME</h2>
<p> rdiffdir &#8211; compute and apply signatures and diffs to directories </p>
<h2>SYNOPSIS</h2>
<p> <code>rdiffdir</code> <code>[</code><i>options</i><code>]</code> <code>sig[nature]</code> <i>basis_dir signature_file</i> </p>
<p> <code>rdiffdir</code> <code>[</code><i>options</i><code>]</code> <code>delta</code> <i>full_sigtar</i> <code>{</code><i>incr_sigtar</i><code>}</code> <i>new_dir delta_file</i> </p>
<p> <code>rdiffdir</code> <code>[</code><i>options</i><code>]</code> <code>patch</code> <i>basis_dir delta_file</i> </p>
<p> <code>rdiffdir</code> <code>[</code><i>options</i><code>]</code> <code>tar</code> <i>basis_dir tar_file</i> </p>
<p> If <i>signature_file</i> or <i>delta_file</i> are &quot;-&quot;, the data will be read from stdin or written to stdout as appropriate. </p>
<h2>DESCRIPTION</h2>
<p> <code>rdiffdir</code> is supposed to be like rdiff, but can operate on directories. See <code><a href="/docs/linux/man/1-rdiff/">rdiff</a></code>(1) for more information. The syntax is similar. </p>
<p> Regarding the <code>delta</code> command, the <i>full_sigtar</i> operand is a <i>signature_file</i> written by an earlier <code>signature</code> or <code>tar</code> command (the latter using the <code>&#8211;write-sig-to</code> option). The optional <i>incr_sigtar</i> operands are signature files written by earlier <code>delta</code> commands using the <i>&#8211;write-sig-to</i> option. This way the Nth invocation of the <code>delta</code> command can parse (and extend) the signature chain that has been founded by the first <code>signature</code> or <code>tar</code> command with a full signature, and then extended by the subsequent N-1 <code>delta</code> invocations with incremental signatures. It is the responsibility of the user to specify the sigtar operands in logical increment order. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;write-sig-to </code><i>sigfile</i></p>
<dd> This option is only used in <code>delta</code> and <code>tar</code> modes. When specified, rdiffdir will write a signature of the directory it is processing to sigfile. The end result will be a delta and a new signature calculated over the <code>same</code> data. </p>
<dt><code>-z, &#8211;gzip-compress</code></p>
<dd> Enable gzip compression and decompression of signature and delta files. </p>
</dl>
<h2>SELECTION OPTIONS</h2>
<p> In <code>signature</code> and <code>delta</code> modes, rdiffdir accepts <code>duplicity</code>-like selection options including &#8211;exclude, &#8211;exclude-filelist, etc. See the <code><a href="/docs/linux/man/1-duplicity/">duplicity</a></code>(1) manual page for more information. </p>
<h2>BUGS</h2>
<p> Hard links are currently unsupported (they will be treated as non-linked regular files). </p>
<p> Bad signatures will be treated as empty instead of logging appropriate error message. </p>
<h2>AUTHOR</h2>
<dl>
<dt><code>Original Author</code> &#8211; Ben Escoto &lt;bescoto [at] stanford.edu&gt;</p>
<dd>
<dt><code>Current Maintainer</code> &#8211; Kenneth Loafman &lt;kenneth [at] loafman.com&gt;</p>
<dd>
<dt><code>Continuous Contributors</code></p>
<dd> Edgar Soldin, Mike Terry</dl>
<p> Also we&#8217;d like to thank everybody posting issues to the mailing list or on launchpad, sending in patches or contributing otherwise. Duplicity wouldn&#8217;t be as stable and useful if it weren&#8217;t for you. </p>
<p> A special thanks goes to rsync.net, a Cloud Storage provider with explicit support for duplicity, for several monetary donations and for providing a special &quot;duplicity friends&quot; rate for their offsite backup service. Email info [at] rsync.net for details. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-duplicity/">duplicity</a></code>(1), <code><a href="/docs/linux/man/1-python/">python</a></code>(1), <code><a href="/docs/linux/man/1-rdiff/">rdiff</a></code>(1), <code><a href="/docs/linux/man/1-rdiff-backup/">rdiff-backup</a></code>(1). </p>
<h2>Index</h2>
