---
title: "maildropgdbm(7)"
name: "maildropgdbm"
section: "7"
letter: "m"
url: "/docs/linux/man/7-maildropgdbm/"
description: "maildropgdbm – GDBM/DB support in maildrop"
---

<p>maildropgdbm &#8211; GDBM/DB support in maildrop</p>
<h2>Synopsis</h2>
<pre>gdbmopen(filename, mode)
gdbmclose
gdbmfetch(key [,default])
gdbmstore(key,value)</pre>
<h2>Description</h2>
<p>The gdbm family of functions provides access to the GDBM library &#8211; a library of routines that manage simple database files. The library provides a way of quickly storing and looking up key/data pairs. GDBM support in <code>maildrop</code> is optional, and may not be available to you. GDBM support in <code>maildrop</code> can optionally be implemented using the DB library. This option is selected by the system administrator. If this is the case, these functions still work exactly as described below, except that they will operate on DB hash files, instead of GDBM files. To see whether GDBM or DB support is used, run the command &quot;<code>maildrop -v&quot;</code>. GDBM support is minimal, and simplistic. A filter file may have only one gdbm file open at the same time. However, the filter file can close the current gdbm file, and open another one. If another filter file is included using the include statement, the included filter file may open its own, separate, gdbm file. A GDBM file contains a list of key/value pairs. All keys in the GDBM file are unique. After storing an arbitrary key/value pair in the GDBM file, the value associated with the given key can be quickly located and retrieved.</p>
<h3>gdbmclose &#8211; close gdbm file</h3>
<dl>
<dd>
<pre>gdbmclose</pre>
</dl>
<p> This function closes the current GDBM file.</p>
<h3>gdbmfetch &#8211; retrieve data</h3>
<dl>
<dd>
<pre>gdbmfetch (<i>key</i> [, <i>options</i>] [, <i>default</i>])</pre>
</dl>
<p> This function retrieves the data for the given key. <i>key</i> is the key to retrieve. The <code>gdbmfetch</code> function returns the data associated with this key. If the key does not exist in the GDBM file, <code>gdbmfetch</code> returns the <code>default</code> argument. If the <code>default</code> argument is not specified, <code>gdbmfetch</code> returns empty text. Please note that the <code>default</code> argument is not actually evaluated unless the key does not exist in the GDBM file. The <i>options</i> argument specifies additional <code>maildrop</code> value-added features. The following functionality is not available in the GDBM library, but is rather provided by <code>maildrop</code>. If the <i>options</i> argument is set to &quot;D&quot;, and the key could not be found in the GDBM database, and the key is of the form &quot;user [at] domain&quot;, <code>maildrop</code> will then attempt to look up the key &quot;user@&quot;. If that key is also not found, <code>maildrop</code> finally looks up the key &quot;domain&quot;. If &quot;domain&quot; is also not found, and domain is of the form &quot;a.b.c.d.tld&quot; (with variable number of period-separated sections), <code>maildrop</code> then attempts to look up the key &quot;b.c.d.tld&quot;. If that key is not found, <code>maildrop</code> tries &quot;c.d.tld&quot;, and so on, until a key is found, or there are no more subdomains to remove, at which point <code>gdbmfetch</code> will return either the <code>default</code> argument, or empty text. If the <i>options</i> argument is set to &quot;D&quot;, and the key could not be found in the GDBM database, and the key is of the form &quot;a.b.c.d.tld&quot; (with variable number of period-separated sections), <code>maildrop</code> will also attempt to look up keys for successive higher-level domains in the GDBM database.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 GDBM databases are case sensitive. Make sure that the GDBM database is created using lowercase letters only, and use the m[blue]<code>tolower</code>m[]<font SIZE="-2">[1]</font> function to convert the key to lowercase.  If the <i>options</i> argument is &quot;I&quot;, and the key is not in the GDBM database, and the key is of the form &quot;w.x.y.z&quot; (with variable number of period-separated sections), <code>maildrop</code> then tries to look up the key &quot;w.x.y&quot;, then &quot;w.x&quot;, until a key is found, or there are no more sections to remove. Use this feature to look up IP-address based GDBM lists.</p>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 These features are implemented by brute force: if the query doesn&#8217;t succeed, try again. Take note of potential denial-of-service attacks where key is set to a long text string consisting mostly of periods, which will result in numerous GDBM queries that will take an excessive amount of time to complete.</dl>
<h3>gdbmopen &#8211; open gdbm file</h3>
<dl>
<dd>
<pre>gdbmopen (<i>file</i> [, <i>mode</i>])</pre>
</dl>
<p> <code>gdbmopen</code> opens the indicated GDBM file. The optional second argument specifies the following: &quot;R&quot;</p>
<dl>
<dd>Open this GDBM file for reading.</dl>
<p> &quot;W&quot;</p>
<dl>
<dd>Open this GDBM file for reading and writing.</dl>
<p> &quot;C&quot;</p>
<dl>
<dd>Open this GDBM file for reading and writing. If the GBDM file doesn&#8217;t exist, create it.</dl>
<p> &quot;N&quot;</p>
<dl>
<dd>Create a new GDBM file. If the file exists, the existing file is deleted. The file is opened for reading and writing.</dl>
<p> The <i>mode</i> argument defaults to &quot;R&quot; is used. In embedded mode, only &quot;R&quot; is allowed. The GDBM library allows multiple processes to read the same GDBM file at the same time, but it does not allow multiple access when the GDBM file is open for writing. Using m[blue]<code>flock</code>m[]<font SIZE="-2">[2]</font> or m[blue]<code>dotlock</code>m[]<font SIZE="-2">[3]</font> is highly recommended. In delivery mode, <code>maildrop</code> runs from the recipient&#8217;s home directory. Keep that in mind while specifying the filename. The gdbmopen function returns 0 if the GDBM file was successfully opened, non-zero otherwise.</p>
<h3>gdbmstore &#8211; store data</h3>
<dl>
<dd>
<pre>gdbmstore(<i>key</i>, <i>value</i>)</pre>
</dl>
<p> <i>key</i> is the key value to store in the GDBM file. <i>value</i> is the value to store. If <i>key</i> already exists in the GDBM file, <i>value</i> replacest the old value. The <code>gdbmstore</code> function is only permitted if the GDBM file is opened for writing. If <i>gdbmopen</i> opened the GDBM file for reading only, <code>gdbmstore</code> will return -1. Otherwise, <code>gdbmstore</code> returns 0.</p>
<h2>Author</h2>
<p><code>Sam Varshavchik</code></p>
<dl>
<dd>Author</dl>
<h2>Notes</h2>
<dl>
<dt> 1.</p>
<dd><code>tolower</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#tolower">http://www.courier-mta.org/maildrop/maildropfilter.html#tolower</a></dl>
<dt> 2.</p>
<dd><code>flock</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#flock">http://www.courier-mta.org/maildrop/maildropfilter.html#flock</a></dl>
<dt> 3.</p>
<dd><code>dotlock</code></p>
<dl>
<dd><a rel="nofollow" href="http://www.courier-mta.org/maildrop/maildropfilter.html#dotlock">http://www.courier-mta.org/maildrop/maildropfilter.html#dotlock</a></dl>
