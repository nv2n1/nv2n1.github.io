---
title: "v2cc(5)"
name: "v2cc"
section: "5"
letter: "v"
url: "/docs/linux/man/5-v2cc/"
description: "v2cc.libs – VHDL library mapping file for the FreeHDL compiler/simulator."
---

<p>v2cc.libs &#8211; VHDL library mapping file for the FreeHDL compiler/simulator.</p>
<h2>Description</h2>
<p><code>FreeHDL</code> is a compiler/simulator suite for the hardware description language VHDL. VHDL&#8217;93 as well as VHDL&#8217;87 standards are supported. <code>FreeHDL</code> translates the original VHDL source FILEs into C++. Then, the C++ source can be compiled and linked to the kernel to build the simulation program. Starting the generated executable will simulate the corresponding VHDL model. The actual build process to generate the simulator from the VHDL source is a complex process which is handled by the <code>gvhdl</code> script. FreeHDL does not have a opaque notion of design libraries. VHDL files are not pre-analyzed and checked into some library data base as in other VHDL compiler/simulator systems. Instead, whenever a reference to a design unit needs to be made, FreeHDL parses the VHDL code of that design unit from fresh. Therefore, it needs to be able to find the source file of a design unit given the VHDL name of that unit. Thus, as far as FreeHDL is concerned, a design library is a mapping from VHDL identifiers to file names. There is also a mapping for getting library names from mapping files. Such a mapping is specified via a &quot;mapping file&quot;. It contains a list of pattern rules that each transform a certain class of identifiers into file names. The syntax of a mapping file is:<br />
&nbsp;<wbr>&nbsp;<wbr>Lexical:<br />
&nbsp;<wbr>&nbsp;<wbr>litchar:&nbsp;<wbr>&#8216;a&#8217;..&#8217;z&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;A&#8217;..&#8217;Z&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;0&#8217;..&#8217;9&#8242;&nbsp;<wbr>|&nbsp;<wbr>&#8216;_&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;/&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;-&#8216;&nbsp;<wbr>|&nbsp;<wbr>&#8216;.&#8217;&nbsp;<wbr>escchar<br />
&nbsp;<wbr>&nbsp;<wbr>escchar:&nbsp;<wbr>&#8216;\&#8217;&nbsp;<wbr>char<br />
&nbsp;<wbr>&nbsp;<wbr>whitespace:&nbsp;<wbr>&#8216;&nbsp;<wbr>&#8216;&nbsp;<wbr>|&nbsp;<wbr>&#8216;
&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;	&#8217;&nbsp;<wbr>| comment<br />
&nbsp;<wbr>&nbsp;<wbr>comment:&nbsp;<wbr>&#8216;#&#8217;&nbsp;<wbr>any_character*&nbsp;<wbr>&#8216;
&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>opchar:&nbsp;<wbr>&#8216;:&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;,&#8217;&nbsp;<wbr>|&nbsp;<wbr>&#8216;(&#8216;&nbsp;<wbr>|&nbsp;<wbr>&#8216;)&#8217;<br />
&nbsp;<wbr>&nbsp;<wbr>specchar: every printable char except litchar, whitespace and opchar<br />
&nbsp;<wbr>&nbsp;<wbr>symchar: litchar | specchar<br />
&nbsp;<wbr>&nbsp;<wbr>symbol: symchar+<br />
&nbsp;<wbr>&nbsp;<wbr>Grammar:<br />
&nbsp;<wbr>&nbsp;<wbr>mapping: version patternrule* </p>
<pre><code>version: &quot;v2cc_mapfile&quot; &quot;0&quot;</code></pre>
<p>&nbsp;<wbr>&nbsp;<wbr>patternrule: symbol&nbsp;<wbr>[&nbsp;<wbr>&#8216;:&#8217;&nbsp;<wbr>symbol&nbsp;<wbr>] Comments are ignored. A mapping files specifies a sequence of pattern rules. When transforming an identifier, each rule is tried in turn and the first one that matches is chosen. A rule looks like<br />
&nbsp;<wbr>&nbsp;<wbr>pattern: filename When the &quot;: filename&quot; part is omitted, it defaults to &quot;patternEXT&quot; where &quot;EXT&quot; is determined by the user of the mapping file. The &quot;pattern&quot; can contain the special character &quot;&lt;&quot; which introduces a `wildcard&#8217;. The &quot;&lt;&quot; must be followed by a &quot;&gt;&quot;, with arbitrary characters inbetween. These characters form the name of the wildcard. A wildcard matches any sequence of characters. There can be any number of wildcards in the pattern, but each must have a unique name. The &quot;filename&quot; can also contain the character &quot;&lt;&quot;, followed by a name, followed by &quot;&gt;&quot;. There, it introduces a `wildcard substitution&#8217;. It will be replaced with the characters that matched the wildcard with the same name in &quot;pattern&quot;. When there is no wildcard in &quot;pattern&quot; with the right name, it will be replaced with nothing. While doing this replacement, the characters &quot;#&quot; and &quot;/&quot; are replaced as &quot;##&quot;, and &quot;#-&quot; respectively. No other character translations are done, so if you have funny characters in your VHDL identifiers, you will have funny characters in your filenames. Before doing the comparison with the patterns, the VHDL identifier is brought into a canonical form: when it is not an abstract identifier, all its characters are down-cased. When the resulting filename is relative (does not begin with &quot;/&quot;), it is prefixed with the directory of the mapping file. A non-existent mapping file is equivalent to the single rule<br />
&nbsp;<wbr>&nbsp;<wbr>&lt;&gt; An empty mapping file is just that: an empty mapping. The mapping does not need to be reversible. It is OK when multiple identifiers map to a single filename. No special character besides &quot;&lt;&quot; and &quot;&gt;&quot; is valid in &quot;pattern&quot; or &quot;filename&quot;. They are reserved for future extensions. The mapping files for going from design unit names to filenames are found by looking into directories specified by the `v2cc library path&#8217;. You can use the environment variable V2CC_LIBRARY_PATH and command line options to define the path. When the environment variable is not set, it defaults to a value that makes the standard libraries available that are distributed and installed with v2cc itself. When it is set, it completely overwrites this default value. The variable V2CC_LIBRARY_PATH consists of &quot;:&quot; separated filenames. The filename &quot;*&quot; is replaced with the default value mentioned above. In addition to the environment variable, you can use the &quot;-L libdir&quot; command line option with v2cc. The directories specified with &quot;-L&quot; are added in front of the ones specified by V2CC_LIBRARY_PATH. In the final library path, they appear in the same order as on the command line. Looking for a design unit named UNIT in a library named LIB is done like this: </p>
<pre><code>for each component of the library path, L

if L is a regular file
set LMAP to L

else if L is a directory
set LMAP to L/v2cc.libs

else
continue with next component

translate LIB into FLIB using LMAP with EXT=&quot;&quot;

if FLIB.vhdl exists
terminate with FLIB.vhdl as the result

if FLIB.v2cc exists
set UMAP to FLIB.v2cc

else if FLIB is a directory
set UMAP to FLIB/v2cc.units

else
continue with next component

translate UNIT into FUNIT using UMAP with EXT=&quot;.vhdl&quot;

terminate with FUNIT as the result
terminate unsuccessfully
</code></pre>
<p> This mechanism is used for all design units that are referenced from within VHDL code (or via other means). There is a complication with architectures and package bodies, though, because they are not uniquely identified by a single identifier. For them, a artificial identifier is constructed. Architectures get names of the form<br />
&nbsp;<wbr>&lt;entity&gt;(&lt;architecture&gt;) while package bodies become<br />
&nbsp;<wbr>&lt;package&gt;(body) For example, &quot;architecture struct of model&quot; is turned into &quot;model(struct)&quot; and &quot;package body misc&quot; is turned into &quot;misc(body)&quot;. When a design file contains multiple design units, they are all parsed, checked for correctness and remembered, but only the needed unit will be used for code generation. That is, when a design file contains both a package header and a package body and the package header is referenced from another design unit, no code will be generated for the package body. When one of the ignored units will be referenced later in the same invocation of v2cc, the design file will not be read again because all design units are retained in core.</p>
<h2>Examples</h2>
<p>The simplest situation is when you have no mapping files at all. A design library is then a directory on your library path. The name of that directory is that of the library in VHDL. Each file in that directory with a &quot;.vhdl&quot; extension is used for a design unit with the same name as the file without the extension. </p>
<p> Say you have this directory structure </p>
<p>&nbsp;<wbr>somedir/<br />
std/<br />
&nbsp;<wbr>&nbsp;<wbr>standard.vhdl<br />
&nbsp;<wbr>&nbsp;<wbr>textio.vhdl<br />
ieee/<br />
&nbsp;<wbr>&nbsp;<wbr>numeric_bit.vhdl<br />
&nbsp;<wbr>&nbsp;<wbr>std_logic_1164.vhdl </p>
<p> When you put &quot;somedir&quot; into your library path, you have access to the design units </p>
<p>&nbsp;<wbr>STD.STANDARD<br />
&nbsp;<wbr>STD.TEXTIO<br />
&nbsp;<wbr>IEEE.NUMERIC_BIT<br />
&nbsp;<wbr>IEEE.STD_LOGIC_1164 </p>
<p> In this situation, you have one file per design unit. When you have one file per design library, it would look like this </p>
<p>&nbsp;<wbr>somedir/<br />
fmf.vhdl </p>
<p> All references to design units in the FMF design library would be routed to &quot;fmf.vhdl&quot;. </p>
<p> As another example assume that all VHDL libraries are mapped into subdirs starting from root directory &quot;/foo&quot;. Further, assume that there are VHDL libraries named &quot;lib1&quot; and &quot;lib2&quot;. They shall be mapped to subdir &quot;/foo/lib1_dir&quot; and &quot;/foo/lib2_dir&quot;. Hence, the file/directory structure is as follows: </p>
<p> /foo <tt>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;- library root directory<br />
 /foo/v2cc.libs <tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;- mapping control file<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><br />
 /foo/lib1_dir<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;- library dir for VHDL library lib1<br />
 /foo/lib1_dir/comp1.vhdl &lt;- file that contains VHDL model comp1 /foo/lib2_dir<tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt><tt>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr></tt>&lt;- library dir for VHDL library lib2<br />
 /foo/lib2_dir/comp2.vhdl &lt;- file that contains VHDL model comp2 </p>
<p> Then, file &quot;/foo/v2cc.libs&quot; should contain: </p>
<p> v2cc_mapfile 0 lib1 : lib1_dir lib2 : lib2_dir </p>
<p> In order to compile a design named comp1 (stored in file comp1.vhdl) into VHDL library lib1 goto subdir &quot;/foo/lib1_dir&quot; and execute: </p>
<p>&nbsp;<wbr>gvhdl -c -L .. -l lib1 comp1.vhdl </p>
<p> Note that option &quot;-l lib1&quot; forces the compiler to associate the model stored in &quot;comp1.vhdl&quot; with VHDL library lib1. Note further, that the compiler switch &quot;-L ..&quot; specifies the path to the directory where &quot;v2cc.libs&quot; is stored. You may also specify an absolute path: </p>
<p>&nbsp;<wbr>gvhdl -c -L&nbsp;<wbr>/foo -l lib1 comp1.vhdl </p>
<p> Note that comp1 should reside in a file named &quot;comp1.vhdl&quot;. </p>
<p> If lib2 contains a design comp2 that makes use of comp1 from lib1 then goto &quot;/foo/lib2_dir&quot; and run the following command to create an executable for model comp2: </p>
<p>&nbsp;<wbr>gvhdl -L .. -l lib2 comp2.vhdl ../lib1_dir/comp1.o&nbsp;<wbr></p>
<h2>See Also</h2>
<p><a href="/docs/linux/man/1-gvhdl/">gvhdl</a>(1), <a href="/docs/linux/man/1-freehdl-v2cc/">freehdl-v2cc</a>(1), <a href="/docs/linux/man/1-freehdl-config/">freehdl-config</a>(1)</p>
<h2>Availability</h2>
<p>The latest version of FreeHDL can always be obtained from <code><a rel="nofollow" href="http://www.freehdl.seul.org">www.freehdl.seul.org</a></code></p>
<h2>Reporting Bugs</h2>
<p>Known bugs are documented within the BUGS file. If your report addresses a parser related topic then contact Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt;. If it is related to the code generator or compiler then send an email to Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;. If your are not sure send it to Edwin. He will take care of forwarding your report to the appropriate recipient.</p>
<h2>Copyright</h2>
<p>Edwin Naroska &#169; 1999, 2000, 2001, 2002, 2003, 2004, 2005 &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt; </p>
<p> This is free software; see the source for copying conditions. There is NO warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.</p>
<h2>Authors</h2>
<p>Written by Marius Vollmer &lt;mvo [at] zagadka.ping.de&gt; and Edwin Naroska &lt;edwin [at] ds.e-technik.uni-dortmund.de&gt;.</p>
