---
title: "opaextractlids(8)"
name: "opaextractlids"
section: "8"
letter: "o"
url: "/docs/linux/man/8-opaextractlids/"
---

opaextractlids 

 

 

 Produces a CSV file listing all or some of the LIDs in the fabric. opaextractlids is a front end to the opareport tool. The output from this tool can be imported into a spreadsheet or parsed by other scripts.

<h2>Syntax</h2>

opaextractlids [--help] [opareport <i>options</i>]

<h2>Options</h2>

<dl><dt>--help
<dd>Produces full help text. 

<dt>opareport <i>options</i>
<dd>Options are passed to opareport. See <i>opareport</i> for the full set of options. 

</dl>

<h2>Examples</h2>

# List all the lids in the fabric: 
 opaextractlids 
 <pre><code># List all the lids of end-nodes:

opaextractlids -F &quot;nodetype:FI&quot;</code></pre> 
 # List all the lids on the 2nd HFI's fabric of a multi-plane fabric: 
 opaextractlids -h 2 
