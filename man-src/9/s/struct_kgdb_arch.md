---
title: "struct_kgdb_arch(9)"
name: "struct_kgdb_arch"
section: "9"
letter: "s"
url: "/docs/linux/man/9-struct_kgdb_arch/"
description: "struct_kgdb_arch – Describe architecture specific values."
---

<p>struct_kgdb_arch &#8211; Describe architecture specific values.</p>
<h2>Synopsis</h2>
<pre><code>struct kgdb_arch {
    unsigned char gdb_bpt_instr[BREAK_INSTR_SIZE];
    unsigned long flags;
    int (*set_breakpoint)(unsigned long, char *);
    int (*remove_breakpoint)(unsigned long, char *);
    int (*set_hw_breakpoint)(unsigned long, int, enum kgdb_bptype);
    int (*remove_hw_breakpoint)(unsigned long, int, enum kgdb_bptype);
    void (*disable_hw_break)(struct pt_regs *regs);
    void (*remove_all_hw_break)(void);
    void (*correct_hw_break)(void);
    void (*enable_nmi)(bool on);
};</code></pre>
<h2>Members</h2>
<p>gdb_bpt_instr[BREAK_INSTR_SIZE]</p>
<dl>
<dd>The instruction to trigger a breakpoint.</dl>
<p> flags</p>
<dl>
<dd>Flags for the breakpoint, currently just <code>KGDB_HW_BREAKPOINT</code>.</dl>
<p> set_breakpoint</p>
<dl>
<dd>Allow an architecture to specify how to set a software breakpoint.</dl>
<p> remove_breakpoint</p>
<dl>
<dd>Allow an architecture to specify how to remove a software breakpoint.</dl>
<p> set_hw_breakpoint</p>
<dl>
<dd>Allow an architecture to specify how to set a hardware breakpoint.</dl>
<p> remove_hw_breakpoint</p>
<dl>
<dd>Allow an architecture to specify how to remove a hardware breakpoint.</dl>
<p> disable_hw_break</p>
<dl>
<dd>Allow an architecture to specify how to disable hardware breakpoints for a single cpu.</dl>
<p> remove_all_hw_break</p>
<dl>
<dd>Allow an architecture to specify how to remove all hardware breakpoints.</dl>
<p> correct_hw_break</p>
<dl>
<dd>Allow an architecture to specify how to correct the hardware debug registers.</dl>
<p> enable_nmi</p>
<dl>
<dd>Manage NMI-triggered entry to KGDB</dl>
<h2>Author</h2>
<p><code>Jason Wessel</code> &lt;jason.wessel [at] windriver.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
