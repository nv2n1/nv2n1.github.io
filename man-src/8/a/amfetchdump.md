---
title: "amfetchdump(8)"
name: "amfetchdump"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amfetchdump/"
description: "amfetchdump – extract backup images from multiple Amanda tapes."
---

<p>amfetchdump &#8211; extract backup images from multiple Amanda tapes.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amfetchdump</code> [-c | -C | -l] [-p | -n] [-a] [-O&nbsp;<wbr><i>directory</i>] [-d&nbsp;<wbr><i>device</i>] [-h | &#8211;header-file&nbsp;<wbr><i>filename</i> | &#8211;header-fd&nbsp;<wbr><i>fd</i>] [&#8211;decompress | &#8211;no-decompress | &#8211;server-decompress | &#8211;client-decompress] [&#8211;extract &#8211;directory<i>&nbsp;<wbr>directory</i>&nbsp;<wbr>[&#8211;data-path<i>&nbsp;<wbr>amanda|directtcp</i>]&nbsp;<wbr>[&#8211;application-property&nbsp;<wbr><i>NAME=VALUE</i>]*] [&#8211;decrypt | &#8211;no-decrypt | &#8211;server-decrypt | &#8211;client-decrypt] [&#8211;exact_match] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] <i>config</i> <i>hostname</i> [<i>disk</i>&nbsp;<wbr>[&nbsp;<wbr><i>date</i>&nbsp;<wbr>[&nbsp;<wbr><i>level</i>&nbsp;<wbr>[&nbsp;<wbr><i>hostname</i>&nbsp;<wbr>[&#8230;]&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]]</dl>
<h2>Description</h2>
<p><code>Amfetchdump</code></p>
<dd>pulls one or more matching dumps from tape or from the holding disk, handling the reassembly of multi-tape split dump files as well as any tape autochanger operations. The dump are by default decompressed and decrypted. </p>
<p> It will automatically use the Amanda catalog to locate available dumps on tape, in the same way that the <code>find</code> feature of <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8) lists available dumps. </p>
<p> The <i>hostname</i>, <i>diskname</i>, <i>datestamp</i>, and <i>level</i> dump specifications are further described in <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7). Note that at minimum a <i>hostname</i> must be specified. </p>
<p> Unless <code>-p</code> is used, backup images are extracted to files in the current directory named: </p>
<p> If a changer error occurs, or the <code>-d</code> option is given, then amfetchdump prompts for each required volume. </p>
<p> <i>hostname.diskname.datestamp.dumplevel</i></p>
<h2>Options</h2>
<p><code>-p</code></p>
<dl>
<dd>Pipe exactly one complete dump file to <i>stdout</i>, instead of writing the file to disk. This will restore only the first matching dumpfile (where &quot;first&quot; is determined by the dump log search facility).</dl>
<p> <code>-h</code></p>
<dl>
<dd>Output the amanda header as a 32K block to same output as the image.</dl>
<p> <code>&#8211;header-fd</code> <i>fd</i></p>
<dl>
<dd>Output the amanda header to the numbered file descriptor.</dl>
<p> <code>&#8211;header-file</code> <i>filename</i></p>
<dl>
<dd>Output the amanda header to the filename.</dl>
<p> <code>-d</code> <i>device_or_changer</i></p>
<dl>
<dd>Restore from this device or changer instead of the default, prompting for each volume.</dl>
<p> <code>-O</code> <i>directory</i></p>
<dl>
<dd>Output restored files to this directory, instead of to the current working directory.</dl>
<p> <code>-c</code></p>
<dl>
<dd>Compress output, fastest method available.</dl>
<p> <code>-C</code></p>
<dl>
<dd>Compress output, smallest file size method available.</dl>
<p> <code>&#8211;decompress</code></p>
<dl>
<dd>Always do the decompression, this is the default.</dl>
<p> <code>&#8211;no-decompress</code></p>
<dl>
<dd>Never do the decompression.</dl>
<p> <code>&#8211;server-decompress</code></p>
<dl>
<dd>Do the decompression only if the compression was done on the server.</dl>
<p> <code>&#8211;client-decompress</code></p>
<dl>
<dd>Do the decompression only if the compression was done on the client.</dl>
<p> <code>&#8211;decrypt</code></p>
<dl>
<dd>Always do the decryption, this is the default.</dl>
<p> <code>&#8211;no-decrypt</code></p>
<dl>
<dd>Never do the decryption.</dl>
<p> <code>&#8211;server-decrypt</code></p>
<dl>
<dd>Do the decryption only if the encryption was done on the server.</dl>
<p> <code>&#8211;client-decrypt</code></p>
<dl>
<dd>Do the decryption only if the encryption was done on the client.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <code>&#8211;extract</code></p>
<dl>
<dd>Extract the backup on the server in the <i>directory</i> directory.</dl>
<p> <code>&#8211;directory</code> <i>directory</i></p>
<dl>
<dd>Where to extract the backup with the <code>&#8211;extract</code> option. </p>
<p> Warning: All files in that directory can be removed.</dl>
<p> <code>&#8211;data-path</code> amanda|directtcp</p>
<dl>
<dd>The data path to use with <code>&#8211;extract</code>, the default is to use the fatest data path.</dl>
<p> <code>&#8211;application-property</code> <i>NAME=VALUE</i></p>
<dl>
<dd>Application property to send to the application with <code>&#8211;extract.</code></dl>
<p> <code>-l</code></p>
<dl>
<dd>Leave dumps in the compressed/uncompressed and encrypted/unencrypted state in which they were found on tape. It is a synonym for <code>&#8211;no-decompression</code> <code>&#8211;no-decryption</code></dl>
<p> <code>-a</code></p>
<dl>
<dd>Assume that all tapes are already available, via tape changer or otherwise, instead of prompting the operator to ensure that all tapes are loaded.</dl>
<p> <code>-n</code></p>
<dl>
<dd>Do not reassemble split dump files at all, just restore each piece as an individual file.</dl>
<p> <code>-o</code> <i>configoption</i></p>
<dl>
<dd>See the &quot;<code>CONFIGURATION OVERRIDE</code>&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Examples</h2>
<p>All the examples here assume your configuration is called <i>SetA</i>. </p>
<p> Here&#8217;s a simple case, restoring all known dumps of the host vanya to the current working directory. </p>
<pre>$ amfetchdump SetA vanya</pre>
<p>A more likely scenario involves restoring a particular dump from a particular date. We&#8217;ll pipe this one to <code>GNU-tar</code> as well, to automatically extract the dump. </p>
<pre>$ amfetchdump -p SetA vanya /home 20051020 | gtar -xvpf -</pre>
<h2>Caveats</h2>
<p><code>Amfetchdump</code> is dependent on accessing your server&#8217;s config, tape changer, and (normally) dump logs. As such, it&#8217;s not necessarily the most useful tool when those have all been wiped out and you desperately need to pull things from your tape. Pains have been taken to make it as capable as possible, but for seriously minimialist restores, look to <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8) or <code><a href="/docs/linux/man/8-dd/">dd</a></code>(8) instead.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7), <code><a href="/docs/linux/man/8-amadmin/">amadmin</a></code>(8), <code><a href="/docs/linux/man/8-amrestore/">amrestore</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>John Stange</code> &lt;building [at] nap.edu&gt;</p>
<dl>
<dd>National Academies Press</dl>
<p> <code>Ian Turner</code> &lt;ian [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
