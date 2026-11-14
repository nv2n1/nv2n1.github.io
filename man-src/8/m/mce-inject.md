---
title: "mce-inject(8)"
name: "mce-inject"
section: "8"
letter: "m"
url: "/docs/linux/man/8-mce-inject/"
---

mce-inject - Inject machine checks into x86 kernel for testing

<h2>Synopsis</h2>

mce-inject mce-file1 ... 
 mce-inject &lt; mce-file

<h2>Description</h2>

mce-inject allows to inject machine checks in a running x86 Linux kernel. machine checks are internal CPU errors. This tool is intended to test the machine check handling code. The injection only happens on the software level and does not simulate full machine check handling on the platform level. The machine checks to be injected are described in a input language similar to the format the kernel outputs on a panic message (with a few extension). In general you should be able to pipe in a panic message to inject that mce. See the IA32 SDM Vol3a chapter 14 for the details on fields. They correspond to the machine check MSRs of the standard IA32 Machine check architecture described there.

<h2>Input Language</h2>

These generally represent the similarly CPU MSRs, with some metadata on where to inject the exception. Please see the IA software developers Manual for more details. 

 The machine check always starts with <i>MCE</i> or <i>CPU number|broadcast [bank-number]</i> Machine check is injected on CPU xx or broadcasted to all CPUs 

 <i>BANK bank-number</i> Machine check bank to inject on. 

 <i>STATUS {number|fatal|corrected|uncorrected|pcc|uc|val|en|over|ar|ucna|srao|srar|s}</i> 

 The symbols generally represent hardware register bits, as documented in the Intel software developer's manual. When multiple are listed they are ored together. 

 <i>MCGSTATUS {number|mcip|ripv|eipv}</i> 

 The symbols generally represent hardware register bits, as documented in the Intel software developer's manual. When multiple are listed they are ored together. 

 <i>ADDR number</i> 

 <i>RIP number</i> <i>RIP number:&lt;number&gt;{string}</i> <i>RIP number:number</i> 

 <i>MISC number</i> 

 <i>CPU number : machine check exception : number BANK number : number</i> parsed for compatibility with kernel output. Use explicit statements 

 <i>TSC number</i> TSC state injected in machine check 

 <i>NOBROADCAST</i> Don't broadcast exceptions to all CPUs. Default is to broadcast UC 

 <i>IRQBROADCAST</i> Broadcast IRQ to all CPUs that not getting error injection. 

 <i>NMIBROADCAST</i> Broadcast NMI to all CPUs that not getting error injection. 

 <i>IN_IRQ</i> MCE should be injected in interrupt context 

 <i>IN_PROC</i> MCE injected in process context. 

 <i>HOLD</i> Don't inject MCE immediately but hold it for later injection. This is useful for testing injection on multiple CPUs in parallel 

 <i>SOCKETID number</i> Socketid. Ignored by kernel on injection. 

 <i>MCGCAP number</i> Machine check capabilities register value. Currently ignored by kernel on injection. 

 <i>POLL</i> Inject in machine check poller code. 

 <i>EXCP</i> Inject as machine check exception. 

 <i>APICID number</i> APIC ID of CPU. Ignored by kernel on injection. 

 A list of symbols ors the symbols together. 

 

 Multiple fields can be on a line. number can be hex/octal/decimal in the usual C format. Multiple machine checks can be in a single file, each new one starts with &quot;CPU&quot; or &quot;MCE&quot;. For all missing fields reasonable default values are filled in (hopefully) Comments start with # until the end of the line The keywords are case-insensitive.

<h2>Requirements</h2>

mce-inject to run as root. /dev/mcelog has to exist. The kernels needs to have machine check injection ( <i>CONFIG_X86_MCE_INJECT</i> ) enabled and if modular the mce-inject module loaded. This option is available in Linux 2.6.31 or later.

<h2>Notes</h2>

The <i>mce-test</i> package has a lot of input file examples.

<h2>See Also</h2>

Intel 64 and IA32 Architectures Software Developer's manual, Volume 3, System programming guide Parts 1 and 2. Machine checks are described in Chapter 14 in Part1 and in Append ix E in Part2. Datasheet of your CPU. 
