---
title: "soscleaner(8)"
name: "soscleaner"
section: "8"
letter: "s"
url: "/docs/linux/man/8-soscleaner/"
description: "soscleaner – clean sosreports of sensitive information"
---

<p>soscleaner &#8211; clean sosreports of sensitive information</p>
<h2>Synopsis</h2>
<p>soscleaner -l LOGLEVEL -d DOMAIN -f FILE -q</p>
<h2>Description</h2>
<p>soscleaner is an attempt to begin the process of cleaning potentially sensitive hostnames and IPv4 addresses from an sosreport after it has been created. It is NOT a full cleaning, but it attempts to be a good starting point. If a Fully Qualified Domain Name is used for the hostname, it can substitute instances of hostnames on that domain with a consistent substitution. If an FQDN is not used, it will replace all instances of the short hostname. It also replaces instances of IPv4 addresses with a randomly assignable IPv4 range.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code>, <code>&#8211;domain</code>=<i>DOMAIN</i></p>
<dd>optional additional domains to be analyzed during the soscleaner process</p>
<dt><code>-f</code>, <code>&#8211;file</code>=<i>FILE</i></p>
<dd>optional additonal files to be analyzed. Can be used in addtion to supplying an sosreport, or can be used without specifying an sosreport. If no sosreport is supplied, no hostnames will be obfuscated usless the -d flag is used to add a domain for analysis</p>
<dt><code>-l</code>, <code>&#8211;loglevel</code>=<i>LOGLEVEL</i></p>
<dd>the desired loglevel to be used. default is &#8216;INFO&#8217; (including quotes). Options are &#8216;DEBUG&#8217;,&#8217;INFO&#8217;,&#8217;WARNING&#8217;,&#8217;ERROR&#8217;. <code>-q</code>, <code>&#8211;quiet</code> Quiet mode. Nothing will be output to STDOUT. logfiles will still be created.</dl>
<h2>Examples</h2>
<dl>
<dt><code>supply an sosreport</code></p>
<dd>soscleaner /path/to/sosreport.tar.gz</p>
<dt><code>change logging level</code></p>
<dd>soscleaner -l DEBUG /path/to/sosreport.tar.gz (warning &#8211; DEBUG level logging is extremely intensive.)</p>
<dt><code>supply additonal domains</code></p>
<dd>soscleaner -d foo.com -d google.com /path/to/sosreport.tar.gz</p>
<dt><code>supply additional files</code></p>
<dd>soscleaner -f /path/to/file1 -f /path/to/file2 /path/to/sosreport.tar.gz</p>
<dt><code>only analyze files</code></p>
<dd>soscleaner -f /path/to/file1 -f /path/to/file2 -d foo.com (It is highly recommended to use the -d flag if only scanning files, so hostnames will be obfuscated.)</dl>
<h2>Bugs</h2>
<p>Please report new bugs to <a rel="nofollow" href="https://github.com/jduncan-rva/soscleaner/issues">https://github.com/jduncan-rva/soscleaner/issues</a></p>
<h2>Author</h2>
<p>Jamie Duncan (jduncan [at] redhat.com)</p>
