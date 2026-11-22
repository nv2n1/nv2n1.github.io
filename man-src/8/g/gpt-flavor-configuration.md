---
title: "gpt-flavor-configuration(8)"
name: "gpt-flavor-configuration"
section: "8"
letter: "g"
url: "/docs/linux/man/8-gpt-flavor-configuration/"
description: "gpt-flavor-configuration – Permutes the build flavor choices found in the flavor configuration file."
---

<p><code>gpt-flavor-configuration</code> &#8211; Permutes the build flavor choices found in the flavor configuration file.</p>
<h2>Synopsis</h2>
<p><code>gpt-flavor-configuration</code> [-installdir=&lt;DIR&gt; -standard -all -conf=&lt;flavor configuration file&gt;]</p>
<h2>Description</h2>
<p><code>gpt-flavor-configuration</code> produce a list of build flavors. The default is a list of installed flavors. If the <code>-standard</code> or <code>-all</code> flags are used then the script permutes the flavor choices listed in the flavor configuration file. The file <tt>$GPT_LOCATION</tt>/share/globus/globus_flavor_labels.conf is the default. The possible fields for a flavor are described in the file <tt>$GPT_LOCATION</tt>/share/globus/dtd/globus_flavors.dtd</p>
<h2>Options</h2>
<dl>
<dt><code>-conf=flavor configuration file</code></dt>
<dd>Permute the choices found in this file rather than the default.</dd>
<dt><code>-all</code></dt>
<dd>Permute all possible flavor choices..</dd>
<dt><code>-standard</code></dt>
<dd>Permute the standard flavor choices.</dd>
<dt><code>-help</code></dt>
<dd>Print a brief help message and exits.</dd>
<dt><code>-man</code></dt>
<dd>Prints the manual page and exits.</dd>
<dt><code>-version</code></dt>
<dd>Prints the version of GPT and exits.</dd></dl>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
