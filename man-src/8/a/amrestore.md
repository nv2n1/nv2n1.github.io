---
title: "amrestore(8)"
name: "amrestore"
section: "8"
letter: "a"
url: "/docs/linux/man/8-amrestore/"
description: "amrestore – low-level data-extraction from Amanda volumes"
---

<p>amrestore &#8211; low-level data-extraction from Amanda volumes</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>amrestore</code> [&#8211;config&nbsp;<wbr><i>config</i>] [-r | -c | -C] [-b&nbsp;<wbr><i>blocksize</i>] [-f&nbsp;<wbr><i>filenum</i>] [-l&nbsp;<wbr><i>label</i>] [-p] [-h] [&#8211;exact-match] [<code>-o</code>&nbsp;<wbr><i>configoption</i>&#8230;] [{<i>changerspec</i>} | {[&#8211;holding]&nbsp;<wbr><i>holdingfile</i>}] [<i>hostname</i>&nbsp;<wbr>[&nbsp;<wbr><i>diskname</i>&nbsp;<wbr>[&nbsp;<wbr><i>datestamp</i>&nbsp;<wbr>[&nbsp;<wbr><i>hostname</i>&nbsp;<wbr>[&nbsp;<wbr><i>diskname</i>&nbsp;<wbr>[&nbsp;<wbr><i>datestamp</i>&nbsp;<wbr>&#8230;&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]&nbsp;<wbr>]]</dl>
<dd>Note that this is the only Amanda command which does not take a configuration name as its first argument.</p>
<h2>Description</h2>
<p><i>Amrestore</i> is a very low-level tool for extracting data from Amanda volumes. It does not consult any catalog information or other metadata, basing its operations only on the headers found on the volume. This makes it an appropriate tool for bare-metal restores of an Amanda server, or other situations where the catalog is not available. </p>
<p> See <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8) and <code><a href="/docs/linux/man/8-amrecover/">amrecover</a></code>(8) for higher-level recoveries. </p>
<p> The tool does not reassemble split dumps, but can uncompress compressed dumps. Note that decompression may fail for split parts after the first. If this occurs, extract the parts without decompressing, concatenate them, and decompress the result. </p>
<p> Data is restored from the current volume in <i>changerspec</i>, or from the holding file <i>holdingfile</i>. In most cases, <i>changerspec</i> will name a particular device, e.g., tape:/dev/nst0 or s3:mybucket/tape-1. </p>
<p> Only dumps matching the dump specification beginning with <i>hostname</i> are extracted. If no specification is given, every file on the volume (or the entire holdingfile) is restored. See the &quot;DUMP SPECIFICATIONS&quot; section of <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7) for more information. </p>
<p> Unless <code>-p</code> is used, candidate backup images are extracted to files in the current directory named: hostname.diskname.datestamp.dumplevel</p>
<h2>Options</h2>
<p><code>-b </code><i>blocksize</i></p>
<dl>
<dd>Use the given blocksize to read the volume. The default is defined by the device.</dl>
<p> <code>-f </code><i>filenum</i></p>
<dl>
<dd>Seek to file <i>filenum</i> before beginning the restore operation.</dl>
<p> <code>-l </code><i>label</i></p>
<dl>
<dd>Check that the volume has label <i>label</i>.</dl>
<p> <code>-p</code></p>
<dl>
<dd>Pipe the first matching file to standard output. This is typically used in a shell pipeline to send the data to a process like <code>tar</code> for extraction.</dl>
<p> <code>-c</code>, <code>-C</code></p>
<dl>
<dd>If the file is not already compressed, compress it using the fastest (<code>-c</code>) or best (<code>-C</code>) compression algorithm. Note that <code>amrestore</code> will not re-compress an already-compressed file. Without either of these options, <code>amrestore</code> will automatically uncompress any compressed files. This option is useful when the destination disk is small.</dl>
<p> <code>-h</code></p>
<dl>
<dd>Include 32k headers on all output files, similar to a holding file. This header can be read by another application or utility (see <code>Amanda::Header</code>) during the next phase of processing.</dl>
<p> <code>-r</code></p>
<dl>
<dd>Output raw files. This is similar to <code>-h</code>, but also disables any automatic decompression. Output file names will have a .RAW extension.</dl>
<p> <code>&#8211;exact-match</code></p>
<dl>
<dd>The host and disk are parsed as exact values</dl>
<p> <code>-o </code><i>configoption</i></p>
<dl>
<dd>See the &quot;CONFIGURATION OVERRIDE&quot; section in <code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8).</dl>
<h2>Examples</h2>
<p>The following does an interactive restore of disk <i>rz3g</i> from host <i>seine</i>, to restore particular files. Note the use of the <i>b</i> option to <i>restore</i>, which causes it to read in units of two 512-byte blocks (1 Kbyte) at a time. This helps keep it from complaining about short reads. </p>
<pre> amrestore -p /dev/nrmt9 seine rz3g | tar -xv</pre>
<p>The next example extracts all backup images for host <i>seine</i>. This is a typical way to extract all data for a host after a disk crash. </p>
<pre> amrestore /dev/nrmt9 seine</pre>
<p>If the backup datestamp in the above example is 20070125 and <i>seine</i> has level 0 backups of disks <i>rz1a</i> and <i>rz1g</i> on the tape, these files will be created in the current directory: </p>
<pre> seine.rz1a.19910125.0
 seine.rz1g.19910125.0</pre>
<p>You may also use <code>amrestore</code> to extract a backup image from a holding disk file that has not yet been flushed to tape: </p>
<pre> amrestore -p /amanda/20001119/seine.rz1a.2 | tar -xv</pre>
<h2>Caveats</h2>
<p><code>GNU-tar</code> must be used to restore files from backup images created with the GNUTAR dumptype. Vendor tar programs sometimes fail to read GNU Tar images.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-amanda/">amanda</a></code>(8), <code><a href="/docs/linux/man/7-amanda-match/">amanda-match</a></code>(7), <code><a href="/docs/linux/man/8-amfetchdump/">amfetchdump</a></code>(8), <code><a href="/docs/linux/man/8-amrecover/">amrecover</a></code>(8) </p>
<p> The Amanda Wiki: : <a rel="nofollow" href="http://wiki.zmanda.com/">http://wiki.zmanda.com/</a></p>
<h2>Authors</h2>
<p><code>James da Silva</code> &lt;jds [at] amanda.org&gt; </p>
<p> <code>Stefan G. Weichinger</code> &lt;sgw [at] amanda.org&gt; </p>
<p> <code>Dustin J. Mitchell</code> &lt;dustin [at] zmanda.com&gt;</p>
<dl>
<dd>Zmanda, Inc. (<a rel="nofollow" href="http://www.zmanda.com)">http://www.zmanda.com)</a></dl>
