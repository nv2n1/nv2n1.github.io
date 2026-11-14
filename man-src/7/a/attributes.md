---
title: "attributes(7)"
name: "attributes"
section: "7"
letter: "a"
url: "/docs/linux/man/7-attributes/"
description: "attributes – POSIX safety concepts"
---

<p>attributes &#8211; POSIX safety concepts</p>
<h2>Description</h2>
<p><i>Note</i>: the text of this man page is based on the material taken from the &quot;POSIX Safety Concepts&quot; section of the GNU C Library manual. Further details on the topics described here can be found in that manual. </p>
<p> Various function manual pages include a section ATTRIBUTES that describes the safety of calling the function in various contexts. This section annotates functions with the following safety markings:</p>
<dl>
<dt><i>MT-Safe</i></p>
<dd><i>MT-Safe</i> or Thread-Safe functions are safe to call in the presence of other threads. MT, in MT-Safe, stands for Multi Thread.</p>
<dd>Being MT-Safe does not imply a function is atomic, nor that it uses any of the memory synchronization mechanisms POSIX exposes to users. It is even possible that calling MT-Safe functions in sequence does not yield an MT-Safe combination. For example, having a thread call two MT-Safe functions one right after the other does not guarantee behavior equivalent to atomic execution of a combination of both functions, since concurrent calls in other threads may interfere in a destructive way.</p>
<dd>Whole-program optimizations that could inline functions across library interfaces may expose unsafe reordering, and so performing inlining across the GNU C Library interface is not recommended. The documented MT-Safety status is not guaranteed under whole-program optimization. However, functions defined in user-visible headers are designed to be safe for inlining.</p>
<dt><i>MT-Unsafe</i></p>
<dd><i>MT-Unsafe</i> functions are not safe to call in a multithreaded programs.</dl>
<p> Other keywords that appear in safety notes are defined in subsequent sections.</p>
<h3>Conditionally safe features</h3>
<p>For some features that make functions unsafe to call in certain contexts, there are known ways to avoid the safety problem other than refraining from calling the function altogether. The keywords that follow refer to such features, and each of their definitions indicates how the whole program needs to be constrained in order to remove the safety problem indicated by the keyword. Only when all the reasons that make a function unsafe are observed and addressed, by applying the documented constraints, does the function become safe to call in a context.</p>
<dl>
<dt><i>init</i></p>
<dd>Functions marked with <i>init</i> as an MT-Unsafe feature perform MT-Unsafe initialization when they are first called.</p>
<dd>Calling such a function at least once in single-threaded mode removes this specific cause for the function to be regarded as MT-Unsafe. If no other cause for that remains, the function can then be safely called after other threads are started.</p>
<dt><i>race</i></p>
<dd>Functions annotated with <i>race</i> as an MT-Safety issue operate on objects in ways that may cause data races or similar forms of destructive interference out of concurrent execution. In some cases, the objects are passed to the functions by users; in others, they are used by the functions to return values to users; in others, they are not even exposed to users.</p>
<dt><i>const</i></p>
<dd>Functions marked with <i>const</i> as an MT-Safety issue non-atomically modify internal objects that are better regarded as constant, because a substantial portion of the GNU C Library accesses them without synchronization. Unlike <i>race</i>, which causes both readers and writers of internal objects to be regarded as MT-Unsafe,this mark is applied to writers only. Writers remainMT-Unsafeto call, but the then-mandatory constness of objects they modify enables readers to be regarded as MT-Safe(as long as no other reasons for them to be unsafe remain), since the lack of synchronization is not a problem when the objects are effectively constant.</p>
<dd>The identifier that follows the <i>const</i> mark will appear by itself as a safety note in readers. Programs that wish to work around this safety issue, so as to call writers, may use a non-recursive read-write lock associated with the identifier, and guard <i>all</i> calls to functions marked with <i>const</i> followed by the identifier with a write lock, and <i>all</i> calls to functions marked with the identifier by itself with a read lock.</p>
<dt><i>sig</i></p>
<dd>Functions marked with <i>sig</i> as a MT-Safety issue may temporarily install a signal handler for internal purposes, which may interfere with other uses of the signal, identified after a colon.</p>
<dd>This safety problem can be worked around by ensuring that no other uses of the signal will take place for the duration of the call. Holding a non-recursive mutex while calling all functions that use the same temporary signal; blocking that signal before the call and resetting its handler afterwards is recommended.</p>
<dt><i>term</i></p>
<dd>Functions marked with <i>term</i> as an MT-Safety issue may change the terminal settings in the recommended way, namely: call <code><a href="/docs/linux/man/3-tcgetattr/">tcgetattr</a></code>(3), modify some flags, and then call <code><a href="/docs/linux/man/3-tcsetattr/">tcsetattr</a></code>(3), this creates a window in which changes made by other threads are lost. Thus, functions marked with <i>term</i> are MT-Unsafe.</p>
<dd>It is thus advisable for applications using the terminal to avoid concurrent and reentrant interactions with it, by not using it in signal handlers or blocking signals that might use it, and holding a lock while calling these functions and interacting with the terminal. This lock should also be used for mutual exclusion with functions marked with <i>race:tcattr(fd)</i>, where <i>fd</i> is a file descriptor for the controlling terminal. The caller may use a single mutex for simplicity, or use one mutex per terminal, even if referenced by different file descriptors.</dl>
<h3>Other safety remarks</h3>
<p>Additional keywords may be attached to functions, indicating features that do not make a function unsafe to call, but that may need to be taken into account in certain classes of programs:</p>
<dl>
<dt><i>locale</i></p>
<dd>Functions annotated with <i>locale</i> as an MT-Safety issue read from the locale object without any form of synchronization. Functions annotated with <i>locale</i> called concurrently with locale changes may behave in ways that do not correspond to any of the locales active during their execution, but an unpredictable mix thereof.</p>
<dd>We do not mark these functions as MT-Unsafe,however, because functions that modify the locale object are marked with <i>const:locale</i> and regarded as unsafe. Being unsafe, the latter are not to be called when multiple threads are running or asynchronous signals are enabled, and so the locale can be considered effectively constant in these contexts, which makes the former safe.</p>
<dt><i>env</i></p>
<dd>Functions marked with <i>env</i> as an MT-Safety issue access the environment with <code><a href="/docs/linux/man/3-getenv/">getenv</a></code>(3) or similar, without any guards to ensure safety in the presence of concurrent modifications.</p>
<dd>We do not mark these functions as MT-Unsafe,however, because functions that modify the environment are all marked with <i>const:env</i> and regarded as unsafe. Being unsafe, the latter are not to be called when multiple threads are running or asynchronous signals are enabled, and so the environment can be considered effectively constant in these contexts, which makes the former safe.</p>
<dt><i>hostid</i></p>
<dd>The function marked with <i>hostid</i> as an MT-Safety issue reads from the system-wide data structures that hold the &quot;host ID&quot; of the machine. These data structures cannot generally be modified atomically. Since it is expected that the &quot;host ID&quot; will not normally change, the function that reads from it (<code><a href="/docs/linux/man/3-gethostid/">gethostid</a></code>(3)) is regarded as safe, whereas the function that modifies it (<code><a href="/docs/linux/man/3-sethostid/">sethostid</a></code>(3)) is marked with <i>const:hostid</i>, indicating it may require special care if it is to be called. In this specific case, the special care amounts to system-wide (not merely intra-process) coordination.</p>
<dt><i>sigintr</i></p>
<dd>Functions marked with <i>sigintr</i> as an MT-Safety issue access the GNU C Library <i>_sigintr</i> internal data structure without any guards to ensure safety in the presence of concurrent modifications.</p>
<dd>We do not mark these functions as MT-Unsafe,however, because functions that modify this data structure are all marked with <i>const:sigintr</i> and regarded as unsafe. Being unsafe, the latter are not to be called when multiple threads are running or asynchronous signals are enabled, and so the data structure can be considered effectively constant in these contexts, which makes the former safe.</p>
<dt><i>cwd</i></p>
<dd>Functions marked with <i>cwd</i> as an MT-Safety issue may temporarily change the current working directory during their execution, which may cause relative pathnames to be resolved in unexpected ways in other threads or within asynchronous signal or cancellation handlers.</p>
<dd>This is not enough of a reason to mark so-marked functions as MT-Unsafe, but when this behavior is optional (e.g., <code><a href="/docs/linux/man/3-nftw/">nftw</a></code>(3) with <code>FTW_CHDIR</code>), avoiding the option may be a good alternative to using full pathnames or file descriptor-relative (e.g., <code><a href="/docs/linux/man/2-openat/">openat</a></code>(2)) system calls.</p>
<dt><i>:identifier</i></p>
<dd>Annotations may sometimes be followed by identifiers, intended to group several functions that, for example, access the data structures in an unsafe way, as in <i>race</i> and <i>const</i>, or to provide more specific information, such as naming a signal in a function marked with <i>sig</i>. It is envisioned that it may be applied to <i>lock</i> and <i>corrupt</i> as well in the future.</p>
<dd>In most cases, the identifier will name a set of functions, but it may name global objects or function arguments, or identifiable properties or logical components associated with them, with a notation such as, for example, <i>:buf(arg)</i> to denote a buffer associated with the argument <i>arg</i>, or <i>:tcattr(fd)</i> to denote the terminal attributes of a file descriptor <i>fd</i>.</p>
<dd>The most common use for identifiers is to provide logical groups of functions and arguments that need to be protected by the same synchronization primitive in order to ensure safe operation in a given context.</p>
<dt><i>/condition</i></p>
<dd>Some safety annotations may be conditional, in that they only apply if a boolean expression involving arguments, global variables or even the underlying kernel evaluates to true. For example, <i>/!ps</i> and <i>/one_per_line</i> indicate the preceding marker only applies when argument <i>ps</i> is NULL, or global variable <i>one_per_line</i> is nonzero.</p>
<dd>When all marks that render a function unsafe are adorned with such conditions, and none of the named conditions hold, then the function can be regarded as safe.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/7-pthreads/">pthreads</a></code>(7), <code><a href="/docs/linux/man/7-signal-safety/">signal-safety</a></code>(7)</p>
<h2>Colophon</h2>
<p>This page is part of release 5.10 of the Linux <i>man-pages</i> project. A description of the project, information about reporting bugs, and the latest version of this page, can be found at <a rel="nofollow" href="https://www.kernel.org/doc/man-pages/.">https://www.kernel.org/doc/man-pages/.</a> </p>
