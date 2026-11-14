---
title: "mib2c-conf(5)"
name: "mib2c-conf"
section: "5"
letter: "m"
url: "/docs/linux/man/5-mib2c-conf/"
---

mib2c.conf - How to write mib2c.conf files to do ANYTHING based on MIB input.

<h2>Synopsis</h2>

% cat &gt; mib2c.test.conf &lt;&lt; EOF @foreach $t table@ 
&nbsp;<wbr>&nbsp;Starting table&nbsp;$t 
&nbsp;<wbr>&nbsp;@foreach&nbsp;$c column@ 
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;echo&nbsp;$t has column&nbsp;$c which has a syntax of&nbsp;$c.syntax 
&nbsp;<wbr>&nbsp;@end@ 

 @end@ EOF 

 % mib2c -c mib2c.test.conf internet

<h2>Description</h2>

The mib2c.conf script language is a MIB-particular language designed to easily process MIB nodes in ways that you want. mib2c is a misnomer (for historical purposes), because you can produce anything (not just C code). Look in the Net-SNMP &quot;local&quot; directory for a bunch of example mib2c.*.conf files and behold the power before you.

<h2>Commands</h2>

All commands within mib2c.conf files are embraced by @ signs. Anything with an @ sign at the front and back of the line is generally supposed to be a mib2c specific command. These are detailed here:
<dl><dt>@open FILE@
<dd>writes generated output to FILE note that for file specifications, opening '-' will print to stdout.
<dt>@append FILE@
<dd>appends the given FILE
<dt>@close FILE@
<dd>closes the given FILE
<dt>@push@
<dd>save the current outputs, then clear outputs. Use with @open@ and @pop@ to write to a new file without interfering with current outputs.
<dt>@pop@
<dd>pop up the process() stack one level. Use after a @push@ to return to the previous set of open files.
<dt>@foreach $VAR scalar@
<dd>repeat iterate over code until @end@ setting $VAR to all known scalars
<dt>@foreach $VAR table@
<dd>repeat iterate over code until @end@ setting $VAR to all known tables
<dt>@foreach $VAR column@
<dd>repeat iterate over code until @end@ setting $VAR to all known columns within a given table. Obviously this must be called within a foreach-table clause.
<dt>@foreach $VAR nonindex@
<dd>repeat iterate over code until @end@ setting $VAR to all known non-index columns within a given table. Obviously this must be called within a foreach-table clause.
<dt>@foreach $VAR internalindex@
<dd>repeat iterate over code until @end@ setting $VAR to all known internal index columns within a given table. Obviously this must be called within a foreach-table clause.
<dt>@foreach $VAR externalindex@
<dd>repeat iterate over code until @end@ setting $VAR to all known external index columns within a given table. Obviously this must be called within a foreach-table clause.
<dt>@foreach $VAR index@
<dd>repeat iterate over code until @end@ setting $VAR to all known indexes within a given table. Obviously this must be called within a foreach-table clause.
<dt>@foreach $VAR notifications@
<dd>repeat iterate over code until @end@ setting $VAR to all known notifications
<dt>@foreach $VAR varbinds@
<dd>repeat iterate over code until @end@ setting $VAR to all known varbinds Obviously this must be called within a foreach-notifications clause.
<dt>@foreach $LABEL, $VALUE enum@
<dd>repeat iterate over code until @end@ setting $LABEL and $VALUE to the label and values from the enum list.
<dt>@foreach $RANGE_START, $RANGE_END range NODE@
<dd>repeat iterate over code until @end@ setting $RANGE_START and $RANGE_END to the legal accepted range set for a given mib NODE.
<dt>@foreach $var stuff a b c d@
<dd>repeat iterate over values a, b, c, d as assigned generically (ie, the values are taken straight from the list with no mib-expansion, etc).
<dt>@while expression@
<dd>repeat iterate over code until the expression is false
<dt>@eval $VAR = expression@
<dd>evaluates expression and assigns the results to $VAR. This is not a full perl eval, but sort of a &quot;&quot;psuedo&quot;&quot; eval useful for simple expressions while keeping the same variable name space. See below for a full-blown export to perl.
<dt>@perleval STUFF@
<dd>evaluates STUFF directly in perl. Note that all mib2c variables interpereted within .conf files are in $vars{NAME} and that a warning will be printed if STUFF does not return 0. (adding a 'return 0;' at the end of STUFF is a workaround.
<dt>@startperl@
<dd><dt>@endperl@
<dd>treats everything between these tags as perl code, and evaluates it.
<dt>@next@
<dd>restart foreach; should only be used inside a conditional. skips out of current conditional, then continues to skip to end for the current foreach clause.
<dt>@if expression@
<dd>evaluates expression, and if expression is true processes contained part until appropriate @end@ is reached. If the expression is false, the next @elsif expression@ expression (if it exists) will be evaluated, until an expression is true. If no such expression exists and an @else@ clause is found, it will be evaluated.
<dt>@ifconf file@
<dd>If the specified file can be found in the conf file search path, and if found processes contained part until an appropriate @end@ is found. As with a regular @if expression@, @elsif expression@ and @else@ can be used.
<dt>@ifdir dir@
<dd>If the specified directory exists, process contained part until an appropriate @end@ is found. As with a regular @if expression@, @elsif expression@ and @else@ can be used.
<dt>@define NAME@
<dd><dt>@enddefine@
<dd>Memorizes &quot;&quot;stuff&quot;&quot; between the define and enddefine tags for later calling as NAME by @calldefine NAME@.
<dt>@calldefine NAME@
<dd>Executes stuff previously memorized as NAME.
<dt>@printf &quot;expression&quot; stuff1, stuff2, ...@
<dd>Like all the other printf's you know and love.
<dt>@run FILE@
<dd>Sources the contents of FILE as a mib2c file, but does not affect current files opened.
<dt>@include FILE@
<dd>Sources the contents of FILE as a mib2c file and appends its output to the current output.
<dt>@prompt $var QUESTION@
<dd>Presents the user with QUESTION, expects a response and puts it in $var
<dt>@print STUFF@
<dd>Prints stuff directly to the users screen (ie, not to where normal mib2c output goes)
<dt>@quit@
<dd>Bail out (silently)
<dt>@exit@
<dd>Bail out!</dl>

<h2>Variables</h2>

Variables in the mib2c language look very similar to perl variables, in that they start with a &quot;$&quot;. They can be used for anything you want, but most typically they'll hold mib node names being processed by @foreach ...@ clauses. 

 They also have a special properties when they are a mib node, such that adding special suffixes to them will allow them to be interpreted in some fashion. The easiest way to understand this is through an example. If the variable 'x' contained the word 'ifType' then some magical things happen. In mib2c output, anytime $x is seen it is replaced with &quot;ifType&quot;. Additional suffixes can be used to get other aspects of that mib node though. If $x.objectID is seen, it'll be replaced by the OID for ifType: &quot;.1.3.6.1.2.1.2.2.1.3&quot;. Other suffixes that can appear after a dot are listed below. 

 One last thing: you can use things like $vartext immediately ending in some other text, you can use {}s to get proper expansion of only part of the mib2c input. IE, $xtext will produce &quot;$xtext&quot;, but ${x}text will produce &quot;ifTypetext&quot; instead.
<dl><dt>$var.uc
<dd>all upper case version of $var
<dt>$var.objectID
<dd>dotted, fully-qualified, and numeric OID
<dt>$var.commaoid
<dd>comma separated numeric OID for array initialization
<dt>$var.oidlength
<dd>length of the oid
<dt>$var.subid
<dd>last number component of oid
<dt>$var.module
<dd>MIB name that the object comes from
<dt>$var.parent
<dd>contains the label of the parent node of $var.
<dt>$var.isscalar
<dd>returns 1 if var contains the name of a scalar
<dt>$var.iscolumn
<dd>returns 1 if var contains the name of a column
<dt>$var.children
<dd>returns 1 if var has children
<dt>$var.perltype
<dd>node's perl SYNTAX ($SNMP::MIB{node}{'syntax'})
<dt>$var.type
<dd>node's ASN_XXX type (Net-SNMP specific #define)
<dt>$var.decl
<dd>C data type (char, u_long, ...)
<dt>$var.readable
<dd>1 if an object is readable, 0 if not
<dt>$var.settable
<dd>1 if an object is writable, 0 if not
<dt>$var.creatable
<dd>1 if a column object can be created as part of a new row, 0 if not
<dt>$var.noaccess
<dd>1 if not-accessible, 0 if not
<dt>$var.accessible
<dd>1 if accessible, 0 if not
<dt>$var.storagetype
<dd>1 if an object is a StorageType object, 0 if not
<dt>$var.rowstatus
<dd>1 if an object is a RowStatus object, 0 if not 'settable', 'creatable', 'lastchange', 'storagetype' and 'rowstatus' can also be used with table variables to indicate whether it contains writable, creatable, LastChange, StorageType or RowStatus column objects
<dt>$var.hasdefval
<dd>returns 1 if var has a DEFVAL clause
<dt>$var.defval
<dd>node's DEFVAL
<dt>$var.hashint
<dd>returns 1 if var has a HINT clause
<dt>$var.hint
<dd>node's HINT
<dt>$var.ranges
<dd>returns 1 if var has a value range defined
<dt>$var.enums
<dd>returns 1 if var has enums defined for it.
<dt>$var.access
<dd>node's access type
<dt>$var.status
<dd>node's status
<dt>$var.syntax
<dd>node's syntax
<dt>$var.reference
<dd>node's reference
<dt>$var.description
<dd>node's description</dl>

<h2>See Also</h2>

<a HREF="/docs/linux/man/1-mib2c/">mib2c</a>(1) 
