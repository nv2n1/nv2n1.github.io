---
title: "sc_debugger(3)"
name: "sc_debugger"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_debugger/"
description: "sc::Debugger –"
---

<p>sc::Debugger &#8211; </p>
<p> The <code>Debugger</code> class describes what should be done when a catastrophic error causes unexpected program termination.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;bug.h&gt;</code></pre>
<p> Inherits <code>sc::SavableState</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>Debugger (const char *exec=0)



Debugger (const Ref&lt; KeyVal &gt; &amp;)


The KeyVal constructor understands the following keywords:.


Debugger (StateIn &amp;)



virtual void debug (const char *reason=0)


The debug member attempts to start a debugger running on the current process.


virtual void traceback (const char *reason=0)


The traceback member attempts a stack traceback for the current process.


virtual void set_debug_on_signal (int)


Turn on or off debugging on a signel. The default is on.


virtual void set_traceback_on_signal (int)


Turn on or off traceback on a signel. The default is on.


virtual void set_exit_on_signal (int)


Turn on or off exit after a signel. The default is on.


virtual void set_wait_for_debugger (int)


Turn on or off running an infinite loop after the debugger is started.


virtual void handle (int sig)


The Debugger will be actived when sig is caught.


virtual void handle_defaults ()


This calls handle(int) with all of the major signals.


virtual void set_prefix (const char *p)


This sets a prefix which preceeds all messages printing by Debugger.


virtual void set_prefix (int p)


Set the prefix to the decimal represention of p followed by a ': '.


virtual void set_cmd (const char *)


Sets the command to be exectuted when debug is called.


virtual void default_cmd ()


Calls set_cmd with a hopefully suitable default.


virtual void set_exec (const char *)


Set the name of the exectuble for the current process.


virtual void got_signal (int sig)


Called with signal sig is received. This is mainly for internal use.


void save_data_state (StateOut &amp;)


Save the base classes (with save_data_state) and the members in the same order that the StateIn CTOR initializes them.



Static Public Member Functions
static void set_default_debugger (const Ref&lt; Debugger &gt; &amp;)


Set the global default debugger. The initial value is null.


static Debugger * default_debugger ()


Return the global default debugger.



Protected Member Functions
void init ()



Protected Attributes
char * prefix_



char * exec_



char * cmd_



volatile int debugger_ready_



int debug_



int traceback_



int exit_on_signal_



int sleep_



int wait_for_debugger_



int handle_sigint_



int * mysigs_



Static Protected Attributes
static Debugger * default_debugger_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>Debugger</code> class describes what should be done when a catastrophic error causes unexpected program termination. </p>
<p> It can try things such as start a debugger running where the program died or it can attempt to produce a stack traceback showing roughly where the program died. These attempts will not always succeed.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::Debugger::Debugger (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor understands the following keywords:. .IP &quot;debug&quot; 1c Try to start a debugger when an error occurs. Doesn&#8217;t work on all machines. The default is true, if possible. </p>
<dl>
<dt>traceback</p>
<dd>Try to print out a traceback extracting return addresses from the call stack. Doesn&#8217;t work on most machines. The default is true, if possible.</dl>
<dl>
<dt>exit</p>
<dd>Exit on errors. The default is true.</dl>
<dl>
<dt>wait_for_debugger</p>
<dd>When starting a debugger go into an infinite loop to give the debugger a chance to attach to the process. The default is true.</dl>
<dl>
<dt>sleep</p>
<dd>When starting a debugger wait this many seconds to give the debugger a chance to attach to the process. The default is 0.</dl>
<dl>
<dt>handle_defaults</p>
<dd>Handle a standard set of signals such as SIGBUS, SIGSEGV, etc. The default is true.</dl>
<dl>
<dt>prefix</p>
<dd>Gives a string that is printed before each line that is printed by <code>Debugger</code>. The default is nothing.</dl>
<dl>
<dt>cmd</p>
<dd>Gives a command to be executed to start the debugger. The default varies with machine.</dl>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::Debugger::debug (const char * reason = 0) [virtual]</h3>
<p>The debug member attempts to start a debugger running on the current process.</p>
<h3>void sc::Debugger::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::SavableState</code>.</p>
<h3>virtual void sc::Debugger::set_cmd (const char *) [virtual]</h3>
<p>Sets the command to be exectuted when debug is called. The character sequence &#8216;$(EXEC)&#8217; is replaced by the executable name (see set_exec), &#8216;$(PID)&#8217; is replaced by the current process id, and &#8216;$(PREFIX)&#8217; is replaced by the prefix.</p>
<h3>virtual void sc::Debugger::set_exec (const char *) [virtual]</h3>
<p>Set the name of the exectuble for the current process. It is up to the programmer to set this, even if the <code>Debugger</code> is initialized with the <code>KeyVal</code> constructor.</p>
<h3>virtual void sc::Debugger::set_wait_for_debugger (int) [virtual]</h3>
<p>Turn on or off running an infinite loop after the debugger is started. This loop gives the debugger a chance to attack to the process. The default is on.</p>
<h3>virtual void sc::Debugger::traceback (const char * reason = 0) [virtual]</h3>
<p>The traceback member attempts a stack traceback for the current process. A symbol table must be saved for the executable if any sense is to be made of the traceback. Tracebacks are currently available only for a limited number of architectures.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
