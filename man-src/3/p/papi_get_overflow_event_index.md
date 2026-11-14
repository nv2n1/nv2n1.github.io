---
title: "papi_get_overflow_event_index(3)"
name: "papi_get_overflow_event_index"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_overflow_event_index/"
---

PAPI_get_overflow_event_index - 

 converts an overflow vector into an array of indexes to overflowing events
<h2>Synopsis</h2><h2>Detailed Description</h2><pre>@param EventSet
 an integer handle to a PAPI event set as created by PAPI_create_eventset
@param overflow_vector
 a vector with bits set for each counter that overflowed. 
 This vector is passed by the system to the overflow handler routine.
@param *array
 an array of indexes for events in EventSet. 
 No more than *number indexes will be stored into the array.
@param *number 
 On input the variable determines the size of the array. 
 On output the variable contains the number of indexes in the array. 
@retval PAPI_EINVAL 
 One or more of the arguments is invalid. This could occur if the overflow_vector is empty (zero), if the array or number pointers are NULL, if the value of number is less than one, or if the EventSet is empty.
@retval PAPI_ENOEVST
The EventSet specified does not exist.
@par Examples</pre>&nbsp;<wbr> 

 <pre> void handler(int EventSet, void *address, long_long overflow_vector, void *context){
 int Events[4], number, i;
 int total = 0, retval;
 printf(&quot;Overflow #%d Handler(%d) Overflow at %p! vector=0x%llx,
 total, EventSet, address, overflow_vector);
 total++;
 number = 4;
 retval = PAPI_get_overflow_event_index(EventSet,
 overflow_vector, Events, &amp;number);
 if(retval == PAPI_OK)
 for(i=0; i&lt;number; i++) printf(&quot;Event index[%d] = %d&quot;, i, Events[i]);}
* </pre>&nbsp;<wbr>&nbsp;<wbr> 

 <pre>@see PAPI_overflow</pre>&nbsp;<wbr> 

<h2>Author</h2>Generated automatically by Doxygen for PAPI from the source code.
