---
title: "verify_krb5_conf(8)"
name: "verify_krb5_conf"
section: "8"
letter: "v"
url: "/docs/linux/man/8-verify_krb5_conf/"
description: "verify_krb5_conf – checks krb5.conf for obvious errors"
---

<p><code>verify_krb5_conf</code> &#8211; checks krb5.conf for obvious errors</p>
<h2>Synopsis</h2>
<p><i>[config-file]</i></p>
<h2>Description</h2>
<p>reads the configuration file krb5.conf or the file given on the command line, parses it, checking verifying that the syntax is not correctly wrong. </p>
<p> If the file is syntactically correct, tries to verify that the contents of the file is of relevant nature.</p>
<h2>Environment</h2>
<p><code>KRB5_CONFIG</code> points to the configuration file to read.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/krb5.conf </code></p>
<dd>Kerberos 5 configuration file</dl>
<h2>Diagnostics</h2>
<p>Possible output from include:</p>
<dl>
<dt><code>&quot;&lt;path&gt;: failed to parse &lt;something&gt; as size/time/number/boolean&quot;</code></p>
<dd>Usually means that &lt;something&gt; is misspelled, or that it contains weird characters. The parsing done by is more strict than the one performed by libkrb5, so strings that work in real life might be reported as bad.</p>
<dt><code>&quot;&lt;path&gt;: host not found (&lt;hostname&gt;)&quot;</code></p>
<dd>Means that &lt;path&gt; is supposed to point to a host, but it can&#8217;t be recognised as one.</p>
<dt><code>&lt;path&gt;: unknown or wrong type</code></p>
<dd>Means that &lt;path&gt; is either a string when it should be a list, vice versa, or just that is confused.</p>
<dt><code>&lt;path&gt;: unknown entry</code></p>
<dd>Means that &lt;string&gt; is not known by <code>.</code></dl>
<h2>See Also</h2>
<p>krb5.conf5</p>
<h2>Bugs</h2>
<p>Since each application can put almost anything in the config file, it&#8217;s hard to come up with a watertight verification process. Most of the default settings are sanity checked, but this does not mean that every problem is discovered, or that everything that is reported as a possible problem actually is one. This tool should thus be used with some care. It should warn about obsolete data, or bad practice, but currently doesn&#8217;t. </p>
