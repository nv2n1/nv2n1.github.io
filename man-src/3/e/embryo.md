---
title: "embryo(3)"
name: "embryo"
section: "3"
letter: "e"
url: "/docs/linux/man/3-embryo/"
description: "Embryo.h – Embryo virtual machine library."
---

<p>Embryo.h &#8211; Embryo virtual machine library. </p>
<h2>Synopsis</h2>
<h3>Defines</h3>
<p>#define <code>EMBRYO_FUNCTION_NONE</code> 0x7fffffff<br />
 <i>An invalid/non-existant function. </i><br />
 #define <code>EMBRYO_FUNCTION_MAIN</code> -1<br />
 <i>Start at program entry point. </i><br />
 #define <code>EMBRYO_FUNCTION_CONT</code> -2<br />
 <i>Continue from last address. </i><br />
 #define <code>EMBRYO_CELL_NONE</code> 0x7fffffff<br />
 <i>An invalid cell reference. </i><br />
 #define <code>EMBRYO_PROGRAM_OK</code> 1<br />
 <i>Program was run successfully. </i><br />
 #define <code>EMBRYO_PROGRAM_SLEEP</code> 2<br />
 <i>The program&#8217;s execution was interrupted by a Small </i>sleep command.<br />
 #define <code>EMBRYO_PROGRAM_FAIL</code> 0<br />
 <i>An error in the program caused it to fail. </i><br />
 #define <code>EMBRYO_FLOAT_TO_CELL</code>(f) ((Embryo_Float_Cell) f).c<br />
 <i>Float to Embryo_Cell. </i><br />
 #define <code>EMBRYO_CELL_TO_FLOAT</code>(c) ((Embryo_Float_Cell) c).f<br />
 <i>Embryo_Cell to float. </i></p>
<h3>Enumerations</h3>
<p>enum { , <code>EMBRYO_ERROR_ASSERT</code>, <code>EMBRYO_ERROR_STACKERR</code>, <code>EMBRYO_ERROR_BOUNDS</code>, <code>EMBRYO_ERROR_MEMACCESS</code>, <code>EMBRYO_ERROR_INVINSTR</code>, <code>EMBRYO_ERROR_STACKLOW</code>, <code>EMBRYO_ERROR_HEAPLOW</code>, <code>EMBRYO_ERROR_CALLBACK</code>, <code>EMBRYO_ERROR_NATIVE</code>, <code>EMBRYO_ERROR_DIVIDE</code>, <code>EMBRYO_ERROR_SLEEP</code>, <code>EMBRYO_ERROR_MEMORY</code> = 16, <code>EMBRYO_ERROR_FORMAT</code>, <code>EMBRYO_ERROR_VERSION</code>, <code>EMBRYO_ERROR_NOTFOUND</code>, <code>EMBRYO_ERROR_INDEX</code>, <code>EMBRYO_ERROR_DEBUG</code>, <code>EMBRYO_ERROR_INIT</code>, <code>EMBRYO_ERROR_USERDATA</code>, <code>EMBRYO_ERROR_INIT_JIT</code>, <code>EMBRYO_ERROR_PARAMS</code>, <code>EMBRYO_ERROR_DOMAIN</code> } </p>
<h3>Functions</h3>
<p>EAPI int <code>embryo_init</code> (void)<br />
 <i>Initialises the Embryo library. </i><br />
 EAPI int <code>embryo_shutdown</code> (void)<br />
 <i>Shuts down the Embryo library. </i><br />
 EAPI Embryo_Program * <code>embryo_program_new</code> (void *data, int size)<br />
 <i>Creates a new Embryo program, with bytecode data that can be freed. </i><br />
 EAPI Embryo_Program * <code>embryo_program_const_new</code> (void *data, int size)<br />
 <i>Creates a new Embryo program, with bytecode data that cannot be freed. </i><br />
 EAPI Embryo_Program * <code>embryo_program_load</code> (char *file)<br />
 <i>Creates a new Embryo program based on the bytecode data stored in the given file. </i><br />
 EAPI void <code>embryo_program_free</code> (Embryo_Program *ep)<br />
 <i>Frees the given Embryo program. </i><br />
 EAPI void <code>embryo_program_native_call_add</code> (Embryo_Program *ep, const char *name, Embryo_Cell(*func)(Embryo_Program *ep, Embryo_Cell *params))<br />
 <i>Adds a native program call to the given Embryo program. </i><br />
 EAPI void <code>embryo_program_vm_reset</code> (Embryo_Program *ep)<br />
 <i>Resets the current virtual machine session of the given program. </i><br />
 EAPI void <code>embryo_program_vm_push</code> (Embryo_Program *ep)<br />
 <i>Starts a new virtual machine session for the given program. </i><br />
 EAPI void <code>embryo_program_vm_pop</code> (Embryo_Program *ep)<br />
 <i>Frees the current virtual machine session associated with the given program. </i><br />
 EAPI void <code>embryo_swap_16</code> (unsigned short *v)<br />
 <i>Ensures that the given unsigned short integer is in the small endian format. </i><br />
 EAPI void <code>embryo_swap_32</code> (unsigned int *v)<br />
 <i>Ensures that the given unsigned integer is in the small endian format. </i><br />
 EAPI Embryo_Function <code>embryo_program_function_find</code> (Embryo_Program *ep, const char *name)<br />
 <i>Returns the function in the given program with the given name. </i><br />
 EAPI Embryo_Cell <code>embryo_program_variable_find</code> (Embryo_Program *ep, const char *name)<br />
 <i>Retrieves the location of the public variable in the given program with the given name. </i><br />
 EAPI int <code>embryo_program_variable_count_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the number of public variables in the given program. </i><br />
 EAPI Embryo_Cell <code>embryo_program_variable_get</code> (Embryo_Program *ep, int num)<br />
 <i>Retrieves the location of the public variable in the given program with the given identifier. </i><br />
 EAPI void <code>embryo_program_error_set</code> (Embryo_Program *ep, int error)<br />
 <i>Sets the error code for the given program to the given code. </i><br />
 EAPI int <code>embryo_program_error_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the current error code for the given program. </i><br />
 EAPI void <code>embryo_program_data_set</code> (Embryo_Program *ep, void *data)<br />
 <i>Sets the data associated to the given program. </i><br />
 EAPI void * <code>embryo_program_data_get</code> (Embryo_Program *ep)<br />
 <i>Retrieves the data associated to the given program. </i><br />
 EAPI const char * <code>embryo_error_string_get</code> (int error)<br />
 <i>Retrieves a string describing the given error code. </i><br />
 EAPI int <code>embryo_data_string_length_get</code> (Embryo_Program *ep, Embryo_Cell *str_cell)<br />
 <i>Retrieves the length of the string starting at the given cell. </i><br />
 EAPI void <code>embryo_data_string_get</code> (Embryo_Program *ep, Embryo_Cell *str_cell, char *dst)<br />
 <i>Copies the string starting at the given cell to the given buffer. </i><br />
 EAPI void <code>embryo_data_string_set</code> (Embryo_Program *ep, const char *src, Embryo_Cell *str_cell)<br />
 <i>Copies string in the given buffer into the virtual machine memory starting at the given cell. </i><br />
 EAPI Embryo_Cell * <code>embryo_data_address_get</code> (Embryo_Program *ep, Embryo_Cell addr)<br />
 <i>Retreives a pointer to the address in the virtual machine given by the given cell. </i><br />
 EAPI Embryo_Cell <code>embryo_data_heap_push</code> (Embryo_Program *ep, int cells)<br />
 <i>Increases the size of the heap of the given virtual machine by the given number of Embryo_Cells. </i><br />
 EAPI void <code>embryo_data_heap_pop</code> (Embryo_Program *ep, Embryo_Cell down_to)<br />
 <i>Decreases the size of the heap of the given virtual machine down to the given size. </i><br />
 EAPI int <code>embryo_program_recursion_get</code> (Embryo_Program *ep)<br />
 <i>Returns the number of virtual machines are running for the given program. </i><br />
 EAPI int <code>embryo_program_run</code> (Embryo_Program *ep, Embryo_Function func)<br />
 <i>Runs the given function of the given Embryo program in the current virtual machine. </i><br />
 EAPI Embryo_Cell <code>embryo_program_return_value_get</code> (Embryo_Program *ep)<br />
 <i>Retreives the return value of the last called function of the given program. </i><br />
 EAPI void <code>embryo_program_max_cycle_run_set</code> (Embryo_Program *ep, int max)<br />
 <i>Sets the maximum number of abstract machine cycles any given program run can execute before being put to sleep and returning. </i><br />
 EAPI int <code>embryo_program_max_cycle_run_get</code> (Embryo_Program *ep)<br />
 <i>Retreives the maximum number of abstract machine cycles a program is allowed to run. </i><br />
 EAPI int <code>embryo_parameter_cell_push</code> (Embryo_Program *ep, Embryo_Cell cell)<br />
 <i>Pushes an Embryo_Cell onto the function stack to use as a parameter for the next function that is called in the given program. </i><br />
 EAPI int <code>embryo_parameter_string_push</code> (Embryo_Program *ep, const char *str)<br />
 <i>Pushes a string onto the function stack to use as a parameter for the next function that is called in the given program. </i><br />
 EAPI int <code>embryo_parameter_cell_array_push</code> (Embryo_Program *ep, Embryo_Cell *cells, int num)<br />
 <i>Pushes an array of Embryo_Cells onto the function stack to be used as parameters for the next function that is called in the given program. </i></p>
<h2>Detailed Description</h2>
<p>Embryo virtual machine library. </p>
<p> This file includes the routines needed for Embryo library interaction. This is the <i>only</i> file you need to include.</p>
<h2>Define Documentation</h2>
<h3>#define EMBRYO_FUNCTION_CONT -2</h3>
<p>Continue from last address. </p>
<p> For use with <code>embryo_program_run</code>. </p>
<p> Referenced by embryo_program_run().</p>
<h3>#define EMBRYO_FUNCTION_MAIN -1</h3>
<p>Start at program entry point. </p>
<p> For use with <code>embryo_program_run</code>. </p>
<p> Referenced by embryo_program_run().</p>
<h2>Enumeration Type Documentation</h2>
<h3>anonymous enum</h3>
<p><code>Enumerator: </code></p>
<dl COMPACT>
<dt><i>EMBRYO_ERROR_ASSERT </i></p>
<dd>Forced exit.</p>
<dt><i>EMBRYO_ERROR_STACKERR </i></p>
<dd>Assertion failed.</p>
<dt><i>EMBRYO_ERROR_BOUNDS </i></p>
<dd>Stack/heap collision.</p>
<dt><i>EMBRYO_ERROR_MEMACCESS </i></p>
<dd>Index out of bounds.</p>
<dt><i>EMBRYO_ERROR_INVINSTR </i></p>
<dd>Invalid memory access.</p>
<dt><i>EMBRYO_ERROR_STACKLOW </i></p>
<dd>Invalid instruction.</p>
<dt><i>EMBRYO_ERROR_HEAPLOW </i></p>
<dd>Stack underflow.</p>
<dt><i>EMBRYO_ERROR_CALLBACK </i></p>
<dd>Heap underflow.</p>
<dt><i>EMBRYO_ERROR_NATIVE </i></p>
<dd>No callback, or invalid callback.</p>
<dt><i>EMBRYO_ERROR_DIVIDE </i></p>
<dd>Native function failed.</p>
<dt><i>EMBRYO_ERROR_SLEEP </i></p>
<dd>Divide by zero.</p>
<dt><i>EMBRYO_ERROR_MEMORY </i></p>
<dd>Go into sleepmode &#8211; code can be restarted.</p>
<dt><i>EMBRYO_ERROR_FORMAT </i></p>
<dd>Out of memory.</p>
<dt><i>EMBRYO_ERROR_VERSION </i></p>
<dd>Invalid file format.</p>
<dt><i>EMBRYO_ERROR_NOTFOUND </i></p>
<dd>File is for a newer version of the Embryo_Program.</p>
<dt><i>EMBRYO_ERROR_INDEX </i></p>
<dd>Function not found.</p>
<dt><i>EMBRYO_ERROR_DEBUG </i></p>
<dd>Invalid index parameter (bad entry point).</p>
<dt><i>EMBRYO_ERROR_INIT </i></p>
<dd>Debugger cannot run.</p>
<dt><i>EMBRYO_ERROR_USERDATA </i></p>
<dd>Embryo_Program not initialized (or doubly initialized).</p>
<dt><i>EMBRYO_ERROR_INIT_JIT </i></p>
<dd>Unable to set user data field (table full).</p>
<dt><i>EMBRYO_ERROR_PARAMS </i></p>
<dd>Cannot initialize the JIT.</p>
<dt><i>EMBRYO_ERROR_DOMAIN </i></p>
<dd>Parameter error.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Embryo from the source code.</p>
