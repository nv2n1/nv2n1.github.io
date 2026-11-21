---
title: "elf(5)"
name: "elf"
section: "5"
letter: "e"
url: "/docs/linux/man/5-elf/"
description: "elf – format of Executable and Linking Format (ELF) files"
---

<p>elf &#8211; format of Executable and Linking Format (ELF) files</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;elf.h&gt;</code></pre>
<h2>Description</h2>
<p>The header file <i>&lt;elf.h&gt;</i> defines the format of ELF executable binary files. Amongst these files are normal executable files, relocatable object files, core files, and shared objects. An executable file using the ELF file format consists of an ELF header, followed by a program header table or a section header table, or both. The ELF header is always at offset zero of the file. The program header table and the section header table&#8217;s offset in the file are defined in the ELF header. The two tables describe the rest of the particularities of the file. This header file describes the above mentioned headers as C structures and also includes structures for dynamic sections, relocation sections and symbol tables.</p>
<h3>Basic types</h3>
<p>The following types are used for N-bit architectures (N=32,64, <i>ElfN</i> stands for <i>Elf32</i> or <i>Elf64</i>, <i>uintN_t</i> stands for <i>uint32_t</i> or <i>uint64_t</i>): ElfN_Addr Unsigned program address, uintN_t ElfN_Off Unsigned file offset, uintN_t ElfN_Section Unsigned section index, uint16_t ElfN_Versym Unsigned version symbol information, uint16_t Elf_Byte unsigned char ElfN_Half uint16_t ElfN_Sword int32_t ElfN_Word uint32_t ElfN_Sxword int64_t ElfN_Xword uint64_t (Note: the *BSD terminology is a bit different. There, <i>Elf64_Half</i> is twice as large as <i>Elf32_Half</i>, and <i>Elf64Quarter</i> is used for <i>uint16_t</i>. In order to avoid confusion these types are replaced by explicit ones in the below.) All data structures that the file format defines follow the &quot;natural&quot; size and alignment guidelines for the relevant class. If necessary, data structures contain explicit padding to ensure 4-byte alignment for 4-byte objects, to force structure sizes to a multiple of 4, and so on.</p>
<h3>ELF header (Ehdr)</h3>
<p>The ELF header is described by the type <i>Elf32_Ehdr</i> or <i>Elf64_Ehdr</i>: desc = note-&gt;n_descsz == 0 ? NULL :<br />
memory + sizeof(*note) + ALIGN_UP(note-&gt;n_namesz, 4);<br />
/* The next note follows both (with alignment) */<br />
next_note = memory + sizeof(*note) +<br />
ALIGN_UP(note-&gt;n_namesz, 4) +<br />
ALIGN_UP(note-&gt;n_descsz, 4); typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char e_ident[EI_NIDENT];<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_machine;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_version;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfN_Addr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_entry;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfN_Off&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_phoff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ElfN_Off&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_shoff;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_ehsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_phentsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_phnum;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_shentsize;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_shnum;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;e_shstrndx; } ElfN_Ehdr; The fields have the following meanings:</p>
<dl>
<dt><i>e_ident</i></dt>
<dd>This array of bytes specifies how to interpret the file, independent of the processor or the file&#8217;s remaining contents. Within this array everything is named by macros, which start with the prefix <code>EI_</code> and may contain values which start with the prefix <code>ELF</code>. The following macros are defined:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>EI_MAG0</code></dt>
<dd>The first byte of the magic number. It must be filled with <code>ELFMAG0</code>. (0: 0x7f)</dd>
<dt><code>EI_MAG1</code></dt>
<dd>The second byte of the magic number. It must be filled with <code>ELFMAG1</code>. (1: &#8216;E&#8217;)</dd>
<dt><code>EI_MAG2</code></dt>
<dd>The third byte of the magic number. It must be filled with <code>ELFMAG2</code>. (2: &#8216;L&#8217;)</dd>
<dt><code>EI_MAG3</code></dt>
<dd>The fourth byte of the magic number. It must be filled with <code>ELFMAG3</code>. (3: &#8216;F&#8217;)</dd>
<dt><code>EI_CLASS</code></dt>
<dd>The fifth byte identifies the architecture for this binary:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ELFCLASSNONE</code></dt>
<dd>This class is invalid.</dd>
<dt><code>ELFCLASS32</code></dt>
<dd>This defines the 32-bit architecture. It supports machines with files and virtual address spaces up to 4 Gigabytes.</dd>
<dt><code>ELFCLASS64</code></dt>
<dd>This defines the 64-bit architecture.</dd></dl>
</dl>
<dt><code>EI_DATA</code></dt>
<dd>The sixth byte specifies the data encoding of the processor-specific data in the file. Currently, these encodings are supported:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ELFDATANONE</code></dt>
<dd>Unknown data format.</dd>
<dt><code>ELFDATA2LSB</code></dt>
<dd>Two&#8217;s complement, little-endian.</dd>
<dt><code>ELFDATA2MSB</code></dt>
<dd>Two&#8217;s complement, big-endian.</dd></dl>
</dl>
<dt><code>EI_VERSION</code></dt>
<dd>The seventh byte is the version number of the ELF specification:</dd>
<dd>
</dd><dl>
<dd>
</dd><dl>
<dt><code>EV_NONE</code></dt>
<dd>Invalid version.</dd>
<dt><code>EV_CURRENT</code></dt>
<dd>Current version.</dd></dl>
</dl>
<dt><code>EI_OSABI</code></dt>
<dd>The eighth byte identifies the operating system and ABI to which the object is targeted. Some fields in other ELF structures have flags and values that have platform-specific meanings; the interpretation of those fields is determined by the value of this byte. For example:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ELFOSABI_NONE</code></dt>
<dd>Same as ELFOSABI_SYSV</dd>
<dt><code>ELFOSABI_SYSV</code></dt>
<dd>UNIX System V ABI</dd>
<dt><code>ELFOSABI_HPUX</code></dt>
<dd>HP-UX ABI</dd>
<dt><code>ELFOSABI_NETBSD</code></dt>
<dd>NetBSD ABI</dd>
<dt><code>ELFOSABI_LINUX</code></dt>
<dd>Linux ABI</dd>
<dt><code>ELFOSABI_SOLARIS</code></dt>
<dd>Solaris ABI</dd>
<dt><code>ELFOSABI_IRIX</code></dt>
<dd>IRIX ABI</dd>
<dt><code>ELFOSABI_FREEBSD</code></dt>
<dd>FreeBSD ABI</dd>
<dt><code>ELFOSABI_TRU64</code></dt>
<dd>TRU64 UNIX ABI</dd>
<dt><code>ELFOSABI_ARM</code></dt>
<dd>ARM architecture ABI</dd>
<dt><code>ELFOSABI_STANDALONE</code></dt>
<dd>Stand-alone (embedded) ABI</dd></dl>
</dl>
<dt><code>EI_ABIVERSION</code></dt>
<dd>The ninth byte identifies the version of the ABI to which the object is targeted. This field is used to distinguish among incompatible versions of an ABI. The interpretation of this version number is dependent on the ABI identified by the <code>EI_OSABI</code> field. Applications conforming to this specification use the value 0.</dd>
<dt><code>EI_PAD</code></dt>
<dd>Start of padding. These bytes are reserved and set to zero. Programs which read them should ignore them. The value for <code>EI_PAD</code> will change in the future if currently unused bytes are given meanings.</dd>
<dt><code>EI_NIDENT</code></dt>
<dd>The size of the <i>e_ident</i> array.</dd></dl>
</dl>
<dt><i>e_type</i></dt>
<dd>This member of the structure identifies the object file type:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>ET_NONE</code></dt>
<dd>An unknown type.</dd>
<dt><code>ET_REL</code></dt>
<dd>A relocatable file.</dd>
<dt><code>ET_EXEC</code></dt>
<dd>An executable file.</dd>
<dt><code>ET_DYN</code></dt>
<dd>A shared object.</dd>
<dt><code>ET_CORE</code></dt>
<dd>A core file.</dd></dl>
</dl>
<dt><i>e_machine</i></dt>
<dd>This member specifies the required architecture for an individual file. For example:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>EM_NONE</code></dt>
<dd>An unknown machine</dd>
<dt><code>EM_M32</code></dt>
<dd>AT&amp;T WE 32100</dd>
<dt><code>EM_SPARC</code></dt>
<dd>Sun Microsystems SPARC</dd>
<dt><code>EM_386</code></dt>
<dd>Intel 80386</dd>
<dt><code>EM_68K</code></dt>
<dd>Motorola 68000</dd>
<dt><code>EM_88K</code></dt>
<dd>Motorola 88000</dd>
<dt><code>EM_860</code></dt>
<dd>Intel 80860</dd>
<dt><code>EM_MIPS</code></dt>
<dd>MIPS RS3000 (big-endian only)</dd>
<dt><code>EM_PARISC</code></dt>
<dd>HP/PA</dd>
<dt><code>EM_SPARC32PLUS</code></dt>
<dd>SPARC with enhanced instruction set</dd>
<dt><code>EM_PPC</code></dt>
<dd>PowerPC</dd>
<dt><code>EM_PPC64</code></dt>
<dd>PowerPC 64-bit</dd>
<dt><code>EM_S390</code></dt>
<dd>IBM S/390</dd>
<dt><code>EM_ARM</code></dt>
<dd>Advanced RISC Machines</dd>
<dt><code>EM_SH</code></dt>
<dd>Renesas SuperH</dd>
<dt><code>EM_SPARCV9</code></dt>
<dd>SPARC v9 64-bit</dd>
<dt><code>EM_IA_64</code></dt>
<dd>Intel Itanium</dd>
<dt><code>EM_X86_64</code></dt>
<dd>AMD x86-64</dd>
<dt><code>EM_VAX</code></dt>
<dd>DEC Vax</dd></dl>
</dl>
<dt><i>e_version</i></dt>
<dd>This member identifies the file version:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>EV_NONE</code></dt>
<dd>Invalid version</dd>
<dt><code>EV_CURRENT</code></dt>
<dd>Current version</dd></dl>
</dl>
<dt><i>e_entry</i></dt>
<dd>This member gives the virtual address to which the system first transfers control, thus starting the process. If the file has no associated entry point, this member holds zero.</dd>
<dt><i>e_phoff</i></dt>
<dd>This member holds the program header table&#8217;s file offset in bytes. If the file has no program header table, this member holds zero.</dd>
<dt><i>e_shoff</i></dt>
<dd>This member holds the section header table&#8217;s file offset in bytes. If the file has no section header table, this member holds zero.</dd>
<dt><i>e_flags</i></dt>
<dd>This member holds processor-specific flags associated with the file. Flag names take the form EF_`machine_flag&#8217;. Currently, no flags have been defined.</dd>
<dt><i>e_ehsize</i></dt>
<dd>This member holds the ELF header&#8217;s size in bytes.</dd>
<dt><i>e_phentsize</i></dt>
<dd>This member holds the size in bytes of one entry in the file&#8217;s program header table; all entries are the same size.</dd>
<dt><i>e_phnum</i></dt>
<dd>This member holds the number of entries in the program header table. Thus the product of <i>e_phentsize</i> and <i>e_phnum</i> gives the table&#8217;s size in bytes. If a file has no program header, <i>e_phnum</i> holds the value zero.</dd>
<dd>If the number of entries in the program header table is larger than or equal to <code>PN_XNUM</code> (0xffff), this member holds <code>PN_XNUM</code> (0xffff) and the real number of entries in the program header table is held in the <i>sh_info</i> member of the initial entry in section header table. Otherwise, the <i>sh_info</i> member of the initial entry contains the value zero.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>PN_XNUM</code></dt>
<dd>This is defined as 0xffff, the largest number <i>e_phnum</i> can have, specifying where the actual number of program headers is assigned.</dd></dl>
</dl>
<dt><i>e_shentsize</i></dt>
<dd>This member holds a sections header&#8217;s size in bytes. A section header is one entry in the section header table; all entries are the same size.</dd>
<dt><i>e_shnum</i></dt>
<dd>This member holds the number of entries in the section header table. Thus the product of <i>e_shentsize</i> and <i>e_shnum</i> gives the section header table&#8217;s size in bytes. If a file has no section header table, <i>e_shnum</i> holds the value of zero.</dd>
<dd>If the number of entries in the section header table is larger than or equal to <code>SHN_LORESERVE</code> (0xff00), <i>e_shnum</i> holds the value zero and the real number of entries in the section header table is held in the <i>sh_size</i> member of the initial entry in section header table. Otherwise, the <i>sh_size</i> member of the initial entry in the section header table holds the value zero.</dd>
<dt><i>e_shstrndx</i></dt>
<dd>This member holds the section header table index of the entry associated with the section name string table. If the file has no section name string table, this member holds the value <code>SHN_UNDEF</code>.</dd>
<dd>If the index of section name string table section is larger than or equal to <code>SHN_LORESERVE</code> (0xff00), this member holds <code>SHN_XINDEX</code> (0xffff) and the real index of the section name string table section is held in the <i>sh_link</i> member of the initial entry in section header table. Otherwise, the <i>sh_link</i> member of the initial entry in section header table contains the value zero.</dd></dl>
<h3>Program header (Phdr)</h3>
<p>An executable or shared object file&#8217;s program header table is an array of structures, each describing a segment or other information the system needs to prepare the program for execution. An object file <i>segment</i> contains one or more <i>sections</i>. Program headers are meaningful only for executable and shared object files. A file specifies its own program header size with the ELF header&#8217;s <i>e_phentsize</i> and <i>e_phnum</i> members. The ELF program header is described by the type <i>Elf32_Phdr</i> or <i>Elf64_Phdr</i> depending on the architecture: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Off&nbsp;<wbr>&nbsp;p_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr p_vaddr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr p_paddr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_filesz;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_memsz;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_align; } Elf32_Phdr; typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Off&nbsp;<wbr>&nbsp;p_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr p_vaddr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr p_paddr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_filesz;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_memsz;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;p_align; } Elf64_Phdr; The main difference between the 32-bit and the 64-bit program header lies in the location of the <i>p_flags</i> member in the total struct.</p>
<dl>
<dt><i>p_type</i></dt>
<dd>This member of the structure indicates what kind of segment this array element describes or how to interpret the array element&#8217;s information.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>PT_NULL</code></dt>
<dd>The array element is unused and the other members&#8217; values are undefined. This lets the program header have ignored entries.</dd>
<dt><code>PT_LOAD</code></dt>
<dd>The array element specifies a loadable segment, described by <i>p_filesz</i> and <i>p_memsz</i>. The bytes from the file are mapped to the beginning of the memory segment. If the segment&#8217;s memory size <i>p_memsz</i> is larger than the file size <i>p_filesz</i>, the &quot;extra&quot; bytes are defined to hold the value 0 and to follow the segment&#8217;s initialized area. The file size may not be larger than the memory size. Loadable segment entries in the program header table appear in ascending order, sorted on the <i>p_vaddr</i> member.</dd>
<dt><code>PT_DYNAMIC</code></dt>
<dd>The array element specifies dynamic linking information.</dd>
<dt><code>PT_INTERP</code></dt>
<dd>The array element specifies the location and size of a null-terminated pathname to invoke as an interpreter. This segment type is meaningful only for executable files (though it may occur for shared objects). However it may not occur more than once in a file. If it is present, it must precede any loadable segment entry.</dd>
<dt><code>PT_NOTE</code></dt>
<dd>The array element specifies the location of notes (ElfN_Nhdr).</dd>
<dt><code>PT_SHLIB</code></dt>
<dd>This segment type is reserved but has unspecified semantics. Programs that contain an array element of this type do not conform to the ABI.</dd>
<dt><code>PT_PHDR</code></dt>
<dd>The array element, if present, specifies the location and size of the program header table itself, both in the file and in the memory image of the program. This segment type may not occur more than once in a file. Moreover, it may occur only if the program header table is part of the memory image of the program. If it is present, it must precede any loadable segment entry.</dd>
<dt><code>PT_LOPROC</code>, <code>PT_HIPROC</code></dt>
<dd>Values in the inclusive range [<code>PT_LOPROC</code>, <code>PT_HIPROC</code>] are reserved for processor-specific semantics.</dd>
<dt><code>PT_GNU_STACK</code></dt>
<dd>GNU extension which is used by the Linux kernel to control the state of the stack via the flags set in the <i>p_flags</i> member.</dd></dl>
</dl>
<dt><i>p_offset</i></dt>
<dd>This member holds the offset from the beginning of the file at which the first byte of the segment resides.</dd>
<dt><i>p_vaddr</i></dt>
<dd>This member holds the virtual address at which the first byte of the segment resides in memory.</dd>
<dt><i>p_paddr</i></dt>
<dd>On systems for which physical addressing is relevant, this member is reserved for the segment&#8217;s physical address. Under BSD this member is not used and must be zero.</dd>
<dt><i>p_filesz</i></dt>
<dd>This member holds the number of bytes in the file image of the segment. It may be zero.</dd>
<dt><i>p_memsz</i></dt>
<dd>This member holds the number of bytes in the memory image of the segment. It may be zero.</dd>
<dt><i>p_flags</i></dt>
<dd>This member holds a bit mask of flags relevant to the segment:</dd>
<dl>
<dd>
</dd><dl>
<dt><code>PF_X</code></dt>
<dd>An executable segment.</dd>
<dt><code>PF_W</code></dt>
<dd>A writable segment.</dd>
<dt><code>PF_R</code></dt>
<dd>A readable segment.</dd></dl>
</dl>
<dd>A text segment commonly has the flags <code>PF_X</code> and <code>PF_R</code>. A data segment commonly has <code>PF_W</code> and <code>PF_R</code>.</dd>
<dt><i>p_align</i></dt>
<dd>This member holds the value to which the segments are aligned in memory and in the file. Loadable process segments must have congruent values for <i>p_vaddr</i> and <i>p_offset</i>, modulo the page size. Values of zero and one mean no alignment is required. Otherwise, <i>p_align</i> should be a positive, integral power of two, and <i>p_vaddr</i> should equal <i>p_offset</i>, modulo <i>p_align</i>.</dd></dl>
<h3>Section header (Shdr)</h3>
<p>A file&#8217;s section header table lets one locate all the file&#8217;s sections. The section header table is an array of <i>Elf32_Shdr</i> or <i>Elf64_Shdr</i> structures. The ELF header&#8217;s <i>e_shoff</i> member gives the byte offset from the beginning of the file to the section header table. <i>e_shnum</i> holds the number of entries the section header table contains. <i>e_shentsize</i> holds the size in bytes of each entry. A section header table index is a subscript into this array. Some section header table indices are reserved: the initial entry and the indices between <code>SHN_LORESERVE</code> and <code>SHN_HIRESERVE</code>. The initial entry is used in ELF extensions for <i>e_phnum</i>, <i>e_shnum</i>, and <i>e_shstrndx</i>; in other cases, each field in the initial entry is set to zero. An object file does not have sections for these special indices:</p>
<dl>
<dt><code>SHN_UNDEF</code></dt>
<dd>This value marks an undefined, missing, irrelevant, or otherwise meaningless section reference.</dd>
<dt><code>SHN_LORESERVE</code></dt>
<dd>This value specifies the lower bound of the range of reserved indices.</dd>
<dt><code>SHN_LOPROC</code>, <code>SHN_HIPROC</code></dt>
<dd>Values greater in the inclusive range [<code>SHN_LOPROC</code>, <code>SHN_HIPROC</code>] are reserved for processor-specific semantics.</dd>
<dt><code>SHN_ABS</code></dt>
<dd>This value specifies the absolute value for the corresponding reference. For example, a symbol defined relative to section number <code>SHN_ABS</code> has an absolute value and is not affected by relocation.</dd>
<dt><code>SHN_COMMON</code></dt>
<dd>Symbols defined relative to this section are common symbols, such as FORTRAN COMMON or unallocated C external variables.</dd>
<dt><code>SHN_HIRESERVE</code></dt>
<dd>This value specifies the upper bound of the range of reserved indices. The system reserves indices between <code>SHN_LORESERVE</code> and <code>SHN_HIRESERVE</code>, inclusive. The section header table does not contain entries for the reserved indices.</dd></dl>
<p> The section header has the following structure: typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr sh_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Off&nbsp;<wbr>&nbsp;sh_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_link;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_info;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_addralign;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_entsize; } Elf32_Shdr; typedef struct {<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_name;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_type;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_flags;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr sh_addr;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Off&nbsp;<wbr>&nbsp;sh_offset;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_size;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_link;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_info;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_addralign;<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;sh_entsize; } Elf64_Shdr; No real differences exist between the 32-bit and 64-bit section headers.</p>
<dl>
<dt><i>sh_name</i></dt>
<dd>This member specifies the name of the section. Its value is an index into the section header string table section, giving the location of a null-terminated string.</dd>
<dt><i>sh_type</i></dt>
<dd>This member categorizes the section&#8217;s contents and semantics.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>SHT_NULL</code></dt>
<dd>This value marks the section header as inactive. It does not have an associated section. Other members of the section header have undefined values.</dd>
<dt><code>SHT_PROGBITS</code></dt>
<dd>This section holds information defined by the program, whose format and meaning are determined solely by the program.</dd>
<dt><code>SHT_SYMTAB</code></dt>
<dd>This section holds a symbol table. Typically, <code>SHT_SYMTAB</code> provides symbols for link editing, though it may also be used for dynamic linking. As a complete symbol table, it may contain many symbols unnecessary for dynamic linking. An object file can also contain a <code>SHT_DYNSYM</code> section.</dd>
<dt><code>SHT_STRTAB</code></dt>
<dd>This section holds a string table. An object file may have multiple string table sections.</dd>
<dt><code>SHT_RELA</code></dt>
<dd>This section holds relocation entries with explicit addends, such as type <i>Elf32_Rela</i> for the 32-bit class of object files. An object may have multiple relocation sections.</dd>
<dt><code>SHT_HASH</code></dt>
<dd>This section holds a symbol hash table. An object participating in dynamic linking must contain a symbol hash table. An object file may have only one hash table.</dd>
<dt><code>SHT_DYNAMIC</code></dt>
<dd>This section holds information for dynamic linking. An object file may have only one dynamic section.</dd>
<dt><code>SHT_NOTE</code></dt>
<dd>This section holds notes (ElfN_Nhdr).</dd>
<dt><code>SHT_NOBITS</code></dt>
<dd>A section of this type occupies no space in the file but otherwise resembles <code>SHT_PROGBITS</code>. Although this section contains no bytes, the <i>sh_offset</i> member contains the conceptual file offset.</dd>
<dt><code>SHT_REL</code></dt>
<dd>This section holds relocation offsets without explicit addends, such as type <i>Elf32_Rel</i> for the 32-bit class of object files. An object file may have multiple relocation sections.</dd>
<dt><code>SHT_SHLIB</code></dt>
<dd>This section is reserved but has unspecified semantics.</dd>
<dt><code>SHT_DYNSYM</code></dt>
<dd>This section holds a minimal set of dynamic linking symbols. An object file can also contain a <code>SHT_SYMTAB</code> section.</dd>
<dt><code>SHT_LOPROC</code>, <code>SHT_HIPROC</code></dt>
<dd>Values in the inclusive range [<code>SHT_LOPROC</code>, <code>SHT_HIPROC</code>] are reserved for processor-specific semantics.</dd>
<dt><code>SHT_LOUSER</code></dt>
<dd>This value specifies the lower bound of the range of indices reserved for application programs.</dd>
<dt><code>SHT_HIUSER</code></dt>
<dd>This value specifies the upper bound of the range of indices reserved for application programs. Section types between <code>SHT_LOUSER</code> and <code>SHT_HIUSER</code> may be used by the application, without conflicting with current or future system-defined section types.</dd></dl>
</dl>
<dt><i>sh_flags</i></dt>
<dd>Sections support one-bit flags that describe miscellaneous attributes. If a flag bit is set in <i>sh_flags</i>, the attribute is &quot;on&quot; for the section. Otherwise, the attribute is &quot;off&quot; or does not apply. Undefined attributes are set to zero.</dd>
<dl>
<dd>
</dd><dl>
<dt><code>SHF_WRITE</code></dt>
<dd>This section contains data that should be writable during process execution.</dd>
<dt><code>SHF_ALLOC</code></dt>
<dd>This section occupies memory during process execution. Some control sections do not reside in the memory image of an object file. This attribute is off for those sections.</dd>
<dt><code>SHF_EXECINSTR</code></dt>
<dd>This section contains executable machine instructions.</dd>
<dt><code>SHF_MASKPROC</code></dt>
<dd>All bits included in this mask are reserved for processor-specific semantics.</dd></dl>
</dl>
<dt><i>sh_addr</i></dt>
<dd>If this section appears in the memory image of a process, this member holds the address at which the section&#8217;s first byte should reside. Otherwise, the member contains zero.</dd>
<dt><i>sh_offset</i></dt>
<dd>This member&#8217;s value holds the byte offset from the beginning of the file to the first byte in the section. One section type, <code>SHT_NOBITS</code>, occupies no space in the file, and its <i>sh_offset</i> member locates the conceptual placement in the file.</dd>
<dt><i>sh_size</i></dt>
<dd>This member holds the section&#8217;s size in bytes. Unless the section type is <code>SHT_NOBITS</code>, the section occupies <i>sh_size</i> bytes in the file. A section of type <code>SHT_NOBITS</code> may have a nonzero size, but it occupies no space in the file.</dd>
<dt><i>sh_link</i></dt>
<dd>This member holds a section header table index link, whose interpretation depends on the section type.</dd>
<dt><i>sh_info</i></dt>
<dd>This member holds extra information, whose interpretation depends on the section type.</dd>
<dt><i>sh_addralign</i></dt>
<dd>Some sections have address alignment constraints. If a section holds a doubleword, the system must ensure doubleword alignment for the entire section. That is, the value of <i>sh_addr</i> must be congruent to zero, modulo the value of <i>sh_addralign</i>. Only zero and positive integral powers of two are allowed. The value 0 or 1 means that the section has no alignment constraints.</dd>
<dt><i>sh_entsize</i></dt>
<dd>Some sections hold a table of fixed-sized entries, such as a symbol table. For such a section, this member gives the size in bytes for each entry. This member contains zero if the section does not hold a table of fixed-size entries.</dd></dl>
<p> Various sections hold program and control information:</p>
<dl>
<dt><i>.bss</i></dt>
<dd>This section holds uninitialized data that contributes to the program&#8217;s memory image. By definition, the system initializes the data with zeros when the program begins to run. This section is of type <code>SHT_NOBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</dd>
<dt><i>.comment</i></dt>
<dd>This section holds version control information. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</dd>
<dt><i>.ctors</i></dt>
<dd>This section holds initialized pointers to the C++ constructor functions. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</dd>
<dt><i>.data</i></dt>
<dd>This section holds initialized data that contribute to the program&#8217;s memory image. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</dd>
<dt><i>.data1</i></dt>
<dd>This section holds initialized data that contribute to the program&#8217;s memory image. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</dd>
<dt><i>.debug</i></dt>
<dd>This section holds information for symbolic debugging. The contents are unspecified. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</dd>
<dt><i>.dtors</i></dt>
<dd>This section holds initialized pointers to the C++ destructor functions. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</dd>
<dt><i>.dynamic</i></dt>
<dd>This section holds dynamic linking information. The section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Whether the <code>SHF_WRITE</code> bit is set is processor-specific. This section is of type <code>SHT_DYNAMIC</code>. See the attributes above.</dd>
<dt><i>.dynstr</i></dt>
<dd>This section holds strings needed for dynamic linking, most commonly the strings that represent the names associated with symbol table entries. This section is of type <code>SHT_STRTAB</code>. The attribute type used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.dynsym</i></dt>
<dd>This section holds the dynamic linking symbol table. This section is of type <code>SHT_DYNSYM</code>. The attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.fini</i></dt>
<dd>This section holds executable instructions that contribute to the process termination code. When a program exits normally the system arranges to execute the code in this section. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</dd>
<dt><i>.gnu.version</i></dt>
<dd>This section holds the version symbol table, an array of <i>ElfN_Half</i> elements. This section is of type <code>SHT_GNU_versym</code>. The attribute type used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.gnu.version_d</i></dt>
<dd>This section holds the version symbol definitions, a table of <i>ElfN_Verdef</i> structures. This section is of type <code>SHT_GNU_verdef</code>. The attribute type used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.gnu.version_r</i></dt>
<dd>This section holds the version symbol needed elements, a table of <i>ElfN_Verneed</i> structures. This section is of type <code>SHT_GNU_versym</code>. The attribute type used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.got</i></dt>
<dd>This section holds the global offset table. This section is of type <code>SHT_PROGBITS</code>. The attributes are processor-specific.</dd>
<dt><i>.hash</i></dt>
<dd>This section holds a symbol hash table. This section is of type <code>SHT_HASH</code>. The attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.init</i></dt>
<dd>This section holds executable instructions that contribute to the process initialization code. When a program starts to run the system arranges to execute the code in this section before calling the main program entry point. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</dd>
<dt><i>.interp</i></dt>
<dd>This section holds the pathname of a program interpreter. If the file has a loadable segment that includes the section, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, that bit will be off. This section is of type <code>SHT_PROGBITS</code>.</dd>
<dt><i>.line</i></dt>
<dd>This section holds line number information for symbolic debugging, which describes the correspondence between the program source and the machine code. The contents are unspecified. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</dd>
<dt><i>.note</i></dt>
<dd>This section holds various notes. This section is of type <code>SHT_NOTE</code>. No attribute types are used.</dd>
<dt><i>.note.ABI-tag</i></dt>
<dd>This section is used to declare the expected run-time ABI of the ELF image. It may include the operating system name and its run-time versions. This section is of type <code>SHT_NOTE</code>. The only attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.note.gnu.build-id</i></dt>
<dd>This section is used to hold an ID that uniquely identifies the contents of the ELF image. Different files with the same build ID should contain the same executable content. See the <code>&#8211;build-id</code> option to the GNU linker (<code>ld</code> (1)) for more details. This section is of type <code>SHT_NOTE</code>. The only attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.note.GNU-stack</i></dt>
<dd>This section is used in Linux object files for declaring stack attributes. This section is of type <code>SHT_PROGBITS</code>. The only attribute used is <code>SHF_EXECINSTR</code>. This indicates to the GNU linker that the object file requires an executable stack.</dd>
<dt><i>.note.openbsd.ident</i></dt>
<dd>OpenBSD native executables usually contain this section to identify themselves so the kernel can bypass any compatibility ELF binary emulation tests when loading the file.</dd>
<dt><i>.plt</i></dt>
<dd>This section holds the procedure linkage table. This section is of type <code>SHT_PROGBITS</code>. The attributes are processor-specific.</dd>
<dt><i>.relNAME</i></dt>
<dd>This section holds relocation information as described below. If the file has a loadable segment that includes relocation, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. By convention, &quot;NAME&quot; is supplied by the section to which the relocations apply. Thus a relocation section for <code>.text</code> normally would have the name <code>.rel.text</code>. This section is of type <code>SHT_REL</code>.</dd>
<dt><i>.relaNAME</i></dt>
<dd>This section holds relocation information as described below. If the file has a loadable segment that includes relocation, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. By convention, &quot;NAME&quot; is supplied by the section to which the relocations apply. Thus a relocation section for <code>.text</code> normally would have the name <code>.rela.text</code>. This section is of type <code>SHT_RELA</code>.</dd>
<dt><i>.rodata</i></dt>
<dd>This section holds read-only data that typically contributes to a nonwritable segment in the process image. This section is of type <code>SHT_PROGBITS</code>. The attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.rodata1</i></dt>
<dd>This section holds read-only data that typically contributes to a nonwritable segment in the process image. This section is of type <code>SHT_PROGBITS</code>. The attribute used is <code>SHF_ALLOC</code>.</dd>
<dt><i>.shstrtab</i></dt>
<dd>This section holds section names. This section is of type <code>SHT_STRTAB</code>. No attribute types are used.</dd>
<dt><i>.strtab</i></dt>
<dd>This section holds strings, most commonly the strings that represent the names associated with symbol table entries. If the file has a loadable segment that includes the symbol string table, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. This section is of type <code>SHT_STRTAB</code>.</dd>
<dt><i>.symtab</i></dt>
<dd>This section holds a symbol table. If the file has a loadable segment that includes the symbol table, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. This section is of type <code>SHT_SYMTAB</code>.</dd>
<dt><i>.text</i></dt>
<dd>This section holds the &quot;text&quot;, or executable instructions, of a program. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</dd></dl>
<h3>String and symbol tables</h3>
<p>String table sections hold null-terminated character sequences, commonly called strings. The object file uses these strings to represent symbol and section names. One references a string as an index into the string table section. The first byte, which is index zero, is defined to hold a null byte (&#8216;\0&#8217;). Similarly, a string table&#8217;s last byte is defined to hold a null byte, ensuring null termination for all strings. </p>
<p> An object file&#8217;s symbol table holds information needed to locate and relocate a program&#8217;s symbolic definitions and references. A symbol table index is a subscript into this array. </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_name; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_value; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_size; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_info; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_other; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_shndx; } Elf32_Sym; </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_name; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_info; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;unsigned char st_other; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint16_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_shndx; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_value; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;st_size; } Elf64_Sym; </p>
<p> The 32-bit and 64-bit versions have the same members, just in a different order. </p>
<dl>
<dt><i>st_name</i></dt>
<dd> <p> This member holds an index into the object file&#8217;s symbol string table, which holds character representations of the symbol names. If the value is nonzero, it represents a string table index that gives the symbol name. Otherwise, the symbol has no name. </p>
 </dd>
<dt><i>st_value</i></dt>
<dd> <p> This member gives the value of the associated symbol. </p>
 </dd>
<dt><i>st_size</i></dt>
<dd> <p> Many symbols have associated sizes. This member holds zero if the symbol has no size or an unknown size. </p>
 </dd>
<dt><i>st_info</i></dt>
<dd> <p> This member specifies the symbol&#8217;s type and binding attributes: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>STT_NOTYPE</code></dt>
<dd> <p> The symbol&#8217;s type is not defined. </p>
 </dd>
<dt><code>STT_OBJECT</code></dt>
<dd> <p> The symbol is associated with a data object. </p>
 </dd>
<dt><code>STT_FUNC</code></dt>
<dd> <p> The symbol is associated with a function or other executable code. </p>
 </dd>
<dt><code>STT_SECTION</code></dt>
<dd> <p> The symbol is associated with a section. Symbol table entries of this type exist primarily for relocation and normally have <code>STB_LOCAL</code> bindings. </p>
 </dd>
<dt><code>STT_FILE</code></dt>
<dd> <p> By convention, the symbol&#8217;s name gives the name of the source file associated with the object file. A file symbol has <code>STB_LOCAL</code> bindings, its section index is <code>SHN_ABS</code>, and it precedes the other <code>STB_LOCAL</code> symbols of the file, if it is present. </p>
 </dd>
<dt><code>STT_LOPROC</code>, <code>STT_HIPROC</code></dt>
<dd> <p> Values in the inclusive range [<code>STT_LOPROC</code>, <code>STT_HIPROC</code>] are reserved for processor-specific semantics. </p>
 </dd>
<dt><code>STB_LOCAL</code></dt>
<dd> <p> Local symbols are not visible outside the object file containing their definition. Local symbols of the same name may exist in multiple files without interfering with each other. </p>
 </dd>
<dt><code>STB_GLOBAL</code></dt>
<dd> <p> Global symbols are visible to all object files being combined. One file&#8217;s definition of a global symbol will satisfy another file&#8217;s undefined reference to the same symbol. </p>
 </dd>
<dt><code>STB_WEAK</code></dt>
<dd> <p> Weak symbols resemble global symbols, but their definitions have lower precedence. </p>
 </dd>
<dt><code>STB_LOPROC</code>, <code>STB_HIPROC</code></dt>
<dd> <p> Values in the inclusive range [<code>STB_LOPROC</code>, <code>STB_HIPROC</code>] are reserved for processor-specific semantics. </p>
 </dd></dl>
</dl>
<dd> <p> There are macros for packing and unpacking the binding and type fields: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>ELF32_ST_BIND(</code><i>info</i><code>)</code>, <code>ELF64_ST_BIND(</code><i>info</i><code>)</code></dt>
<dd> <p> Extract a binding from an <i>st_info</i> value. </p>
 </dd>
<dt><code>ELF32_ST_TYPE(</code><i>info</i><code>)</code>, <code>ELF64_ST_TYPE(</code><i>info</i><code>)</code></dt>
<dd> <p> Extract a type from an <i>st_info</i> value. </p>
 </dd>
<dt><code>ELF32_ST_INFO(</code><i>bind</i><code>, </code><i>type</i><code>)</code>, <code>ELF64_ST_INFO(</code><i>bind</i><code>, </code><i>type</i><code>)</code></dt>
<dd> <p> Convert a binding and a type into an <i>st_info</i> value. </p>
 </dd></dl>
</dl>
<dt><i>st_other</i></dt>
<dd> <p> This member defines the symbol visibility. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>STV_DEFAULT</code></dt>
<dd> <p> Default symbol visibility rules. Global and weak symbols are available to other modules; references in the local module can be interposed by definitions in other modules. </p>
 </dd>
<dt><code>STV_INTERNAL</code></dt>
<dd> <p> Processor-specific hidden class. </p>
 </dd>
<dt><code>STV_HIDDEN</code></dt>
<dd> <p> Symbol is unavailable to other modules; references in the local module always resolve to the local symbol (i.e., the symbol can&#8217;t be interposed by definitions in other modules). </p>
 </dd>
<dt><code>STV_PROTECTED</code></dt>
<dd> <p> Symbol is available to other modules, but references in the local module always resolve to the local symbol. </p>
 </dd></dl>
<p> There are macros for extracting the visibility type: </p>
<p> <code>ELF32_ST_VISIBILITY</code>(other) or <code>ELF64_ST_VISIBILITY</code>(other) </dl>
 </p>
<dt><i>st_shndx</i></dt>
<dd> <p> Every symbol table entry is &quot;defined&quot; in relation to some section. This member holds the relevant section header table index. </p>
 </dd></dl>
<h3>Relocation entries (Rel & Rela)</h3>
<p> Relocation is the process of connecting symbolic references with symbolic definitions. Relocatable files must have information that describes how to modify their section contents, thus allowing executable and shared object files to hold the right information for a process&#8217;s program image. Relocation entries are these data. </p>
<p> Relocation structures that do not need an addend: </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr r_offset; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_info; } Elf32_Rel; </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr r_offset; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_info; } Elf64_Rel; </p>
<p> Relocation structures that need an addend: </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr r_offset; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_info; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int32_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_addend; } Elf32_Rela; </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr r_offset; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;uint64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_info; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;int64_t&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;r_addend; } Elf64_Rela; </p>
<dl>
<dt><i>r_offset</i></dt>
<dd> <p> This member gives the location at which to apply the relocation action. For a relocatable file, the value is the byte offset from the beginning of the section to the storage unit affected by the relocation. For an executable file or shared object, the value is the virtual address of the storage unit affected by the relocation. </p>
 </dd>
<dt><i>r_info</i></dt>
<dd> <p> This member gives both the symbol table index with respect to which the relocation must be made and the type of relocation to apply. Relocation types are processor-specific. When the text refers to a relocation entry&#8217;s relocation type or symbol table index, it means the result of applying <code>ELF[32|64]_R_TYPE</code> or <code>ELF[32|64]_R_SYM</code>, respectively, to the entry&#8217;s <i>r_info</i> member. </p>
 </dd>
<dt><i>r_addend</i></dt>
<dd> <p> This member specifies a constant addend used to compute the value to be stored into the relocatable field. </p>
 </dd></dl>
<h3>Dynamic tags (Dyn)</h3>
<p> The <i>.dynamic</i> section contains a series of structures that hold relevant dynamic linking information. The <i>d_tag</i> member controls the interpretation of <i>d_un</i>. </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Sword&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_tag; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word d_val; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Addr d_ptr; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;d_un; } Elf32_Dyn; extern Elf32_Dyn _DYNAMIC[]; </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Sxword&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;d_tag; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;union&nbsp;{ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Xword d_val; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Addr&nbsp;<wbr>&nbsp;d_ptr; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;}&nbsp;d_un; } Elf64_Dyn; extern Elf64_Dyn _DYNAMIC[]; </p>
<dl>
<dt><i>d_tag</i></dt>
<dd> <p> This member may have any of the following values: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>DT_NULL</code></dt>
<dd> <p> Marks end of dynamic section </p>
 </dd>
<dt><code>DT_NEEDED</code></dt>
<dd> <p> String table offset to name of a needed library </p>
 </dd>
<dt><code>DT_PLTRELSZ</code></dt>
<dd> <p> Size in bytes of PLT relocation entries </p>
 </dd>
<dt><code>DT_PLTGOT</code></dt>
<dd> <p> Address of PLT and/or GOT </p>
 </dd>
<dt><code>DT_HASH</code></dt>
<dd> <p> Address of symbol hash table </p>
 </dd>
<dt><code>DT_STRTAB</code></dt>
<dd> <p> Address of string table </p>
 </dd>
<dt><code>DT_SYMTAB</code></dt>
<dd> <p> Address of symbol table </p>
 </dd>
<dt><code>DT_RELA</code></dt>
<dd> <p> Address of Rela relocation table </p>
 </dd>
<dt><code>DT_RELASZ</code></dt>
<dd> <p> Size in bytes of the Rela relocation table </p>
 </dd>
<dt><code>DT_RELAENT</code></dt>
<dd> <p> Size in bytes of a Rela relocation table entry </p>
 </dd>
<dt><code>DT_STRSZ</code></dt>
<dd> <p> Size in bytes of string table </p>
 </dd>
<dt><code>DT_SYMENT</code></dt>
<dd> <p> Size in bytes of a symbol table entry </p>
 </dd>
<dt><code>DT_INIT</code></dt>
<dd> <p> Address of the initialization function </p>
 </dd>
<dt><code>DT_FINI</code></dt>
<dd> <p> Address of the termination function </p>
 </dd>
<dt><code>DT_SONAME</code></dt>
<dd> <p> String table offset to name of shared object </p>
 </dd>
<dt><code>DT_RPATH</code></dt>
<dd> <p> String table offset to library search path (deprecated) </p>
 </dd>
<dt><code>DT_SYMBOLIC</code></dt>
<dd> <p> Alert linker to search this shared object before the executable for symbols </p>
 </dd>
<dt><code>DT_REL</code></dt>
<dd> <p> Address of Rel relocation table </p>
 </dd>
<dt><code>DT_RELSZ</code></dt>
<dd> <p> Size in bytes of Rel relocation table </p>
 </dd>
<dt><code>DT_RELENT</code></dt>
<dd> <p> Size in bytes of a Rel table entry </p>
 </dd>
<dt><code>DT_PLTREL</code></dt>
<dd> <p> Type of relocation entry to which the PLT refers (Rela or Rel) </p>
 </dd>
<dt><code>DT_DEBUG</code></dt>
<dd> <p> Undefined use for debugging </p>
 </dd>
<dt><code>DT_TEXTREL</code></dt>
<dd> <p> Absence of this entry indicates that no relocation entries should apply to a nonwritable segment </p>
 </dd>
<dt><code>DT_JMPREL</code></dt>
<dd> <p> Address of relocation entries associated solely with the PLT </p>
 </dd>
<dt><code>DT_BIND_NOW</code></dt>
<dd> <p> Instruct dynamic linker to process all relocations before transferring control to the executable </p>
 </dd>
<dt><code>DT_RUNPATH</code></dt>
<dd> <p> String table offset to library search path </p>
 </dd>
<dt><code>DT_LOPROC</code>, <code>DT_HIPROC</code></dt>
<dd> <p> Values in the inclusive range [<code>DT_LOPROC</code>, <code>DT_HIPROC</code>] are reserved for processor-specific semantics </p>
 </dd></dl>
</dl>
<dt><i>d_val</i></dt>
<dd> <p> This member represents integer values with various interpretations. </p>
 </dd>
<dt><i>d_ptr</i></dt>
<dd> <p> This member represents program virtual addresses. When interpreting these addresses, the actual address should be computed based on the original file value and memory base address. Files do not contain relocation entries to fixup these addresses. </p>
 </dd>
<dt><i>_DYNAMIC</i></dt>
<dd> <p> Array containing all the dynamic structures in the <i>.dynamic</i> section. This is automatically populated by the linker. </p>
 </dd></dl>
<h3>Notes (Nhdr)</h3>
<p> ELF notes allow for appending arbitrary information for the system to use. They are largely used by core files (<i>e_type</i> of <code>ET_CORE</code>), but many projects define their own set of extensions. For example, the GNU tool chain uses ELF notes to pass information from the linker to the C library. </p>
<p> Note sections contain a series of notes (see the <i>struct</i> definitions below). Each note is followed by the name field (whose length is defined in <i>n_namesz</i>) and then by the descriptor field (whose length is defined in <i>n_descsz</i>) and whose starting address has a 4 byte alignment. Neither field is defined in the note struct due to their arbitrary lengths. </p>
<p> An example for parsing out two consecutive notes should clarify their layout in memory: </p>
<p> void *memory, *name, *desc; Elf64_Nhdr *note, *next_note; </p>
<p> /* The buffer is pointing to the start of the section/segment */ note = memory; </p>
<p> /* If the name is defined, it follows the note */ name = note-&gt;n_namesz == 0 ? NULL : memory + sizeof(*note); </p>
<p> /* If the descriptor is defined, it follows the name <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;(with alignment)&nbsp;*/ </p>
<p> desc = note-&gt;n_descsz == 0 ? NULL : <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;memory&nbsp;+&nbsp;sizeof(*note)&nbsp;+&nbsp;ALIGN_UP(note-&gt;n_namesz, 4); </p>
<p> /* The next note follows both (with alignment) */ next_note = memory + sizeof(*note) + <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ALIGN_UP(note-&gt;n_namesz, 4)&nbsp;+ <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;ALIGN_UP(note-&gt;n_descsz, 4); </p>
<p> Keep in mind that the interpretation of <i>n_type</i> depends on the namespace defined by the <i>n_namesz</i> field. If the <i>n_namesz</i> field is not set (e.g., is 0), then there are two sets of notes: one for core files and one for all other ELF types. If the namespace is unknown, then tools will usually fallback to these sets of notes as well. </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word n_namesz; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word n_descsz; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf32_Word n_type; } Elf32_Nhdr; </p>
<p> typedef struct { <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Word n_namesz; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Word n_descsz; <br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;Elf64_Word n_type; } Elf64_Nhdr; </p>
<dl>
<dt><i>n_namesz</i></dt>
<dd> <p> The length of the name field in bytes. The contents will immediately follow this note in memory. The name is null terminated. For example, if the name is &quot;GNU&quot;, then <i>n_namesz</i> will be set to 4. </p>
 </dd>
<dt><i>n_descsz</i></dt>
<dd> <p> The length of the descriptor field in bytes. The contents will immediately follow the name field in memory. </p>
 </dd>
<dt><i>n_type</i></dt>
<dd> <p> Depending on the value of the name field, this member may have any of the following values: </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>Core files (e_type = ET_CORE)</code></dt>
<dd> <p> Notes used by all core files. These are highly operating system or architecture specific and often require close coordination with kernels, C libraries, and debuggers. These are used when the namespace is the default (i.e., <i>n_namesz</i> will be set to 0), or a fallback when the namespace is unknown. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>NT_PRSTATUS</code></dt>
<dd> <p> prstatus struct </p>
 </dd>
<dt><code>NT_FPREGSET</code></dt>
<dd> <p> fpregset struct </p>
 </dd>
<dt><code>NT_PRPSINFO</code></dt>
<dd> <p> prpsinfo struct </p>
 </dd>
<dt><code>NT_PRXREG</code></dt>
<dd> <p> prxregset struct </p>
 </dd>
<dt><code>NT_TASKSTRUCT</code></dt>
<dd> <p> task structure </p>
 </dd>
<dt><code>NT_PLATFORM</code></dt>
<dd> <p> String from sysinfo(SI_PLATFORM) </p>
 </dd>
<dt><code>NT_AUXV</code></dt>
<dd> <p> auxv array </p>
 </dd>
<dt><code>NT_GWINDOWS</code></dt>
<dd> <p> gwindows struct </p>
 </dd>
<dt><code>NT_ASRS</code></dt>
<dd> <p> asrset struct </p>
 </dd>
<dt><code>NT_PSTATUS</code></dt>
<dd> <p> pstatus struct </p>
 </dd>
<dt><code>NT_PSINFO</code></dt>
<dd> <p> psinfo struct </p>
 </dd>
<dt><code>NT_PRCRED</code></dt>
<dd> <p> prcred struct </p>
 </dd>
<dt><code>NT_UTSNAME</code></dt>
<dd> <p> utsname struct </p>
 </dd>
<dt><code>NT_LWPSTATUS</code></dt>
<dd> <p> lwpstatus struct </p>
 </dd>
<dt><code>NT_LWPSINFO</code></dt>
<dd> <p> lwpinfo struct </p>
 </dd>
<dt><code>NT_PRFPXREG</code></dt>
<dd> <p> fprxregset struct </p>
 </dd>
<dt><code>NT_SIGINFO</code></dt>
<dd> <p> siginfo_t (size might increase over time) </p>
 </dd>
<dt><code>NT_FILE</code></dt>
<dd> <p> Contains information about mapped files </p>
 </dd>
<dt><code>NT_PRXFPREG</code></dt>
<dd> <p> user_fxsr_struct </p>
 </dd>
<dt><code>NT_PPC_VMX</code></dt>
<dd> <p> PowerPC Altivec/VMX registers </p>
 </dd>
<dt><code>NT_PPC_SPE</code></dt>
<dd> <p> PowerPC SPE/EVR registers </p>
 </dd>
<dt><code>NT_PPC_VSX</code></dt>
<dd> <p> PowerPC VSX registers </p>
 </dd>
<dt><code>NT_386_TLS</code></dt>
<dd> <p> i386 TLS slots (struct user_desc) </p>
 </dd>
<dt><code>NT_386_IOPERM</code></dt>
<dd> <p> x86 io permission bitmap (1=deny) </p>
 </dd>
<dt><code>NT_X86_XSTATE</code></dt>
<dd> <p> x86 extended state using xsave </p>
 </dd>
<dt><code>NT_S390_HIGH_GPRS</code></dt>
<dd> <p> s390 upper register halves </p>
 </dd>
<dt><code>NT_S390_TIMER</code></dt>
<dd> <p> s390 timer register </p>
 </dd>
<dt><code>NT_S390_TODCMP</code></dt>
<dd> <p> s390 time-of-day (TOD) clock comparator register </p>
 </dd>
<dt><code>NT_S390_TODPREG</code></dt>
<dd> <p> s390 time-of-day (TOD) programmable register </p>
 </dd>
<dt><code>NT_S390_CTRS</code></dt>
<dd> <p> s390 control registers </p>
 </dd>
<dt><code>NT_S390_PREFIX</code></dt>
<dd> <p> s390 prefix register </p>
 </dd>
<dt><code>NT_S390_LAST_BREAK</code></dt>
<dd> <p> s390 breaking event address </p>
 </dd>
<dt><code>NT_S390_SYSTEM_CALL</code></dt>
<dd> <p> s390 system call restart data </p>
 </dd>
<dt><code>NT_S390_TDB</code></dt>
<dd> <p> s390 transaction diagnostic block </p>
 </dd>
<dt><code>NT_ARM_VFP</code></dt>
<dd> <p> ARM VFP/NEON registers </p>
 </dd>
<dt><code>NT_ARM_TLS</code></dt>
<dd> <p> ARM TLS register </p>
 </dd>
<dt><code>NT_ARM_HW_BREAK</code></dt>
<dd> <p> ARM hardware breakpoint registers </p>
 </dd>
<dt><code>NT_ARM_HW_WATCH</code></dt>
<dd> <p> ARM hardware watchpoint registers </p>
 </dd>
<dt><code>NT_ARM_SYSTEM_CALL</code></dt>
<dd> <p> ARM system call number </p>
 </dd></dl>
</dl>
<dt><code>n_name = GNU</code></dt>
<dd> <p> Extensions used by the GNU tool chain. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>NT_GNU_ABI_TAG</code></dt>
<dd> <p> Operating system (OS) ABI information. The desc field will be 4 words: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> word 0: OS descriptor (<code>ELF_NOTE_OS_LINUX</code>, <code>ELF_NOTE_OS_GNU</code>, and so on)` </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> word 1: major version of the ABI </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> word 2: minor version of the ABI </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> word 3: subminor version of the ABI </p>
 </dd></dl>
</dl>
<dt><code>NT_GNU_HWCAP</code></dt>
<dd> <p> Synthetic hwcap information. The desc field begins with two words: </p>
 </dd>
<dd>  </dd>
<dl>
<dd>  </dd>
<dl>
<dt>&bull;</dt>
<dd> <p> word 0: number of entries </p>
 </dd>
<dt>&bull;</dt>
<dd> <p> word 1: bit mask of enabled entries </p>
 </dd></dl>
</dl>
<dd> <p> Then follow variable-length entries, one byte followed by a null-terminated hwcap name string. The byte gives the bit number to test if enabled, (1U &lt;&lt; bit) &amp; bit mask. </p>
 </dd>
<dt><code>NT_GNU_BUILD_ID</code></dt>
<dd> <p> Unique build ID as generated by the GNU <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1) <code>--build-id</code> option. The desc consists of any nonzero number of bytes. </p>
 </dd>
<dt><code>NT_GNU_GOLD_VERSION</code></dt>
<dd> <p> The desc contains the GNU Gold linker version used. </p>
 </dd></dl>
</dl>
<dt><code>Default/unknown namespace (e_type != ET_CORE)</code></dt>
<dd> <p> These are used when the namespace is the default (i.e., <i>n_namesz</i> will be set to 0), or a fallback when the namespace is unknown. </p>
 </dd>
<dl>
<dd>  </dd>
<dl>
<dt><code>NT_VERSION</code></dt>
<dd> <p> A version string of some sort. </p>
 </dd>
<dt><code>NT_ARCH</code></dt>
<dd> <p> Architecture information. </p>
 </dd></dl>
</dl>
</dl>
</dl>
</dl>
<h2>NOTES</h2>
<p> ELF first appeared in System V. The ELF format is an adopted standard. </p>
<p> The extensions for <i>e_phnum</i>, <i>e_shnum</i>, and <i>e_shstrndx</i> respectively are Linux extensions. Sun, BSD and AMD64 also support them; for further information, look under SEE ALSO.  </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-as/">as</a></code>(1), <code><a href="/docs/linux/man/1-elfedit/">elfedit</a></code>(1), <code><a href="/docs/linux/man/1-gdb/">gdb</a></code>(1), <code><a href="/docs/linux/man/1-ld/">ld</a></code>(1), <code><a href="/docs/linux/man/1-nm/">nm</a></code>(1), <code><a href="/docs/linux/man/1-objcopy/">objcopy</a></code>(1), <code><a href="/docs/linux/man/1-objdump/">objdump</a></code>(1), <code><a href="/docs/linux/man/1-patchelf/">patchelf</a></code>(1), <code><a href="/docs/linux/man/1-readelf/">readelf</a></code>(1), <code><a href="/docs/linux/man/1-size/">size</a></code>(1), <code><a href="/docs/linux/man/1-strings/">strings</a></code>(1), <code><a href="/docs/linux/man/1-strip/">strip</a></code>(1), <code><a href="/docs/linux/man/2-execve/">execve</a></code>(2), <code><a href="/docs/linux/man/3-dl_iterate_phdr/">dl_iterate_phdr</a></code>(3), <code><a href="/docs/linux/man/5-core/">core</a></code>(5), <code><a href="/docs/linux/man/8-ld.so/">ld.so</a></code>(8) </p>
<p> Hewlett-Packard, <i>Elf-64 Object File Format</i>. </p>
<p> Santa Cruz Operation, <i>System V Application Binary Interface</i>. </p>
<p> UNIX System Laboratories, &quot;Object Files&quot;, <i>Executable and Linking Format (ELF)</i>. </p>
<p> Sun Microsystems, <i>Linker and Libraries Guide</i>. </p>
<p> AMD64 ABI Draft, <i>System V Application Binary Interface AMD64 Architecture Processor Supplement</i>.  </p>
<h2>COLOPHON</h2>
<p> This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
<h2>Index</h2>
