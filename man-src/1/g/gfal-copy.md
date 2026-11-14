---
title: "gfal-copy(1)"
name: "gfal-copy"
section: "1"
letter: "g"
url: "/docs/linux/man/1-gfal-copy/"
description: "gfal-copy – Copy files"
---

<h2>NAME</h2>
<p> gfal-copy &#8211; Copy files</p>
<h2>SYNOPSIS</h2>
<p> <code>gfal-copy</code> [ <i>OPTION</i> ]&#8230; <i>SOURCE</i> <i>DEST1 [ DEST2 &#8230; ]</i> </p>
<h2>DESCRIPTION</h2>
<p> <code>gfal-copy</code> Copies files from source to destination(s). If several destinations are specified, the file will be copy in a chain: src -&gt; dst1, dst1 -&gt; dst2, &#8230; If used in an interactive console, transfer information will be giving during the copy, which varies depending on the available information. This command can be used to upload local files to remote file systems and to register files in the file catalog (see examples). </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-h, &#8211;help</code></p>
<dd> show help about the command.</p>
<dt><code>-V, &#8211;version</code></p>
<dd> output version information and exit.</p>
<dt><code>-v, &#8211;verbose</code></p>
<dd> verbose mode. Repeat up to 3 times for the most verbose mode.</p>
<dt><code>-D, &#8211;definition</code></p>
<dd> define properties for gfal2.</p>
<dt><code>-C, &#8211;client-info</code></p>
<dd> provide custom client-side information</p>
<dt><code>-t, &#8211;timeout </code><i>TIMEOUT</i></p>
<dd> maximum time for the operation to terminate &#8211; default is 1800 seconds. This timeout is enforced by gfal2-util, so it applies to the overall operation. It should be greater or equal than &#8211;transfer-timeout.</p>
<dt><code>-E, &#8211;cert </code><i>CERT</i></p>
<dd> user certificate</p>
<dt><code>&#8211;key </code><i>KEY</i></p>
<dd> user private key</p>
<dt><code>-4</code></p>
<dd> Forces gfal2-util to use IPv4 addresses only</p>
<dt><code>-6</code></p>
<dd> Forces gfal2-util to use IPv6 addresses only</p>
<dt><code>-f, &#8211;force</code></p>
<dd> if destination file(s) cannot be overwritten, delete it and try again</p>
<dt><code>-p, &#8211;parent</code></p>
<dd> if the destination directory does not exist, create it</p>
<dt><code>-n, &#8211;nbstreams </code><i>NBSTREAMS</i></p>
<dd> specify the maximum number of parallel streams to use for the copy</p>
<dt><code>&#8211;tcp-buffersize </code><i>TCP_BUFFERSIZE</i></p>
<dd> specify the TCP buffersize</p>
<dt><code>-s, &#8211;src-spacetoken </code><i>SRC_SPACETOKEN</i></p>
<dd> source spacetoken to use for the transfer</p>
<dt><code>-S, &#8211;dst-spacetoken </code><i>DST_SPACETOKEN</i></p>
<dd> destination spacetoken to use for the transfer</p>
<dt><code>-T, &#8211;transfer-timeout </code><i>TRANSFER_TIMEOUT</i></p>
<dd> timeout for the transfer operation. This timeout is enforced by each plugin, so it applies to the transfer operation only.</p>
<dt><code>-K, &#8211;checksum </code><i>CHECKSUM</i></p>
<dd> checksum algorithm to use, or algorithm:value</p>
<dt><code>&#8211;from-file </code><i>FROM_FILE</i></p>
<dd> read sources from a file</p>
<dt><code>&#8211;just-copy</code></p>
<dd> just do the copy and skip any preparation (i.e. checksum, overwrite, etc.) </p>
</dl>
<h2>EXAMPLES</h2>
<dl>
<dt>Copy a file to <a href="srm://endpoint.cern.ch/path/group,">srm://endpoint.cern.ch/path/group,</a> preferring a protocol as specified in the configuration file:</p>
<dd> <code>gfal-copy file:///etc/group <a href="srm://endpoint.cern.ch/path/">srm://endpoint.cern.ch/path/</a></code></dl>
<dl>
<dt>You can specify directly a protocol, if you know that it is supported by the end point:</p>
<dd> <code>gfal-copy file:///tmp/test <a href="gsiftp://endpoint.cern.ch/path/test">gsiftp://endpoint.cern.ch/path/test</a></code></dl>
<dl>
<dt>
<dt>Do a chained copy:</p>
<dd>
<dd> <code>gfal-copy file:///tmp/test <a href="gsiftp://endpoint.cern.ch/path/test">gsiftp://endpoint.cern.ch/path/test</a> file:///tmp/test2</code></dl>
<dl>
<dt>Registration of a file in the LFC:</p>
<dd> <code>gfal-copy file:///tmp/source <a href="gsiftp://endpoint.cern.ch/path/test">gsiftp://endpoint.cern.ch/path/test</a> <a href="lfc://lfc-host.cern.ch/lfn">lfc://lfc-host.cern.ch/lfn</a></code> </p>
</dl>
<h2>FILES</h2>
<p> <i>/etc/gfal2.d/*</i></p>
<dl>
<dt>
<dd> All configuration files in this directory affect the behavior of the underlying gfal2, in particular, the default choice of transfer protocols. </p>
</dl>
<h2>AUTHORS</h2>
<p> Duarte Meneses &lt;duarte.meneses [at] cern.ch&gt;<br />
 Adrien Devresse &lt;adrien.devresse [at] cern.ch&gt;<br />
 Alejandro Alvarez Ayllon &lt;alejandro.alvarez.ayllon [at] cern.ch&gt; </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-gfal-copy/">gfal-copy</a></code>(1), <code><a href="/docs/linux/man/1-gfal-rm/">gfal-rm</a></code>(1), <code><a href="/docs/linux/man/1-gfal-cat/">gfal-cat</a></code>(1), <code><a href="/docs/linux/man/1-gfal-save/">gfal-save</a></code>(1), <code><a href="/docs/linux/man/1-gfal-mkdir/">gfal-mkdir</a></code>(1), <code><a href="/docs/linux/man/1-gfal-ls/">gfal-ls</a></code>(1), <code><a href="/docs/linux/man/1-gfal-xattr/">gfal-xattr</a></code>(1) </p>
<h2>Index</h2>
