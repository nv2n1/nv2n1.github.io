---
title: "tc-bpf(8)"
name: "tc-bpf"
section: "8"
letter: "t"
url: "/docs/linux/man/8-tc-bpf/"
description: "BPF – BPF programmable classifier and actions for ingress/egress queueing disciplines"
---

<p>BPF &#8211; BPF programmable classifier and actions for ingress/egress queueing disciplines</p>
<h2>Synopsis</h2>
<h3>eBPF classifier (filter) or action:</h3>
<p><code>tc filter &#8230; bpf</code> [ <code>object-file</code> OBJ_FILE ] [ <code>section</code> CLS_NAME ] [ <code>export</code> UDS_FILE ] [ <code>verbose</code> ] [ <code>direct-action</code> | <code>da</code> ] [ <code>skip_hw</code> | <code>skip_sw</code> ] [ <code>police</code> POLICE_SPEC ] [ <code>action</code> ACTION_SPEC ] [ <code>classid</code> CLASSID ]<br />
 <code>tc action &#8230; bpf</code> [ <code>object-file</code> OBJ_FILE ] [ <code>section</code> CLS_NAME ] [ <code>export</code> UDS_FILE ] [ <code>verbose</code> ]</p>
<h3>cBPF classifier (filter) or action:</h3>
<p><code>tc filter &#8230; bpf</code> [ <code>bytecode-file</code> BPF_FILE | <code>bytecode</code> BPF_BYTECODE ] [ <code>police</code> POLICE_SPEC ] [ <code>action</code> ACTION_SPEC ] [ <code>classid</code> CLASSID ]<br />
 <code>tc action &#8230; bpf</code> [ <code>bytecode-file</code> BPF_FILE | <code>bytecode</code> BPF_BYTECODE ] </p>
<h2>Description</h2>
<p>Extended Berkeley Packet Filter ( <code>eBPF</code> ) and classic Berkeley Packet Filter (originally known as BPF, for better distinction referred to as <code>cBPF</code> here) are both available as a fully programmable and highly efficient classifier and actions. They both offer a minimal instruction set for implementing small programs which can safely be loaded into the kernel and thus executed in a tiny virtual machine from kernel space. An in-kernel verifier guarantees that a specified program always terminates and neither crashes nor leaks data from the kernel. In Linux, it&#8217;s generally considered that eBPF is the successor of cBPF. The kernel internally transforms cBPF expressions into eBPF expressions and executes the latter. Execution of them can be performed in an interpreter or at setup time, they can be just-in-time compiled (JIT&#8217;ed) to run as native machine code. Currently, the eBPF JIT compiler is available for the following architectures:</p>
<dl>
<dt>*</p>
<dd>x86_64 (since Linux 3.18)</p>
<dt>*</p>
<dd>arm64 (since Linux 3.18)</p>
<dt>*</p>
<dd>s390 (since Linux 4.1)</p>
<dt>*</p>
<dd>ppc64 (since Linux 4.8)</p>
<dt>*</p>
<dd>sparc64 (since Linux 4.12)</p>
<dt>*</p>
<dd>mips64 (since Linux 4.13)</p>
<dt>*</p>
<dd>arm32 (since Linux 4.14)</p>
<dt>*</p>
<dd>x86_32 (since Linux 4.18)</dl>
<p> Whereas the following architectures have cBPF, but did not (yet) switch to eBPF JIT support:</p>
<dl>
<dt>*</p>
<dd>ppc32</p>
<dt>*</p>
<dd>sparc32</p>
<dt>*</p>
<dd>mips32</dl>
<p> eBPF&#8217;s instruction set has similar underlying principles as the cBPF instruction set, it however is modelled closer to the underlying architecture to better mimic native instruction sets with the aim to achieve a better run-time performance. It is designed to be JIT&#8217;ed with a one to one mapping, which can also open up the possibility for compilers to generate optimized eBPF code through an eBPF backend that performs almost as fast as natively compiled code. Given that LLVM provides such an eBPF backend, eBPF programs can therefore easily be programmed in a subset of the C language. Other than that, eBPF infrastructure also comes with a construct called &quot;maps&quot;. eBPF maps are key/value stores that are shared between multiple eBPF programs, but also between eBPF programs and user space applications. For the traffic control subsystem, classifier and actions that can be attached to ingress and egress qdiscs can be written in eBPF or cBPF. The advantage over other classifier and actions is that eBPF/cBPF provides the generic framework, while users can implement their highly specialized use cases efficiently. This means that the classifier or action written that way will not suffer from feature bloat, and can therefore execute its task highly efficient. It allows for non-linear classification and even merging the action part into the classification. Combined with efficient eBPF map data structures, user space can push new policies like classids into the kernel without reloading a classifier, or it can gather statistics that are pushed into one map and use another one for dynamically load balancing traffic based on the determined load, just to provide a few examples. </p>
<h2>Parameters</h2>
<h3>object-file</h3>
<p>points to an object file that has an executable and linkable format (ELF) and contains eBPF opcodes and eBPF map definitions. The LLVM compiler infrastructure with <code><a href="/docs/linux/man/1-clang/">clang</a>(1)</code> as a C language front end is one project that supports emitting eBPF object files that can be passed to the eBPF classifier (more details in the <code>EXAMPLES</code> section). This option is mandatory when an eBPF classifier or action is to be loaded.</p>
<h3>section</h3>
<p>is the name of the ELF section from the object file, where the eBPF classifier or action resides. By default the section name for the classifier is called &quot;classifier&quot;, and for the action &quot;action&quot;. Given that a single object file can contain multiple classifier and actions, the corresponding section name needs to be specified, if it differs from the defaults.</p>
<h3>export</h3>
<p>points to a Unix domain socket file. In case the eBPF object file also contains a section named &quot;maps&quot; with eBPF map specifications, then the map file descriptors can be handed off via the Unix domain socket to an eBPF &quot;agent&quot; herding all descriptors after tc lifetime. This can be some third party application implementing the IPC counterpart for the import, that uses them for calling into <code><a href="/docs/linux/man/2-bpf/">bpf</a>(2)</code> system call to read out or update eBPF map data from user space, for example, for monitoring purposes or to push down new policies.</p>
<h3>verbose</h3>
<p>if set, it will dump the eBPF verifier output, even if loading the eBPF program was successful. By default, only on error, the verifier log is being emitted to the user.</p>
<h3>direct-action | da</h3>
<p>instructs eBPF classifier to not invoke external TC actions, instead use the TC actions return codes (<code>TC_ACT_OK</code>, <code>TC_ACT_SHOT</code> etc.) for classifiers.</p>
<h3>skip_hw | skip_sw</h3>
<p>hardware offload control flags. By default TC will try to offload filters to hardware if possible. <code>skip_hw</code> explicitly disables the attempt to offload. <code>skip_sw</code> forces the offload and disables running the eBPF program in the kernel. If hardware offload is not possible and this flag was set kernel will report an error and filter will not be installed at all.</p>
<h3>police</h3>
<p>is an optional parameter for an eBPF/cBPF classifier that specifies a police in <code><a href="/docs/linux/man/1-tc/">tc</a>(1)</code> which is attached to the classifier, for example, on an ingress qdisc.</p>
<h3>action</h3>
<p>is an optional parameter for an eBPF/cBPF classifier that specifies a subsequent action in <code><a href="/docs/linux/man/1-tc/">tc</a>(1)</code> which is attached to a classifier.</p>
<h3>classid</h3>
<h3>flowid</h3>
<p>provides the default traffic control class identifier for this eBPF/cBPF classifier. The default class identifier can also be overwritten by the return code of the eBPF/cBPF program. A default return code of <code>-1</code> specifies the here provided default class identifier to be used. A return code of the eBPF/cBPF program of 0 implies that no match took place, and a return code other than these two will override the default classid. This allows for efficient, non-linear classification with only a single eBPF/cBPF program as opposed to having multiple individual programs for various class identifiers which would need to reparse packet contents.</p>
<h3>bytecode</h3>
<p>is being used for loading cBPF classifier and actions only. The cBPF bytecode is directly passed as a text string in the form of <code>&#8216;s,c t f k,c t f k,c t f k,&#8230;&#8217;</code> , where <code>s</code> denotes the number of subsequent 4-tuples. One such 4-tuple consists of <code>c t f k</code> decimals, where <code>c</code> represents the cBPF opcode, <code>t</code> the jump true offset target, <code>f</code> the jump false offset target and <code>k</code> the immediate constant/literal. There are various tools that generate code in this loadable format, for example, <code>bpf_asm</code> that ships with the Linux kernel source tree under <code>tools/net/</code> , so it is certainly not expected to hack this by hand. The <code>bytecode</code> or <code>bytecode-file</code> option is mandatory when a cBPF classifier or action is to be loaded.</p>
<h3>bytecode-file</h3>
<p>also being used to load a cBPF classifier or action. It&#8217;s effectively the same as <code>bytecode</code> only that the cBPF bytecode is not passed directly via command line, but rather resides in a text file.</p>
<h2>Examples</h2>
<h3>eBPF TOOLING</h3>
<p>A full blown example including eBPF agent code can be found inside the iproute2 source package under: <code>examples/bpf/</code> As prerequisites, the kernel needs to have the eBPF system call namely <code><a href="/docs/linux/man/2-bpf/">bpf</a>(2)</code> enabled and ships with <code>cls_bpf</code> and <code>act_bpf</code> kernel modules for the traffic control subsystem. To enable eBPF/eBPF JIT support, depending which of the two the given architecture supports: <code>echo 1 &gt; /proc/sys/net/core/bpf_jit_enable</code> A given restricted C file can be compiled via LLVM as: <code>clang -O2 -emit-llvm -c bpf.c -o &#8211; | llc -march=bpf -filetype=obj -o bpf.o</code> The compiler invocation might still simplify in future, so for now, it&#8217;s quite handy to alias this construct in one way or another, for example: </p>
<pre>__bcc() {
 clang -O2 -emit-llvm -c $1 -o - | \
 llc -march=bpf -filetype=obj -o &quot;`basename $1 .c`.o&quot;
}
alias bcc=__bcc</pre>
<p>A minimal, stand-alone unit, which matches on all traffic with the default classid (return code of -1) looks like: </p>
<pre><code>#include &lt;pcap.h&gt;
#include &lt;stdio.h&gt;

int main(int argc, char **argv)
{
    struct bpf_program prog;
    struct bpf_insn *ins;
    int i, ret, dlt = DLT_RAW;

    if (argc &lt; 2 || argc &gt; 3)
        return 1;
    if (argc == 3) {
        dlt = pcap_datalink_name_to_val(argv[1]);
        if (dlt == -1)
            return 1;
    }

    ret = pcap_compile_nopcap(-1, dlt, &amp;prog, argv[argc - 1],
                              1, PCAP_NETMASK_UNKNOWN);
    if (ret)
        return 1;

    printf(&quot;%d,&quot;, prog.bf_len);
    ins = prog.bf_insns;

    for (i = 0; i &lt; prog.bf_len - 1; ++ins, ++i)
        printf(&quot;%u %u %u %u,&quot;, ins-&gt;code,
               ins-&gt;jt, ins-&gt;jf, ins-&gt;k);
    printf(&quot;%u %u %u %u&quot;,
           ins-&gt;code, ins-&gt;jt, ins-&gt;jf, ins-&gt;k);

    pcap_freecode(&amp;prog);
    return 0;
}</code></pre>
<p> More examples can be found further below in subsection <code>eBPF PROGRAMMING</code> as focus here will be on tooling. There can be various other sections, for example, also for actions. Thus, an object file in eBPF can contain multiple entrance points. Always a specific entrance point, however, must be specified when configuring with tc. A license must be part of the restricted C code and the license string syntax is the same as with Linux kernel modules. The kernel reserves its right that some eBPF helper functions can be restricted to GPL compatible licenses only, and thus may reject a program from loading into the kernel when such a license mismatch occurs. The resulting object file from the compilation can be inspected with the usual set of tools that also operate on normal object files, for example <code><a href="/docs/linux/man/1-objdump/">objdump</a>(1)</code> for inspecting ELF section headers: </p>
<pre>objdump -h bpf.o
[...]
3 classifier 000007f8 0000000000000000 0000000000000000 00000040 2**3
 CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
4 action-mark 00000088 0000000000000000 0000000000000000 00000838 2**3
 CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
5 action-rand 00000098 0000000000000000 0000000000000000 000008c0 2**3
 CONTENTS, ALLOC, LOAD, RELOC, READONLY, CODE
6 maps 00000030 0000000000000000 0000000000000000 00000958 2**2
 CONTENTS, ALLOC, LOAD, DATA
7 license 00000004 0000000000000000 0000000000000000 00000988 2**0
 CONTENTS, ALLOC, LOAD, DATA
[...]</pre>
<p>Adding an eBPF classifier from an object file that contains a classifier in the default ELF section is trivial (note that instead of &quot;object-file&quot; also shortcuts such as &quot;obj&quot; can be used): <code>bcc bpf.c</code><br />
 <code>tc filter add dev em1 parent 1: bpf obj bpf.o flowid 1:1</code> In case the classifier resides in ELF section &quot;mycls&quot;, then that same command needs to be invoked as: <code>tc filter add dev em1 parent 1: bpf obj bpf.o sec mycls flowid 1:1</code> Dumping the classifier configuration will tell the location of the classifier, in other words that it&#8217;s from object file &quot;bpf.o&quot; under section &quot;mycls&quot;: <code>tc filter show dev em1</code><br />
 <code>filter parent 1: protocol all pref 49152 bpf</code><br />
 <code>filter parent 1: protocol all pref 49152 bpf handle 0x1 flowid 1:1 bpf.o:[mycls]</code> The same program can also be installed on ingress qdisc side as opposed to egress &#8230; <code>tc qdisc add dev em1 handle ffff: ingress</code><br />
 <code>tc filter add dev em1 parent ffff: bpf obj bpf.o sec mycls flowid ffff:1</code> &#8230; and again dumped from there: <code>tc filter show dev em1 parent ffff:</code><br />
 <code>filter protocol all pref 49152 bpf</code><br />
 <code>filter protocol all pref 49152 bpf handle 0x1 flowid ffff:1 bpf.o:[mycls]</code> Attaching a classifier and action on ingress has the restriction that it doesn&#8217;t have an actual underlying queueing discipline. What ingress can do is to classify, mangle, redirect or drop packets. When queueing is required on ingress side, then ingress must redirect packets to the <code>ifb</code> device, otherwise policing can be used. Moreover, ingress can be used to have an early drop point of unwanted packets before they hit upper layers of the networking stack, perform network accounting with eBPF maps that could be shared with egress, or have an early mangle and/or redirection point to different networking devices. Multiple eBPF actions and classifier can be placed into a single object file within various sections. In that case, non-default section names must be provided, which is the case for both actions in this example: <code>tc filter add dev em1 parent 1: bpf obj bpf.o flowid 1:1 \</code><br />
 <code>action bpf obj bpf.o sec action-mark \</code><br />
 <code>action bpf obj bpf.o sec action-rand ok</code> The advantage of this is that the classifier and the two actions can then share eBPF maps with each other, if implemented in the programs. In order to access eBPF maps from user space beyond <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> setup lifetime, the ownership can be transferred to an eBPF agent via Unix domain sockets. There are two possibilities for implementing this: <code>1)</code> implementation of an own eBPF agent that takes care of setting up the Unix domain socket and implementing the protocol that <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> dictates. A code example of this can be found inside the iproute2 source package under: <code>examples/bpf/</code> <code>2)</code> use <code>tc exec</code> for transferring the eBPF map file descriptors through a Unix domain socket, and spawning an application such as <code><a href="/docs/linux/man/1-sh/">sh</a>(1)</code> . This approach&#8217;s advantage is that tc will place the file descriptors into the environment and thus make them available just like stdin, stdout, stderr file descriptors, meaning, in case user applications run from within this fd-owner shell, they can terminate and restart without losing eBPF maps file descriptors. Example invocation with the previous classifier and action mixture: <code>tc exec bpf imp /tmp/bpf</code><br />
 <code>tc filter add dev em1 parent 1: bpf obj bpf.o exp /tmp/bpf flowid 1:1 \</code><br />
 <code>action bpf obj bpf.o sec action-mark \</code><br />
 <code>action bpf obj bpf.o sec action-rand ok</code> Assuming that eBPF maps are shared with classifier and actions, it&#8217;s enough to export them once, for example, from within the classifier or action command. tc will setup all eBPF map file descriptors at the time when the object file is first parsed. When a shell has been spawned, the environment will have a couple of eBPF related variables. BPF_NUM_MAPS provides the total number of maps that have been transferred over the Unix domain socket. BPF_MAP&lt;X&gt;&#8217;s value is the file descriptor number that can be accessed in eBPF agent applications, in other words, it can directly be used as the file descriptor value for the <code><a href="/docs/linux/man/2-bpf/">bpf</a>(2)</code> system call to retrieve or alter eBPF map values. &lt;X&gt; denotes the identifier of the eBPF map. It corresponds to the <code>id</code> member of <code>struct bpf_elf_map</code> from the tc eBPF map specification. The environment in this example looks as follows: </p>
<pre>sh# env | grep BPF
 BPF_NUM_MAPS=3
 BPF_MAP1=6
 BPF_MAP0=5
 BPF_MAP2=7
sh# ls -la /proc/self/fd
 [...]
 lrwx------. 1 root root 64 Apr 14 16:46 5 -&gt; anon_inode:bpf-map
 lrwx------. 1 root root 64 Apr 14 16:46 6 -&gt; anon_inode:bpf-map
 lrwx------. 1 root root 64 Apr 14 16:46 7 -&gt; anon_inode:bpf-map
sh# my_bpf_agent</pre>
<p>eBPF agents are very useful in that they can prepopulate eBPF maps from user space, monitor statistics via maps and based on that feedback, for example, rewrite classids in eBPF map values during runtime. Given that eBPF agents are implemented as normal applications, they can also dynamically receive traffic control policies from external controllers and thus push them down into eBPF maps to dynamically adapt to network conditions. Moreover, eBPF maps can also be shared with other eBPF program types (e.g. tracing), thus very powerful combination can therefore be implemented.</p>
<h3>eBPF PROGRAMMING</h3>
<p>eBPF classifier and actions are being implemented in restricted C syntax (in future, there could additionally be new language frontends supported). The header file <code>linux/bpf.h</code> provides eBPF helper functions that can be called from an eBPF program. This man page will only provide two minimal, stand-alone examples, have a look at <code>examples/bpf</code> from the iproute2 source package for a fully fledged flow dissector example to better demonstrate some of the possibilities with eBPF. Supported 32 bit classifier return codes from the C program and their meanings: <code>0</code> , denotes a mismatch<br />
 <code>-1</code> , denotes the default classid configured from the command line<br />
 <code>else</code> , everything else will override the default classid to provide a facility for non-linear matching Supported 32 bit action return codes from the C program and their meanings ( <code>linux/pkt_cls.h</code> ): <code>TC_ACT_OK (0)</code> , will terminate the packet processing pipeline and allows the packet to proceed<br />
 <code>TC_ACT_SHOT (2)</code> , will terminate the packet processing pipeline and drops the packet<br />
 <code>TC_ACT_UNSPEC (-1)</code> , will use the default action configured from tc (similarly as returning <code>-1</code> from a classifier)<br />
 <code>TC_ACT_PIPE (3)</code> , will iterate to the next action, if available<br />
 <code>TC_ACT_RECLASSIFY (1)</code> , will terminate the packet processing pipeline and start classification from the beginning<br />
 <code>else</code> , everything else is an unspecified return code Both classifier and action return codes are supported in eBPF and cBPF programs. To demonstrate restricted C syntax, a minimal toy classifier example is provided, which assumes that egress packets, for instance originating from a container, have previously been marked in interval [0, 255]. The program keeps statistics on different marks for user space and maps the classid to the root qdisc with the marking itself as the minor handle:  Another small example is a port redirector which demuxes destination port 80 into the interval [8080, 8087] steered by RSS, that can then be attached to ingress qdisc. The exercise of adding the egress counterpart and IPv6 support is left to the reader: #include &lt;pcap.h&gt;<br />
#include &lt;stdio.h&gt;</p>
<p>int main(int argc, char **argv)<br />
{<br />
    struct bpf_program prog;<br />
    struct bpf_insn *ins;<br />
    int i, ret, dlt = DLT_RAW;</p>
<p>    if (argc &lt; 2 || argc &gt; 3)<br />
        return 1;<br />
    if (argc == 3) {<br />
        dlt = pcap_datalink_name_to_val(argv[1]);<br />
        if (dlt == -1)<br />
            return 1;<br />
    }</p>
<p>    ret = pcap_compile_nopcap(-1, dlt, &amp;prog, argv[argc &#8211; 1],<br />
                              1, PCAP_NETMASK_UNKNOWN);<br />
    if (ret)<br />
        return 1;</p>
<p>    printf(&quot;%d,&quot;, prog.bf_len);<br />
    ins = prog.bf_insns;</p>
<p>    for (i = 0; i &lt; prog.bf_len &#8211; 1; ++ins, ++i)<br />
        printf(&quot;%u %u %u %u,&quot;, ins-&gt;code,<br />
               ins-&gt;jt, ins-&gt;jf, ins-&gt;k);<br />
    printf(&quot;%u %u %u %u&quot;,<br />
           ins-&gt;code, ins-&gt;jt, ins-&gt;jf, ins-&gt;k);</p>
<p>    pcap_freecode(&amp;prog);<br />
    return 0;<br />
} The related helper header file <code>helpers.h</code> in both examples was:  Best practice, we recommend to only have a single eBPF classifier loaded in tc and perform <code>all</code> necessary matching and mangling from there instead of a list of individual classifier and separate actions. Just a single classifier tailored for a given use-case will be most efficient to run.</p>
<h3>eBPF DEBUGGING</h3>
<p>Both tc <code>filter</code> and <code>action</code> commands for <code>bpf</code> support an optional <code>verbose</code> parameter that can be used to inspect the eBPF verifier log. It is dumped by default in case of an error. In case the eBPF/cBPF JIT compiler has been enabled, it can also be instructed to emit a debug output of the resulting opcode image into the kernel log, which can be read via <code><a href="/docs/linux/man/1-dmesg/">dmesg</a>(1)</code> : <code>echo 2 &gt; /proc/sys/net/core/bpf_jit_enable</code> The Linux kernel source tree ships additionally under <code>tools/net/</code> a small helper called <code>bpf_jit_disasm</code> that reads out the opcode image dump from the kernel log and dumps the resulting disassembly: <code>bpf_jit_disasm -o</code> Other than that, the Linux kernel also contains an extensive eBPF/cBPF test suite module called <code>test_bpf</code> . Upon &#8230; <code>modprobe test_bpf</code> &#8230; it performs a diversity of test cases and dumps the results into the kernel log that can be inspected with <code><a href="/docs/linux/man/1-dmesg/">dmesg</a>(1)</code> . The results can differ depending on whether the JIT compiler is enabled or not. In case of failed test cases, the module will fail to load. In such cases, we urge you to file a bug report to the related JIT authors, Linux kernel and networking mailing lists.</p>
<h3>cBPF</h3>
<p>Although we generally recommend switching to implementing <code>eBPF</code> classifier and actions, for the sake of completeness, a few words on how to program in cBPF will be lost here. Likewise, the <code>bpf_jit_enable</code> switch can be enabled as mentioned already. Tooling such as <code>bpf_jit_disasm</code> is also independent whether eBPF or cBPF code is being loaded. Unlike in eBPF, classifier and action are not implemented in restricted C, but rather in a minimal assembler-like language or with the help of other tooling. The raw interface with tc takes opcodes directly. For example, the most minimal classifier matching on every packet resulting in the default classid of 1:1 looks like: <code>tc filter add dev em1 parent 1: bpf bytecode &#8216;1,6 0 0 4294967295,&#8217; flowid 1:1</code> The first decimal of the bytecode sequence denotes the number of subsequent 4-tuples of cBPF opcodes. As mentioned, such a 4-tuple consists of <code>c t f k</code> decimals, where <code>c</code> represents the cBPF opcode, <code>t</code> the jump true offset target, <code>f</code> the jump false offset target and <code>k</code> the immediate constant/literal. Here, this denotes an unconditional return from the program with immediate value of -1. Thus, for egress classification, Willem de Bruijn implemented a minimal stand-alone helper tool under the GNU General Public License version 2 for <code><a href="/docs/linux/man/8-iptables/">iptables</a>(8)</code> BPF extension, which abuses the <code>libpcap</code> internal classic BPF compiler, his code derived here for usage with <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> : </p>
<pre><code>#include &lt;pcap.h&gt;
#include &lt;stdio.h&gt;

int main(int argc, char **argv)
{
    struct bpf_program prog;
    struct bpf_insn *ins;
    int i, ret, dlt = DLT_RAW;

    if (argc &lt; 2 || argc &gt; 3)
        return 1;
    if (argc == 3) {
        dlt = pcap_datalink_name_to_val(argv[1]);
        if (dlt == -1)
            return 1;
    }

    ret = pcap_compile_nopcap(-1, dlt, &amp;prog, argv[argc - 1],
                              1, PCAP_NETMASK_UNKNOWN);
    if (ret)
        return 1;

    printf(&quot;%d,&quot;, prog.bf_len);
    ins = prog.bf_insns;

    for (i = 0; i &lt; prog.bf_len - 1; ++ins, ++i)
        printf(&quot;%u %u %u %u,&quot;, ins-&gt;code,
               ins-&gt;jt, ins-&gt;jf, ins-&gt;k);
    printf(&quot;%u %u %u %u&quot;,
           ins-&gt;code, ins-&gt;jt, ins-&gt;jf, ins-&gt;k);

    pcap_freecode(&amp;prog);
    return 0;
}</code></pre>
<p> Given this small helper, any <code><a href="/docs/linux/man/8-tcpdump/">tcpdump</a>(8)</code> filter expression can be abused as a classifier where a match will result in the default classid: <code>bpftool EN10MB &#8216;tcp[tcpflags] &amp; tcp-syn != 0&#8217; &gt; /var/bpf/tcp-syn</code><br />
 <code>tc filter add dev em1 parent 1: bpf bytecode-file /var/bpf/tcp-syn flowid 1:1</code> Basically, such a minimal generator is equivalent to: <code>tcpdump -iem1 -ddd &#8216;tcp[tcpflags] &amp; tcp-syn != 0&#8217; | tr &#8216;\n&#8217; &#8216;,&#8217; &gt; /var/bpf/tcp-syn</code> Since <code>libpcap</code> does not support all Linux&#8217; specific cBPF extensions in its compiler, the Linux kernel also ships under <code>tools/net/</code> a minimal BPF assembler called <code>bpf_asm</code> for providing full control. For detailed syntax and semantics on implementing such programs by hand, see references under <code>FURTHER READING</code> . Trivial toy example in <code>bpf_asm</code> for classifying IPv4/TCP packets, saved in a text file called <code>foobar</code> : </p>
<pre>ldh [12]
jne #0x800, drop
ldb [23]
jneq #6, drop
ret #-1
drop: ret #0</pre>
<p>Similarly, such a classifier can be loaded as: <code>bpf_asm foobar &gt; /var/bpf/tcp-syn</code><br />
 <code>tc filter add dev em1 parent 1: bpf bytecode-file /var/bpf/tcp-syn flowid 1:1</code> For BPF classifiers, the Linux kernel provides additionally under <code>tools/net/</code> a small BPF debugger called <code>bpf_dbg</code> , which can be used to test a classifier against pcap files, single-step or add various breakpoints into the classifier program and dump register contents during runtime. Implementing an action in classic BPF is rather limited in the sense that packet mangling is not supported. Therefore, it&#8217;s generally recommended to make the switch to eBPF, whenever possible. </p>
<h2>Further Reading</h2>
<p>Further and more technical details about the BPF architecture can be found in the Linux kernel source tree under <code>Documentation/networking/filter.txt</code> . </p>
<p> Further details on eBPF <code><a href="/docs/linux/man/8-tc/">tc</a>(8)</code> examples can be found in the iproute2 source tree under <code>examples/bpf/</code> .</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-tc/">tc</a></code>(8), <code><a href="/docs/linux/man/8-tc-ematch/">tc-ematch</a></code>(8) <code><a href="/docs/linux/man/2-bpf/">bpf</a></code>(2) <code><a href="/docs/linux/man/4-bpf/">bpf</a></code>(4) </p>
<h2>Authors</h2>
<p>Manpage written by Daniel Borkmann. </p>
<p> Please report corrections or improvements to the Linux kernel networking mailing list: <code>&lt;netdev [at] vger.kernel.org&gt;</code></p>
