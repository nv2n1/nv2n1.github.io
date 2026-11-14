---
title: "setrans-conf(8)"
name: "setrans-conf"
section: "8"
letter: "s"
url: "/docs/linux/man/8-setrans-conf/"
---

setrans.conf - translation configuration file for MCS/MLS SELinux systems 

<h2>Description</h2>

The <i>/etc/selinux/{SELINUXTYPE}/setrans.conf</i> configuration file specifies the way that SELinux MCS/MLS labels are translated into human readable form by the mcstransd daemon. The default policies support 16 sensitivity levels (s0 through s15) and 1024 categories (c0 through c1023). Multiple categories can be separated with commas (c0,c1,c3,c5) and a range of categories can be shortened using dot notation (c0.c3,c5).

<h3>Keywords</h3>

<dl><dt>Base
<dd>once a base is declared, subsequent sensitivity label definitions will have all modifiers applied to them during translation. Sensitivity labels defined before the base declaration are immediately cached and no modifiers will be applied these are used as direct translations.
<dt>Default
<dd>defines the category bit range that will be used for inverse bits.
<dt>Domain
<dd>creates a new domain with the supplied name.
<dt>Include
<dd>read and process the contents of the specified configuration file.
<dt>Join
<dd>defines a character used to separate members of a modifier group when more than one is specified (ex. USA/AUS).
<dt>ModifierGroup
<dd>a means of grouping category bit definitions by how they modify the sensitivity label.
<dt>Prefix
<dd>word(s) that may proceed member(s) of a modifier group (ex. REL USA).
<dt>Suffix
<dd>word(s) that may follow member(s) of a modifier group (ex. USA EYES ONLY).
<dt>Whitespace
<dd>defines the set of acceptable white space characters that may be used in label being translated.</dl>

<h3>Sensitivity Level Definition Examples</h3>

<dl><dt>s0=SystemLow
<dd>defines a translation of s0 (the lowest sensitivity level) with no categories to SystemLow.
<dt>s15:c0.c1023=SystemHigh
<dd>defines a translation of s15:c0.c1023 to SystemHigh. c0.c1023 is shorthand for all categories. A colon separates the sensitivity level and categories.
<dt>s0-s15:c0.c1023=SystemLow-SystemHigh
<dd>defines a range translation of of s0-s15:c0.c1023 to SystemLow-SystemHigh. The two range components are separated by a dash.
<dt>s0:c0=PatientRecord
<dd>defines a translation of sensitivity s0 with category c0 to PatientRecord.
<dt>s0:c1=Accounting
<dd>defines a translation of sensitivity s0 with category c1 to Accounting.
<dt>s2:c1,c2,c3=Confidential3Categories
<dd><dt>s2:c1.c3=Confidential3Categories
<dd>both define a translation of sensitivity s2 with categories c1, c2 and c3 to Confidential3Categories.
<dt>s5=TopSecret
<dd>defines a translation of sensitivity s5 with no categories to TopSecret.</dl>

<h3>Constraint Examples</h3>

<dl><dt>c0!c1
<dd>if category bits 0 and 1 are both set, the constraint will fail and the original context will be returned.
<dt>c5.c9&gt;c1
<dd>if category bits 5 through 9 are set, bit 1 must also be set or the constraint will fail and the original context will be returned.
<dt>s1!c5,c9
<dd>if category bits 5 and 9 are set and the sensitivity level is s1, the constraint will fail and the original context will be returned. 

<h2>Author</h2>

&nbsp;<wbr>Written by Joe Nall&nbsp;<wbr>&lt;joe [at] nall.com&gt;. 
&nbsp;<wbr>Updated by Ted X. Toth&nbsp;<wbr>&lt;txtoth [at] gmail.com&gt;. 
&nbsp;<wbr>

<h2>See Also</h2>

<a HREF="/docs/linux/man/8-selinux/">selinux</a>(8), <a HREF="/docs/linux/man/8-mcs/">mcs</a>(8), <a HREF="/docs/linux/man/8-mls/">mls</a>(8), <a HREF="/docs/linux/man/1-chcon/">chcon</a>(1) 

<h2>Files</h2>

/etc/selinux/{SELINUXTYPE}/setrans.conf 
 /usr/share/mcstrans/examples
