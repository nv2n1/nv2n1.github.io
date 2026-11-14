---
title: "yasm_arch(7)"
name: "yasm_arch"
section: "7"
letter: "y"
url: "/docs/linux/man/7-yasm_arch/"
description: "yasm_arch – Yasm Supported Target Architectures"
---

<p>yasm_arch &#8211; Yasm Supported Target Architectures</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>yasm</code> <code>-a&nbsp;<wbr></code><i>arch</i> [<code>-m&nbsp;<wbr></code><i>machine</i>] <i>&#8230;</i></dl>
<h2>Description</h2>
<dd>The standard Yasm distribution includes a number of modules for different target architectures. Each target architecture can support one or more machine architectures. </p>
<p> The architecture and machine are selected on the <code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1) command line by use of the <code>-a </code><i>arch</i> and <code>-m </code><i>machine</i> command line options, respectively. </p>
<p> The machine architecture may also automatically be selected by certain object formats. For example, the &#8220;elf32&#8221; object format selects the &#8220;x86&#8221; machine architecture by default, while the &#8220;elf64&#8221; object format selects the &#8220;amd64&#8221; machine architecture by default.</p>
<h2>X86 Architecture</h2>
<p>The &#8220;x86&#8221; architecture supports the IA-32 instruction set and derivatives and the AMD64 instruction set. It consists of two machines: &#8220;x86&#8221; (for the IA-32 and derivatives) and &#8220;amd64&#8221; (for the AMD64 and derivatives). The default machine for the &#8220;x86&#8221; architecture is the &#8220;x86&#8221; machine.</p>
<h3>BITS Setting</h3>
<p>The x86 architecture BITS setting specifies to Yasm the processor mode in which the generated code is intended to execute. x86 processors can run in three different major execution modes: 16-bit, 32-bit, and on AMD64-supporting processors, 64-bit. As the x86 instruction set contains portions whose function is execution-mode dependent (such as operand-size and address-size override prefixes), Yasm cannot assemble x86 instructions correctly unless it is told by the user in what processor mode the code will execute. </p>
<p> The BITS setting can be changed in a variety of ways. When using the NASM-compatible parser, the BITS setting can be changed directly via the use of the <code>BITS xx</code> assembler directive. The default BITS setting is determined by the object format in use.</p>
<h3>BITS 64 Extensions</h3>
<p>The AMD64 architecture is a new 64-bit architecture developed by AMD, based on the 32-bit x86 architecture. It extends the original x86 architecture by doubling the number of general purpose and SIMD registers, extending the arithmetic operations and address space to 64 bits, as well as other features. </p>
<p> Recently, Intel has introduced an essentially identical version of AMD64 called EM64T. </p>
<p> When an AMD64-supporting processor is executing in 64-bit mode, a number of additional extensions are available, including extra general purpose registers, extra SSE2 registers, and RIP-relative addressing. </p>
<p> Yasm extends the base NASM syntax to support AMD64 as follows. To enable assembly of instructions for the 64-bit mode of AMD64 processors, use the directive <code>BITS 64</code>. As with NASM&#8217;s BITS directive, this does not change the format of the output object file to 64 bits; it only changes the assembler mode to assume that the instructions being assembled will be run in 64-bit mode. To specify an AMD64 object file, use <code>-m amd64</code> on the Yasm command line, or explicitly target a 64-bit object format such as <code>-f win64</code> or <code>-f elf64</code>. </p>
<p> <font SIZE="+1"> <code>Register Changes</code></p>
<dl>
<dd>The additional 64-bit general purpose registers are named r8-r15. There are also 8-bit (rXb), 16-bit (rXw), and 32-bit (rXd) subregisters that map to the least significant 8, 16, or 32 bits of the 64-bit register. The original 8 general purpose registers have also been extended to 64-bits: eax, edx, ecx, ebx, esi, edi, esp, and ebp have new 64-bit versions called rax, rdx, rcx, rbx, rsi, rdi, rsp, and rbp respectively. The old 32-bit registers map to the least significant bits of the new 64-bit registers. </p>
<p> New 8-bit registers are also available that map to the 8 least significant bits of rsi, rdi, rsp, and rbp. These are called sil, dil, spl, and bpl respectively. Unfortunately, due to the way instructions are encoded, these new 8-bit registers are encoded the same as the old 8-bit registers ah, dh, ch, and bh. The processor tells which is being used by the presence of the new REX prefix that is used to specify the other extended registers. This means it is illegal to mix the use of ah, dh, ch, and bh with an instruction that requires the REX prefix for other reasons. For instance: </p>
<dl>
<dd></font></p>
<pre>add ah, [r10]</pre>
</dl>
<p> (NASM syntax) is not a legal instruction because the use of r10 requires a REX prefix, making it impossible to use ah. </p>
<p> In 64-bit mode, an additional 8 SSE2 registers are also available. These are named xmm8-xmm15.</dl>
<p> <font SIZE="+1"> <code>64 Bit Instructions</code></p>
<dl>
<dd>By default, most operations in 64-bit mode remain 32-bit; operations that are 64-bit usually require a REX prefix (one bit in the REX prefix determines whether an operation is 64-bit or 32-bit). Thus, essentially all 32-bit instructions have a 64-bit version, and the 64-bit versions of instructions can use extended registers &#8220;for free&#8221; (as the REX prefix is already present). Examples in NASM syntax: </p>
<dl>
<dd></font></p>
<pre>mov eax, 1 ; 32-bit instruction</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, 1 ; 64-bit instruction</pre>
</dl>
<p> Instructions that modify the stack (push, pop, call, ret, enter, and leave) are implicitly 64-bit. Their 32-bit counterparts are not available, but their 16-bit counterparts are. Examples in NASM syntax: </p>
<dl>
<dd>
<pre>push eax ; illegal instruction</pre>
</dl>
<dl>
<dd>
<pre>push rbx ; 1-byte instruction</pre>
</dl>
<dl>
<dd>
<pre>push r11 ; 2-byte instruction with REX prefix</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Implicit Zero Extension</code></p>
<dl>
<dd>Results of 32-bit operations are implicitly zero-extended to the upper 32 bits of the corresponding 64-bit register. 16 and 8 bit operations, on the other hand, do not affect upper bits of the register (just as in 32-bit and 16-bit modes). This can be used to generate smaller code in some instances. Examples in NASM syntax: </p>
<dl>
<dd></font></p>
<pre>mov ecx, 1 ; 1 byte shorter than mov rcx, 1</pre>
</dl>
<dl>
<dd>
<pre>and edx, 3 ; equivalent to and rdx, 3</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Immediates</code></p>
<dl>
<dd>For most instructions in 64-bit mode, immediate values remain 32 bits; their value is sign-extended into the upper 32 bits of the target register prior to being used. The exception is the mov instruction, which can take a 64-bit immediate when the destination is a 64-bit register. Examples in NASM syntax: </p>
<dl>
<dd></font></p>
<pre>add rax, 1 ; optimized down to signed 8-bit</pre>
</dl>
<dl>
<dd>
<pre>add rax, dword 1 ; force size to 32-bit</pre>
</dl>
<dl>
<dd>
<pre>add rax, 0xffffffff ; sign-extended 32-bit</pre>
</dl>
<dl>
<dd>
<pre>add rax, -1 ; same as above</pre>
</dl>
<dl>
<dd>
<pre>add rax, 0xffffffffffffffff ; truncated to 32-bit (warning)</pre>
</dl>
<dl>
<dd>
<pre>mov eax, 1 ; 5 byte</pre>
</dl>
<dl>
<dd>
<pre>mov rax, 1 ; 5 byte (optimized to signed 32-bit)</pre>
</dl>
<dl>
<dd>
<pre>mov rax, qword 1 ; 10 byte (forced 64-bit)</pre>
</dl>
<dl>
<dd>
<pre>mov rbx, 0x1234567890abcdef ; 10 byte</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, 0xffffffff ; 10 byte (does not fit in signed 32-bit)</pre>
</dl>
<dl>
<dd>
<pre>mov ecx, -1 ; 5 byte, equivalent to above</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, sym ; 5 byte, 32-bit size default for symbols</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, qword sym ; 10 byte, override default size</pre>
</dl>
<p> The handling of mov reg64, unsized immediate is different between YASM and NASM 2.x; YASM follows the above behavior, while NASM 2.x does the following: </p>
<dl>
<dd>
<pre>add rax, 0xffffffff ; sign-extended 32-bit immediate</pre>
</dl>
<dl>
<dd>
<pre>add rax, -1 ; same as above</pre>
</dl>
<dl>
<dd>
<pre>add rax, 0xffffffffffffffff ; truncated 32-bit (warning)</pre>
</dl>
<dl>
<dd>
<pre>add rax, sym ; sign-extended 32-bit immediate</pre>
</dl>
<dl>
<dd>
<pre>mov eax, 1 ; 5 byte (32-bit immediate)</pre>
</dl>
<dl>
<dd>
<pre>mov rax, 1 ; 10 byte (64-bit immediate)</pre>
</dl>
<dl>
<dd>
<pre>mov rbx, 0x1234567890abcdef ; 10 byte instruction</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, 0xffffffff ; 10 byte instruction</pre>
</dl>
<dl>
<dd>
<pre>mov ecx, -1 ; 5 byte, equivalent to above</pre>
</dl>
<dl>
<dd>
<pre>mov ecx, sym ; 5 byte (32-bit immediate)</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, sym ; 10 byte instruction</pre>
</dl>
<dl>
<dd>
<pre>mov rcx, qword sym ; 10 byte (64-bit immediate)</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Displacements</code></p>
<dl>
<dd>Just like immediates, displacements, for the most part, remain 32 bits and are sign extended prior to use. Again, the exception is one restricted form of the mov instruction: between the al/ax/eax/rax register and a 64-bit absolute address (no registers allowed in the effective address). In NASM syntax, use of the 64-bit absolute form requires <code>[qword]</code>. Examples in NASM syntax: </p>
<dl>
<dd></font></p>
<pre>mov eax, [1] ; 32 bit, with sign extension</pre>
</dl>
<dl>
<dd>
<pre>mov al, [rax-1] ; 32 bit, with sign extension</pre>
</dl>
<dl>
<dd>
<pre>mov al, [qword 0x1122334455667788] ; 64-bit absolute</pre>
</dl>
<dl>
<dd>
<pre>mov al, [0x1122334455667788] ; truncated to 32-bit (warning)</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>RIP Relative Addressing</code></p>
<dl>
<dd>In 64-bit mode, a new form of effective addressing is available to make it easier to write position-independent code. Any memory reference may be made RIP relative (RIP is the instruction pointer register, which contains the address of the location immediately following the current instruction). </p>
<p> In NASM syntax, there are two ways to specify RIP-relative addressing: </p>
<dl>
<dd></font></p>
<pre>mov dword [rip+10], 1</pre>
</dl>
<p> stores the value 1 ten bytes after the end of the instruction. <code>10</code> can also be a symbolic constant, and will be treated the same way. On the other hand, </p>
<dl>
<dd>
<pre>mov dword [symb wrt rip], 1</pre>
</dl>
<p> stores the value 1 into the address of symbol <code>symb</code>. This is distinctly different than the behavior of: </p>
<dl>
<dd>
<pre>mov dword [symb+rip], 1</pre>
</dl>
<p> which takes the address of the end of the instruction, adds the address of <code>symb</code> to it, then stores the value 1 there. If <code>symb</code> is a variable, this will <i>not</i> store the value 1 into the <code>symb</code> variable! </p>
<p> Yasm also supports the following syntax for RIP-relative addressing: </p>
<dl>
<dd>
<pre>mov [rel sym], rax ; RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [abs sym], rax ; not RIP-relative</pre>
</dl>
<p> The behavior of: </p>
<dl>
<dd>
<pre>mov [sym], rax</pre>
</dl>
<p> Depends on a mode set by the DEFAULT directive, as follows. The default mode is always &quot;abs&quot;, and in &quot;rel&quot; mode, use of registers, an fs or gs segment override, or an explicit &quot;abs&quot; override will result in a non-RIP-relative effective address. </p>
<dl>
<dd>
<pre>default rel</pre>
</dl>
<dl>
<dd>
<pre>mov [sym], rbx ; RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [abs sym], rbx ; not RIP-relative (explicit override)</pre>
</dl>
<dl>
<dd>
<pre>mov [rbx+1], rbx ; not RIP-relative (register use)</pre>
</dl>
<dl>
<dd>
<pre>mov [fs:sym], rbx ; not RIP-relative (fs or gs use)</pre>
</dl>
<dl>
<dd>
<pre>mov [ds:sym], rbx ; RIP-relative (segment, but not fs or gs)</pre>
</dl>
<dl>
<dd>
<pre>mov [rel sym], rbx ; RIP-relative (redundant override)</pre>
</dl>
<dl>
<dd>
<pre>default abs</pre>
</dl>
<dl>
<dd>
<pre>mov [sym], rbx ; not RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [abs sym], rbx ; not RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [rbx+1], rbx ; not RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [fs:sym], rbx ; not RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [ds:sym], rbx ; not RIP-relative</pre>
</dl>
<dl>
<dd>
<pre>mov [rel sym], rbx ; RIP-relative (explicit override)</pre>
</dl>
</dl>
<p> <font SIZE="+1"> <code>Memory references</code></p>
<dl>
<dd>Usually the size of a memory reference can be deduced by which registers you&#8217;re moving&#8211;for example, &quot;mov [rax],ecx&quot; is a 32-bit move, because ecx is 32 bits. YASM currently gives the non-obvious &quot;invalid combination of opcode and operands&quot; error if it can&#8217;t figure out how much memory you&#8217;re moving. The fix in this case is to add a memory size specifier: qword, dword, word, or byte. </p>
<p> Here&#8217;s a 64-bit memory move, which sets 8 bytes starting at rax: </p>
<dl>
<dd></font></p>
<pre>mov qword [rax], 1</pre>
</dl>
<p> Here&#8217;s a 32-bit memory move, which sets 4 bytes: </p>
<dl>
<dd>
<pre>mov dword [rax], 1</pre>
</dl>
<p> Here&#8217;s a 16-bit memory move, which sets 2 bytes: </p>
<dl>
<dd>
<pre>mov word [rax], 1</pre>
</dl>
<p> Here&#8217;s an 8-bit memory move, which sets 1 byte: </p>
<dl>
<dd>
<pre>mov byte [rax], 1</pre>
</dl>
</dl>
<h2>Lc3B Architecture</h2>
<p>The &#8220;lc3b&#8221; architecture supports the LC-3b ISA as used in the ECE 312 (now ECE 411) course at the University of Illinois, Urbana-Champaign, as well as other university courses. See m[blue]<code><a rel="nofollow" href="http://courses.ece.uiuc.edu/ece411/">http://courses.ece.uiuc.edu/ece411/</a></code>m[] for more details and example code. The &#8220;lc3b&#8221; architecture consists of only one machine: &#8220;lc3b&#8221;.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-yasm/">yasm</a></code>(1)</p>
<h2>Bugs</h2>
<p>When using the &#8220;x86&#8221; architecture, it is overly easy to generate AMD64 code (using the <code>BITS 64</code> directive) and generate a 32-bit object file (by failing to specify <code>-m amd64</code> on the command line or selecting a 64-bit object format). Similarly, specifying <code>-m amd64</code> does not default the BITS setting to 64. An easy way to avoid this is by directly specifying a 64-bit object format such as <code>-f elf64</code>.</p>
<h2>Author</h2>
<p><code>Peter Johnson</code> &lt;peter [at] tortall.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2005, 2006, 2007 Peter Johnson</p>
