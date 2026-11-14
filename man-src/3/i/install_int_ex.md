---
title: "install_int_ex(3)"
name: "install_int_ex"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_int_ex/"
description: "install_int_ex – Adds or modifies a timer. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_int_ex &#8211; Adds or modifies a timer. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_int_ex(void (*proc)(), int speed);</code></p>
<h2>DESCRIPTION</h2>
<p> Adds a function to the list of user timer handlers or, if it is already installed, retroactively adjusts its speed (i.e makes as though the speed change occurred precisely at the last tick). The speed is given in hardware clock ticks, of which there are 1193181 a second. You can convert from other time formats to hardware clock ticks with the macros: </p>
<pre>
   SECS_TO_TIMER(secs)  - give the number of seconds between
                          each tick
   MSEC_TO_TIMER(msec)  - give the number of milliseconds
                          between ticks
   BPS_TO_TIMER(bps)    - give the number of ticks each second
   BPM_TO_TIMER(bpm)    - give the number of ticks per minute
   
</pre>
<p> There can only be sixteen timers in use at a time, and some other parts of Allegro (the GUI code, the mouse pointer display routines, rest(), the FLI player, and the MIDI player) need to install handlers of their own, so you should avoid using too many at the same time. If you call this routine without having first installed the timer module, install_timer() will be called automatically. </p>
<p> Your function will be called by the Allegro interrupt handler and not directly by the processor, so it can be a normal C function and does not need a special wrapper. You should be aware, however, that it will be called in an interrupt context, which imposes a lot of restrictions on what you can do in it. It should not use large amounts of stack, it must not make any calls to the operating system, use C library functions, or contain any floating point code, and it must execute very quickly. Don&#8217;t try to do lots of complicated code in a timer handler: as a general rule you should just set some flags and respond to these later in your main control loop. </p>
<p> In a DOS protected mode environment like DJGPP, memory is virtualised and can be swapped to disk. Due to the non-reentrancy of DOS, if a disk swap occurs inside an interrupt handler the system will die a painful death, so you need to make sure you lock all the memory (both code and data) that is touched inside timer routines. Allegro will lock everything it uses, but you are responsible for locking your handler functions. The macros LOCK_VARIABLE (variable), END_OF_FUNCTION (function_name), END_OF_STATIC_FUNCTION (function_name), and LOCK_FUNCTION (function_name) can be used to simplify this task. For example, if you want an interrupt handler that increments a counter variable, you should write: </p>
<pre><code>
volatile int counter;

void my_timer_handler()
{
    counter++;
}

END_OF_FUNCTION(my_timer_handler)
</code></pre>
<p> and in your initialisation code you should lock the memory: </p>
<pre><code>
LOCK_VARIABLE(counter);
LOCK_FUNCTION(my_timer_handler);
</code></pre>
<p> Obviously this can get awkward if you use complicated data structures and call other functions from within your handler, so you should try to keep your interrupt routines as simple as possible.</p>
<h2>RETURN VALUE</h2>
<p> Returns zero on success, or a negative number if there is no room to add a new user timer. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_timer/">install_timer</a></code>(3), <code><a href="/docs/linux/man/3-remove_int/">remove_int</a></code>(3), <code><a href="/docs/linux/man/3-install_int/">install_int</a></code>(3), <code><a href="/docs/linux/man/3-install_param_int_ex/">install_param_int_ex</a></code>(3), <code><a href="/docs/linux/man/3-excamera/">excamera</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-extimer/">extimer</a></code>(3), <code><a href="/docs/linux/man/3-exunicod/">exunicod</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
