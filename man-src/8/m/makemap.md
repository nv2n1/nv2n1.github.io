---
title: "makemap(8)"
name: "makemap"
section: "8"
letter: "m"
url: "/docs/linux/man/8-makemap/"
description: "makemap – create database maps for sendmail"
---

<p>makemap &#8211; create database maps for sendmail</p>
<h2>Synopsis</h2>
<p><code>makemap</code> [<code>-C</code> <i>file</i>] [<code>-N</code>] [<code>-c</code> <i>cachesize</i>] [<code>-d</code>] [<code>-D</code> <i>commentchar</i>] [<code>-e</code>] [<code>-f</code>] [<code>-l</code>] [<code>-o</code>] [<code>-r</code>] [<code>-s</code>] [<code>-t</code> <i>delim</i>] [<code>-u</code>] [<code>-v</code>] <i>maptype mapnam</i></p>
<h2>Description</h2>
<p><code>Makemap</code> creates the database maps used by the keyed map lookups in sendmail(8). It reads input from the standard input and outputs them to the indicated <i>mapname.</i> </p>
<p> Depending on how it is compiled, <code>makemap</code> handles up to three different database formats, selected using the <i>maptype</i> parameter. They may be</p>
<dl>
<dt>btree</dt>
<dd>B-Tree format maps. This requires the new Berkeley DB library.</dd>
<dt>hash</dt>
<dd>Hash format maps. This also requires the Berkeley DB library.</dd></dl>
<p> In all cases, <code>makemap</code> reads lines from the standard input consisting of two words separated by white space. The first is the database key, the second is the value. The value may contain &#8220;%<i>n</i>&#8221; strings to indicate parameter substitution. Literal percents should be doubled (&#8220;%%&#8221;). Blank lines and lines beginning with &#8220;#&#8221; are ignored. </p>
<p> Notice: do <code>not</code> use <code>makemap</code> to create the aliases data base, but <code>newaliases</code> which puts a special token into the data base that is required by <code>sendmail.</code> </p>
<p> If the <i>TrustedUser</i> option is set in the sendmail configuration file and <code>makemap</code> is invoked as root, the generated files will be owned by the specified <i>TrustedUser.</i></p>
<h3>Flags</h3>
<dl>
<dt><code>-C</code></dt>
<dd>Use the specified <code>sendmail</code> configuration file for looking up the TrustedUser option.</dd>
<dt><code>-N</code></dt>
<dd>Include the null byte that terminates strings in the map. This must match the -N flag in the sendmail.cf &#8220;K&#8221; line.</dd>
<dt><code>-c</code></dt>
<dd>Use the specified hash and B-Tree cache size.</dd>
<dt><code>-D</code></dt>
<dd>Use to specify the character to use to indicate a comment (which is ignored) instead of the default of &#8216;#&#8217;.</dd>
<dt><code>-d</code></dt>
<dd>Allow duplicate keys in the map. This is only allowed on B-Tree format maps. If two identical keys are read, they will both be inserted into the map.</dd>
<dt><code>-e</code></dt>
<dd>Allow empty value (right hand side).</dd>
<dt><code>-f</code></dt>
<dd>Normally all upper case letters in the key are folded to lower case. This flag disables that behaviour. This is intended to mesh with the -f flag in the <code>K </code> line in sendmail.cf. The value is never case folded.</dd>
<dt><code>-l</code></dt>
<dd>List supported map types.</dd>
<dt><code>-o</code></dt>
<dd>Append to an old file. This allows you to augment an existing file.</dd>
<dt><code>-r</code></dt>
<dd>Allow replacement of existing keys. Normally <code>makemap</code> complains if you repeat a key, and does not do the insert.</dd>
<dt><code>-s</code></dt>
<dd>Ignore safety checks on maps being created. This includes checking for hard or symbolic links in world writable directories.</dd>
<dt><code>-t</code></dt>
<dd>Use the specified delimiter instead of white space (also for dumping a map).</dd>
<dt><code>-u</code></dt>
<dd>dump (unmap) the content of the database to standard output.</dd>
<dt><code>-v</code></dt>
<dd>Verbosely print what it is doing.</dd></dl>
<h2>See Also</h2>
<p>sendmail(8), <a href="/docs/linux/man/1-newaliases/">newaliases</a>(1)</p>
<h2>History</h2>
<p>The <code>makemap</code> command appeared in 4.4BSD.</p>
