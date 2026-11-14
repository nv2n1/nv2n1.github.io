---
title: "opaextracterror(8)"
name: "opaextracterror"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextracterror/"
---

opaextracterror 

 

 

 Produces a CSV file listing all or some of the errors in the current fabric. opaextracterror is a front end to the opareport tool. The output from this tool can be imported into a spreadsheet or parsed by other scripts.

<h2>Syntax</h2>

opaextracterror [--help] [opareport <i>options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>opareport <i>options</i>
<dd>Options are passed to opareport. See <i>opareport</i> for the full set of options. 

</dl>

<h2>Examples</h2>

# List all the link errors in the fabric: 
 opaextracterror 
 <pre><code># List all the link errors related to a switch named &quot;OmniPth00117501ffffffff&quot;:

opaextracterror -F &quot;node:OmniPth00117501ffffffff&quot;
# List all the link errors for end-nodes:

opaextracterror -F &quot;nodetype:FI&quot;</code></pre> 
 # List all the link errors on the 2nd HFI's fabric of a multi-plane fabric: 
 opaextracterror -h 2 
