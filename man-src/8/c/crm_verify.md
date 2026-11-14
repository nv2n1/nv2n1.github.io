---
title: "crm_verify(8)"
name: "crm_verify"
section: "8"
letter: "c"
url: "/docs/linux/man/8-crm_verify/"
description: "Pacemaker – Part of the Pacemaker cluster resource manager"
---

<p>Pacemaker &#8211; Part of the Pacemaker cluster resource manager</p>
<h2>Synopsis</h2>
<p><code>crm_verify</code> [<i>modifiers</i>] <i>data_source</i></p>
<h2>Description</h2>
<p>crm_verify &#8211; Check a (complete) confiuration for syntax and common conceptual errors. </p>
<p> Checks the well-formedness of an XML configuration, its conformance to the configured DTD/schema and for the presence of common misconfigurations. </p>
<p> It reports two classes of problems, errors and warnings. Errors must be fixed before the cluster will work properly. However, it is left up to the administrator to decide if the warnings should also be fixed.</p>
<h2>Options</h2>
<dl>
<dt>-?, <code>&#8211;help</code></p>
<dd>This text</p>
<dt>-$, <code>&#8211;version</code></p>
<dd>Version information</p>
<dt><code>-V</code>, <code>&#8211;verbose</code></p>
<dd>Increase debug output</dl>
<h3>Data sources:</h3>
<dl>
<dt><code>-L</code>, <code>&#8211;live-check</code></p>
<dd>Check the configuration used by the running cluster</p>
<dt><code>-x</code>, <code>&#8211;xml-file</code>=<i>value</i></p>
<dd>Check the configuration in the named file</p>
<dt><code>-X</code>, <code>&#8211;xml-text</code>=<i>value</i></p>
<dd>Check the configuration in the supplied string</p>
<dt> <code>-p</code>, <code>&#8211;xml-pipe</code> Check the configuration piped in via stdin</dl>
<h3>Additional Options:</h3>
<dl>
<dt><code>-S</code>, <code>&#8211;save-xml</code>=<i>value</i></p>
<dd>
<dd>Save the verified XML to the named file. Most useful with <code>-L</code></dl>
<h2>Examples</h2>
<p>Check the consistency of the configuration in the running cluster:</p>
<dl>
<dd># crm_verify &#8211;live-check</dl>
<p> Check the consistency of the configuration in a given file and produce verbose output:</p>
<dl>
<dd># crm_verify &#8211;xml-file file.xml &#8211;verbose</dl>
<h2>Author</h2>
<p>Written by Andrew Beekhof</p>
<h2>Reporting Bugs</h2>
<p>Report bugs to pacemaker [at] oss.clusterlabs.org</p>
