---
title: "named-checkzone(8)"
name: "named-checkzone"
section: "8"
letter: "n"
url: "/docs/linux/man/8-named-checkzone/"
description: "named-checkzone, named-compilezone – zone file validity checking or converting tool"
---

<p>named-checkzone, named-compilezone &#8211; zone file validity checking or converting tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named-checkzone</code> [<code>-d</code>] [<code>-h</code>] [<code>-j</code>] [<code>-q</code>] [<code>-v</code>] [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-f&nbsp;<wbr></code><i>format</i>] [<code>-F&nbsp;<wbr></code><i>format</i>] [<code>-i&nbsp;<wbr></code><i>mode</i>] [<code>-k&nbsp;<wbr></code><i>mode</i>] [<code>-m&nbsp;<wbr></code><i>mode</i>] [<code>-M&nbsp;<wbr></code><i>mode</i>] [<code>-n&nbsp;<wbr></code><i>mode</i>] [<code>-L&nbsp;<wbr></code><i>serial</i>] [<code>-o&nbsp;<wbr></code><i>filename</i>] [<code>-r&nbsp;<wbr></code><i>mode</i>] [<code>-s&nbsp;<wbr></code><i>style</i>] [<code>-S&nbsp;<wbr></code><i>mode</i>] [<code>-t&nbsp;<wbr></code><i>directory</i>] [<code>-T&nbsp;<wbr></code><i>mode</i>] [<code>-w&nbsp;<wbr></code><i>directory</i>] [<code>-D</code>] [<code>-W&nbsp;<wbr></code><i>mode</i>] {zonename} {filename}</p>
<dt> <code>named-compilezone</code> [<code>-d</code>] [<code>-j</code>] [<code>-q</code>] [<code>-v</code>] [<code>-c&nbsp;<wbr></code><i>class</i>] [<code>-C&nbsp;<wbr></code><i>mode</i>] [<code>-f&nbsp;<wbr></code><i>format</i>] [<code>-F&nbsp;<wbr></code><i>format</i>] [<code>-i&nbsp;<wbr></code><i>mode</i>] [<code>-k&nbsp;<wbr></code><i>mode</i>] [<code>-m&nbsp;<wbr></code><i>mode</i>] [<code>-n&nbsp;<wbr></code><i>mode</i>] [<code>-L&nbsp;<wbr></code><i>serial</i>] [<code>-r&nbsp;<wbr></code><i>mode</i>] [<code>-s&nbsp;<wbr></code><i>style</i>] [<code>-t&nbsp;<wbr></code><i>directory</i>] [<code>-T&nbsp;<wbr></code><i>mode</i>] [<code>-w&nbsp;<wbr></code><i>directory</i>] [<code>-D</code>] [<code>-W&nbsp;<wbr></code><i>mode</i>] {<code>-o&nbsp;<wbr></code><i>filename</i>} {zonename} {filename}</dl>
<h2>Description</h2>
<p><code>named-checkzone</code></p>
<dd>checks the syntax and integrity of a zone file. It performs the same checks as <code>named</code> does when loading a zone. This makes <code>named-checkzone</code> useful for checking zone files before configuring them into a name server. </p>
<p> <code>named-compilezone</code> is similar to <code>named-checkzone</code>, but it always dumps the zone contents to a specified file in a specified format. Additionally, it applies stricter check levels by default, since the dump output will be used as an actual zone file loaded by <code>named</code>. When manually specified otherwise, the check levels must at least be as strict as those specified in the <code>named</code> configuration file.</p>
<h2>Options</h2>
<p>-d</p>
<dl>
<dd>Enable debugging.</dl>
<p> -h</p>
<dl>
<dd>Print the usage summary and exit.</dl>
<p> -q</p>
<dl>
<dd>Quiet mode &#8211; exit code only.</dl>
<p> -v</p>
<dl>
<dd>Print the version of the <code>named-checkzone</code> program and exit.</dl>
<p> -j</p>
<dl>
<dd>When loading the zone file read the journal if it exists.</dl>
<p> -c <i>class</i></p>
<dl>
<dd>Specify the class of the zone. If not specified, &quot;IN&quot; is assumed.</dl>
<p> -i <i>mode</i></p>
<dl>
<dd>Perform post-load zone integrity checks. Possible modes are <code>&quot;full&quot;</code> (default), <code>&quot;full-sibling&quot;</code>, <code>&quot;local&quot;</code>, <code>&quot;local-sibling&quot;</code> and <code>&quot;none&quot;</code>. </p>
<p> Mode <code>&quot;full&quot;</code> checks that MX records refer to A or AAAA record (both in-zone and out-of-zone hostnames). Mode <code>&quot;local&quot;</code> only checks MX records which refer to in-zone hostnames. </p>
<p> Mode <code>&quot;full&quot;</code> checks that SRV records refer to A or AAAA record (both in-zone and out-of-zone hostnames). Mode <code>&quot;local&quot;</code> only checks SRV records which refer to in-zone hostnames. </p>
<p> Mode <code>&quot;full&quot;</code> checks that delegation NS records refer to A or AAAA record (both in-zone and out-of-zone hostnames). It also checks that glue address records in the zone match those advertised by the child. Mode <code>&quot;local&quot;</code> only checks NS records which refer to in-zone hostnames or that some required glue exists, that is when the nameserver is in a child zone. </p>
<p> Mode <code>&quot;full-sibling&quot;</code> and <code>&quot;local-sibling&quot;</code> disable sibling glue checks but are otherwise the same as <code>&quot;full&quot;</code> and <code>&quot;local&quot;</code> respectively. </p>
<p> Mode <code>&quot;none&quot;</code> disables the checks.</dl>
<p> -f <i>format</i></p>
<dl>
<dd>Specify the format of the zone file. Possible formats are <code>&quot;text&quot;</code> (default) and <code>&quot;raw&quot;</code>.</dl>
<p> -F <i>format</i></p>
<dl>
<dd>Specify the format of the output file specified. For <code>named-checkzone</code>, this does not cause any effects unless it dumps the zone contents. </p>
<p> Possible formats are <code>&quot;text&quot;</code> (default) and <code>&quot;raw&quot;</code> or <code>&quot;raw=N&quot;</code>, which store the zone in a binary format for rapid loading by <code>named</code>. <code>&quot;raw=N&quot;</code> specifies the format version of the raw zone file: if N is 0, the raw file can be read by any version of <code>named</code>; if N is 1, the file can be read by release 9.9.0 or higher. The default is 1.</dl>
<p> -k <i>mode</i></p>
<dl>
<dd>Perform <code>&quot;check-names&quot;</code> checks with the specified failure mode. Possible modes are <code>&quot;fail&quot;</code> (default for <code>named-compilezone</code>), <code>&quot;warn&quot;</code> (default for <code>named-checkzone</code>) and <code>&quot;ignore&quot;</code>.</dl>
<p> -L <i>serial</i></p>
<dl>
<dd>When compiling a zone to &#8216;raw&#8217; format, set the &quot;source serial&quot; value in the header to the specified serial number. (This is expected to be used primarily for testing purposes.)</dl>
<p> -m <i>mode</i></p>
<dl>
<dd>Specify whether MX records should be checked to see if they are addresses. Possible modes are <code>&quot;fail&quot;</code>, <code>&quot;warn&quot;</code> (default) and <code>&quot;ignore&quot;</code>.</dl>
<p> -M <i>mode</i></p>
<dl>
<dd>Check if a MX record refers to a CNAME. Possible modes are <code>&quot;fail&quot;</code>, <code>&quot;warn&quot;</code> (default) and <code>&quot;ignore&quot;</code>.</dl>
<p> -n <i>mode</i></p>
<dl>
<dd>Specify whether NS records should be checked to see if they are addresses. Possible modes are <code>&quot;fail&quot;</code> (default for <code>named-compilezone</code>), <code>&quot;warn&quot;</code> (default for <code>named-checkzone</code>) and <code>&quot;ignore&quot;</code>.</dl>
<p> -o <i>filename</i></p>
<dl>
<dd>Write zone output to <i>filename</i>. If <i>filename</i> is <i>&#8211;</i> then write to standard out. This is mandatory for <code>named-compilezone</code>.</dl>
<p> -r <i>mode</i></p>
<dl>
<dd>Check for records that are treated as different by DNSSEC but are semantically equal in plain DNS. Possible modes are <code>&quot;fail&quot;</code>, <code>&quot;warn&quot;</code> (default) and <code>&quot;ignore&quot;</code>.</dl>
<p> -s <i>style</i></p>
<dl>
<dd>Specify the style of the dumped zone file. Possible styles are <code>&quot;full&quot;</code> (default) and <code>&quot;relative&quot;</code>. The full format is most suitable for processing automatically by a separate script. On the other hand, the relative format is more human-readable and is thus suitable for editing by hand. For <code>named-checkzone</code> this does not cause any effects unless it dumps the zone contents. It also does not have any meaning if the output format is not text.</dl>
<p> -S <i>mode</i></p>
<dl>
<dd>Check if a SRV record refers to a CNAME. Possible modes are <code>&quot;fail&quot;</code>, <code>&quot;warn&quot;</code> (default) and <code>&quot;ignore&quot;</code>.</dl>
<p> -t <i>directory</i></p>
<dl>
<dd>Chroot to <i>directory</i> so that include directives in the configuration file are processed as if run by a similarly chrooted named.</dl>
<p> -T <i>mode</i></p>
<dl>
<dd>Check if Sender Policy Framework (SPF) records exist and issues a warning if an SPF-formatted TXT record is not also present. Possible modes are <code>&quot;warn&quot;</code> (default), <code>&quot;ignore&quot;</code>.</dl>
<p> -w <i>directory</i></p>
<dl>
<dd>chdir to <i>directory</i> so that relative filenames in master file $INCLUDE directives work. This is similar to the directory clause in <i>named.conf</i>.</dl>
<p> -D</p>
<dl>
<dd>Dump zone file in canonical format. This is always enabled for <code>named-compilezone</code>.</dl>
<p> -W <i>mode</i></p>
<dl>
<dd>Specify whether to check for non-terminal wildcards. Non-terminal wildcards are almost always the result of a failure to understand the wildcard matching algorithm (RFC 1034). Possible modes are <code>&quot;warn&quot;</code> (default) and <code>&quot;ignore&quot;</code>.</dl>
<p> zonename</p>
<dl>
<dd>The domain name of the zone being checked.</dl>
<p> filename</p>
<dl>
<dd>The name of the zone file.</dl>
<h2>Return Values</h2>
<p><code>named-checkzone</code> returns an exit status of 1 if errors were detected and 0 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/8-named-checkconf/">named-checkconf</a></code>(8), RFC 1035, BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004-2007, 2009-2011, 2013 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000-2002 Internet Software Consortium.</p>
