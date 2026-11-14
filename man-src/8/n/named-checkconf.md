---
title: "named-checkconf(8)"
name: "named-checkconf"
section: "8"
letter: "n"
url: "/docs/linux/man/8-named-checkconf/"
description: "named-checkconf – named configuration file syntax checking tool"
---

<p>named-checkconf &#8211; named configuration file syntax checking tool</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named-checkconf</code> [<code>-h</code>] [<code>-v</code>] [<code>-j</code>] [<code>-t&nbsp;<wbr></code><i>directory</i>] {filename} [<code>-p</code>] [<code>-z</code>]</dl>
<h2>Description</h2>
<p><code>named-checkconf</code></p>
<dd>checks the syntax, but not the semantics, of a <code>named</code> configuration file. The file is parsed and checked for syntax errors, along with all files included by it. If no file is specified, <i>/etc/named.conf</i> is read by default. </p>
<p> Note: files that <code>named</code> reads in separate parser contexts, such as <i>rndc.key</i> and <i>bind.keys</i>, are not automatically read by <code>named-checkconf</code>. Configuration errors in these files may cause <code>named</code> to fail to run, even if <code>named-checkconf</code> was successful. <code>named-checkconf</code> can be run on these files explicitly, however.</p>
<h2>Options</h2>
<p>-h</p>
<dl>
<dd>Print the usage summary and exit.</dl>
<p> -t <i>directory</i></p>
<dl>
<dd>Chroot to <i>directory</i> so that include directives in the configuration file are processed as if run by a similarly chrooted named.</dl>
<p> -v</p>
<dl>
<dd>Print the version of the <code>named-checkconf</code> program and exit.</dl>
<p> -p</p>
<dl>
<dd>Print out the <i>named.conf</i> and included files in canonical form if no errors were detected.</dl>
<p> -z</p>
<dl>
<dd>Perform a test load of all master zones found in <i>named.conf</i>.</dl>
<p> -j</p>
<dl>
<dd>When loading a zonefile read the journal if it exists.</dl>
<p> filename</p>
<dl>
<dd>The name of the configuration file to be checked. If not specified, it defaults to <i>/etc/named.conf</i>.</dl>
<h2>Return Values</h2>
<p><code>named-checkconf</code> returns an exit status of 1 if errors were detected and 0 otherwise.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/8-named-checkzone/">named-checkzone</a></code>(8), BIND 9 Administrator Reference Manual.</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2005, 2007, 2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000-2002 Internet Software Consortium.</p>
