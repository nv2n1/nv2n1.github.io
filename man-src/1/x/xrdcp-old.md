---
title: "xrdcp-old(1)"
name: "xrdcp-old"
section: "1"
letter: "x"
url: "/docs/linux/man/1-xrdcp-old/"
description: "xrdcp-old – copy files"
---

<h2>NAME</h2>
<p> xrdcp-old &#8211; copy files</p>
<h2>SYNOPSIS</h2>
<pre><code>
xrdcp - old[options] source destination
            options : [--cksum args][--debug lvl][--coerce][--force]
                                    [--help][--license][--nopbar][--posc] [--proxy ipaddr:port]
                                    [--recursive][--retry time][--server][--silent]
                                    [--sources num][--streams num][--tpc][--verbose]
                                    [--version][--xrate rate] legacy options : [-adler][-DSparm string][-DIparm number]
                                                                                       [-md5][-np][-ODcgi][-OScgi][-x]
</code></pre>
<h2>DESCRIPTION</h2>
<p> <code>This tool is DEPRECATED. It is what used to be xrdcp prior to xrootd 4.0.0 release. Please use xrdcp instead.</code> </p>
<p> The <code>xrdcp-old</code> utility copies one or more files from one location to another. The data source and destination may be a local or remote file or directory. Additionally, the data source may also reside on multiple servers.</p>
<h2>OPTIONS</h2>
<p> {<code>-C | &#8211;cksum</code>} <i>type</i>[<code>:</code>{<i>value</i>|<code>print</code>}]</p>
<dl>
<dt>
</dt><dd> obtains the checksum of <i>type</i> (i.e. adler32, crc32, or md5) from the source, computes the checksum at the destination, and verifies that they are the same. If a <i>value</i> is specified, it is used as the source checksum. When <code>print</code> is specified, the checksum at the destination is printed but is <i>not</i> verified. </dd>
</dl>
<p> {<code>-d</code> | <code>&#8211;debug</code>} <i>lvl</i></p>
<dl>
<dt>
</dt><dd> debug level: 1 (low), 2 (medium), 3 (high) </dd>
</dl>
<p> {<code>-F</code> | &#8211;coerce}</p>
<dl>
<dt>
</dt><dd> ignores locking semantics on the destination file. This option may lead to file corruption if not properly used. </dd>
</dl>
<p> {<code>-f</code> | <code>&#8211;force</code>}</p>
<dl>
<dt>
</dt><dd> re-creates a file if it is already present. </dd>
</dl>
<p> {<code>-h</code> | &#8211;help}</p>
<dl>
<dt>
</dt><dd> displays usage information. </dd>
</dl>
<p> {<code>-H</code> | &#8211;license}</p>
<dl>
<dt>
</dt><dd> displays license terms and conditions. </dd>
</dl>
<p> {<code>-N</code> | <code>&#8211;nopbar</code>}</p>
<dl>
<dt>
</dt><dd> does not display the progress bar. </dd>
</dl>
<p> {<code>-P</code> | <code>&#8211;posc</code>}</p>
<dl>
<dt>
</dt><dd> requests POSC (persist-on-successful-close) processing to create a new file. Files are automatically deleted should they not be successfully closed. </dd>
</dl>
<p> {<code>-D</code> | <code>&#8211;proxy</code>} <i>proxyaddr</i><code>:</code><i>proxyport</i></p>
<dl>
<dt>
</dt><dd> use <i>proxyaddr</i><code>:</code><i>proxyport</i> as a SOCKS4 proxy. Only numerical addresses are supported. </dd>
</dl>
<p> {<code>-r</code> | <code>&#8211;recursive</code>}</p>
<dl>
<dt>
</dt><dd> recursively copy all files starting at the given source directory. This option is <i>only</i> supported for local files. </dd>
</dl>
<p> <code>&#8211;server</code></p>
<dl>
<dt>
</dt><dd> runs as if in a server environment. Used only for server-side third party copy support. </dd>
</dl>
<p> {<code>-s</code> | <code>&#8211;silent</code>}</p>
<dl>
<dt>
</dt><dd> neither produces summary information nor displays the progress bar. </dd>
</dl>
<p> {<code>-y</code> | <code>&#8211;sources</code>} <i>num</i></p>
<dl>
<dt>
</dt><dd> uses up to <i>num</i> sources to copy the file. </dd>
</dl>
<p> {<code>-S</code> | <code>&#8211;streams</code>} <i>num</i></p>
<dl>
<dt>
</dt><dd> uses <i>num</i> additional parallel streams to do the transfer. The maximum value is 15. The default is 0 (i.e., use only the main stream). </dd>
</dl>
<p> <code>&#8211;tpc</code></p>
<dl>
<dt>
</dt><dd> copies the file from remote server to remote server using third-party-copy protocol (i.e., data flows from server to server). The source and destination servers must support third party copies. Additional security restrictions may apply and may cause the copy to fail if they cannot be satisfied. </dd>
</dl>
<p> {<code>-v</code> | <code>&#8211;verbose</code>}</p>
<dl>
<dt>
</dt><dd> displays summary output. </dd>
</dl>
<p> {<code>-V</code> | <code>-version</code>}</p>
<dl>
<dt>
</dt><dd> displays version information and immediately exits. </dd>
</dl>
<p> {<code>-X</code> | <code>&#8211;xrate</code>} <i>rate</i></p>
<dl>
<dt>
</dt><dd> limits the copy speed to the specified <i>rate</i><code>. The rate may be qualified with the letter k</code>, <code>m</code>, or <code>g</code> to indicate kilo, mega, or giga bytes, respectively. The option only applies when the source or destination is local. </dd>
</dl>
<h2>LEGACY OPTIONS</h2>
<p> Legacy options are provided for backward compatability. These are now deprecated and should be avoided. <code>&#8211;adler</code></p>
<dl>
<dt>
</dt><dd> equivalent to &quot;<code>&#8211;cksum adler32:print</code>&quot;. </dd>
</dl>
<p> <code>-DI</code><i>pname numberval</i></p>
<dl>
<dt>
</dt><dd> set the internal parameter <i>pname</i> with the numeric value <i>numberval</i>. </dd>
</dl>
<p> <code>-DS</code><i>pname stringval</i></p>
<dl>
<dt>
</dt><dd> set the internal parameter <i>pname</i> with the string value <i>stringval</i>. </dd>
</dl>
<p> <code>-md5</code></p>
<dl>
<dt>
</dt><dd> equivalent to &quot;<code>&#8211;cksum md5:print</code>&quot;. </dd>
</dl>
<p> <code>-np</code></p>
<dl>
<dt>
</dt><dd> equivalent to &quot;<code>&#8211;nopbar</code>&quot;. </dd>
</dl>
<p> <code>-OD</code><i>cgi</i></p>
<dl>
<dt>
</dt><dd> add cgi information <i>cgi</i> to any destination xrootd URL. You should specify the opaque information directly on the destination URL. </dd>
</dl>
<p> <code>-OS</code><i>cgi</i></p>
<dl>
<dt>
</dt><dd> add cgi information <i>cgi</i> to any source xrootd URL. </dd>
</dl>
<p> <code>-x</code></p>
<dl>
<dt>
</dt><dd> equivalent to &quot;<code>&#8211;sources 12</code>&quot;. </dd>
</dl>
<h2>OPERANDS</h2>
<p> <i>source</i></p>
<dl>
<dt>
</dt><dd> a local file, a local directory name suffixed by /, or an xrootd URL in the form of <center> <code><a href="xroot://[">xroot://[</a></code><i>user</i><code>@</code>]<i>host[</i><code>:</code><i>port</i>]<code>/</code><i>absolutepath</i><br />
 </center> The <i>absolutepath</i> can be a directory. </dd>
</dl>
<p> <i>destination</i></p>
<dl>
<dt>
</dt><dd> a dash (i.e. <code>&#8211;</code>) indicating stanard out, a local file, a local directory name suffixed by /, or an xrootd URL in the form <center> <code><a href="xroot://[">xroot://[</a></code><i>user</i><code>@</code>]<i>host[</i><code>:</code><i>port</i>]<code>/</code><i>absolutepath</i><br />
 </center> The <i>absolutepath</i> can be a directory. </dd>
</dl>
<h2>EXAMPLES (GENERIC)</h2>
<dl>
<dt>local file upload:</dt>
<dd>
 <code>$ xrdcp-old /tmp/myfile <a href="xroot://foo.bar.com//data/myfile">xroot://foo.bar.com//data/myfile</a></code> </dd>
<dt>remote file download:</dt>
<dd>
 <code>$ xrdcp-old <a href="xroot://foo.bar.com//data/myfile">xroot://foo.bar.com//data/myfile</a> /tmp/myfile</code> </dd>
<dt>remote-remote copy:</dt>
<dd>
 <code>$ xrdcp-old <a href="xroot://foo.bar.com//data/myfile1">xroot://foo.bar.com//data/myfile1</a> <a href="xroot://foo.bar.com//data/myfile2">xroot://foo.bar.com//data/myfile2</a></code> </dd>
</dl>
<h2>EXAMPLES (CASTOR)</h2>
<dl>
<dt>local file upload to a Castor instance using a specific service class and stager:</dt>
<dd>
 <code>$ xrdcp-old /tmp/myfile root://&lt;stagerhost&gt;.cern.ch//castor/cern.ch/data/myfile -ODstagerHost=$STAGE_HOST&amp;svcClass=$STAGE_SVCCLASS</code><br />
 [ you need to escape the &#8216;&amp;&#8217; in the shell ]</dd>
<dt>remote file download from a Castor instance using a specific stager:</dt>
<dd>
 <code>$ xrdcp-old /tmp/myfile root://&lt;stagerhost&gt;.cern.ch//castor/cern.ch/data/myfile -OSstagerHost=$STAGE_HOST</code></dd>
<dt>client-proxy copy to-/from- a Castor instance:</dt>
<dd>
 <code>$ xrdcp-old</code><br />
 <code>root://&lt;stagerA&gt;.cern.ch//castor/cern.ch/data/stagerA/myfile -OSstagerHost=&lt;stagerA&gt;</code><br />
 <code>root://&lt;stagerB&gt;.cern.ch//castor/cern.ch/data/stagerB/myfile -ODstagerHost=&lt;stagerA&gt;</code> </dd>
<p> [ you cannot copy between stagers using the same logical filename in the castor namespace! ]</dl>
<h2>NOTES</h2>
<p> Documentation for all components associated with <code>xrdcp-old</code> can be found at <a rel="nofollow" href="http://xrootd.org/docs.html">http://xrootd.org/docs.html</a></p>
<h2>DIAGNOSTICS</h2>
<p> Errors yield an error message and a non-zero exit status.</p>
<h2>LICENSE</h2>
<p> License terms can be displayed by typing &quot;<code>xrootd -H</code>&quot;.</p>
<h2>SUPPORT LEVEL</h2>
<p> The <code>xrdcp</code> command is supported by the xrootd collaboration. Contact information can be found at <center> <a rel="nofollow" href="http://xrootd.org/contact.html">http://xrootd.org/contact.html</a><br />
 </center> </p>
