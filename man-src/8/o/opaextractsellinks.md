---
title: "opaextractsellinks(8)"
name: "opaextractsellinks"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractsellinks/"
---

opaextractsellinks 

 

 

 Produces a CSV file listing all or some of the links in the fabric. opaextractsellinks is a front end to the opareport tool. The output from this tool can be imported into a spreadsheet or parsed by other scripts.

<h2>Syntax</h2>

opaextractsellinks [--help] [opareport <i>options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>opareport <i>options</i>
<dd>Options are passed to opareport. See <i>opareport</i> for the full set of options. 

</dl>

<h2>Examples</h2>

# List all the links in the fabric: 
 opaextractsellinks 
 <pre><code># List all the links to a switch named &quot;OmniPth00117501ffffffff&quot;:

opaextractsellinks -F &quot;node:OmniPth00117501ffffffff&quot;
# List all the connections to end-nodes:

opaextractsellinks -F &quot;nodetype:FI&quot;</code></pre> 
 # List all the links on the 2nd HFI's fabric of a multi-plane fabric: 
 opaextractsellinks -h 2 
