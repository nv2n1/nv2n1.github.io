---
title: "llvm-exegesis-14(1)"
name: "llvm-exegesis-14"
section: "1"
letter: "l"
url: "/docs/linux/man/1-llvm-exegesis-14/"
description: "llvm-exegesis – LLVM Machine Instruction Benchmark"
---

<h2 class="name">NAME</h2>
<p> llvm-exegesis &#8211; LLVM Machine Instruction Benchmark </p>
<h2>SYNOPSIS</h2>
<p> <code>llvm-exegesis</code> [<i>options</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>llvm-exegesis</code> is a benchmarking tool that uses information available in LLVM to measure host machine instruction characteristics like latency, throughput, or port decomposition. </p>
<p> Given an LLVM opcode name and a benchmarking mode, <code>llvm-exegesis</code> generates a code snippet that makes execution as serial (resp. as parallel) as possible so that we can measure the latency (resp. inverse throughput/uop decomposition) of the instruction. The code snippet is jitted and executed on the host subtarget. The time taken (resp. resource usage) is measured using hardware performance counters. The result is printed out as YAML to the standard output. </p>
<p> The main goal of this tool is to automatically (in)validate the LLVM’s TableDef scheduling models. To that end, we also provide analysis of the results. </p>
<p> <code>llvm-exegesis</code> can also benchmark arbitrary user-provided code snippets.</p>
<h2>EXAMPLE 1: BENCHMARKING INSTRUCTIONS</h2>
<p> Assume you have an X86-64 machine. To measure the latency of a single instruction, run: </p>
<pre>
$ llvm-exegesis -mode=latency -opcode-name=ADD64rr
</pre>
<p> Measuring the uop decomposition or inverse throughput of an instruction works similarly: </p>
<pre>
$ llvm-exegesis -mode=uops -opcode-name=ADD64rr
$ llvm-exegesis -mode=inverse_throughput -opcode-name=ADD64rr
</pre>
<p> The output is a YAML document (the default is to write to stdout, but you can redirect the output to a file using <i>-benchmarks-file</i>): </p>
<pre>
---
key:
  opcode_name:     ADD64rr
  mode:            latency
  config:          ''
cpu_name:        haswell
llvm_triple:     x86_64-unknown-linux-gnu
num_repetitions: 10000
measurements:
  - { key: latency, value: 1.0058, debug_string: '' }
error:           ''
info:            'explicit self cycles, selecting one aliasing configuration.
Snippet:
ADD64rr R8, R8, R10
'
...
</pre>
<p> To measure the latency of all instructions for the host architecture, run: </p>
<pre>
$ llvm-exegesis -mode=latency -opcode-index=-1
</pre>
<h2>EXAMPLE 2: BENCHMARKING A CUSTOM CODE SNIPPET</h2>
<p> To measure the latency/uops of a custom piece of code, you can specify the <i>snippets-file</i> option (<i>&#8211;</i> reads from standard input). </p>
<pre>
$ echo &quot;vzeroupper&quot; | llvm-exegesis -mode=uops -snippets-file=-
</pre>
<p> Real-life code snippets typically depend on registers or memory. <code>llvm-exegesis</code> checks the liveliness of registers (i.e. any register use has a corresponding def or is a “live in”). If your code depends on the value of some registers, you have two options:</p>
<dl>
<dt>&bull;</p>
<dd> Mark the register as requiring a definition. <code>llvm-exegesis</code> will automatically assign a value to the register. This can be done using the directive <i>LLVM-EXEGESIS-DEFREG &lt;reg name&gt; &lt;hex_value&gt;</i>, where <i>&lt;hex_value&gt;</i> is a bit pattern used to fill <i>&lt;reg_name&gt;</i>. If <i>&lt;hex_value&gt;</i> is smaller than the register width, it will be sign-extended.</p>
<dt>&bull;</p>
<dd> Mark the register as a “live in”. <code>llvm-exegesis</code> will benchmark using whatever value was in this registers on entry. This can be done using the directive <i>LLVM-EXEGESIS-LIVEIN &lt;reg name&gt;</i>. </p>
<p> For example, the following code snippet depends on the values of XMM1 (which will be set by the tool) and the memory buffer passed in RDI (live in). </p>
<pre>
# LLVM-EXEGESIS-LIVEIN RDI
# LLVM-EXEGESIS-DEFREG XMM1 42
vmulps        (%rdi), %xmm1, %xmm2
vhaddps       %xmm2, %xmm2, %xmm3
addq $0x10, %rdi
</pre>
</dl>
<h2>EXAMPLE 3: ANALYSIS</h2>
<p> Assuming you have a set of benchmarked instructions (either latency or uops) as YAML in file <i>/tmp/benchmarks.yaml</i>, you can analyze the results using the following command: </p>
<pre>
  $ llvm-exegesis -mode=analysis \
-benchmarks-file=/tmp/benchmarks.yaml \
-analysis-clusters-output-file=/tmp/clusters.csv \
-analysis-inconsistencies-output-file=/tmp/inconsistencies.html
</pre>
<p> This will group the instructions into clusters with the same performance characteristics. The clusters will be written out to <i>/tmp/clusters.csv</i> in the following format: </p>
<pre>
cluster_id,opcode_name,config,sched_class
...
2,ADD32ri8_DB,,WriteALU,1.00
2,ADD32ri_DB,,WriteALU,1.01
2,ADD32rr,,WriteALU,1.01
2,ADD32rr_DB,,WriteALU,1.00
2,ADD32rr_REV,,WriteALU,1.00
2,ADD64i32,,WriteALU,1.01
2,ADD64ri32,,WriteALU,1.01
2,MOVSX64rr32,,BSWAP32r_BSWAP64r_MOVSX64rr32,1.00
2,VPADDQYrr,,VPADDBYrr_VPADDDYrr_VPADDQYrr_VPADDWYrr_VPSUBBYrr_VPSUBDYrr_VPSUBQYrr_VPSUBWYrr,1.02
2,VPSUBQYrr,,VPADDBYrr_VPADDDYrr_VPADDQYrr_VPADDWYrr_VPSUBBYrr_VPSUBDYrr_VPSUBQYrr_VPSUBWYrr,1.01
2,ADD64ri8,,WriteALU,1.00
2,SETBr,,WriteSETCC,1.01
...
</pre>
<p> <code>llvm-exegesis</code> will also analyze the clusters to point out inconsistencies in the scheduling information. The output is an html file. For example, <i>/tmp/inconsistencies.html</i> will contain messages like the following : [image] </p>
<p> Note that the scheduling class names will be resolved only when <code>llvm-exegesis</code> is compiled in debug mode, else only the class id will be shown. This does not invalidate any of the analysis results though.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-help</code></p>
<dd> Print a summary of command line options.</p>
<dt><code>-opcode-index=&lt;LLVM opcode index&gt;</code></p>
<dd> Specify the opcode to measure, by index. Specifying <i>-1</i> will result in measuring every existing opcode. See example 1 for details. Either <i>opcode-index</i>, <i>opcode-name</i> or <i>snippets-file</i> must be set.</p>
<dt><code>-opcode-name=&lt;opcode name 1&gt;,&lt;opcode name 2&gt;,&#8230;</code></p>
<dd> Specify the opcode to measure, by name. Several opcodes can be specified as a comma-separated list. See example 1 for details. Either <i>opcode-index</i>, <i>opcode-name</i> or <i>snippets-file</i> must be set.</p>
<dt><code>-snippets-file=&lt;filename&gt;</code></p>
<dd> Specify the custom code snippet to measure. See example 2 for details. Either <i>opcode-index</i>, <i>opcode-name</i> or <i>snippets-file</i> must be set.</p>
<dt><code>-mode=[latency|uops|inverse_throughput|analysis]</code></p>
<dd> Specify the run mode. Note that some modes have additional requirements and options. </p>
<p> <i>latency</i> mode can be make use of either RDTSC or LBR. <i>latency[LBR]</i> is only available on X86 (at least <i>Skylake</i>). To run in <i>latency</i> mode, a positive value must be specified for <i>x86-lbr-sample-period</i> and <i>–repetition-mode=loop</i>. </p>
<p> In <i>analysis</i> mode, you also need to specify at least one of the <i>-analysis-clusters-output-file=</i> and <i>-analysis-inconsistencies-output-file=</i>.</p>
<dt><code>-x86-lbr-sample-period=&lt;nBranches/sample&gt;</code></p>
<dd> Specify the LBR sampling period &#8211; how many branches before we take a sample. When a positive value is specified for this option and when the mode is <i>latency</i>, we will use LBRs for measuring. On choosing the “right” sampling period, a small value is preferred, but throttling could occur if the sampling is too frequent. A prime number should be used to avoid consistently skipping certain blocks.</p>
<dt><code>-repetition-mode=[duplicate|loop|min]</code></p>
<dd> Specify the repetition mode. <i>duplicate</i> will create a large, straight line basic block with <i>num-repetitions</i> instructions (repeating the snippet <i>num-repetitions</i>/<i>snippet size</i> times). <i>loop</i> will, optionally, duplicate the snippet until the loop body contains at least <i>loop-body-size</i> instructions, and then wrap the result in a loop which will execute <i>num-repetitions</i> instructions (thus, again, repeating the snippet <i>num-repetitions</i>/<i>snippet size</i> times). The <i>loop</i> mode, especially with loop unrolling tends to better hide the effects of the CPU frontend on architectures that cache decoded instructions, but consumes a register for counting iterations. If performing an analysis over many opcodes, it may be best to instead use the <i>min</i> mode, which will run each other mode, and produce the minimal measured result.</p>
<dt><code>-num-repetitions=&lt;Number of repetitions&gt;</code></p>
<dd> Specify the target number of executed instructions. Note that the actual repetition count of the snippet will be <i>num-repetitions</i>/<i>snippet size</i>. Higher values lead to more accurate measurements but lengthen the benchmark.</p>
<dt><code>-loop-body-size=&lt;Preferred loop body size&gt;</code></p>
<dd> Only effective for <i>-repetition-mode=[loop|min]</i>. Instead of looping over the snippet directly, first duplicate it so that the loop body contains at least this many instructions. This potentially results in loop body being cached in the CPU Op Cache / Loop Cache, which allows to which may have higher throughput than the CPU decoders.</p>
<dt><code>-max-configs-per-opcode=&lt;value&gt;</code></p>
<dd> Specify the maximum configurations that can be generated for each opcode. By default this is <i>1</i>, meaning that we assume that a single measurement is enough to characterize an opcode. This might not be true of all instructions: for example, the performance characteristics of the LEA instruction on X86 depends on the value of assigned registers and immediates. Setting a value of <i>-max-configs-per-opcode</i> larger than <i>1</i> allows <i>llvm-exegesis</i> to explore more configurations to discover if some register or immediate assignments lead to different performance characteristics.</p>
<dt><code>-benchmarks-file=&lt;/path/to/file&gt;</code></p>
<dd> File to read (<i>analysis</i> mode) or write (<i>latency</i>/<i>uops</i>/<i>inverse_throughput</i> modes) benchmark results. “-” uses stdin/stdout.</p>
<dt><code>-analysis-clusters-output-file=&lt;/path/to/file&gt;</code></p>
<dd> If provided, write the analysis clusters as CSV to this file. “-” prints to stdout. By default, this analysis is not run.</p>
<dt><code>-analysis-inconsistencies-output-file=&lt;/path/to/file&gt;</code></p>
<dd> If non-empty, write inconsistencies found during analysis to this file. <i>&#8211;</i> prints to stdout. By default, this analysis is not run.</p>
<dt><code>-analysis-clustering=[dbscan,naive]</code></p>
<dd> Specify the clustering algorithm to use. By default DBSCAN will be used. Naive clustering algorithm is better for doing further work on the <i>-analysis-inconsistencies-output-file=</i> output, it will create one cluster per opcode, and check that the cluster is stable (all points are neighbours).</p>
<dt><code>-analysis-numpoints=&lt;dbscan numPoints parameter&gt;</code></p>
<dd> Specify the numPoints parameters to be used for DBSCAN clustering (<i>analysis</i> mode, DBSCAN only).</p>
<dt><code>-analysis-clustering-epsilon=&lt;dbscan epsilon parameter&gt;</code></p>
<dd> Specify the epsilon parameter used for clustering of benchmark points (<i>analysis</i> mode).</p>
<dt><code>-analysis-inconsistency-epsilon=&lt;epsilon&gt;</code></p>
<dd> Specify the epsilon parameter used for detection of when the cluster is different from the LLVM schedule profile values (<i>analysis</i> mode).</p>
<dt><code>-analysis-display-unstable-clusters</code></p>
<dd> If there is more than one benchmark for an opcode, said benchmarks may end up not being clustered into the same cluster if the measured performance characteristics are different. by default all such opcodes are filtered out. This flag will instead show only such unstable opcodes.</p>
<dt><code>-ignore-invalid-sched-class=false</code></p>
<dd> If set, ignore instructions that do not have a sched class (class idx = 0).</p>
<dt><code>-mcpu=&lt;cpu name&gt;</code></p>
<dd> If set, measure the cpu characteristics using the counters for this CPU. This is useful when creating new sched models (the host CPU is unknown to LLVM).</p>
<dt><code>&#8211;dump-object-to-disk=true</code></p>
<dd> By default, llvm-exegesis will dump the generated code to a temporary file to enable code inspection. You may disable it to speed up the execution and save disk space.</dl>
<h2>EXIT STATUS</h2>
<p> <code>llvm-exegesis</code> returns 0 on success. Otherwise, an error message is printed to standard error, and the tool returns a non 0 value.</p>
<h2>AUTHOR</h2>
<p> Maintained by the LLVM Team (<a rel="nofollow" href="https://llvm.org/">https://llvm.org/</a>).</p>
<h2>COPYRIGHT</h2>
<p> 2003-2022, LLVM Project </p>
<h2>Index</h2>
