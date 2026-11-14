---
title: "nlist(3)"
name: "nlist"
section: "3"
letter: "n"
url: "/docs/linux/man/3-nlist/"
description: "nlist – retrieve symbol table name list from an executable file"
---

<p><code>nlist</code> &#8211; retrieve symbol table name list from an executable file</p>
<h2>Library</h2>
<p>Lb libbsd</p>
<h2>Synopsis</h2>
<p>In bsd/nlist.h Ft int Fn nlist const char *filename struct nlist *nl</p>
<h2>Description</h2>
<p>The Fn nlist function retrieves name list entries from the symbol table of an executable file (see a.out5). The argument Fa nl is set to reference the beginning of the list. The list is preened of binary and invalid data; if an entry in the name list is valid, the Fa n_type and Fa n_value for the entry are copied into the list referenced by Fa nl . No other data is copied. The last entry in the list is always <code>NULL</code></p>
<h2>Return Values</h2>
<p>The number of invalid entries is returned if successful; otherwise, if the file Fa filename does not exist or is not executable, the returned value is -1.</p>
<h2>See Also</h2>
<p>a.out5</p>
<h2>History</h2>
<p>A Fn nlist function appeared in AT&amp;T System v6 .</p>
