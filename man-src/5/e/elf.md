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
<dt><i>e_ident</i></p>
<dd>This array of bytes specifies how to interpret the file, independent of the processor or the file&#8217;s remaining contents. Within this array everything is named by macros, which start with the prefix <code>EI_</code> and may contain values which start with the prefix <code>ELF</code>. The following macros are defined:</p>
<dl>
<dd>
<dl>
<dt><code>EI_MAG0</code></p>
<dd>The first byte of the magic number. It must be filled with <code>ELFMAG0</code>. (0: 0x7f)</p>
<dt><code>EI_MAG1</code></p>
<dd>The second byte of the magic number. It must be filled with <code>ELFMAG1</code>. (1: &#8216;E&#8217;)</p>
<dt><code>EI_MAG2</code></p>
<dd>The third byte of the magic number. It must be filled with <code>ELFMAG2</code>. (2: &#8216;L&#8217;)</p>
<dt><code>EI_MAG3</code></p>
<dd>The fourth byte of the magic number. It must be filled with <code>ELFMAG3</code>. (3: &#8216;F&#8217;)</p>
<dt><code>EI_CLASS</code></p>
<dd>The fifth byte identifies the architecture for this binary:</p>
<dl>
<dd>
<dl>
<dt><code>ELFCLASSNONE</code></p>
<dd>This class is invalid.</p>
<dt><code>ELFCLASS32</code></p>
<dd>This defines the 32-bit architecture. It supports machines with files and virtual address spaces up to 4 Gigabytes.</p>
<dt><code>ELFCLASS64</code></p>
<dd>This defines the 64-bit architecture.</dl>
</dl>
<dt><code>EI_DATA</code></p>
<dd>The sixth byte specifies the data encoding of the processor-specific data in the file. Currently, these encodings are supported:</p>
<dl>
<dd>
<dl>
<dt><code>ELFDATANONE</code></p>
<dd>Unknown data format.</p>
<dt><code>ELFDATA2LSB</code></p>
<dd>Two&#8217;s complement, little-endian.</p>
<dt><code>ELFDATA2MSB</code></p>
<dd>Two&#8217;s complement, big-endian.</dl>
</dl>
<dt><code>EI_VERSION</code></p>
<dd>The seventh byte is the version number of the ELF specification:</p>
<dd>
<dl>
<dd>
<dl>
<dt><code>EV_NONE</code></p>
<dd>Invalid version.</p>
<dt><code>EV_CURRENT</code></p>
<dd>Current version.</dl>
</dl>
<dt><code>EI_OSABI</code></p>
<dd>The eighth byte identifies the operating system and ABI to which the object is targeted. Some fields in other ELF structures have flags and values that have platform-specific meanings; the interpretation of those fields is determined by the value of this byte. For example:</p>
<dl>
<dd>
<dl>
<dt><code>ELFOSABI_NONE</code></p>
<dd>Same as ELFOSABI_SYSV</p>
<dt><code>ELFOSABI_SYSV</code></p>
<dd>UNIX System V ABI</p>
<dt><code>ELFOSABI_HPUX</code></p>
<dd>HP-UX ABI</p>
<dt><code>ELFOSABI_NETBSD</code></p>
<dd>NetBSD ABI</p>
<dt><code>ELFOSABI_LINUX</code></p>
<dd>Linux ABI</p>
<dt><code>ELFOSABI_SOLARIS</code></p>
<dd>Solaris ABI</p>
<dt><code>ELFOSABI_IRIX</code></p>
<dd>IRIX ABI</p>
<dt><code>ELFOSABI_FREEBSD</code></p>
<dd>FreeBSD ABI</p>
<dt><code>ELFOSABI_TRU64</code></p>
<dd>TRU64 UNIX ABI</p>
<dt><code>ELFOSABI_ARM</code></p>
<dd>ARM architecture ABI</p>
<dt><code>ELFOSABI_STANDALONE</code></p>
<dd>Stand-alone (embedded) ABI</dl>
</dl>
<dt><code>EI_ABIVERSION</code></p>
<dd>The ninth byte identifies the version of the ABI to which the object is targeted. This field is used to distinguish among incompatible versions of an ABI. The interpretation of this version number is dependent on the ABI identified by the <code>EI_OSABI</code> field. Applications conforming to this specification use the value 0.</p>
<dt><code>EI_PAD</code></p>
<dd>Start of padding. These bytes are reserved and set to zero. Programs which read them should ignore them. The value for <code>EI_PAD</code> will change in the future if currently unused bytes are given meanings.</p>
<dt><code>EI_NIDENT</code></p>
<dd>The size of the <i>e_ident</i> array.</dl>
</dl>
<dt><i>e_type</i></p>
<dd>This member of the structure identifies the object file type:</p>
<dl>
<dd>
<dl>
<dt><code>ET_NONE</code></p>
<dd>An unknown type.</p>
<dt><code>ET_REL</code></p>
<dd>A relocatable file.</p>
<dt><code>ET_EXEC</code></p>
<dd>An executable file.</p>
<dt><code>ET_DYN</code></p>
<dd>A shared object.</p>
<dt><code>ET_CORE</code></p>
<dd>A core file.</dl>
</dl>
<dt><i>e_machine</i></p>
<dd>This member specifies the required architecture for an individual file. For example:</p>
<dl>
<dd>
<dl>
<dt><code>EM_NONE</code></p>
<dd>An unknown machine</p>
<dt><code>EM_M32</code></p>
<dd>AT&amp;T WE 32100</p>
<dt><code>EM_SPARC</code></p>
<dd>Sun Microsystems SPARC</p>
<dt><code>EM_386</code></p>
<dd>Intel 80386</p>
<dt><code>EM_68K</code></p>
<dd>Motorola 68000</p>
<dt><code>EM_88K</code></p>
<dd>Motorola 88000</p>
<dt><code>EM_860</code></p>
<dd>Intel 80860</p>
<dt><code>EM_MIPS</code></p>
<dd>MIPS RS3000 (big-endian only)</p>
<dt><code>EM_PARISC</code></p>
<dd>HP/PA</p>
<dt><code>EM_SPARC32PLUS</code></p>
<dd>SPARC with enhanced instruction set</p>
<dt><code>EM_PPC</code></p>
<dd>PowerPC</p>
<dt><code>EM_PPC64</code></p>
<dd>PowerPC 64-bit</p>
<dt><code>EM_S390</code></p>
<dd>IBM S/390</p>
<dt><code>EM_ARM</code></p>
<dd>Advanced RISC Machines</p>
<dt><code>EM_SH</code></p>
<dd>Renesas SuperH</p>
<dt><code>EM_SPARCV9</code></p>
<dd>SPARC v9 64-bit</p>
<dt><code>EM_IA_64</code></p>
<dd>Intel Itanium</p>
<dt><code>EM_X86_64</code></p>
<dd>AMD x86-64</p>
<dt><code>EM_VAX</code></p>
<dd>DEC Vax</dl>
</dl>
<dt><i>e_version</i></p>
<dd>This member identifies the file version:</p>
<dl>
<dd>
<dl>
<dt><code>EV_NONE</code></p>
<dd>Invalid version</p>
<dt><code>EV_CURRENT</code></p>
<dd>Current version</dl>
</dl>
<dt><i>e_entry</i></p>
<dd>This member gives the virtual address to which the system first transfers control, thus starting the process. If the file has no associated entry point, this member holds zero.</p>
<dt><i>e_phoff</i></p>
<dd>This member holds the program header table&#8217;s file offset in bytes. If the file has no program header table, this member holds zero.</p>
<dt><i>e_shoff</i></p>
<dd>This member holds the section header table&#8217;s file offset in bytes. If the file has no section header table, this member holds zero.</p>
<dt><i>e_flags</i></p>
<dd>This member holds processor-specific flags associated with the file. Flag names take the form EF_`machine_flag&#8217;. Currently, no flags have been defined.</p>
<dt><i>e_ehsize</i></p>
<dd>This member holds the ELF header&#8217;s size in bytes.</p>
<dt><i>e_phentsize</i></p>
<dd>This member holds the size in bytes of one entry in the file&#8217;s program header table; all entries are the same size.</p>
<dt><i>e_phnum</i></p>
<dd>This member holds the number of entries in the program header table. Thus the product of <i>e_phentsize</i> and <i>e_phnum</i> gives the table&#8217;s size in bytes. If a file has no program header, <i>e_phnum</i> holds the value zero.</p>
<dd>If the number of entries in the program header table is larger than or equal to <code>PN_XNUM</code> (0xffff), this member holds <code>PN_XNUM</code> (0xffff) and the real number of entries in the program header table is held in the <i>sh_info</i> member of the initial entry in section header table. Otherwise, the <i>sh_info</i> member of the initial entry contains the value zero.</p>
<dl>
<dd>
<dl>
<dt><code>PN_XNUM</code></p>
<dd>This is defined as 0xffff, the largest number <i>e_phnum</i> can have, specifying where the actual number of program headers is assigned.</dl>
</dl>
<dt><i>e_shentsize</i></p>
<dd>This member holds a sections header&#8217;s size in bytes. A section header is one entry in the section header table; all entries are the same size.</p>
<dt><i>e_shnum</i></p>
<dd>This member holds the number of entries in the section header table. Thus the product of <i>e_shentsize</i> and <i>e_shnum</i> gives the section header table&#8217;s size in bytes. If a file has no section header table, <i>e_shnum</i> holds the value of zero.</p>
<dd>If the number of entries in the section header table is larger than or equal to <code>SHN_LORESERVE</code> (0xff00), <i>e_shnum</i> holds the value zero and the real number of entries in the section header table is held in the <i>sh_size</i> member of the initial entry in section header table. Otherwise, the <i>sh_size</i> member of the initial entry in the section header table holds the value zero.</p>
<dt><i>e_shstrndx</i></p>
<dd>This member holds the section header table index of the entry associated with the section name string table. If the file has no section name string table, this member holds the value <code>SHN_UNDEF</code>.</p>
<dd>If the index of section name string table section is larger than or equal to <code>SHN_LORESERVE</code> (0xff00), this member holds <code>SHN_XINDEX</code> (0xffff) and the real index of the section name string table section is held in the <i>sh_link</i> member of the initial entry in section header table. Otherwise, the <i>sh_link</i> member of the initial entry in section header table contains the value zero.</dl>
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
<dt><i>p_type</i></p>
<dd>This member of the structure indicates what kind of segment this array element describes or how to interpret the array element&#8217;s information.</p>
<dl>
<dd>
<dl>
<dt><code>PT_NULL</code></p>
<dd>The array element is unused and the other members&#8217; values are undefined. This lets the program header have ignored entries.</p>
<dt><code>PT_LOAD</code></p>
<dd>The array element specifies a loadable segment, described by <i>p_filesz</i> and <i>p_memsz</i>. The bytes from the file are mapped to the beginning of the memory segment. If the segment&#8217;s memory size <i>p_memsz</i> is larger than the file size <i>p_filesz</i>, the &quot;extra&quot; bytes are defined to hold the value 0 and to follow the segment&#8217;s initialized area. The file size may not be larger than the memory size. Loadable segment entries in the program header table appear in ascending order, sorted on the <i>p_vaddr</i> member.</p>
<dt><code>PT_DYNAMIC</code></p>
<dd>The array element specifies dynamic linking information.</p>
<dt><code>PT_INTERP</code></p>
<dd>The array element specifies the location and size of a null-terminated pathname to invoke as an interpreter. This segment type is meaningful only for executable files (though it may occur for shared objects). However it may not occur more than once in a file. If it is present, it must precede any loadable segment entry.</p>
<dt><code>PT_NOTE</code></p>
<dd>The array element specifies the location of notes (ElfN_Nhdr).</p>
<dt><code>PT_SHLIB</code></p>
<dd>This segment type is reserved but has unspecified semantics. Programs that contain an array element of this type do not conform to the ABI.</p>
<dt><code>PT_PHDR</code></p>
<dd>The array element, if present, specifies the location and size of the program header table itself, both in the file and in the memory image of the program. This segment type may not occur more than once in a file. Moreover, it may occur only if the program header table is part of the memory image of the program. If it is present, it must precede any loadable segment entry.</p>
<dt><code>PT_LOPROC</code>, <code>PT_HIPROC</code></p>
<dd>Values in the inclusive range [<code>PT_LOPROC</code>, <code>PT_HIPROC</code>] are reserved for processor-specific semantics.</p>
<dt><code>PT_GNU_STACK</code></p>
<dd>GNU extension which is used by the Linux kernel to control the state of the stack via the flags set in the <i>p_flags</i> member.</dl>
</dl>
<dt><i>p_offset</i></p>
<dd>This member holds the offset from the beginning of the file at which the first byte of the segment resides.</p>
<dt><i>p_vaddr</i></p>
<dd>This member holds the virtual address at which the first byte of the segment resides in memory.</p>
<dt><i>p_paddr</i></p>
<dd>On systems for which physical addressing is relevant, this member is reserved for the segment&#8217;s physical address. Under BSD this member is not used and must be zero.</p>
<dt><i>p_filesz</i></p>
<dd>This member holds the number of bytes in the file image of the segment. It may be zero.</p>
<dt><i>p_memsz</i></p>
<dd>This member holds the number of bytes in the memory image of the segment. It may be zero.</p>
<dt><i>p_flags</i></p>
<dd>This member holds a bit mask of flags relevant to the segment:</p>
<dl>
<dd>
<dl>
<dt><code>PF_X</code></p>
<dd>An executable segment.</p>
<dt><code>PF_W</code></p>
<dd>A writable segment.</p>
<dt><code>PF_R</code></p>
<dd>A readable segment.</dl>
</dl>
<dd>A text segment commonly has the flags <code>PF_X</code> and <code>PF_R</code>. A data segment commonly has <code>PF_W</code> and <code>PF_R</code>.</p>
<dt><i>p_align</i></p>
<dd>This member holds the value to which the segments are aligned in memory and in the file. Loadable process segments must have congruent values for <i>p_vaddr</i> and <i>p_offset</i>, modulo the page size. Values of zero and one mean no alignment is required. Otherwise, <i>p_align</i> should be a positive, integral power of two, and <i>p_vaddr</i> should equal <i>p_offset</i>, modulo <i>p_align</i>.</dl>
<h3>Section header (Shdr)</h3>
<p>A file&#8217;s section header table lets one locate all the file&#8217;s sections. The section header table is an array of <i>Elf32_Shdr</i> or <i>Elf64_Shdr</i> structures. The ELF header&#8217;s <i>e_shoff</i> member gives the byte offset from the beginning of the file to the section header table. <i>e_shnum</i> holds the number of entries the section header table contains. <i>e_shentsize</i> holds the size in bytes of each entry. A section header table index is a subscript into this array. Some section header table indices are reserved: the initial entry and the indices between <code>SHN_LORESERVE</code> and <code>SHN_HIRESERVE</code>. The initial entry is used in ELF extensions for <i>e_phnum</i>, <i>e_shnum</i>, and <i>e_shstrndx</i>; in other cases, each field in the initial entry is set to zero. An object file does not have sections for these special indices:</p>
<dl>
<dt><code>SHN_UNDEF</code></p>
<dd>This value marks an undefined, missing, irrelevant, or otherwise meaningless section reference.</p>
<dt><code>SHN_LORESERVE</code></p>
<dd>This value specifies the lower bound of the range of reserved indices.</p>
<dt><code>SHN_LOPROC</code>, <code>SHN_HIPROC</code></p>
<dd>Values greater in the inclusive range [<code>SHN_LOPROC</code>, <code>SHN_HIPROC</code>] are reserved for processor-specific semantics.</p>
<dt><code>SHN_ABS</code></p>
<dd>This value specifies the absolute value for the corresponding reference. For example, a symbol defined relative to section number <code>SHN_ABS</code> has an absolute value and is not affected by relocation.</p>
<dt><code>SHN_COMMON</code></p>
<dd>Symbols defined relative to this section are common symbols, such as FORTRAN COMMON or unallocated C external variables.</p>
<dt><code>SHN_HIRESERVE</code></p>
<dd>This value specifies the upper bound of the range of reserved indices. The system reserves indices between <code>SHN_LORESERVE</code> and <code>SHN_HIRESERVE</code>, inclusive. The section header table does not contain entries for the reserved indices.</dl>
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
<dt><i>sh_name</i></p>
<dd>This member specifies the name of the section. Its value is an index into the section header string table section, giving the location of a null-terminated string.</p>
<dt><i>sh_type</i></p>
<dd>This member categorizes the section&#8217;s contents and semantics.</p>
<dl>
<dd>
<dl>
<dt><code>SHT_NULL</code></p>
<dd>This value marks the section header as inactive. It does not have an associated section. Other members of the section header have undefined values.</p>
<dt><code>SHT_PROGBITS</code></p>
<dd>This section holds information defined by the program, whose format and meaning are determined solely by the program.</p>
<dt><code>SHT_SYMTAB</code></p>
<dd>This section holds a symbol table. Typically, <code>SHT_SYMTAB</code> provides symbols for link editing, though it may also be used for dynamic linking. As a complete symbol table, it may contain many symbols unnecessary for dynamic linking. An object file can also contain a <code>SHT_DYNSYM</code> section.</p>
<dt><code>SHT_STRTAB</code></p>
<dd>This section holds a string table. An object file may have multiple string table sections.</p>
<dt><code>SHT_RELA</code></p>
<dd>This section holds relocation entries with explicit addends, such as type <i>Elf32_Rela</i> for the 32-bit class of object files. An object may have multiple relocation sections.</p>
<dt><code>SHT_HASH</code></p>
<dd>This section holds a symbol hash table. An object participating in dynamic linking must contain a symbol hash table. An object file may have only one hash table.</p>
<dt><code>SHT_DYNAMIC</code></p>
<dd>This section holds information for dynamic linking. An object file may have only one dynamic section.</p>
<dt><code>SHT_NOTE</code></p>
<dd>This section holds notes (ElfN_Nhdr).</p>
<dt><code>SHT_NOBITS</code></p>
<dd>A section of this type occupies no space in the file but otherwise resembles <code>SHT_PROGBITS</code>. Although this section contains no bytes, the <i>sh_offset</i> member contains the conceptual file offset.</p>
<dt><code>SHT_REL</code></p>
<dd>This section holds relocation offsets without explicit addends, such as type <i>Elf32_Rel</i> for the 32-bit class of object files. An object file may have multiple relocation sections.</p>
<dt><code>SHT_SHLIB</code></p>
<dd>This section is reserved but has unspecified semantics.</p>
<dt><code>SHT_DYNSYM</code></p>
<dd>This section holds a minimal set of dynamic linking symbols. An object file can also contain a <code>SHT_SYMTAB</code> section.</p>
<dt><code>SHT_LOPROC</code>, <code>SHT_HIPROC</code></p>
<dd>Values in the inclusive range [<code>SHT_LOPROC</code>, <code>SHT_HIPROC</code>] are reserved for processor-specific semantics.</p>
<dt><code>SHT_LOUSER</code></p>
<dd>This value specifies the lower bound of the range of indices reserved for application programs.</p>
<dt><code>SHT_HIUSER</code></p>
<dd>This value specifies the upper bound of the range of indices reserved for application programs. Section types between <code>SHT_LOUSER</code> and <code>SHT_HIUSER</code> may be used by the application, without conflicting with current or future system-defined section types.</dl>
</dl>
<dt><i>sh_flags</i></p>
<dd>Sections support one-bit flags that describe miscellaneous attributes. If a flag bit is set in <i>sh_flags</i>, the attribute is &quot;on&quot; for the section. Otherwise, the attribute is &quot;off&quot; or does not apply. Undefined attributes are set to zero.</p>
<dl>
<dd>
<dl>
<dt><code>SHF_WRITE</code></p>
<dd>This section contains data that should be writable during process execution.</p>
<dt><code>SHF_ALLOC</code></p>
<dd>This section occupies memory during process execution. Some control sections do not reside in the memory image of an object file. This attribute is off for those sections.</p>
<dt><code>SHF_EXECINSTR</code></p>
<dd>This section contains executable machine instructions.</p>
<dt><code>SHF_MASKPROC</code></p>
<dd>All bits included in this mask are reserved for processor-specific semantics.</dl>
</dl>
<dt><i>sh_addr</i></p>
<dd>If this section appears in the memory image of a process, this member holds the address at which the section&#8217;s first byte should reside. Otherwise, the member contains zero.</p>
<dt><i>sh_offset</i></p>
<dd>This member&#8217;s value holds the byte offset from the beginning of the file to the first byte in the section. One section type, <code>SHT_NOBITS</code>, occupies no space in the file, and its <i>sh_offset</i> member locates the conceptual placement in the file.</p>
<dt><i>sh_size</i></p>
<dd>This member holds the section&#8217;s size in bytes. Unless the section type is <code>SHT_NOBITS</code>, the section occupies <i>sh_size</i> bytes in the file. A section of type <code>SHT_NOBITS</code> may have a nonzero size, but it occupies no space in the file.</p>
<dt><i>sh_link</i></p>
<dd>This member holds a section header table index link, whose interpretation depends on the section type.</p>
<dt><i>sh_info</i></p>
<dd>This member holds extra information, whose interpretation depends on the section type.</p>
<dt><i>sh_addralign</i></p>
<dd>Some sections have address alignment constraints. If a section holds a doubleword, the system must ensure doubleword alignment for the entire section. That is, the value of <i>sh_addr</i> must be congruent to zero, modulo the value of <i>sh_addralign</i>. Only zero and positive integral powers of two are allowed. The value 0 or 1 means that the section has no alignment constraints.</p>
<dt><i>sh_entsize</i></p>
<dd>Some sections hold a table of fixed-sized entries, such as a symbol table. For such a section, this member gives the size in bytes for each entry. This member contains zero if the section does not hold a table of fixed-size entries.</dl>
<p> Various sections hold program and control information:</p>
<dl>
<dt><i>.bss</i></p>
<dd>This section holds uninitialized data that contributes to the program&#8217;s memory image. By definition, the system initializes the data with zeros when the program begins to run. This section is of type <code>SHT_NOBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</p>
<dt><i>.comment</i></p>
<dd>This section holds version control information. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</p>
<dt><i>.ctors</i></p>
<dd>This section holds initialized pointers to the C++ constructor functions. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</p>
<dt><i>.data</i></p>
<dd>This section holds initialized data that contribute to the program&#8217;s memory image. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</p>
<dt><i>.data1</i></p>
<dd>This section holds initialized data that contribute to the program&#8217;s memory image. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</p>
<dt><i>.debug</i></p>
<dd>This section holds information for symbolic debugging. The contents are unspecified. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</p>
<dt><i>.dtors</i></p>
<dd>This section holds initialized pointers to the C++ destructor functions. This section is of type <code>SHT_PROGBITS</code>. The attribute types are <code>SHF_ALLOC</code> and <code>SHF_WRITE</code>.</p>
<dt><i>.dynamic</i></p>
<dd>This section holds dynamic linking information. The section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Whether the <code>SHF_WRITE</code> bit is set is processor-specific. This section is of type <code>SHT_DYNAMIC</code>. See the attributes above.</p>
<dt><i>.dynstr</i></p>
<dd>This section holds strings needed for dynamic linking, most commonly the strings that represent the names associated with symbol table entries. This section is of type <code>SHT_STRTAB</code>. The attribute type used is <code>SHF_ALLOC</code>.</p>
<dt><i>.dynsym</i></p>
<dd>This section holds the dynamic linking symbol table. This section is of type <code>SHT_DYNSYM</code>. The attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.fini</i></p>
<dd>This section holds executable instructions that contribute to the process termination code. When a program exits normally the system arranges to execute the code in this section. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</p>
<dt><i>.gnu.version</i></p>
<dd>This section holds the version symbol table, an array of <i>ElfN_Half</i> elements. This section is of type <code>SHT_GNU_versym</code>. The attribute type used is <code>SHF_ALLOC</code>.</p>
<dt><i>.gnu.version_d</i></p>
<dd>This section holds the version symbol definitions, a table of <i>ElfN_Verdef</i> structures. This section is of type <code>SHT_GNU_verdef</code>. The attribute type used is <code>SHF_ALLOC</code>.</p>
<dt><i>.gnu.version_r</i></p>
<dd>This section holds the version symbol needed elements, a table of <i>ElfN_Verneed</i> structures. This section is of type <code>SHT_GNU_versym</code>. The attribute type used is <code>SHF_ALLOC</code>.</p>
<dt><i>.got</i></p>
<dd>This section holds the global offset table. This section is of type <code>SHT_PROGBITS</code>. The attributes are processor-specific.</p>
<dt><i>.hash</i></p>
<dd>This section holds a symbol hash table. This section is of type <code>SHT_HASH</code>. The attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.init</i></p>
<dd>This section holds executable instructions that contribute to the process initialization code. When a program starts to run the system arranges to execute the code in this section before calling the main program entry point. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</p>
<dt><i>.interp</i></p>
<dd>This section holds the pathname of a program interpreter. If the file has a loadable segment that includes the section, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, that bit will be off. This section is of type <code>SHT_PROGBITS</code>.</p>
<dt><i>.line</i></p>
<dd>This section holds line number information for symbolic debugging, which describes the correspondence between the program source and the machine code. The contents are unspecified. This section is of type <code>SHT_PROGBITS</code>. No attribute types are used.</p>
<dt><i>.note</i></p>
<dd>This section holds various notes. This section is of type <code>SHT_NOTE</code>. No attribute types are used.</p>
<dt><i>.note.ABI-tag</i></p>
<dd>This section is used to declare the expected run-time ABI of the ELF image. It may include the operating system name and its run-time versions. This section is of type <code>SHT_NOTE</code>. The only attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.note.gnu.build-id</i></p>
<dd>This section is used to hold an ID that uniquely identifies the contents of the ELF image. Different files with the same build ID should contain the same executable content. See the <code>&#8211;build-id</code> option to the GNU linker (<code>ld</code> (1)) for more details. This section is of type <code>SHT_NOTE</code>. The only attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.note.GNU-stack</i></p>
<dd>This section is used in Linux object files for declaring stack attributes. This section is of type <code>SHT_PROGBITS</code>. The only attribute used is <code>SHF_EXECINSTR</code>. This indicates to the GNU linker that the object file requires an executable stack.</p>
<dt><i>.note.openbsd.ident</i></p>
<dd>OpenBSD native executables usually contain this section to identify themselves so the kernel can bypass any compatibility ELF binary emulation tests when loading the file.</p>
<dt><i>.plt</i></p>
<dd>This section holds the procedure linkage table. This section is of type <code>SHT_PROGBITS</code>. The attributes are processor-specific.</p>
<dt><i>.relNAME</i></p>
<dd>This section holds relocation information as described below. If the file has a loadable segment that includes relocation, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. By convention, &quot;NAME&quot; is supplied by the section to which the relocations apply. Thus a relocation section for <code>.text</code> normally would have the name <code>.rel.text</code>. This section is of type <code>SHT_REL</code>.</p>
<dt><i>.relaNAME</i></p>
<dd>This section holds relocation information as described below. If the file has a loadable segment that includes relocation, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. By convention, &quot;NAME&quot; is supplied by the section to which the relocations apply. Thus a relocation section for <code>.text</code> normally would have the name <code>.rela.text</code>. This section is of type <code>SHT_RELA</code>.</p>
<dt><i>.rodata</i></p>
<dd>This section holds read-only data that typically contributes to a nonwritable segment in the process image. This section is of type <code>SHT_PROGBITS</code>. The attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.rodata1</i></p>
<dd>This section holds read-only data that typically contributes to a nonwritable segment in the process image. This section is of type <code>SHT_PROGBITS</code>. The attribute used is <code>SHF_ALLOC</code>.</p>
<dt><i>.shstrtab</i></p>
<dd>This section holds section names. This section is of type <code>SHT_STRTAB</code>. No attribute types are used.</p>
<dt><i>.strtab</i></p>
<dd>This section holds strings, most commonly the strings that represent the names associated with symbol table entries. If the file has a loadable segment that includes the symbol string table, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. This section is of type <code>SHT_STRTAB</code>.</p>
<dt><i>.symtab</i></p>
<dd>This section holds a symbol table. If the file has a loadable segment that includes the symbol table, the section&#8217;s attributes will include the <code>SHF_ALLOC</code> bit. Otherwise, the bit will be off. This section is of type <code>SHT_SYMTAB</code>.</p>
<dt><i>.text</i></p>
<dd>This section holds the &quot;text&quot;, or executable instructions, of a program. This section is of type <code>SHT_PROGBITS</code>. The attributes used are <code>SHF_ALLOC</code> and <code>SHF_EXECINSTR</code>.</dl>
<h3>String and symbol tables</h3>
<p>String table sections hold null-terminated character sequences, commonly called strings. The object file uses these strings to represent symbol and section names. One references a string as an index into the string table section. The first byte, which is index zero, is defined to hold a null byte (&#8216;
