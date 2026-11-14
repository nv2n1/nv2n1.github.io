---
title: "osspuuid(3)"
name: "osspuuid"
section: "3"
letter: "o"
url: "/docs/linux/man/3-osspuuid/"
description: "OSSP::uuid – OSSP uuid Perl Binding"
---

<p>OSSP::uuid &#8211; OSSP uuid Perl Binding </p>
<h2>Description</h2>
<p><font SIZE="-1"><code>OSSP</code></font><code> uuid</code> is a <font SIZE="-1">ISO-C:1999</font> application programming interface (<font SIZE="-1">API</font>) and corresponding command line interface (<font SIZE="-1">CLI</font>) for the generation of <font SIZE="-1">DCE 1.1, ISO/IEC 11578:1996</font> and <font SIZE="-1">RFC 4122</font> compliant <i>Universally Unique Identifier</i> (<font SIZE="-1">UUID</font>). It supports <font SIZE="-1">DCE 1.1</font> variant UUIDs of version 1 (time and node based), version 3 (name based, <font SIZE="-1">MD5</font>), version 4 (random number based) and version 5 (name based, <font SIZE="-1">SHA-1</font>). Additional <font SIZE="-1">API</font> bindings are provided for the languages <font SIZE="-1">ISO-C<font SIZE="-2">++</font>:1998,</font> Perl:5 and <font SIZE="-1">PHP:4/5.</font> Optional backward compatibility exists for the ISO-C <font SIZE="-1">DCE-1.1</font> and Perl Data::UUID APIs. </p>
<p> <code>OSSP::uuid</code> is the Perl binding to the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> <font SIZE="-1">API.</font> Three variants are provided:</p>
<h3>TIE-STYLE <font SIZE="-1">API</font></h3>
<p>The TIE-style <font SIZE="-1">API</font> is a functionality-reduced wrapper around the OO-style <font SIZE="-1">API</font> and intended for very high-level convenience programming:</p>
<dl COMPACT>
<dt>&quot;use OSSP::uuid;&quot;</p>
<dd>
<dt><code>tie</code>&quot; my $uuid, &#8216;OSSP::uuid::tie&#8217;, $mode, &#8230;;&quot;</p>
<dd>
<dt>&quot;$uuid = [ $mode, &#8230; ];&quot;</p>
<dd>
<dt>&quot;print &quot;UUID=$uuid
&quot;;&quot;</p>
<dd>
<dt>&quot;untie $uuid;&quot;</p>
<dd></dl>
<h3>OO-STYLE <font SIZE="-1">API</font></h3>
<p>The OO-style <font SIZE="-1">API</font> is a wrapper around the C-style <font SIZE="-1">API</font> and intended for high-level regular programming.</p>
<dl COMPACT>
<dt>&quot;use OSSP::uuid;&quot;</p>
<dd>
<dt>&quot;my $uuid = &quot;<code>new</code>&quot; OSSP::uuid;&quot;</p>
<dd>
<dt>&quot;$uuid-&gt;&quot;<code>load</code>&quot;($name);&quot;</p>
<dd>
<dt>&quot;$uuid-&gt;&quot;<code>make</code>&quot;($mode, &#8230;);&quot;</p>
<dd>
<dt>&quot;$result = $uuid-&gt;&quot;<code>isnil</code>&quot;();&quot;</p>
<dd>
<dt>&quot;$result = $uuid-&gt;&quot;<code>compare</code>&quot;($uuid2);&quot;</p>
<dd>
<dt>&quot;$uuid-&gt;&quot;<code>import</code>&quot;($fmt, $data_ptr);&quot;</p>
<dd>
<dt>&quot;$data_ptr = $uuid-&gt;&quot;<code>export</code>&quot;($fmt);&quot;</p>
<dd>
<dt>&quot;[(]$str[, $rc)] = $uuid-&gt;&quot;<code>error</code>&quot;();&quot;</p>
<dd>
<dt>&quot;$ver = $uuid-&gt;&quot;<code>version</code>&quot;();&quot;</p>
<dd>
<dt>&quot;undef $uuid;&quot;</p>
<dd></dl>
<p> Additionally, the strings <tt>&quot;v1&quot;</tt>, <tt>&quot;v3&quot;</tt>, <tt>&quot;v4&quot;</tt>, <tt>&quot;v5&quot;</tt> and <tt>&quot;mc&quot;</tt> can be used in <tt>$mode</tt> and the strings <tt>&quot;bin&quot;</tt>, <tt>&quot;str&quot;</tt>, and <tt>&quot;txt&quot;</tt> can be used for <tt>$fmt</tt>.</p>
<h3>C-STYLE <font SIZE="-1">API</font></h3>
<p>The C-style <font SIZE="-1">API</font> is a direct mapping of the <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> ISO-C <font SIZE="-1">API</font> to Perl and is intended for low-level programming. See <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3) for a description of the functions and their expected arguments.</p>
<dl COMPACT>
<dt>&quot;use OSSP::uuid qw(:all);&quot;</p>
<dd>
<dt>&quot;my $uuid; $rc = &quot;<code>uuid_create</code>&quot;($uuid);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_load</code>&quot;($uuid, $name);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_make</code>&quot;($uuid, $mode, &#8230;);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_isnil</code>&quot;($uuid, $result);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_compare</code>&quot;($uuid, $uuid2, $result);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_import</code>&quot;($uuid, $fmt, $data_ptr, $data_len);&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_export</code>&quot;($uuid, $fmt, $data_ptr, $data_len);&quot;</p>
<dd>
<dt>&quot;$str = &quot;<code>uuid_error</code>&quot;($rc);&quot;</p>
<dd>
<dt>&quot;$ver = &quot;<code>uuid_version</code>&quot;();&quot;</p>
<dd>
<dt>&quot;$rc = &quot;<code>uuid_destroy</code>&quot;($uuid);&quot;</p>
<dd></dl>
<p> Additionally, the following constants are exported for use in <tt>$rc</tt>, <tt>$mode</tt>, <tt>$fmt</tt> and <tt>$ver</tt>: </p>
<p> <tt>&quot;UUID_VERSION&quot;</tt>, <tt>&quot;UUID_LEN_BIN&quot;</tt>, <tt>&quot;UUID_LEN_STR&quot;</tt>, <tt>&quot;UUID_RC_OK&quot;</tt>, <tt>&quot;UUID_RC_ARG&quot;</tt>, <tt>&quot;UUID_RC_MEM&quot;</tt>, <tt>&quot;UUID_RC_SYS&quot;</tt>, <tt>&quot;UUID_RC_INT&quot;</tt>, <tt>&quot;UUID_RC_IMP&quot;</tt>, <tt>&quot;UUID_MAKE_V1&quot;</tt>, <tt>&quot;UUID_MAKE_V3&quot;</tt>, <tt>&quot;UUID_MAKE_V4&quot;</tt>, <tt>&quot;UUID_MAKE_V5&quot;</tt>, <tt>&quot;UUID_MAKE_MC&quot;</tt>, <tt>&quot;UUID_FMT_BIN&quot;</tt>, <tt>&quot;UUID_FMT_STR&quot;</tt>, <tt>&quot;UUID_FMT_SIV&quot;</tt>, <tt>&quot;UUID_FMT_TXT&quot;</tt>.</p>
<h2>Examples</h2>
<p>The following two examples create the version 3 <font SIZE="-1">UUID </font><tt>&quot;02d9e6d5-9467-382e-8f9b-9300a64ac3cd&quot;</tt>, both via the OO-style and the C-style <font SIZE="-1">API.</font> Error handling is omitted here for easier reading, but has to be added for production-quality code. </p>
<pre> # TIE-style API (very high-level)
 use OSSP::uuid;
 tie my $uuid, 'OSSP::uuid::tie';
 $uuid = [ &quot;v1&quot; ];
 print &quot;UUIDs: $uuid, $uuid, $uuid
&quot;;
 $uuid = [ &quot;v3&quot;, &quot;ns:URL&quot;, &quot;<a rel="nofollow" href="http://www.ossp.org/">http://www.ossp.org/</a>&quot; ];
 print &quot;UUIDs: $uuid, $uuid, $uuid
&quot;;
 untie $uuid;
 # OO-style API (high-level)
 use OSSP::uuid;
 my $uuid = new OSSP::uuid;
 my $uuid_ns = new OSSP::uuid;
 $uuid_ns-&gt;load(&quot;ns:URL&quot;);
 $uuid-&gt;make(&quot;v3&quot;, $uuid_ns, &quot;<a rel="nofollow" href="http://www.ossp.org/">http://www.ossp.org/</a>&quot;);
 undef $uuid_ns;
 my $str = $uuid-&gt;export(&quot;str&quot;);
 undef $uuid;
 print &quot;$str
&quot;;
 # C-style API (low-level)
 use OSSP::uuid qw(:all);
 my $uuid; uuid_create($uuid);
 my $uuid_ns; uuid_create($uuid_ns);
 uuid_load($uuid_ns, &quot;ns:URL&quot;);
 uuid_make($uuid, UUID_MAKE_V3, $uuid_ns, &quot;<a rel="nofollow" href="http://www.ossp.org/">http://www.ossp.org/</a>&quot;);
 uuid_destroy($uuid_ns);
 my $str; uuid_export($uuid, UUID_FMT_STR, $str, undef);
 uuid_destroy($uuid);
 print &quot;$str
&quot;;</pre>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/1-uuid/">uuid</a></i>(1), <i><a href="/docs/linux/man/1-uuid-config/">uuid-config</a></i>(1), <i><a href="/docs/linux/man/3-uuid/">uuid</a></i>(3).</p>
<h2>History</h2>
<p>The Perl binding <code>OSSP::uuid</code> to <font SIZE="-1"><code>OSSP</code></font><code> uuid</code> was implemented in November 2004 by Ralf S. Engelschall &lt;rse [at] engelschall.com&gt;.</p>
