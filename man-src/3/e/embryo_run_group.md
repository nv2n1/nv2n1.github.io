---
title: "embryo_run_group(3)"
name: "embryo_run_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo_run_group/"
description: "Program Run Functions – Functions that are involved in actually running functions in an Embryo program."
---

<p>Program Run Functions &#8211; Functions that are involved in actually running functions in an Embryo program. </p>
<h3>Functions</h3>
<p>EAPI int <code>embryo_program_recursion_get</code> (Embryo_Program *ep)<br />
 <i>Returns the number of virtual machines are running for the given program. </i><br />
 EAPI int <code>embryo_program_run</code> (Embryo_Program *ep, Embryo_Function fn)<br />
 <i>Runs the given function of the given Embryo program in the current virtual machine. </i><br />
 EAPI Embryo_Cell <code>embryo_program_return_value_get</code> (Embryo_Program *ep)<br />
 <i>Retreives the return value of the last called function of the given program. </i><br />
 EAPI void <code>embryo_program_max_cycle_run_set</code> (Embryo_Program *ep, int max)<br />
 <i>Sets the maximum number of abstract machine cycles any given program run can execute before being put to sleep and returning. </i><br />
 EAPI int <code>embryo_program_max_cycle_run_get</code> (Embryo_Program *ep)<br />
 <i>Retreives the maximum number of abstract machine cycles a program is allowed to run. </i></p>
<h2>Detailed Description</h2>
<p>Functions that are involved in actually running functions in an Embryo program.</p>
<h2>Function Documentation</h2>
<h3>EAPI int embryo_program_max_cycle_run_get (Embryo_Program * ep)</h3>
<p>Retreives the maximum number of abstract machine cycles a program is allowed to run. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of cycles a run cycle is allowed to run for this program.</dl>
<p> This returns the value set by <code>embryo_program_max_cycle_run_set()</code>. See <code>embryo_program_max_cycle_run_set()</code> for more information.</p>
<h3>EAPI void embryo_program_max_cycle_run_set (Embryo_Program * ep, int max)</h3>
<p>Sets the maximum number of abstract machine cycles any given program run can execute before being put to sleep and returning. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>max</i> The number of machine cycles as a limit.</dl>
<p> This sets the maximum number of abstract machine (virtual machine) instructions that a single run of an embryo function (even if its main) can use before embryo <code>embryo_program_run()</code> reutrns with the value EMBRYO_PROGRAM_TOOLONG. If the function fully executes within this number of cycles, <code>embryo_program_run()</code> will return as normal with either EMBRYO_PROGRAM_OK, EMBRYO_PROGRAM_FAIL or EMBRYO_PROGRAM_SLEEP. If the run exceeds this instruction count, then EMBRYO_PROGRAM_TOOLONG will be returned indicating the program exceeded its run count. If the app wishes to continue running this anyway &#8211; it is free to process its own events or whatever it wants and continue the function by calling embryo_program_run(program, EMBRYO_FUNCTION_CONT); which will start the run again until the instruction count is reached. This can keep being done to allow the calling program to still be able to control things outside the embryo function being called. If the maximum run cycle count is 0 then the program is allowed to run forever only returning when it is done. </p>
<p> It is important to note that abstract machine cycles are NOT the same as the host machine cpu cycles. They are not fixed in runtime per cycle, so this is more of a helper tool than a way to HARD-FORCE a script to only run for a specific period of time. If the cycle count is set to something low like 5000 or 1000, then every 1000 (or 5000) cycles control will be returned to the calling process where it can check a timer to see if a physical runtime limit has been elapsed and then abort runing further assuming a &#8216;runaway script&#8217; or keep continuing the script run. This limits resolution to only that many cycles which do not take a determined amount of time to execute, as this varies from cpu to cpu and also depends on how loaded the system is. Making the max cycle run too low will impact performance requiring the abstract machine to do setup and teardown cycles too often comapred to cycles actually executed. </p>
<p> Also note it does NOT include nested abstract machines. IF this abstract machine run calls embryo script that calls a native function that in turn calls more embryo script, then the 2nd (and so on) levels are not included in this run count. They can set their own max instruction count values separately. </p>
<p> The default max cycle run value is 0 in any program until set with this function.</p>
<h3>EAPI int embryo_program_recursion_get (Embryo_Program * ep)</h3>
<p>Returns the number of virtual machines are running for the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The number of virtual machines running.</dl>
<h3>EAPI Embryo_Cell embryo_program_return_value_get (Embryo_Program * ep)</h3>
<p>Retreives the return value of the last called function of the given program. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>An Embryo_Cell representing the return value of the function that was last called.</dl>
<h3>EAPI int embryo_program_run (Embryo_Program * ep, Embryo_Function fn)</h3>
<p>Runs the given function of the given Embryo program in the current virtual machine. </p>
<p> The parameter fn can be found using <code>embryo_program_function_find</code>. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>For Embryo to be able to run a function, it must have been declared public in the Small source code.</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ep</i> The given program.<br />
 <i>fn</i> The given function. Normally &#8216;main&#8217;, in which case the constant EMBRYO_FUNCTION_MAIN can be used.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>EMBRYO_PROGRAM_OK on success. EMBRYO_PROGRAM_SLEEP if the program is halted by the Small sleep call. EMBRYO_PROGRAM_FAIL if there is an error. EMBRYO_PROGRAM_TOOLONG if the program executes for longer than it is allowed to in abstract machine instruction count.</dl>
<p> References EMBRYO_CELL_NONE, embryo_data_address_get(), embryo_data_heap_push(), embryo_data_string_set(), EMBRYO_ERROR_BOUNDS, EMBRYO_ERROR_DIVIDE, EMBRYO_ERROR_HEAPLOW, EMBRYO_ERROR_INDEX, EMBRYO_ERROR_INIT, EMBRYO_ERROR_INVINSTR, EMBRYO_ERROR_MEMACCESS, EMBRYO_ERROR_SLEEP, EMBRYO_FUNCTION_CONT, EMBRYO_FUNCTION_MAIN, EMBRYO_PROGRAM_FAIL, EMBRYO_PROGRAM_OK, and EMBRYO_PROGRAM_SLEEP.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
