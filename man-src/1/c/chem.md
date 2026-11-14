---
title: "chem(1)"
name: "chem"
section: "1"
letter: "c"
url: "/docs/linux/man/1-chem/"
description: "chem – groff preprocessor for producing chemical structure diagrams"
---

<h2 class="name">NAME</h2>
<p> chem &#8211; groff preprocessor for producing chemical structure diagrams </p>
<h2>SYNOPSIS</h2>
<p> [ <code>&#8212;</code> ] [<i>filespec</i> &#8230; ] <code>-h</code> <code>&#8211;help</code> <code>-v</code> <code>&#8211;version</code></p>
<h2>DESCRIPTION</h2>
<p> <i>chem</i> produces chemical structure diagrams. Today&#8217;s version is best suited for organic chemistry (bonds, rings). The <code>chem</code> program is a <code>groff</code> preprocessor like <code>eqn</code>, <code>pic</code>, <code>tbl</code>, etc. It generates <i>pic</i> output such that all <i>chem</i> parts are translated into diagrams of the <i>pic</i> language. </p>
<p> A <i>filespec</i> argument is either a file name of an existing file or a minus character <code>&#8211;</code>, meaning standard input. If no argument is specified then standard input is taken automatically. <code>-h</code> and <code>&#8211;help</code> display a usage message, whereas <code>-v</code> and <code>&#8211;version</code> display version information; all exit. </p>
<p> The program <code>chem</code> originates from the Perl source file <i>chem.pl</i>. It tells <code>pic</code> to include a copy of the macro file <i>chem.pic</i>. Moreover the <i>groff</i> source file <i>pic.tmac</i> is loaded. </p>
<p> In a style reminiscent of <i>eqn</i> and <i>pic</i>, the <i>chem</i> diagrams are written in a special language. </p>
<p> A set of <i>chem</i> lines looks like this</p>
<dl>
<dt>
<dd>
<pre>
<code>.cstart
</code><i>chem data</i>
.cend
</pre>
</dl>
<p> Lines containing the keywords <code>.cstart</code> and <code>.cend</code> start and end the input for <code>chem</code>, respectively. In <i>pic</i> context, i.e., after the call of <code>.PS</code>, <i>chem</i> input can optionally be started by the line <code>begin~chem</code> and ended by the line with the single word <code>end</code> instead. </p>
<p> Anything outside these initialization lines is copied through without modification; all data between the initialization lines is converted into <i>pic</i> commands to draw the diagram. </p>
<p> As an example,</p>
<dl>
<dt>
<dd>
<pre>
<code>.cstart
CH3
bond
CH3
.cend
</code></pre>
</dl>
<p> prints two <code>CH3</code> groups with a bond between them. </p>
<p> To actually view this, you must run <code>chem</code> followed by <code>groffer</code>:</p>
<dl>
<dt>
<dd> <code>chem [file &#8230; ] | groffer</code></dl>
<p> If you want to create just <code>groff</code> output, you must run <code>chem</code> followed by <code>groff</code> with the option <code>-p</code> for the activation of <code>pic</code>:</p>
<dl>
<dt>
<dd> <code>chem [file &#8230; ] | groff -p &#8230; </code></dl>
<h2>THE LANGUAGE</h2>
<p> The <i>chem</i> input language is rather small. It provides rings of several styles and a way to glue them together as desired, bonds of several styles, moieties (e.g., <code>C</code>, <code>NH3</code>, &#8230; , and strings.</p>
<h3>Setting Variables</h3>
<p> There are some variables that can be set by commands. Such commands have two possible forms, either</p>
<dl>
<dt>
<dd>
<p> <i>variable value</i></dl>
<p> or</p>
<dl>
<dt>
<dd>
<p> <i>variable </i><code>=</code><i> value</i></dl>
<p> This sets the given <i>variable</i> to the argument <i>value</i>. If more arguments are given only the last argument is taken, all other arguments are ignored. </p>
<p> There are only a few variables to be set by these commands:</p>
<dl>
<dt><code>textht</code><i> arg</i></p>
<dd> Set the height of the text to <i>arg</i>; default is 0.16.</p>
<dt><code>cwid</code><i> arg</i></p>
<dd> Set the character width to <i>arg</i>; default is 0.12.</p>
<dt><code>db</code><i> arg</i></p>
<dd> Set the bond length to <i>arg</i>; default is 0.2.</p>
<dt><code>size</code><i> arg</i></p>
<dd> Scale the diagram to make it look plausible at point size <i>arg</i>; default is 10 point.</dl>
<h3>Bonds</h3>
<p> This</p>
<dl>
<dt>
<dd> [<i>direction</i>] [<i>length n</i>] [<code>from&nbsp;</code><i>Name</i>|<i>picstuff</i>]</dl>
<p> draws a single bond in direction from nearest corner of <i>Name</i>. <code>bond</code> can also be <code>double bond</code>, <code>front bond</code>, <code>back bond</code>, etc. (We will get back to <i>Name</i> soon.) </p>
<p> <i>direction</i> is the angle in degrees (0~up, positive clockwise) or a direction word like <code>up</code>, <code>down</code>, <code>sw</code> (=~southwest), etc. If no direction is specified, the bond goes in the current direction (usually that of the last bond). </p>
<p> Normally the bond begins at the last object placed; this can be changed by naming a <code>from</code> place. For instance, to make a simple alkyl chain:</p>
<dl>
<dt>
<dd>
<table>
<tr VALIGN=top>
<td><code>CH3</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>bond</code></td>
<td>(this one goes right from the CH3)
</td>
</tr>
<tr VALIGN=top>
<td><code>C</code></td>
<td>(at the right end of the bond)
</td>
</tr>
<tr VALIGN=top>
<td><code>double bond up</code></td>
<td>(from the C)
</td>
</tr>
<tr VALIGN=top>
<td><code>O</code></td>
<td>(at the end of the double bond)
</td>
</tr>
<tr VALIGN=top>
<td><code>bond right from C</code></td>
<td>
</td>
</tr>
<tr VALIGN=top>
<td><code>CH3</code></td>
<td>
</td>
</tr>
</table>
</dl>
<p> A length in inches may be specified to override the default length. Other <i>pic</i> commands can be tacked on to the end of a bond command, to created dotted or dashed bonds or to specify a <code>to</code> place.</p>
<h3>Rings</h3>
<p> There are lots of rings, but only 5 and 6-sided rings get much support. <code>ring</code> by itself is a 6-sided ring; <code>benzene</code> is the benzene ring with a circle inside. <code>aromatic</code> puts a circle into any kind of ring.</p>
<dl>
<dt>
<dd> [<code>pointing&nbsp;</code>(<code>up</code>|<code>right</code>|<code>left</code>|<code>down</code>)] [<code>aromatic</code>] [<code>put Mol at&nbsp;</code><i>n/</i>] [<code>double&nbsp;</code><i>i</i>,<i>j&nbsp;/</i><i>k</i>,<i>l&nbsp;/</i>&#8230; [<i>picstuff</i>]</dl>
<p> The vertices of a ring are numbered 1, 2, &#8230; from the vertex that points in the natural compass direction. So for a hexagonal ring with the point at the top, the top vertex is~1, while if the ring has a point at the east side, that is vertex~1. This is expressed as</p>
<dl>
<dt>
<dd>
<pre>
R1: ring pointing up
R2: ring pointing right
</pre>
</dl>
<p> The ring vertices are named <code>.V1</code>, &#8230; , <code>.V</code><i>n</i>, with <code>.V1</code> in the pointing direction. So the corners of <code>R1</code> are <code>R1.V1</code> (the <i>top</i>), <code>R1.V2</code>, <code>R1.V3</code>, <code>R1.V4</code> (the <i>bottom</i>), etc., whereas for <code>R2</code>, <code>R2.V1</code> is the rightmost vertex and <code>R2.V4</code> the leftmost. These vertex names are used for connecting bonds or other rings. For example,</p>
<dl>
<dt>
<dd>
<pre>
R1: benzene pointing right
R2: benzene pointing right with .V6 at R1.V2
</pre>
</dl>
<p> creates two benzene rings connected along a side. </p>
<p> Interior double bonds are specified as <code>double&nbsp;</code><i>n1</i><code>,</code><i>n2 n3</i><code>,</code><i>n4&nbsp;</i>&#8230; ; each number pair adds an interior bond. So the alternate form of a benzene ring is</p>
<dl>
<dt>
<dd> <code>ring double 1,2 3,4 5,6</code></dl>
<p> Heterocycles (rings with something other than carbon at a vertex) are written as <code>put&nbsp;</code><i>X&nbsp;</i><code>at&nbsp;</code><i>V</i>, as in</p>
<dl>
<dt>
<dd> <code>R: ring put N at 1 put O at 2</code></dl>
<p> In this heterocycle, <code>R.N</code> and <code>R.O</code> become synonyms for <code>R.V1</code> and <code>R.V2</code>. </p>
<p> There are two 5-sided rings. <code>ring5</code> is pentagonal with a side that matches the 6-sided ring; it has four natural directions. A <code>flatring</code> is a 5-sided ring created by chopping one corner of a 6-sided ring so that it exactly matches the 6-sided rings. </p>
<p> The description of a ring has to fit on a single line.</p>
<h3>Moieties and Strings</h3>
<p> A moiety is a string of characters beginning with a capital letter, such as N(C2H5)2. Numbers are converted to subscripts (unless they appear to be fractional values, as in N2.5H). The name of a moiety is determined from the moiety after special characters have been stripped out: e.g., N(C2H5)2) has the name NC2H52. </p>
<p> Moieties can be specified in two kinds. Normally a moiety is placed right after the last thing mentioned, separated by a semicolon surrounded by spaces, e.g.,</p>
<dl>
<dt>
<dd> <code>B1: bond ; OH</code></dl>
<p> Here the moiety is <code>OH</code>; it is set after a bond. </p>
<p> As the second kind a moiety can be positioned as the first word in a <i>pic</i>-like command, e.g.,</p>
<dl>
<dt>
<dd> <code>CH3 at C + (0.5,0.5)</code></dl>
<p> Here the moiety is <code>CH3</code>. It is placed at a position relative to <code>C</code>, a moiety used earlier in the chemical structure. </p>
<p> So moiety names can be specified as <i>chem</i> positions everywhere in the <i>chem</i> code. Beneath their printing moieties are names for places. </p>
<p> The moiety <code>BP</code> is special. It is not printed but just serves as a mark to be referred to in later <i>chem</i> commands. For example,</p>
<dl>
<dt>
<dd> <code>bond ; BP</code></dl>
<p> sets a mark at the end of the bond. This can be used then for specifying a place. The name <code>BP</code> is derived from <i>branch point</i> (i.e., line crossing). </p>
<p> A string within double quotes <code>&quot;</code> is interpreted as a part of a <i>chem</i> command. It represents a string that should be printed (without the quotes). Text within quotes &quot;&#8230; &quot; is treated more or less like a moiety except that no changes are made to the quoted part.</p>
<h3>Names</h3>
<p> In the alkyl chain above, notice that the carbon atom <code>C</code> was used both to draw something and as the name for a place. A moiety always defines a name for a place; you can use your own names for places instead, and indeed, for rings you will have to. A name is just</p>
<dl>
<dt>
<dd> <i>Name</i><code>:</code> &#8230;</dl>
<p> <i>Name</i> is often the name of a moiety like <code>CH3</code>, but it need not to be. Any name that begins with a capital letter and which contains only letters and numbers is valid:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>First:</code></p>
<dd> <code>bond</code> <code>bond 30 from First</code></dl>
</dl>
<h3>Miscellaneous</h3>
<p> The specific construction</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>bond&nbsp;</code>&#8230; <code> ; moiety</code></p>
<dd></dl>
</dl>
<p> is equivalent to</p>
<dl>
<dt>
<dd>
<pre>
bond
moiety
</pre>
</dl>
<p> Otherwise, each item has to be on a separate line (and only one line). Note that there must be whitespace after the semicolon which separates the commands. </p>
<p> A period character <code>.</code> or a single quote <code>&#8216;</code> in the first column of a line signals a <i>troff</i> command, which is copied through as-is. </p>
<p> A line whose first non-blank character is a hash character (<code>#</code>) is treated as a comment and thus ignored. However, hash characters within a word are kept. </p>
<p> A line whose first word is <code>pic</code> is copied through as-is after the word <code>pic</code> has been removed. </p>
<p> The command</p>
<dl>
<dt>
<dd> <code>size</code> <i>n</i></dl>
<p> scales the diagram to make it look plausible at point size~<i>n</i> (default is 10~point). </p>
<p> Anything else is assumed to be <i>pic</i> code, which is copied through with a label. </p>
<p> Since <code>chem</code> is a <code>pic</code> preprocessor, it is possible to include <i>pic</i> statements in the middle of a diagram to draw things not provided for by <i>chem</i> itself. Such <i>pic</i> statements should be included in <i>chem</i> code by adding <code>pic</code> as the first word of this line for clarity. </p>
<p> The following <i>pic</i> commands are accepted as <i>chem</i> commands, so no <code>pic</code> command word is needed:</p>
<dl>
<dt>
<dd> <code>define</code> Start the definition of <i>pic</i> macro within <i>chem</i>.</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>[</code></p>
<dd> Start a block composite.</p>
<dt><code>]</code></p>
<dd> End a block composite.</p>
<dt><code>{</code></p>
<dd> Start a macro definition block.</p>
<dt><code>}</code></p>
<dd> End a macro definition block.</dl>
</dl>
</dl>
<p> The macro names from <code>define</code> statements are stored and their call is accepted as a <i>chem</i> command as well.</p>
<h3>WISH LIST</h3>
<p> This TODO list was collected by Brian Kernighan. </p>
<p> Error checking is minimal; errors are usually detected and reported in an oblique fashion by <i>pic</i>. </p>
<p> There is no library or file inclusion mechanism, and there is no shorthand for repetitive structures. </p>
<p> The extension mechanism is to create <i>pic</i> macros, but these are tricky to get right and don&#8217;t have all the properties of built-in objects. </p>
<p> There is no in-line chemistry yet (e.g., analogous to the $&#8230; $ construct of eqn). </p>
<p> There is no way to control entry point for bonds on groups. Normally a bond connects to the carbon atom if entering from the top or bottom and otherwise to the nearest corner. </p>
<p> Bonds from substituted atoms on heterocycles do not join at the proper place without adding a bit of <i>pic</i>. </p>
<p> There is no decent primitive for brackets. </p>
<p> Text (quoted strings) doesn&#8217;t work very well. </p>
<p> A squiggle bond is needed.</p>
<h2>FILES</h2>
<dl>
<dt><i>/usr/:share/:groff/:1.22.4/pic/chem.pic</i></p>
<dd> A collection of <i>pic</i> macros needed by <code>chem</code>.</p>
<dt><i>/usr/:share/:groff/:1.22.4/:tmac/pic.tmac</i></p>
<dd> A macro file which redefines <code>.PS</code> and <code>.PE</code> to center <i>pic</i> diagrams.</p>
<dt><i>/usr/:share/:doc/:groff-base/examples/chem/</i>*<i>.chem</i></p>
<dd> Example files for <i>chem</i>.</p>
<dt><i>/usr/:share/:doc/:groff-base/examples/chem/122/</i>*<i>.chem</i></p>
<dd> Example files from the classical <i>chem</i> article <i>CHEM &#8211; A Program for Typesetting Chemical Structure Diagrams</i> [CSTR~#122].</dl>
<h2>AUTHORS</h2>
<p> The GNU version of <code>chem</code> was written by Bernd Warken It is based on the documentation of Brian Kernighan&#8217;s original <i>awk</i> version of <i>chem</i> at</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-groff/">groff</a></code>(1), <code><a href="/docs/linux/man/1-pic/">pic</a></code>(1), <code><a href="/docs/linux/man/1-groffer/">groffer</a></code>(1). </p>
<p> You can still get the original chem awk source Its <code>README</code> file was used for this manual page. </p>
<p> The other classical document on <i>chem</i> is <i>CHEM &#8211; A Program for Typesetting Chemical Structure Diagrams</i> [CSTR~#122] </p>
<h2>Index</h2>
