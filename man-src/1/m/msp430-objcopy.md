---
title: "msp430-objcopy(1)"
name: "msp430-objcopy"
section: "1"
letter: "m"
url: "/docs/linux/man/1-msp430-objcopy/"
description: "objcopy – copy and translate object files"
---

<h2>NAME</h2>
<p> objcopy &#8211; copy and translate object files</p>
<h2>SYNOPSIS</h2>
<p> objcopy [<code>-F</code> <i>bfdname</i>|<code>&#8211;target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-I</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;input-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-O</code>&nbsp;<wbr><i>bfdname</i>|<code>&#8211;output-target=</code><i>bfdname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-B</code>&nbsp;<wbr><i>bfdarch</i>|<code>&#8211;binary-architecture=</code><i>bfdarch</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-S</code>|<code>&#8211;strip-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-g</code>|<code>&#8211;strip-debug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-K</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;keep-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-N</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;strip-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-unneeded-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-G</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;keep-global-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;localize-hidden</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-L</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;localize-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;globalize-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-W</code>&nbsp;<wbr><i>symbolname</i>|<code>&#8211;weaken-symbol=</code><i>symbolname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-w</code>|<code>&#8211;wildcard</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-x</code>|<code>&#8211;discard-all</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-X</code>|<code>&#8211;discard-locals</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-b</code>&nbsp;<wbr><i>byte</i>|<code>&#8211;byte=</code><i>byte</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-i</code>&nbsp;<wbr><i>interleave</i>|<code>&#8211;interleave=</code><i>interleave</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-j</code>&nbsp;<wbr><i>sectionname</i>|<code>&#8211;only-section=</code><i>sectionname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-R</code>&nbsp;<wbr><i>sectionname</i>|<code>&#8211;remove-section=</code><i>sectionname</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-p</code>|<code>&#8211;preserve-dates</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;debugging</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;gap-fill=</code><i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;pad-to=</code><i>address</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;set-start=</code><i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;adjust-start=</code><i>incr</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-addresses=</code><i>incr</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-address</code>&nbsp;<wbr><i>section</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-lma</code>&nbsp;<wbr><i>section</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-section-vma</code>&nbsp;<wbr><i>section</i>{=,+,-}<i>val</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-warnings</code>]&nbsp;<wbr>[<code>&#8211;no-change-warnings</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;set-section-flags</code>&nbsp;<wbr><i>section</i>=<i>flags</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;add-section</code>&nbsp;<wbr><i>sectionname</i>=<i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;rename-section</code>&nbsp;<wbr><i>oldname</i>=<i>newname</i>[,<i>flags</i>]]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;change-leading-char</code>]&nbsp;<wbr>[<code>&#8211;remove-leading-char</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;reverse-bytes=</code><i>num</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;srec-len=</code><i>ival</i>]&nbsp;<wbr>[<code>&#8211;srec-forceS3</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;redefine-sym</code>&nbsp;<wbr><i>old</i>=<i>new</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;redefine-syms=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;weaken</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;strip-unneeded-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-global-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;localize-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;globalize-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;weaken-symbols=</code><i>filename</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;alt-machine-code=</code><i>index</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-symbols=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-sections=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;prefix-alloc-sections=</code><i>string</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;add-gnu-debuglink=</code><i>path-to-file</i>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;keep-file-symbols</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;only-keep-debug</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;extract-symbol</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;writable-text</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;readonly-text</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;pure</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;impure</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-v</code>|<code>&#8211;verbose</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>-V</code>|<code>&#8211;version</code>]<br />
&nbsp;<wbr>&nbsp;<wbr>[<code>&#8211;help</code>]&nbsp;<wbr>[<code>&#8211;info</code>]<br />
&nbsp;<wbr>&nbsp;<wbr><i>infile</i>&nbsp;<wbr>[<i>outfile</i>]</p>
<h2>DESCRIPTION</h2>
<p> The <font SIZE="-1">GNU</font> <code>objcopy</code> utility copies the contents of an object file to another. <code>objcopy</code> uses the <font SIZE="-1">GNU</font> <font SIZE="-1">BFD</font> Library to read and write the object files. It can write the destination object file in a format different from that of the source object file. The exact behavior of <code>objcopy</code> is controlled by command-line options. Note that <code>objcopy</code> should be able to copy a fully linked file between any two formats. However, copying a relocatable object file between any two formats may not work as expected. </p>
<p> <code>objcopy</code> creates temporary files to do its translations and deletes them afterward. <code>objcopy</code> uses <font SIZE="-1">BFD</font> to do all its translation work; it has access to all the formats described in <font SIZE="-1">BFD</font> and thus is able to recognize most formats without being told explicitly. </p>
<p> <code>objcopy</code> can be used to generate S-records by using an output target of <code>srec</code> (e.g., use <code>-O srec</code>). </p>
<p> <code>objcopy</code> can be used to generate a raw binary file by using an output target of <code>binary</code> (e.g., use <code>-O binary</code>). When <code>objcopy</code> generates a raw binary file, it will essentially produce a memory dump of the contents of the input object file. All symbols and relocation information will be discarded. The memory dump will start at the load address of the lowest section copied into the output file. </p>
<p> When generating an S-record or a raw binary file, it may be helpful to use <code>-S</code> to remove sections containing debugging information. In some cases <code>-R</code> will be useful to remove sections which contain information that is not needed by the binary file. </p>
<p> Note&#8212;<code>objcopy</code> is not able to change the endianness of its input files. If the input format has an endianness (some formats do not), <code>objcopy</code> can only copy the inputs into file formats that have the same endianness or which have no endianness (e.g., <code>srec</code>). (However, see the <code>&#8211;reverse-bytes</code> option.)</p>
<h2>OPTIONS</h2>
<dl>
<dt><i>infile</i></p>
<dd>
<dt><i>outfile</i></p>
<dd> The input and output files, respectively. If you do not specify <i>outfile</i>, <code>objcopy</code> creates a temporary file and destructively renames the result with the name of <i>infile</i>.</p>
<dt><code>-I</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;input-target=</code><i>bfdname</i></p>
<dd> Consider the source file&#8217;s object format to be <i>bfdname</i>, rather than attempting to deduce it.</p>
<dt><code>-O</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;output-target=</code><i>bfdname</i></p>
<dd> Write the output file using the object format <i>bfdname</i>.</p>
<dt><code>-F</code> <i>bfdname</i></p>
<dd>
<dt><code>&#8211;target=</code><i>bfdname</i></p>
<dd> Use <i>bfdname</i> as the object format for both the input and the output file; i.e., simply transfer data from source to destination with no translation.</p>
<dt><code>-B</code> <i>bfdarch</i></p>
<dd>
<dt><code>&#8211;binary-architecture=</code><i>bfdarch</i></p>
<dd> Useful when transforming a raw binary input file into an object file. In this case the output architecture can be set to <i>bfdarch</i>. This option will be ignored if the input file has a known <i>bfdarch</i>. You can access this binary data inside a program by referencing the special symbols that are created by the conversion process. These symbols are called _binary_<i>objfile</i>_start, _binary_<i>objfile</i>_end and _binary_<i>objfile</i>_size. e.g. you can transform a picture file into an object file and then access it in your code using these symbols.</p>
<dt><code>-j</code> <i>sectionname</i></p>
<dd>
<dt><code>&#8211;only-section=</code><i>sectionname</i></p>
<dd> Copy only the named section from the input file to the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable.</p>
<dt><code>-R</code> <i>sectionname</i></p>
<dd>
<dt><code>&#8211;remove-section=</code><i>sectionname</i></p>
<dd> Remove any section named <i>sectionname</i> from the output file. This option may be given more than once. Note that using this option inappropriately may make the output file unusable.</p>
<dt><code>-S</code></p>
<dd>
<dt><code>&#8211;strip-all</code></p>
<dd> Do not copy relocation and symbol information from the source file.</p>
<dt><code>-g</code></p>
<dd>
<dt><code>&#8211;strip-debug</code></p>
<dd> Do not copy debugging symbols or sections from the source file.</p>
<dt><code>&#8211;strip-unneeded</code></p>
<dd> Strip all symbols that are not needed for relocation processing.</p>
<dt><code>-K</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;keep-symbol=</code><i>symbolname</i></p>
<dd> When stripping symbols, keep symbol <i>symbolname</i> even if it would normally be stripped. This option may be given more than once.</p>
<dt><code>-N</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;strip-symbol=</code><i>symbolname</i></p>
<dd> Do not copy symbol <i>symbolname</i> from the source file. This option may be given more than once.</p>
<dt><code>&#8211;strip-unneeded-symbol=</code><i>symbolname</i></p>
<dd> Do not copy symbol <i>symbolname</i> from the source file unless it is needed by a relocation. This option may be given more than once.</p>
<dt><code>-G</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;keep-global-symbol=</code><i>symbolname</i></p>
<dd> Keep only symbol <i>symbolname</i> global. Make all other symbols local to the file, so that they are not visible externally. This option may be given more than once.</p>
<dt><code>&#8211;localize-hidden</code></p>
<dd> In an <font SIZE="-1">ELF</font> object, mark all symbols that have hidden or internal visibility as local. This option applies on top of symbol-specific localization options such as <code>-L</code>.</p>
<dt><code>-L</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;localize-symbol=</code><i>symbolname</i></p>
<dd> Make symbol <i>symbolname</i> local to the file, so that it is not visible externally. This option may be given more than once.</p>
<dt><code>-W</code> <i>symbolname</i></p>
<dd>
<dt><code>&#8211;weaken-symbol=</code><i>symbolname</i></p>
<dd> Make symbol <i>symbolname</i> weak. This option may be given more than once.</p>
<dt><code>&#8211;globalize-symbol=</code><i>symbolname</i></p>
<dd> Give symbol <i>symbolname</i> global scoping so that it is visible outside of the file in which it is defined. This option may be given more than once.</p>
<dt><code>-w</code></p>
<dd>
<dt><code>&#8211;wildcard</code></p>
<dd> Permit regular expressions in <i>symbolname</i>s used in other command line options. The question mark (?), asterisk (*), backslash (\) and square brackets ([]) operators can be used anywhere in the symbol name. If the first character of the symbol name is the exclamation point (!) then the sense of the switch is reversed for that symbol. For example: </p>
<pre>
          -w -W !foo -W fo*
</pre>
<p> would cause objcopy to weaken all symbols that start with &#8220;fo&#8221; except for the symbol &#8220;foo&#8221;.</p>
<dt><code>-x</code></p>
<dd>
<dt><code>&#8211;discard-all</code></p>
<dd> Do not copy non-global symbols from the source file.</p>
<dt><code>-X</code></p>
<dd>
<dt><code>&#8211;discard-locals</code></p>
<dd> Do not copy compiler-generated local symbols. (These usually start with <code>L</code> or <code>.</code>.)</p>
<dt><code>-b</code> <i>byte</i></p>
<dd>
<dt><code>&#8211;byte=</code><i>byte</i></p>
<dd> Keep only every <i>byte</i>th byte of the input file (header data is not affected). <i>byte</i> can be in the range from 0 to <i>interleave</i>-1, where <i>interleave</i> is given by the <code>-i</code> or <code>&#8211;interleave</code> option, or the default of 4. This option is useful for creating files to program <font SIZE="-1">ROM</font>. It is typically used with an <tt>&quot;srec&quot;</tt> output target.</p>
<dt><code>-i</code> <i>interleave</i></p>
<dd>
<dt><code>&#8211;interleave=</code><i>interleave</i></p>
<dd> Only copy one out of every <i>interleave</i> bytes. Select which byte to copy with the <code>-b</code> or <code>&#8211;byte</code> option. The default is 4. <code>objcopy</code> ignores this option if you do not specify either <code>-b</code> or <code>&#8211;byte</code>.</p>
<dt><code>-p</code></p>
<dd>
<dt><code>&#8211;preserve-dates</code></p>
<dd> Set the access and modification dates of the output file to be the same as those of the input file.</p>
<dt><code>&#8211;debugging</code></p>
<dd> Convert debugging information, if possible. This is not the default because only certain debugging formats are supported, and the conversion process can be time consuming.</p>
<dt><code>&#8211;gap-fill</code> <i>val</i></p>
<dd> Fill gaps between sections with <i>val</i>. This operation applies to the <i>load address</i> (<font SIZE="-1">LMA</font>) of the sections. It is done by increasing the size of the section with the lower address, and filling in the extra space created with <i>val</i>.</p>
<dt><code>&#8211;pad-to</code> <i>address</i></p>
<dd> Pad the output file up to the load address <i>address</i>. This is done by increasing the size of the last section. The extra space is filled in with the value specified by <code>&#8211;gap-fill</code> (default zero).</p>
<dt><code>&#8211;set-start</code> <i>val</i></p>
<dd> Set the start address of the new file to <i>val</i>. Not all object file formats support setting the start address.</p>
<dt><code>&#8211;change-start</code> <i>incr</i></p>
<dd>
<dt><code>&#8211;adjust-start</code> <i>incr</i></p>
<dd> Change the start address by adding <i>incr</i>. Not all object file formats support setting the start address.</p>
<dt><code>&#8211;change-addresses</code> <i>incr</i></p>
<dd>
<dt><code>&#8211;adjust-vma</code> <i>incr</i></p>
<dd> Change the <font SIZE="-1">VMA</font> and <font SIZE="-1">LMA</font> addresses of all sections, as well as the start address, by adding <i>incr</i>. Some object file formats do not permit section addresses to be changed arbitrarily. Note that this does not relocate the sections; if the program expects sections to be loaded at a certain address, and this option is used to change the sections such that they are loaded at a different address, the program may fail.</p>
<dt><code>&#8211;change-section-address</code> <i>section</i><code>{=,+,-}</code><i>val</i></p>
<dd>
<dt><code>&#8211;adjust-section-vma</code> <i>section</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change both the <font SIZE="-1">VMA</font> address and the <font SIZE="-1">LMA</font> address of the named <i>section</i>. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>section</i> does not exist in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-section-lma</code> <i>section</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change the <font SIZE="-1">LMA</font> address of the named <i>section</i>. The <font SIZE="-1">LMA</font> address is the address where the section will be loaded into memory at program load time. Normally this is the same as the <font SIZE="-1">VMA</font> address, which is the address of the section at program run time, but on some systems, especially those where a program is held in <font SIZE="-1">ROM</font>, the two can be different. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>section</i> does not exist in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-section-vma</code> <i>section</i><code>{=,+,-}</code><i>val</i></p>
<dd> Set or change the <font SIZE="-1">VMA</font> address of the named <i>section</i>. The <font SIZE="-1">VMA</font> address is the address where the section will be located once the program has started executing. Normally this is the same as the <font SIZE="-1">LMA</font> address, which is the address where the section will be loaded into memory, but on some systems, especially those where a program is held in <font SIZE="-1">ROM</font>, the two can be different. If <code>=</code> is used, the section address is set to <i>val</i>. Otherwise, <i>val</i> is added to or subtracted from the section address. See the comments under <code>&#8211;change-addresses</code>, above. If <i>section</i> does not exist in the input file, a warning will be issued, unless <code>&#8211;no-change-warnings</code> is used.</p>
<dt><code>&#8211;change-warnings</code></p>
<dd>
<dt><code>&#8211;adjust-warnings</code></p>
<dd> If <code>&#8211;change-section-address</code> or <code>&#8211;change-section-lma</code> or <code>&#8211;change-section-vma</code> is used, and the named section does not exist, issue a warning. This is the default.</p>
<dt><code>&#8211;no-change-warnings</code></p>
<dd>
<dt><code>&#8211;no-adjust-warnings</code></p>
<dd> Do not issue a warning if <code>&#8211;change-section-address</code> or <code>&#8211;adjust-section-lma</code> or <code>&#8211;adjust-section-vma</code> is used, even if the named section does not exist.</p>
<dt><code>&#8211;set-section-flags</code> <i>section</i><code>=</code><i>flags</i></p>
<dd> Set the flags for the named section. The <i>flags</i> argument is a comma separated string of flag names. The recognized names are <code>alloc</code>, <code>contents</code>, <code>load</code>, <code>noload</code>, <code>readonly</code>, <code>code</code>, <code>data</code>, <code>rom</code>, <code>share</code>, and <code>debug</code>. You can set the <code>contents</code> flag for a section which does not have contents, but it is not meaningful to clear the <code>contents</code> flag of a section which does have contents&#8212;just remove the section instead. Not all flags are meaningful for all object file formats.</p>
<dt><code>&#8211;add-section</code> <i>sectionname</i><code>=</code><i>filename</i></p>
<dd> Add a new section named <i>sectionname</i> while copying the file. The contents of the new section are taken from the file <i>filename</i>. The size of the section will be the size of the file. This option only works on file formats which can support sections with arbitrary names.</p>
<dt><code>&#8211;rename-section</code> <i>oldname</i><code>=</code><i>newname</i><code>[,</code><i>flags</i><code>]</code></p>
<dd> Rename a section from <i>oldname</i> to <i>newname</i>, optionally changing the section&#8217;s flags to <i>flags</i> in the process. This has the advantage over usng a linker script to perform the rename in that the output stays as an object file and does not become a linked executable. </p>
<p> This option is particularly helpful when the input format is binary, since this will always create a section called .data. If for example, you wanted instead to create a section called .rodata containing binary data you could use the following command line to achieve it: </p>
<pre>
          objcopy -I binary -O &lt;output_format&gt; -B &lt;architecture&gt; \
           --rename-section .data=.rodata,alloc,load,readonly,data,contents \
           &lt;input_binary_file&gt; &lt;output_object_file&gt;
</pre>
<dt><code>&#8211;change-leading-char</code></p>
<dd> Some object file formats use special characters at the start of symbols. The most common such character is underscore, which compilers often add before every symbol. This option tells <code>objcopy</code> to change the leading character of every symbol when it converts between object file formats. If the object file formats use the same leading character, this option has no effect. Otherwise, it will add a character, or remove a character, or change a character, as appropriate.</p>
<dt><code>&#8211;remove-leading-char</code></p>
<dd> If the first character of a global symbol is a special symbol leading character used by the object file format, remove the character. The most common symbol leading character is underscore. This option will remove a leading underscore from all global symbols. This can be useful if you want to link together objects of different file formats with different conventions for symbol names. This is different from <code>&#8211;change-leading-char</code> because it always changes the symbol name when appropriate, regardless of the object file format of the output file.</p>
<dt><code>&#8211;reverse-bytes=</code><i>num</i></p>
<dd> Reverse the bytes in a section with output contents. A section length must be evenly divisible by the value given in order for the swap to be able to take place. Reversing takes place before the interleaving is performed. </p>
<p> This option is used typically in generating <font SIZE="-1">ROM</font> images for problematic target systems. For example, on some target boards, the 32-bit words fetched from 8-bit ROMs are re-assembled in little-endian byte order regardless of the <font SIZE="-1">CPU</font> byte order. Depending on the programming model, the endianness of the <font SIZE="-1">ROM</font> may need to be modified. </p>
<p> Consider a simple file with a section containing the following eight bytes: <tt>12345678</tt>. </p>
<p> Using <code>&#8211;reverse-bytes=2</code> for the above example, the bytes in the output file would be ordered <tt>21436587</tt>. </p>
<p> Using <code>&#8211;reverse-bytes=4</code> for the above example, the bytes in the output file would be ordered <tt>43218765</tt>. </p>
<p> By using <code>&#8211;reverse-bytes=2</code> for the above example, followed by <code>&#8211;reverse-bytes=4</code> on the output file, the bytes in the second output file would be ordered <tt>34127856</tt>.</p>
<dt><code>&#8211;srec-len=</code><i>ival</i></p>
<dd> Meaningful only for srec output. Set the maximum length of the Srecords being produced to <i>ival</i>. This length covers both address, data and crc fields.</p>
<dt><code>&#8211;srec-forceS3</code></p>
<dd> Meaningful only for srec output. Avoid generation of S1/S2 records, creating S3-only record format.</p>
<dt><code>&#8211;redefine-sym</code> <i>old</i><code>=</code><i>new</i></p>
<dd> Change the name of a symbol <i>old</i>, to <i>new</i>. This can be useful when one is trying link two things together for which you have no source, and there are name collisions.</p>
<dt><code>&#8211;redefine-syms=</code><i>filename</i></p>
<dd> Apply <code>&#8211;redefine-sym</code> to each symbol pair &quot;<i>old</i> <i>new</i>&quot; listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol pair per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;weaken</code></p>
<dd> Change all global symbols in the file to be weak. This can be useful when building an object which will be linked against other objects using the <code>-R</code> option to the linker. This option is only effective when using an object file format which supports weak symbols.</p>
<dt><code>&#8211;keep-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;keep-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;strip-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;strip-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;strip-unneeded-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;strip-unneeded-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;keep-global-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;keep-global-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;localize-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;localize-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;globalize-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;globalize-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;weaken-symbols=</code><i>filename</i></p>
<dd> Apply <code>&#8211;weaken-symbol</code> option to each symbol listed in the file <i>filename</i>. <i>filename</i> is simply a flat file, with one symbol name per line. Line comments may be introduced by the hash character. This option may be given more than once.</p>
<dt><code>&#8211;alt-machine-code=</code><i>index</i></p>
<dd> If the output architecture has alternate machine codes, use the <i>index</i>th code instead of the default one. This is useful in case a machine is assigned an official code and the tool-chain adopts the new code, but other applications still depend on the original code being used. For <font SIZE="-1">ELF</font> based architectures if the <i>index</i> alternative does not exist then the value is treated as an absolute number to be stored in the e_machine field of the <font SIZE="-1">ELF</font> header.</p>
<dt><code>&#8211;writable-text</code></p>
<dd> Mark the output text as writable. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;readonly-text</code></p>
<dd> Make the output text write protected. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;pure</code></p>
<dd> Mark the output file as demand paged. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;impure</code></p>
<dd> Mark the output file as impure. This option isn&#8217;t meaningful for all object file formats.</p>
<dt><code>&#8211;prefix-symbols=</code><i>string</i></p>
<dd> Prefix all symbols in the output file with <i>string</i>.</p>
<dt><code>&#8211;prefix-sections=</code><i>string</i></p>
<dd> Prefix all section names in the output file with <i>string</i>.</p>
<dt><code>&#8211;prefix-alloc-sections=</code><i>string</i></p>
<dd> Prefix all the names of all allocated sections in the output file with <i>string</i>.</p>
<dt><code>&#8211;add-gnu-debuglink=</code><i>path-to-file</i></p>
<dd> Creates a .gnu_debuglink section which contains a reference to <i>path-to-file</i> and adds it to the output file.</p>
<dt><code>&#8211;keep-file-symbols</code></p>
<dd> When stripping a file, perhaps with <code>&#8211;strip-debug</code> or <code>&#8211;strip-unneeded</code>, retain any symbols specifying source file names, which would otherwise get stripped.</p>
<dt><code>&#8211;only-keep-debug</code></p>
<dd> Strip a file, removing contents of any sections that would not be stripped by <code>&#8211;strip-debug</code> and leaving the debugging sections intact. In <font SIZE="-1">ELF</font> files, this preserves all note sections in the output. </p>
<p> The intention is that this option will be used in conjunction with <code>&#8211;add-gnu-debuglink</code> to create a two part executable. One a stripped binary which will occupy less space in <font SIZE="-1">RAM</font> and in a distribution and the second a debugging information file which is only needed if debugging abilities are required. The suggested procedure to create these files is as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>1.&lt;Link the executable as normal. Assuming that is is called&gt;</p>
<dd> <tt>&quot;foo&quot;</tt> then&#8230;</p>
<dt>1.&lt;Run objcopy &#8211;only-keep-debug foo foo.dbg to&gt;</p>
<dd> create a file containing the debugging info.</p>
<dt>1.&lt;Run objcopy &#8211;strip-debug foo to create a&gt;</p>
<dd> stripped executable.</p>
<dt>1.&lt;Run objcopy &#8211;add-gnu-debuglink=foo.dbg foo&gt;</p>
<dd> to add a link to the debugging info into the stripped executable.</dl>
</dl>
<dl>
<dt>
<dd>
<p> Note&#8212;the choice of <tt>&quot;.dbg&quot;</tt> as an extension for the debug info file is arbitrary. Also the <tt>&quot;--only-keep-debug&quot;</tt> step is optional. You could instead do this:</p>
<dl>
<dt>1.&lt;Link the executable as normal.&gt;</p>
<dd>
<dt>1.&lt;Copy foo to <tt>foo.full&gt;</p>
<dd>
<dt>1.&lt;Run objcopy --strip-debug foo&gt;</p>
<dd>
<dt>1.&lt;Run objcopy --add-gnu-debuglink=foo.full foo&gt;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> i.e., the file pointed to by the </tt><code>&#8211;add-gnu-debuglink</code> can be the full executable. It does not have to be a file created by the <code>&#8211;only-keep-debug</code> switch. </p>
<p> Note&#8212;this switch is only intended for use on fully linked files. It does not make sense to use it on object files where the debugging information may be incomplete. Besides the gnu_debuglink feature currently only supports the presence of one filename containing debugging information, not multiple filenames on a one-per-object-file basis.</dl>
<dt><code>&#8211;extract-symbol</code></p>
<dd> Keep the file&#8217;s section flags and symbols but remove all section data. Specifically, the option:</p>
<dl>
<dt>
<dd>
<dl>
<dt>*&lt;removes the contents of all sections;&gt;</p>
<dd>
<dt>*&lt;sets the size of every section to zero; and&gt;</p>
<dd>
<dt>*&lt;sets the file&#8217;s start address to zero.&gt;</p>
<dd></dl>
</dl>
<dl>
<dt>
<dd>
<p> This option is used to build a <i>.sym</i> file for a VxWorks kernel. It can also be a useful way of reducing the size of a <code>&#8211;just-symbols</code> linker input file.</dl>
<dt><code>-V</code></p>
<dd>
<dt><code>&#8211;version</code></p>
<dd> Show the version number of <code>objcopy</code>.</p>
<dt><code>-v</code></p>
<dd>
<dt><code>&#8211;verbose</code></p>
<dd> Verbose output: list all object files modified. In the case of archives, <code>objcopy -V</code> lists all members of the archive.</p>
<dt><code>&#8211;help</code></p>
<dd> Show a summary of the options to <code>objcopy</code>.</p>
<dt><code>&#8211;info</code></p>
<dd> Display a list showing all architectures and object formats available.</p>
<dt><code>@</code><i>file</i></p>
<dd> Read command-line options from <i>file</i>. The options read are inserted in place of the original @<i>file</i> option. If <i>file</i> does not exist, or cannot be read, then the option will be treated literally, and not removed. </p>
<p> Options in <i>file</i> are separated by whitespace. A whitespace character may be included in an option by surrounding the entire option in either single or double quotes. Any character (including a backslash) may be included by prefixing the character to be included with a backslash. The <i>file</i> may itself contain additional @<i>file</i> options; any such options will be processed recursively.</dl>
<h2>SEE ALSO</h2>
<p> <i><a href="/docs/linux/man/1-ld/">ld</a></i>(1), <i><a href="/docs/linux/man/1-objdump/">objdump</a></i>(1), and the Info entries for <i>binutils</i>.</p>
<h2>COPYRIGHT</h2>
<p> Copyright (c) 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008 Free Software Foundation, Inc. </p>
<p> Permission is granted to copy, distribute and/or modify this document under the terms of the <font SIZE="-1">GNU</font> Free Documentation License, Version 1.2 or any later version published by the Free Software Foundation; with no Invariant Sections, with no Front-Cover Texts, and with no Back-Cover Texts. A copy of the license is included in the section entitled &#8220;<font SIZE="-1">GNU</font> Free Documentation License&#8221;. </p>
<h2>Index</h2>
