---
title: "abc(1)"
name: "abc"
section: "1"
letter: "a"
url: "/docs/linux/man/1-abc/"
description: "abc – sequential logic synthesis and formal verification"
---

<h2>NAME</h2>
<p> abc &#8211; sequential logic synthesis and formal verification</p>
<h2>SYNOPSIS</h2>
<p> <code>abc</code> [<i>OPTIONS</i>] <i>FILE</i></p>
<h2>DESCRIPTION</h2>
<p> ABC is a growing software system for synthesis and verification of binary sequential logic circuits appearing in synchronous hardware designs. ABC combines scalable logic optimization based on And-Inverter Graphs (AIGs), optimal-delay DAG-based technology mapping for look-up tables and standard cells, and innovative algorithms for sequential synthesis and verification. </p>
<p> ABC provides an experimental implementation of these algorithms and a programming environment for building similar applications. Future development will focus on improving the algorithms and making most of the packages stand-alone. This will allow the user to customize ABC for their needs as if it were a toolbox rather than a complete tool.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-c</code> <i>CMD</i></p>
<dd> Execute commands <i>CMD</i>.</p>
<dt><code>-q</code> <i>CMD</i></p>
<dd> Execute commands <i>CMD</i> quietly.</p>
<dt><code>-C</code> <i>CMD</i></p>
<dd> Execute commands <i>CMD</i>, then continue in interactive mode.</p>
<dt><code>-F</code> <i>SCRIPT</i></p>
<dd> Execute commands from script file <i>SCRIPT</i> and echo commands.</p>
<dt><code>-f</code> <i>SCRIPT</i></p>
<dd> Execute commands from script file <i>SCRIPT</i>.</p>
<dt><code>-h</code></p>
<dd> Print command usage.</p>
<dt><code>-o</code> <i>FILE</i></p>
<dd> Store the result in <i>FILE</i>.</p>
<dt><code>-s</code></p>
<dd> Do not read any initialization file.</p>
<dt><code>-t</code> <i>TYPE</i></p>
<dd> Specify the input type, one of <i>blif_mv</i>, <i>blif_mvs</i>, <i>blif</i>, or <i>none</i>. The default is <i>blif_mv</i>.</p>
<dt><code>-T</code> <i>TYPE</i></p>
<dd> Specify the output type, one of <i>blif_mv</i>, <i>blif_mvs</i>, <i>blif</i>, or <i>none</i>. The default is <i>blif_mv</i>.</p>
<dt><code>-x</code></p>
<dd> Equivalent to <i>-t none -T none</i>.</p>
<dt><code>-b</code></p>
<dd> Run in bridge mode.</dl>
<h2>INTRODUCTION</h2>
<p> Data structures and algorithms at the heart of a software system determine its capabilities in processing data and its efficiency as a programming environment for building new applications. Extensive experience of developing and using SIS, VIS, and MVSIS, makes it clear that these systems do not provide a flexible programming environment to implement recent innovations, such as integration of technology mapping and retiming. Specifically, the SIS environment is outdated and rather inefficient when handling large circuits. VIS, designed as a formal verification tool for multi-valued specifications, does not provide enough flexibility for binary synthesis. MVSIS was developed and extensively used by us in the recent years for implementing new synthesis algorithms for both multi-valued and binary networks. Finally, we became convinced that (a) the basic data structures and algorithms of MVSIS can be made considerably simpler and easier to use by assuming binary networks, and (b) a central place in the new system should be given to a new data structure, AIGs (multi-level logic networks composed of two-input ANDs and inverters), which promises improvements in quality and runtime of synthesis and verification. </p>
<p> This understanding motivates us to redevelop the core packages of MVSIS resulting in a new programming environment named ABC. As the name suggests, the primary goal is to keep data structures simple and flexible for a wide range of applications. The “philosophy of ABC” has several basic premises. One of them is allowing for a variety of functional representations, such as BDDs and SOPs, to solve specialized tasks, while defaulting to AIGs for the mainstream network manipulation. Representing logic using AIGs leads to a remarkable uniformity in computation and efficient interfacing with CNF-based SAT solvers for handing Boolean reasoning problems. Another fundamental premise of ABC is the synergy between synthesis and verification using efficient SAT-based Boolean reasoning on the AIG for combinational and sequential equivalence checking. </p>
<p> The goal of the ABC project is to provide a public-domain implementation of the state-of-the-art combinational and sequential synthesis algorithms and, at the same time, create an open-source environment, in which such applications can be developed and compared. The current version of ABC can optimize/map/retime industrial gate-level designs with 100K gates and 10K sequential elements for optimal delay and heuristically minimized area in about one minute of CPU time on a modern computer. The runtime of the combinational synthesis, mapping, and verification is typically faster. </p>
<h2>Index</h2>
