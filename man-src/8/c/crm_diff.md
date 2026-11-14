---
title: "crm_diff(8)"
name: "crm_diff"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_diff/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_diff</code> <i>original_xml operation </i>[<i>options</i>]</p>
<h2>Description</h2>
<p>crm_diff &#8211; A utility for comparing Pacemaker configurations (XML format) </p>
<p> The tool produces a custom (diff-like) output which it can also apply like a patch</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Original XML:</h3>
<dl>
<dt><code>-o</code>, <code>&#8211;original</code>=<i>value</i></p>
<dd>XML is contained in the named file</p>
<dt><code>-O</code>, <code>&#8211;original-string</code>=<i>value</i></p>
<dd>XML is contained in the supplied string</dl>
<h3>Operation:</h3>
<dl>
<dt><code>-n</code>, <code>&#8211;new</code>=<i>value</i></p>
<dd>Compare the original XML to the contents of the named file</p>
<dt><code>-N</code>, <code>&#8211;new-string</code>=<i>value</i></p>
<dd>Compare the original XML to the contents of the supplied string</p>
<dt><code>-p</code>, <code>&#8211;patch</code>=<i>value</i></p>
<dd>Patch the original XML with the contents of the named file</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-c</code>, <code>&#8211;cib</code></p>
<dd>Compare/patch the inputs as a CIB (includes versions details)</p>
<dt><code>-u</code>, <code>&#8211;no-version</code></p>
<dd>Generate the difference without versions details</dl>
<h2>Examples</h2>
<p>Obtain the two different configuration files by running cibadmin on the two cluster setups to compare:</p>
<dl>
<dd># cibadmin &#8211;query &gt; cib-old.xml</p>
<dd># cibadmin &#8211;query &gt; cib-new.xml</dl>
<p> Calculate and save the difference between the two files:</p>
<dl>
<dd># crm_diff &#8211;original cib-old.xml &#8211;new cib-new.xml &gt; patch.xml</dl>
<p> Apply the patch to the original file:</p>
<dl>
<dd># crm_diff &#8211;original cib-old.xml &#8211;patch patch.xml &gt; updated.xml</dl>
<p> Apply the patch to the running cluster:</p>
<dl>
<dd># cibadmin &#8211;patch patch.xml</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
