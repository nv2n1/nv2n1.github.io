---
title: "opaextractbadlinks(8)"
name: "opaextractbadlinks"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractbadlinks/"
---

opaextractbadlinks 

 

 

 Produces a CSV file listing all or some of the links that exceed opareport -o error thresholds. opaextractbadlinks is a front end to the opareport tool. The output from this tool can be imported into a spreadsheet or parsed by other scripts.

<h2>Syntax</h2>

opaextractbadlinks [--help] [opareport <i>options</i>]

<h2>Options</h2>

<dl><dt>opareport <i>options</i>
<dd>Options are passed to opareport. See <i>opareport</i> for the full set of options. 

</dl>

<h2>Examples</h2>

# List all the bad links in the fabric: 
 opaextractbadlinks 
 <pre><code># List all the bad links to a switch named &quot;OmniPth00117501ffffffff&quot;:

opaextractbadlinks -F &quot;node:OmniPth00117501ffffffff&quot;
# List all the bad links to end-nodes:

opaextractbadlinks -F &quot;nodetype:FI&quot;</code></pre> 
 # List all the bad links on the 2nd HFI's fabric of a multi-plane fabric: 
 opaextractbadlinks -h 2 
 
