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
<p><code>gpt-flavor-configuration</code> [-installdir=&lt;<font SIZE="-1">DIR</font>&gt; -standard -all -conf=&lt;flavor configuration file&gt;]</p>
<h2>Description</h2>
<p><code>gpt-flavor-configuration</code> produce a list of build flavors. The default is a list of installed flavors. If the <code>-standard</code> or <code>-all</code> flags are used then the script permutes the flavor choices listed in the flavor configuration file. The file <tt>$GPT_LOCATION</tt>/share/globus/globus_flavor_labels.conf is the default. The possible fields for a flavor are described in the file <tt>$GPT_LOCATION</tt>/share/globus/dtd/globus_flavors.dtd</p>
<h2>Options</h2>
<dl>
<dt><code>-conf=flavor configuration file</code></p>
<dd>Permute the choices found in this file rather than the default.</p>
<dt><code>-all</code></p>
<dd>Permute all possible flavor choices..</p>
<dt><code>-standard</code></p>
<dd>Permute the standard flavor choices.</p>
<dt><code>-help</code></p>
<dd>Print a brief help message and exits.</p>
<dt><code>-man</code></p>
<dd>Prints the manual page and exits.</p>
<dt><code>-version</code></p>
<dd>Prints the version of <font SIZE="-1">GPT</font> and exits.</dl>
<h2>Author</h2>
<p>Michael Bletzinger &lt;mbletzin.ncsa.uiuc.edu&gt; and Eric Blau &lt;eblau.ncsa.uiuc.edu&gt;</p>
