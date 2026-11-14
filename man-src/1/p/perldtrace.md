---
title: "perldtrace(1)"
name: "perldtrace"
section: "1"
letter: "p"
url: "/docs/linux/man/1-perldtrace/"
---

<h2 class="name">NAME</h2>
 

 perldtrace - Perl's support for DTrace 

<h2>SYNOPSIS</h2>

 <pre><code>
#dtrace - Zn 'perl::sub-entry, perl::sub-return { trace(copyinstr(arg0)) }'
dtrace : description 'perl::sub-entry, perl::sub-return ' matched 10 probes
#perl - E 'sub outer { inner(@_) } sub inner { say shift } outer("hello")'
         hello(dtrace output)
             CPU ID FUNCTION : NAME
                               0 75915 Perl_pp_entersub : sub
                                                          -
                                                          entry BEGIN
                                                          0 75915 Perl_pp_entersub : sub
                                                                                     -
                                                                                     entry import
                                                                                     0 75922 Perl_pp_leavesub : sub
                                                                                                                -
                                                                                                                return import
                                                                                                                0 75922 Perl_pp_leavesub : sub
                                                                                                                                           -
                                                                                                                                           return BEGIN
                                                                                                                                           0 75915 Perl_pp_entersub : sub
                                                                                                                                                                      -
                                                                                                                                                                      entry outer
                                                                                                                                                                      0 75915 Perl_pp_entersub : sub
                                                                                                                                                                                                 -
                                                                                                                                                                                                 entry inner
                                                                                                                                                                                                 0 75922 Perl_pp_leavesub : sub
                                                                                                                                                                                                                            -
                                                                                                                                                                                                                            return inner
                                                                                                                                                                                                                            0 75922 Perl_pp_leavesub : sub
                                                                                                                                                                                                                                                       -
                                                                                                                                                                                                                                                       return outer
</code></pre>

<h2>DESCRIPTION</h2>

 DTrace is a framework for comprehensive system- and application-level tracing. Perl is a DTrace <i>provider</i>, meaning it exposes several <i>probes</i> for instrumentation. You can use these in conjunction with kernel-level probes, as well as probes from other providers such as MySQL, in order to diagnose software defects, or even just your application's bottlenecks. 

 Perl must be compiled with the <tt>&quot;-Dusedtrace&quot;</tt> option in order to make use of the provided probes. While DTrace aims to have no overhead when its instrumentation is not active, Perl's support itself cannot uphold that guarantee, so it is built without DTrace probes under most systems. One notable exception is that Mac <font SIZE="-1">OS X</font> ships a <i>/usr/bin/perl</i> with DTrace support enabled.

<h2>HISTORY</h2>

<dl>
<dt>5.10.1
<dd> Perl's initial DTrace support was added, providing <tt>&quot;sub-entry&quot;</tt> and <tt>&quot;sub-return&quot;</tt> probes.
<dt>5.14.0
<dd> The <tt>&quot;sub-entry&quot;</tt> and <tt>&quot;sub-return&quot;</tt> probes gain a fourth argument: the package name of the function.
<dt>5.16.0
<dd> The <tt>&quot;phase-change&quot;</tt> probe was added.
<dt>5.18.0
<dd> The <tt>&quot;op-entry&quot;</tt>, <tt>&quot;loading-file&quot;</tt>, and <tt>&quot;loaded-file&quot;</tt> probes were added.</dl>

<h2>PROBES</h2>

<dl>
<dt>sub-entry(<font SIZE="-1">SUBNAME, FILE, LINE, PACKAGE</font>)
<dd> Traces the entry of any subroutine. Note that all of the variables refer to the subroutine that is being invoked; there is currently no way to get ahold of any information about the subroutine's <i>caller</i> from a DTrace action. 

 
 :*perl*::sub-entry
 {
     printf("%s::%s entered at %s line %d\n",
            copyinstr(arg3), copyinstr(arg0), copyinstr(arg1), arg2);
 }

<dt>sub-return(<font SIZE="-1">SUBNAME, FILE, LINE, PACKAGE</font>)
<dd> Traces the exit of any subroutine. Note that all of the variables refer to the subroutine that is returning; there is currently no way to get ahold of any information about the subroutine's <i>caller</i> from a DTrace action. 

 
 :*perl*::sub-return
 {
     printf("%s::%s returned at %s line %d\n",
            copyinstr(arg3), copyinstr(arg0), copyinstr(arg1), arg2);
 }

<dt>phase-change(<font SIZE="-1">NEWPHASE, OLDPHASE</font>)
<dd> Traces changes to Perl's interpreter state. You can internalize this as tracing changes to Perl's <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> variable, especially since the values for <tt>&quot;NEWPHASE&quot;</tt> and <tt>&quot;OLDPHASE&quot;</tt> are the strings that <tt>&quot;${^GLOBAL_PHASE}&quot;</tt> reports. 

 
 :*perl*::phase-change
 {
     printf("Phase changed from %s to %s\n",
            copyinstr(arg1), copyinstr(arg0));
 }

<dt>op-entry(<font SIZE="-1">OPNAME</font>)
<dd> Traces the execution of each opcode in the Perl runloop. This probe is fired before the opcode is executed. When the Perl debugger is enabled, the DTrace probe is fired <i>after</i> the debugger hooks (but still before the opcode itself is executed). 

 
 :*perl*::op-entry
 {
     printf("About to execute opcode %s\n", copyinstr(arg0));
 }

<dt>loading-file(<font SIZE="-1">FILENAME</font>)
<dd> Fires when Perl is about to load an individual file, whether from <tt>&quot;use&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;do&quot;</tt>. This probe fires before the file is read from disk. The filename argument is converted to local filesystem paths instead of providing <tt>&quot;Module::Name&quot;</tt>-style names. 

 
 :*perl*:loading-file
 {
     printf("About to load %s\n", copyinstr(arg0));
 }

<dt>loaded-file(<font SIZE="-1">FILENAME</font>)
<dd> Fires when Perl has successfully loaded an individual file, whether from <tt>&quot;use&quot;</tt>, <tt>&quot;require&quot;</tt>, or <tt>&quot;do&quot;</tt>. This probe fires after the file is read from disk and its contents evaluated. The filename argument is converted to local filesystem paths instead of providing <tt>&quot;Module::Name&quot;</tt>-style names. 

 
 :*perl*:loaded-file
 {
     printf("Successfully loaded %s\n", copyinstr(arg0));
 }
</dl>

<h2>EXAMPLES</h2>

<dl>
<dt>Most frequently called functions
<dd> 
#dtrace - qZn 'sub-entry { @[strjoin(strjoin(copyinstr(arg3),"::"),copyinstr(arg0))] = count() } END {trunc(@, 10)}'
Class::MOP::Attribute::slots 400 Try::Tiny::catch 411 Try::Tiny::try 411 Class::MOP::Instance::inline_slot_access 451 Class::MOP::Class::Immutable::Trait:: : around 472 Class::MOP::Mixin::AttributeCore::has_initializer 496 Class::MOP::Method::Wrapped::__ANON__ 544 Class::MOP::Package::_package_stash 737 Class::MOP::Class::initialize 1128 Class::MOP::get_metaclass_by_name 1204

<dt>Trace function calls
<dd> 
#dtrace - qFZn 'sub-entry, sub-return { trace(copyinstr(arg0)) }'
0-&gt;Perl_pp_entersub BEGIN 0 &lt; -Perl_pp_leavesub BEGIN 0-&gt;Perl_pp_entersub BEGIN 0-&gt;Perl_pp_entersub import 0 &lt; -Perl_pp_leavesub import 0 &lt; -Perl_pp_leavesub BEGIN 0-&gt;Perl_pp_entersub BEGIN 0-&gt;Perl_pp_entersub dress 0 &lt; -Perl_pp_leavesub dress 0-&gt;Perl_pp_entersub dirty 0 &lt; -Perl_pp_leavesub dirty 0-&gt;Perl_pp_entersub whiten 0 &lt; -Perl_pp_leavesub whiten 0 &lt; -Perl_dounwind BEGIN

<dt>Function calls during interpreter cleanup
<dd> 
#dtrace - Zn 'phase-change /copyinstr(arg0) == "END"/ { self-&gt;ending = 1 } sub-entry /self-&gt;ending/ { trace(copyinstr(arg0)) }'
CPU ID FUNCTION : NAME 1 77214 Perl_pp_entersub : sub - entry END 1 77214 Perl_pp_entersub : sub - entry END 1 77214 Perl_pp_entersub : sub - entry cleanup 1 77214 Perl_pp_entersub : sub - entry _force_writable 1 77214 Perl_pp_entersub : sub - entry _force_writable

<dt>System calls at compile time
<dd> 
#dtrace - qZn 'phase-change /copyinstr(arg0) == "START"/ { self-&gt;interesting = 1 } phase-change /copyinstr(arg0) == "RUN"/ { self-&gt;interesting = 0 } syscall::: /self-&gt;interesting/ { @[probefunc] = count() } END { trunc(@, 3) }'
lseek 310 read 374 stat64 1056

<dt>Perl functions that execute the most opcodes
<dd> <pre><code>
#dtrace - qZn 'sub-entry { self-&gt;fqn = strjoin(copyinstr(arg3), strjoin("::", copyinstr(arg0))) } op-entry /self-&gt;fqn != ""/ { @[self-&gt;fqn] = count() } END { trunc(@, 3) }'
warnings::unimport 4589 Exporter::Heavy::_rebuild_cache 5039 Exporter::import 14578
</code></pre></dl>

<h2>REFERENCES</h2>

<dl>
<dt>DTrace Dynamic Tracing Guide
<dd> &lt;<a rel="nofollow" HREF="http://dtrace.org/guide/preface.html">http://dtrace.org/guide/preface.html</a>&gt;
<dt>DTrace: Dynamic Tracing in Oracle Solaris, Mac <font SIZE="-1">OS X</font> and FreeBSD
<dd> &lt;<a rel="nofollow" HREF="http://www.amazon.com/DTrace-Dynamic-Tracing-Solaris-FreeBSD/dp/0132091518/">http://www.amazon.com/DTrace-Dynamic-Tracing-Solaris-FreeBSD/dp/0132091518/</a>&gt;</dl>

<h2>SEE ALSO</h2>

<dl>
<dt>Devel::DTrace::Provider
<dd> This <font SIZE="-1">CPAN</font> module lets you create application-level DTrace probes written in Perl.</dl>

<h2>AUTHORS</h2>

 Shawn M Moore <tt>&quot;sartak [at] gmail.com&quot;</tt> 

<h2>Index</h2>


