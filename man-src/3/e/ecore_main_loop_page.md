---
title: "ecore_main_loop_page(3)"
name: "ecore_main_loop_page"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_main_loop_page/"
description: "Ecore_Main_Loop_Page – The Ecore Main Loop"
---

<p>Ecore_Main_Loop_Page &#8211; The Ecore Main Loop </p>
<h2>What is Ecore?</h2>
<p>Ecore is a clean and tiny event loop library with many modules to do lots of convenient things for a programmer, to save time and effort. </p>
<p> It&#8217;s small and lean, designed to work on embedded systems all the way to large and powerful multi-cpu workstations. It serialises all system signals, events etc. into a single event queue, that is easily processed without needing to worry about concurrency. A properly written, event-driven program using this kind of programming doesn&#8217;t need threads, nor has to worry about concurrency. It turns a program into a state machine, and makes it very robust and easy to follow. </p>
<p> Ecore gives you other handy primitives, such as timers to tick over for you and call specified functions at particular times so the programmer can use this to do things, like animate, or time out on connections or tasks that take too long etc. </p>
<p> Idle handlers are provided too, as well as calls on entering an idle state (often a very good time to update the state of the program). All events that enter the system are passed to specific callback functions that the program sets up to handle those events. Handling them is simple and other Ecore modules produce more events on the queue, coming from other sources such as file descriptors etc. </p>
<p> Ecore also lets you have functions called when file descriptors become active for reading or writing, allowing for streamlined, non-blocking IO. </p>
<p> Here is an exmaple of a simple program and its basic event loop flow: </p>
<h2>How does Ecore work?</h2>
<p>Ecore is very easy to learn and use. All the function calls are designed to be easy to remember, explicit in describing what they do, and heavily name-spaced. Ecore programs can start and be very simple. </p>
<p> For example: </p>
<pre>#include &lt;<a href="file:/usr/include/Ecore.h">Ecore.h</a>&gt;
int main(int argc, const char **argv)
{
 ecore_init();
 ecore_app_args_set(argc, argv);
 ecore_main_loop_begin();
 ecore_shutdown();
 return 0;
}</pre>
<p>This program is very simple and does&#8217;t check for errors, but it does start up and begin a main loop waiting for events or timers to tick off. This program doesn&#8217;t set up any, but now we can expand on this simple program a little more by adding some event handlers and timers. </p>
<pre>#include &lt;<a href="file:/usr/include/Ecore.h">Ecore.h</a>&gt;
Ecore_Timer *timer1 = NULL;
Ecore_Event_Handler *handler1 = NULL;
double start_time = 0.0;
int timer_func(void *data)
{
 printf('Tick timer. Sec: %3.2f, ecore_time_get() - start_time);
 return 1;
}
int exit_func(void *data, int ev_type, void *ev)
{
 Ecore_Event_Signal_Exit *e;
 e = (Ecore_Event_Signal_Exit *)ev;
 if (e-&gt;interrupt) printf('Exit: interrupt);
 else if (e-&gt;quit) printf('Exit: quit);
 else if (e-&gt;terminate) printf('Exit: terminate);
 ecore_main_loop_quit();
 return 1;
}
int main(int argc, const char **argv)
{
 ecore_init();
 ecore_app_args_set(argc, argv); 
 start_time = ecore_time_get();
 handler1 = ecore_event_handler_add(ECORE_EVENT_SIGNAL_EXIT, exit_func, NULL);
 timer1 = ecore_timer_add(0.5, timer_func, NULL); 
 ecore_main_loop_begin();
 ecore_shutdown();
 return 0;
}</pre>
<p>In the previous example, we initialize our application and get the time at which our program has started so we can calculate an offset. We set up a timer to tick off in 0.5 seconds, and since it returns 1, will keep ticking off every 0.5 seconds until it returns 0, or is deleted by hand. An event handler is set up to call a function &#8211; exit_func(), whenever an event of type ECORE_EVENT_SIGNAL_EXIT is received (CTRL-C on the command line will cause such an event to happen). If this event occurs it tells you what kind of exit signal was received, and asks the main loop to quit when it is finished by calling <code>ecore_main_loop_quit()</code>. </p>
<p> The handles returned by <code>ecore_timer_add()</code> and <code>ecore_event_handler_add()</code> are only stored here as an example. If you don&#8217;t need to address the timer or event handler again you don&#8217;t need to store the result, so just call the function, and don&#8217;t assign the result to any variable. </p>
<p> This program looks slightly more complex than needed to do these simple things, but in principle, programs don&#8217;t get any more complex. You add more event handlers, for more events, will have more timers and such, BUT it all follows the same principles as shown in this example.</p>
