---
title: "makedumpfile(5)"
name: "makedumpfile"
section: "5"
letter: "m"
url: "/docs/linux/man/5-makedumpfile/"
description: "makedumpfile.conf – The filter configuration file for makedumpfile(8)."
---

<p>makedumpfile.conf &#8211; The filter configuration file for <a href="/docs/linux/man/8-makedumpfile/">makedumpfile</a>(8).</p>
<h2>Description</h2>
<p>The makedumpfile.conf is a configuration file for makedumpfile tool. makedumpfile.conf file contains the erase commands to filter out desired kernel data from the vmcore while creating <i>DUMPFILE</i> using makedumpfile tool. makedumpfile reads the filter config and builds the list of memory addresses and its sizes after processing filter commands. The memory locations that require to be filtered out are then poisoned with character <i>X</i> (58 in Hex).</p>
<h2>File Format</h2>
<p>The file consists of module sections that contains filter commands. A section begins with the name of the section in square brackets and continues until the next section begins. </p>
<p> &quot;[&quot;&lt;<i>ModuleName</i>&gt;&quot;]&quot;<br />
 &lt;<i>FilterCommands</i>&gt; </p>
<p> where<br />
 &quot;[&quot; is the character <code>[</code><br />
 &quot;]&quot; is the character <code>]</code></p>
<dl>
<dt>&lt;<i>ModuleName</i>&gt;</p>
<dd>is either &#8216;vmlinux&#8217; or name of a Linux kernel module.</p>
<dt>&lt;<i>FilterCommands</i>&gt;</p>
<dd>is a list of one or more filter commands as described in the section <code>FILTER COMMANDS</code> of this manual page.</dl>
<p> The section name indicates a kernel module name (including <code>vmlinux</code>) where the symbols specified in subsequent erase commands belong to. The unnamed section defaults to <code>[vmlinux]</code> section. However, a user can also explicitly define <code>[vmlinux]</code> section. The sections help makedumpfile tool to select appropriate kernel or module debuginfo file before processing the subsequent erase commands. Before selecting appropriate debuginfo file, the module name is validated against the loaded modules from the vmcore. If no match is found, then the section is ignored and makedumpfile skips to the next module section. If match is found, then makedumpfile will try to load the corresponding module debuginfo file. If module debuginfo is not available then, makedumpfile will skip the section with a warning message.</p>
<h2>Filter Commands</h2>
<h3>filter command</h3>
<p>A filter command is either an erase command or a loop construct. Each erase command and loop construct must start with a new line. Each filter command describes data in the dump to be erased. Syntax: </p>
<p> &lt;<i>EraseCommands</i>&gt;|&lt;<i>LoopConstruct</i>&gt; </p>
<p> where</p>
<dl>
<dt>&lt;<i>EraseCommands</i>&gt;</p>
<dd>Described in the subsection <code>erase command</code> of this manual page.</p>
<dt>&lt;<i>LoopConstruct</i>&gt;</p>
<dd>Described in the subsection <code>Loop construct</code> of this manual page.</dl>
<h3>erase command</h3>
<p>Erase specified size of a kernel data referred by specified kernel/module symbol or its member component. The erase command syntax is: </p>
<p> <code>erase</code> &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] [<code>size</code> &lt;<i>SizeValue</i>&gt;[K|M]]<br />
 <code>erase</code> &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] [<code>size</code> &lt;<i>SizeSymbol</i>&gt;]<br />
 <code>erase</code> &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] [<code>nullify</code>] </p>
<p> where </p>
<dl>
<dt>&lt;<i>Symbol</i>&gt;</p>
<dd>A kernel or module symbol (variable) name that is part of global symbols <code>/proc/kallsyms</code>.</p>
<dt>&lt;<i>SizeValue</i>&gt;</p>
<dd>A positive integer value as a size of the data in bytes to be erased. The suffixes &#8216;K&#8217; and &#8216;M&#8217; can be used to specify kilobytes and Megabytes respectively where, K means 1024 bytes and M means 1024 ^ 2 = 1048576 bytes. The suffixes are not case sensitive.</p>
<dt>&lt;<i>SizeSymbol</i>&gt;</p>
<dd>A simple expression of the form &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] that denotes a symbol which contains a positive integer value as a size of the data in bytes to be erased.</p>
<dt>&lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]]</p>
<dd>A simple expression that results into either a global kernel symbol name or its member components. The expression always uses &#8216;.&#8217; operator to specify the <i>member</i> component of kernel symbol or its member irrespective of whether it is of pointer type or not.</p>
<dt><i>member</i>[&#8230;]</p>
<dd>Member or component of member in &lt;<i>Symbol</i>&gt;.</dl>
<p> The <code>erase</code> command takes two arguments 1. kernel symbol name or its member components and 2. size of the data referred by argument (1) OR <code>nullify</code> keyword. The second argument <code>size</code> OR <code>nullify</code> is optional. The unit for size value is in <code>bytes</code>. If <code>size</code> option is not specified then the size of the first argument is determined according to its data type using dwarf info from debuginfo file. In case of &#8216;<code>char *</code>&#8216; data type, the length of string pointed by &#8216;<code>char *</code>&#8216; pointer is determined with an upper limit of 1024. The <code>size</code> can be specified in two forms 1. a integer value as explained above (&lt;<i>SizeValue</i>&gt;) and 2. a simple expression in the form of &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]]] that results into base type (integer) variable. </p>
<p> If the specified &lt;<i>Symbol</i>&gt; is of type &#8216;<code>void *</code>&#8216;, then user needs to provide either <code>size</code> or <code>nullify</code> option, otherwise the erase command will not have any effect. </p>
<p> The <code>nullify</code> option only works if specified &lt;<i>Symbol</i>&gt; is a pointer. Instead of erasing data pointed by the specified pointer <code>nullify</code> erases the pointer value and set it to &#8216;0&#8217; (NULL). Please note that by nullifying the pointer values may affect the debug ability of created <i>DUMPFILE</i>. Use the <code>nullify</code> option only when the size of data to be erased is not known. <code>e.g.</code> data pointed by &#8216;<code>void *</code>&#8216;. </p>
<p> Let us look at the makedumpfile.conf file from the example below which was configured to erase desired kernel data from the kernel module with name <code>mymodule</code>. At line 1 and 3, the user has not specified size option while erasing &#8216;array_var&#8217; and &#8216;mystruct1.name&#8217; symbols. Instead the user depends on makedumpfile to automatically determine the sizes to be erased <code>i.e</code> 100 bytes for &#8216;array_var&#8217; and 11 bytes for &#8216;mystruct1.name&#8217;. At line 2, while erasing the &#8216;mystruct1.buffer&#8217; member the user has specified the size value 25 against the actual size of 50. In this case the user specified <code>size</code> takes the precedence and makedumpfile erases only 25 bytes from &#8216;mystruct1.buffer&#8217;. At line 4, the size of the data pointed by <code>void *</code> pointer &#8216;mystruct1.addr&#8217; is unknown. Hence the <code>nullify</code> option has been specified to reset the pointer value to NULL. At line 5, the &#8216;mystruct2.addr_size&#8217; is specified as <code>size</code> argument to determine the size of the data pointed by <code>void *</code> pointer &#8216;mystruct2.addr&#8217;. </p>
<p> <code>Example:</code> </p>
<p> Assuming the following piece of code is from kernel module &#8216;mymodule&#8217;: </p>
<p> struct s1 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>char *name;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>void *addr1;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>void *addr2;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>char buffer[50];</p>
<p> };<br />
 struct s2 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>void *addr;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>long addr_size;</p>
<p> }; </p>
<p> /* Global symbols */<br />
 char array_var[100];<br />
 struct s1 mystruct1;<br />
 struct s2 *mystruct2; </p>
<p> int foo()<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>s1.name = &quot;Hello World&quot;;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> } </p>
<p> <code>makedumpfile.conf:</code><br />
 [mymodule]<br />
 erase array_var<br />
 erase mystruct1.buffer size 25<br />
 erase mystruct1.name<br />
 erase mystruct1.addr1 nullify<br />
 # Assuming addr2 points to 1024 bytes<br />
 erase mystruct1.addr2 size 1K<br />
 erase mystruct2.addr size mystruct2.addr_size<br />
 <code>EOF</code></p>
<h3>Loop construct</h3>
<p>A Loop construct allows the user to traverse the linked list or array elements and erase the data contents referred by each element. </p>
<p> <code>for</code> &lt;<i>id</i>&gt; <code>in</code> {&lt;<i>ArrayVar</i>&gt; |<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &lt;<i>StructVar</i>&gt; <code>via</code> &lt;<i>NextMember</i>&gt; |</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt> &lt;<i>ListHeadVar</i>&gt; <code>within</code><br />
 &lt;<i>StructName</i>&gt;<code>:</code>&lt;<i>ListHeadMember</i>&gt;}<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><code>erase</code> &lt;<i>id</i>&gt;[.<i>MemberExpression</i>]<br />
 [<code>size</code> &lt;<i>SizeExpression</i>&gt;|<code>nullify</code>]<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[<code>erase</code> &lt;<i>id</i>&gt;&#8230;]</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>[&#8230;]</p>
<p> <code>endfor</code> </p>
<p> where </p>
<dl>
<dt>&lt;<i>id</i>&gt;</p>
<dd>Arbitrary name used to temporarily point to elements of the list. This is also called iteration variable.</p>
<dt>&lt;<i>ArrayVar</i>&gt;</p>
<dd>A simple expression in the form of &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] that results into an array variable.</p>
<dt>&lt;<i>StructVar</i>&gt;</p>
<dd>A simple expression in the form of &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] that results into a variable that points to a structure.</p>
<dt>&lt;<i>NextMember</i>&gt;</p>
<dd>Member within &lt;<i>StructVar</i>&gt; that points to an object of same type that of &lt;<i>StructVar</i>&gt;.</p>
<dt>&lt;<i>ListHeadVar</i>&gt;</p>
<dd>A simple expression in the form of &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]] that results into a variable of type struct list_head.</p>
<dt>&lt;<i>StructName</i>&gt;</p>
<dd>Name of the structure type that can be traversed using HEAD variable &lt;<i>ListHeadVar</i>&gt; and contains a member named &lt;<i>ListHeadMember</i>&gt;.</p>
<dt>&lt;<i>ListHeadMember</i>&gt;</p>
<dd>Name of a member in &lt;<i>StructName</i>&gt;, of type struct list_head.</p>
<dt>&lt;<i>MemberExpression</i>&gt;</p>
<dd>A simple expression in the form of [.<i>member</i>[&#8230;]] to specify a member or component of an element in &lt;<i>ArrayVar</i>&gt;, &lt;<i>StructVar</i>&gt; or &lt;<i>StructName</i>&gt;.</p>
<dt>&lt;<i>SizeExpression</i>&gt;</p>
<dd>Size value in the form of &lt;<i>SizeValue</i>&gt;, &lt;<i>id</i>&gt;[.<i>MemberExpression</i>] or &lt;<i>Symbol</i>&gt;[.<i>member</i>[&#8230;]].</dl>
<p> The <code>for</code> loop construct allows to iterate on list of elements in an array or linked lists. Each element in the list is assigned to iteration variable &lt;<i>id</i>&gt;. The type of the iteration variable is determined by that of the list elements. The entry specified after &#8216;<code>in</code>&#8216; terminal is called LIST entry. The LIST entry can be an array variable, structure variable/pointer or a struct list_head type variable. The set of <code>erase</code> commands specified between <code>for</code> and <code>endfor</code>, will be executed for each element in the LIST entry. </p>
<p> If the LIST entry specified is an array variable, then the loop will be executed for each array element. The size of the array will be determined by using dwarf information. </p>
<p> If the LIST entry specified is a structure variable/pointer, then a traversal member (&lt;<i>NextMember</i>&gt;) must be specified using &#8216;<code>via</code>&#8216; terminal. The <code>for</code> loop will continue until the value of traversal member is NULL or matches with address of the first node &lt;<i>StructVar</i>&gt; if it is a circular linked list. </p>
<p> If the LIST entry is specified using a struct list_head type variable, then <code>within</code> terminal must be used to specify the structure name &lt;<i>StructName</i>&gt; that is surrounding to it along with the struct list_head type member after &#8216;<code>:</code>&#8216; which is part of the linked list. In the erase statement &lt;<i>id</i>&gt; then denotes the structure that the list_head is contained in (ELEMENT_OF). </p>
<p> The below example illustrates how to use loop construct for traversing Array, linked list via next member and list_head. </p>
<p> <code>Example:</code> </p>
<p> Assuming following piece of code is from kernel module &#8216;mymodule&#8217;: </p>
<p> struct s1 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct *next;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct list_head list;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>char private[100];</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>void *key;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>long key_size;</p>
<p> }; </p>
<p> /* Global symbols */<br />
 struct s1 mystruct1;<br />
 static LIST_HEAD(s1_list_head);<br />
 struct s1 myarray[100]; </p>
<p> void foo()<br />
 {<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>struct s1 *s1_ptr;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>s1_ptr = malloc(&#8230;);</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>list_add(&amp;s1_ptr-&gt;list, &amp;s1_list_head);</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&#8230;</p>
<p> } </p>
<p> <code>makedumpfile.conf:</code><br />
 [mymodule]<br />
 # erase private fields from list starting with mystruct1 connected via<br />
 # &#8216;next&#8217; member:<br />
 for mys1 in mystruct1 via next<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.private</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.key size mys1.key_size</p>
<p> endfor </p>
<p> # erase private fields from list starting with list_head variable<br />
 # s1_list_head.<br />
 for mys1 in s1_list_head.next within s1:list<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.private</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.key size mys1.key_size</p>
<p> endfor </p>
<p> # erase private fields from all elements of the array myarray:<br />
 for mys1 in myarray<br />
 <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.private</p>
<p> <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>erase mys1.key size mys1.key_size</p>
<p> endfor<br />
 <code>EOF</code> </p>
<p> In the above example, the first <code>for</code> construct traverses the linked list through a specified structure variable <code>mystruct1</code> of type <code>struct s1</code>. The linked list can be traversed using &#8216;<code>next</code>&#8216; member of <code>mystruct1</code>. Hence a <code>via</code> terminal has been used to specify the traversal member name &#8216;<code>next</code>&#8216;. </p>
<p> The second <code>for</code> construct traverses the linked list through a specified struct list_head variable <code>s1_list_head.next</code>. The global symbol <code>s1_list_head</code> is a start address of the linked list and its <code>next</code> member points to the address of struct list_head type member &#8216;<code>list</code>&#8216; from <code>struct s1</code>. Hence a <code>within</code> terminal is used to specify the structure name &#8216;<code>s1</code>&#8216; that can be traversed using <code>s1_list_head.next</code> variable along with the name of struct list_head type member &#8216;<code>list</code>&#8216; which is part of the linked list that starts from <code>s1_list_head</code> global symbol. </p>
<p> The third <code>for</code> construct traverses the array elements specified through a array variable <code>myarray</code>.</p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/8-makedumpfile/">makedumpfile</a>(8) </p>
